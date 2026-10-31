# 外部独立评阅 C2：主要文字可选，整合前还差两处小修

**七处真实返修均通过事实与语义门槛；20 项当前选文可供作者选择。** 独立重建的 23 项 v4 依赖没有虚构新实验，但其中一项放回完整句子后有重复。N07 的表值完全保留，却仍有一个不适合跨指标共用的方向箭头。建议只修这两处，再做有界核验，不再启动全套候选竞赛。

这不是作者批准或 thesis 实施，也不是对尚缺 run/GT 证据的认证。下面的“可选”仅评价指定版本的提案文字。Reader 的最终整合仍应等待两处修正及其准确绑定。

## 两个具体剩余修改

### 1. V4-R2-04-sync-3：组合后出现 Supported…supported

R2 的实际组合 roadmap 是：

```latex
\textbf{Chapter~3} addresses Scenario~S1. Supported by listening tests, it shows that velocity completion can improve expressive rendering on fixed symbolic notes, supported by objective evaluation and the listening study.
```

这不是 T08 的共著论文说明写错，而是继承的局部替换留下了原句前半部。同一句两次 supported，且 listening tests / the listening study 的单复数不统一，不符合本轮“精简、人类可读”的目标。

最小修正：将该 dependency 的源替换范围向前扩展，包含 `Supported by listening tests, `，新句首用大写 It。不要添加第 45 个有重叠的补丁。

```latex
\textbf{Chapter~3} addresses Scenario~S1. It shows that velocity completion can improve expressive rendering on fixed symbolic notes, supported by objective evaluation and the listening study.
```

保留正面研究结果与证据，不改成只有“研究了什么”的弱化摘要。其余 v4 听测同步可保留。

### 2. N07：去掉 GT−Flat 行的共用向上箭头

当前 proposal 仍写：

```latex
\textbf{$\Delta$ (GT $-$ Flat) $\uparrow$}
```

对 r/cosine，GT−Flat 的正差表示 GT 较高；对 MAE，有利差值为负。一个共同的 ↑ 会误导方向。仅改为：

```latex
\textbf{$\Delta$ (GT $-$ Flat)}
```

**所有数值保持原样。** 58 个 numeric tokens 相同只是必要检查，不能替代方向和文字语义检查。本问题存在于原表、也遗留在 N07 格式副本中；不是新实验结果错误。0.193 与显示端点差 0.192 的舍入提示继续保留为未决，不静默纠数。

建议用新的最终提案副本/整合输入实现上述修正，保留已冻结的 C1/R2 记录与原 thesis。两处准确修正已准备在 evaluator-owned 的 `evaluator_cycle2_dependencies_corrected_proposal.json` 和 `evaluator_cycle2_N07_corrected_proposal.tex`；虚拟组合 diff 为 `evaluator_cycle2_two_repairs.diff`。修正后仍是 44 个无重叠操作、数字全同，核验见 `evaluator_cycle2_repair_verification.json`。这些是已评阅的具体修正提案，没有写入 writer 或论文文件。

## 七处实际改稿：按文字评价，不按回应表打勾

R/V/C/N/H/D = 回应问题 / 作者语气 / 局部与全文衔接 / 小修必要性 / 可读性 / 信息密度。1–4 为序位判断，不求和；编辑提出的问题不冒充 examiner 新要求。

| ID | 语义/事实 | R/V/C/N/H/D | 独立判断 |
| --- | --- | --- | --- |
| T01 | PASS/PASS | 4/4/4/4/4/4 | note content and timing 对应真实回复；data condition 与 training condition 可重叠，定义没有把不可靠标签写成完全无标签。 |
| T03 | PASS/PASS | 4/4/3/4/4/3 | regular grid、simultaneous notes、binary/single-channel 的顺序清楚；比原先接口循环说明更具体。与前后 method 段有轻微重复，但不值得重排章节。 |
| T07 | PASS/PASS | 4/4/3/4/3/3 | on the target recordings 限定了缺少单独测量的范围。observed degradation 在方法节略有前指，但不是需要再改的事实问题。 |
| T11 | PASS/PASS | 4/4/4/4/4/4 | 直接解释 Huber，未建立优势不等于从未做过比较；公式和设置没有丢失。 |
| N02 | PASS/PASS | 4/4/4/4/4/4 | 保留 notes/velocities、改变 rendered sound；明确整个 renderer 干预，无 gain-only 因果或重复数字。 |
| N03 | PASS/PASS | 4/4/3/4/4/3 | 正面说明 r 的用途、降低 absolute-level 依赖及有限 piano diagnostic；第二句与 N01 略重复，但有助于交代选择，不必再压缩。 |
| N05a | PASS/PASS | 4/4/4/3/4/4 | 保留原首句 boundaries，删去防御句；范围不重新分类，是一个确切的 KEEP 胜出。 |

