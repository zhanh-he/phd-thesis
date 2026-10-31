from pathlib import Path
import json,hashlib
root=Path('/Users/jollibear/Documents/tmp/phd thesis')
checks=[
 ('Chapter_1/Intro.tex','MIDI velocity is a universal loudness variable for all instruments'),
 ('Chapter_1/Intro.tex','large-scale non-piano score-dynamics transcription with human labels'),
 ('Chapter_1/Intro.tex','By intentionally ordering these environments from the tightly constrained to the ambiguous'),
 ('Chapter_3/chap3.tex','This chapter addresses Scenario~S1, the most controlled setting in the thesis map.'),
 ('Chapter_3/chap3.tex','This chapter studied the most controlled form of expressive-label recovery'),
 ('Chapter_4/chap4.tex','MIDI velocity is defined at note onset.'),
 ('Chapter_7/Conclusion.tex','The first method contribution establishes the most controlled setting'),
 ('Chapter_6/chap6.tex',"It does not claim that $V^{\\star}$ recovers the performer's physical gesture.")
]
report=[]
for path,quote in checks:
 t=(root/path).read_text(); hits=[n for n,line in enumerate(t.splitlines(),1) if quote in line]
 report.append({'path':path,'quote':quote,'exact_occurrences':t.count(quote),'source_lines':hits,'unique':len(hits)==1})
Path(__file__).with_name('quote_checks.json').write_text(json.dumps(report,indent=2))
for r in report:print(r['path'],r['source_lines'],'unique=',r['unique'])
assert all(r['unique'] for r in report)
