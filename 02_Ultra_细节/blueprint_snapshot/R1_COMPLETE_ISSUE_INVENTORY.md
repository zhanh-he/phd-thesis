# R1 完整问题清单

评审：Dr Emmanouil Benetos

正文p1及签名p4确认身份。p3批准进入viva，评价excellent/top25%；p1肯定原创性、文献、方法、实验、英语。以下38项含可选建议和讨论问题，并非38项必须实验。

工作类型：C=口头/定义澄清；W=重写说明；E=补引现有证据/核查来源；F=排版；A=已有输出再分析；X=新实验。A/X注明可选，均未执行，也不是自动承诺。P0=今天优先，P1=备用，P2=答辩后。所有条目状态均为 planned，未修改论文。

页码格式：p=论文印刷页；PDF=文件从1计数页。主版本为 Zhanhong_He_PhD_Thesis_v0.pdf；报告无印刷页号，以PDF页计。正文 p1–112 对应 PDF28–139（偏移+27）；不要把front matter套用该偏移。

## R1-01 引用改 author–year

- 来源：报告PDF p1；性质：可选建议；优先级：P2。
- 对应论文：全书引用；reference.bib / IEEEbib.bst。
- 处理：先核对 UWA/学院格式约束；author–year 是可读性建议，不当作学术缺陷。
- 工作：F；答辩卡：—；状态：planned。

## R1-02 ISMIR 2026 状态

- 来源：报告PDF p2；性质：更新建议；优先级：P2。
- 对应论文：Authorship Declaration 印刷v / PDF8；Ch6 §6.1 p85 / PDF112。
- 处理：报告称 accepted；以录用信/正式记录核对后更新 under review；不把评审文字等同独立发表状态验证。
- 工作：W/E；答辩卡：—；状态：planned。

## R1-03 Fig1.1 总 AMT 标题范围过宽

- 来源：报告PDF p2；性质：范围批评；优先级：P2。
- 对应论文：Fig1.1 p2 / PDF29；§1.2 p3 / PDF30。
- 处理：改为本文聚焦 dynamics 的示意图；说明 instrument identity、playing techniques 未画入。
- 工作：W/F；答辩卡：—；状态：planned。

## R1-04 recollecting 歧义

- 来源：报告PDF p2；性质：文字建议；优先级：P2。
- 对应论文：§1.1 末段 p3 / PDF30。
- 处理：改 collecting；同时审慎删除 entirely bypass annotation ambiguities 之类过强措辞。后一项为本次阅读补充，不是报告原话。
- 工作：W；答辩卡：—；状态：planned。

## R1-05 weakly expressive / weakly supervised

- 来源：报告PDF p2；性质：定义问题；优先级：P0。
- 对应论文：§1.5 p6 / PDF33；§1.6 pp6–7 / PDF33–34。
- 处理：补操作定义：前者 dynamics missing/flat/unreliable；后者目标 velocity 无直接标签、以 renderer proxy 提供间接监督；不等同节奏表现力弱。
- 工作：C/W；答辩卡：A02；状态：planned。

## R1-06 Table1.2 缺 audio→velocity 场景

- 来源：报告PDF p2；性质：场景建议；优先级：P1。
- 对应论文：Table1.2 p6 / PDF33；§6.3 p88 / PDF115；Table7.1 p106 / PDF133。
- 处理：保留三核心场景，另列 Ch6 的 audio+aligned notes、无目标 velocity 标签；不是 audio-only 无结构。
- 工作：C/W；答辩卡：A01；状态：planned。

## R1-07 Perceptual 不必经 MIDI 才到 score

- 来源：报告PDF p2；性质：概念问题；优先级：P2。
- 对应论文：Fig2.1 p10 / PDF37；§5.3 p69 / PDF96。
- 处理：加 perceptual→score 的直接路径；层次表示不同概念，不是必经串行管线。
- 工作：C/W/F；答辩卡：A01；状态：planned。

## R1-08 Table2.3 列组三分隔

- 来源：报告PDF p2；性质：可选排版建议；优先级：P2。
- 对应论文：Table2.3 p14 / PDF41。
- 处理：用列间距/分组表头或细竖线区分 1–3/4–6/7–9；遵守全书表格风格。
- 工作：F；答辩卡：—；状态：planned。

## R1-09 velocity 总是 onset 属性吗

