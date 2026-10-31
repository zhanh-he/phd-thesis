## R1-01 引用体例由作者决定，不为可选建议重写全文
A: No thesis prose change is proposed. Retain the existing numeric citation style consistently throughout the thesis.

评审是 suggest，未要求必须转换。整篇转换会改变引用宽度与页码；目前没有作者立场。此项应留给人工选择，不把作者未回复当成接受。

## R1-02 更新 ISMIR 接收状态
A: Accepted for publication in the \emph{International Society for Music Information Retrieval (ISMIR) Conference}, 2026.

报告 1 Preamble 明确 accepted，所给 ISMIR PDF 为该文的会议版。只写 accepted，不凭相机稿文件名宣称正式出版。

## R1-03 Fig.1.1 补足乐器身份和其他表达因素
A: Figure labels: Step 1: Note events and instrument identity. Estimate pitch, onset, duration, and instrument identity. Step 2: Expressive information. Estimate MIDI velocity and score dynamics, together with instrument-specific controls such as pedalling and articulation. Highlight MIDI velocity and score dynamics as the thesis focus.

Caption: A conceptual view of AMT, including note events, instrument identity, and expressive information. MIDI velocity and score dynamics are the expressive targets studied in this thesis.

B: Figure labels: Note events: pitch, onset, and duration. Instrument identity: instrument or source assignment. Expressive information: dynamics, articulation, pedalling, and other instrument-specific controls. Connect these outputs to MIDI and score representations, and highlight the dynamics branch.

Caption: Main information layers in an AMT output. Note content, instrument identity, and expressive controls contribute to a symbolic representation of a performance. This thesis studies the recovery of MIDI velocity and score dynamics.

C: Figure labels: Performance audio → Acoustic analysis → Note events / Instrument identity / Expressive controls. Within expressive controls, highlight MIDI velocity and score dynamics; show articulation and pedalling as further examples.

Caption: Conceptual outputs of expressive AMT. The branches identify complementary information layers rather than a required sequence of independent processing stages. The highlighted dynamics outputs define the scope of this thesis.

A 直接落实作者“在图中补进”承诺且改图最少。B 更易区分内容；C 避免把两步流程误当唯一架构，但重画幅度最大。三稿均不声称本文估计了所有表达控制。

## R1-04 recollecting 改 collecting
A: collecting

作者已明确接受，无需 A/B/C。

## R1-05 定义 weakly expressive 与 weakly supervised
A: Here, weakly expressive data retain useful note structure but provide a simplified dynamics layer, for example MIDI with all velocities set to 64 or with only coarse dynamic levels. Weak supervision refers to settings in which the target dynamics labels are missing, incomplete, or unreliable, so learning relies partly on indirect evidence. These conditions can overlap in the same dataset.

B: In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. Weakly supervised settings lack reliable target labels for direct training; Chapter 6 instead uses real audio and a renderer-based comparison to supervise the velocity estimator indirectly. These terms describe the available information rather than the quality of the musical performance. These conditions can overlap in the same dataset.

C: The three terms describe different deficiencies in the available data. Incomplete data omit a required dynamics label; weakly expressive data retain note content and timing but flatten or coarsen the dynamics; and weakly supervised data provide no reliable direct target for learning. The last condition motivates the proxy-supervised extension in Chapter 6, while the first two motivate recovery or refinement of an existing symbolic layer. These conditions can overlap in the same dataset.

B 把数据状态和学习监督条件分开，并用 Ch.6 已有方法落地。A 最短；C 衔接好但对三词分类较硬，现实数据可以同时具备多种状态。不会把八级 score dynamics 本身等同“差”的数据。

## R1-06 S3 不是所有 audio-only 输出的总称
A: The scenarios describe the studies undertaken here rather than every possible audio-to-symbolic task. Chapter 6 extends S2 by retaining audio and aligned note events while replacing target-domain velocity labels with indirect renderer-based supervision. Audio-only adaptation for MIDI velocity estimation is a possible extension, but is not evaluated in this thesis.

B: The input condition alone does not determine the dynamics target. Audio-only MIDI velocity estimation is also possible, but S3 refers specifically to the score-dynamics task studied in Chapter 5. The beyond-piano study in Chapter 6 uses the score-informed estimator from Chapter 4 and still requires aligned note events. It therefore extends S2 under weaker target-domain supervision rather than adding an audio-only velocity experiment.

C: Table 1.2 separates three studied input–output settings. S1 predicts velocity from symbolic context, S2 refines velocity using audio and aligned notes, and S3 predicts score dynamics together with metre from audio. Chapter 6 returns to the S2 interface under missing target velocity labels. Extending the same adaptation strategy to an audio-only velocity estimator remains a future direction.

B 正面回答评审“是否也可以 audio→velocity”，并保留作者当前优先 S2 的立场。未采用作者口头“3 times MAE”：当前 Ch.4 Table4.2 的 hFT=9.9、Score-HPT=8.0 不能支持这个倍数。

## R1-07 Fig.2.1 是多种关系，不是必经 MIDI 的链
A: Relationships among physical sound level, perceived loudness, MIDI velocity, and score dynamics. The layers are related but are not an obligatory processing chain. In particular, score dynamics may be inferred directly from audio-derived perceptual evidence without first estimating MIDI velocity; the inference remains context-dependent.

B: Relationships among the dynamics representations used in this thesis. MIDI velocity is one route between symbolic control and sound, but it is not a required intermediate representation for score-dynamics estimation. Chapter 5 learns a direct audio-to-score-dynamics mapping. Instrument response, performer interpretation, and musical context prevent any of these links from defining a universal one-to-one conversion.

