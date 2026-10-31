# Draft revision report for GRS

Candidate: Zhanhong He  
Thesis: *Recovering Musical Dynamics for Expressive Automatic Music Transcription*

**内部初稿，尚不可提交。** 本稿只描述拟答复和拟改动，未声称已经完成修改。GRS 专用模板／提交格式【待核验】；正式修订基线【待作者确认，见 DECISIONS.md】；最终页码【待核验】。Report 1 为 Dr Emmanouil Benetos；Report 2 在正文中未确认署名，本稿仅用 Examiner 2，不凭 PDF metadata 指定身份。

**英文均为待决定的说明稿；依赖实验事实的 Q/P 等分支还须先满足各自核验条件。** 本轮未修改正文，英文不预写“已改好／已检查最终 PDF”。最终定点核验已通过，39项文字可供作者选择，4项事实待核；这不表示作者批准或已执行。跨项来源核验继续保留。内部核验记录仅放中文栏，作者旧回复与编辑提案分开。批准只读取 [DECISIONS.md](DECISIONS.md)。

**新增可选补充：** [全文语境补充](SUPPLEMENTS_v4.md)经独立文字复核，分别在R1-09／06／04补充栏选择；不扩大原批准范围。R1-35另有KEEP原caption／原图。下方原英文仍为条件草稿，只有实际选定／实施或确认保留后，才按真实差异定稿。

## Proposed opening

> I thank both examiners for their careful reading and constructive comments. The responses below explain the research choices and the clarifications proposed for this minor revision.

【待决定】【待修改】【待核验】当前没有正文实施。待实际改动并逐项核验后，再按真实差异写正式完成式。当前较新 PDF 已有内容单独记归属，不能计作本轮新做，也不能遗漏正式基线到最终稿的真实差异。

## Existing differences requiring baseline confirmation

当前 main.pdf／源码已包含相对 Z_He_PhD_Thesis.pdf 的一些实质性差异。它们在本轮第三编辑开始前已存在；本稿既不把它们算成本轮新做，也不退回或丢弃。正式送审基线确认后，如这些差异属于正式返修，仍应依据真实前后版本纳入最终 revision report，不能因当前源文已解决问题就写“无修改”。本表是状态记录，不是新增 examiner 要求。

| 已有差异 | 当前工作源文状态与定位 | 本轮归属／后续处理 |
| --- | --- | --- |
| Ch4 Recall protocol | `Chapter_4/chap4.tex:169–174` 区分本 thesis 固定 MIDI-scale Recall10%、外部 Recall 与 velocity-aware transcription protocol | 早前已有；正式基线【待确认】，最终差异【待核验】 |
| Ch4 external baseline metrics | `Chapter_4/chap4.tex:246–279` 分开来源协议，不把未经核实或不兼容的 Recall 数字填入同列 | 早前已有；保留当前修正，不能当本轮新做，也不能误写为完全没变 |
| Ch5 ANN／CCI | `Chapter_5/chap5.tex:198`、`251–265` 区分 CCI 与 F1，并未将旧草稿未核实 ANN 29.4% 放进 dynamics-F1 列 | 早前已有；不恢复旧数，不新增实验；对应正式 revision 状态【待基线核验】 |
| Ch4 prior-work misalignment claim | `Chapter_4/chap4.tex:302` 说明自身 shifted-score conditioning／post-processing，避免将差异归因于早前工作的未记录实现 | 早前已有；保留已收紧表述，正式报告按基线实际差异填写 |

文字差异证据见 `evidence/existing_pdf_text_difference.diff`（保留在原目录，未收入精简ZIP） 和 [SOURCES.md](SOURCES.md)。当前源码只是提案工作坐标，未重新编译，不能据此保证与任一 PDF 逐字一致。

## Examiner 1

### R1-01

**Consider author-year citations for readability.**

**原报告位置：** Report 1, Introduction, citation-style suggestion；原报告物理页 1。[完整原话与原回复](COMMENT_MAP.md#r1-01)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

**保留数字制的拟答复，待作者选择：**

> Thank you for the suggestion. I propose to retain the existing numerical citation style consistently throughout the thesis.

**改为 author-year 的拟答复，待作者选择：**

> Thank you for the suggestion. I propose to adopt an author-year format for the citations and bibliography throughout the thesis.

【待决定】【待核验】两种立场均未选定；若采用切换方案，引用命令、bibliography style 与最终布局需统一核验。英文不预写已经完成检查。

**拟修改／保留说明：** 比较保留数字制与统一切换；采用前先看渲染效果，不自动改格式。

**工作定位：** `main.tex:49`（`citation style`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待决定】保留数字制或切换 author-year；未取得最终排版结果。

**关联决定：** [决定清单，查 R1-01](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-01)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-02

**Update the submitted ISMIR 2026 paper to accepted for publication.**

**原报告位置：** Report 1, Specific comments and questions, Preamble；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-02)。

**作者已记录立场：** 【作者未回复】；报告明确说已 accepted，目录中有 camera-ready paper。

**拟英文答复【待决定；说明稿，未执行】：**

> The ISMIR 2026 entry should read “Accepted for publication” rather than “Under review”. I propose to update that status in the authorship declaration.

**拟修改／保留说明：** 拟把第四篇论文更新为 accepted；不补未经核实的出版信息。

**工作定位：** `Declaration/author_declaration.tex:64`（`ISMIR publication entry`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验】最终书目信息；不影响 accepted 状态的提案。

**关联决定：** [决定清单，查 R1-02](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-02)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-03

**Figure 1.1 is presented as general AMT architecture but omits instrument identity and other expressive aspects.**

**原报告位置：** Report 1, Chapter 1, bullet 1（转写定位 1.1）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-03)。

**作者已记录立场：** 明确同意补 instrument identities 与其他 expressive aspects。

**拟英文答复【待决定；说明稿，未执行】：**

> The diagram is intended as a conceptual overview of AMT. Instrument identity, articulation and other instrument-specific controls belong to that broader view, while MIDI velocity and score dynamics are the targets studied in this thesis. I propose to show those additional outputs explicitly and highlight the dynamics branch as the thesis focus.

**拟修改／保留说明：** 在原图局部补 instrument identity／expressive aspects 并标明 dynamics 为本 thesis 焦点。

**工作定位：** `Chapter_1/Intro.tex:28`（`fig:intro_expressive_amt`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】需审实际图示及图注，而非只审文字承诺。

**关联决定：** [决定清单，查 R1-03](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-03)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-04

**Replace the ambiguous “recollecting” in the final paragraph of Section 1.1.**

