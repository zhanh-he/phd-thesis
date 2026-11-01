# Reusable reviewer workbench 数据约定

这个工作台可以复用于下一篇论文的 revision。运行时只有本地 HTML；论文、意见、定位与初始建议来自 `data.json`，手动选择和文字进入独立 JSON ledger。不要把真实作者笔记写成模板的初始值。

## 新稿最小流程

1. 在新稿根目录放一个 `revision_workbench/` 文件夹，复制本工具的 `build.py`、`template.html`、`style.css`、`app.js`、`ledger.js`。保留本说明，并把 `reusable.template.json` 复制为该文件夹的 `data.json`。
2. 把 `documentId` 换成**这篇稿件独有且长期不变**的 ID，填写稿件名、reviewer、原意见与源码定位。模板里所有 `REPLACE_…` 内容都必须替换；模板不是实际修订数据。`REPLACE_WITH_UNIQUE_MANUSCRIPT_ID` 是禁止交付的占位 ID。
3. 将 reviewer 和 comment 按 report 原顺序放进数组。补齐原意见、作者原回复出处及修改位置；没有明确作者决定就填 `pending`。检查所有相对路径、行号、原句和来源版本。
4. 在新稿根目录运行 `python3 revision_workbench/build.py`，然后双击生成的 `START_HERE.html`。构建不需要额外 Python 包，页面运行不依赖 Python。
5. 开始录入后，以 JSON 备份为正式可携带记录。每次导出下载带时间戳的新文件，保留旧备份；工具不连接或改写已有磁盘文件。更新程序或修改 `data.json` 前先导出，再在更新后的页面合并导入验证。

构建默认读取同目录 `data.json`，写入稿件根目录 `START_HERE.html`，并以稿件根目录为源码路径基准。需要独立数据或输出时，可用 `python3 revision_workbench/build.py --data PATH --output PATH --source-root PATH`；所有来源链接仍须能从实际输出 HTML 的位置正确打开。

不同稿件必须使用不同 `documentId`。同一稿件更新 edition、候选文字或 HTML 文件名时，保持原 `documentId` 和已有 comment ID；另用 `candidateVersion` 标记内容变化。浏览器保存按 document ID 分区，另一篇稿件的 ledger 会被拒绝导入。浏览器/路径/设备差异仍可能隔离本地保存，不能靠 ID 实现跨设备同步。

当前 thesis 的 `verify_sources.py` 与 `source_baseline.json` 专门保护 43 条意见和原论文文件，**不是通用新稿验证器**；不要把该 thesis 基线当成新论文的来源证明。新稿需建立自己的来源检查，至少人工逐项核对原报告、原回复和当前源码。测试夹具中的示例不等于真实作者决定或经核实的引用。

## 顶层字段

| 字段 | 约定 |
| --- | --- |
| `schemaVersion` | 当前数据结构为整数 `1`。这是页面数据版本；ledger 有独立的版本校验。 |
| `documentId` | 稿件独有、长期稳定的非空字符串。不要使用易变的文件名、当前日期或 edition 作为唯一身份。 |
| `manuscript` | `{title, owner, subtitle}`；页面显示的稿件信息。所有值为纯文本。 |
| `reviewers` | 按原报告次序排列的 `[{id, displayName, shortName}]`。ID 唯一，comment 的 `reviewer` 引用它。 |
| `edition` | 本次数据/建议版本的可读名称，不替代 document ID。 |
| `sourceBaseline` | `{label, ...}`，说明当前源码快照，可附 commit、日期或 hash 清单。未确定送审 PDF 版本要明示，不推测页码。 |
| `comments` | 按实际展示顺序排列的 comment 数组。ID 唯一且稳定，数量和 reviewer 名称没有通用固定值。 |
| `sources` | `{相对文件路径: {text, sha256}}`；嵌入准确源码，为断网和双击 HTML 提供上下文预览。`sha256` 对应原文件 UTF-8 字节。 |

构建器可增加 `currentSources`、位置的 `binding` 和 comment 的 `sourceBindingVersion`，这些是重新核对当前文件产生的元数据，不替换原 `sources`、原行号或原句。不要把生成的 binding 状态手改成“已核对”。较新的未知数据 schema 保留原数据并以只读方式展示；这与 ledger 导入的独立兼容检查不同。

