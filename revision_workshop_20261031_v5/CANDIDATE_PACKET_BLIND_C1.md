# Anonymous candidate packet — cycle 1

Read source evidence before scoring. Codes conceal provenance; do not infer quality from order. Some insertions compete with no added prose. Some unchanged incumbents can tie. Score hard gates before preferences.

## Rubric
Hard gates: (1) semantic/technical fidelity to supplied manuscript, (2) factual support / no invented result. FAIL excludes a candidate. Then ordinal 0–3 (0=misses need,1=partial,2=adequate,3=strong) for reviewer response, author voice, necessity/minor-revision scope, cohesion on reinsertion, clarity/brevity. Do NOT sum into precise composite. Pairwise choose winner and runner-up with concrete wording and one-sentence reason. KEEP can win. Readability counts are flags only.

Voice reference: use concrete task → input/target → method reason → measured outcome/limit. Prefer note-level MIDI velocity, aligned note events, score dynamics, renderer-conditioned. Use we for actual method choice; do not turn absence of documented evidence into proof the experiment never happened. Retain British thesis spelling, citations and mathematical anchors. Real source voice card is separate.

## T01

Source: `Chapter_1/Intro.tex`; anchor: `The thesis is driven by`

Operation: Insert immediately after the central question, before This question is studied...

Need: Define weakly expressive and weak supervision.

Evidence: Author response 1.3: notes/timing exist but velocities flattened (64) or coarse; weak supervision = missing/low-quality labels. Ch6 uses renderer-based supervision. Data conditions may overlap.

Context before:
```latex
g? The goal is to make existing music data more expressive and directly usable by providing dynamics, whether as note-level MIDI velocity for production workflows, or as score dynamics for pedagogy and analysis.

\section{Unified Thesis Question and Three Core Scenarios}
\label{sec:intro:question}

The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target. By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.

\begin{table}[h!]
\centering
\caption{The three core supervision scenarios studied in this thesis. Each scenario specifies the available data, the mi
```

Context after:
```latex
Insertion must not repeat definitions in this supplied context.
```

### T01-K

```latex
Weakly expressive describes the data: note content and timing are available, but dynamics are flattened or coarsened. Weakly supervised describes the learning setting: reliable target labels are unavailable, so the estimator uses indirect evidence. Chapter~\ref{ch:beyondpiano} studies the latter setting.
```

### T01-L

```latex
Here, weakly expressive data retain note structure but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.
```

### T01-M

```latex
In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. Weakly supervised settings lack reliable target labels for direct training; Chapter 6 instead uses real audio and a renderer-based comparison to supervise the velocity estimator indirectly. These terms describe the available information rather than the quality of the musical performance. These conditions can overlap in the same dataset.
```

### T01-N

```latex
[No additional paragraph.]
```

## T02

Source: `Chapter_1/Intro.tex`; anchor: `The thesis is driven by`

Operation: Insert after scenario table; S3 sentence and beyond-piano scope bullet receive separate v4 repairs.

Need: Would audio-to-MIDI-velocity also be a scenario, particularly Chapter 6?

Evidence: Ch6 uses score-informed HPT with aligned note events. Author says audio-only adaptation not established. S3 here is Ch5 score-dynamics target. No same-protocol 3x MAE evidence.

Context before:
```latex
g? The goal is to make existing music data more expressive and directly usable by providing dynamics, whether as note-level MIDI velocity for production workflows, or as score dynamics for pedagogy and analysis.

\section{Unified Thesis Question and Three Core Scenarios}
\label{sec:intro:question}

The thesis is driven by the following question:
\begin{quote}
\textbf{How can musically interpretable dynamics labels be recovered from incomplete, weakly expressive, or weakly supervised music data without rewriting note content or note timing?}
\end{quote}
This question is studied under three core scenarios, outlined in Table~\ref{tab:intro_scenarios}. These scenarios represent a clear methodological progression. \textbf{Scenario S1} isolates the recovery task to a strict \textit{symbolic-only} setting. \textbf{Scenario S2} introduces acoustic evidence but maintains a reliable structural prior via an \textit{audio-plus-score} alignment. Finally, \textbf{Scenario S3} removes structural support entirely, tackling the fully open, \textit{audio-only} setting to recover a \textit{score-facing} target. By intentionally ordering these environments from the tightly constrained to the ambiguous, they form the core empirical arc of the thesis.

\begin{table}[h!]
\centering
\caption{The three core supervision scenarios studied in this thesis. Each scenario specifies the available data, the mi
```

Context after:
```latex
Insertion must not repeat definitions in this supplied context.
```

### T02-K

```latex
Chapter~\ref{ch:beyondpiano} extends S2 to guitar when target-domain velocity labels are unavailable. It retains the score-informed estimator and aligned note events. Audio-only velocity adaptation remains future work; S3 instead targets score dynamics.
```

### T02-L

```latex
Audio-only MIDI velocity estimation is a related task, but it is not the setting studied in Chapter~\ref{ch:beyondpiano}. That chapter retains the aligned notes used in S2 and replaces direct velocity supervision with a renderer-based comparison.
```

### T02-M

```latex
The input condition alone does not determine the dynamics target. Audio-only MIDI velocity estimation is also possible, but S3 refers specifically to the score-dynamics task studied in Chapter 5. The beyond-piano study in Chapter 6 uses the score-informed estimator from Chapter 4 and still requires aligned note events. It therefore extends S2 under weaker target-domain supervision rather than adding an audio-only velocity experiment.
```

### T02-N

```latex
[No additional paragraph.]
```

## T03

Source: `Chapter_3/chap3.tex`; anchor: `This motivates the image-based view`

Operation: Replace this one related-work paragraph; preserve following Problem Setting.

