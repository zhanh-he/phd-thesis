'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const Ledger = require('../ledger.js');
class Storage {
  constructor() { this.data = new Map(); this.disabled = false; this.failAfter = Infinity; this.writes = 0; }
  get length() { if (this.disabled) throw new Error('blocked'); return this.data.size; }
  key(i) { if (this.disabled) throw new Error('blocked'); return [...this.data.keys()][i] || null; }
  getItem(k) { if (this.disabled) throw new Error('blocked'); return this.data.has(k) ? this.data.get(k) : null; }
  setItem(k, v) { if (this.disabled || this.writes >= this.failAfter) throw new Error('quota/blocked'); this.writes++; this.data.set(k, String(v)); }
}
const make = (storage, extra) => new Ledger({storage, docId:'test-thesis', knownIds:['R1-01','R2-01'], ...extra});
const raw = ledger => JSON.parse(ledger.exportJSON());

test('fresh load is empty and independent of page filename', () => {
  const storage = new Storage(), a = make(storage);
  assert.equal(a.get('R1-01','plan').value, undefined);
  assert.equal(a.status().operationCount,0);
  a.set('R1-01','plan','new page filename must retain this');
  const b = make(storage);
  assert.equal(b.get('R1-01','plan').value,'new page filename must retain this');
  assert.equal(b.status().unsavedOperations,0);
});

test('every keystroke saves synchronously and refresh/reopen retains exact multiline LaTeX', () => {
  const storage = new Storage(), a = make(storage);
  const text = 'English line 1\n\\textbf{exact}  two spaces\n中文\n\n';
  for (let i=1;i<=text.length;i++) a.set('R1-01','actualText',text.slice(0,i));
  assert.equal(storage.writes,text.length);
  assert.equal(make(storage).get('R1-01','actualText').value,text);
  assert.equal(make(storage).history('R1-01','actualText').length,text.length);
});

test('long typing uses lossless storage deltas with bounded chains and retains emoji/LaTeX edits', () => {
  const storage=new Storage(), a=make(storage);
  let text='A'.repeat(600)+'\n\\textbf{🙂 中文}';
  a.set('R1-01','actualText',text);
  for(let i=0;i<80;i++) { text=text.slice(0,300)+'🙂'+text.slice(300); a.set('R1-01','actualText',text); }
  assert.ok([...storage.data.values()].some(value=>JSON.parse(value).storageFormat==='thesis-revision-storage-v1'&&JSON.parse(value).kind==='string-splice'));
  assert.ok([...a.storageDepth.values()].every(depth=>depth<=32));
  const b=make(storage); assert.equal(b.get('R1-01','actualText').value,text);
  assert.equal(b.status().quarantinedCount,0); assert.equal(b.history().length,81);
  assert.deepEqual(raw(b).operations.map(o=>o.value),raw(a).operations.map(o=>o.value));
});

test('stale tabs editing different fields or records merge without full-ledger replacement', () => {
  const storage = new Storage(), a = make(storage), b = make(storage);
  a.set('R1-01','plan','A'); b.set('R1-01','actualText','B'); b.set('R2-01','plan','C');
  a.refresh();
  assert.equal(a.get('R1-01','plan').value,'A'); assert.equal(a.get('R1-01','actualText').value,'B');
  assert.equal(make(storage).get('R2-01','plan').value,'C');
});

test('simultaneous same-field edits retain both versions; continued typing only replaces own branch', () => {
  const storage = new Storage(), a = make(storage), b = make(storage);
  const baseA = a.get('R1-01','plan').heads, baseB = b.get('R1-01','plan').heads;
  const aa = a.set('R1-01','plan','A1',{baseHeads:baseA});
  b.set('R1-01','plan','B1',{baseHeads:baseB});
  const a2 = a.set('R1-01','plan','A2',{baseHeads:[aa.writeHead]});
  const state = a.get('R1-01','plan');
  assert.equal(state.value,undefined); assert.equal(state.conflict,true);
  assert.deepEqual(new Set(state.conflicts.map(op=>op.value)),new Set(['A2','B1']));
  assert.ok(state.heads.includes(a2.writeHead));
  a.set('R1-01','plan','A2 + B1',{baseHeads:state.heads,reason:'explicit user merge'});
  b.refresh();
  assert.equal(b.get('R1-01','plan').value,'A2 + B1'); assert.equal(b.get('R1-01','plan').conflict,false);
  assert.equal(b.history('R1-01','plan').length,4);
});

