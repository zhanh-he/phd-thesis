# v5 精选修改：精确原文与最终提案

全部为未实施的建议。原文来自当前LaTeX，尚未认定正式送审PDF。旧DECISIONS、所有旧稿均保留；旧YES不自动批准新文字。N01/N02/N03/N07为同一个一致性组，须一起看。

[先看简短推荐](EDITORIAL_RECOMMENDATIONS_v5.md) · [独立评分](evidence/BLIND_CRITIQUE_C1.md) · [第二轮反向释义复核](evidence/CRITIQUE_C2.md)

<a id="t01"></a>

## T01 · R1-05

`Chapter_1/Intro.tex:114` · Insert immediately after the central question, before This question is studied...

把79词旧定义缩成45词；区分数据状态和监督条件，保留重叠和Ch6实例。

**原文位置：** 当前没有下列解释；周围原段保留，插入后的完整语境见本节末尾。方括号标记不是论文原句。

**推荐英文：**
```latex
Here, weakly expressive data retain note structure but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.
```

<details><summary>放回原段后的完整语境</summary>

```latex
 and directly usable by providing dynamics, whether as note-level MIDI velocity for production workflows, or as score dynamics for pedagogy and analysis.

\section{Unified Thesis Question and Three Core Scenarios}
\label{sec:intro:question}

The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}

Here, weakly expressive data retain note structure but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.


This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target. By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.

\begin{table}[h!]
\centering
\caption{The three core supervision scenarios studied in this thesis. Each scenario specifies the available data, the missing expressive layer, and the target output.}
\label{tab
```

</details>

<a id="t02"></a>

## T02 · R1-06

`Chapter_1/Intro.tex:114` · Insert after scenario table; S3 sentence and beyond-piano scope bullet receive separate v4 repairs.

保留aligned notes和S2关系；不再重新解释所有可能audio-only任务。

**原文位置：** 当前没有下列解释；周围原段保留，插入后的完整语境见本节末尾。方括号标记不是论文原句。

**推荐英文：**
```latex
Chapter~\ref{ch:beyondpiano} extends S2 to guitar when target-domain velocity labels are unavailable. It retains the score-informed estimator and aligned note events. Audio-only velocity adaptation remains future work; S3 instead targets score dynamics.
```

<details><summary>放回原段后的完整语境</summary>

```latex
xtbf{Available Data} & \textbf{Missing Expressive Layer} & \textbf{Target Output} \\
\midrule
S1 & MIDI note sequence & Note-level expressive intensity & MIDI velocity completion \\
S2 & Performance audio and aligned MIDI (score) & Reliable note-level expressive intensity & Score-informed MIDI velocity refinement \\
S3 & Performance audio only & Human-readable score dynamics and metrical coordinates & Beat-synchronous dynamic levels, beats, and downbeats \\
\bottomrule
\end{tabularx}
\end{table}

Chapter~\ref{ch:beyondpiano} extends S2 to guitar when target-domain velocity labels are unavailable. It retains the score-informed estimator and aligned note events. Audio-only velocity adaptation remains future work; S3 instead targets score dynamics.



\begin{figure}[ht]
  \centering
  \includegraphics[width=\linewidth]{Chapter_1/figures/Overview.jpg}
  \caption{Thesis roadmap within the expressive AMT pipeline. The diagram highlights the standalone sub-tasks of dynamics recovery and their corresponding chapters, ranging from symbolic MIDI velocity completion to direct audio-to-score dynamics estimation.}
  \label{fig:intro_overview}
\end{figure}

\section{Aim, Scope, and Assumptions}
\label{sec:intro:scope}

Building upon the strict assumption of structural preservation established in Section~\ref{sec:intro:gap_stance}, the empirical scope and boundaries of this thesis are defined as follows:

\begin{itemize}
    \item \textbf{Primary empirical focus on piano.} The main experimental focus is piano music. This is a practical constraint
```

</details>

<a id="t03"></a>

## T03 · R1-17

`Chapter_3/chap3.tex:26` · Replace this one related-work paragraph; preserve following Problem Setting.

同时回答二维输入、单通道输出和note-list取舍；保留原引用。

**准确原文：**
```latex
This motivates the image-based view adopted in the present chapter. By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly. U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic and does not rely on acoustic input \cite{he2025filling,kim2024method}. This makes the chapter a natural starting point for the broader thesis.
```

**推荐英文：**
```latex
We use piano rolls because the U-Net processes two-dimensional pitch--time neighbourhoods, including simultaneous notes. The input is binary and the output is a single-channel velocity roll, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
```

<details><summary>放回原段后的完整语境</summary>

