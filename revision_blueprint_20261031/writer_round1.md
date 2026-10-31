# 第一轮英文修改候选

本文件是写作窗第一轮，尚未通过独立审查，也未执行任何 thesis 源修改。请先看每项中文判断，再按需要读英文。作者只在第三编辑维护的统一决策清单填写 YES/NO 与 A/B/C；本文件只引用相同编号，不另设一套选择。YES 只代表批准提案。最终页码【待正式基线和编译核验】。当前定位使用 SOURCES.md 列明 hash 的 LaTeX 源码。

A 为最小有效修改，B 为更清楚的局部解释，C 为较完整的局部叙述或衔接。三稿是互斥替代，不把三段全部塞进 thesis。事实性纠错、已有内容足够或合并项只给一稿。每个实质项的内部小稿、淘汰原因和选稿链见 writer_working.md；它们是本轮写作比较，不冒充独立审查轮次。

## 建议先看

- R1-05 / R1-06 / R1-15：定义和场景关系，避免全书叙述互相矛盾。
- R1-17 / R1-24：image-like 与 Ch.4 matrix-plus-token 的准确解释。
- R1-25 / R1-29：已有方法说明，不追加实验。
- R1-33 / R1-34：直接保留作者已有谨慎回复。
- R2-02 / R2-03 / R2-04：论文来源边界、可迁移范围、小听测限制。
- 先不要定稿 V-02 / V-03 / V-04 / V-05 / V-06：需要原记录或作者决定；详见文末。

## 全部覆盖索引

