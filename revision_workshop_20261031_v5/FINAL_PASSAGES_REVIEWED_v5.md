# 可供选择的最终文字：原文、英文提案与连读语境

这些文字的解释更具体，少重复和防御语气；原本清楚的图注、听测稿和技术细节保留。**thesis正文未动，作者尚未批准。**

组合语境仅演示20项选文、N07和23项已列明依赖；不是44项执行决定清单，不表示43项评审事项全部关闭。旧YES不继承，KEEP单项不自动批准其他范围。

当前LaTeX是工作坐标，正式送审PDF仍待确认。来源、事实待核和准确范围见[共同复核记录](FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md)与[依赖清单](DEPENDENCIES_REVIEWED_v5.json)。

<a id="t01"></a>

## T01 · `Chapter_1/Intro.tex:114`

范围：Insert immediately after the central question, before This question is studied...

原有段落保留；此项是新增解释，下面的完整连读显示插入位置。

提案英文：
```latex
Here, weakly expressive data retain note content and timing but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\section{Unified Thesis Question and Three Core Scenarios}
\label{sec:intro:question}

The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}

Here, weakly expressive data retain note content and timing but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.


This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} uses an \textit{audio-only} input to jointly estimate dynamic markings and the metrical coordinates needed for a \textit{score-facing} output. These settings form the core empirical arc of the thesis by varying both the available evidence and the target representation.

\begin{table}[h!]
\centering
\caption{The three core supervision scenarios studied in this thesis. Each scenario specifies the available data, the missing expressive layer, and the target output.}
\label{tab:intro_scenarios}
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Scenario} & \textbf{Available Data} & \textbf{Missing Expressive Layer} & \textbf{Target Output} \\
\midrule
S1 & MIDI note sequence & Note-level expressive intensity & MIDI velocity completion \\
S2 & Performance audio and aligned MIDI (score) & Reliable note-level expressive intensity & Score-informed MIDI velocity refinement \\
S3 & Performance audio only & Human-readable score dynamics and metrical coordinates & Beat-synchronous dynamic levels, beats, and downbeats \\
\bottomrule
\end{tabularx}
\end{table}
```

</details>

此处预览带入：V4-scope-1, V4-R1-15-sync-4。

<a id="t02"></a>

## T02 · `Chapter_1/Intro.tex:114`

范围：Insert after scenario table; S3 sentence and beyond-piano scope bullet receive separate v4 repairs.

原有段落保留；此项是新增解释，下面的完整连读显示插入位置。

提案英文：
```latex
Chapter~\ref{ch:beyondpiano} extends S2 to guitar when target-domain velocity labels are unavailable. It retains the score-informed estimator and aligned note events. Audio-only velocity adaptation remains future work; S3 instead targets score dynamics.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} uses an \textit{audio-only} input to jointly estimate dynamic markings and the metrical coordinates needed for a \textit{score-facing} output. These settings form the core empirical arc of the thesis by varying both the available evidence and the target representation.

\begin{table}[h!]
\centering
\caption{The three core supervision scenarios studied in this thesis. Each scenario specifies the available data, the missing expressive layer, and the target output.}
\label{tab:intro_scenarios}
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.15}
\begin{tabularx}{\textwidth}{l X X X}
\toprule
\textbf{Scenario} & \textbf{Available Data} & \textbf{Missing Expressive Layer} & \textbf{Target Output} \\
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
```

</details>

此处预览带入：V4-scope-1, V4-R1-15-sync-4。

<a id="t03"></a>

## T03 · `Chapter_3/chap3.tex:26`

范围：Replace this one related-work paragraph; preserve following Problem Setting.

准确原文：
```latex
This motivates the image-based view adopted in the present chapter. By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly. U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic and does not rely on acoustic input \cite{he2025filling,kim2024method}. This makes the chapter a natural starting point for the broader thesis.
```

