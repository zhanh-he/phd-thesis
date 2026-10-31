#!/usr/bin/env python3
"""Read-only R2 integrity checks; writes reports only beside this script."""
from pathlib import Path
import hashlib,json,re,datetime,sys
out=Path(__file__).resolve().parent
thesis=Path('/Users/jollibear/Documents/tmp/phd thesis')
v5=thesis/'revision_workshop_20261031_v5'
local=out.parent/'workshop_r2'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
frozen=load(out/'frozen_before_r2.json')
protected=[{'path':r['path'],'exists':Path(r['path']).exists(),'unchanged':Path(r['path']).exists() and sha(Path(r['path']))==r['sha256']} for r in frozen['files']]
request=load(v5/'evaluator_cycle1_post_reveal.json')
old={r['id']:r for r in load(v5/'FINAL_SELECTION.json')}
report={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_files':protected,'all_frozen_unchanged':all(r['unchanged'] for r in protected),'requested_change_ids':[r['id'] for r in request['changes']]}
# Anchor checks against untouched real source, excluding insertion-marker pseudo-originals.
anchors=[];spans={}
for id,r in old.items():
 p=thesis/r['source'];s=p.read_text();original=r.get('original','')
 if original.startswith('['):
  count=s.count(r['anchor']);anchors.append({'id':id,'kind':'insertion_anchor','count':count,'valid':count==1})
 else:
  count=s.count(original);anchors.append({'id':id,'kind':'exact_original','count':count,'valid':count==1})
  if count==1:spans.setdefault(r['source'],[]).append((s.index(original),s.index(original)+len(original),id))
report['source_anchor_checks']=anchors
report['source_replacement_overlaps']=[{'source':source,'ids':[a[2],b[2]]} for source,rows in spans.items() for i,a in enumerate(rows) for b in rows[i+1:] if max(a[0],b[0])<min(a[1],b[1])]
required=['FINAL_SELECTION_R2.json','CANDIDATE_PACKET_R2_FULL_CONTEXT.md','WRITER_REVISION_RESPONSE_R2.md']
report['r2_files']={name:{'local_exists':(local/name).exists(),'shared_exists':(v5/name).exists()} for name in required}
if not (local/required[0]).exists():
 report['status']='PENDING R2 writer files; frozen and source-overlap checks completed.'
else:
 data=load(local/required[0]);newrows=data if isinstance(data,list) else data.get('passages',data.get('selection',[]));new={r['id']:r for r in newrows}
 changed=[id for id in old if id in new and old[id].get('selected')!=new[id].get('selected')]
 report['selected_text_changed_ids']=changed
 expected={r['id'] for r in request['changes']}
 report['exactly_seven_requested_texts_changed']=set(changed)==expected
 report['requested_text_checks']=[{'id':r['id'],'changed':r['id'] in changed,'matches_evaluator_suggestion':new.get(r['id'],{}).get('selected')==r['suggested_text']} for r in request['changes']]
 report['accepted_existing_selected_unchanged']=[{'id':id,'unchanged':id in new and new[id].get('selected')==old[id].get('selected')} for id in request['accept_existing_selected']]
 report['t10_v4_unchanged']=new.get('T10',{}).get('selected')==old['T10']['selected'] and new.get('T10',{}).get('selected_provenance')==old['T10'].get('selected_provenance')
 report['new_ids']=[id for id in new if id not in old]
 for name in required:
  p=local/name;q=v5/name
  if p.exists():report['r2_files'][name]['local_sha256']=sha(p)
  if q.exists():report['r2_files'][name]['shared_sha256']=sha(q)
  if p.exists() and q.exists():report['r2_files'][name]['local_shared_identical']=p.read_bytes()==q.read_bytes()
 table=(v5/'N07_TABLE_MARKUP_PROPOSAL.tex').read_text()
 table=table[table.index('\\begin{table}'):].strip()
 ev=load(v5/'evidence/N07_table_markup_check.json')
 numeric=lambda s:re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?',s)
 report['n07_exact_checked_proposal']=table==ev['proposed'].strip()
 report['n07_numeric_tokens_unchanged']=numeric(table)==numeric(ev['old'])
 report['status']='R2 selection available; semantic/full-context review must be recorded separately.'
(out/'r2_check_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps({k:v for k,v in report.items() if k in ['status','all_frozen_unchanged','requested_change_ids','selected_text_changed_ids','exactly_seven_requested_texts_changed','t10_v4_unchanged','new_ids','source_replacement_overlaps','n07_numeric_tokens_unchanged']},indent=2))