| 编号 | 修改点 | 写作推荐 | 备注 |
| --- | --- | --- | --- |
| [R1-01](#r1-01) | 引用体例由作者决定，不为可选建议重写全文 | A | 单一纠错／保留／合并稿 |
| [R1-02](#r1-02) | 更新 ISMIR 接收状态 | A | 单一纠错／保留／合并稿 |
| [R1-03](#r1-03) | Fig.1.1 补足乐器身份和其他表达因素 | A | A/B/C |
| [R1-04](#r1-04) | recollecting 改 collecting | A | 单一纠错／保留／合并稿 |
| [R1-05](#r1-05) | 定义 weakly expressive 与 weakly supervised | B | A/B/C |
| [R1-06](#r1-06) | S3 不是所有 audio-only 输出的总称 | B | A/B/C |
| [R1-07](#r1-07) | Fig.2.1 是多种关系，不是必经 MIDI 的链 | B | A/B/C |
| [R1-08](#r1-08) | Bark 表每组三列加分隔线 | A | 单一纠错／保留／合并稿 |
| [R1-09](#r1-09) | 把 onset 说法限定为本文的 Note On velocity | B | A/B/C |
| [R1-10](#r1-10) | Fig.2.3 颜色不能猜含义 | A | 单一纠错／保留／合并稿 |
| [R1-11](#r1-11) | humanisation 用一行定义 | A | 单一纠错／保留／合并稿 |
| [R1-12](#r1-12) | crescendo 已有定义，只补定位与范围 | A | 单一纠错／保留／合并稿 |
| [R1-13](#r1-13) | 数据表拆清 note events、performance velocity、score 与音频可用性 | A | A/B/C |
| [R1-14](#r1-14) | 背景定义常用指标，同时保留 Ch.5 平均方式待核验 | B | A/B/C |
| [R1-15](#r1-15) | 用信息条件描述 S1，不用单一难度排序 | B | A/B/C |
| [R1-16](#r1-16) | 区分跨曲目使用与风格控制 | B | A/B/C |
| [R1-17](#r1-17) | image-like 的含义与 piano-roll 选择一起解释 | B | A/B/C |
| [R1-18](#r1-18) | piano roll 与 event list 的取舍 | A | 单一纠错／保留／合并稿 |
| [R1-19](#r1-19) | recovery 是实验构造，estimation 是一般任务 | B | A/B/C |
| [R1-20](#r1-20) | physical time 是兼容性选择，不是 beat-alignment 劣势的证明 | B | A/B/C |
| [R1-21](#r1-21) | 量化 MIDI 听测保留作者说明，待刺激记录对齐 | A（暂存，待 V-02 后定稿） | A/B/C |
| [R1-22](#r1-22) | 单列 baselines，重排已有事实即可 | A | 单一纠错／保留／合并稿 |
| [R1-23](#r1-23) | modular correction 的实际适用范围与联合模型互补 | B | A/B/C |
| [R1-24](#r1-24) | Ch.4 实际上是矩阵接口加 onset tokens | A | 单一纠错／保留／合并稿 |
| [R1-25](#r1-25) | 明确 hybrid loss 的相对权重与证据边界 | B | A/B/C |
| [R1-26](#r1-26) | Table4.1 每个 setup 用现有变量逐一解释 | A | 单一纠错／保留／合并稿 |
| [R1-27](#r1-27) | 完整 AMT 集成作为未来方向，不虚报已验证性能 | B | A/B/C |
| [R1-28](#r1-28) | state 与 boundary 是互补监督，并非二选一 | B | A/B/C |
| [R1-29](#r1-29) | 共享表征、分头 loss 与 decoding 连接同时说明 | B | A/B/C |
| [R1-30](#r1-30) | cross-dataset 是测迁移边界，不是分离风格因果 | B | A/B/C |
| [R1-31](#r1-31) | 不用未测的 simpler 或 efficiency 优越性 | B | A/B/C |
| [R1-32](#r1-32) | V^(0) 是粗估 roll，Vhat 是 correction 后的逐音值 | A | 单一纠错／保留／合并稿 |
| [R1-33](#r1-33) | DDSP fidelity 是限制，退化不等于因果证明 | B | A/B/C |
| [R1-34](#r1-34) | Huber 的梯度理由与 MAE 对照边界 | B | A/B/C |
| [R1-35](#r1-35) | Fig6.2 已提 rendered audio，补图内 teacher 路径 | A | 单一纠错／保留／合并稿 |
| [R1-36](#r1-36) | 自动选择 SoundFont 留为明确未来工作 | B | A/B/C |
| [R1-37](#r1-37) | 完整 AMT 与 note accuracy 的回应统一放一处 | A | 单一纠错／保留／合并稿 |
| [R1-38](#r1-38) | 明确未显式恢复渐强渐弱，加入 span 输出方向 | B | A/B/C |
| [R2-01](#r2-01) | 现有章节首尾已经显式回应中心问题，推荐保留 | A | 单一纠错／保留／合并稿 |
| [R2-02](#r2-02) | 四篇论文的技术贡献与 thesis 新增综合分开 | B | A/B/C |
| [R2-03](#r2-03) | 把 beyond-piano 可迁移与未验证部分写具体 | B | A/B/C |
| [R2-04](#r2-04) | 11位听者与8段刺激是补充证据，避免 definitive validation | B | A/B/C |
| [R2-05](#r2-05) | 只列实际见到的语言／格式问题 | A | 单一纠错／保留／合并稿 |

<a id="r1-01"></a>

## R1-01 引用体例由作者决定，不为可选建议重写全文

**拟执行位置／操作**：保留方案：正文无替换。若作者选择 author–year，另做全局排版与引用检查，不能只改一行命令就宣称完成。

**准确原文与当前源码位置**

`main.tex` line 48（当前来源 hash 见 SOURCES.md）

```latex
% --------------------- Bibliography and hyperlinks ---------------------
\usepackage[square,numbers,sort&compress]{natbib}
\setlength\bibhang{.3in}
\usepackage[colorlinks=true,
                            citecolor=black,
                            linkcolor=black,
                            urlcolor=red,
                            linktocpage=true,
                            hyperfootnotes=false]{hyperref}
```

**英文候选**

### A

No thesis prose change is proposed. Retain the existing numeric citation style consistently throughout the thesis.

**写作推荐**：A。评审是 suggest，未要求必须转换。整篇转换会改变引用宽度与页码；目前没有作者立场。此项应留给人工选择，不把作者未回复当成接受。

**边界／待核验**：【作者决定：保留 numeric / 改 author–year】。如改，natbib 参数、bibliographystyle、文内作者姓名引用、最终布局须一并核验。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-02"></a>

## R1-02 更新 ISMIR 接收状态

**拟执行位置／操作**：只替换第四篇声明中的状态行，题名与作者保持不变。

**准确原文与当前源码位置**

`Declaration/author_declaration.tex` line 41（当前来源 hash 见 SOURCES.md）

```latex
\begin{tabular}{@{}p{\dimexpr\textwidth-2\tabcolsep\relax}@{}}
\textbf{Details of the work:} \\
\textbf{Zhanhong He}, Hanyu Meng, Defeng (David) Huang, Roberto Togneri,\\
``Joint Estimation of Piano Dynamics and Metrical Structure with a Multi-task Multi-Scale Network,''\\
\emph{Proc.\ IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)},
pp.~14607--14611, 2026.\\
% arXiv:2510.18190. DOI: 10.48550/arXiv.2510.18190.\\%[0.3cm]
\textbf{Location in thesis: Chapter 5} \\
\textbf{Student contribution to work: 80\%}\\
% {[insert text: describe your contribution vs.\ co-authors (methods, data, experiments, writing, etc.)]}
%\\[0.3cm]
%\textbf{Co-author signatures and dates:} \\
%Hanyu Meng:\ \rule{6cm}{0.4pt}\ \ \ Date:\ \rule{3cm}{0.4pt}\\
%David Huang:\ \rule{6cm}{0.4pt}\ \ \ Date:\ \rule{3cm}{0.4pt}\\
%Roberto Togneri:\ \rule{6cm}{0.4pt}\ \ \ Date:\ \rule{3cm}{0.4pt}
\end{tabular} 
	
\vskip 0.6cm
	
\begin{tabular}{@{}p{\dimexpr\textwidth-2\tabcolsep\relax}@{}}
\textbf{Details of the work:} \\
\textbf{Zhanhong He}, Hanyu Meng, Defeng (David) Huang, Roberto Togneri,\\
``Beyond Piano: Cross-Instrument MIDI Velocity Estimation via Differentiable SoundFont Proxies,''\\
Under review (\emph{International Society for Music Information Retrieval (ISMIR)} Conference), 2026.\\
% arXiv:2510.18190. DOI: 10.48550/arXiv.2510.18190.\\%[0.3cm]
\textbf{Location in thesis: Chapter 6} \\
\textbf{Student contribution to work: 80\%}\\
% {[insert text: describe your contribution vs.\ co-authors (methods, data, experiments, writing, etc.)]}
%\\[0.3cm]
%\textbf{Co-author signatures and dates:} \\
%Hanyu Meng:\ \rule{6cm}{0.4pt}\ \ \ Date:\ \rule{3cm}{0.4pt}\\
%David Huang:\ \rule{6cm}{0.4pt}\ \ \ Date:\ \rule{3cm}{0.4pt}\\
%Roberto Togneri:\ \rule{6cm}{0.4pt}\ \ \ Date:\ \rule{3cm}{0.4pt}
\end{tabular}
```

**英文候选**

### A

Accepted for publication in the \emph{International Society for Music Information Retrieval (ISMIR) Conference}, 2026.

**写作推荐**：A。报告 1 Preamble 明确 accepted，所给 ISMIR PDF 为该文的会议版。只写 accepted，不凭相机稿文件名宣称正式出版。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-03"></a>

## R1-03 Fig.1.1 补足乐器身份和其他表达因素

**拟执行位置／操作**：下列为候选图内英文标签与完整 caption；须在提案副本绘图后核验，不覆盖原图。A 保留布局，B 加支路，C 改为并列输出。

**准确原文与当前源码位置**

`Chapter_1/Intro.tex` line 24（当前来源 hash 见 SOURCES.md）

```latex
\begin{figure}[h!]
  \centering
  \includegraphics[width=\linewidth]{Chapter_1/figures/AMT.png}
  \caption{The general architecture of an AMT system, illustrating the transformation of raw acoustic audio into foundational note events and expressive dynamic information. The outputs are MIDI data and musical scores.}
  \label{fig:intro_expressive_amt}
\end{figure}
```

**英文候选**

### A

Figure labels: Step 1: Note events and instrument identity. Estimate pitch, onset, duration, and instrument identity. Step 2: Expressive information. Estimate MIDI velocity and score dynamics, together with instrument-specific controls such as pedalling and articulation. Highlight MIDI velocity and score dynamics as the thesis focus.

Caption: A conceptual view of AMT, including note events, instrument identity, and expressive information. MIDI velocity and score dynamics are the expressive targets studied in this thesis.

### B

Figure labels: Note events: pitch, onset, and duration. Instrument identity: instrument or source assignment. Expressive information: dynamics, articulation, pedalling, and other instrument-specific controls. Connect these outputs to MIDI and score representations, and highlight the dynamics branch.

Caption: Main information layers in an AMT output. Note content, instrument identity, and expressive controls contribute to a symbolic representation of a performance. This thesis studies the recovery of MIDI velocity and score dynamics.

### C

Figure labels: Performance audio → Acoustic analysis → Note events / Instrument identity / Expressive controls. Within expressive controls, highlight MIDI velocity and score dynamics; show articulation and pedalling as further examples.

Caption: Conceptual outputs of expressive AMT. The branches identify complementary information layers rather than a required sequence of independent processing stages. The highlighted dynamics outputs define the scope of this thesis.

**写作推荐**：A。A 直接落实作者“在图中补进”承诺且改图最少。B 更易区分内容；C 避免把两步流程误当唯一架构，但重画幅度最大。三稿均不声称本文估计了所有表达控制。

**边界／待核验**：【待绘图副本】【待视觉核验】；现图还含 every music notes、exact 等表述，可在副本改为 note events，避免准确率绝对化。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-04"></a>

## R1-04 recollecting 改 collecting

**拟执行位置／操作**：只替换一个词，其他语句的可选精简另见 R2-05。

**准确原文与当前源码位置**

`Chapter_1/Intro.tex` line 45（当前来源 hash 见 SOURCES.md）

```latex
By contrast, recollecting new datasets from scratch is a costly process constrained by audio-to-score synchronisation challenges, required musical expertise, and copyright restrictions \cite{li2019urmp,foscarin2020asap,morsi2022bottlenecks}. Therefore, this thesis treats \emph{label recovery} as a scalable, principled strategy. By retroactively estimating missing dynamics on existing corpora, we entirely bypass acquisition bottlenecks and annotation ambiguities, unlocking a vast, previously untapped resource for data-driven music research.
```

**英文候选**

### A

collecting

**写作推荐**：A。作者已明确接受，无需 A/B/C。

**全文同步提案**（原文件均未改）

- `Chapter_7/Conclusion.tex`
  - 原：without recollecting them from scratch.
  - 拟：without collecting them again from scratch.

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-05"></a>

## R1-05 定义 weakly expressive 与 weakly supervised

**拟执行位置／操作**：在 §1.5 中心问题后、三场景介绍前插入一段。

**准确原文与当前源码位置**

`Chapter_1/Intro.tex` line 114（当前来源 hash 见 SOURCES.md）

```latex
The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target. By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.
```

**英文候选**

### A

Here, weakly expressive data retain useful note structure but provide a simplified dynamics layer, for example MIDI with all velocities set to 64 or with only coarse dynamic levels. Weak supervision refers to settings in which the target dynamics labels are missing, incomplete, or unreliable, so learning relies partly on indirect evidence.

### B

In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. Weakly supervised settings lack reliable target labels for direct training; Chapter 6 instead uses real audio and a renderer-based comparison to supervise the velocity estimator indirectly. These terms describe the available information rather than the quality of the musical performance.

### C

The three terms describe different deficiencies in the available data. Incomplete data omit a required dynamics label; weakly expressive data retain note content and timing but flatten or coarsen the dynamics; and weakly supervised data provide no reliable direct target for learning. The last condition motivates the proxy-supervised extension in Chapter 6, while the first two motivate recovery or refinement of an existing symbolic layer.

**写作推荐**：B。B 把数据状态和学习监督条件分开，并用 Ch.6 已有方法落地。A 最短；C 衔接好但对三词分类较硬，现实数据可以同时具备多种状态。不会把八级 score dynamics 本身等同“差”的数据。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-06"></a>

## R1-06 S3 不是所有 audio-only 输出的总称

**拟执行位置／操作**：在 Table 1.2 后补充；同步将同节“from tightly constrained to ambiguous”的总排序改为“different combinations of evidence and target representation”。

**准确原文与当前源码位置**

`Chapter_1/Intro.tex` line 114（当前来源 hash 见 SOURCES.md）

```latex
The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target. By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.
```

`Chapter_6/chap6.tex` line 14（当前来源 hash 见 SOURCES.md）

```latex
From the thesis perspective, this chapter occupies a distinct position. It keeps the note-level MIDI velocity target and the score-informed VeloEst architecture introduced in Chapter~\ref{ch:scoreinf}, but it relaxes the assumption that ground-truth velocity labels are available for the target instrument. It complements Chapter~\ref{ch:audiodyn}, which addressed Scenario~S3 with a different output (beat-synchronous score dynamics), by extending the velocity-focused work to a label-scarce setting. The chapter therefore contributes to thesis Requirement~R5 by combining numerical diagnostics, perceptual loudness correlations, and renderer-robust evaluation evidence, and to Requirement~R6 by treating beyond-piano transfer as a missing-supervision problem rather than ordinary acoustic domain shift.
```

**英文候选**

### A

The scenarios describe the studies undertaken here rather than every possible audio-to-symbolic task. Chapter 6 extends S2 by retaining audio and aligned note events while replacing target-domain velocity labels with indirect renderer-based supervision. Audio-only adaptation for MIDI velocity estimation is a possible extension, but is not evaluated in this thesis.

### B

The input condition alone does not determine the dynamics target. Audio-only MIDI velocity estimation is also possible, but S3 refers specifically to the score-dynamics task studied in Chapter 5. The beyond-piano study in Chapter 6 uses the score-informed estimator from Chapter 4 and still requires aligned note events. It therefore extends S2 under weaker target-domain supervision rather than adding an audio-only velocity experiment.

### C

Table 1.2 separates three studied input–output settings. S1 predicts velocity from symbolic context, S2 refines velocity using audio and aligned notes, and S3 predicts score dynamics together with metre from audio. Chapter 6 returns to the S2 interface under missing target velocity labels. Extending the same adaptation strategy to an audio-only velocity estimator remains a future direction.

**写作推荐**：B。B 正面回答评审“是否也可以 audio→velocity”，并保留作者当前优先 S2 的立场。未采用作者口头“3 times MAE”：当前 Ch.4 Table4.2 的 hFT=9.9、Score-HPT=8.0 不能支持这个倍数。

**边界／待核验**：不新增 audio-only velocity 实验；Ch.4 global shift 的鲁棒性不等于 Ch.6 任意 onset error 无影响。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-07"></a>

## R1-07 Fig.2.1 是多种关系，不是必经 MIDI 的链

**拟执行位置／操作**：修改 Figure2.1 caption；图副本增加 perceptual/audio → score dynamics 的虚线关系并注明 contextual inference，不改成固定换算。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 14（当前来源 hash 见 SOURCES.md）

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.9\linewidth]{Chapter_2/figures/dynamics_layers_v1.jpg}
  \caption{Layered view of dynamics used in this thesis. Physical sound level, perceived loudness, MIDI velocity, and score dynamics are linked but not interchangeable. Each transition is many-to-many or instrument-specific.}
  \label{fig:bg_dynamics_layers}
\end{figure}
```

`Chapter_2/Background.tex` line 26（当前来源 hash 见 SOURCES.md）

```latex
This layered view has an important methodological consequence. There is no single exact lookup table that converts score dynamics, loudness, and MIDI velocity into one another. Nominal mappings are convenient for notation software and rendering systems, but they remain conventions. They should not be mistaken for measurement standards. This point is central to the whole dissertation because each chapter targets a different layer of the same broader expressive problem. Table~\ref{tab:bg_dynamics_compare} summarises the three dynamics representations that recur throughout this thesis, together with their temporal anchors, strengths, and limitations.
```

**英文候选**

### A

Relationships among physical sound level, perceived loudness, MIDI velocity, and score dynamics. The layers are related but are not an obligatory processing chain. In particular, score dynamics may be inferred directly from audio-derived perceptual evidence without first estimating MIDI velocity; the inference remains context-dependent.

### B

Relationships among the dynamics representations used in this thesis. MIDI velocity is one route between symbolic control and sound, but it is not a required intermediate representation for score-dynamics estimation. Chapter 5 learns a direct audio-to-score-dynamics mapping. Instrument response, performer interpretation, and musical context prevent any of these links from defining a universal one-to-one conversion.

### C

The representations provide complementary descriptions of dynamics. Rendering relates MIDI velocity to acoustic output, psychoacoustic analysis relates audio to loudness, and contextual inference relates performed sound to score markings. The direct audio-to-score-dynamics route studied in Chapter 5 therefore coexists with velocity-based workflows; none supplies a fixed instrument-independent lookup table.

**写作推荐**：B。B 同时保留作者强调的 instrument/style 不确定性并承认评审提出的直接路径，符合 Ch.5 实际输入输出。A 短；C 更像正文解释而非图注，可能变长。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-08"></a>

## R1-08 Bark 表每组三列加分隔线

**拟执行位置／操作**：只在 Table2.3 的三组三列之间加线；这是格式提案，需最终排版核验。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 127（当前来源 hash 见 SOURCES.md）

```latex
\begin{table*}[!htbp]
    \centering
    \caption{Approximate relation between critical-band rate in Bark and frequency in Hz. The full psychoacoustic scale spans 24 critical bands.}
    \label{tab:bark_table}
    \setlength{\tabcolsep}{4.6pt}
    \fontsize{11pt}{13pt}\selectfont
    \renewcommand{\arraystretch}{1.18}
    \begin{tabular}{ccc@{\hspace{8pt}}ccc@{\hspace{8pt}}ccc}
        \toprule
        \makecell[c]{\textbf{Critical}\\[1pt]\textbf{band rate}\\[1pt]\textbf{$z$ [Bark]}} &
        \makecell[c]{\textbf{Frequency}\\[1pt]\textbf{$f$ [Hz]}} &
        \makecell[c]{\textbf{$\Delta f$}\\[1pt]\textbf{[Hz]}} &
        \makecell[c]{\textbf{Critical}\\[1pt]\textbf{band rate}\\[1pt]\textbf{$z$ [Bark]}} &
        \makecell[c]{\textbf{Frequency}\\[1pt]\textbf{$f$ [Hz]}} &
        \makecell[c]{\textbf{$\Delta f$}\\[1pt]\textbf{[Hz]}} &
        \makecell[c]{\textbf{Critical}\\[1pt]\textbf{band rate}\\[1pt]\textbf{$z$ [Bark]}} &
        \makecell[c]{\textbf{Frequency}\\[1pt]\textbf{$f$ [Hz]}} &
        \makecell[c]{\textbf{$\Delta f$}\\[1pt]\textbf{[Hz]}} \\
        \midrule
        0 & 0    & 100 & 9  & 1080  & 190 & 18 & 4400  & 900  \\
        1 & 100  & 100 & 10 & 1270  & 210 & 19 & 5300  & 1100 \\
        2 & 200  & 100 & 11 & 1480  & 240 & 20 & 6400  & 1300 \\
        3 & 300  & 100 & 12 & 1720  & 280 & 21 & 7700  & 1800 \\
        4 & 400  & 110 & 13 & 2000  & 320 & 22 & 9500  & 2500 \\
        5 & 510  & 120 & 14 & 2320  & 380 & 23 & 12000 & 3500 \\
        6 & 630  & 140 & 15 & 2700  & 450 & 24 & 15500 & --   \\
        7 & 770  & 150 & 16 & 3150  & 550 &    &       &      \\
        8 & 920  & 160 & 17 & 3700  & 700 &    &       &      \\
        \bottomrule
    \end{tabular}
\end{table*}
A common analytic approximation from physical frequency $f$ in kHz to Bark rate $z$ is
\begin{equation}
z(f_{\mathrm{kHz}}) = 13\arctan(0.76 f_{\mathrm{kHz}}) + 3.5\arctan\!\left(\frac{f_{\mathrm{kHz}}^2}{7.5^2}\right),
\label{eq:bg:bark_mapping}
\end{equation}
where $f_{\mathrm{kHz}}$ denotes frequency in kHz \cite{pampalk2002content,pampalk2004exploring,zwicker1999psychoacoustics}. This equation defines the Bark coordinate itself. It does not yet compute loudness.
```

**英文候选**

### A

\begin{tabular}{ccc|ccc|ccc}

**写作推荐**：A。精确对应评审的 1–3 / 4–6 / 7–9，不误改 Table2.4 的软件映射表。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-09"></a>

## R1-09 把 onset 说法限定为本文的 Note On velocity

**拟执行位置／操作**：替换 §2.3.2 第一段；可在 Ch.1 首次定义同步加入 Note On 限定。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 274（当前来源 hash 见 SOURCES.md）

```latex
MIDI velocity is a different kind of representation. It is attached to a note onset rather than to a phrase or region. In conventional MIDI performance data, a sounding note onset carries a discrete velocity value on a finite integer scale. In a chord, each note may have a different velocity. In a rapid passage, every note can carry its own local attack value. MIDI velocity is therefore a micro-level representation: it serialises note-level actions rather than summarising the expressive state of a passage.
```

**英文候选**

### A

In this thesis, MIDI velocity means the Note On velocity associated with a note attack. MIDI also supports Note Off velocity and separate control messages, which are not the targets studied here. Each sounding note can therefore receive its own onset-velocity value, including notes played simultaneously in a chord.

### B

The target studied here is MIDI Note On velocity: a discrete control value attached to the start of a note. This definition is narrower than the full MIDI protocol, which also includes Note Off velocity, aftertouch, and continuous controllers. The thesis estimates one onset value per note rather than a time-varying control trajectory.

### C

The note-level target in this thesis is Note On velocity. It records or controls the attack of an individual note, so simultaneous notes may have different values. Other MIDI messages can describe release behaviour or changes during a note, but these remain outside the present target. This is why the velocity chapters preserve note events and estimate only an onset attribute.

**写作推荐**：B。作者确认 onset 的本意可保留，但全 MIDI protocol 的“always”需收窄。已向 MIDI Association 官方 message summary 核验 Note On、Note Off、aftertouch、CC 的区分；不新增未经同意的 bibliography 条目。A 最短；C 强调与 thesis 关系，略重。

**边界／待核验**：官方核验来源：https://midi.org/summary-of-midi-1-0-messages 。本段不讨论 velocity=0 的额外编码细节，避免引入与当前问题无关的规范内容。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-10"></a>

## R1-10 Fig.2.3 颜色不能猜含义

**拟执行位置／操作**：推荐在图副本把 (d)–(f) note marks 改成单一颜色，保留 (g) 原有 grey/black/red metrical 编码；下列句子补入原 caption 的 (d)–(f) 描述后。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 442（当前来源 hash 见 SOURCES.md）

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.98\linewidth]{Chapter_2/figures/temporal_units}
  \caption[Aligned temporal coordinates across audio, symbolic, and metrical representations]{Aligned temporal representations for a 20\,s excerpt from MazurkaBL M33-4 (pid918726-08, 40--60\,s). Panels (a)--(c) show frame-level acoustic evidence: the log-Mel spectrogram, Bark-scale specific loudness (BSSL), and Bark-scale total loudness (BSTL). Panels (d)--(f) show note-level symbolic coordinates: note onsets, note-event spans, and a MIDI piano-roll visualisation. Panel (g) shows the metrical and phrase grid, with beats in grey, downbeats in black, and phrase boundaries in red. The figure illustrates how the same performance segment can be re-indexed from dense audio frames to note events and then to beat-, bar-, and phrase-level coordinates for dynamics recovery.}
  \label{fig:bg_temporal_units}
\end{figure}
```

**英文候选**

### A

Panels (d)–(f) use a uniform colour for note events; colour does not encode velocity, voice, or instrument identity. Horizontal position indicates time. The vertical axes in (e) and (f) show the displayed event-lane index and MIDI pitch, respectively.

**写作推荐**：A。现资产没有图例和作图脚本，不能从色相推断是 velocity 或 voice。统一颜色是可实施且不改变本图 temporal-coordinate 用途的最小方案。

**边界／待核验**：候选 caption 只在完成对应副本改图后可用。若保留现有颜色，必须先找到作图源确认编码并新增准确图例【待查】。已查看 main.pdf 物理页52／印刷页25，panel标题在白底PDF中正常显示；PNG工具黑区是透明背景预览，不能当论文排版缺陷。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-11"></a>

## R1-11 humanisation 用一行定义

**拟执行位置／操作**：在 §2.5.1 首句后补定义。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 490（当前来源 hash 见 SOURCES.md）

```latex
Expressive performance rendering aims to generate expressive control signals from symbolic input. Many systems predict timing, dynamics, and sometimes articulation jointly \cite{jeong2019virtuosonet,borovik2023scoreperformer}. These models are important because they show that expressive performance can be learned from symbolic structure. At the same time, they reveal a practical limitation for the present thesis. Joint expressive rendering may alter more than the user wants. In production or corpus-upgrading settings, the desired operation is often narrower: preserve the notes and timing, and recover only the missing dynamics layer. This narrower, controllable objective is the entry point for Chapter~\ref{ch:velcomp}.
```

**英文候选**

### A

Here, humanisation refers to adding or varying expressive controls in a symbolic sequence, such as note timing and velocity, to move it away from a mechanically uniform rendering.

**写作推荐**：A。无需删除已有术语；定义后马上回到本文只改 velocity 的范围，短句就能解决。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-12"></a>

## R1-12 crescendo 已有定义，只补定位与范围

**拟执行位置／操作**：保留 §2.3.1 已有定义，在 §2.6.1 末补一个 cross-reference，避免重复一整段基础知识。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 263（当前来源 hash 见 SOURCES.md）

```latex
Dynamic markings are the conventional score vocabulary for notated loudness and dynamic change. They include static markings such as \textit{pp}, \textit{p}, \textit{mp}, \textit{mf}, \textit{f}, and \textit{ff}, as well as directional indications such as \textit{crescendo}, \textit{diminuendo}, and hairpins. Although a marking is printed at a specific visual position, its musical scope is usually broader than that position. A single \textit{p} may govern a phrase, a texture, or a formal region until a later marking or musical event changes the dynamic state. A crescendo indicates a tendency over a span, not an isolated value at one note.
```

`Chapter_2/Background.tex` line 528（当前来源 hash 见 SOURCES.md）

```latex
Computational modelling of dynamics has a long history in expressive performance research \cite{cancinoChacon2018computational}. Rather than focusing only on note-level control, this line of work studies how performed loudness relates to symbolic dynamic markings and phrase structure. Kosta and collaborators showed both the usefulness and the ambiguity of this relationship \cite{kosta2014dynpiano,kosta2016mapping,kosta2018mazurkabl}. Other work has further analysed dynamic principles in piano performance \cite{jones2023probingdyn}.
```

**英文候选**

### A

Besides static levels, score dynamics includes gradual indications such as crescendo and diminuendo, as described in Section 2.3.1. Chapter 5 estimates the five static levels available in its annotations and their change points; it does not explicitly decode these longer-span symbols.

**写作推荐**：A。原文 §2.3.1 已明确 directional indications、hairpins 和 span。真正缺口是 §2.6.1 与 Ch.5 实验范围衔接；未来方向另见 R1-38。

**关联意见**：R1-38。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-13"></a>

## R1-13 数据表拆清 note events、performance velocity、score 与音频可用性

**拟执行位置／操作**：各稿给出完整 caption/notes 提案；不自动重写数据值。A 改表头和注，B 加 audio 列须逐行核验，C 把模态解释移至表后。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 594（当前来源 hash 见 SOURCES.md）

```latex
The empirical claims of this thesis are conditioned on what each available dataset can support. Table~\ref{tab:dataset_comparison} summarises the representative corpora relevant to expressive label recovery, listing their instrument coverage, scale, and which expressive modalities (MIDI velocity, score, and score dynamics) are actually available. The MIDI column also includes note annotations that can be converted to MIDI, such as the JAMS annotations in GuitarSet. The discussion that follows turns these modality differences into chapter-specific constraints.
```

`Chapter_2/Background.tex` line 596（当前来源 hash 见 SOURCES.md）

```latex
\begin{table}[!htbp]
\centering
\caption{Representative datasets relevant to expressive label recovery in this thesis. Each dataset is summarised by its instrument family, scale, and the expressive modalities (MIDI, velocity, score, score dynamics) it provides.}
\label{tab:dataset_comparison}
```

**英文候选**

### A

Representative datasets relevant to expressive label recovery. “MIDI / note annotations” includes performance MIDI and aligned note annotations convertible to MIDI; it does not by itself imply measured velocity. “Velocity” indicates the availability of the note-level dynamics target, with qualifications stated in the row notes. “Score” refers to a reference symbolic score, rather than the performance timing in MIDI. A triangle marks a qualification in the corresponding row. For ATEPP, 43% denotes the reported share of recordings paired with scores, not a verified share with score-dynamics labels. Audio access limitations are stated separately in the row notes.

### B

Representative datasets relevant to expressive label recovery, separating audio access, note annotations, captured velocity, reference scores, and score-dynamics annotations. A tick indicates the stated modality, a cross indicates its absence, and a triangle refers to a qualification in the row notes. The audio column distinguishes available performance recordings, externally linked recordings, and software-rendered material. For ATEPP, the reported 43% applies to score availability; the dynamic markings in those scores have not been verified.

### C

The table separates structural note information from expressive supervision. A MIDI file or a convertible note annotation can provide pitch and timing without containing measured performance velocity. Reference scores provide notated structure and may be quantised, whereas performance MIDI retains performed timing. The 43% shown for ATEPP describes score coverage and should not be read as the availability of verified dynamic markings. Audio access and any annotation qualifications remain dataset-specific and are stated in the row notes.

**写作推荐**：A。A 避免把当前包含 GuitarSet/JAMS 和软件 MIDI 的一整列都说成 unquantised performance MIDI。保留作者关于43%的意思，但不把有score自动推成有verified dynamics。B 最直接回应 audio-column 建议，但表已宽且需核验每行，C 文字较自然但图例仍需一致。

**边界／待核验**：【待确认 ATEPP 数据版本及43%分母】；B 的 audio 列只可用原资料逐行填，特别 MID-FiLD 必须区分软件制作／rendered 与 human recording，不能凭列名全打勾。不触碰已修正 MAESTRO/MAPS 数字。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-14"></a>

## R1-14 背景定义常用指标，同时保留 Ch.5 平均方式待核验

**拟执行位置／操作**：在 §2.8.3 首段后插入；A 最短，B 给公式，C 给读者如何读各指标的衔接。

**准确原文与当前源码位置**

`Chapter_2/Background.tex` line 886（当前来源 hash 见 SOURCES.md）

```latex
Score dynamics is usually evaluated as classification on a musically meaningful grid. F1 score is common because the class distribution is imbalanced and because some symbols occur much less frequently than others \cite{kosta2017thesis}. In the present thesis, beat-synchronous evaluation is especially important because it avoids arbitrary frame-level tolerance choices and aligns the prediction target with how the annotations are actually used in music notation.
```

`Chapter_2/Background.tex` line 879（当前来源 hash 见 SOURCES.md）

```latex
Velocity should be evaluated at note level rather than by naive frame-wise error. Otherwise, long sustained notes dominate the metric. Standard statistics include mean absolute error and related dispersion measures \cite{kuo2021velocity,kim2024method}. However, numerical accuracy alone is not sufficient. A model can achieve a decent average error while producing over-smoothed or mechanically centred dynamics. Distribution-sensitive measures, visual inspection, and listening tests therefore play an important complementary role. This is especially evident in Chapter~\ref{ch:velcomp}, where perceptual differences are not always fully captured by raw error.
```

**英文候选**

### A

Precision is the fraction of predicted labels or events that are correct, and recall is the fraction of reference labels or events that are recovered. Their harmonic mean is F1. For note-level velocity, MAE measures the mean absolute difference from the reference value; Chapter 3 additionally reports error dispersion, tolerance-based recall, and predicted-velocity dispersion. Each metric is computed on the coordinate appropriate to its target.

### B

For a given class or event type, precision is TP/(TP+FP), recall is TP/(TP+FN), and F1 is 2TP/(2TP+FP+FN), where TP, FP, and FN are true positives, false positives, and false negatives. Macro-F1 averages the class-wise scores equally, whereas support-weighted F1 weights them by their reference counts. These averages answer different questions and must be identified when reporting score-dynamics results. Note-level velocity MAE averages the absolute prediction error over the reference note onsets; its full definition and the complementary dispersion metrics are given in Section 3.6.3.

### C

Evaluation follows the output representation. Note-wise velocity error measures agreement with captured MIDI values, while velocity dispersion checks whether the output collapses towards a constant. Score dynamics is assessed as beat-wise classification, for which precision, recall, and F1 describe false labels and missed labels. Beats and downbeats are evaluated as time-stamped events. The task-specific definitions in Chapters 3–6 state the averaging rule, temporal grid, and matching tolerance used for each result.

**写作推荐**：B。B 正式区分 macro 与 weighted，能补齐 background，又不擅自断言现有 Ch.5 数值是哪一种。A 更短但数学定义略弱；C 适合读者导向，缺明确定义。Chapter3 metrics 实际 §3.6.3，最终自动引用 label 应取代硬编码编号。

**边界／待核验**：V-05：Ch.5 公式写 macro，固定 evaluator 写 weighted；未确认实际论文 run。不得把此背景定义当作已解决运行来源。公式采用通用定义，空分母规则留给实现核验。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-15"></a>

## R1-15 用信息条件描述 S1，不用单一难度排序

**拟执行位置／操作**：替换 Ch.3 首段首句；同义修正 §3.3、§3.11、Ch.7 §7.1.2，并去掉 Intro 对三个异质任务的整体难度排序。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 13（当前来源 hash 见 SOURCES.md）

```latex
This chapter addresses Scenario~S1, the most controlled setting in the thesis map. Here the symbolic notes and their timing are already known, but the note-level velocity is missing, flattened, or musically uninformative. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?
```

`Chapter_7/Conclusion.tex` line 48（当前来源 hash 见 SOURCES.md）

```latex
The first method contribution establishes the most controlled setting: the symbolic note sequence is fixed, and only the missing MIDI velocity layer is restored. Chapter~\ref{ch:velcomp} reformulates this task as image colourisation on sparse piano-roll matrices. This is not only an architectural analogy. Polyphonic symbolic music contains local pitch--time neighbourhoods and vertical chordal patterns that are weakened when the task is treated as a plain sequence. A U-Net with window attention and a sparsity-aware loss can exploit this structure while leaving the underlying note content unchanged.
```

**英文候选**

### A

This chapter addresses Scenario S1, in which note content and timing are given but no performance audio or dynamics labels are available as input.

### B

This chapter addresses Scenario S1: the symbolic notes and their timing are known, while the dynamics layer is missing and no performance audio is available. The fixed note structure constrains what may be changed, but does not uniquely determine how the notes should be played.

### C

The symbolic-only case separates two kinds of constraint. Notes and timing are fixed, so the model changes only velocity; the performance itself is not observed, so the expressive interpretation remains ambiguous. This chapter asks whether symbolic context alone can support a useful velocity profile under those conditions.

**写作推荐**：B。B 保留作者“输入信号更少”的本意，也说清 fixed structure 与 velocity ambiguity 可以同时成立。A 改动最小；C 解释更细但可能与后段重复。同步修正处均按同一语义，不能换个 constrained 单词继续做难度辩护。

**全文同步提案**（原文件均未改）

- `Chapter_3/chap3.tex`
  - 原：This chapter studies the most constrained setting in that map:
  - 拟：This chapter studies the symbolic-only setting in that map:

- `Chapter_3/chap3.tex`
  - 原：This chapter studied the most controlled form of expressive-label recovery:
  - 拟：This chapter studied expressive-label recovery without acoustic input:

- `Chapter_7/Conclusion.tex`
  - 原：The first method contribution establishes the most controlled setting:
  - 拟：The first method contribution addresses the symbolic-only setting:

- `Chapter_1/Intro.tex`
  - 原：By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.
  - 拟：These settings form the core empirical arc of the thesis by varying both the available evidence and the target representation.

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-16"></a>

## R1-16 区分跨曲目使用与风格控制

**拟执行位置／操作**：在 Ch.3 Discussion 的 empirical-scope 段后插入。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 459（当前来源 hash 见 SOURCES.md）

```latex
The empirical scope of the chapter is piano-based, using datasets recorded with Yamaha Disklavier instruments.
Within that scope, the cross-dataset MAESTRO-to-SMD results show that the image-colourisation formulation is not merely memorising one corpus.
```

`Chapter_3/chap3.tex` line 444（当前来源 hash 见 SOURCES.md）

```latex
\paragraph{Results.}
Although a substantial gap to human performance remains, the proposed U-Net clearly outperforms the other systems.
The Flat model performs worst, consistent with earlier findings that default velocity is musically inadequate \cite{kuo2021velocity}.
The seen, less-seen, and unseen repertoire groups are best interpreted as descriptive groups rather than as a strict complexity-controlled comparison.
Even so, the relatively narrow 95\% confidence intervals across groups suggest that participants rated the stimuli with reasonable consistency.
```

**英文候选**

### A

The model is not conditioned on composer or performer identity. Its aim is to provide a useful velocity completion across the piano repertoire represented in the data, rather than to reproduce a requested style. The composer groups in the listening test provide descriptive evidence about this scope, not a controlled study of stylistic effects.

### B

Composer and performance style can influence a plausible velocity profile, but the present model does not offer explicit style control. The available training data motivated learning a shared completion model rather than separate composer-specific models. The listening results include more familiar and unseen composers, although the small, unbalanced set of excerpts cannot isolate composer style from piece-specific differences.

### C

A completed velocity profile is one plausible expressive interpretation of a fixed note sequence. The present model learns this interpretation from pooled piano performances without a composer or style control input. The descriptive composer groups in the listening test help reveal where transfer may be weaker, while controlled style conditioning remains beyond the evidence reported here.

**写作推荐**：B。B 忠实保留作者因数据不足从 style-control 转向 generalisation 的解释，不引入 Dolby 内部或未发表开发史。A 较短；C 更突出多解性，可与 R1-19 合并时去重。

**边界／待核验**：不能把 two unseen composers 或MOS差异写成因果性 composer effect，也不声称模型已 generalise to any style。

**关联意见**：R1-19; R2-04。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-17"></a>

## R1-17 image-like 的含义与 piano-roll 选择一起解释

**拟执行位置／操作**：替换 Ch.3 §3.2 最后一个方法动机段；与 R1-18 共用。正文描述用 image-like / single-channel velocity roll；正式论文题名与 thesis 章名不机械改名。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 26（当前来源 hash 见 SOURCES.md）

```latex
This motivates the image-based view adopted in the present chapter. By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly. U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic and does not rely on acoustic input \cite{he2025filling,kim2024method}. This makes the chapter a natural starting point for the broader thesis.
```

`Chapter_3/chap3.tex` line 43（当前来源 hash 见 SOURCES.md）

```latex
This chapter instead exploits the spatial structure of polyphonic symbolic music by treating MIDI as an image-colourisation problem. MIDI without velocity is represented as a binary pianoroll, while the target is a velocity-valued pianoroll. This formulation is especially natural for instruments such as piano, where multiple simultaneous notes create rich vertical patterns. Current dataset availability restricts the experiments here to piano data, but the formulation itself is not tied to piano alone.
```

**英文候选**

### A

The representation is image-like because pitch and time form a two-dimensional grid processed by convolutional layers. The binary piano roll provides the note structure, and the target velocity roll assigns a scalar value at note locations. Colourisation is an analogy for adding the missing velocity layer; the model does not predict RGB colours.

### B

A piano roll places simultaneous notes along the pitch axis and their local evolution along time, giving the U-Net a regular two-dimensional input. Convolution and skip connections can then use local pitch–time neighbourhoods while preserving the given note structure. The output is a single-channel velocity roll. We use colourisation as an analogy for completing that missing scalar layer, rather than for predicting RGB colour.

### C

The choice of representation follows the proposed architecture. A piano roll exposes local pitch–time neighbourhoods and simultaneous-note patterns on a regular grid that can be processed by a U-Net. Note-list or event-token representations are valid alternatives, but would require a different interface. The image-like formulation studied here adds a single velocity channel to existing notes; its advantages over the selected baselines do not establish that it is superior to every event-based formulation.

**写作推荐**：B。B 同时回答“为什么叫image-like”和“为什么用piano roll”，不把 analogy 当RGB回归，也不作 representation 因果优越性的过强归因。A 最短，C 比较边界最清楚但更长。

**边界／待核验**：V-03：当前源码写 F input；固定训练快照配置 onset_mask=True 且默认 matrix channels=2，不能直接证明论文run。此段只解释表示，不重复确定未经核验的实际输入分支。

**关联意见**：R1-18。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**全文同步提案**（原文件均未改）

- `main.tex; Chapter_1/Intro.tex; Chapter_7/Conclusion.tex`
  - 原：image colourisation / image-colourisation used as a literal task claim
  - 拟：Retain the formal chapter/paper titles; where explaining the method, state the image-like, single-channel velocity-layer analogy. Do not mechanically replace the published paper title.

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-18"></a>

## R1-18 piano roll 与 event list 的取舍

**拟执行位置／操作**：与 R1-17 共用同一段，不重复插入。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 43（当前来源 hash 见 SOURCES.md）

```latex
This chapter instead exploits the spatial structure of polyphonic symbolic music by treating MIDI as an image-colourisation problem. MIDI without velocity is represented as a binary pianoroll, while the target is a velocity-valued pianoroll. This formulation is especially natural for instruments such as piano, where multiple simultaneous notes create rich vertical patterns. Current dataset availability restricts the experiments here to piano data, but the formulation itself is not tied to piano alone.
```

**英文候选**

### A

Use the selected paragraph under R1-17. It explains the regular pitch–time grid and limits the comparison to the representations actually studied.

**写作推荐**：A。两个问题紧邻且共享解释；一段即可覆盖，另在 representation 开头保留 O/F/V 数学定义。

**关联意见**：R1-17。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-19"></a>

## R1-19 recovery 是实验构造，estimation 是一般任务

**拟执行位置／操作**：在 §3.3 问题设定末补一段。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 31（当前来源 hash 见 SOURCES.md）

```latex
MIDI (Musical Instrument Digital Interface) is the dominant symbolic format in modern music production. A MIDI file that resembles sheet music can still sound mechanical when its note velocities are undefined or flattened to a default constant. In contrast, MIDI captured from human performance preserves the performer's control of intensity and therefore carries a substantial portion of the perceived musical expression. As discussed in the thesis introduction, dynamics is the expressive dimension targeted first in this thesis because it is both perceptually salient and directly editable. This chapter studies the most constrained setting in that map: recovering note-level MIDI velocity when the symbolic notes and their timing are already known.
```

**英文候选**

### A

Velocity completion is an estimation task. In the supervised experiments, reference velocities are removed from captured performances, so recovery describes the reconstruction setting. At deployment, a sequence with flat or missing velocities may admit several plausible completions; the model does not recover a uniquely determined original performance from note structure alone.

### B

We use completion for the operation of adding missing velocities and estimation for the prediction problem. Recovery is appropriate in the supervised evaluation because the withheld reference values are known. For new symbolic input, the output is instead an estimated expressive profile, whose usefulness need not imply that it reproduces one uniquely correct interpretation.

### C

The training construction begins with performance MIDI and withholds its velocity layer. This permits a direct comparison against captured values, but does not make velocity a deterministic function of the score. The same estimator can complete previously unseen or quantised MIDI without a recorded reference; in that use, its output should be read as a plausible velocity realisation rather than a reconstruction of a known performer.

**写作推荐**：B。B 保留作者“开始是recovery，最终task是estimation”，不强迫全论文统一成一个词。A 很直接；C 衔接应用好，但与 R1-21 可能重复。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-20"></a>

## R1-20 physical time 是兼容性选择，不是 beat-alignment 劣势的证明

**拟执行位置／操作**：在 §3.4.2 segmentation 结果后插入；同时将“10s roughly four measures at120 BPM”改为“several bars, depending on tempo and metre”。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 61（当前来源 hash 见 SOURCES.md）

```latex
The segment duration is a key design variable in this formulation.
Because a MIDI performance often exceeds three minutes, we split each piece into shorter segments to keep the computation tractable.
The number of time frames \(T\) determines the temporal granularity of the matrix representation, so the timestep resolution is
\begin{equation}
\text{Resolution} = \frac{\text{Segment Duration}}{T}.
\label{eq:velcomp_resolution}
\end{equation}
Unlike tasks that require fine temporal resolution to detect unknown note events, the present task already assumes that note timing is given.
This makes a more computationally efficient timestep resolution feasible.
With a fixed input size of \(T=96\), we explored segment durations of 5 s, 10 s, 15 s, and 20 s in hyperparameter search and found that 10 s yielded the best results.
A plausible explanation is that a 10-second window often captures a musically coherent phrase, for example roughly four measures at 120 BPM, providing enough context without overextending the receptive field.
```

`Chapter_3/chap3.tex` line 61（当前来源 hash 见 SOURCES.md）

```latex
The segment duration is a key design variable in this formulation.
Because a MIDI performance often exceeds three minutes, we split each piece into shorter segments to keep the computation tractable.
The number of time frames \(T\) determines the temporal granularity of the matrix representation, so the timestep resolution is
\begin{equation}
\text{Resolution} = \frac{\text{Segment Duration}}{T}.
\label{eq:velcomp_resolution}
\end{equation}
Unlike tasks that require fine temporal resolution to detect unknown note events, the present task already assumes that note timing is given.
This makes a more computationally efficient timestep resolution feasible.
With a fixed input size of \(T=96\), we explored segment durations of 5 s, 10 s, 15 s, and 20 s in hyperparameter search and found that 10 s yielded the best results.
A plausible explanation is that a 10-second window often captures a musically coherent phrase, for example roughly four measures at 120 BPM, providing enough context without overextending the receptive field.
```

**英文候选**

### A

The fixed-duration representation accepts the note timings already present in a MIDI file, including performance MIDI and estimated note events, without requiring a beat map. A musical-time representation is also possible, but is not compared in the present experiments.

### B

We use physical time to retain the timing supplied with the input and to avoid requiring a score or beat map. This is useful when the input comes from a performance or a transcription system as well as from a quantised score. A beat-relative representation could provide useful metrical context; the present study does not establish whether it would improve velocity estimation.

### C

Physical-time and musical-time grids emphasise different information. The current grid accepts existing event times directly, while a beat-relative grid could normalise tempo and expose metrical position. Such a representation need not remove expressive timing if that information is retained separately. We therefore treat the choice as an untested representation alternative, rather than claim that beat alignment would necessarily reduce expressiveness.

**写作推荐**：B。B 保留作者兼容 AMT 输入的实际动机，但不把 beat-relative 等同 hard quantisation。C 更直接纠正逻辑，语气稍像回复而非正文；A 最小。

**边界／待核验**：这里只改说明，不增加实验。10s=4 measures 的解释本来取决于 metre/tempo；4/4在120BPM的4小节是8s。

**全文同步提案**（原文件均未改）

- `Chapter_3/chap3.tex`
  - 原：roughly four measures at 120 BPM
  - 拟：several bars, depending on tempo and metre

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-21"></a>

## R1-21 量化 MIDI 听测保留作者说明，待刺激记录对齐

**拟执行位置／操作**：应用讨论可以先写；正式 Stimuli 句子须依 V-02 的原刺激／生成记录定稿。以下三稿均不把“原SMD MIDI删velocity”自动解释成未量化。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 375（当前来源 hash 见 SOURCES.md）

```latex
\paragraph{Stimuli.}
The test used eight 10-second MIDI segments, each selected from one of the SMD performances listed in Table~\ref{tab:velcomp_composers}.
For each segment, the original human-performed velocities were removed to create a common symbolic input.
The Flat, ConvAE, and U-Net outputs were then rendered as stimuli, while the original MIDI with human-performed velocity served as the reference.
All stimuli were rendered with the PianoTeq~8 plug-in using the Steinway Model D instrument.
```

`Chapter_3/chap3.tex` line 375（当前来源 hash 见 SOURCES.md）

```latex
\paragraph{Stimuli.}
The test used eight 10-second MIDI segments, each selected from one of the SMD performances listed in Table~\ref{tab:velcomp_composers}.
For each segment, the original human-performed velocities were removed to create a common symbolic input.
The Flat, ConvAE, and U-Net outputs were then rendered as stimuli, while the original MIDI with human-performed velocity served as the reference.
All stimuli were rendered with the PianoTeq~8 plug-in using the Steinway Model D instrument.
```

**英文候选**

### A

The model is intended for MIDI with fixed notes and timing, including quantised composition input. Training on performance MIDI provides captured velocity targets, while the extent to which the learned profile transfers to quantised input depends on the input context. The timing preparation of the listening-test stimuli is specified in the protocol below. 【Timing preparation: confirm the quantisation step and whether it was shared by system inputs and the reference.】

### B

Performance MIDI supplies the supervised velocity targets, but the completion operation itself does not require expressive input velocities or unquantised timing. The author reports that quantised score-MIDI was used in the listening test. 【Before inclusion, replace this note with the exact verified timing preparation of the eight stimuli.】 The test supports that practical use within its small selected set, rather than a controlled comparison of quantised and performance-timed input.

### C

The composition use case concerns preserving the input composition while adding a velocity profile. Performance MIDI is used for training because it provides captured targets; this does not restrict the interface to performance-timed inputs. 【If confirmed by the stimulus records: For the listening test, the note timings were quantised before the common symbolic input and reference were rendered, while the original velocity values were retained for the reference.】 A dedicated comparison between timing representations is outside the reported experiment.

**写作推荐**：A（暂存，待 V-02 后定稿）。这里不应替作者改口说听测一定未量化，也不能把作者经验说成已核验的controlled comparison。A 的应用表述可以继续审查；所有正式协议句必须等既有刺激记录，不需重做实验。B 保留原说明的证据等级，不能原样带 author reports 进 thesis。C 仅在量化处理两边一致的具体条件成立时可用。

**边界／待核验**：【待核验：8个刺激输入、reference、生成脚本或作者具体说明】。现目录只有代码片段配置与文字，没有原刺激MIDI；不能定稿。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-22"></a>

## R1-22 单列 baselines，重排已有事实即可

**拟执行位置／操作**：在 Experimental Setup 新增 Baselines 小节，将 Quantitative Results 已有说明移入；以下为完整可用段落，原处不重复。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 241（当前来源 hash 见 SOURCES.md）

```latex
Tables~\ref{tab:velcomp_results_smd} and \ref{tab:velcomp_results_maestro} report the model performance when all trainable systems are trained only on the MAESTRO training set.
The Flat model assigns a fixed velocity of 64, corresponding to the default behaviour of common music software.
The Seq2Seq baseline uses pretrained weights from \cite{kim2023piano}, while ConvAE \cite{kuo2021velocity} is re-implemented and trained within the same framework.
Across both test conditions, the proposed U-Net outperforms the comparison systems on all reported objective metrics.
```

`Chapter_3/chap3.tex` line 194（当前来源 hash 见 SOURCES.md）

```latex
The trained models include the proposed U-Net and a re-implemented ConvAE baseline \cite{kuo2021velocity}.
Continuous segments from the same piece are arranged into the same batch in the training setup used here, with the aim of preserving local musical continuity.
Both models are trained for 300 epochs on the MAESTRO training set with learning rate \(10^{-5}\), batch size 3, and the same loss function.
Training takes approximately 12 hours on an NVIDIA V100 32~GiB GPU using the Ranger21 optimiser.
The top three checkpoints of each model, selected by validation performance on MAESTRO, are then tested on the MAESTRO test split and on SMD for cross-dataset evaluation.
```

**英文候选**

### A

We compare against three baselines. Flat assigns velocity 64 to every note and represents a sequence without note-wise dynamic variation. Seq2Seq uses the pretrained attention-based model of Kim et al. (2023). ConvAE follows Kuo et al. (2021) and is re-implemented in our training framework. ConvAE and the proposed U-Net are trained on the same MAESTRO split with the same training schedule and objective; Seq2Seq retains its available pretrained weights. All outputs are evaluated at the given note onsets using the metrics defined below.

**写作推荐**：A。无需新增网络细节或未经核验的parametercounts。既有引用键 kim2023piano / kuo2021velocity 应用于此段，英文作者年仅为阅读写法，排版沿作者最终citation选择。

**边界／待核验**：V-03 涉及ConvAE和U-Net实际输入mask分支：如强调“完全相同input”需run记录；本段只说已写明的训练schedule/objective。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-23"></a>

## R1-23 modular correction 的实际适用范围与联合模型互补

**拟执行位置／操作**：在 §4.4 末补一段；不改变训练或模型。

**准确原文与当前源码位置**

`Chapter_4/chap4.tex` line 50（当前来源 hash 见 SOURCES.md）

```latex
This separation of roles is important. The acoustic branch still provides the initial evidence for performance intensity. The score does not overwrite that evidence. Instead, it regularises the estimate by telling the model where notes occur and how they are organised in time. Later results will show that this division of labour is strong enough to improve both in-domain accuracy and cross-dataset behaviour.
```

**英文候选**

### A

This modular setting is useful when trusted note events already exist, as in aligned educational or archival material. It does not imply that velocity and note detection are independent in performance, or that joint modelling cannot improve transcription. The present evaluation isolates velocity estimation at known notes and therefore does not measure gains in note detection.

### B

The separation is a task definition rather than a claim that note content and dynamics are independent. It fits applications with a reliable score or existing note sequence, where replacing note decisions is unnecessary. Joint note-and-velocity models may use these quantities to support one another, but that benefit is outside an evaluation that supplies reference note events. The contribution here is a reusable refinement interface under this stated condition.

### C

Modular refinement and joint transcription address different use conditions. If a reliable note sequence is available, a velocity-only correction can improve its expressive layer while preserving the user's structure. If the note sequence is uncertain, a joint system may be more appropriate because dynamics and note evidence can interact. This chapter studies the first condition and leaves the second as an integration direction.

**写作推荐**：B。B 正面回应 ecological validity，承认联合建模价值而不撤回作者模块化贡献。A 较短，C 对应用条件分流更清楚但与原§4.3重复。

**边界／待核验**：“backbone unchanged”应指architecture/interface；当前训练写 jointly trained，Background写frozen需 V-04 核验，不能据此给全网络冻结承诺。

**关联意见**：R1-27; R1-37。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-24"></a>

## R1-24 Ch.4 实际上是矩阵接口加 onset tokens

**拟执行位置／操作**：在 §4.5.1 定义 O/F/Fex 后补充；这属于事实性解释，给一稿。

**准确原文与当前源码位置**

`Chapter_4/chap4.tex` line 67（当前来源 hash 见 SOURCES.md）

```latex
Consistent with the standard paradigm of score-informed MIDI velocity estimation \cite{kim2024method}, we rasterise the aligned score into pianoroll-like binary matrices at the same time resolution as the AMT output. Let $T$ be the number of frames and $P$ the number of piano keys. In our setting, $T=1001$ and $P=88$. We define the onset matrix $\mathbf{O}\in\{0,1\}^{T\times P}$, the frame matrix $\mathbf{F}\in\{0,1\}^{T\times P}$, and the onset-excluded sustain matrix $\mathbf{F}^{\mathrm{ex}}\in\{0,1\}^{T\times P}$ as
\begin{equation}
\mathbf{F}^{\mathrm{ex}} = \mathbf{F} - \mathbf{O}.
\label{eq:scoreinf:fex}
\end{equation}
We further define the nonzero index sets
\begin{equation}
\mathcal{I} = \{(t,p)\mid O_{t,p}=1\},
\qquad
\mathcal{J} = \{(t,p)\mid F_{t,p}=1\}.
\label{eq:scoreinf:index}
\end{equation}
The onset set $\mathcal{I}$ is used for tokenisation in the Transformer correction module. The frame set $\mathcal{J}$ is used for loss masking.
```

`Chapter_4/chap4.tex` line 106（当前来源 hash 见 SOURCES.md）

```latex
\textbf{Final design: score-informed Transformer correction module.} Our final design replaces the frame-wise BiLSTM with an onset-token Transformer correction module. For computational efficiency, we tokenise only the score onset coordinates in $\mathcal{I}$. This yields a variable-length sequence of $N=|\mathcal{I}|$ tokens per segment. For each onset token $i=(t_i,p_i)\in\mathcal{I}$, we form an embedding
\begin{equation}
\mathbf{x}_i = \mathbf{e}^{(t)}_{t_i} + \mathbf{e}^{(p)}_{p_i} + \mathbf{W}_f\mathbf{f}_i,
\label{eq:scoreinf:token}
\end{equation}
where $\mathbf{e}^{(t)}_{t_i}$ and $\mathbf{e}^{(p)}_{p_i}$ are learnable time and pitch embeddings. The feature vector $\mathbf{f}_i$ contains the onset-wise preliminary velocity $\hat{V}_{0,t_i,p_i}$ together with optional score-derived features from $\mathbf{F}$ or $\mathbf{F}^{\mathrm{ex}}$, projected by $\mathbf{W}_f$. Stacking all embeddings yields $\mathbf{X}\in\mathbb{R}^{N\times d}$. This sequence is processed by a lightweight Transformer encoder implemented as a streamlined Conformer-like block~\cite{gulati2020conformer}, as shown in Figure~\ref{fig:scoreinf_encoder}.
```

**英文候选**

### A

The matrices provide a common pitch–time interface with the AMT velocity map and make onset and sustain masking explicit. They are not the final sequence representation of the Transformer: the correction module extracts the known onset coordinates and processes them as note tokens. The frame-wise BiLSTM variant retains the dense grid for comparison. The final design therefore combines a piano-roll interface with event-centred correction rather than choosing dense matrices over event tokens throughout.

**写作推荐**：A。作者批注提到multi-scale，但本章最终模块是onset-tokenTransformer；不能把Ch.5架构动机借来当Ch.4事实。此稿直接对照数学定义与现有architecture，无需暗示尝试过任何未报告模型。

**边界／待核验**：不作eventtransformer与grid谁更优的普遍结论。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-25"></a>

## R1-25 明确 hybrid loss 的相对权重与证据边界

**拟执行位置／操作**：在 §4.5.3 公式后补充或替换解释段；保留已有 kim2024method 引用。

**准确原文与当前源码位置**

`Chapter_4/chap4.tex` line 133（当前来源 hash 见 SOURCES.md）

```latex
All models are trained with the hybrid loss adopted in prior score-informed work~\cite{kim2024method}. It combines frame-wise binary cross-entropy with onset-wise $\ell_1$ loss:
\begin{equation}
\mathcal{L}
= \frac{1}{|\mathcal{J}|}\sum_{(t,p)\in\mathcal{J}} \ell_{\mathrm{bce}}\big(V_{t,p},\hat{V}_{t,p}\big)
+ \frac{1}{|\mathcal{I}|}\sum_{(t,p)\in\mathcal{I}} \left|V_{t,p}-\hat{V}_{t,p}\right|.
\label{eq:scoreinf:loss}
\end{equation}
Here $\mathbf{V}$ is the ground-truth velocity target and $\hat{\mathbf{V}}$ is the predicted velocity output of either the baseline AMT branch or the score-informed system. This hybrid supervision is useful because it constrains both the local onset value and the broader note sustain region, while still keeping note-level precision central to the objective.
```

`Chapter_4/chap4.tex` line 133（当前来源 hash 见 SOURCES.md）

```latex
All models are trained with the hybrid loss adopted in prior score-informed work~\cite{kim2024method}. It combines frame-wise binary cross-entropy with onset-wise $\ell_1$ loss:
\begin{equation}
\mathcal{L}
= \frac{1}{|\mathcal{J}|}\sum_{(t,p)\in\mathcal{J}} \ell_{\mathrm{bce}}\big(V_{t,p},\hat{V}_{t,p}\big)
+ \frac{1}{|\mathcal{I}|}\sum_{(t,p)\in\mathcal{I}} \left|V_{t,p}-\hat{V}_{t,p}\right|.
\label{eq:scoreinf:loss}
\end{equation}
Here $\mathbf{V}$ is the ground-truth velocity target and $\hat{\mathbf{V}}$ is the predicted velocity output of either the baseline AMT branch or the score-informed system. This hybrid supervision is useful because it constrains both the local onset value and the broader note sustain region, while still keeping note-level precision central to the objective.
```

**英文候选**

### A

Each component is averaged over its own mask, and the two means have equal relative coefficients in the stated objective. This is a fixed design choice adopted from Kim et al. (2024), not a claim that the two losses or their gradients have equal numerical magnitude.

### B

The frame-wise BCE and onset-wise L1 terms are normalised by their respective active positions and combined with equal relative coefficients. We follow the hybrid objective of Kim et al. (2024); our preliminary comparison also favoured hybrid supervision over frame-only or onset-only alternatives, as reported in the associated SMC paper. This supports the retained formulation, but does not establish that equal weighting is optimal for every backbone or dataset.

### C

The two terms serve related but different roles: frame-wise BCE supervises the active note region, while onset-wise L1 directly penalises the note velocity read during post-processing. Averaging each term over its own mask avoids making its contribution depend only on the number of active frames. We retain the equal-coefficient hybrid used in the prior work and our preliminary verification, without claiming a universal balance of gradient magnitudes.

**写作推荐**：B。上传SMC PDF §3.3确实写preliminary hybrid vs single-target comparison，支持作者“我验证过”；没有ratio sweep记录则不能写“最佳比例已完整证明”。A最短，C解释任务目的。固定代码theta=.5与论文sum有共同整体尺度差异，但相对1:1相同；不擅改公式。

**边界／待核验**：V-04：核对实际run的theta及作者验证范围；不能把defaultconfig当最终run。若不愿在正文提paper，可把as reported...改为现有citation，事实仍保留。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-26"></a>

## R1-26 Table4.1 每个 setup 用现有变量逐一解释

**拟执行位置／操作**：在 Table4.1 前补一段定义，表格数字保持原样。

**准确原文与当前源码位置**

`Chapter_4/chap4.tex` line 182（当前来源 hash 见 SOURCES.md）

```latex
We first attach the proposed modules to HPT and denote the resulting systems as Score-HPT. HPT is used as the initial testbed because it is lightweight and prevalent in recent piano transcription work. This lets us isolate the effect of score-informed correction before extending the method to other backbones. Table~\ref{tab:scoreinf_maestro} summarises the results on the MAESTRO test set.
```

`Chapter_4/chap4.tex` line 67（当前来源 hash 见 SOURCES.md）

```latex
Consistent with the standard paradigm of score-informed MIDI velocity estimation \cite{kim2024method}, we rasterise the aligned score into pianoroll-like binary matrices at the same time resolution as the AMT output. Let $T$ be the number of frames and $P$ the number of piano keys. In our setting, $T=1001$ and $P=88$. We define the onset matrix $\mathbf{O}\in\{0,1\}^{T\times P}$, the frame matrix $\mathbf{F}\in\{0,1\}^{T\times P}$, and the onset-excluded sustain matrix $\mathbf{F}^{\mathrm{ex}}\in\{0,1\}^{T\times P}$ as
\begin{equation}
\mathbf{F}^{\mathrm{ex}} = \mathbf{F} - \mathbf{O}.
\label{eq:scoreinf:fex}
\end{equation}
We further define the nonzero index sets
\begin{equation}
\mathcal{I} = \{(t,p)\mid O_{t,p}=1\},
\qquad
\mathcal{J} = \{(t,p)\mid F_{t,p}=1\}.
\label{eq:scoreinf:index}
\end{equation}
The onset set $\mathcal{I}$ is used for tokenisation in the Transformer correction module. The frame set $\mathcal{J}$ is used for loss masking.
```

**英文候选**

### A

In Table 4.1, audio denotes the standalone HPT velocity branch. The score-informed rows add either the frame-wise BiLSTM or the onset-token Transformer correction module. The onset condition uses the score onset matrix O; onset + frame additionally supplies the active-note matrix F; and onset + frame_ex uses F − O to distinguish sustain from the onset frame. These conditions vary the correction module and its score features under the same MAESTRO training and evaluation setting. Parameter counts refer to the complete velocity-estimation system shown in each row.

**写作推荐**：A。对照表中每行和已有 O/F/Fex 定义，避免再创造setup编号。若公式采用label引用，最终改成Table~ref避免编号漂移。

**边界／待核验**：实际train_mode、SMD development subset是否用于设计选择另记V-04；本段不替协议打包票。 方法段当前BiLSTM只展示3P拼接，未展示onset-only维度；需按已有run配置补准确形状，不能推测。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-27"></a>

## R1-27 完整 AMT 集成作为未来方向，不虚报已验证性能

**拟执行位置／操作**：在 Ch.5 §5.3 两种使用方式后插一段；Ch.7 §7.4.5 用所选稿最后两句承接，避免重复整段。与R1-37共用。

**准确原文与当前源码位置**

`Chapter_5/chap5.tex` line 36（当前来源 hash 见 SOURCES.md）

```latex
Given a piano performance audio signal, the system predicts four synchronised output sequences on a frame grid: dynamic levels, dynamic change points, beats, and downbeats. The dynamic targets are the score-facing outputs, while beats and downbeats provide the metrical structure required to align these labels to a symbolic score. This joint design serves two practical modes of use. In the first mode, a reliable beat grid is already available from an aligned score or a score-level AMT system, and the predicted dynamic labels are attached to that grid. In the second mode, no score is available, and the model first predicts beats and downbeats by itself, then uses the estimated grid to place the dynamic labels.
```

`Chapter_7/Conclusion.tex` line 157（当前来源 hash 见 SOURCES.md）

```latex
The broader direction is an AMT paradigm in which note detection is only the first layer. A musically useful transcription should not stop at pitch and onset. It should also recover the expressive information that makes the transcription interpretable as performance and usable as symbolic music data. Dynamics is the layer studied in this thesis, but the same logic can extend to articulation, pedal, phrasing, and timbre.
```

**英文候选**

### A

These outputs could be attached to the note content of a score-level AMT system to produce dynamics-annotated notation. The present experiments evaluate dynamics and metrical estimation separately from note transcription, so they do not establish the performance of a complete integrated AMT system or an improvement in note-detection accuracy.

### B

A practical integration would combine the estimated dynamics with note content from a score or a note-transcription system, using a shared beat grid. This provides a route to expressive notation, but it introduces additional alignment and error-propagation questions. The present thesis evaluates the dynamics components under their stated inputs; a complete system and any benefit to pitch, onset, or offset accuracy remain to be tested.

### C

The models supply complementary expressive layers that could enrich an AMT output. Chapter 4 refines velocity at known notes, while Chapter 5 provides score-facing markings on a metrical grid. Combining these layers with note transcription is a natural next step. It would require evaluating both the recovered dynamics and the complete symbolic output, because perceptual usefulness and note-event accuracy need not improve together.

**写作推荐**：B。B 是可实施的接口解释且明确未测pitch/onset/offset效益，保留作者想做但需要更多时间的立场。A最小，C跨章衔接最好但新增内容略多。没有把BSSL feature直接等同听觉偏好已证实。

**关联意见**：R1-23; R1-37。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-28"></a>

## R1-28 state 与 boundary 是互补监督，并非二选一

**拟执行位置／操作**：在 §5.3 target 定义后补一段，强调现有 beat-level decoding。

**准确原文与当前源码位置**

`Chapter_5/chap5.tex` line 38（当前来源 hash 见 SOURCES.md）

```latex
More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat.
```

`Chapter_5/chap5.tex` line 97（当前来源 hash 见 SOURCES.md）

```latex
Change points are determined in two stages. First, we identify all frames whose change-point probability exceeds 75\%. Second, we snap each candidate to the nearest detected beat. This beat-snapping step is motivated by the annotation style of MazurkaBL, where dynamic markings are beat-aligned rather than freely placed in continuous time \cite{kosta2018mazurkabl}. The step also keeps evaluation consistent with prior work \cite{kosta2017thesis}.
```

**英文候选**

### A

The dynamic-level head estimates the prevailing state, while the change-point head estimates where that state changes. Both are converted to the beat grid during decoding. The separate boundary target complements beat-wise level prediction; it does not replace it.

### B

Beat-wise level prediction and change-point estimation answer different questions: which dynamic level applies, and where a new dynamic region begins. The model predicts both on the frame grid, with the dynamic loss masked to annotated beats and change points snapped to beats during decoding. A separate boundary head gives transitions their own supervision rather than deriving every change from fluctuations in the level sequence. The present experiments do not establish that it is the only valid formulation.

### C

A score-facing annotation needs both a level and a decision about when to write a new marking. Predicting a level at each beat supplies the first, but does not by itself distinguish a stable region from a new notated event. The change-point head explicitly models that boundary decision and is decoded on the same beat grid. This is the role of the separate target, rather than an alternative to beat-synchronous dynamics.

**写作推荐**：B。B 接住作者“dynamic markingsdecode到beat”的说明，同时解释为何还有CPt。A短但理由少；C叙述自然但“newnotatedevent”需与数据CPt标签定义一致。不声称已有去CPthead独立消融证明必需。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-29"></a>

## R1-29 共享表征、分头 loss 与 decoding 连接同时说明

**拟执行位置／操作**：在 §5.5.2 metrical post-processing 后补说明；Fig5.2提案副本用虚线连接两个输出至共同postprocessing框，而非新增learnedheadedge。

**准确原文与当前源码位置**

`Chapter_5/chap5.tex` line 79（当前来源 hash 见 SOURCES.md）

```latex
The shared encoder provides a common latent representation, but the tasks remain acoustically diverse. To reduce negative transfer, we use a Multi-gate Mixture-of-Experts (MMoE) layer \cite{ma2018mmoe} as a task-aware decoder.
```

`Chapter_5/chap5.tex` line 95（当前来源 hash 见 SOURCES.md）

```latex
The model outputs frame-wise probabilities, which are converted into discrete musical events through tailored post-processing. For beat and downbeat detection, we use the thresholding and local-maximum peak-picking steps of \cite{foscarin2024beat}: probabilities are thresholded at 50\%, and peak picking is applied within a 7-frame local neighbourhood (radius 3 at 50~fps). For dynamic markings, the dynamic level at each beat is determined by taking the \texttt{argmax} of the class probabilities at that frame. When an external beat grid is available, this sampling step is performed on that grid; otherwise, the model's own beat predictions are used, which gives the fully end-to-end mode considered in this chapter.
```

**英文候选**

### A

Beat and downbeat predictions share the encoder and expert pool, but use separate heads and loss terms. Their event outputs are linked during post-processing: when predicted beats are available, detected downbeats are snapped to the nearest predicted beat and duplicate positions are removed. No explicit beat–downbeat consistency term is added to the training loss.

### B

The beat and downbeat tasks are coupled through shared representation learning and through decoding, rather than by a direct connection between their output heads. Each head has its own shift-tolerant loss. In post-processing, downbeats are moved to the nearest predicted beat when a beat sequence is available, with duplicate events removed. This enforces the event-level relation at decoding time without adding a learned cross-head constraint.

### C

The architecture separates task-specific prediction from musical consistency at the output. The shared encoder and MMoE experts let beat and downbeat learning use common evidence, while separate gates, heads, and losses preserve their task-specific decisions. The decoder then snaps downbeats to predicted beats where available. A stronger consistency objective during training is a possible extension, but is not part of the reported model.

**写作推荐**：B。固定beat_postproc.py明确有条件snap和dedup，符合作者第二条回复。B清楚区分coupling阶段；A最短，C更完整但会与MMoE段重复。不再写“只有共享，完全无连接”。

**边界／待核验**：【最终评估run应核对是否调用此postprocessor】。来源代码的存在与作者说明相互支持，但不自动覆盖所有 baseline 的解码行为。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-30"></a>

## R1-30 cross-dataset 是测迁移边界，不是分离风格因果

**拟执行位置／操作**：在 cross-dataset 小节首段后补充；当前数值与 averaging/checkpoint 规则待V-05，不在此改表。

**准确原文与当前源码位置**

`Chapter_5/chap5.tex` line 328（当前来源 hash 见 SOURCES.md）

```latex
The 5-fold MazurkaBL evaluation already gives a partial test of generalisation, because the folds are piece-disjoint and the model is always evaluated on unseen mazurkas within the same corpus. However, it remains an in-domain setting: performer pool, recording conditions, repertoire family, and annotation conventions are all inherited from MazurkaBL. We therefore add a stricter cross-dataset experiment on Vienna4x22 and Batik-plays-Mozart, using them as test-only corpora after the MazurkaBL training stage.
```

`Chapter_5/chap5.tex` line 392（当前来源 hash 见 SOURCES.md）

```latex
The cross-dataset results make this distinction more concrete. If score dynamics were merely a continuous loudness variable relabelled into five fixed bins, an out-of-domain corpus with compatible audio quality would mainly cause smooth calibration errors. Instead, Vienna4x22 shows that the symbolic prior itself matters: a passage that is moderate in acoustic intensity may be notated as \textit{p}, \textit{mf}, or \textit{f} depending on the local phrase, edition, and corpus convention. A model trained on MazurkaBL carries a learned expectation about how often each of these labels should occur, and this expectation can become wrong even when the metrical grid remains reasonably stable. The model is therefore learning an acoustic, metrical, and editorial mapping at the same time.
```

**英文候选**

**不论选A/B/C均需附加的协议说明**（以当前书面protocol为条件，原run对齐后采用）

Under the selection rule described here, labels from each external corpus are used to choose the transferred fold: the multitask fold is selected by dynamic F1, while single-task models are selected separately for their respective tasks. No fine-tuning is performed on the external recordings, but the reported selection is still informed by the target labels. The scores should therefore be read as a target-selected transfer diagnostic and may be optimistic relative to an evaluation in which model selection is fixed before seeing target labels.

### A

Cross-dataset evaluation asks whether the learned dynamics mapping remains useful when repertoire, performers, recording conditions, and annotation conventions change together. It does not isolate the effect of any one of these factors, and a transfer gap is therefore not a direct estimate of a composer or performer effect.

### B

Composer- and performer-dependent dynamics make external evaluation useful rather than unnecessary. A model trained on one corpus may learn its repertoire and annotation conventions as well as acoustic cues. Vienna4x22 and Batik-plays-Mozart test this combined shift, but their size and composition do not permit a balanced attribution to composer, performer, or recording conditions. The results are transfer diagnostics, not evidence of uniform generalisation.

### C

The external tests probe where the learned mapping stops transferring. They complement piece-disjoint MazurkaBL folds by changing several corpus conditions at once, including repertoire and score-label conventions. Their mixed outcomes therefore help delimit the claim: a perceptually motivated front-end does not remove stylistic or editorial dependence. A balanced study would be needed to separate those effects, but is outside the current experiment.

**写作推荐**：B。保留作者“正因style/performer相关才要测”的立场，同时不能把当前Vienna明显降低概括成goodgeneralisation。A最小；C解释失败边界强，可能与已有讨论重复。

**边界／待核验**：V-05：目标corpus标签用于bestfold选择时只能称target-selecteddiagnostic，不能描述成完全未经target选择的无偏deployment。实际表与协议未对齐前，不填因果解释或更强结论。 上述英文disclosure准确描述当前书面protocol，不保证当前表值已按该protocol生成；V-05仍需原run来源。若实际汇总规则不同，应先对齐规则再采用相应说明。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-31"></a>

## R1-31 不用未测的 simpler 或 efficiency 优越性

**拟执行位置／操作**：替换 §6.2 对 synthetic-data transfer 的过渡段；作者想强调省标签／更直接，不能扩大成已测运行效率。

**准确原文与当前源码位置**

`Chapter_6/chap6.tex` line 31（当前来源 hash 见 SOURCES.md）

```latex
This chapter takes a different and simpler route. Instead of training on synthesised audio with synthetic labels, the front-end estimator is trained directly against real performance audio. The synthesiser is involved at training time only as a differentiable interface that connects predicted velocities to a measurable property of the real recording. This avoids the synthesis-to-performance domain gap that dominates synthetic-data transfer pipelines, at the cost of needing a differentiable supervision interface that is reliable across the instruments of interest.
```

**英文候选**

### A

This chapter instead adapts the estimator directly on real performance audio without requiring target-domain velocity labels. A differentiable renderer supplies the indirect training signal, while renderer mismatch remains a limitation.

### B

This chapter takes a more direct route to target-domain adaptation. Rather than relying only on transfer from synthetically labelled audio, the estimator is adapted using real performance recordings and a differentiable rendering interface. This reduces dependence on target velocity annotation, but does not remove the need to model or approximate the renderer.

### C

The practical aim is to reduce dependence on unavailable target-domain velocity labels. We therefore train the adaptation stage against real performance audio through a differentiable interface. The advantage concerns access to supervision; it is not a claim that designing the synthesiser or proxy is simpler, or that its computational cost is lower than all alternatives.

**写作推荐**：B。B 既保留作者更直接／减少annotation需求的意思，也与上传ISMIR的more direct route一致。A最短，C明确比较轴但否定句偏多。作者提moreefficient可理解为labelacquisition效率，未经测量不建议直接写generalefficiency。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-32"></a>

## R1-32 V^(0) 是粗估 roll，Vhat 是 correction 后的逐音值

**拟执行位置／操作**：替换 §6.4.1 最后一段；明确 fixed 指 architecture，不把 adaptation 中 VeloEst 写成权重冻结。

**准确原文与当前源码位置**

`Chapter_6/chap6.tex` line 93（当前来源 hash 见 SOURCES.md）

```latex
The estimator has two stages. The acoustic module, borrowed from the High-Resolution Piano Transcription system~\cite{kong2021hpt}, takes log-Mel spectrograms computed at $100$\,fps from $22050$\,Hz mono audio (FFT size $2048$, hop $221$\,samples, Hann window) as input and predicts a coarse velocity roll $V^{(0)}$. A score-informed Transformer then refines $V^{(0)}$ into $\hat{V}$ using aligned note information. The detailed architecture and supervised training procedure are given in Chapter~\ref{ch:scoreinf}; the present chapter treats this estimator as a fixed black-box front-end whose checkpoint is then adapted.
```

`Chapter_6/chap6.tex` line 91（当前来源 hash 见 SOURCES.md）

```latex
VeloEst acts as the shared front-end of the framework, estimating note-wise MIDI velocities $\hat{V}$ from the performance audio and aligned note events. We use the score-informed HPT model with onset and frame as score-guidance, which is identified as the best VeloEst configuration in Chapter~\ref{ch:scoreinf}~\cite{he2026score}. We keep its architecture unchanged and use the publicly available checkpoint trained on MAESTRO with ground-truth velocity supervision $\mathcal{L}_{\mathrm{velo}}$. This fixed estimator keeps the cross-instrument experiment focused on the supervision interface rather than on introducing a new velocity-estimation architecture.
```

**英文候选**

### A

VeloEst first predicts a coarse frame-wise velocity roll V^(0) from audio. The score-informed Transformer refines the values at the aligned note onsets, and V-hat denotes the corrected note-wise values read for the rendering interface. The superscript (0) identifies the intermediate acoustic stage, not the pre-adaptation checkpoint. When the estimates are stored as a roll, the renderer still receives the corresponding onset reads. The architecture is kept unchanged during adaptation, but its parameters are fine-tuned; the synthesis or proxy back-end remains frozen.

**写作推荐**：A。直接解决符号区分和roll/vector层级，顺便消除同段fixedblackbox与fine-tuned矛盾。最终LaTeX应保留原数学符号V^{(0)}、hat V，勿将此阅读用plaintext符号原样写进正文。

**边界／待核验**：需与 Ch.4 记号 Vhat_0 / Vhat_corr 做crossreference；不要求全章大规模改名。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-33"></a>

## R1-33 DDSP fidelity 是限制，退化不等于因果证明

**拟执行位置／操作**：在 §6.4.2 末增加，并把 Results 中确定性因果说法改为 consistent with。

**准确原文与当前源码位置**

`Chapter_6/chap6.tex` line 111（当前来源 hash 见 SOURCES.md）

```latex
The advantage of this interface is that it exposes the front end to rich waveform gradients. The risk, already noted in Section~\ref{sec:bp:related}, is that any timbral or recording mismatch between $\tilde{a}$ and $a$ also enters the gradient. When the synthesiser is not a faithful match for the target recordings, the gradient can become dominated by nuisance compensation rather than by velocity correction.
```

`Chapter_6/chap6.tex` line 429（当前来源 hash 见 SOURCES.md）

```latex
Second, on guitar (Table~\ref{tab:bp_results_guitar}) Diff-SFProxy achieves the best $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ on both GAPS and FL datasets, outperforming flat velocity, zero-shot transfer, and Diff-Synth across all back-end crop lengths. Diff-Synth, by contrast, does not reliably improve guitar performance and can degrade it. On FL dataset, the $5$\,s Diff-Synth back-end falls below flat velocity in $r_{\mathrm{BSSL}}$ ($0.646$ vs.\ $0.714$). This supports the concern raised in Section~\ref{ssec:bp:adapt_diffsynth}: waveform-level objectives are more exposed to timbral and room-acoustic mismatch than parameter-level supervision.
```

**英文候选**

### A

DDSP-Piano and DDSP-Guitar-Synth are differentiable approximations of the target instruments. Their timbre and velocity response need not match the real recordings. The observed degradation after Diff-Synth adaptation is consistent with acoustic mismatch, but we have not separately measured reconstruction fidelity or the accuracy of velocity-related gradients on the target data.

### B

The waveform back-ends are used as differentiable approximations rather than exact reproductions of the recorded instruments. Their usefulness depends both on acoustic fidelity and on whether changing velocity produces the appropriate change in sound. The Diff-Synth results are consistent with a mismatch in this interface, but do not isolate its cause: reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.

### C

A differentiable synthesiser can offer useful gradients without reproducing every detail of a recording, but the relevant error is not timbral fidelity alone. Its velocity-to-sound response must also be suitable for the adaptation target. The present comparison shows weaker adaptation with the selected Diff-Synth back-ends; it does not establish which component of their mismatch caused the degradation. This limits the conclusion to the tested interfaces and recordings.

**写作推荐**：B。B几乎保持作者当前回复的谨慎证据边界，区分waveformfidelity和velocitygradientfaithfulness。A最短，C逻辑更细但易重复现有discussion。不追加faithfulness实验。

**全文同步提案**（原文件均未改）

- `Chapter_6/chap6.tex`
  - 原：A waveform or spectral loss therefore spends much of its gradient budget on residual mismatch rather than on velocity-dependent behaviour.
  - 拟：A waveform or spectral loss can be influenced by residual mismatch as well as velocity-dependent behaviour.

- `Chapter_6/chap6.tex`
  - 原：Longer crops give waveform-level objectives more of the underlying timbral mismatch to fit, while parameter-level supervision sees only per-note targets and is therefore much less sensitive to crop length.
  - 拟：The crop-length pattern is consistent with greater exposure of the waveform objective to acoustic mismatch, but the present comparison does not isolate that mechanism.

- `Chapter_6/chap6.tex`
  - 原：Diff-SFProxy avoids this contamination by treating velocity as the only loudness-shaping degree of freedom, but the choice carries its own cost.
  - 拟：Diff-SFProxy restricts the adapted control to velocity, but this does not remove effects of unobserved controls from the target audio.

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-34"></a>

## R1-34 Huber 的梯度理由与 MAE 对照边界

**拟执行位置／操作**：替换 §6.4.3 对 Huber 的解释句，保留β=1.0及1:1 PHE/OSF现有设置。

**准确原文与当前源码位置**

`Chapter_6/chap6.tex` line 116（当前来源 hash 见 SOURCES.md）

```latex
In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). The Huber form tolerates outliers from onset contamination such as overlapping notes, while the parameter-space objective concentrates gradients on note intensity and attack behaviour rather than on waveform details that are weakly related to velocity.
```

`Chapter_6/chap6.tex` line 116（当前来源 hash 见 SOURCES.md）

```latex
In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). The Huber form tolerates outliers from onset contamination such as overlapping notes, while the parameter-space objective concentrates gradients on note intensity and attack behaviour rather than on waveform details that are weakly related to velocity.
```

**英文候选**

### A

We use Huber loss with beta = 1. It is quadratic for small residuals and L1-like for larger residuals, giving smoother gradients near zero while limiting the influence of large errors. No dedicated comparison with MAE is reported.

### B

Huber loss is used for its quadratic behaviour near zero and L1-like behaviour for larger residuals. With beta = 1, it provides smoother small-error gradients than MAE while retaining a linear penalty for large PHE/OSF errors. This is a design rationale; a dedicated MAE comparison has not established that Huber gives better adaptation in this setting.

### C

The parameter targets can contain residual error from overlapping notes and imperfect onset alignment. Huber provides a smooth small-error region while retaining linear growth for larger residuals, so it is a practical compromise for the chosen objective. We use beta = 1 throughout. The choice should not be read as an experimentally established advantage over MAE, which also has a linear penalty for large errors.

**写作推荐**：B。B与作者原回复一致，避免把MAE本来也robust的性质误说成Huber独有优势。A最短，C结合场景但“imperfectalignment”只是合理动机非独立测量。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-35"></a>

## R1-35 Fig6.2 已提 rendered audio，补图内 teacher 路径

**拟执行位置／操作**：原caption已有SoundFont-rendered，不声称整项未回应。候选副本在teacher支路的SoundFont和targetparams之间加框“SoundFont-rendered audio”；当前资产teacher在左侧，不照搬评审right的位置。

**准确原文与当前源码位置**

`Chapter_6/chap6.tex` line 201（当前来源 hash 见 SOURCES.md）

```latex
\begin{figure}[t]
\centering
\includegraphics[width=0.68\columnwidth]{Chapter_6/figures/p2.jpg}
\caption{An encoder-only Transformer maps padded note sequences to per-note PHE/OSF targets extracted from SoundFont-rendered audio.}
\label{fig:bp_proxy_arch}
\end{figure}
```

**英文候选**

### A

Offline training of the differentiable SoundFont proxy. Sampled MIDI notes and velocities are rendered by the SoundFont; PHE and OSF extracted from this rendered audio provide the teacher targets. The Transformer predicts the same parameters from the note sequence. Real performance audio is used later for VeloEst adaptation, not to generate these offline teacher targets.

**写作推荐**：A。caption区分两训练阶段；图内明确中间audio节点即可。现图已有“Render MIDI to Audio”，因此也可选择仅保留原图／增加目标标签，不必重新设计整个架构。

**边界／待核验**：【待绘图副本与视觉核验】。任何修改只在提案副本，当前图源不变。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-36"></a>

## R1-36 自动选择 SoundFont 留为明确未来工作

**拟执行位置／操作**：在 §6.9.4 第一段后补两至三句，不追加实验。

**准确原文与当前源码位置**

`Chapter_6/chap6.tex` line 517（当前来源 hash 见 SOURCES.md）

```latex
Several boundaries should be kept in mind. First, the recovered velocity is renderer-conditioned (Section~\ref{ssec:bp:scope}). The SoundFont is selected by ear from a small candidate pool. A mismatched SoundFont would produce a teacher signal that the target recordings cannot match, so renderer choice is part of the operational definition rather than an incidental detail.
```

**英文候选**

### A

Automating SoundFont selection is a natural extension. A matching procedure could compare candidate renderers with representative target recordings, but should assess their velocity response as well as timbral similarity.

### B

Automatic SoundFont selection could make the framework easier to apply to larger or more varied corpora. Such a procedure would need to consider both timbral match and the velocity-dependent response that supplies the training signal. The present study uses by-ear selection and does not evaluate an automated selection method.

### C

Renderer selection is part of the definition of the recovered velocity, so automation would change more than an implementation detail. A useful selection procedure should choose a renderer whose sound and velocity response fit the intended target material. Developing and evaluating that procedure remains future work; the current results retain the stated manually selected SoundFonts.

**写作推荐**：B。B肯定评审想法且保留作者“重要但目前未做”的立场。上传ISMIR结尾已有同一futurework；不把自动选择当成本轮必做条件。A最短，C更强调operationaldefinition。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-37"></a>

## R1-37 完整 AMT 与 note accuracy 的回应统一放一处

**拟执行位置／操作**：采用 R1-27 所选稿的跨章／future version，保留其性能未验证的边界，不重复整段。

**准确原文与当前源码位置**

`Chapter_7/Conclusion.tex` line 157（当前来源 hash 见 SOURCES.md）

```latex
The broader direction is an AMT paradigm in which note detection is only the first layer. A musically useful transcription should not stop at pitch and onset. It should also recover the expressive information that makes the transcription interpretable as performance and usable as symbolic music data. Dynamics is the layer studied in this thesis, but the same logic can extend to articulation, pedal, phrasing, and timbre.
```

**英文候选**

### A

Integrating the proposed dynamics layers with note transcription is a natural next step. Such a system should be evaluated for expressive usefulness as well as pitch, onset, and offset accuracy; the present component-level studies do not establish an improvement in those note-transcription measures.

**写作推荐**：A。保留作者对human-prefer与客观指标可能不一致的判断，但不把这种可能性写成本文已测结论。

**关联意见**：R1-27。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r1-38"></a>

## R1-38 明确未显式恢复渐强渐弱，加入 span 输出方向

**拟执行位置／操作**：在 Ch.7 §7.3 score-dynamics 限制段后补；若选B/C，后一句放 §7.4.2 或单独简短future段，避免§7.3重复。

**准确原文与当前源码位置**

`Chapter_7/Conclusion.tex` line 115（当前来源 hash 见 SOURCES.md）

```latex
Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.
```

`Chapter_5/chap5.tex` line 399（当前来源 hash 见 SOURCES.md）

```latex
Several limitations should be kept in mind. First, the dynamic vocabulary is restricted to the five static score levels present in MazurkaBL plus a \textit{blank} class. The model does not explicitly represent longer-span symbols such as \textit{crescendo} and \textit{diminuendo}; instead, it captures local transitions through change points. Second, the beat-aligned post-processing reflects the annotation style of MazurkaBL. This is musically sensible for this dataset, but it may not transfer directly to corpora with different editorial conventions.
```

**英文候选**

### A

The score-dynamics model is restricted to the five static levels in MazurkaBL and their change points. It does not explicitly recover crescendo, diminuendo, or other span-based expressive symbols, which remain future targets.

### B

The five static levels and change points studied in Chapter 5 do not cover the full dynamics vocabulary. A change point indicates a boundary between regions; it does not specify the onset, duration, or direction of a crescendo or diminuendo. Extending the output to such spans would require compatible annotations and an evaluation of both the symbol and its temporal extent.

### C

Score dynamics includes sustained instructions as well as discrete levels. The present model estimates static levels and local transitions, leaving gradual directions such as crescendo and diminuendo implicit. A future score-facing interface could represent these as labelled spans alongside the beat-wise levels, while preserving the distinction between a gradual instruction and an abrupt change of dynamic state.

**写作推荐**：B。B说明CPt不等于hairpin，限制与future要求相连而不提出本轮新实验。A最短，C叙述顺畅但implicit可能被误读为已可靠检测，因此B更稳。

**关联意见**：R1-12。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r2-01"></a>

## R2-01 现有章节首尾已经显式回应中心问题，推荐保留

**拟执行位置／操作**：推荐不追加四段重复导语；保留现有 Overview/Summary，由 R1-15 修正 Ch.3 条件用语，R1-06 澄清 Ch.6 与S2。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 13（当前来源 hash 见 SOURCES.md）

```latex
This chapter addresses Scenario~S1, the most controlled setting in the thesis map. Here the symbolic notes and their timing are already known, but the note-level velocity is missing, flattened, or musically uninformative. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?
```

`Chapter_4/chap4.tex` line 8（当前来源 hash 见 SOURCES.md）

```latex
This chapter addresses Scenario S2 of the thesis. In this setting, a performance audio recording and an aligned symbolic score are both available. This situation is common in music education, rehearsal analysis, and curated audio--score archives. The score supplies reliable note content and approximate temporal structure. However, its expressive information is often incomplete, simplified, or unreliable. At the same time, modern automatic music transcription (AMT) systems can estimate note-level MIDI velocity from audio, but these estimates remain noisy and sensitive to acoustic domain shift. The central question of this chapter is: \emph{when note events are already known from a score, how should score information be used to improve AMT-estimated velocity without redesigning the whole transcription backbone?}
```

`Chapter_5/chap5.tex` line 11（当前来源 hash 见 SOURCES.md）

```latex
Score-level dynamic markings such as \emph{p}, \emph{mf}, and \emph{f} provide the principal human-readable description of musical intensity in notated music. These markings are inherently relative, are naturally indexed by the beat grid rather than by individual note onsets, and cannot in general be inferred from the symbolic score itself. This chapter addresses Scenario~S3 of the thesis, in which performance audio is the only available input and the desired output is a beat-synchronous symbolic description of dynamics. Recovering such a representation requires not only the dynamic labels themselves but also the metrical structure needed to anchor them on a score.
```

`Chapter_6/chap6.tex` line 14（当前来源 hash 见 SOURCES.md）

```latex
From the thesis perspective, this chapter occupies a distinct position. It keeps the note-level MIDI velocity target and the score-informed VeloEst architecture introduced in Chapter~\ref{ch:scoreinf}, but it relaxes the assumption that ground-truth velocity labels are available for the target instrument. It complements Chapter~\ref{ch:audiodyn}, which addressed Scenario~S3 with a different output (beat-synchronous score dynamics), by extending the velocity-focused work to a label-scarce setting. The chapter therefore contributes to thesis Requirement~R5 by combining numerical diagnostics, perceptual loudness correlations, and renderer-robust evaluation evidence, and to Requirement~R6 by treating beyond-piano transfer as a missing-supervision problem rather than ordinary acoustic domain shift.
```

**英文候选**

### A

No additional thesis paragraph is proposed. The existing chapter overviews explicitly state the data condition, dynamics target, and relation to the thesis question. Retain those paragraphs, subject to the specific terminology and scope corrections identified in R1-06 and R1-15.

**写作推荐**：A。报告2也肯定现有chapterpositioning结构。逐章实际原文已经给scope，不为形式性满足建议堆叠同义段。最终revisionreport可准确说“保留并澄清已有联系”，不能称新增了四段若没新增。

**关联意见**：R1-06; R1-15; R2-02。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r2-02"></a>

## R2-02 四篇论文的技术贡献与 thesis 新增综合分开

**拟执行位置／操作**：替换 §1.8 第一段；短mapping可用既有authorshipdeclaration的crossreference，不改80%声明或抢占未核实的新增实验。

**准确原文与当前源码位置**

`Chapter_1/Intro.tex` line 177（当前来源 hash 见 SOURCES.md）

```latex
Referring to Figure~\ref{fig:intro_overview}, the core methodological chapters (Chapters 3--5) preserve the technical contributions of their respective peer-reviewed publications, adapted to form a unified narrative.
```

`Chapter_1/Intro.tex` line 161（当前来源 hash 见 SOURCES.md）

```latex
\begin{itemize}
    \item \textbf{A thesis-level formulation of dynamics-oriented label recovery.} The dissertation argues that dynamics should be treated as a primary target in expressive AMT and evaluates the robustness across diverse data distributions rather than relying on a single, idealised dataset.
    
    \item \textbf{A symbolic method for note-level velocity completion (Addressing S1).} It reformulates MIDI velocity completion as an image-colourisation problem on sparse piano-roll representations, introducing a U-Net architecture with window attention and a sparsity-aware loss \cite{he2025filling}.
```

**英文候选**

### A

Chapters 3–6 develop the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common dynamics-recovery question, a comparison of data-availability conditions, and a cross-chapter discussion of representation and evaluation. These thesis-level syntheses should be distinguished from the method contributions attributed to the individual studies.

### B

The technical chapters are based on four co-authored studies: symbolic velocity completion (CMMR 2025, Chapter 3), score-informed correction (SMC 2026, Chapter 4), joint dynamics and metrical estimation (ICASSP 2026, Chapter 5), and cross-instrument proxy supervision (ISMIR 2026, Chapter 6). Their authorship and publication details are listed in the Authorship Declaration. The thesis-level addition is the common label-recovery formulation, the scenario map connecting the studies, the shared background, and the synthesis of their assumptions and limitations in Chapter 7.

### C

The four studies address different parts of the same expressive-label problem. The technical methods are attributed to their associated co-authored papers, while the thesis develops the connections between them: which musical structure is trusted, which dynamics representation is recovered, and what supervision and evaluation support the resulting claim. This synthesis is developed in Chapters 1, 2, and 7 and in the positioning sections of the technical chapters. It should be read as the thesis contribution alongside, rather than as a replacement for, the individual method contributions.

**写作推荐**：B。B补入原文遗漏的Ch.6并给读者明确mapping，所称thesisaddition都能从独立论文与当前chapter结构核实，不把已有paper的proxy诊断说成thesis新增。A最短，C更流畅但不如B可查。

**边界／待核验**：V-07：上传ICASSP PDF含PENDING／placeholder，不能凭该版本确定哪些Ch.5结果是最终发表内容或thesis新增；如学校要求逐项新增实验清单，先核对最终papers。ISMIR status用R1-02更新为accepted，其他published/accepted日期不凭metadata推断。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r2-03"></a>

## R2-03 把 beyond-piano 可迁移与未验证部分写具体

**拟执行位置／操作**：替换 Ch.7 §7.3 的 piano-centric 段；Ch.6 保留已有 attack-driven 限制，不重复加新段。

**准确原文与当前源码位置**

`Chapter_7/Conclusion.tex` line 113（当前来源 hash 见 SOURCES.md）

```latex
Second, the strongest direct supervision in the thesis remains piano-centric. This reflects the state of available velocity-labelled datasets rather than a belief that piano dynamics is the universal template for all instruments. Chapter~\ref{ch:beyondpiano} addresses this bias by moving into a label-scarce guitar setting, but the broader point remains: once the target instrument lacks direct performance-control labels, the interpretation of recovered velocity must be stated operationally.
```

`Chapter_6/chap6.tex` line 519（当前来源 hash 见 SOURCES.md）

```latex
Second, the experiments focus on piano and guitar. Both instruments are predominantly percussive in their attack profile, which favours the OSF parameter. Sustained-bow instruments such as violin, or breath-driven instruments such as flute, would require acoustic parameters that capture sustain and continuous-modulation cues beyond the PHE/OSF pair used here. The claim is therefore tied to the tested attack-driven setting.
```

**英文候选**

### A

The strongest direct supervision remains piano-based. The guitar study supports the use of a renderer-conditioned onset-velocity coordinate in the tested guitar corpora, evaluated through rendered loudness rather than captured guitar velocity. It does not validate the same estimator or parameter set for voice, bowed strings, or wind instruments.

### B

The piano chapters support conclusions about the tested piano datasets and targets. Chapter 6 extends the supervision strategy to guitar, where the evidence concerns renderer-conditioned velocities and loudness agreement rather than recovery of captured physical velocity labels. Voice, bowed strings, and wind instruments were not evaluated. Their sustained dynamics and continuous controls would require suitable target coordinates and descriptors beyond the attack-focused PHE/OSF pair used here.

### C

What can transfer beyond piano is the recovery framework: specify the trusted notes, choose an editable dynamics coordinate, and match the supervision to that coordinate. The empirical evidence is narrower. It covers piano and the tested guitar adaptation, not a validated instrument-general estimator. For voice, bowed strings, and wind instruments, onset intensity alone cannot describe the sustained and continuously shaped aspects of dynamics, so the target and comparison features would need to be reconsidered.

**写作推荐**：B。B直接点名examiner列的四类并区分principletransfer与performancevalidated。A最短，C很好衔接中心论点但对新乐器的目标设计论述略多。没有把guitar r当canonicalvelocityaccuracy。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r2-04"></a>

## R2-04 11位听者与8段刺激是补充证据，避免 definitive validation

**拟执行位置／操作**：在 Ch.3 Perceptual Evaluation 结果段末加限制；并按下方全局同步清单收窄overview/abstract/summary文字。

**准确原文与当前源码位置**

`Chapter_3/chap3.tex` line 371（当前来源 hash 见 SOURCES.md）

```latex
\paragraph{Participants.}
We recruited 11 expert listeners aged 18 or above, selected for substantial musical background and experience with critical listening studies.
Participants completed the survey anonymously through the Qualtrics platform \cite{qualtrics}.
```

`Chapter_3/chap3.tex` line 457（当前来源 hash 见 SOURCES.md）

```latex
The evaluation design is therefore deliberately broader than a single regression score. Objective error metrics quantify note-wise accuracy, \(SD_{\mathrm{velo}}\) checks whether the predicted velocity distribution retains expressive spread, and the listening test verifies that the recovered layer changes perceived musical quality. This combination is important because a velocity-completion model can be numerically close to the target while still sounding too flat, or can sound more expressive while producing larger point-wise deviations.
```

`main.tex` line 123（当前来源 hash 见 SOURCES.md）

```latex
%\maketitle
	\frontmatter
%	\linenumbers
	\clearpage
	\thispagestyle{empty}
	\phantom{a}
	\vfill
	\vfill
    
	\include{Declaration/declaration}
    
    
	\begin{abstract}
	Automatic music transcription has matured in its treatment of note pitch and timing, but musical dynamics remains less fully addressed. This thesis treats dynamics as a missing expressive label layer that can be recovered from music data already partly specified, without rewriting note content or note timing. Its unifying question is \emph{how musically interpretable dynamics labels can be recovered from incomplete, weakly expressive, or weakly supervised music data}. Two complementary targets within expressive music performance recur throughout: note-level MIDI velocity, the per-onset control variable used in MIDI workflows, and score-level dynamics, the beat-aligned markings such as \textit{p}, \textit{mf}, and \textit{f} written in notation.
		
	The thesis first addresses the symbolic-only setting by reformulating MIDI velocity completion as image colourisation on sparse piano-roll matrices. A U-Net with window attention and a sparsity-aware loss recovers the missing velocity layer, and the results are validated through cross-dataset objective metrics and a MUSHRA-inspired listening test.
		
	It then turns to score-informed velocity estimation in the audio-plus-score setting, using a Transformer correction module that refines AMT-estimated velocity at aligned score onsets. Rather than replacing the AMT backbone, the module uses score structure as a late correction prior, transfers across the HPT, HPPNet, and DynEst backbones, improves cross-dataset behaviour from MAESTRO to SMD, and remains stable under audio--score timing shifts of up to several seconds.
		
	A further study treats the audio-only setting with a score-facing output. It jointly estimates beat-synchronous dynamic markings, change points, beats, and downbeats from performance audio. A Bark-scale specific loudness front-end, a multi-scale encoder, and an MMoE decoder are combined to address the conflicting temporal requirements of dynamic-level estimation, change-point detection, and metrical localisation, producing output that can be written back into a score.
		
	Finally, the thesis reports an exploratory extension beyond piano. To recover note-level velocity for instruments without direct labels, it treats the problem as renderer-conditioned analysis-by-synthesis and compares two differentiable synthesis interfaces. The proposed differentiable SoundFont proxy supervises velocity through note-wise loudness-related descriptors rather than waveforms. On guitar, this proxy interface adapts a piano-pretrained estimator more reliably than a differentiable waveform synthesiser under recording mismatch.
		
	Taken together, these studies form a scenario map rather than an end-to-end pipeline. They show that dynamics recovery becomes tractable when the output layer, temporal coordinate, evidence source, and supervision regime are matched to one another. The thesis therefore extends expressive AMT beyond note detection by making existing music data more expressive, editable, and usable in settings where direct dynamics labels are partial or absent.
		
	\textbf{Keywords}: automatic music transcription; expressive music performance; MIDI velocity; dynamic markings; score-informed velocity estimation; differentiable SoundFont proxy.
	\end{abstract}
	
	\include{Acknowledgments/acknowledgements}
	
    \include{Declaration/author_declaration}
    
	\setcounter{tocdepth}{2}
	\tableofcontents
	\listoffigures
	\listoftables
	\include{Abbreviations/abbreviation}
```

**英文候选**

### A

The listening test provides complementary evidence for the objective results. With 11 expert listeners and eight selected excerpts, it supports the perceived benefit of velocity completion in this setting rather than definitive perceptual validation across listeners and repertoire.

### B

The listening evidence is limited to 11 expert listeners, eight selected excerpts, and one rendering configuration. It supports the objective comparison within that setting, but does not establish perceptual validity across the wider repertoire, listener population, or synthesis systems. The composer-group scores are descriptive and should be read with the same limitation.

### C

The improvement over the selected baselines is supported by both note-wise metrics and this small reference-based listening study. The perceptual result is evidence that the velocity layer matters for the tested stimuli, not a population-wide estimate of musical naturalness. Broader listener and repertoire coverage would be needed before making that stronger claim.

**写作推荐**：B。B覆盖人数、刺激与renderer三条现存限制，不新增实验。A最小，C叙述好但“matters”略抽象。保留作者结果价值，不把modest改写成无效。quantisation不在此抢先定论。

**边界／待核验**：V-02quantisation待查；不得把confidencenarrow本身当generalisation证明。

**关联意见**：R1-16; R1-21。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**全文同步提案**（原文件均未改）

- `main.tex`
  - 原：the results are validated through cross-dataset objective metrics and a MUSHRA-inspired listening test.
  - 拟：the results are assessed through cross-dataset objective metrics and a small MUSHRA-inspired listening test.

- `Chapter_3/chap3.tex`
  - 原：the listening test verifies that the recovered layer changes perceived musical quality.
  - 拟：the listening test provides complementary evidence of perceived improvement for the selected stimuli.

- `Chapter_1/Intro.tex`
  - 原：it demonstrates that recovering a decoupled expressive layer on fixed symbolic notes is enough to transform a mechanical MIDI sequence into an expressive performance.
  - 拟：it examines how completing velocity on fixed symbolic notes can improve expressive rendering, using objective evaluation and a small listening study.

- `Chapter_7/Conclusion.tex`
  - 原：yet the listening test shows a clear improvement over flat and sequence-oriented baselines.
  - 拟：and the small listening study supports an improvement over Flat and ConvAE on the selected excerpts.

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

<a id="r2-05"></a>

## R2-05 只列实际见到的语言／格式问题

**拟执行位置／操作**：只提出可核验的小修正，不批量换同义词。以下为 replacement 清单，原文及位置见本节引文。

**准确原文与当前源码位置**

`Chapter_1/Intro.tex` line 50（当前来源 hash 见 SOURCES.md）

```latex
Expressive AMT extends beyond note transcription to capture the full aspects of a human performance. A comprehensive expressive transcription can be conceptually divided into three layers \cite{cancinoChacon2018computational}:
\begin{itemize}
\item \textbf{Timing Layer:} Captures the temporal elasticity of a performance, including macro-level tempo variation, beat-level timing, inter-onset intervals (IOIs), and micro-level articulation.
\item \textbf{Dynamic Layer:} Represents the intensity and energy of the music performance, bridging physical machine measurements (e.g., MIDI velocity) with semantic cognitive notations (e.g., score dynamic markings).
\item \textbf{Control Layer:} Includes instrument-specific techniques and acoustic modifiers, such as sustain pedalling, vibrato, reverberation, and amplifier configurations.
\end{itemize}
While all three layers are essential for the computational understanding of expressiveness in performance, this thesis singles out the \textbf{Dynamic Layer} as its primary focus. This choice does not diminish the importance of timing or control parameters. Rather, dynamics is chosen to move AMT beyond notes for three reasons:
```

`Chapter_5/chap5.tex` line 319（当前来源 hash 见 SOURCES.md）

```latex
The component ablations show that all major parts of the model contribute to the final performance, but not in the same way. The most diagnostic result is the removal of temporal scaling. Setting $s=1$ reduces the average F1 from 55.0 to 46.5, with particularly large drops in change-point F1 and downbeat F1. This indicates that the performance gain does not merely come from using a deeper convolutional encoder, but from exposing the downstream tasks to genuinely different temporal resolutions. Removing MMoE also degrades all four tasks, supporting the view that the four heads have different preference on the same shared latent. The overlap-based data augmentation gives a further improvement, which is expected for this dataset because change points and downbeats are sparse events. Overlapping audio segments increase the chance that such events appear in varied local contexts during training.
```

`Chapter_5/chap5.tex` line 321（当前来源 hash 见 SOURCES.md）

```latex
The temporal-scaling results give a detailed view of the multi-scale encoder. The reference architecture of \cite{li2023frame} uses a scaling factor of 3, but this value is not optimal for our tasks combination. With $s=3$, beat F1 and change-point F1 remain strong, but the average score is lower than the full model. Increasing the factor to $s=5$ gives the best overall balance. A slightly larger value, $s=7$, remains competitive and gives the second-best average score, but further increasing the factor to $s=9$ causes a clear degradation, especially for downbeats. This pattern suggests that the model needs a sufficiently coarse branch to capture long-range dynamic context, but excessive temporal compression begins to remove information that cannot be fully recovered for event localisation. The best value is therefore not simply the largest receptive field, but the best compromise between contextual abstraction and temporal precision.
```

`Chapter_3/chap3.tex` line 358（当前来源 hash 见 SOURCES.md）

```latex
\textbf{MIDI segment duration.} The analysis shows that reducing it from 20 to 10 seconds improves performance, while further reduction to 5 seconds slightly worsens the accuracy metrics. This is likely because a 10-second segment roughly encompasses four measures at 120 beats per minute (BPM), forming a complete musical phrase that aids in semantic segmentation.
```

**英文候选**

### A

“capture the full aspects of a human performance” → “capture several aspects of a human performance”

“the four heads have different preference on the same shared latent” → “the four heads have different preferences for the shared representation”

“not optimal for our tasks combination” → “not optimal for this combination of tasks”

“a 10-second segment roughly encompasses four measures at 120 beats per minute (BPM)” → “a 10-second segment can span several bars, depending on tempo and metre”

**写作推荐**：A。前三处是实际措辞／语法问题，最后一处是可核验时间解释。Figure2.3标题与其他排版问题须先看现存PDF页面再定，不能把PDF抽取换行自动当LaTeX缺陷。

**边界／待核验**：与R1-20同一10s解释只改一次。更大的事实／协议疑点列在V-01至V-07，不能当proofreading静默修掉。

**关联意见**：R1-04; R1-20。只执行一份共享文字，COMMENT_MAP 不丢原意见。

**决定／路线**：仅引用统一决策清单的同编号，不在本文件填写。　**执行**：【未执行】　**复审**：【独立审查待进行】

## 待核验边界与独立审查重点

| 编号 | 已核实的材料冲突／边界 | 需要什么才能定稿 | 现在可以做什么 |
| --- | --- | --- | --- |
| V-01 | 两份thesis PDF 154/155物理页，正文与背景表述有差异；README未指定基线 | 作者指定正式送审／修订基线；最终compile核验 | 当前LaTeX行号写候选，PDF身份分开，不静默选择旧页码 |
| V-02 | 作者批注说听测使用quantised score-MIDI；正文只描述SMD原MIDI去velocity | 已有8个刺激、reference及生成步骤，或作者具体确认 | R1-21保留两种证据，不写肯定的未量化／已量化协议 |
| V-03 | Ch.3正文F input，配置onset_mask=True；loss onsetmask后CosSim轴／归一化与正文公式可能不同；正文把1×1称global | 论文实际run的config/checkpoint与代码版本映射 | 解释image-like表示；不把defaultconfig当论文run；1×1空间窗口不是global，标签待作者核定 |
| V-04 | Ch.2说frozen frontend，Ch.4说jointlytrained；固定代码有多trainingmode。loss theta=.5，paper与thesis写sum | 最终训练mode、adapter/velocitybranch更新范围、损失验证记录；SMD10%用于何种选择 | R1-23限定architecture/interface；R1-25保留1:1相对权重和已有preliminary验证，不声称equalgradient或完整ratio最优 |
| V-05 | Ch.5正文macro-F1，固定evaluator weighted；当前Table5.4与保存输出来源／fold规则需对齐；正文targetdynamic-best与各任务max存在旧核对疑点 | 最终evaluator版本、每行checkpoint来源、原已有逐录音预测或作者确认 | 不改表值、不从aggregatedweighted分数反推macro；把外部target-selectedbestfold标成诊断，不能声称unbiaseddeployment |
| V-06 | Fig6.3自称guitar ground-truthvelocities，与realGAPS/FL无velocitylabels并列；图没有可识别snippet provenance | 该片段和作图来源，确定syntheticcontrol、measured或其他reference | 不凭图色猜来源，不默认删图、不替作者选解释；对应caption与论证暂不定稿 |
| V-07 | ICASSP提供稿p4有PENDING THIS PART，p5有replacement table说明；标题与declaration有差异 | 最终发表版本或作者说明本稿用途 | 不自动把它认作cleanfinal，不声称Ch.5新增内容已完全逐项映射 |

本轮不改bibliography、results、figure原资产或研究代码。无新实验、无模型训练、无submission、无Gitcommit/push。GRS报告由第三编辑在独立审查后汇总，本文件不把候选写成已经完成。
