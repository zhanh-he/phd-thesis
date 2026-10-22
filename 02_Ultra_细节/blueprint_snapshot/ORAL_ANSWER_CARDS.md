# 答辩英文回应卡 / Spoken answer cards

这是基于手稿的回应草案，不代表已验证训练代码、原始数据或额外实验。每卡先读30秒core；被追问时使用1–2分钟expansion。不要把planned revision说成已完成。所有页码以v0为主；原论文链接见START_HERE。

## A01 — 一条主线、四种条件与论文新增贡献

关联：R1-06、07；R2-01、02。中文要点：统一的是“可信结构下补足dynamics标签”，不是四章串成一个端到端系统。先说问题，再说四章各自条件；文章方法与thesis综合分开。

**30-second core**

“My central question is how to recover a useful dynamics layer when some musical structure is already available. The four studies address different evidence conditions: symbolic notes, audio with an aligned score, audio alone for score dynamics, and aligned notes without target velocity labels. They form a scenario map. The thesis-level contribution is the common formulation and the comparison of what each setting allows us to claim.”

**1–2-minute expansion**

“Chapter 3 holds the note sequence fixed and estimates missing velocity from symbolic context. Chapter 4 adds acoustic evidence and uses the score to correct velocity at known onsets. Chapter 5 changes the output to beat-synchronous score markings and estimates the metrical coordinate as well. Chapter 6 returns to note-level velocity, but replaces direct target labels with a renderer-based supervision interface. These are related questions with different targets and assumptions.

The authorship declaration identifies the associated papers, while Sections 1.7 and 1.8 describe the common thesis framing. I agree that the distinction between an existing paper contribution and a new thesis synthesis should be easier to inspect. I will add a provenance table and a short closing statement in each technical chapter, identifying its data condition, output, evidence and limitation. I will check the original paper versions before labelling any experiment as a new thesis addition.”

**实际证据**：Abstract PDF4；§1.5–8 印刷pp6–8/PDF33–35；Authorship Declaration v/PDF8（四篇、均声明80%）；Table7.1 p106/PDF133。已有各章定位段，不宜说完全没有统一叙事。

**让步/边界**：四章不是完整AMT系统；Ch6仍需要aligned notes；不能说“首次”或“新实验”而没有版本对照。

**具体修订**：给Table1.2增加Ch6扩展行；§1.7后加published/adapted/thesis synthesis表；每章结尾补上述四要素。今天可解释，答辩后文字修订，无需新训练。

## A02 — controlled / recovery 是否过强，weakly 的定义

关联：R1-05、15、19。中文要点：结构确定不等于表达唯一；承认无音频时无法唯一找回原演奏。weakly expressive描述标签，weak supervision描述监督。

**30-second core**

“I agree that ‘most controlled’ can be misleading. Chapter 3 fixes the notes and timing, but removing audio makes the dynamics less identifiable. I mean structurally controlled, rather than easier to infer. Its output is a plausible conditional velocity completion, not a guaranteed reconstruction of the original performance. I will make that distinction explicit and define the two uses of ‘weakly’ operationally.”

**1–2-minute expansion**

“There are two separate axes. One is how much structure is trusted: in Chapter 3, pitches, onsets and offsets are given. The other is how much evidence constrains expression: without audio, several musically reasonable velocity profiles can correspond to the same notes. The model learns a conditional tendency from performed piano MIDI, and direct error against one reference is only one way of evaluating that tendency.

By weakly expressive data, I mean data whose dynamics layer is absent, flat or unreliable; I do not mean that all aspects of the music lack expression. By weak supervision in Chapter 6, I mean that real target recordings lack direct velocity labels and instead supply an indirect renderer-based learning signal. I will replace the ambiguous ordering from ‘constrained to ambiguous’ with a two-axis scenario description, and qualify ‘recovery’ as completion, refinement or renderer-conditioned estimation according to the chapter.”

**实际证据**：§1.5 p6/PDF33；§3.1–4 pp39–41/PDF66–68；§3.10 p50/PDF77；§6.3 p88/PDF115。Ch3 input为binary frame roll，非audio。

**让步/边界**：单一reference不穷尽可接受表达；没有概率多解实验。不能凭“结构固定”声称任务更容易。