```latex
d timing while improving only intensity. A velocity-only formulation is narrower, but it is also more controllable.

Recent symbolic velocity-prediction methods have typically treated the task as sequential prediction. Representative examples include convolutional autoencoders and sequence-to-sequence models with attention \cite{kuo2021velocity,kim2023piano}. These models establish that note-level velocity can be learned from symbolic context. However, piano-roll data is sparse and polyphonic. The relevant structure is not only sequential. It is also spatial. Simultaneous notes create meaningful vertical patterns, and short local pitch--time neighborhoods often carry clear expressive cues.

We use piano rolls because the U-Net processes two-dimensional pitch--time neighbourhoods, including simultaneous notes. The input is binary and the output is a single-channel velocity roll, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.

\section{Problem Setting}
\label{sec:velcomp:problem}

MIDI (Musical Instrument Digital Interface) is the dominant symbolic format in modern music production. A MIDI file that resembles sheet music can still sound mechanical when its note velocities are undefined or flattened to a default constant. In contrast, MIDI captured from human performance preserves the performer's control of intensity and therefore carries a substantial portion of the perceived musical expression. As discussed in the thesis introduction, dynamics is the expressive dimension targeted first in this thesis because it is both perceptually salient and directly editable. This chapter studies the most constrained setting
```

</details>

<a id="t04"></a>

## T04 · R1-23

`Chapter_4/chap4.tex:50` · Insert after modular-principle paragraph; original material before insertion remains.

邻段已讲应用场景；只补未评价joint note-detection收益这一必要边界。

**原文位置：** 当前没有下列解释；周围原段保留，插入后的完整语境见本节末尾。方括号标记不是论文原句。

**推荐英文：**
```latex
Note detection and velocity estimation may benefit from joint modelling, but this chapter evaluates velocity at supplied note onsets and does not test that benefit.
```

<details><summary>放回原段后的完整语境</summary>

```latex
roach and earlier score-informed feature-fusion approaches.}
\label{fig:scoreinf_compare}
\end{figure}

The interface of the proposed system is intentionally simple. The AMT backbone first predicts a preliminary velocity map from audio. The aligned score is then converted into symbolic features at the same time resolution. A lightweight score-informed module finally corrects the preliminary estimate at note onsets. This design has three practical advantages. First, it keeps the acoustic front end reusable. Second, it allows the correction module to be attached to several AMT backbones with only small engineering changes. Third, it constrains the score-informed stage to a narrow task. The module adjusts \emph{how loudly} a note is played. It does not decide \emph{whether} the note exists.

This separation of roles is important. The acoustic branch still provides the initial evidence for performance intensity. The score does not overwrite that evidence. Instead, it regularises the estimate by telling the model where notes occur and how they are organised in time. Later results will show that this division of labour is strong enough to improve both in-domain accuracy and cross-dataset behaviour.

Note detection and velocity estimation may benefit from joint modelling, but this chapter evaluates velocity at supplied note onsets and does not test that benefit.



\section{Score-Informed Correction Module}
\label{sec:scoreinf:method}

Figure~\ref{fig:scoreinf_framework} shows the complete framework. The score-informed module is attached after the velocity branch of a chosen AMT system. Only the velocity estimate is corrected. The rest of the transcription backbone remains unchanged.

\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth]{Chapter_4/figures/p2.jpg}
\caption{Proposed score-informed MIDI velocity estimation framework. The AMT backbone provides a preliminary velocity estimate. The score-informed module refines this estimate using features extracted from the aligned MIDI score.}
\label{fig:scoreinf_framework}
\end{figure}

\subsection{MIDI score features}
\label{sec:scoreinf:features}

Consistent with the standard paradigm 
```

</details>

<a id="t05"></a>

## T05 · R1-28

`Chapter_5/chap5.tex:38` · Append only the selected rationale to the existing target paragraph; preserve all class and grid definitions.

承认level变化也能给边界，再说本工作显式监督；不制造必要性或消融结果。

**原文位置：** 当前没有下列解释；周围原段保留，插入后的完整语境见本节末尾。方括号标记不是论文原句。

**推荐英文：**
```latex
Changes in the predicted level sequence could also define boundaries. The separate change-point head instead learns an explicit boundary target, while the level head predicts the dynamic state.
```

<details><summary>放回原段后的完整语境</summary>

```latex
 grid is already available from an aligned score or a score-level AMT system, and the predicted dynamic labels are attached to that grid. In the second mode, no score is available, and the model first predicts beats and downbeats by itself, then uses the estimated grid to place the dynamic labels.

More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat.

Changes in the predicted level sequence could also define boundaries. The separate change-point head instead learns an explicit boundary target, while the level head predicts the dynamic state.



This task directly matches the role assigned to Chapter~5 in the thesis plan: score-level dynamics should be represented as a beat-synchronous interface comprising dynamic levels, change points, and metrical structure. It also supports the broader thesis objective of recovering expressive labels without changing the underlying note content or timing.

\section{Perceptually Grounded Features and Multi-Scale Backbone}
\label{sec:audiodyn_features}

\subsection{Audio feature representations}
\label{ssec:audiodyn_features}

Log-Mel spectrograms serve as the standard input representation in many modern MIR systems, providing a natural baseline for both dynamics estimation and beat/downbeat tracking tasks. For a consistent comparison, we adopt the 50-fps log-Mel configuration used by Beat This
```