- 来源：报告PDF p2；性质：协议范围问题；优先级：P2。
- 对应论文：§2.3.2 p19 / PDF46；§4.5.4 p57 / PDF84。
- 处理：明确研究的是 Note On attack velocity；MIDI 协议还有 release velocity、aftertouch、CC 等不同机制。提交前查正式 MIDI 规范，本文未做外部协议核验。
- 工作：C/W；答辩卡：—；状态：planned。

## R1-10 Fig2.3(e,f) 颜色语义

- 来源：报告PDF p2；性质：图例缺失；优先级：P2。
- 对应论文：Fig2.3 p25 / PDF52。
- 处理：视觉确认存在多色但无色条/图例；必须追查作图源，不能猜是 velocity、pitch 或事件编号；补图例或统一非语义颜色。
- 工作：F/E；答辩卡：—；状态：planned。

## R1-11 humanisation 未定义

- 来源：报告PDF p2；性质：术语建议；优先级：P2。
- 对应论文：§2.5.1 pp26–27 / PDF53–54。
- 处理：给出宽定义（赋予机械符号可感知的演奏变化），再限定本文只改 velocity；不要暗示已改 timing/articulation。
- 工作：C/W；答辩卡：—；状态：planned。

## R1-12 背景补 crescendo/diminuendo

- 来源：报告PDF p2；性质：覆盖建议；优先级：P2。
- 对应论文：§2.3.1 p18 / PDF45；§2.6.1 pp28–29 / PDF55–56。
- 处理：已有背景提及方向性符号；补与五类静态标签的区别，并说明当前模型不识别 hairpin span。
- 工作：W/E；答辩卡：—；状态：planned。

## R1-13 Table2.7 模态、符号、43%

- 来源：报告PDF p2；性质：表格澄清批评；优先级：P2。
- 对应论文：Table2.7 p35 / PDF62。
- 处理：逐一解决：新增 audio 列；区分 performed unquantised MIDI / quantised reference；定义三角表示可用性或可靠性限制；为43%写清分母和模态，须回原数据源核实。不得猜统计含义。
- 工作：F/W/E；答辩卡：—；状态：planned。

## R1-14 集中定义 dynamics 指标

- 来源：报告PDF p2；性质：背景建议；优先级：P2。
- 对应论文：§2.8.2–4 p36 / PDF63；§3.6.3 p45 / PDF72；§5.6.3 pp76–77 / PDF103–104；§6.8.2 pp98–99 / PDF125–126。
- 处理：背景加指标导航表，指向正式定义、单位、评估坐标和能支持的主张；不要混淆 Recall10%、note detection F1、loudness r。
- 工作：W/E；答辩卡：—；状态：planned。

## R1-15 most controlled 不等于更易识别

- 来源：报告PDF p2；性质：任务定位批评；优先级：P0。
- 对应论文：§3.1 p39 / PDF66；§1.5 p6 / PDF33。
- 处理：改 structurally fixed；承认无音频使 expressive target 更欠定，与结构已知是两个独立轴。
- 工作：C/W；答辩卡：A02；状态：planned。

## R1-16 风格/作曲家依赖

- 来源：报告PDF p2；性质：泛化问题；优先级：P1。
- 对应论文：§3.6.1 pp43–44 / PDF70–71；Table3.6 p49 / PDF76；§3.10 p50 / PDF77。
- 处理：报告性能限定为 piano/repertoire；seen/unseen 组是描述性非受控比较，不证明 composer-invariance；分层复核属于可选后续分析。
- 工作：C/W/E；A可选；答辩卡：A04；状态：planned。

## R1-17 image-based 是否成立

- 来源：报告PDF p2；性质：术语批评；优先级：P1。
- 对应论文：§3.2–4 pp39–42 / PDF66–69。
- 处理：用 sparse 2D piano-roll regression；colourisation 是从占用矩阵到 velocity 强度的类比，不是 RGB/颜色通道算法。
- 工作：C/W；答辩卡：A03；状态：planned。

## R1-18 piano-roll 相对 note list

- 来源：报告PDF p2；性质：表示论证问题；优先级：P1。
- 对应论文：§3.3–5 pp40–43 / PDF67–70。
- 处理：解释 pitch×time 的局部复音与卷积先验、mask；承认栅格开销/分辨率，未做同容量 event-vs-roll 因果比较。
- 工作：C/W/E；答辩卡：A03；状态：planned。

## R1-19 velocity recovery 还是 estimation

- 来源：报告PDF p2；性质：目标语义问题；优先级：P0。
- 对应论文：§3.3 pp40–41 / PDF67–68；§3.10 p50 / PDF77。
- 处理：无音频只能给出 plausible completion/conditional estimate，不可能保证唯一恢复原演奏；收窄全文措辞。
- 工作：C/W；答辩卡：A02；状态：planned。

