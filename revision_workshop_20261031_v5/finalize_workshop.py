from pathlib import Path
import json,re,hashlib,difflib
root=Path('/Users/jollibear/Documents/tmp/phd thesis');stage=Path(__file__).resolve().parent
items=json.loads((stage/'evidence/selected_passages_c2.json').read_text())
old=next(x['selected'] for x in items if x['id']=='N01')
new='Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.'
for x in items:
 if x['id']=='N01':x['selected']=new
 x['reinserted_context']=x['reinserted_context'].replace(old,new)
reasons={
'T01':'把79词旧定义缩成45词；区分数据状态和监督条件，保留重叠和Ch6实例。',
'T02':'保留aligned notes和S2关系；不再重新解释所有可能audio-only任务。',
'T03':'同时回答二维输入、单通道输出和note-list取舍；保留原引用。',
'T04':'邻段已讲应用场景；只补未评价joint note-detection收益这一必要边界。',
'T05':'承认level变化也能给边界，再说本工作显式监督；不制造必要性或消融结果。',
'T06':'直接讲piano-pretrained estimator在real audio上adapt；不声称更简单、更高效或消除域差异。',
'T07':'保留退化观察，明确fidelity/gradient未分开测；删掉较长解释。',
'T08':'四篇co-authored studies与thesis synthesis说清即可；会议和作者清单交给已有Declaration。',
'T09':'保留Second顺序；piano/guitar已测与其他乐器未测在一段内讲清。',
'T10':'旧v4 A仍胜出：mean similarity、11位听者/8段/一个renderer和composer分组范围都准确。',
'T11':'实际PDF说not established，不是did not conduct；不替作者添加否定实验历史。',
'N01':'两种指标都把GT排在flat之上；gap数字本身不能证明哪种更敏感。',
'N02':'换SoundFont是renderer整体变化；不能隔离absolute gain，也不能直接比MAE与r量尺。',
'N03':'保留选择Pearson的正面理由，删掉cosine/MAE普遍失败的结论。',
'N04':'同步Ch2与Ch6：renderer mismatch可能影响梯度，不写必然主导。'}
for x in items:x['reason_zh']=reasons.get(x['id'],x.get('reason_zh',''))
(stage/'FINAL_SELECTION.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
lines=['# v5 精选修改：精确原文与最终提案\n','全部为未实施的建议。原文来自当前LaTeX，尚未认定正式送审PDF。旧DECISIONS、所有旧稿均保留；旧YES不自动批准新文字。N01/N02/N03/N07为同一个一致性组，须一起看。\n','[先看简短推荐](EDITORIAL_RECOMMENDATIONS_v5.md) · [独立评分](evidence/BLIND_CRITIQUE_C1.md) · [第二轮反向释义复核](evidence/CRITIQUE_C2.md)\n']
for x in items:
 s=(root/x['source']).read_text();anchor=x['anchor'];line=s[:s.index(anchor)].count('\n')+1
 x['source_line']=line
 lines.append(f"## {x['id']} · {x['related']}\n\n`{x['source']}:{line}` · {x['operation']}\n\n{x['reason_zh']}\n")
 if x['original'].startswith('[No additional'):
  lines.append('**原文位置：** 当前没有下列解释；周围原段保留，插入后的完整语境见本节末尾。方括号标记不是论文原句。\n')
 else:lines.append('**准确原文：**\n```latex\n'+x['original']+'\n```\n')
 lines.append('**推荐英文：**\n```latex\n'+(x['selected'] or '[删除该句，不补新句]')+'\n```\n')
 lines.append('<details><summary>放回原段后的完整语境</summary>\n\n```latex\n'+x['reinserted_context']+'\n```\n\n</details>\n')
(stage/'FINAL_PASSAGES_WITH_ORIGINALS.md').write_text('\n'.join(lines))
(stage/'FINAL_SELECTION.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
# Integrity verifies manuscript remains exactly as first workshop snapshot.
manifest=json.loads((stage/'evidence/source_hashes_before.json').read_text());changes=[]
for file,before in manifest.items():
 now=hashlib.sha256((root/file).read_bytes()).hexdigest()
 if now!=before:changes.append(file)
checks={'source_snapshot_files':len(manifest),'changed_source_files':changes,'passages':len(items),'unique_non_insertion_originals':all((root/x['source']).read_text().count(x['original'])==1 for x in items if not x['original'].startswith('[No additional')),'N01_C2_minimal_repair_applied':True,'table_values_unchanged':json.loads((stage/'evidence/N07_table_markup_check.json').read_text())['numeric_tokens_unchanged'],'old_recommendations_modified':False,'author_decisions_modified':False,'experiments_run':False,'external_apis_or_uploads':False}
(stage/'evidence/FINAL_INTEGRITY_CHECK.json').write_text(json.dumps(checks,indent=2))
assert not changes,changes
print(json.dumps(checks,ensure_ascii=False))
# Word counts are reproducible workload diagnostics, never quality scores.
tour=[x for x in items if x['id'].startswith('T') and x['id']!='T10']
counts=[{'id':x['id'],'old_recommended_words':len(re.findall(r'\b[\w-]+\b',x['variants']['V4'])),'new_words':len(re.findall(r'\b[\w-]+\b',x['selected']))} for x in tour]
(stage/'evidence/passage_word_counts.json').write_text(json.dumps(counts,indent=2))
print('10 changed incumbent passages, rough regex words:',sum(x['old_recommended_words'] for x in counts),'->',sum(x['new_words'] for x in counts))
