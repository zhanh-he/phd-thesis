from pathlib import Path
import copy,difflib,hashlib,json,re
root=Path('/Users/jollibear/Documents/tmp/phd thesis');v5=root/'revision_workshop_20261031_v5';out=Path(__file__).resolve().parent
old=json.loads((v5/'FINAL_SELECTION.json').read_text());post=json.loads((v5/'evaluator_cycle1_post_reveal.json').read_text());byid={x['id']:x for x in old}
protected=['FINAL_SELECTION.json','FINAL_PASSAGES_WITH_ORIGINALS.md','EDITORIAL_RECOMMENDATIONS_v5.md','WRITER_READER_PACKET.json','CANDIDATE_PACKET_BLIND_C1.md','CANDIDATE_PACKET_C2_REINSERTED.md','evidence/provenance_key.json','evidence/BLIND_CRITIQUE_C1.md','evidence/CRITIQUE_C2.md','N07_TABLE_MARKUP_PROPOSAL.tex']
protected_hashes={f:hashlib.sha256((v5/f).read_bytes()).hexdigest() for f in protected}
(out/'evidence/protected_writer_before_R2.json').write_text(json.dumps(protected_hashes,indent=2))
new=copy.deepcopy(old);newby={x['id']:x for x in new};changes=[]
reasons={
'T01':'接受。note content and timing逐项对应作者真实定义，比note structure精确，不引入新的数据类别。',
'T03':'接受实质合并。旧稿先说U-Net需二维输入，理由偏循环；现在先交代simultaneous notes与local neighbourhoods如何放到regular grid，再说明binary/single-channel与note-list接口代价。为必要信息接受略长文本，不追求最短。',
'T07':'接受。补on the target recordings，限定未单独测量的对象；不暗示这些合成器从未做过保真评估。',
'T11':'接受可选精简。旧v5与批注相容，并非确定的事实错误；删through a dedicated comparison减少实验史歧义，只保留尚未确立优势。',
'N02':'接受实质意见，整合位置略调整。删去紧邻表格的四个delta，不从舍入端点重算0.193。保留GT notes/velocities不变、rendered sound变化及非gain-only干预。metric purpose移到N03首句，避免相邻两段重复同一句目的说明。',
'N03':'接受目的句写法，并承接N02末句的absolute-level目的。用For label-free guitar evaluation替代therefore；保留piano/two SoundFonts范围及complementary diagnostics，不重新声称优越性。',
'N05a':'接受KEEP原首句。scope boundaries不全等于缺陷；只删后面的防御句，原分类不变。'}
for c in post['changes']:
 id=c['id'];assert c['current_selected_text']==byid[id]['selected'],(id,'frozen text mismatch')
 text=c['suggested_text']
 if id=='N02':text='Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.'
 if id=='N03':text='For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement while reducing dependence on absolute level. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.'
 x=newby[id];x['selected']=text;x['revision']='R2 after external C1';x['external_c1_response']=reasons[id]
 changes.append({'id':id,'decision':'ACCEPT_WITH_INTEGRATION' if id in ['N02','N03'] else 'ACCEPT','reason_zh':reasons[id],'source':x['source'],'source_line':x['source_line'],'before':byid[id]['selected'],'after':text,'suggested_text_from_external':c['suggested_text'],'exact_diff':'\n'.join(difflib.unified_diff(byid[id]['selected'].splitlines(),text.splitlines(),fromfile=f'{id} frozen writer selection',tofile=f'{id} R2 proposal',lineterm=''))})
# Carry forward exact named v4 synchronisations into context previews only.
# Every operation is an unapproved proposal, never an implementation action.
chapfiles=sorted(set(x['source'] for x in new)|{'main.tex'});src={f:(root/f).read_text() for f in chapfiles};deps=[]
def adddep(id,file,oldtext,newtext,origin):
 assert src[file].count(oldtext)==1,(id,'dependency quote',src[file].count(oldtext))
 deps.append({'id':id,'file':file,'line':src[file][:src[file].index(oldtext)].count('\n')+1,'old':oldtext,'new':newtext,'origin':origin,'status':'carried-forward unapproved proposal; preview assumption only'})
supp=(root/'revision_blueprint_20261031/SUPPLEMENTS_v4.md').read_text()
first=supp.split('## 1. 前言定义同步',1)[1].split('## 2. S3与guitar范围',1)[0]
for i,m in enumerate(re.finditer(r'^### Intro:(\d+)[^\n]*\n(.*?)(?=^### |\Z)',first,re.M|re.S),1):
 blocks=re.findall(r'```latex\n(.*?)\n```',m.group(2),re.S);assert len(blocks) in (1,2)
 adddep(f'V4-velocity-{i}','Chapter_1/Intro.tex',blocks[0].strip(),blocks[1].strip() if len(blocks)==2 else '', 'SUPPLEMENTS_v4.md §1')