提案英文：
```latex
We use a piano roll to place simultaneous notes and local pitch--time neighbourhoods on a regular grid for the convolutional U-Net. The input is binary; the single-channel output supplies velocity values, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
MIDI velocity completion sits at the intersection of expressive rendering and symbolic refinement. Broad expressive-rendering systems often predict timing, articulation, and dynamics jointly \cite{jeong2019virtuosonet,borovik2023scoreperformer}. These systems are important, but they are not ideal when the practical goal is to preserve a user's note content and timing while improving only intensity. A velocity-only formulation is narrower, but it is also more controllable.

Recent symbolic velocity-prediction methods have typically treated the task as sequential prediction. Representative examples include convolutional autoencoders and sequence-to-sequence models with attention \cite{kuo2021velocity,kim2023piano}. These models establish that note-level velocity can be learned from symbolic context. However, piano-roll data is sparse and polyphonic. The relevant structure is not only sequential. It is also spatial. Simultaneous notes create meaningful vertical patterns, and short local pitch--time neighborhoods often carry clear expressive cues.

We use a piano roll to place simultaneous notes and local pitch--time neighbourhoods on a regular grid for the convolutional U-Net. The input is binary; the single-channel output supplies velocity values, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.

\section{Problem Setting}
\label{sec:velcomp:problem}

MIDI (Musical Instrument Digital Interface) is the dominant symbolic format in modern music production. A MIDI file that resembles sheet music can still sound mechanical when its note velocities are undefined or flattened to a default constant. In contrast, MIDI captured from human performance preserves the performer's control of intensity and therefore carries a substantial portion of the perceived musical expression. As discussed in the thesis introduction, dynamics is the expressive dimension targeted first in this thesis because it is both perceptually salient and directly editable. This chapter studies the symbolic-only setting in that map: recovering note-level MIDI velocity when the symbolic notes and their timing are already known.

\begin{figure}[t]
\begin{center}
\includegraphics[width=0.86\textwidth]{Chapter_3/figures/p1.png}
\caption{Comparison between MIDI notes with human-performed velocity and music-software default velocity (64 when unspecified). The standard deviation of velocity (\(SD_{\text{velo}}\)) represents the dispersion of velocities around their mean across pitches.}
\label{fig:velcomp_intro}
\end{center}
\end{figure}

This setting is practically important for two reasons. First, a large amount of MIDI used in digital audio workstation workflows is created by step input, quantisation, or low-cost controllers, leaving velocity flat. Second, many expressive rendering systems modify several performance dimensions jointly, including timing and sometimes note content, which is undesirable when the goal is to preserve the user's composition. By isolating velocity, the task becomes a precise and controllable refinement problem: the notes, onsets, and offsets remain fixed, and only note intensity is completed.

This chapter instead exploits the spatial structure of polyphonic symbolic music by treating MIDI as an image-colourisation problem. MIDI without velocity is represented as a binary pianoroll, while the target is a velocity-valued pianoroll. This formulation is especially natural for instruments such as piano, where multiple simultaneous notes create rich vertical patterns. Current dataset availability restricts the experiments here to piano data, but the formulation itself is not tied to piano alone.

\section{Representation as Image-like MIDI Matrices}
\label{sec:velcomp:representation}

\subsection{Matrix Representation}
\label{sec:velcomp:matrix}

To process MIDI as images, we convert each performance into three matrices of size \(T \times P\), where \(T\) is the number of time frames and \(P=88\) is the number of piano pitches.
The three matrices are a binary onset roll \(O\), marking note starts; a binary frame roll \(F\), indicating note activation over time; and a velocity roll \(V\), acting as the target colour intensity.
In the implemented system, \(F\) is the network input, \(V\) is the prediction target, and \(O\) is used for onset masking in the loss.
For the velocity roll, integer values in \([0,127]\) are normalised to \([0,1)\) to match the model output activation range.
During post-processing, the model output is denormalised by scaling and rounding back to integer MIDI velocity.
As illustrated in Figure~\ref{fig:velcomp_model}, these matrices are highly sparse.
```

</details>

此处预览带入：V4-R1-15-sync-1。

<a id="t04"></a>

## T04 · `Chapter_4/chap4.tex:50`

范围：Insert after modular-principle paragraph; original material before insertion remains.

原有段落保留；此项是新增解释，下面的完整连读显示插入位置。

提案英文：
```latex
Note detection and velocity estimation may benefit from joint modelling, but this chapter evaluates velocity at supplied note onsets and does not test that benefit.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
The interface of the proposed system is intentionally simple. The AMT backbone first predicts a preliminary velocity map from audio. The aligned score is then converted into symbolic features at the same time resolution. A lightweight score-informed module finally corrects the preliminary estimate at note onsets. This design has three practical advantages. First, it keeps the acoustic front end reusable. Second, it allows the correction module to be attached to several AMT backbones with only small engineering changes. Third, it constrains the score-informed stage to a narrow task. The module adjusts \emph{how loudly} a note is played. It does not decide \emph{whether} the note exists.

This separation of roles is important. The acoustic branch still provides the initial evidence for performance intensity. The score does not overwrite that evidence. Instead, it regularises the estimate by telling the model where notes occur and how they are organised in time. Later results will show that this division of labour is strong enough to improve both in-domain accuracy and cross-dataset behaviour.

Note detection and velocity estimation may benefit from joint modelling, but this chapter evaluates velocity at supplied note onsets and does not test that benefit.



\section{Score-Informed Correction Module}
\label{sec:scoreinf:method}
```

</details>

<a id="t05"></a>

## T05 · `Chapter_5/chap5.tex:38`

范围：Append only the selected rationale to the existing target paragraph; preserve all class and grid definitions.

原有段落保留；此项是新增解释，下面的完整连读显示插入位置。