Need: Explain image-based/colourisation and piano roll versus note lists.

Evidence: Author response: binary roll to single-channel velocity roll, 2D convolutions; no RGB. Actual model F input / V target / O loss mask; P=88 and T=96. Do not claim causal superiority over all event representations.

Context before:
```latex
ted Work}
\label{sec:velcomp:related}

MIDI velocity completion sits at the intersection of expressive rendering and symbolic refinement. Broad expressive-rendering systems often predict timing, articulation, and dynamics jointly \cite{jeong2019virtuosonet,borovik2023scoreperformer}. These systems are important, but they are not ideal when the practical goal is to preserve a user's note content and timing while improving only intensity. A velocity-only formulation is narrower, but it is also more controllable.

Recent symbolic velocity-prediction methods have typically treated the task as sequential prediction. Representative examples include convolutional autoencoders and sequence-to-sequence models with attention \cite{kuo2021velocity,kim2023piano}. These models establish that note-level velocity can be learned from symbolic context. However, piano-roll data is sparse and polyphonic. The relevant structure is not only sequential. It is also spatial. Simultaneous notes create meaningful vertical patterns, and short local pitch--time neighborhoods often carry clear expressive cues.
```

Context after:
```latex
\section{Problem Setting}
\label{sec:velcomp:problem}

MIDI (Musical Instrument Digital Interface) is the dominant symbolic format in modern music production. A MIDI file that resembles sheet music can still sound mechanical when its note velocities are undefined or flattened to a default constant. In contrast, MIDI captured from human performance preserves the performer's control of intensity and therefore carries a substantial portion of the perceived musical expression. As discussed in the thesis introduction, dynamics is the expressive dimension targeted first in this thesis because it is both perceptually salient and directly editable. This chapter studies the most constrained setting in that map: recovering note-level MIDI velocity when the symbolic notes and their timing are already known.

\begin{figure}[t]
\begin{center}
\includegraphics[width=0.86\textwidth]{Chapter_3/figures/p1.png}
\caption{Comparison between MIDI notes with human-performed velocity and music-software default velocity (64 when unspecified). The standard deviation of velocity (\(SD_{\text{velo}}\)) repre
```

### T03-K

```latex
A piano roll places simultaneous notes along the pitch axis and their local evolution along time, giving the U-Net a regular two-dimensional input. Convolution and skip connections can then use local pitch–time neighbourhoods while preserving the given note structure. The output is a single-channel velocity roll. We use colourisation as an analogy for completing that missing scalar layer, rather than for predicting RGB colour. This representation motivates the U-Net and attention design used here \cite{he2025filling,kim2024method}.
```

### T03-L

```latex
This motivates the image-based view adopted in the present chapter. By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly. U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic and does not rely on acoustic input \cite{he2025filling,kim2024method}. This makes the chapter a natural starting point for the broader thesis.
```

### T03-M

```latex
We use piano rolls because the U-Net processes two-dimensional pitch--time neighbourhoods, including simultaneous notes. The input is binary and the output is a single-channel velocity roll, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
```

### T03-N

```latex
A piano roll gives the U-Net a regular pitch--time grid, with simultaneous notes aligned along the pitch axis. The binary input represents note structure; the single-channel output adds velocity values. Colourisation describes this missing-layer analogy, rather than RGB prediction. This representation supports the convolutional U-Net and window attention used here \cite{he2025filling,kim2024method}.
```

## T04

Source: `Chapter_4/chap4.tex`; anchor: `This separation of roles is important.`

Operation: Insert after modular-principle paragraph; original material before insertion remains.

Need: Is separate velocity refinement ecologically valid? Joint modelling may improve notes.

Evidence: Known score notes are supplied; no complete note-accuracy improvement evaluated. Ch4 already gives education/archives use cases and modularity rationale.

Context before:
```latex
d reusable. Second, it allows the correction module to be attached to several AMT backbones with only small engineering changes. Third, it constrains the score-informed stage to a narrow task. The module adjusts \emph{how loudly} a note is played. It does not decide \emph{whether} the note exists.

This separation of roles is important. The acoustic branch still provides the initial evidence for performance intensity. The score does not overwrite that evidence. Instead, it regularises the estimate by telling the model where notes occur and how they are organised in time. Later results will show that this division of labour is strong enough to improve both in-domain accuracy and cross-dataset behaviour.

\section{Score-Informed Correction Module}
\label{sec:scoreinf:method}

Figure~\ref{fig:scoreinf_framework} shows the complete framework. The score-informed module is attached after the velocity branch of a chosen AMT system. Only the velocity estimate is corrected. The rest of the transcription backbone remains unchanged.

\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth]{Chapter_4/figures/p2.jpg}
\caption{Proposed score-informed MIDI velocity estimation framework. The AMT backbone provides a preliminary velocity estimate. The score-informed module refines this estimate using features extracted from the aligned MIDI score.}
\label{fig:scoreinf_framework}
\end{
```

Context after:
```latex
Insertion must not repeat definitions in this supplied context.
```

### T04-K

```latex
The separation suits applications with trusted note events. Note detection and velocity estimation may benefit from joint modelling, but this chapter evaluates velocity at supplied note onsets and does not test that benefit.
```

### T04-L

```latex
[No additional paragraph.]
```

### T04-M

```latex
This modular setting is useful when trusted note events already exist, as in aligned educational or archival material. It does not imply that velocity and note detection are independent in performance, or that joint modelling cannot improve transcription. The present evaluation isolates velocity estimation at known notes and therefore does not measure gains in note detection.
```

### T04-N

```latex
This setting assumes that note events are already reliable. When note decisions are uncertain, joint note-and-velocity estimation may be useful. Here, the aim is to refine the velocity layer of an existing sequence.
```

## T05

