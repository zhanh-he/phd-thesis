#!/usr/bin/env python3
"""Extract a small, frozen v3/v4 reading packet. Never edits thesis or ledger."""
import json, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OLD = ROOT / 'revision_blueprint_20261031'
rows = {x['id']: x for x in json.loads((OLD/'evidence/writer_candidates_round3.json').read_text())}
comments = {x['id']: x for x in json.loads((OLD/'evidence/comment_map.json').read_text())}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def make(key, i, title, short, why, stance, scope, pending, labels, focus=None):
    r, c = rows[key], comments[key]
    o = r['originals'][i]
    opts = [{'id': k, 'label': labels[k], 'kind': 'replacement', 'fullText': v,
             'focusText': focus(v) if focus else v} for k,v in r['variants'].items()]
    return {'id': key, 'title': title, 'short': short, 'group': '文字澄清', 'why': why,
      'stance': stance, 'scope': scope, 'pending': pending, 'operation': 'replacement',
      'sourceFile': o['file'], 'sourceLine': o['line'], 'originalFull': o['text'],
      'originalFocus': focus(o['text']) if focus else o['text'], 'options': opts,
      'recommended': r['recommendation'], 'recommendationLabel': '旧轮编辑推荐',
      'reviewStatus': '旧轮已复核，待作者选择',
      'reviewFile': 'revision_blueprint_20261031/reviewer_final.md',
      'candidateFile': 'revision_blueprint_20261031/writer_round3.md',
      'candidateAnchor': key.lower(), 'reviewerComment': c['comment'], 'authorResponse': c['response'],
      'commentFile': 'revision_blueprint_20261031/COMMENT_MAP.md',
      'contextAfter': r.get('context_after',''), 'followthrough': r.get('followthrough',[])}

first=lambda t:t.split('. ',1)[0]+'.'
loss=lambda t:t.split('This hybrid supervision is useful because ',1)[-1] if t.startswith('This hybrid supervision') else (t[t.index('This hybrid supervision is useful because '):] if 'This hybrid supervision is useful because ' in t else t[t.index('The frame-wise BCE'): ] if 'The frame-wise BCE' in t else t[t.index('Each component'): ] if 'Each component' in t else t[t.index('The two components'): ] if 'The two components' in t else '')
# Use a shared, exact prefix to identify the small loss explanation; no prose rewriting.
loss_original=rows['R1-25']['originals'][0]['text']
loss_prefix=loss_original[:loss_original.index('This hybrid supervision')]
def loss(t):
    if not t.startswith(loss_prefix): raise ValueError('Loss prefix changed; re-check source')
    return t[len(loss_prefix):]

cards=[]
cards.append(make('R1-15',0,'把 S1 的信息条件说准','只改首句，保留研究问题。',
 '“most controlled”会把信息条件读成难度排序；直接写只有符号输入。',
 '你说本意是“less input signal”，并同意换词。',
 'Ch3 首段只换第一句；四处相关表述随所选方案同步，见完整范围。', '',
 {'A':'A · 只修首句','B':'B · 解释估计歧义','C':'C · 压缩整段'},first))
cards[-1]['group']='场景'
cards[-1]['short']='推荐只改首句，也可比较整段写法。'
for o in cards[-1]['options']:
    if o['id'] in ['B','C']:
        o['originalFocus']=cards[-1]['originalFull']
        o['focusText']=o['fullText']
        o['summary']='这一版重写整个首段；下方显示完整变化。'
        o['scope']='Ch3 首段整体替换为这一版；四处相关表述随稿同步。不是只改第一句。'
    else:o['summary']='只改首句，保留后面两句和研究问题。'
cards.append(make('R1-25',0,'把 loss 的 1:1 说出来','公式保留，补清平均方式和已有比较。',
 '评审问两项怎样平衡；原段没有直接说每项先平均、相对系数各为 1。',
 '你写明沿用 Kim，并说自己验证过，准备补引用。',
 '只替换 loss 段最后的解释；原引言、公式、变量定义和引用保留。',
 'V-04：实际 run 的 theta、整体尺度和验证范围仍需记录对齐。选文字不确认最佳比例。',
 {'A':'A · 最短解释','B':'B · 保留 SMC 初步比较','C':'C · 解释两项作用'},loss))
