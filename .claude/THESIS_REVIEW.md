# Thesis Review — 重复、深度、写作问题

Snapshot: 2026-05-17 (Auto-mode review)

---

## 0. 已经执行的改动（之前的 sessions）

| 改动 | 文件 | 状态 |
|---|---|---|
| 合并 sentence-per-line 段落为 prose block | Ch3, Ch4, Ch5 (no-op), Ch6 (仅清尾空格) | Done |
| 删 Ch4 line 509 的 thesis-bridge 段落 | `Chapter_4/chap4.tex` | Done |
| 修 Ch3 语法错 `this chapter is instead to exploit` → `instead exploits`，并去掉与 Related Work 重复的前半句 | `Chapter_3/chap3.tex:43` | Done |
| 删掉 Ch3 \red 标记的定位句 `"establishes ... building block"` | `Chapter_3/chap3.tex:460` | Done |
| 收紧 Ch4 §"Modular Correction Principle" 开头，明确 cross-ref 到 Related Work | `Chapter_4/chap4.tex §4.4` | Done |
| 重写 Ch4 Summary 末段为深入讨论 score-prior 为何有效（3 个 sharpening points） | `Chapter_4/chap4.tex:325` | Done |
| 重写 Ch5 Overview 开头，以研究对象本身切入 | `Chapter_5/chap5.tex:11` | Done |
| 删 Ch5 Discussion §1 的 `"different thesis-level point from Chapters..."` meta 开头 | `Chapter_5/chap5.tex:337` | Done |
| 删 Ch5 Discussion §3 的 `"complements the velocity-focused chapters..."` bookends | `Chapter_5/chap5.tex:341` | Done |
| 整节删除 Ch6 §"What This Chapter Is and Is Not" | `Chapter_6/chap6.tex` | Done |

`\red{}` macro 还在 `main.tex` 里（备用）。所有原本的 `\red{...}` 标记都已处理完。

---

## 1. 剩下 6 处 thesis-positioning 冗余（还没动，等你拍板）

这些段落唯一的作用就是重述章节在 thesis 里的位置。Overview 已经讲过一遍，下面这些是第二/第三遍。

### 1.1 Ch3 line 26 — Related Work 收尾句
原文：
> `"This makes the chapter a natural starting point for the broader thesis."`

— 纯定位句，删掉不影响段落。
**判断：删**。

### 1.2 Ch4 line 19 — Related Work 末段
原文：
> `"For a thesis contribution, accuracy alone is not enough. The method should also expose a reusable principle. This is the main reason for the late-correction stance adopted in this chapter."`

— "For a thesis contribution" 这种 meta 语气破坏学术声音。
**判断：改写**。保留 "reusable principle" 的实质，去掉 framing。
建议改成：
> `"The method should expose a reusable principle, not just an accuracy improvement, which motivates the late-correction stance pursued in this chapter."`

### 1.3 Ch4 line 34 — Problem Setting 收尾段
原文：
> `"Relative to the rest of the thesis, this chapter therefore sits between symbolic completion and higher-level dynamic analysis. Unlike Chapter~\ref{ch:velcomp}, it operates on real audio and must cope with acoustically induced error. Unlike Chapter~\ref{ch:audiodyn}, its output remains note-level MIDI velocity rather than broader dynamic categories or change patterns. This middle position makes it a useful bridge in the thesis narrative."`

— Problem Setting 内部又做了一次章节定位。Overview 已经讲过。
**判断：整段删**。

### 1.4 Ch5 line 13 — Overview 第二段
原文：
> `"Instead of recovering note-level velocity, which is precise and directly editable, the present chapter targets a more interpretable score-facing representation. It therefore completes the thesis map by addressing the setting in which audio is the only available input and the desired output is a beat-synchronous symbolic description rather than raw note-level control."`

— "completes the thesis map" 是 meta。
**判断：改写或整段删**。可以合并进新的开头段，整个第二段都可以消失。

### 1.5 Ch5 line 43 — Problem Setting 收尾段
原文：
> `"This task directly matches the role assigned to Chapter~5 in the thesis plan: score-level dynamics should be represented as a beat-synchronous interface comprising dynamic levels, change points, and metrical structure. It also supports the broader thesis objective of recovering expressive labels without changing the underlying note content or timing."`

— "the role assigned to Chapter~5 in the thesis plan" 是 meta。实质内容（4-target 界面）line 32 已经讲过。
**判断：整段删**。

### 1.6 Ch6 line 17 — Overview 第二段
原文：
> `"From the thesis perspective, this chapter occupies a distinct position. It keeps the note-level MIDI velocity target and the score-informed VeloEst architecture introduced in Chapter~\ref{ch:scoreinf}, but it relaxes the assumption that ground-truth velocity labels are available for the target instrument. It complements Chapter~\ref{ch:audiodyn}... The chapter therefore contributes to thesis Requirement~R5 by combining numerical diagnostics, perceptual loudness correlations, and renderer-robust evaluation evidence, and to Requirement~R6 by treating beyond-piano transfer as a missing-supervision problem rather than ordinary acoustic domain shift."`