test('an old tab without refresh cannot acknowledge an unseen same-field value', () => {
  const storage = new Storage(), a = make(storage), b = make(storage);
  a.set('R1-01','plan','new tab edit'); b.set('R1-01','plan','old tab edit');
  assert.equal(b.get('R1-01','plan').conflict,true);
  assert.deepEqual(new Set(make(storage).get('R1-01','plan').conflicts.map(o=>o.value)),new Set(['new tab edit','old tab edit']));
});

test('export/import roundtrip is idempotent, merges offline edits, and retains unknown IDs/fields/provenance', () => {
  const storage = new Storage(), a = make(storage);
  a.set('R1-01','authorDecision','modify',{candidateVersion:'v5'});
  a.set('R1-01','plan','first\nsecond\n\\newcommand{\\x}{y}');
  a.set('R99-unknown','futureField',{exact:'keep me',flag:false});
  const data = raw(a); data.operations[0].futureProvenance = {source:'document.txt',line:12};
  const b = make(new Storage());
  assert.equal(b.importJSON(JSON.stringify(data)).added,3);
  assert.equal(b.importJSON(JSON.stringify(data)).added,0);
  assert.deepEqual(b.get('R99-unknown','futureField').value,{exact:'keep me',flag:false});
  assert.ok(b.snapshot().unknownRecords['R99-unknown']);
  assert.deepEqual(raw(b).operations.find(op=>op.id===data.operations[0].id).futureProvenance,{source:'document.txt',line:12});
  const c=make(new Storage()); c.importJSON(JSON.stringify(data));
  b.set('R1-01','plan','offline revision'); c.set('R1-01','plan','other device revision');
  c.importJSON(b.exportJSON());
  assert.equal(c.get('R1-01','plan').conflict,true);
  assert.equal(c.get('R1-01','authorDecision').value,'modify');
});

test('invalid import is rejected completely before any mutation', () => {
  const storage = new Storage(), a = make(storage); a.set('R1-01','plan','saved');
  const before = a.history(), writes = storage.writes, data = raw(a);
  data.operations.push({...data.operations[0],id:'new-op',value:'looks valid'});
  data.operations.push({...data.operations[0],id:'bad-op',parents:['missing-parent']});
  assert.throws(()=>a.importJSON(JSON.stringify(data)),/Missing parent/);
  assert.deepEqual(a.history(),before); assert.equal(storage.writes,writes);
  const collision = raw(a); collision.operations[0].value='replace existing';
  assert.throws(()=>a.importJSON(JSON.stringify(collision)),/collision/); assert.deepEqual(a.history(),before);
  const foreign = raw(a); foreign.documentId='different-document';
  assert.throws(()=>a.importJSON(JSON.stringify(foreign)),/another document/);
  assert.throws(()=>a.importJSON('{broken'),SyntaxError);
});

test('schema evolution accepts compatible extra fields but rejects unsupported minimum reader version', () => {
  const a = make(new Storage()); a.set('R1-01','plan','saved'); const future=raw(a);
  future.schemaVersion=2; future.minReaderVersion=1; future.operations[0].newField='retained';
  const b=make(new Storage()); b.importJSON(JSON.stringify(future));
  assert.equal(raw(b).operations[0].newField,'retained');
  assert.ok(b.status().warnings.some(w=>w.code==='newer-compatible-schema'));
  future.minReaderVersion=2;
  assert.throws(()=>b.importJSON(JSON.stringify(future)),/newer workbench/);
  assert.equal(b.history().length,1);
});

test('imported future metadata and recovery survive reopen and repeated exports without nesting or duplication', () => {
  const source=make(new Storage()); source.set('R1-01','plan','text'); const data=raw(source);
  data.futureMetadata={proof:'must retain',unknown:['A',7]};
  data.recovery.quarantinedStorage=[{key:'old-key',raw:'{broken',error:'old failure'}];
  const storage=new Storage(), a=make(storage); a.importJSON(JSON.stringify(data));
  const b=make(storage), first=raw(b);
  assert.equal(b.status().metadataCount,1);
  assert.deepEqual(first.recovery.importedMetadata[0].metadata.futureMetadata,data.futureMetadata);
  assert.equal(first.recovery.importedMetadata[0].metadata.recovery.quarantinedStorage[0].raw,'{broken');
  b.importJSON(b.exportJSON()); assert.equal(b.status().metadataCount,1);
  const c=make(new Storage()); c.importJSON(b.exportJSON());
  assert.equal(c.status().metadataCount,1);
  assert.deepEqual(raw(c).recovery.importedMetadata,first.recovery.importedMetadata);
});

