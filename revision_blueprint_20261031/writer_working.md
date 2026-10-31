# 第一轮内部候选探索记录

这份是可查的写作比较记录，不是另一位模型的评审，也不宣称已完成返修复审。每项 A1/A2、B1/B2、C1/C2 为实际探索过的短稿，列明为什么没有直接采用；A3/B3/C3 是送独立审查的完整候选。序号表示各路线的编辑小稿，不表示独立实验、独立模型或已执行修改。简单纠错不凑九稿。


## R1-01

单一事实纠错、保留或合并项；不机械凑多稿。评审是 suggest，未要求必须转换。整篇转换会改变引用宽度与页码；目前没有作者立场。此项应留给人工选择，不把作者未回复当成接受。

## R1-02

单一事实纠错、保留或合并项；不机械凑多稿。报告 1 Preamble 明确 accepted，所给 ISMIR PDF 为该文的会议版。只写 accepted，不凭相机稿文件名宣称正式出版。

## R1-03 Fig.1.1 补足乐器身份和其他表达因素

**A1 短稿**

> Step 2: Dynamics and other expressive parameters.

未直接采用：保留布局但仍未在图中给instrumentidentity独立位置。

**A2 短稿**

> Note events include pitch, duration, and instrument assignment.

未直接采用：简短但onset和表达controls需在别处补全。

**A3 送审完整候选**

Figure labels: Step 1: Note events and instrument identity. Estimate pitch, onset, duration, and instrument identity. Step 2: Expressive information. Estimate MIDI velocity and score dynamics, together with instrument-specific controls such as pedalling and articulation. Highlight MIDI velocity and score dynamics as the thesis focus.

Caption: A conceptual view of AMT, including note events, instrument identity, and expressive information. MIDI velocity and score dynamics are the expressive targets studied in this thesis.

**B1 短稿**

> Add a parallel instrument-identity branch beside the dynamics branch.

未直接采用：有效但缺完整caption，需说明scopehighlight。

**B2 短稿**

> Show dynamics, articulation, and pedal controls in a shared expression box.

未直接采用：表达层清楚，identity仍须独立补入。

**B3 送审完整候选**

Figure labels: Note events: pitch, onset, and duration. Instrument identity: instrument or source assignment. Expressive information: dynamics, articulation, pedalling, and other instrument-specific controls. Connect these outputs to MIDI and score representations, and highlight the dynamics branch.

Caption: Main information layers in an AMT output. Note content, instrument identity, and expressive controls contribute to a symbolic representation of a performance. This thesis studies the recovery of MIDI velocity and score dynamics.

**C1 短稿**

> The diagram summarises the outputs of expressive transcription.

未直接采用：可作caption开头，未解释并列而非强制串行。

**C2 短稿**

> Audio analysis supplies note, source, and expressive information.

未直接采用：source可能歧义为source-separation，最终稿用instrumentidentity。

**C3 送审完整候选**

Figure labels: Performance audio → Acoustic analysis → Note events / Instrument identity / Expressive controls. Within expressive controls, highlight MIDI velocity and score dynamics; show articulation and pedalling as further examples.

Caption: Conceptual outputs of expressive AMT. The branches identify complementary information layers rather than a required sequence of independent processing stages. The highlighted dynamics outputs define the scope of this thesis.

**本轮取舍**：推荐 A。A 直接落实作者“在图中补进”承诺且改图最少。B 更易区分内容；C 避免把两步流程误当唯一架构，但重画幅度最大。三稿均不声称本文估计了所有表达控制。

## R1-04

单一事实纠错、保留或合并项；不机械凑多稿。作者已明确接受，无需 A/B/C。

## R1-05 定义 weakly expressive 与 weakly supervised

**A1 短稿**

> Weakly expressive data have constant or coarse dynamics.

未直接采用：短而有效，但没给retainedstructure条件。

**A2 短稿**

> Weak supervision means that direct dynamics labels are limited.

未直接采用：正确但limited过宽，缺missing/unreliable的区分。

**A3 送审完整候选**

Here, weakly expressive data retain useful note structure but provide a simplified dynamics layer, for example MIDI with all velocities set to 64 or with only coarse dynamic levels. Weak supervision refers to settings in which the target dynamics labels are missing, incomplete, or unreliable, so learning relies partly on indirect evidence.

**B1 短稿**

> The terms distinguish missing expression from missing supervision.

未直接采用：清楚但还只是概括，没有操作性例子。

**B2 短稿**

> Weakly expressive MIDI retains notes but simplifies their velocities.

未直接采用：适合MIDI，未覆盖其他表征和weak-supervision条件。

**B3 送审完整候选**

In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. Weakly supervised settings lack reliable target labels for direct training; Chapter 6 instead uses real audio and a renderer-based comparison to supervise the velocity estimator indirectly. These terms describe the available information rather than the quality of the musical performance.

**C1 短稿**

> The scenarios begin with different kinds of missing information.

未直接采用：衔接自然但没有定义术语。

**C2 短稿**

> Flat velocity motivates completion, while absent labels motivate indirect learning.

未直接采用：好例子，但容易把复杂场景缩成两个互斥类别。

**C3 送审完整候选**

The three terms describe different deficiencies in the available data. Incomplete data omit a required dynamics label; weakly expressive data retain note content and timing but flatten or coarsen the dynamics; and weakly supervised data provide no reliable direct target for learning. The last condition motivates the proxy-supervised extension in Chapter 6, while the first two motivate recovery or refinement of an existing symbolic layer.

**本轮取舍**：推荐 B。B 把数据状态和学习监督条件分开，并用 Ch.6 已有方法落地。A 最短；C 衔接好但对三词分类较硬，现实数据可以同时具备多种状态。不会把八级 score dynamics 本身等同“差”的数据。

## R1-06 S3 不是所有 audio-only 输出的总称

**A1 短稿**

> Chapter 6 is a label-scarce extension of S2.

未直接采用：准确但还没正面回答audio-onlyvelocity是否可做。

**A2 短稿**

> S3 denotes audio-only score-dynamics estimation in this thesis.

未直接采用：范围清楚但未解释Chapter6为何不属于S3。

**A3 送审完整候选**

The scenarios describe the studies undertaken here rather than every possible audio-to-symbolic task. Chapter 6 extends S2 by retaining audio and aligned note events while replacing target-domain velocity labels with indirect renderer-based supervision. Audio-only adaptation for MIDI velocity estimation is a possible extension, but is not evaluated in this thesis.

**B1 短稿**

> Audio-only velocity estimation is another valid target for adaptation.

未直接采用：回应可行性，缺当前实际方法边界。

**B2 短稿**

> The beyond-piano estimator still takes aligned note events as input.

未直接采用：关键事实清楚，需补区别于targetvelocitylabels。

**B3 送审完整候选**

The input condition alone does not determine the dynamics target. Audio-only MIDI velocity estimation is also possible, but S3 refers specifically to the score-dynamics task studied in Chapter 5. The beyond-piano study in Chapter 6 uses the score-informed estimator from Chapter 4 and still requires aligned note events. It therefore extends S2 under weaker target-domain supervision rather than adding an audio-only velocity experiment.

**C1 短稿**

> The scenario map varies evidence and target representation.

未直接采用：可替换难度排序，但需具体章节映射。

**C2 短稿**

> Chapter 6 revisits velocity under weaker target-domain supervision.

未直接采用：衔接好，尚未说明沿用S2接口。

**C3 送审完整候选**

Table 1.2 separates three studied input–output settings. S1 predicts velocity from symbolic context, S2 refines velocity using audio and aligned notes, and S3 predicts score dynamics together with metre from audio. Chapter 6 returns to the S2 interface under missing target velocity labels. Extending the same adaptation strategy to an audio-only velocity estimator remains a future direction.

**本轮取舍**：推荐 B。B 正面回答评审“是否也可以 audio→velocity”，并保留作者当前优先 S2 的立场。未采用作者口头“3 times MAE”：当前 Ch.4 Table4.2 的 hFT=9.9、Score-HPT=8.0 不能支持这个倍数。

