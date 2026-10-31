# 修订来源与版本边界

这是第一轮写作与证据清单，不是已执行修订。只读取 `phd thesis` 下材料；没有读取 `phd otherfiles`。

## 目前可以确定的事

- 报告 1：Dr Emmanouil Benetos，正文日期 24 September 2026，4 页。PDF 内有 25 条不同回复文字；PDFKit 返回 50 个 annotation 对象是 Highlight 与 Popup 的重复表示，不是 50 条回复。已直接抽取并对照 Markdown。报告 2：4 页，无作者回复批注；元数据 Author 为 Waleed Abdulla，但报告正文未见签名，不能仅凭 metadata 确认评审身份。
- `Z_He_PhD_Thesis.pdf` 共 154 个物理页，PDF metadata CreationDate 2026-05-25；`main.pdf` 共 155 个物理页，metadata CreationDate 2026-10-31。时间是文件元数据，不能证明哪版为学校正式送审稿。
- 两个 PDF 不能互换页码：例如 Chapter 4 在前者印刷页 51 开始、后者页 53。两份内容也有真实差异，例如 Background 的 attention 文献表述、MAESTRO/MAPS 统计与说明；不能概括成仅排版不同。完整抽取文本差异见 evidence/existing_pdf_text_difference.diff。
- 本轮提案以当前 `main.tex` 及其实际 include 的七章 `.tex` 为可定位文本，`main.pdf` 为较近的现存排版参考；这只是工作坐标，不替作者决定正式修订基线。正式采用与最终页码均【待作者确认／待核验】。未重新编译，未宣称源码与 PDF 完全等价。
- 评审原文以两份原始 PDF 为准，Markdown 为便于定位的转写。缺失回复统一记【作者未回复】，不自动视为同意。报告 1 的 25 条回复已从 PDF annotations 核验；报告 2 均无当前立场。
- 四篇论文均已读取首页和摘要并逐项进入技术核对。文件名按 PAPER_RENAME_MAP.md 规整，字节校验一致。论文是次要风格与方法来源；不把论文内容自动当成 thesis 已做工作。

## 文件角色

| 文件 | 本轮用途 | 限制 |
| --- | --- | --- |
| main.tex 与 Chapter_1 至 Chapter_7 的 include 源码 | 段落原文、术语、全文一致性和候选插入点 | 只读；LaTeX 行号作为本轮稳定位置 |
| 两个 thesis PDF | 版本差异、图像和排版核验 | 页码各自独立，不复用旧 v0 页码 |
| 两份 Preliminary Report PDF | 评审文字与作者原批注 | 不把机器转写或旧工具解释当作者立场 |
| 两个 README_Preliminary_Report_*.md | 可搜索的意见／回复转写 | 与 PDF 交叉核验 |
| publish_paper 四篇 PDF | 发表范围、方法与风格辅助核对 | 不是新实验或自动修订依据 |
| 02_Ultra_细节 中固定源码与已有输出 | 查证已知具体疑点 | 默认配置不证明论文实验实际运行配置；旧核查不替代新判断 |
| .claude 旧生成核查、backups | 本轮不作为当前任务指令或写作基线 | 不继承旧生成稿结论；无回滚或恢复 |
| reference.bib、casm.bib | 现有引用键核对 | 不编辑；未新增文献或宣称作者年制已采用 |

## 需要人或原始记录才能最终解决的边界

1. 正式修订基线；已提供两套准确文件身份，候选可继续写。
2. Ch.3 听测刺激是否经过 timing quantisation：作者批注明确说 yes，而正文描述 SMD 原 MIDI 去掉 velocity；无刺激文件或生成记录可直接判定。
3. Ch.3 loss/input/window labels 与固定源码差异、Ch.4 实际训练分支和权重验证范围、Ch.5 最终表的 F1 平均／checkpoint 选择。只核对已有材料，不重训。
4. Fig.6.3 guitar “ground-truth velocities” 的来源身份，不能从图像推断是真实标注、合成控制值或 pseudo-label。
5. 当前目录未找到 GRS revision-report 专用模板／提交说明，报告只能做待核验 blueprint。

