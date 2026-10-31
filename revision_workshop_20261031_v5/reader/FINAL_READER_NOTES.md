# 最终阅读器核验

入口为 [index.html](index.html)，直接file://打开，无需localhost或网络。此页是writer/evaluator对指定文字达成一致后的最新提案，不表示作者已选择、正文已实施，或run／GT已认证。

## 准确版本

使用 `READER_PACKET_REVIEWED_v5.json`，输入SHA256固定为 `9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17`。最终20项选文hash逐一对应cycle2接受记录；扩展roadmap范围和N07去箭头两项准确修补已获writer确认。最终八份虚拟组合文档hash与独立评阅的修正后hash相同，仍为44个不重叠操作。没有额外改写英文。

`prepare_final_packet.py`与`final_agreement_checks.py`核对准确输入、writer交付清单、两处差异、选文／dependency／table／context来源后，生成 `reviewed_v5_packet.json`。`build_reader.py`只作转义、句级差异和单文件嵌入；差异比较忽略句末空白的纯显示差别，但DOM文字逐字保留。N01首屏只显示第一段，并明确这是五范围一致性组，完整内容可展开。

[准确接入检查](evidence/final_packet_ingestion.json) · [构建核验](evidence/build_validation.json)。

## 阅读与选择范围

首屏只放六个实际例子及简短理由，没有内部评分或轮次计数。桌面并排，窄屏原生段落选择器＋上下对照。原段、候选、KEEP、表示模式、增删标记、筛选与全文／证据按需展开。

- `v5-N01`明确覆盖三段解释、N07表格和Ch2 N04，共五范围；KEEP也覆盖完整组。
- `v5-ROADMAP`在“同步范围与沿用项”可展开或直接搜索。它已扩展源范围，属于本轮新修正；不借旧R2-04行批准，也不再当作原样沿用的v4。
- 其他22个原样v4依赖只作有版本范围的对照；不要求再填第二套选择。
- N05b/c各自独立，不挂作N05a的自动followthrough。固定连读中的T09等其他提案也保持独立。
- 旧DECISIONS链接明确为历史参考；作者可用稳定v5编号及方案回复，之后由协调者明确同步。`v5_scope_mapping.json`只是准确ID到范围的只读映射，无作者选择字段。

没有保存或批准按钮、localStorage、表单或第二份可编辑ledger。临时查看状态只存在于当前页内存；重置、重载或另一标签页不会修改作者决定。

## 实际界面测试

最终页面独立跑 [94项真实Chrome检查](evidence/final_browser_validation.json)，不是复用旧五卡结果。覆盖所有推荐／备选／KEEP反复切换的逐字文本，插入与完整连读、v4/v5区别、两处修补、独立可选范围、稳定ID及ROADMAP搜索、空结果恢复、全局重置、键盘Tab/Enter/details、模式切换、双标签页及重载、390px窄屏无横向溢出。零页面外网请求、零运行异常。

截图均实际查看：[桌面首卡](evidence/final-desktop.png) · [piano roll](evidence/final-piano-roll.png) · [指标](evidence/final-metrics.png) · [防御句删改](evidence/final-defensive-prose.png) · [v4/v5连读](evidence/final-context.png) · [窄屏首部](evidence/final-narrow-top.png) · [窄屏文字](evidence/final-narrow-text.png)。

旧首页逐字归档为`legacy_v3_v4.html`，两份provisional页面仍保留原字节。没有上传、发布、改thesis、写旧决定或安装依赖。

## 界限

正式送审版本、听测timing处理、实际run／checkpoint／table来源、吉他Fig6.3 GT、最终ICASSP仍待原材料确认；R1-13/21/26/30没有因文字通过而结案。Markdown来源在浏览器中不可靠支持行锚点，因此链接注明对应编号供搜索，不声称直接跳到批准行。
