# Zhanhong He — Defence & revision blueprint

2026-10-22（答辩时区UTC+08:00；确切时间未知）。这是答辩/小修规划，未改论文、未启动Ultra。

**先读 [TODAY_DEFENCE_BRIEF.md](TODAY_DEFENCE_BRIEF.md)，再练 [12张答辩卡](ORAL_ANSWER_CARDS.md)。** 每卡都有30秒核心、1–2分钟英文扩展、中文解释、论文证据、限制和修改计划。

两份报告基调积极：R1 Dr Emmanouil Benetos（正文与签名确认）批准进入viva、excellent/top25%（报告p3）；R2建议Pass with minor revisions、overall2 Excellent，明确无需新数据/新实验/大改（p1/4）。这均是preliminary recommendation，不等于最终答辩结果。R2正文无署名，PDF Author=Waleed Abdulla仅作待确认元数据。

## 使用顺序

1. 今天：[TODAY_DEFENCE_BRIEF.md](TODAY_DEFENCE_BRIEF.md) → [ORAL_ANSWER_CARDS.md](ORAL_ANSWER_CARDS.md)。
2. 小修：[THESIS_REVISION_BLUEPRINT.md](THESIS_REVISION_BLUEPRINT.md)。
3. 完整追踪：[combined matrix](COMBINED_RESPONSE_REVISION_MATRIX.md)；[R1全部38项](R1_COMPLETE_ISSUE_INVENTORY.md)、[R2全部5项](R2_COMPLETE_ISSUE_INVENTORY.md)。含全部小问题，区分问题/批评/可选建议，状态都是planned。
4. 开Ultra时才复制：[ULTRA_EXECUTION_PROMPT.txt](ULTRA_EXECUTION_PROMPT.txt)。要求重读两报告和完整论文、逐项回应、保留原件、change log，不臆造实验。
5. 检查边界：[READING_COVERAGE.md](READING_COVERAGE.md)、[补充核查缺口](appendix/VERIFICATION_GAPS.md)、[source manifest](SOURCE_MANIFEST.json)。

## 需要作者优先核查的三处

- Fig6.3的guitar GT标签来源（p101/PDF128）尚未证实。不得猜测其是真实测量、合成control或pseudo-label；可能需收窄/移除依赖主张。
- Ch5外部结果按target dynamic F1挑best transferred fold（p75/80；PDF102/107），应称乐观transfer diagnostic。
- Ch4 frozen/jointly trained文字不一致（p28/58；PDF55/85），须查训练记录，不把架构不变说成权重冻结。

## 已核实本机路径

原始源副本：`/Users/jollibear/Documents/PhD_Thesis_Source_20261022`

规划包：`/Users/jollibear/Documents/PhD_Defence_Blueprint_20261022`

打包文件：`/Users/jollibear/Documents/PhD_Defence_Blueprint_20261022.zip`

仓库：`https://github.com/zhanh-he/phd-thesis`（gh核实public/main）；commit：`7e319875a8b1e9fc8f6a0afa4dc4417b03212226`。未改可见性、权限或上传原始报告。

| 原始文档 | 页数 | bytes | SHA256 |
|---|---:|---:|---|
| Zhanhong_He_PhD_Thesis_v0.pdf（主证据） | 154 | 14835628 | 3479394740921480c1325c70cc343eaea9e5d09df174be449415a9c8dacb4798 |
| Preliminary_Report_PhD_thesis_Zhanhong_He 1.pdf | 4 | 225062 | 8a9412c1401a41a5b4f82865faf759f255a20f03cf7997d92be0278a3a582e78 |
| Preliminary_Report_PhD_thesis_Zhanhong_He 2.pdf | 4 | 118876 | c9d8a2a843e3c9cd167e751ed0dec8f7cd7ca757a6a8fabea2abc747b1c61020 |

还有Z_He_PhD_Thesis.pdf和main.pdf，均154页但hash/部分内容不同；源码LaTeX齐备，未编译验证与v0一致。正文印刷p1–112对应PDF28–139；前置页不能套此偏移。

本次完成两报告全文和全部8页视觉检查，论文Ch1–7正文文本与23关键页视觉检查；未宣称全154页逐页视觉校对、未核验参考文献或重新跑实验。规划zip只包含规划/清单/manifest，不含原始PDF、完整报告转写或图像缓存。未上传Library；如需分享，仅分享本规划并保持owner-only。
