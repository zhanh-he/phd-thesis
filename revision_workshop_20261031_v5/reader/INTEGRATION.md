# 给整合者：接入最终 v5 packet

本目录只负责只读比较；不修改 writer/evaluator 输出、旧决定或 thesis。最终新稿需写作与独立评审达成一致后再接入。当前 `initial_packet.json` 明确是旧轮示例，不是 v5 结果。

## 文件和构建

- `initial_packet.json`：完整五卡数据，不从浏览器取作者决定。
- `make_initial_packet.py`：从冻结候选与批注 JSON 抽取旧示例，R1-35 推荐依据 v4 覆盖为 KEEP。不要用它覆盖最终新稿 packet。
- `reader_template.html`：页面与只读交互；`build_reader.py` 把任一合格 packet 嵌入 `index.html`，运行时不 fetch。
- `test_reader.mjs`：当前五卡的真实 Chrome 回归检查，无第三方依赖。最终卡片集合改变时需同步其卡数／措辞断言，不能沿用旧测试结果。

默认重建：

```sh
python3 build_reader.py
```

接入新稿：从 writer 的准确字段和 evaluator 的一致结论生成 `reviewed_v5_packet.json`，不要手抄英文；保留独立 packet，不覆盖旧 packet。

```sh
python3 build_reader.py --packet reviewed_v5_packet.json
```

输出仅限本 reader/。构建会核对源码整块、focus 子串、同步点原文、链接存在性、来源 SHA、KEEP 和安全字段。不会写 DECISIONS。v5 必须设置 `packetStatus: "jointly-reviewed-v5"`，并有 `reviewAgreement`（写作／评审文件、准确范围和一致结论）；构建检查存在，整合者仍须核验其真实性。

## Packet 字段

最直接的格式实例是 `initial_packet.json`。根字段为：`schemaVersion:1`、`edition`、`packetStatus`、`versionNotice`、`cards`、`provenance:[{path,sha256}]`。所有路径相对 `phd thesis/`，不得指向外部或上传 URL。

每卡：

- `id,title,short,group,why,stance,scope,pending`：中文阅读说明；`stance` 只写有记录的作者立场，编辑建议放 `why`。
- `sourceFile,sourceLine,originalFull,originalFocus`：准确源码与默认焦点。焦点必须是整块的原样子串；图注去壳时另用 `sourceExact` 指定准确 `\\caption{…}`。
- `operation`：`replacement` 或 `insertion`；插入时左侧显示保留的原段，右侧仅显示新段，展开后连读。
- `options:[{id,label,kind,fullText,focusText}]`：`kind` 为 `replacement`／`insertion`／`keep`，必须包含 KEEP。文字均准确提取。可按选项设 `originalFocus,summary,scope`，例如 A 只改首句而 B/C 重写全段时，B/C 必须默认展示全部变化，说明也随稿变化。
- `recommended,recommendationLabel,reviewStatus`：编辑推荐及版本；不得用作者批准字段代替，不显示未经核验的分数。
- `decisionPath`：只链接原 DECISIONS 对应编号；原 Markdown 没有可用 HTML 锚点时明确用编号搜索。新 v5 不从旧 YES 继承授权；未建立可准确记录的新稿范围前不要把旧行说成 v5 批准入口。
- `reviewFile,candidateFile,candidateAnchor,commentFile,reviewerComment,authorResponse`：审核和原话。没有回复就明说，不制造同意。
- 可选 `contextAfter,followthrough:[{file,line,old,new}],originalImage,recommendationSource,optionNotes`。同步内容必须符合所有显示稿的实际范围；KEEP 不显示替换稿同步操作。

若最终 v5 对同一卡的同步稿不同，请增加按选项同步字段，或把稿拆成独立且明确的卡；不要借用旧共同同步表。初版 `followthrough` 仅适用于其已核验旧候选。

## 复测和边界

使用已安装 Chrome 的隔离临时 profile；不要连接用户现有浏览器 profile。用 `--headless --disable-background-networking --disable-extensions --no-first-run --remote-debugging-port=0` 启动；`READER_CDP_PORT` 可指定本机端口运行 `node test_reader.mjs`。原测试 profile 已关闭并清理。

最终换稿后重新核对精确引用／替换和插入范围、所有保留项、作者立场、事实条件、KEEP、Markdown 链接、切换／筛选重置、键盘、双标签页及桌面／窄屏截图。真实查看截图，不把旧 93 项通过算给新文本。初版没有安装依赖，也不需要服务器或 CDN。

## 新增：外部独立评审待确认的 writer 接入

`prepare_writer_packet.py` 会按准确 FINAL_SELECTION 校验 writer 输入，生成独立 `provisional_v5_packet.json`。不修改 writer 输入，也不认定其推荐已获外部接受。

```sh
python3 prepare_writer_packet.py
python3 build_reader.py --packet provisional_v5_packet.json --output provisional.html --allow-provisional
```

暂定状态不得输出为 `index.html`。原首页保持不变；新预览的菜单、状态、历史清单链接和原话标签均按实际权限与来源展示。完整接入问题见 `WRITER_PACKET_INGESTION_NOTES.md`，独立预览测试为 `test_provisional.mjs`。这不是最终合稿步骤；外部评审有具体改稿后，须重新取得最终准确packet，重新验证所有来源。

## R2：七处重写与明确的组合依赖

独立脚本`prepare_r2_packet.py`读取R2准确输入、选文、23项v4依赖和44操作manifest，验证七处before/after、四个插入边界、无重叠，并重建整段预览。R2英文不从旧`reinserted_context`回退。`contextHtml`经过允许的mark标签检查后，去标记仍必须精确等于`contextPreview`。

```sh
python3 prepare_r2_packet.py
python3 build_reader.py --packet provisional_r2_packet.json --output provisional_r2.html --allow-provisional
```

旧index和上一版provisional保持不变。外部cycle2结论未确认前，R2始终pending。完整核验与下一步见`R2_INGESTION_NOTES.md`，测试为`test_r2.mjs`。不要让用户把旧DECISIONS行误当作新v5批准：页面只用稳定v5编号/版本在聊天中表达选择，之后由协调者明确同步，reader不造第二份决定状态。

## 当前最终入口（优先于上方历史准备记录）

`index.html`现在装入修补后共同复核的v5提案；旧示例精确保存在同目录`legacy_v3_v4.html`，两份provisional也保留。最终入口说明见`README.md`，核验见`FINAL_READER_NOTES.md`。

```sh
python3 prepare_final_packet.py
python3 build_reader.py --packet reviewed_v5_packet.json
```

最终适配器固定核对父级给定canonical packet SHA、writer/evaluator准确修补与接受hash，不通过则不会生成新数据。未来如果writer交付内容变化，需要新的明确版本绑定；不能绕过hash检查或把旧选择转给新稿。最终浏览器测试为`test_final.mjs`，使用隔离Chrome临时profile；不要连接用户浏览器配置。
