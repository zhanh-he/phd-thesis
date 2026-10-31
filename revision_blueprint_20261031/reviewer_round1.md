# 第一轮独立候选审查

日期：2026-10-31。审查对象为 writer_round1.md、writer_working.md、COMMENT_MAP.md、ID_CROSSWALK.md、SOURCES.md、WRITER_HANDOFF.md；另按协调者要求检查 GRS_REVISION_REPORT_DRAFT.md 的 R1-21。先前独立基线已在阅读这些候选之前完成。本轮没有改 thesis、writer 文件、决定清单或 GRS 文件。

结论：43 项都已审到，27 组 A/B/C 共81稿，另16项单稿/保留/合并方案。多项可以继续采用，但整包尚不通过。必须返修的是实际段落拼接、R1-32误删方法配置、R1-21的论文/报告语体、R1-28C的逻辑、R2-02的归属表述和R2-04的听测表述。无需新增实验或改变研究设计。

“通过”只表示当前候选文字在列明的范围内可接受，不表示作者YES、不表示事实缺口已关闭、更不表示已实施。待查的run、刺激来源、图来源和正式baseline仍保留待核验。

## 可追溯性检查

- 43个canonical ID与独立基线完全相同，COMMENT_MAP保留38项R1、5项R2及一般评价的索引；没有把赞扬段落变成新的修改承诺。
- writer候选JSON记录97个候选：81个A/B/C＋16个单稿。75处原文引文逐项在当前源码中找到，75处行号也完全匹配；未发现编造原句。
- 81个A/B/C送审正文与working中的A3/B3/C3逐个归一化比较，81/81一致。working有162个A1/A2/B1/B2/C1/C2短稿标题及162条对应取舍理由。
- 这些短稿有实际文字，不能说完全没有探索记录；但多数是互补的句子/图标签草图，不是两篇完整候选段落。例如R1-25 A1说equal relative coefficients，A2说own active positions，最终A3合并两项；R2-02 B1是四篇会议映射，B2是shared background/scenario map。这更像组件草图与合成，不足以证明162次完整独立改写。
- 单个整理文件也不能证明生成先后或独立多轮淘汰；本轮不认证“真实经历了162次独立修改”。应准确称为“短稿/组件草图及取舍”，不要倒填轮次、时间或独立模型。实际的writer round1→本审查→writer round2→复审才是可观察的多轮循环。
- 不要求机械重写全部162条。对本轮要返修的关键项，下一轮保存确切新段落、修复理由与本审查定位即可；不要把新写内容回填成旧轮的历史。

本轮读取的主要输入SHA256：

| 文件 | SHA256 |
| --- | --- |
| writer_round1.md | ef6c0d0c8e0c0e55bd1fdd4c032fc9816a8050313f11ca02bdd8244859a5dcaf |
| writer_working.md | 4fefce6703c8d7e24ceb319d07adf6da130d1c35a6a481b3f47b7b16c7708adf |
| COMMENT_MAP.md | f8c9f9357f17d1060fb294e31196e3e846411369ede5518bb868fdb194ee7d18 |
| ID_CROSSWALK.md | 7a371efb1b5ed54706a1ee376bf24b6c522418c2fdd9c8bdd4d00290a0d95d20 |
| SOURCES.md | aef54e4c2c6aee498d99f2bb7c9719680dc81c71a12f11ac55dfb8dbdceab064 |
| WRITER_HANDOFF.md | ec0566434ff40f4344962edc766fe0b20661c3c018f272896d19624774bfd2ed |
| GRS_REVISION_REPORT_DRAFT.md 初读版本 | 90a7c7886bacc1727eb9a965d72f344d01c69c06692900941107ca20d5f8544d |
| GRS_REVISION_REPORT_DRAFT.md 审查期间更新版本 | 6a4bc3489c918946e07bbb3cf13b1328b9e6336fbcfb2f80bca8051bfcfb7736 |

## 27组实质候选逐稿结论

下表的行号均指上述hash的writer_round1.md。P=通过；V=返修；R=拒绝当前写法；“—”不存在该路线。拒绝的是当前文字，不是否定作者的研究立场。详细修复见后文F编号。