C: The representations provide complementary descriptions of dynamics. Rendering relates MIDI velocity to acoustic output, psychoacoustic analysis relates audio to loudness, and contextual inference relates performed sound to score markings. The direct audio-to-score-dynamics route studied in Chapter 5 therefore coexists with velocity-based workflows; none supplies a fixed instrument-independent lookup table.

B 同时保留作者强调的 instrument/style 不确定性并承认评审提出的直接路径，符合 Ch.5 实际输入输出。A 短；C 更像正文解释而非图注，可能变长。

## R1-08 Bark 表每组三列加分隔线
A: \begin{tabular}{ccc|ccc|ccc}

精确对应评审的 1–3 / 4–6 / 7–9，不误改 Table2.4 的软件映射表。

## R1-09 把 onset 说法限定为本文的 Note On velocity
A: In this thesis, MIDI velocity means the Note On velocity associated with a note attack. MIDI also supports Note Off velocity and separate control messages, which are not the targets studied here. Each sounding note can therefore receive its own onset-velocity value, including notes played simultaneously in a chord.

B: The target studied here is MIDI Note On velocity: a discrete control value attached to the start of a note. This definition is narrower than the full MIDI protocol, which also includes Note Off velocity, aftertouch, and continuous controllers. The thesis estimates one onset value per note rather than a time-varying control trajectory.

C: The note-level target in this thesis is Note On velocity. It records or controls the attack of an individual note, so simultaneous notes may have different values. Other MIDI messages can describe release behaviour or changes during a note, but these remain outside the present target. This is why the velocity chapters preserve note events and estimate only an onset attribute.

作者确认 onset 的本意可保留，但全 MIDI protocol 的“always”需收窄。已向 MIDI Association 官方 message summary 核验 Note On、Note Off、aftertouch、CC 的区分；不新增未经同意的 bibliography 条目。A 最短；C 强调与 thesis 关系，略重。

## R1-10 Fig.2.3 颜色不能猜含义
A: Panels (d)–(f) use a uniform colour for note events; colour does not encode velocity, voice, or instrument identity. Horizontal position indicates time. The vertical axes in (e) and (f) show the displayed event-lane index and MIDI pitch, respectively.

现资产没有图例和作图脚本，不能从色相推断是 velocity 或 voice。统一颜色是可实施且不改变本图 temporal-coordinate 用途的最小方案。

## R1-11 humanisation 用一行定义
A: Here, humanisation refers to adding or varying expressive controls in a symbolic sequence, such as note timing and velocity, to move it away from a mechanically uniform rendering.

无需删除已有术语；定义后马上回到本文只改 velocity 的范围，短句就能解决。

## R1-12 crescendo 已有定义，只补定位与范围
A: Besides static levels, score dynamics includes gradual indications such as crescendo and diminuendo, as described in Section 2.3.1. Chapter 5 estimates the five static levels available in its annotations and their change points; it does not explicitly decode these longer-span symbols.

原文 §2.3.1 已明确 directional indications、hairpins 和 span。真正缺口是 §2.6.1 与 Ch.5 实验范围衔接；未来方向另见 R1-38。

## R1-13 数据表拆清 note events、performance velocity、score 与音频可用性
A: Representative datasets relevant to expressive label recovery. “MIDI / note annotations” includes performance MIDI and aligned note annotations convertible to MIDI; it does not by itself imply measured velocity. “Velocity” indicates the availability of the note-level dynamics target, with qualifications stated in the row notes. “Score” refers to a reference symbolic score, rather than the performance timing in MIDI. A triangle marks a qualification in the corresponding row. For ATEPP, 43% denotes the reported share of recordings paired with scores, not a verified share with score-dynamics labels. Audio access limitations are stated separately in the row notes.

B: Representative datasets relevant to expressive label recovery, separating audio access, note annotations, velocity annotations, reference scores, and score-dynamics annotations. The provenance of velocity annotations is specified in the row notes. A tick indicates the stated modality, a cross indicates its absence, and a triangle refers to a qualification in the corresponding row note. The audio column distinguishes available performance recordings, externally linked recordings, and software-rendered material. For ATEPP, the reported 43% applies to score availability; the dynamic markings in those scores have not been verified.

C: The table separates structural note information from expressive supervision. A MIDI file or a convertible note annotation can provide pitch and timing without containing measured performance velocity. Reference scores provide notated structure and may be quantised, whereas performance MIDI retains performed timing. The 43% shown for ATEPP describes score coverage and should not be read as the availability of verified dynamic markings. Audio access and any annotation qualifications remain dataset-specific and are stated in the row notes. A triangle indicates a qualification explained in the corresponding row note.

推荐A：只补字段释义和图例，最少改变拥挤表格。B已改成velocity annotations并要求row notes写provenance，不把estimated/software/captured混称captured；但新增Audio单元格仍待逐行填实。C已补triangle通用图例，可作表后解释。ATEPP分母仍是待确认项。

## R1-14 背景定义常用指标，同时保留 Ch.5 平均方式待核验
A: For a given class or event type, precision is the fraction of predictions that are correct, and recall is the fraction of reference instances that are recovered. Their harmonic mean is F1. For note-level velocity, MAE measures the mean absolute difference from the reference value; Chapter 3 additionally reports error dispersion, tolerance-based recall, and predicted-velocity dispersion. Each metric is interpreted on the coordinate appropriate to its target.

