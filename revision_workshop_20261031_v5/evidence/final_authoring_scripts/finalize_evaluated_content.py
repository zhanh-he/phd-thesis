from pathlib import Path
import copy,difflib,hashlib,json,re
root=Path('/Users/jollibear/Documents/tmp/phd thesis');v5=root/'revision_workshop_20261031_v5';out=Path(__file__).resolve().parent
verdict=json.loads((v5/'evaluator_cycle2_verdict.json').read_text());selected=json.loads((v5/'FINAL_SELECTION_R2.json').read_text());deps=json.loads((v5/'evaluator_cycle2_dependencies_corrected_proposal.json').read_text());olddeps=json.loads((v5/'DEPENDENCIES_R2.json').read_text());m=json.loads((v5/'evidence/R2_context_operation_manifest.json').read_text());oldops=m['operations'];ops=copy.deepcopy(oldops)
reviewed={k:hashlib.sha256((v5/k).read_bytes()).hexdigest() for k in verdict['reviewedInputSnapshot']}
assert reviewed==verdict['reviewedInputSnapshot'],'R2 frozen input changed after external C2'
selected_changed=[x['id'] for x in selected if hashlib.sha256(x['selected'].encode()).hexdigest()!=verdict['acceptedSelectedTextSha256'][x['id']]];assert not selected_changed
files=sorted(set(o['file'] for o in ops));src={f:(root/f).read_text() for f in files}
for p in verdict['reviewedSourceProvenance']:assert hashlib.sha256((root/p['path']).read_bytes()).hexdigest()==p['sha256']
# Acknowledge exact evaluated source-range repair; only status metadata changes.
dep=next(d for d in deps if d['id']=='V4-R2-04-sync-3');s=src[dep['file']];assert s.count(dep['old'])==1;op=next(o for o in ops if o['id']==dep['id']);op.update(start=s.index(dep['old']),end=s.index(dep['old'])+len(dep['old']),new=dep['new'])
for d in deps:d['status']='writer/evaluator agreed for author choice; author-unapproved; not implemented'
(out/'DEPENDENCIES_REVIEWED_v5.json').write_text(json.dumps(deps,ensure_ascii=False,indent=2))
# Adopt evaluator's exact table artifact byte-for-byte, including unchanged values.
corrected_table_file=v5/'evaluator_cycle2_N07_corrected_proposal.tex';table_artifact=corrected_table_file.read_bytes();assert hashlib.sha256(table_artifact).hexdigest()==verdict['correctedProposalArtifactSha256'][corrected_table_file.name]
(out/'N07_TABLE_MARKUP_REVIEWED_v5.tex').write_bytes(table_artifact)
text=table_artifact.decode();table=text[text.index('\\begin{table}'):text.index('\\end{table}')+len('\\end{table}')]
op=next(o for o in ops if o['id']=='N07');op['new']=table
semantic=lambda o:(o['file'],o['start'],o['end'],o['new'],o['kind'])
changed=[o['id'] for o,p in zip(ops,oldops) if semantic(o)!=semantic(p)];assert set(changed)=={'V4-R2-04-sync-3','N07'} and len(changed)==2
# Rebuild from source only, never write a manuscript copy or compile it.
assembled={};positions={};overlap=[]
for f,s in src.items():
 oo=sorted([o for o in ops if o['file']==f],key=lambda x:(x['start'],x['end']))
 for a,b in zip(oo,oo[1:]):
  if b['start']<a['end']:overlap.append([f,a['id'],b['id']])
 for o in oo:
  shift=sum(len(p['new'])-(p['end']-p['start']) for p in oo if p['end']<=o['start'] and p['id']!=o['id']);positions[o['id']]={'start':o['start']+shift,'end':o['start']+shift+len(o['new'])}
 for o in reversed(oo):s=s[:o['start']]+o['new']+s[o['end']:]
 assembled[f]=s
