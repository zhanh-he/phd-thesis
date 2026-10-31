# 独立评阅基线：先看原稿，再判断修改是否值得

阶段：source-only baseline。此次尚未阅读旧提案的推荐、通过记录或 v5 writer 候选；也未修改论文、旧提案或 writer 文件。下列文字是评阅意见和可选替换句，不是已采用的正文修改。

## 先看值得真正处理的例子

### 1. 听觉结果不能从客观基线顺手扩大

结论原句：

> “yet the listening test shows a clear improvement over flat and sequence-oriented baselines.”

位置：`Chapter_7/Conclusion.tex:50`。但 `Chapter_3/chap3.tex:369` 明确列出的听觉系统是 U-Net、ConvAE 和 Flat；`375–379` 说明是八段 SMD performance MIDI、各十秒。Seq2Seq 在客观比较中出现，不等于参加了该听觉实验。

建议只替换结论中的对应一句：

> The listening test provides supporting perceptual evidence for U-Net over ConvAE and flat velocity on the eight piano excerpts tested.

这比新增一段泛泛的“样本量局限”更有用：先说清比较对象，再在 Chapter 3 的结果或局限处交代 11 位 expert listeners。不要在每个总结里重复样本数。该句只概括文内报告的结果，不独立证明统计显著性。

### 2. 一般 velocity 定义应与自己的 ISMIR 论文一致

引言把 MIDI velocity 写成 “independent, static integer representing its initial strike force”（`Intro.tex:89`），另称 “a universal loudness variable for all instruments”（`Intro.tex:62`）。这将 piano 的物理直觉扩成一般定义，也与 Chapter 2、Chapter 6 的 renderer dependence 不一致。

ISMIR 论文第一页的语言锚点是：

> “MIDI velocity is the per-note control parameter in symbolic music systems, controlling expressive aspects of rendering such as amplitude and timbre.”

可用的简明替换：

> MIDI velocity is a per-note control parameter that affects the amplitude and timbre of rendered sound. Its effect depends on the instrument and renderer, so it is related to, but not interchangeable with, loudness.

如需解释 piano 标签，再另用一句说 sensor-equipped piano recordings；不要把 physical strike force 留作所有乐器的定义。既然改定义，也要检查表格 `Intro.tex:82` 的 “Physical measurement”，否则只改一段会留下冲突。

### 3. “more efficient route” 也没有消除原问题

作者确实在批注中提出把 “simpler route” 改成 “more efficient route”（Report 1，Chapter 6.1）。但现有回复没有提供效率比较。更稳妥的做法是直接描述区别：

> Instead of training the estimator on synthetic audio, we adapt it against real recordings through a differentiable renderer interface.

`Chapter_6/chap6.tex:31` 的 “avoids the synthesis-to-performance domain gap” 也需收敛；该章后面仍讨论 renderer mismatch。不能借着换词暗示这类差异已经消失。

### 4. 有些原文应该直接胜出

当前 Fig.6.2 caption 原文（`Chapter_6/chap6.tex:204`）：

> An encoder-only Transformer maps padded note sequences to per-note PHE/OSF targets extracted from SoundFont-rendered audio.

已经交代了 targets 来自 rendered audio。优先 KEEP；先核对评审实际看到的版本，不能因旧评审曾问过就继续扩写。当前 `V^{(0)}` 与 `hat V` 也已在 `Chapter_6/chap6.tex:93` 同段解释。两项均不能据此认定正式送审 PDF 的问题已经解决。

### 5. 一些复杂句是在为论文辩护，未增加研究内容

结论：

> “These boundaries are not artefacts of unfinished implementation;” (`Conclusion.tex:109`)
>
> “These directions extend the thesis argument rather than repair it.” (`Conclusion.tex:124`)

建议分别只留正常引导句：

> The thesis has several limitations.
>
> The results suggest several directions for future research.

这不是把作者改成更冷淡的声音，而是去掉读者无需知道的审查姿态。类似的 “These assumptions are not weaknesses of the argument” (`Conclusion.tex:117`) 也不必保留。

## 作者语气：主要模仿什么

主要锚点采用本人领衔、已发表或已接收论文的真实学术 prose，并以 thesis 中具体方法段落交叉确认。共同署名论文可以证明既有学术写法；不能证明每句话均由本人独立起草，更不能声称已识别稳定的个人语言指纹。

| 可观察特点 | 真实例子 | 后续改写准则 |
| --- | --- | --- |
| 先给具体任务和对象 | SMC 第 1 页：“By contrast, our work focuses on refining the MIDI velocity predicted by AMT systems.” | 先写 audio、notes、score、velocity，再引入抽象论点。 |
| 正常学术第一人称，动词明确 | CMMR 第 1 页：“In this paper, we introduce the U-Net” | 可以保留 we use / propose / adopt / evaluate，不必全部改成 this thesis argues。 |
| 用一句说清范围 | CMMR 第 1 页：“Current dataset availability restricts our experiments to piano data.” | 边界放在相关结果旁边；不要连续加入并非普适、仍有价值、不否认其他方法等句子。 |
| 方法细节可以长，只要各句有分工 | Ch3:51–55 依次说明 O/F/V、input/target/mask、normalisation 和 post-processing | 精简不等于删掉能复现方法的区别。 |
| 以条件限定结果 | SMC 摘要使用 “Under this training protocol” | 保留范围限定；不将当前最优写成通用最优。 |