**原报告位置：** Report 1, Chapter 1, bullet 2（转写定位 1.2）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-04)。

**作者已记录立场：** 明确同意 collecting。

**拟英文答复【待决定；说明稿，未执行】：**

> “Collecting” is the intended word. I propose to replace “recollecting” in this sentence and the corresponding use in the conclusion.

**拟修改／保留说明：** 改为 collecting，并检查结论同类用法；单项纠错。

**工作定位：** `Chapter_1/Intro.tex:32`（`sec:motivation`）；`Chapter_7/Conclusion.tex:148`（`ssec:conclusion:future_curation`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】明确纠错不需强凑 A/B/C。

【新增补充，另选】[动机末句](SUPPLEMENTS_v4.md#3-动机末句--r1-04)只收窄Intro:45末句承诺；原collecting修正与合并包范围不变。

**关联决定：** [决定清单，查 R1-04](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-04)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-05

**Define weakly expressive and weakly supervised music data.**

**原报告位置：** Report 1, Chapter 1, bullet 3（转写定位 1.3）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-05)。

**作者已记录立场：** 同意补定义；已给出表达简化与标签缺失／低质量的解释。

**拟英文答复【待决定；说明稿，未执行】：**

> In this thesis, weakly expressive data retain useful note structure but contain a simplified dynamics layer, such as constant or coarsely quantised velocities. Weakly supervised settings lack reliable direct dynamics labels and use indirect evidence for learning. These conditions describe the available information and can overlap.

**拟修改／保留说明：** 区分表达层被简化与监督标签不足，保留 default 64／粗量化例子。

**工作定位：** `Chapter_1/Intro.tex:112`（`sec:intro:question`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】粗量化不一概等于没有表达；定义不冒充通用术语标准。

**关联决定：** [决定清单，查 R1-05](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-05)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-06

**Could performance-audio-to-MIDI-velocity be an additional scenario, particularly for Chapter 6?**

**原报告位置：** Report 1, Chapter 1, bullet 4（转写定位 1.4）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-06)。

**作者已记录立场：** 坚持当前采用 score-informed 模型；未建立 audio-only adaptation。

**拟英文答复【待决定；说明稿，未执行】：**

> Chapter 6 uses performance audio together with aligned note events. It extends the score-informed S2 setting under missing target-domain velocity labels. Audio-only adaptation for MIDI velocity is a possible extension, distinct from S3, whose target is score dynamics rather than note-level velocity.

**拟修改／保留说明：** 澄清 Ch6 是 S2 的标签稀缺扩展；audio-only velocity adaptation 留未来。

**工作定位：** `Chapter_1/Intro.tex:123`（`tab:intro_scenarios`）；`Chapter_6/chap6.tex:89`（`ssec:bp:veloest`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验】作者“三倍 MAE”未有同协议证据，拟答复不采用该比值。

【新增补充，另选】[S3与guitar范围](SUPPLEMENTS_v4.md#2-s3与guitar范围--r1-06)只替Intro:118的S3句及153的scope bullet；R1-15尾句仍依原项选择。

**关联决定：** [决定清单，查 R1-06](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-06)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-07

**Must the perceptual level correspond through MIDI velocity, or can it link directly to score dynamics?**

**原报告位置：** Report 1, Chapter 2, bullet 1（转写定位 2.1）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-07)。

**作者已记录立场：** 强调 instrument／performer context 与对应关系的不确定性。

**拟英文答复【待决定；说明稿，未执行】：**

> The diagram is intended to describe related representations rather than a mandatory processing chain. Perceptual evidence can support score-dynamics estimation directly, without an intermediate MIDI-velocity estimate; Chapter 5 is an example. Instrument response, performance interpretation and musical context make these relations context-dependent.

**拟修改／保留说明：** 图注说明 many-to-many；直接回答 perceptual→score 可不经过 MIDI。

**工作定位：** `Chapter_2/Background.tex:18`（`fig:bg_dynamics_layers`）；`Chapter_2/Background.tex:22`（`sec:bg:dynamics:layers`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】同时回答 direct link 与非一一映射，避免只回复后者。

**关联决定：** [决定清单，查 R1-07](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-07)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-08

**Separate the three triplets of columns in Table 2.3 more clearly.**

**原报告位置：** Report 1, Chapter 2, bullet 2（转写定位 2.2）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-08)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> I propose to separate the three groups of columns more clearly in Table 2.3, using the same grouping of values.

**拟修改／保留说明：** 细分隔线或适度加组间距；单项排版提案。

**工作定位：** `Chapter_2/Background.tex:130`（`tab:bark_table`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验】执行后检查表格宽度与可读性。

**关联决定：** [决定清单，查 R1-08](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-08)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-09

**Does the statement that MIDI velocity is attached to a note onset always hold for the MIDI protocol?**

**原报告位置：** Report 1, Chapter 2, bullet 3（转写定位 2.3）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-09)。

**作者已记录立场：** 原批注仅 “Yes a true”；没有具体修订承诺。

**拟英文答复【待决定；说明稿，未执行】：**

> In the velocity-estimation chapters, the target is MIDI Note On velocity, attached to an individual note attack. This is narrower than the full MIDI protocol, which also supports release-related information and separate expressive controls. These chapters estimate one onset-velocity value per note rather than a continuous control trajectory.

**拟修改／保留说明：** 把目标限定为本论文的 note-on velocity；不扩大为所有 MIDI 控制。

**工作定位：** `Chapter_2/Background.tex:272`（`sec:bg:midi_velocity`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待决定】是否接受此精确限定；不把简短 Yes 扩为已批准。

【新增补充，另选】[前言定义同步](SUPPLEMENTS_v4.md#1-前言定义同步--r1-09)含八处Intro一致性操作；不从原R1-09 B继承YES，不把简短原批注当作作者已批准。

**关联决定：** [决定清单，查 R1-09](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-09)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-10

**Explain the colours in Figure 2.3(e) and (f).**

**原报告位置：** Report 1, Chapter 2, bullet 4（转写定位 2.4）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-10)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

**仅在统一颜色的提案版本实际完成并通过图示核验后适用：**

> A uniform colour for note events would remove the impression that colour encodes an additional variable. In that version, horizontal position indicates time, while the relevant vertical axes identify the event-lane index and MIDI pitch.

【待决定】【待修改】【待核验】这是对统一色方案的解释，不声称当前图已改。若保留原多色图，则仍需核对并解释其真实颜色语义。

**拟修改／保留说明：** 第一轮提案用统一颜色消除额外语义，并补轴说明；实际图示待审。

