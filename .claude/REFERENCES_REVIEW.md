# References Review — 引用核查

Snapshot: 2026-05-17

扫描范围：`Chapter_1/Intro.tex`, `Chapter_2/Background.tex`, `Chapter_3/chap3.tex`, `Chapter_4/chap4.tex`, `Chapter_5/chap5.tex`, `Chapter_6/chap6.tex`, `Chapter_7/Conclusion.tex`, `main.tex`。

---

## 0. 这次自动修了什么

| 修复 | 文件 | 状态 |
|---|---|---|
| 加上缺失的 `@Misc{francoisleduc_zenodo,...}` 条目（之前 `Chapter_2/Background.tex` cite 了但没定义） | `reference.bib` (在 `riley2024high` 后面) | Done |
| 把 `riley2024high` 里那个借存 Leduc dataset URL 的 `mycomment` 移走（因为 Leduc 现在有自己的 entry 了） | `reference.bib` | Done |
| Stray `11` after `\end{tabular}`（会被渲染成文字"11"出现在 PDF 里） | `Chapter_2/Background.tex:150` | Done |
| `Cross-Instruments`（复数）→ `Cross-Instrument`（单数，匹配实际章节标题） | `Declaration/author_declaration.tex:63` | Done |

修复后重新扫描：**全文 0 个 undefined reference**。

---

## 1. 统计

| 指标 | 数量 |
|---|---|
| 正文里用到的 unique cite key | 160 |
| `reference.bib` 里定义的 cite key | 245 |
| Used 但 undefined（修复后） | 0 |
| Defined 但从未引用（orphan） | 79 |
| 重复的 `@type{key,...}` entry | 0 |
| 引用次数最高的 key | `kim2024method`（17 次） |

`reference.bib` 总共 2803 行。各章 citation 密度：

| Chapter | `\cite{}` 次数 |
|---|---|
| Intro (Ch1) | 11 |
| Background (Ch2) | 86 |
| Velocity completion (Ch3) | 24 |
| Score-informed (Ch4) | 27 |
| Audio-only score dynamics (Ch5) | 29 |
| Beyond piano (Ch6) | 21 |
| Conclusion (Ch7) | 0 |
| Backup_table.tex（孤儿文件） | 13 |

Conclusion 零引用对 synthesis chapter 来说是 OK 的，但还是要扫一遍 §"Limitations and Scope" 和 §"Future Research Directions" 里有没有事实断言其实需要 attribute。

---

## 2. Citation 语义错位——需要讨论

不是 undefined-ref 错，而是 **被引论文不能干净支持上下文 claim** 的地方。

### 2.1 Ch1 line 62 — `\cite{kim2024method, kim2025velocity2dms}`
原 claim：
> `"score dynamics provide a standardised notational vocabulary for composition, pedagogy, and performance analysis"`

- `kim2024method`（Kim et al. 2024 ISMIR）："A method for MIDI velocity estimation for piano performance by a U-Net with attention and FiLM"——这是 **velocity 估计** paper，不是讲 score dynamics 是标准记谱词汇的。Mismatch。
- `kim2025velocity2dms` —— 大概是 velocity-to-dynamic-marking 转换。如果是，那更接近但仍然在讲 mapping，不是"vocabulary"。

**建议：** 换成音乐学 / 记谱学的引用，或者干脆删了（这个 claim 本来就是常识）。bib 里已有的合适替代：`kosta2014dynpiano`、`cancinoChacon2018computational`、`palamara2020dynamic`。

### 2.2 Ch1 line 65 — `\cite{ryu2024midfild,lee2025gigamidi,tamer2023violin,loth2025goat,xie2025finegrained}`
原 claim：
> `"...control parameters remain sparse and weakly standardised ... across different instruments."`

五个引用串在一起支持一个 claim。"for example" 式的 cluster 可以接受，但 **`xie2025finegrained` 要查一下** —— 这是 control-parameter dataset paper 还是 method paper？如果是 method paper，就不能支持"sparse and weakly standardised"这个关于**数据集**的 claim。

