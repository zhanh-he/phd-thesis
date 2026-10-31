# v5 writer packet 接入准备 · 仍待外部独立评审

[暂定只读预览](provisional.html)与原 [index.html](index.html)分开。页面头部、每卡和候选菜单都写明待独立评审；没有将 writer 内部 C1/C2 记录视为父级独立评审已接受。未改任何 writer 英文或来源文件。

## 实际核对

writer 输入是**六张精选卡**，不是15张。15组 tournament 项、N05/N06小修及表格提案在完整材料中，当前原 `FINAL_SELECTION.json` 共20条。六处原文均在源码中唯一匹配，行号正确；现有四个源码 hash 全匹配。V5候选均逐字对应 FINAL_SELECTION；N01三段恰为N01/N02/N03拼接。N07表格和N04背景从句也逐字匹配。GRID是T03 FRESH_1备选，需要另指向C1来源。

[writer_packet_ingestion.json](evidence/writer_packet_ingestion.json)记录逐项结果及来源 SHA；适配 packet 额外冻结必需同步的Ch2，以及writer选择、完整稿和内部评阅等16个输入文件。`selected_passages_c2.json` 的N01是修复前快照；新适配只取 FINAL_SELECTION 的修复后版本，未擅自改字。

## 已处理的接入缺陷

- writer 的 `optionNotes` 是字符串，而旧UI按选项字典读取：已转换展示结构，保留“尚未绑定v5批准入口”原说明。
- `decisionPath` 都指旧通用DECISIONS，T11/N01不是其中有效v5决定行：链接明确历史参考；已知旧ID显示R1-34／17／05／35，新稿批准范围尚未加入，不声称可批准新稿。
- `reviewerComment` 有摘要、`authorResponse` 有编辑状态，不能统称原话：已有评审项接入真实COMMENT_MAP原文；新发现改用“编辑发现摘要／立场记录”标签，writer摘要保存在数据中。
- `pending` 全是共同工作状态，不能将六卡都筛成科学事实阻塞：共同状态移到全局／来源说明，不冒充逐卡事实条件。
- N01按五个范围展示：Ch6三段＋N07表格＋Ch2N04。KEEP说明覆盖全组，不只保留主段。
- N05a/b/c是三处可独立保留的小修：b/c明确是独立可选，不从a继承批准；查看a的KEEP仍能看到b/c。
- 旧 `short===why` 导致重复，已避免重复渲染。T01的79→45词比较明确是旧v4提案，非thesis现有定义。

## 15项怎样保持好读

保持六处优先导航、一次只看一处。完整15组按“新发现／解释更短／旧稿胜出”放在默认关闭的来源索引；没有把15段、评分表或内部审查流水铺到首屏。原文、替代稿、整组同步范围与证据按需展开。导航短说明最多两行，完整说明在当前卡。

## 验证与下一步

待定预览单独通过51项真实Chrome检查；[桌面](evidence/provisional-desktop.png)／[窄屏](evidence/provisional-narrow.png)截图已实际查看，零运行异常、零页面外网请求，旧index hash未变。[验证JSON](evidence/provisional_browser_validation.json)。这只验证UI与准确接入，**不表示英文质量已通过父级独立评审**。

`prepare_writer_packet.py` 生成专用 `provisional_v5_packet.json`；`build_reader.py` 只有带 `--allow-provisional` 且输出为另一个文件时才允许暂定状态，禁止覆盖index。最终需父级提供评审一致后的准确packet/评阅范围；不要只改一个status就宣传通过。替换新文字后重新做逐字来源与界面复测，不沿用本轮51项算给下一版。