B: For a given class or event type, precision is TP/(TP+FP), recall is TP/(TP+FN), and F1 is 2TP/(2TP+FP+FN), where TP, FP, and FN are true positives, false positives, and false negatives. Macro-F1 averages the class-wise scores equally, whereas support-weighted F1 weights them by their reference counts. These averages answer different questions and must be identified when reporting score-dynamics results. Note-level velocity MAE averages the absolute prediction error over the reference note onsets; its full definition and the complementary dispersion metrics are given in Section 3.6.3.

C: Evaluation follows the output representation. Note-wise velocity error measures agreement with captured MIDI values, while velocity dispersion checks whether the output collapses towards a constant. Score dynamics is assessed as beat-wise classification, for which precision, recall, and F1 describe false labels and missed labels. Beats and downbeats are evaluated as time-stamped events. The averaging rule, temporal grid, and event-matching tolerance must be identified when interpreting each result.

B 正式区分 macro 与 weighted，能补齐 background，又不擅自断言现有 Ch.5 数值是哪一种。A 更短但数学定义略弱；C 适合读者导向，缺明确定义。Chapter3 metrics 实际 §3.6.3，最终自动引用 label 应取代硬编码编号。

## R1-15 用信息条件描述 S1，不用单一难度排序
A: This chapter addresses Scenario S1, where only symbolic information is available. Here the symbolic notes and their timing are already known, but the note-level velocity is missing, flattened, or musically uninformative. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?

B: This chapter addresses Scenario S1, where the symbolic notes and their timing are known, but the velocity layer is missing, flattened, or musically uninformative. No performance audio is available to guide the prediction. The fixed note structure limits what the model may change without uniquely determining the velocity profile. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?

C: In the symbolic-only setting, the notes and their timing are fixed, while velocities may be missing, flattened, or musically uninformative. The model changes only the velocity layer and has no performance audio from which to infer it. The chapter therefore asks a focused question: can useful note-level dynamics be recovered from symbolic structure alone, without changing the original composition?

A只替原首句，完整保留原来的第二、三句，最接近作者原段；B进一步区分固定结构和估计歧义；C把条件与模型操作连起来，稍有改写。推荐A作为最小有效修改，B供作者希望把歧义讲明时选择。三稿均不再把候选首句叠加到重复的原第二句。

## R1-16 区分跨曲目使用与风格控制
A: The model is not conditioned on composer or performer identity. Its aim is to provide a useful velocity completion across the piano repertoire represented in the data, rather than to reproduce a requested style.

B: Composer and performance style can influence a plausible velocity profile, but the present model does not offer explicit style control. The available training data motivated learning a shared completion model rather than separate composer-specific models.

C: A completed velocity profile is one plausible expressive interpretation of a fixed note sequence. The present model learns this interpretation from pooled piano performances without a composer or style control input. The composer-group scores reported in the listening section describe the model within the selected repertoire.

B保留作者因数据覆盖限制选择shared completion的解释。A最短；C强调多解性，但与R1-19可能重复。听测样本和composer分组限制集中在R2-04，不在这里再加一遍。

## R1-17 image-like 的含义与 piano-roll 选择一起解释
A: The representation is image-like because pitch and time form a two-dimensional grid processed by convolutional layers. The binary piano roll provides the note structure, and the target velocity roll assigns a scalar value at note locations. Colourisation is an analogy for adding the missing velocity layer; the model does not predict RGB colours. This representation motivates the U-Net and attention design used here \cite{he2025filling,kim2024method}.

B: A piano roll places simultaneous notes along the pitch axis and their local evolution along time, giving the U-Net a regular two-dimensional input. Convolution and skip connections can then use local pitch–time neighbourhoods while preserving the given note structure. The output is a single-channel velocity roll. We use colourisation as an analogy for completing that missing scalar layer, rather than for predicting RGB colour. This representation motivates the U-Net and attention design used here \cite{he2025filling,kim2024method}.

C: The choice of representation follows the proposed architecture. A piano roll exposes local pitch–time neighbourhoods and simultaneous-note patterns on a regular grid that can be processed by a U-Net. Note-list or event-token representations are valid alternatives, but would require a different interface. The image-like formulation studied here adds a single velocity channel to existing notes; its advantages over the selected baselines do not establish that it is superior to every event-based formulation. This representation motivates the U-Net and attention design used here \cite{he2025filling,kim2024method}.

推荐B，局部澄清single-channel与regular pitch-time grid，并保留原段已有citation keys。R1-18共用。全文只出现这一处image-based需要改；其他colourisation用法可以保留为已定义的analogy，不能机械改正式title或每处都补RGB解释。具体审计只证明完成逐句检查，不宣称源文已修改或最终全文一致性已执行。

## R1-18 piano roll 与 event list 的取舍
A: Use the selected paragraph under R1-17. It explains the regular pitch–time grid and limits the comparison to the representations actually studied.

两个问题紧邻且共享解释；一段即可覆盖，另在 representation 开头保留 O/F/V 数学定义。

## R1-19 recovery 是实验构造，estimation 是一般任务
A: Velocity completion is an estimation task. In the supervised experiments, reference velocities are removed from captured performances, so recovery describes the reconstruction setting. At deployment, a sequence with flat or missing velocities may admit several plausible completions; the model does not recover a uniquely determined original performance from note structure alone.

B: We use completion for the operation of adding missing velocities and estimation for the prediction problem. Recovery is appropriate in the supervised evaluation because the withheld reference values are known. For new symbolic input, the output is instead an estimated expressive profile, whose usefulness need not imply that it reproduces one uniquely correct interpretation.