### 2.3 Ch3 §3.2 (line 26) — `he2025filling` 自引
原文：
> `"U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic ... \cite{he2025filling,kim2024method}"`

`he2025filling` 就是 **Chapter 3 改编自的那篇会议论文**（章节 provenance 和 Declaration 都明示了）。在 thesis chapter 内部引用它派生自的会议论文，如果 framing 清楚是可以的，但这里像引用别人的 prior art 一样引用。读起来像 opaque self-citation。

**建议：** 要么删掉（thesis 已经在 chapter provenance 里声明是 adapted from `he2025filling`），要么明示：`"as in our earlier work \cite{he2025filling}"`。

### 2.4 Ch4 line 19 — `\cite{martak2026soundmusicbias}`
原文：
> `"Recent analysis shows that transcription models can absorb strong sound and recording biases, which then harm cross-dataset behaviour \cite{martak2026soundmusicbias}."`

2026 引用。要确认这篇 paper 真的已经发表/接收（不是 in submission），因为这个 assertion 是 §4.6 cross-dataset 分析的关键支撑。

### 2.5 Ch4 line 162 — `\cite{he2026dynest}` 介绍 DynEst 作为 baseline
DynEst 是 Chapter 5 / ICASSP 2026 paper。和 §2.3 同样的 self-citation pattern —— 把**下一章**当 external prior art 引。现在 bib 指向 ICASSP 版可以工作，但顺序读下来 reviewer 会困惑。

**建议：** DynEst 第一次出现时加一句 `(see also Chapter~\ref{ch:audiodyn})` 括号说明。

### 2.6 Ch6 line 21 — "Reliable velocity labels are crucial for..." 的 clustered citation
原文：
> `"...for expressive rendering~\cite{rhyu2022sketching, zhang2024dexter}, music generation~\cite{tang2025integrated, borovik2025symupe}, performance analysis~\cite{morsi2025enable_rach3}, and data curation~\cite{zhang2022atepp}."`

每个下游领域一两个 cite。要核对一下：
- `rhyu2022sketching`、`zhang2024dexter` —— 这些 paper 真的需要"可靠的 note-level velocity label"吗（不是任意表情信号）？
- `morsi2025enable_rach3` —— 如果 Rach3 paper 的核心是 velocity，OK。

这些是次要问题，flag 出来是因为 clustered citation 容易从 paper 版本直接搬过来，但 thesis 改写句子的时候没相应更新。

---

## 3. 79 个 orphan reference（defined 但从未 cite）

最终提交前清理是 optional 的（LaTeX 不会报错），但每个 orphan 都是 drafting artefact，值得 review 一下是不是本来该被引用。代表性样本：

```
Roblek2019FAD, Schreiber2020LocalTempo, ableton-live-editing-midi,
ableton-live-keyboard-shortcuts, ansi_s34_2007, anwar2024imagesurvey,
azad2024unetreview, balke2025choralebricks, bigras2024loudness,
bittner2017deep, bladon1981vowel, bock2016joint, brunner2018midivae,
cancinochacon2024rach3, chang2024yourmt3plus, cheuk2023jointist,
chou2024midibert, dallinger2025piano_ssm, deng2023singing_transcription,
dong2022cswin, dorico-playback-options, dosovitskiy2021vit,
emerson2025multimodal, finale-autodynamic, goeblBresin2003accuracy,
goel2021automatic, he2026score, hong2018but, hracs2012creative
```

几个我觉得**可能本来该被引但被遗漏了**：