assert len(ops)==44 and not overlap
virtual_hash={f:hashlib.sha256(s.encode()).hexdigest() for f,s in assembled.items()};assert virtual_hash==verdict['correctedVirtualOverlaySha256'],(virtual_hash,verdict['correctedVirtualOverlaySha256'])
oldtable=next(o['new'] for o in oldops if o['id']=='N07');tokens=lambda s:re.findall(r'(?<![A-Za-z_])[-+]?\d+(?:\.\d+)?',s)
assert tokens(oldtable)==tokens(table) and len(tokens(table))==58
assert '$\\Delta$ (GT $-$ Flat) $\\uparrow$' not in table
# Final contexts have a single current field; remove stale frozen preview fields
# so adapters cannot accidentally use earlier prose.
for x in selected:
 for field in ['reinserted_context','reinserted_context_r2','context_state','context_dependency_ids']:x.pop(field,None)
 s=assembled[x['source']];t=positions[x['id']]
 if x['id'] in ['N01','N02','N03']:a=s.index('\\subsection{Why Pearson');b=s.index('\\subsection{When Diff-Synth',a);context=s[a:b].strip()
 elif x['id']=='T03':a=s.index('MIDI velocity completion sits at the intersection');b=s.index('\\subsection{MIDI Segmentation}',a);context=s[a:b].strip()
 elif x['id']=='T08':a=s.index('\\section{Thesis Organisation}');context=s[a:].strip()
 elif x['id'] in ['N05a','N05c']:a=s.index('\\section{Limitations and Scope}');b=s.index('\\section{Future Research Directions}',a);context=s[a:b].strip()
 else:
  a=max(0,s.rfind('\n\n',0,max(0,t['start']-1)));a=max(0,s.rfind('\n\n',0,max(0,a-1)));b=s.find('\n\n',t['end']);b=len(s) if b<0 else b;b2=s.find('\n\n',b+2);b=b2 if b2>=0 else len(s);context=s[a:b].strip()
  if len(context)>6500:context=s[max(0,t['start']-1200):min(len(s),t['end']+1800)].strip()
 assert assembled[x['source']].count(context)==1
 x['reinserted_context_final']=context;x['context_dependency_ids_final']=[d['id'] for d in deps if d['file']==x['source'] and d['new'] and d['new'] in context];x['review_status']='writer/external evaluator agreed for author choice; not author approved or implemented';x['context_state_final']='20 reviewed selected passages + N07 + 23 explicit author-unapproved dependencies; proposed virtual combination only';x['previousSelectionPath']='FINAL_SELECTION_R2.json'