**具体修订**：§1.5定义术语、§3.1改structurally fixed，§3.3/3.10明确conditional completion；统一结论措辞。今天澄清+答辩后改写。

## A03 — piano-roll、event tokens、musical time与quantised score

关联：R1-17、18、20、21、24。中文要点：Ch3是2D稀疏回归，“颜色”是强度类比；Ch4最终已经是onset tokens；performance→quantised泛化未验证。

**30-second core**

“For Chapter 3, the piano roll gives a simple two-dimensional representation of simultaneity and local pitch–time structure. ‘Colourisation’ is an analogy for adding velocity intensity, not an RGB method. Chapter 4 actually tokenises score onsets for its final Transformer. I agree that beat-based inputs and quantised scores deserve separate evaluation; the current performance-MIDI results do not establish that transfer.”

**1–2-minute expansion**

“In Chapter 3 the input is an 88-pitch by 96-frame occupancy matrix, and the target carries velocity values. Convolutions and skip connections exploit local polyphonic patterns, while the loss masks note onsets. The cost is rasterisation and a fixed physical-time grid. The duration ablation compares five, ten, fifteen and twenty seconds; it is not a beat-alignment experiment.

Chapter 4 retains frame-aligned score matrices as an interface to the AMT output, but the final correction network extracts onset coordinates and processes a variable-length note-token sequence. That is an event-oriented computation within a frame-compatible interface.

A beat-based representation could make rhythm and tempo relationships more explicit, but would require musical-time information and a controlled comparison. More importantly, the Chapter 3 evaluation preserves performed timing. I will separate the demonstrated performance-MIDI task from the proposed quantised-composition application, and describe a quantisation or beat-grid comparison as future work rather than claiming that it has already succeeded.”

**实际证据**：§3.4 pp41–42/PDF68–69；Table3.4 p48/PDF75；§3.6 pp43–44/PDF70–71；§4.5.1–2 pp54–56/PDF81–83。Fig4.2视觉确认onset tokenisation。

**让步/边界**：现有baseline comparison不构成严格same-capacity representation ablation；performance timing可能携带表达线索。

**具体修订**：改image-based为sparse 2D piano-roll formulation；补representational trade-off段；收窄量化应用结论。event/beat/quantised对比为可选新实验，需用户确认后才开展。

## A04 — 风格依赖与11人听测的证据强度

关联：R1-16；R2-04。中文要点：承认learned style prior；听测支持而非证明普适。数字只背一组，别把CI当显著性检验。

**30-second core**

“The listening test provides supporting perceptual evidence within a small, controlled piano setting. It involved eleven expert listeners and eight short excerpts, rendered with one calibrated Pianoteq configuration. The U-Net received higher mean similarity ratings than the comparison systems, but this is not definitive validation across listeners, repertoire or instruments. Composer-group results are descriptive, and I will state those limits more clearly.”

**1–2-minute expansion**

“Velocity completion necessarily learns stylistic regularities from its training data. The SMD evaluation helps test transfer beyond the exact MAESTRO performances, but the corpora still share much of their classical-piano repertoire. The listening examples include familiar, less familiar and unseen composers, yet those groups are not matched for musical complexity or other confounds. I would therefore not infer composer independence from their ordering.

The listening test was reference-based and MUSHRA-inspired, rather than a strict MUSHRA protocol. All stimuli preserved the same notes and timing, which isolates the audible effect of the velocity layer under the chosen renderer. Table 3.6 reports an overall mean of 3.01 for U-Net, compared with 2.08 for ConvAE and 1.50 for flat velocity. Those are useful descriptive results. They complement the objective metrics, but the small participant and stimulus sample limits population-level conclusions. I will revise the discussion accordingly and separate a larger, balanced perceptual study as an optional extension.”

**实际证据**：Table3.1 p44/PDF71；§3.9 pp48–49/PDF75–76；Table3.6同p49；U-Net 3.01±0.34 / ConvAE2.08±0.33 / Flat1.50±0.37（文中标95%CI）；不是已复核原始ratings的重分析。

**让步/边界**：11人/8×10秒、单renderer、专家群体；CI不证明每个pair有显著差异，也不是严格style-disjoint实验。