test('optional known-field validation rejects malformed choices atomically while retaining unknown IDs and fields', () => {
  const validateField=(recordId,field,value)=>recordId!=='R1-01' || field!=='authorDecision' || ['modify','keep','pending'].includes(value);
  const a=make(new Storage(),{validateField});
  assert.throws(()=>a.set('R1-01','authorDecision','yes'),/rejected/);
  a.set('R99-unknown','authorDecision','future choice');
  const source=make(new Storage()); source.set('R1-01','plan','valid'); source.set('R1-01','authorDecision','invalid');
  assert.throws(()=>a.importJSON(source.exportJSON()),/rejected/);
  assert.equal(a.history().length,1);
  assert.equal(a.get('R99-unknown','authorDecision').value,'future choice');
});

test('changed candidate versions preserve decisions but require re-review', () => {
  const storage=new Storage(), a=make(storage);
  a.set('R1-01','authorDecision','modify',{candidateVersion:'v5'});
  const b=make(storage);
  assert.equal(b.get('R1-01','authorDecision','v5').stale,false);
  assert.equal(b.get('R1-01','authorDecision','v6').stale,true);
  assert.equal(b.get('R1-01','authorDecision','v6').value,'modify');
  b.set('R1-01','authorDecision','modify',{candidateVersion:'v6'});
  assert.equal(b.get('R1-01','authorDecision','v6').stale,false);
});

test('undo and history restore append recovery operations instead of deleting history', () => {
  const a=make(new Storage()); const old=a.set('R1-01','plan','first');
  a.set('R1-01','plan','second'); a.undo('R1-01','plan');
  assert.equal(a.get('R1-01','plan').value,'first'); assert.equal(a.history().length,3);
  a.set('R1-01','plan','third'); a.restore('R1-01','plan',old.operationId);
  assert.equal(a.get('R1-01','plan').value,'first'); assert.equal(a.history().length,5);
});

test('corrupted storage is quarantined, raw content retained, and valid data never reset', () => {
  const storage=new Storage(), a=make(storage); a.set('R1-01','plan','valid');
  const badKey=a.prefix+'corrupt'; storage.data.set(badKey,'{broken');
  const b=make(storage);
  assert.equal(b.get('R1-01','plan').value,'valid'); assert.equal(b.status().quarantinedCount,1);
  assert.equal(storage.getItem(badKey),'{broken');
  assert.equal(raw(b).recovery.quarantinedStorage[0].raw,'{broken');
  b.set('R2-01','plan','new valid'); assert.equal(make(storage).get('R2-01','plan').value,'new valid');
});

test('corrupt cyclic relationships surface recovery alternatives instead of a blank seeded field', () => {
  const storage=new Storage(), source=make(new Storage()); source.set('R1-01','plan','first');
  const base=raw(source).operations[0];
  const first={...base,id:'cycle-a',parents:['cycle-b'],value:'recover A'}, second={...base,id:'cycle-b',parents:['cycle-a'],value:'recover B'};
  const prefix=source.prefix;
  storage.data.set(prefix+first.id,JSON.stringify(first)); storage.data.set(prefix+second.id,JSON.stringify(second));
  const a=make(storage), state=a.get('R1-01','plan');
  assert.equal(state.corruptGraph,true); assert.equal(state.conflict,true);
  assert.deepEqual(new Set(state.conflicts.map(o=>o.value)),new Set(['recover A','recover B']));
  assert.ok(a.status().warnings.some(w=>w.code==='invalid-graph'));
  assert.equal(raw(a).operations.length,2);
});

test('disabled storage warns, preserves in-memory text, and exports a recoverable ledger', () => {
  const storage=new Storage(); storage.disabled=true; const a=make(storage);
  a.set('R1-01','plan','not lost');
  assert.equal(a.status().mode,'memory'); assert.equal(a.status().unsavedOperations,1);
  const b=make(new Storage()); b.importJSON(a.exportJSON()); assert.equal(b.get('R1-01','plan').value,'not lost');
  assert.ok(a.status().warnings.some(w=>w.code==='storage-unavailable'));
});

test('storage quota failure during import retains every operation in memory and supports retry', () => {
  const source=make(new Storage()); source.set('R1-01','plan','A'); source.set('R1-01','actualText','B');
  const storage=new Storage(); storage.failAfter=1; const a=make(storage);
  const result=a.importJSON(source.exportJSON());
  assert.equal(result.added,2); assert.equal(a.get('R1-01','actualText').value,'B');
  assert.equal(a.status().unsavedOperations,1); assert.equal(a.status().mode,'memory');
  storage.failAfter=Infinity; a.retrySave();
  assert.equal(a.status().unsavedOperations,0); assert.equal(a.status().mode,'browser');
  assert.equal(make(storage).get('R1-01','actualText').value,'B');
});