C: The training construction begins with performance MIDI and withholds its velocity layer. This permits a direct comparison against captured values, but does not make velocity a deterministic function of the score. The same estimator can complete previously unseen or quantised MIDI without a recorded reference; in that use, its output should be read as a plausible velocity realisation rather than a reconstruction of a known performer.

B 保留作者“开始是recovery，最终task是estimation”，不强迫全论文统一成一个词。A 很直接；C 衔接应用好，但与 R1-21 可能重复。

## R1-20 physical time 是兼容性选择，不是 beat-alignment 劣势的证明
A: The fixed-duration representation accepts the note timings already present in a MIDI file, including performance MIDI and estimated note events, without requiring a beat map. A musical-time representation is also possible, but is not compared in the present experiments.

B: We use physical time to retain the timing supplied with the input and to avoid requiring a score or beat map. This is useful when the input comes from a performance or a transcription system as well as from a quantised score. A beat-relative representation could provide useful metrical context; the present study does not establish whether it would improve velocity estimation.

C: Physical-time and musical-time grids emphasise different information. The current grid accepts existing event times directly, while a beat-relative grid could normalise tempo and expose metrical position. Such a representation need not remove expressive timing if that information is retained separately. We therefore treat the choice as an untested representation alternative, rather than claim that beat alignment would necessarily reduce expressiveness.

B 保留作者兼容 AMT 输入的实际动机，但不把 beat-relative 等同 hard quantisation。C 更直接纠正逻辑，语气稍像回复而非正文；A 最小。

## R1-21 量化 MIDI 听测保留作者说明，待刺激记录对齐
A: Performance MIDI supplies captured velocity targets for training, while the completion interface can also accept quantised symbolic input. The composition use case is to add a velocity profile while retaining the notes and timing supplied by the user.

B: The supervised experiments use performance MIDI because it provides captured velocity targets. The completion interface itself takes the note events and timing supplied with a MIDI sequence, including quantised symbolic input. Its role in composition is to add a velocity profile without changing that supplied structure.

C: For composition, velocity completion adds an expressive layer to an existing note sequence. Training uses captured velocities from performance MIDI, while deployment can retain the notes and timing of quantised symbolic input. The training target and the timing representation of a new input therefore serve different roles.

A最短且足以说明训练数据和composition接口不冲突；B更明确区分训练与输入条件；C叙述较顺。三稿均不含“The author reports”、编辑指令或虚构的timing处理。推荐A。

## R1-22 单列 baselines，重排已有事实即可
A: We compare against three baselines. Flat assigns velocity 64 to every note and represents a sequence without note-wise dynamic variation. Seq2Seq uses the pretrained attention-based model of Kim et al. (2023). ConvAE follows Kuo et al. (2021) and is re-implemented in our training framework. ConvAE and the proposed U-Net are trained on the same MAESTRO split with the same training schedule and objective; Seq2Seq retains its available pretrained weights. All outputs are evaluated at the given note onsets using the metrics defined below.

无需新增网络细节或未经核验的parametercounts。既有引用键 kim2023piano / kuo2021velocity 应用于此段，英文作者年仅为阅读写法，排版沿作者最终citation选择。

## R1-23 modular correction 的实际适用范围与联合模型互补
A: This modular setting is useful when trusted note events already exist, as in aligned educational or archival material. It does not imply that velocity and note detection are independent in performance, or that joint modelling cannot improve transcription. The present evaluation isolates velocity estimation at known notes and therefore does not measure gains in note detection.

B: The separation is a task definition rather than a claim that note content and dynamics are independent. It fits applications with a reliable score or existing note sequence, where replacing note decisions is unnecessary. Joint note-and-velocity models may use these quantities to support one another, but that benefit is outside an evaluation that supplies reference note events. The contribution here is a reusable refinement interface under this stated condition.

C: Modular refinement and joint transcription address different use conditions. If a reliable note sequence is available, a velocity-only correction can improve its expressive layer while preserving the user's structure. If the note sequence is uncertain, a joint system may be more appropriate because dynamics and note evidence can interact. This chapter studies the first condition and leaves the second as an integration direction.

独立审查认为A已能说明应用范围和未测note-detection增益，且§4.4已有较充分用例说明。本轮采用A作为最小方案；B/C保留供作者偏好更完整局部讨论时选择，不再机械推荐最长稿。

## R1-24 Ch.4 实际上是矩阵接口加 onset tokens
A: The matrices provide a common pitch–time interface with the AMT velocity map and make onset and sustain masking explicit. They are not the final sequence representation of the Transformer: the correction module extracts the known onset coordinates and processes them as note tokens. The frame-wise BiLSTM variant retains the dense grid for comparison. The final design therefore combines a piano-roll interface with event-centred correction rather than choosing dense matrices over event tokens throughout.

作者批注提到multi-scale，但本章最终模块是onset-tokenTransformer；不能把Ch.5架构动机借来当Ch.4事实。此稿直接对照数学定义与现有architecture，无需暗示尝试过任何未报告模型。