**具体修订**：§3.9–10加入supporting evidence和抽样限制；去除definitive/verified普适判断；若已有ratings可核对listener/stimulus聚合，无原数据不补造统计。

## A05 — 模块化velocity与完整AMT、生态效度

关联：R1-23、27、37。中文要点：已知音符场景有现实价值，但存在漏错音时不够；joint modelling值得研究，不能冒称note F1改善。

**30-second core**

“The modular design addresses a real but restricted use case: audio with trusted note events from an aligned score. It improves velocity attached to those events and makes the correction reusable across backbones. It does not repair missing or incorrect notes. I agree that velocity and note transcription can help each other, but the thesis does not demonstrate a gain in note-transcription accuracy from joint modelling.”

**1–2-minute expansion**

“In education and curated archives, an aligned score can already supply the note structure, so separating dynamics is useful. Chapter 4 evaluates velocity at those known onsets. Its cross-backbone results support a reusable correction interface: for example, on SMD, HPT velocity MAE changes from 10.0 to 8.0 with Score-HPT. That result supports velocity correction under score support; it is not evidence that pitch or onset detection improves.

For Chapter 5, the outputs can conceptually be attached to a score produced by a note-transcription system, and the chapter illustrates that workflow. However, estimating beats, dynamics and change points is not equivalent to validating the complete note-to-score pipeline.

A full integration study would need to propagate uncertain note events or alignments and measure both note accuracy and dynamics quality. I will make the present interface assumptions explicit, distinguish the illustrated workflow from the evaluated system, and discuss joint training as a complementary research direction.”

**实际证据**：§4.3–5.4 pp52–57/PDF79–84；Table4.2 p63/PDF90（HPT10.0/Score-HPT8.0；不是同篇note F1）；§5.3 p69/PDF96；Fig5.1 p68/PDF95；§7.4.5 p112/PDF139。

**让步/边界**：known-note evaluation不覆盖note错误；global timing shift不等同真实缺音/局部tempo warp；“保持架构”不等同权重冻结。

**具体修订**：给Ch4/5各写input contract、未评估的完整管线限制；新joint-AMT或note-F1验证列为可选新实验，不作为小修必做。

## A06 — Ch4 loss权重和Table4.1协议

关联：R1-25、26。中文要点：系数相等不等于loss平衡；明确输入与训练更新范围，细节未由代码证明就不臆测。

**30-second core**

“Equation 4.6 combines mean BCE over active frames with mean L1 error at note onsets, using unit coefficients. The normalisation prevents note duration from directly controlling the number of onset terms, but it does not guarantee equal numerical or gradient contributions. I have not reported a weight-sensitivity study. I will clarify that choice and define every input variant in Table 4.1 before presenting its results.”

**1–2-minute expansion**

“The two terms supervise different aspects of the prediction. The active-frame term retains information over sounding-note regions, while the onset term directly targets the value assigned to each MIDI note. Separate averaging makes their sample counts explicit, but it does not prove an optimal balance. I would describe the current objective as an adopted hybrid design, supported by the system-level results, rather than as a demonstrated best weighting.

The table also needs a clearer protocol. ‘Audio’ denotes the AMT velocity branch; onset and frame are aligned binary score features; frame-excluded-onset is frame minus onset. The BiLSTM processes dense frame sequences, while the final Transformer uses onset tokens and a bounded residual update. The reported setup describes retraining the velocity branch and a jointly trained score-informed counterpart. I will reconcile that description with any ‘frozen’ wording elsewhere after checking the implementation records. A targeted loss-weight comparison would be useful, but it is not part of the evidence currently reported.”

**实际证据**：Eq4.1–5 pp55–56/PDF82–83；Eq4.6 p57/PDF84；§4.6.2 p58/PDF85；Table4.1 p59/PDF86。unit系数与两个平均项已视觉核对。

**让步/边界**：§2.5.4 p28/PDF55称frozen AMT front-end，而§4.6.2称jointly trained；须查训练记录，今天不要直接承诺“backbone frozen”。源仓库有论文LaTeX，没有本实验训练代码/日志可在本次核验。

**具体修订**：Table4.1前加协议与notation表；统一freeze/train描述；补实际loss尺度/梯度记录若已有。权重消融为可选新实验，不能虚构已做。

