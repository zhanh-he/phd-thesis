"""Read-only exact integration verification. Never edits thesis or proposal files."""
from pathlib import Path
import json,re,hashlib,datetime
out=Path(__file__).resolve().parent
root=Path('/Users/jollibear/Documents/tmp/phd thesis');v5=root/'revision_workshop_20261031_v5'
load=lambda p:json.loads(p.read_text());digest=lambda s:hashlib.sha256(s.encode()).hexdigest();filedigest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
frozen=load(out/'frozen_before_final.json');verdict=load(v5/'evaluator_cycle2_verdict.json')
required=['FINAL_SELECTION_REVIEWED_v5.json','DEPENDENCIES_REVIEWED_v5.json','CANDIDATE_PACKET_FINAL_v5.md','READER_PACKET_REVIEWED_v5.json','N07_TABLE_MARKUP_REVIEWED_v5.tex']
report={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_file_count':len(frozen['files']),'frozen_changed':[r['path'] for r in frozen['files'] if not Path(r['path']).exists() or filedigest(Path(r['path']))!=r['sha256']],'files':{name:(v5/name).exists() for name in required}}
if not all(report['files'].values()):
 report['status']='PENDING final versioned artifacts'
 (out/'final_check_results.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2));raise SystemExit(0)
rows=load(v5/required[0]);byid={r['id']:r for r in rows};deps=load(v5/required[1]);depbyid={r['id']:r for r in deps}
report['selected_hashes']=[{'id':id,'matches_external_accepted_sha256':id in byid and digest(byid[id]['selected'])==h} for id,h in verdict['acceptedSelectedTextSha256'].items()]
report['selected_ids_match_external']=set(byid)==set(verdict['acceptedSelectedIds'])
expecteddeps=load(v5/'evaluator_cycle2_dependencies_corrected_proposal.json');report['dependencies_exact_evaluator_corrective_artifact_including_metadata']=deps==expecteddeps
sourcefields=['id','file','line','old','new']
report['dependencies_source_operations_exact_evaluator_correction']=[{k:d[k] for k in sourcefields} for d in deps]==[{k:d[k] for k in sourcefields} for d in expecteddeps]
report['dependency_metadata_changes']=[{'id':a['id'],'changed_fields':[k for k in set(a)|set(b) if a.get(k)!=b.get(k)]} for a,b in zip(deps,expecteddeps) if a!=b]
expectedtable=(v5/'evaluator_cycle2_N07_corrected_proposal.tex').read_text();table=(v5/required[4]).read_text()
report['table_exact_evaluator_corrective_artifact']=table==expectedtable
expectedtable=expectedtable[expectedtable.index('\\begin{table}'):].strip();table=table[table.index('\\begin{table}'):].strip()
oldtable=load(v5/'evidence/N07_table_markup_check.json')['old']
numbers=lambda s:re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?',s)
report['table_numeric_token_count']=len(numbers(table));report['table_numeric_sequence_unchanged']=numbers(table)==numbers(oldtable)
report['gt_flat_shared_up_arrow_removed']=r'\textbf{$\Delta$ (GT $-$ Flat)}' in table and r'\textbf{$\Delta$ (GT $-$ Flat) $\uparrow$}' not in table
baseops=load(v5/'evidence/R2_context_operation_manifest.json')['operations'];ops=[];problems=[]
for b in baseops:
 o=b.copy();id=o['id'];s=(root/o['file']).read_text()
 if id in byid:
  r=byid[id];o['new']='\n\n'+r['selected']+'\n\n' if b['kind']=='insertion' else r['selected']
  if b['kind']!='insertion' and s[b['start']:b['end']]!=r['original']:problems.append([id,'selected source mapping'])
 elif id in depbyid:
  d=depbyid[id]
  if s.count(d['old'])!=1:problems.append([id,'dependency old quote not unique'])
  o['start']=s.index(d['old']);o['end']=o['start']+len(d['old']);o['new']=d['new']
 elif id=='N07':
  o['new']=table
  if s[b['start']:b['end']]!=oldtable:problems.append([id,'table source mapping'])
 else:problems.append([id,'unexpected operation ID'])
 ops.append(o)
report['operation_count']=len(ops)
changed=[o['id'] for o,b in zip(ops,baseops) if o!=b];report['changed_operation_ids']=changed
report['only_two_operations_changed']=set(changed)=={'V4-R2-04-sync-3','N07'}
assembled={};overlaps=[]
for file in {o['file'] for o in ops}:
 source=(root/file).read_text();group=sorted([o for o in ops if o['file']==file],key=lambda x:(x['start'],x['end']))
 for a,b in zip(group,group[1:]):
  if a['end']>b['start']:overlaps.append([file,a['id'],b['id']])
 # Independent left-to-right reconstruction from true sources.
 cursor=0;parts=[]
 for o in group:parts.extend([source[cursor:o['start']],o['new']]);cursor=o['end']
 parts.append(source[cursor:]);assembled[file]=''.join(parts)
report['source_overlaps']=overlaps
report['virtual_overlay_hashes']=[{'file':file,'actual_sha256':digest(s),'matches_external_corrected_overlay':digest(s)==verdict['correctedVirtualOverlaySha256'][file]} for file,s in sorted(assembled.items())]
report['source_hashes']=[{'file':r['path'],'matches_external_reviewed_source':filedigest(root/r['path'])==r['sha256']} for r in verdict['reviewedSourceProvenance']]
# Choose only explicitly FINAL/REVIEWED contexts; never silently use old contexts.
ctxresults=[]
for r in rows:
 keys=[k for k in r if k.startswith('reinserted_context_') and ('final' in k.lower() or 'reviewed' in k.lower()) and isinstance(r[k],str)]
 if len(keys)!=1:
  ctxresults.append({'id':r['id'],'context_keys':keys,'problem':'requires one explicitly final/reviewed context field'});problems.append([r['id'],'missing/ambiguous final context']);continue
 k=keys[0];ctx=r[k];s=assembled[r['source']];present=s.count(ctx)==1
 starts=present and (s.index(ctx)==0 or s[s.index(ctx)-2:s.index(ctx)]=='\n\n')
 selected=r['selected'];once=ctx.count(selected)==1 if selected else True
 ctxresults.append({'id':r['id'],'field':k,'contiguous_in_corrected_overlay':present,'starts_on_full_paragraph_boundary':starts,'selected_text_present_once_or_exact_deletion':once})
 if not (present and starts and once):problems.append([r['id'],'final context integrity'])
report['contexts']=ctxresults
report['problems']=problems
report['status']='CHECKS COMPLETE; manual packet/reader mapping verification still required'
report['all_programmatic_checks_passed']=not report['frozen_changed'] and report['selected_ids_match_external'] and all(x['matches_external_accepted_sha256'] for x in report['selected_hashes']) and report['dependencies_source_operations_exact_evaluator_correction'] and report['table_exact_evaluator_corrective_artifact'] and report['table_numeric_token_count']==58 and report['table_numeric_sequence_unchanged'] and report['gt_flat_shared_up_arrow_removed'] and len(ops)==44 and report['only_two_operations_changed'] and not overlaps and not problems and all(x['matches_external_corrected_overlay'] for x in report['virtual_overlay_hashes']) and all(x['matches_external_reviewed_source'] for x in report['source_hashes'])
(out/'final_check_results.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps({k:v for k,v in report.items() if k not in ['files','selected_hashes','source_hashes','virtual_overlay_hashes','contexts']},indent=2))
