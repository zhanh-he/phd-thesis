# 独立审查基线

日期：2026-10-31。角色：第二聊天的独立审查者。本文件形成前，没有阅读写作聊天的候选、推荐或提案文件。这里判断的是源材料与作者回复；尚未审查任何 A/B/C 候选，不代表作者批准，也不代表修改已执行。

核心判断：这是以澄清为主的 minor revision。应保留现有章节结构、研究定位、数据和实验。最需要修的不是整篇语言，而是少量定义、图表说明、贡献归属和证据边界。几处事实冲突须先核验，不能用流畅措辞覆盖。

## 材料与版本

仅使用 `/Users/jollibear/Documents/tmp/phd thesis/` 中的材料及 `publish_paper/`。未读 otherfiles。未修改 thesis、作者回复、参考文献或图片；未编译源项目、运行实验、提交 Git、推送或提交 GRS。

| 材料 | 独立核对结果 | 本轮用途 |
| --- | --- | --- |
| 当前 `main.tex` 与七章 `.tex`、`Declaration/author_declaration.tex` | 当前可编辑源文；大量章节末总结和开头定位已存在 | 候选定位依据；不是已经获用户指定的最终提交基线 |
| `main.pdf` | 155 个物理页；PDF 元数据创建及修改时间均为 2026-10-31 01:39:13 UTC | 较新的现存渲染件；已核对若干源码特征与关键图表页 |
| `Z_He_PhD_Thesis.pdf` | 154 个物理页；元数据创建时间 2026-05-25 23:14:10 UTC、修改时间 23:20:18 UTC | 较早现存 PDF；不可把页码与 main.pdf 混用 |
| 报告 1 PDF | 4 页，正文日期 24 September 2026；25 条 Highlight 回复，各另有 Popup，不能当成 50 条不同回复 | examiner 原话和作者立场的主要证据 |
| 报告 2 PDF | 4 页，无 PDF 回复批注 | 其明确要求是 minor revisions，不要求新增实验、数据收集或大改写 |
| 两份 `README_Preliminary_Report_*.md` | 是报告与回复的可检索转写；其中 `zhanhong not response yet` 为整理时占位符 | 方便逐项索引；空白不代表同意，也不代表拒绝 |
| 四篇 paper PDF | CMMR 12 页、SMC 8 页、ICASSP 6 页、ISMIR 8 页；标题与四个技术章一一对应 | 次级语言与发表内容参照；不取代 thesis 本身 |

`README.md` 明确说两个 thesis PDF 尚未指定哪个是基线，也未验证源码与哪份完全一致。独立文本比较确有差异，例如新 PDF 的第 4 章区分外部 Recall 与固定尺度 Recall10%，第 5 章去除了未核实的 ANN F1。不能把这些既有差异称作“本轮已完成的修订”。本轮没有重新编译，故不能声称 main.pdf 与当前全部源码逐字一致。

关键文件 SHA-256：

- main.pdf：`8cb8dbe9d560980e003148e442cdeae53e7a97495dcee695b8a58df9a0719bb8`
- Z_He_PhD_Thesis.pdf：`cbfcfca09364f85a7f6fcef186114054bfa8c494a87d26271091911a9064de07`
- main.tex：`a55546f7a41c9210f1ecebae71a2167f86e0fb93ddbf96797ba03c1ea270fd39`
- Chapter_3/chap3.tex：`d8d6034e98d8b62fd91ee51652663aedb417d565bdbcd220518a95fb0e3c49c9`
- Chapter_4/chap4.tex：`d3ba02f332041ea4e6e8c89fe342fdf560bd9edda1caafcd4b7c9fb651226eb8`
- Chapter_5/chap5.tex：`60219fbeac5ebb0d2e70be7de2bbf6028c1e1916bf35c3626f0b5d872432e6fe`
- Chapter_6/chap6.tex：`d871241adb95f5d88099d67a4dd01b584b4b004875b8e425fbbc7550c25e32bf`

未从执行环境核实本聊天实际模型名称及 reasoning effort，因此不宣称已使用 Ultra，也不宣称跨模型独立性。独立性来自先读原始材料、隔离候选推荐的工作顺序。

## 作者语言与不应破坏的结构

写作判断主要来自 thesis 的章节 3–6 方法、实验、讨论段落，次级参照四篇 paper。作者现有的有效表达是：先说明任务和可用输入，再解释具体设计为何匹配目标，最后给出数据内成立的结论及边界。应保留 `note-level MIDI velocity`、`score-informed correction`、`beat-synchronous score dynamics`、`renderer-conditioned`、`aligned note events` 等稳定术语。

可保留的语言特征与源证据：

- 技术过程用直白的主语和动词。例如第 4 章“the module adjusts how loudly a note is played”，接着说明它不决定音符是否存在；候选宜继续解释任务边界，不添加口号。
- 适度使用 we 解释实验选择。第 6 章 Huber、renderer 与 label scarcity 的论述有条件性，应继续写明采用了什么、测了什么、没有测什么。
- 准确区分 representation。第 2、5、6 章以及结论都避免把 loudness、velocity、dynamic markings 当成同一物理量，这条主线应保留。
- 原论文标题中的 `Image Colorizer`、既定 paper 标题和方法名属于发表记录，不能为了统一正文术语而改写其正式标题。