不应机械模仿的内容：回复批注中的拼写和语法错误；总论中反复出现的 “deeper thesis result”“thesis stance”等抽象姿态；未验证的强比较和宣传性形容词。作者批注主要用于确认真实意图与未知项，不是逐字仿写的英语模板。

### 两处更像已有论文的定点写法

`Intro.tex:45`（含 recollecting 及 entirely bypass 等扩张表述）：

> Collecting new datasets is costly because audio–score synchronisation, musical expertise, and copyright clearance are required. This thesis therefore studies how missing dynamics labels can be recovered from existing music data.

保留对应引用；不再声称消除了 annotation ambiguities。

`Intro.tex:153` 的 beyond-piano scope 错写成 non-piano **score-dynamics**：

> Chapter 6 explores MIDI velocity estimation beyond piano using guitar recordings. Broader transfer to other instruments remains future work.

这项是目标对齐修正。不是新增其他乐器实验，也不能使 voice、bowed strings 或 winds 自动成为已验证范围。

## 独立优先级：必须回应、可保留、不能当作已证实

### 优先处理

1. **精确纠正定义与目标。** weakly expressive / weakly supervised 给出本论文操作性定义；区分 velocity control、loudness、score markings；Chapter 6 必须保持 audio + aligned notes 的输入条件。Chapter 3 从 fixed notes 推测 plausible velocity，不能宣称还原唯一原表演。
2. **说明清楚而非扩展研究。** loss 的实际系数、共享/独立 head、change-point 与 beat 的 post-processing、表格条件和图中颜色应准确说明。图注无法确定的信息留待证据。
3. **补一份简短 publication → thesis 对应说明。** Report 2:84 要求区分 published、adapted、thesis synthesis。先核对论文版本和真实差别，不能仅因某段在论文未找到就宣称“新增实验”。
4. **把结果约束在证据内。** 11 位听者和八段 piano excerpts 提供支持性证据；MAESTRO→SMD 不是单独隔离的 composer/style 实验；跨 piano corpora 也不是跨乐器证明。
5. **做跨段一致性修正。** “most controlled / most constrained” 不应只改 Ch3 opening；需同步 Ch3 problem、summary、Conclusion。引言 velocity 定义也须同步表格和动机段中的相同错误。
6. **优先做必要的语言和图表修正。** collecting、已接受的论文状态、可核查的图例、表格分组与清楚的指标引用。最终排版问题应在确定基线后渲染检查。

Report 1 赞扬整体语言与叙事；Report 2:15,122 明确不需 major rewriting、additional experiments 或 new data。新段落必须能说清解决哪一个真实歧义。

### 有依据的 KEEP / 小改

- Ch3–6 的现有章节 opening 已说明各章条件和目标；只补缺少的连接，不每章重写 opening 再重复 closing。
- Fig.6.2 当前 caption 已说明 SoundFont-rendered targets；`V^{(0)}` / `hat V` 已局部定义。版本核对优先于再次解释。
- Ch3 的 O/F/V 输入、目标与 masking 分工应保留；这类细节不因字数较多而低分。
- Ch6 已有 piano/guitar、attack-driven 参数、manual SoundFont selection、aligned note events 的边界；更清楚即可，不再跨章反复堆 caveats。
- Ch5 已说明五个静态标签与 blank，以及 crescendo/diminuendo 尚未建模；应先看当前内容，再决定补在哪里。

### 不得从作者回复升级成完成结果

| 问题 | 当前证据边界 | 安全表述或动作 |
| --- | --- | --- |
| quantised-score 应用 | 作者批注说 listening test 用 score-MIDI，但 Ch3:375–379 明说 SMD performance MIDI 去掉 velocities | 两者冲突，待核查 stimuli；不能说已验证 quantised-score 使用。 |
| Ch4 loss balance | 方程是两个各自平均的项以相同系数相加；作者说 verified，但未给比较记录 | 说明 equal coefficients，不声称梯度相等、最优权重或完成 ablation。 |
| beat/downbeat coupling | Ch5 共享 encoder/experts，独立 heads/losses；change points 显式 snap to beats | 不把共享表示或 CPt snapping 写成已验证的 beat–downbeat consistency rule。 |
| generalisation | 作者承认没有平衡 composer/performer 的数据；Ch5:377–383 同时涉及 acoustic/repertoire/label-prior shift | 描述 cross-dataset results，不写成独立证明 composer/performer invariance。 |
| Diff-Synth fidelity | PDF 真实批注明说未分别测 fidelity 与 velocity-gradient accuracy | mismatch 是 plausible explanation，不是被独立确认的因果机制。 |
| Huber vs MAE | PDF 真实批注明说没有 dedicated comparison | 解释 smooth quadratic/linear transition 和 beta=1，不说胜过 MAE。 |
| guitar GT 图 | Ch6:442–447 使用 ground truth；真实 guitar 目标标签又被说成不可获得 | provenance 未核实，相关句不能作为 ready-to-paste 最终事实。 |
| full AMT / note accuracy | 讨论可接入，不等于已经完整集成和评测 | 未来工作或工程可能性，不新增 improved note transcription 结论。 |