**工作定位：** `Chapter_2/Background.tex:446`（`fig:bg_temporal_units`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字复核通过；实施后仍待视觉核验】若选统一颜色提案，须审实际图示与轴标；若保留多色，仍需原图颜色语义。

**关联决定：** [决定清单，查 R1-10](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-10)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-11

**Define or replace “humanisation”.**

**原报告位置：** Report 1, Chapter 2, bullet 5（转写定位 2.5）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-11)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> Here, humanisation means adding or varying expressive controls in a symbolic sequence to move it away from a mechanically uniform rendering. The velocity-completion task in Chapter 3 has the narrower aim of changing velocity while preserving note content and timing.

**拟修改／保留说明：** 定义一般 humanisation，再限定 Ch3 velocity completion 只补 velocity。

**工作定位：** `Chapter_2/Background.tex:488`（`sec:bg:velocity:rendering`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不把一般 humanisation 定义成只改 velocity。

**关联决定：** [决定清单，查 R1-11](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-11)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-12

**Discuss crescendo and diminuendo in Section 2.6.1.**

**原报告位置：** Report 1, Chapter 2, bullet 6（转写定位 2.6）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-12)。

**作者已记录立场：** 【作者未回复】；Ch2 已有相关定义，拟避免重复。

**拟英文答复【待决定；说明稿，未执行】：**

> Crescendo and diminuendo describe gradual instructions over a span and are already introduced in Section 2.3.1. I propose a short cross-reference in Section 2.6.1, distinguishing these instructions from the static dynamic levels and change points estimated in Chapter 5.

**拟修改／保留说明：** 指向已有定义，并简述渐变记号与本研究离散目标的边界。

**工作定位：** `Chapter_2/Background.tex:261`（`sec:bg:dynamic_markings`）；`Chapter_2/Background.tex:526`（`sec:bg:scoredyn:loudness`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】可与 R1-38 共用范围说明，仍逐项回复。

**关联决定：** [决定清单，查 R1-12](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-12)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-13

**Clarify audio availability, the triangular symbol, performance versus reference MIDI and the 43% entry in Table 2.7.**

**原报告位置：** Report 1, Chapter 2, bullet 7（转写定位 2.7）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-13)。

**作者已记录立场：** 说明 performance MIDI 与 score 区别；43% 指 ATEPP 有 score 的 recording 比例。

**拟英文答复【待决定；说明稿，未执行】：**

> The intended distinction is between structural note annotations, velocity annotations, reference scores and audio access. Velocity annotations have different provenance across datasets, which needs to remain explicit in the row notes. I propose to clarify those columns and the triangular qualification symbol. The ATEPP 43% entry refers to score availability, rather than verified score-dynamics annotations.

**拟修改／保留说明：** 补音频可用性、列定义、符号图例与 43% 分母；逐数据集核验。

**工作定位：** `Chapter_2/Background.tex:599`（`tab:dataset_comparison`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 F04】各行 velocity annotation 区分 recorded／estimated／software-generated；43% 含义保留作者 score availability 说明，确切分母待核验，不能全表统称 measured velocity。

**关联决定：** [决定清单，查 R1-13](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮局部文字可选，完整项目事实待核](writer_round3.md#r1-13)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-14

**Define commonly used dynamics-prediction evaluation metrics in the background.**

**原报告位置：** Report 1, Chapter 2, bullet 8（转写定位 2.8）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-14)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> For a given class or event type, precision is TP/(TP+FP), recall is TP/(TP+FN), and F1 is their harmonic mean. Macro-F1 averages class-wise scores equally, whereas support-weighted F1 weights them by reference counts. Note-wise velocity MAE averages absolute error at reference note onsets. These definitions distinguish the principal measures used to interpret the dynamics results.

**拟修改／保留说明：** 补短定义与后文章节公式的交叉引用，不重复整套推导。

**工作定位：** `Chapter_2/Background.tex:877`（`sec:bg:dataeval:velocity`）；`Chapter_2/Background.tex:884`（`sec:bg:dataeval:scoredyn`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 V-05／F05】定义 macro 与 weighted 不等于已查明 Ch5 各表的实际 averaging；各结果仍须与最终 evaluator 对齐。保留不同 Recall 协议的区别。

**关联决定：** [决定清单，查 R1-14](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-14)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-15

**Reconsider “most controlled”: symbolic prediction without audio has less direct dynamics evidence.**

**原报告位置：** Report 1, Chapter 3, bullet 1（转写定位 3.1）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-15)。

**作者已记录立场：** 同意原词不准，意在说明输入信息较少。

**拟英文答复【待决定；说明稿，未执行】：**

> Scenario S1 fixes the symbolic notes and timing but provides no performance audio as input. Fixing the note structure limits what the model may change without uniquely determining the velocity profile. I propose to describe these information conditions directly in place of the ambiguous “most controlled” ordering.

**拟修改／保留说明：** 改为 fixed structure／symbolic-only evidence；同步相关排序。

**工作定位：** `Chapter_3/chap3.tex:11`（`sec:velcomp:overview`）；`Chapter_1/Intro.tex:112`（`sec:intro:question`）；`Chapter_7/Conclusion.tex:46`（`ssec:conclusion:ch3`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】需检查 problem setting、summary 与场景排序的同步。

**关联决定：** [决定清单，查 R1-15](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-15)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-16

**To what extent should velocity completion be style- or composer-specific?**

**原报告位置：** Report 1, Chapter 3, bullet 2（转写定位 3.2）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-16)。

**作者已记录立场：** 不做 style control；数据不足，已有听测 composer 分组。

**拟英文答复【待决定；说明稿，未执行】：**

> The model is not conditioned on composer or performer identity. Its aim is useful completion across the available piano repertoire rather than explicit style control. The composer groups in the listening study are descriptive: the selected excerpts were not balanced to isolate composer or style effects.

**拟修改／保留说明：** 区分风格控制与跨 repertoire 泛化；现有分组只作描述。

**工作定位：** `Chapter_3/chap3.tex:139`（`sec:velcomp:datasets`）；`Chapter_3/chap3.tex:451`（`sec:velcomp:discussion`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不纳入未公开 internship 经历或失败尝试作为正式证据。

**关联决定：** [决定清单，查 R1-16](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-16)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-17

**Justify or clarify “image-based”, since the method does not predict colour channels.**

**原报告位置：** Report 1, Chapter 3, bullet 3（转写定位 3.3）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-17)。

**作者已记录立场：** 愿用 image-like；colourisation 是二维矩阵处理类比。