## R1-07 Fig.2.1 是多种关系，不是必经 MIDI 的链

**A1 短稿**

> The layers in Figure 2.1 are related representations, not required processing stages.

未直接采用：足够简短，但directroute仍未明说。

**A2 短稿**

> MIDI velocity is not required for audio-to-score-dynamics estimation.

未直接采用：直接答问题，缺contextdependent限定。

**A3 送审完整候选**

Relationships among physical sound level, perceived loudness, MIDI velocity, and score dynamics. The layers are related but are not an obligatory processing chain. In particular, score dynamics may be inferred directly from audio-derived perceptual evidence without first estimating MIDI velocity; the inference remains context-dependent.

**B1 短稿**

> Chapter 5 estimates score dynamics directly from audio.

未直接采用：明确例证，缺instrument/style条件。

**B2 短稿**

> Perceived loudness may inform a score marking without a velocity estimate.

未直接采用：正确但mayinform不够解释为何非一一对应。

**B3 送审完整候选**

Relationships among the dynamics representations used in this thesis. MIDI velocity is one route between symbolic control and sound, but it is not a required intermediate representation for score-dynamics estimation. Chapter 5 learns a direct audio-to-score-dynamics mapping. Instrument response, performer interpretation, and musical context prevent any of these links from defining a universal one-to-one conversion.

**C1 短稿**

> Rendering and inference link the layers in different directions.

未直接采用：可改善图意，需具体标出哪些链接。

**C2 短稿**

> The direct route still depends on musical context and annotation convention.

未直接采用：保留作者重点，但缺route的主语。

**C3 送审完整候选**

The representations provide complementary descriptions of dynamics. Rendering relates MIDI velocity to acoustic output, psychoacoustic analysis relates audio to loudness, and contextual inference relates performed sound to score markings. The direct audio-to-score-dynamics route studied in Chapter 5 therefore coexists with velocity-based workflows; none supplies a fixed instrument-independent lookup table.

**本轮取舍**：推荐 B。B 同时保留作者强调的 instrument/style 不确定性并承认评审提出的直接路径，符合 Ch.5 实际输入输出。A 短；C 更像正文解释而非图注，可能变长。

## R1-08

单一事实纠错、保留或合并项；不机械凑多稿。精确对应评审的 1–3 / 4–6 / 7–9，不误改 Table2.4 的软件映射表。

## R1-09 把 onset 说法限定为本文的 Note On velocity

**A1 短稿**

> Here velocity refers to the Note On value of each note.

未直接采用：准确最短，未回答protocol其他velocity的例外。

**A2 短稿**

> The thesis predicts one attack-velocity value per note event.

未直接采用：任务清楚，但需把NoteOn术语明确写出。

**A3 送审完整候选**

In this thesis, MIDI velocity means the Note On velocity associated with a note attack. MIDI also supports Note Off velocity and separate control messages, which are not the targets studied here. Each sounding note can therefore receive its own onset-velocity value, including notes played simultaneously in a chord.

**B1 短稿**

> Note Off velocity and continuous controls are outside the target studied here.

未直接采用：有效限定，缺正面target定义。

**B2 短稿**

> The onset-centred definition concerns the thesis target rather than every MIDI message.

未直接采用：回应准确但偏答辩口吻。

**B3 送审完整候选**

The target studied here is MIDI Note On velocity: a discrete control value attached to the start of a note. This definition is narrower than the full MIDI protocol, which also includes Note Off velocity, aftertouch, and continuous controllers. The thesis estimates one onset value per note rather than a time-varying control trajectory.

**C1 短稿**

> A note-wise attack value gives an editable dynamics coordinate.

未直接采用：有衔接价值，未说明protocol范围。

**C2 短稿**

> MIDI can describe release and within-note controls separately from the attack value.

未直接采用：可作为末句，但不必长篇展开每类control。

**C3 送审完整候选**

The note-level target in this thesis is Note On velocity. It records or controls the attack of an individual note, so simultaneous notes may have different values. Other MIDI messages can describe release behaviour or changes during a note, but these remain outside the present target. This is why the velocity chapters preserve note events and estimate only an onset attribute.

**本轮取舍**：推荐 B。作者确认 onset 的本意可保留，但全 MIDI protocol 的“always”需收窄。已向 MIDI Association 官方 message summary 核验 Note On、Note Off、aftertouch、CC 的区分；不新增未经同意的 bibliography 条目。A 最短；C 强调与 thesis 关系，略重。

## R1-10

单一事实纠错、保留或合并项；不机械凑多稿。现资产没有图例和作图脚本，不能从色相推断是 velocity 或 voice。统一颜色是可实施且不改变本图 temporal-coordinate 用途的最小方案。

## R1-11

单一事实纠错、保留或合并项；不机械凑多稿。无需删除已有术语；定义后马上回到本文只改 velocity 的范围，短句就能解决。

## R1-12

单一事实纠错、保留或合并项；不机械凑多稿。原文 §2.3.1 已明确 directional indications、hairpins 和 span。真正缺口是 §2.6.1 与 Ch.5 实验范围衔接；未来方向另见 R1-38。

## R1-13 数据表拆清 note events、performance velocity、score 与音频可用性

**A1 短稿**

> A triangle denotes a qualification explained in the dataset row.

未直接采用：最小图例有效，但没有解决MIDI/43%。

**A2 短稿**

> The 43% entry describes ATEPP score coverage.

未直接采用：符合作者说明，仍需说明不是verifieddynamics比例。

**A3 送审完整候选**

Representative datasets relevant to expressive label recovery. “MIDI / note annotations” includes performance MIDI and aligned note annotations convertible to MIDI; it does not by itself imply measured velocity. “Velocity” indicates the availability of the note-level dynamics target, with qualifications stated in the row notes. “Score” refers to a reference symbolic score, rather than the performance timing in MIDI. A triangle marks a qualification in the corresponding row. For ATEPP, 43% denotes the reported share of recordings paired with scores, not a verified share with score-dynamics labels. Audio access limitations are stated separately in the row notes.

**B1 短稿**

> An audio column would distinguish direct recordings from external links and rendered material.

未直接采用：规划合理，实际单元格仍需逐行核验。

**B2 短稿**

> MIDI availability and captured-velocity availability are listed separately.

未直接采用：关键区别清楚，当前MIDI还包括convertiblenoteannotations。

**B3 送审完整候选**

Representative datasets relevant to expressive label recovery, separating audio access, note annotations, captured velocity, reference scores, and score-dynamics annotations. A tick indicates the stated modality, a cross indicates its absence, and a triangle refers to a qualification in the row notes. The audio column distinguishes available performance recordings, externally linked recordings, and software-rendered material. For ATEPP, the reported 43% applies to score availability; the dynamic markings in those scores have not been verified.

**C1 短稿**

> The table describes what can supervise each dynamics task.

未直接采用：叙述清楚，但需要具体modalityglossary。

**C2 短稿**

> Performance timing and quantised score structure are different data roles.

未直接采用：保留作者本意，但不能把整列所有MIDI都说成performance。

**C3 送审完整候选**

The table separates structural note information from expressive supervision. A MIDI file or a convertible note annotation can provide pitch and timing without containing measured performance velocity. Reference scores provide notated structure and may be quantised, whereas performance MIDI retains performed timing. The 43% shown for ATEPP describes score coverage and should not be read as the availability of verified dynamic markings. Audio access and any annotation qualifications remain dataset-specific and are stated in the row notes.

**本轮取舍**：推荐 A。A 避免把当前包含 GuitarSet/JAMS 和软件 MIDI 的一整列都说成 unquantised performance MIDI。保留作者关于43%的意思，但不把有score自动推成有verified dynamics。B 最直接回应 audio-column 建议，但表已宽且需核验每行，C 文字较自然但图例仍需一致。

## R1-14 背景定义常用指标，同时保留 Ch.5 平均方式待核验

**A1 短稿**

> F1 combines precision and recall for a class or event type.