Source: `Chapter_5/chap5.tex`; anchor: `More specifically, the dynamic-level target`

Operation: Append only the selected rationale to the existing target paragraph; preserve all class and grid definitions.

Need: Why an explicit change-point head rather than beat/downbeat level predictions alone?

Evidence: Original paragraph defines frame outputs, beat sampling and beat-snapped change points. No isolated change-point causal gain established. A boundary can be derived from level transitions.

Context before:
```latex
grid is already available from an aligned score or a score-level AMT system, and the predicted dynamic labels are attached to that grid. In the second mode, no score is available, and the model first predicts beats and downbeats by itself, then uses the estimated grid to place the dynamic labels.

More specifically, the dynamic-level target is formulated as a six-class frame-wise prediction problem, including one \textit{blank} class before the first annotated marking and the five score-dynamics classes used in MazurkaBL: \textit{pp}, \textit{p}, \textit{mf}, \textit{f}, and \textit{ff}. The change-point target is binary and indicates whether a contextual transition between adjacent dynamic regimes occurs at a given time. Beats and downbeats are also binary frame-wise targets. At inference time, the frame-wise outputs are converted into beat-synchronous score annotations by sampling the dynamic class at beat locations and snapping detected change points to the nearest beat.

This task directly matches the role assigned to Chapter~5 in the thesis plan: score-level dynamics should be represented as a beat-synchronous interface comprising dynamic levels, change points, and metrical structure. It also supports the broader thesis objective of recovering expressive labels without changing the underlying note content or timing.

\section{Perceptually Grounded Features and Multi-Scale
```

Context after:
```latex
Insertion must not repeat definitions in this supplied context.
```

### T05-K

```latex
We give change points a separate head to supervise transitions directly, alongside the prevailing dynamic level. This complements the beat-wise level output.
```

### T05-L

```latex
The separate change-point head gives transitions an explicit supervision target, instead of deriving boundaries only from changes in the predicted level sequence. It complements the beat-wise level output by modelling when a new dynamic region begins.
```

### T05-M

```latex
Changes in the predicted level sequence could also define boundaries. The separate change-point head instead learns an explicit boundary target, while the level head predicts the dynamic state.
```

### T05-N

```latex
[No additional rationale beyond the existing target definitions.]
```

## T06

Source: `Chapter_6/chap6.tex`; anchor: `This chapter takes a different and simpler route.`

Operation: Replace this paragraph only; preceding synthetic-data transfer paragraph and following Diff-Synth discussion remain.

Need: Do not assert modelling simplicity without evidence; author suggested efficiency but no cost comparison.

Evidence: ISMIR paper says more direct route; adaptation on real recordings via differentiable renderer/proxy. Need retain that interface does not eliminate mismatch. No runtime/cost superiority measured.

Context before:
```latex
ier performances. For guitar, violin, and many other instruments, public datasets~\cite{tamer2023violin, riley2024gaps, riley2024high} provide audio and aligned notes but no velocity labels. This precludes both supervised training and label-based domain transfer. The asymmetry between piano and other instruments is therefore not primarily a modelling gap but a labelling gap, and any method that aims to address the gap must operate without ground-truth note-level velocity supervision in the target domain.

\paragraph{Synthetic-data transfer for transcription.}
A common response to label scarcity in transcription is to train on synthesised audio, where symbolic labels are available by construction, and then transfer the model to real performances~\cite{maman2022general, zang2024synthtab, kusaka2025learn}. Recent works also use synthetic data and domain adaptation for annotation-free transcription and violin playing-technique recognition~\cite{sato2024annotationfree,wang2026vioptt}; these studies do not establish recovery of expressive note-level velocity on real non-piano recordings.
```

Context after:
```latex
\paragraph{Differentiable waveform synthesisers.}
Differentiable digital signal processing provides a flexible route for embedding synthesis inside end-to-end learning~\cite{engel2020ddsp}. The same idea has been extended to MIDI-conditioned instrument synthesisers, including DDSP-Piano~\cite{renault2023ddsp_piano} and the string-wise guitar model of Jonason~\emph{et~al.}~\cite{jonason2024guitar}. The original guitar model uses a loudness-derived proxy for MIDI velocity. In the Diff-Synth path studied here, the instrument-specific back-ends render predicted velocities into audio for adaptation with an audio reconstruction loss. The DDSP family also includes integrated systems with detailed expressive control~\cite{wu2022mididdsp}.

Two limitations of waveform-level supervision are relevant here. First, a Diff-Synth only approximates the real instrument; its waveform statistics differ from real recordings in timbre, articulation, microphone response, and room acoustics. A waveform or spectral loss therefore spends much of its gradient budget on residual mismatch rather than on veloc
```

### T06-K

```latex
This chapter takes a more direct route to target-domain adaptation. Rather than relying only on transfer from synthetically labelled audio, the estimator is adapted using real performance recordings and a differentiable rendering interface. This reduces dependence on target velocity annotation, but does not remove the need to model or approximate the renderer.
```

### T06-L

```latex
This chapter instead adapts a piano-pretrained estimator using real performance audio, without requiring target-domain velocity labels. A differentiable renderer or proxy supplies the training signal. Its match to the target recordings remains a limitation.
```

### T06-M

```latex
We instead adapt the estimator on real performance recordings through a differentiable rendering interface. This provides indirect supervision when target-domain velocity labels are unavailable, while still requiring a suitable renderer or proxy.
```

### T06-N

```latex
This chapter takes a different and simpler route. Instead of training on synthesised audio with synthetic labels, the front-end estimator is trained directly against real performance audio. The synthesiser is involved at training time only as a differentiable interface that connects predicted velocities to a measurable property of the real recording. This avoids the synthesis-to-performance domain gap that dominates synthetic-data transfer pipelines, at the cost of needing a differentiable supervision interface that is reliable across the instruments of interest.
```

