# 先看这里：这轮返修值得改什么

我的判断是：**以局部澄清为主，保留现有章节结构、实验和核心问题。** 最值得改的是“模型拿到什么信息、为什么这样设计、结果支持到什么程度”这几处解释。已有导语、公式、参数和实测结果都不需要为了回应评审而重写一遍。

下面是原段与拟段的节选，完整替换范围可展开查看。**正文尚未修改；YES只确认明确的提案。** 选择统一记在 [决定清单](DECISIONS.md)，这一页只帮助阅读。

## 1. 把场景说准，主线继续保留

评审质疑“most controlled”：没有音频，不代表信息最充分。你原本想说输入信息更少，也已同意换词。推荐只修正描述条件的首句，保留后面“固定音符与时间、补回velocity”的提问。

**原文：** “This chapter addresses Scenario~S1, the most controlled setting in the thesis map.”

**拟稿：** “This chapter addresses Scenario S1, where only symbolic information is available.”

同组补清 weakly expressive／weakly supervised 定义、Ch6与S2的关系，以及四篇研究怎样组成thesis。已有章节首尾导语继续用。[查看这组改动与决定位置](CHANGE_CARDS_v2.md#framing)。

## 2. 在读者会停下来的地方，补具体解释

**Piano roll：** 评审问“为什么是image-based，为什么不用note list？”你原答复已说清二维矩阵和单通道输出。推荐把这个理由写进正文，保留正式paper题名。

原段节选：“By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly.”

拟段节选：“The output is a single-channel velocity roll. We use colourisation as an analogy for completing that missing scalar layer, rather than for predicting RGB colour.”

**Hybrid loss：** 评审问两项怎样平衡。你说沿用Kim，并验证过。推荐直接回答：**每项各自平均后，以相对1:1合并**；完整稿保留公式、Kim引用和SMC已有的初步比较。

原段节选：“This hybrid supervision is useful because it constrains both the local onset value and the broader note sustain region, while still keeping note-level precision central to the objective.”

拟段节选：“The frame-wise BCE and onset-wise L1 terms are averaged over their respective active positions and combined with equal relative coefficients.”

这些是解释上的改善。实际run配置仍按记录核对，不由一个文字YES代替。[查看方法、图表与接口这一组](CHANGE_CARDS_v2.md#explanation)。

## 3. 保留结果，把结论落在实际测量上

评审认可听测的价值，希望明确它提供支持性证据；未找到你对此条的既有回复。推荐保留 **U-Net平均similarity高于Flat和ConvAE、Flat最低** 的观察，把“clearly outperforms”说得更具体。

**原文：** “Although a substantial gap to human performance remains, the proposed U-Net clearly outperforms the other systems.”

**拟段节选：** “U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts…”

完整稿再集中说明11位听者、8个片段、一个PianoTeq配置；MOS表和置信区间保留。同样处理Ch6：实测退化和数值保留，对原因的解释与“已证明原因”区分开。[查看结果解释这一组](CHANGE_CARDS_v2.md#claims)。

## 4. 说清用途和下一步，保持minor revision的范围

评审不认同“simpler route”。你原拟换成“more efficient”；我更推荐描述具体路径，因为现有材料没有成本比较。

**原文：** “This chapter takes a different and simpler route.”

**拟稿：** “This chapter takes a more direct route to target-domain adaptation.”

完整段保留用real recordings减少目标velocity标签依赖的动机，也交代renderer的要求。完整AMT集成、自动选SoundFont、渐变记号和其他乐器，则作为短而具体的适用边界／未来方向。[查看范围这一组](CHANGE_CARDS_v2.md#scope)。

## 哪些可以直接保留

已有chapter overviews、正式paper题名、loss公式、复现参数及有效定量观察优先保留。数字制引用也可以保留，是否切换author–year由你单独选。`recollecting → collecting`等小修合并看；合并包也含baseline整理和VeloEst解释，先看准确差异再决定。[小修与单一方案合并包](CHANGE_CARDS_v2.md#small)。

## 你现在怎样决定

按上面四组阅读即可；组号只是导航，不是笼统批准。只在 [DECISIONS.md](DECISIONS.md#完整追踪表) 的对应条目填YES／NO；按行内说明填写；需比较多稿的填版本，已明确唯一稿或局部范围的无需再选字母。R1-18随R1-17，R1-37随R1-27的Ch7稿，避免同一段选两次。组合稿和事实待核项的批准范围已写在各行。

现在最有用的一项材料确认是：**哪份文件是学校实际收到的送审版本？** `main.pdf`与`Z_He_PhD_Thesis.pdf`内容有差别，影响最终report的前后对照。[填写基线](DECISIONS.md#submission-baseline)。这不阻止先选文字。

量化MOS的原说明保留；input/reference处理、最终run与表值来源、吉他图GT和最终ICASSP稿，先由我们继续查已有记录，缺材料时再请你指出位置。四项待核里可先选的文字与仍冻结的事实已分开列在 [这里](CHANGE_CARDS_v2.md#pending-scope)，完整核验目录仍在 [决定清单](DECISIONS.md#事实确认)。

[GRS回复初稿](GRS_REVISION_REPORT_DRAFT.md)已留好逐条框架，等你的选择和实际修改确定后，再写成正式完成式说明。