— 整本 thesis 最重的定位段。提到 R5/R6（这是 Introduction 的事）、桥接 Ch4 和 Ch5。
**判断：改写或删**。R5/R6 的映射应该在 Chapter 1，章节自己只讲方法学贡献就好。"keeps VeloEst, relaxes label assumption" 这个事实可以保留，但去掉 meta framing。

---

## 2. Starter（章节开头）深度不足

### 2.1 Ch3 line 17 — contributions list 太泛
原文：
> `"Second, it develops a U-Net-based model with window attention and a sparsity-aware loss tailored to this representation."`

"Develops a U-Net" 信息量为零——每篇 velocity paper 都"develops some network"。真正的 contribution 是 **2×2 windowed scaled-dot-product attention** + **onset-masked、velocity-boundary-weighted hybrid (BCE + CosSim) loss**。这两点都在 §3.6 Ablation 里被验证过。

**建议改成：**
> `"Second, it develops a U-Net backbone whose two design choices are tailored to the polyphonic-sparse setting: windowed scaled-dot-product attention with a 2×2 window for local polyphonic aggregation, and an onset-masked hybrid (BCE + cosine-similarity) loss with V-shaped weighting around the velocity-distribution boundary."`

### 2.2 Ch4 Overview — 最近改完了，没问题。

### 2.3 Ch5 Overview — 改完没问题。但 line 13 的第二段还是冗余（见 §1.4）。

### 2.4 Ch6 Overview — opener (line 11) 扎实；line 17 还是 meta（见 §1.6）。

---

## 3. Discussion 深度欠缺（最大的机会）

四个 content chapter 的 Discussion 深度差异巨大：Ch6 是 paper-grade，Ch3/Ch4/Ch5 都被压扁了。

### 3.1 Ch3 Discussion — 三处缺失的实质分析

**(a) Chopin Op.~10 No.~4 的 metric-failure 案例没被回收**
§3.5 Quantitative Results line 300 提到：
> `"...there are cases in which they fail to reflect perceptual differences. The Chopin Op.~10 No.~4 excerpt is one such example, where a mid-range local optimum produces superficially acceptable error values."`

这是一个教科书式的论点：**客观指标可以同时给出"合理"的 MAE 和一个听感平庸的输出**。Discussion 应该专门用一段讨论这种 metric-perception disagreement，并把它和 $SD_{velo}$ 的提出动机联系起来。

**(b) U-Net vs ConvAE 没有做机制性比较**
Table 3.2 给 U-Net 11.5 vs ConvAE 12.3 MAE on MAESTRO。读者只能猜原因。Ablation Summary 其实分得很清楚：
- 去掉 window attention 掉 0.8 MAE
- 去掉 weighting 掉 ~0.1 MAE
- 去掉 masking 掉更多

Discussion 应该综合一句：U-Net 的提升主要来自 **windowed local polyphonic aggregation**，不是 loss 调整。ConvAE 两个都没有。这才是 paper-grade 的解读。

**(c) $SD_{velo}$ 被当成 side metric，但实际上是方法学贡献**
它是揭穿"flat output 也能 MAE 不错"这种失败模式的关键指标。Discussion 应该给它一段，把它定位为 perception-aligned diagnostic，而不只是 5 个 metric 里的一个。

### 3.2 Ch4 Discussion — 三处缺失的实质分析

**(a) 对比 FiLM U-Net 的机制没分析**
Table 4.2 显示 Score-HPT 8.0 MAE / FiLM U-Net 9.9 MAE on SMD，参数还更少。FiLM 也是"structural prior"方法——所以"score as structural prior"不能解释差距。真正的差异在以下一个或多个：
1. Late vs early fusion（架构）
2. Onset-token sparse 表征 vs frame-wise dense（表征）
3. Hybrid (BCE+L1) onset-masked loss vs FiLM 的 loss
4. Bounded residual update `clip(v + α tanh(δ))` 限制 correction magnitude

新写的 line 325 段落（"acoustic invariance"）argue 了第 1 点，但 FiLM 的具体对比应该明确提出来。

**(b) Cross-backbone orthogonality 需要更强的 framing**
HPT (log-Mel), HPPNet (originally CQT), DynEst (originally BSSL) 覆盖了现代 AMT 的主要 acoustic representation 家族。同一个 correction module 在三个 backbone 上都给 ~1.5–2 MAE 提升。这比现在 Discussion 里写出来的更强地证明 representation-orthogonal information。

**(c) Robustness 实验范围没诚实标出**
Shift 实验用的是 **global** displacement ±0.1 到 ±2.5 s。实际的 alignment error 通常是 **non-uniform**（tempo-induced local drift）。Discussion line 314 应该加一句："Local, non-uniform mis-alignment of the kind produced by tempo drift is not tested here." 这预防 reviewer 反驳，也是诚实写作的范例。