不应机械模仿的现稿问题：`omnipotent dataset`、`entirely bypass`、`innovatively` 等过强表述；反复使用“the deeper thesis result”“not only...”“the main result is therefore...”的总结节奏。它们在现稿出现，不等于每段新增文字都应复制。也不应大面积替换现稿来追求一种统一的 AI 文风。

以下内容本身有效，应以“保留／引用已有段落”为优先候选：四个技术章开头与结尾的定位；第 6 章 renderer-conditioned 定义；第 5 章 score dynamics 与 MIDI velocity 区别；第 5 章既有 crescendo/diminuendo 限制；第 6 章承认 Diff-Synth 在匹配条件下仍有价值。新段落应填缺口，不重复这些内容。

## 先解决的证据冲突

这里的 E 编号是审查风险编号，不是新增 reviewer 意见。不要把它们伪装成 examiner 原话。

| 风险 | 直接证据 | 独立判断与允许的处理 |
| --- | --- | --- |
| E01 听测是否量化 | 作者对 R1 原 3.7 的回复称 MOS 用了 quantised score-MIDI；`chap3.tex` 375–380 行写八个 SMD 演奏 MIDI 片段去掉 human-performed velocity，原 CMMR paper 的 Stimuli 段也如此 | 不能仅凭正文省略量化步骤就否定作者说明：SMD performance MIDI 也可能经过量化。保留作者当前说明的来源归属，核对实际刺激输入与预处理记录；在完成前不写“必定量化”或“必定保留演奏时值”，也不称已作受控 quantised-vs-performance 对比 |
| E02 吉他图的 GT 来源 | `chap6.tex` 442–447 行及 main.pdf 物理页 130／印刷页 103 称图 6.3 为 guitar excerpt with ground-truth velocities；本章多处又说 GAPS/FL 没有真实 velocity 标签；原图写 GT MIDI Notes + Velo，但未写数据集 | 是事实来源问题。先核对实际片段 ID／绘图脚本／生成记录；不能直接改称 piano，也不能改称 synthetic guitar，二者都尚未证实。来源不明时可提出删除该图中关于真实 GT 的证明性解释，仍须作者决定 |
| E03 第 4 章前端冻结与联合训练 | `Background.tex` 511 行称 frozen AMT front-end；`chap4.tex` 162 行说 baseline 与包括 correction module 的 jointly trained counterpart；第 6 章又有“fixed black-box front-end whose checkpoint is then adapted” | 区分 architecture unchanged 与 parameters frozen。候选不得把前者写成后者。第 4 章按实际训练记录统一；第 6 章应明确 VeloEst 更新、两类监督后端冻结，这一点本章已有直接说明 |
| E04 第 5 章 target-informed fold selection | `chap5.tex` 187、330 行：在外部目标 corpus 上按最佳 dynamic F1 选 fold，single-task 各任务分别选最佳 fold；同时称 test-only、stricter transfer | 无 fine-tuning 不等于目标标签未参与选择，应说明 best-fold 选择的乐观性。补充算术核对：当前表5.4的32个显示值全部等于保留输出的各任务最大值，只有22项匹配正文所写selection rule；表值来源与聚合方式须核验。不得据此自行改表，也不要求新增实验 |
| E05 三倍 MAE | R1 原 1.4 作者回复称 hFT MAE 约三倍；现稿表 4.2 的 SMD hFT=9.9、Score-HPT=8.0，未支持此比值 | 保留作者“本研究选择较强 score-informed 初始化”的立场，但不复制三倍数字；除非有清楚的同协议证据 |
| E06 1×1 window 与 global attention | `chap3.tex` 93–100 行把 n×n 说成 local window size；356 行却称 1×1 window attention 即 global attention | 两种参数含义不一致。要按实际实现核对是 window size、window count 还是 partition count；不能凭常识直接把既有消融标签改成另一个数值 |
| E07 MAPS 的叙述范围 | 第 4 章 Summary 321 行称 SMD/MAPS generalisation，但当前实验与结果正文主要列 MAESTRO/SMD；SMC paper 的摘要确提 MAPS | 已发表 paper 的说法不自动变成本 thesis 已展示的结果。候选宜限定当前章实际展示的数据，或给出现有 MAPS 结果确切位置，不新增实验 |

这些冲突不说明实验无效；它们限制的是可在修改文字和 GRS report 中使用的确定性。正式答复不得用“We have verified...”掩盖尚未核验的来源。

## 报告 1 逐项基线

下表编号按“总体 citation 建议、preamble、再按各章项目”顺序定义，共 38 个可处理项目。`原项` 是两份 README 转写中的章内项目号（PDF 为按章排列的 bullets），用于与写作清单交叉核对。若协调者已有不同 canonical ID，请以原项做一次明确 crosswalk，不能静默覆盖或漏项。所有作者决定仍为【待定】；“建议”只是审查判断。

