from pathlib import Path
import re,json,hashlib
root=Path('/Users/jollibear/Documents/tmp/phd thesis')
stage=Path(__file__).resolve().parent
s=(root/'revision_blueprint_20261031/writer_round3.md').read_text()
idx={}
for match in re.finditer(r'^## (R[12]-\d{2}) ([^\n]+)\n(.*?)(?=^## R[12]-|\Z)',s,re.M|re.S):
 id,title,body=match.groups(); d={'title':title,'alternatives':{}}
 for m in re.finditer(r'^### ([ABC])\n(.*?)(?=^### |\*\*评价与推荐\*\*|\Z)',body,re.M|re.S):
  t=m.group(2).strip(); t=t.split('**')[0].strip();d['alternatives'][m.group(1)]=t
 rec=re.search(r'\*\*评价与推荐\*\*：(.*?)(?=\n\n|\Z)',body,re.S)
 d['reason']=rec.group(1) if rec else ''
 idx[id]=d
(stage/'evidence/prior_candidates.json').write_text(json.dumps(idx,ensure_ascii=False,indent=2))
(stage/'evidence/prior_candidates_compact.md').write_text('\n\n'.join(f"## {id} {x['title']}\n"+'\n\n'.join(f"{k}: {v}" for k,v in x['alternatives'].items())+'\n\n'+x['reason'] for id,x in idx.items()))
manifest={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob('Chapter_*/*.tex')}
for f in ['main.tex','main.pdf','Z_He_PhD_Thesis.pdf','README_Preliminary_Report_1.md','README_Preliminary_Report_2.md']:
 p=root/f; manifest[f]=hashlib.sha256(p.read_bytes()).hexdigest()
(stage/'evidence/source_hashes_before.json').write_text(json.dumps(manifest,indent=2))
print('Extracted',len(idx),'comment groups;',sum(len(x['alternatives']) for x in idx.values()),'routes; hashed',len(manifest),'sources')
