from pathlib import Path
import re, json, hashlib, difflib
root=Path('/Users/jollibear/Documents/tmp/phd thesis')
paths=[root/'Chapter_1/Intro.tex',root/'Chapter_2/Background.tex']+[root/f'Chapter_{i}/chap{i}.tex' for i in range(3,7)]+[root/'Chapter_7/Conclusion.tex']
patterns={'renderer_conditioned':r'renderer[ -]conditioned','physical_gesture':r'physical (?:measurement|gesture|truth)','structural_preservation':r'(?:preserv\w*|without (?:changing|rewriting)).{0,90}(?:note|timing)','controlled_setting':r'most controlled|most constrained|tightly constrained','image_colourisation':r'image.colouri[sz]ation','thesis_question':r'(?:central|thesis|broader).{0,30}(?:question|objective|stance)'}
report={'scope':'Current seven chapter .tex files only; raw-source lexical matches. These are diagnostics, not quality scores.','files':[],'matches':{}}
for p in paths:
 t=p.read_text()
 entry={'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':len(p.read_bytes()),'lines':len(t.splitlines())}
 report['files'].append(entry)
 for name,pat in patterns.items():
  hits=[]
  for n,line in enumerate(t.splitlines(),1):
   if re.search(pat,line,re.I):hits.append({'line':n,'text':line})
  report['matches'].setdefault(name,{})[str(p.relative_to(root))]=hits
out=Path(__file__).parent
(out/'source_checks.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
for name,group in report['matches'].items():
 print(name, sum(map(len,group.values())),{k:len(v) for k,v in group.items() if v})