## 本轮环境与方法

- 当前模型／effort 在此执行环境未向写作任务暴露，不能声称已核实 Ultra。父任务负责可用配置与三个聊天协调。
- PDF read-only inspection 使用 macOS PDFKit 抽取文字、元数据、批注和页面图。系统未提供 pypdf/pdfplumber/Poppler；workspace-dependency loader 返回仅 local threads 支持。没有为此安装软件。
- 这是只读 PDF／文档检查，不创建／编辑 PDF 或 DOCX。报告页已渲染核验，后续图像疑点继续逐页查看。
- 下列 SHA256 与完整 evidence/source_sha256.json 用于交付前核对源文件未变；唯一允许的源目录改动是四篇 PDF 重命名。

## 关键来源校验值

- `Z_He_PhD_Thesis.pdf` — 14833690 bytes; SHA256 `cbfcfca09364f85a7f6fcef186114054bfa8c494a87d26271091911a9064de07`
- `main.pdf` — 14403753 bytes; SHA256 `8cb8dbe9d560980e003148e442cdeae53e7a97495dcee695b8a58df9a0719bb8`
- `main.tex` — 8145 bytes; SHA256 `a55546f7a41c9210f1ecebae71a2167f86e0fb93ddbf96797ba03c1ea270fd39`
- `README_Preliminary_Report_1.md` — 20902 bytes; SHA256 `e5916abeffcabf7e863728d9fca7ca2ca1eb76fadc595e7e24c2e4c595c17179`
- `README_Preliminary_Report_2.md` — 10907 bytes; SHA256 `89b84809d49df248ecc4da8825399fe73ff700edee1f3e9bd56d957e7614cdd3`
- `Preliminary_Report_PhD_thesis_Zhanhong_He 1.pdf` — 185540 bytes; SHA256 `28ad09550e7a47eff77693476db82d4d4d9a71ad5557871cfb27c72200ed63a4`
- `Preliminary_Report_PhD_thesis_Zhanhong_He 2.pdf` — 118876 bytes; SHA256 `c9d8a2a843e3c9cd167e751ed0dec8f7cd7ca757a6a8fabea2abc747b1c61020`
- `reference.bib` — 146502 bytes; SHA256 `0f171e7d67c82e44fa2bc2f292aa5f1e5a3ec470de1a86f754ff907c045c5573`
- `casm.bib` — 121156 bytes; SHA256 `e787436aa31f737e54ac125e5bd0e47b575353388fc2a2628f05126ad7e2a438`

## 第一轮补充核验

- 25/25 条不同 PDF 作者批注经 Unicode／空白／blockquote 排版归一化后，与 README 转写逐条匹配。没有把 Highlight 与 Popup 复制成两条回应。
- 两份报告的全部8页已渲染并查看；当前 main.pdf 的物理页29（Fig1.1）、52（Fig2.3）、122（Fig6.2）、130（Fig6.3）已查看。Fig2.3在PDF白底中标题正常，图片工具显示的黑色透明区不是论文缺陷。
- 提供的 ICASSP PDF 物理页4可见 “PENDING THIS PART”，表中还有 “no yet”；页5的Table2 caption明确说正在被figure替换。已经渲染看图核验。此PDF可作为提供稿的标题／方法参照，不能不加限定地认定为最终发表版本。它的标题与authorshipdeclaration也不同，具体见PAPER_RENAME_MAP.md。
- R1-09的MIDI NoteOn／NoteOff／aftertouch／CC区分另向[MIDI Association官方message summary](https://midi.org/summary-of-midi-1-0-messages)核验（2026-10-31）。这仅用于事实澄清，未添加bibliography条目、未修改论文引用。
- `reviewer_baseline.md`的E01中“当前可安全说明听测以performanceMIDI为主”不能直接进入定稿：作者说听测输入已quantised，而原文只交代SMD来源与去velocity。未核验前，两种肯定版本都应保留待查。写作候选R1-21按此处理。
- Writer与独立审查者的38项R1、5项R2编号相同，原项crosswalk见ID_CROSSWALK.md。第三编辑应在唯一决策清单接收YES/NO，writer文件不另设填写入口。
