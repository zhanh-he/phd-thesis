from pathlib import Path
import json
out=Path(__file__).resolve().parent;root=Path('/Users/jollibear/Documents/tmp/phd thesis/revision_workshop_20261031_v5')
changes=json.loads((out/'evidence/R2_exact_changes.json').read_text());new={x['id']:x for x in json.loads((out/'FINAL_SELECTION_R2.json').read_text())}
lines=['# Writer R2：回应第一次外部独立评阅\n','**阶段：已作实际定点返修，等待第二次外部整段评阅。** 不宣称joint approval。C1匿名候选、先前FINAL_SELECTION／推荐／reader输入和全部评分均冻结保留。R2另存新文件。正文、旧DECISIONS、PDF、数据、bibliography、图像未改。\n','本轮依据：`evaluator_cycle1.md`及其`evaluator_cycle1_post_reveal.json`。先回读真实源文与前后段，再作以下七处取舍。此前两轮是writer内部子代理评阅；这次外部C1单独计数、量尺不混用。\n','## 逐项取舍与理由\n','| ID | 决定 | 实际理由 |\n|---|---|---|']
for c in changes:lines.append('| '+c['id']+' | '+c['decision']+' | '+c['reason_zh']+' |')
lines+=['\nN02/N03采用外部意见的内容，但将metric-purpose句只放在N03，避免紧接两段重复用途。不是拒绝renderer/gain区别或absolute-level目的；第二次外部评阅可据整段判断这个整合。\n','T11的新精简是降低歧义，旧v5句与真实批注相容，并不被改写成已知错误。v4“did not conduct”应理解为资料不足以断言的实验史，不因此证明它必然为假；不回填或篡改旧评分。\n','## 七处准确diff：冻结writer选稿 → R2\n']
for c in changes:
 lines.append(f"### {c['id']} · 当前源坐标 `{c['source']}:{c['source_line']}`\n\n```diff\n{c['exact_diff']}\n```\n")
