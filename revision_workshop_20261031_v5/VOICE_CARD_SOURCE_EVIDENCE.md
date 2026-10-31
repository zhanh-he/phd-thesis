# Independent source-first voice and claim card

This report was made before reading any files in `revision_blueprint_20261031`. It uses the current LaTeX, actual author comments transcribed from Report 1, and the first two pages of the CMMR and ISMIR papers. Current LaTeX is a readable source, not proof that it is the submitted PDF baseline. Published papers establish the most defensible polished scholarly register; informal reviewer replies establish intended stance, not grammatical templates.

## What sounds like the author

1. **Start with the practical task, then name the representation, then explain the method.** CMMR p.1: “The task of filling MIDI velocity is termed MIDI velocity prediction”; “In this paper, we introduce the U-Net”. ISMIR p.1 begins with existing datasets and missing reliable velocities, then defines label-scarce adaptation. Prefer a concrete one-sentence task over a second thesis-level manifesto.
2. **Use direct research verbs with explicit objects.** The papers repeatedly use “we introduce”, “we adopt”, “we develop”, “we evaluate”; ISMIR p.2: “We adopt the score-HPT model”; “During cross-instrument adaptation, only VeloEst is updated”. Methods should say which model takes which inputs and what changes. Passive prose is useful for fixed protocols, not to hide agency.
3. **Terminology is musical and operational.** Preserve “MIDI velocity”, “aligned note events”, “note-level”, “piano roll”, “score dynamics”, “BSSL/BSTL”, “Diff-Synth”, “Diff-SFProxy”. In the newer paper, “renderer-conditioned velocities” is author-published terminology, not an unnecessary caveat invented by this workshop. Prefer it once at the defining point, then use “recovered velocity”.
4. **The argument is usually motivation → design choice → result → limit.** CMMR p.1 gives software-MIDI problem, velocity-only scope, U-Net design, MAESTRO/SMD evaluation, with “Current dataset availability restricts our experiments to piano data.” ISMIR p.1 gives label scarcity, real-audio adaptation, then two concrete benefits of the proxy. “The main result is therefore a design principle rather than just a lower error table” (current Ch4:321) is more rhetorical than the paper register; do not multiply such sentences simply to imitate current thesis framing.
5. **Keep the author's willingness to concede, without reproducing rough spoken grammar.** Report 1:223 says “Yes my mistake” and intends “less input signal”; 243–247 explains the two-dimensional input/output and accepts “image-like”. 405 states that mismatch is consistent with degradation but not separately measured. 413 states that Huber superiority over MAE has not been established; it does not categorically state that no comparison was ever conducted. Polished replies should preserve these limits and directness, not adopt defensive new justifications.
6. **Do not oversanitize useful concrete examples.** The author's reply at 231–235 gives Chopin/Beethoven and seen/unseen composers to explain intended style control. A short example can be more human and precise than “heterogeneous distributional regimes”. But the public scholarly version need not disclose the informal Dolby explanation in 279–283.

## Hard factual/semantic gates

| Topic | Source evidence | Safe editorial boundary |
| --- | --- | --- |
| S1 “most controlled” | Ch3:13,31,465; author reply 223 explicitly agrees this implies the wrong inferential constraint | Replace the global ranking, not the fixed-note assumption. “Symbolic-only setting” or “setting with fixed notes and timing” works. The author means less input evidence, not easier inference. Check Intro:118, Conclusion:48 too. |
| Preserve timing | Ch3:41 fixes notes, onsets, offsets; Ch4:319 corrects velocity at known score onsets; Ch5:36 predicts beats/downbeats when a grid is absent | Do not claim every chapter starts with known timing. Ch5 estimates a metrical grid; the methods do not jointly rewrite note content. Ch4's “correction” is velocity correction, not temporal correction. |
| Beyond-piano inputs | Ch6:91–93 explicitly uses score-informed HPT and aligned note information; :523 requires aligned note events. ISMIR p.2 says the same | Do not promise audio-only guitar transcription or a complete audio-to-MIDI system. Audio-only adaptation remains a possible future direction, per author reply 137–139. |
| Physical interpretation | Ch6:58–69 defines the renderer-relative target; :459 says different SoundFonts can give different recovered velocities; ISMIR abstract uses “renderer-conditioned” | Do not call acoustic guitar velocities measured striking force, canonical GT, or physically absolute. Preserve the relation to the selected renderer. |
| Diff-Synth mismatch | Report 1:405: “we have not separately measured reconstruction fidelity and velocity-gradient accuracy”; Ch6:36 describes mismatch mechanism | Say mismatch is a plausible interpretation of the tested degradation, not experimentally isolated cause or measured gradient-fidelity failure. |
| Huber | Author reply 413 says superiority over MAE was not established through a dedicated comparison | State smooth near-zero / L1-like large-error design rationale. Do not say it improved robustness empirically compared with MAE. |
| Guitar figure GT | Ch6:442,447 calls a guitar panel GT; :8,:26 say public target corpora lack velocity labels | The source has unresolved tension. The report alone cannot identify the figure's provenance. Flag author fact check; changing labels blindly would manufacture provenance. |
| Generalisation | Ch6:519 limits experiments to attack-driven piano/guitar; :523 retains aligned notes | Do not generalise the measured result to voice, bowed strings or winds. Instrument-specific sustain controls are future work. |

## Minimum-edit examples for the main workshop

These are source-first suggestions, not decisions on any older proposal:

- Ch3:13: “This chapter addresses Scenario S1, the symbolic-only setting in the thesis map.” Keep the next sentence about fixed notes/timing. This removes the disputed ranking at a cost of four words; no larger rewrite is needed unless the paragraph has another demonstrable defect.
- Ch3:31: replace “the most constrained setting in that map” with “the symbolic-only setting in that map”. Ch3:465 and Conclusion:48 require corresponding local repair; Intro's “tightly constrained to the ambiguous” also deserves semantic review because S1 has fixed structure but less performance evidence.
- Ch6:31 “a different and simpler route” is not defensible as a complexity claim. ISMIR p.1 already uses the better author-published wording “a more direct route”. Use that phrase rather than introducing unmeasured efficiency claims.
- Intro:89 “initial strike force” is narrower than the thesis' cross-instrument operational meaning. A note-onset control value consistent with Ch6:21–23 is safer than physical force. Do not let a useful short definition erase the instrument-dependent mapping.

## Checks actually used

Read current Intro, Ch3–6 openings/method context/summaries, Conclusion context, and genuine author reviewer responses. Read CMMR and ISMIR PDF pages 1–2 locally with macOS PDFKit through Swift. `python3` had no pypdf, pdfplumber, PyMuPDF or textstat; `pdftotext`, Vale and LanguageTool were not on PATH. No installation, external grammar/LLM endpoint, upload, or manuscript modification was used. PDF line breaks/hyphenation were treated as extraction artifacts, not author style.