## T07

Source: `Chapter_6/chap6.tex`; anchor: `The advantage of this interface is that it exposes`

Operation: Replace discussion paragraph at end Diff-Synth subsection.

Need: Comment on DDSP-Piano/Guitar faithfulness.

Evidence: Author response 6.3 explicitly: degradation consistent with mismatch; reconstruction fidelity and velocity-gradient accuracy not separately measured. Do not erase tested degradation or invent causal proof.

Context before:
```latex
of~\cite{jonason2024guitar} as the piano and guitar waveform back-ends, respectively.

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
```

Context after:
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
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averag
```

### T07-K

```latex
The advantage of this interface is that it exposes the front end to rich waveform gradients. The risk, already noted in Section~\ref{sec:bp:related}, is that any timbral or recording mismatch between $\tilde{a}$ and $a$ also enters the gradient. When the synthesiser is not a faithful match for the target recordings, the gradient can become dominated by nuisance compensation rather than by velocity correction.
```

### T07-L

```latex
The waveform back-ends are used as differentiable approximations rather than exact reproductions of the recorded instruments. Their usefulness depends both on acoustic fidelity and on whether changing velocity produces the appropriate change in sound. The Diff-Synth results are consistent with a mismatch in this interface, but do not isolate its cause: reconstruction fidelity and velocity-gradient accuracy were not measured separately on the target recordings.
```

### T07-M

```latex
The waveform interface supplies gradients through a differentiable approximation of the instrument. Its timbre and velocity response may differ from the target recordings. The observed degradation is consistent with this mismatch, but reconstruction fidelity and velocity-gradient accuracy were not measured separately.
```

### T07-N

```latex
DDSP-Piano and DDSP-Guitar-Synth approximate the target instruments. Their velocity-to-sound response is relevant to adaptation as well as their acoustic fidelity. Diff-Synth degraded performance in these experiments; the comparison does not identify which part of that mismatch caused the degradation.
```

## T08

Source: `Chapter_1/Intro.tex`; anchor: `Referring to Figure`

Operation: Replace only opening paragraph of Thesis Organisation; retain chapter-by-chapter roadmap.

Need: Distinguish co-authored paper methods from thesis synthesis.

Evidence: Authorship Declaration maps Ch3 CMMR, Ch4 SMC, Ch5 ICASSP, Ch6 ISMIR. Existing Intro and Conclusion synthesize targets/data/supervision/limits. Final ICASSP source version unresolved; no exhaustive novelty claim.

Context before:
```latex
sparsity-aware loss \cite{he2025filling}.

    \item \textbf{A modular score-informed correction strategy (Addressing S2).} It introduces a lightweight Transformer correction module that refines AMT-estimated velocity using an aligned score. The design prioritises modularity and compatibility with existing AMT systems over a fully bespoke end-to-end architecture.

    \item \textbf{An audio-only framework for score-dynamics recovery (Addressing S3).} It proposes a compact multi-task multi-scale network that jointly estimates dynamic levels, change points, beats, and downbeats. It innovatively combines a perceptually motivated Bark-scale specific loudness front-end with task-aware decoding through MMoE \cite{he2026dynest,ma2018mmoe}.
  
    \item \textbf{An exploratory cross-instrument methodology.} It confronts the piano bias by investigating cross-instrument MIDI velocity estimation when true labels are scarce, employing a differentiable proxy for black-box synthesisers as part of the supervision signal.
\end{itemize}


\section{Thesis Organisation}
\label{sec:intro:organisation}
```

Context after:
```latex
\textbf{Chapter~2} establishes the shared conceptual system, defining dynamics across audio, MIDI, and score, while reviewing baseline AMT models, datasets, and evaluation strategies.

\textbf{Chapter~3} addresses Scenario~S1. Supported by listening tests, it demonstrates that recovering a decoupled expressive layer on fixed symbolic notes is enough to transform a mechanical MIDI sequence into an expressive performance.

\textbf{Chapter~4} addresses Scenario~S2. It details the Transformer correction module, demonstrating superior generalisation under dataset shift and robustness to audio-to-score misalignment.

\textbf{Chapter~5} addresses Scenario~S3. It presents the multi-task framework to extract human-readable score dynamics alongside their metrical anchors directly from audio.

\textbf{Chapter~6} acts as an exploratory extension. It probes the frontier where direct velocity labels disappear, testing a route for cross-instrument MIDI velocity estimation via proxy supervision.

\textbf{Chapter~7} synthesises the findings across the four studies, states the limitations clearly, a
```

### T08-K

```latex
The technical chapters are based on four co-authored studies: symbolic velocity completion (CMMR 2025, Chapter 3), score-informed correction (SMC 2026, Chapter 4), joint dynamics and metrical estimation (ICASSP 2026, Chapter 5), and cross-instrument proxy supervision (ISMIR 2026, Chapter 6). Their authorship and publication details are listed in the Authorship Declaration. The thesis brings these studies together through a common label-recovery formulation and scenario map, provides shared background, and synthesises their assumptions and limitations in Chapter 7.
```

### T08-L

```latex
Chapters 3--6 are based on the four co-authored studies listed in the Authorship Declaration. The thesis brings them together through a common label-recovery question, a shared account of dynamics representations, and the cross-chapter discussion of assumptions and limitations in Chapter~\ref{ch:conclusion}.
```

### T08-M

```latex
The four technical studies are presented in Chapters 3--6, with their co-authorship and publication details in the Authorship Declaration. The thesis synthesis is developed in Chapters 1, 2, and 7: it relates their data conditions, dynamics targets, and evaluation choices.
```

### T08-N

```latex
Referring to Figure~\ref{fig:intro_overview}, the core methodological chapters (Chapters 3--5) preserve the technical contributions of their respective peer-reviewed publications, adapted to form a unified narrative.
```

## T09

Source: `Chapter_7/Conclusion.tex`; anchor: `Second, the strongest direct supervision`

Operation: Replace this piano-centric limitation paragraph; Ch6 detailed sustained-control limitations remain.

Need: Clarify which conclusions transfer to guitar, voice, bowed strings, winds.

Evidence: Piano and guitar evaluated; guitar evidence rendered loudness, not captured velocity labels. Ch6 already states attack-driven PHE/OSF and sustain limits. Voice/bowed/wind not evaluated.

Context before:
```latex
ult is not that weaker supervision makes the task impossible. Rather, weaker supervision changes what can be claimed. Each claim is valid inside its representational boundary. The thesis contribution is to make those boundaries explicit instead of hiding them behind a single generic term such as dynamics.

