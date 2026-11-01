/* Append-only, per-field revision ledger. No network or external dependencies. */
(function (root, factory) {
  'use strict';
  const Ledger = factory();
  if (typeof module === 'object' && module.exports) module.exports = Ledger;
  if (root) root.RevisionLedger = Ledger;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const FORMAT = 'thesis-revision-ledger';
  const SCHEMA = 1;
  const STORAGE_FORMAT = 'thesis-revision-storage-v1';
  const OPERATION_VALUE_LIMIT = 8 * 1024 * 1024;
  const BACKUP_LIMIT = 64 * 1024 * 1024;
  const clone = value => value === null || typeof value !== 'object' ? value : JSON.parse(JSON.stringify(value));
  const sorted = value => Array.isArray(value) ? value.map(sorted) : value && typeof value === 'object' ? Object.fromEntries(Object.keys(value).sort().map(k => [k, sorted(value[k])])) : value;
  const equal = (a, b) => JSON.stringify(sorted(a)) === JSON.stringify(sorted(b));
  const errorText = e => String(e && e.message || e);
  function uuid() {
    if (typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function') return crypto.randomUUID();
    return Date.now().toString(36) + '-' + Math.random().toString(36).slice(2) + '-' + Math.random().toString(36).slice(2);
  }
  function assert(condition, message) { if (!condition) throw new Error(message); }
  function validateName(value, label, max) {
    assert(typeof value === 'string' && value.length > 0 && value.length <= max && !/[\u0000-\u001f]/.test(value), 'Invalid ' + label);
  }
  function validateValue(value, limit) {
    assert(value !== undefined, 'Undefined values are not supported; use null or an empty string');
    function check(item) {
      if (item === null || typeof item === 'string' || typeof item === 'boolean') return;
      if (typeof item === 'number') { assert(Number.isFinite(item), 'Numbers must be finite'); return; }
      assert(typeof item === 'object' && (Array.isArray(item) || Object.getPrototypeOf(item) === Object.prototype || Object.getPrototypeOf(item) === null), 'Value must contain only JSON data');
      for (const child of Object.values(item)) check(child);
    }
    check(value);
    const raw = JSON.stringify(value);
    assert(typeof raw === 'string' && raw.length <= (limit || OPERATION_VALUE_LIMIT), 'Value is not valid JSON or is too large');
    assert(equal(value, JSON.parse(raw)), 'Value must contain only JSON data');
  }
  function validateOperation(op, docId) {
    assert(op && typeof op === 'object' && !Array.isArray(op), 'Invalid operation');
    validateName(op.id, 'operation ID', 300);
    assert(op.documentId === docId, 'Operation belongs to another document');
    validateName(op.recordId, 'record ID', 300);
    validateName(op.field, 'field name', 300);
    assert(Array.isArray(op.parents) && op.parents.length <= 10000 && op.parents.every(p => typeof p === 'string' && p.length > 0 && p.length <= 300), 'Invalid operation parents');
    assert(new Set(op.parents).size === op.parents.length && !op.parents.includes(op.id), 'Invalid duplicate or self parent');
    assert(typeof op.timestamp === 'string' && Number.isFinite(Date.parse(op.timestamp)), 'Invalid operation timestamp');
    validateName(op.actor, 'actor', 300);
    if (op.candidateVersion !== undefined && op.candidateVersion !== null) validateName(op.candidateVersion, 'candidate version', 1000);
    validateValue(op.value);
    return op;
  }
  function validateGraph(ops, requireParents) {
    for (const op of ops.values()) {
      for (const parentId of op.parents) {
        const parent = ops.get(parentId);
        if (!parent) { assert(!requireParents, 'Missing parent operation: ' + parentId); continue; }
        assert(parent.recordId === op.recordId && parent.field === op.field, 'Parent refers to a different field');
      }
    }
    const visited = new Set(), active = new Set();
    function visit(id) {
      if (visited.has(id) || !ops.has(id)) return;
      assert(!active.has(id), 'Operation graph contains a cycle');
      active.add(id);
      for (const parentId of ops.get(id).parents) visit(parentId);
      active.delete(id); visited.add(id);
    }
    for (const id of ops.keys()) visit(id);
  }
  class RevisionLedger {
    constructor(options) {
      options = options || {};
      this.docId = options.docId || 'zhanh-he-phd-thesis-review';
      validateName(this.docId, 'document ID', 300);
      this.namespace = 'revision-ledger:' + encodeURIComponent(this.docId) + ':';
      this.prefix = this.namespace + 'op:';
      this.metaPrefix = this.namespace + 'meta:';
      this.actor = options.actor || uuid();
      this.onChange = typeof options.onChange === 'function' ? options.onChange : function () {};
      this.onWarning = typeof options.onWarning === 'function' ? options.onWarning : function () {};
      this.knownIds = options.knownIds ? new Set(options.knownIds) : null;
      this.validateField = typeof options.validateField === 'function' ? options.validateField : null;
      this.ops = new Map();
      this.fieldIndex = new Map();
      this.rawCache = new Map();
      this.storageDepth = new Map();
      this.persisted = new Set();
      this.quarantine = new Map();
      this.warnings = new Map();
      this.importMetadata = new Map();
      this.metadataRawCache = new Map();
      this.persistedMetadata = new Set();
      this.lastSavedAt = null;
      this.storage = null;
      this.storageReadable = false;
      this.storageWritable = false;
      try {
        this.storage = Object.prototype.hasOwnProperty.call(options, 'storage') ? options.storage : typeof localStorage !== 'undefined' ? localStorage : null;
        if (!this.storage) throw new Error('Browser storage is unavailable');
        void this.storage.length;
        this.storageReadable = true;
        this.storageWritable = true; // Writes are checked synchronously for every operation.
      } catch (e) { this._warn('storage-unavailable', '浏览器保存不可用；当前修改仅在本页内存。请立即导出 JSON 备份。 ' + errorText(e)); }
      this.refresh(false);
      this._storageListener = event => {
        if (!event || event.key === null || String(event.key).startsWith(this.namespace)) this.refresh();
      };
      if (typeof addEventListener === 'function') addEventListener('storage', this._storageListener);
    }
    _warn(code, message) {
      if (this.warnings.get(code) === message) return;
      this.warnings.set(code, message);
      try { this.onWarning({code, message}); } catch (_) { /* UI callbacks cannot break saving. */ }
    }
    _notify(reason) { try { this.onChange({reason, status: this.status()}); } catch (_) { /* Caller can re-render later. */ } }
    status() {
      return {documentId: this.docId, mode: this.storageWritable ? 'browser' : 'memory', storageReadable: this.storageReadable, storageWritable: this.storageWritable,
        operationCount: this.ops.size, metadataCount: this.importMetadata.size,
        unsavedOperations: this.ops.size - this.persisted.size + this.importMetadata.size - this.persistedMetadata.size,
        quarantinedCount: this.quarantine.size, lastSavedAt: this.lastSavedAt, warnings: [...this.warnings].map(([code, message]) => ({code, message}))};
    }
    refresh(notify) {
      let changed = false;
      let operationsChanged = false;
      if (this.storage && this.storageReadable) {
        try {
          // Capture keys before reading; another tab can append but cannot invalidate old operations.
          const keys = [], payloads = new Map(), resolving = new Set(), decoded = new Map();
          const metadataKeys = [], validPersisted = new Set(), validMetadata = new Set();
          for (let i = 0; i < this.storage.length; i++) {
            const key = this.storage.key(i);
            if (key && key.startsWith(this.prefix)) keys.push(key);
            if (key && key.startsWith(this.metaPrefix)) metadataKeys.push(key);
          }
          for (const key of metadataKeys) {
            let raw = null;
            const id = key.slice(this.metaPrefix.length);
            try {
              raw = this.storage.getItem(key); if (raw === null) continue;
              // Metadata is immutable too. Full workbench context can be MiBs;
              // unchanged bytes must not be parsed/validated on every keystroke.
              if (this.importMetadata.has(id) && this.metadataRawCache.get(id) === raw) {
                validMetadata.add(id); this.quarantine.delete(key); continue;
              }
              const meta = this._validateMetadata(JSON.parse(raw));
              assert(key === this.metaPrefix + meta.id, 'Metadata storage key does not match ID');
              if (this.importMetadata.has(meta.id)) assert(equal(this.importMetadata.get(meta.id), meta), 'Metadata ID collision');
              else { this.importMetadata.set(meta.id, clone(meta)); changed = true; }
              validMetadata.add(meta.id); this.metadataRawCache.set(meta.id, raw); this.quarantine.delete(key);
            } catch (e) {
              this.quarantine.set(key, {key, raw, error: errorText(e)});
              this._warn('corrupt-storage', '发现损坏的浏览器记录，已保留原始数据且未覆盖。请导出 JSON，查看恢复数据后再处理。');
            }
          }
          for (const key of keys) payloads.set(key.slice(this.prefix.length), this.storage.getItem(key));
          const decode = id => {
            if (decoded.has(id)) return decoded.get(id);
            if (resolving.has(id)) throw new Error('Storage delta contains a cycle');
            const raw = payloads.get(id);
            if (raw === undefined || raw === null) {
              assert(this.ops.has(id), 'Missing string-delta base: ' + id);
              return this.ops.get(id);
            }
            if (this.rawCache.get(id) === raw && this.ops.has(id)) return this.ops.get(id);
            resolving.add(id);
            const parsed = JSON.parse(raw);
            let op = parsed;
            // Raw v1 operations may legitimately carry arbitrary future fields
            // named encoding/storageFormat/operation. Recognize them FIRST.
            const rawOperation = parsed && ['id', 'documentId', 'recordId', 'field', 'value'].every(name => Object.prototype.hasOwnProperty.call(parsed, name));
            const envelope = !rawOperation && parsed && parsed.storageFormat === STORAGE_FORMAT;
            const legacyDelta = !rawOperation && parsed && parsed.encoding === 'string-splice-v1' && parsed.operation && parsed.delta;
            if (envelope) {
              assert(parsed.kind === 'operation' || parsed.kind === 'string-splice', 'Unknown operation storage envelope');
              op = parsed.operation;
            }
            if ((envelope && parsed.kind === 'string-splice') || legacyDelta) {
              const d = parsed.delta, deltaOperation = parsed.operation;
              assert(deltaOperation && d && typeof d.baseId === 'string' && Number.isInteger(d.start) && d.start >= 0 && Number.isInteger(d.remove) && d.remove >= 0 && typeof d.insert === 'string', 'Invalid string delta');
              assert(Array.isArray(deltaOperation.parents) && deltaOperation.parents.includes(d.baseId), 'String delta base is not an operation parent');
              const base = decode(d.baseId);
              assert(typeof base.value === 'string' && d.start + d.remove <= base.value.length, 'Invalid string delta range');
              op = Object.assign({}, deltaOperation, {value: base.value.slice(0, d.start) + d.insert + base.value.slice(d.start + d.remove)});
              this.storageDepth.set(id, (this.storageDepth.get(d.baseId) || 0) + 1);
              assert(this.storageDepth.get(id) <= 64, 'String delta chain is too deep');
            } else this.storageDepth.set(id, 0);
            validateOperation(op, this.docId);
            if (this.validateField) assert(this.validateField(op.recordId, op.field, clone(op.value)) !== false, 'Field value rejected by workbench validation');
            assert(op.id === id, 'Storage key does not match operation ID');
            resolving.delete(id);
            decoded.set(id, op);
            return op;
          };
          for (const key of keys) {
            let raw = null;
            try {
              raw = payloads.get(key.slice(this.prefix.length));
              if (raw === null) continue;
              resolving.clear();
              const op = decode(key.slice(this.prefix.length));
              if (this.ops.has(op.id)) assert(this.ops.get(op.id) === op || equal(this.ops.get(op.id), op), 'Conflicting payload for an existing operation ID');
              else { this._addOperation(clone(op)); changed = true; operationsChanged = true; }
              validPersisted.add(op.id);
              this.rawCache.set(op.id, raw);
              this.quarantine.delete(key);
              if (!this.lastSavedAt || op.timestamp > this.lastSavedAt) this.lastSavedAt = op.timestamp;
            } catch (e) {
              this.quarantine.set(key, {key, raw, error: errorText(e)});
              this._warn('corrupt-storage', '发现损坏的浏览器记录，已保留原始数据且未覆盖。请导出 JSON，查看恢复数据后再处理。');
            }
          }
          // Persisted flags describe the CURRENT browser keys, not historical
          // successful writes. Memory operations remain intact after deletion.
          this.persisted = validPersisted; this.persistedMetadata = validMetadata;
          if (this.status().unsavedOperations > 0) this._warn('storage-record-missing', '浏览器中有记录缺失或损坏；原文仍在本页内存。请导出 JSON，并点击重试保存以恢复。');
          else this.warnings.delete('storage-record-missing');
          if (operationsChanged) {
            try { validateGraph(this.ops, true); } catch (e) { this._warn('invalid-graph', '记录关系异常；原始操作已保留。 ' + errorText(e)); }
          }
        } catch (e) {
          this.storageReadable = false; this.storageWritable = false;
          this._warn('storage-read-failed', '无法读取浏览器保存；本页记录仍在内存。请立即导出 JSON。 ' + errorText(e));
        }
      }
      if (changed && notify !== false) this._notify('refresh');
      return this.status();
    }
    _fieldEntry(recordId, field) {
      const key = JSON.stringify([recordId, field]);
      let entry = this.fieldIndex.get(key);
      if (!entry) {
        entry = {operations: new Map(), ordered: null, state: null};
        this.fieldIndex.set(key, entry);
      }
      return entry;
    }
    _addOperation(op) {
      if (this.ops.has(op.id)) return;
      this.ops.set(op.id, op);
      const entry = this._fieldEntry(op.recordId, op.field);
      entry.operations.set(op.id, op); entry.ordered = null; entry.state = null;
    }
    _fieldOps(recordId, field) {
      const entry = this._fieldEntry(recordId, field);
      if (entry.ordered === null) entry.ordered = [...entry.operations.values()].sort((a, b) => a.timestamp.localeCompare(b.timestamp) || a.id.localeCompare(b.id));
      return entry.ordered;
    }
    _fieldState(recordId, field) {
      const entry = this._fieldEntry(recordId, field);
      if (entry.state !== null) return entry.state;
      const operations = this._fieldOps(recordId, field), suppressed = new Set();
      for (const op of operations) for (const parent of op.parents) suppressed.add(parent);
      let active = operations.filter(op => !suppressed.has(op.id));
      // Corrupt cyclic storage must never make a filled field look blank. Surface
      // unreachable operations as explicit recovery alternatives instead.
      const byId = new Map(operations.map(op => [op.id, op])), reachable = new Set(), stack = active.map(op => op.id);
      while (stack.length) {
        const id = stack.pop();
        if (reachable.has(id) || !byId.has(id)) continue;
        reachable.add(id); stack.push(...byId.get(id).parents);
      }
      const unreachable = operations.filter(op => !reachable.has(op.id));
      if (unreachable.length) active = active.concat(unreachable);
      const one = active.length === 1 ? active[0] : null;
      entry.state = {active, one, corruptGraph: unreachable.length > 0};
      return entry.state;
    }
    get(recordId, field, expectedCandidateVersion) {
      const {active, one, corruptGraph} = this._fieldState(recordId, field);
      return {value: one ? clone(one.value) : undefined, heads: active.map(op => op.id), conflict: active.length > 1, corruptGraph,
        conflicts: active.length > 1 ? clone(active) : [], alternatives: clone(active), candidateVersion: one ? one.candidateVersion || null : null,
        stale: expectedCandidateVersion !== undefined && active.some(op => (op.candidateVersion || null) !== expectedCandidateVersion),
        updatedAt: active.length ? active[active.length - 1].timestamp : null};
    }
    set(recordId, field, value, options) {
      options = options || {};
      validateName(recordId, 'record ID', 300); validateName(field, 'field name', 300); validateValue(value);
      if (this.validateField) assert(this.validateField(recordId, field, clone(value)) !== false, 'Field value rejected by workbench validation');
      // Capture observed heads BEFORE refresh. A stale caller must not unknowingly acknowledge an unseen edit.
      const parents = options.baseHeads === undefined ? this.get(recordId, field).heads : options.baseHeads.slice();
      this.refresh(false);
      const op = {id: this.actor + ':' + uuid(), documentId: this.docId, recordId, field, value: clone(value), parents,
        actor: this.actor, timestamp: new Date().toISOString(), candidateVersion: options.candidateVersion === undefined ? null : options.candidateVersion};
      if (options.reason) op.reason = String(options.reason);
      validateOperation(op, this.docId);
      for (const parentId of op.parents) {
        const parent = this.ops.get(parentId);
        assert(parent && parent.recordId === recordId && parent.field === field, 'Edit base is missing or refers to another field');
      }
      this._addOperation(op);
      this._persist(op);
      this._notify('set');
      return Object.assign(this.get(recordId, field, options.candidateVersion), {writeHead: op.id, operationId: op.id});
    }
    _persist(op, repair) {
      if (!this.storage || !this.storageWritable) return false;
      const key = this.prefix + op.id;
      try {
        const existing = this.storage.getItem(key);
        // Immutable IDs are written once. A retry never replaces an existing payload.
        if (existing !== null) {
          this.refresh(false);
          if (this.persisted.has(op.id) && equal(this.ops.get(op.id), op)) return true;
          assert(repair === true, 'Storage operation ID collision');
          if (!this._preserveCorruptStorage(key, existing)) return false;
          assert(this.storage.getItem(key) === existing, 'Storage changed during recovery; retry again');
        }
        let encoded = JSON.stringify({storageFormat: STORAGE_FORMAT, kind: 'operation', operation: op});
        const parent = op.parents.length === 1 ? this.ops.get(op.parents[0]) : null;
        let depth = 0;
        if (parent && this.persisted.has(parent.id) && (this.storageDepth.get(parent.id) || 0) < 32 && typeof parent.value === 'string' && typeof op.value === 'string') {
          let start = 0, suffix = 0;
          while (start < parent.value.length && start < op.value.length && parent.value[start] === op.value[start]) start++;
          while (suffix < parent.value.length - start && suffix < op.value.length - start && parent.value[parent.value.length - 1 - suffix] === op.value[op.value.length - 1 - suffix]) suffix++;
          const operation = Object.assign({}, op); delete operation.value;
          const compressed = JSON.stringify({storageFormat: STORAGE_FORMAT, kind: 'string-splice', operation, delta: {baseId: parent.id, start,
            remove: parent.value.length - start - suffix, insert: op.value.slice(start, op.value.length - suffix)}});
          if (compressed.length < encoded.length) { encoded = compressed; depth = (this.storageDepth.get(parent.id) || 0) + 1; }
        }
        this.storage.setItem(key, encoded);
        assert(this.storage.getItem(key) === encoded, 'Browser did not retain the saved operation');
        this.persisted.add(op.id);
        this.rawCache.set(op.id, encoded);
        this.storageDepth.set(op.id, depth);
        this.quarantine.delete(key);
        this.lastSavedAt = new Date().toISOString();
        return true;
      } catch (e) {
        this.storageWritable = false;
        this._warn('storage-write-failed', '浏览器保存失败（可能已满或被禁用）；修改保留在本页内存。请立即导出 JSON。 ' + errorText(e));
        return false;
      }
    }
    retrySave() {
      if (!this.storage) return this.status();
      this.storageReadable = true; this.storageWritable = true;
      this.refresh(false);
      for (const op of this.ops.values()) if (!this.persisted.has(op.id)) this._persist(op, true);
      for (const meta of this.importMetadata.values()) if (!this.persistedMetadata.has(meta.id)) this._persistMetadata(meta, true);
      if (this.storageWritable) {
        this.warnings.delete('storage-unavailable'); this.warnings.delete('storage-read-failed'); this.warnings.delete('storage-write-failed');
      }
      if (this.status().unsavedOperations === 0) this.warnings.delete('storage-record-missing');
      this._notify('retry-save'); return this.status();
    }
    history(recordId, field) {
      if (recordId !== undefined && field !== undefined) return clone(this._fieldOps(recordId, field));
      return clone([...this.ops.values()].filter(op => (recordId === undefined || op.recordId === recordId) && (field === undefined || op.field === field))
        .sort((a, b) => a.timestamp.localeCompare(b.timestamp) || a.id.localeCompare(b.id)));
    }
    undo(recordId, field) {
      this.refresh(false);
      const state = this.get(recordId, field);
      assert(state.heads.length === 1, 'Resolve the conflict explicitly before undoing');
      const current = this.ops.get(state.heads[0]);
      const previous = current.parents.map(id => this.ops.get(id)).filter(Boolean);
      assert(previous.length <= 1, 'This edit resolved a conflict; choose a historical value explicitly');
      return this.set(recordId, field, previous.length ? previous[0].value : '', {baseHeads: state.heads,
        candidateVersion: previous.length ? previous[0].candidateVersion : null, reason: 'undo:' + current.id});
    }
    restore(recordId, field, operationId) {
      const old = this.ops.get(operationId);
      assert(old && old.recordId === recordId && old.field === field, 'History operation does not match this field');
      return this.set(recordId, field, old.value, {baseHeads: this.get(recordId, field).heads, candidateVersion: old.candidateVersion, reason: 'restore:' + old.id});
    }
    snapshot() {
      const records = Object.create(null), unknownRecords = Object.create(null);
      const pairs = new Map();
      for (const op of this.ops.values()) pairs.set(JSON.stringify([op.recordId, op.field]), [op.recordId, op.field]);
      for (const [recordId, field] of pairs.values()) {
        const target = this.knownIds && !this.knownIds.has(recordId) ? unknownRecords : records;
        if (!target[recordId]) target[recordId] = Object.create(null);
        target[recordId][field] = this.get(recordId, field);
      }
      return {documentId: this.docId, schemaVersion: SCHEMA, records, unknownRecords, status: this.status()};
    }
    exportJSON() {
      this.refresh(false);
      const output = JSON.stringify({format: FORMAT, schemaVersion: SCHEMA, minReaderVersion: SCHEMA, documentId: this.docId, exportedAt: new Date().toISOString(),
        operations: this.history(), recovery: {quarantinedStorage: clone([...this.quarantine.values()]), importedMetadata: clone([...this.importMetadata.values()])}}, null, 2);
      assert(output.length <= BACKUP_LIMIT, 'Backup exceeds the 64 MiB import limit. Keep this page open and export smaller recovery batches.');
      return output;
    }
    _validateMetadata(meta) {
      assert(meta && typeof meta === 'object' && !Array.isArray(meta), 'Invalid import metadata');
      validateName(meta.id, 'metadata ID', 300);
      assert(meta.documentId === this.docId, 'Metadata belongs to another document');
      assert(typeof meta.timestamp === 'string' && Number.isFinite(Date.parse(meta.timestamp)), 'Invalid metadata timestamp');
      validateValue(meta.metadata, BACKUP_LIMIT);
      return meta;
    }
    _preserveCorruptStorage(key, raw) {
      // Repair is user-triggered via retrySave. Preserve the exact bad bytes in
      // another immutable browser key BEFORE replacing a damaged known key.
      let recovery = [...this.importMetadata.values()].find(meta => meta.metadata && meta.metadata.storageRecovery && meta.metadata.storageRecovery.key === key && meta.metadata.storageRecovery.raw === raw);
      if (!recovery) {
        recovery = {id: 'storage-recovery-' + uuid(), documentId: this.docId, timestamp: new Date().toISOString(),
          metadata: {storageRecovery: {key, raw, error: this.quarantine.has(key) ? this.quarantine.get(key).error : 'Immutable storage payload mismatch', action: 'explicit retrySave recovery'}}};
        this._validateMetadata(recovery); this.importMetadata.set(recovery.id, recovery);
      }
      return this.persistedMetadata.has(recovery.id) || this._persistMetadata(recovery);
    }
    _persistMetadata(meta, repair) {
      if (!this.storage || !this.storageWritable) return false;
      try {
        const key = this.metaPrefix + meta.id, encoded = JSON.stringify(meta), existing = this.storage.getItem(key);
        const cached = existing !== null && this.metadataRawCache.get(meta.id) === existing && this.importMetadata.get(meta.id) === meta;
        let equivalent = cached;
        if (existing !== null && !equivalent) { try { equivalent = equal(JSON.parse(existing), meta); } catch (_) { equivalent = false; } }
        if (existing !== null && !equivalent) {
          assert(repair === true, 'Metadata ID collision');
          if (!this._preserveCorruptStorage(key, existing)) return false;
          assert(this.storage.getItem(key) === existing, 'Storage changed during recovery; retry again');
        }
        if (existing === null || !equivalent) this.storage.setItem(key, encoded);
        const retained = this.storage.getItem(key);
        assert(retained === (existing === null || !equivalent ? encoded : existing), 'Browser did not retain imported metadata');
        this.persistedMetadata.add(meta.id); this.metadataRawCache.set(meta.id, retained); this.quarantine.delete(key); this.lastSavedAt = new Date().toISOString(); return true;
      } catch (e) {
        this.storageWritable = false;
        this._warn('storage-write-failed', '浏览器保存失败（可能已满或被禁用）；修改保留在本页内存。请立即导出 JSON。 ' + errorText(e));
        return false;
      }
    }
    importJSON(text) {
      assert(typeof text === 'string' && text.length <= BACKUP_LIMIT, 'Import must be a JSON file smaller than 64 MiB');
      const input = JSON.parse(text);
      assert(input && input.format === FORMAT, 'This is not a thesis revision ledger backup');
      assert(Number.isInteger(input.schemaVersion) && input.schemaVersion >= 1, 'Invalid backup schema version');
      assert((input.minReaderVersion || input.schemaVersion) <= SCHEMA, 'Backup requires a newer workbench. Nothing was imported.');
      assert(input.documentId === this.docId, 'Backup belongs to another document. Nothing was imported.');
      assert(Array.isArray(input.operations) && input.operations.length <= 100000, 'Invalid operations list');
      if (input.recovery !== undefined) assert(input.recovery && typeof input.recovery === 'object' && !Array.isArray(input.recovery), 'Invalid backup recovery data');
      this.refresh(false);
      const combined = new Map(this.ops), incoming = new Map();
      // Validate the COMPLETE merge before changing memory or browser storage.
      for (const raw of input.operations) {
        const op = clone(validateOperation(raw, this.docId));
        if (this.validateField) assert(this.validateField(op.recordId, op.field, clone(op.value)) !== false, 'Field value rejected by workbench validation');
        if (combined.has(op.id)) assert(equal(combined.get(op.id), op), 'Operation ID collision; import aborted without replacing saved data');
        else { combined.set(op.id, op); incoming.set(op.id, op); }
      }
      validateGraph(combined, true);
      const metadata = new Map();
      if (input.recovery && input.recovery.importedMetadata !== undefined) {
        assert(Array.isArray(input.recovery.importedMetadata), 'Invalid imported metadata list');
        for (const raw of input.recovery.importedMetadata) {
          const meta = clone(this._validateMetadata(raw));
          if (this.importMetadata.has(meta.id)) assert(equal(this.importMetadata.get(meta.id), meta), 'Metadata ID collision');
          else if (metadata.has(meta.id)) assert(equal(metadata.get(meta.id), meta), 'Metadata ID collision');
          else metadata.set(meta.id, meta);
        }
      }
      const extra = Object.fromEntries(Object.entries(input).filter(([key]) => !['operations', 'format', 'schemaVersion', 'minReaderVersion', 'documentId', 'exportedAt', 'recovery'].includes(key)));
      if (input.recovery) {
        const recoveryExtras = Object.fromEntries(Object.entries(input.recovery).filter(([key, value]) => key !== 'importedMetadata' && !(key === 'quarantinedStorage' && Array.isArray(value) && value.length === 0)));
        if (Object.keys(recoveryExtras).length) extra.recovery = recoveryExtras;
      }
      if (Object.keys(extra).length && ![...this.importMetadata.values(), ...metadata.values()].some(meta => equal(meta.metadata, extra))) {
        const meta = {id: 'import-' + uuid(), documentId: this.docId, timestamp: new Date().toISOString(), metadata: clone(extra)};
        this._validateMetadata(meta); metadata.set(meta.id, meta);
      }
      for (const op of incoming.values()) this._addOperation(op);
      for (const [id, meta] of metadata) this.importMetadata.set(id, meta);
      for (const op of incoming.values()) this._persist(op);
      for (const meta of metadata.values()) this._persistMetadata(meta);
      if (input.schemaVersion > SCHEMA) this._warn('newer-compatible-schema', '已合并兼容的新版本数据；未知字段及条目已保留。');
      this._notify('import');
      return {added: incoming.size, total: this.ops.size, unknownIds: Object.keys(this.snapshot().unknownRecords), status: this.status()};
    }
    destroy() { if (typeof removeEventListener === 'function') removeEventListener('storage', this._storageListener); }
  }
  RevisionLedger.FORMAT = FORMAT;
  RevisionLedger.SCHEMA_VERSION = SCHEMA;
  return RevisionLedger;
});