**拟英文答复【待决定；说明稿，未执行】：**

> The representation is image-like because pitch and time form a regular two-dimensional grid processed by the U-Net. The output is a single-channel velocity roll. Colourisation is an analogy for completing the missing scalar layer, not RGB prediction; the formal published title retains its original wording.

**拟修改／保留说明：** 正文解释 image-like pitch–time matrices；保留已发表标题。

**工作定位：** `Chapter_3/chap3.tex:20`（`sec:velcomp:related`）；`Chapter_3/chap3.tex:46`（`sec:velcomp:representation`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验】attention window 术语另有实现冲突 E06，不随本项猜改数值。

**关联决定：** [决定清单，查 R1-17](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-17)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-18

**Justify piano rolls rather than MIDI-like note lists.**

**原报告位置：** Report 1, Chapter 3, bullet 4（转写定位 3.4）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-18)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> A piano roll exposes simultaneous notes and local pitch–time neighbourhoods on a regular grid, which suits the convolutional architecture used here. An event-list representation is a valid alternative but would require a different model interface.

**拟修改／保留说明：** 补二维局部／和声邻域与固定网格成本的具体取舍。

**工作定位：** `Chapter_3/chap3.tex:29`（`sec:velcomp:problem`）；`Chapter_3/chap3.tex:46`（`sec:velcomp:representation`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不补不存在的 event-based 对比结果。

**关联决定：** [决定清单，查 R1-18](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-18)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-19

**Is the Chapter 3 task velocity recovery or velocity estimation?**

**原报告位置：** Report 1, Chapter 3, bullet 5（转写定位 3.5）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-19)。

**作者已记录立场：** 训练时删除已知 velocity；部署时是 estimation。

**拟英文答复【待决定；说明稿，未执行】：**

> In Chapter 3, completion describes adding the missing velocity layer and estimation describes the prediction problem. Recovery describes the supervised reconstruction setting in which reference velocities are withheld. For new symbolic input, the output is a plausible expressive profile rather than a uniquely determined original performance.

**拟修改／保留说明：** 解释 recovery/completion 为任务设定，estimation 为模型行为。

**工作定位：** `Chapter_3/chap3.tex:29`（`sec:velcomp:problem`）；`Chapter_3/chap3.tex:49`（`sec:velcomp:matrix`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不机械把全文 recovery 换成 estimation。

**关联决定：** [决定清单，查 R1-19](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-19)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-20

**Could a musical-time, beat-aligned representation be preferable to physical time?**

**原报告位置：** Report 1, Chapter 3, bullet 6（转写定位 3.6）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-20)。

**作者已记录立场：** 倾向 physical time，担心量化损失；也希望适用于 AMT 输出。

**拟英文答复【待决定；说明稿，未执行】：**

> Physical time preserves the timings supplied with the input and allows use without a beat map. A beat-relative representation could add metrical context and need not discard expressive timing. The present study does not compare these alternatives, so I propose to explain the choice in terms of input compatibility.

**拟修改／保留说明：** 解释兼容未 beat-aligned 数据的选择，并承认未比较替代方案。

**工作定位：** `Chapter_3/chap3.tex:59`（`sec:velcomp:segmentation`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不把 musical time 与硬量化等同。

**关联决定：** [决定清单，查 R1-20](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-20)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-21

**Does evaluation on performance MIDI conflict with the envisaged composition use case?**

**原报告位置：** Report 1, Chapter 3, bullet 7（转写定位 3.7）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-21)。

**作者已记录立场：** 不认为冲突，称网上量化 MIDI 与听测支持；正文尚未交代该 timing preprocessing。

**拟英文答复【待决定；说明稿，未执行】：**

**Q：仅在记录确认听测输入经过 timing quantisation 后可用；不推定 reference 采用相同处理：**

> The composition use case is to add velocity while preserving the note content and timing supplied by the user. Performance MIDI provides captured velocity targets for training. The listening-test inputs were timing-quantised versions of the selected SMD excerpts, with velocity values removed before estimation. I propose to clarify this preparation in the listening-test protocol and distinguish this evaluation from a controlled comparison of timing representations.

**P：仅在记录明确确认听测输入保留 performance timing 后可用；当前不选定，也不据此否定作者原陈述：**

> The composition use case is to add velocity while preserving the note content and timing supplied by the user. Performance MIDI provides captured velocity targets for training. The listening-test inputs were derived from the selected SMD performances and retained their performance timing, with velocity values removed before estimation. I propose to clarify this preparation in the listening-test protocol and distinguish this evaluation from a controlled comparison of timing representations.

【待核验 V-02】Q／P 均未选定。作者“量化 MOS”陈述保留；需补齐 input 与 reference 的实际 timing preparation。captured velocity targets 与是否量化 timing 没有这里所声称的因果关系。记录未明时，仅前两句与拟澄清协议的末句可作说明稿，不能据此输出确定的另一种未量化协议。

**拟修改／保留说明：** 保留 composition 动机；量化听测断言待刺激记录核验。

**工作定位：** `Chapter_3/chap3.tex:139`（`sec:velcomp:datasets`）；`Chapter_3/chap3.tex:367`（`sec:velcomp:perceptual`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 V-02／E01／F02】保留作者 quantised MOS 陈述；补齐 input 与 reference timing preparation。Q/P 均未选，不从 captured targets 推导 timing 条件，不需要新增实验。

**关联决定：** [决定清单，查 R1-21](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮局部文字可选，完整项目事实待核](writer_round3.md#r1-21)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-22

**Present the baselines in a dedicated subsection with more detail.**

**原报告位置：** Report 1, Chapter 3, bullet 8（转写定位 3.8）；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r1-22)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> The baselines are Flat velocity, an available pretrained Seq2Seq model, and ConvAE re-implemented in the local training framework. ConvAE and U-Net share the stated local training procedure, while Seq2Seq retains its pretrained weights. I propose to collect these existing details in a dedicated subsection, preserving those differences in training and checkpoint sources.

**拟修改／保留说明：** 局部集中 Flat／Seq2Seq／ConvAE 的来源、训练与用法。

**工作定位：** `Chapter_3/chap3.tex:192`（`sec:velcomp:training`）；`Chapter_3/chap3.tex:239`（`sec:velcomp:results`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】基于既有训练说明，不补未经记录的配置。

**关联决定：** [决定清单，查 R1-22](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-22)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-23

**Discuss ecological validity of separating dynamics refinement from note transcription and the potential value of coupling them.**

