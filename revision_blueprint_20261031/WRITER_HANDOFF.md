# 写作窗第一轮交接

第一轮候选已可进入独立审查；没有完成候选复审，不宣称最终通过。

- 全覆盖：R1 38项＋R2 5项；与reviewer_baseline编号一一相同，见ID_CROSSWALK.md。
- 27个实质项提供A/B/C完整英文候选，共81个最终路线候选；另有162个可读短稿和具体淘汰／合并理由。其余16项为单一纠错、共享段落或保留原文，不凑版本。
- writer_round1.md 是主要送审稿，包含75处准确源码原段与行号、操作范围、每稿取舍、推荐、依赖与全文同步提案。writer_working.md 是工作比较，不给用户作主要阅读入口。
- SOURCES.md／COMMENT_MAP.md／PAPER_RENAME_MAP.md／evidence内source_sha256.json提供来源、25条作者原回复、版本边界和重命名证据。全部128份记录的来源hash未变；唯一源目录操作是4篇paper重命名，字节逐个一致。
- 只用phdthesis及publish_paper；没有读取otherfiles。没有thesis/response/bibliography/figure源码修改、编译、训练、实验、commit、push或submission。
- 作者决定应由第三编辑在唯一清单维护；本文件和writer_round1不另设YES/NO填写入口。所有执行状态仍为未执行，最终页码待核验。

## 独立审查先看什么

1. R1-25 的hybrid objective：上传SMC §3.3确有preliminaryhybrid对single-target验证说明，不能把作者“我验证过”写成从未验证；但无ratio最优结论。代码theta=.5与文稿sum的相对1:1相同，整体尺度需与run说明对齐。
2. R1-29：固定beat_postproc.py在有beat时确实snapdownbeat并deduplicate；作者decoder连接说明有直接实现支持。候选仍要求最终evaluationrun调用路径对齐。
3. R1-30新增英文target-selectedfolddisclosure，精确区分no fine-tuning与targetlabels参与selection；不改表，不新增实验。实际表来源／weighted-vs-macro仍是V-05，不能把两件事混成已全部解决。
4. R1-21：不采用“听测以performance MIDI为主”的肯定句；作者说量化，正文只交代SMD来源，预处理未清楚。两边都不能替作者定稿。需要既有刺激记录，不要求新实验。
5. R2-02：上传ICASSP物理p4/p5含PENDING、no yet、replacementtable说明，已渲染核验；不能把它当cleanfinal来认定thesis新增了哪些结果。
6. R1-33给出了跨段的弱因果措辞同步提案，避免正文另处继续说mismatch已获因果证明。R2-04同步收窄abstract、Intro、Discussion、Conclusion的perceptualvalidation措辞。
7. 现存main.pdf Fig2.3（physical52/printed25）白底显示正常，PNG透明黑区不是排版缺陷。颜色语义仍未知，R1-10建议提案副本统一色，不猜原来含义。

## 可直接判断的实际候选示例

### R1-25 明确 hybrid loss 的相对权重与证据边界

原文片段（`Chapter_4/chap4.tex` line133）

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

推荐 B

The frame-wise BCE and onset-wise L1 terms are normalised by their respective active positions and combined with equal relative coefficients. We follow the hybrid objective of Kim et al. (2024); our preliminary comparison also favoured hybrid supervision over frame-only or onset-only alternatives, as reported in the associated SMC paper. This supports the retained formulation, but does not establish that equal weighting is optimal for every backbone or dataset.

### R1-29 共享表征、分头 loss 与 decoding 连接同时说明

原文片段（`Chapter_5/chap5.tex` line79）

```latex
The shared encoder provides a common latent representation, but the tasks remain acoustically diverse. To reduce negative transfer, we use a Multi-gate Mixture-of-Experts (MMoE) layer \cite{ma2018mmoe} as a task-aware decoder.
```

推荐 B

The beat and downbeat tasks are coupled through shared representation learning and through decoding, rather than by a direct connection between their output heads. Each head has its own shift-tolerant loss. In post-processing, downbeats are moved to the nearest predicted beat when a beat sequence is available, with duplicate events removed. This enforces the event-level relation at decoding time without adding a learned cross-head constraint.

### R1-33 DDSP fidelity 是限制，退化不等于因果证明

原文片段（`Chapter_6/chap6.tex` line111）

```latex
The advantage of this interface is that it exposes the front end to rich waveform gradients. The risk, already noted in Section~\ref{sec:bp:related}, is that any timbral or recording mismatch between $\tilde{a}$ and $a$ also enters the gradient. When the synthesiser is not a faithful match for the target recordings, the gradient can become dominated by nuisance compensation rather than by velocity correction.
```

推荐 B

The waveform back-ends are used as differentiable approximations rather than exact reproductions of the recorded instruments. Their usefulness depends both on acoustic fidelity and on whether changing velocity produces the appropriate change in sound. The Diff-Synth results are consistent with a mismatch in this interface, but do not isolate its cause: reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.

### R2-04 11位听者与8段刺激是补充证据，避免 definitive validation

原文片段（`Chapter_3/chap3.tex` line371）

```latex
\paragraph{Participants.}
We recruited 11 expert listeners aged 18 or above, selected for substantial musical background and experience with critical listening studies.
Participants completed the survey anonymously through the Qualtrics platform \cite{qualtrics}.
```

推荐 B

The listening evidence is limited to 11 expert listeners, eight selected excerpts, and one rendering configuration. It supports the objective comparison within that setting, but does not establish perceptual validity across the wider repertoire, listener population, or synthesis systems. The composer-group scores are descriptive and should be read with the same limitation.

## 尚未解决的具体边界

- Pending：正式baseline（两个PDF154/155页，LaTeX工作坐标不等于作者正式选择）、听测量化预处理、Ch3 run/input/loss/window含义、Ch4 run训练范围与SMD开发用途／onsetonly维度、Ch5 evaluator与fold汇总来源、Fig6.3吉他GT身份、ICASSP最终版本。
- Pending：图1.1／2.1／2.3／5.2／6.2仍为图内label与caption提案，未在原资产实施；若需要候选视觉稿，应只在提案目录建副本。
- Unknown：执行环境没有暴露实际model/effort，因此不能声称已验证Ultra或跨模型。
- Failed（无写入）：尝试用Codex跨聊天消息工具向父线程01a17638-4f05-718f-b12b-37e6189870e0发送早期inventory，返回thread not found；未重试。此次final会由平台自动通知父任务；所有有用结果已经写入共享目录。

下一步：父任务把实际writer_round1.md交给独立审查者逐句批评，再把具体critique发回写作窗返修。本轮没有代第三编辑创建最终concise表或GRSreport，也不把尚未发生的修改写成We have revised。