| ID | 原项与定位 | 作者现有立场 | 独立判断与最小必要处理 |
| --- | --- | --- | --- |
| R1-01 | Introduction citation style；`main.tex:49`、`main.tex:175` | 未回复 | author-year 是建议而非硬性要求。保留 numeric 可成为选项；若选择切换须统一 natbib／bibliography 并后续渲染复核，不能把全论文格式重做当成自动接受 |
| R1-02 | Preamble，ISMIR status；`author_declaration.tex:64` | 未回复 | examiner 已明确 accepted，且有 camera-ready PDF。提出把 Under review 改为 accepted；未核实正式 proceedings 前不要编页码、DOI或正式出版状态 |
| R1-03 | 1.1 Fig 1.1；`Intro.tex` → `fig:intro_expressive_amt`；AMT.png | 同意补 instrument identity／其他 expressive aspects | 图仍只画 dynamics/velocity。优先按作者已有立场局部补图，再用 scope 说明保留 dynamics 重点；仅缩窄 caption 应明确为与作者当前计划不同的备选，不能预设采用；避免承诺完整表达建模 |
| R1-04 | 1.2 Motivation 末段；`Intro.tex:45` | 同意 collecting | 直接改单词；结论 150 行也有 recollecting，需同步核对。无需 A/B/C |
| R1-05 | 1.3 research question；`Intro.tex` → `sec:intro:question` | 同意补 weakly expressive／weak supervision 定义 | 应区分表达层简化与标签监督不足，保留作者 default 64／粗量化例子；不把全部 8 级量化一律判成无表达，也不将 weak supervision 等同一个技术范式 |
| R1-06 | 1.4 Table 1.2；`Intro.tex` → `tab:intro_scenarios`；第6章 `ssec:bp:veloest` | 现阶段做 S2，audio-only velocity adaptation 留未来 | 同意保留 S1/S2/S3，不新增未做 scenario。加一句第 6 章延伸 S2 的标签条件，audio-only velocity 是不同于 S3 score-dynamics 的可研究方向。禁用未核实三倍 MAE；global shift 稳定不等于任意错音或alignment稳定 |
| R1-07 | 2.1 Fig 2.1；`Background.tex` → `fig:bg_dynamics_layers`、`sec:bg:dynamics:layers` | 强调 instrument／performer context 与不确定性 | 尊重 many-to-many 立场，同时直接回答：perceptual evidence 可直接用于 score-dynamics，不必经过 MIDI。图不是必须串行经过 velocity 的 pipeline；第 5 章就是实例。文字已有不等价论述，可改图注／加一句，不重写背景 |
| R1-08 | 2.2 Table 2.3；`Background.tex` → `tab:bark_table`；main.pdf 印刷 p14 | 未回复 | 实际已有组间空隙，但三组仍较近。加两条细分隔或增加组间距均可；按 examiner 意见采用细线即可，不必三方案 |
| R1-09 | 2.3 MIDI protocol；`Background.tex` → `sec:bg:midi_velocity`（274行） | 回答 Yes | 用精确目标 `note-on velocity` 保留作者本意。不要把“本论文的 velocity 目标在 onset”扩成“MIDI 所有动态控制都只有 onset”；连续控制与其他事件不能因此被否认 |
| R1-10 | 2.4 Fig 2.3(e)(f)；`Background.tex` → `fig:bg_temporal_units`；main.pdf 印刷 p25 | 未回复 | 图注没有解释蓝绿颜色。须先核对画图源数据/色彩映射；不能猜成 pitch、velocity、instrument 或 note identity。若色彩无数据语义，可明确 purely visual distinction，但这也需核实 |
| R1-11 | 2.5 humanisation；`Background.tex` → `sec:bg:velocity:rendering` | 未回复 | 定义一次：在符号音符基础上加入演奏式变化。再说明本章 narrowing to velocity，不把一般 humanisation 定义为只改 velocity |
| R1-12 | 2.6 crescendo/diminuendo；`Background.tex` → `sec:bg:dynamic_markings`、`sec:bg:scoredyn:loudness` | 未回复 | 2.3.1 已定义两词与 hairpins，且解释 span。可以保留这段，在 2.6.1 增一个交叉指向，说明模型只估静态等级与 change points；不重复一段基础知识 |
| R1-13 | 2.7 Table 2.7；`Background.tex` → `tab:dataset_comparison`；main.pdf 印刷 p35 | MIDI=unquantised performance，score=quantised；43%=有 score 的比例 | 现稿已扩 MIDI 到 GuitarSet 可转 note annotation，与回复中的严格定义不完全相同；有 ATEPP 自动转写与 MID-FiLD 软件数据，不能全表宣称 human-performed MIDI。需 column glossary、Audio列或清楚的音频可用性说明、三角符号通用图例、43% 分母与含义。不要声称所有数据可直接获取；表已拥挤，排版实施时复核 |
| R1-14 | 2.8 metrics definitions；`Background.tex` → `sec:bg:dataeval:velocity`、`sec:bg:dataeval:scoredyn` | 未回复 | 增简明定义＋指向后文公式足够：note-wise MAE/dispersion/tolerance recall、classwise macro-F1、loudness correlation。不得把不同来源 Recall 或 CCI 混作当前指标；现稿已有仔细区分，应保留 |
| R1-15 | 3.1 most controlled；`chap3.tex:13`、`chap3.tex:31`、`chap3.tex:465`；`Intro.tex:118`；结论 `ssec:conclusion:ch3` | 接受措辞问题，意在 less input signal | 应区分 fixed note structure 与 less observable evidence，取消“更易／更有约束”的含混排序。不要只改一处；保留结构固定这个正确条件，避免称为完全 unconstrained generation |
| R1-16 | 3.2 composer/style；`chap3.tex` → `sec:velcomp:datasets`、`tab:velcomp_mos`、`sec:velcomp:discussion` | 不做风格控制，数据不足；已有 composer分组 | 可补局部讨论，区分 conditional style control 与 generalisation。8段／11人分组只是 descriptive，不能称因果风格实验或严格 composer-balanced design。Dolby内部经历／未公开失败不自动写进学术正文 |
| R1-17 | 3.3 image-based；`chap3.tex` → `sec:velcomp:related`、`sec:velcomp:representation` | 建议 image-like，二维矩阵不是RGB | 同意澄清 analogy，保留二维卷积／pitch-time representation 的事实及正式 paper标题。没有要求换方法名或全章改成另一叙述 |
| R1-18 | 3.4 piano-roll justification；`chap3.tex` → `sec:velcomp:problem`、`sec:velcomp:representation` | 未回复 | 现稿已说明 vertical patterns，可补它与 event list 的具体工程取舍：二维局部邻域、固定网格、稀疏性/时间分辨率成本。禁止未做实验的 event-based优劣断言 |
| R1-19 | 3.5 recovery vs estimation；`chap3.tex` → `sec:velcomp:problem`、`sec:velcomp:matrix` | 去掉已有 velocity 制训练样本；部署是estimation | 接受。解释 recovery/completion 是任务设定，estimation 是模型行为；符号上下文不足以唯一恢复原演奏意图。保留 thesis统称，不机械全篇替词 |
| R1-20 | 3.6 physical vs musical time；`chap3.tex` → `sec:velcomp:segmentation` | 偏向physical time，怕量化损失；也面向AMT输出 | 可保留以兼容未经 beat alignment 的数据。beat-relative representation 并不必然把 expressive timing量化抹掉；说明未比较，音乐时间值得未来研究，而不是说必然不如 physical time |
| R1-21 | 3.7 performance vs reference MIDI；`chap3.tex` → `sec:velcomp:datasets`、`sec:velcomp:perceptual`；375–380行 | 不认为冲突；声称网上量化 MIDI 与MOS都支持 | 必须先处理 E01。可接受 composition 是动机，不能把未核实小试写成正式验证。作者不想扩实验应尊重，讨论scope即可 |
| R1-22 | 3.8 baseline subsection；`chap3.tex` → `sec:velcomp:training`、`sec:velcomp:results` | 未回复 | Flat／pretrained Seq2Seq／reimplemented ConvAE 已有信息但分散。可就地归一小段或小节，说明训练与检查点来源；不把预训练 Seq2Seq 说成与其他系统同样从头训练 |
| R1-23 | 4.1 ecological validity／joint transcription；`chap4.tex` → `sec:scoreinf:problem`、`sec:scoreinf:principle`、`sec:scoreinf:discussion` | 未回复 | 现有教育/档案用例可支持限定场景。明确 modular correction 与可能的 joint learning 互补；本章不测 note F1 增益。不要反向主张所有现实AMT都该解耦，也不承诺重做联合系统 |
| R1-24 | 4.2 piano-roll vs event-based；`chap4.tex` → `sec:scoreinf:features`、`sec:scoreinf:arch` | 为multi-scale方便，未成功的transformer尝试 | 重要：当前章的 Transformer 已按 onset tokens工作，并非全程dense piano-roll。解释 acoustic map／score raster接口 与 correction token sequence 两层；不能写成“本模型拒绝event representation”，也不要混入第5章multi-scale动机 |
| R1-25 | 4.3 loss balance；`chap4.tex` → `sec:scoreinf:loss`、`eq:scoreinf:loss` | 引 Kim2024，认为比例已验证 | 现稿已 cite Kim 与两个单独平均的损失，可明确 unit coefficients。没有loss-weight sweep证据时，不称 universally optimal 或已证明最佳；作者“我验证过”作为待核验记录，不升级为新增表格结果 |
| R1-26 | 4.4 Table4.1 conditions；`chap4.tex` → `tab:scoreinf_maestro`、`sec:scoreinf:features`、`sec:scoreinf:arch` | 未回复 | 定义 onset-only、onset+frame、onset+frame_ex，与 BiLSTM/Transformer 两分组；特别核对 onset-only 的输入维度（正文BiLSTM只写3P）和 feature读取方式。无需改结果或加实验 |
| R1-27 | 5.1 complete AMT；`chap5.tex` → `sec:audiodyn_targets`、`fig:audiodyn_workflow` | 未回复 | 图展示可集成接口/案例，不足以证明已实现完整系统并测note accuracy。答“本章提供 dynamics/metre component；完整整合非本章实验”，具体是否曾拼接须查既有演示，不编造 |
| R1-28 | 5.2 change-point need；`chap5.tex` → `sec:audiodyn_targets`、`ssec:audiodyn_post` | levels decoded at beats | 该回复只回答时间单位，尚未回答为何单独 CP head。补 regime level 与transition detection的不同角色，均落在beat grid。不要说 model 没预测beat-wise levels，也不声称CP head直接改善Dyn F1除非已有对应消融 |
| R1-29 | 5.3 beat/downbeat connection；`chap5.tex` → `ssec:audiodyn_mmoe`、`ssec:audiodyn_post`、`ssec:audiodyn_loss` | 两条批注：可进一步连接；只在decoding相连 | 现稿可确认共享encoder/experts、独立gates/heads、additive losses。补充读代码后确认：保留的 `beat_postproc.py:139–147` 会把 downbeats 吸附至预测 beats，`final_evaluation.py:119–120` 调用该路径，支持作者 decoding connection 的说法。正文应补这一省略；最终实验与该固定代码版本的对应仍需核验，不能说已有训练loss一致性项 |
| R1-30 | 5.4 cross-dataset necessity；`chap5.tex` → `ssec:audiodyn_data`、`ssec:audiodyn_cross_dataset`、`ssec:audiodyn_limits` | 目的是检验composer/performer泛化，没有平衡数据 | 支持保留外部transfer诊断，但不能声称已隔离composer/performer因子。当前数据尤其需 E04 disclosure；Vienna/Batik与Mazurka label-prior差异的现有讨论可保留，因果语气宜限定 |
| R1-31 | 6.1 simpler route；`chap6.tex:31` | 愿改more efficient route | 建议更准确说明省去target velocity annotation或从real-audio adaptation出发；未比较总开发/计算/标注cost，不把 simpler换成同样无证据的more efficient。保留作者方法立场 |
| R1-32 | 6.2 V0 vs Vhat；`chap6.tex` → `ssec:bp:veloest`；91–93行 | 未回复 | 当前已说明coarse roll→score-refined output。可添一句两者不是pre/post adaptation checkpoint对比，并与第4章Vhat_0符号对齐；尽量不重复整段架构 |
| R1-33 | 6.3 synth faithfulness；`chap6.tex` → `ssec:bp:adapt_diffsynth`、`ssec:bp:adapt_results`、`ssec:bp:when_diffsynth` | 正确限定：degradation consistent with mismatch，未单独测fidelity与gradient accuracy | 该回复比部分正文更稳妥，应保留并用于局部限定。不能把consistent with写成证明原因；保留 matched Diff-Synth could be useful 的现有边界 |
| R1-34 | 6.4 Huber vs MAE；`chap6.tex` → `ssec:bp:adapt_diffsfproxy`；126行 | β=1，smallerror smooth／largeerror L1；无专门MAE比较 | 可接受并补两句。描述优化动机，不写empirically better than MAE；当前outlier解释已有，可保留，不需新消融 |
| R1-35 | 6.5 Fig6.2 rendered target；`chap6.tex` → `fig:bp_proxy_arch`、`ssec:bp:proxy_training`；main.pdf 印刷 p95 | 未回复 | 现图已写 SoundFont Render MIDI to Audio，caption明确SoundFont-rendered targets，较原意见已部分满足。优先更清楚标offline proxy training，保留真实音频adaptation的独立阶段说明；不强制重画全图 |
| R1-36 | 6.6 SoundFont selection；`chap6.tex` → `ssec:bp:soundfonts`、`ssec:bp:limitations` | 可自动化，但留未来 | 接受留未来。说明人工audition当前做法与主观性；可以提出 future automatic selection，不能发明候选池规模、盲听、算法比较或最优renderer证据 |
| R1-37 | 7.1 completeAMT／transcription gain；`Conclusion.tex` → `ssec:conclusion:future_amt` | 可能更human-prefer，未完成，客观指标可能不同 | integration可行性可讨论；没有实验不能称提高note transcription、BSSL必然更好听或objective一定下降。保留未来研究，以representation-specific evaluation和多输出接口解释 |
| R1-38 | 7.2 broader dynamic marks；`Conclusion.tex` → `sec:conclusion:future`；`chap5.tex` → `ssec:audiodyn_limits` | 同意补crescendo | 第5章限制已明确静态五级+blank，不等同explicit hairpins。第7章加一个很短future direction足够，区分连续渐强/渐弱与离散CP，不重写未来章节 |