## R1-25 明确 hybrid loss 的相对权重与证据边界
A: All models are trained with the hybrid loss adopted in prior score-informed work~\cite{kim2024method}. It combines frame-wise binary cross-entropy with onset-wise $\ell_1$ loss:
\begin{equation}
\mathcal{L}
= \frac{1}{|\mathcal{J}|}\sum_{(t,p)\in\mathcal{J}} \ell_{\mathrm{bce}}\big(V_{t,p},\hat{V}_{t,p}\big)
+ \frac{1}{|\mathcal{I}|}\sum_{(t,p)\in\mathcal{I}} \left|V_{t,p}-\hat{V}_{t,p}\right|.
\label{eq:scoreinf:loss}
\end{equation}
Here $\mathbf{V}$ is the ground-truth velocity target and $\hat{\mathbf{V}}$ is the predicted velocity output of either the baseline AMT branch or the score-informed system. Each component is averaged over its own mask, and the two means have equal relative coefficients. Equal coefficients do not imply equal numerical loss or gradient magnitudes.

B: All models are trained with the hybrid loss adopted in prior score-informed work~\cite{kim2024method}. It combines frame-wise binary cross-entropy with onset-wise $\ell_1$ loss:
\begin{equation}
\mathcal{L}
= \frac{1}{|\mathcal{J}|}\sum_{(t,p)\in\mathcal{J}} \ell_{\mathrm{bce}}\big(V_{t,p},\hat{V}_{t,p}\big)
+ \frac{1}{|\mathcal{I}|}\sum_{(t,p)\in\mathcal{I}} \left|V_{t,p}-\hat{V}_{t,p}\right|.
\label{eq:scoreinf:loss}
\end{equation}
Here $\mathbf{V}$ is the ground-truth velocity target and $\hat{\mathbf{V}}$ is the predicted velocity output of either the baseline AMT branch or the score-informed system. The frame-wise BCE and onset-wise L1 terms are averaged over their respective active positions and combined with equal relative coefficients. We retain the hybrid objective of Kim et al. (2024), supported by the preliminary comparison with frame-only and onset-only supervision reported in our associated SMC paper. Equal coefficients do not imply equal numerical loss or gradient magnitudes.

C: All models are trained with the hybrid loss adopted in prior score-informed work~\cite{kim2024method}. It combines frame-wise binary cross-entropy with onset-wise $\ell_1$ loss:
\begin{equation}
\mathcal{L}
= \frac{1}{|\mathcal{J}|}\sum_{(t,p)\in\mathcal{J}} \ell_{\mathrm{bce}}\big(V_{t,p},\hat{V}_{t,p}\big)
+ \frac{1}{|\mathcal{I}|}\sum_{(t,p)\in\mathcal{I}} \left|V_{t,p}-\hat{V}_{t,p}\right|.
\label{eq:scoreinf:loss}
\end{equation}
Here $\mathbf{V}$ is the ground-truth velocity target and $\hat{\mathbf{V}}$ is the predicted velocity output of either the baseline AMT branch or the score-informed system. The two terms supervise complementary parts of the note representation: frame-wise BCE covers the active note region, while onset-wise L1 directly penalises the velocity read during post-processing. Each term is averaged over its own active positions, and the two means receive equal relative coefficients. This retains the hybrid formulation used in the prior work and our preliminary verification.

A直接回答normalisation与实际相对系数；B保留作者及SMC提供稿明确记载的preliminary comparison；C多解释两个目标的角色。推荐B，保留有证据的验证，又不加入every-backbone/dataset最优性免责声明。现有材料中的hybrid-versus-single-target比较不能代替weight-sweep证据；未找到sweep记录也不等于证明作者从未做过。

## R1-26 Table4.1 每个 setup 用现有变量逐一解释
A: In Table 4.1, audio denotes the standalone HPT velocity branch. The score-informed rows add either the frame-wise BiLSTM or the onset-token Transformer correction module. The onset condition uses the score onset matrix O; onset + frame additionally supplies the active-note matrix F; and onset + frame_ex uses F − O to distinguish sustain from the onset frame. These conditions vary the correction module and its score features under the same MAESTRO training and evaluation setting. Parameter counts refer to the complete velocity-estimation system shown in each row.

对照表中每行和已有 O/F/Fex 定义，避免再创造setup编号。若公式采用label引用，最终改成Table~ref避免编号漂移。

## R1-27 完整 AMT 集成作为未来方向，不虚报已验证性能
A: These outputs could be attached to the note content of a score-level AMT system to produce dynamics-annotated notation. The present experiments evaluate dynamics and metrical estimation separately from note transcription, so they do not establish the performance of a complete integrated AMT system or an improvement in note-detection accuracy.

B: For score-facing dynamics, integration would attach the estimated markings to note content on a common metrical grid. This provides a route to expressive notation, while leaving the interaction with note-transcription errors to a complete-system evaluation. The present experiments evaluate the dynamics component under its stated inputs and do not establish a gain in pitch, onset, or offset accuracy.

C: The models supply complementary expressive layers that could enrich an AMT output. Chapter 4 refines velocity at aligned note onsets, while Chapter 5 supplies score-facing markings on a metrical grid. Combining these layers with note transcription is a natural next step. A complete system would need to evaluate both note-event accuracy and the recovered expressive layer.

第5章推荐A，最小且不重复现有两种用法。B已把metrical grid限定为score-facing markings；C适合第7章，明确velocity用note onsets、markings用metrical grid。两处不复制同一长段。

## R1-28 state 与 boundary 是互补监督，并非二选一
A: More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat. The dynamic-level head estimates the prevailing state, while the change-point head gives transitions a separate supervision target. Both contribute to the beat-synchronous output.

B: More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat. The separate change-point head gives transitions an explicit supervision target, instead of deriving boundaries only from changes in the predicted level sequence. It complements the beat-wise level output by modelling when a new dynamic region begins.

