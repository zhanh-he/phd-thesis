# 7分钟开场白｜English

> 13 paragraphs, aligned with the Chinese version. Read the body in order; do not read the paragraph numbers. Spoken text: 899 words, approximately 6.66–7.49 minutes at 120–135 words per minute. Timing is estimated, not measured.

## 01

Thank you for the opportunity to present my thesis. Two performances can contain the same notes and still sound very different. Dynamics is part of that difference. My research asks how we can add a useful, editable dynamics layer to existing music data when that information is missing or unreliable. I study this question within expressive automatic music transcription.

## 02

Dynamics helps shape a phrase, bring out a melody, and balance simultaneous notes. But we need to distinguish the sound we hear from the labels we predict. Audio loudness, MIDI velocity, and score markings are related representations. MIDI velocity is a note-level control whose effect depends on the instrument and renderer. A score marking such as piano or forte is contextual. There is no universal conversion between these representations.

## 03

This distinction also explains the practical motivation. A musician may already have a reliable note sequence but lack useful velocity values. An analyst may have a recording and want dynamics placed on a score. These are different needs. By defining the missing layer explicitly, we can preserve trusted musical information and make the new output easier to inspect and edit. Preserving the notes does not imply that only one expressive interpretation is valid.

## 04

The thesis develops four studies around the information available. The first has symbolic notes alone. The second adds audio and an aligned score. The third starts from audio and predicts score dynamics. The fourth retains aligned notes but lacks direct velocity labels for the target instrument. Each study addresses a different condition of the same research question.

## 05

The first study completes MIDI velocity from symbolic context. It uses a two-dimensional piano roll and a U-Net to model pitch and time relationships while keeping the supplied notes unchanged. The reported piano experiments show lower velocity error than the listed comparison systems. The contribution is a method for plausible conditional completion. It does not identify a unique original performance when no performance audio is available.

## 06

The evaluation combines objective error measures with a small listening study. In the listening comparison, the notes, timing, and rendering setup are held constant, so listeners hear the consequences of changing velocity. The tested comparisons are the proposed model, a convolutional autoencoder, and flat velocity. These results support the audible usefulness of the predicted layer in the selected piano examples. The listening study complements the objective results and has a limited sample of listeners and excerpts.

## 07

The second study uses performance audio together with aligned score events. An acoustic estimator provides an initial velocity estimate. A Transformer then uses score information to correct it at the supplied note onsets. The reported comparisons show improvements across the tested piano estimators and datasets. This contributes a modular way to use score structure for velocity refinement. Its measured benefit concerns velocity at known notes; improved note detection is a separate question.

## 08

The next study changes the output representation. Instead of assigning a control value to each known note, it asks for a score-facing description of dynamics. A dynamic level describes a local regime. A change point describes where that regime changes. Beats and downbeats provide musical positions for those labels. Treating these as related but distinct targets lets the model share context while keeping their outputs interpretable.

## 09

The third study predicts dynamic levels, change points, beats, and downbeats from audio. It combines Bark-scale loudness features with a multiscale encoder and task-specific decoding. The design brings broader dynamic context together with precise event timing. Its contribution is a joint framework for a different symbolic target: score dynamics. The reported dynamics and change-point evaluation uses an annotated beat grid, so those scores describe that condition rather than a complete transcription pipeline.

## 10

The fourth study asks what we can do without direct target-instrument velocity labels. A piano-pretrained estimator is adapted through a differentiable SoundFont proxy. The proxy links predicted controls to note-wise acoustic descriptors, allowing real audio to provide an indirect learning signal. On the tested guitar recordings, the reported resynthesis-loudness correlations favour this interface over the compared alternatives. The output is a renderer-conditioned control value. This is useful evidence about matching dynamic behaviour, with a different interpretation from directly measured velocity accuracy.

## 11

The proxy first learns how the chosen renderer responds to note controls. During adaptation, that proxy is fixed and supplies gradients to the estimator. Comparing selected descriptors focuses the learning signal on dynamics-related behaviour. It does not remove every difference between a renderer and a recording. The piano results are also informative: the directly supervised checkpoint remains the stronger reference. The proxy approach addresses missing target labels, rather than replacing reliable direct supervision wherever it exists.

## 12

Across the studies, the main finding is that the target, musical coordinate, and learning signal need to fit together. Symbolic context supports plausible completion. Aligned notes support audio-based correction. Score dynamics needs a metrical coordinate. Missing direct labels call for an explicit indirect objective. The strongest direct evidence is piano-based; guitar provides an exploratory extension. These distinctions make the methods useful while keeping each claim connected to the evidence that supports it.

## 13

My overall contribution is a set of methods for these information conditions, together with a coherent account of how to interpret and evaluate their outputs. The aim is to make existing music data more expressive and editable through a dynamics layer that we can inspect. Thank you for listening. I welcome your questions and the opportunity to discuss the work.