未直接采用：正确但没给definition，仍像泛泛介绍。

**A2 短稿**

> Velocity MAE is averaged over note onsets rather than sustained frames.

未直接采用：有效但只覆盖velocity，没回应scoremetrics。

**A3 送审完整候选**

Precision is the fraction of predicted labels or events that are correct, and recall is the fraction of reference labels or events that are recovered. Their harmonic mean is F1. For note-level velocity, MAE measures the mean absolute difference from the reference value; Chapter 3 additionally reports error dispersion, tolerance-based recall, and predicted-velocity dispersion. Each metric is computed on the coordinate appropriate to its target.

**B1 短稿**

> Macro-F1 gives every class equal weight.

未直接采用：定义简洁，需与supportweighted区分以暴露当前未定项。

**B2 短稿**

> Support-weighted F1 reflects the reference frequency of each class.

未直接采用：定义正确，需同时说macro及所用grid。

**B3 送审完整候选**

For a given class or event type, precision is TP/(TP+FP), recall is TP/(TP+FN), and F1 is 2TP/(2TP+FP+FN), where TP, FP, and FN are true positives, false positives, and false negatives. Macro-F1 averages the class-wise scores equally, whereas support-weighted F1 weights them by their reference counts. These averages answer different questions and must be identified when reporting score-dynamics results. Note-level velocity MAE averages the absolute prediction error over the reference note onsets; its full definition and the complementary dispersion metrics are given in Section 3.6.3.

**C1 短稿**

> The evaluation coordinate changes with the representation being recovered.

未直接采用：有全文衔接，但单独不足作为metric定义。

**C2 短稿**

> Error, dispersion, and classification scores answer complementary questions.

未直接采用：读者导向好，仍应给出具体量的含义。

**C3 送审完整候选**

Evaluation follows the output representation. Note-wise velocity error measures agreement with captured MIDI values, while velocity dispersion checks whether the output collapses towards a constant. Score dynamics is assessed as beat-wise classification, for which precision, recall, and F1 describe false labels and missed labels. Beats and downbeats are evaluated as time-stamped events. The task-specific definitions in Chapters 3–6 state the averaging rule, temporal grid, and matching tolerance used for each result.

**本轮取舍**：推荐 B。B 正式区分 macro 与 weighted，能补齐 background，又不擅自断言现有 Ch.5 数值是哪一种。A 更短但数学定义略弱；C 适合读者导向，缺明确定义。Chapter3 metrics 实际 §3.6.3，最终自动引用 label 应取代硬编码编号。

## R1-15 用信息条件描述 S1，不用单一难度排序

**A1 短稿**

> This chapter studies velocity completion from symbolic input alone.

未直接采用：最短且准确，未强调notes/timing固定。

**A2 短稿**

> The note sequence is known, but the performed dynamics are not observed.

未直接采用：抓住信息差，仍需点明noaudio。

**A3 送审完整候选**

This chapter addresses Scenario S1, in which note content and timing are given but no performance audio or dynamics labels are available as input.

**B1 短稿**

> Fixed note structure limits the output without uniquely determining velocity.

未直接采用：重要区分，但需接回S1task。

**B2 短稿**

> S1 removes acoustic evidence while retaining the symbolic coordinate.

未直接采用：清楚但symboliccoordinate略抽象。

**B3 送审完整候选**

This chapter addresses Scenario S1: the symbolic notes and their timing are known, while the dynamics layer is missing and no performance audio is available. The fixed note structure constrains what may be changed, but does not uniquely determine how the notes should be played.

**C1 短稿**

> The chapter starts with the input condition requiring no performance recording.

未直接采用：叙述平顺，但重点应是可观测信息而非convenience。

**C2 短稿**

> Completion is constrained in what may change and ambiguous in what should be predicted.

未直接采用：概念准确，措辞略重，最终稿用具体notes/dynamics。

**C3 送审完整候选**

The symbolic-only case separates two kinds of constraint. Notes and timing are fixed, so the model changes only velocity; the performance itself is not observed, so the expressive interpretation remains ambiguous. This chapter asks whether symbolic context alone can support a useful velocity profile under those conditions.

**本轮取舍**：推荐 B。B 保留作者“输入信号更少”的本意，也说清 fixed structure 与 velocity ambiguity 可以同时成立。A 改动最小；C 解释更细但可能与后段重复。同步修正处均按同一语义，不能换个 constrained 单词继续做难度辩护。

## R1-16 区分跨曲目使用与风格控制

**A1 短稿**

> The current model has no composer or performer control input.

未直接采用：事实够清楚，但未解释generalisationscope。

**A2 短稿**

> The model learns a shared velocity-completion function from pooled piano data.

未直接采用：有帮助，仍需指出style可影响plausibility。

**A3 送审完整候选**

The model is not conditioned on composer or performer identity. Its aim is to provide a useful velocity completion across the piano repertoire represented in the data, rather than to reproduce a requested style. The composer groups in the listening test provide descriptive evidence about this scope, not a controlled study of stylistic effects.

**B1 短稿**

> Limited training coverage motivated a shared model rather than separate style controls.

未直接采用：保留作者动机，但需要配合已报告证据边界。

**B2 短稿**

> The composer groups are descriptive subsets of the eight listening excerpts.

未直接采用：准确、具体，但没有连接训练目标。

**B3 送审完整候选**

Composer and performance style can influence a plausible velocity profile, but the present model does not offer explicit style control. The available training data motivated learning a shared completion model rather than separate composer-specific models. The listening results include more familiar and unseen composers, although the small, unbalanced set of excerpts cannot isolate composer style from piece-specific differences.

**C1 短稿**

> A symbolic sequence can support different expressive interpretations.

未直接采用：适合作为讨论起点，需补模型如何取一种。

**C2 短稿**

> The observed composer-group gap suggests a transfer question rather than a style-control result.

未直接采用：合理但gap不宜单独做因果暗示。

**C3 送审完整候选**

A completed velocity profile is one plausible expressive interpretation of a fixed note sequence. The present model learns this interpretation from pooled piano performances without a composer or style control input. The descriptive composer groups in the listening test help reveal where transfer may be weaker, while controlled style conditioning remains beyond the evidence reported here.

**本轮取舍**：推荐 B。B 忠实保留作者因数据不足从 style-control 转向 generalisation 的解释，不引入 Dolby 内部或未发表开发史。A 较短；C 更突出多解性，可与 R1-19 合并时去重。

## R1-17 image-like 的含义与 piano-roll 选择一起解释

**A1 短稿**

> Image-like refers to the two-dimensional pitch–time grid.

未直接采用：精准但没解释colourisation是scalaranalogy。

**A2 短稿**

> The target adds a scalar velocity layer to a binary note representation.

未直接采用：核心技术准确，需连接U-Net与局部结构。

**A3 送审完整候选**

The representation is image-like because pitch and time form a two-dimensional grid processed by convolutional layers. The binary piano roll provides the note structure, and the target velocity roll assigns a scalar value at note locations. Colourisation is an analogy for adding the missing velocity layer; the model does not predict RGB colours.

**B1 短稿**

> The grid makes simultaneous pitches available as local spatial context.

未直接采用：有效理由但单句未覆盖time/rasterisationcost。

**B2 短稿**

> A U-Net can process the regular grid without predicting new note content.

未直接采用：与结构preservation一致，但缺eventalternative说明。

**B3 送审完整候选**

A piano roll places simultaneous notes along the pitch axis and their local evolution along time, giving the U-Net a regular two-dimensional input. Convolution and skip connections can then use local pitch–time neighbourhoods while preserving the given note structure. The output is a single-channel velocity roll. We use colourisation as an analogy for completing that missing scalar layer, rather than for predicting RGB colour.

**C1 短稿**

> The representation is chosen to match the convolutional architecture.

未直接采用：叙述好，尚需具体机制而非适配性空话。

**C2 短稿**

> An event list is a valid alternative with a different model interface.

未直接采用：合理边界，但单独看像让步而非选择动机。

**C3 送审完整候选**

