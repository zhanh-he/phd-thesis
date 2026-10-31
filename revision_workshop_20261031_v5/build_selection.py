from pathlib import Path
import json,re,hashlib,difflib
root=Path('/Users/jollibear/Documents/tmp/phd thesis');stage=Path(__file__).resolve().parent
items=json.loads((stage/'evidence/tournament_source.json').read_text()); key=json.loads((stage/'evidence/provenance_key.json').read_text())
wins={'T01':'L','T02':'K','T03':'M','T04':'K','T05':'M','T06':'L','T07':'M','T08':'L','T09':'L','T10':'L','N01':'L','N02':'M','T11':'L','N03':'L','N04':'N'}
selected=[]
for x in items:
 code=x['id']+'-'+wins[x['id']];kind=key[x['id']][code];text=x['variants'][kind]
 if x['id']=='T04':text=text.split('. ',1)[1]
 if x['id']=='T09':text='Second, '+text[0].lower()+text[1:]
 if x['id']=='N01':text='Both similarity metrics score GT above flat velocity. Pearson $r$ gives a larger numerical GT--flat gap on BSSL and BSTL in this table, although the gaps are measured on different scales.'
 if x['id']=='N03':text=text.replace('headline measure','main measure').replace(' rather than treated as generally invalid measures','')
 x['selected']=text;x['selected_code']=code;x['selected_provenance']=kind
 selected.append(x)
# Pure small editorial deletions: outside the tournament, explicitly compared by C2.
extras=[
 ('N05a','Chapter_7/Conclusion.tex','The thesis has several boundaries. These boundaries are not artefacts of unfinished implementation; they follow from the problem definition and from the representational choices made throughout the dissertation.','The thesis has several limitations.','删除无必要的审查姿态；不改后文实际限制。'),
 ('N05b','Chapter_7/Conclusion.tex','The results of the thesis suggest several directions for future research. These directions extend the thesis argument rather than repair it.','The results suggest several directions for future research.','未来工作开头无需替论文辩护。'),
 ('N05c','Chapter_7/Conclusion.tex','These assumptions are not weaknesses of the argument. They are the conditions under which label recovery, rather than unconstrained generation, becomes meaningful.','These assumptions define the conditions for the label-recovery tasks studied here.','保留条件含义，删掉不必要的反驳。'),
 ('N06a','Chapter_3/chap3.tex','A plausible explanation is that a 10-second window often captures a musically coherent phrase, for example roughly four measures at 120 BPM, providing enough context without overextending the receptive field.','','保留T=96和5/10/15/20秒实测比较；不以固定秒长推断完整乐句。'),
 ('N06b','Chapter_3/chap3.tex','This is likely because a 10-second segment roughly encompasses four measures at 120 beats per minute (BPM), forming a complete musical phrase that aids in semantic segmentation.','','v4修了小节数，却仍可能留下完整乐句的无依据推断；只保留已报告结果。')]
for id,source,original,new,reason in extras:
 assert (root/source).read_text().count(original)==1,(id,'quote')
 selected.append({'id':id,'related':'optional small deletion','source':source,'anchor':original,'operation':'Replace only this exact text; empty replacement means delete sentence.','original':original,'selected':new,'reason_zh':reason,'selected_provenance':'fresh minimum edit','selected_code':None})
(stage/'evidence/selected_passages_c2.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2))
# Assemble each whole selected source paragraph; adjacent metric edits assembled together.
patches=[]
for x in selected:
 src=(root/x['source']).read_text(); original=x['original'];new=x['selected']
 if original.startswith('[No additional'):
  if x['id']=='T01':
   ix=src.index('\\end{quote}',src.index('The thesis is driven by'))+len('\\end{quote}')
   before=src[max(0,ix-500):ix];after=src[ix:ix+900]
  elif x['id']=='T02':
   ix=src.index('\\end{table}',src.index('\\label{tab:intro_scenarios}'))+len('\\end{table}')
   before=src[max(0,ix-500):ix];after=src[ix:ix+800]
  elif x['id']=='T04':
   orig=x['context_before'];anchor=x['anchor'];start=src.index(anchor);ix=src.index('\n\n',start)
   before=src[max(0,start-800):ix];after=src[ix:ix+800]
  elif x['id']=='T05':
   start=src.index(x['anchor']);ix=src.index('\n\n',start)
   before=src[max(0,start-300):ix];after=src[ix:ix+800]
  result=before+'\n\n'+new+'\n\n'+after
 else:
  assert src.count(original)==1,(x['id'],src.count(original))
  start=src.index(original); pstart=src.rfind('\n\n',0,start)+2;pend=src.find('\n\n',start+len(original));pend=pend if pend>=0 else len(src)
  result=src[max(0,pstart-700):pstart]+src[pstart:pend].replace(original,new)+src[pend:pend+700]
 if x['id'].startswith('N0') and x['id'] in ('N01','N02','N03'):
  result=src[src.index('To test dynamics sensitivity,'):src.index('\\subsection{When Diff-Synth')]
  for y in selected:
   if y['id'] in ('N01','N02','N03'):result=result.replace(y['original'],y['selected'])
 x['reinserted_context']=result
 patches.append(f"## {x['id']} — {x['related']}\n\nSource `{x['source']}`. {x['operation']}\n\nExact original:\n```latex\n{x['original']}\n```\n\nSelected replacement:\n```latex\n{x['selected'] or '[DELETE; insert nothing]'}\n```\n\nFull paragraph / neighbouring context after reinsertion:\n```latex\n{result}\n```\n")
(stage/'CANDIDATE_PACKET_C2_REINSERTED.md').write_text('# Candidate packet — cycle 2\n\nThese are selected-and-revised passages after independent C1. Verify factual/semantic gates first, then source voice, local necessity and whole-paragraph coherence. Reject improvements that create a new claim. T10 is deliberately the retained old candidate; source/provenance is no longer hidden in this cycle. N05/N06 are optional local deletions found by source review, not prior scored tournament winners. Confirm / change / KEEP with concrete reason. Reverse-paraphrase the claim for each disputed passage and identify any delta. No total score.\n\n'+'\n'.join(patches))
# Reproducible local checks, never writes manuscript.
checks=[]
for x in selected:
 s=(root/x['source']).read_text();new=x['selected'];original=x['original']
 checks.append({'id':x['id'],'source':x['source'],'source_occurrences':s.count(original),'insertion':original.startswith('[No additional'),'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'selected_words':len(re.findall(r'\b[\w-]+\b',new)),'original_words':len(re.findall(r'\b[\w-]+\b',original)) if not original.startswith('[No additional') else None,'diff':list(difflib.unified_diff(original.splitlines(),new.splitlines(),fromfile='CURRENT SOURCE',tofile='PROPOSAL ONLY',lineterm=''))})
(stage/'evidence/selected_quote_diff_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
(stage/'evidence/selected_passages_c2.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2))
print(len(selected),'source-scoped proposals; 15 tournament selections + 5 small edits; all non-insertion originals uniquely matched.')