\section{Limitations and Scope}
\label{sec:conclusion:limitations}

The thesis has several boundaries. These boundaries are not artefacts of unfinished implementation; they follow from the problem definition and from the representational choices made throughout the dissertation.

First, the thesis focuses on dynamics rather than on the full space of musical expression. Timing, articulation, pedalling, timbre, and phrasing interact with dynamics in real performance. The systems developed here isolate dynamics because it is perceptually salient, directly useful for data curation, and recoverable under structural preservation. This isolation is methodologically useful, but it also means that the recovered layer is one dimension of expression rather than a complete performance model.
```

Context after:
```latex
Third, score dynamics is inherently contextual. A dynamic marking is not a fixed loudness threshold. It depends on edition, local musical function, register, texture, and phrase context. Chapter~\ref{ch:audiodyn} treats score dynamics as a beat-synchronous symbolic target because that is the most useful interface for notation and analysis. The resulting labels should therefore be read as score-facing annotations under a specific annotation convention, not as universal statements about physical loudness.

Fourth, several chapters assume that structural coordinates are available or recoverable. Score-informed velocity correction assumes aligned score events. The beyond-piano proxy framework assumes aligned note events. Audio-to-score dynamics estimates beats and downbeats, but still relies on the idea that beat-synchronous output is the right symbolic interface. These assumptions are not weaknesses of the argument. They are the conditions under which label recovery, rather than unconstrained generation, becomes meaningful.