所有链接均相对于根目录 `START_HERE.html`。使用仓库内路径，如 `paper/main.tex`；不要写某台 Mac 的绝对路径、`file://` URL、`..` 路径穿越或外部网址来冒充本地来源。JSON 里的换行使用 `\n`，LaTeX 反斜杠使用 JSON 的 `\\`；用 JSON 工具生成，避免人工转义错误。

## 每条 comment

| 字段 | 约定 |
| --- | --- |
| `id` | 稳定工作 ID，如 `REV-A-001`。原报告没有编号时可自建，但 `reportLabel` 必须保留原标题/条目位置，不能伪称 PDF 印有该 ID。 |
| `reviewer`, `reportOrder`, `reportLabel` | reviewer 引用、其报告内顺序和原报告定位标签。数组顺序为实际顺序；按状态筛选不改变它。 |
| `title`, `meaning`, `original` | 简短标题、中文意思、完整 reviewer 原文。翻译/概括放在 `meaning`，不改写 `original`。 |
| `report` | `{path, page, label}`；`page` 是指定原报告 PDF 的一基页码，未核对用 `null`。这不是 thesis 页码。 |
| `authorReply` | `{text, sources, decision, prefill, reason}`。只放实际作者原回复；没有回复时 `text:""`、`sources:[]`、`decision:"pending"`、`prefill:false`。 |
| `assistant` | `{decision, reason, shortReason?}`。助手的修改建议及简短证据，不能当作作者表态。 |
| `recommendation` | 可读的具体修改建议，不声称已实施。 |
| `locations` | 全部需要处理、同步或明确保留的位置；见下表。 |
| `proposals` | 精确候选文字数组；没有可靠英文候选时用 `[]`，不要为凑字段编写作者的新稿。 |
| `candidateVersion` | 非空内容版本，推荐使用 SHA256；候选或其所依赖的源码范围改变时更新。保存的决定绑定此版本，不能把旧选择静默转成新稿批准。 |
| `evidencePending` | 尚待确认的事实/证据字符串数组，与双方决定和执行进度分别记录。 |

`decision` 的值只能是 `modify`（修改）、`keep`（保留/不修改）或 `pending`（待定）。`prefill:true` 需要明确原回复意图和出处；解释、技术辩护、疑问、条件式或某个分句同意，不足以代填整项决定。预填仅表示对 reviewer 问题的处理意向，不批准具体 candidate wording。

`authorReply.text` 保留源文字。多个原 PDF 批注按原顺序用空行拼接，批注编号、解释和中文总结放在独立元数据或 `reason`，不要追加到作者原话。`sources` 支持两种来源：

- 文本行：`{path, lineStart, lineEnd, quote}`，行号从 1 开始，quote 与该范围内原文完全一致。
- PDF 批注：`{path, pdfPage, annotationId, quote, pdfSha256}`，需要核对原 PDF 的页码、审计中可回查的批注编号、完整原话和文件 hash；审计自建编号不能伪称为 PDF 印出的编号。只有生成的转录或推荐稿不能构成作者决定证据。

可用 `authorReply.scopedDecisions[]` 单独表示原回复中已明确的局部范围决定，每项有独立 `id`、`label`、`decision`、`scope`、`exact_quote` 和 `version`，并附出处。例如“项目/实验不再扩展”可以预填 `keep`，而“是否补写论文说明”的主决定仍是 `pending`。局部勾选不转移成整项拒绝，也不批准任何新文字。跨意见共用操作和 `independentlyOptional` 小修要保留各自归属与独立选择，避免一次勾选扩大范围。

## 定位与候选

每个 `locations[]` 至少含：`file`、一基闭区间 `lineStart`/`lineEnd`、精确可搜索的 `quote`、原文 `before`/`after` 上下文（文件边界可为空）、`operation`、可读 `section`、`note`。可加稳定 `key`、`role`、`baseline` 和同步关系说明。图表/二进制资源通过其 LaTeX 引用位置定位，再在 note 中列出资产路径和视觉核验要求。

`operation` 使用 `replacement`、`insertion`、`deletion`、`formatting`、`keep` 或 `verify`。插入必须给出准确锚点和前/后方向；删除给出完整范围；同步项列出所有相关位置及所属 comment。来源版本不确定时，分别列出各 baseline 和待确认项，不把不同版本的行号拼成一个确定位置。

