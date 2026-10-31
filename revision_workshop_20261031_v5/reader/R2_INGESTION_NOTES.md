# R2 接入准备 · cycle2 结论未确认

最新暂定页：[provisional_r2.html](provisional_r2.html)。[历史示例](index.html)和[上一版暂定页](provisional.html)保留原字节，未更新为R2。R2页面没有宣传为共同定稿。

新稿请用稳定 **v5-ID＋R2／KEEP** 回复；旧清单只作历史对照，旧YES不转移。T03也可比较GRID。N01是明确五范围一致性组；N05b/c各自保留独立编号，不随a自动采用。Fig6.2为沿用v4的KEEP，不要求重复选择。

## 准确核验

- `FINAL_SELECTION_R2.json`20项＋`DEPENDENCIES_R2.json`23项＋N07，共44个操作，ID唯一、源偏移准确、范围无重叠。
- 四处插入T01/T02/T04/T05逐项核对真实问句／table／段落结束边界；不是只因空范围而通过。
- 七个R2改稿T01/T03/T07/T11/N02/N03/N05a，before/after分别精确对应冻结旧选稿与R2选稿。
- Huber候选准确包含：`We have not established an advantage over MAE.`，不再有`through a dedicated comparison`。
- 全部23项v4新文字都存在于对应旧来源，旧文字唯一匹配源码。整合器没有改写任何候选。
- 五处整段`contextPreview`均为独立重建完整组合源后的唯一准确切片；不使用JSON中保留的旧`reinserted_context`。额外列出同语境其他v5提案，避免`contextDependencyIds=[]`被误读为其他内容已实施。

[接入检查JSON](evidence/r2_packet_ingestion.json)保存44个源操作、插入位置与26个冻结输入SHA。`prepare_r2_packet.py`只在reader内生成`provisional_r2_packet.json`。

## 阅读与决定安全

首屏六处精选、完整15组按需索引，一次看一段。返修过程中的“接受实质合并”等内部日志不放在标题，用简短中文阅读说明；原writer说明仍保留在数据中。英文逐字不变。

展开相邻语境：绿色为v5提案，蓝色为沿用v4提案，原文无底色；每处依赖能展开准确old/new和有版本范围的历史选择。组合预览固定为R2，查看KEEP／GRID时不冒充已经重算它。显示其他未批准提案ID；本卡KEEP不批准或拒绝其他依赖。

旧DECISIONS链接始终标明历史参考，不作为T11/N01等新稿的批准行；回复说明用`v5-T11（R2／KEEP）`等稳定身份。没有可编辑新ledger、localStorage、自动保存或自动批准。writer返修回应标成“非评审结论”，实际外部C1另链；真实批注链接使用正确R1编号。

## 浏览器验证

[73项真实Chrome检查](evidence/r2_browser_validation.json)通过，零运行异常、零页面外网请求。包含稳定v5编号及独立小修编号搜索、历史链接/回复语义、原文候选精确性、Huber新句、五处准确组合语境、v4独立标色、KEEP范围、N05独立子项、窄屏无溢出与旧HTML未变。

截图已实际查看：[桌面](evidence/r2-desktop.png) · [v4/v5上下文](evidence/r2-v4-context.png) · [窄屏](evidence/r2-narrow.png)。这些结果证明接入和UI，不代替外部cycle2对写作的判断。

## 下一步

等待父级提供真实`evaluator_cycle2`结论与最终一致packet，再接入主入口并重做对应复测。当前生成器刻意保留pending；不自动读到任何cycle2文件就改状态，不编辑作者现有决定清单。正式送审基线与原事实待核项仍保留。
