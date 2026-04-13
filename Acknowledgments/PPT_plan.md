# PhD Thesis Defense Presentation: Recovering Musical Dynamics for Expressive AMT
**Target Audience:** Audio and Signal Processing Experts (Non-Music Experts).
**Tone:** Academic, rigorous, deep into methodology, emphasizing contributions.
**Duration:** 40 Minutes (Approx. 25 Slides).

## 💡 System Instruction for NotebookLM (Provide this first)
*Prompt to NotebookLM:*
"I am preparing my PhD thesis defense presentation based on the uploaded document 'main.pdf'. The presentation is 40 minutes long. The audience consists of audio and signal processing experts who do NOT have a formal music background. Therefore, all musical concepts (e.g., MIDI velocity, score dynamics, notes) must be clearly mapped to signal processing and acoustic concepts (e.g., attack intensity, perceptual loudness representations, symbolic control variables). I will provide you with a series of prompts, one for each slide. For each slide, generate: 1) The Slide Title. 2) 3-4 concise, highly academic bullet points emphasizing methodology and contributions. 3) Suggestions for visuals/diagrams from the thesis. 4) Detailed Speaker Notes (approx. 150-200 words) that I can read during the defense to sound authoritative and clear."

---

## 📄 Slide-by-Slide Prompts

### Part 1: Introduction & Problem Formulation

**Slide 1: Title Slide**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 1. Create a title slide for the thesis: 'Recovering Musical Dynamics for Expressive Automatic Music Transcription'. Include my name, Zhanhong He. [cite_start]In the speaker notes, provide a strong 1-minute opening hook that introduces Automatic Music Transcription (AMT) as an acoustic-to-symbolic mapping problem, and immediately highlight the missing dimension: expressive dynamics[cite: 1441, 1442]."

**Slide 2: The Gap in Current AMT Systems**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 2. Focus on the 'Research Gap'[cite: 1478, 1479]. [cite_start]Explain that current deep-learning AMT excels at structural recovery (pitch and timing) but fails at expressive recovery (dynamics)[cite: 1443, 1444]. Frame this as an asymmetric progress problem. [cite_start]Explain why structurally perfect but flat transcription is insufficient for rendering, analysis, or data curation[cite: 1446, 1447, 1466, 1467, 1468]. [cite_start]In the speaker notes, emphasize our contribution: establishing dynamics as a first-class target in expressive AMT[cite: 1445]."

**Slide 3: Operationalizing Dynamics (Acoustic vs. Symbolic)**
*Prompt for NotebookLM:*
"Generate Slide 3. This is crucial for the audio expert audience. [cite_start]Explain the 4-layer taxonomy of dynamics from the thesis: 1) Physical sound level (dB/energy), 2) Perceived loudness (frequency/masking dependent), 3) MIDI velocity (note-onset control proxy), 4) Score dynamics (symbolic, context-dependent intention)[cite: 1657]. Use Figure 2.1 as the visual suggestion. [cite_start]Emphasize that mapping between these layers is a complex, non-linear inverse problem, not a simple lookup table[cite: 1661]."

**Slide 4: Thesis Unified Framework & Three Core Scenarios**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 4. Outline the thesis structure based on the three core scenarios (S1, S2, S3)[cite: 1546, 1548, 1551]. [cite_start]Explain how supervision weakens progressively across the chapters: S1 uses symbolic notes only [cite: 1546][cite_start], S2 uses audio + aligned score [cite: 1548][cite_start], and S3 uses audio only[cite: 1551]. [cite_start]Briefly mention Chapter 6 as an exploratory beyond-piano extension[cite: 1564]. [cite_start]Speaker notes should frame this as a robust label-recovery framework under heterogeneous supervision regimes[cite: 1583]."

---

### Part 2: Scenario S1 - Symbolic-Only Recovery

**Slide 5: Problem Setting - Symbolic MIDI Velocity Completion**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 5. Introduce Chapter 3: Symbolic MIDI Velocity Completion[cite: 1584]. [cite_start]Define the problem: completing note-level intensity (velocity) when structural notes and timing are already fixed[cite: 1546, 1547]. Explain this as a data curation and rendering necessity where acoustic input is unavailable. [cite_start]Emphasize the constraint: we must not alter the original composition's note content[cite: 1575]."

**Slide 6: Method - Image Colorization on Sparse Representations**
*Prompt for NotebookLM:*
"Generate Slide 6. Deep dive into the Chapter 3 methodology. [cite_start]Explain the novel formulation: treating symbolic MIDI as a sparse 2D image (piano-roll) and velocity completion as an image colorization task[cite: 1584]. [cite_start]Discuss why this captures local polyphonic structure and spatial regularities better than pure sequence models[cite: 602, 603, 604, 605]. Visual: Suggest showing the U-Net input/output rolls."