## A07 — change point、beat/downbeat耦合和hairpins

关联：R1-28、29、38。中文要点：state与transition不同；共享但无显式约束；CPt不是渐强跨度。

**30-second core**

“The dynamic head predicts a state, while the change-point head highlights sparse transitions between regimes. Beat and downbeat heads share the encoder and experts, so they are linked through representation learning and training gradients. They do not currently have an explicit downbeat-within-beat constraint. I will distinguish that implicit sharing from structural consistency, and state that static levels plus change points do not represent crescendo or diminuendo spans.”

**1–2-minute expansion**

“The motivation for the change-point head is that a score annotation needs both a dynamic state and a location where the regime changes. In this implementation the outputs are predicted on a frame grid and then read or snapped on a beat grid. This matches the available annotation convention and gives sparse transition supervision a dedicated objective.

However, predicting level at each beat and taking differences is a reasonable alternative. The chapter does not isolate the benefit of the change-point head against that specific baseline, so I will present the rationale without claiming that explicit change points are necessary in every system.

Similarly, separate beat and downbeat heads can exploit the same shared information without being forced to produce logically consistent events. A joint decoder or consistency term could address that, but it remains an extension. Finally, the five score-dynamics labels describe static levels. A hairpin needs direction and a time span, so I will add that distinction to the thesis-wide limitations as well as the Chapter 5 limitations.”

**实际证据**：§5.3 p69/PDF96；Fig5.2 p72/PDF99；Eq5.2–7 pp73–74/PDF100–101；§5.7.5 p82/PDF109。五静态类pp,p,mf,f,ff加blank，不含mp/hairpin span。

**让步/边界**：Table5.3的MMoE等消融不是CPt-vs-level-difference消融；没有显式downbeat⊆beat约束。

**具体修订**：补state/transition与共享/显式耦合说明；结论§7.3同步hairpin限制；新结构约束和CPt替代baseline为可选实验。

## A08 — Ch5跨数据集：为何做、能够说明什么

关联：R1-30；本次核查V-01。中文要点：迁移失败是有用发现；annotation prior解释是合理推断非因果分离；目标上挑best-fold必须坦白。

**30-second core**

“Cross-dataset evaluation is useful here as a stress test, rather than as an assumption that score dynamics is composer independent. It exposes differences in acoustics, repertoire and annotation conventions. I should also qualify the protocol: the external table selects the best transferred fold using target dynamic F1. That is an optimistic diagnostic, not an unbiased estimate with completely target-independent model selection.”

**1–2-minute expansion**

“The piece-disjoint MazurkaBL folds test unseen pieces within one corpus. Vienna and Batik then ask a different question: what happens when the recording conditions, repertoire and score-label priors change? The transfer results show that dynamic-label prediction and metrical tracking can fail differently. For the proposed BSSL multitask model, dynamic F1 is 54.4 in-domain, while the selected-fold Vienna score is 32.0. This comparison is descriptive because the aggregation and selection protocols differ.

The class distributions make annotation shift a plausible contributor, but the current study does not experimentally separate its causal effect from acoustics or repertoire. I will avoid presenting that explanation as established causation.

The most immediate revision is to label the external table explicitly as a best-fold transfer diagnostic. If retained per-fold outputs are available, a stronger summary would report all folds or use source-validation selection. That would be a reanalysis of existing outputs where possible, not a claim that a new experiment has already been completed.”

**实际证据**：§5.6.1 pp74–75/PDF101–102；Table5.1 p75/PDF102；Table5.2 p78/PDF105；§5.7.3/Table5.4 p80/PDF107；讨论pp81–82/PDF108–109。BSSL multitask Vienna32.0/Batik53.0；Vienna38.2来自log-Mel变体，不与54.4混说为同一模型。

**让步/边界**：no fine-tuning不等于未用target labels挑checkpoint；single-task每任务独立挑best fold与multitask按dynamic挑fold，比较不完全对称。

**具体修订**：显著标注protocol；保留原表并补all-fold/source-selected摘要（若已有预测可得）；无预测才提出重跑，先征得用户同意。

## A09 — Ch6到底恢复什么、DDSP保真度与跨乐器边界

