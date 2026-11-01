#!/usr/bin/env python3
"""Build a self-contained workbench while conservatively checking source anchors.

Relative source paths resolve against this manuscript directory, or an explicit
--source-root. Original snapshots and locations remain intact. Current bindings
are annotations; missing or ambiguous quotes never select a nearby line.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PLACEHOLDER_DOCUMENT_ID = 'REPLACE_WITH_UNIQUE_MANUSCRIPT_ID'


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def validate_envelope(data: dict) -> None:
    """Check understood fields without whitelisting away future extensions."""
    if not isinstance(data, dict):
        raise ValueError('The manuscript dataset must be a JSON object')
    version = data.get('schemaVersion')
    if type(version) is not int or version < 1:
        raise ValueError('schemaVersion must be a positive integer')
    document_id = data.get('documentId')
    if not isinstance(document_id, str) or not document_id.strip() or len(document_id) > 300 or re.search(r'[\x00-\x1f]', document_id):
        raise ValueError('documentId must be a stable, nonempty manuscript identity')
    if document_id == PLACEHOLDER_DOCUMENT_ID:
        raise ValueError('Replace the template documentId with a unique stable manuscript ID before building')
    if version != 1:
        # Preserve unsupported future payloads for the UI read-only/download
        # path; do not interpret, reconstruct, or silently downgrade them.
        return
    reviewers, comments = data.get('reviewers'), data.get('comments')
    if not isinstance(reviewers, list) or not isinstance(comments, list):
        raise ValueError('Schema 1 requires ordered reviewers[] and comments[] arrays')
    reviewer_ids, comment_ids = [], []
    for reviewer in reviewers:
        if not isinstance(reviewer, dict) or not isinstance(reviewer.get('id'), str) or not reviewer['id']:
            raise ValueError('Each reviewer requires a stable string id')
        reviewer_ids.append(reviewer['id'])
    if len(set(reviewer_ids)) != len(reviewer_ids):
        raise ValueError('Reviewer IDs must be unique')
    for comment in comments:
        if not isinstance(comment, dict) or not isinstance(comment.get('id'), str) or not comment['id']:
            raise ValueError('Each comment requires a stable string id')
        if comment.get('reviewer') not in reviewer_ids:
            raise ValueError('A comment refers to an undefined reviewer')
        if not isinstance(comment.get('locations', []), list):
            raise ValueError('Comment locations must be an array')
        comment_ids.append(comment['id'])
    if len(set(comment_ids)) != len(comment_ids):
        raise ValueError('Comment IDs must be unique within a manuscript')


def safe_source(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or '\\' in relative:
        raise ValueError('Invalid relative source path')
    posix = PurePosixPath(relative)
    if posix.is_absolute() or '..' in posix.parts:
        raise ValueError('Source path must remain inside this manuscript')
    result = (root / posix).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError('Source path escapes this manuscript')
    return result


def occurrences(text: str, quote: str) -> list[int]:
    positions, start = [], 0
    while True:
        position = text.find(quote, start)
        if position < 0:
            return positions
        positions.append(position)
        start = position + 1


def line_span(text: str, start: int, quote: str) -> tuple[int, int]:
    # Text indices are internal only. No UTF-16/codepoint offset interoperability
    # is promised; exported line numbers refer to this exact source snapshot.
    end = max(start, start + len(quote) - 1)
    return text.count('\n', 0, start) + 1, text.count('\n', 0, end) + 1


def bind_location(location: dict, data: dict, source_root: Path, current_sources: dict) -> dict:
    binding = {'status': 'needs_relocation', 'reviewRequired': True,
               'reason': '需重新定位；保留原始位置与原句。'}
    relative, quote = location.get('file'), location.get('quote')
    try:
        path = safe_source(source_root, relative)
    except (ValueError, TypeError):
        binding['reason'] = '源文件路径不属于当前稿件；原始定位已保留。'
        return binding
    try:
        content = path.read_bytes()
        text = content.decode('utf-8')
    except (OSError, UnicodeError):
        binding['reason'] = '当前源文件不存在、无法读取或不是 UTF-8 文本；原始定位已保留。'
        return binding
    current_hash = sha256(content)
    current_sources[relative] = {'text': text, 'sha256': current_hash}
    binding['currentSourceSha256'] = current_hash
    snapshot = data.get('sources', {}).get(relative, {})
    expected_hash = location.get('sourceSha256') or snapshot.get('sha256')
    if not expected_hash:
        binding['reason'] = '缺少原始源码版本哈希，不能自动确认定位。'
        return binding
    if not isinstance(quote, str) or not quote:
        binding['reason'] = '缺少可精确搜索的原句，不能自动确认定位。'
        return binding
    if isinstance(snapshot.get('text'), str) and snapshot.get('sha256'):
        if sha256(snapshot['text'].encode('utf-8')) != snapshot['sha256']:
            binding['reason'] = '原始源码快照与其哈希不一致；保留数据并等待核实。'
            return binding
    positions = occurrences(text, quote)
    if not positions:
        binding['reason'] = '原句在当前源码中已找不到；需重新定位，原句未被替换。'
        return binding
    start_line, end_line = location.get('lineStart'), location.get('lineEnd')
    if current_hash == expected_hash and type(start_line) is int and type(end_line) is int:
        lines = text.splitlines(keepends=True)
        if 1 <= start_line <= end_line <= len(lines):
            range_start = sum(len(line) for line in lines[:start_line - 1])
            range_end = sum(len(line) for line in lines[:end_line])
            within = [p for p in positions if range_start <= p and p + len(quote) <= range_end]
            if len(within) == 1:
                first, last = line_span(text, within[0], quote)
                return {'status': 'verified', 'lineStart': first, 'lineEnd': last,
                        'currentSourceSha256': current_hash, 'reviewRequired': False,
                        'matchedBy': 'source-hash-and-original-range', 'reason': '源码版本与原始范围核对一致。'}
    if len(positions) == 1:
        position, matched_by = positions[0], 'unique-exact-quote'
    else:
        prefix = location.get('prefix', location.get('before', ''))
        suffix = location.get('suffix', location.get('after', ''))
        prefix = prefix if isinstance(prefix, str) else ''
        suffix = suffix if isinstance(suffix, str) else ''
        contextual = [p for p in positions if (prefix or suffix)
                      and (not prefix or text[:p].endswith(prefix))
                      and (not suffix or text[p + len(quote):].startswith(suffix))]
        if len(contextual) != 1:
            binding['reason'] = '当前源码有多个相同原句，前后文不能唯一确认；需重新定位。'
            return binding
        position, matched_by = contextual[0], 'unique-exact-quote-and-context'
    first, last = line_span(text, position, quote)
    changed = current_hash != expected_hash
    return {'status': 'relocated', 'lineStart': first, 'lineEnd': last,
            'currentSourceSha256': current_hash, 'reviewRequired': changed,
            'matchedBy': matched_by,
            'reason': '源码版本已变化，已按唯一原句重新定位；旧决定需要复核。' if changed else '已按唯一精确原句或前后文重新定位。'}


def prepare_data(data: dict, source_root: Path = ROOT) -> dict:
    validate_envelope(data)
    prepared = copy.deepcopy(data)
    if prepared['schemaVersion'] != 1:
        return prepared
    current_sources = {}
    for comment in prepared['comments']:
        signature = []
        for location in comment.get('locations', []):
            if not isinstance(location, dict):
                raise ValueError('Every location must be a JSON object')
            # Keep future binding extensions while recomputing safety fields.
            previous = location.get('binding')
            binding = copy.deepcopy(previous) if isinstance(previous, dict) else {}
            for key in ('status', 'lineStart', 'lineEnd', 'currentSourceSha256', 'reviewRequired', 'matchedBy', 'reason'):
                binding.pop(key, None)
            binding.update(bind_location(location, prepared, source_root, current_sources))
            location['binding'] = binding
            signature.append({'file': location.get('file'), 'quote': location.get('quote'),
                              'originalSourceSha256': location.get('sourceSha256'),
                              'currentSourceSha256': binding.get('currentSourceSha256'), 'status': binding['status']})
        comment['sourceBindingVersion'] = 'source-binding-' + sha256(json.dumps(signature, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())[:24]
    existing_sources = prepared.get('currentSources', {})
    if not isinstance(existing_sources, dict):
        raise ValueError('currentSources must be an object when present')
    merged_sources = copy.deepcopy(existing_sources)
    for relative, snapshot in current_sources.items():
        old = merged_sources.get(relative)
        merged_sources[relative] = {**(old if isinstance(old, dict) else {}), **snapshot}
    prepared['currentSources'] = merged_sources
    return prepared


def build(data_path: Path | str | None = None, output_path: Path | str | None = None, source_root: Path | str | None = None) -> dict:
    data_path = Path(data_path) if data_path is not None else HERE / 'data.json'
    output_path = Path(output_path) if output_path is not None else ROOT / 'START_HERE.html'
    source_root = Path(source_root).resolve() if source_root is not None else ROOT
    data = prepare_data(json.loads(data_path.read_text(encoding='utf-8')), source_root)
    template = (HERE / 'template.html').read_text(encoding='utf-8')
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    pieces = {
        '/* WORKBENCH_CSS */': (HERE / 'style.css').read_text(encoding='utf-8'),
        '/* WORKBENCH_DATA */': payload,
        '/* WORKBENCH_LEDGER */': (HERE / 'ledger.js').read_text(encoding='utf-8').replace('</script', '<\\/script'),
        '/* WORKBENCH_APP */': (HERE / 'app.js').read_text(encoding='utf-8').replace('</script', '<\\/script'),
    }
    for marker, text in pieces.items():
        if template.count(marker) != 1:
            raise ValueError(f'Template must contain exactly one {marker}')
        template = template.replace(marker, text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template, encoding='utf-8')
    comments = data.get('comments')
    count = len(comments) if isinstance(comments, list) else 'future-schema'
    print(f'Built {output_path.name}: {len(template.encode()):,} bytes, {count} comments')
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=HERE / 'data.json', help='Manuscript JSON dataset')
    parser.add_argument('--output', type=Path, default=ROOT / 'START_HERE.html', help='Self-contained HTML output')
    parser.add_argument('--source-root', type=Path, default=ROOT, help='Directory containing manuscript source files')
    args = parser.parse_args()
    try:
        build(args.data, args.output, args.source_root)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(2, f'Build failed: {exc}\n')
