# 全文 Proofread Pass（错误、typo、写作改进）

Snapshot: 2026-05-17

这份文件覆盖前置部分、Intro、Background、Conclusion、Declaration、Acknowledgments 等 Ch3–Ch6 之外的内容。Ch3–Ch6 的重复问题和 Discussion 深度问题在 `THESIS_REVIEW.md` 里。

---

## 0. 这次已经自动修了

| 问题 | 位置 | 修复 |
|---|---|---|
| `\end{tabular}` 后面有 stray `11`，会在 PDF 里以"11"显示 | `Chapter_2/Background.tex:150` | 已删 |
| `francoisleduc_zenodo` 在 Background 被 cite 但 bib 里没定义 | `Chapter_2/Background.tex:794` | 在 `reference.bib` 补了 `@Misc` entry |
| Declaration 里 `Cross-Instruments`（复数）和实际 chapter title `Cross-Instrument` 不一致 | `Declaration/author_declaration.tex:63` | 改回单数 |

修后全文 **0 个 undefined ref**。

---

## 1. Acknowledgments 需要重写（不是改稿，是大改）

`Acknowledgments/acknowledgements.tex` 三段短文里有 ~10 处英文语法错。因为致谢是个人语气，我**没有**自动改；下面是问题清单，你可以一次过。

### 第 1 段（Roberto / Defeng）

原句 → 问题：

- `"His coursework unit is the most clearly one I got"` —— `most clearly one` 不合语法。可能想说：
  > `"His coursework unit was the clearest one I took during my undergraduate study,"`

- `"he shows me the light to step-in this journey"` → `"shown me a path into this journey"`；`step-in` 不是动词。

- `"With many times of my wasting time consultant,"` → 意思不清。大概是：
  > `"Despite the many times I took up his time during consultations,"`

- `"he always kind"` → 缺系动词。应为 `"he was always kind"`。

- `"even thought our topic is not such closed"` →
  > `"even though our research topics are not so closely aligned"`

- `"undoubtly a expertise and professional"` →
  > `"undoubtedly an expert and a professional"`（`undoubtly` 也是 `undoubtedly` 的拼写错误）

- `"In Chinese language, we said the Teachers is like our fathers"` →
  > `"In Chinese, there is a saying that teachers are like fathers"`
  或者直接保留原文 `一日为师，终身为父`

- `"this is my ultimately lucky"` →
  > `"I have been extraordinarily lucky"`

### 第 2 段（家人）

- `"what they give me can never pay back"` → `"what they have given me can never be repaid"`
- `"I got many happiness"` → `"have received much happiness"` 或 `"so much joy"`
- `"her families: Wen He, Jiahui, Jiaxuan, Jennie, and Jiacheng"` → `"her family: ..."`（单数）
- `"the most relaxable time"` → `"the most relaxing time"`

### 第 3 段（Hanyu）

- `"She is take over my boring life"` → `"She has taken over my otherwise boring life"`
- `"make every day colorful"` → 配合上一句改时态：`"and made every day colourful"`
- `"We have the same topic"` → `"We share research topics and interests"`

### 第 4 段（同事）

- `"Yuliang. Zhihui and Kaibu..."` —— **placeholder 没填完**。要么补全名单，要么去掉结尾的 `...`。`Yuliang` 后面那个单独的句号也是 typo。

### 第 5 段（结尾）

- `"Staying in UWA has felt like a family to me"` → 主语不能是动名词 `Staying`，应改成：
  > `"UWA has felt like a family to me"`

实质内容是好的，这些都是语法修复，不是内容重写。

---

## 2. 前置部分（front matter）小修

### 2.1 `main.tex` Abstract——小瑕疵
Abstract 结构良好。一个可读性微调：第三段
> `"Chapter~4 proposes a lightweight Transformer correction module that refines AMT-estimated velocity at aligned score onsets."`

`"at aligned score onsets"` 措辞不寻常 —— "score onsets" 指 score 里的 onset 位置，但模型实际是在**对应到 aligned score event 的 audio onset**上做修正。建议改成：`"at score-aligned note onsets"`。

### 2.2 Author Declaration
- 当前每篇 paper 都写 `\textbf{Student contribution to work: 80\%}`。如果实际贡献率不一样，替换成正确数字；如果真都是 80%，保持。
- 底部 (line 92–109) 给出 `Defeng Huang`、`Roberto Togneri`、`Hanyu Meng`、`David Cooper` 的签名块。Hanyu Meng 实际上只是 Ch5 和 Ch6 的合作者，目前 declaration 把所有 co-author 集中一页签字，可以接受，但 UWA template 可能要求每个 declaration block 单独列对应 paper。提交前对照最新 UWA template 一下。

### 2.3 Title page (`main.tex`)
- Line 104：`B.Sc. in FieldA; B.Sc. in FieldB; M.Sc in FieldC` —— **placeholder**。提交前填上实际学位和学校。
- Line 105：`February 2016` —— 这个日期肯定是 placeholder（一般是提交月份/年份，例如 May 2026）。