cards[-1]['group']='方法'
cards.append(make('R1-21',2,'说明 composition 怎样使用','原段保留，后面新增应用段。',
 '分开说训练标签的来源和实际输入接口，回答 performance MIDI 与 composition 的关系。',
 '你明确说试过量化 MIDI，并说 MOS 用量化 score-MIDI；这条原话保留，具体刺激流程待查。',
 '只在 Ch3 Discussion 首段后插入所示应用段，不替换 Stimuli；原量化批注不由此改写。',
 'V-02：输入和 reference 的 timing preparation、量化步骤仍待生成记录。这里的文字选择不确认听测协议。',
 {'A':'A · 两句说明','B':'B · 分开训练与输入','C':'C · 从创作用途切入'}))
cards[-1]['operation']='insertion'
cards[-1]['group']='用途'
for o in cards[-1]['options']:
    o['kind']='insertion'
    o['summary']='原段后新增'+('两' if o['id']=='A' else '三')+'句应用说明。'
cards[-1]['contextAfter']=''
cards.append(make('R1-35',0,'图注已经说清，可以保留','当前推荐 KEEP，不为了改而扩写。',
 '原图注已写 SoundFont-rendered audio；长解释未必帮助这处阅读。',
 '未找到你对此条的既有回复；KEEP 是编辑建议，不是你的批准。',
 'KEEP 保留 Fig6.2 原图与原图注。旧 A 另含图内标签修改，尚需副本与视觉核验。',
 '', {'A':'旧 A · 扩写图注（需另核图）'}))
c=cards[-1]
caption=c['originalFull'].split('\\caption{',1)[1].rsplit('}\\n',1)[0] if False else c['originalFull'].split('\\caption{',1)[1].split('\n\\label',1)[0][:-1]
c['originalFull']=caption;c['originalFocus']=caption
c['sourceExact']='\\caption{'+caption+'}'
c['recommended']='KEEP';c['recommendationLabel']='v4 复核推荐'
c['reviewFile']='revision_blueprint_20261031/contextual_review_v4.md'
c['options'].insert(0,{'id':'KEEP','label':'KEEP · 保留原图和原图注','kind':'keep','fullText':caption,'focusText':caption})
c['optionNotes']={'A':'这里只比较旧 A 的图注文字。原提案还涉及图内标签；未制作并核验副本，不能由图注选择视为完成。'}
c['group']='保留'
c['originalImage']='Chapter_6/figures/p2.jpg'
c['recommendationSource']='revision_blueprint_20261031/SUPPLEMENTS_v4.md#keep-r1-35'
cards.append(make('R2-04',3,'结果保留，解释更准确','保留 U-Net 排序，集中交代听测范围。',
 '把“clearly outperforms”落到实际的 mean similarity，并保留系统间的已报告排序。',
 '未找到你对此条的既有回复；推荐措辞来自编辑与复核。',
 '替换 Ch3 Results 段；MOS 表、CI、Participants 与 Stimuli 保留。摘要、引言和结论有四处同步。',
 'V-02：timing preparation 仍待记录；此段不补未经确认的处理细节。',
 {'A':'A · 保留排序和引用','B':'B · 直接报告读数','C':'C · 强调与客观结果互补'}))
cards[-1]['group']='结果'
for c in cards:
    c['options'].append({'id':'KEEP','label':'KEEP · 保留原文','kind':'keep','fullText':c['originalFull'],'focusText':c['originalFocus']}) if c['recommended']!='KEEP' else None
    c['decisionPath']='revision_blueprint_20261031/DECISIONS.md#decision-'+c['id'].lower()
packet={'schemaVersion':1,'edition':'旧轮 v3／v4 · 五处示例','packetStatus':'reviewed-legacy',
 'versionNotice':'现在展示旧轮已复核文字。v5 新稿尚未接入，不继承任何旧批准。',
 'purpose':'只读比较；查看写法不会记录选择。作者决定只写入原 DECISIONS.md。',
 'cards':cards,'provenance':[]}
for name in ['evidence/writer_candidates_round3.json','evidence/comment_map.json','evidence/supplements_v4.json','reviewer_final.md','contextual_review_v4.md','SUPPLEMENTS_v4.md']:
    p=OLD/name;packet['provenance'].append({'path':str(p.relative_to(ROOT)),'sha256':sha(p)})
(HERE/'initial_packet.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
print('Extracted',len(cards),'cards; current R1-35 recommendation overridden from v4: KEEP')