### T01 不需要再为 incomplete 建立第三套术语

审稿人要求定义的是 weakly expressive 与 weakly supervised。前文已经用“missing expressive label layer”说明 incomplete 的普通含义。当前两项定义对作者实际回复足够忠实，再加互斥类别反而需要全篇新增分类纪律。retain timing 指保留给定时间信息，**没有**断言时间未经量化，也没有替听测 timing-preparation 问题提供答案。

### T03 不是一项表示法优越性的实验结论

新的 note-list interface 句只描述所选二维网络与表示的接口差异。没有声称 event models 已被公平比较并输掉。原有 F input / V target / O mask 以及矩阵尺寸继续保留。这里允许略长，是因为增加了必要理由，不用字数下降证明质量。

### T07 / T11 保留真实作者的认知边界

T07 只说 degradation 与 mismatch 相容，未独立隔离 fidelity/gradient mechanism。T11 只说尚未确立 MAE 优势。两者都没有把“未找到有力比较证据”变成“历史上从未做过实验”。作者 PDF 批注仍是依据，版本与运行记录仍待核实。

### N02/N03 合并用途句是合理的实际返修

Writer 没有逐字复制 C1 两段建议，而是将 correlation 的用途只放到 N03，避免相邻重复。这个取舍更适合连读，内容没有丢失。r 的数学性质和本表的有限观察分开表达；没有把 guitar 的 loudness agreement 写成 physical velocity truth。

## 其余选文、KEEP 和继承依赖

**以下 20 个选文 ID 均可供作者选择：** T01–T11；N01–N04；N05a/b/c；N06a/b。这里 T01–T11 包含全部十一个 T 项，不包括任一旧候选版本的自动批准。

- T02 保留 aligned notes、S2 extension 与 S3 不同输出；没有添加 audio-only guitar-velocity 实验。
- T04 一句补足 joint-modelling evaluation 边界；T05 区分 boundary/state 监督，未虚构独立 head ablation 收益。
- T06 保留 real-audio adaptation 和 renderer limitation；T08 区分共著研究与 thesis synthesis，未声称完成 exhaustive novelty inventory。
- T09 保留 Second 及 piano/guitar 证据范围。连续控制需要其他 descriptors 的句子应按 sustained/continuous modelling 理解，不扩大成其他乐器连 onset-level approximation 都不可能。
- **T10 继续保留 v4**，具体比较对象、reference similarity 和 11/8/one rendering 均有源文依据，不为可选偏好换稿。
- N01 的有限诊断表述、N04 的 can-divert、N05b/c 的去防御句，以及 N06a/b 删除未验证完整乐句解释均可用。
- **KEEP-FIG62 继续保留原图注/原图。** 原文已明确 SoundFont-rendered targets，不能因此确认 Fig6.3 GT。

23 个依赖均已逐条对照源文和既有 v4 提案。**22 个可原样进入选择；`V4-R2-04-sync-3` 需上方组合语境修正。** 该项事实内容通过，但重复表达不宜作为最终阅读文本。

| 依赖组 | 精确 ID | 结果 |
| --- | --- | --- |
| 引言 velocity | V4-velocity-1…8 | 可选；control 与 renderer effect 同步，删除 mf 物理默认的无依据句。 |
| 输入与输出范围 | V4-scope-1/2 | 可选；S3 联合估计 metrical coordinates，Chapter 6 是 guitar velocity。 |
| 动机 | V4-motivation | 可选；reduce need 保留价值而不声称绕过全部采集/标注问题。 |
| S1 表述 | V4-S1-opening；V4-R1-15-sync-1…4 | 可选；不再把固定 notes 与有 acoustic evidence 的信息约束混为一谈。 |
| 听测 | V4-R2-04-sync-1/2/4 | 可选；assessed、reference similarity、Flat/ConvAE 均准确。 |
| 听测 roadmap | V4-R2-04-sync-3 | 需组合句修正；不重新开展听测。 |
| DDSP | V4-R1-33-common-1…3 | 可选；保留 0.083/within 0.01 观察，mechanism 不再被写成独立证实的因果。 |