| 项目 | A | B | C | 独立判断与下一轮路线 |
| --- | --- | --- | --- | --- |
| R1-03，178–192行 | P | P | P | 都落实作者补instrument identity/其他表达因素的意思。A最小，C更能避免强制串行流程。保留图副本/视觉核验门槛；不能把图内“Estimate”误读成本文实现全部输出 |
| R1-05，252–260行 | P | P | P | B较清楚地区分数据状态与学习条件，推荐B。建议一句注明这些条件可重叠，避免whereas形成互斥分类；该小改不改变三稿实质 |
| R1-06，294–302行 | P | P | P | B正面区分audio-only input与score-dynamics target，符合作者S2立场。未使用无来源三倍MAE，正确；各稿均不新增audio-only实验 |
| R1-07，339–347行 | P | P | P | B适合caption，C更适合正文；三稿都保留context dependence，又承认第5章direct route。采用一处解释即可，不在图注和正文各复制长段 |
| R1-09，431–439行 | P | P | P | Note On限定准确；A更短，B覆盖protocol例外最清楚。保留技术术语，不扩成MIDI控制综述；最终引用仍须沿作者体例 |
| R1-13，561–569行 | P | V | V | 选A作为最小caption/notes方案。B的“captured velocity”与现表混合来源不符；C遗漏三角符号解释，见F04。ATEPP分母、Audio逐行数据仍待核验 |
| R1-14，601–609行 | V | P | V | B明确class/event-type，区分macro与weighted且未替未核验结果定性。A需同样加class-specific限定；C不能保证当前矛盾的定义就是每个结果实际用的规则，见F05 |
| R1-15，641–649行 | V | V | V | 三稿的内容边界都对，但操作写“只替换首句”时均与紧接的原句重复。需要完整assembled opening，见F01；推荐修后的B |
| R1-16，702–710行 | P | P | P | B保留作者不做style control的真实动机，并把composer groups限为描述性。与R2-04合并限制，避免同一小听测在邻近段落反复受审 |
| R1-17，744–752行 | P | P | P | B最好地解释局部pitch–time结构和single-channel target。C最后的普遍优越性免责声明可删，但不构成技术错误。全文同步计划尚须具体化，见F10 |
| R1-19，812–820行 | P | P | P | B简洁保留recovery/estimation区分。C说接口可接受quantised input不等于声称其效果已严格验证；与R1-21共享部分不再插两次 |
| R1-20，870–878行 | P | P | P | B把physical time解释为timestamp/beat-map条件；C承认beat-relative可保留expressive offsets，科学上有益但略像回应。推荐B，保留未比较这一事实即可 |
| R1-21，924–932行 | V | R | V | A可保留应用段，协议占位移出正文；B的“The author reports...”及编辑指令不可进thesis，拒绝当前语体；C只可作明确条件分支。全部仍依V-02待查，见F02及GRS专节 |
| R1-23，997–1005行 | P | P | P | 三稿都保留modularity且承认joint modelling。考虑§4.4已较长，独立偏好A的最小范围说明，不必机械选B。可把用途解释与已有末段合并 |
| R1-25，1102–1110行 | P | V | P | A回答实际比例且不混同gradient magnitude；B保留preliminary evidence正确，但最后的every-backbone/dataset免责声明过量。推荐修后的B，见F03；C若保留也可简短收尾 |
| R1-27，1186–1194行 | P | V | P | A最适合第5章局部说明；B“shared beat grid”应限定score-facing integration，不能笼统覆盖逐音velocity接口；C适合第7章跨章future。见F06 |
| R1-28，1226–1234行 | P | V | R | A短且正确。B前两句重复紧邻原target段，保留独立boundary supervision的说明即可。C称beat-wise levels本身不能区分stable/new region，逻辑过强，拒绝该理由，见F07 |
| R1-29，1264–1272行 | P | P | P | A、B都准确表达共享/独立heads/loss与解码snap。B可用。保留beat sequence available条件；不把default evaluation code等同全部最终run，见F08 |
| R1-30，1304–1316行 | P | V | V | A解释combined shift最自然。B首句rebuttal-shaped；C“stops transferring”过度以失败定调。共用protocol段仅作为书面规则的条件稿，并须与表源对齐，见F09 |
| R1-31，1342–1350行 | P | P | P | A最直接。B的“more direct”有具体real-audio adaptation解释，未声称算力/成本更低，因此可以保留，不因含比较词而自动否决。C末尾通用否定可省略 |
| R1-33，1412–1420行 | P | P | V | B忠实于作者未单独测fidelity/gradient的说明，推荐B。C的“which component of their mismatch caused”仍预设mismatch为原因，须修；跨段弱化因果提案基本正确，见F11 |
| R1-34，1484–1492行 | P | V | P | Huber小残差梯度理由正确，A最小。B的“a dedicated MAE comparison has not established”可被读成做了却未证实，改为明确未做；保留β与PHE/OSF 1:1且避免重复，见F12 |
| R1-36，1547–1555行 | P | P | V | A/B给出具体未来方向，符合作者不扩大本轮的立场。C说automation“would change more than an implementation detail”过重；真正改变操作目标的是选中renderer，不是自动化本身，见F13 |
| R1-38，1611–1619行 | P | P | V | B区分boundary与gradual span，适合未来方向。C“leaving ... implicit”可能暗示现系统已间接恢复hairpins，改为not explicitly represented即可 |
| R2-02，1698–1706行 | P | V | P | 明确四章/四paper mapping有价值。B的“The thesis-level addition is”与其推荐理由构成过于确定的新增归属，见F14；A/C可作组织性说明但不替代最终paper差分核对 |
| R2-03，1738–1746行 | P | P | P | B区分piano直接标签与guitar loudness agreement，点明未测voice/bowed/wind。其连续控制论证与第6章已有attack-driven限制一致，不需新增实验；C首句可用may transfer更温和 |
| R2-04，1820–1828行 | P | V | V | A最接近所需的局部补充。B的perceptual validity过泛、限制堆叠；C的population-wide musical naturalness不是此test实际评价目标。应写所测reference similarity及范围，见F15 |

