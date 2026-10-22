# 7分钟开场白｜English

> Spoken version based on the abstract; 13 paragraphs aligned with the Chinese. Read from 01 to 13; skip the numbers and this note. 863 spoken words: approximately 6.39–7.19 minutes at 120–135 words per minute. Timing is estimated, not measured.

## 01

Hello everyone, and thank you for being here. My thesis is about musical dynamics: how strong or soft the music is, and how that changes through a performance. Automatic music transcription has made good progress on pitch and timing. But getting the notes right still leaves out part of the performance. The part I focus on is dynamics.

## 02

The problem I want to solve is quite specific. We often already have some useful material: notes, MIDI, or a performance recording. What is missing, or unreliable, is the dynamics information. So I ask whether we can use what we already have to fill in that layer. Where the notes and timing are trusted, I keep them and focus on dynamics. That is the starting point of the thesis.

## 03

There are two targets here. One is MIDI velocity, the control value assigned to each note. The other is score dynamics, such as piano, mezzo forte, and forte. Both relate to loudness, but they are not the same thing. The same velocity can sound different with another instrument or renderer. So before building a model, I need to be clear about which target I am trying to predict.

## 04

The first study starts with symbolic notes alone. The pitches and timing are there, but velocity is missing or set to the same value for every note. I put the notes on a piano-roll grid and use a U-Net with window attention to fill in velocity. The model and loss take account of how sparse the notes are on that grid, while keeping the supplied notes and timing unchanged.

## 05

On the piano datasets, this gives lower velocity error than the comparison systems. I also ran a small listening study. The notes, timing, and rendering setup stay the same; only velocity changes. The results support an audible benefit from that layer. Of course, without audio, the same notes can have several reasonable interpretations. This is about completing a plausible performance, rather than uniquely recovering the original one.

## 06

The second study adds audio and an aligned score. Now I want to use the note information in the score to help correct the audio-based velocity estimate. Instead of designing a whole transcription system from scratch, I add a Transformer correction module to an existing velocity estimator. It reads information at the supplied note onsets and corrects the initial velocity values there.

## 07

I test this with several piano estimators, including transfer from MAESTRO to SMD. In these comparisons, adding score-informed correction improves velocity estimation. I also test global timing shifts between the audio and score. The point is to see how existing note structure can help refinement, and how the module can work with different front ends. This part takes the notes as given and evaluates velocity at those notes.

## 08

The third study changes the question. Suppose we only have a recording, and we want dynamics that can be placed on a score. Here, I predict dynamic levels, change points, beats, and downbeats, rather than velocity for each note. We need to know the current dynamic level, where it changes, and where those labels belong in musical time.

## 09

These tasks need different views of time. Dynamic levels benefit from broader context, while beats need precise event timing. I combine Bark-scale loudness features, a multiscale encoder, and multitask decoding so that the tasks can use information at different scales. The comparisons support a balance between these needs: longer context does not improve everything. The reported dynamics and change-point scores use reference beats, which is important when interpreting the results.

## 10

The final study moves beyond piano. Piano has useful note-level velocity labels, but real guitar recordings generally do not offer the same direct labels. Even with audio and aligned notes, we are missing the target needed for direct supervision. I therefore start from a piano-pretrained estimator and investigate adaptation using an indirect learning signal from real audio.

## 11

I train a differentiable SoundFont proxy. It first learns how a chosen renderer maps notes and velocity to loudness-related descriptors. I then keep that proxy fixed, extract target descriptors from the real recording, and update the velocity estimator. This gives us a connection between predicted controls and the acoustic target. We can use that connection to work out how the estimator should change, without direct velocity labels for those recordings.

## 12

On the tested guitar recordings, this proxy approach gives better loudness correlation than the compared alternatives. After resynthesis, the loudness contour is closer to the recording. The resulting velocity is a control for the chosen renderer, not a measurement of physical plucking force. On piano, the directly supervised model remains stronger. So this study provides a route for the situation where direct target labels are missing.

## 13

Looking back, the four studies answer the same question with different information available: notes alone, audio with a score, audio alone, or audio and notes without direct velocity labels. My contribution is to develop methods for these settings and make clear what we recover, what evidence we use, and how we evaluate it. The goal is to make dynamics in existing music data something we can complete, inspect, and edit. Thank you. I look forward to discussing the work with you.