报告 1 的 Introduction 其余部分、六项 merit criteria、overall recommendation 与签名页，主要是肯定／流程性结论，没有额外修改要求。应在完整 response register 保留“acknowledged，no thesis change proposed”，不把每段赞扬变成一项必须 YES/NO 的编辑任务。

## 报告 2 逐项基线

报告2没有作者回复，全部立场【待作者决定】。五个可处理项目如下；其中 R2-01 来自 Main strengths 内嵌的建议，不能因为标题是 strengths而漏掉。

| ID | 原文位置 | 现稿证据 | 独立判断与最小必要处理 |
| --- | --- | --- | --- |
| R2-01 | Main strengths首段：技术章与中心问题更明确连接 | 第3–6章已有Chapter Overview、positioning、summary | 优先保留；每章最多补一句“available data → missing label → structural condition”，避免再加一套重复overview。第6章保留S2 label-scarce extension，不假称S3 audio-only velocity |
| R2-02 | Main weaknesses第1段：published/adapted/new thesis synthesis | `Intro.tex` 157–188；authorship declaration；各章文件开头注释；四篇paper | 真缺口：正文只说3–5 adapted，没有清楚列thesis新增的conceptual synthesis与局部扩展，且第6章也有ISMIRpaper。用小映射表或短段指向四篇paper，明确哪些是paper贡献、叙事整理或已有增补。没有逐项diff证据，不认定新增实验／某表全为thesis原创 |
| R2-03 | Main weaknesses第2段：generalisation to guitar/voice/bowed/wind | `chap5.tex` 401；`chap6.tex` 517–523；`Conclusion.tex` 121–150 | 现有限制较好，补voice并集中区分 empirical evidence（piano/guitar）与hypothesis（voice/bowed/wind）。attack-based PHE/OSF不保证适于连续音，不用新实验填表 |
| R2-04 | Main weaknesses第3段：11专家听测只是支持 | `chap3.tex` 371–380、445–460；`Conclusion.tex` 54；abstract | 应明确sample小、8片段、单renderer／所选repertoire，支持而非definitive validation。保留已有MOS及CI，不从CI窄推大范围泛化，不添加未经报告的显著性、效应量或排除程序 |
| R2-05 | Main weaknesses第4段：minor English/formatting | 关键图表已抽查；Table2.7拥挤；正文少量语法与重复 | 可做局部proofread候选和排版清单，区分实际PDF缺陷与text extraction断行。当前PNG透明背景在图片工具显示黑色，不代表PDF黑底；main.pdf Figure2.3实际显示正常，不能误报缺图 |

