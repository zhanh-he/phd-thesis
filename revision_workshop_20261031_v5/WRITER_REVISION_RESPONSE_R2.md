# Writer R2：回应第一次外部独立评阅

**阶段：已作实际定点返修，等待第二次外部整段评阅。** 不宣称joint approval。C1匿名候选、先前FINAL_SELECTION／推荐／reader输入和全部评分均冻结保留。R2另存新文件。正文、旧DECISIONS、PDF、数据、bibliography、图像未改。

本轮依据：`evaluator_cycle1.md`及其`evaluator_cycle1_post_reveal.json`。先回读真实源文与前后段，再作以下七处取舍。此前两轮是writer内部子代理评阅；这次外部C1单独计数、量尺不混用。

## 逐项取舍与理由

| ID | 决定 | 实际理由 |
|---|---|---|
| T01 | ACCEPT | 接受。note content and timing逐项对应作者真实定义，比note structure精确，不引入新的数据类别。 |
| T03 | ACCEPT | 接受实质合并。旧稿先说U-Net需二维输入，理由偏循环；现在先交代simultaneous notes与local neighbourhoods如何放到regular grid，再说明binary/single-channel与note-list接口代价。为必要信息接受略长文本，不追求最短。 |
| T07 | ACCEPT | 接受。补on the target recordings，限定未单独测量的对象；不暗示这些合成器从未做过保真评估。 |
| T11 | ACCEPT | 接受可选精简。旧v5与批注相容，并非确定的事实错误；删through a dedicated comparison减少实验史歧义，只保留尚未确立优势。 |
| N02 | ACCEPT_WITH_INTEGRATION | 接受实质意见，整合位置略调整。删去紧邻表格的四个delta，不从舍入端点重算0.193。保留GT notes/velocities不变、rendered sound变化及非gain-only干预。metric purpose移到N03首句，避免相邻两段重复同一句目的说明。 |
| N03 | ACCEPT_WITH_INTEGRATION | 接受目的句写法，并承接N02末句的absolute-level目的。用For label-free guitar evaluation替代therefore；保留piano/two SoundFonts范围及complementary diagnostics，不重新声称优越性。 |
| N05a | ACCEPT | 接受KEEP原首句。scope boundaries不全等于缺陷；只删后面的防御句，原分类不变。 |

N02/N03采用外部意见的内容，但将metric-purpose句只放在N03，避免紧接两段重复用途。不是拒绝renderer/gain区别或absolute-level目的；第二次外部评阅可据整段判断这个整合。

T11的新精简是降低歧义，旧v5句与真实批注相容，并不被改写成已知错误。v4“did not conduct”应理解为资料不足以断言的实验史，不因此证明它必然为假；不回填或篡改旧评分。

## 七处准确diff：冻结writer选稿 → R2

### T01 · 当前源坐标 `Chapter_1/Intro.tex:114`

```diff
--- T01 frozen writer selection
+++ T01 R2 proposal
@@ -1 +1 @@
-Here, weakly expressive data retain note structure but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.
+Here, weakly expressive data retain note content and timing but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.
```

### T03 · 当前源坐标 `Chapter_3/chap3.tex:26`

```diff
--- T03 frozen writer selection
+++ T03 R2 proposal
@@ -1 +1 @@
-We use piano rolls because the U-Net processes two-dimensional pitch--time neighbourhoods, including simultaneous notes. The input is binary and the output is a single-channel velocity roll, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
+We use a piano roll to place simultaneous notes and local pitch--time neighbourhoods on a regular grid for the convolutional U-Net. The input is binary; the single-channel output supplies velocity values, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
```

### T07 · 当前源坐标 `Chapter_6/chap6.tex:111`

```diff
--- T07 frozen writer selection
+++ T07 R2 proposal
@@ -1 +1 @@
-The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately.
+The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.
```

### T11 · 当前源坐标 `Chapter_6/chap6.tex:126`