The choice of representation follows the proposed architecture. A piano roll exposes local pitch–time neighbourhoods and simultaneous-note patterns on a regular grid that can be processed by a U-Net. Note-list or event-token representations are valid alternatives, but would require a different interface. The image-like formulation studied here adds a single velocity channel to existing notes; its advantages over the selected baselines do not establish that it is superior to every event-based formulation.

**本轮取舍**：推荐 B。B 同时回答“为什么叫image-like”和“为什么用piano roll”，不把 analogy 当RGB回归，也不作 representation 因果优越性的过强归因。A 最短，C 比较边界最清楚但更长。

## R1-18

单一事实纠错、保留或合并项；不机械凑多稿。两个问题紧邻且共享解释；一段即可覆盖，另在 representation 开头保留 O/F/V 数学定义。

## R1-19 recovery 是实验构造，estimation 是一般任务

**A1 短稿**

> Recovery describes reconstruction of velocities withheld during evaluation.

未直接采用：准确，但只说evaluation，未交代deployment。

**A2 短稿**

> Completion adds missing velocities, while estimation describes the prediction operation.

未直接采用：术语清楚，需补非唯一性。

**A3 送审完整候选**

Velocity completion is an estimation task. In the supervised experiments, reference velocities are removed from captured performances, so recovery describes the reconstruction setting. At deployment, a sequence with flat or missing velocities may admit several plausible completions; the model does not recover a uniquely determined original performance from note structure alone.

**B1 短稿**

> The reference performance permits numerical reconstruction error to be measured.

未直接采用：证据清楚，仍需避免暗示score决定target。

**B2 短稿**

> For new MIDI, the estimated profile is an expressive realisation rather than a known original.

未直接采用：应用边界好，可与training句合并。

**B3 送审完整候选**

We use completion for the operation of adding missing velocities and estimation for the prediction problem. Recovery is appropriate in the supervised evaluation because the withheld reference values are known. For new symbolic input, the output is instead an estimated expressive profile, whose usefulness need not imply that it reproduces one uniquely correct interpretation.

**C1 短稿**

> Withheld values make recovery measurable without making performance interpretation unique.

未直接采用：解释有力，但句子概念密度稍高。

**C2 短稿**

> The same interface accepts symbolic input with or without a recorded performance reference.

未直接采用：实用衔接，需限定实验支持范围。

**C3 送审完整候选**

The training construction begins with performance MIDI and withholds its velocity layer. This permits a direct comparison against captured values, but does not make velocity a deterministic function of the score. The same estimator can complete previously unseen or quantised MIDI without a recorded reference; in that use, its output should be read as a plausible velocity realisation rather than a reconstruction of a known performer.

**本轮取舍**：推荐 B。B 保留作者“开始是recovery，最终task是estimation”，不强迫全论文统一成一个词。A 很直接；C 衔接应用好，但与 R1-21 可能重复。

## R1-20 physical time 是兼容性选择，不是 beat-alignment 劣势的证明

**A1 短稿**

> Physical time accepts the existing note timestamps without a beat map.

未直接采用：理由有效，但未承认musicaltimealternative。

**A2 短稿**

> The model retains the supplied timing rather than constructing a metrical alignment.

未直接采用：与作者意图一致，需避免与fulltimingaccuracy混淆。

**A3 送审完整候选**

The fixed-duration representation accepts the note timings already present in a MIDI file, including performance MIDI and estimated note events, without requiring a beat map. A musical-time representation is also possible, but is not compared in the present experiments.

**B1 短稿**

> A beat-relative grid could add tempo-normalised metrical context.

未直接采用：公允，但还需说明本研究没比较。

**B2 短稿**

> Using seconds supports performance-timed and transcription-derived MIDI.

未直接采用：实际动机清楚，未说明quantised也可接受。

**B3 送审完整候选**

We use physical time to retain the timing supplied with the input and to avoid requiring a score or beat map. This is useful when the input comes from a performance or a transcription system as well as from a quantised score. A beat-relative representation could provide useful metrical context; the present study does not establish whether it would improve velocity estimation.

**C1 短稿**

> The coordinate choice trades direct timestamp compatibility for explicit metrical context.

未直接采用：取舍合理但并非严格互斥，最终稿应更谨慎。

**C2 短稿**

> Musical time can preserve expressive offsets if they are represented separately.

未直接采用：纠正过强量化担忧，但不宜喧宾夺主成新方法建议。

**C3 送审完整候选**

Physical-time and musical-time grids emphasise different information. The current grid accepts existing event times directly, while a beat-relative grid could normalise tempo and expose metrical position. Such a representation need not remove expressive timing if that information is retained separately. We therefore treat the choice as an untested representation alternative, rather than claim that beat alignment would necessarily reduce expressiveness.

**本轮取舍**：推荐 B。B 保留作者兼容 AMT 输入的实际动机，但不把 beat-relative 等同 hard quantisation。C 更直接纠正逻辑，语气稍像回复而非正文；A 最小。

## R1-21 量化 MIDI 听测保留作者说明，待刺激记录对齐

**A1 短稿**

> Training uses captured performance MIDI because it supplies velocity targets.

未直接采用：安全事实，但不回答compositiondeployment。

**A2 短稿**

> Quantised MIDI can use the same completion interface.

未直接采用：接口说明有效，不能由此推出formalperceptualvalidation。

**A3 送审完整候选**

The model is intended for MIDI with fixed notes and timing, including quantised composition input. Training on performance MIDI provides captured velocity targets, while the extent to which the learned profile transfers to quantised input depends on the input context. The timing preparation of the listening-test stimuli is specified in the protocol below. 【Timing preparation: confirm the quantisation step and whether it was shared by system inputs and the reference.】

**B1 短稿**

> The author reports quantised score-MIDI in the listening study.

未直接采用：保留立场，但只可放证据说明，不原样写成论文protocol。

**B2 短稿**

> The stimulus timing preparation must distinguish source MIDI from rendered test input.

未直接采用：正确检查点，仍不是最终可用方法句。

**B3 送审完整候选**

Performance MIDI supplies the supervised velocity targets, but the completion operation itself does not require expressive input velocities or unquantised timing. The author reports that quantised score-MIDI was used in the listening test. 【Before inclusion, replace this note with the exact verified timing preparation of the eight stimuli.】 The test supports that practical use within its small selected set, rather than a controlled comparison of quantised and performance-timed input.

**C1 短稿**

> The composition use case concerns preserving the supplied notes and timing.

未直接采用：不依赖未核验stimuli，适合先写。

**C2 短稿**

> The test can support quantised input only to the extent established by its preparation records.

未直接采用：边界稳妥，但正式正文应换成具体已核实procedure。

**C3 送审完整候选**

The composition use case concerns preserving the input composition while adding a velocity profile. Performance MIDI is used for training because it provides captured targets; this does not restrict the interface to performance-timed inputs. 【If confirmed by the stimulus records: For the listening test, the note timings were quantised before the common symbolic input and reference were rendered, while the original velocity values were retained for the reference.】 A dedicated comparison between timing representations is outside the reported experiment.

**本轮取舍**：推荐 A（暂存，待 V-02 后定稿）。这里不应替作者改口说听测一定未量化，也不能把作者经验说成已核验的controlled comparison。A 的应用表述可以继续审查；所有正式协议句必须等既有刺激记录，不需重做实验。B 保留原说明的证据等级，不能原样带 author reports 进 thesis。C 仅在量化处理两边一致的具体条件成立时可用。

## R1-22

单一事实纠错、保留或合并项；不机械凑多稿。无需新增网络细节或未经核验的parametercounts。既有引用键 kim2023piano / kuo2021velocity 应用于此段，英文作者年仅为阅读写法，排版沿作者最终citation选择。

## R1-23 modular correction 的实际适用范围与联合模型互补

**A1 短稿**

> The intended applications already provide a score or trusted note sequence.

未直接采用：场景明确，但没回应jointlearning可能有益。

**A2 短稿**

> The evaluation corrects velocity at given notes and does not measure note-detection gains.