lines+=['## 明确保留\n','T10继续用v4，不为微小措辞偏好换稿。T02/T04/T05/T06/T08/T09/N01/N04/N05b/N05c/N06a/N06b均未改选稿。Fig6.2原caption／图、O/F/V角色、loss公式、beta／权重、frontend参数及实测表值保持原样。N05a特别恢复原首句，是一项确切的KEEP胜出。\n','## v4已解决的内容只继承，不记作新发现\n','组合预览明确带入23项既有依赖：SUPPLEMENTS_v4的8处velocity定义、S3/scope两处及动机末句；R1-15的首段及四处S1同步；R2-04的四处听测概括同步；R1-33的三个共同完整段落（含五个原局部动作）。详见`DEPENDENCIES_R2.json`。\n','这些依赖仍是未批准提案，只为本次组合语境演示。没有声称43项全部被作者采用；本卡KEEP不自动批准／拒绝其他依赖，旧YES不继承。`CANDIDATE_PACKET_R2_FULL_CONTEXT.md`不再让相关语境保留旧S3、most-constrained或错误听测比较对象。\n','## 指标表与舍入提示\n','N01/N02/N03与N07必须同组。N07沿用原副本：表环境内58个数字token顺序不变，12个数值bold/underline包装变0。外部评阅指出显示端点0.702−0.510与报告delta0.193的精度差；本轮不诊断成数据错误，不重算或静默修数。删掉正文数字复述也避免把报告值写成我们重新计算的结果。N04保留已通过的conditional can-divert从句，不为了换词再扩一轮。\n','## 有界excerpt review独立记录\n','父级另报告GPT-6.1-sol的bounded excerpt review。它未访问全文、真实批注或表格；只作所见片段的序位编辑判断。不算第二次外部全文审查。原始归属／范围／评分和采用取舍另存`evidence/BOUNDED_EXCERPT_REVIEW_PARENT_R2.md`，不与full-source C1合并。\n','## 交给第二次外部评阅\n','- `FINAL_SELECTION_R2.json`：20项精确源操作及当前英文。\n- `CANDIDATE_PACKET_R2_FULL_CONTEXT.md`：包含v4依赖的组合整段预览。\n- `FINAL_PASSAGES_R2.md`：相同准确英文的阅读入口。\n- `WRITER_READER_PACKET_R2.json`：新版本无损reader输入；状态刻意保留`writer-r2-pending-external-cycle2`，不能直接冒充jointly-reviewed。没有改reader HTML。\n- `evidence/R2_exact_changes.json`／`R2_context_operation_manifest.json`：准确diff、插入位置、依赖、无重叠检查。\n','正式送审基线、R1-13/21/26/30、run／checkpoint／table provenance、guitar GT和最终ICASSP版本继续开放。没有新实验、编译、外传或提交。\n']
(out/'WRITER_REVISION_RESPONSE_R2.md').write_text('\n'.join(lines))
# New compact reader-facing overview; never overwrite the historical version.
s=(root/'EDITORIAL_RECOMMENDATIONS_v5.md').read_text()
s=s.replace('# 这轮真正值得看的变化','# 外部C1后：七处定点返修，等待第二轮评阅',1)
oldintro='**旧稿保留，thesis正文未动。** 我重新评了43组、97条旧路线，对15处关键文字做了原文／旧稿／两种新稿比较，再做两轮独立批评与整段拼接核验。结果不是多加43段：十处旧解释被缩短，一处旧听测稿继续胜出；另外找到旧版漏掉的论证与语气问题。'
newintro='**正文未动，旧稿和旧决定均保留。** 先前重审43组／97条路线，完成两轮内部子代理评阅；现在已根据第一次外部独立评阅，对七处作真实返修。第二次外部整段评阅仍待完成，这一版不是最终共同裁决。T10继续用v4，Fig6.2等有依据的KEEP保留。'
assert oldintro in s;s=s.replace(oldintro,newintro)
s=s.replace('We have not established an advantage over MAE through a dedicated comparison.','We have not established an advantage over MAE.')
s=s.replace('FINAL_PASSAGES_WITH_ORIGINALS.md','FINAL_PASSAGES_R2.md')
s=s.replace('这些十处（含Huber）的同一粗略分词记录是603→374词，**只说明篇幅变化，不是质量分**。是否更好由事实、回应和拼接检查判断。','这轮不是只追求最短。T03接受了略长的新合并稿，让regular pitch–time grid对卷积的实际用处更清楚；N02删掉紧邻表格的四个数字复述，metric purpose集中在N03。T01写明note content and timing，T07补on the target recordings。七处准确diff见[返修回应](WRITER_REVISION_RESPONSE_R2.md)。')
s=s.replace('结论不需要说“这些限制不是没完成”“未来方向不是在修补论文”。推荐删三处防御语气，实际限制与未来工作全部保留：','结论保留原首句“The thesis has several boundaries.”，只删后面的防御句，避免把scope boundaries重新归类成limitations。另两处也只去防御语气，实际范围和未来工作保留：')
s=s.replace('[两轮实际批评与核验](WORKSHOP_METHOD_AND_RESULTS.md)','[本轮外部C1回应与准确diff](WRITER_REVISION_RESPONSE_R2.md)')
s=s.replace('N01/N02/N03三个解释段与N07表格标记一起看；','N01/N02/N03三个解释段与N07表格标记一起看；N03用“For label-free guitar evaluation, we use…”说明目的，避免“therefore”的推论姿态。')
s+='\n组合整段预览带入的v4依赖另列在[DEPENDENCIES_R2.json](DEPENDENCIES_R2.json)。这些不是本轮新发现，也不是作者已批准。\n'
(out/'EDITORIAL_RECOMMENDATIONS_R2.md').write_text(s)
(out/'evidence/BOUNDED_EXCERPT_REVIEW_PARENT_R2.md').write_text('''# 父级报告的有界excerpt review：单独归属\n\n来源：本任务收到的父级delegation消息，报告模型为GPT-6.1-sol。此writer未自行调用或独立核验该模型运行。它是bounded excerpt review，明确未访问full thesis、annotation或table，不是full-source verification，不计作外部完整审查轮次。\n\n父级报告的序位（precision / clarity）：N01 4/4；N02 4/4，保留renderer/gain区分；T11 4/3，qualifier逻辑上不必然断言未做实验，但有不必要的history歧义；N03 4/3，去therefore；N04 4/3，现有can-divert可用，另一个reflect-mismatch写法仅可选；N05a 3/4，最低风险保留boundaries首句；N05b/c 4/4。无总分、平均、质量百分比。\n\n本轮取舍：T11去qualifier；N03改目的句；N05a恢复原首句。N01/N04/N05b/c保留。N02的renderer整体干预区分保留；去数字复述来自full-source外部C1意见，不能把这项依据追溯成bounded review已核验原表。\n\n完整源语境的外部C1依据独立保存在evaluator_cycle1.md/post_reveal.json；下一次外部全文语境复核尚待进行。\n''')
print('Wrote R2 response with seven exact diffs, new compact overview and separate bounded-review provenance.')
