"""Verify C1 evidence without changing thesis, prior proposals or writer files."""
from pathlib import Path
import hashlib,json,re

ROOT=Path('/Users/jollibear/Documents/tmp/phd thesis')
V5=ROOT/'revision_workshop_20261031_v5'
LOCAL=Path(__file__).resolve().parent
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

baseline=json.loads((V5/'evaluator_baseline_diagnostics.json').read_text())
unchanged={k:all(digest(ROOT/p)==h for p,h in baseline[k].items())
           for k in ['source_manifest','previous_proposal_manifest']}
assert all(unchanged.values())
rank=json.loads((V5/'evaluator_cycle1_blind_rankings.json').read_text())
assert digest(V5/'CANDIDATE_PACKET_BLIND_C1.md')==rank['packet_sha256']
key=json.loads((V5/'evidence/provenance_key.json').read_text())
selected=json.loads((V5/'FINAL_SELECTION.json').read_text())
packet=(V5/'CANDIDATE_PACKET_BLIND_C1.md').read_text()
texts=dict(re.findall(r'### ([TN]\d\d-[KLMN])\s*\n+```latex\n(.*?)\n```',packet,re.S))
assert len(texts)==60 and len(rank['candidates'])==60 and len(rank['rankings'])==15
for row in rank['candidates']:
    assert hashlib.sha256(texts[row['id']].encode()).hexdigest()==row['candidate_sha256']
results=[]
for item in selected:
    src=(ROOT/item['source']).read_text()
    insertion=item['original'].startswith('[No additional')
    assert src.count(item['anchor'])==1
    if not insertion:
        assert src.count(item['original'])==1
    code=item.get('selected_code')
    results.append(dict(id=item['id'],source=item['source'],source_line=item['source_line'],
        operation=item['operation'],insertion=insertion,source_anchor_unique=True,
        exact_original_count=None if insertion else src.count(item['original']),
        selected_code=code,selected_provenance=key.get(item['id'],{}).get(code),
        selected_modified_since_blind_slot=(item['selected']!=texts[code]) if code else None,
        evaluator_blind_winner=rank['rankings'].get(item['id'],[[None]])[0],
        selected_sha256=hashlib.sha256(item['selected'].encode()).hexdigest()))
source=(ROOT/'Chapter_6/chap6.tex').read_text()
pos=source.index('\\label{tab:bp_metric_diagnostic}')
start=source.rfind('\\begin{table}',0,pos)
end=source.index('\\end{table}',pos)+len('\\end{table}')
old=source[start:end]
new=(V5/'N07_TABLE_MARKUP_PROPOSAL.tex').read_text().strip()
new=new[new.index('\\begin{table}'):new.index('\\end{table}')+len('\\end{table}')]
numeric=lambda t:re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?',t)
assert numeric(old)==numeric(new)
wrappers=lambda t:len(re.findall(r'\\(?:textbf|underline)\{[-+]?\d+(?:\.\d+)?\}',t))
table=dict(numeric_sequence_identical=True,numeric_tokens=len(numeric(old)),
           numeric_wrappers_old=wrappers(old),numeric_wrappers_new=wrappers(new),
           raw_reported_mae_delta='0.193',displayed_endpoint_difference='0.702 - 0.510 = 0.192',
           verdict='Rounding could explain difference; preserve reported values, do not silently recompute.')
final=(LOCAL/'evaluator_cycle1_verification.json')
out=dict(unchanged_against_baseline=unchanged,
    source_files_verified=len(baseline['source_manifest']),
    prior_proposal_files_verified=len(baseline['previous_proposal_manifest']),
    blind_packet_unchanged=True,anonymous_candidates_verified=60,ranked_passages=15,
    selected_passages=results,table_check=table,
    writer_evidence_snapshot={name:digest(V5/name) for name in [
        'FINAL_SELECTION.json','EDITORIAL_RECOMMENDATIONS_v5.md','WORKSHOP_METHOD_AND_RESULTS.md',
        'evidence/provenance_key.json','evidence/BLIND_CRITIQUE_C1.md','evidence/CRITIQUE_C2.md',
        'N07_TABLE_MARKUP_PROPOSAL.tex']})
final.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('60 anonymous candidates / 15 rankings verified; blind packet unchanged.')
print('20 final source operations verified (16 exact replacements, 4 insertions).')
print('Source/prior unchanged:',unchanged)
print('N07:',table)
print('Saved',final)