- **`he2026score`** —— 听名字像是你的另一篇 paper，现在没用。看下是不是 Ch4 或 Ch5 该引。
- **`cancinochacon2024rach3`** —— Cancino-Chacón 已经在 Ch2 line 24/50/51 被引过。这可能是同作者更新的 paper，应该在 score-dynamics 或 performance-analysis 讨论里也引。
- **`bock2016joint`** —— Böck 早期讲 joint task 的 paper。Ch5 beat/downbeat 部分可以和 `bock2020deconstruct` 一起引。
- **`brunner2018midivae`** —— MIDI VAE；Ch3 如果想讨论 symbolic generative baseline，这个合适。
- **`dorfer2018msmd`** 在 Ch2 dataset table 里。但 `msmd` 可能没在其他地方讨论，这没关系。

完整 79 个的列表可以用下面这个命令复现：

```bash
comm -13 \
  <(grep -hoE "\\\\cite[a-zA-Z]*\{[^}]+\}" Chapter_*/*.tex main.tex | \
    sed -E 's/\\cite[a-zA-Z]*\{([^}]+)\}/\1/' | tr ',' '\n' | \
    sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u) \
  <(grep -hoE "@[a-zA-Z]+\{[a-zA-Z0-9_:.-]+," reference.bib | \
    sed -E 's/@[a-zA-Z]+\{([^,]+),/\1/' | sort -u)
```

---

## 4. 其他 reference 相关观察

### 4.1 孤儿文件 `Chapter_2/Backup_table.tex`
这个文件存在，包含 13 个 `\cite{...}`，但**不被 `main.tex` include**。是旧版 dataset comparison table 的备份。要么直接删，要么挪出 `Chapter_2/` 目录。

### 4.2 Bib 里 citation style 混乱
Header 写着 bib 是从 `cmmr2025.bib + dynest.bib + ISMIRtemplate.bib + smc2026.bib` 合并来的。所以：
- 有的 entry 用 `booktitle=icassp`（string macro），有的硬编码完整 booktitle。
- 有的用 `bk_month`、`bk_address`、`bk_organization`（自定义字段）。在 IEEEbib style 下不会出错，但说明 entry 是从不同 paper template 拷过来的、惯例不一致。
- 不会编译错，但 bibliography 渲染可能不一致。提交前过一遍 normalisation。

### 4.3 `main.tex` 用了 `IEEEbib` 风格
```latex
\bibliographystyle{IEEEbib}
```
IEEEbib 是 UWA 可接受的 thesis style，但**不产生 hyperlink DOI**。如果提交 policy 要求 clickable DOI，换成 `IEEEtranN`、`unsrtnat`，或者自定义版本，并确认每个 entry 都有 DOI 字段。

### 4.4 各章 citation 密度差异大
Ch2 有 86 个，Ch3 有 24 个，Ch7 有 0 个。这是预期的（Ch2 background-heavy，Ch7 synthesis-heavy）。但 Ch3 的数量对一个需要对比好几个 baseline（Seq2Seq、ConvAE、Flat）的 chapter 来说偏低。考虑 Related Work / Experimental section 的引用支撑是否充足。

---

## 5. Action checklist

- [x] 加上 `francoisleduc_zenodo` —— 这次已修
- [x] 删 Ch2 表格末尾 stray `11` —— 这次已修
- [x] Declaration 里 `Cross-Instruments` → `Cross-Instrument` —— 这次已修
- [ ] §2.1 Ch1 line 62 citation mismatch —— 把 `kim2024method,kim2025velocity2dms` 换成音乐学/记谱学引用
- [ ] §2.2 Ch1 line 65 —— 核对 clustered citation 每个成员是否支持 dataset-availability claim
- [ ] §2.3 Ch3 line 26 —— reframe 或删掉 `he2025filling` self-cite
- [ ] §2.5 Ch4 line 162 —— DynEst 首次出现时加 forward reference to Chapter 5
- [ ] 删 `Chapter_2/Backup_table.tex`（孤儿文件）
- [ ] Review 79 个 orphan bib entry（`he2026score`、`cancinochacon2024rach3`、`bock2016joint`、`brunner2018midivae` 看起来最可能本来该被引）
- [ ] 决定最终提交是否要换掉 `IEEEbib` 改用 DOI-emitting style
