<!-- 本文完整保留 PDF 的全部评审文字；原文件没有回复批注。只调整 Markdown 排版、合并印刷换行和跨页段落，并把跨页评分表合为一张表（重复表头只保留一次）。无回复处统一标为 zhanhong not response yet。 -->

# Examiner Report

Thesis Title:

*Recovering Musical Dynamics for Expressive Automatic Music Transcription*

Candidate: Zhanhong HE

This thesis is presented for the degree of Doctor of Philosophy at the University of Western Australia.

Based on the thesis and the assessment guidelines, my views and recommended decision are detailed as follows:

This is a strong PhD thesis. It makes a clear and original contribution to expressive automatic music transcription by treating musical dynamics as a recoverable expressive layer, rather than limiting transcription to pitch and timing. The work is coherent, technically competent, experimentally supported, and generally written to a publishable standard. It does not, in my view, require substantive amendments, resubmission, additional data collection, or major rewriting.

**Zhanhong’s response:**

> zhanhong not response yet

The assessment guidelines require judgment against six merit criteria: originality, understanding of the literature, comprehensiveness, appropriateness of techniques, exposition of results, and English/presentation quality. They also deﬁne Pass with minor revisions as appropriate, where the thesis largely satisﬁes the requirements but needs minor changes that do not affect the conclusions.

**Zhanhong’s response:**

> zhanhong not response yet

## Summary evaluation against the six criteria

| Criterion | Evaluation | Suggested score |
| --- | --- | --- |
| Original contribution | Strong and original contribution to expressive AMT, especially dynamics recovery | 2 |
| Literature familiarity | Broad and well-structured review of AMT, MIR, loudness, MIDI velocity, score dynamics, and differentiable synthesis | 2 |
| Comprehensive study | Covers symbolic-only, audio-plus-score, audio-only, and exploratory beyond-piano settings | 2 |
| Techniques | Appropriate and well-applied: U-Net, attention, Transformer correction, multi-task learning, Bark-scale loudness, differentiable proxy supervision | 2 |
| Results and exposition | Results are clearly organized with objective metrics, ablations, cross-dataset tests, and listening evaluation | 2–3 |
| English and presentation | Generally publishable, with some need for proofreading and tightening | 2 |

**Zhanhong’s response:**

> zhanhong not response yet

## Main strengths

The thesis has a clear central question: how musically interpretable dynamics labels can be recovered from incomplete, weakly expressive, or weakly supervised music data without changing note content or timing. This question gives the thesis a coherent intellectual framework and avoids the common problem of a PhD thesis appearing like a collection of disconnected papers. However, the thesis question is clearly articulated in the Abstract, Chapters 1 & 2, and revisited in the Conclusion. The technical chapters do address this question through speciﬁc recovery scenarios, such as symbolic velocity completion, score-informed velocity correction, audio-only score-dynamics recovery, and beyond-piano proxy-supervised velocity estimation. However, the connection between each technical chapter and the central thesis question could be made more explicit. I recommend a minor revision in which each technical chapter includes a short opening or closing paragraph that explains how that chapter addresses the central question under its speciﬁc data-availability condition. This is a minor revision, not a substantive ﬂaw. Technically, the contribution is substantial.

**Zhanhong’s response:**

> zhanhong not response yet

The experimental design is credible. For example, Chapter 3 evaluates velocity completion using MAE, MSE, SDae, Recall10%, SDvelo, and a MUSHRA-inspired listening test. The proposed U-Net improves over ﬂat velocity, Seq2Seq, and ConvAE baselines on both MAESTRO and SMD. On MAESTRO, MAE improves to 11.5 compared with 12.3 for ConvAE and 14.8 for ﬂat velocity; on SMD, MAE improves to 11.2 compared with 12.5 for ConvAE and 15.3 for ﬂat velocity.

**Zhanhong’s response:**

> zhanhong not response yet

The thesis also shows good methodological awareness. It recognizes that MIDI velocity, audio loudness, and score dynamics are related but not interchangeable. This is important because it prevents the work from making over-simple claims about mapping one representation directly into another. The thesis repeatedly returns to this issue in its framing, methodology, and future work.

**Zhanhong’s response:**

> zhanhong not response yet

The beyond-piano chapter is a valuable exploratory extension. It does not overclaim universality. Ch. 6 explains that Diff-SFProxy is useful when a matched differentiable synthesizer is unavailable or unreliable, while still acknowledging cases where waveform-based Diff-Synth may be preferable.

**Zhanhong’s response:**

> zhanhong not response yet

