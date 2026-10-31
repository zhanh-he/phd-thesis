"""Independently reconstruct proposal contexts in memory; never writes source."""
from pathlib import Path
import json,re,collections,hashlib
out=Path(__file__).parent;local=out.parent/'workshop_r2';root=Path('/Users/jollibear/Documents/tmp/phd thesis');v5=root/'revision_workshop_20261031_v5'
load=lambda p:json.loads(p.read_text())
rows=load(local/'FINAL_SELECTION_R2.json');byid={r['id']:r for r in rows};deps=load(local/'DEPENDENCIES_R2.json');depbyid={r['id']:r for r in deps}
manifest=load(local/'evidence/R2_context_operation_manifest.json');ops=manifest['operations'];table=load(v5/'evidence/N07_table_markup_check.json')
source={op['file']:(root/op['file']).read_text() for op in ops};problems=[];verified=[]
for op in ops:
 id=op['id'];s=source[op['file']];actual=s[op['start']:op['end']]
 if id in byid:
  row=byid[id];expected_old='' if row['original'].startswith('[') else row['original'];expected_new=op['new'] if op['kind']=='insertion' else row['selected']
  if op['kind']=='insertion':
   if op['new'].strip()!=row['selected']:problems.append([id,'insertion text mismatch'])
 elif id in depbyid:expected_old=depbyid[id]['old'];expected_new=depbyid[id]['new']
 elif id=='N07':expected_old=table['old'];expected_new=table['proposed']
 else:problems.append([id,'unknown op']);continue
 valid=actual==expected_old and op['new']==expected_new
 if not valid:problems.append([id,'interval content or replacement mismatch'])
 verified.append({'id':id,'source_interval_matches_exact_original':actual==expected_old,'new_text_matches_named_selection':op['new']==expected_new})
assembled={};overlaps=[]
for file,s in source.items():
 fileops=sorted([o for o in ops if o['file']==file],key=lambda o:(o['start'],o['end']))
 for a,b in zip(fileops,fileops[1:]):
  if a['end']>b['start']:overlaps.append([file,a['id'],b['id']])
 # Build left to right, independently of the writer's right-to-left construction.
 cursor=0;parts=[]
 for op in fileops:parts.extend([s[cursor:op['start']],op['new']]);cursor=op['end']
 parts.append(s[cursor:]);assembled[file]=''.join(parts)
contexts=[]
for row in rows:
 ctx=row['reinserted_context_r2'];text=assembled[row['source']];hits=text.count(ctx)
 declared=row.get('context_dependency_ids',[])
 missing=[id for id in declared if depbyid[id]['new'] not in ctx]
 contexts.append({'id':row['id'],'contiguous_in_independently_assembled_proposal':hits==1,'selected_present_once':ctx.count(row['selected'])==1 if row['selected'] else None,'declared_dependency_ids':declared,'declared_dependencies_missing':missing,'starts_at_full_paragraph_boundary':text.index(ctx)==0 or text[text.index(ctx)-2:text.index(ctx)]=='\n\n'})
 if hits!=1 or missing:problems.append([row['id'],'context/dependency mismatch'])
expected=load(out/'named_v4_sync_sources.json')['operations'];coverage=[]
for r in expected:
 t=assembled[r['source']];ok=r['new'] in t if r['new'] else r['old'] not in t
 coverage.append({'id':r['id'],'expected_named_sync_applied_in_memory':ok})
 if not ok:problems.append([r['id'],'missing named v4 sync'])
# KEEP figure: exact source caption and all image bytes remain protected elsewhere.
s=source['Chapter_6/chap6.tex'];a=assembled['Chapter_6/chap6.tex'];pat=r'\\begin\{figure\}.*?\\end\{figure\}'
find=lambda text:next(f for f in re.findall(pat,text,re.S) if 'encoder-only Transformer' in f)
keepfig=find(s)==find(a)
report={'operation_count':len(ops),'dependency_count':len(deps),'operation_integrity':verified,'source_overlaps':overlaps,'contexts':contexts,'required_named_v4_coverage':coverage,'keep_fig62_exact_figure_environment_unchanged':keepfig,'n07_exact_table_present_in_metric_context':table['proposed'] in byid['N01']['reinserted_context_r2'],'metric_three_contexts_identical':len({byid[id]['reinserted_context_r2'] for id in ['N01','N02','N03']})==1,'problems':problems,'all_checks_passed':not problems and not overlaps and keepfig}
(out/'r2_context_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['operation_integrity','contexts','required_named_v4_coverage']},indent=2))