**原报告位置：** Report 1, Chapter 4, bullet 1（转写定位 4.1）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-23)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> The modular design targets settings with trusted note events, such as aligned-score archives and performance feedback. This is a task boundary rather than a claim that notes and dynamics are independent. Joint modelling may allow the two forms of evidence to support one another; the present known-note evaluation does not measure gains in note detection.

**拟修改／保留说明：** 限定 aligned-score 应用；承认 joint learning 价值与未测 note F1。

**工作定位：** `Chapter_4/chap4.tex:37`（`sec:scoreinf:principle`）；`Chapter_4/chap4.tex:307`（`sec:scoreinf:discussion`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 E03】前端 frozen 与 jointly trained 的既有表述冲突，不在答复中预设。

**关联决定：** [决定清单，查 R1-23](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-23)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-24

**Motivate piano rolls relative to event-based representations in Chapter 4.**

**原报告位置：** Report 1, Chapter 4, bullet 2（转写定位 4.2）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-24)。

**作者已记录立场：** 强调实现便利；批注提 multi-scale，需与当前章方法区分。

**拟英文答复【待决定；说明稿，未执行】：**

> The score matrices provide a common pitch–time interface with the acoustic velocity map. The final Transformer then processes the known onset coordinates as note tokens, while the BiLSTM variant uses the dense frame sequence. The design combines a raster interface with event-centred correction rather than using dense piano rolls throughout.

**拟修改／保留说明：** 说明 score raster 接口与 onset-token Transformer 两层，不误称全程 dense roll。

**工作定位：** `Chapter_4/chap4.tex:65`（`sec:scoreinf:features`）；`Chapter_4/chap4.tex:82`（`sec:scoreinf:arch`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不把 Ch5 multi-scale 或未公开失败试验当 Ch4 依据。

**关联决定：** [决定清单，查 R1-24](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-24)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-25

**Explain whether the two loss components are balanced or require weighting.**

**原报告位置：** Report 1, Chapter 4, bullet 3（转写定位 4.3）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-25)。

**作者已记录立场：** 认为沿用 Kim2024 比例并已验证；SMC 提供稿 §3.3 明确记录 preliminary hybrid-vs-single-target comparison，支持曾作初步验证，但不等于完整 ratio sweep。

**拟英文答复【待决定；说明稿，未执行】：**

> In the stated objective, the frame-wise BCE and onset-wise L1 terms are averaged over their respective active positions and combined with equal relative coefficients. The hybrid formulation follows the cited score-informed work and is supported by the preliminary comparison with frame-only and onset-only alternatives reported in the SMC paper. Equal coefficients do not imply equal numerical loss or gradient magnitudes.

**拟修改／保留说明：** 说明书面 objective 中各自平均后的相对等权，保留 Kim 引用与 SMC preliminary comparison；不把问题扩大成万能最优比例。

**工作定位：** `Chapter_4/chap4.tex:131`（`sec:scoreinf:loss`）；`Chapter_4/chap4.tex:138`（`eq:scoreinf:loss`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 V-04】保留 SMC §3.3 的 preliminary comparison 证据；再核对实际 run 的 theta 与分支，不把初步比较升级为最优比例证明，不要求新 sweep。

**关联决定：** [决定清单，查 R1-25](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-25)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-26

**Define the experimental settings in Table 4.1 in the main text.**

**原报告位置：** Report 1, Chapter 4, bullet 4（转写定位 4.4）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-26)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> Table 4.1 varies the correction module and its score features. The onset-only condition uses the score onset matrix; onset-plus-frame adds the active-note matrix; onset-plus-frame-ex uses the onset-excluded frame matrix. The BiLSTM and Transformer rows distinguish dense frame-wise correction from onset-token correction. I propose to define these conditions together in the experimental protocol.

**拟修改／保留说明：** 定义 onset-only／onset+frame／onset+frame_ex，并区分 BiLSTM／Transformer。

**工作定位：** `Chapter_4/chap4.tex:187`（`tab:scoreinf_maestro`）；`Chapter_4/chap4.tex:65`（`sec:scoreinf:features`）；`Chapter_4/chap4.tex:82`（`sec:scoreinf:arch`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验】onset-only 输入维度；MAPS 结论的本章证据 E07。

**关联决定：** [决定清单，查 R1-26](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮局部文字可选，完整项目事实待核](writer_round3.md#r1-26)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-27

**Was the Chapter 5 output combined with note-based AMT to obtain a complete system?**

**原报告位置：** Report 1, Chapter 5, bullet 1（转写定位 5.1）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-27)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> For the score-facing markings in Chapter 5, integration would attach estimated dynamics to note content on a common metrical grid. Note-level velocity correction instead uses aligned note onsets. The chapter evaluates dynamics and metrical targets; those component evaluations do not establish complete integrated AMT performance or an improvement in pitch, onset or offset accuracy.

**拟修改／保留说明：** shared beat grid 只限 Ch5 score-facing markings；逐音 velocity 用 aligned onsets。是否曾拼接与是否测过 note-accuracy 增益分别记录。

**工作定位：** `Chapter_5/chap5.tex:32`（`sec:audiodyn_targets`）；`Chapter_5/chap5.tex:19`（`fig:audiodyn_workflow`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验】现有示例是完整集成输出还是概念性工作流；不猜测是否曾尝试。

**关联决定：** [决定清单，查 R1-27](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-27)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-28

**Explain why change points are modelled explicitly rather than only predicting levels at beats or downbeats.**

**原报告位置：** Report 1, Chapter 5, bullet 2（转写定位 5.2）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-28)。

**作者已记录立场：** 原回复只说明 dynamic markings 解码到 beat level。

**拟英文答复【待决定；说明稿，未执行】：**

> The separate change-point head gives transitions an explicit supervision target, instead of deriving boundaries only from changes in the predicted level sequence. It complements the beat-wise level output by modelling when a new dynamic region begins.

**拟修改／保留说明：** 分别解释 regime label 与 transition detection；两者都落 beat grid。

**工作定位：** `Chapter_5/chap5.tex:32`（`sec:audiodyn_targets`）；`Chapter_5/chap5.tex:93`（`ssec:audiodyn_post`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字复核通过；事实边界保留】说明显式 boundary supervision，不主张相邻 beat labels 无法导出边界，也不虚报 CP-head 独立消融收益。

**关联决定：** [决定清单，查 R1-28](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-28)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-29

**Explain the connection between beat and downbeat components in Figure 5.2 and the loss.**

**原报告位置：** Report 1, Chapter 5, bullet 3（转写定位 5.3）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-29)。