(out/'FINAL_SELECTION_REVIEWED_v5.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2))
# Exact-source final reading / reviewer packets.
intro=['# 可供选择的最终文字：原文、英文提案与连读语境\n','这些文字的解释更具体，少重复和防御语气；原本清楚的图注、听测稿和技术细节保留。**thesis正文未动，作者尚未批准。**\n','组合语境仅演示20项选文、N07和23项已列明依赖；不是44项执行决定清单，不表示43项评审事项全部关闭。旧YES不继承，KEEP单项不自动批准其他范围。\n','当前LaTeX是工作坐标，正式送审PDF仍待确认。来源、事实待核和准确范围见[共同复核记录](FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md)与[依赖清单](DEPENDENCIES_REVIEWED_v5.json)。\n']
lines=[]
for x in selected:
 lines.append(f'<a id="{x["id"].lower()}"></a>\n\n## {x["id"]} · `{x["source"]}:{x["source_line"]}`\n\n范围：{x["operation"]}\n')
 if x['original'].startswith('[No additional'):lines.append('原有段落保留；此项是新增解释，下面的完整连读显示插入位置。\n')
 else:lines.append('准确原文：\n```latex\n'+x['original']+'\n```\n')
 lines.append('提案英文：\n```latex\n'+(x['selected'] or '[删除该句，不加新句]')+'\n```\n')
 lines.append('<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>\n\n```latex\n'+x['reinserted_context_final']+'\n```\n\n</details>\n')
 if x['context_dependency_ids_final']:lines.append('此处预览带入：'+', '.join(x['context_dependency_ids_final'])+'。\n')
lines.append('## N07：指标表格式\n\n[准确表格副本](N07_TABLE_MARKUP_REVIEWED_v5.tex)。移除跨指标数值best/second-best强调，并删掉GT−Flat共用向上箭头；58个数值token及其顺序完全保留。不从舍入端点重算0.193。\n')
finalmd='\n'.join(intro+lines);(out/'FINAL_PASSAGES_REVIEWED_v5.md').write_text(finalmd);(out/'CANDIDATE_PACKET_FINAL_v5.md').write_text(finalmd.replace('# 可供选择的最终文字：原文、英文提案与连读语境','# Writer/evaluator final reviewed packet — author choice only',1))
# Final reader data: author-facing summaries; reviewed English stays identical.
reader=json.loads((v5/'WRITER_READER_PACKET_R2.json').read_text());by={x['id']:x for x in selected};base='revision_workshop_20261031_v5/'
reader['edition']='论文修改精选 · 可供选择';reader['packetStatus']='jointly-reviewed-v5';reader['versionNotice']='以下是共同复核后的修改提案；正文未动，也不表示作者已批准。浏览选择不保存，不写入DECISIONS。';reader['contextDependenciesFile']=base+'DEPENDENCIES_REVIEWED_v5.json';reader['finalSelectionFile']=base+'FINAL_SELECTION_REVIEWED_v5.json';reader['contextField']='reinserted_context_final';reader['contextAssumptions']='Full contexts combine 20 reviewed selected proposals, corrected N07 and 23 explicitly listed dependencies; author approval and implementation remain separate.'
reader['reviewAgreement']={'writerFile':base+'FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md','externalCycle1':base+'evaluator_cycle1.md','externalCycle2':base+'evaluator_cycle2.md','verdict':base+'evaluator_cycle2_verdict.json','exactCorrectionsAcknowledged':['V4-R2-04-sync-3','N07'],'selectedTextHashesMatchVerdict':True,'correctedOverlayHashesMatchVerdict':True,'scope':'20 selected texts, 23 declared dependency texts including corrected source range, and exact corrected N07; agreed for author choice only. Six reader cards are a read-only selection, not executable approval.','authorApproval':False,'sourceImplementation':False,'runOrGTVerificationCompleted':False,'readerUiVerification':'pending final integrator; old five-card tests do not certify this packet'}
summaries={
'T11':('解释为何使用Huber，同时保留尚未证实优于MAE的边界。','公式和参数保留；不把未证实优势写成从未做过比较。'),
'N01':('保留数字，分清指标用途与表格支持的结论。','不同指标的gap不能单独判断sensitivity；换SoundFont测试的是renderer整体变化。'),
'T03':('说明piano roll与二维U-Net的对应关系。','regular grid保留同时发声和局部pitch–time关系；colourisation是补velocity的类比。'),
'T01':('区分力度被简化的数据与缺少可靠标签的学习条件。','写清note content and timing，保留两种条件可重叠的含义。'),
'N05a':('保留研究范围，只删替论文辩护的句子。','boundaries原首句保留；具体范围和未来方向不删。'),
'KEEP-FIG62':('保留已经交代清楚的原图注。','原文已写明teacher targets来自SoundFont-rendered audio，无需再扩四句。')}
for c in reader['cards']:
 id=c['id'];c['short'],c['why']=summaries[id];c['reviewStatus']='共同复核，可供选择；未批准／未实施';c['recommendationLabel']='编辑推荐';c['pending']='正式送审基线及相关事实仍待核；旧YES不继承。';c['reviewFile']=base+'FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md';c['candidateFile']=base+'FINAL_PASSAGES_REVIEWED_v5.md' if id!='KEEP-FIG62' else base+'AUTHOR_READING_GUIDE_v5.md';c['optionNotes']='仅供只读比较；此处的浏览选择不构成批准，也不会保存。';c.pop('contextDependencyIds',None)
 if id in by:
  c['contextPreview']=by[id]['reinserted_context_final'];c['contextDependencyIdsFinal']=by[id]['context_dependency_ids_final'];c['contextPreviewState']='proposed combination with explicitly named dependencies; no implementation'
 if id=='N01':
  newtext='\n\n'.join(by[k]['selected'] for k in ['N01','N02','N03']);opt=next(o for o in c['options'] if o['id']==c['recommended']);opt.update(id='REVIEWED',label='推荐稿',fullText=newtext,focusText=newtext);c['recommended']='REVIEWED';ft=next(f for f in c['followthrough'] if f['file']=='Chapter_6/chap6.tex');ft['new']=table;c['scope']='五范围一致性组：N01/N02/N03三个解释段、N07表格格式、N04背景从句；其余上下文依赖另行选择。'
 elif id in by:
  opt=next(o for o in c['options'] if o['id']==c['recommended']);opt.update(id='REVIEWED',label='推荐稿',fullText=by[id]['selected'],focusText=by[id]['selected']);c['recommended']='REVIEWED'
 if id=='N05a':
  c.pop('followthrough',None);c['scope']='只保留本段首句并删除后续防御句。N05b/c是独立可选小修，不因查看本卡自动采用。';c['independentOptionalPassages']=[{'id':i,'path':base+'FINAL_PASSAGES_REVIEWED_v5.md#'+i.lower()} for i in ['N05b','N05c']]
 if id=='KEEP-FIG62':c['candidateAnchor']='keep-list';c['scope']='KEEP原caption／图；不因此确认Fig6.3 GT来源。'
reader['provenance']=verdict['reviewedSourceProvenance']
# Hash-binding outputs are emitted below; no self-referential packet hash.
(out/'READER_PACKET_REVIEWED_v5.json').write_text(json.dumps(reader,ensure_ascii=False,indent=2))
manifest={'operations':ops,'dependencies':deps,'overlaps':overlap,'assembled_preview_only':True,'only_changed_operation_ids':changed,'selectedTextChangesFromR2':selected_changed,'virtual_overlay_sha256':virtual_hash,'authorApproval':False,'sourceImplementation':False}
(out/'evidence/FINAL_OPERATION_MANIFEST_v5.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
# Exact R2->final virtual diff, comparable to evaluator-owned diff.
diffs=[]
for f in files:
 s=src[f]
 for o in sorted([o for o in oldops if o['file']==f],key=lambda o:(o['start'],o['end']),reverse=True):s=s[:o['start']]+o['new']+s[o['end']:]
 if s!=assembled[f]:diffs+=list(difflib.unified_diff(s.splitlines(),assembled[f].splitlines(),fromfile='R2-preview/'+f,tofile='reviewed-final-preview/'+f,lineterm=''))
(out/'evidence/FINAL_TWO_REPAIRS_v5.diff').write_text('\n'.join(diffs)+'\n')
check={'exactly_two_operation_changes':changed,'operation_count':len(ops),'zero_overlaps':not overlap,'all_20_selected_hashes_match_external_C2':not selected_changed,'table_numeric_tokens':len(tokens(table)),'table_numeric_sequence_unchanged':tokens(table)==tokens(oldtable),'all_eight_virtual_hashes_match_external_C2':virtual_hash==verdict['correctedVirtualOverlaySha256'],'R2_frozen_hashes_unchanged':reviewed==verdict['reviewedInputSnapshot'],'source_hashes_match_external_C2':True,'source_writes':False,'old_outputs_overwritten':False,'author_approval':False}
(out/'evidence/FINAL_WRITER_VERIFICATION_v5.json').write_text(json.dumps(check,ensure_ascii=False,indent=2));print(json.dumps(check,ensure_ascii=False))