这两个作者自己肯定知道，但 final sweep 时容易漏。

---

## 3. Introduction (Chapter 1) — 小修 + 一个实质问题

### 3.1 标点 / 排版
- Line 20：段落结尾 `as depicted in Figure~\ref{fig:intro_expressive_amt}` —— **少了句号**。
- Line 18 段尾在 `}` 之前有 trailing space。小事。

### 3.2 词汇
- Line 109：`"...without rewriting note content or trusted timing?"` —— `trusted timing` 读起来怪。Thesis 其他地方说"preserved timing"或"fixed timing"。建议改为 `preserved note timing` 或 `trusted alignment`。

### 3.3 Citation mismatch（也在 `REFERENCES_REVIEW.md §2.1`）
Line 62：`\cite{kim2024method,kim2025velocity2dms}` 不支持"score dynamics 是 standardised notational vocabulary"的 claim。换成音乐学引用（或直接去掉——这个 claim 是常识）。

### 3.4 §"Aim, Scope, and Assumptions"——措辞小修
Line 153：`"large-scale non-piano score-dynamics transcription with human labels remains outside the scope of the core scenarios"` —— Ch5 的 score-dynamics transcription 是给 piano 做的，但这句读起来像 non-piano score-dynamics 也在某处被讨论。其实没有。改成：
> `"non-piano dynamics recovery is treated only as an exploratory extension (Chapter~\ref{ch:beyondpiano}), and large-scale non-piano score-dynamics transcription is left to future work."`

### 3.5 §"Main Contributions"——velocity completion 那条 self-cite
Line 164：`"...introducing a U-Net architecture with window attention and a sparsity-aware loss \cite{he2025filling}."` —— 引的是 Ch3 改编自的会议论文。在 Main Contributions 里 self-cite 表明工作是 peer-reviewed 发表的，可以接受，但要注意有些 examiner 会 flag。仅作提示。

---

## 4. Background (Chapter 2) — 小修

### 4.1 Section heading 大小写不一致
- §4.2 line 54：`\section{Dynamics in audio}` —— `audio` 小写。
- §4.3 line 249：`\section{Dynamics in MIDI and Score}` —— Title Case。
- §4.1 line 9：`\section{Musical Dynamics}` —— Title Case。

挑一个统一。UWA thesis 一般是 Title Case。建议：`\section{Dynamics in Audio}`。

### 4.2 冠词用法
Line 240：`"The pitch, loudness, and timbre can jointly affect perceived instrument dynamics"` —— 列表前的 `The` 读起来怪。建议：
> `"Pitch, loudness, and timbre can jointly affect perceived instrument dynamics"`

### 4.3 表格 footnote 不一致
几个 table（比如 Table 2.4 line 290 附近）用 `\tablefootnote{...}` 加 `mycomment`-style note。和 Ch4 的 `\tablefootnote{...}` 风格不一致。不是 hard error，只是 inconsistency。

### 4.4 AMT-SOTA table footnote
Line 410：`$^\dagger$ Re-evaluation on MAESTRO v3 by SemiCRF paper. \\` —— `\parbox` 内 footnote 末尾的 `\\` 不寻常；编译后检查 footnote 是否正常显示。

### 4.5 Dataset table 里有可能错的 warning marker
Line 626（ATEPP）：Score 和 Dynamics 列 `\cmark\ 43\% & \warn\ 43\%`。`43\%` 作为 label 看起来奇怪——是"score coverage 43%"还是"dynamics coverage 43%"？读者光看 caption 大概看不懂这个百分比是啥。

### 4.6 §"From physical sound level to symbolic dynamics" 小措辞
Line 24：`"MIDI velocity describes a control quantity at note onset."` —— 短而精。下一句：
> `"In acoustic piano settings it is best interpreted as a proxy for performer action rather than as a universal loudness unit"`

考虑把 `acoustic piano settings` 换成 `acoustic-piano performance contexts` 或 `for sensor-equipped acoustic pianos`。

### 4.7 §"Bark-scale and critical bands" 数学排版
Line 150：`\end{tabular}11` —— **这次已修**。
Equation (2.6) line 155：`arctan` 原本要是 roman 看起来奇怪；当前是 `\arctan`（math operator，正确），无需修。

### 4.8 §"Other Audio Representations" 的 citation chain
Line 242–244 两段里多次出现 4-cite cluster。stylistic 上偏重。考虑拆开，每个 claim 给一个代表性引用。

---

## 5. Conclusion (Chapter 7) — 总体不错，小修

Conclusion 状态良好：术语一致、复述中心问题、按章节列贡献、有 Limitations + Future Work。四个 cross-chapter findings 子节（§§7.3.1–7.3.4）尤其强。