Finally, the thesis uses multiple forms of evidence rather t
```

### T09-K

```latex
The empirical findings cover the tested piano datasets and guitar adaptation. The guitar results concern renderer-conditioned dynamics, rather than measured physical velocity. Extending the approach to voice, bowed strings, or wind instruments would require descriptors for sustained dynamics and a separate evaluation.
```

### T09-L

```latex
The strongest direct supervision remains piano-based. Chapter~\ref{ch:beyondpiano} extends the approach to guitar using renderer-conditioned velocity and loudness-based evaluation. Voice, bowed strings, and wind instruments were not evaluated; their sustained and continuous controls would require targets and acoustic descriptors beyond the attack-focused PHE/OSF pair.
```

### T09-M

```latex
Second, the strongest direct supervision in the thesis remains piano-centric. This reflects the state of available velocity-labelled datasets rather than a belief that piano dynamics is the universal template for all instruments. Chapter~\ref{ch:beyondpiano} addresses this bias by moving into a label-scarce guitar setting, but the broader point remains: once the target instrument lacks direct performance-control labels, the interpretation of recovered velocity must be stated operationally.
```

### T09-N

```latex
The piano chapters support conclusions about the tested piano datasets and targets. Chapter 6 extends the supervision strategy to guitar, where the evidence concerns renderer-conditioned velocities and loudness agreement rather than recovery of captured physical velocity labels. Voice, bowed strings, and wind instruments were not evaluated. Their sustained dynamics and continuous controls would require suitable target coordinates and descriptors beyond the attack-focused PHE/OSF pair used here.
```

## T10

Source: `Chapter_3/chap3.tex`; anchor: `Although a substantial gap to human performance remains`

Operation: Replace listening Results paragraph only; MOS/CI table and participant/procedure descriptions remain.

Need: Listening test with 11 experts supports objective results, not definitive perceptual validation.

Evidence: 11 expert listeners, eight selected SMD excerpts, one PianoTeq configuration. Similarity to human-performed-MIDI rendering reference. Means Flat1.50 ConvAE2.08 U-Net3.01, not significance test. Composer groups descriptive. Citation kuo2021velocity retained if stating previous finding.

Context before:
```latex
osers include \{Bart\'ok, Ravel\}. Best score is highlighted in bold.}
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
```

Context after:
```latex
\section{Discussion}
\label{sec:velcomp:discussion}

This chapter has verified that note-level dynamics can be recovered usefully even when the symbolic notes and timing are held fixed. It turns expressive enhancement into a controllable post-processing stage rather than a full performance-rendering problem, which is exactly the setting encountered in many MIDI-production and corpus-curation workflows.

The image-colourisation view is effective because it matches the structure of the data. Polyphonic note patterns create meaningful vertical and local spatial regularities that are awkward to express in purely sequential terms. The U-Net captures this local structure well, and the sparsity-aware loss prevents the model from spending most of its capacity on silent regions. The results suggest that this representation choice is a major reason the method surpasses the sequence-based baselines considered here.

The evaluation design is therefore deliberately broader than a single regression score. Objective error metrics quantify note-wise accuracy, \(SD_{\mathrm{velo}}\) checks whether
```

### T10-K

```latex
The mean ratings favour U-Net over Flat and ConvAE in similarity to the human-performed reference. This supports the objective results within the listening-test setting: 11 expert listeners, eight selected excerpts and one PianoTeq configuration. The composer groups describe the selected repertoire rather than a controlled style comparison. Flat received the lowest ratings, consistent with earlier findings \cite{kuo2021velocity}.
```

### T10-L

```latex
U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts, while Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. The listening study provides supplementary perceptual evidence from 11 expert listeners, eight selected SMD excerpts, and one PianoTeq rendering configuration. The composer-group scores are descriptive rather than a controlled comparison of stylistic effects.
```

### T10-M

```latex
Although a substantial gap to human performance remains, the proposed U-Net clearly outperforms the other systems.
The Flat model performs worst, consistent with earlier findings that default velocity is musically inadequate \cite{kuo2021velocity}.
The seen, less-seen, and unseen repertoire groups are best interpreted as descriptive groups rather than as a strict complexity-controlled comparison.
Even so, the relatively narrow 95\% confidence intervals across groups suggest that participants rated the stimuli with reasonable consistency.
```

### T10-N

```latex
U-Net received higher mean similarity ratings than Flat and ConvAE on the selected excerpts. Flat received the lowest ratings, consistent with earlier findings on default velocity \cite{kuo2021velocity}. With 11 expert listeners, eight excerpts and one PianoTeq configuration, this study provides supporting perceptual evidence. The composer groups are descriptive and do not isolate stylistic effects.
```

## N01

Source: `Chapter_6/chap6.tex`; anchor: `To test dynamics sensitivity,`

Operation: Replace paragraph interpreting GT-vs-Flat separation; keep table/numbers and next paragraph.

Need: Local source-integrity repair found during independent audit, beyond v4. Do the table values establish insensitive cosine?

Evidence: Table reports r/CS/MAE on different numerical scales. Pearson GT-Flat: .118/.263; cosine: .052/.047. All GT cosine > Flat. No independent calibrated sensitivity comparison. Numeric gaps alone are not commensurate effect sizes.

Context before:
```latex
\\
\cmidrule(lr){2-4} \cmidrule(l){5-7}
& $r$ & $cs$ & MAE & $r$ & $cs$ & MAE \\
\midrule
\textbf{GT velocity}            & 0.870 & 0.939 & 0.702 & 0.883 & 0.975 & 3.706 \\
\,-\, uses YDP Piano            & 0.836 & 0.926 & 0.510 & 0.872 & 0.973 & 1.983 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & \underline{0.034} & \textbf{0.013} & 0.193
                                & \underline{0.011} & \textbf{0.002} & 1.723 \\
\midrule
\textbf{Flat velocity = 64}     & 0.752 & 0.887 & 0.786 & 0.620 & 0.928 & 4.065 \\
\,-\, uses YDP Piano            & 0.733 & 0.883 & 0.637 & 0.617 & 0.930 & 2.750 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & \underline{0.019} & \textbf{0.004} & 0.149
                                & \underline{0.003} & \textbf{0.002} & 1.314 \\
\midrule
\textbf{$\Delta$ (GT $-$ Flat) $\uparrow$}
                                & \textbf{+0.118} & \underline{+0.052} & -0.083
                                & \textbf{+0.263} & \underline{+0.047} & -0.359 \\
\bottomrule
\end{tabular}
\end{table}
```

Context after:
```latex
To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.

Pearson $r$ on BSSL/BSTL therefore provides the right trade-off for this chapter. Cosine similarity and MAE fail on sensitivity and robustness, respectively, and are kept only as diagnostic alternatives. This is also the reason the main results table reports $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ as the headline metrics for label-free guitar evaluation.

\subsection{When Diff-Synth Should Still Be Preferred}
\label{ssec:bp:when_diffsynth}

Diff-SFProxy is not a universal replacement for Diff-Synth. Three conditions favour the waveform interface. First, the matched di
```

### N01-K

```latex
Both Pearson $r$ and cosine similarity assign higher scores to GT than to flat-velocity resynthesis. On the reported scales, the GT--flat differences are $0.118$ and $0.263$ for Pearson $r$, compared with $0.052$ and $0.047$ for cosine similarity on BSSL and BSTL, respectively. These values describe this diagnostic; the different metric scales do not establish that cosine similarity is generally insensitive to dynamics.
```

### N01-L

```latex
The diagnostic separates GT from flat velocity with both similarity metrics. Pearson $r$ gives a larger numerical GT--flat gap on BSSL and BSTL in this table, although the gaps are measured on different scales. We use this as a dataset-specific diagnostic rather than a general sensitivity ranking.
```

### N01-M

```latex
To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.
```

### N01-N

```latex
To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.
```

## N02

Source: `Chapter_6/chap6.tex`; anchor: `To evaluate renderer robustness,`

Operation: Replace one renderer-robustness paragraph; preserve table and no metric re-computation.

Need: Does swapping a SoundFont isolate absolute gain?

Evidence: SoundFont swap changes renderer, not a controlled gain-only factor. MAE drift .193 BSSL/1.723 BSTL vs r .034/.011. Those scales differ; numerical gaps cannot prove causal gain sensitivity or universal robustness.

Context before:
```latex
2} & 1.723 \\
\midrule
\textbf{Flat velocity = 64}     & 0.752 & 0.887 & 0.786 & 0.620 & 0.928 & 4.065 \\
\,-\, uses YDP Piano            & 0.733 & 0.883 & 0.637 & 0.617 & 0.930 & 2.750 \\
$\Delta\lvert$Sal.\,$-$\,YDP$\rvert$ $\downarrow$
                                & \underline{0.019} & \textbf{0.004} & 0.149
                                & \underline{0.003} & \textbf{0.002} & 1.314 \\
\midrule
\textbf{$\Delta$ (GT $-$ Flat) $\uparrow$}
                                & \textbf{+0.118} & \underline{+0.052} & -0.083
                                & \textbf{+0.263} & \underline{+0.047} & -0.359 \\