R2的其余段落、six-criteria评分表、overall remarks、recommendation属于评价或对上述要求的重复总结。保留原文索引与acknowledgement即可，不重复制造新修改项。特别保留“no additional experiments, new data collection, or major rewriting”的明确边界。

## 候选进入独立复审的门槛

后续需要看到实际候选文字，不只看写作聊天说“已改好”。每个 substantive A/B/C都应附准确原文、`.tex`定位/label、作者立场、所依赖证据；A是最小可行改法，B补局部解释，C改善局部衔接，不能让C扩大实验或论点范围。简单纠错只需一个版本；本来足够的原文可以获选。

将按五项复核：回应是否答到问题、技术含义和数字是否有证据、全文是否冲突、是否保留作者语言与立场、是否超出minor revision。拒绝一个候选时指出具体词句与修复方式；复审时检查修后的实际文本。不要求两个聊天在无证据处强行达成一致。

GRS blueprint 应把本轮全部措辞标为拟稿。YES 仅表示批准方案；在thesis实际改动并逐项核验前，状态必须保留【待修改】【待核验】，不能填写最终页码或把“We have revised...”写成既成事实。当前材料没有可确认的GRS专用revision-report模板／格式要求；不得声称符合某个未见到的官方模板。

## 补充核查 两个 PDF 与源码的关系