</details>

<a id="t06"></a>

## T06 · R1-31

`Chapter_6/chap6.tex:31` · Replace this paragraph only; preceding synthetic-data transfer paragraph and following Diff-Synth discussion remain.

直接讲piano-pretrained estimator在real audio上adapt；不声称更简单、更高效或消除域差异。

**准确原文：**
```latex
This chapter takes a different and simpler route. Instead of training on synthesised audio with synthetic labels, the front-end estimator is trained directly against real performance audio. The synthesiser is involved at training time only as a differentiable interface that connects predicted velocities to a measurable property of the real recording. This avoids the synthesis-to-performance domain gap that dominates synthetic-data transfer pipelines, at the cost of needing a differentiable supervision interface that is reliable across the instruments of interest.
```

**推荐英文：**
```latex
This chapter instead adapts a piano-pretrained estimator using real performance audio, without requiring target-domain velocity labels. A differentiable renderer or proxy supplies the training signal. Its match to the target recordings remains a limitation.
```

<details><summary>放回原段后的完整语境</summary>

```latex
ms to address the gap must operate without ground-truth note-level velocity supervision in the target domain.

\paragraph{Synthetic-data transfer for transcription.}
A common response to label scarcity in transcription is to train on synthesised audio, where symbolic labels are available by construction, and then transfer the model to real performances~\cite{maman2022general, zang2024synthtab, kusaka2025learn}. Recent works also use synthetic data and domain adaptation for annotation-free transcription and violin playing-technique recognition~\cite{sato2024annotationfree,wang2026vioptt}; these studies do not establish recovery of expressive note-level velocity on real non-piano recordings.

This chapter instead adapts a piano-pretrained estimator using real performance audio, without requiring target-domain velocity labels. A differentiable renderer or proxy supplies the training signal. Its match to the target recordings remains a limitation.

\paragraph{Differentiable waveform synthesisers.}
Differentiable digital signal processing provides a flexible route for embedding synthesis inside end-to-end learning~\cite{engel2020ddsp}. The same idea has been extended to MIDI-conditioned instrument synthesisers, including DDSP-Piano~\cite{renault2023ddsp_piano} and the string-wise guitar model of Jonason~\emph{et~al.}~\cite{jonason2024guitar}. The original guitar model uses a loudness-derived proxy for MIDI velocity. In the Diff-Synth path studied here, the instrument-specific back-ends render predicted velocities into audio for adaptation with an audio reconstruction loss. The DDSP family also includes integrated systems with detailed
```

</details>

<a id="t07"></a>

## T07 · R1-33

`Chapter_6/chap6.tex:111` · Replace discussion paragraph at end Diff-Synth subsection.

保留退化观察，明确fidelity/gradient未分开测；删掉较长解释。

**准确原文：**
```latex
The advantage of this interface is that it exposes the front end to rich waveform gradients. The risk, already noted in Section~\ref{sec:bp:related}, is that any timbral or recording mismatch between $\tilde{a}$ and $a$ also enters the gradient. When the synthesiser is not a faithful match for the target recordings, the gradient can become dominated by nuisance compensation rather than by velocity correction.
```

**推荐英文：**
```latex
The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately.
```

<details><summary>放回原段后的完整语境</summary>

```latex
}
\label{eq:bp_audio_loss}
\mathcal{L}_{\mathrm{audio}}
= \sum_{\omega \in \Omega} \Bigl(
\bigl\lVert \lvert\mathrm{STFT}_{\omega}(\tilde{a})\rvert - \lvert\mathrm{STFT}_{\omega}(a)\rvert \bigr\rVert_1 \\
+ \bigl\lVert \log(\lvert\mathrm{STFT}_{\omega}(\tilde{a})\rvert+\epsilon) - \log(\lvert\mathrm{STFT}_{\omega}(a)\rvert+\epsilon) \bigr\rVert_1
\Bigr),
\end{multline}
where $\Omega = \{2048, 1024, 512, 256, 128, 64\}$ as in~\cite{engel2020ddsp}. For each $\omega \in \Omega$, $\mathrm{STFT}_{\omega}$ uses an $\omega$-sample Hann window with $75\%$ overlap and an $\omega$-point FFT. The logarithm is applied to $\lvert\cdot\rvert + \epsilon$ with $\epsilon = 10^{-7}$ for numerical stability.

The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately.

\subsection{Adaptation via Diff-SFProxy}
\label{ssec:bp:adapt_diffsfproxy}

In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$
```

</details>

<a id="t08"></a>

## T08 · R2-02

`Chapter_1/Intro.tex:177` · Replace only opening paragraph of Thesis Organisation; retain chapter-by-chapter roadmap.

