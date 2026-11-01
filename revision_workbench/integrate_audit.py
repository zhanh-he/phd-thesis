#!/usr/bin/env python3
"""Normalize the independently audited reviewer data for the offline UI.

This copies evidence and source snapshots, never edits thesis files or author
decisions. Run only after the source auditor marks the packet complete.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def decision(value: str) -> str:
    return {'modify': 'modify', 'no_modify': 'keep', 'no-modify': 'keep',
            'keep': 'keep', 'pending': 'pending'}[value]


def reply_display(value: str) -> str:
    # Some native annotations contain literal backslash-n separators. Keep their
    # exact bytes in the provenance; only render those separators as new lines.
    return value.replace('\\n', '\n')


def integrate(source: Path) -> dict:
    raw = source.read_bytes()
    audit = json.loads(raw)
    assert len(audit['items']) == 43
    assert audit['audit_status'] not in {'assembling_locations', 'draft', 'pending'}, 'Auditor has not finished this packet'
    assert all(x['locations_complete'] for x in audit['items']), 'Some source locations are still pending'
    expected = [f'R1-{i:02}' for i in range(1, 39)] + [f'R2-{i:02}' for i in range(1, 6)]
    assert [x['id'] for x in audit['items']] == expected
    sources = {}
    for relative, expected_hash in audit['source_snapshot'].items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT)
        content = path.read_bytes()
        assert digest(content) == expected_hash, f'Source baseline differs: {relative}'
        sources[relative] = {'text': content.decode(), 'sha256': expected_hash}
    reports = {r['id']: r for r in audit['reports']}
    recheck_path=source.with_name('author_prefill_recheck_v2.json')
    recheck=json.loads(recheck_path.read_text()) if recheck_path.is_file() else {}
    display_corrections={c['id']:c for c in recheck.get('proposed_display_correction',{}).get('items',[])}
    comments = []
    for item in audit['items']:
        cid = item['id']
        report = reports[item['reviewer_id']]
        assert digest((ROOT / report['source_pdf']).read_bytes()) == report['sha256']
        locations = []
        proposals = []
        for loc in item['locations']:
            asset = loc.get('file') if loc.get('asset') else None
            anchor_loc = loc.get('texReference', loc) if asset else loc
            if asset:
                assert digest((ROOT / asset).read_bytes()) == loc['sourceSha256'], f'Asset differs: {asset}'
            relative = anchor_loc.get('relative_file', anchor_loc.get('file'))
            start = anchor_loc.get('source_line_start', anchor_loc.get('lineStart'))
            end = anchor_loc.get('source_line_end', anchor_loc.get('lineEnd'))
            quote = anchor_loc.get('anchor_quote', anchor_loc.get('anchorExact'))
            assert relative in sources, (cid, relative)
            lines = sources[relative]['text'].splitlines(keepends=True)
            assert 1 <= start <= end <= len(lines), (cid, relative, start, end)
            assert quote and quote in ''.join(lines[start-1:end]), (cid, 'exact quote not in declared lines', loc)
            path = loc.get('section_path', loc.get('sectionPath', []))
            if isinstance(path, list):
                section = loc.get('plain_label') or ' / '.join(x.get('title_tex', x.get('title', '')) if isinstance(x, dict) else str(x) for x in path)
            else:
                section = loc.get('plain_label') or str(path)
            operation = str(loc['operation']).lower()
            operation = {'review_only': 'verify', 'review-only': 'verify', 'pending_scope_gap': 'verify', 'reference_only': 'keep', 'format': 'formatting'}.get(operation, operation)
            position = loc.get('insertPosition', loc.get('insertion_position'))
            note = ''
            if operation in {'insert', 'insertion'}:
                note = '在上述原文之后插入；原文保留。'
                if position:
                    p = str(position)
                    if 'after end{table}, before subsection' in p:
                        note = '在 \\end{table} 后、下一个 \\subsection 前插入；原句中的标题只用于定位。'
                    elif 'within same caption' in p:
                        note = '在下方对应说明句后追加，仍放在同一图注内。'
                    elif 'before next subsection' in p or 'before next figure' in p:
                        note = '在下方段落后、下一个小节标题或图之前插入。'
            elif operation in {'delete', 'deletion'}:
                note = '只删除下列原文范围。'
            elif operation == 'keep':
                note = '保留这里的原文。'
            elif operation == 'verify':
                note = '这里需先核实原始记录，再填写实际修改文字；目前不提供可直接替换的定稿。'
            elif operation == 'formatting':
                note = '按建议调整这里的 LaTeX 格式。'
            else:
                note = '按下方建议替换这里的原文。'
            if asset:
                note = '先制作图像副本并核对；下方是图中文字与布局建议。'
            elif quote.strip().startswith('\\caption{') and loc.get('proposedEnglish') and not loc['proposedEnglish'].lstrip().startswith('\\caption{'):
                note = '只替换 \\caption{…} 内的英文，保留 LaTeX 命令与花括号。'
            elif loc.get('locationId')=='R1-13-midi-header':
                note = '只更换表头英文，保留 &、\\textbf{…} 和表格列结构。'
            normalized = {'key': loc.get('location_id', loc.get('locationId')), 'file': relative,
                          'lineStart': start, 'lineEnd': end, 'quote': quote,
                          'before': ''.join(lines[max(0, start-4):start-1]),
                          'after': ''.join(lines[end:min(len(lines), end+3)]),
                          'operation': operation, 'section': re.sub(r'，第[0-9—\-]+行(?:（此后补充）)?', '', section or relative),
                          'note': note, 'sourceSha256': sources[relative]['sha256'],
                          'role': loc.get('role',loc.get('assistant_disposition')), 'asset': asset, 'baseline': 'current-repository-source',
                          'sharedEditId': loc.get('sharedEditId',loc.get('location_id',loc.get('locationId'))),
                          'sharedWith': loc.get('relatedCommentIds',loc.get('shared_or_synchronous_ids', [])),
                          'independentlyOptional': loc.get('independentlyOptional',False),
                          'selectedForDefaultRoute': loc.get('defaultIncludedInRecommendedAction',True),
                          'primaryOperation': loc.get('locationId') in item.get('recommended_route',{}).get('primary_operation_ids',[]),
                          'operationOwner': loc.get('ownerCommentId',loc.get('operation_owner_comment', cid)),
                          'audit': loc}
            # Exact duplicate source operations add no information to the UI.
            identity = (relative, start, end, quote, operation, loc.get('proposedEnglish',loc.get('proposed_english', loc.get('proposedText'))))
            if any(l.get('_identity') == identity for l in locations):
                continue
            normalized['_identity'] = identity
            i = len(locations)
            locations.append(normalized)
            proposed = loc.get('proposedEnglish',loc.get('proposed_english', loc.get('proposedText')))
            if proposed is not None and operation not in {'keep','verify'}:
                proposals.append({'id': normalized['key'], 'locationIndex': i, 'operation': operation,
                                  'text': proposed, 'source': loc.get('proposalEvidence',loc.get('proposal_origin'))})
        for loc in locations:
            loc.pop('_identity')
        replies = item['author_prefill_evidence']['actual_replies']
        provenance = [{'path': report['source_pdf'], 'pdfPage': r['pdf_page'],
                       'annotationId': r['annotation_id'], 'quote': r['exact_quote'],
                       'pdfSha256': report['sha256']} for r in replies]
        original = item['original_order']
        report_label = original.get('legacy_transcription_label')
        if report_label:
            report_label = '报告 ' + report_label
        elif original.get('section') == 'Preamble':
            report_label = '报告前言'
        elif item['reviewer_id'] == 'R1':
            report_label = '报告引言'
        else:
            report_label = f'报告意见 {item["sequence_in_report"]}'
        normalized_item = {'id': cid, 'reviewer': item['reviewer_id'],
                           'reportOrder': item['sequence_in_report'], 'reportLabel': report_label,
                           'title': item['reviewer_question_zh'], 'original': item['reviewer_comment']['text'],
                           'meaning': item['reviewer_question_zh'],
                           'report': {'path': report['source_pdf'], 'page': item['reviewer_comment']['pdf_page'],
                                      'label': report['display_name'], 'sha256': report['sha256'], 'originalOrder': original},
                           'authorReply': {'text': '\n\n'.join(r['exact_quote'] for r in replies),
                                           'displayText': item.get('author_reply_display_text'),
                                           'sources': provenance, 'decision': decision(item['author_decision_seed']),
                                           'prefill': item['author_decision_seed'] != 'pending',
                                           'reason': item['author_reply_summary_zh']},
                           'assistant': {'decision': decision(item['assistant_decision']),
                                         'reason': item['assistant_rationale_zh']},
                           'recommendation': ('建议不改：' if decision(item['assistant_decision']) == 'keep' else '建议改：') + item['recommended_action_zh'],
                           'locations': locations, 'proposals': proposals,
                           'evidencePending': [],
                           'pendingEvidenceDetails': item.get('pending_evidence', []),
                           'rawAudit': item,
                           'auditItem': cid}
        binding = {'recommendation': normalized_item['recommendation'], 'assistant': normalized_item['assistant'],
                   'locations': [{k: l[k] for k in ['file', 'quote', 'operation']} for l in locations],
                   'proposals': proposals}
        normalized_item['candidateVersion'] = 'recommendation-' + digest(json.dumps(binding, ensure_ascii=False, sort_keys=True).encode())[:24]
        correction=display_corrections.get(cid)
        if correction:
            assert correction['author_decision_seed']==item['author_decision_seed']
            normalized_item['authorReply']['stance']=correction['author_reply_summary_zh']
            scopes=[]
            for sub in correction.get('author_subpart_decisions',[]):
                native=next(r for r in replies if r['annotation_id']==sub['annotation_id'])
                assert sub['exact_quote'] in native['exact_quote']
                scopes.append({**sub,'decision':decision(sub['decision']),'label':'不扩展当前项目','version':'scope-'+digest(json.dumps(sub,sort_keys=True,ensure_ascii=False).encode())[:24]})
            normalized_item['authorReply']['scopedDecisions']=scopes
        comments.append(normalized_item)
    result = {'schemaVersion': 1, 'documentId': 'zhanh-he-phd-thesis-review',
              'edition': 'Reviewer revision workbench · 2026-11-01',
              'manuscript': {'title': 'Recovering Musical Dynamics for Expressive Automatic Music Transcription', 'owner': 'ZHANHONG HE · PHD THESIS'},
              'reviewRoundId': 'phd-examiner-reports-2026',
              'referenceLinks': [{'label': '历史只读 reader', 'path': 'revision_workshop_20261031_v5/reader/index.html'}],
              'reviewers': [{'id': r['id'], 'displayName': r['display_name'], 'shortName': ('1 · Benetos' if r['id']=='R1' else '2 · 奥克兰大学教授')} for r in audit['reports']],
              'sourceBaseline': {'label': 'b2995d0 当前仓库源码；报告 PDF 页码与论文页码分开',
                                 'gitCommit': 'b2995d0aa9ddcb47532a47bcd326f6200fc7b12a',
                                 'auditedEvidenceSha256': digest(raw)},
              'comments': comments, 'sources': sources}
    (HERE / 'evidence' / 'author_decision_evidence.json').write_bytes(raw)
    if recheck:
        assert recheck['audit_status']=='complete'
        (HERE / 'evidence' / 'author_prefill_recheck_v2.json').write_bytes(recheck_path.read_bytes())
        recheck_md=recheck_path.with_suffix('.md')
        if recheck_md.is_file():(HERE / 'evidence' / recheck_md.name).write_bytes(recheck_md.read_bytes())
    audit_md = source.with_name('source_location_audit.md')
    if audit_md.is_file():
        (HERE / 'evidence' / 'source_location_audit.md').write_bytes(audit_md.read_bytes())
    (HERE / 'data.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('audit', type=Path)
    args = parser.parse_args()
    result = integrate(args.audit)
    print(f'Integrated {len(result["comments"])} comments, {sum(len(c["locations"]) for c in result["comments"])} exact source locations')