test('malicious or cyclic parents, non-JSON values and foreign field bases are rejected', () => {
  const a=make(new Storage()); const write=a.set('R1-01','plan','saved');
  assert.throws(()=>a.set('R1-01','actualText','x',{baseHeads:[write.writeHead]}),/another field/);
  assert.throws(()=>a.set('R1-01','plan',NaN),/finite/);
  assert.throws(()=>a.set('R1-01','plan',undefined),/Undefined/);
  const data=raw(a), first={...data.operations[0],id:'cycle-1',parents:['cycle-2']},second={...data.operations[0],id:'cycle-2',parents:['cycle-1']};
  data.operations.push(first,second); assert.throws(()=>a.importJSON(JSON.stringify(data)),/cycle/);
  assert.equal(a.history().length,1);
});

test('a second manuscript isolates overlapping comment IDs and supports different reviewer counts and source order', () => {
  const storage=new Storage();
  const thesisIds=Array.from({length:43},(_,i)=>i===0?'R1-01':'thesis-'+String(i+1).padStart(2,'0'));
  // Deliberately use a different reviewer order, unequal counts, and IDs whose
  // lexical order does not match the report. The ledger keys values by ID;
  // callers retain this source order instead of relying on write/index order.
  const manuscriptReviewers=[
    {id:'reviewer-Z',comments:['R1-01','Z-comment-20']},
    {id:'reviewer-A',comments:['A-comment-09','A-comment-01','A-final-note']}
  ];
  const manuscriptIds=manuscriptReviewers.flatMap(reviewer=>reviewer.comments);
  const thesis=new Ledger({storage,docId:'phd-thesis-project',knownIds:thesisIds});
  const manuscript=new Ledger({storage,docId:'manuscript-journal-2027',knownIds:manuscriptIds});
  thesis.set('R1-01','plan','Thesis-specific plan');
  thesis.set('thesis-43','authorDecision','keep',{candidateVersion:'thesis-v5'});
  for(const id of [...manuscriptIds].reverse()) manuscript.set(id,'plan','Manuscript plan for '+id);
  thesis.refresh(); manuscript.refresh();
  assert.equal(thesis.get('R1-01','plan').value,'Thesis-specific plan');
  assert.equal(manuscript.get('R1-01','plan').value,'Manuscript plan for R1-01');
  assert.equal(thesis.get('Z-comment-20','plan').value,undefined);
  assert.equal(manuscript.get('thesis-43','authorDecision').value,undefined);
  assert.deepEqual(manuscriptIds.map(id=>manuscript.get(id,'plan').value),[
    'Manuscript plan for R1-01','Manuscript plan for Z-comment-20',
    'Manuscript plan for A-comment-09','Manuscript plan for A-comment-01','Manuscript plan for A-final-note'
  ]);
  assert.equal(raw(thesis).operations.length,2); assert.equal(raw(manuscript).operations.length,5);
  const reopenedThesis=new Ledger({storage,docId:'phd-thesis-project',knownIds:thesisIds});
  const reopenedManuscript=new Ledger({storage,docId:'manuscript-journal-2027',knownIds:manuscriptIds});
  assert.equal(reopenedThesis.get('R1-01','plan').value,'Thesis-specific plan');
  assert.equal(reopenedManuscript.get('R1-01','plan').value,'Manuscript plan for R1-01');
  assert.deepEqual(Object.keys(reopenedManuscript.snapshot().unknownRecords),[]);
});

test('foreign manuscript imports reject atomically even with overlapping IDs or a forged top-level document ID', () => {
  const storage=new Storage();
  const thesis=new Ledger({storage,docId:'thesis',knownIds:['R1-01']});
  const manuscript=new Ledger({storage,docId:'new-manuscript',knownIds:['R1-01','Reviewer-B-2']});
  thesis.set('R1-01','actualText','Thesis text\n\\section{Keep exact}');
  manuscript.set('R1-01','actualText','Different paper text');
  manuscript.set('Reviewer-B-2','plan','New manuscript-only comment');
  const before=thesis.history(),writes=storage.writes;
  assert.throws(()=>thesis.importJSON(manuscript.exportJSON()),/another document/);
  assert.deepEqual(thesis.history(),before); assert.equal(storage.writes,writes);
  const forged=raw(manuscript); forged.documentId='thesis';
  assert.throws(()=>thesis.importJSON(JSON.stringify(forged)),/another document/);
  assert.deepEqual(thesis.history(),before); assert.equal(storage.writes,writes);
  assert.equal(thesis.get('Reviewer-B-2','plan').value,undefined);
  assert.equal(thesis.get('R1-01','actualText').value,'Thesis text\n\\section{Keep exact}');
});

