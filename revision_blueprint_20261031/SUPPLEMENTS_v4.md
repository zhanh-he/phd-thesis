# 全文对读后的三项补充

[返回简短入口](START_HERE.md)。以下文字已通过[定点独立复核](contextual_review_v4.md)，**仍待作者选择，未实施**。它们补到既有ID下，不新增examiner问题，也不从原方案的YES继承批准。三处只在[DECISIONS的补充栏](DECISIONS.md#supplements-v4)填写；本页没有另一套决定框。

## 1. 前言定义同步 · R1-09

前言把velocity写成普适的physical intensity／force测量，后文已区分piano传感器proxy与renderer-dependent control。推荐统一前言定义，同时删除把mf称作人类感知中性基准的末句。

**你的已有立场：** R1-09原批注仅“Yes a true”，不构成这组新文字的批准；R2-03未找到既有回复。此处是编辑建议。[原评审／批注](COMMENT_MAP.md#r1-09)。

**本次YES：** 只批准以下八处Intro操作，作为一组一致性小修；不改第2章已审原稿，不推定guitar GT来源。[唯一补充决定栏](DECISIONS.md#supplement-r1-09)。


### Intro:89 · 替换MIDI velocity整段

原文：

```latex
Originating from the physical sensors of electronic keyboards and pianos, MIDI velocity is a machine-centric measurement of physical intensity. To say it operates as a "note-level" parameter means that every music note from a discrete key strike is assigned an independent, static integer representing its initial strike force. This strict per-note measurement dictates that velocity functions as a discrete loudness control parameter. It is highly granular and absolute within its own scale, yet the resulting loudness highly depends on the acoustic environment and the specific instrument being played. Because MIDI velocity is necessary for MIDI-to-audio playback in DAWs and synthesisers, a common default is set to 64 when it is missing.
```

拟稿：

```latex
Here, MIDI velocity refers to the velocity value in a Note On message. It is a machine-readable control parameter. In sensor-equipped piano data, the recorded value acts as a discretised proxy for key or hammer motion. Each note carries an integer value that can be edited independently, although its acoustic effect depends on the instrument and renderer. When expressive values are missing, a MIDI sequence may instead use a constant such as 64.
```

### Intro:62 · 只替换短语

原文：

```latex
a universal loudness variable for all instruments
```

拟稿：

```latex
an editable note-level control
```

### Intro:43 · 只替换短语

原文：

```latex
a deep semantic gap exists between physical machine measurements (MIDI velocity) and subjective human cognition (score dynamics)
```

拟稿：

```latex
a gap remains between machine-readable control values (MIDI velocity) and context-dependent musical notation (score dynamics)
```

### Intro:53 · 只替换短语

原文：

```latex
bridging physical machine measurements (e.g., MIDI velocity) with semantic cognitive notations (e.g., score dynamic markings)
```

拟稿：

```latex
using note-level controls (e.g., MIDI velocity) and contextual notation (e.g., score dynamic markings)
```

### Intro:82 · 只替换Nature单元格

原文：

```latex
\makecell[l]{Physical\\measurement}
```

拟稿：

```latex
\makecell[l]{Note-level\\control}
```

### Intro:100 · 只替换短语

原文：

```latex
a machine-centric, physical parameter
```

拟稿：

```latex
a machine-readable control parameter
```

### Intro:100 · 只替换动词短语

原文：

```latex
bridge the fundamental gap between objective physical measurement and subjective human cognition
```

拟稿：

```latex
bridge acoustic observations, performance controls, and musical notation
```

### Intro:92 · 删除这一整句，不加默认值

原文：

```latex
In symbolic environments, the default assumption is often that missing score dynamics should be filled with \textit{mf} (mezzo-forte), which is the neutral middle ground of human perceptual loudness.
```

**拟操作：删除上方完整一句，不加替代默认值。**

这组保留sensor-captured piano数据的有效含义、逐音编辑与64例子。Score dynamics段的其他定义和metrical说明保留，Background的名义播放映射保留；不把mf作为有效记号否定掉。

## 2. S3与guitar范围 · R1-06

**评审与原立场：** R1-06询问Ch6是否也是audio-to-velocity场景；你说明当前采用score-informed模型，audio-only adaptation尚未建立。新增两处只是让前言跟Chapter5／6既有任务一致，不补新实验。[原答复](COMMENT_MAP.md#r1-06)。

**本次YES：** 仅以下两处；关联R1-15／R2-03但不另设重复输入。[唯一补充决定栏](DECISIONS.md#supplement-r1-06)。


### Intro:118 · 只替换S3句

原文：

```latex
Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target.
```

拟稿：

```latex
Finally, \textbf{Scenario S3} uses an \textit{audio-only} input to jointly estimate dynamic markings and the metrical coordinates needed for a \textit{score-facing} output.
```

### Intro:153 · 只替换该scope bullet

原文：

```latex
    \item \textbf{Exploration beyond the piano.} Extending velocity estimation beyond the piano is recognised as an important direction to counter the dataset bias in expressive AMT. However, large-scale non-piano score-dynamics transcription with human labels remains outside the scope of the core scenarios, and will only be investigated as an exploratory extension.
```

拟稿：

```latex
\item \textbf{Exploration beyond the piano.} Chapter~\ref{ch:beyondpiano} explores note-level velocity estimation for guitar using indirect supervision. Large-scale non-piano score-dynamics transcription with human labels remains outside the scope of this thesis.
```

audio-only是没有外给score的输入条件，模型仍联合估计用于score-facing输出的metrical coordinates。第6章是guitar note-level velocity的间接监督探索；不因此声称有captured guitar velocity真值。

**拼接边界：** Intro:118末句“These settings form the core empirical arc...”仍只依R1-15自己的选择。本补充不批准、不重复实施该句，也不整段覆盖另选的结尾。R1-06原B在table后的位置不变，R1-05定义插入点保留。

## 3. 动机末句 · R1-04

评审原先指出recollecting用词，你同意改collecting。下面收窄“entirely bypass”的承诺是**另一个编辑建议**：保留label recovery的价值，承诺减少采集需求，不说消除标注歧义。[原答复](COMMENT_MAP.md#r1-04)。

**本次YES：** 仅Intro:45末句；不批准或拒绝collecting，不扩大单一方案合并包。[唯一补充决定栏](DECISIONS.md#supplement-r1-04)。

原文：

```latex
By retroactively estimating missing dynamics on existing corpora, we entirely bypass acquisition bottlenecks and annotation ambiguities, unlocking a vast, previously untapped resource for data-driven music research.
```

拟稿：

```latex
By estimating missing dynamics on existing corpora, we can reduce the need for new data collection and make those corpora more useful for music research.
```

前两句和现有引用保留；第一句中的collecting仍随原R1-04单独决定。

<a id="keep-r1-35"></a>

## Fig6.2：推荐KEEP原caption／原图 · R1-35

评审问teacher target是否rendered audio；未找到作者既有回复。当前图注已写清来源，方法也已说明offline proxy training，推荐保留这行：

```latex
\caption{An encoder-only Transformer maps padded note sequences to per-note PHE/OSF targets extracted from SoundFont-rendered audio.}
```

[定点复核](contextual_review_v4.md#4-r1-35-fig62推荐keep原长a仍是可选解释)已直接查看未改图：teacher路径在左支路，现有“Render MIDI to Audio”标签能够说明来源。无须为了回复right-hand措辞画错支路。KEEP不把Fig6.3所谓GT的来源一并解决。

**选择：** 在[R1-35唯一决定行](DECISIONS.md#decision-r1-35)明确选KEEP或原A。NO原A不自动等于选KEEP；原A的四句解释仍保留为[可选长稿](writer_round3.md#r1-35)，没有覆盖删除。若要另加图内标签，填自定，图副本实施后另做视觉核验。

KEEP可用的GRS事实说明【仍待作者决定；未声称新增内容】：

> Figure 6.2 shows offline proxy training. Its caption identifies the teacher targets as PHE/OSF extracted from SoundFont-rendered audio.