本节是在基线形成后按协调者要求追加的证据核查；仍未阅读写作聊天候选。只读了本地 Git 历史、保留代码与既有输出，没有联网查来源，没有运行 notebook 或模型。

**尚不能确定哪一份是正式 submitted baseline。** 支持 `Z_He_PhD_Thesis.pdf` 可能接近 examiner 所读版本的内容证据是：报告1 PDF第1页写154页、127页主体；该PDF确为154个物理页，末页印刷号127，而main.pdf是155个物理页、末页印刷号128。不过页数不是文件身份凭证，不能据此认定它就是提交件。报告2列出的第3章 MAE 11.5/12.3/14.8、11.2/12.5/15.3，在两份PDF都存在，不能用来二选一。报告1所提“most controlled”“simpler route”等措辞两份也都有。

本地 Git 进一步显示：

- `2f035edec2cd7d6bcb1b0859a9767a9038d2fdfa` 的提交说明为 `to final`，同一提交新增 Z PDF，并修改了另一份 main.pdf。说明文字没有明确指定哪个文件作为GRS提交附件；不能把 `to final` 直接解释成 submitted。
- Z PDF 在该提交与当前的 Git blob 都为 `c93e52174e3ca7cd0649150be850a6b08ba91b38`。
- `58a07ec` 的说明为 `Merge bibliography, correct thesis citations, and rebuild PDF`，更新main.pdf为当前 blob `84dc72efc06fcd51ef7f7c7df1da6c559108685b`。当前main.tex、七章正文与authorship declaration相对该提交无差异，且下列新版PDF文字对应当前源码。这是“当前源码与main.pdf关联较强”的证据，不是已重编译验证全部字节一致。
- 当前README明确保留基线未定；目录中未识别到把某PDF的hash或确切附件与GRS接收/提交记录绑定的证据。正式baseline仍为【待作者或提交记录确认】。

以下页码同时列出物理页与印刷页；P为物理页，p为印刷页。

