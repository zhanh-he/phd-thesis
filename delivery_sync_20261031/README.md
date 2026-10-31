# 完整同步校验

本目录记录 2026-10-31 完整交付，不替代论文审阅结论。

- `source_manifest.json`：原项目每个纳入文件的相对路径、字节数及 SHA-256；406 文件，共 88,694,705 bytes。每个文件均按原字节保留，包含备份、四篇论文 PDF、全部 blueprint/v5 文件、候选、评分、证据及两份 ZIP。
- 仅排除清单列明的两项 `__pycache__/*.pyc`（19,181 bytes），属于可重建 Python 缓存；`.git` 内部数据库不属于项目文件。未省略有意义的交付物。
- `verify_sync.py`：仅用 Python 标准库核对清单、主阅读页、其他阅读页相对文件引用与已记录来源哈希。从仓库任意位置运行 `python3 delivery_sync_20261031/verify_sync.py`。
- `delivery_manifest.json`：仓库全部项目与新增同步文件的路径、字节数及 SHA-256，唯一不自列的是清单自身；校验脚本也检查没有漏文件。
- `prepush_verification.json`：生成完整交付清单之前的源文件与阅读页校验结果；最终完整覆盖再由脚本核验。
- `offline_qa.json`：本次在完全独立副本重建和运行浏览器检查的结果；没有覆盖原项目的历史证据。
- `offline_qa_browser_validation.json`：独立副本的实际浏览器测试报告。

原始项目目录未被改动。同步在临时 checkout 完成，仓库可见性保持不变，未向 finding-jobs 或 GitHub Pages 发布 thesis。历史脚本里存在的原电脑绝对路径按原样保留；日常阅读使用根目录 `START_HERE.md` 和相对路径。