## 16项单稿 保留或合并方案

| 项目 | 结论 | 具体核查 |
| --- | --- | --- |
| R1-01 A，90行 | 通过 | 保留numeric是可供作者选择的合理方案；不是默认作者拒绝examiner。不能把候选说明句粘进正文 |
| R1-02 A，149行 | 通过 | accepted有报告原文支持；没有编造出版页码或DOI。仅状态行修改足够 |
| R1-04 A，218行及同步 | 通过 | collecting正确；结论的“collecting them again from scratch”可更自然写“collecting new data from scratch”，属可选微调，不扩大任务 |
| R1-08 A，407行 | 通过 | ccc三组分线对应正确的Bark表；实施时保留其他表内容并渲染，不能只检验LaTeX字符串 |
| R1-10 A，470行 | 条件通过 | 统一色后的caption自洽，且解决未知原色语义而不猜。仅适用于已经完成对应图副本的方案；保留原图就不能用该caption |
| R1-11 A，496行 | 通过 | humanisation定义短、含timing和velocity，未把一般概念缩成本文特例 |
| R1-12 A，526行 | 通过 | 保留已有crescendo定义并补scope/cross-reference，避免重写背景。与R1-38共用信息，最终用label引用 |
| R1-18 A，786行 | 通过 | 合并到R1-17可以覆盖选择piano roll的理由。此句是操作说明，不是拟插入thesis的英文正文 |
| R1-22 A，971行 | 通过 | 正确区分pretrained Seq2Seq与本地重训ConvAE/U-Net，未强称同一输入分支。最终保留citation keys，别把作者年阅读写法变成强制体例转换 |
| R1-24 A，1056行 | 通过 | matrix interface＋onset tokens解释准确，也防止把Ch5 multi-scale动机挪用到Ch4 |
| R1-26 A，1154行 | 通过 | 条件与表中O/F/Fex映射正确；onset-only具体维度与parameter-count覆盖范围仍应与run核验，不据本段伪称已核验所有设置 |
| R1-32 A，1380行 | 返修操作范围 | 文字本身澄清了V0/hatV与架构/参数；但“替换最后一段”会删除22.05kHz、FFT2048、hop221等配置，而§6.5.1再引用这里的FFT设置。见F16 |
| R1-35 A，1521行 | 条件通过 | 离线teacher rendering与real-audio adaptation区分准确；原图已有Render MIDI to Audio，不必重画整架构。图副本和caption一并核验 |
| R1-37 A，1579行 | 通过 | 不虚报note F1改善；与R1-27合并，保留一处完整integration讨论即可 |
| R2-01 A，1663行 | 通过 | 现稿已有每章定位，保留并修正术语足够。不在report声称新增四段；R1-06/R1-15仍须实际落实 |
| R2-05 A，1898–1904行 | 通过 | 四项都对应实有措辞；10s/小节说明与R1-20同一处只改一次。不能把其余技术疑点打包为proofread |