second=supp.split('## 2. S3与guitar范围',1)[1].split('## 3. 动机末句',1)[0]
for i,m in enumerate(re.finditer(r'^### Intro:(\d+)[^\n]*\n(.*?)(?=^### |\Z)',second,re.M|re.S),1):
 blocks=re.findall(r'```latex\n(.*?)\n```',m.group(2),re.S);assert len(blocks)==2
 adddep(f'V4-scope-{i}','Chapter_1/Intro.tex',blocks[0].strip(),blocks[1].strip(),'SUPPLEMENTS_v4.md §2')
third=supp.split('## 3. 动机末句',1)[1].split('<a id="keep-r1-35">',1)[0]
blocks=re.findall(r'```latex\n(.*?)\n```',third,re.S);assert len(blocks)==2
adddep('V4-motivation','Chapter_1/Intro.tex',blocks[0].strip(),blocks[1].strip(),'SUPPLEMENTS_v4.md §3')
writer=(root/'revision_blueprint_20261031/writer_round3.md').read_text();prior=json.loads((v5/'evidence/prior_candidates.json').read_text())
def section(id):return re.search(r'^## '+id+r' .*?\n(.*?)(?=^## R[12]-|\Z)',writer,re.M|re.S).group(1)
def para(file,start):
 return next(p.strip() for p in src[file].split('\n\n') if start in p)
orig=para('Chapter_3/chap3.tex','This chapter addresses Scenario~S1,')
adddep('V4-S1-opening','Chapter_3/chap3.tex',orig,prior['R1-15']['alternatives']['A'],'writer_round3.md R1-15 A')
for id in ['R1-15','R2-04']:
 for i,m in enumerate(re.finditer(r'- `([^`]+)` line (\d+)\n  - 原：([^\n]+)\n  - 拟：([^\n]+)',section(id)),1):
  adddep(f'V4-{id}-sync-{i}',m.group(1),m.group(3),m.group(4),f'writer_round3.md {id} exact synchronisation')
# Preserve the three complete v4 common paragraphs (five clause actions).
part=section('R1-33');pending=[]
for m in re.finditer(r'- `([^`]+)` line (\d+)\n  - 原：([^\n]+)\n  - 拟：([^\n]+)',part):pending.append((m.group(1),m.group(3),m.group(4)))
for m in re.finditer(r'- `([^`]+)` line (\d+)\n  - 删除原整句：([^\n]+)',part):pending.append((m.group(1),m.group(3),''))
for i,start in enumerate(['Two limitations of waveform-level supervision are relevant here.','Third, the asymmetry between the two adaptation interfaces widens with crop length.','Velocity is not the only MIDI control that shapes rendered dynamics:'],1):
 file='Chapter_6/chap6.tex';original=para(file,start);replacement=original
 for f,a,b in pending:
  if f==file and a in replacement:replacement=replacement.replace(a,b)
 replacement=re.sub(r' {2,}',' ',replacement).strip()
 assert replacement!=original
 adddep(f'V4-R1-33-common-{i}',file,original,replacement,'writer_round3.md R1-33 common three paragraphs / five actions')
assert len(deps)==23,len(deps)
(out/'DEPENDENCIES_R2.json').write_text(json.dumps(deps,ensure_ascii=False,indent=2))
# Locate all operations in original source first, then apply from right to left.
ops=[]
for x in new:
 s=src[x['source']];a=x['original'];b=x['selected']
 if a.startswith('[No additional'):
  if x['id']=='T01':pos=s.index('\\end{quote}',s.index('The thesis is driven by'))+len('\\end{quote}')
  elif x['id']=='T02':pos=s.index('\\end{table}',s.index('\\label{tab:intro_scenarios}'))+len('\\end{table}')
  else:pos=s.index('\n\n',s.index(x['anchor']))
  ops.append({'id':x['id'],'file':x['source'],'start':pos,'end':pos,'new':'\n\n'+b+'\n\n','kind':'insertion'})
 else:
  assert s.count(a)==1,(x['id'],'source quote');pos=s.index(a)
  ops.append({'id':x['id'],'file':x['source'],'start':pos,'end':pos+len(a),'new':b,'kind':'replacement'})
for d in deps:
 s=src[d['file']];pos=s.index(d['old']);ops.append({'id':d['id'],'file':d['file'],'start':pos,'end':pos+len(d['old']),'new':d['new'],'kind':'dependency'})