Structurally, I like the thesis's approach, where each main technical chapter begins with a clear chapter overview and positioning statement, then proceeds through problem formulation, methodology, experimental design, results, discussion, and summary. This organization helps the reader understand the speciﬁc role of each chapter within the broader thesis. It is particularly effective in this thesis because the work consists of several related but distinct recovery scenarios. The introductory sections clarify the purpose and scope of each chapter, while the discussion and summary sections help connect the technical results back to the central research question. Overall, this chapter structure improves readability, coherence, and progression across the thesis.

**Zhanhong’s response:**

> zhanhong not response yet

## Overall remarks

The most prominent contribution of the thesis, in my view as the examiner, is found in Chapter 6, where the candidate extends the velocity-recovery problem beyond the supervised piano setting by introducing a differentiable SoundFont proxy for weakly supervised cross-instrument velocity estimation. This chapter is particularly impressive because it addresses the absence of reliable target-domain velocity labels and proposes a carefully constrained proxy-supervision strategy. The contribution is original, technically interesting, and critically presented, especially in its recognition that the recovered velocity should be interpreted as a renderer-conditioned dynamics coordinate rather than a direct physical measurement. Chapter 4 is also a strong practical contribution because its modular score-informed correction strategy can improve velocity estimation without redesigning existing AMT backbones. Chapter 5 is conceptually important because it treats score dynamics as a different symbolic target from MIDI velocity.

**Zhanhong’s response:**

> zhanhong not response yet

## Main weaknesses and required minor revisions

The thesis should more explicitly distinguish between published contributions, adapted contributions, and new thesis-level syntheses. The thesis states that Chapters 3–5 preserve technical contributions from peer-reviewed publications and adapt them into a uniﬁed narrative. This is acceptable, but the reader or I, as a thesis reviewer, would beneﬁt from a clearer statement of what was newly added to the thesis, especially in the introduction or contribution section.

**Zhanhong’s response:**

> zhanhong not response yet

The discussion of generalisability should be strengthened. The thesis is honest that the main empirical focus is piano, with beyond-piano work treated as exploratory. However, I think a clearer statement of which conclusions can and cannot be transferred to guitar, voice, bowed strings, and wind instruments would be more informative. This is a minor revision because the limitation is already acknowledged, but it could be improved.

**Zhanhong’s response:**

> zhanhong not response yet

The perceptual evaluation in Chapter 3 is useful but modest in scale, with 11 expert listeners. This does not invalidate the work, but the thesis should more clearly and explicitly state that the listening test supports the objective results rather than providing deﬁnitive perceptual validation.

**Zhanhong’s response:**

> zhanhong not response yet

Some presentation improvements are advisable. The English is generally excellent and suitable for publication. Still, there are a few formatting artifacts and phrasing issues, likely from PDF conversion or LaTeX output, such as line-break artifacts. These could be corrected.

**Zhanhong’s response:**

> zhanhong not response yet

## Recommendation:

I would recommend: Pass with minor revisions to the satisfaction of the supervisors. This thesis is clearly above the minimum PhD standard.

**Zhanhong’s response:**

> zhanhong not response yet

The thesis satisﬁes the requirements for the award of the PhD degree. It makes a substantial, original, and technically sound contribution to expressive automatic music transcription, especially in recovering MIDI velocity and score-level dynamics. The candidate demonstrates strong familiarity with the relevant literature, applies appropriate modern machine-learning techniques, and presents results through suitable quantitative, ablation, cross-dataset, and perceptual evaluations. The thesis is well organized and generally written to a publishable standard.

**Zhanhong’s response:**

> zhanhong not response yet

The required revisions are minor and should focus on improving clarity rather than changing the substance of the work. In particular, the candidate should clarify the relationship between published papers and thesis-level contributions, strengthen the discussion of generalisability beyond piano, state the limitations of the perceptual evaluation more explicitly, and correct minor English, formatting, and presentation issues. No additional experiments, new data collection, or major rewriting are required.

**Zhanhong’s response:**

> zhanhong not response yet

This thesis is clearly above the minimum PhD standard. I would recommend “Pass with minor revisions to the satisfaction of the supervisors” because there are still a few presentation and clariﬁcation issues. I would also not recommend “Pass with substantive amendments” because the research design, contribution, results, and conclusions are already sound.

**Zhanhong’s response:**

> zhanhong not response yet

Finally, according to the review guidelines, a Pass with minor revisions and an overall score of 2 (Excellent) is the most defensible decision.

**Zhanhong’s response:**

> zhanhong not response yet

*Type text here*