## 必须返修的具体文字与完整上下文

### F01 R1-15 只替首句会制造重复

位置：writer 621、645行；源文 `Chapter_3/chap3.tex:13`。B写：

> the symbolic notes and their timing are known, while the dynamics layer is missing

操作却说只替第一句。保留下来的下一原句立即又是：

> Here the symbolic notes and their timing are already known, but the note-level velocity is missing, flattened, or musically uninformative.

不是B的技术判断错，而是assembled paragraph不合格。A/C也会重复fixed notes/input condition。建议把操作改为替换原段前两句，保留原问题句，并提交实际合成段，例如：

> This chapter addresses Scenario S1, where the symbolic notes and their timing are given, but the velocity layer is missing, flattened, or musically uninformative and no performance audio is available. Fixing the note structure limits what the model may change without uniquely determining the velocity profile. The chapter therefore asks whether useful note-level dynamics can be recovered from symbolic structure alone, without changing the original composition.

这只是返修示例，不是替writer选择最终版本。后面的15行仍可保留应用语境；不再重复一遍输入定义。同步修正§3.3、§3.11、Intro排序与Conclusion首句的方向正确。

### F02 R1-21 把应用段与尚未核实的协议分支分开

A的“The timing preparation ... is specified ... below”在核验前并不成立；B的“The author reports...”不是thesis作者自述语气；C的量化输入/量化reference/保留原velocity是一个具体条件，不能因作者说“量化MOS”就替他补齐全部步骤。

要求：正文候选先只写可确定的应用与训练来源；V-02状态、作者原说明和条件分支留在候选外。不要用尚未填实的编辑说明把B标成可直接粘贴的完整正文。例如可先采用：

> Performance MIDI supplies captured velocity targets for training, while the completion interface can also accept quantised symbolic input. The composition use case is to add a velocity profile while retaining the notes and timing supplied by the user.

随后另列【协议句待定：作者说明听测使用量化score-MIDI；需要把SMD来源与实际timing preparation写清】。核验后给出真实处理步骤，不预写一个只能证明“删velocity”的未量化版本，也不替作者否定量化说明。

### F03 R1-25 保留已有验证 不追加万能最优免责声明

SMC提供稿§3.3在公式后确有：preliminary multi-scale/hybrid supervision consistently outperformed frame-only/onset-only alternatives，并说省略详细ablation。原paper给出的是hybrid-vs-single-objective证据，不是loss-weight sweep，更不是所有backbone的最优比例证明。作者“我验证过”不应被改成“完全没做过验证”。

B的最后一句：

> does not establish that equal weighting is optimal for every backbone or dataset

逻辑上不错，但examiner问实际balance，这个普遍命题不是正文必须逐次否定的对象。A关于equal coefficients≠equal numerical gradients的区别有用，且更贴问题。建议局部版本：