table=json.loads((v5/'evidence/N07_table_markup_check.json').read_text());s=src['Chapter_6/chap6.tex'];pos=s.index(table['old']);ops.append({'id':'N07','file':'Chapter_6/chap6.tex','start':pos,'end':pos+len(table['old']),'new':table['proposed'],'kind':'replacement'})
assembled={};transforms={};overlaps=[]
for file,s in src.items():
 fileops=sorted([o for o in ops if o['file']==file],key=lambda x:(x['start'],x['end']))
 for a,b in zip(fileops,fileops[1:]):
  if b['start']<a['end']:overlaps.append((file,a['id'],b['id']))
 for o in fileops:
  shift=sum(len(p['new'])-(p['end']-p['start']) for p in fileops if p['end']<=o['start'] and p['id']!=o['id'])
  transforms[o['id']]={'file':file,'start':o['start']+shift,'end':o['start']+shift+len(o['new'])}
 text=s
 for o in reversed(fileops):text=text[:o['start']]+o['new']+text[o['end']:]
 assembled[file]=text
assert not overlaps,overlaps
# Scoped contexts are full section neighbourhoods from assembled PROPOSAL text,
# not current-source claims. Source operations and assumptions remain separate.
for x in new:
 t=transforms[x['id']];s=assembled[x['source']]
 if x['id'] in ['N01','N02','N03']:
  start=s.index('\\subsection{Why Pearson');end=s.index('\\subsection{When Diff-Synth',start);context=s[start:end].strip()
 elif x['id']=='T03':
  start=s.index('MIDI velocity completion sits at the intersection');end=s.index('\\subsection{MIDI Segmentation}',start);context=s[start:end].strip()
 elif x['id']=='T08':
  start=s.index('\\section{Thesis Organisation}');context=s[start:].strip()
 elif x['id'] in ['N05a','N05c']:
  start=s.index('\\section{Limitations and Scope}');end=s.index('\\section{Future Research Directions}',start);context=s[start:end].strip()
 else:
  a=s.rfind('\n\n',0,max(0,t['start']-1));a=max(0,a)
  # Include prior and following complete paragraphs, up to modest source context.
  a=s.rfind('\n\n',0,max(0,a-1));a=max(0,a)
  end=s.find('\n\n',t['end']);end=len(s) if end<0 else end
  end2=s.find('\n\n',end+2);end=end2 if end2>=0 else len(s)
  context=s[a:end].strip()
  if len(context)>6500:context=s[max(0,t['start']-1200):min(len(s),t['end']+1800)].strip()
 x['reinserted_context_r2']=context;x['context_state']='R2 selected proposals + 23 explicitly listed v4 dependencies; no source implementation';x['context_dependency_ids']=[d['id'] for d in deps if d['file']==x['source'] and d['new'] and d['new'] in context]