提案英文：
```latex
Changes in the predicted level sequence could also define boundaries. The separate change-point head instead learns an explicit boundary target, while the level head predicts the dynamic state.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
Given a piano performance audio signal, the system predicts four synchronised output sequences on a frame grid: dynamic levels, dynamic change points, beats, and downbeats. The dynamic targets are the score-facing outputs, while beats and downbeats provide the metrical structure required to align these labels to a symbolic score. This joint design serves two practical modes of use. In the first mode, a reliable beat grid is already available from an aligned score or a score-level AMT system, and the predicted dynamic labels are attached to that grid. In the second mode, no score is available, and the model first predicts beats and downbeats by itself, then uses the estimated grid to place the dynamic labels.

More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat.

Changes in the predicted level sequence could also define boundaries. The separate change-point head instead learns an explicit boundary target, while the level head predicts the dynamic state.



This task directly matches the role assigned to Chapter~5 in the thesis plan: score-level dynamics should be represented as a beat-synchronous interface comprising dynamic levels, change points, and metrical structure. It also supports the broader thesis objective of recovering expressive labels without changing the underlying note content or timing.
```

</details>

<a id="t06"></a>

## T06 · `Chapter_6/chap6.tex:31`

范围：Replace this paragraph only; preceding synthetic-data transfer paragraph and following Diff-Synth discussion remain.

准确原文：
```latex
This chapter takes a different and simpler route. Instead of training on synthesised audio with synthetic labels, the front-end estimator is trained directly against real performance audio. The synthesiser is involved at training time only as a differentiable interface that connects predicted velocities to a measurable property of the real recording. This avoids the synthesis-to-performance domain gap that dominates synthetic-data transfer pipelines, at the cost of needing a differentiable supervision interface that is reliable across the instruments of interest.
```

提案英文：
```latex
This chapter instead adapts a piano-pretrained estimator using real performance audio, without requiring target-domain velocity labels. A differentiable renderer or proxy supplies the training signal. Its match to the target recordings remains a limitation.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\paragraph{Velocity estimation has so far been almost exclusively a piano problem.}
Learning-based velocity estimation from performance audio recovers expressive labels well, but almost entirely in the piano domain~\cite{jeong2018timbre, simonetta2022acoustics, kim2024method}. The reason is data: piano datasets such as MAESTRO~\cite{hawthorne2019maestro} provide note-aligned velocity labels sourced from Yamaha Disklavier performances. For guitar, violin, and many other instruments, public datasets~\cite{tamer2023violin, riley2024gaps, riley2024high} provide audio and aligned notes but no velocity labels. This precludes both supervised training and label-based domain transfer. The asymmetry between piano and other instruments is therefore not primarily a modelling gap but a labelling gap, and any method that aims to address the gap must operate without ground-truth note-level velocity supervision in the target domain.

\paragraph{Synthetic-data transfer for transcription.}
A common response to label scarcity in transcription is to train on synthesised audio, where symbolic labels are available by construction, and then transfer the model to real performances~\cite{maman2022general, zang2024synthtab, kusaka2025learn}. Recent works also use synthetic data and domain adaptation for annotation-free transcription and violin playing-technique recognition~\cite{sato2024annotationfree,wang2026vioptt}; these studies do not establish recovery of expressive note-level velocity on real non-piano recordings.

This chapter instead adapts a piano-pretrained estimator using real performance audio, without requiring target-domain velocity labels. A differentiable renderer or proxy supplies the training signal. Its match to the target recordings remains a limitation.

\paragraph{Differentiable waveform synthesisers.}
Differentiable digital signal processing provides a flexible route for embedding synthesis inside end-to-end learning~\cite{engel2020ddsp}. The same idea has been extended to MIDI-conditioned instrument synthesisers, including DDSP-Piano~\cite{renault2023ddsp_piano} and the string-wise guitar model of Jonason~\emph{et~al.}~\cite{jonason2024guitar}. The original guitar model uses a loudness-derived proxy for MIDI velocity. In the Diff-Synth path studied here, the instrument-specific back-ends render predicted velocities into audio for adaptation with an audio reconstruction loss. The DDSP family also includes integrated systems with detailed expressive control~\cite{wu2022mididdsp}.
```

</details>

<a id="t07"></a>

## T07 · `Chapter_6/chap6.tex:111`

范围：Replace discussion paragraph at end Diff-Synth subsection.

准确原文：
```latex
The advantage of this interface is that it exposes the front end to rich waveform gradients. The risk, already noted in Section~\ref{sec:bp:related}, is that any timbral or recording mismatch between $\tilde{a}$ and $a$ also enters the gradient. When the synthesiser is not a faithful match for the target recordings, the gradient can become dominated by nuisance compensation rather than by velocity correction.
```