```diff
--- T11 frozen writer selection
+++ T11 R2 proposal
@@ -1 +1 @@
-We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE through a dedicated comparison.
+We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE.
```

### N02 · 当前源坐标 `Chapter_6/chap6.tex:503`

```diff
--- N02 frozen writer selection
+++ N02 R2 proposal
@@ -1 +1 @@
-Changing from Salamander to YDP while retaining the GT notes and velocities changes MAE by $0.193$ on BSSL and $1.723$ on BSTL; the corresponding changes in Pearson $r$ are $0.034$ and $0.011$. This tests the effect of the renderer change as a whole, rather than absolute gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.
+Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.
```

### N03 · 当前源坐标 `Chapter_6/chap6.tex:505`

```diff
--- N03 frozen writer selection
+++ N03 R2 proposal
@@ -1 +1 @@
-We therefore use Pearson $r$ on BSSL/BSTL as the main measure of rendered loudness-contour agreement for label-free guitar evaluation. In this piano diagnostic, it distinguishes GT from flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
+For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement while reducing dependence on absolute level. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

### N05a · 当前源坐标 `Chapter_7/Conclusion.tex:109`

```diff
--- N05a frozen writer selection
+++ N05a R2 proposal
@@ -1 +1 @@
-The thesis has several limitations.
+The thesis has several boundaries.
```

## 明确保留

T10继续用v4，不为微小措辞偏好换稿。T02/T04/T05/T06/T08/T09/N01/N04/N05b/N05c/N06a/N06b均未改选稿。Fig6.2原caption／图、O/F/V角色、loss公式、beta／权重、frontend参数及实测表值保持原样。N05a特别恢复原首句，是一项确切的KEEP胜出。

## v4已解决的内容只继承，不记作新发现

组合预览明确带入23项既有依赖：SUPPLEMENTS_v4的8处velocity定义、S3/scope两处及动机末句；R1-15的首段及四处S1同步；R2-04的四处听测概括同步；R1-33的三个共同完整段落（含五个原局部动作）。详见`DEPENDENCIES_R2.json`。

这些依赖仍是未批准提案，只为本次组合语境演示。没有声称43项全部被作者采用；本卡KEEP不自动批准／拒绝其他依赖，旧YES不继承。`CANDIDATE_PACKET_R2_FULL_CONTEXT.md`不再让相关语境保留旧S3、most-constrained或错误听测比较对象。

## 指标表与舍入提示

N01/N02/N03与N07必须同组。N07沿用原副本：表环境内58个数字token顺序不变，12个数值bold/underline包装变0。外部评阅指出显示端点0.702−0.510与报告delta0.193的精度差；本轮不诊断成数据错误，不重算或静默修数。删掉正文数字复述也避免把报告值写成我们重新计算的结果。N04保留已通过的conditional can-divert从句，不为了换词再扩一轮。

## 有界excerpt review独立记录

父级另报告GPT-6.1-sol的bounded excerpt review。它未访问全文、真实批注或表格；只作所见片段的序位编辑判断。不算第二次外部全文审查。原始归属／范围／评分和采用取舍另存`evidence/BOUNDED_EXCERPT_REVIEW_PARENT_R2.md`，不与full-source C1合并。

## 交给第二次外部评阅

- `FINAL_SELECTION_R2.json`：20项精确源操作及当前英文。
- `CANDIDATE_PACKET_R2_FULL_CONTEXT.md`：包含v4依赖的组合整段预览。
- `FINAL_PASSAGES_R2.md`：相同准确英文的阅读入口。
- `WRITER_READER_PACKET_R2.json`：新版本无损reader输入；状态刻意保留`writer-r2-pending-external-cycle2`，不能直接冒充jointly-reviewed。没有改reader HTML。
- `evidence/R2_exact_changes.json`／`R2_context_operation_manifest.json`：准确diff、插入位置、依赖、无重叠检查。

正式送审基线、R1-13/21/26/30、run／checkpoint／table provenance、guitar GT和最终ICASSP版本继续开放。没有新实验、编译、外传或提交。