> The frame-wise BCE and onset-wise L1 terms are averaged over their respective active positions and combined with equal relative coefficients. We retain the hybrid objective of Kim et al. (2024), supported by our preliminary comparison with frame-only and onset-only alternatives. Equal coefficients do not imply equal numerical loss or gradient magnitudes.

若正文不需最后一句，可只保留前两句。实际theta=.5与公式sum的整体尺度区别继续留run核验，不改公式。无需把没有weight sweep重复写在正文、GRS、表注多个位置。

### F04 R1-13 表格模态要与实际单元格一致

B的“captured velocity”会把estimated、software-generated、captured等现表不同来源压成一个词。改成：

> velocity annotations, with their provenance specified in the row notes

C若替换caption/notes，需补：

> A triangle indicates a qualification explained in the corresponding row note.

A作为最小方案较好。没有逐行核实Audio栏和velocity provenance前，不把B当整表已完成。现阶段不是要求重查所有dataset，更不是重画数据结论；只需保留清楚的字段与待填边界。

### F05 R1-14 定义与实际采用的指标不能混写

A的“fraction of predicted labels ... correct”若理解成全部multiclass labels，会接近accuracy，不能不加class条件再称其harmonic mean为macro/weighted F1。按B补“for a given class or event type”。

C的：

> The task-specific definitions ... state the averaging rule ... used for each result.

在Ch5 macro-vs-weighted未对齐时是过度保证。改成：

> The averaging rule, temporal grid, and event-matching tolerance must be identified when interpreting each result.

B本身可通过：它定义两种F1而没有假定当前数值是哪种。不要借此“定义补齐”就宣布V-05已解决。

### F06 R1-27 beat grid 限定于 score-facing dynamics

B的“combine ... note content ... using a shared beat grid”适用于第5章notated markings，但不能成为第4章note-onset velocity整合的统一坐标。建议：

> For score-facing dynamics, integration would attach the estimated markings to note content on a common metrical grid. Note-level velocity correction instead uses aligned note onsets.

第5章局部可只保留第一句；第7章若概括所有方法再补第二句。不要为解释一个接口引入新的score-alignment系统或声称已实现完整AMT。

### F07 R1-28C 把建模选择说成逻辑必需

C的：

> Predicting a level at each beat ... does not by itself distinguish a stable region from a new notated event.

不应这样作为必须另设head的理由。相邻beat labels的变化可以导出边界；本工作选择的是显式监督一个boundary target，不是证明另一种表述无法区分状态变化。B还重复了紧邻原文已说明的frame grid、beat mask与beat-snapping。

建议保留现有target定义，在其后只补独特理由：

> The separate change-point head gives transitions an explicit supervision target, instead of deriving boundaries only from changes in the predicted level sequence. It complements the beat-wise level output by modelling when a new dynamic region begins.

不需要再加“not the only valid formulation”这一普遍免责声明。也不能声称去CP head的独立消融已证明它提高Dyn F1。

### F08 R1-29 decoding 有实证代码 但要精确归因

三稿的实现描述成立，尤其保留when beats available。独立重读确认：

- `input_snapshot/pytorch/post_processor/beat_postproc.py:139–147`在有预测beat时snap downbeats并unique去重。
- `input_snapshot/pytorch/final_evaluation.py:68–72`的evaluate默认advanced_only=False，并创建type="minimal"的Postprocessor。
- 同文件115–120行的normal evaluation分支确实把beat/downbeat logits送入该对象；225、231行的`--advanced`会选择不同运行分支。

因此可以说“保留代码的normal/default evaluation路径实现此操作”，不能说仅凭函数存在就证明所有最终表格、所有baseline、所有run都用了它。作者原回复与实现相互支持，候选不必摆出普遍怀疑作者的姿态；只把最终run版本对应保留在外部核验清单。图5.2应是输出至post-processing的连接，不能画成新增learned cross-head edge。

### F09 R1-30 thesis 内不必重演 examiner 的争论

B的：

> useful rather than unnecessary

是在对评审问题作答，不像放在实验协议中的解释。可改为：