关联：R1-33；R2-03；本次核查V-02。中文要点：renderer-conditioned、不是物理真值；承认钢琴监督基线最佳；吉他改善是loudness correlation；语音/弦乐/管乐不能外推。

**30-second core**

“Outside sensor-recorded piano, I interpret velocity operationally: a renderer-conditioned note-level control that reproduces aspects of the observed dynamics. The guitar evidence is based on resynthesised loudness correlations, not ground-truth velocity accuracy. A mismatched DDSP renderer can direct gradients toward timbre or recording differences. The results support the proxy in the tested setting, while a well-matched differentiable synthesiser could still be preferable.”

**1–2-minute expansion**

“Equation 6.3 defines the target relative to a renderer and a comparison space. That matters because guitar, voice, bowed strings and wind instruments do not share a single physical onset-velocity coordinate. In the tested guitar setting, Diff-SFProxy gives higher loudness correlations than zero-shot VeloEst and the tested Diff-Synth adaptation. For example, on FL, BSSL correlation is 0.777 for the proxy and 0.740 for zero-shot VeloEst.

This does not establish a general fidelity ranking of the synthesisers. The experiments measure how useful their supervision is for velocity under this setup. On piano, the directly supervised baseline remains better than either adaptation strategy, which reinforces the distinction between an indirect dynamics objective and true velocity supervision.

The features emphasise early harmonic energy and attack flux, so transfer to sustained-bow or breath-driven instruments would require different control and feature choices. I will state those boundaries explicitly. I will also verify the provenance of Figure 6.3 before making any claim that a real guitar example has measured ground-truth velocities.”

**实际证据**：§6.3/Eq6.3 p88/PDF115；Table6.2 p99/PDF126（MAESTRO MAE baseline3.9/proxy10.5；不是proxy优于监督）；Table6.3 p100/PDF127；§6.9.1–4 pp101–103/PDF128–130。

**让步/边界**：Fig6.3 p101/PDF128称guitar GT，但§6.6.1/6.8.1称真实GAPS/FL无velocity标签；目前无法判定图来自synthetic/piano还是误标。不能靠猜测修补。loudness r不是人类听测，也不确定真实手势。

**具体修订**：加跨乐器claim boundary表；核查Fig6.3资产/脚本/数据来源后改caption或撤去其物理GT主张；未确认前不以该图支持真实吉他准确性。新instrument/fidelity测试均需另议。

## A10 — V^(0)、Vhat，proxy训练与adaptation两阶段

关联：R1-32、35。中文要点：三个不同对象：粗roll、修正velocity、参数descriptor；分清训练谁/冻结谁/target来自哪里。

**30-second core**

“V-zero is the coarse velocity roll from the acoustic module. V-hat is the score-corrected prediction produced by the Transformer. Neither is a ground-truth label. There are also two separate proxy stages: offline training matches SoundFont-rendered targets and updates the proxy; adaptation freezes that proxy and updates VeloEst against descriptors extracted from real recordings. I will make those stages and symbols explicit in the figure.”

**1–2-minute expansion**

“The notation follows the estimator architecture: acoustic features produce a preliminary velocity map, and score information refines its onset values. Chapter 6 then uses that same estimator as the front end for two possible adaptation interfaces. In Diff-Synth, predicted velocities are rendered into audio and compared in spectral space. In Diff-SFProxy, the frozen proxy maps notes and predicted velocities into PHE and OSF descriptors.

Figure 6.2 concerns building the proxy. A known synthetic note sequence, including sampled velocities, is rendered through the selected SoundFont. The extractor measures the target descriptors from that rendered audio, and the proxy learns to predict them. In adaptation, the target descriptors instead come from the real recording. The functional loss can look the same even though the target source and the parameters being updated are different.

I agree that combining these stages without explicit labels invites confusion. I will show two panels, label rendered versus real audio, and identify the trainable and frozen components in each.”

**实际证据**：§6.4.1 pp89–90/PDF116–117；Eq6.5 p90/PDF117；Fig6.2 p93/PDF120；§6.5.4 pp94–95/PDF121–122；§6.4 p89/PDF116明确adaptation仅更新VeloEst、backends frozen。

