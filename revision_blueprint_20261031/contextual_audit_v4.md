# 全文语境补查 v4：三组值得补的小修，其余收住

**仅新增建议，尚未独立审查、未经作者选择、未实施。** 冻结的第三轮仍以 [最终独立核验](reviewer_final.md) 为准：39项文字可选、4项事实待核。本文件不替换第三轮，不另设决定入口；由编辑决定是否把下面三组送入定点复审和唯一选择表。

位置均指当前 LaTeX；与正式送审 PDF 的版本绑定仍待确认。本次把43项推荐与其源文前后段落对读，并重点重读 Abstract、Introduction、各章开头／讨论／结尾及最终 Conclusion。检查的是拼接后的论证与阅读，不是再做一次方法事实认证。新增问题均来自未改源码的上下文，不能算作 examiner 新提出的意见，也不能写进 GRS 为“已修改”。

| 优先级 | 值得做什么 | 关联原ID | 对 KEEP ORIGINAL 的判断 |
| --- | --- | --- | --- |
| 1 | 把前言的 velocity 定义与第2／6／7章统一 | R1-09，关联 R2-03 | 原文“通用响度变量／物理强度测量”与后文明确的 control／renderer-conditioned 定义冲突，值得局部修正。 |
| 2 | 修正 S3 与 beyond-piano 范围的两个易误读句 | R1-06、R1-15，关联 R2-03 | 保留原句会把“无外给 score”说成“无结构支持”，并容易让第6章被读成非钢琴 score dynamics。 |
| 3 | 收窄 data-curation 动机里“完全绕过困难”的承诺 | R1-04，关联 R2-05 | 只改 collecting 还留下正文实际承认的矛盾；换末句即可，无须补一段局限。 |

这三组是联动编辑建议，不新增43项之外的审稿问题编号。它们不触及结果、数据处理或实验。其余已审推荐没有发现需要再展开改写的叙事问题；下面另列一项更适合 KEEP 的图注选择。

## 1. 前言用同一套 velocity 定义【新增文字，未审】

**原始上下文**，[Intro.tex:89](../Chapter_1/Intro.tex)，位于“两种互补表示”的 MIDI velocity 段，后接 score dynamics 定义：

```latex
Originating from the physical sensors of electronic keyboards and pianos, MIDI velocity is a machine-centric measurement of physical intensity. To say it operates as a "note-level" parameter means that every music note from a discrete key strike is assigned an independent, static integer representing its initial strike force. This strict per-note measurement dictates that velocity functions as a discrete loudness control parameter. It is highly granular and absolute within its own scale, yet the resulting loudness highly depends on the acoustic environment and the specific instrument being played. Because MIDI velocity is necessary for MIDI-to-audio playback in DAWs and synthesisers, a common default is set to 64 when it is missing.
```

同一节前面的编辑性论据，[Intro.tex:62](../Chapter_1/Intro.tex)：

```latex
Unlike complex continuous controls (e.g., guitar overdrive or piano pedalling), dynamics offers an exceptionally tractable and editable symbolic representation. MIDI velocity is a universal loudness variable for all instruments in digital audio workstations (DAWs), while score dynamics provide a standardised notational vocabulary for composition, pedagogy, and performance analysis \cite{kosta2014dynpiano,cancinoChacon2018computational}. This dual status makes dynamics a robust bridge between low-level MIR outputs and higher-level musical practice.
```

对照已有正文：Background:276 把 piano velocity 定义为 key／hammer motion 的 discretised proxy；:280 明说其 acoustic effect 依赖 instrument／renderer。Conclusion:88 直接称它为 note-level control parameter，:90 明说它不是普适 physical measurement。第6章的研究对象也已定义为 renderer-conditioned velocity。这里应让前言跟随后文已有定义，而不是把后文改成普适物理真值。

**拟替换整个 :89 段：**

```latex
Here, MIDI velocity refers to the velocity value in a Note On message. It is a machine-readable control parameter. In sensor-equipped piano data, the recorded value acts as a discretised proxy for key or hammer motion. Each note carries an integer value that can be edited independently, although its acoustic effect depends on the instrument and renderer. When expressive values are missing, a MIDI sequence may instead use a constant such as 64.
```

**同一组必须随改的短语**，避免只修一段后矛盾仍在：