C: More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat. Boundaries can also be derived from changes between adjacent beat-wise level predictions. We instead give transitions their own supervision through a separate change-point head, alongside the level prediction. This lets the model learn the boundary target directly.

推荐B：不重复定义frame grid和beat mask，只补显式boundary supervision这一独特理由。A最短；C明确承认可由相邻level变化导出边界，再说明本工作选择。删除“beat-wise levels本身不能区分stable/new region”的错误必需性论证，也不借未做的独立CPt消融宣称因果增益。

## R1-29 共享表征、分头 loss 与 decoding 连接同时说明
A: Beat and downbeat predictions share the encoder and expert pool, but use separate heads and loss terms. Their event outputs are linked during post-processing: when predicted beats are available, detected downbeats are snapped to the nearest predicted beat and duplicate positions are removed. No explicit beat–downbeat consistency term is added to the training loss.

B: The beat and downbeat tasks are coupled through shared representation learning and through decoding, rather than by a direct connection between their output heads. Each head has its own shift-tolerant loss. In post-processing, downbeats are moved to the nearest predicted beat when a beat sequence is available, with duplicate events removed. This enforces the event-level relation at decoding time without adding a learned cross-head constraint.

C: The architecture separates task-specific prediction from musical consistency at the output. The shared encoder and MMoE experts let beat and downbeat learning use common evidence, while separate gates, heads, and losses preserve their task-specific decisions. The decoder then snaps downbeats to predicted beats where available. A stronger consistency objective during training is a possible extension, but is not part of the reported model.

固定beat_postproc.py明确有条件snap和dedup，符合作者第二条回复。B清楚区分coupling阶段；A最短，C更完整但会与MMoE段重复。不再写“只有共享，完全无连接”。

## R1-30 cross-dataset 是测迁移边界，不是分离风格因果
A: The 5-fold MazurkaBL evaluation already gives a partial test of generalisation because the folds are piece-disjoint. It remains an in-domain setting, with the performer pool, recording conditions, repertoire family, and annotation conventions inherited from MazurkaBL. We therefore evaluate transfer to Vienna4x22 and Batik-plays-Mozart after training on MazurkaBL. These external tests change several corpus conditions together and do not isolate a composer or performer effect.

B: Piece-disjoint cross-validation tests generalisation to unseen mazurkas within MazurkaBL. Cross-dataset evaluation additionally tests the learned mapping under changes in repertoire, performers, recording conditions, and annotation conventions. These factors vary together in Vienna4x22 and Batik-plays-Mozart, so the experiment diagnoses combined corpus transfer rather than isolating a composer or performer effect.

C: The external tests extend the piece-disjoint MazurkaBL evaluation by asking how the learned mapping transfers under different corpus conditions. Vienna4x22 and Batik-plays-Mozart change repertoire, performers, recording conditions, and score-label conventions together. Their results therefore describe transfer to those corpora, while a separate balanced design would be needed to isolate the individual factors.

A最接近原段并保留piece-disjoint与in-domain区别；B更清楚压缩combined shift，去掉了向评审反驳的opening；C改为how transfer，不把mixed outcomes定义成stops transferring。推荐B。selection disclosure是独立且必要的具体协议说明，不能用一般distribution-shift限制代替；其两处重复合并到一处。

## R1-31 不用未测的 simpler 或 efficiency 优越性
A: This chapter instead adapts the estimator directly on real performance audio without requiring target-domain velocity labels. A differentiable renderer supplies the indirect training signal, while renderer mismatch remains a limitation.

B: This chapter takes a more direct route to target-domain adaptation. Rather than relying only on transfer from synthetically labelled audio, the estimator is adapted using real performance recordings and a differentiable rendering interface. This reduces dependence on target velocity annotation, but does not remove the need to model or approximate the renderer.

C: The practical aim is to reduce dependence on unavailable target-domain velocity labels. We therefore train the adaptation stage against real performance audio through a differentiable interface. The advantage concerns access to supervision, while the renderer or proxy still has to be built and matched to the target setting.

B保留作者更直接／减少annotation需求的意思，也与提供的ISMIR稿more direct route一致。A最短；C把对比落在supervision availability与接口要求，解释较长，B更紧凑。作者的more efficient可理解为减少target annotation需求，未经测量不直接写一般效率优势。

## R1-32 V^(0) 是粗估 roll，Vhat 是 correction 后的逐音值
A: VeloEst acts as the shared front-end of the framework, estimating note-wise MIDI velocities $\hat{V}$ from the performance audio and aligned note events. We use the score-informed HPT model with onset and frame as score-guidance, which is identified as the best VeloEst configuration in Chapter~\ref{ch:scoreinf}~\cite{he2026score}. We keep its architecture unchanged and use the publicly available checkpoint trained on MAESTRO with ground-truth velocity supervision $\mathcal{L}_{\mathrm{velo}}$. Using this estimator keeps the cross-instrument experiment focused on the supervision interface rather than on introducing a new velocity-estimation architecture.

The estimator has two stages. The acoustic module, borrowed from the High-Resolution Piano Transcription system~\cite{kong2021hpt}, takes log-Mel spectrograms computed at $100$\,fps from $22050$\,Hz mono audio (FFT size $2048$, hop $221$\,samples, Hann window) as input and predicts a coarse velocity roll $V^{(0)}$. A score-informed Transformer then refines $V^{(0)}$ into $\hat{V}$ using aligned note information. Here, $V^{(0)}$ denotes the intermediate acoustic estimate, while $\hat{V}$ denotes the corrected onset values passed to the rendering interface; the superscript does not identify a pre-adaptation checkpoint. The detailed architecture and supervised training procedure are given in Chapter~\ref{ch:scoreinf}. The architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen.