\bottomrule
\end{tabular}
\end{table}

To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.
```

Context after:
```latex
Pearson $r$ on BSSL/BSTL therefore provides the right trade-off for this chapter. Cosine similarity and MAE fail on sensitivity and robustness, respectively, and are kept only as diagnostic alternatives. This is also the reason the main results table reports $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ as the headline metrics for label-free guitar evaluation.

\subsection{When Diff-Synth Should Still Be Preferred}
\label{ssec:bp:when_diffsynth}

Diff-SFProxy is not a universal replacement for Diff-Synth. Three conditions favour the waveform interface. First, the matched differentiable synthesiser must exist for the target instrument and expose a faithful per-note velocity control. Second, its waveform statistics must be acoustically close to the target recordings. Third, the supervision must be allowed to reach beyond velocity and update auxiliary controls such as pedal or articulation. When all three conditions hold, waveform supervision can in principle deliver richer gradients than parameter supervision, and the present chapter does not contest this in general terms.

The claim o
```

### N02-K

```latex
To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.
```

### N02-L

```latex
To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.
```

### N02-M

```latex
Changing from Salamander to YDP while retaining the GT notes and velocities changes MAE by $0.193$ on BSSL and $1.723$ on BSTL; the corresponding changes in Pearson $r$ are $0.034$ and $0.011$. This tests the effect of the renderer change as a whole, rather than absolute gain alone. Pearson $r$ is used here to compare loudness-contour agreement while reducing dependence on absolute level.
```

### N02-N

```latex
The SoundFont swap leaves the note velocities fixed but changes their rendered sound. Pearson $r$ changes by $0.034$ on BSSL and $0.011$ on BSTL, while MAE changes by $0.193$ and $1.723$. This supports using $r$ for the present renderer comparison, without identifying gain as the sole source of the MAE change.
```

## T11

Source: `Chapter_6/chap6.tex`; anchor: `The Huber form tolerates outliers`

Operation: Replace only the last rationale sentence after beta=1.0 and 1:1 weighting; preserve equations/settings.

Need: Justify Huber versus MAE without overstating what the actual author response established.

Evidence: Actual response: We chose Huber because it provides smoother gradients for small PHE/OSF errors while retaining an L1-like penalty for large errors. We use beta=1, but we have not established that it performs better than MAE through a dedicated comparison. This establishes no superiority claim, but does not by itself prove no comparison was ever conducted.

Context before:
```latex
iff-SFProxy path, the back-end is a frozen differentiable proxy $P$ of an instrument-specific SoundFont. Let $F$ denote the note-wise loudness-related acoustic parameter extractor that reads audio conditioned on the note events $E$. Both $F$ and $P$ output the same kind of low-dimensional, note-wise dynamics descriptor; their precise construction is deferred to Section~\ref{sec:bp:diffsfproxy}. Given predicted velocities $\hat{V}$, the two feature streams are
\begin{equation}
\label{eq:bp_sfproxy_features}
Z = F(a, E), \qquad \tilde{Z} = P(E, \hat{V}).
\end{equation}
The adaptation loss is a Huber (Smooth-$L_1$) distance between the two extracted parameter groups,
\begin{equation}
\label{eq:bp_param_loss}
\mathcal{L}_{\mathrm{params}} = \mathrm{Huber}_\beta\!\left(\tilde{Z} - Z\right),
\end{equation}
with the default $\beta = 1.0$. Each $Z_n = (\mathrm{PHE}_n, \mathrm{OSF}_n) \in \mathbb{R}^2$ contains the two note-wise parameters defined in Section~\ref{ssec:bp:acoustic_params}, and the loss averages over both components and all valid notes, weighting PHE and OSF equally ($1{:}1$).
```

Context after:
```latex
The asymmetry between Eq.~\eqref{eq:bp_audio_loss} and Eq.~\eqref{eq:bp_param_loss} is the central design point of this chapter. The Diff-Synth path optimises in waveform/spectral space, where velocity is one of many factors influencing the signal. The Diff-SFProxy path optimises in a low-dimensional note-wise dynamics space, where velocity is the dominant factor by construction. The remainder of the chapter tests whether this difference matters in practice.

\subsection{Shared Regularisers and Total Objective}
\label{ssec:bp:regularisers}

Both adaptation paths share two auxiliary regularisers on the predicted onset-velocity distribution $\hat{\mathbf{v}} \in [0,1]^{N}$, where $N$ is the number of valid onsets in a batch. The first is an anti-collapse prior,
\begin{equation}
\label{eq:bp_anti_loss}
\mathcal{L}_{\mathrm{anti}}(\hat{\mathbf{v}}) = (\bar{v} - \mu)^2
+ \max\!\left(0,\ \sigma_{\min}^2 - \mathrm{Var}(\hat{\mathbf{v}})\right),
\end{equation}
where $\bar{v}$ and $\mathrm{Var}(\hat{\mathbf{v}})$ are the empirical mean and variance over onset positions, $\mu = 0.5$ is a des
```

### T11-K

```latex
Huber combines a quadratic region for small residuals with an L1-like penalty for large errors. This motivates the choice, rather than establishing that it performs better than MAE.
```

### T11-L

```latex
We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE through a dedicated comparison.
```

### T11-M

```latex
The Huber form tolerates outliers from onset contamination such as overlapping notes, while the parameter-space objective concentrates gradients on note intensity and attack behaviour rather than on waveform details that are weakly related to velocity.
```

### T11-N

```latex
Huber is quadratic for small residuals and L1-like for larger residuals, giving smoother gradients near zero while limiting the influence of large errors. We did not conduct a dedicated comparison with MAE.
```

## N03

Source: `Chapter_6/chap6.tex`; anchor: `Pearson $r$ on BSSL/BSTL therefore`

Operation: Replace the concluding metric-choice paragraph after N01/N02; do not leave the original fail/right-trade-off claim behind.

Need: Keep a positive reason for the chosen headline metric without claiming a validated universal metric ranking.

Evidence: Same table as N01/N02. Pearson r distinguishes GT from Flat under tested SoundFonts; calibration and metric values are not commensurate effect sizes. Choice of r remains justified as contour-agreement measure, not physical velocity truth.

Context before:
```latex
-0.083
                                & \textbf{+0.263} & \underline{+0.047} & -0.359 \\
