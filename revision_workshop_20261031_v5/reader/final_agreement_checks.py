"""Exact bounded final checks and display-only adaptation. No writer/source edits."""
import copy, hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
WORK=HERE.parent
ROOT=WORK.parent

def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def finalize_packet(*,packet,source,selected,deps_data,depmap,ops,assembled,deps,manifest,input_path):
 delivery=read(WORK/'FINAL_DELIVERY_MANIFEST_v5.json');verdict=read(WORK/'evaluator_cycle2_verdict.json')
 required='9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17'
 if sha(input_path)!=required or sha(input_path)!=delivery['readerPacketSha256']:raise ValueError('Reviewed packet SHA differs from parent/writer binding')
 if source.get('packetStatus')!='jointly-reviewed-v5' or source.get('contextField')!='reinserted_context_final':raise ValueError('Final reviewed context identity missing')
 for name,h in delivery['files'].items():
  if sha(WORK/name)!=h:raise ValueError('Final delivery changed: '+name)
 if set(source['reviewAgreement'].get('exactCorrectionsAcknowledged',[]))!={'V4-R2-04-sync-3','N07'}:raise ValueError('Exact writer repair agreement missing')
 if delivery['authorApproved'] or delivery['implemented']:raise ValueError('Text agreement is not author approval/implementation')
 if set(selected)!=set(verdict['acceptedSelectedIds']):raise ValueError('Accepted selected ID set mismatch')
 for oid,row in selected.items():
  if hashlib.sha256(row['selected'].encode()).hexdigest()!=verdict['acceptedSelectedTextSha256'][oid]:raise ValueError('Final text differs from acceptance: '+oid)
 corrected=read(WORK/'evaluator_cycle2_dependencies_corrected_proposal.json')
 if len(corrected)!=len(deps_data):raise ValueError('Corrected dependency count mismatch')
 for a,b in zip(deps_data,corrected):
  if any(a[k]!=b[k]for k in ['id','file','line','old','new']):raise ValueError('Final dependency differs from reviewed repair')
 if sha(WORK/'N07_TABLE_MARKUP_REVIEWED_v5.tex')!=verdict['correctedProposalArtifactSha256']['evaluator_cycle2_N07_corrected_proposal.tex']:raise ValueError('Corrected N07 table bytes differ')
 oldops={o['id']:o for o in read(WORK/'evidence/R2_context_operation_manifest.json')['operations']}
 changed=[o['id']for o in ops if o!=oldops[o['id']]]
 if set(changed)!={'V4-R2-04-sync-3','N07'}:raise ValueError('Unexpected final operation changes')
 for name,assembled_text in assembled.items():
  if hashlib.sha256(assembled_text.encode()).hexdigest()!=verdict['correctedVirtualOverlaySha256'][name]:raise ValueError('Corrected virtual overlay hash mismatch: '+name)
 for oid,row in selected.items():
  if row['reinserted_context_final'] not in assembled[row['source']]:raise ValueError('Final context not in exact overlay')
 packet.pop('provisionalNotice',None)
 packet['packetStatus']='jointly-reviewed-v5';packet['edition']='v5 最新修改提案'
 packet['versionNotice']='这是 v5 最新提案，指定文字已复核，正文未改。v4 仅作沿用与对照；新稿用 v5 编号回复，旧 YES 不转移。'
 packet['contextAssumptions']='固定组合预览包括本轮提案与明确沿用项；均未实施，不互相代填选择。'
 packet['mastNote']='本地只读 · 供你选择'
 packet['purpose']='最终只读比较；作者以稳定v5编号表达选择，reader不保存决定；旧页面原样归档。'
 packet['reviewAgreement']=copy.deepcopy(source['reviewAgreement']);packet['reviewAgreement']['parentEvaluatorPending']=False;packet['reviewAgreement']['externalCycle2Pending']=False
 packet['reviewAgreement']['readerUiVerification']='Final build must pass reader-owned browser validation; no inherited UI pass.'
 packet['overviewSummary']='其他段落与保留项'
 packet['overviewNote']='这里是准确全文和各自范围；原 Markdown 打开后可搜索编号。已有 v4 范围只作对照，不要求再选一次。'
 packet['correctedDependencyIds']=['V4-R2-04-sync-3'];packet['retainedV4DependencyCount']=22
 packet['remainingMaterials']=['正式送审版本','听测 timing 处理','实际 run／checkpoint／表源','吉他 Fig6.3 GT 来源','最终 ICASSP 版本']
 fixed=depmap['V4-R2-04-sync-3']
 packet['synchronization']=[
 {'displayId':'v5-N01','title':'指标五处作为一组','summary':'N01/N02/N03 三段解释＋N07 表格方向与标记＋Ch2 N04 从句。保留所有数字。','path':'revision_workshop_20261031_v5/FINAL_PASSAGES_REVIEWED_v5.md#n01'},
 {'displayId':'v5-ROADMAP','title':'删掉同一句的 supported 重复','summary':'这是本轮扩展范围后的新修正，不是原样沿用 v4。','sourceFile':fixed['file'],'sourceLine':fixed['line'],'old':fixed['old'],'new':fixed['new'],'responseInstruction':'这处可用 v5-ROADMAP（推荐稿／KEEP）单独回复；旧 YES 不适用。'},
 {'displayId':'v4','title':'原样沿用项','summary':'只为组合语境保留既有提案和范围；旧选择不扩展到新的 v5 文字。','path':'revision_workshop_20261031_v5/DEPENDENCIES_REVIEWED_v5.json'}]
 copytext={
 'T11':('Huber 为什么这样选','保留梯度理由，准确说明尚未确立优于 MAE。'),
 'N01':('指标能说明什么','保留表值，分清相似性与 renderer 变化，收准推理和表格方向。'),
 'T03':('为什么用 piano roll','规则网格呈现同时音与局部邻域，再交代输入和输出。'),
 'T01':('两个术语分开说','区分力度被简化的数据和缺可靠标签的学习条件。'),
 'N05a':('保留范围，删去防御句','保留 boundaries 与实际限制，让结论直接进入内容。'),
 'KEEP-FIG62':('Fig6.2：保留原图注','现有图注已经说明 SoundFont-rendered teacher targets。')}
 for c in packet['cards']:
  c['title'],c['whyDisplay']=copytext[c['id']];c['navSummary']=c['whyDisplay'];c['short']=c['whyDisplay'];c['why']=c['whyDisplay']
  c['showRecommendationLabel']=False
  if c['id']in['N01','N05a']:c['scopeNote']=''
  c['reviewStatus']='文字已复核 · 供你选择';c['recommendationLabel']='本轮推荐';c['candidateSourceLabel']='准确最终提案'
  c['reviewFile']='revision_workshop_20261031_v5/evaluator_cycle2.md';c['reviewLinkLabel']='独立文字复核（指定范围）'
  c['writerAgreementFile']='revision_workshop_20261031_v5/FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md'
  c['statusNote']='这些是供作者选择的提案，未写回正文。实验／运行记录核验仍按原材料处理。'
  c['writerOptionNotes']=c['optionNotes'];c['optionNotes']={}
  c['variantDisplayLabels']={o['id']:('新增段 · 本轮推荐稿'if c['operation']=='insertion'else'本轮推荐稿')for o in c['options']if o['id']==c['recommended']}
  c['responseInstruction']=f'新稿用 v5-{c["id"]}（推荐稿／KEEP）回复我；旧 YES 不转移。'
  if c['id']=='T03':c['responseInstruction']='新稿用 v5-T03（推荐稿／GRID／KEEP）回复我；旧 YES 不转移。'
  if c['id']=='KEEP-FIG62':c['displayId']='v4 · Fig6.2';c['responseInstruction']='此处只展示既有 v4 KEEP 选项，不新增 v5 决定。'
  if c['id']=='N01':
   c['responseInstruction']='用 v5-N01（推荐稿／KEEP）回复这一组五处；旧 YES 不转移。'
   c['originalFocus']=c['originalFull'].split('\n\n',1)[0]
   for o in c['options']:o['focusText']=c['originalFocus']if o['kind']=='keep'else o['fullText'].split('\n\n',1)[0]
   c['focusNote']='先看第一段的变化；这是一组五处修改，完整内容在下方。'
  if c['id']=='N05a':
   c['scopeDisplay']='保留第一句 The thesis has several boundaries.；只删除其后防御性解释。b/c 是下方独立可选的小修。'
   c['independentOptionalDetails']=[{'id':oid,'file':selected[oid]['source'],'line':selected[oid]['source_line'],'old':selected[oid]['original'],'new':selected[oid]['selected']}for oid in ['N05b','N05c']]
  c['contextCarriedV4Ids']=[oid for oid in c.get('contextV4DependencyIds',[])if oid!='V4-R2-04-sync-3']
  c['contextCorrectedV5Ids']=['ROADMAP']if'V4-R2-04-sync-3'in c.get('contextV4DependencyIds',[])else[]
  if c.get('contextPreview'):c['contextIncludedProposalIds']+=c['contextCorrectedV5Ids']
  for d in c.get('contextDependencyDetails',[]):
   if d['id']=='V4-R2-04-sync-3':d['isCorrected']=True;d['responseId']='v5-ROADMAP';d.pop('legacyReference',None)
 for name in ['FINAL_DELIVERY_MANIFEST_v5.json','FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md','evaluator_cycle2.md','evaluator_cycle2_verdict.json','evaluator_cycle2_repair_verification.json','evaluator_cycle2_dependencies_corrected_proposal.json','evaluator_cycle2_N07_corrected_proposal.tex']:
  deps.add(WORK/name)
 packet['provenance']=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)}for p in sorted(deps)]
 mapping=[]
 for c in packet['cards']:
  if c['id']=='KEEP-FIG62':continue
  ids=['N01','N02','N03','N07','N04']if c['id']=='N01'else[c['id']]
  mapping.append({'displayId':'v5-'+c['id'],'version':'reviewed-v5-20261031','sourcePacketSha256':sha(input_path),'rangeIds':ids,'allowedReplyLabels':['推荐稿','KEEP']+(['GRID']if c['id']=='T03'else[])})
 for oid in ['N05b','N05c']:mapping.append({'displayId':'v5-'+oid,'version':'reviewed-v5-20261031','rangeIds':[oid],'allowedReplyLabels':['推荐稿','KEEP']})
 mapping.append({'displayId':'v5-ROADMAP','version':'reviewed-v5-20261031','rangeIds':['V4-R2-04-sync-3'],'old':fixed['old'],'new':fixed['new'],'allowedReplyLabels':['推荐稿','KEEP']})
 (HERE/'v5_scope_mapping.json').write_text(json.dumps({'readOnly':True,'purpose':'Proposed response ID mapping; not an author decision ledger.','sourcePacketSha256':sha(input_path),'items':mapping},ensure_ascii=False,indent=2)+'\n')
 manifest['status']='writer/evaluator agreed exact repaired text; author approval and implementation pending'
 manifest['sourceSnapshots']=packet['provenance'];manifest['exactRepairedOperationIds']=changed;manifest['acceptedSelectionHashes']=verdict['acceptedSelectedTextSha256'];manifest['overlayMatchesEvaluator']=True
 manifest['newDecisionInstruction']='Reply using v5 IDs + 推荐稿/KEEP; source ledger is historical/current existing scope only.'