## R1-20 musical time/beat-aligned 输入

- 来源：报告PDF p2；性质：替代设计问题；优先级：P1。
- 对应论文：§3.4.2 pp41–42 / PDF68–69；Table3.4 p48 / PDF75。
- 处理：已做的是物理时间10s/96帧及5/10/15/20s对比；beat-aligned 尚未报告。解释可行收益和额外 beat/tempo 信息，列为可选实验。
- 工作：C/W/E；X可选；答辩卡：A03；状态：planned。

## R1-21 performance MIDI 对量化作曲的迁移

- 来源：报告PDF p2；性质：使用场景批评；优先级：P0。
- 对应论文：§3.1 p39 / PDF66；§3.6.1 pp43–44 / PDF70–71。
- 处理：承认评估保留演奏时值，不能由该结果证明 quantised score 使用场景；弱化该应用结论；受控量化评估属新增实验。
- 工作：C/W；X可选；答辩卡：A03；状态：planned。

## R1-22 Ch3 baseline 独立小节

- 来源：报告PDF p2；性质：呈现建议；优先级：P2。
- 对应论文：§3.6.2 p44 / PDF71；§3.7 p45 / PDF72。
- 处理：列 Flat64、pretrained Seq2Seq、reimplemented ConvAE，训练数据/损失/选择/资源来源差异；不称所有系统同等重训。
- 工作：W/E；答辩卡：—；状态：planned。

## R1-23 隔离 velocity 与联合 AMT 的取舍

- 来源：报告PDF p3；性质：生态效度与替代建模问题；优先级：P0。
- 对应论文：§4.3–5 pp52–57 / PDF79–84；Table4.2 p63 / PDF90。
- 处理：这是 known-note correction；实用但不处理漏错音，未证明优于 joint training 或提升 note F1；承认互相促进的可能。
- 工作：C/W/E；X可选；答辩卡：A05；状态：planned。

## R1-24 Ch4 为何不用 event-based

- 来源：报告PDF p3；性质：表示论证问题；优先级：P0。
- 对应论文：§4.5.1–2 pp54–56 / PDF81–83；Fig4.2 p54 / PDF81。
- 处理：澄清 frame roll 作为 AMT 接口，最终 Transformer 已只 tokenise score onsets；不是全程 dense-grid Transformer。
- 工作：C/W/E；答辩卡：A03；状态：planned。

## R1-25 BCE 与 L1 是否平衡

- 来源：报告PDF p3；性质：loss设计问题；优先级：P0。
- 对应论文：Eq4.6 p57 / PDF84。
- 处理：两个均值项显式系数均1；不同归一化并不保证数值/梯度相等；没有权重消融证据，解释理由并标记可选敏感性分析。
- 工作：C/W/E；X可选；答辩卡：A06；状态：planned。

## R1-26 Table4.1 设置未定义

- 来源：报告PDF p3；性质：实验描述批评；优先级：P0。
- 对应论文：§4.5.1–2 pp54–56 / PDF81–83；§4.6.2 p58 / PDF85；Table4.1 p59 / PDF86。
- 处理：表前定义 audio/onset/frame/frameex、BiLSTM/Transformer、训练更新范围、验证选择、参数；不要把unchanged architecture说成frozen weights。
- 工作：C/W/E；答辩卡：A06；状态：planned。

## R1-27 Ch5 是否接 note-based AMT

- 来源：报告PDF p3；性质：系统整合问题；优先级：P1。
- 对应论文：§5.3 p69 / PDF96；Fig5.1 p68 / PDF95；§5.6.3 pp76–77 / PDF103–104。
- 处理：区分演示工作流与完整系统量化；报告动态/节拍任务不等同已验证 note+score 联合性能。
- 工作：C/W/E；X可选；答辩卡：A05；状态：planned。

## R1-28 为什么显式 change point

- 来源：报告PDF p3；性质：设计动机批评；优先级：P0。
- 对应论文：§5.3 p69 / PDF96；§5.5.2–3 pp72–73 / PDF99–100；§5.7.4 p81 / PDF108。
- 处理：level 是状态、CPt 是稀疏转折；说明目标/后处理，承认从相邻 level 差分可得 baseline，但未报告其消融。
- 工作：C/W/E；X可选；答辩卡：A07；状态：planned。

## R1-29 beat/downbeat 独立头与 Eq5.2