(out/'FINAL_SELECTION_R2.json').write_text(json.dumps(new,ensure_ascii=False,indent=2))
(out/'evidence/R2_exact_changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
# Complete full-context review packet; no hidden historical overwrite.
lines=['# R2：外部C1后实际返修与整段语境\n','阶段：writer response after first external cycle；**等待第二次外部评阅**。不是joint final approval。七处文字返修；其余选稿保持，包括T10的v4胜出。\n','当前LaTeX只作工作坐标；正式送审PDF未定。以下是**组合提案预览**：20项选稿、N07和明确列出的23项v4同步。没有写回源码，没有声明全部43项采用或全文最终一致。KEEP本卡不自动批准/拒绝其他依赖，旧YES不继承。\n','依赖详细原文/拟文：[DEPENDENCIES_R2.json](DEPENDENCIES_R2.json)。继承v4的修复不算本轮新发现。\n']
for x in new:
 lines.append(f'<a id="{x["id"].lower()}"></a>\n\n## {x["id"]} · {x["source"]}:{x["source_line"]}\n\nOperation: {x["operation"]}\n')
 if x['original'].startswith('[No additional'):lines.append('当前此处没有新增解释段；这是插入选择，原有段落保留。\n')
 else:lines.append('准确当前原文：\n```latex\n'+x['original']+'\n```\n')
 lines.append('R2提案英文：\n```latex\n'+(x['selected'] or '[DELETE; insert nothing]')+'\n```\n')
 lines.append('组合提案的完整段落／相邻语境：\n```latex\n'+x['reinserted_context_r2']+'\n```\n')
 if x['context_dependency_ids']:lines.append('本视图包含的v4依赖：'+', '.join(x['context_dependency_ids'])+'。\n')
lines.append('## N07：同组表格格式\n\n表格提案沿用冻结的N07_TABLE_MARKUP_PROPOSAL.tex；58个数字token顺序不变，只去12处跨指标数值强调和相应caption句。不从舍入端点重算delta；0.193保持报告值。\n')
packet='\n'.join(lines)
(out/'CANDIDATE_PACKET_R2_FULL_CONTEXT.md').write_text(packet)
(out/'FINAL_PASSAGES_R2.md').write_text(packet.replace('# R2：外部C1后实际返修与整段语境','# R2精选英文：原文与组合提案语境',1))
# Reader export is a NEW input; it remains blocked from joint-final build until
# actual external-cycle2 agreement exists. No reader-owned file is written.
reader=json.loads((v5/'WRITER_READER_PACKET.json').read_text());reader['edition']='v5 R2 · 外部C1后返修候选';reader['packetStatus']='writer-r2-pending-external-cycle2';reader['versionNotice']='本输入已落实第一次外部评阅的七处返修，仍待第二次外部全文语境复核；禁止冒充jointly-reviewed-v5。';reader['contextAssumptions']='Full-context packet assumes 20 R2 selected proposals, N07 and 23 named v4 dependencies; none are implemented or author-approved.';reader['contextDependenciesFile']='revision_workshop_20261031_v5/DEPENDENCIES_R2.json'
reader['reviewAgreement']={'writerFile':'revision_workshop_20261031_v5/WRITER_REVISION_RESPONSE_R2.md','externalC1':'revision_workshop_20261031_v5/evaluator_cycle1.md','externalPostReveal':'revision_workshop_20261031_v5/evaluator_cycle1_post_reveal.json','scope':'Seven reasoned revisions; N02 metric purpose moved into N03 to avoid adjacent repetition; prior KEEP and inherited v4 syncs retained. External cycle2 pending.','externalCycle2Pending':True,'internalRounds':'Earlier writer-internal C1/C2 kept separate from external assessment.'}
for c in reader['cards']:
 id=c['id'];c['candidateFile']='revision_workshop_20261031_v5/FINAL_PASSAGES_R2.md' if id!='KEEP-FIG62' else 'revision_workshop_20261031_v5/EDITORIAL_RECOMMENDATIONS_R2.md';c['reviewFile']='revision_workshop_20261031_v5/WRITER_REVISION_RESPONSE_R2.md';c['reviewStatus']='外部C1后定点返修；第二次外部评阅待完成';c['recommendationLabel']='R2 writer推荐；待外部C2';c['pending']='提案未实施；外部C2待评阅；正式基线和事实待核项保留；不继承旧YES。'
 if id in newby:
  text=newby[id]['selected'];opt=next(o for o in c['options'] if o['id']=='V5');opt['id']='R2';opt['label']='R2 · 当前返修推荐';opt['fullText']=text;opt['focusText']=text;c['recommended']='R2';c['why']=reasons.get(id,c['why']);c['short']=c['why']
  c['contextPreview']=newby[id]['reinserted_context_r2'];c['contextDependencyIds']=newby[id]['context_dependency_ids']
 if id=='N01':
  text='\n\n'.join(newby[k]['selected'] for k in ['N01','N02','N03']);opt=next(o for o in c['options'] if o['id']=='R2');opt['fullText']=text;opt['focusText']=text
 if id=='KEEP-FIG62':c['candidateAnchor']='keep-list'
# Lossless reader text checks and source proof.
for c in reader['cards']:
 assert c.get('sourceExact',c['originalFull']) in (root/c['sourceFile']).read_text()
 for o in c['options']:assert o['focusText'] in o['fullText']
 for f in c.get('followthrough',[]):assert f['old'] in (root/f['file']).read_text()
(out/'WRITER_READER_PACKET_R2.json').write_text(json.dumps(reader,ensure_ascii=False,indent=2))
(out/'evidence/R2_context_operation_manifest.json').write_text(json.dumps({'operations':ops,'dependencies':deps,'overlaps':overlaps,'assembled_preview_only':True},ensure_ascii=False,indent=2))
# Protected files and real thesis snapshot remain unchanged.
source_before=json.loads((v5/'evidence/source_hashes_before.json').read_text());source_changed=[f for f,h in source_before.items() if hashlib.sha256((root/f).read_bytes()).hexdigest()!=h]
protected_changed=[f for f,h in protected_hashes.items() if hashlib.sha256((v5/f).read_bytes()).hexdigest()!=h]
assert not source_changed and not protected_changed
ver={'revised_ids':[x['id'] for x in changes],'exact_seven_requested_ids':set(x['id'] for x in changes)==set(c['id'] for c in post['changes']),'unchanged_selected_ids':[x['id'] for x in new if x['id'] not in reasons],'T10_frozen_v4_unchanged':newby['T10']['selected']==byid['T10']['selected'],'v4_dependency_count':len(deps),'context_operation_count':len(ops),'overlaps':overlaps,'source_snapshot_files':len(source_before),'source_changed':source_changed,'frozen_writer_changed':protected_changed,'table_numeric_tokens_unchanged':True,'no_source_writes':True,'reader_status':reader['packetStatus']}
(out/'evidence/R2_WRITER_INTEGRITY.json').write_text(json.dumps(ver,ensure_ascii=False,indent=2))
print(json.dumps(ver,ensure_ascii=False))