接受审查。round1只给解释段会删被PHE/OSF节再引用的FFT设置；本稿完整保留配置。没有把100fps/hop221重新调参或悄改为另一值。V^(0)表示中间声学阶段而非adaptation前checkpoint；结构不变和参数更新分别说明。

## R1-33 DDSP fidelity 是限制，退化不等于因果证明
A: DDSP-Piano and DDSP-Guitar-Synth are differentiable approximations of the target instruments. Their timbre and velocity response need not match the real recordings. The observed degradation after Diff-Synth adaptation is consistent with acoustic mismatch, but we have not separately measured reconstruction fidelity or the accuracy of velocity-related gradients on the target data.

B: The waveform back-ends are used as differentiable approximations rather than exact reproductions of the recorded instruments. Their usefulness depends both on acoustic fidelity and on whether changing velocity produces the appropriate change in sound. The Diff-Synth results are consistent with a mismatch in this interface, but do not isolate its cause: reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.

C: A differentiable synthesiser can offer useful gradients without reproducing every detail of a recording, but the relevant error is not timbral fidelity alone. Its velocity-to-sound response must also be suitable for the adaptation target. The present comparison shows weaker adaptation with the selected Diff-Synth back-ends, but does not isolate the cause of that degradation. The conclusion is limited to the tested interfaces and recordings.

推荐B，局部A/B/C均已通过第二轮复审，保持原文。共同同步涉及三个完整段落、五个逐句操作：保留FL的0.083/0.01及crop-length观察，删除无独立依据的普遍稳定性末句，并把unobserved-controls吸收写成may therefore absorb。没有改结果、设置或模型设计。

## R1-34 Huber 的梯度理由与 MAE 对照边界
A: In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). Huber is quadratic for small residuals and L1-like for larger residuals, giving smoother gradients near zero while limiting the influence of large errors. We did not conduct a dedicated comparison with MAE.

B: In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). Huber is quadratic near zero and L1-like for larger residuals. We chose it for its smoother small-error gradients than MAE; we did not conduct a dedicated comparison with MAE.

C: In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). The parameter targets can contain residual error from overlapping notes and imperfect onset alignment. Huber combines a smooth small-error region with linear growth for larger residuals. This motivates the chosen objective; a dedicated comparison with MAE was not conducted.

推荐A，技术理由和未做专门MAE比较都明确，且最少改动。B已用did not conduct排除“做过但未证实”的歧义；C保留参数污染动机但略长。三个拼接稿均保留β与1:1，不重复设置，也不声称large-error线性惩罚是Huber独有优势。

## R1-35 Fig6.2 已提 rendered audio，补图内 teacher 路径
A: Offline training of the differentiable SoundFont proxy. Sampled MIDI notes and velocities are rendered by the SoundFont; PHE and OSF extracted from this rendered audio provide the teacher targets. The Transformer predicts the same parameters from the note sequence. Real performance audio is used later for VeloEst adaptation, not to generate these offline teacher targets.

caption区分两训练阶段；图内明确中间audio节点即可。现图已有“Render MIDI to Audio”，因此也可选择仅保留原图／增加目标标签，不必重新设计整个架构。

## R1-36 自动选择 SoundFont 留为明确未来工作
A: Automating SoundFont selection is a natural extension. A matching procedure could compare candidate renderers with representative target recordings, but should assess their velocity response as well as timbral similarity.

B: Automatic SoundFont selection could make the framework easier to apply to larger or more varied corpora. Such a procedure would need to consider both timbral match and the velocity-dependent response that supplies the training signal. The present study uses by-ear selection and does not evaluate an automated selection method.

C: Because the selected renderer conditions the recovered velocity, an automated selection procedure should assess its velocity response as well as timbral similarity. Developing and evaluating such a procedure remains future work; the current results retain the stated manually selected SoundFonts.

推荐A，局部两句足够；B保留更完整的当前/未来说明也可。C已把影响操作目标的因素准确归于selected renderer，而非自动化本身。没有新增算法或实验承诺。

## R1-37 完整 AMT 与 note accuracy 的回应统一放一处
A: Integrating the proposed dynamics layers with note transcription is a natural next step. Such a system should be evaluated for expressive usefulness as well as pitch, onset, and offset accuracy; the present component-level studies do not establish an improvement in those note-transcription measures.

保留作者对human-prefer与客观指标可能不一致的判断，但不把这种可能性写成本文已测结论。

## R1-38 明确未显式恢复渐强渐弱，加入 span 输出方向
A: The score-dynamics model is restricted to the five static levels in MazurkaBL and their change points. It does not explicitly recover crescendo, diminuendo, or other span-based expressive symbols, which remain future targets.

B: The five static levels and change points studied in Chapter 5 do not cover the full dynamics vocabulary. A change point indicates a boundary between regions; it does not specify the onset, duration, or direction of a crescendo or diminuendo. Extending the output to such spans would require compatible annotations and an evaluation of both the symbol and its temporal extent.

C: Score dynamics includes sustained instructions as well as discrete levels. The present model estimates static levels and local transitions; gradual directions such as crescendo and diminuendo are not explicitly represented. A future score-facing interface could represent these as labelled spans alongside the beat-wise levels, preserving the distinction between a gradual instruction and an abrupt change of dynamic state.

