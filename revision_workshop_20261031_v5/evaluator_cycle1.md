# 外部独立评阅 C1：需要定点返修，再做第二轮

本轮已实际比较匿名包的 **15 段、60 个候选**，先保存 `evaluator_cycle1_provisional.md` / `evaluator_cycle1_blind_rankings.json`，随后才读 provenance、writer 推荐与最终选稿。采用预先冻结的六维 **1–4 序位**，没有采用内部评阅的 0–3 五维量尺，没有总分或质量百分比。来源标签隐藏，但熟悉的原文可能被认出；不是双盲。

**结论：当前选稿没有保留被本轮排除的事实论断；仍建议按下列具体理由返修，不应直接宣称完成两轮外部评阅或已经全文达成一致。** 这是一次外部评阅，写作任务先前的两轮属于其内部子代理流程。正式修订基线、run/GT 和四项证据依赖没有因此解决。

## 先改这些具体地方

### A. T03：理由应解释 grid 的用处，而非只说网络需要二维输入

Writer 选 T03-M；匿名时我和 source-only voice 评阅者均偏好 N。M 的 “We use piano rolls because the U-Net processes two-dimensional…” 接近接口上的循环解释；“A note-list representation would require a different model interface” 是真实代价，但不足以单独说明 grid 的好处。不是事实硬门槛失败，是对评审问题的回答还可以更具体。

建议用下面的合并稿，允许为必要信息多几个词，不追求最短：

```latex
We use a piano roll to place simultaneous notes and local pitch--time neighbourhoods on a regular grid for the convolutional U-Net. The input is binary; the single-channel output supplies velocity values, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
```

保留后文 F input / V target / O mask，不再添一段未经做过的 event-model 对比。

### B. N02/N03：解释选择，少抄数字、少写推论姿态

N02 的最终文字正确地否认 gain-only intervention，但重抄紧邻表格的四个 delta 没有必要。还发现一个**来源显示精度提示**：表内报告 BSSL MAE delta 为 0.193，显示的端点 0.702−0.510 为 0.192；可能来自舍入，不能认定数据错误或静默改数。

N02 推荐替换：

```latex
Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.
```

若作者要保留四个数字，至少称 “the reported changes”，不声称重新从显示值计算。**表格数字全部保持不变。**

N03 当前 “We therefore use…” 不再声称通用优越性，已过事实门槛；但刚否定 gap 的优越性证明后，用中性目的句更顺：