提案英文：
```latex
The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
In the Diff-Synth path, the back-end is a frozen, instrument-specific differentiable waveform synthesiser. Given note events $E$ derived from the aligned score and the predicted velocities $\hat{V}$, Diff-Synth renders audio $\tilde{a}$. We use instrument-specific adaptations of DDSP-Piano~\cite{renault2023ddsp_piano} and the string-wise guitar synthesiser of~\cite{jonason2024guitar} as the piano and guitar waveform back-ends, respectively.

The adaptation loss is the multi-scale spectral loss of~\cite{engel2020ddsp}, which is widely adopted in the differentiable synthesiser family~\cite{renault2023ddsp_piano, jonason2024guitar, wu2022mididdsp}. It is applied between the rendered audio $\tilde{a}$ and the real performance audio $a$:
\begin{multline}
\label{eq:bp_audio_loss}
\mathcal{L}_{\mathrm{audio}}
= \sum_{\omega \in \Omega} \Bigl(
\bigl\lVert \lvert\mathrm{STFT}_{\omega}(\tilde{a})\rvert - \lvert\mathrm{STFT}_{\omega}(a)\rvert \bigr\rVert_1 \\
+ \bigl\lVert \log(\lvert\mathrm{STFT}_{\omega}(\tilde{a})\rvert+\epsilon) - \log(\lvert\mathrm{STFT}_{\omega}(a)\rvert+\epsilon) \bigr\rVert_1
\Bigr),
\end{multline}
where $\Omega = \{2048, 1024, 512, 256, 128, 64\}$ as in~\cite{engel2020ddsp}. For each $\omega \in \Omega$, $\mathrm{STFT}_{\omega}$ uses an $\omega$-sample Hann window with $75\%$ overlap and an $\omega$-point FFT. The logarithm is applied to $\lvert\cdot\rvert + \epsilon$ with $\epsilon = 10^{-7}$ for numerical stability.

The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.

\subsection{Adaptation via Diff-SFProxy}
\label{ssec:bp:adapt_diffsfproxy}
```

</details>

<a id="t08"></a>

## T08 · `Chapter_1/Intro.tex:177`

范围：Replace only opening paragraph of Thesis Organisation; retain chapter-by-chapter roadmap.

准确原文：
```latex
Referring to Figure~\ref{fig:intro_overview}, the core methodological chapters (Chapters 3--5) preserve the technical contributions of their respective peer-reviewed publications, adapted to form a unified narrative.
```

提案英文：
```latex
Chapters 3--6 are based on the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common label-recovery question, a shared account of dynamics representations, and the cross-chapter discussion of assumptions and limitations in Chapter~\ref{ch:conclusion}.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\section{Thesis Organisation}
\label{sec:intro:organisation}

Chapters 3--6 are based on the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common label-recovery question, a shared account of dynamics representations, and the cross-chapter discussion of assumptions and limitations in Chapter~\ref{ch:conclusion}.

\textbf{Chapter~2} establishes the shared conceptual system, defining dynamics across audio, MIDI, and score, while reviewing baseline AMT models, datasets, and evaluation strategies.

\textbf{Chapter~3} addresses Scenario~S1. It shows that velocity completion can improve expressive rendering on fixed symbolic notes, supported by objective evaluation and the listening study.

\textbf{Chapter~4} addresses Scenario~S2. It details the Transformer correction module, demonstrating superior generalisation under dataset shift and robustness to audio-to-score misalignment.

\textbf{Chapter~5} addresses Scenario~S3. It presents the multi-task framework to extract human-readable score dynamics alongside their metrical anchors directly from audio.

\textbf{Chapter~6} acts as an exploratory extension. It probes the frontier where direct velocity labels disappear, testing a route for cross-instrument MIDI velocity estimation via proxy supervision.

\textbf{Chapter~7} synthesises the findings across the four studies, states the limitations clearly, and outlines future directions for expressive AMT.
```

</details>

此处预览带入：V4-R2-04-sync-3。

<a id="t09"></a>

## T09 · `Chapter_7/Conclusion.tex:113`

范围：Replace this piano-centric limitation paragraph; Ch6 detailed sustained-control limitations remain.

准确原文：
```latex
Second, the strongest direct supervision in the thesis remains piano-centric. This reflects the state of available velocity-labelled datasets rather than a belief that piano dynamics is the universal template for all instruments. Chapter~\ref{ch:beyondpiano} addresses this bias by moving into a label-scarce guitar setting, but the broader point remains: once the target instrument lacks direct performance-control labels, the interpretation of recovered velocity must be stated operationally.
```

提案英文：
```latex
Second, the strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
The thesis has several boundaries.

First, the thesis focuses on dynamics rather than on the full space of musical expression. Timing, articulation, pedalling, timbre, and phrasing interact with dynamics in real performance. The systems developed here isolate dynamics because it is perceptually salient, directly useful for data curation, and recoverable under structural preservation. This isolation is methodologically useful, but it also means that the recovered layer is one dimension of expression rather than a complete performance model.

Second, the strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.

Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.
```

</details>

<a id="t10"></a>

## T10 · `Chapter_3/chap3.tex:445`

范围：Replace listening Results paragraph only; MOS/CI table and participant/procedure descriptions remain.

准确原文：
```latex
Although a substantial gap to human performance remains, the proposed U-Net clearly outperforms the other systems.
The Flat model performs worst, consistent with earlier findings that default velocity is musically inadequate \cite{kuo2021velocity}.
The seen, less-seen, and unseen repertoire groups are best interpreted as descriptive groups rather than as a strict complexity-controlled comparison.
Even so, the relatively narrow 95\% confidence intervals across groups suggest that participants rated the stimuli with reasonable consistency.
```