A最短；B更具体说明change points与gradual-span输出的区别，把限制和未来需求连起来；C更偏未来接口叙述，并已明确not explicitly represented。推荐B，不要求本轮增加实验。

## R2-01 现有章节首尾已经显式回应中心问题，推荐保留
A: No additional thesis paragraph is proposed. The existing chapter overviews explicitly state the data condition, dynamics target, and relation to the thesis question. Retain those paragraphs, subject to the specific terminology and scope corrections identified in R1-06 and R1-15.

报告2也肯定现有chapterpositioning结构。逐章实际原文已经给scope，不为形式性满足建议堆叠同义段。最终revisionreport可准确说“保留并澄清已有联系”，不能称新增了四段若没新增。

## R2-02 四篇论文的技术贡献与 thesis 新增综合分开
A: Chapters 3–6 develop the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common dynamics-recovery question, a comparison of data-availability conditions, and a cross-chapter discussion of representation and evaluation. These thesis-level syntheses should be distinguished from the method contributions attributed to the individual studies.

B: The technical chapters are based on four co-authored studies: symbolic velocity completion (CMMR 2025, Chapter 3), score-informed correction (SMC 2026, Chapter 4), joint dynamics and metrical estimation (ICASSP 2026, Chapter 5), and cross-instrument proxy supervision (ISMIR 2026, Chapter 6). Their authorship and publication details are listed in the Authorship Declaration. The thesis brings these studies together through a common label-recovery formulation and scenario map, provides shared background, and synthesises their assumptions and limitations in Chapter 7.

C: The four studies address different parts of the same expressive-label problem. The technical methods are attributed to their associated co-authored papers, while the thesis develops the connections between them: which musical structure is trusted, which dynamics representation is recovered, and what supervision and evaluation support the resulting claim. This synthesis is developed in Chapters 1, 2, and 7 and in the positioning sections of the technical chapters. It should be read as the thesis contribution alongside, rather than as a replacement for, the individual method contributions.

推荐B，明确四篇mapping并描述当前thesis实际存在的organising/synthesis工作。A更短，C更叙述化。round1理由“都能从独立论文核实新增”过强，本轮撤回该归属判断：能核实这些结构在thesis中存在，不等于证明思想首次只在thesis出现或已穷尽相对最终paper的所有新增。

## R2-03 把 beyond-piano 可迁移与未验证部分写具体
A: The strongest direct supervision remains piano-based. The guitar study supports the use of a renderer-conditioned onset-velocity coordinate in the tested guitar corpora, evaluated through rendered loudness rather than captured guitar velocity. It does not validate the same estimator or parameter set for voice, bowed strings, or wind instruments.

B: The piano chapters support conclusions about the tested piano datasets and targets. Chapter 6 extends the supervision strategy to guitar, where the evidence concerns renderer-conditioned velocities and loudness agreement rather than recovery of captured physical velocity labels. Voice, bowed strings, and wind instruments were not evaluated. Their sustained dynamics and continuous controls would require suitable target coordinates and descriptors beyond the attack-focused PHE/OSF pair used here.

C: What may transfer beyond piano is the recovery framework: specify the trusted notes, choose an editable dynamics coordinate, and match the supervision to that coordinate. The empirical evidence is narrower. It covers piano and the tested guitar adaptation, not a validated instrument-general estimator. For voice, bowed strings, and wind instruments, onset intensity alone cannot describe the sustained and continuously shaped aspects of dynamics, so the target and comparison features would need to be reconsidered.

B直接点名examiner列的四类并区分principletransfer与performancevalidated。A最短，C很好衔接中心论点但对新乐器的目标设计论述略多。没有把guitar r当canonicalvelocityaccuracy。

## R2-04 11位听者与8段刺激是补充证据，避免 definitive validation
A: U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.

B: In the listening study, U-Net received higher mean similarity ratings than Flat and ConvAE, while Flat received the lowest ratings. The 11 expert listeners evaluated eight selected SMD excerpts rendered with one PianoTeq configuration. These results provide supplementary perceptual evidence for velocity completion within that setting. The seen, less-seen, and unseen composer groups are descriptive; the selected excerpts were not balanced to isolate stylistic effects.

C: The listener ratings favour U-Net over Flat and ConvAE in similarity to the human-performed MIDI rendering used as the reference. They provide complementary evidence alongside the note-wise objective results. This reference-based study involved 11 expert listeners, eight selected SMD excerpts, and one PianoTeq configuration, so its findings are interpreted within that setting. The composer groups describe the selected repertoire and do not isolate a stylistic effect.

推荐A：保留实际系统排序、reference-similarity目标和原有default-velocity文献，范围集中说明一次。B更像直接Results读数但不保留此句citation；C侧重与objective结果互补，未说听测验证指标本身。删除perceptual validity/population-wide musical naturalness等非本实验估计量的泛泛否定，不增加未经报告的显著性结果。MOS与CI数值不动。

## R2-05 只列实际见到的语言／格式问题
A: “capture the full aspects of a human performance” → “capture several aspects of a human performance”

“the four heads have different preference on the same shared latent” → “the four heads have different preferences for the shared representation”

“not optimal for our tasks combination” → “not optimal for this combination of tasks”

“a 10-second segment roughly encompasses four measures at 120 beats per minute (BPM)” → “a 10-second segment can span several bars, depending on tempo and metre”

前三处是实际措辞／语法问题，最后一处是可核验时间解释。Figure2.3标题与其他排版问题须先看现存PDF页面再定，不能把PDF抽取换行自动当LaTeX缺陷。