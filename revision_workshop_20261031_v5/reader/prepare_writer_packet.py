#!/usr/bin/env python3
"""Create a provisional display adapter; never changes writer or reviewer files."""
import argparse, copy, hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
WORK=HERE.parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=WORK/'WRITER_READER_PACKET.json');args=ap.parse_args()
 source=read(args.input);packet=copy.deepcopy(source)
 selected={r['id']:r for r in read(WORK/'FINAL_SELECTION.json')}
 comments={r['id']:r for r in read(ROOT/'revision_blueprint_20261031/evidence/comment_map.json')}
 packet['packetStatus']='writer-provisional'
 packet['sourcePacketStatus']=source['packetStatus']
 packet['edition']='v5 待独立评审 · 六处精选预览'
 packet['versionNotice']='待独立评审：这是 writer 的 v5 暂定候选。内部 C1/C2 记录不等于本轮外部评审同意；此预览不批准任何文字。'
 packet['provisionalNotice']='独立评审尚未确认；默认仅展示六处精选，完整十五组比较按需查阅。'
 packet['reviewAgreement']['parentEvaluatorPending']=True
 packet['mastNote']='只读预览 · writer 暂定稿'
 packet['purpose']='只读暂定比较。原 index.html 继续展示历史已复核例子；不写作者决定。'
 rows=[];deps={args.input.resolve(),WORK/'FINAL_SELECTION.json',WORK/'FINAL_PASSAGES_WITH_ORIGINALS.md',WORK/'EDITORIAL_RECOMMENDATIONS_v5.md',WORK/'CANDIDATE_PACKET_BLIND_C1.md',ROOT/'revision_blueprint_20261031/evidence/comment_map.json'}
 legacy={'T11':'R1-34','T03':'R1-17','T01':'R1-05','KEEP-FIG62':'R1-35'}
 for c in packet['cards']:
  cid=c['id'];c['writerScope']=c['scope'];c['writerReviewSummary']=c['reviewerComment'];c['writerAuthorResponseSummary']=c['authorResponse']
  original=(ROOT/c['sourceFile']).read_text();quote=c.get('sourceExact',c['originalFull']);count=original.count(quote)
  if count!=1:raise ValueError(f'{cid}: original quote must match uniquely, found {count}')
  actual_line=original[:original.index(quote)].count('\n')+1
  if actual_line!=c['sourceLine']:raise ValueError(f'{cid}: line mismatch')
  c['reviewStatus']='暂定候选 · 外部独立评审待确认'
  c['recommendationLabel']='writer 暂定推荐（待独立评审）'
  # Workflow pending is not a scientific fact blocker. Preserve its exact text separately.
  c['statusNote']=c['pending'];c['pending']=''
  note=c.get('optionNotes','')
  if isinstance(note,str):c['optionNotes']={o['id']:note for o in c['options']}
  c['candidateSourceLabel']='writer 准确候选（待独立评审）'
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
   if cid=='N01':expected='\n\n'.join(selected[k]['selected'] for k in ['N01','N02','N03']);proof=['FINAL_SELECTION.json#N01','FINAL_SELECTION.json#N02','FINAL_SELECTION.json#N03']
   elif cid=='T03' and o['id']=='GRID':
    expected=selected[cid]['variants']['FRESH_1'];proof=['FINAL_SELECTION.json#T03.variants.FRESH_1']
    c['candidateEvidenceByOption'][o['id']]={'path':'revision_workshop_20261031_v5/CANDIDATE_PACKET_BLIND_C1.md#t03','label':'GRID 备选原来源'}
   else:expected=selected[cid]['selected'];proof=[f'FINAL_SELECTION.json#{cid}.selected']
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
   c['baselineNote']='79→45 词比较的是旧 v4 提案；当前 thesis 没有这段定义。'
  if cid=='KEEP-FIG62':c['keepScope']='保留 Fig6.2 原图与原图注；不确认 Fig6.3 的 GT 来源。'
  for f in c.get('followthrough',[]):
   fp=ROOT/f['file'];deps.add(fp)
   if fp.read_text().count(f['old'])!=1:raise ValueError(f'{cid}: followthrough source must match uniquely')
   if f['new'] and f['new'] not in (WORK/'FINAL_PASSAGES_WITH_ORIGINALS.md').read_text() and f['new'] not in (WORK/'N07_TABLE_MARKUP_PROPOSAL.tex').read_text():raise ValueError(f'{cid}: followthrough candidate not found')
  for field in ['sourceFile','candidateFile','reviewFile','commentFile']:
   deps.add(ROOT/c[field].split('#',1)[0])
 for v in packet['reviewAgreement'].values():
  if isinstance(v,str) and v.startswith('revision_workshop_') and (ROOT/v).is_file():deps.add(ROOT/v)
 deps.add(WORK/'N07_TABLE_MARKUP_PROPOSAL.tex')
 packet['provenance']=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}for p in sorted(deps)]
 # Fifteen tournament items are an optional topic index, not fifteen simultaneous cards.
 groups=[('新发现',['T11','N01','N02','N03','N04']),('解释更短',['T01','T02','T03','T04','T05','T06','T07','T08','T09']),('旧稿胜出',['T10'])]
 packet['overviewGroups']=[{'title':title,'items':[{'id':cid,'label':selected[cid]['reviewer_need'],'path':f'revision_workshop_20261031_v5/FINAL_PASSAGES_WITH_ORIGINALS.md#{cid.lower()}'}for cid in ids]}for title,ids in groups]
 packet['overviewSource']='revision_workshop_20261031_v5/FINAL_PASSAGES_WITH_ORIGINALS.md'
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
 (HERE/'provisional_v5_packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
 (HERE/'evidence/writer_packet_ingestion.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 print(f'Prepared {len(packet["cards"])} provisional cards, 15-item optional index, {len(deps)} frozen input hashes. Writer/ledger files unchanged.')
if __name__=='__main__':main()