未直接采用：证据界限清楚，未解释实际应用价值。

**A3 送审完整候选**

This modular setting is useful when trusted note events already exist, as in aligned educational or archival material. It does not imply that velocity and note detection are independent in performance, or that joint modelling cannot improve transcription. The present evaluation isolates velocity estimation at known notes and therefore does not measure gains in note detection.

**B1 短稿**

> Modularity is a design choice for known-note refinement, not an independence assumption.

未直接采用：核心解释好，但需给教育／档案例子。

**B2 短稿**

> Joint transcription may exploit interactions between note evidence and velocity.

未直接采用：公允承认评审观点，缺本方法角色。

**B3 送审完整候选**

The separation is a task definition rather than a claim that note content and dynamics are independent. It fits applications with a reliable score or existing note sequence, where replacing note decisions is unnecessary. Joint note-and-velocity models may use these quantities to support one another, but that benefit is outside an evaluation that supplies reference note events. The contribution here is a reusable refinement interface under this stated condition.

**C1 短稿**

> The available structure determines whether refinement or joint inference is the appropriate task.

未直接采用：衔接自然但过抽象。

**C2 短稿**

> Preserving a trusted note sequence avoids replacing decisions that the application already supplies.

未直接采用：具体且有效，可与jointsetting补充句合并。

**C3 送审完整候选**

Modular refinement and joint transcription address different use conditions. If a reliable note sequence is available, a velocity-only correction can improve its expressive layer while preserving the user's structure. If the note sequence is uncertain, a joint system may be more appropriate because dynamics and note evidence can interact. This chapter studies the first condition and leaves the second as an integration direction.

**本轮取舍**：推荐 B。B 正面回应 ecological validity，承认联合建模价值而不撤回作者模块化贡献。A 较短，C 对应用条件分流更清楚但与原§4.3重复。

## R1-24

单一事实纠错、保留或合并项；不机械凑多稿。作者批注提到multi-scale，但本章最终模块是onset-tokenTransformer；不能把Ch.5架构动机借来当Ch.4事实。此稿直接对照数学定义与现有architecture，无需暗示尝试过任何未报告模型。

## R1-25 明确 hybrid loss 的相对权重与证据边界

**A1 短稿**

> The two masked means use equal relative coefficients.

未直接采用：直接答比例，但需解释equalcoeff不等于equalgradient。

**A2 短稿**

> Each term is normalised over its own active positions.

未直接采用：说明normalisation，仍不能独自证明比例合理。

**A3 送审完整候选**

Each component is averaged over its own mask, and the two means have equal relative coefficients in the stated objective. This is a fixed design choice adopted from Kim et al. (2024), not a claim that the two losses or their gradients have equal numerical magnitude.

**B1 短稿**

> The hybrid objective follows Kim et al. (2024).

未直接采用：来源已存在，单句仍没保留作者本地验证。

**B2 短稿**

> Preliminary comparisons favoured hybrid over single-target supervision.

未直接采用：上传SMC支持，但不等于weightsweep最优。

**B3 送审完整候选**

The frame-wise BCE and onset-wise L1 terms are normalised by their respective active positions and combined with equal relative coefficients. We follow the hybrid objective of Kim et al. (2024); our preliminary comparison also favoured hybrid supervision over frame-only or onset-only alternatives, as reported in the associated SMC paper. This supports the retained formulation, but does not establish that equal weighting is optimal for every backbone or dataset.

**C1 短稿**

> The frame and onset terms supervise complementary parts of the note representation.

未直接采用：任务动机清楚，需明确实际ratio。

**C2 短稿**

> The chosen ratio is retained across the studied backbones without a universal optimality claim.

未直接采用：边界合适，但实际run还需记录对齐。

**C3 送审完整候选**

The two terms serve related but different roles: frame-wise BCE supervises the active note region, while onset-wise L1 directly penalises the note velocity read during post-processing. Averaging each term over its own mask avoids making its contribution depend only on the number of active frames. We retain the equal-coefficient hybrid used in the prior work and our preliminary verification, without claiming a universal balance of gradient magnitudes.

**本轮取舍**：推荐 B。上传SMC PDF §3.3确实写preliminary hybrid vs single-target comparison，支持作者“我验证过”；没有ratio sweep记录则不能写“最佳比例已完整证明”。A最短，C解释任务目的。固定代码theta=.5与论文sum有共同整体尺度差异，但相对1:1相同；不擅改公式。

## R1-26

单一事实纠错、保留或合并项；不机械凑多稿。对照表中每行和已有 O/F/Fex 定义，避免再创造setup编号。若公式采用label引用，最终改成Table~ref避免编号漂移。

## R1-27 完整 AMT 集成作为未来方向，不虚报已验证性能

**A1 短稿**

> The dynamics outputs can be attached to an existing symbolic score.

未直接采用：接口可行，未说明完整AMT尚未evaluated。

**A2 短稿**

> The experiments evaluate the dynamics component rather than integrated note transcription.

未直接采用：范围准确，应用路径还需补一句。

**A3 送审完整候选**

These outputs could be attached to the note content of a score-level AMT system to produce dynamics-annotated notation. The present experiments evaluate dynamics and metrical estimation separately from note transcription, so they do not establish the performance of a complete integrated AMT system or an improvement in note-detection accuracy.

**B1 短稿**

> An integrated system would align predicted note content and dynamics on a common beat grid.

未直接采用：具体integration方向，但errorpropagation未提。

**B2 短稿**

> Pitch, onset, offset, and dynamics should be assessed separately in such an integration.

未直接采用：评价原则好，未交代本文已有结果的界限。

**B3 送审完整候选**

A practical integration would combine the estimated dynamics with note content from a score or a note-transcription system, using a shared beat grid. This provides a route to expressive notation, but it introduces additional alignment and error-propagation questions. The present thesis evaluates the dynamics components under their stated inputs; a complete system and any benefit to pitch, onset, or offset accuracy remain to be tested.

**C1 短稿**

> The chapters supply complementary layers for a future expressive transcription system.

未直接采用：衔接好，但要点名velocity与scoremarkings。

**C2 短稿**

> Expressive usefulness and note-event accuracy are distinct outcomes.

未直接采用：保留作者判断，不能当作本文已测二者差异。

**C3 送审完整候选**

The models supply complementary expressive layers that could enrich an AMT output. Chapter 4 refines velocity at known notes, while Chapter 5 provides score-facing markings on a metrical grid. Combining these layers with note transcription is a natural next step. It would require evaluating both the recovered dynamics and the complete symbolic output, because perceptual usefulness and note-event accuracy need not improve together.

**本轮取舍**：推荐 B。B 是可实施的接口解释且明确未测pitch/onset/offset效益，保留作者想做但需要更多时间的立场。A最小，C跨章衔接最好但新增内容略多。没有把BSSL feature直接等同听觉偏好已证实。

## R1-28 state 与 boundary 是互补监督，并非二选一

**A1 短稿**

> Dynamic levels describe states and change points describe their boundaries.

未直接采用：最短准确，未回答两者均beatdecoded。

**A2 短稿**

> Both outputs are placed on the beat grid during decoding.

未直接采用：回应作者原话，但单独没解释separatehead理由。

**A3 送审完整候选**

The dynamic-level head estimates the prevailing state, while the change-point head estimates where that state changes. Both are converted to the beat grid during decoding. The separate boundary target complements beat-wise level prediction; it does not replace it.

**B1 短稿**

> The boundary head gives transitions a supervised target distinct from the prevailing level.

未直接采用：理由清楚，需避免暗示已证明必要。

**B2 短稿**

> Beat-masked level learning and beat-snapped change points use the same metrical coordinate.

未直接采用：技术准确，但句子只谈时间单位。

**B3 送审完整候选**

Beat-wise level prediction and change-point estimation answer different questions: which dynamic level applies, and where a new dynamic region begins. The model predicts both on the frame grid, with the dynamic loss masked to annotated beats and change points snapped to beats during decoding. A separate boundary head gives transitions their own supervision rather than deriving every change from fluctuations in the level sequence. The present experiments do not establish that it is the only valid formulation.