- 来源：报告PDF p3；性质：结构耦合问题；优先级：P0。
- 对应论文：Fig5.2 p72 / PDF99；Eq5.2 p73 / PDF100。
- 处理：共享encoder/experts通过梯度关联；独立gates/heads和相加loss没有显式downbeat⊆beat约束；补图注和局限。
- 工作：C/W/E；X可选；答辩卡：A07；状态：planned。

## R1-30 Ch5 跨数据集是否必要

- 来源：报告PDF p3；性质：评估范围问题；优先级：P0。
- 对应论文：§5.6.1 pp74–75 / PDF101–102；§5.7.3–5 pp80–82 / PDF107–109。
- 处理：用于揭示 acoustic/repertoire/annotation shift，不以普遍composer invariant为前提；解释目标集best-fold选择乐观性（补充风险V-01）。
- 工作：C/W/E；A可选；答辩卡：A08；状态：planned。

## R1-31 simpler route 过强

- 来源：报告PDF p3；性质：措辞批评；优先级：P1。
- 对应论文：§6.2 p87 / PDF114。
- 处理：改 avoids direct target-velocity annotation / task-focused supervision；承认proxy建模和SoundFont选择成本、并未消除所有domain gap。
- 工作：C/W；答辩卡：A12；状态：planned。

## R1-32 V^(0) 与 Vhat

- 来源：报告PDF p3；性质：符号澄清问题；优先级：P0。
- 对应论文：§6.4.1 pp89–90 / PDF116–117；§4.5.2 pp55–56 / PDF82–83。
- 处理：V^(0)为声学粗velocity roll；Vhat为score-informed Transformer后的修正预测；不表示真实标签或两个适配方法。
- 工作：C/W/E；答辩卡：A10；状态：planned。

## R1-33 DDSP-Piano/Guitar-Synth 保真度

- 来源：报告PDF p3；性质：模型有效性问题；优先级：P0。
- 对应论文：§6.4.2 p90 / PDF117；Tables6.2–3 pp99–100 / PDF126–127；§6.9.3 p103 / PDF130。
- 处理：承认renderer mismatch，表中只支持此setting的任务相关效果，不是独立合成器fidelity排名；matched DDSP仍可能更适合。
- 工作：C/W/E；X可选；答辩卡：A09；状态：planned。

## R1-34 Huber 为什么优于/代替 MAE

- 来源：报告PDF p3；性质：loss理由问题；优先级：P0。
- 对应论文：Eq6.6 p91 / PDF118；§6.5.4 pp94–95 / PDF121–122。
- 处理：解释SmoothL1近零平滑、小残差二次/大残差线性；相对MAE不是简单更抗大异常值；无Huber-vs-MAE消融，不声称证实更优。
- 工作：C/W/E；X可选；答辩卡：A11；状态：planned。

## R1-35 Fig6.2 渲染音频来源

- 来源：报告PDF p3；性质：图注澄清问题；优先级：P1。
- 对应论文：Fig6.2 p93 / PDF120；§6.5.4 pp94–95 / PDF121–122。
- 处理：图中teacher target来自SoundFont-rendered audio；与adaptation real-audio target分两panel；方向/版式以现图为准，不照搬报告right side。
- 工作：C/W/F；答辩卡：A10；状态：planned。

## R1-36 能否自动选 SoundFont

- 来源：报告PDF p3；性质：自动化建议/问题；优先级：P1。
- 对应论文：§6.6.2 p96 / PDF123；§6.9.4 p103 / PDF130。
- 处理：当前由耳听小候选集；可在独立验证集比较descriptor/loudness匹配并检查饱和，禁止按test挑bank；尚未实施。
- 工作：C/W；X可选；答辩卡：A12；状态：planned。

## R1-37 完整 AMT 与 note 性能

- 来源：报告PDF p3；性质：整合与效果问题；优先级：P0。
- 对应论文：§7.4.5 p112 / PDF139；§4.5.4 p57 / PDF84。
- 处理：给出future integration路径；已证实的是known-note velocity gains，不冒称pitch/onset F1增益。
- 工作：C/W；X可选；答辩卡：A05；状态：planned。

## R1-38 结论补渐强渐弱未覆盖

- 来源：报告PDF p3；性质：局限/未来建议；优先级：P1。
- 对应论文：§5.7.5 p82 / PDF109；§7.3–4 pp110–111 / PDF137–138。
- 处理：Ch5 已明确只5静态类；在全书结论同步限制；hairpins需起止/方向/持续跨度标签，不把CPt当成crescendo识别。
- 工作：W/E；答辩卡：A07；状态：planned。

