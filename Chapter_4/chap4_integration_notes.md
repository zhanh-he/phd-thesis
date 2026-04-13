# Chapter 4 integration notes

## What I changed
- Rebuilt Chapter 4 around the thesis skeleton:
  - Problem Setting
  - Modular Correction Principle
  - Score-Informed Correction Module
  - Integration with AMT Backbones and Experimental Protocol
  - Results and Analysis
  - Discussion
- Kept the paper core almost unchanged:
  - figures
  - equations
  - tables
  - core experiment paragraphs
- Removed the paper-style standalone related work section from Chapter 4.
- Added a thesis-style discussion section.
- Added a short provenance note at the start of the chapter.

## What I moved toward Chapter 2
The heavy literature review is better placed in Chapter 2.
This includes:
- early score-informed velocity estimation
- deep learning score-informed methods
- representative velocity-enabled AMT backbones
- early fusion versus late correction framing

I prepared a revised `literatureReview_revised.tex` with this shift.

## What Chapter 4 may still need
1. A short opening sentence in Chapter 1 or the chapter roadmap that explicitly says Chapter 4 is Scenario S2.
2. A brief statement in Chapter 4 that the score provides note events while the model only refines velocity.
3. If space allows, one short failure-case subsection or paragraph with examples of:
   - alignment error
   - missing ornament in score
   - repeated-passage mismatch
4. If you have the material, one tiny table or paragraph about inference cost or runtime overhead.
5. If examiners may ask about fairness, one sentence that HPPNet and DynEst were retrained with log-Mel for uniform comparison.

## Best minimal next additions
If you only add two thesis-only things beyond the paper, add these:
- a failure mode paragraph
- a practical implication paragraph for education and archive curation