提案英文：
```latex
U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\begin{table}[h]
\centering
\caption{Listening-test results. MOS values with 95\% confidence intervals are reported. ``Most seen'' composers include \{Chopin, Bach, Beethoven\}; ``less seen'' composers include \{Rachmaninoff, Haydn, Mozart\}; and ``unseen'' composers include \{Bart\'ok, Ravel\}. Best score is highlighted in bold.}
\label{tab:velcomp_mos}
% \scriptsize                        % 控制字体, 把字体切到 LaTeX 预定义的小字号
\setlength{\tabcolsep}{7pt}          % 控制表格列与列之间的左右留白
\fontsize{11pt}{13pt}\selectfont     % 直接设置字体大小和行高
\renewcommand{\arraystretch}{1.2}    % 控制表格行高倍率
% 调整结束
\begin{tabular}{l|cccc}
\toprule
\multicolumn{1}{c|}{\multirow{2}{*}{\textbf{Model}}}
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
```

</details>

<a id="n01"></a>

## N01 · `Chapter_6/chap6.tex:501`

范围：Replace paragraph interpreting GT-vs-Flat separation; keep table/numbers and next paragraph.

准确原文：
```latex
To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.
```

提案英文：
```latex
Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\subsection{Why Pearson \texorpdfstring{$r$}{r} on BSSL/BSTL}
\label{ssec:bp:metric_diagnostic}

Table~\ref{tab:bp_metric_diagnostic} tests three candidate metrics, Pearson correlation $r$, cosine similarity $cs$, and MAE on BSSL and BSTL, against the two requirements implied above: sensitivity to expressive dynamics and robustness to renderer-specific loudness calibration. Real audio is compared with GT-note resynthesis under either ground-truth or flat velocity, and using either the Salamander default piano or the alternative YDP Grand Piano.

\begin{table}[!ht]
\caption{MAESTRO metric diagnostic. Real audio is compared with GT-note resynthesis using GT or flat velocity under the Salamander (default) or YDP Grand Piano. Summary rows show GT-Flat separation and SoundFont drift.}
\label{tab:bp_metric_diagnostic}
\centering
\fontsize{11pt}{13pt}\selectfont
\setlength{\tabcolsep}{11pt}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{l||ccc|ccc}
\toprule
\multicolumn{1}{c||}{\multirow{3}{*}{\textbf{Method}}}
& \multicolumn{6}{c}{\textbf{MAESTRO test set}} \\
\cmidrule(l){2-7}
& \multicolumn{3}{c|}{\textbf{BSSL}} & \multicolumn{3}{c}{\textbf{BSTL}} \\
\cmidrule(lr){2-4} \cmidrule(l){5-7}
& $r$ & $cs$ & MAE & $r$ & $cs$ & MAE \\
\midrule
\textbf{GT velocity}            & 0.870 & 0.939 & 0.702 & 0.883 & 0.975 & 3.706 \\
\,-\, uses YDP Piano            & 0.836 & 0.926 & 0.510 & 0.872 & 0.973 & 1.983 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & 0.034 & 0.013 & 0.193
                                & 0.011 & 0.002 & 1.723 \\
\midrule
\textbf{Flat velocity = 64}     & 0.752 & 0.887 & 0.786 & 0.620 & 0.928 & 4.065 \\
\,-\, uses YDP Piano            & 0.733 & 0.883 & 0.637 & 0.617 & 0.930 & 2.750 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & 0.019 & 0.004 & 0.149
                                & 0.003 & 0.002 & 1.314 \\
\midrule
\textbf{$\Delta$ (GT $-$ Flat)}
                                & +0.118 & +0.052 & -0.083
                                & +0.263 & +0.047 & -0.359 \\
\bottomrule
\end{tabular}
\end{table}

Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.

For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement while reducing dependence on absolute level. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

</details>

<a id="n02"></a>

## N02 · `Chapter_6/chap6.tex:503`

范围：Replace one renderer-robustness paragraph; preserve table and no metric re-computation.

准确原文：
```latex
To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.
```

提案英文：
```latex
Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\subsection{Why Pearson \texorpdfstring{$r$}{r} on BSSL/BSTL}
\label{ssec:bp:metric_diagnostic}

Table~\ref{tab:bp_metric_diagnostic} tests three candidate metrics, Pearson correlation $r$, cosine similarity $cs$, and MAE on BSSL and BSTL, against the two requirements implied above: sensitivity to expressive dynamics and robustness to renderer-specific loudness calibration. Real audio is compared with GT-note resynthesis under either ground-truth or flat velocity, and using either the Salamander default piano or the alternative YDP Grand Piano.