| 内容 | Z PDF 的实际文字/表值 | main.pdf 与当前源码 | 对本次提案的影响 |
| --- | --- | --- | --- |
| §4.6.3 对旧Recall的定义 | P85/p58把旧Recall写成预测velocity非零的覆盖率，并称当前Recall10%与mir_eval的velocity criterion一致 | P87/p60改成不建立两种Recall等价；说明mir_eval有note matching及全局velocity变换；源码 `sec:scoreinf:metrics` | 指标澄清在现存新版中已经发生，应保留。不能再把旧公式当当前准确描述，也不能声称这是本轮新修 |
| Table4.2 | P90/p63把FiLM U-Net 73.0%、hFT 76.5%、Transkun 82.1%放入Recall10%列，Transkun粗体 | P91/p64三项均为破折号，Score-HPT 80.3%为可比列最佳；源码 `tab:scoreinf_smd` | 候选与GRS拟答复必须用版本明确的表，不能拼接旧表外部Recall和新表解释 |
| §4.7.3 comparison protocol | P89/p62称all models同一训练协议 | P91/p64区分本地训练与外部来源原协议；源码 `sec:scoreinf:results:comparison` | 保留较窄的可比性，不将externally reported结果说成本地统一重训 |
| §4.7.4 misalignment | P90/p63声称前人conditioning用shifted score、post-processing用unshifted score，并称本研究修正了此问题 | P92/p65只报告本研究同一shifted score用于conditioning和onset post-processing，不再断言前人未记载的实现；源码 `sec:scoreinf:results:robustness` | 不恢复对前人实现未经核实的指控；global-shift结果不能扩大成任意alignment错误的证据 |
| Table5.2及ANN baseline | P105/p78列ANN dynamics F1=29.4，并笼统说表内F1按5折均值与SD | P105/p78解释CCI与F1不同；P107/p80表内ANN为破折号，caption区分本地5折与PELT原协议；源码 `ssec:audiodyn_baselines`、`tab:audiodyn_main_results` | 这是实质指标/表述修正，非纯排版。保留现稿边界；不把29.4直接放回F1列 |
| 第6章DDSP输入控制 | P117/p90称两类原始DDSP均以per-note velocity为native control | P119/p92改称instrument-specific adaptations；源码 `ssec:bp:adapt_diffsynth` 第97行 | 解释本研究后端适配与原始方法的区别；该措辞变化本身没有测量合成保真度，仍需遵守作者对R1原6.3的限定 |
| 五项核心风险是否仅由PDF版本造成 | 两份都写SMD刺激去velocity、frozen前端与jointly trained、target-corpus best-fold、吉他GT图和hFT MAE9.9/Score-HPT8.0 | 当前源码也保留这些内容；下节给出逐项证据 | 不能通过直接选较新PDF消除这些问题；仍可在源码定位上继续做局部提案 |

另外，MAESTRO时长、引用归属、部分数据表模态定义也有既有修正。以上只列会改变回应或候选判断的关键差异，不把换行、引用编号和分页漂移当成新的科学变化。

## 补充核查 五项技术风险的来源分层

这里明确区分 examiner 问题、作者回答和审查者推论。E编号不是新增examiner要求。

### E01 听测 MIDI 是否经过量化

- **Examiner原问：** 报告1 PDF第2页Chapter3倒数第2项，问performance MIDI而非reference quantised MIDI是否与composition use case冲突；转写 `README_Preliminary_Report_1.md:275`。
- **作者回答：** 同文件279行，称下载的量化MIDI推理有效，并称MOS用了quantised score-MIDI。应保留为作者对实际工作的当前说明，不能用旧工具判断覆盖。
- **源证据：** `Chapter_3/chap3.tex:375–380`、label `sec:velcomp:perceptual`；Z PDF P75/p48、main.pdf P76/p49；CMMR paper §5.2 Stimuli、PDF第9页，均说刺激源于SMD演奏，去掉human-performed velocity。它们没有明确交代量化预处理。两份PDF没有在这点上给出不同答案。
- **审查推论：** 这是预处理说明缺口，而非已经证明作者记错。performance MIDI可以是数据来源，随后仍可量化；需要实际刺激文件/生成流程把来源、量化与velocity删除顺序写清。当前材料没有足够证据选定“timing一定保留”或“一定量化”；也没有受控量化比较证据。

### E02 Fig6.3 的 guitar ground-truth velocity 身份

- **Examiner原问：** 两份报告均未明确指出Fig6.3的GT身份冲突。报告1原6.5问的是Fig6.2 rendered audio，不能误写成examiner已经指控Fig6.3。
- **作者回答：** 没有针对Fig6.3数据身份的原始回复。第6章真实吉他无velocity标签的阐述来自论文自身。
- **源证据：** `Chapter_6/chap6.tex:442、447`及 `fig:bp_ablations`：guitar excerpt与ground-truth velocities；图资产 `Chapter_6/figures/p3.jpg` 左面板写GT MIDI Notes + Velo。Z PDF P128/p101、main.pdf P130/p103。相反，本章 `sec:bp:problem`、`ssec:bp:datasets`及 `tab:bp_results_guitar`都说真实GAPS/FL没有velocity标签；`sec:bp:proxy_diagnostic`允许的是程序生成的合成guitar已知控制值。
- **审查推论：** 图未标明片段/数据集/合成来源，身份不能由图的色彩、键盘音域或文件名猜定。可能解释不止一种，未获得来源前不写成真实GT、pseudo-label或synthetic GT中的任何一种确定结论。只有核对原图生成记录才能决定该如何澄清，不能预先强制删图。

### E03 前端 frozen 与 jointly trained

