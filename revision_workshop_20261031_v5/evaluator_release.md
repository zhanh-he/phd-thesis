# 有界交付核验：PASS

最终文字包与实际六卡 reader 均通过本次检查，未发现需要继续返修的内容、选择语义或阅读缺陷。可以交付给作者阅读和选择；不代表作者批准、论文正文实施或 run/GT 认证。

## 内容与范围

- 最终 packet 的 SHA-256 与指定值 `9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17` 一致。
- 两项 C2 修正准确采用：roadmap 不再 Supported…supported；N07 删除共用 ↑。
- 20 项选文英文 hash 全部保持 C2 接受版本；23 项依赖匹配 evaluator 的准确修正版。
- 44 个操作无重叠；八个组合文档 hash 全部对应 evaluator 的 corrected overlays；全部 58 个 table numeric tokens 保持原样。
- 六条 highlights 的 before/after 引文及标签准确。T11 的旧“did not conduct”标作 v4 提案而非作者原话；T01 长定义也标为 v4 解释稿。
- 19 个源文件、80 个旧提案文件 hash 不变，包含原 DECISIONS；交付 manifest 的 12 个文件 hash 全部匹配。

程序证据：`evaluator_release_content_verification.json`；可复跑检查：`evaluator_release_verify.py`。另一个本地 source reviewer 也独立完成上述限定范围核验，未报告差异，不算新增一轮风格审查。

## 实际阅读与交互

开始时 `reader/index.html` 仍是旧五卡；我没有把旧结果算作最终验收。整合完成后，实际通过本机 Chrome 的 CUA 进入最终 `file:` 页面，逐卡阅读 **T11、N01、T03、T01、N05a、KEEP-FIG62**，读取 AX 并检查截图。

- **原文与来源：** Huber 左侧是当前 `.tex` 原句，展开后 examiner question、真实作者回复和编辑建议分开。没有将 v4 提案写成作者原话。
- **KEEP 与备选：** Huber 的 KEEP 两侧原文相同；T03 的 GRID 真实切换且明确标为备选，组合预览不会悄悄随备选变成另一组已批准文本。
- **插入：** T01 明确显示原问题保留、定义插在其后，没有伪装为替换中心问题。
- **同步：** N01 展开后能读三个解释段、N07 表格和 N04 背景从句；五范围一致性组清楚可见。
- **v4/v5：** T01 相邻语境说明绿色为本轮 v5、蓝色为沿用 v4，其余为原文，明确是未实施的组合示例。
- **独立可选：** N05b/c 各有 v5 编号，明确“不随本卡自动采用”；没有从 a 推导对 b/c 的同意。
- **真正保留：** Fig6.2 明确为既有 v4 KEEP，两侧图注相同，不新增 v5 决定，也不解决 Fig6.3 GT。
- **不自动保存：** 实际操作关键词筛选、KEEP、GRID、刷新、重置。刷新后搜索清空、Huber 恢复推荐、T03 不再保留先前 GRID 浏览选择；没有批准动作或 DECISIONS 写入。
- **首屏：** 理由已是实际价值说明，内部“接受返修”等记录没有占据第一屏。桌面截图可读；另独立查看 integrator 的 narrow top/text 截图，未见实质水平溢出或重叠。

直接阅读证据与最终 HTML hash：`evaluator_release_reading_test.json`。本次 CUA 截图保留在该评阅对话中；另可检查 reader 生成并保存的：

- `reader/evidence/final-desktop.png`
- `reader/evidence/final-context.png`
- `reader/evidence/final-metrics.png`
- `reader/evidence/final-defensive-prose.png`
- `reader/evidence/final-narrow-top.png` / `final-narrow-text.png`

## 离线和状态纪律

页面以本地文件加载；template 没有 fetch/XHR/WebSocket/beacon 或 storage API，CSP 为 `connect-src 'none'`。Integrator 的实际浏览器回归记录为 94 项检查、runtime errors 与 external requests 均为空；本次另独立观察到刷新不持久化选择。测试记录与所看 HTML 的 hash 均已绑定到 release evidence。

工具导航曾有一次 native typeText 丢失 URL 标点，Chrome 搜索了错误的本地路径；随后用 paste、先核对 AX 地址再进入正确 `file:` 页面。这是测试工具导航问题，不是 reader 发出的网络请求；未输入或上传 thesis 正文。这里不把整个浏览器导航过程伪称为零外部请求。

**没有剩余交付缺陷。** 正式送审基线、R1-13/21/26/30、run/checkpoint/table provenance、guitar GT 和最终 ICASSP 版本仍开放。本次 PASS 不关闭这些科学证据问题，也不改变作者决定。未改 source、writer、reader 或旧评阅文件。