**Slide 7: Architecture - Attention U-Net & Sparsity-Aware Loss**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 7. Detail the network design for Chapter 3. Highlight the use of an Attention U-Net combining skip connections for fine detail with window attention for global context[cite: 497, 498, 1585]. [cite_start]Critically, explain the 'sparsity-aware loss function' [cite: 1585][cite_start]—why it is necessary to prevent the network from wasting capacity on the overwhelming zero-valued (silent) regions of the MIDI matrix[cite: 679]."

**Slide 8: Contributions & Results (S1)**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 8. Summarize the results of Chapter 3. Highlight both objective metrics improvements and the human listening tests[cite: 1585]. [cite_start]Point out that our model produces more human-like intensity profiles (dispersion-sensitive statistic SD_velo) compared to sequence-based baselines[cite: 660, 661]. [cite_start]Frame the contribution: note-level dynamics can be recovered as a controllable post-processing layer without acoustic data[cite: 1613]."

---

### Part 3: Scenario S2 - Score-Informed Refinement

**Slide 9: Problem Setting - Score-Informed Velocity Estimation**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 9. Introduce Chapter 4[cite: 1586]. [cite_start]The setting changes: we now have performance audio and an aligned symbolic score[cite: 1548]. [cite_start]Problem: AMT-estimated velocities are noisy and sensitive to acoustic domain shifts[cite: 700]. [cite_start]The goal is to refine note-level MIDI velocity using the score as a structural prior[cite: 1549, 1550]."

**Slide 10: Method - The Modular Correction Principle**
*Prompt for NotebookLM:*
"Generate Slide 10. Explain the core philosophy of Chapter 4: Late residual correction. [cite_start]Contrast this with traditional 'early-fusion' models that require redesigning the entire acoustic AMT backbone[cite: 718, 719, 720]. [cite_start]Emphasize that our modular approach allows portability across different state-of-the-art AMT front-ends without re-engineering[cite: 1588]. Suggest Figure 4.1 (Modular correction vs feature-fusion)."

**Slide 11: Architecture - Lightweight Token-Based Transformer**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 11. Detail the architecture of the score-informed module[cite: 1587]. [cite_start]Explain the shift from dense frame processing to a token-based representation (onset tokens)[cite: 499, 500, 501]. [cite_start]Discuss the lightweight Conformer-like Transformer encoder [cite: 1405] [cite_start]and why it prevents the network from over-fitting to domain-specific acoustic envelopes compared to recurrent models (like BiLSTM)[cite: 806, 807, 808]."

**Slide 12: Robustness and Generalization (S2)**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 12. Present the key findings of Chapter 4. Emphasize the model's strong cross-dataset generalization and portability across AMT backbones[cite: 805]. [cite_start]Highlight the robustness analysis: the Transformer correction remains effective even under moderate audio-score misalignment [cite: 1587][cite_start], which is a critical engineering requirement for real-world archives[cite: 792, 795]."

---

### Part 4: Scenario S3 - Audio-Only Recovery

**Slide 13: Problem Setting - Beat-Synchronous Score Dynamics**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 13. Introduce Chapter 5[cite: 1589]. [cite_start]Setting: Audio input only, no structural support[cite: 1551]. [cite_start]Target shift: Moving from precise machine-control (MIDI velocity) to human-readable, relative score dynamics (e.g., pp, mf, f)[cite: 1551, 1821, 1822]. [cite_start]Explain why this requires a musically meaningful coordinate system (beat grid) rather than isolated note events[cite: 1813, 1815]."

**Slide 14: Feature Engineering - Bark-Scale Specific Loudness (BSSL)**
*Prompt for NotebookLM:*
"Generate Slide 14. This slide is critical for audio experts. Defend the input feature choice. [cite_start]Explain why raw spectrograms (Log-Mel) are sub-optimal for dynamics[cite: 936, 1681]. [cite_start]Introduce the perceptually grounded BSSL front-end[cite: 1590, 1769]. [cite_start]Detail how it accounts for frequency-dependent hearing sensitivity, critical-band interaction, and masking [cite: 1679][cite_start], preserving the perceptual spectral envelope crucial for human loudness perception[cite: 1793]."

**Slide 15: Method - Multi-Task Multi-Scale Network & MMoE**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 15. Detail the Chapter 5 architecture[cite: 1589]. [cite_start]Explain the necessity of Multi-Scale encoding to capture both fine metrical timing (beats) and long-context phrase-level dynamic intent[cite: 1589, 939, 943]. [cite_start]Introduce the Multi-gate Mixture-of-Experts (MMoE) decoder[cite: 1590]. [cite_start]Explain how MMoE performs task-aware routing to jointly estimate dynamic levels, change points, beats, and downbeats while mitigating negative transfer between tasks[cite: 492, 493, 494]."