test('same manuscript source updates preserve exact old choices, flag new candidates and retain newer unknown IDs', () => {
  const storage=new Storage(),docId='manuscript-rounds';
  const original=new Ledger({storage,docId,knownIds:['review-A-1','review-B-1']});
  original.set('review-A-1','authorDecision','keep',{candidateVersion:'round1-candidate'});
  original.set('review-A-1','plan','Original decision evidence\nDo not paraphrase.\n\\cite{Exact2027}');
  original.set('review-B-1','actualText','Archived comment text\n  Preserve spaces.\n');
  const newerDevice=new Ledger({storage:new Storage(),docId,knownIds:['review-A-1','review-C-new']});
  newerDevice.importJSON(original.exportJSON());
  newerDevice.set('review-C-new','plan','New reviewer note\nAwait source update.');
  original.importJSON(newerDevice.exportJSON());
  const reopenedOldSource=new Ledger({storage,docId,knownIds:['review-A-1','review-B-1']});
  assert.equal(reopenedOldSource.snapshot().unknownRecords['review-C-new'].plan.value,'New reviewer note\nAwait source update.');
  // A later source dataset changes both its comment roster and candidate text.
  const updated=new Ledger({storage,docId,knownIds:['review-C-new','review-A-1']});
  const oldChoice=updated.get('review-A-1','authorDecision','round2-candidate');
  assert.equal(oldChoice.value,'keep'); assert.equal(oldChoice.stale,true);
  assert.equal(oldChoice.candidateVersion,'round1-candidate');
  assert.equal(updated.get('review-A-1','plan').value,'Original decision evidence\nDo not paraphrase.\n\\cite{Exact2027}');
  assert.equal(updated.snapshot().records['review-C-new'].plan.value,'New reviewer note\nAwait source update.');
  assert.equal(updated.snapshot().unknownRecords['review-B-1'].actualText.value,'Archived comment text\n  Preserve spaces.\n');
  const portable=new Ledger({storage:new Storage(),docId,knownIds:['review-A-1']});
  portable.importJSON(updated.exportJSON());
  assert.equal(portable.get('review-A-1','authorDecision','round2-candidate').stale,true);
  assert.equal(portable.snapshot().unknownRecords['review-C-new'].plan.value,'New reviewer note\nAwait source update.');
  assert.equal(portable.snapshot().unknownRecords['review-B-1'].actualText.value,'Archived comment text\n  Preserve spaces.\n');
});

test('field index avoids global scans and only invalidates the field receiving a local or remote operation', () => {
  const storage=new Storage(),a=make(storage);
  a.set('R1-01','plan','plan 1'); a.set('R2-01','actualText',{text:'exact object value'});
  a.get('R1-01','plan'); a.get('R2-01','actualText');
  const planEntry=a._fieldEntry('R1-01','plan'),actualEntry=a._fieldEntry('R2-01','actualText');
  const oldActualState=actualEntry.state,oldPlanState=planEntry.state;
  // Reads and a local write must not enumerate the entire operation collection.
  const values=a.ops.values;
  a.ops.values=()=>{ throw new Error('Unexpected global operation scan'); };
  assert.equal(a.get('R1-01','plan').value,'plan 1');
  assert.equal(a.history('R2-01','actualText').length,1);
  a.set('R1-01','plan','plan 2');
  assert.notEqual(planEntry.state,oldPlanState);
  assert.equal(actualEntry.state,oldActualState);
  a.ops.values=values;
  const b=make(storage); b.set('R1-01','plan','remote plan 3');
  const localPlanState=planEntry.state; a.refresh();
  assert.equal(planEntry.state,null); assert.equal(actualEntry.state,oldActualState);
  assert.equal(a.get('R1-01','plan').value,'remote plan 3');
  assert.notEqual(planEntry.state,localPlanState);
  const state=a.get('R2-01','actualText');
  state.value.text='caller mutation'; state.heads.push('fake'); state.alternatives[0].value.text='also mutated';
  assert.deepEqual(a.get('R2-01','actualText').value,{text:'exact object value'});
  assert.equal(a.get('R2-01','actualText').heads.length,1);
});

