# 外部C1后：七处定点返修，等待第二轮评阅

**正文未动，旧稿和旧决定均保留。** 先前重审43组／97条路线，完成两轮内部子代理评阅；现在已根据第一次外部独立评阅，对七处作真实返修。第二次外部整段评阅仍待完成，这一版不是最终共同裁决。T10继续用v4，Fig6.2等有依据的KEEP保留。

## 1. 新发现：有三句话需要比v4更精确

**Huber：** 你真实PDF批注说尚未确立优于MAE，旧推荐却写成没有做过比较。改成：

> We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE.

公式、β=1和1:1权重保持原样。[准确原文／改稿](FINAL_PASSAGES_R2.md#t11)。

**Ch6指标：** 原稿用r和cosine不同响应量尺的gap，证明cosine“不敏感”；又把换SoundFont的MAE变化归因于absolute gain。这两步推理都超过表格本身。推荐保留全部数字，写清两种similarity都将GT排在flat之上，SoundFont比较改变的是renderer整体。

> Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

N01/N02/N03三个解释段与N07表格标记一起看；N03用“For label-free guitar evaluation, we use…”说明目的，避免“therefore”的推论姿态。表格只去掉跨指标的“最佳／次佳”数值强调，12处格式包装被移除，**每个数字完全保留**。[完整一致性组](FINAL_PASSAGES_R2.md#n01) · [表格副本提案](N07_TABLE_MARKUP_PROPOSAL.tex)。

**背景同步：** v4只收紧了Ch6，Ch2仍说无关因素必然主导梯度。现在只把该从句改成条件表述：[N04](FINAL_PASSAGES_R2.md#n04)。

## 2. 更像你的方式：先把具体事情讲明白

真正论文样本的顺序通常是：实际问题 → 输入与目标 → 选这个方法的理由 → 结果和范围。少加“the deeper thesis result”式宣言。v5保留术语、参数、引用和正面结果，只缩掉重复解释。

| 需要解释什么 | v5的处理 | 看英文 |
|---|---|---|
| weakly expressive / weak supervision | 两种信息条件分清，保留Ch6实例和可重叠性 | [T01](FINAL_PASSAGES_R2.md#t01) |
| Ch6与S2/S3的关系 | guitar＋aligned notes＋间接监督；audio-only velocity仍是未来 | [T02](FINAL_PASSAGES_R2.md#t02) |
| image-like与piano roll | 二维邻域、binary input、single-channel output；直接回应note-list取舍 | [T03](FINAL_PASSAGES_R2.md#t03) |
| modular correction | 邻段已有用途；只补joint note-detection收益未测这一个边界 | [T04](FINAL_PASSAGES_R2.md#t04) |
| change-point head | 承认level变化也能给边界，解释为何显式监督 | [T05](FINAL_PASSAGES_R2.md#t05) |
| real-audio adaptation | 不用未经比较的simple/efficient，也不说域差异消失 | [T06](FINAL_PASSAGES_R2.md#t06) |
| DDSP fidelity | 保留退化观察与未单独测量的边界，更短地说明 | [T07](FINAL_PASSAGES_R2.md#t07) |
| paper与thesis贡献 | 四篇研究与共同综合说清，会议清单交给Declaration | [T08](FINAL_PASSAGES_R2.md#t08) |
| 泛化范围 | 保留piano/guitar已测、其他乐器未测、renderer-conditioned解释 | [T09](FINAL_PASSAGES_R2.md#t09) |

这轮不是只追求最短。T03接受了略长的新合并稿，让regular pitch–time grid对卷积的实际用处更清楚；N02删掉紧邻表格的四个数字复述，metric purpose集中在N03。T01写明note content and timing，T07补on the target recordings。七处准确diff见[返修回应](WRITER_REVISION_RESPONSE_R2.md)。

## 3. 再做一点减法

结论保留原首句“The thesis has several boundaries.”，只删后面的防御句，避免把scope boundaries重新归类成limitations。另两处也只去防御语气，实际范围和未来工作保留：[N05a–c](FINAL_PASSAGES_R2.md#n05a)。

两处“十秒≈四小节≈完整乐句”的解释也可直接删除。v4修正了小节数，但“完整乐句”的推断仍可能留下。保留实际测试过5/10/15/20秒及10秒最好的结果：[N06a–b](FINAL_PASSAGES_R2.md#n06a)。

<a id="keep-list"></a>

## 4. 明确保留，不为显得改得多而动

- **T10沿用v4听测结果稿。** 新稿没有明显更好。保留mean similarity、11位听者、8段、一个PianoTeq配置及composer分组范围；v4已修正Conclusion的“sequence-oriented”比较对象，不能把它当本轮新发现。
- **Fig6.2原图／caption。** 已说targets来自SoundFont-rendered audio；v4补充已推荐KEEP，本轮确认保留。
- **现有Ch3–6导语和总结结构。** 不再追加四段相同的thesis定位；只修具体scope/术语。
- **O/F/V定义、loss公式、β/权重、frontend配置、表格实测数字。** 这些细节长一点仍有用。
- **GRS的状态纪律。** 原草稿没有虚称这轮修改已完成；保留其内部核验用途，不把逐项工作流记录放在第一屏。

## 真正有区别的备选

默认推荐上面的短稿，不强求每一项再看ABC。

- **T03想少谈note list：** 匿名备选N以grid、binary input、single-channel output为主；读起来更窄，但对评审的representation比较回答较少。[两种全文](CANDIDATE_PACKET_BLIND_C1.md#t03)。
- **T08想让四篇mapping一眼可见：** v4 B把会议与章节逐一列出，较长但更明确；短稿让Declaration承担已有清单。
- **N05只是语气偏好：** 原段事实未被否定；可以保留原文。我的推荐是去掉这些防御句。

## 现在仍需要事实，而不是继续润色

正式送审PDF基线、听测timing处理、实际run／checkpoint／表源、Ch5 averaging与decoding是否用于最终run、吉他Fig6.3 GT来源、ICASSP最终版本仍未确认。R1-13/21/26/30的事实依赖继续开放；新文字不让它们自动变成ready。

[精确原文与全部最终英文](FINAL_PASSAGES_R2.md) · [43组重新筛选](evidence/ALL_43_REAUDIT_INDEPENDENT.md) · [声音依据](VOICE_CARD_BRIEF.md) · [本轮外部C1回应与准确diff](WRITER_REVISION_RESPONSE_R2.md)

组合整段预览带入的v4依赖另列在[DEPENDENCIES_R2.json](DEPENDENCIES_R2.json)。这些不是本轮新发现，也不是作者已批准。