另一个小而明确的问题：Ch3:71 用 “roughly four measures at 120 BPM” 解释十秒；未给拍号，不能用来证明 window 与乐句吻合。4/4、120 BPM 下四小节是八秒。可仅写 “A 10-second segment performed best among the tested durations.” 不加一个未经测量的机制故事。

## 后续候选的评分方法（冻结于看提案之前）

事实/语义保真先过硬门槛：**PASS / FAIL / UNRESOLVED**。PASS 是与已核验材料相容；不是对所有实验真实性的独立认证。FAIL 包括错误比较对象、增添未做实验、把猜测写成机制结果；UNRESOLVED 用于基线、run、GT provenance 或明确缺证项，不能装作已通过。作者语气再好也不能弥补硬门槛失败。

通过后分六个维度做 1–4 的序位判断，不报小数、加权总分或客观质量百分比：

| 维度 | 4：可直接取用 | 3：局部修改后可用 | 2：需要实质重写 | 1：不应选 |
| --- | --- | --- | --- | --- |
| 回应评审 | 完整解决具体疑问，保留原研究边界 | 回应正确但一个细节或位置待调 | 只回应一半或将问题绕成泛论 | 没回应或答错 |
| 作者语气 | 具体对象和方法动作，与已提交论文接近 | 有少量抽象/模板表达 | 连续立场宣言、宣传或防御句 | 研究内容被泛话替代 |
| 局部与全文衔接 | 放回前后段自然，术语和 scope 全文一致 | 一个交叉引用或重复需处理 | 多处冲突或重叠 | 改后逻辑不成立 |
| minor-revision 必要性 | 用最小充分改动解决问题，KEEP 也可得 4 | 有少量可删解释 | 改动与问题明显不成比例 | 无收益或扩大任务 |
| 可读性 | 输入→动作→结果/边界清楚，读一遍能懂 | 一句可简化 | 读者需回读才能找主语或条件 | 关键含义无法判断 |
| 篇幅与信息密度 | 每句有新的必要信息，长短与任务匹配 | 一处冗余 | 多句重复 caveat 或重复定义 | 主要是审计话语/填充内容 |

**锚点而非现成全篇评分：** 当前 Fig.6.2 caption 在内容、可读性、必要性上可 KEEP（4）；“more efficient route” 在比较证据不足时为 UNRESOLVED，不能靠语言分入选；把 comparison 改为 U-Net/ConvAE/Flat 的短句解决了具体语义错误，比保留宽泛 sequence-oriented 更优；详细 O/F/V 方法段虽长仍可得高信息密度分。

后续比较 ORIGINAL / prior / fresh 时，先由不知来源的阅读者按匿名候选排相对顺序，尽可能先隐藏作者和推荐标签，再揭示来源核验原句和全文。若评阅者已认出来源，必须注明非盲评，不能声称双盲。各维度允许不同候选胜出；最终可保留原句、取旧稿，或要求新的局部写法。暂未给 v4/v5 任何质量分。

## 本轮工具做了什么、没有证明什么

- 用本机 PDFKit 直接提取两份报告、两份现存 thesis PDF，以及 CMMR、SMC、ISMIR 的实际 PDF 文本；没有上传或外传。
- Report 1 有 50 个含 contents 的 annotation objects，去重后 **25 条真实批注**；全部与 Markdown 回复逐字吻合（仅去掉 Markdown `>` 与折叠空白）。这验证回复转写，不证明回复中的事实。
- Report 2 无批注；其 Markdown 占位 “not response yet” 不是作者写下的回复。
- `Z_He_PhD_Thesis.pdf` 是 **154 页**，`main.pdf` 是 **155 页**。已记录各文件 SHA-256；未认定哪份是正式送审基线，也未认定 LaTeX 与任何 PDF 完全对应。
- Python 标准库脚本核验 **11 处关键引文**的精确源文本，并保存源文件与旧提案目录的只读指纹。后续可以独立复查，不依赖评阅者记忆。
- 关键词与重复计数仅用于提示回读，不是 author-voice 检测器，不用可读性公式为技术论述下判决。默认 Python 未提供 proselint/LanguageTool/PyMuPDF；未安装未知工具。用已安装系统 PDFKit 和开源 Python 标准库完成所需检查。

工具：`evaluator_extract.swift`、`evaluator_baseline_checks.py`。检查结果：`evaluator_baseline_diagnostics.json`。原始提取 JSON 留在本次 evaluator 工作区，避免把全文又复制成新的用户入口。

**仍未解决：** 正式修订基线；run 与 GT provenance；任务明确指定的 R1-13/21/26/30 四项 evidence-pending 状态。此轮没有读取旧 item map，故不擅自将这些 ID 重新解释为报告的小节号。未做实验，未改结论，未宣布任何待核项已经完成。下一步等待 writer packet 后做两轮有争议候选的实质比较，而非重复盖通过章。