test('5200-operation workload keeps repeated 43-by-6 field reads cached', t => {
  const {performance}=require('node:perf_hooks');
  // Fast native-like key access avoids benchmarking the fixture's usual
  // Array.from(Map.keys()) key() implementation instead of the ledger.
  class FastStorage extends Storage {
    constructor(){super();this.keyList=[];}
    key(i){return this.keyList[i]??null;}
    setItem(key,value){if(!this.data.has(key))this.keyList.push(key);super.setItem(key,value);}
  }
  const storage=new FastStorage(),ids=Array.from({length:43},(_,i)=>'comment-'+i);
  const fields=['authorDecision','assistantDecision','plan','actualText','executionStatus','verificationNotes'];
  const seed=make(new Storage()); seed.set('R1-01','plan','seed'); const template=raw(seed).operations[0];
  const operations=[],heads=new Map();
  for(let i=0;i<5200;i++){
    const recordId=ids[i%43],field=fields[Math.floor(i/43)%6],key=recordId+'/'+field,id='bench-'+i;
    operations.push({...template,id,recordId,field,value:'saved-'+i+'X'.repeat(1000),parents:heads.has(key)?[heads.get(key)]:[]});
    heads.set(key,id);
  }
  const ledger=make(storage,{knownIds:ids});
  ledger.importJSON(JSON.stringify({format:Ledger.FORMAT,schemaVersion:1,minReaderVersion:1,documentId:'test-thesis',operations}));
  let start=performance.now();
  for(let pass=0;pass<10;pass++)for(const id of ids)for(const field of fields)ledger.get(id,field);
  const readMs=performance.now()-start;
  const unchangedCache=ledger._fieldEntry(ids[42],fields[5]).state;
  start=performance.now();ledger.set(ids[0],'plan','new input');
  for(const id of ids)for(const field of fields)ledger.get(id,field);
  const writeMs=performance.now()-start;
  assert.equal(ledger._fieldEntry(ids[42],fields[5]).state,unchangedCache);
  assert.equal(ledger.get(ids[0],'plan').value,'new input');
  assert.equal(ledger.status().operationCount,5201);assert.equal(ledger.status().unsavedOperations,0);
  t.diagnostic('Node in-memory-storage sample: 2580 reads='+readMs.toFixed(2)+'ms; write + 258 reads='+writeMs.toFixed(2)+'ms. No browser timing promise.');
});

test('actual large workbench metadata validates on reopen once and remains cached during input/refresh/export', t => {
  const fs=require('node:fs'),path=require('node:path'),{performance}=require('node:perf_hooks');
  const dataset=JSON.parse(fs.readFileSync(path.join(__dirname,'../data.json'),'utf8'));
  const context={dataset,sourceBaseline:dataset.sourceBaseline},bytes=Buffer.byteLength(JSON.stringify(context));
  assert.ok(bytes>100000,'Benchmark must exercise real large source metadata');
  const storage=new Storage(),a=make(storage),input=raw(a);input.workbenchContext=context;
  a.importJSON(JSON.stringify(input));
  const meta=[...a.importMetadata.values()][0],metadataKey=a.metaPrefix+meta.id;
  assert.equal(a.metadataRawCache.get(meta.id),storage.getItem(metadataKey));
  const reopened=make(storage);
  assert.deepEqual([...reopened.importMetadata.values()][0].metadata.workbenchContext,context);
  let revalidations=0;
  const originalValidate=reopened._validateMetadata;
  reopened._validateMetadata=function(value){revalidations++;return originalValidate.call(this,value);};
  let start=performance.now();for(let i=0;i<20;i++)reopened.refresh(false);const refreshMs=performance.now()-start;
  start=performance.now();reopened.set('R1-01','plan','input with large metadata present');const setMs=performance.now()-start;
  start=performance.now();const exported=JSON.parse(reopened.exportJSON());const exportMs=performance.now()-start;
  assert.equal(revalidations,0,'Identical immutable metadata bytes must not be reparsed/revalidated');
  assert.deepEqual(exported.recovery.importedMetadata[0].metadata.workbenchContext,context);
  assert.equal(reopened.get('R1-01','plan').value,'input with large metadata present');
  assert.equal(reopened.status().unsavedOperations,0);
  t.diagnostic('Actual context '+bytes+' bytes; Node memory storage:20 refreshes='+refreshMs.toFixed(2)+'ms;set='+setMs.toFixed(2)+'ms;export+parse='+exportMs.toFixed(2)+'ms. No browser timing promise.');
});