**作者已记录立场：** 两条批注均保留：可更强连接；称只在 decoding 有连接。

**拟英文答复【待决定；说明稿，未执行】：**

**实现归属限定为已保留的 normal/default evaluation 路径，不代表全部最终表和 baseline 的 run 已核实：**

> Beat and downbeat predictions share the encoder and expert pool but retain separate heads and loss terms. In the normal evaluation path of the retained code, where predicted beats are available, the postprocessor snaps downbeats to those beats and removes duplicate positions. This is an output constraint rather than a learned cross-head consistency term in the training objective.

【待核验 V-05】首审 F08 核对了保留代码中 postprocessor 的默认建立与 normal 分支调用。最终每张表／各 baseline 所用分支仍需与实际 run 对应；作者两条批注继续保留。

**拟修改／保留说明：** 区分 shared encoder/experts、独立 heads/loss 与有条件 snap/dedup；最终 run 调用待核验。

**工作定位：** `Chapter_5/chap5.tex:77`（`ssec:audiodyn_mmoe`）；`Chapter_5/chap5.tex:100`（`ssec:audiodyn_loss`）；`Chapter_5/chap5.tex:93`（`ssec:audiodyn_post`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 V-05】写作窗已找到固定 beat_postproc.py 的有条件 snap/dedup；需确认最终评估 run 调用该版本，不把“源码存在”当成所有结果都已核实。

**关联决定：** [决定清单，查 R1-29](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-29)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-30

**Explain the value of cross-dataset evaluation given composer and performer dependence.**

**原报告位置：** Report 1, Chapter 5, bullet 4（转写定位 5.4）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-30)。

**作者已记录立场：** 意在检查泛化；承认没有 composer／performer 平衡数据。

**拟英文答复【待决定；说明稿，未执行】：**

**范围说明及当前书面规则的拟答复；不是表值溯源已核实的声明：**

> Cross-dataset evaluation tests the learned mapping under changes in repertoire, performers, recording conditions and annotation conventions. These factors vary together in the external corpora, so the experiment diagnoses combined corpus transfer rather than isolating a composer or performer effect. The current protocol description uses target-corpus F1 to select transferred checkpoints without fine-tuning; such selection produces a target-informed diagnostic rather than an estimate based on selection independent of target labels.

【待核验 V-05／F09】英文最后一句只准确归属当前书面 protocol，不能据此宣布现有表值来源、共同 fold 或 macro/weighted F1 已对齐。正式答复须依实际核实的选择规则定稿。

**拟修改／保留说明：** 保留 transfer diagnostic；披露 target-informed best-fold 与未隔离因素。

**工作定位：** `Chapter_5/chap5.tex:151`（`ssec:audiodyn_data`）；`Chapter_5/chap5.tex:326`（`ssec:audiodyn_cross_dataset`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 V-05／E04／F09】当前书面选择规则与最终表 provenance 分开。首审指出共同 fold 与 per-task maxima 的来源未对齐，macro／weighted 也待查；不能凭 disclosure 宣布已解决。

**关联决定：** [决定清单，查 R1-30](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮局部文字可选，完整项目事实待核](writer_round3.md#r1-30)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-31

**Reconsider the claim that analysis by synthesis and DDSP constitute a “simpler route”.**

**原报告位置：** Report 1, Chapter 6, bullet 1（转写定位 6.1）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-31)。

**作者已记录立场：** 愿将 simpler 改为 more efficient；保留方法立场。

**拟英文答复【待决定；说明稿，未执行】：**

> The intended advantage is access to supervision: real target audio can support adaptation without direct target-domain velocity labels. A differentiable synthesiser or proxy still has to be designed or supplied. I propose to state this supervision advantage directly in place of “simpler route”.

**拟修改／保留说明：** 用无需 target velocity labels 的准确动机替换比较性形容词。

**工作定位：** `Chapter_6/chap6.tex:19`（`sec:bp:related`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待决定】措辞与作者拟用 more efficient 有差别，理由是缺少成本比较。

**关联决定：** [决定清单，查 R1-31](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-31)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-32

**Distinguish V^(0) from V-hat in Section 6.4.1.**

**原报告位置：** Report 1, Chapter 6, bullet 2（转写定位 6.2）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-32)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> V^(0) denotes the intermediate coarse acoustic velocity roll, while V-hat denotes the score-refined values read at aligned note onsets for the rendering interface. The superscript does not identify a pre-adaptation checkpoint. The estimator architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen.

**拟修改／保留说明：** 保留原 acoustic 配置句、FFT／hop 等参数及 Ch4 引用，只补符号与 adaptation 范围的澄清；不删除后文所引用配置。

**工作定位：** `Chapter_6/chap6.tex:89`（`ssec:bp:veloest`）；`Chapter_4/chap4.tex:82`（`sec:scoreinf:arch`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】architecture unchanged 不等于 adaptation 时参数 frozen。

**关联决定：** [决定清单，查 R1-32](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-32)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-33

**Comment on the faithfulness of DDSP-Piano and DDSP-Guitar-Synth.**

**原报告位置：** Report 1, Chapter 6, bullet 3（转写定位 6.3）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-33)。

**作者已记录立场：** 已说明未单独测 reconstruction fidelity／velocity-gradient accuracy。

**拟英文答复【待决定；说明稿，未执行】：**

> The differentiable synthesisers used here are approximations whose timbre and velocity-to-sound response may differ from the target recordings. The observed degradation is consistent with acoustic mismatch but does not isolate the cause of the degradation. We did not separately measure reconstruction fidelity or velocity-gradient accuracy on the target recordings.

**拟修改／保留说明：** 沿用作者谨慎回复：consistent with mismatch，非证明原因。

**工作定位：** `Chapter_6/chap6.tex:96`（`ssec:bp:adapt_diffsynth`）；`Chapter_6/chap6.tex:508`（`ssec:bp:when_diffsynth`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不升级为已验证因果解释。

**关联决定：** [决定清单，查 R1-33](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-33)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-34

**Justify Huber distance rather than MAE.**

**原报告位置：** Report 1, Chapter 6, bullet 4（转写定位 6.4）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-34)。

**作者已记录立场：** 已明确优化动机、β=1 和没有 dedicated comparison。

**拟英文答复【待决定；说明稿，未执行】：**

> Huber loss is used with beta = 1 for smooth small-error behaviour and an L1-like penalty for larger PHE/OSF residuals. We did not conduct a dedicated comparison with MAE.

**拟修改／保留说明：** 解释 small-error smooth／large-error L1-like、β=1；承认无 MAE 专项比较。