四篇co-authored studies与thesis synthesis说清即可；会议和作者清单交给已有Declaration。

**准确原文：**
```latex
Referring to Figure~\ref{fig:intro_overview}, the core methodological chapters (Chapters 3--5) preserve the technical contributions of their respective peer-reviewed publications, adapted to form a unified narrative.
```

**推荐英文：**
```latex
Chapters 3--6 are based on the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common label-recovery question, a shared account of dynamics representations, and the cross-chapter discussion of assumptions and limitations in Chapter~\ref{ch:conclusion}.
```

<details><summary>放回原段后的完整语境</summary>

```latex
framework for score-dynamics recovery (Addressing S3).} It proposes a compact multi-task multi-scale network that jointly estimates dynamic levels, change points, beats, and downbeats. It innovatively combines a perceptually motivated Bark-scale specific loudness front-end with task-aware decoding through MMoE \cite{he2026dynest,ma2018mmoe}.
  
    \item \textbf{An exploratory cross-instrument methodology.} It confronts the piano bias by investigating cross-instrument MIDI velocity estimation when true labels are scarce, employing a differentiable proxy for black-box synthesisers as part of the supervision signal.
\end{itemize}


\section{Thesis Organisation}
\label{sec:intro:organisation}

Chapters 3--6 are based on the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common label-recovery question, a shared account of dynamics representations, and the cross-chapter discussion of assumptions and limitations in Chapter~\ref{ch:conclusion}.

\textbf{Chapter~2} establishes the shared conceptual system, defining dynamics across audio, MIDI, and score, while reviewing baseline AMT models, datasets, and evaluation strategies.

\textbf{Chapter~3} addresses Scenario~S1. Supported by listening tests, it demonstrates that recovering a decoupled expressive layer on fixed symbolic notes is enough to transform a mechanical MIDI sequence into an expressive performance.

\textbf{Chapter~4} addresses Scenario~S2. It details the Transformer correction module, demonstrating superior generalisation under dataset shift and robustness to audio-to-score misalignment.

\textbf{Chapter~5} addresses Scenario~S3. It presents the multi-task framework 
```

</details>

<a id="t09"></a>

## T09 · R2-03

`Chapter_7/Conclusion.tex:113` · Replace this piano-centric limitation paragraph; Ch6 detailed sustained-control limitations remain.

保留Second顺序；piano/guitar已测与其他乐器未测在一段内讲清。

**准确原文：**
```latex
Second, the strongest direct supervision in the thesis remains piano-centric. This reflects the state of available velocity-labelled datasets rather than a belief that piano dynamics is the universal template for all instruments. Chapter~\ref{ch:beyondpiano} addresses this bias by moving into a label-scarce guitar setting, but the broader point remains: once the target instrument lacks direct performance-control labels, the interpretation of recovered velocity must be stated operationally.
```

**推荐英文：**
```latex
Second, the strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.
```

<details><summary>放回原段后的完整语境</summary>

```latex
oundaries. These boundaries are not artefacts of unfinished implementation; they follow from the problem definition and from the representational choices made throughout the dissertation.

First, the thesis focuses on dynamics rather than on the full space of musical expression. Timing, articulation, pedalling, timbre, and phrasing interact with dynamics in real performance. The systems developed here isolate dynamics because it is perceptually salient, directly useful for data curation, and recoverable under structural preservation. This isolation is methodologically useful, but it also means that the recovered layer is one dimension of expression rather than a complete performance model.

Second, the strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.

Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.

Fourth, several chapters assume that structural coordinates are available or recoverable. Score-informed velocity correction assumes aligned score events. The beyond-piano proxy framework 
```

</details>

<a id="t10"></a>

## T10 · R2-04

`Chapter_3/chap3.tex:445` · Replace listening Results paragraph only; MOS/CI table and participant/procedure descriptions remain.

旧v4 A仍胜出：mean similarity、11位听者/8段/一个renderer和composer分组范围都准确。

**准确原文：**
```latex
Although a substantial gap to human performance remains, the proposed U-Net clearly outperforms the other systems.
The Flat model performs worst, consistent with earlier findings that default velocity is musically inadequate \cite{kuo2021velocity}.
The seen, less-seen, and unseen repertoire groups are best interpreted as descriptive groups rather than as a strict complexity-controlled comparison.
Even so, the relatively narrow 95\% confidence intervals across groups suggest that participants rated the stimuli with reasonable consistency.
```

**推荐英文：**
```latex
U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.
```

<details><summary>放回原段后的完整语境</summary>