### 3.3 Ch5 Discussion — 三处缺失 + 一个严重问题

**🚨 严重：Cross-dataset Vienna4x22 table (line 321–330) 全是 `pend` 占位符**

Table 5.5 entries `pend pend pend pend ... pend` 是占位值。这是 examiner 一眼能看到的硬伤。

选项：
- （最好）把实验跑完，填表。
- （可接受）降级到 Future Work / 删掉这个 table 和对应的 §5.7.3 段，换成 Limitations 里一句 forward-looking sentence。
- （最差）带着占位符送审。这在 viva 上是致命的。

**(a) 为什么 s=5 是 sweet spot 没解释**
Ablation 给：s=1 (avg 46.5), s=3 (53.9), s=5 (55.0), s=7 (54.4), s=9 (52.9)。U 型曲线，峰值在 5。Discussion 应该说：
- Beat/downbeat tracking 需要高时间分辨率（有效 ≥20 fps）
- Dynamic levels 和 change points 需要跨越至少一个 phrase 的 context（~4–8 s）
- s=5 在 50 fps base 下意味着最粗 branch 是 2 fps（0.5 s/frame）——刚够跨 phrase，其他 branch 保留 50 fps 精度
- s=9 over-compress，downbeat 掉得最厉害（数据印证）

这是 paper 版本一定有的 multi-scale design-rationale。

**(b) 为什么 BSSL 打败 log-Mel 没解读**
三个候选解释：
1. Perceptual compression (Bark scale) 本身就和 dynamics 对齐
2. 22-band vs 128-bin 降低了 memorise recording-specific bias 的容量
3. Band-wise structure 携带 register-dependent loudness cue

现在的 Discussion 没在这三个里选。即使承认"目前不知道哪个对，值得后续研究"也比沉默好。

**(c) §"Discussion: why score dynamics is not a relabelled MIDI velocity problem" 结构偏轻**
经过 §337/§341 修剪后只剩 3 个短段。对 PhD chapter 的 Discussion 来说太轻。考虑加一段讨论 **ordinality**：5 个 dynamic class (pp/p/mf/f/ff) 本身有序，但 categorical cross-entropy 把 `f` vs `pp` 和 `f` vs `mf` 当成同样错。Ordinal regression 会尊重这个顺序。这是一个值得承认的实在 limitation。

### 3.4 Ch6 Discussion — 已经 paper-grade

四个 substantive subsections：§"What the Recovered Velocity Represents", §"Why Pearson r on BSSL/BSTL", §"When Diff-Synth Should Still Be Preferred", §"Limitations"。直接拿这个 structure 当其他章节的 template。

---

## 4. 结构建议

Ch6 的 Discussion 结构在 Ch3/Ch4/Ch5 也推广一下：

```
\section{Discussion}
  \subsection{What the chapter establishes}      % 结果归纳
  \subsection{Why the chosen design works}       % 机制分析 + 文献对比
  \subsection{Where the result does / does not hold}  % 边界与限制
  \subsection{Broader implications}               % 方法学反思
```

这是"扩展会议论文"和"PhD chapter"的结构差距。

---

## 5. 攻克深度问题的优先级

1. **Ch5 Vienna4x22 占位符** —— 信誉风险，先处理。
2. **Ch3 Discussion 加 Chopin metric-failure + $SD_{velo}$ 方法学定位** —— 性价比最高的深度提升。
3. **Ch4 Discussion 加 FiLM 机制对比 + cross-backbone orthogonality 解读 + robustness 范围承认** —— 让本章最容易被驳的 claim 更难驳。
4. **Ch5 Discussion 加 s=5 / BSSL 的解读 + ordinality limitation** —— 把 Discussion 从 ablation report 升级成 methodology argument。
5. **把 Ch6 Discussion 结构推广到 Ch3/Ch4/Ch5** —— 一致性 pass。
6. **清掉 §1 的 6 处 thesis-positioning 残留** —— 快赢，低风险。

---

## 6. 引用的相关文件

- `/Users/hanyu/Documents/Thesis_v0/Chapter_3/chap3.tex`
- `/Users/hanyu/Documents/Thesis_v0/Chapter_4/chap4.tex`
- `/Users/hanyu/Documents/Thesis_v0/Chapter_5/chap5.tex`
- `/Users/hanyu/Documents/Thesis_v0/Chapter_6/chap6.tex`
- `/Users/hanyu/Documents/Thesis_v0/.claude/merge_paragraphs.py`（合并段落用的脚本）
- 备份：`/tmp/chap{3,4,5,6}.before.tex`
- 相关 review：`.claude/REFERENCES_REVIEW.md`、`.claude/FULL_THESIS_PROOFREAD.md`