\begin{table}[!ht]
\caption{MAESTRO metric diagnostic. Real audio is compared with GT-note resynthesis using GT or flat velocity under the Salamander (default) or YDP Grand Piano. Summary rows show GT-Flat separation and SoundFont drift.}
\label{tab:bp_metric_diagnostic}
\centering
\fontsize{11pt}{13pt}\selectfont
\setlength{\tabcolsep}{11pt}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{l||ccc|ccc}
\toprule
\multicolumn{1}{c||}{\multirow{3}{*}{\textbf{Method}}}
& \multicolumn{6}{c}{\textbf{MAESTRO test set}} \\
\cmidrule(l){2-7}
& \multicolumn{3}{c|}{\textbf{BSSL}} & \multicolumn{3}{c}{\textbf{BSTL}} \\
\cmidrule(lr){2-4} \cmidrule(l){5-7}
& $r$ & $cs$ & MAE & $r$ & $cs$ & MAE \\
\midrule
\textbf{GT velocity}            & 0.870 & 0.939 & 0.702 & 0.883 & 0.975 & 3.706 \\
\,-\, uses YDP Piano            & 0.836 & 0.926 & 0.510 & 0.872 & 0.973 & 1.983 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & 0.034 & 0.013 & 0.193
                                & 0.011 & 0.002 & 1.723 \\
\midrule
\textbf{Flat velocity = 64}     & 0.752 & 0.887 & 0.786 & 0.620 & 0.928 & 4.065 \\
\,-\, uses YDP Piano            & 0.733 & 0.883 & 0.637 & 0.617 & 0.930 & 2.750 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & 0.019 & 0.004 & 0.149
                                & 0.003 & 0.002 & 1.314 \\
\midrule
\textbf{$\Delta$ (GT $-$ Flat)}
                                & +0.118 & +0.052 & -0.083
                                & +0.263 & +0.047 & -0.359 \\
\bottomrule
\end{tabular}
\end{table}

Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.

For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement while reducing dependence on absolute level. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

</details>

<a id="t11"></a>

## T11 · `Chapter_6/chap6.tex:126`

范围：Replace only the last rationale sentence after beta=1.0 and 1:1 weighting; preserve equations/settings.

准确原文：
```latex
The Huber form tolerates outliers from onset contamination such as overlapping notes, while the parameter-space objective concentrates gradients on note intensity and attack behaviour rather than on waveform details that are weakly related to velocity.
```

提案英文：
```latex
We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
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
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$). We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE.

The asymmetry between Eq.~\eqref{eq:bp_audio_loss} and Eq.~\eqref{eq:bp_param_loss} is the central design point of this chapter. The Diff-Synth path optimises in waveform/spectral space, where velocity is one of many factors influencing the signal. The Diff-SFProxy path optimises in a low-dimensional note-wise dynamics space, where velocity is the dominant factor by construction. The remainder of the chapter tests whether this difference matters in practice.
```

</details>

<a id="n03"></a>

## N03 · `Chapter_6/chap6.tex:505`

范围：Replace the concluding metric-choice paragraph after N01/N02; do not leave the original fail/right-trade-off claim behind.

准确原文：
```latex
Pearson $r$ on BSSL/BSTL therefore provides the right trade-off for this chapter. Cosine similarity and MAE fail on sensitivity and robustness, respectively, and are kept only as diagnostic alternatives. This is also the reason the main results table reports $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ as the headline metrics for label-free guitar evaluation.
```

提案英文：
```latex
For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement while reducing dependence on absolute level. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\subsection{Why Pearson \texorpdfstring{$r$}{r} on BSSL/BSTL}
\label{ssec:bp:metric_diagnostic}

Table~\ref{tab:bp_metric_diagnostic} tests three candidate metrics, Pearson correlation $r$, cosine similarity $cs$, and MAE on BSSL and BSTL, against the two requirements implied above: sensitivity to expressive dynamics and robustness to renderer-specific loudness calibration. Real audio is compared with GT-note resynthesis under either ground-truth or flat velocity, and using either the Salamander default piano or the alternative YDP Grand Piano.

\begin{table}[!ht]
\caption{MAESTRO metric diagnostic. Real audio is compared with GT-note resynthesis using GT or flat velocity under the Salamander (default) or YDP Grand Piano. Summary rows show GT-Flat separation and SoundFont drift.}
\label{tab:bp_metric_diagnostic}
\centering
\fontsize{11pt}{13pt}\selectfont
\setlength{\tabcolsep}{11pt}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{l||ccc|ccc}
\toprule
\multicolumn{1}{c||}{\multirow{3}{*}{\textbf{Method}}}
& \multicolumn{6}{c}{\textbf{MAESTRO test set}} \\
\cmidrule(l){2-7}
& \multicolumn{3}{c|}{\textbf{BSSL}} & \multicolumn{3}{c}{\textbf{BSTL}} \\
\cmidrule(lr){2-4} \cmidrule(l){5-7}
& $r$ & $cs$ & MAE & $r$ & $cs$ & MAE \\
\midrule
\textbf{GT velocity}            & 0.870 & 0.939 & 0.702 & 0.883 & 0.975 & 3.706 \\
\,-\, uses YDP Piano            & 0.836 & 0.926 & 0.510 & 0.872 & 0.973 & 1.983 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & 0.034 & 0.013 & 0.193
                                & 0.011 & 0.002 & 1.723 \\
\midrule
\textbf{Flat velocity = 64}     & 0.752 & 0.887 & 0.786 & 0.620 & 0.928 & 4.065 \\
\,-\, uses YDP Piano            & 0.733 & 0.883 & 0.637 & 0.617 & 0.930 & 2.750 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & 0.019 & 0.004 & 0.149
                                & 0.003 & 0.002 & 1.314 \\
\midrule
\textbf{$\Delta$ (GT $-$ Flat)}
                                & +0.118 & +0.052 & -0.083
                                & +0.263 & +0.047 & -0.359 \\
\bottomrule
\end{tabular}
\end{table}

Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.

Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.

For label-free guitar evaluation, we use Pearson $r$ on BSSL/BSTL to measure rendered loudness-contour agreement while reducing dependence on absolute level. In the piano diagnostic, it scores GT above flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics.
```