**C1 短稿**

> A score annotation requires a level and a decision about a new marking.

未直接采用：叙述贴合应用，须对齐具体CPt标签定义。

**C2 短稿**

> Separate transition supervision avoids relying only on changes in argmax level predictions.

未直接采用：合理动机但没有对应独立消融，最终稿需限定不是onlyvalidformulation。

**C3 送审完整候选**

A score-facing annotation needs both a level and a decision about when to write a new marking. Predicting a level at each beat supplies the first, but does not by itself distinguish a stable region from a new notated event. The change-point head explicitly models that boundary decision and is decoded on the same beat grid. This is the role of the separate target, rather than an alternative to beat-synchronous dynamics.

**本轮取舍**：推荐 B。B 接住作者“dynamic markingsdecode到beat”的说明，同时解释为何还有CPt。A短但理由少；C叙述自然但“newnotatedevent”需与数据CPt标签定义一致。不声称已有去CPthead独立消融证明必需。

## R1-29 共享表征、分头 loss 与 decoding 连接同时说明

**A1 短稿**

> Beat and downbeat outputs use separate heads but a shared encoder.

未直接采用：不完整，还需experts与decoding联系。

**A2 短稿**

> Downbeats are snapped to predicted beats in the decoder when beats are available.

未直接采用：关键补充准确，仍需说明trainingloss。

**A3 送审完整候选**

Beat and downbeat predictions share the encoder and expert pool, but use separate heads and loss terms. Their event outputs are linked during post-processing: when predicted beats are available, detected downbeats are snapped to the nearest predicted beat and duplicate positions are removed. No explicit beat–downbeat consistency term is added to the training loss.

**B1 短稿**

> The tasks are coupled in representation learning and post-processing.

未直接采用：概括清楚，但需要具体coupling操作。

**B2 短稿**

> Their additive losses do not include a separate consistency term.

未直接采用：可澄清equation，缺解码事实。

**B3 送审完整候选**

The beat and downbeat tasks are coupled through shared representation learning and through decoding, rather than by a direct connection between their output heads. Each head has its own shift-tolerant loss. In post-processing, downbeats are moved to the nearest predicted beat when a beat sequence is available, with duplicate events removed. This enforces the event-level relation at decoding time without adding a learned cross-head constraint.

**C1 短稿**

> Musical output consistency is handled after task-specific prediction.

未直接采用：叙述好，但不能把所有consistency都概括成已解决。

**C2 短稿**

> Separate task gates preserve distinct predictions while shared experts supply common evidence.

未直接采用：适合architecture说明，需接decodedsubsetrelation。

**C3 送审完整候选**

The architecture separates task-specific prediction from musical consistency at the output. The shared encoder and MMoE experts let beat and downbeat learning use common evidence, while separate gates, heads, and losses preserve their task-specific decisions. The decoder then snaps downbeats to predicted beats where available. A stronger consistency objective during training is a possible extension, but is not part of the reported model.

**本轮取舍**：推荐 B。固定beat_postproc.py明确有条件snap和dedup，符合作者第二条回复。B清楚区分coupling阶段；A最短，C更完整但会与MMoE段重复。不再写“只有共享，完全无连接”。

## R1-30 cross-dataset 是测迁移边界，不是分离风格因果

**A1 短稿**

> External tests measure transfer under combined corpus differences.

未直接采用：安全但没有点名composer/performer。

**A2 短稿**

> The experiment does not isolate a composer or performer effect.

未直接采用：直达边界，缺为何仍值得做。

**A3 送审完整候选**

Cross-dataset evaluation asks whether the learned dynamics mapping remains useful when repertoire, performers, recording conditions, and annotation conventions change together. It does not isolate the effect of any one of these factors, and a transfer gap is therefore not a direct estimate of a composer or performer effect.

**B1 短稿**

> Style dependence is one reason to test a model on another corpus.

未直接采用：保留作者立场，仍需对mixedresults谨慎。

**B2 短稿**

> Repertoire, acoustics, and annotation conventions change together in these tests.

未直接采用：具体解释有力，需说明不是uniformgeneralisation。

**B3 送审完整候选**

Composer- and performer-dependent dynamics make external evaluation useful rather than unnecessary. A model trained on one corpus may learn its repertoire and annotation conventions as well as acoustic cues. Vienna4x22 and Batik-plays-Mozart test this combined shift, but their size and composition do not permit a balanced attribution to composer, performer, or recording conditions. The results are transfer diagnostics, not evidence of uniform generalisation.

**C1 短稿**

> The external corpora reveal limits not visible in piece-disjoint within-corpus folds.

未直接采用：衔接自然，但targetselectionprotocol须披露。

**C2 短稿**

> A transfer gap can reflect both acoustic mismatch and score-label convention.

未直接采用：合理解释，不能声称分离了因果。

**C3 送审完整候选**

The external tests probe where the learned mapping stops transferring. They complement piece-disjoint MazurkaBL folds by changing several corpus conditions at once, including repertoire and score-label conventions. Their mixed outcomes therefore help delimit the claim: a perceptually motivated front-end does not remove stylistic or editorial dependence. A balanced study would be needed to separate those effects, but is outside the current experiment.

**本轮取舍**：推荐 B。保留作者“正因style/performer相关才要测”的立场，同时不能把当前Vienna明显降低概括成goodgeneralisation。A最小；C解释失败边界强，可能与已有讨论重复。

## R1-31 不用未测的 simpler 或 efficiency 优越性

**A1 短稿**

> The estimator is adapted on real audio without target-domain velocity labels.

未直接采用：最小事实准确，未说明renderer仍需建模。

**A2 短稿**

> The route reduces dependence on target velocity annotation.

未直接采用：比较轴清楚，不能扩大成总效率。

**A3 送审完整候选**

This chapter instead adapts the estimator directly on real performance audio without requiring target-domain velocity labels. A differentiable renderer supplies the indirect training signal, while renderer mismatch remains a limitation.

**B1 短稿**

> We use real performance audio as the target for adaptation.

未直接采用：直接但与synthetictrainingalternative的对照不完整。

**B2 短稿**

> A differentiable rendering interface supplies indirect supervision.

未直接采用：技术准确，缺sourcepretraining与mismatch边界。

**B3 送审完整候选**

This chapter takes a more direct route to target-domain adaptation. Rather than relying only on transfer from synthetically labelled audio, the estimator is adapted using real performance recordings and a differentiable rendering interface. This reduces dependence on target velocity annotation, but does not remove the need to model or approximate the renderer.

**C1 短稿**

> The advantage concerns access to supervision rather than a universal reduction in complexity.

未直接采用：边界好，但更像回复而非method过渡。

**C2 短稿**

> The approach is more direct in how it connects predictions to real target recordings.

未直接采用：保留作者意图，需明确direct具体指何训练过程。

**C3 送审完整候选**

The practical aim is to reduce dependence on unavailable target-domain velocity labels. We therefore train the adaptation stage against real performance audio through a differentiable interface. The advantage concerns access to supervision; it is not a claim that designing the synthesiser or proxy is simpler, or that its computational cost is lower than all alternatives.

**本轮取舍**：推荐 B。B 既保留作者更直接／减少annotation需求的意思，也与上传ISMIR的more direct route一致。A最短，C明确比较轴但否定句偏多。作者提moreefficient可理解为labelacquisition效率，未经测量不建议直接写generalefficiency。

## R1-32

单一事实纠错、保留或合并项；不机械凑多稿。直接解决符号区分和roll/vector层级，顺便消除同段fixedblackbox与fine-tuned矛盾。最终LaTeX应保留原数学符号V^{(0)}、hat V，勿将此阅读用plaintext符号原样写进正文。

## R1-33 DDSP fidelity 是限制，退化不等于因果证明

**A1 短稿**

> The DDSP back-ends approximate the target instruments.

未直接采用：准确但不足回应faithfulness的实证限制。