```latex
row{2}{*}{\textbf{Model}}}
& \multicolumn{4}{c}{\textbf{SMD dataset (selected corpus)}} \\
\cmidrule(l){2-5}
& \makecell{\textbf{Most Seen}\\\textbf{Compo. MOS} \(\uparrow\)}
& \makecell{\textbf{Less Seen}\\\textbf{Compo. MOS} \(\uparrow\)}
& \makecell{\textbf{Unseen}\\\textbf{Compo. MOS} \(\uparrow\)}
& \makecell{\textbf{Overall}\\\textbf{MOS} \(\uparrow\)} \\
\midrule
Flat & $1.58 \pm 0.36$ & $1.64 \pm 0.44$ & $1.18 \pm 0.42$ & $1.50 \pm 0.37$ \\
ConvAE & $1.93 \pm 0.34$ & $2.40 \pm 0.39$ & $1.80 \pm 0.44$ & $2.08 \pm 0.33$ \\
\textbf{U-Net} & $\mathbf{3.10 \pm 0.38}$ & $\mathbf{3.16 \pm 0.29}$ & $\mathbf{2.67 \pm 0.46}$ & $\mathbf{3.01 \pm 0.34}$ \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Results.}
U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.

\section{Discussion}
\label{sec:velcomp:discussion}

This chapter has verified that note-level dynamics can be recovered usefully even when the symbolic notes and timing are held fixed. It turns expressive enhancement into a controllable post-processing stage rather than a full performance-rendering problem, which is exactly the setting encountered in many MIDI-production and corpus-curation workflows.

The image-colourisation view is effective because it matches the structure of the data. Polyphonic note patterns create meaningful vertical and local spatial regularities that are awkward to express in purely sequential terms. The U-Net captures this local structure well, and the sparsity-a
```

</details>

<a id="n01"></a>

## N01 · NEW: metric interpretation

`Chapter_6/chap6.tex:501` · Replace paragraph interpreting GT-vs-Flat separation; keep table/numbers and next paragraph.

两种指标都把GT排在flat之上；gap数字本身不能证明哪种更敏感。

**准确原文：**
```latex
To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.
```

**推荐英文：**
```latex
Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.
```

<details><summary>放回原段后的完整语境</summary>

```latex
Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

Changing from Salamander to YDP while retaining the GT notes and velocities changes MAE by $0.193$ on BSSL and $1.723$ on BSTL; the corresponding changes in Pearson $r$ are $0.034$ and $0.011$. This tests the effect of the renderer change as a whole, rather than absolute gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.

We therefore use Pearson $r$ on BSSL/BSTL as the main measure of rendered loudness-contour agreement for label-free guitar evaluation. In this piano diagnostic, it distinguishes GT from flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.


```

</details>

<a id="n02"></a>

## N02 · NEW: renderer/gain inference

`Chapter_6/chap6.tex:503` · Replace one renderer-robustness paragraph; preserve table and no metric re-computation.

换SoundFont是renderer整体变化；不能隔离absolute gain，也不能直接比MAE与r量尺。

**准确原文：**
```latex
To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.
```

**推荐英文：**
```latex
Changing from Salamander to YDP while retaining the GT notes and velocities changes MAE by $0.193$ on BSSL and $1.723$ on BSTL; the corresponding changes in Pearson $r$ are $0.034$ and $0.011$. This tests the effect of the renderer change as a whole, rather than absolute gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.
```

<details><summary>放回原段后的完整语境</summary>

```latex
Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

Changing from Salamander to YDP while retaining the GT notes and velocities changes MAE by $0.193$ on BSSL and $1.723$ on BSTL; the corresponding changes in Pearson $r$ are $0.034$ and $0.011$. This tests the effect of the renderer change as a whole, rather than absolute gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.

We therefore use Pearson $r$ on BSSL/BSTL as the main measure of rendered loudness-contour agreement for label-free guitar evaluation. In this piano diagnostic, it distinguishes GT from flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.


```

</details>

<a id="t11"></a>

## T11 · R1-34

`Chapter_6/chap6.tex:126` · Replace only the last rationale sentence after beta=1.0 and 1:1 weighting; preserve equations/settings.

实际PDF说not established，不是did not conduct；不替作者添加否定实验历史。

**准确原文：**
```latex
The Huber form tolerates outliers from onset contamination such as overlapping notes, while the parameter-space objective concentrates gradients on note intensity and attack behaviour rather than on waveform details that are weakly related to velocity.
```

**推荐英文：**
```latex
We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE through a dedicated comparison.
```

<details><summary>放回原段后的完整语境</summary>