**让步/边界**：报告说right part，但当前Fig6.2 teacher branch在左侧；回应对象是rendered target的语义，不纠缠方向。Ch6所谓fixed front-end应解释固定架构/初始化，不能说适配阶段VeloEst参数冻结。

**具体修订**：统一V0/V^(0)/Vhat；图分两panel并加训练状态；不需新增实验。

## A11 — Huber与MAE：设计理由不等于消融结论

关联：R1-34。中文要点：SmoothL1小残差平滑，大残差线性；MAE本来也是线性，不能说“比MAE更抗异常值”就结束。

**30-second core**

“I chose Smooth L1 as a pragmatic optimisation compromise: it is quadratic near zero and linear for larger residuals. The local smoothness can help optimise noisy note-wise descriptors. MAE is also linear in the tails, so I would not claim that Huber is automatically more robust than MAE to large errors. The thesis does not report a direct comparison demonstrating that it is superior.”

**1–2-minute expansion**

“The descriptors can be contaminated by overlapping notes and imperfect onset windows. A quadratic loss everywhere could give large residuals excessive influence. Smooth L1 limits that behaviour while keeping a smooth gradient near small residuals. Relative to MAE, the specific motivation is the transition near zero, not a fundamentally different tail behaviour.

Equation 6.6 states beta equal to one and equal weighting of the two descriptor components over valid notes. Those are design choices, and their numerical meaning depends on the descriptor scales. The present results support the complete adaptation method under that choice; they do not isolate the causal contribution of the loss function.

I will revise the explanation to distinguish motivation from experimental evidence and document the actual feature scaling from the implementation. A matched MAE comparison would be a focused sensitivity study, but I will not describe it as completed or necessary to preserve the current conclusions. If requested after the defence, it should use fixed data splits, seeds and model-selection rules.”

**实际证据**：Eq6.6 p91/PDF118；§6.5.4 pp94–95/PDF121–122；论文beta1.0、PHE/OSF1:1。现有Tables6.2–3是crop/regulariser/pretraining消融，没有MAE-vs-Huber行。

**让步/边界**：未核对实现中的归一化及loss reduction；不以理论理由替代实测优越性。

**具体修订**：补SmoothL1分段行为、尺度说明、无direct ablation声明；新loss比较仅列可选实验。

## A12 — “simpler”、SoundFont耳听选择与自动化

关联：R1-31、36。中文要点：简化的是目标域标签需求/接口，不是整个建模；仍有real-vs-renderer gap；自动选择尚未做。

**30-second core**

“I agree that ‘simpler’ is too broad. The approach reduces the need for direct target-domain velocity labels and focuses supervision on a small descriptor space, but it adds proxy training and renderer selection. The SoundFonts were selected by listening from a small candidate pool. That is a practical choice with a reproducibility limitation, and I will document it and describe automated selection as future work.”

**1–2-minute expansion**

“The estimator adapts against real recordings, which avoids relying only on synthetic-audio transfer for the front end. However, the proxy itself is trained on synthetic renderings, so renderer-to-recording mismatch remains. I should describe where the mismatch enters rather than claiming that the domain gap disappears.

The selected assets are Salamander Grand Piano for piano and Spanish Classical Guitar for guitar. The chapter reports an additional piano-renderer diagnostic for the evaluation metric, but that is not an automated bank-selection experiment and does not establish that the selected guitar bank is optimal.

A possible automated procedure would rank a predefined candidate pool on a separate validation set using task-relevant descriptor or loudness agreement, with checks for velocity saturation and a transparent selection rule. It should not choose a bank using the final test scores. Even a good automatic match would remain task-conditioned rather than prove physical equivalence to the performer’s instrument. I will soften the wording and separate this proposed extension from the work already done.”

**实际证据**：§6.2 p87/PDF114；§6.6.2 p96/PDF123；§6.9.2 p102/PDF129（两种piano renderer的metric diagnostic）；§6.9.4 p103/PDF130。

**让步/边界**：试听选择主观、候选小；metric diagnostic≠bank search；voice/wind等不只需换bank，还需改变特征与控制维度。

**具体修订**：将simpler改focused indirect supervision；补候选/选择记录（若实际记录可得）；自动bank选择为可选后续实验，未经确认不运行。
