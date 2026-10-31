# 阅读器初版：检查与边界

本轮重新实读了旧 START_HERE／CHANGE_CARDS／DECISIONS，并独立复查；旧 audit 的 P0 批准范围问题已经修复，不能继续说当前清单仍有那些矛盾。剩余阅读负担是：要跨三份文件找准确英文、表格编号比改动抢眼、完整公式让小改显得很大。

本地阅读器每次显示一张卡，先给实际原句与候选，再给范围；作者原立场、编辑建议和事实条件分开。只选五个能检验不同语义的旧例：首句替换、loss 解释、原段后新增、KEEP、听测结果措辞。没有分数装饰或批准按钮。

## 独立检查带来的实际修正

- R1-15 A 只改首句，但 B/C 重写全段：改为各稿准确的默认显示范围和说明，避免把整段重写包装成一词小修。
- R1-21 A 两句、B/C 三句：总导航改成“新增应用段”，逐稿说明实际句数。新增段不覆盖原 Stimuli。
- R1-35 旧 JSON 推荐 A 已被 v4 KEEP 覆盖：默认用 v4 KEEP，旧 A 明确留作历史比较，图内标签修改仍需副本核验。
- 显式前后导航把新标题滚到屏内并给焦点；切稿仍保留控件焦点。KEEP 不显示替换稿同步动作。
- 真实打开原 DECISIONS.md 后确认 Chrome 显示 text/markdown 的原始文本，Markdown `#decision-…` 不跳行。因此入口写“打开原决定清单 · 搜索编号”，不承诺定位到行。

## 实际验证

Python 标准库从冻结 JSON 抽取准确候选，逐字匹配原 .tex，记录来源 SHA。独立检查也确认五张卡的所有非 KEEP 英文完整稿均逐字存在于 `writer_round3.md`。

已安装 Chrome 的隔离临时 profile，加 Node 内置 CDP/WebSocket 做真实浏览器检查：[browser_validation.json](evidence/browser_validation.json)，93 项通过，零运行异常，零外网请求。覆盖所有写法三轮重复切换、原文／候选模式、事实筛选和空结果恢复、重置、键盘 Tab/Enter／details、底部下一处滚动、双标签页独立、重载默认值、实际 Markdown 链接，以及五卡 390px 无横向溢出。截图实际查看：桌面首卡／插入／KEEP／loss、窄屏首部和比较文字。

[build_validation.json](evidence/build_validation.json) 为准确引用与来源检查；[desktop-first.png](evidence/desktop-first.png) · [desktop-insertion.png](evidence/desktop-insertion.png) · [desktop-keep.png](evidence/desktop-keep.png) · [desktop-loss.png](evidence/desktop-loss.png) · [narrow-top.png](evidence/narrow-top.png) · [narrow-text.png](evidence/narrow-text.png)。

## 尚未完成的内容

当前只装入旧 v3／v4 五处例子，不能称作新 v5 重写成果，也不代表完整 43 项重新通过。等待 parent 提供写作和独立评审一致的新稿 packet；接入后须重新核对范围并复测。正式送审基线与原事实待核项仍由原材料管理，不由 UI 关闭。22 个 .tex／.bib／PDF 对早期来源清单的 SHA 均相同，见 [source_integrity.json](evidence/source_integrity.json)。原稿、旧决定、旧材料均未改写；未发布或上传。隔离测试浏览器已关闭，临时 profile 已清理。
