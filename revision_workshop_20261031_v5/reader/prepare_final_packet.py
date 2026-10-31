#!/usr/bin/env python3
"""Create a provisional display adapter; never changes writer or reviewer files."""
import argparse, copy, hashlib, html, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
WORK=HERE.parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=WORK/'READER_PACKET_REVIEWED_v5.json');args=ap.parse_args()
 source=read(args.input);packet=copy.deepcopy(source)
 selected={r['id']:r for r in read(WORK/'FINAL_SELECTION_REVIEWED_v5.json')}
 comments={r['id']:r for r in read(ROOT/'revision_blueprint_20261031/evidence/comment_map.json')}
 packet['packetStatus']='writer-provisional'
 packet['sourcePacketStatus']=source['packetStatus']
 packet['edition']='v5 R2 待 cycle2 复核 · 六处精选预览'
 packet['versionNotice']='v5 最新 R2 提案 · 已按第一轮外部意见返修，第二轮复核尚未确认。v4 只作沿用与对照；新稿请回复 v5 编号，旧 YES 不转移。'
 packet['provisionalNotice']='cycle2尚未确认；先看六处，完整十五组与沿用v4依赖按需展开。'
 packet['reviewAgreement']['parentEvaluatorPending']=True
 packet['mastNote']='只读预览 · v5 R2 待 cycle2'
 packet['purpose']='只读暂定比较。原 index.html 继续展示历史已复核例子；不写作者决定。'
 rows=[];deps={args.input.resolve(),WORK/'FINAL_SELECTION_REVIEWED_v5.json',WORK/'FINAL_PASSAGES_REVIEWED_v5.md',WORK/'AUTHOR_READING_GUIDE_v5.md',WORK/'CANDIDATE_PACKET_BLIND_C1.md',ROOT/'revision_blueprint_20261031/evidence/comment_map.json'}
 legacy={'T11':'R1-34','T03':'R1-17','T01':'R1-05','KEEP-FIG62':'R1-35'}
 for c in packet['cards']:
  cid=c['id'];c['writerScope']=c['scope'];c['writerReviewSummary']=c['reviewerComment'];c['writerAuthorResponseSummary']=c['authorResponse']
  original=(ROOT/c['sourceFile']).read_text();quote=c.get('sourceExact',c['originalFull']);count=original.count(quote)
  if count!=1:raise ValueError(f'{cid}: original quote must match uniquely, found {count}')
  actual_line=original[:original.index(quote)].count('\n')+1
  if actual_line!=c['sourceLine']:raise ValueError(f'{cid}: line mismatch')
  c['reviewStatus']='v5 最新 R2 提案 · cycle2 待确认'
  c['recommendationLabel']='R2 暂定推荐（待 cycle2）'
  # Workflow pending is not a scientific fact blocker. Preserve its exact text separately.
  c['statusNote']=c['pending'];c['pending']=''
  note=c.get('optionNotes','')
  if isinstance(note,str):c['optionNotes']={o['id']:note for o in c['options']}
  c['candidateSourceLabel']='R2 准确提案（待 cycle2）'
  c['decisionNotice']='新 v5 范围尚未写入原决定清单。链接仅供查看历史，旧 YES 不批准本页新稿。'
  c['decisionLinkLabel']='查看原决定清单（历史参考）'
  if cid in legacy:
   lid=legacy[cid];c['legacyDecisionId']=lid
   c['decisionLinkLabel']=f'查看旧清单 · 搜索 {lid}（历史参考）'
   c['reviewerComment']=comments[lid]['comment'];c['authorResponse']=comments[lid]['response']
   c['evidenceKind']='original';c['commentSearchId']=lid
  else:c['evidenceKind']='editorial'
  c['candidateEvidenceByOption']={}
  for o in c['options']:
   if o['kind']=='keep':continue
   if cid=='N01':expected='\n\n'.join(selected[k]['selected'] for k in ['N01','N02','N03']);proof=['FINAL_SELECTION_REVIEWED_v5.json#N01','FINAL_SELECTION_REVIEWED_v5.json#N02','FINAL_SELECTION_REVIEWED_v5.json#N03']
   elif cid=='T03' and o['id']=='GRID':
    expected=selected[cid]['variants']['FRESH_1'];proof=['FINAL_SELECTION_REVIEWED_v5.json#T03.variants.FRESH_1']
    c['candidateEvidenceByOption'][o['id']]={'path':'revision_workshop_20261031_v5/CANDIDATE_PACKET_BLIND_C1.md#t03','label':'GRID 备选原来源'}
   else:expected=selected[cid]['selected'];proof=[f'FINAL_SELECTION_REVIEWED_v5.json#{cid}.selected']
   if o['fullText']!=expected:raise ValueError(f'{cid}/{o["id"]}: candidate differs from final writer selection')
   rows.append({'id':cid,'option':o['id'],'candidateExact':True,'candidateProof':proof})
  if cid=='N01':
   c['scopeNote']='一致性组：Ch6 三个解释段＋N07 表格标记＋Ch2 N04 从句。下方能展开全部五个范围；这里没有批准操作。'
   c['keepScope']='保留本组现有三段解释、N07 表格标记和 Ch2 N04 从句；本组新修正均未采用。'
   c['followthroughLabel']='本组其余两处：N07 表格标记、Ch2 N04 从句'
  if cid=='N05a':
   c['scopeDisplay']='本卡主文本只改结论段引导句；b/c 是下方单独列出的可选小修。具体限制与未来方向保留。'
   c['scopeNote']='这三处小修改可以各自保留。下方列 b/c 供一起阅读，不把对 a 的任何决定扩展给 b/c。'
   c['followthroughLabel']='同类可选小修 b/c · 每处独立审阅'
   c['followthroughIndependent']=True
  if cid=='T01':
   c['navSummary']='新增术语定义，原问题保留。'
   c['baselineNote']='这是新增定义，当前 thesis 的中心问题段保持原样。'
  if cid=='KEEP-FIG62':c['keepScope']='保留 Fig6.2 原图与原图注；不确认 Fig6.3 的 GT 来源。'
  for f in c.get('followthrough',[]):
   fp=ROOT/f['file'];deps.add(fp)
   if fp.read_text().count(f['old'])!=1:raise ValueError(f'{cid}: followthrough source must match uniquely')
   if f['new'] and f['new'] not in (WORK/'FINAL_PASSAGES_REVIEWED_v5.md').read_text() and f['new'] not in (WORK/'N07_TABLE_MARKUP_REVIEWED_v5.tex').read_text():raise ValueError(f'{cid}: followthrough candidate not found')
  for field in ['sourceFile','candidateFile','reviewFile','commentFile']:
   deps.add(ROOT/c[field].split('#',1)[0])
 for v in packet['reviewAgreement'].values():
  if isinstance(v,str) and v.startswith('revision_workshop_') and (ROOT/v).is_file():deps.add(ROOT/v)
 deps.add(WORK/'N07_TABLE_MARKUP_REVIEWED_v5.tex')
 packet['provenance']=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}for p in sorted(deps)]
 # Fifteen tournament items are an optional topic index, not fifteen simultaneous cards.
 groups=[('新发现',['T11','N01','N02','N03','N04']),('解释更短',['T01','T02','T03','T04','T05','T06','T07','T08','T09']),('旧稿胜出',['T10'])]
 packet['overviewGroups']=[{'title':title,'items':[{'id':cid,'label':selected[cid]['reviewer_need'],'path':f'revision_workshop_20261031_v5/FINAL_PASSAGES_REVIEWED_v5.md#{cid.lower()}'}for cid in ids]}for title,ids in groups]
 packet['overviewSource']='revision_workshop_20261031_v5/FINAL_PASSAGES_REVIEWED_v5.md'
 # Keep process history out of first screen. It remains available here for integrator audit.
 manifest={'sourcePacket':str(args.input.resolve().relative_to(ROOT)),'sourcePacketSha256':sha(args.input),'status':'provisional; parent evaluator pending','priorityCards':len(packet['cards']),'tournamentItems':15,'fullSelectionEntries':len(selected),'sourceQuoteChecks':[],'candidateChecks':rows,'writerFilesModified':False,'decisionWrites':False,'findings':[
  'Six selected cards, not fifteen. The fifteen tournament items remain in the linked source index.',
  'optionNotes is a string in writer input; adapted to per-option notes so historical-approval restriction stays visible.',
  'decisionPath links old generic ledger; explicitly historical, legacy IDs mapped where known, no v5 author-choice endpoint claimed.',
  'Reviewer summaries and editorial status were not verbatim quotes; legacy cards now attach actual COMMENT_MAP text, new findings use editorial labels.',
  'Workflow pending text separated from actual fact-pending filter.',
  'N01 is a five-range consistency group; KEEP scope covers full group.',
  'N05b/c remain optional independent edits, not approval inherited from N05a.',
  'Source provenance expanded to mandatory Ch2 followthrough and exact writer/review/alternative inputs.',
  'GRID alternative needs C1 source; final passages only contain selected V5.',
  'FINAL_SELECTION N01 includes later C2 repair, whereas selected_passages_c2 snapshot is older; final packet uses FINAL_SELECTION.'
 ]}
 for c in packet['cards']:manifest['sourceQuoteChecks'].append({'id':c['id'],'unique':True,'exactLine':c['sourceLine'],'sourceFile':c['sourceFile']})

 # R2 validation: exact IDs/offsets, insertion anchors, v4 provenance and assembled context.
 depfile=WORK/'DEPENDENCIES_REVIEWED_v5.json';deps_data=read(depfile);depmap={d['id']:d for d in deps_data}
 opfile=WORK/'evidence/FINAL_OPERATION_MANIFEST_v5.json';ops=read(opfile)['operations'];opmap={o['id']:o for o in ops}
 changes=read(WORK/'evidence/R2_exact_changes.json')
 if len(opmap)!=44 or len(ops)!=44 or len(selected)!=20 or len(depmap)!=23:raise ValueError('R2 requires 20 proposals + 23 dependencies + N07, all IDs unique')
 if set(opmap)!=set(selected)|set(depmap)|{'N07'}:raise ValueError('R2 operation IDs do not match exact selection/dependency sets')
 old_selected={x['id']:x for x in read(WORK/'FINAL_SELECTION.json')}
 if len(changes)!=7 or {c['id']for c in changes}!={'T01','T03','T07','T11','N02','N03','N05a'}:raise ValueError('Seven exact R2 rewrites not identified')
 for change in changes:
  if change['before']!=old_selected[change['id']]['selected'] or change['after']!=selected[change['id']]['selected']:raise ValueError('R2 before/after mismatch')
 byfile={};operation_checks=[]
 for op in ops:
  fp=ROOT/op['file'];deps.add(fp);src=fp.read_text();a,b=op['start'],op['end']
  if not isinstance(a,int) or not isinstance(b,int) or not 0<=a<=b<=len(src):raise ValueError('Invalid source offsets')
  oid=op['id'];actual_old=src[a:b]
  if oid in selected:
   row=selected[oid]
   if row['source']!=op['file'] or op['new'].strip()!=row['selected']:raise ValueError(f'{oid}: selected operation content mismatch')
   insertion=row['original'].startswith('[')
   if insertion!=(op['kind']=='insertion') or insertion!=(a==b):raise ValueError(f'{oid}: insertion/replacement mismatch')
   if not insertion and actual_old!=row['original']:raise ValueError(f'{oid}: original source offset mismatch')
  elif oid in depmap:
   dep=depmap[oid]
   if op['file']!=dep['file'] or actual_old!=dep['old'] or op['new']!=dep['new']:raise ValueError(f'{oid}: dependency mismatch')
   v4src=ROOT/'revision_blueprint_20261031'/('SUPPLEMENTS_v4.md' if dep['origin'].startswith('SUPPLEMENTS') else 'writer_round3.md');deps.add(v4src)
   if oid!='V4-R2-04-sync-3' and dep['new'] and dep['new'] not in v4src.read_text():raise ValueError(f'{oid}: inherited v4 new text not in named source')
  else:
   if op['new'] not in (WORK/'N07_TABLE_MARKUP_REVIEWED_v5.tex').read_text():raise ValueError('N07 markup mismatch')
  byfile.setdefault(op['file'],[]).append(op)
  operation_checks.append({'id':oid,'kind':op['kind'],'source':op['file'],'start':a,'end':b,'exact':True})
 # Verify four insertions occur at the stated source boundaries, not merely arbitrary empty offsets.
 intro=(ROOT/'Chapter_1/Intro.tex').read_text()
 q=next(c for c in packet['cards']if c['id']=='T01')['originalFull']
 anchors={'T01':intro.index(q)+len(q),'T02':intro.index('\\end{table}',intro.index('\\label{tab:intro_scenarios}'))+len('\\end{table}')}
 for oid in ['T04','T05']:
  row=selected[oid];src=(ROOT/row['source']).read_text();anchors[oid]=src.index('\n\n',src.index(row['anchor']))
 for oid,pos in anchors.items():
  if opmap[oid]['start']!=pos:raise ValueError(f'{oid}: actual insertion boundary disagrees with instruction')
 assembled={};tracked={}
 for name,fileops in byfile.items():
  src=(ROOT/name).read_text();cursor=0;pieces=[];positions=[];outlen=0;last=None
  for op in sorted(fileops,key=lambda x:(x['start'],x['end'])):
   if op['start']<cursor or (last and op['start']==last['start']):raise ValueError('Overlapping R2 operations')
   unchanged=src[cursor:op['start']];pieces.append(unchanged);outlen+=len(unchanged)
   start=outlen;pieces.append(op['new']);outlen+=len(op['new'])
   positions.append({'id':op['id'],'start':start,'end':outlen,'isV4':(op['id'] in depmap and op['id']!='V4-R2-04-sync-3') or op['id']=='T10'})
   cursor=op['end'];last=op
  pieces.append(src[cursor:]);assembled[name]=''.join(pieces);tracked[name]=positions
 ccopy={
 'T11':('说明选 Huber 的理由，不推断实验历史。','保留梯度理由，只说明尚未确立优于 MAE。'),
 'N01':('保留表值，把指标推理落在实际比较上。','区分不同量尺的 gap 与 renderer 整体变化，移除超过证据的结论。'),
 'T03':('先解释规则网格，再说明输入和输出。','让 simultaneous notes 与局部邻域说明表示的用途，再交代模型接口。'),
 'T01':('分清数据状态与监督条件。','补清 note content and timing、简化 dynamics 和间接监督的区别。'),
 'N05a':('保留 boundaries，只删防御句。','保留原首句；不把所有 scope boundaries 都改称 limitations。'),
 'KEEP-FIG62':('沿用 v4 的 KEEP，不再扩写图注。','原 caption 已说明 SoundFont-rendered audio；这里保留原图和原注。')}
 for c in packet['cards']:
  c['reviewLinkLabel']='writer 返修回应（非评审结论）';c['externalReviewFile']='revision_workshop_20261031_v5/evaluator_cycle1.md'
  c['writerWhy']=c['why'];c['writerShort']=c['short'];c['navSummary'],c['whyDisplay']=ccopy[c['id']]
  c['displayId']='v5-'+c['id'];c['responseInstruction']=f'新稿请用 v5-{c["id"]}（R2／KEEP）回复我；旧清单仅供对照，旧 YES 不转移。' if c['id']!='KEEP-FIG62' else 'Fig6.2 沿用 v4 的 KEEP；这里只作对照，不要求重复选择。'
  if c['id']=='T03':c['responseInstruction']='新稿请用 v5-T03（R2／GRID／KEEP）回复我；旧清单仅供对照，旧 YES 不转移。'
  for f in c.get('followthrough',[]):
   matches=[o['id']for o in ops if o['file']==f['file'] and o['new']==f['new']]
   if len(matches)==1:f['proposalId']=matches[0]
  if c['id']=='N05a':c['scopeDisplay']='保留第一句 The thesis has several boundaries.；只删除其后防御性解释。b/c 仍是各自可选的小修。'
  if c['id']=='N01':c['responseInstruction']='这一组用 v5-N01（R2／KEEP）回复我；范围含 N01/N02/N03、N07、N04，旧 YES 不转移。'
  if not c.get('contextPreview'):continue
  preview=c['contextPreview'];whole=assembled[c['sourceFile']]
  if whole.count(preview)!=1:raise ValueError(f'{c["id"]}: contextPreview not an exact unique slice of reconstructed R2 source')
  off=whole.index(preview);end=off+len(preview);included=[t for t in tracked[c['sourceFile']]if (t['start']<end and t['end']>off)or(t['start']==t['end'] and off<=t['start']<end)]
  inherited=[t['id']for t in included if t['id']in depmap]
  if set(inherited)!=set(c.get('contextDependencyIdsFinal',[])):raise ValueError(f'{c["id"]}: declared v4 context deps differ from reconstruction')
  c['contextIncludedProposalIds']=[t['id']for t in included if t['id']not in depmap]
  c['contextV4DependencyIds']=inherited
  c['contextLegend']='绿色：本轮 v5 提案；蓝色：沿用 v4 提案；无底色：其余原文。连读示例不是已实施全文。'
  c['contextDependencyDetails']=[]
  for oid in inherited:
   d=copy.deepcopy(depmap[oid])
   if oid.startswith('V4-velocity'):legacy_id='R1-09';anchor='supplement-r1-09'
   elif oid.startswith('V4-scope'):legacy_id='R1-06';anchor='supplement-r1-06'
   elif oid=='V4-motivation':legacy_id='R1-04';anchor='supplement-r1-04'
   elif oid.startswith('V4-R2-04'):legacy_id='R2-04';anchor='decision-r2-04'
   elif oid.startswith('V4-R1-33'):legacy_id='R1-33';anchor='decision-r1-33'
   else:legacy_id='R1-15';anchor='decision-r1-15'
   d['legacyId']=legacy_id;d['legacyReference']='revision_blueprint_20261031/DECISIONS.md#'+anchor
   c['contextDependencyDetails'].append(d)
  at=0;parts=[]
  for t in included:
   a=max(0,t['start']-off);b=min(len(preview),t['end']-off)
   if a==b:continue
   parts.append(html.escape(preview[at:a]));cls='context-v4'if t['isV4']else'context-v5';parts.append(f'<mark class="{cls}" title="{html.escape(t["id"],quote=True)}">'+html.escape(preview[a:b])+'</mark>');at=b
  parts.append(html.escape(preview[at:]));c['contextHtml']=''.join(parts)
 if not selected['T11']['selected'].endswith('We have not established an advantage over MAE.'):raise ValueError('Huber latest wording is not the required exact sentence')
 for name in ['DEPENDENCIES_REVIEWED_v5.json','CANDIDATE_PACKET_FINAL_v5.md','evidence/FINAL_OPERATION_MANIFEST_v5.json','evidence/R2_exact_changes.json','FINAL_SELECTION.json']:
  deps.add(WORK/name)
 packet['contextAssumptions']='固定组合预览：20项R2选文、N07与23项明确v4依赖均为未实施提案。新稿和沿用v4文字分别标明；本卡KEEP不改变其他依赖。'
 packet['provenance']=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}for p in sorted(deps)]
 for g in packet['overviewGroups']:
  for item in g['items']:item['path']=item['path'].replace('FINAL_PASSAGES_REVIEWED_v5.md','CANDIDATE_PACKET_FINAL_v5.md')
 manifest['status']='R2 provisional; evaluator_cycle2 verdict pending';manifest['operationChecks']=operation_checks;manifest['sourceSnapshots']=packet['provenance'];manifest['insertionAnchorChecks']=anchors
 manifest['newDecisionInstruction']='Use stable v5 IDs with R2/KEEP in chat; old DECISIONS is historical reference, no second editable ledger.'
 manifest['findings'].append('R2 contextPreview is exactly reconstructed from 44 operations. It includes other unapproved proposals as well as v4 deps; these are separately listed and highlighted.')
 from final_agreement_checks import finalize_packet
 finalize_packet(packet=packet,source=source,selected=selected,deps_data=deps_data,depmap=depmap,ops=ops,assembled=assembled,deps=deps,manifest=manifest,input_path=args.input)
 (HERE/'reviewed_v5_packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
 (HERE/'evidence/final_packet_ingestion.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 print(f'Prepared {len(packet["cards"])} final reviewed cards, {len(deps)} frozen inputs; no author-choice writes.')
if __name__=='__main__':main()
