# 公开设计参考与许可证

本工作台采用仓库内自写的 JavaScript、HTML、CSS 和 Python；没有复制、安装、打包或调用下列项目的代码，也没有新增其运行依赖。以下记录借鉴的公开设计概念，不把本工具声称为这些项目的实现或兼容客户端。许可证适用于各上游项目；日后若实际引入代码，需另行核对对应版本、文件与许可义务。

| 参考 | 上游许可 / 来源 | 本工具采用的概念与边界 |
| --- | --- | --- |
| [Jupyter nbformat](https://github.com/jupyter/nbformat) | [BSD 3-Clause](https://github.com/jupyter/nbformat/blob/main/LICENSE)；[格式的向后兼容变更](https://nbformat.readthedocs.io/en/latest/format_description.html#backward-compatible-changes) | 稳定条目 ID、显式 schema 版本、兼容导入时保留未知字段/元数据。这里使用独立 reviewer 数据与 ledger 结构，不生成或解析 notebook。 |
| [Hypothesis client](https://github.com/hypothesis/client) / [W3C Web Annotation](https://www.w3.org/TR/annotation-model/#text-quote-selector) | Hypothesis [主要 BSD 2-Clause，另列部分组件的独立许可](https://github.com/hypothesis/client/blob/main/LICENSE)；W3C TextQuoteSelector 规范 | 以准确原句和前后文辅助定位，避免只给随编辑漂移的页码/行号。没有接入 Hypothesis 服务；本工具的源码范围和 hash 不是 W3C 字符位置 selector，也不宣称 UTF-16 与 Unicode code point offset 互换兼容。 |
| [Automerge](https://github.com/automerge/automerge) | [MIT](https://github.com/automerge/automerge/blob/main/LICENSE)；[冲突与可见替代值](https://automerge.org/docs/reference/documents/conflicts/) | 字段独立合并、同字段冲突保留可见替代值。实现为本地不可变操作键和父操作关系；没有加入 Automerge/CRDT 库，不声称跨设备实时协作。 |
| [CodeMirror merge](https://github.com/codemirror/merge) | [MIT](https://github.com/codemirror/merge/blob/main/LICENSE)；GitHub 上游已归档并迁至 [code.haverbeke.berlin](https://code.haverbeke.berlin/codemirror/merge) | 原文与建议文字并列，帮助人工核对范围。没有引入编辑器或 merge 组件，也没有将已归档 GitHub 仓库设为活动依赖。 |

当前实现的关键边界：每篇稿件以独立 `documentId` 隔离；每字段追加操作而非覆盖整份旧表；未知 ID/字段及兼容元数据保留；保存冲突和候选版本变化需要明确处理；双方决定与实际执行/核验分别记录。JSON 导出是可携带备份，浏览器存储不是跨浏览器、设备或路径同步。以上机制均不自动修改论文、上传笔记或推送 Git。
