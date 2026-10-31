**资料页：** 当前简短入口统一为[START_HERE](START_HERE.md)。本页保留八处完整片段；新增[三项前言补充与R1-35 KEEP](SUPPLEMENTS_v4.md)单独选择，原冻结文字不覆盖、不自动扩大YES。

# 第三轮拟采用片段预览

**全部仍是提案，未执行。最终定点核验通过：39项文字可供作者选择，4项事实待核。** 下面8处中，R1-21只有应用段文字可选，其听测协议仍待记录；其余7处文字已可供选择。作者只在 [DECISIONS.md](DECISIONS.md) 决定，旧版批准未自动转入第三轮。

先看这张表；需要复制或比较时，再看下面的原句、操作范围和实际英文。全部43项的第三轮候选仍在 [writer_round3.md](writer_round3.md)。

| 意见／拟路线 | 这次具体改善 | 实际英文节选，未执行 |
| --- | --- | --- |
| [R1-05 B](#r1-05) | 给中心问题中的术语补定义，并说明信息条件可重叠 | In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. |
| [R1-15 A](#r1-15) | 只取消难度排序，保留作者原首段的提问与句式 | This chapter addresses Scenario S1, where only symbolic information is available. |
| [R1-17 B](#r1-17) | 把 colourisation 准确解释为缺失 scalar layer 的类比 | The output is a single-channel velocity roll. |
| [R1-21 A](#r1-21) | 把 composition 用途与训练来源说清，不替听测协议定案 | The composition use case is to add a velocity profile while retaining the notes and timing supplied by the user. |
| [R1-25 B](#r1-25) | 回答实际相对权重，保留 preliminary comparison | Equal coefficients do not imply equal numerical loss or gradient magnitudes. |
| [R1-32 A](#r1-32) | 澄清符号与 adaptation，同时保留复现所需参数 | The architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen. |
| [R2-02 B](#r2-02) | 补全四研究映射，说明 thesis 如何综合 | The thesis brings these studies together through a common label-recovery formulation and scenario map, provides shared background, and synthesises their assumptions and limitations in Chapter 7. |
| [R2-04 A](#r2-04) | 保留实际系统排序，把听测说回 reference similarity | The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. |

## 拟保留的内容

- R1-01：数字制引用是可保留的方案，仍待作者选择；不是默认拒绝 examiner，也不自动切换 author-year。
- R2-01：保留已有 chapter overviews，只随 R1-06／15 局部澄清，不新增四段同义导语。
- R1-18：与 R1-17 共用一段，不重复插入。R1-27／37 当前拟组合为 Ch5 A＋Ch7 的 R1-27C，不再另插第三段；完整组合仍文字可供选择；仍未批准／执行。

V01–V07 均保持待核验。这里的干净英文不表示听测 timing、最终 run、F1/fold、吉他图 GT 或最终 ICASSP 版本已经查清；正式基线与页码也未定。

## R1-05

**定义 weakly expressive 与 weakly supervised；拟路线 B，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r1-05)。

**原文上下文：** [Chapter_1/Intro.tex:114](../Chapter_1/Intro.tex)。

```latex
The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}
```

**拟操作：** 在中心问题后、场景介绍前插入下段。问题句保留；Intro 的总排序句另随 R1-15 同步，不把原有 tightly constrained→ambiguous 视为已保留。

**拟采用英文，未执行：**

```latex
In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. Weakly supervised settings lack reliable target labels for direct training; Chapter 6 instead uses real audio and a renderer-based comparison to supervise the velocity estimator indirectly. These terms describe the available information rather than the quality of the musical performance. These conditions can overlap in the same dataset.
```

## R1-15

**用信息条件描述 S1，不用单一难度排序；拟路线 A，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r1-15)。

**原文上下文：** [Chapter_3/chap3.tex:13](../Chapter_3/chap3.tex)。

```latex
This chapter addresses Scenario~S1, the most controlled setting in the thesis map. Here the symbolic notes and their timing are already known, but the note-level velocity is missing, flattened, or musically uninformative. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?
```

**拟操作：** 替换 Ch.3 §3.1 首段整体。下方拟选稿已完整拼接，后面的应用段保持原样；同步位置仍按各自准确原句局部替换。

**拟采用英文，未执行：**

```latex
This chapter addresses Scenario S1, where only symbolic information is available. Here the symbolic notes and their timing are already known, but the note-level velocity is missing, flattened, or musically uninformative. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?
```

**联动的 Intro 排序句：**

```latex
These settings form the core empirical arc of the thesis by varying both the available evidence and the target representation.
```

它替换原来的 “By intentionally ordering these environments from the tightly constrained to the ambiguous...” 句，其他同步点见第三轮 R1-15。后面的应用段保持，不重复叠加输入定义。

## R1-17

**image-like 的含义与 piano-roll 选择一起解释；拟路线 B，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r1-17)。

**原文上下文：** [Chapter_3/chap3.tex:26](../Chapter_3/chap3.tex)。

```latex
This motivates the image-based view adopted in the present chapter. By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly. U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic and does not rely on acoustic input \cite{he2025filling,kim2024method}. This makes the chapter a natural starting point for the broader thesis.
```

**拟操作：** 只替换 §3.2 的这一方法动机段。line 43 的相关论述与正式 paper／chapter 题名保留；R1-18 共用下段。12处术语出现点的保留／替换表见第三轮全文，不全篇机械改词。

**拟采用英文，未执行：**

```latex
A piano roll places simultaneous notes along the pitch axis and their local evolution along time, giving the U-Net a regular two-dimensional input. Convolution and skip connections can then use local pitch–time neighbourhoods while preserving the given note structure. The output is a single-channel velocity roll. We use colourisation as an analogy for completing that missing scalar layer, rather than for predicting RGB colour. This representation motivates the U-Net and attention design used here \cite{he2025filling,kim2024method}.
```

## R1-21

**量化 MIDI 听测保留作者说明，待刺激记录对齐；拟路线 A。应用段文字可选，完整项目事实待核；未批准／执行。** [完整候选与其他路线](writer_round3.md#r1-21)。

**原文上下文：** [Chapter_3/chap3.tex:453](../Chapter_3/chap3.tex)。

```latex
This chapter has verified that note-level dynamics can be recovered usefully even when the symbolic notes and timing are held fixed. It turns expressive enhancement into a controllable post-processing stage rather than a full performance-rendering problem, which is exactly the setting encountered in many MIDI-production and corpus-curation workflows.
```

**拟操作：** 在 Ch.3 Discussion 的首段后插入一段应用说明，原 Stimuli 协议暂不替换。下方拟选稿只写已知训练来源与接口用途；量化预处理字段放在候选之外。

**拟采用英文，未执行：**

```latex
Performance MIDI supplies captured velocity targets for training, while the completion interface can also accept quantised symbolic input. The composition use case is to add a velocity profile while retaining the notes and timing supplied by the user.
```

**仍待核验 V-02：** 作者已说明听测用了量化 score-MIDI；原 Stimuli 段暂不替换，input 与 reference 的具体 timing preparation 待既有记录确认。此处拟稿只是应用说明，不关闭该问题。

## R1-25

**明确 hybrid loss 的相对权重与证据边界；拟路线 B，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r1-25)。

**原文上下文：** [Chapter_4/chap4.tex:133](../Chapter_4/chap4.tex)。

```latex
Here $\mathbf{V}$ is the ground-truth velocity target and $\hat{\mathbf{V}}$ is the predicted velocity output of either the baseline AMT branch or the score-informed system. This hybrid supervision is useful because it constrains both the local onset value and the broader note sustain region, while still keeping note-level precision central to the objective.
```

**拟操作：** 保留原 loss 引言、公式、两个 denominator 和变量定义；下方只展示完整 B 中拟替换的解释句，不重复插入公式。完整拼接稿见上方链接。

**拟采用英文，未执行：**

```latex
The frame-wise BCE and onset-wise L1 terms are averaged over their respective active positions and combined with equal relative coefficients. We retain the hybrid objective of Kim et al. (2024), supported by the preliminary comparison with frame-only and onset-only supervision reported in our associated SMC paper. Equal coefficients do not imply equal numerical loss or gradient magnitudes.
```

**仍待核验 V-04：** SMC preliminary hybrid comparison 的记录保留；实际 theta、训练分支与验证范围不因文字清楚就视为已全部对齐。

## R1-32

**V^(0) 是粗估 roll，Vhat 是 correction 后的逐音值；拟路线 A，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r1-32)。

**原文上下文：** [Chapter_6/chap6.tex:93](../Chapter_6/chap6.tex)。

```latex
The estimator has two stages. The acoustic module, borrowed from the High-Resolution Piano Transcription system~\cite{kong2021hpt}, takes log-Mel spectrograms computed at $100$\,fps from $22050$\,Hz mono audio (FFT size $2048$, hop $221$\,samples, Hann window) as input and predicts a coarse velocity roll $V^{(0)}$. A score-informed Transformer then refines $V^{(0)}$ into $\hat{V}$ using aligned note information. The detailed architecture and supervised training procedure are given in Chapter~\ref{ch:scoreinf}; the present chapter treats this estimator as a fixed black-box front-end whose checkpoint is then adapted.
```

**拟操作：** 将 §6.4.1 两个原段替换为下列两段完整拼接稿：只澄清fixed架构和V^(0)/Vhat含义，保留原全部前端采样率、fps、FFT、hop、Hann、checkpoint来源和Chapter4架构引用。

**拟采用英文，未执行：**

```latex
VeloEst acts as the shared front-end of the framework, estimating note-wise MIDI velocities $\hat{V}$ from the performance audio and aligned note events. We use the score-informed HPT model with onset and frame as score-guidance, which is identified as the best VeloEst configuration in Chapter~\ref{ch:scoreinf}~\cite{he2026score}. We keep its architecture unchanged and use the publicly available checkpoint trained on MAESTRO with ground-truth velocity supervision $\mathcal{L}_{\mathrm{velo}}$. Using this estimator keeps the cross-instrument experiment focused on the supervision interface rather than on introducing a new velocity-estimation architecture.

The estimator has two stages. The acoustic module, borrowed from the High-Resolution Piano Transcription system~\cite{kong2021hpt}, takes log-Mel spectrograms computed at $100$\,fps from $22050$\,Hz mono audio (FFT size $2048$, hop $221$\,samples, Hann window) as input and predicts a coarse velocity roll $V^{(0)}$. A score-informed Transformer then refines $V^{(0)}$ into $\hat{V}$ using aligned note information. Here, $V^{(0)}$ denotes the intermediate acoustic estimate, while $\hat{V}$ denotes the corrected onset values passed to the rendering interface; the superscript does not identify a pre-adaptation checkpoint. The detailed architecture and supervised training procedure are given in Chapter~\ref{ch:scoreinf}. The architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen.
```

**必须保留：** 100 fps、22050 Hz、FFT 2048、hop 221、Hann、checkpoint 来源和 Ch4 引用都在上述完整两段中；不能只粘末尾澄清而删除前文配置。

## R2-02

**四篇论文的技术贡献与 thesis 新增综合分开；拟路线 B，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r2-02)。

**原文上下文：** [Chapter_1/Intro.tex:177](../Chapter_1/Intro.tex)。

```latex
Referring to Figure~\ref{fig:intro_overview}, the core methodological chapters (Chapters 3--5) preserve the technical contributions of their respective peer-reviewed publications, adapted to form a unified narrative.
```

**拟操作：** 替换 §1.8 首段整体；下方拟选稿为完整段落，下一原段Chapter2组织说明保持。四篇mapping与authorship reference保留，新增综合描述不声称独占或穷尽novelty。

**拟采用英文，未执行：**

```latex
The technical chapters are based on four co-authored studies: symbolic velocity completion (CMMR 2025, Chapter 3), score-informed correction (SMC 2026, Chapter 4), joint dynamics and metrical estimation (ICASSP 2026, Chapter 5), and cross-instrument proxy supervision (ISMIR 2026, Chapter 6). Their authorship and publication details are listed in the Authorship Declaration. The thesis brings these studies together through a common label-recovery formulation and scenario map, provides shared background, and synthesises their assumptions and limitations in Chapter 7.
```

**仍待核验 V-07：** 这里说明四研究与组织性综合，不证明思想只在 thesis 首次出现，也不穷尽逐结果 novelty。所给 ICASSP 稿含未完成标记，最终发表基线仍待确认。

## R2-04

**11位听者与8段刺激是补充证据，避免 definitive validation；拟路线 A，文字可供选择；仍未批准／执行。** [完整候选与其他路线](writer_round3.md#r2-04)。

**原文上下文：** [Chapter_3/chap3.tex:444](../Chapter_3/chap3.tex)。

```latex
\paragraph{Results.}
Although a substantial gap to human performance remains, the proposed U-Net clearly outperforms the other systems.
The Flat model performs worst, consistent with earlier findings that default velocity is musically inadequate \cite{kuo2021velocity}.
The seen, less-seen, and unseen repertoire groups are best interpreted as descriptive groups rather than as a strict complexity-controlled comparison.
Even so, the relatively narrow 95\% confidence intervals across groups suggest that participants rated the stimuli with reasonable consistency.
```

**拟操作：** 替换 Ch.3 Perceptual Evaluation 的Results段整体，保留MOS表、CI、participants/stimuli/calibration/procedure；不改成仅陈述研究意图。把样本/renderer与composer分组范围集中在此，R1-16不再重复限制。

**拟采用英文，未执行：**

```latex
U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.
```

**评分目标的原文依据：** `Chapter_3/chap3.tex:414–415`。

```latex
In each trial, the audio rendered from the human-performed MIDI served as the fixed reference, and the rendered system outputs were judged relative to that reference.
Following a MUSHRA-inspired reference-based procedure \cite{series2014mursha}, participants rated each processed stimulus independently on a continuous 0--5 scale, where the labelled intervals corresponded to ``bad'', ``poor'', ``fair'', ``good'', and ``excellent'' similarity.
```

MOS／CI 表、participants／stimuli／calibration／procedure 保留。摘要与 Discussion、Intro、Conclusion 的四处精确同步见第三轮；V-02 timing 不在 Results 中猜填。

## 版本与决定

本预览绑定 [第三轮来源身份](editor_crosswalk.md#第三轮来源身份)。所选片段若返修，旧批准不自动授权新文字。正式实施仍需作者决定和对应事实核验；最终页码【待核验】。