</details>

<a id="n04"></a>

## N04 · `Chapter_2/Background.tex:587`

范围：Replace only this clause in the existing long paragraph; keep representations, comparison-space distinction and citations.

准确原文：
```latex
so the gradient signal is dominated by factors unrelated to velocity.
```

提案英文：
```latex
so renderer mismatch can divert the gradient from velocity-relevant differences.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
The combination of differentiable rendering and prediction networks defines an \emph{analysis-by-synthesis} setting. A network proposes control values for an observed recording; the renderer turns those values back into audio (or into an intermediate audio-derived quantity); a loss compares the rendered output with the observed signal. This paradigm becomes the central tool when true note-level velocity labels are unavailable, because the renderer takes the place of a label by linking predicted control to a measurable property of the recording.

Two design axes matter for this thesis. The first is the comparison space. \emph{Signal-domain} losses (waveform or spectral) can be applied directly to the rendered output, but they conflate velocity with timbre, recording chain, and room response, so renderer mismatch can divert the gradient from velocity-relevant differences. \emph{Parameter-domain} or perceptual proxy losses instead extract a small set of velocity-relevant acoustic descriptors (e.g.\ note-wise loudness, attack envelope) from both the rendered and the observed audio and compare them in that lower-dimensional space. The latter is closer in spirit to the parameter-extraction proxies used in spectral-modelling research and trades waveform fidelity for stronger alignment with the velocity target. The second axis is the renderer's domain coverage. A differentiable renderer adapted to piano need not transfer to guitar or violin without further work~\cite{renault2023ddsp_piano,wiggins2023ddsp_guitar_model}, which is one of the practical constraints of cross-instrument analysis-by-synthesis.

For expressive AMT, this strategy is attractive but delicate. It makes label-scarce learning possible, yet it also ties the learning signal to the adequacy of the renderer: a proxy objective can reward compatibility with the synthesiser more than compatibility with real instrumental control, and reconstruction error is therefore not the same thing as accurate velocity recovery. Chapter~\ref{ch:beyondpiano} adopts the analysis-by-synthesis route explicitly under these constraints. It contrasts a waveform-domain DDSP-style supervision interface with a low-dimensional parameter-space proxy built from a frozen SoundFont teacher, and treats proxy supervision as a method family with explicit limits rather than as a universal substitute for true note-level labels.
```

</details>

<a id="n05a"></a>

## N05a · `Chapter_7/Conclusion.tex:109`

范围：Replace only this exact text; empty replacement means delete sentence.

准确原文：
```latex
The thesis has several boundaries. These boundaries are not artefacts of unfinished implementation; they follow from the problem definition and from the representational choices made throughout the dissertation.
```

提案英文：
```latex
The thesis has several boundaries.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\section{Limitations and Scope}
\label{sec:conclusion:limitations}

The thesis has several boundaries.

First, the thesis focuses on dynamics rather than on the full space of musical expression. Timing, articulation, pedalling, timbre, and phrasing interact with dynamics in real performance. The systems developed here isolate dynamics because it is perceptually salient, directly useful for data curation, and recoverable under structural preservation. This isolation is methodologically useful, but it also means that the recovered layer is one dimension of expression rather than a complete performance model.

Second, the strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.

Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.

Fourth, several chapters assume that structural coordinates are available or recoverable. Score-informed velocity correction assumes aligned score events. The beyond-piano proxy framework assumes aligned note events. Audio-to-score dynamics estimates beats and downbeats, but still relies on the idea that beat-synchronous output is the right symbolic interface. These assumptions define the conditions for the label-recovery tasks studied here.

Finally, the thesis uses multiple forms of evidence rather than a single unified benchmark. This is necessary because the targets differ across chapters. It also means that the contributions should be read as a coherent scenario map, not as four entries in one leaderboard. The unifying object is not one architecture or one dataset. It is the recovery of musically interpretable dynamics under different structural and supervisory conditions.
```

</details>

<a id="n05b"></a>