```latex
STFT}_{\omega}$ uses an $\omega$-sample Hann window with $75\%$ overlap and an $\omega$-point FFT. The logarithm is applied to $\lvert\cdot\rvert + \epsilon$ with $\epsilon = 10^{-7}$ for numerical stability.

The advantage of this interface is that it exposes the front end to rich waveform gradients. The risk, already noted in Section~\ref{sec:bp:related}, is that any timbral or recording mismatch between $\tilde{a}$ and $a$ also enters the gradient. When the synthesiser is not a faithful match for the target recordings, the gradient can become dominated by nuisance compensation rather than by velocity correction.

\subsection{Adaptation via Diff-SFProxy}
\label{ssec:bp:adapt_diffsfproxy}

In the Diff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE through a dedicated comparison.

The asymmetry between Eq.~\eqref{eq:bp_audio_loss} and Eq.~\eqref{eq:bp_param_loss} is the central design point of this chapter. The Diff-Synth path optimises in waveform/spectral space, where velocity is one of many factors influencing the signal. The Diff-SFProxy path optimises in a low-dimensional note-wise dynamics space, where velocity is the dominant factor by construction. The remainder of the chapter tests whether this difference matters in practice.

\subsection{Shared Regularisers and Total Objective}
\label{ssec:bp:regularisers}

Both adaptation paths share two auxiliary regularisers on the predicted onset-velocity distribution $\hat{\mathbf{v}} \in [0,1]^{N}$, where $N$ is the 
```

</details>

<a id="n03"></a>

## N03 · NEW: metric conclusion synchronisation

`Chapter_6/chap6.tex:505` · Replace the concluding metric-choice paragraph after N01/N02; do not leave the original fail/right-trade-off claim behind.

保留选择Pearson的正面理由，删掉cosine/MAE普遍失败的结论。

**准确原文：**
```latex
Pearson $r$ on BSSL/BSTL therefore provides the right trade-off for this chapter. Cosine similarity and MAE fail on sensitivity and robustness, respectively, and are kept only as diagnostic alternatives. This is also the reason the main results table reports $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ as the headline metrics for label-free guitar evaluation.
```

**推荐英文：**
```latex
We therefore use Pearson $r$ on BSSL/BSTL as the main measure of rendered loudness-contour agreement for label-free guitar evaluation. In this piano diagnostic, it distinguishes GT from flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

<details><summary>放回原段后的完整语境</summary>

```latex
Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

Changing from Salamander to YDP while retaining the GT notes and velocities changes MAE by $0.193$ on BSSL and $1.723$ on BSTL; the corresponding changes in Pearson $r$ are $0.034$ and $0.011$. This tests the effect of the renderer change as a whole, rather than absolute gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.

We therefore use Pearson $r$ on BSSL/BSTL as the main measure of rendered loudness-contour agreement for label-free guitar evaluation. In this piano diagnostic, it distinguishes GT from flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.


```

</details>

<a id="n04"></a>

## N04 · R1-33 missed background synchronisation

`Chapter_2/Background.tex:587` · Replace only this clause in the existing long paragraph; keep representations, comparison-space distinction and citations.

同步Ch2与Ch6：renderer mismatch可能影响梯度，不写必然主导。

**准确原文：**
```latex
so the gradient signal is dominated by factors unrelated to velocity.
```

**推荐英文：**
```latex
so renderer mismatch can divert the gradient from velocity-relevant differences.
```

<details><summary>放回原段后的完整语境</summary>

```latex
hat the downstream model can plausibly learn.

\subsection{Analysis-by-synthesis and label-scarce velocity recovery}
\label{sec:bg:synth:analysis}

The combination of differentiable rendering and prediction networks defines an \emph{analysis-by-synthesis} setting. A network proposes control values for an observed recording; the renderer turns those values back into audio (or into an intermediate audio-derived quantity); a loss compares the rendered output with the observed signal. This paradigm becomes the central tool when true note-level velocity labels are unavailable, because the renderer takes the place of a label by linking predicted control to a measurable property of the recording.

Two design axes matter for this thesis. The first is the comparison space. \emph{Signal-domain} losses (waveform or spectral) can be applied directly to the rendered output, but they conflate velocity with timbre, recording chain, and room response, so renderer mismatch can divert the gradient from velocity-relevant differences. \emph{Parameter-domain} or perceptual proxy losses instead extract a small set of velocity-relevant acoustic descriptors (e.g.\ note-wise loudness, attack envelope) from both the rendered and the observed audio and compare them in that lower-dimensional space. The latter is closer in spirit to the parameter-extraction proxies used in spectral-modelling research and trades waveform fidelity for stronger alignment with the velocity target. The second axis is the renderer's domain coverage. A differentiable renderer adapted to piano need not transfer to guitar or violin without further work~\cite{renault2023ddsp_piano,wiggins2023ddsp_guitar_model}, which is one of the practical constraints of cross-instrument analysis-by-synthesis.

