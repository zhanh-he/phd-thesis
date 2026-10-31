# 博士论文返修简明预览

Zhanhong He · Recovering Musical Dynamics for Expressive Automatic Music Transcription

39项文字已可供你选择，4项仍需证据才能定稿。所有修改仍是提案，thesis正文未改；可选不等于已批准，也不等于已执行。

已完成两轮独立审查和第三轮定点核验。最后的R1-33保留0.083、0.01和2s／5s的结果，只删除过强机制断言，并将未测风险改为“may therefore absorb”。下面展示可以直接判断的实际修改。

| 意见／建议路线 | 具体改善 | 实际英文节选 |
| --- | --- | --- |
| [R1-05 B](RECOMMENDED_PREVIEW.md#r1-05)；文字可选 | 定义与信息条件 | In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. |
| [R1-15 A](RECOMMENDED_PREVIEW.md#r1-15)；文字可选 | 保留原声，取消难度排序 | This chapter addresses Scenario S1, where only symbolic information is available. |
| [R1-17 B](RECOMMENDED_PREVIEW.md#r1-17)；文字可选 | image-like 的技术含义 | The output is a single-channel velocity roll. |
| [R1-21 A](RECOMMENDED_PREVIEW.md#r1-21)；应用段可选，协议待核 | composition 接口 | The composition use case is to add a velocity profile while retaining the notes and timing supplied by the user. |
| [R1-25 B](RECOMMENDED_PREVIEW.md#r1-25)；文字可选 | loss 的实际相对权重 | Equal coefficients do not imply equal numerical loss or gradient magnitudes. |
| [R1-32 A](RECOMMENDED_PREVIEW.md#r1-32)；文字可选 | 符号与 adaptation 范围 | The architecture is retained during adaptation, while VeloEst parameters are updated and the synthesis or proxy back-end remains frozen. |
| [R2-02 B](RECOMMENDED_PREVIEW.md#r2-02)；文字可选 | 四研究与 thesis 综合 | The thesis brings these studies together through a common label-recovery formulation and scenario map, provides shared background, and synthesises their assumptions and limitations in Chapter 7. |
| [R2-04 A](RECOMMENDED_PREVIEW.md#r2-04)；文字可选 | 听测结果与适用范围 | The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. |

## 你怎样决定

只在DECISIONS.md填写。采用当前方案：填YES和对应版本；不采用当前方案：填NO；希望换写法：选另一版本或填自定并留一句备注。YES不触发修改正文。常规小修可用v3包批量选择，共用段落只选主项。

旧版选择没有自动转给第三轮。现有chapter overviews、正式paper题名、loss公式和VeloEst配置优先保留；数字制引用也是可保留的选项。

## 四项事实待核

这些是既有材料或记录问题，局部英文可以选择，不要求新增实验。

| 意见 | 已可选择的部分 | 定稿前需要的记录 |
| --- | --- | --- |
| R1-13 | 字段和图注的表达可选。 | ATEPP 43% 对应版本与分母；各行 Audio／velocity provenance 的原资料。 |
| R1-21 | composition 用途与训练来源的应用段可选。 | 八个 input／reference 的 timing、grid、duration、系统间共用处理；作者量化 MOS 陈述保留，Q/P 未选。 |
| R1-26 | O/F/Fex 与两类 correction module 的解释可选。 | onset-only 实际输入形状、parameter-count 覆盖范围及对应 run／计数依据。 |
| R1-30 | combined corpus transfer 的目的段可选。 | 最终 evaluator、macro／weighted F1、checkpoint／共同 fold 与表值来源；书面披露不能代替核实。 |

## 其他仍开放的来源核验

39项文字可选没有关闭以下问题。先查现有材料；记录仍缺时再由作者确认。

| 核验组 | 仍需确认 |
| --- | --- |
| V-01 | 正式送审是哪一份 PDF／源版本？请以提交记录或作者确认绑定；最终页码与 GRS 模板仍待核。 |
| V-02 | 听测 input 与 reference 各自怎样处理 timing、grid、duration？优先查既有刺激及生成记录。 |
| V-03 | Ch3 实际 run 的 mask、channels、loss 轴／归一化、attention window／partition 配置是什么？ |
| V-04 | Ch4 的 frozen／joint training、theta／整体尺度、onset-only 形状、参数计数及 SMD 开发用途对应哪些记录？ |
| V-05 | Ch5 最终各表对应哪个 evaluator、F1 平均、checkpoint／fold、normal／advanced decoder 分支？ |
| V-06 | Fig6.3 所谓 guitar GT velocity 来自哪个片段／生成过程，是真实标注、合成控制或其他 reference？ |
| V-07 | 请确认最终 ICASSP 发表稿或提供稿的用途；含占位的版本不能确定逐结果 published／adapted／thesis-new 归属。 |

## 深入材料

- RECOMMENDED_PREVIEW.md：8处拟选片段，含原句、完整上下文和操作范围。
- writer_round3.md：全部43项与97条候选路线；冻结版本，最终核验见reviewer_final.md。
- DECISIONS.md：唯一YES/NO、版本、备注与事实确认清单。
- GRS_REVISION_REPORT_DRAFT.md：43条英文说明稿，保留待决定／待修改／待核验；正式report最后按实际差异写完成式。
- COMMENT_MAP.md／editor_crosswalk.md／SOURCES.md：原评审、作者原回复、编号、版本和证据边界。

精简ZIP保留上述提案与审查历史，排除大体积证据和源文件副本。本摘要可独立阅读；解压后与这些文件放在同一目录，可打开深入链接。