\bottomrule
\end{tabular}
\end{table}

To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.

To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.
```

Context after:
```latex
\subsection{When Diff-Synth Should Still Be Preferred}
\label{ssec:bp:when_diffsynth}

Diff-SFProxy is not a universal replacement for Diff-Synth. Three conditions favour the waveform interface. First, the matched differentiable synthesiser must exist for the target instrument and expose a faithful per-note velocity control. Second, its waveform statistics must be acoustically close to the target recordings. Third, the supervision must be allowed to reach beyond velocity and update auxiliary controls such as pedal or articulation. When all three conditions hold, waveform supervision can in principle deliver richer gradients than parameter supervision, and the present chapter does not contest this in general terms.

The claim of this chapter is narrower. In many cross-instrument settings, none of these three conditions holds robustly. A matched Diff-Synth may not exist for the target instrument, may be expensive to retrain at the desired crop length, or may differ from the real recordings in timbre and recording chain. A practical SoundFont, by contrast, is widely available, plug-an
```

### N03-K

```latex
Pearson $r$ on BSSL/BSTL therefore provides the right trade-off for this chapter. Cosine similarity and MAE fail on sensitivity and robustness, respectively, and are kept only as diagnostic alternatives. This is also the reason the main results table reports $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ as the headline metrics for label-free guitar evaluation.
```

### N03-L

```latex
We therefore use Pearson $r$ on BSSL/BSTL as the headline measure of rendered loudness-contour agreement for label-free guitar evaluation. In this piano diagnostic, it distinguishes GT from flat velocity under both tested SoundFonts. Cosine similarity and MAE are retained as complementary diagnostics rather than treated as generally invalid measures.
```

### N03-M

```latex
The diagnostic supports our use of Pearson $r$ on BSSL/BSTL for the present loudness-contour comparison. It distinguishes GT from flat velocity under both tested SoundFonts, while cosine similarity and MAE describe other aspects of agreement. The main guitar results therefore report $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$.
```

### N03-N

```latex
Pearson $r$ on BSSL/BSTL therefore provides the right trade-off for this chapter. Cosine similarity and MAE fail on sensitivity and robustness, respectively, and are kept only as diagnostic alternatives. This is also the reason the main results table reports $r_{\mathrm{BSSL}}$ and $r_{\mathrm{BSTL}}$ as the headline metrics for label-free guitar evaluation.
```

## N04

Source: `Chapter_2/Background.tex`; anchor: `so the gradient signal is dominated`

Operation: Replace only this clause in the existing long paragraph; keep representations, comparison-space distinction and citations.

Need: Avoid a background universal causal claim inconsistent with later conditional DDSP mismatch interpretation.

Evidence: Ch6 source says gradient can become dominated when renderer mismatches; actual author response says mismatch mechanism not separately isolated. v4 fixes Ch6 but leaves this unqualified Chapter2 clause.

Context before:
```latex
ds on how much of the timbral, recording-chain, and room behaviour the renderer captures. The choice of differentiable renderer therefore conditions what the downstream model can plausibly learn.

\subsection{Analysis-by-synthesis and label-scarce velocity recovery}
\label{sec:bg:synth:analysis}

The combination of differentiable rendering and prediction networks defines an \emph{analysis-by-synthesis} setting. A network proposes control values for an observed recording; the renderer turns those values back into audio (or into an intermediate audio-derived quantity); a loss compares the rendered output with the observed signal. This paradigm becomes the central tool when true note-level velocity labels are unavailable, because the renderer takes the place of a label by linking predicted control to a measurable property of the recording.

Two design axes matter for this thesis. The first is the comparison space. \emph{Signal-domain} losses (waveform or spectral) can be applied directly to the rendered output, but they conflate velocity with timbre, recording chain, and room response,
```

Context after:
```latex
\emph{Parameter-domain} or perceptual proxy losses instead extract a small set of velocity-relevant acoustic descriptors (e.g.\ note-wise loudness, attack envelope) from both the rendered and the observed audio and compare them in that lower-dimensional space. The latter is closer in spirit to the parameter-extraction proxies used in spectral-modelling research and trades waveform fidelity for stronger alignment with the velocity target. The second axis is the renderer's domain coverage. A differentiable renderer adapted to piano need not transfer to guitar or violin without further work~\cite{renault2023ddsp_piano,wiggins2023ddsp_guitar_model}, which is one of the practical constraints of cross-instrument analysis-by-synthesis.

For expressive AMT, this strategy is attractive but delicate. It makes label-scarce learning possible, yet it also ties the learning signal to the adequacy of the renderer: a proxy objective can reward compatibility with the synthesiser more than compatibility with real instrumental control, and reconstruction error is therefore not the same thing as accura
```

### N04-K

```latex
so the gradient signal is dominated by factors unrelated to velocity.
```

### N04-L

```latex
so the gradient signal is dominated by factors unrelated to velocity.
```

### N04-M

```latex
so the gradient signal can be influenced by factors unrelated to velocity.
```

### N04-N

```latex
so renderer mismatch can divert the gradient from velocity-relevant differences.
```