**Slide 16: Joint Estimation Results & Contributions**
*Prompt for NotebookLM:*
"Generate Slide 16. Summarize Chapter 5 results. [cite_start]State that joint learning of metre and dynamics significantly outperforms single-task baselines[cite: 930]. [cite_start]Highlight the massive dimensionality reduction achieved by BSSL (128 mel bins down to 22 Bark bands), which enables long-context processing (60-second segments) on standard hardware[cite: 933, 934]. [cite_start]Conclude that this produces actionable, score-facing symbolic annotations directly from audio[cite: 1319]."

---

### Part 5: Exploratory Frontier - Beyond Piano

**Slide 17: Problem Setting - Cross-Instrument Transfer & Data Scarcity**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 17. Introduce Chapter 6 (Exploratory extension)[cite: 1595]. [cite_start]Explain the fundamental bottleneck in expressive AMT: reliable note-level velocity ground truth is overwhelmingly concentrated on instrumented pianos (e.g., Disklavier)[cite: 1571]. [cite_start]Address the problem of extending velocity estimation to other instruments where direct supervised labels are scarce or non-existent[cite: 1498, 1499, 1595]."

**Slide 18: Method - Supervision via Differentiable Proxies**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 18. Explain the proposed solution: bypassing the need for ground-truth MIDI velocity by using proxy supervision[cite: 1321, 1322]. [cite_start]Contrast Route III (Matched Differentiable Synthesizers like DDSP) with Route IV (Differentiable Neural Proxies of black-box SoundFont renderers)[cite: 1038, 1039]. [cite_start]Frame the 'DiffProxy' as a portable solution for cross-instrument transfer when matched waveform renderers are unavailable[cite: 1042]."

**Slide 19: The Neural SoundFont Proxy Interface**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 19. Dive deeper into the DiffProxy mechanism[cite: 1177]. [cite_start]Explain how the proxy maps note-wise parameters to acoustic features (like loudness contours) through a frozen, differentiable network[cite: 1177, 1178, 1181]. [cite_start]Emphasize that gradients flow back from the signal domain to correct the velocity estimator, optimizing for attack and intensity cues rather than full waveform reconstruction[cite: 1178]."

**Slide 20: Diagnostics & Exploratory Findings**
*Prompt for NotebookLM:*
[cite_start]"Generate Slide 20. Discuss the evaluation methodology for Chapter 6. Since ground truth is missing, explain the use of time-series agreement measures on specific loudness (BSSL) and total loudness (BSTL) using Pearson correlation[cite: 1120, 1121, 1122]. [cite_start]Summarize the main exploratory finding: when labels are scarce and waveform mismatch is high, a feature-level proxy of a practical renderer provides a superior supervision interface[cite: 1181]."

---

### Part 6: Conclusion

**Slide 21: Summary of Thesis Contributions**
*Prompt for NotebookLM:*
"Generate Slide 21. Synthesize the core contributions. [cite_start]1) Established dynamics as a first-class transcription target[cite: 1445]. [cite_start]2) Formulated a unified label-recovery framework across varying supervision constraints[cite: 1472, 1583]. [cite_start]3) Delivered robust methodologies: U-Net for symbolic completion, Transformer for residual correction, MMoE + BSSL for joint audio-to-score extraction, and DiffProxy for zero-label instrument transfer[cite: 1584, 1586, 1589, 1595]."

**Slide 22: Broader Impact on Audio & MIR**
*Prompt for NotebookLM:*
"Generate Slide 22. Discuss the impact of this work. [cite_start]Frame it not just as a music project, but as a blueprint for bridging semantic gaps between physical measurements and human cognition[cite: 1469]. [cite_start]Highlight applications in dataset curation (upgrading static archives into expressive corpora), expressive digital rendering, and automated performance assessment[cite: 1466, 1471, 1533]."

**Slide 23: Limitations**
*Prompt for NotebookLM:*
"Generate Slide 23. Act as a rigorous PhD candidate acknowledging limitations. [cite_start]1) Empirical focus remains heavily piano-centric due to data availability[cite: 1571]. [cite_start]2) The models preserve note content but do not jointly optimize micro-timing or articulation[cite: 1572, 1578]. [cite_start]3) Score dynamics modelling (Ch 5) relies heavily on beat-synchronous assumptions and a limited vocabulary (pp to ff)[cite: 1813, 1815]."

**Slide 24: Future Directions**
*Prompt for NotebookLM:*
"Generate Slide 24. Propose future research. [cite_start]1) Exploring self-supervised pretraining for cross-instrument velocity estimation[cite: 812]. [cite_start]2) Developing more complex alignment techniques (e.g., handling local tempo warping or missing ornaments) for score-informed models[cite: 810]. 3) Expanding the DiffProxy framework to encompass full multi-dimensional continuous expressive control (e.g., breath pressure, bow speed)."

**Slide 25: Q&A / Thank You**
*Prompt for NotebookLM:*
"Generate Slide 25. A professional closing slide. Title: 'Thank You'. Include bullet points summarizing the core PhD defense statement: 'Recovering musically interpretable dynamics bridges the gap between mechanical notation and expressive performance.' Provide speaker notes thanking the committee and opening the floor for questions."