- **Examiner原问：** 报告1原4.1、PDF第3页／转写305行问解耦dynamics与note transcription的现实有效性，并提联合建模可能有益；没有直接说本研究前端必须冻结或已经冻结。
- **作者回答：** 此项未回复。不能从空白推定接受或反对joint training。
- **源证据：** `Chapter_2/Background.tex:511`明确写frozen AMT front-end；`Chapter_4/chap4.tex:162`明确写retrain velocity branch并与jointly trained counterpart比较。两份PDF都有该矛盾：frozen均在P55/p28，joint在Z P85/p58、main P87/p60。
- **代码证据：** 保留路径 `02_Ultra_细节/审计记录/公开源码_Ch4_22b4db68/pytorch/config/config.yaml:92`默认 `train_mode: joint`；同目录 `pytorch/train_score_inf.py:190–222`同时实现joint与分阶段模式，joint阶段将 `base_adapter`、`post`的requires_grad都设为True。它不证明完整AMT所有预测分支都训练，也不证明所有已报告run均为此模式。
- **审查推论：** architecture unchanged、velocity branch/adapter joint training和其他AMT分支保持不变可以同时成立。应按运行记录统一“冻结的对象/阶段”，不能只删一个词后仍让读者误以为整个AMT都在联合训练。第6章 `chap6.tex:77`又明确VeloEst适配更新、两个后端冻结，应与第4章训练阶段区分。

### E04 外部测试中的目标标签选 fold 与表值聚合

- **Examiner原问：** 报告1 PDF第3页Chapter5第4项，转写371行，问cross-dataset evaluation是否关键，因为dynamics与composer/performer有关；并没有要求删除该实验或指控test leakage。
- **作者回答：** 375–377行，目标是看composer/performer泛化，承认数据没有专门平衡，但认为至少验证了良好泛化。应保留其研究动机，并限制证据能分离的因素。
- **源证据：** `Chapter_5/chap5.tex:187、330`明确依据目标corpus的dynamic F1选multitask fold；single-task则按各任务分别选最佳fold。label `ssec:audiodyn_cross_dataset`；Z PDF P102/p75及P107/p80，main P104/p77及P109/p82。两个版本都如此，不是新增PDF才产生的问题。
- **本轮独立算术核对：** 只解析当前 `tab:audiodyn_cross_dataset` 的32个本地模型显示值，与保留 `02_Ultra_细节/Ch5_现有输出汇总/v0_table5_4_comparison.csv`逐项比对，32/32等于旧表转录值，也32/32等于已存输出的per-task maxima；仅22/32符合正文stated rule。例：Vienna/MultiTask/BSSL表为32.0/29.8/73.8/29.3，共同dynamic-best fold的保存输出为31.96/21.25/73.73/26.96（显示为32.0/21.3/73.7/27.0）。这里没有重算模型F1，也不能从数字匹配独断这些输出就是最终run。
- **审查推论：** 两个不同问题应分开写：即使按正文共同fold规则，目标标签仍参与selection，应明确诊断与optimism边界；此外当前显示值与保存结果的吻合提示聚合规则待核验。不得用“未fine-tune所以完全held-out”作答，也不能自行以另一组数字覆盖表。

### E05 “hFT MAE约三倍”

- **Examiner原问：** 报告1 PDF第2页Chapter1第4项，转写133行，只问是否还可加入performance-audio→MIDI-velocity场景；没有提出任何三倍MAE断言。
- **作者回答：** 转写139行提出hFT约三倍，并以更强的score-informed pretrained model说明当前选择。
- **源证据：** Z PDF Table4.2 P90/p63、main Table4.2 P91/p64、`Chapter_4/chap4.tex` label `tab:scoreinf_smd`，两版均列hFT MAE=9.9、Score-HPT=8.0，显示值之比9.9/8.0=1.2375；两版在这些MAE值上没有差异。
- **审查推论：** 当前表不支持约三倍；作者也可能指另一个数据集或协议，因此不能直接写“作者错了”。可保留score-informed初始化是本研究选择的理由，数字作为【比较对象与协议待核验】；不得混用不同数据集的MAE来凑比值。

### 补充代码证据影响的其他两项判断

- **R1原5.3的decoding连接：** `02_Ultra_细节/Ch5_现有输出汇总/input_snapshot/pytorch/post_processor/beat_postproc.py:139–147`明确将每个downbeat时间改成最近的预测beat时间，再去重；`pytorch/final_evaluation.py:119–120`把beat与downbeat logits一起传给该postprocessor。作者“连接在decoding”有具体实现支持。无显式training consistency loss与有decoding连接并不冲突。最终实验代码版本仍需对应，但不能继续概括“没有输出连接”。本文件R1-29已据此修正。
- **F1 averaging的新核验风险：** 同快照 `pytorch/evaluator.py:58–70`定义weighted F1，69行用 `average="weighted"`；187–189行将它存为dynamic_f1。当前源码 `Chapter_5/chap5.tex:221–237`及两份PDF却给出五类macro-average。不能由聚合结果换算macro-F1，亦不能认定公开快照就是最终实现；须核对实际评估版本。R1-14、R1-30、R2-03的候选应避免未经核实地加重macro-F1解释。

## 基线完成与待续

已完成：独立读源文、两份原始报告及25条原始作者批注；核对四篇paper；识别两份PDF版本；抽查关键图表；建立38项R1与5项R2修改/回应基线及额外证据风险；追加两PDF与源码/Git关系核查、五项来源分层证据和既有表值算术比对。

尚未完成且不声称完成：A/B/C候选审查、作者选择、真实修订、全论文重新渲染QA、实验核验、GRS正式report。下一步由协调者提供第一轮实际候选，再进行独立逐句批评。
