from pathlib import Path
import re,json,collections
from check_sources import root, paths
out=Path(__file__).parent
paras=[]
for p in paths:
 lines=p.read_text().splitlines()
 for n,line in enumerate(lines,1):
  if len(line)<100 or line.lstrip().startswith(('%','\\','&')):continue
  if '&' in line or '\\\\' in line:continue
  # Approximate plain prose only: retain citation/reference markers as tokens.
  s=re.sub(r'\\(?:cite|ref|label|url)\{[^}]*\}','',line)
  s=re.sub(r'\\[A-Za-z]+\*?(?:\[[^]]*\])?', '', s)
  s=s.replace('~',' ').replace('{','').replace('}','')
  words=re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*",s)
  for sentence in re.split(r'(?<=[.!?])\s+(?=[A-Z])',s):
   count=len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*",sentence))
   if count>=45:paras.append({'path':str(p.relative_to(root)),'line':n,'approx_words':count,'sentence':sentence})
report={'method':'Regex diagnostic on source prose lines; excludes obvious command/table/math lines. Approximate lengths are not readability or quality scores. No sentence is changed automatically.','long_sentence_flags':sorted(paras,key=lambda x:-x['approx_words'])}
(out/'prose_diagnostics.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print('Long-sentence flags >=45 approximate words:',len(paras))
for r in report['long_sentence_flags'][:7]:print(r['path'],r['line'],r['approx_words'],r['sentence'][:190])
grs=root/'revision_blueprint_20261031/GRS_REVISION_REPORT_DRAFT.md'
t=grs.read_text();blocks=[]
for m in re.finditer(r'^> (.+)$',t,re.M):
 header=list(re.finditer(r'^### (R[12]-\d+)',t[:m.start()],re.M))
 blocks.append({'id':header[-1].group(1) if header else 'opening','line':t[:m.start()].count('\n')+1,'text':m.group(1)})
status={'english_quote_blocks':len(blocks),'revision_item_headings':len(re.findall(r'^### R[12]-\d+',t,re.M)),'implementation_claim_flags':[b for b in blocks if re.search(r'\b(?:I|We|we) (?:have|has)\b|\b(?:was|were|has been|have been) (?:revised|added|removed|updated|corrected|checked)\b',b['text'])],'first_person_proposal_count':sum('I propose' in b['text'] for b in blocks),'quote_blocks':blocks}
(out/'grs_status_checks.json').write_text(json.dumps(status,ensure_ascii=False,indent=2))
print('GRS', {k:v for k,v in status.items() if k!='quote_blocks'})