| Intro 位置 | 原文中的准确短语 | 拟替换文字 |
| --- | --- | --- |
| :43 | a deep semantic gap exists between physical machine measurements (MIDI velocity) and subjective human cognition (score dynamics) | a gap remains between machine-readable control values (MIDI velocity) and context-dependent musical notation (score dynamics) |
| :53 | bridging physical machine measurements (e.g., MIDI velocity) with semantic cognitive notations (e.g., score dynamic markings) | using note-level controls (e.g., MIDI velocity) and contextual notation (e.g., score dynamic markings) |
| :62 | a universal loudness variable for all instruments | an editable note-level control |
| :82，Nature 单元格 | `\makecell[l]{Physical\\measurement}` | `\makecell[l]{Note-level\\control}` |
| :100 | a machine-centric, physical parameter | a machine-readable control parameter |
| :100，末句中的动词短语 | bridge the fundamental gap between objective physical measurement and subjective human cognition | bridge acoustic observations, performance controls, and musical notation |
| :92，整句 | In symbolic environments, the default assumption is often that missing score dynamics should be filled with \textit{mf} (mezzo-forte), which is the neutral middle ground of human perceptual loudness. | 删除这句；前面的 score-dynamics 定义保留。 |

同节 :92 把名义 \textit{mf} 当作人类响度的“neutral middle ground”，也与 Background:265／285 的上下文性和软件名义映射区分不合。删除这句即可，无须添加新的默认值规则或警告段。

这些措辞仍保留作者“表示之间存在差别”的核心立场，只移除错误的物理／认知二分。不动 :18 对 sensor-captured data 的介绍，也不改 Background／Conclusion 已经准确的解释。R1-09 的第三轮 B 在 Background 的 Note On 限定仍可保留；这里是它原操作中允许的 Intro 同步，并非另加一遍协议介绍。**不据此判定吉他图 GT 的来源。**

## 2. S3 估计结构；第6章估计 velocity【新增文字，未审】

**原始完整段落**，[Intro.tex:118](../Chapter_1/Intro.tex)：

```latex
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target. By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.
```

**拟拼接后的完整段落：** S3 句是本次新增；最后一句已是第三轮 R1-15 的联动，不重复执行。中心问题与 table 后第三轮 R1-06 B 的说明均保留原位置。

```latex
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} uses an \textit{audio-only} input to jointly estimate dynamic markings and the metrical coordinates needed for a \textit{score-facing} output. These settings form the core empirical arc of the thesis by varying both the available evidence and the target representation.
```

理由不是说原作者不知道 meter，而是明确区分“没有外部结构输入”与“模型联合估计结构”。Abstract:142、Ch5:11／95、Conclusion:117 已作后一种解释，前言应与之相符。

**另一个原始 scope bullet**，[Intro.tex:153](../Chapter_1/Intro.tex)：

```latex
\item \textbf{Exploration beyond the piano.} Extending velocity estimation beyond the piano is recognised as an important direction to counter the dataset bias in expressive AMT. However, large-scale non-piano score-dynamics transcription with human labels remains outside the scope of the core scenarios, and will only be investigated as an exploratory extension.
```

**拟替换这一个 bullet：**

```latex
\item \textbf{Exploration beyond the piano.} Chapter~\ref{ch:beyondpiano} explores note-level velocity estimation for guitar using indirect supervision. Large-scale non-piano score-dynamics transcription with human labels remains outside the scope of this thesis.
```

原句的“and will only be investigated”语法上接 non-piano score-dynamics transcription，读者可能误以为这就是第6章的探索。新句直接指出第6章的输出是 guitar note-level velocity；后一句保留 score-dynamics 的范围边界。其依据是 Ch6:7–17 及 Abstract:144 的现有任务定义，不是新加结果或跨乐器实验证据。

## 3. 少作一个过强承诺，不加一层 caveat【新增文字，未审】

**原始完整段落**，[Intro.tex:45](../Chapter_1/Intro.tex)：

```latex
By contrast, recollecting new datasets from scratch is a costly process constrained by audio-to-score synchronisation challenges, required musical expertise, and copyright restrictions \cite{li2019urmp,foscarin2020asap,morsi2022bottlenecks}. Therefore, this thesis treats \emph{label recovery} as a scalable, principled strategy. By retroactively estimating missing dynamics on existing corpora, we entirely bypass acquisition bottlenecks and annotation ambiguities, unlocking a vast, previously untapped resource for data-driven music research.
```