> Cross-dataset evaluation tests the learned mapping under changes in repertoire, performers, recording conditions, and annotation conventions. These factors vary together in Vienna4x22 and Batik-plays-Mozart, so the experiment diagnoses combined corpus transfer rather than isolating a composer or performer effect.

C的“where ... stops transferring”也不宜把mixed outcomes整体定义成失效。改为“how the learned mapping transfers under different corpus conditions”。

1304行target-label-selected protocol说明准确描述当前书面规则，但绝不能把“as described here”当作已核验表值来源。当前表值与已存per-task maxima吻合、共同fold规则仍有10项不符，macro/weighted也未对齐。disclosure可以作为待采用草案，不能单凭它给全部external结果贴上已解决标签。

此外当前§5.6.1、§5.7.3已经分别说明selection，新增protocol段应替换或整合现有selection段，避免三次说同一流程。它对结果解释是实质且必要的，不属于可删的泛泛限制。

### F10 R1-17 全文同步尚未形成可逐句复核的替换表

762–764行的“image colourisation ... used as a literal task claim”不是一条准确原句，而是概括性指令。abstract、Intro、Chapter3/7有不同上下文；“reformulates ... as image colourisation”未必每处都需要替换，既定章节/论文标题更不应改。

要求下一轮列出实际要动的原句、完整replacement和所保留内容；不强迫所有出现点加一遍RGB解释。R1-17B局部段落可通过；“全文已一致”的结论须等真正的逐处对照。

### F11 R1-33C 仍有隐含因果

C的：

> which component of their mismatch caused the degradation

预设mismatch已经是原因，只是不清楚哪一部分。改成：

> The comparison shows weaker adaptation with the selected Diff-Synth back-ends, but does not isolate the cause of that degradation.

B更忠实于作者原回复，可以直接作为路线。A若保留模型名，最终上下文应明确是本研究使用的adapted back-ends，不恢复旧稿“两种原始模型皆native per-note velocity”的断言。

跨段替换1432行方向对；但保留实际“参数域crop-length较稳定”的观察，不要把它也全部消去。将机制说成consistent with就足够。1436行会紧接原句“The recovered velocity absorbs effects...”，衔接正常，不须再添加一段免责声明。

### F12 R1-34B 明说未做 MAE 比较

原句：

> a dedicated MAE comparison has not established that Huber gives better adaptation

容易让人以为做过专门比较，只是结果不支持。作者说的是没有专门比较。改为：

> We did not conduct a dedicated comparison with MAE; Huber was chosen for its smoother small-error gradients.

如前句已写动机，末句只留“We did not conduct a dedicated comparison with MAE.”即可。A和C技术上可接受；与公式后的β=1.0、PHE/OSF 1:1文字整合，不重复报两次β，也不把MAE的大误差linear tail说成Huber独有优势。

### F13 R1-36C 自动化不必改写 recovered velocity 定义

原句：

> automation would change more than an implementation detail

把自动化本身说得过强。更准确的是选择哪个renderer影响操作目标，自动/人工都一样。改为：

> Because the selected renderer conditions the recovered velocity, an automated procedure should assess its velocity response as well as timbral similarity.

B已经足够，不需为这项minor suggestion展开一段新的概念论证。

### F14 R2-02 有综合贡献 不等于已完成 exhaustive novelty mapping

B的：

> The thesis-level addition is ...

与1708行“所称thesisaddition都能从独立论文与当前chapter结构核实”需要收窄。可以从当前thesis直接核实：Ch1提出统一问题和scenario map，Ch2形成共同背景，Ch7比较结构/表征/监督/评价及边界。这支持它们是thesis中的cross-study organising/synthesis内容。

不能由此证明这些思想只在thesis首次出现，或这份列表穷尽thesis相对于四篇最终发表稿的所有新增内容。提供ICASSP稿含PENDING等编辑占位，不能当作clean published baseline；本轮不能宣称已完成精确paper-vs-thesis novelty diff。

建议保留B的四篇mapping与authorship reference，末句改为：

> Across these studies, the thesis develops a common label-recovery formulation and scenario map, introduces shared background, and compares their assumptions and limitations in Chapter 7.