**A2 短稿**

> Adaptation may be affected by differences in timbre and velocity response.

未直接采用：限定稳妥，需说未分别测量。

**A3 送审完整候选**

DDSP-Piano and DDSP-Guitar-Synth are differentiable approximations of the target instruments. Their timbre and velocity response need not match the real recordings. The observed degradation after Diff-Synth adaptation is consistent with acoustic mismatch, but we have not separately measured reconstruction fidelity or the accuracy of velocity-related gradients on the target data.

**B1 短稿**

> The weaker Diff-Synth results are consistent with acoustic mismatch.

未直接采用：保留作者关键句，但还应说明非因果隔离。

**B2 短稿**

> Waveform fidelity and velocity-gradient accuracy are separate properties.

未直接采用：有解释价值，需落回当前实验没有独立验证。

**B3 送审完整候选**

The waveform back-ends are used as differentiable approximations rather than exact reproductions of the recorded instruments. Their usefulness depends both on acoustic fidelity and on whether changing velocity produces the appropriate change in sound. The Diff-Synth results are consistent with a mismatch in this interface, but do not isolate its cause: reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.

**C1 短稿**

> The result concerns the selected interfaces and recordings.

未直接采用：范围明确，缺具体差异机制。

**C2 短稿**

> A well-matched waveform renderer may still supply useful velocity supervision.

未直接采用：与既有discussion一致，但不能单独代替limitation答复。

**C3 送审完整候选**

A differentiable synthesiser can offer useful gradients without reproducing every detail of a recording, but the relevant error is not timbral fidelity alone. Its velocity-to-sound response must also be suitable for the adaptation target. The present comparison shows weaker adaptation with the selected Diff-Synth back-ends; it does not establish which component of their mismatch caused the degradation. This limits the conclusion to the tested interfaces and recordings.

**本轮取舍**：推荐 B。B几乎保持作者当前回复的谨慎证据边界，区分waveformfidelity和velocitygradientfaithfulness。A最短，C逻辑更细但易重复现有discussion。不追加faithfulness实验。

## R1-34 Huber 的梯度理由与 MAE 对照边界

**A1 短稿**

> Huber provides a smooth quadratic region near zero.

未直接采用：核心动机正确，还需largeresidual行为。

**A2 短稿**

> With beta=1, large residuals receive an L1-like penalty.

未直接采用：准确，缺与MAE的实证区别。

**A3 送审完整候选**

We use Huber loss with beta = 1. It is quadratic for small residuals and L1-like for larger residuals, giving smoother gradients near zero while limiting the influence of large errors. No dedicated comparison with MAE is reported.

**B1 短稿**

> The choice concerns optimisation behaviour rather than an established MAE advantage.

未直接采用：边界明确，需加具体梯度解释。

**B2 短稿**

> No dedicated MAE comparison was conducted in the reported study.

未直接采用：保留作者事实，单独写会丢掉设计依据。

**B3 送审完整候选**

Huber loss is used for its quadratic behaviour near zero and L1-like behaviour for larger residuals. With beta = 1, it provides smoother small-error gradients than MAE while retaining a linear penalty for large PHE/OSF errors. This is a design rationale; a dedicated MAE comparison has not established that Huber gives better adaptation in this setting.

**C1 短稿**

> PHE/OSF residuals can include contamination from overlapping notes.

未直接采用：合理taskmotivation，不能当作Huber优于MAE的证明。

**C2 短稿**

> A smooth small-error region is combined with linear tail growth.

未直接采用：简明技术解释，可再给β与未比较限定。

**C3 送审完整候选**

The parameter targets can contain residual error from overlapping notes and imperfect onset alignment. Huber provides a smooth small-error region while retaining linear growth for larger residuals, so it is a practical compromise for the chosen objective. We use beta = 1 throughout. The choice should not be read as an experimentally established advantage over MAE, which also has a linear penalty for large errors.

**本轮取舍**：推荐 B。B与作者原回复一致，避免把MAE本来也robust的性质误说成Huber独有优势。A最短，C结合场景但“imperfectalignment”只是合理动机非独立测量。

## R1-35

单一事实纠错、保留或合并项；不机械凑多稿。caption区分两训练阶段；图内明确中间audio节点即可。现图已有“Render MIDI to Audio”，因此也可选择仅保留原图／增加目标标签，不必重新设计整个架构。

## R1-36 自动选择 SoundFont 留为明确未来工作

**A1 短稿**

> Automatic SoundFont selection is a future extension.

未直接采用：准确但没有说明为何不只是替换manualchoice。

**A2 短稿**

> The current study uses the stated by-ear selections.

未直接采用：保留实际protocol，未来方向还需补一句。

**A3 送审完整候选**

Automating SoundFont selection is a natural extension. A matching procedure could compare candidate renderers with representative target recordings, but should assess their velocity response as well as timbral similarity.

**B1 短稿**

> A matching procedure should consider timbre and velocity response.

未直接采用：具体且有限，不应暗示已有方法实现。

**B2 短稿**

> Automation could make renderer selection more scalable.

未直接采用：应用动机合理，但需要解释监督质量仍待评估。

**B3 送审完整候选**

Automatic SoundFont selection could make the framework easier to apply to larger or more varied corpora. Such a procedure would need to consider both timbral match and the velocity-dependent response that supplies the training signal. The present study uses by-ear selection and does not evaluate an automated selection method.

**C1 短稿**

> Renderer selection conditions the meaning of the recovered velocity.

未直接采用：与核心定义相连，但不能重复一整段scope。

**C2 短稿**

> A future selection method should be evaluated on its usefulness for adaptation.

未直接采用：方向合理，避免提出本轮新算法或测试集调优。

**C3 送审完整候选**

Renderer selection is part of the definition of the recovered velocity, so automation would change more than an implementation detail. A useful selection procedure should choose a renderer whose sound and velocity response fit the intended target material. Developing and evaluating that procedure remains future work; the current results retain the stated manually selected SoundFonts.

**本轮取舍**：推荐 B。B肯定评审想法且保留作者“重要但目前未做”的立场。上传ISMIR结尾已有同一futurework；不把自动选择当成本轮必做条件。A最短，C更强调operationaldefinition。

## R1-37

单一事实纠错、保留或合并项；不机械凑多稿。保留作者对human-prefer与客观指标可能不一致的判断，但不把这种可能性写成本文已测结论。

## R1-38 明确未显式恢复渐强渐弱，加入 span 输出方向

**A1 短稿**

> The current score-dynamics vocabulary does not include explicit crescendo or diminuendo.

未直接采用：最小范围清楚，需指出已有CPt不等价。

**A2 短稿**

> Five static levels and change points cover only part of notated dynamics.

未直接采用：准确概括，但未给futureoutput方向。

**A3 送审完整候选**

The score-dynamics model is restricted to the five static levels in MazurkaBL and their change points. It does not explicitly recover crescendo, diminuendo, or other span-based expressive symbols, which remain future targets.

**B1 短稿**

> A change point is a boundary, whereas a hairpin also has temporal extent and direction.

未直接采用：解释具体，尚需与futureannotation连接。

**B2 短稿**

> Explicit gradual symbols require suitable span annotations.

未直接采用：可作为future限制，不能要求本轮新增数据。

**B3 送审完整候选**

The five static levels and change points studied in Chapter 5 do not cover the full dynamics vocabulary. A change point indicates a boundary between regions; it does not specify the onset, duration, or direction of a crescendo or diminuendo. Extending the output to such spans would require compatible annotations and an evaluation of both the symbol and its temporal extent.

**C1 短稿**

> A score-facing interface could place labelled spans alongside beat-wise levels.

未直接采用：叙述好，保持未来时态即可。

**C2 短稿**

> Gradual instructions should remain distinct from abrupt changes of state.

未直接采用：音乐语义清楚，但单独句子未覆盖研究范围。

**C3 送审完整候选**