**拟拼接后的完整段落：** collecting 已属第三轮 R1-04；本次只替最后一句。

```latex
By contrast, collecting new datasets from scratch is a costly process constrained by audio-to-score synchronisation challenges, required musical expertise, and copyright restrictions \cite{li2019urmp,foscarin2020asap,morsi2022bottlenecks}. Therefore, this thesis treats \emph{label recovery} as a scalable, principled strategy. By estimating missing dynamics on existing corpora, we can reduce the need for new data collection and make those corpora more useful for music research.
```

“entirely bypass ... annotation ambiguities”与 Background 的 alignment／licensing 条件、Ch5 对 edition／annotation convention 的讨论、Conclusion:115 的 contextual target 都不相容。候选保留 label recovery 的实际价值，用 reduce 代替 entirely bypass。无需在动机段罗列技术未知，也不把“未找到记录”写成“没有做过”。

## 真正建议 KEEP 的地方

| 位置／ID | 本轮结论 | 全文语境中的理由 |
| --- | --- | --- |
| R1-35，Fig6.2 caption，Ch6:204 | **优先保留原 caption**；若作者仍想加清晰度，只考虑图内 teacher branch 的 rendered-audio 标签 | 原注已写“PHE/OSF targets extracted from SoundFont-rendered audio”。前面方法段已讲 offline proxy，后面是 adaptation；第三轮四句 caption 正确，但重复流程带来的收益小。这不是 Fig6.3 的 guitar GT 问题。 |
| R1-15 A；R2-01 | 保留已审最小首句修复及现有各章导语／小结结构 | A 保留“missing, flattened, or musically uninformative”和原来的研究提问。Ch5:11 已交代 audio-only、score-facing target、meter；不必再为四章各添一段中心问题。 |
| R1-17 B／R1-18 | 保留已审 B，并共享一个段落；保留前一段及正式题名 | Ch3:24 的 polyphony 动机与 B 的 single-channel／RGB 区分各有作用。再删到只剩术语定义，会削弱评审询问的 representation 理由；也无需到处重写 colourisation。 |
| R1-25 B；R1-32 A | 保留公式、normalisation、relative coefficients、FFT／hop 等具体配置 | “Equal coefficients do not imply equal numerical loss or gradient magnitudes”在此回答的是实际权重问题，不是泛泛自保。两处 Kim 提及略重复，但不值得新开改写轮。R1-32 的2048／221／22050及更新与冻结对象不能为了短而删掉。 |
| R2-04 A | 保留 similarity 的实际系统排序，把11／8／renderer边界集中说明一次 | 已审文字同时保留结果和适用范围。不要把它再扩成“不能证明任何事情”，也不在 Abstract／Conclusion 重复同一听测警告。 |
| R1-30 B；R1-33 B | 保留具体 selection 披露与已收窄的因果解释 | target-label 参与 fold selection 是读者必须知道的 protocol，不能用一句 distribution shift 替代。0.083／0.01 与 bounded consistent-with 解释已平衡，不需再改。 |
| R2-02 B；R2-03 B；Conclusion:143–145 | 保留论文映射／synthesis 及具体跨乐器未来方向 | 已审 B 没有宣称穷尽论文与 thesis 的全部差异；instrument controls 的未来段落已经具体。别再添加模板化 novelty 口号、性能承诺或一整套 disclaimer。 |

原 Fig6.2 caption 全文，供 KEEP 选择复核：

```latex
\caption{An encoder-only Transformer maps padded note sequences to per-note PHE/OSF targets extracted from SoundFont-rendered audio.}
```

## 停止条件与核验

全文语境补查完成。仅建议对上面三组新文字和 R1-35 的 KEEP 倾向作一次定点独立复核；通过后交编辑合并呈现。其余第三轮文字维持通过状态，不启动新的整篇润色循环。V-01–V-07 和四项 evidence-blocked 不因本文件变化；本次不把技术未知当成写作问题来“补齐”。

源清单128/128的 SHA256 与原快照一致；round1／round2／round3及本次检查的冻结候选文件前后 hash 一致。仅新增本文件和 [核验记录](evidence/contextual_audit_v4_validation.json)，未写入论文、回复、DECISIONS 或编辑的入口文件。这里的写稿建议均未作修改完成声明。