test('metadata cache revalidates changed bytes and preserves both stored corruption and original imported context', () => {
  const storage=new Storage(),a=make(storage),input=raw(a);
  input.workbenchContext={source:'trusted original',quote:'Exact original\n\\LaTeX{}'};
  a.importJSON(JSON.stringify(input));a.set('R1-01','plan','saved plan');
  const meta=[...a.importMetadata.values()][0],key=a.metaPrefix+meta.id,originalRaw=storage.getItem(key);
  let validations=0;const originalValidate=a._validateMetadata;
  a._validateMetadata=function(value){validations++;return originalValidate.call(this,value);};
  // Formatting-only changes are safe but must still pass validation before caching.
  storage.data.set(key,JSON.stringify(JSON.parse(originalRaw),null,2));a.refresh(false);
  assert.equal(validations,1);assert.equal(a.status().quarantinedCount,0);
  assert.equal(a.metadataRawCache.get(meta.id),storage.getItem(key));
  // A valid-looking changed payload with the same immutable ID is a collision.
  const tampered=JSON.parse(originalRaw);tampered.metadata.workbenchContext.source='different payload';
  const tamperedRaw=JSON.stringify(tampered);storage.data.set(key,tamperedRaw);a.refresh(false);
  assert.equal(validations,2);assert.equal(a.status().quarantinedCount,1);
  assert.equal(a.status().unsavedOperations,1);
  assert.equal(a.importMetadata.get(meta.id).metadata.workbenchContext.source,'trusted original');
  assert.equal(storage.getItem(key),tamperedRaw,'Do not overwrite evidence of corruption');
  const recovered=JSON.parse(a.exportJSON());
  assert.equal(recovered.recovery.importedMetadata[0].metadata.workbenchContext.source,'trusted original');
  assert.equal(recovered.recovery.quarantinedStorage[0].raw,tamperedRaw);
  assert.equal(a.get('R1-01','plan').value,'saved plan');
  // A conflicting import must reject even otherwise valid new operations atomically.
  const candidate=JSON.parse(a.exportJSON()),before=a.history(),writes=storage.writes;
  candidate.operations.push({...candidate.operations[0],id:'must-not-import',parents:[],value:'new operation'});
  candidate.recovery.importedMetadata[0].metadata.workbenchContext.source='conflicting import';
  assert.throws(()=>a.importJSON(JSON.stringify(candidate)),/Metadata ID collision/);
  assert.deepEqual(a.history(),before);assert.equal(storage.writes,writes);
  assert.equal(a.importMetadata.get(meta.id).metadata.workbenchContext.source,'trusted original');
  // Restoring the original bytes makes the immutable cached data durable again.
  storage.data.set(key,originalRaw);a.refresh(false);
  assert.equal(a.status().quarantinedCount,0);assert.equal(a.status().unsavedOperations,0);
  assert.deepEqual(make(storage).importMetadata.get(meta.id),meta);
});

test('Q01 deleted operation and metadata keys become unsaved and explicit retry restores them before reopen', () => {
  const storage=new Storage(),a=make(storage);
  a.set('R1-01','plan','recover this exact note\n\\cite{Key}');
  const input=raw(a);input.qaFutureMetadata={proof:'recover metadata too'};a.importJSON(JSON.stringify(input));
  assert.equal(a.status().unsavedOperations,0);
  storage.data.clear();a.refresh(false);
  assert.equal(a.status().unsavedOperations,2);
  assert.ok(a.status().warnings.some(w=>w.code==='storage-record-missing'));
  assert.equal(a.get('R1-01','plan').value,'recover this exact note\n\\cite{Key}');
  a.retrySave();assert.equal(a.status().unsavedOperations,0);assert.equal(storage.length,2);
  const reopened=make(storage);
  assert.equal(reopened.get('R1-01','plan').value,'recover this exact note\n\\cite{Key}');
  assert.equal([...reopened.importMetadata.values()][0].metadata.qaFutureMetadata.proof,'recover metadata too');
});

test('Q01 corrupt known operation and metadata bytes are durably archived before explicit retry repairs keys', () => {
  const storage=new Storage(),a=make(storage),write=a.set('R1-01','plan','durable original');
  const input=raw(a);input.qaFutureMetadata={proof:'original metadata'};a.importJSON(JSON.stringify(input));
  const opKey=a.prefix+write.writeHead,meta=[...a.importMetadata.values()][0],metaKey=a.metaPrefix+meta.id;
  const badOp='{QA intentionally malformed JSON',badMeta='{bad metadata';
  storage.data.set(opKey,badOp);storage.data.set(metaKey,badMeta);a.refresh(false);
  assert.equal(a.status().unsavedOperations,2);assert.equal(a.status().quarantinedCount,2);
  assert.equal(storage.getItem(opKey),badOp);assert.equal(storage.getItem(metaKey),badMeta);
  assert.equal(a.get('R1-01','plan').value,'durable original');
  a.retrySave();assert.equal(a.status().unsavedOperations,0);assert.equal(a.status().quarantinedCount,0);
  const reopened=make(storage),recovery=raw(reopened).recovery.importedMetadata;
  assert.equal(reopened.get('R1-01','plan').value,'durable original');
  assert.equal(reopened.importMetadata.get(meta.id).metadata.qaFutureMetadata.proof,'original metadata');
  assert.ok(recovery.some(item=>item.metadata.storageRecovery&&item.metadata.storageRecovery.key===opKey&&item.metadata.storageRecovery.raw===badOp));
  assert.ok(recovery.some(item=>item.metadata.storageRecovery&&item.metadata.storageRecovery.key===metaKey&&item.metadata.storageRecovery.raw===badMeta));
});