**工作定位：** `Chapter_6/chap6.tex:114`（`ssec:bp:adapt_diffsfproxy`）；`Chapter_6/chap6.tex:123`（`eq:bp_param_loss`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】作为选择理由，不伪装消融结论。

**关联决定：** [决定清单，查 R1-34](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-34)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-35

**Show explicitly whether the right-hand training data in Figure 6.2 are rendered audio.**

**原报告位置：** Report 1, Chapter 6, bullet 5（转写定位 6.5）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-35)。

**作者已记录立场：** 【作者未回复】；当前图／图注已部分回答。

**KEEP原caption／原图的拟英文答复【待决定；事实说明，不声称新增】：**

> Figure 6.2 shows offline proxy training. Its caption identifies the teacher targets as PHE/OSF extracted from SoundFont-rendered audio.

**若另选原A的拟英文答复【待决定；说明稿，未执行】：**

> Figure 6.2 concerns offline proxy training. MIDI notes and velocities are rendered by the SoundFont, and PHE/OSF parameters extracted from that audio provide the teacher targets. Real performance audio is used in the later VeloEst adaptation stage, rather than to generate those offline targets. I propose to make the two stages explicit in the figure explanation.

**拟修改／保留说明：** 推荐KEEP现有caption／原图；原A仍可选。理由与准确原注见[定点复核后的KEEP说明](SUPPLEMENTS_v4.md#keep-r1-35)。NO原A不自动等于选择KEEP。

**工作定位：** `Chapter_6/chap6.tex:205`（`fig:bp_proxy_arch`）；`Chapter_6/chap6.tex:231`（`ssec:bp:proxy_training`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待决定】可保留现图；不得把当前已存在说明算作本轮完成修改。

**关联决定：** [决定清单，查 R1-35](DECISIONS.md)；批准值与KEEP／原A方案只读取该行；原A或NO不自动转换为KEEP。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-35)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-36

**Could SoundFont selection be automated rather than made by ear?**

**原报告位置：** Report 1, Chapter 6, bullet 6（转写定位 6.6）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-36)。

**作者已记录立场：** 认为可以自动化，但本轮留未来工作。

**拟英文答复【待决定；说明稿，未执行】：**

> Automatic SoundFont selection is a possible extension. The selected renderer affects the velocity coordinate, so a matching procedure should consider velocity response as well as timbral similarity. The present study uses the stated by-ear selection and does not evaluate an automated selection method.

**拟修改／保留说明：** 说明当前人工试听的主观性；自动选择列未来工作。

**工作定位：** `Chapter_6/chap6.tex:261`（`ssec:bp:soundfonts`）；`Chapter_6/chap6.tex:515`（`ssec:bp:limitations`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】不增加候选池规模、盲听流程或算法结果。

**关联决定：** [决定清单，查 R1-36](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-36)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-37

**Discuss integration into complete AMT and possible effects on transcription performance.**

**原报告位置：** Report 1, Chapter 7, bullet 1（转写定位 7.1）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-37)。

**作者已记录立场：** 认为集成可能；听感／客观指标效应仍是设想。

**拟英文答复【待决定；说明稿，未执行】：**

> The dynamics components could be integrated with note transcription, using aligned onsets for note-level velocity and a metrical grid for score-facing markings. Such a system would need evaluation of expressive usefulness alongside pitch, onset and offset accuracy. The component-level studies do not establish an improvement in those note-transcription measures.

**拟修改／保留说明：** 讨论接口与未来联合评估；不声称已改善 notes 或听感。

**工作定位：** `Chapter_7/Conclusion.tex:155`（`ssec:conclusion:future_amt`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】与 R1-23／27 共享边界，仍保留三处原问题的单独答复。

**关联决定：** [决定清单，查 R1-37](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-37)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R1-38

**Mention unstudied dynamics markings, such as crescendo, as future work.**

**原报告位置：** Report 1, Chapter 7, bullet 2（转写定位 7.2）；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r1-38)。

**作者已记录立场：** 明确同意补充。

**拟英文答复【待决定；说明稿，未执行】：**

> The score-dynamics model estimates the five static levels in its annotations and their change points. It does not explicitly represent crescendo, diminuendo or other gradual instructions as labelled spans. These are appropriate future targets because a change point alone does not specify a gradual instruction’s onset, duration and direction.

**拟修改／保留说明：** 短补未来工作；区分 discrete CP 与 explicit span/hairpin。

**工作定位：** `Chapter_7/Conclusion.tex:122`（`sec:conclusion:future`）；`Chapter_5/chap5.tex:397`（`ssec:audiodyn_limits`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】与 R1-12 共用概念边界，不重复大段背景。

**关联决定：** [决定清单，查 R1-38](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r1-38)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

## Examiner 2

### R2-01

**Make each technical chapter’s relation to the central question explicit under its data-availability condition.**

**原报告位置：** Report 2, Main strengths, embedded chapter-linking suggestion；原报告物理页 2。[完整原话与原回复](COMMENT_MAP.md#r2-01)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> The existing technical-chapter overviews identify the inputs, dynamics target and relation to the central question. I propose to retain those passages and make the local scope clarifications identified in R1-06 and R1-15, rather than add a second set of chapter introductions.

**拟修改／保留说明：** 第一轮提案保留现有 overview，只随 R1-06／15 作局部澄清；不预设新增四段，待独立复审。

**工作定位：** `Chapter_3/chap3.tex:11`（`sec:velcomp:overview`）；`Chapter_4/chap4.tex:6`（`sec:scoreinf:overview`）；`Chapter_5/chap5.tex:9`（`sec:audiodyn:overview`）；`Chapter_6/chap6.tex:6`（`sec:bp:overview`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】Ch6 保留 S2 的 label-scarce extension，不能改写成 audio-only velocity。

**关联决定：** [决定清单，查 R2-01](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r2-01)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R2-02

**Distinguish published contributions, adaptations and new thesis-level synthesis.**

**原报告位置：** Report 2, Main weaknesses and required minor revisions, paragraph 1；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r2-02)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> Chapters 3–6 are associated with the four co-authored studies listed in the Authorship Declaration. Across these studies, the thesis develops a common label-recovery formulation and scenario map, introduces shared background, and compares assumptions and limitations in Chapter 7. I propose to distinguish this organising synthesis from the technical methods attributed to the individual studies.

**拟修改／保留说明：** 用四篇 paper→chapter 映射和短说明区分技术来源与 thesis synthesis。