N07 当前不作无条件接受，修掉箭头后再核验同一数字序列即可。N01–N03 的主要解释可选，但最终 reader 的一致性组不能混入未修的 N07。

## 独立工具核验

`evaluator_cycle2_verify.py` 从 source 原句和插入位置重新构建操作，未运行 writer builder，也未改任何论文文件：

- **44 个操作** = 4 insertion + 16 replacement + 23 inherited dependency + 1 table-format replacement。
- 所有 source quotations 唯一匹配，插入位置独立推导，零重叠；与 writer manifest 的实际范围/替换内容一致。
- **全部 20 个 `reinserted_context_r2`** 都是独立组合文本的精确子串。旧 `reinserted_context` 是冻结的上一版预览，不能混作 R2。
- 修改恰为七个指定 ID；其他选择没有悄悄改动。
- 六张 reader card 的原文、推荐英文、KEEP 及 followthrough 引文都准确；N01 卡确实组合 N01/N02/N03。
- 19 个源文件、80 个旧提案文件 hash 不变，C1 writer 冻结快照也未变。

核验结果见 `evaluator_cycle2_verification.json`。程序匹配证明操作一致性，不证明实验、数据 provenance 或每个未修改章节的全部论断。

## Reader 整合要求：与作者批准分开

R2 输入正确标记仍待外部 C2，23 项依赖也明确为 unapproved preview assumptions。六卡是精选阅读入口，**不是 44 项可执行决定 manifest**。请保留只读查看语义。

1. **先修上方两处，再绑定最终输入 hash。** 不要只将 pending 字段改 false；完整一致性组应来自实际修正后的文本。
2. **更新适配器的来源。** 当前 provisional adapter 仍读取冻结 `FINAL_SELECTION.json`。最终应取修正后的 R2 版本、`reinserted_context_r2` / `contextPreview`，不能混入旧字段或旧五卡。
3. **显示依赖边界。** N01 是三段解释＋N07＋N04 的五范围一致性组；N05b/c 是独立可选小修，不因查看/选择 a 自动采用。上下文预览中的其余 v4 依赖不继承旧 YES。
4. **把内部审查话语移出第一屏。** R2 `short/why` 仍有“接受可选精简”“旧 v5 并非确定错误”“接受实质合并”等过程记录。保留在 writer response；读者入口改说实际价值。例如：

   - T11：解释为何使用 Huber，同时保留尚未证实优于 MAE 的边界。
   - T03：说明 piano roll 与二维 U-Net 的对应关系，明确 colourisation 是补 velocity 的类比。
   - T01：区分力度信息被简化的数据，与缺少可靠标签的学习条件。
   - N05a：保留研究范围，只删替论文辩护的句子。

5. **共同复核不等于作者同意。** `jointly-reviewed-v5` 只能说明 writer/evaluator 对指定文字达成一致。author approval、implementation、run/GT verification 保持独立；界面不保存浏览选择，不写 DECISIONS。

完整最终 reader 尚未做本轮 UI/交互验收；本次只检查了输入与 provisional 模板语义，不能沿用旧五卡测试宣称新六卡已通过。

## 状态与下一步

主要正文提案可选；请 writer 确认是否采用已备好的 **V4-R2-04-sync-3 Supported 重复修正**和 **N07 共用 ↑ 删除**。若采用准确修正文件，只需整合后的 hash/范围有界核验及最终 reader 测试，无需第三次全套语言循环，也无需新实验。此处是 writer/evaluator 的提案协调，不是再次向作者索取批准。

正式送审基线、R1-13/21/26/30、run/checkpoint/table provenance、guitar GT 与最终 ICASSP 版本继续开放。本次没有 source edits、作者批准、编译、实验、commit/push、上传或 publication。