这回答了“thesis如何综合”，同时不虚报独占性。若最终GRS要求逐项说明adapted/new结果，继续保留待核验，不把这种结构性说明包装成已确认全部原创归属。这里不应因此把本来有效的thesis-level conceptual contribution删掉。

### F15 R2-04 一次具体范围说明 优先陈述已获得的证据

B的“does not establish perceptual validity across ...”太泛；C的“not a population-wide estimate of musical naturalness”引入了本文并未声称估计的总体量。现protocol让听者按human-performed MIDI rendering reference的相似程度评分；不是抽象检验一个系统的全部perceptual validity。

局部可写：

> In the listening study, 11 expert listeners rated eight selected SMD excerpts rendered with one PianoTeq configuration. The higher ratings for U-Net than for Flat and ConvAE support the objective comparison within this setting. The composer-group results remain descriptive because the excerpts were not balanced to isolate stylistic effects.

如果R1-16已完整说明composer groups，第三句不必在这里再写。把11人、8段、单renderer集中到一处，保留结果与sample scope；不必在每章都加small或否定句。

全书同步应区别必要纠正与可选微调：

- Abstract `validated`→`assessed`可接受，不需要再加small。整体句可写“the results are assessed through cross-dataset objective metrics and a MUSHRA-inspired listening test”。
- Discussion `verifies ... musical quality`应改为更贴rating target的“provides complementary evidence of greater perceived similarity to the reference on the selected stimuli”。
- Intro拟稿`it examines how ...`只剩研究意图，弱化已得到的结果；可写“it shows that velocity completion can improve expressive rendering on fixed symbolic notes, supported by objective evaluation and the listening study”。无需每次补一串总体外推否定。
- Conclusion把`sequence-oriented baselines`改成Flat和ConvAE是必要事实纠正：听测没有Seq2Seq。可写“the listening study supports an improvement over Flat and ConvAE on the selected excerpts”。不必又重复small。

不是所有谨慎句都应删：R1-21的timing未核验、未作因果style比较、单renderer范围有实际意义，保留在对应位置；不要把它们叠成让读者误以为听测无效的通用警告。

### F16 R1-32 好的澄清句不能删除被后文引用的配置

writer 1360行说替换§6.4.1最后一段。原 `Chapter_6/chap6.tex:93`同段包含22,050Hz、100fps、FFT2048、hop221、Hann等设置，而164行的PHE/OSF提取再次指向本节FFT设置。候选1380行没有这些配置，也没有保留原方法cross-reference。

要求：保留原段的配置句与Chapter4详细架构引用；只替换末尾“fixed black-box...”这类模糊描述，或在定义V0/hatV处增加简短澄清。示例末两句：

> Here, V^(0) denotes the intermediate acoustic estimate, while V-hat denotes the corrected onset values passed to the rendering interface; the superscript does not identify a pre-adaptation checkpoint. The architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen.

原数学符号恢复LaTeX。不要为增加解释牺牲reproducibility信息。

## GRS 草稿 R1-21 单独审查

初读对象：上表90a7c788版本的`GRS_REVISION_REPORT_DRAFT.md:431–449`，尤其441行。审查期间该文件已由其维护者更新，最新分支核查见本节末；以下旧句不再作为当前未修错误重复计数：

> I will not present the listening test as a verified test of timing-quantised score MIDI unless the original stimulus records confirm that preprocessing.

结论：拒绝把这句话作为正式examiner response。它是内部编辑防错规则，不是作者向学校解释研究与修订；而且只复述“methods describes performance-MIDI excerpts”容易让读者误以为作者已撤回其量化MOS说明。这里必须同时保留：SMD是刺激来源；作者当前说明听测用了量化score-MIDI；方法文本尚未明确timing preparation；本轮未核实具体过程。

建议把“核验未完成”留在中文工作状态栏，在英文中用待填写的具体方法字段。可提供以下条件拟稿，**仅在作者确认所述量化处理后使用**，确认条件放在quote外，不把它伪装成既成修改：