**工作定位：** `Chapter_1/Intro.tex:157`（`sec:intro:contrib`）；`Chapter_1/Intro.tex:175`（`sec:intro:organisation`）；`Declaration/author_declaration.tex:1`（`publication entries`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 V-07】ICASSP 提供稿 p4 有 PENDING THIS PART／no yet，p5 表格待替换，且标题与 declaration 不同。需最终发表版本或作者说明本稿用途；当前只作方法／题名参照，不能确定 Ch5 逐结果的 published／thesis-new 归属。此项英文仅在最终映射核验后可用。

**关联决定：** [决定清单，查 R2-02](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r2-02)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R2-03

**Clarify which conclusions transfer beyond piano, including guitar, voice, bowed strings and wind instruments.**

**原报告位置：** Report 2, Main weaknesses and required minor revisions, paragraph 2；原报告物理页 3。[完整原话与原回复](COMMENT_MAP.md#r2-03)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> The empirical evidence concerns the tested piano datasets and exploratory guitar adaptation. The real-audio guitar adaptation evaluation concerns renderer-conditioned velocities and rendered-loudness agreement rather than comparison with target-domain MIDI velocity labels. Voice, bowed strings and wind instruments were not evaluated; their sustained and continuous controls may require different dynamics targets and descriptors beyond the attack-focused PHE/OSF pair.

**拟修改／保留说明：** 集中区分已测 piano/guitar 与未测连续控制乐器；补 voice。

**工作定位：** `Chapter_6/chap6.tex:515`（`ssec:bp:limitations`）；`Chapter_7/Conclusion.tex:107`（`sec:conclusion:limitations`）；`Chapter_7/Conclusion.tex:141`（`ssec:conclusion:future_instruments`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 E02】吉他图所谓 ground truth 来源；未核实前不用于证明跨乐器准确率。

【只作交叉引用】前言定义／guitar范围补充只在R1-09／06补充栏决定；不新增重复批准入口，不关闭GT与run核验。

**关联决定：** [决定清单，查 R2-03](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r2-03)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R2-04

**Present the 11-expert listening test as supporting evidence, not definitive perceptual validation.**

**原报告位置：** Report 2, Main weaknesses and required minor revisions, paragraph 3；原报告物理页 4。[完整原话与原回复](COMMENT_MAP.md#r2-04)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> In the listening study, 11 expert listeners rated eight selected SMD excerpts rendered with one PianoTeq configuration for similarity to the human-performed MIDI rendering reference. The higher ratings for U-Net than for Flat and ConvAE support the objective comparison within this setting. This is supporting perceptual evidence for the selected stimuli and renderer.

**拟修改／保留说明：** 集中说明 11 人／8 片段／单 PianoTeq；写明所测 reference similarity，并保留 U-Net 优于 Flat／ConvAE 的所选材料结果。

**工作定位：** `Chapter_3/chap3.tex:367`（`sec:velcomp:perceptual`）；`Chapter_3/chap3.tex:451`（`sec:velcomp:discussion`）；`Chapter_7/Conclusion.tex:46`（`ssec:conclusion:ch3`）。最终 thesis 页码【待核验】。

**核验缺口：** 【待核验 E01】不把 timing-quantised 刺激当已证实；同时对照摘要和 Ch1 claims。

**关联决定：** [决定清单，查 R2-04](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r2-04)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

### R2-05

**Correct minor English, formatting and presentation defects, including genuine line-break artefacts.**

**原报告位置：** Report 2, Main weaknesses and required minor revisions, paragraph 4；原报告物理页 4。[完整原话与原回复](COMMENT_MAP.md#r2-05)。

**作者已记录立场：** 【作者未回复】。

**拟英文答复【待决定；说明稿，未执行】：**

> I propose to correct the identified local phrasing and presentation issues, including the listed grammar errors and the description of segment duration in relation to bars. A segment’s length in bars depends on tempo and metre, so a fixed duration should not be equated with a fixed number of measures.

**拟修改／保留说明：** 仅列实际源码／渲染可证缺陷，逐项修正，不全篇润色。

**工作定位：** `main.tex:1`（`active thesis source and final PDF`）。最终 thesis 页码【待核验】。

**核验缺口：** 【文字可供选择；相关核验保留】【待核验】需实际缺陷清单与最终编译后逐项核对。文本抽取产生的断行不计作 thesis 缺陷；此内部识别规则不进入正式英文答复。

【只作交叉引用】动机末句是R1-04新增补充，不在原proofreading或合并包批准范围内。

**关联决定：** [决定清单，查 R2-05](DECISIONS.md)；批准值与版本只读取该行。候选【[第三轮文字可供选择，未批准／执行](writer_round3.md#r2-05)】；实施【待修改】；实际差异／完成证据【待填写】；复核【待核验】。

## Other examiner observations

【内部整理】正面评价、评价标准与 examiner 建议集中致谢，不额外生成正文修改任务；嵌入的修改要求和重复总结仍对应上方逐项答复。此说明不进入正式英文 report。

> I am grateful for the examiners’ positive assessment of the contribution, organisation, methodological choices and presentation. The proposed revisions focus on the requested clarifications and presentation changes.

| 原报告范围 | 处理 | 关联 |
| --- | --- | --- |
| Report 1 Introduction | 总体肯定致谢；其中引用格式和发表状态分别回复 | R1-01、R1-02 |
| Report 1 six merit criteria | 致谢；无额外正文改动提案 | COMMENT_MAP R1-G03–G08 |
| Report 1 Overall recommendation／signature | 保留作为报告流程结论；不改写为学校最终决定 | COMMENT_MAP R1-G09 |
| Report 2 opening／six criteria | 致谢；无额外独立修改项 | COMMENT_MAP R2-G01–G03 |
| Report 2 Main strengths | 保留评价；嵌入的 chapter-linking 建议已单列 | R2-01；R2-G04–G07 |
| Report 2 Overall remarks | 致谢；不据此扩大技术结论 | COMMENT_MAP R2-G08 |
| Report 2 Recommendation／repeated four requests | recommendation 如实保留；重复要求回指四项，无重复动作 | R2-02–R2-05；R2-G09–G13 |

## Completion fields

本稿不承担用户选择录入。正式 report 的每个项目，须从 DECISIONS.md 读取决定，再根据真实差异填写实施日期、最终位置和核验结果。未改动项目填写有依据的 no-change response；NO 后需重写时继续保留待处理状态。

Submitted revision baseline【待确认】；revised thesis file【待修改后填写】；final page references【待核验】；supervisor／GRS format requirements【待核验】；actual completion date【待填写】。