test('Q01 failed recovery archival never overwrites corrupt bytes and remains exportable in memory', () => {
  const storage=new Storage(),a=make(storage),write=a.set('R1-01','plan','still recoverable');
  const key=a.prefix+write.writeHead,bad='{damaged bytes';storage.data.set(key,bad);a.refresh(false);
  storage.failAfter=storage.writes;a.retrySave();
  assert.equal(storage.getItem(key),bad);assert.ok(a.status().unsavedOperations>0);
  assert.equal(a.status().mode,'memory');assert.equal(a.get('R1-01','plan').value,'still recoverable');
  const backup=raw(a);assert.ok(backup.recovery.quarantinedStorage.some(item=>item.raw===bad));
  assert.ok(backup.recovery.importedMetadata.some(item=>item.metadata.storageRecovery&&item.metadata.storageRecovery.raw===bad));
  storage.failAfter=Infinity;a.retrySave();
  assert.equal(a.status().unsavedOperations,0);assert.equal(make(storage).get('R1-01','plan').value,'still recoverable');
});

test('Q05 a valid 2 MiB note and legacy duplicated context backup above 8 MiB self-import exactly', () => {
  const note='x'.repeat(2*1024*1024),a=make(new Storage());a.set('R1-01','actualText',note);
  const input=raw(a);
  // Frozen old app copied the same text into several dynamic context views.
  // Continue accepting those real older backups even though new app avoids it.
  input.workbenchContext={records:[{id:'R1-01',current:{actualText:note,fieldState:{value:note,alternatives:[{value:note}],conflicts:[{value:note}]}}}]};
  const text=JSON.stringify(input,null,2);assert.ok(text.length>8*1024*1024&&text.length<64*1024*1024);
  const storage=new Storage(),b=make(storage);b.importJSON(text);
  assert.equal(b.get('R1-01','actualText').value,note);
  const reopened=make(storage);assert.equal(reopened.get('R1-01','actualText').value,note);
  assert.equal([...reopened.importMetadata.values()][0].metadata.workbenchContext.records[0].current.actualText,note);
  const c=make(new Storage());c.importJSON(reopened.exportJSON());assert.equal(c.get('R1-01','actualText').value,note);
});

test('Q08 future encoding/storageFormat operation fields survive import, envelope storage and reopen', () => {
  const source=make(new Storage());source.set('R1-01','plan','exact compatible future note');
  const input=raw(source),op=input.operations[0];
  Object.assign(op,{encoding:'string-splice-v1',storageFormat:'thesis-revision-storage-v1',kind:'string-splice',operation:{future:'data'},delta:{future:'also data'}});
  const storage=new Storage(),a=make(storage);a.importJSON(JSON.stringify(input));
  const stored=JSON.parse(storage.getItem(a.prefix+op.id));
  assert.equal(stored.storageFormat,'thesis-revision-storage-v1');assert.equal(stored.kind,'operation');
  assert.equal(stored.operation.encoding,'string-splice-v1');
  const b=make(storage);assert.equal(b.get('R1-01','plan').value,'exact compatible future note');
  assert.equal(b.status().quarantinedCount,0);assert.deepEqual(raw(b).operations[0],op);
  // Previously stored ordinary raw operations get the same unambiguous precedence.
  const legacyStorage=new Storage();legacyStorage.data.set(a.prefix+op.id,JSON.stringify(op));
  const legacy=make(legacyStorage);assert.equal(legacy.get('R1-01','plan').value,op.value);
  assert.deepEqual(raw(legacy).operations[0],op);
});

test('Q08 backward-compatible raw full and old delta storage still reconstruct exact values', () => {
  const source=make(new Storage());source.set('R1-01','plan','old base text');const parent=raw(source).operations[0];
  const child={...parent,id:'legacy-child',parents:[parent.id]};delete child.value;
  const wrapper={encoding:'string-splice-v1',operation:child,delta:{baseId:parent.id,start:4,remove:4,insert:'replacement'}};
  const storage=new Storage();storage.data.set(source.prefix+parent.id,JSON.stringify(parent));storage.data.set(source.prefix+child.id,JSON.stringify(wrapper));
  const a=make(storage);assert.equal(a.get('R1-01','plan').value,'old replacement text');assert.equal(a.status().quarantinedCount,0);
  a.set('R1-01','plan','new text');assert.equal(make(storage).get('R1-01','plan').value,'new text');
});