> The composition use case is to add velocity while preserving the note content and timing supplied by the user. Performance MIDI provides the captured velocity targets for training, while the completion interface also accepts quantised MIDI. The listening-test stimuli were derived from SMD and prepared as quantised score-MIDI 【specify the quantisation procedure and whether the same note timings were used for the system inputs and reference】. I propose to clarify this preparation in the listening-test protocol and distinguish this evaluation from a controlled comparison of timing representations.

配套工作状态：【作者已记录“量化MOS”；上述具体protocol待作者/既有刺激记录确认；未修改；最终位置待核验】。这不要求新增实验，也不把作者说法降格成“只要没文件就不可信”。

若量化细节仍完全不能确认，英文先仅保留前两句与“I propose to clarify the timing preparation of the SMD-derived listening stimuli in the protocol.”，量化说明和待查项仍保留在工作状态，不输出确定的另一种未量化协议。实施后再根据实际差异转换为正式完成式；本轮不写“We have revised”。

### 审查期间新版 Q/P 分支的复核

最新文件hash为`6a4bc3489c918946e07bbb3cf13b1328b9e6336fbcfb2f80bca8051bfcfb7736`。旧的“I will not present ... unless”已删除，改为明确的Q/P条件稿，不默认reference接受相同timing处理；这是有效修复，不应再把旧语气作为未处理问题。

- Q分支在原记录确认输入量化后可用；它保留作者quantised-MOS说明，也没有凭空补出reference与input相同处理。其范围措辞可通过，仍不代表V-02关闭。
- P分支只在记录明确支持performance timing时可考虑，当前不能拿它替换作者的量化说明。句子“The evaluation used performance-timed MIDI because it supplied captured velocity targets”把数据来源与是否量化作了无证据的因果连接：captured velocity targets同样可与quantised输入并存。删除because理由，分开陈述来源和核实后的timing条件。
- P分支“The discussion now separates ...”在当前未执行蓝图里过早使用完成状态。改成“I propose to clarify the timing preparation in the protocol and distinguish the composition use case from the scope of the listening evaluation.”实施后再根据实际差异写完成式。

本轮不直接改第三编辑文件；上述条件判断交由协调者路由。不得同时把旧稿、Q、P或本节替代示例四套答复塞入正式report。

## 全文一致性 风格 与 minor 范围的总评

可以保留的成果：R1-06的S2/S3区分；R1-09的Note On限定；R1-17的image-like解释；R1-24矩阵接口与tokens；R1-29的decoding联系；R1-33的保真度与梯度区分。它们具体、适合作者技术说明风格，也没有扩大实验。

主要风格问题不是英文不够华丽，而是一些稿把对评审的论辩搬进正文，或用“并未证明所有情况”“不是唯一有效形式”“不代表总体validity”重复保护一个本来已经有限定的结果。需要保留针对实际证据缺口的限定，减少针对未提出的普遍主张的否定。给作者的A/B/C仍应有真实取舍，不能只让最长的B/C显得更完整。

候选对baseline、run provenance、图6.3身份、F1聚合的待核验处理整体谨慎；这些不是可以通过把语句改得更顺来关闭的事项。现有source-local提案可继续写，不因正式submitted baseline待确认而停全部工作。图表变更仅在提案副本制作；本轮没有授权源文件实施。

## 下一轮明确交付要求

1. 逐项回应F01–F16，说明采用/不采用及实际修改。不同意审查意见可以给理由，不强求一致。
2. 至少对R1-15、R1-21、R1-25、R1-28、R1-30、R1-32、R2-02、R2-04交出包含前后衔接的完整assembled paragraph；只交独立新句或“已改好”不足以复审。
3. 保留本轮文件作历史，下一轮写writer_round2.md或明确版本记录；不回填虚构的A1/A2时间顺序。
4. 第三编辑在复审后再采用候选；本审查未改DECISIONS或作者选择，不把“P”自动转为YES。GRS R1-21待决定状态继续保留。

执行结果：本轮审查完成；尚有上述返修与事实核验，整包未获通过。无工具拒绝或不确定写入；thesis、writer和GRS源文件未修改。