For expressive AMT, this strategy is attractive but delicate. It makes label-scarce learning possible, yet it also ties the learning signal to the adequacy of the renderer: a proxy objective can reward compatibility with the synthesiser more than compatibility with real instrumental control, and reconstruction error is therefore not the same thing as accurate velocity recovery. Chapter~\ref{ch:beyondpiano} adopts the analysis-by-synthesis route explicitly under these constraints. It contrasts a waveform-domain DDSP-style supervision interface with a low-dimensional parameter-space proxy built from a frozen SoundFont teacher, and treats proxy supervision as a method family with explicit lim
```

</details>

<a id="n05a"></a>

## N05a · optional small deletion

`Chapter_7/Conclusion.tex:109` · Replace only this exact text; empty replacement means delete sentence.

删除无必要的审查姿态；不改后文实际限制。

**准确原文：**
```latex
The thesis has several boundaries. These boundaries are not artefacts of unfinished implementation; they follow from the problem definition and from the representational choices made throughout the dissertation.
```

**推荐英文：**
```latex
The thesis has several limitations.
```

<details><summary>放回原段后的完整语境</summary>

```latex
ared against Disklavier labels. A score-dynamics estimate can be compared against an editorial annotation convention. A beyond-piano renderer-conditioned velocity cannot claim to be the performer's physical gesture, but it can still be a useful control coordinate for resynthesis, curation, and expressive analysis.

The result is not that weaker supervision makes the task impossible. Rather, weaker supervision changes what can be claimed. Each claim is valid inside its representational boundary. The thesis contribution is to make those boundaries explicit instead of hiding them behind a single generic term such as dynamics.

\section{Limitations and Scope}
\label{sec:conclusion:limitations}

The thesis has several limitations.

First, the thesis focuses on dynamics rather than on the full space of musical expression. Timing, articulation, pedalling, timbre, and phrasing interact with dynamics in real performance. The systems developed here isolate dynamics because it is perceptually salient, directly useful for data curation, and recoverable under structural preservation. This isolation is methodologically useful, but it also means that the recovered layer is one dimension of expression rather than a complete performance model.

Second, the strongest direct supervision in the thesis remains piano-centric. This reflects the state of available velocity-labelled datasets rather than a belief that piano dynamics is t
```

</details>

<a id="n05b"></a>

## N05b · optional small deletion

`Chapter_7/Conclusion.tex:124` · Replace only this exact text; empty replacement means delete sentence.

未来工作开头无需替论文辩护。

**准确原文：**
```latex
The results of the thesis suggest several directions for future research. These directions extend the thesis argument rather than repair it.
```

**推荐英文：**
```latex
The results suggest several directions for future research.
```

<details><summary>放回原段后的完整语境</summary>

```latex
t symbolic interface. These assumptions are not weaknesses of the argument. They are the conditions under which label recovery, rather than unconstrained generation, becomes meaningful.

Finally, the thesis uses multiple forms of evidence rather than a single unified benchmark. This is necessary because the targets differ across chapters. It also means that the contributions should be read as a coherent scenario map, not as four entries in one leaderboard. The unifying object is not one architecture or one dataset. It is the recovery of musically interpretable dynamics under different structural and supervisory conditions.

\section{Future Research Directions}
\label{sec:conclusion:future}

The results suggest several directions for future research.

\subsection{Probabilistic bridges between dynamics representations}
\label{ssec:conclusion:future_bridge}

A natural direction is to model the relations between velocity, loudness, and score dynamics probabilistically. The thesis has deliberately avoided fixed lookup tables because they collapse representation-specific information. A stronger future model could instead treat the three layers as coupled but uncertain variables. A passage might support several plausible score-dynamic annotations, several possible velocity profiles, and several loudness realisations depending on instrument and performance style.

Such a model would allow consistency constraints without enforcing deterministic
```

</details>

<a id="n05c"></a>

## N05c · optional small deletion

`Chapter_7/Conclusion.tex:117` · Replace only this exact text; empty replacement means delete sentence.

保留条件含义，删掉不必要的反驳。

**准确原文：**
```latex
These assumptions are not weaknesses of the argument. They are the conditions under which label recovery, rather than unconstrained generation, becomes meaningful.
```

**推荐英文：**
```latex
These assumptions define the conditions for the label-recovery tasks studied here.
```

<details><summary>放回原段后的完整语境</summary>

```latex
ce guitar setting, but the broader point remains: once the target instrument lacks direct performance-control labels, the interpretation of recovered velocity must be stated operationally.

Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.

Fourth, several chapters assume that structural coordinates are available or recoverable. Score-informed velocity correction assumes aligned score events. The beyond-piano proxy framework assumes aligned note events. Audio-to-score dynamics estimates beats and downbeats, but still relies on the idea that beat-synchronous output is the right symbolic interface. These assumptions define the conditions for the label-recovery tasks studied here.

Finally, the thesis uses multiple forms of evidence rather than a single unified benchmark. This is necessary because the targets differ across chapters. It also means that the contributions should be read as a coherent scenario map, not as four entries in one leaderboard. The unifying object is not one architecture or one dataset. It is the recovery of musically interpretable dynamics under different structural and supervisory conditions.

\section{Future Research Directions}
\label{sec:conclusion:future}

The results of the thesis suggest several directions for future research. These directions extend the thesis argument rather than repair it.

