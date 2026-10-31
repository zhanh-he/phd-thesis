from pathlib import Path
import json,re
root=Path('/Users/jollibear/Documents/tmp/phd thesis');out=Path(__file__).parent;v5=root/'revision_workshop_20261031_v5'
supp=(root/'revision_blueprint_20261031/SUPPLEMENTS_v4.md').read_text().split('## 3. 动机末句')[0]
chunks=re.split(r'^### ',supp,flags=re.M)[1:]
rows=[]
for c in chunks:
 title=c.splitlines()[0];blocks=re.findall(r'```latex\n(.*?)\n```',c,re.S)
 if len(blocks)>=2:old,new=blocks[:2]
 elif len(blocks)==1 and '删除' in title:old,new=blocks[0],''
 else:continue
 rows.append({'id':'Intro-'+title.split(' · ')[0].replace('Intro:','')+'-'+str(len(rows)+1),'group':'SUPPLEMENTS_v4 Intro definition/S3/scope','source':'Chapter_1/Intro.tex','old':old,'new':new})
extra=[
 ('R2-04-abstract','main.tex','the results are validated through cross-dataset objective metrics and a MUSHRA-inspired listening test.','the results are assessed through cross-dataset objective metrics and a MUSHRA-inspired listening test.'),
 ('R2-04-ch3','Chapter_3/chap3.tex','the listening test verifies that the recovered layer changes perceived musical quality.','the listening study provides complementary evidence of greater perceived similarity to the reference on the selected stimuli.'),
 ('R2-04-intro','Chapter_1/Intro.tex','it demonstrates that recovering a decoupled expressive layer on fixed symbolic notes is enough to transform a mechanical MIDI sequence into an expressive performance.','it shows that velocity completion can improve expressive rendering on fixed symbolic notes, supported by objective evaluation and the listening study.'),
 ('R2-04-ch7','Chapter_7/Conclusion.tex','yet the listening test shows a clear improvement over flat and sequence-oriented baselines.','and the listening study supports an improvement over Flat and ConvAE on the selected excerpts.'),
 ('R1-33-ch6-36','Chapter_6/chap6.tex','A waveform or spectral loss therefore spends much of its gradient budget on residual mismatch rather than on velocity-dependent behaviour.','A waveform or spectral loss can be influenced by residual mismatch as well as velocity-dependent behaviour.'),
 ('R1-33-ch6-431a','Chapter_6/chap6.tex','Longer crops give waveform-level objectives more of the underlying timbral mismatch to fit, while parameter-level supervision sees only per-note targets and is therefore much less sensitive to crop length.','The crop-length pattern is consistent with greater exposure of the waveform objective to acoustic mismatch, but the present comparison does not isolate that mechanism.'),
 ('R1-33-ch6-431b','Chapter_6/chap6.tex','This mirrors a long-standing observation in inverse-problem design: a supervision signal that only depends on the latent variable of interest is more stable than a high-dimensional signal that mixes that variable with many nuisance factors.',''),
 ('R1-33-ch6-457a','Chapter_6/chap6.tex','Diff-SFProxy avoids this contamination by treating velocity as the only loudness-shaping degree of freedom, but the choice carries its own cost.','Diff-SFProxy restricts the adapted control to velocity, but this does not remove effects of unobserved controls from the target audio.'),
 ('R1-33-ch6-457b','Chapter_6/chap6.tex','The recovered velocity absorbs effects that, in the real performance, came from other parallel controls.','The recovered velocity may therefore absorb effects that, in the real performance, came from other parallel controls.')]
rows.extend({'id':id,'group':id.split('-ch')[0],'source':source,'old':old,'new':new} for id,source,old,new in extra)
spans={};bad=[]
for r in rows:
 s=(root/r['source']).read_text();r['exact_old_matches']=s.count(r['old']);r['current_source_line']=s[:s.find(r['old'])].count('\n')+1 if r['old'] in s else None
 if r['exact_old_matches']!=1:bad.append(r['id'])
 else:spans.setdefault(r['source'],[]).append((s.index(r['old']),s.index(r['old'])+len(r['old']),r['id']))
for r in json.loads((v5/'FINAL_SELECTION.json').read_text()):
 if r['original'].startswith('['):continue
 s=(root/r['source']).read_text();a=s.index(r['original']);spans.setdefault(r['source'],[]).append((a,a+len(r['original']),r['id']))
overlaps=[{'source':source,'ids':[a[2],b[2]]} for source,rs in spans.items() for i,a in enumerate(rs) for b in rs[i+1:] if max(a[0],b[0])<min(a[1],b[1])]
(out/'named_v4_sync_sources.json').write_text(json.dumps({'status':'Source-only dependency verification; does not implement/approve any change.','count':len(rows),'bad_anchors':bad,'overlaps_with_selected_passages':overlaps,'operations':rows},ensure_ascii=False,indent=2))
print('Named syncs',len(rows),'bad anchors',bad,'overlaps',overlaps)