Score dynamics includes sustained instructions as well as discrete levels. The present model estimates static levels and local transitions, leaving gradual directions such as crescendo and diminuendo implicit. A future score-facing interface could represent these as labelled spans alongside the beat-wise levels, while preserving the distinction between a gradual instruction and an abrupt change of dynamic state.

**本轮取舍**：推荐 B。B说明CPt不等于hairpin，限制与future要求相连而不提出本轮新实验。A最短，C叙述顺畅但implicit可能被误读为已可靠检测，因此B更稳。

## R2-01

单一事实纠错、保留或合并项；不机械凑多稿。报告2也肯定现有chapterpositioning结构。逐章实际原文已经给scope，不为形式性满足建议堆叠同义段。最终revisionreport可准确说“保留并澄清已有联系”，不能称新增了四段若没新增。

## R2-02 四篇论文的技术贡献与 thesis 新增综合分开

**A1 短稿**

> The four technical chapters are based on the co-authored studies in the declaration.

未直接采用：补Ch.6遗漏，但缺thesis新增综合内容。

**A2 短稿**

> The thesis adds a common recovery question and cross-chapter synthesis.

未直接采用：新增综合明确，缺各paper映射。

**A3 送审完整候选**

Chapters 3–6 develop the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common dynamics-recovery question, a comparison of data-availability conditions, and a cross-chapter discussion of representation and evaluation. These thesis-level syntheses should be distinguished from the method contributions attributed to the individual studies.

**B1 短稿**

> Chapter 3 maps to CMMR, Chapter 4 to SMC, Chapter 5 to ICASSP, and Chapter 6 to ISMIR.

未直接采用：可查但像清单，还需说明adaptation与synthesis的不同。

**B2 短稿**

> The shared background and scenario map connect the four method studies.

未直接采用：清楚但未说明方法归属保留。

**B3 送审完整候选**

The technical chapters are based on four co-authored studies: symbolic velocity completion (CMMR 2025, Chapter 3), score-informed correction (SMC 2026, Chapter 4), joint dynamics and metrical estimation (ICASSP 2026, Chapter 5), and cross-instrument proxy supervision (ISMIR 2026, Chapter 6). Their authorship and publication details are listed in the Authorship Declaration. The thesis-level addition is the common label-recovery formulation, the scenario map connecting the studies, the shared background, and the synthesis of their assumptions and limitations in Chapter 7.

**C1 短稿**

> The thesis asks what label is recoverable under each evidence condition.

未直接采用：叙述自然，需防读者仍不清楚publicationboundary。

**C2 短稿**

> The synthesis relates representation, structure, supervision, and evaluation across studies.

未直接采用：具体且有依据，可与明确paperattribution合并。

**C3 送审完整候选**

The four studies address different parts of the same expressive-label problem. The technical methods are attributed to their associated co-authored papers, while the thesis develops the connections between them: which musical structure is trusted, which dynamics representation is recovered, and what supervision and evaluation support the resulting claim. This synthesis is developed in Chapters 1, 2, and 7 and in the positioning sections of the technical chapters. It should be read as the thesis contribution alongside, rather than as a replacement for, the individual method contributions.

**本轮取舍**：推荐 B。B补入原文遗漏的Ch.6并给读者明确mapping，所称thesisaddition都能从独立论文与当前chapter结构核实，不把已有paper的proxy诊断说成thesis新增。A最短，C更流畅但不如B可查。

## R2-03 把 beyond-piano 可迁移与未验证部分写具体

**A1 短稿**

> The empirical evidence is limited to piano and the tested guitar setting.

未直接采用：范围准确，未区分两类groundtruth/evaluation。

**A2 短稿**

> Voice, bowed strings, and wind instruments were not evaluated.

未直接采用：直答要求，缺为什么target可能要变。

**A3 送审完整候选**

The strongest direct supervision remains piano-based. The guitar study supports the use of a renderer-conditioned onset-velocity coordinate in the tested guitar corpora, evaluated through rendered loudness rather than captured guitar velocity. It does not validate the same estimator or parameter set for voice, bowed strings, or wind instruments.

**B1 短稿**

> Guitar velocity is evaluated as a renderer-conditioned coordinate through loudness agreement.

未直接采用：证据界限好，需接其他乐器范围。

**B2 短稿**

> Sustained and continuous controls require descriptors beyond the current attack-focused pair.

未直接采用：对应Ch.6限制，不能写成新模型承诺。

**B3 送审完整候选**

The piano chapters support conclusions about the tested piano datasets and targets. Chapter 6 extends the supervision strategy to guitar, where the evidence concerns renderer-conditioned velocities and loudness agreement rather than recovery of captured physical velocity labels. Voice, bowed strings, and wind instruments were not evaluated. Their sustained dynamics and continuous controls would require suitable target coordinates and descriptors beyond the attack-focused PHE/OSF pair used here.

**C1 短稿**

> The recovery framework may transfer more widely than the current estimator has been validated.

未直接采用：重要区分，略抽象需具体instrumentlist。

**C2 短稿**

> Instrument-appropriate targets should be chosen before applying the framework to continuous sounds.

未直接采用：与futurework衔接好，但应保留实际piano/guitar结论。

**C3 送审完整候选**

What can transfer beyond piano is the recovery framework: specify the trusted notes, choose an editable dynamics coordinate, and match the supervision to that coordinate. The empirical evidence is narrower. It covers piano and the tested guitar adaptation, not a validated instrument-general estimator. For voice, bowed strings, and wind instruments, onset intensity alone cannot describe the sustained and continuously shaped aspects of dynamics, so the target and comparison features would need to be reconsidered.

**本轮取舍**：推荐 B。B直接点名examiner列的四类并区分principletransfer与performancevalidated。A最短，C很好衔接中心论点但对新乐器的目标设计论述略多。没有把guitar r当canonicalvelocityaccuracy。

## R2-04 11位听者与8段刺激是补充证据，避免 definitive validation

**A1 短稿**

> The listening test complements the objective results.

未直接采用：最小限定有效，但缺人数和刺激。

**A2 短稿**

> The evidence is limited to 11 listeners and eight selected excerpts.

未直接采用：清楚，renderer与composer分组范围还需说。

**A3 送审完整候选**

The listening test provides complementary evidence for the objective results. With 11 expert listeners and eight selected excerpts, it supports the perceived benefit of velocity completion in this setting rather than definitive perceptual validation across listeners and repertoire.

**B1 短稿**

> The study supports the comparison in one rendering configuration.

未直接采用：补单renderer边界，缺对listener/repertoire的外推限制。

**B2 短稿**

> The composer groups are descriptive rather than controlled stylistic conditions.

未直接采用：与R1-16一致，但不能单独回答样本规模。

**B3 送审完整候选**

The listening evidence is limited to 11 expert listeners, eight selected excerpts, and one rendering configuration. It supports the objective comparison within that setting, but does not establish perceptual validity across the wider repertoire, listener population, or synthesis systems. The composer-group scores are descriptive and should be read with the same limitation.

**C1 短稿**

> The test shows a benefit on the selected stimuli rather than a population-wide estimate.

未直接采用：叙述平顺，避免“shows”仍过强，最终稿用supports。

**C2 短稿**

> Objective and perceptual evidence are complementary within their stated evaluation scope.

未直接采用：总体收束合适，须加具体样本条件才非套话。

**C3 送审完整候选**

The improvement over the selected baselines is supported by both note-wise metrics and this small reference-based listening study. The perceptual result is evidence that the velocity layer matters for the tested stimuli, not a population-wide estimate of musical naturalness. Broader listener and repertoire coverage would be needed before making that stronger claim.

**本轮取舍**：推荐 B。B覆盖人数、刺激与renderer三条现存限制，不新增实验。A最小，C叙述好但“matters”略抽象。保留作者结果价值，不把modest改写成无效。quantisation不在此抢先定论。

## R2-05

单一事实纠错、保留或合并项；不机械凑多稿。前三处是实际措辞／语法问题，最后一处是可核验时间解释。Figure2.3标题与其他排版问题须先看现存PDF页面再定，不能把PDF抽取换行自动当LaTeX缺陷。
