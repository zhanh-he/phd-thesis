"""Bounded final release checks; only writes evaluator-owned evidence."""
from pathlib import Path
import hashlib,json,re,collections,datetime

ROOT=Path('/Users/jollibear/Documents/tmp/phd thesis')
V5=ROOT/'revision_workshop_20261031_v5'
LOCAL=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
packet_path=V5/'READER_PACKET_REVIEWED_v5.json'
assert sha(packet_path)=='9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17'
verdict=json.loads((V5/'evaluator_cycle2_verdict.json').read_text())
baseline=json.loads((V5/'evaluator_baseline_diagnostics.json').read_text())
for group in ['source_manifest','previous_proposal_manifest']:
 for rel,h in baseline[group].items():assert sha(ROOT/rel)==h,rel
items=json.loads((V5/'FINAL_SELECTION_REVIEWED_v5.json').read_text())
assert len(items)==20
for x in items:
 assert hashlib.sha256(x['selected'].encode()).hexdigest()==verdict['acceptedSelectedTextSha256'][x['id']],x['id']
 assert 'reinserted_context_final' in x
 assert 'reinserted_context' not in x and 'reinserted_context_r2' not in x
deps=json.loads((V5/'DEPENDENCIES_REVIEWED_v5.json').read_text())
corrected=json.loads((V5/'evaluator_cycle2_dependencies_corrected_proposal.json').read_text())
assert len(deps)==23
byid={x['id']:x for x in corrected}
for x in deps:
 for k in ['file','old','new']:assert x[k]==byid[x['id']][k],(x['id'],k)
assert sha(V5/'N07_TABLE_MARKUP_REVIEWED_v5.tex')==sha(V5/'evaluator_cycle2_N07_corrected_proposal.tex')
manifest=json.loads((V5/'evidence/FINAL_OPERATION_MANIFEST_v5.json').read_text())
ops=manifest['operations'];assert len(ops)==44
source={x['file']:(ROOT/x['file']).read_text() for x in ops}
for x in deps:assert source[x['file']].count(x['old'])==1
for x in items:
 if not x['original'].startswith('[No additional'):assert source[x['source']].count(x['original'])==1
old_ops={x['id']:x for x in json.loads((V5/'evidence/R2_context_operation_manifest.json').read_text())['operations']}
changed=[x['id'] for x in ops if any(x[k]!=old_ops[x['id']][k] for k in ['file','start','end','new'])]
assert set(changed)=={'V4-R2-04-sync-3','N07'},changed
overlays={}
for file,s in source.items():
 edits=sorted([x for x in ops if x['file']==file],key=lambda x:(x['start'],x['end']))
 for a,b in zip(edits,edits[1:]):assert a['end']<=b['start'],(a['id'],b['id'])
 for x in reversed(edits):s=s[:x['start']]+x['new']+s[x['end']:]
 overlays[file]=s
assert {f:hashlib.sha256(t.encode()).hexdigest() for f,t in overlays.items()}==verdict['correctedVirtualOverlaySha256']
for x in items:assert x['reinserted_context_final'] in overlays[x['source']],x['id']
table=(V5/'N07_TABLE_MARKUP_REVIEWED_v5.tex').read_text()
table=table[table.index('\\begin{table}'):table.index('\\end{table}')+len('\\end{table}')]
orig=next(x for x in ops if x['id']=='N07')
numbers=lambda s:re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?',s)
assert len(numbers(table))==58 and numbers(table)==numbers(source[orig['file']][orig['start']:orig['end']])
assert '\\textbf{$\\Delta$ (GT $-$ Flat) $\\uparrow$}' not in table
packet=json.loads(packet_path.read_text())
assert packet['packetStatus']=='jointly-reviewed-v5'
agreement=packet['reviewAgreement']
for k in ['authorApproval','sourceImplementation','runOrGTVerificationCompleted']:assert agreement[k] is False
assert set(agreement['exactCorrectionsAcknowledged'])=={'V4-R2-04-sync-3','N07'}
assert len(packet['cards'])==6
for c in packet['cards']:
 s=(ROOT/c['sourceFile']).read_text();assert s.count(c.get('sourceExact',c['originalFull']))==1
 assert any(o['id']=='KEEP' and o['kind']=='keep' for o in c['options'])
 for o in c['options']:assert o['focusText'] in o['fullText']
 for f in c.get('followthrough',[]):assert (ROOT/f['file']).read_text().count(f['old'])==1
 assert not any(j in c['why'] for j in ['接受可选精简','接受实质合并','旧v5与批注相容'])