`proposals[]` 使用 `{id, locationIndex, operation, text, source, version}`，其中 `locationIndex` 是当前 comment 的 locations 零基索引；`text` 保留精确英文/LaTeX。删除候选的 `text` 可为空字符串，代表不添加文字。`source` 说明候选出处，`version`/`candidateVersion` 约束候选身份。建议文本和用户后来填的“实际修改文字”始终分开。

## 源码更新后的重新定位

构建时根据本地实际文件核对来源：原文件 hash、原行范围和准确引句一致时为 `verified`；完整引句在当前文件里唯一命中，或重复引句被直接相邻的准确 prefix/suffix 唯一消歧时，可标为 `relocated`。缺文件、引句消失、重复且不能唯一消歧等情况标为 `needs_relocation`。不按“最近行号”猜测位置，也不做模糊文字替换。

`binding` 包括状态、成功解析后的当前行号、`currentSourceSha256`、原因和 `reviewRequired`；原始位置始终保留。`relocated` 仍需人工复核修改范围，`needs_relocation` 则需重新提供准确锚点。构建器只更新页面定位元数据，不改论文文件。

每条 comment 的 `sourceBindingVersion` 随当前来源快照和定位状态变化；手动决定同时绑定候选 `candidateVersion` 与该来源版本。候选或依赖的源码变化后，旧决定仍留在 ledger 中，但不能静默认作新范围已批准。修改计划和实际文字也继续保留，不由重新定位过程改写。

## Ledger 与兼容性

页面手动记录的字段包括 `assistantDecision`、`authorDecision`、`plan`、`actualText`、`executionStatus`、`verificationNotes`。执行状态为 `not_started`、`planned`、`applied`、`verified`；后两项仍是作者记录，需要实际证据才能写入正式 revision report。

`executionStatus` 与 `verificationNotes` 的版本绑定同时包含当前建议/来源身份和 `actualText` 的操作头。实际文字、候选或源码范围变化后，旧执行/核验值继续保留，当前执行状态按 `not_started` 显示，并明确提示旧记录待确认。恢复历史不能把旧“已核验”自动移给当前新文字；实际文字有冲突或未保存草稿时，要先处理再确认执行状态。

导出的 ledger 含格式名、document ID、schema version 和追加式 per-field operations。每条操作有稳定 ID、字段值、父操作、时间、actor 和可选 candidate version。不要手改操作 ID/父关系来绕过导入校验。不同字段独立合并，同字段并发保留所有分支；解决冲突会新增操作，旧值仍在历史中。导入不会用整份旧快照覆盖当前记录。

导入的未知 comment ID 单独保留并显示提示，未知字段及兼容版本元数据继续随 JSON 备份保留。不能把未知数据当成已审核当前意见。较新且不兼容的 ledger、异稿 document ID 或损坏数据会被拒绝；保留原文件，使用兼容工具处理，不删除原记录或改 ID 强行导入。页面不提供云端同步、自动上传、自动 Git push 或自动论文修改。

浏览器保存项丢失或损坏时，当前内存中的可恢复记录和损坏原始值保留，页面提供“重试浏览器保存”。输入因大小或其他校验失败时，原字保留在本页内存的 `uncommittedDrafts`，保存状态必须显示警告；用户应立即点“救出未保存文字”，不能刷新后假设草稿仍在。常规备份包含未提交草稿，但不把它们伪装成已保存操作；独立救出文件使用 `uncommitted-manuscript-drafts` 格式，需要人工或后续整理工具处理，不是完整 ledger 导入文件。

导出总大小超过限制会明确失败，保留现有记录，不生成缺项却声称成功的备份。备份只附当前静态数据上下文，不把每次的动态用户笔记快照重复嵌入元数据；实际用户文字由操作记录及明确标注的未提交草稿保留。

双方决定的固定颜色规则为：双方 `modify` → 绿色；双方 `keep` → 红色；助手 `keep`/作者 `pending` → 灰色；其余 → 黄色。冲突或旧版本待确认也保持黄色。颜色都有文字，红色表示共同保留，不代表错误；任何颜色都不能单独证明修改已执行。

可选的 `consistencyGroups` 只提供一起核对的提醒：每组含 `id`、`commentIds`、一句 `text` 和 `targets`（`commentId`、`locationKey`、可读 `label`）。跳转使用稳定位置 key；组本身不写决定、不联动勾选，也不意味着整组已实施。