```latex
For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

N01 的 C2 最终两句已经优于原匿名 L：不再笼统说 “different scales”，不必再改。N01/N02/N03/N07 作为同一解释与格式组对读；N04 是相关背景同步。不能只采一段，把旧 “fail on sensitivity and robustness” 留在后面。

### C. N05a：KEEP 原首句，删除防御句即可

Writer 将 “boundaries” 换成 “limitations”。边界包括研究目标和输入条件，未必全是缺陷；此次任务不需要重新分类。我的最小建议是原首句胜出：

```latex
The thesis has several boundaries.
```

只删除其后的 “not artefacts of unfinished implementation…”；具体限制照旧。N05b 和 N05c 的去防御处理可用。这三项均应标为编辑选择，而非 examiner 必须逐字采用的修改。

### D. 三处很小但有意义的精确化

- **T01：** “retain note structure” 改为 **“retain note content and timing”**，明确对应作者实际定义，不增加新分类。
- **T07：** 最后一句加回 **“on the target recordings”**，将未单独测量限定在当前目标数据，避免被读成这些 synthesiser 从未受过任何保真评估。推荐末句：

  > The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.

- **T11：** 当前最终措辞与真实 PDF 回复相容，不属于“虚构未做实验”的旧错。但第二句还可直接精简为：

  > We have not established an advantage over MAE.

  保留第一句的 smooth-gradients / L1-like rationale，β、权重和公式不变。这里是降低语言歧义，不是宣称当前句事实错误。旧候选 T11-N 的 “We did not conduct…” 在本轮标 **UNRESOLVED**：无充分依据断言实验史，不等于已知它必然为假。此前 evaluator baseline 中相同的 categorical 建议也应由这个更谨慎的表述取代。

## 哪些稿应保留，不再为短而重写

- **T10 保留 v4。** 我匿名偏好更短的 N，writer 选择 L（揭示后为 v4）。两者内容都可靠；L 明确保留 selected SMD scope、mean similarity、11/8/one rendering 和 composer grouping，没有实质缺点，不必为七个词另造一轮。保留旧稿是合理结论。
- **Fig.6.2 原 caption / 图继续 KEEP。** 当前已经说明 SoundFont-rendered targets，且 v4 已推荐 KEEP；不是本轮新功劳。
- **T04 最终稿保留。** Writer 已将候选 K 的重复第一句删掉，只补 joint-modelling benefit 未被该评价测量；这正好解决局部缺口。
- **T05、T08 保留最终稿。** 显式 boundary/state 监督的区分具体；四篇共著研究与 thesis synthesis 也说得清楚，没有虚报全部内容的论文归属。
- **T06 保留 writer L 可接受。** 本轮 voice 子评阅者偏好 M+piano-pretrained，我在匿名时偏好 L；都过硬门槛。L 的 renderer limitation 虽与下一节相近，但并不构成需要强制再改的缺点。
- **T09 的 Second 已恢复，保留。** 不把匿名候选的枚举缺口再当成最终稿缺点。
- **N06a/b 两处删除可用。** 保留测试的 5/10/15/20 秒与 10 秒最佳结果，不再用四小节/完整乐句的猜测解释结果。
- **O/F/V、loss、β/权重、frontend 设置、实测表值继续 KEEP。** 技术分工的信息不因长一点而低分。

15 个故意选出的争议段落中，没有 unchanged paragraph 或 no-add 作为原样 winner；不能为了制造 KEEP 比例硬选。上述原首句、旧 v4 听测、图注与技术定义是具体、可说明理由的保留结果。

## 每段匿名选择与最终判断

详细 60 行门槛、六维评分和逐候选理由见冻结文件；这里记录揭示来源后的判断，不能回填改写匿名分数。

| 段落 | 冻结 winner / runner-up | writer 选择 | 外部 C1 最终意见 |
| --- | --- | --- | --- |
| T01 | L / K | L，新稿 | 用 note content and timing 精确化；其余保留。 |
| T02 | K / L | K，新稿 | 保留；必须同时带入已有 S3/scope 同步。 |
| T03 | N / M | M，新稿 | 请求 A 的实质合并改写。 |
| T04 | K / N | K 经删句 | 最终比匿名 K 更好，保留。 |
| T05 | M / L | M，新稿 | 保留，不追加没有 ablation 的免责声明。 |
| T06 | L / M | L，新稿 | 保留；不恢复 simple/efficient/domain-gap 消失。 |
| T07 | M / L | M，新稿 | 加 on the target recordings。 |
| T08 | L / M | L，新稿 | 保留；不等于完成 exhaustive novelty inventory。 |
| T09 | L / N | L 已恢复 Second | 保留；连续控制的扩展需求不等于否定其他 onset-only 任务。 |
| T10 | N / L | L，v4 | 接受 v4 保留，读者不需要为微小偏好换稿。 |
| T11 | L / K | L，新稿 | 可缩短第二句；不推断是否做过全部比较。 |
| N01 | L / K | L 经 C2 改写 | 保留实际 C2 最终两句。 |
| N02 | M / N | M，新稿 | 请求 B 的去数字重复改写；数字留在表中。 |
| N03 | L / M | L 经精简 | 请求 B 的目的句改写，避免因此/优越性联想。 |
| N04 | N / M | N，新稿 | 条件从句可用，保持 comparison-space 其余文字。 |

匿名硬门槛统计只是处理记录：**48 PASS、11 FAIL、1 UNRESOLVED**。PASS 不证明运行记录或原始数据真实性。11 个被排除者分别是 T06-N、T07-N、T10-M、N01-M/N、N02-K/L、N03-K/N、N04-K/L。T11-N 为 UNRESOLVED。重复文本对获得相同判断。

## 不是本轮新缺陷：v4 已有的同步必须继承

独立 baseline 首先看源文，所以会发现源文错误；揭示旧提案后必须区分“源文仍未改”与“旧方案没发现”。

| 问题 | 已有提案的实际证据 | C1 的处理 |
| --- | --- | --- |
| Conclusion 的 sequence-oriented 听测对象 | `revision_blueprint_20261031/writer_round3.md:2072` 已拟为 Flat and ConvAE；Ch3:457 的 verifies 也在同项同步 | **已修于 v4 提案**。不是本轮新发现，不再另造重叠文本。 |
| Ch6 gradient-budget / crop-length 因果语气 | `writer_round3.md:1579` 起已给 can be influenced、consistent with / not isolated 等逐句操作 | **已修于 v4 提案**。N04 新增的是 Ch2:587 漏掉的 unconditional dominated。 |
| 引言 physical velocity、S3 removes all support、beyond-piano 目标错位 | `SUPPLEMENTS_v4.md` 已列定义八处、S3 和 scope bullet 的准确操作 | **已修于 v4 提案**。不能只整合 v5 新段而丢掉这些前提。 |
| Fig.6.2 rendered-audio caption | `SUPPLEMENTS_v4.md` 的 KEEP 明确且有现图依据 | 继续 KEEP，不称新发现。 |
| Huber “did not conduct” | v4 的匿名候选确有该句；真实 PDF 回复只支持未建立优势 | **v5 有实质修正**，继续采用精确证据边界。 |
| Pearson/cosine gap、gain-only 推理、末段 fail 判断、表格强调 | N01–N04 incumbent 的 v4/原文重复已核对 | **本轮超出 v4 的有用发现**；N07 同组格式处理有理由。 |

这些都是**未实施提案**，不是已修改 thesis。当前 reinserted excerpts 仍包含部分旧 scope 句，应在读者整合时显示依赖或共同后的实际上下文，不把单一候选的引用匹配叫作全文已经一致。

## 两轮“独立”评阅的实际证据审计

不只看了 writer 自述。通过只读 thread 记录核对到：

| 实际层级 | 可核验记录 | 合理称法 |
| --- | --- | --- |
| writer 内部 C1 | `/root/blind_cycle1`，thread `01a191f2-d386-73c8-8e9d-6c6525a5703c`；最终回复交付 BLIND_CRITIQUE_C1；文件有 15 行、60 候选槽的五维 0–3 判断与实质退回 | 一位本地子代理的匿名标签评阅；其 metric_audit 子代理另核查 N01/N02，不算第三轮完整审查。 |
| writer 内部 C2 | `/root/source_checks`，thread `01a191ef-b3c9-70dc-b742-dd4962cf400b`；先前做过源头检查，另一 turn 明确交付 21 项 CRITIQUE_C2 | 与 C1 不同的本地子代理做非盲拼接复核；不是新外部 evaluator，也不是对原资料完全无先验的读者。 |
| 本次外部 C1 | 当前独立 evaluator，先建 source-only 基线，再冻结 60 候选分数；本地辅助评阅各核查 24/36 候选 | 与 writer 分开的第一次外部评价；本次辅助子代理不另算外部完整审查轮次。 |

保存的 C1/C2 不是空泛通过记录：C1 淘汰过未证实因果、改 T04 重复、要求 T09 恢复 Second、要求 N01–N03 联动；C2 的 N01 修改已在 FINAL_SELECTION 落实。两个报告及不同 agent 记录支持 writer 确实做了内部两轮，不能将其说成两轮外部独立评阅。WORKSHOP_METHOD/WRITER_HANDOFF 后文已区别内部与当前外部；用户入口首段仍建议明确写 **“两轮内部子代理评阅”**，不要让“独立”承担比证据更大的意思。

我也使用两个本地辅助评阅者分别核查 24/36 候选；他们没有读 provenance 或 writer 推荐。大部分判断一致；T06 的顺序等存在真实偏好差异，未通过平均或多数票生成质量分。两者都不能为“凑原文胜出比例”找到合理的 no-add winner。

## 程序核验及其边界

- 冻结后匿名 packet SHA-256 未变；60 个候选文本 hash 均匹配评分记录。
- 最终 20 个 source operations：16 个原文唯一匹配，4 个真实 insertion；锚点均唯一。此核验不代表每条事实已独立证明。
- N07 表内 **58 个 numeric tokens 顺序完全一致**；12 个数值 bold/underline wrappers 变为 0。核验明确限定 table 环境，避免把 proposal 注释里的 Chapter_6 当成表值。没有重算指标或改变数字。
- 原有 **19 个源文件、80 个旧提案文件**与 source-only baseline 的 hash 一致。
- 核查工具为本地 Python/regex/hashlib 与已保存 PDFKit 提取证据。未联网传论文、安装工具、运行实验、编译正文或改源文。

见 `evaluator_cycle1_verification.json` 及可复跑 `evaluator_cycle1_verify.py`。冻结分数和此后建议分别保存，防止揭示来源后改写初判。

**下一步：** 让 writer 对 A–D 做实际、有理由的取舍和返修，保留本轮不同意见；之后进行第二次外部评阅。Reader integration 仍待真正形成一致意见，不因内部 C2 或本次多数接受而自动变成 jointly reviewed。正式基线、R1-13/21/26/30、run/GT 与最终 ICASSP 版本继续开放；不扩大实验或 thesis 范围。