assert not next(c for c in packet['cards'] if c['id']=='N05a').get('followthrough')
highlights=json.loads((V5/'FINAL_READER_HIGHLIGHTS_v5.json').read_text())
assert len(highlights)==6
frozen={x['id']:x for x in json.loads((V5/'FINAL_SELECTION.json').read_text())}
sel={x['id']:x for x in items}
for h in highlights:
 assert h['after']==sel[h['id']]['selected']
 if h['beforeLabel'].startswith('当前论文'):assert (ROOT/h['source']).read_text().count(h['before'])==1
 else:
  assert 'v4' in h['beforeLabel']
  assert h['before'] in frozen[h['id']]['variants']['V4']
final_inputs=['READER_PACKET_REVIEWED_v5.json','FINAL_SELECTION_REVIEWED_v5.json',
 'DEPENDENCIES_REVIEWED_v5.json','N07_TABLE_MARKUP_REVIEWED_v5.tex',
 'FINAL_READER_HIGHLIGHTS_v5.json','FINAL_PASSAGES_REVIEWED_v5.md',
 'evidence/FINAL_OPERATION_MANIFEST_v5.json','FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md']
delivery=json.loads((V5/'FINAL_DELIVERY_MANIFEST_v5.json').read_text())
for rel,expected in delivery['files'].items():
 assert sha(V5/rel)==expected,rel
template=(V5/'reader/reader_template.html').read_text()
network_storage_apis=['fetch(','XMLHttpRequest','sendBeacon','WebSocket(','localStorage','sessionStorage','indexedDB']
assert not any(s in template for s in network_storage_apis)
assert "connect-src 'none'" in template
index=(V5/'reader/index.html').read_text()
m=re.search(r'<script id="packet" type="application/json">(.*?)</script>',index,re.S)
embedded=json.loads(m.group(1)) if m else {}
out=dict(stage='bounded-final-content-release-verification',passed=True,
 verified_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 packet_sha256=sha(packet_path),exact_two_repairs_verified=changed,
 selected_texts_unchanged=20,dependency_texts_match_evaluator_correction=23,
 scope_operations=44,overlaps=False,numeric_tokens_unchanged=58,
 all_final_contexts_match_corrected_evaluator_overlay=True,
 author_approval=False,source_implementation=False,run_gt_certification=False,
 source_files_unchanged=19,prior_proposal_files_unchanged=80,
 highlights_quote_labels_verified=6,reader_cards=[c['id'] for c in packet['cards']],
 current_source_vs_v4_proposal_labels_exact=True,
 n05bc_not_automatic_followthrough=True,
 delivery_manifest_hashes_verified=len(delivery['files']),
 static_reader_template_network_storage_apis_absent=True,
 static_reader_template_connect_src_none=True,
 reader_index_observed_status=embedded.get('packetStatus'),
 reader_index_observed_cards=[c['id'] for c in embedded.get('cards',[])],
 reader_index_observed_sha256=hashlib.sha256(index.encode()).hexdigest(),
 reader_ui_directly_observed=False,reader_ui_result=None,
 final_input_sha256={name:sha(V5/name) for name in final_inputs},
 ui_stage='Pending direct browser observation; not certified by content checks.')
(LOCAL/'evaluator_release_content_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS: exact final packet hash; two repairs;20 unchanged texts;23 dependencies;44 operations;58 numbers;6 labelled highlights.')
print('PASS: source19/prior80 unchanged; author choice/approval/implementation remain separate.')
print('Current reader index stage:',embedded.get('packetStatus'),[c['id'] for c in embedded.get('cards',[])])