### 5.1 措辞小修
- Line 95：`"score-facing rather than frame-facing"` 简写不错，但 `frame-facing` 是造词；考虑 `"score-facing rather than frame-wise"`，和其他地方词汇对齐。
- Line 99（subsection 标题）：`"Weaker supervision changes the claim, not the value of the problem"` —— 有力，保留。

### 5.2 数值断言要核
Line 57：`"adds about 1\,M parameters on top of an existing AMT backbone, transfers across HPT, HPPNet, and DynEst"` —— 核对一下 1\,M 这个数值匹不匹配最终 Score-HPT 5.0M vs HPT 4.1M（= 0.9M，约 1M 可以）以及 Score-HPPNet 1.5M vs HPPNet 0.5M（= 1.0M）。OK。

### 5.3 Citations
Ch7 有 **0 个 `\cite{}`**。同 `REFERENCES_REVIEW.md` 提的，对 synthesis chapter 可以接受，但确认一下 §"Limitations and Scope" 或 §"Future Research Directions" 里有没有事实断言其实需要 attribute。

### 5.4 §"Future Research Directions"
五个子节（probabilistic bridge、uncertainty-aware annotation、instrument-general coordinates、corpus-scale curation、AMT beyond note detection）读起来好。无问题。

---

## 6. Cross-cutting 写作问题

### 6.1 Ch5 的 `pend` 占位符——和 `THESIS_REVIEW.md §3.3` 重复
**Chapter_5/chap5.tex Table 5.5（cross-dataset Vienna4x22 + Batik-plays-Moz）还有 6 处 `pend`**。这是当前 draft 最严重的硬伤，因为 examiner 一眼能看到。处理选项在 `THESIS_REVIEW.md §3.3`。

### 6.2 6 处 thesis-positioning 残留——和 `THESIS_REVIEW.md §1` 重复
（Ch3 line 26, Ch4 lines 19/34, Ch5 lines 13/43, Ch6 line 17）。`THESIS_REVIEW.md` 里有改写建议。

### 6.3 孤儿文件 `Chapter_2/Backup_table.tex`
不被 `main.tex` include，但还有活的 `\cite{}` 和旧版 dataset table。**建议直接删**再提交。

### 6.4 仓库根目录的旧文件 `all.patch`
`git status` 显示 `?? all.patch` 在 project root。建议清理——如果不再需要就删，如果是 in-progress 就 commit 或挪出仓库。

### 6.5 `.synctex` 文件
`git status` 显示 `main.synctex(busy)` 是 deleted 状态。Synctex 文件应该在 `.gitignore` 里。不是写作问题，是仓库卫生问题。

### 6.6 Bibliography style 的选择
当前 `IEEEbib`。不产生 hyperlink DOI。如果 UWA 提交系统或 examiner 希望 clickable DOI，换成 `IEEEtranN` 之类，并确保 DOI 字段都填了。见 `REFERENCES_REVIEW.md §4.3`。

---

## 7. 最高优先级 TO-DO

按"阻断提交" → "polish" 大致排序：

1. **填 Ch5 Table 5.5 的 Vienna4x22 / Batik 占位符**，或者把实验降级到 Future Work、删表。(`THESIS_REVIEW.md §3.3`)
2. **重写 Acknowledgments**（~30 分钟个人语气编辑）。本文档 §1。
3. **填 `main.tex` title page 占位符**（`B.Sc. in FieldA`、`February 2016`）。§2.3。
4. **Acknowledgments 同事列表补全**（`Yuliang. Zhihui and Kaibu...`）。§1。
5. **决定 6 处 thesis-positioning 残留怎么处理**（Ch3 line 26, Ch4 lines 19/34, Ch5 lines 13/43, Ch6 line 17）。`THESIS_REVIEW.md §1`。
6. **处理 citation-mismatch 清单**（`REFERENCES_REVIEW.md §2.1–§2.6`）。
7. **删 `Chapter_2/Backup_table.tex` 和 `all.patch`**。
8. **Ch2 section heading 大小写统一**（`Dynamics in Audio`）。§4.1。
9. **小 typo**：Ch1 line 20 缺句号，Ch1 line 109 `trusted timing`。§3.1、§3.2。
10. **Discussion 深度补强**（Ch3 Chopin metric-failure、Ch4 FiLM 机制对比、Ch5 multi-scale 解读）。`THESIS_REVIEW.md §3`。

---

## 8. 本次 review 产出的文件

- `/Users/hanyu/Documents/Thesis_v0/.claude/THESIS_REVIEW.md` —— 重复和 Discussion 深度问题（早先 session + 这次增补）
- `/Users/hanyu/Documents/Thesis_v0/.claude/REFERENCES_REVIEW.md` —— 引用问题（这次）
- `/Users/hanyu/Documents/Thesis_v0/.claude/FULL_THESIS_PROOFREAD.md` —— 本文件
- `/Users/hanyu/Documents/Thesis_v0/.claude/merge_paragraphs.py` —— 合并 sentence-per-line 段落的脚本
- 合并步骤的备份：`/tmp/chap{3,4,5,6}.before.tex`