\subsection{Probabilistic bridges between d
```

</details>

<a id="n06a"></a>

## N06a · optional small deletion

`Chapter_3/chap3.tex:71` · Replace only this exact text; empty replacement means delete sentence.

保留T=96和5/10/15/20秒实测比较；不以固定秒长推断完整乐句。

**准确原文：**
```latex
A plausible explanation is that a 10-second window often captures a musically coherent phrase, for example roughly four measures at 120 BPM, providing enough context without overextending the receptive field.
```

**推荐英文：**
```latex
[删除该句，不补新句]
```

<details><summary>放回原段后的完整语境</summary>

```latex
binary onset roll \(O\), marking note starts; a binary frame roll \(F\), indicating note activation over time; and a velocity roll \(V\), acting as the target colour intensity.
In the implemented system, \(F\) is the network input, \(V\) is the prediction target, and \(O\) is used for onset masking in the loss.
For the velocity roll, integer values in \([0,127]\) are normalised to \([0,1)\) to match the model output activation range.
During post-processing, the model output is denormalised by scaling and rounding back to integer MIDI velocity.
As illustrated in Figure~\ref{fig:velcomp_model}, these matrices are highly sparse.

\subsection{MIDI Segmentation}
\label{sec:velcomp:segmentation}

The segment duration is a key design variable in this formulation.
Because a MIDI performance often exceeds three minutes, we split each piece into shorter segments to keep the computation tractable.
The number of time frames \(T\) determines the temporal granularity of the matrix representation, so the timestep resolution is
\begin{equation}
\text{Resolution} = \frac{\text{Segment Duration}}{T}.
\label{eq:velcomp_resolution}
\end{equation}
Unlike tasks that require fine temporal resolution to detect unknown note events, the present task already assumes that note timing is given.
This makes a more computationally efficient timestep resolution feasible.
With a fixed input size of \(T=96\), we explored segment durations of 5 s, 10 s, 15 s, and 20 s in hyperparameter search and found that 10 s yielded the best results.


\begin{figure}[t]
\begin{center}
\includegraphics[width=\textwidth]{Chapter_3/figures/p2.png}
\caption{Proposed U-Net architecture. The model input (\(F\) roll) comprises 88 pitch bins and 96 time frames. Attn block denotes windowed scaled dot-product attention. The final velocity roll (\(V\) roll) is generated during post-processing by extracting velocity at note positions and assigning each note the velocity at its onset.}
\label{fig:velcomp_model}
\end{center}
\vspace{-12pt}
\end{figure}

\section{Model Architecture and Loss}
\label{sec:velcomp:model}

\subsection{U-Net with Window Attention}
\label{sec:velcomp:architecture}

The proposed architecture is shown in Figure~\ref{fig:velcomp
```

</details>

<a id="n06b"></a>

## N06b · optional small deletion

`Chapter_3/chap3.tex:358` · Replace only this exact text; empty replacement means delete sentence.

v4修了小节数，却仍可能留下完整乐句的无依据推断；只保留已报告结果。

**准确原文：**
```latex
This is likely because a 10-second segment roughly encompasses four measures at 120 beats per minute (BPM), forming a complete musical phrase that aids in semantic segmentation.
```

**推荐英文：**
```latex
[删除该句，不补新句]
```

<details><summary>放回原段后的完整语境</summary>

```latex
 & 10s & BCE $<m,w>$  & 11.5 & 227.6 & 9.4 & 63.6\% & 10.9 \\
\bottomrule
\end{tabular}
\end{table*}


\textbf{Window attention mechanism.} We evaluated different attention configurations to assess their impact. Removing attention reduced performance, which highlighted the attention mechanism's role in focusing on salient features and improved U-Net's performance. The 1×1 window attention (i.e., global attention) was tested alongside \{2×2, 4×4, 8×8\} windows, with GPU memory requirements gradually reducing. Among these, 2×2 window attention performed best. The result shows that while window attention mitigates MIDI sparsity, large windows over-compress information, reducing effectiveness.

\textbf{MIDI segment duration.} The analysis shows that reducing it from 20 to 10 seconds improves performance, while further reduction to 5 seconds slightly worsens the accuracy metrics. 

\textbf{Loss function.} Training with BCE loss alone produced a wide velocity dispersion (highest \(SD_{\text{velo}}\)), but this came with the lowest accuracy metrics. Applying the masking $<m>$ improved accuracy but reduced \(SD_{\text{velo}}\) as a trade-off. The weighting $<w>$ encouraged predictions to deviate from the mean, increasing both \(SD_{\text{velo}}\) and accuracy metrics. Finally, adding CosSim achieved the highest overall accuracy, with a negligible drop in \(SD_{\text{velo}}\). This combined loss function $\mathcal{L}_{\mathrm{Comb}}^{<m,w>}$ was recognised as the optimal configuration and applied in the training of both U-Net and ConvAE.

% The application of masking $<m
```

</details>