## N05b · `Chapter_7/Conclusion.tex:124`

范围：Replace only this exact text; empty replacement means delete sentence.

准确原文：
```latex
The results of the thesis suggest several directions for future research. These directions extend the thesis argument rather than repair it.
```

提案英文：
```latex
The results suggest several directions for future research.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
Finally, the thesis uses multiple forms of evidence rather than a single unified benchmark. This is necessary because the targets differ across chapters. It also means that the contributions should be read as a coherent scenario map, not as four entries in one leaderboard. The unifying object is not one architecture or one dataset. It is the recovery of musically interpretable dynamics under different structural and supervisory conditions.

\section{Future Research Directions}
\label{sec:conclusion:future}

The results suggest several directions for future research.

\subsection{Probabilistic bridges between dynamics representations}
\label{ssec:conclusion:future_bridge}
```

</details>

<a id="n05c"></a>

## N05c · `Chapter_7/Conclusion.tex:117`

范围：Replace only this exact text; empty replacement means delete sentence.

准确原文：
```latex
These assumptions are not weaknesses of the argument. They are the conditions under which label recovery, rather than unconstrained generation, becomes meaningful.
```

提案英文：
```latex
These assumptions define the conditions for the label-recovery tasks studied here.
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\section{Limitations and Scope}
\label{sec:conclusion:limitations}

The thesis has several boundaries.

First, the thesis focuses on dynamics rather than on the full space of musical expression. Timing, articulation, pedalling, timbre, and phrasing interact with dynamics in real performance. The systems developed here isolate dynamics because it is perceptually salient, directly useful for data curation, and recoverable under structural preservation. This isolation is methodologically useful, but it also means that the recovered layer is one dimension of expression rather than a complete performance model.

Second, the strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.

Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.

Fourth, several chapters assume that structural coordinates are available or recoverable. Score-informed velocity correction assumes aligned score events. The beyond-piano proxy framework assumes aligned note events. Audio-to-score dynamics estimates beats and downbeats, but still relies on the idea that beat-synchronous output is the right symbolic interface. These assumptions define the conditions for the label-recovery tasks studied here.

Finally, the thesis uses multiple forms of evidence rather than a single unified benchmark. This is necessary because the targets differ across chapters. It also means that the contributions should be read as a coherent scenario map, not as four entries in one leaderboard. The unifying object is not one architecture or one dataset. It is the recovery of musically interpretable dynamics under different structural and supervisory conditions.
```

</details>

<a id="n06a"></a>

## N06a · `Chapter_3/chap3.tex:71`

范围：Replace only this exact text; empty replacement means delete sentence.

准确原文：
```latex
A plausible explanation is that a 10-second window often captures a musically coherent phrase, for example roughly four measures at 120 BPM, providing enough context without overextending the receptive field.
```

提案英文：
```latex
[删除该句，不加新句]
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
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
```

</details>

<a id="n06b"></a>

## N06b · `Chapter_3/chap3.tex:358`

范围：Replace only this exact text; empty replacement means delete sentence.

准确原文：
```latex
This is likely because a 10-second segment roughly encompasses four measures at 120 beats per minute (BPM), forming a complete musical phrase that aids in semantic segmentation.
```

提案英文：
```latex
[删除该句，不加新句]
```

<details><summary>放回全文的完整段落／相邻语境（含明确依赖）</summary>

```latex
\textbf{Window attention mechanism.} We evaluated different attention configurations to assess their impact. Removing attention reduced performance, which highlighted the attention mechanism's role in focusing on salient features and improved U-Net's performance. The 1×1 window attention (i.e., global attention) was tested alongside \{2×2, 4×4, 8×8\} windows, with GPU memory requirements gradually reducing. Among these, 2×2 window attention performed best. The result shows that while window attention mitigates MIDI sparsity, large windows over-compress information, reducing effectiveness.

\textbf{MIDI segment duration.} The analysis shows that reducing it from 20 to 10 seconds improves performance, while further reduction to 5 seconds slightly worsens the accuracy metrics. 

\textbf{Loss function.} Training with BCE loss alone produced a wide velocity dispersion (highest \(SD_{\text{velo}}\)), but this came with the lowest accuracy metrics. Applying the masking $<m>$ improved accuracy but reduced \(SD_{\text{velo}}\) as a trade-off. The weighting $<w>$ encouraged predictions to deviate from the mean, increasing both \(SD_{\text{velo}}\) and accuracy metrics. Finally, adding CosSim achieved the highest overall accuracy, with a negligible drop in \(SD_{\text{velo}}\). This combined loss function $\mathcal{L}_{\mathrm{Comb}}^{<m,w>}$ was recognised as the optimal configuration and applied in the training of both U-Net and ConvAE.
```

</details>

## N07：指标表格式

[准确表格副本](N07_TABLE_MARKUP_REVIEWED_v5.tex)。移除跨指标数值best/second-best强调，并删掉GT−Flat共用向上箭头；58个数值token及其顺序完全保留。不从舍入端点重算0.193。
