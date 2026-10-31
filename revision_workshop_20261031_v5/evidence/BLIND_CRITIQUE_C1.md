# Blind critique — cycle 1

Fifteen tournaments, including the three supplements. I read the candidate packet and source-first voice card before checking manuscript sources; no provenance key or prior proposals were read. Scores are separate ordinal judgments in **response / voice / necessity and minor-revision scope / reinsertion cohesion / clarity** order: **0** misses, **1** partial, **2** adequate, **3** strong. They are not summed. **FAIL** excludes the present wording before preference scoring; omission candidates are assessed against the supplied existing passage.

| Case | Winner | Runner-up | K | L | M | N |
|---|---|---|---|---|---|---|
| T01 | L | K | 3/3/2/3/3 | 3/3/3/3/3 | 3/2/1/2/2 | 0/3/1/3/3 |
| T02 | K | M | 3/3/3/3/3 | 2/3/3/3/3 | 3/2/2/3/2 | 0/3/1/3/3 |
| T03 | M | N | 2/2/2/3/2 | 1/2/2/3/2 | 3/3/3/3/3 | 2/3/3/3/3 |
| T04 | K | M | 3/3/2/2/3 | 1/3/3/3/3 | 3/2/1/2/2 | 2/3/2/2/3 |
| T05 | M | L | 2/3/2/3/3 | 3/3/2/3/3 | 3/3/3/3/3 | 1/3/2/3/3 |
| T06 | L | M | 3/2/2/3/2 | 3/3/3/3/3 | 2/3/3/3/3 | FAIL |
| T07 | M | L | 1/2/2/3/2 | 3/3/2/3/2 | 3/3/3/3/3 | FAIL |
| T08 | L | M | 3/2/1/2/2 | 3/3/3/3/3 | 2/3/3/3/3 | 1/2/2/3/3 |
| T09 | L | N | 2/3/3/2/3 | 3/3/3/2/3 | 1/2/2/3/2 | 3/3/2/2/2 |
| T10 | L | N | 3/3/2/3/3 | 3/3/3/3/3 | FAIL | 3/3/3/3/3 |
| N01 | L | K | 3/2/2/2/2 | 3/3/3/2/3 | FAIL | FAIL |
| N02 | M | N | FAIL | FAIL | 3/3/3/2/3 | 2/3/3/2/3 |
| T11 | L | K | 2/2/3/3/3 | 3/3/3/3/3 | 1/2/1/2/2 | FAIL |
| N03 | L | M | FAIL | 3/3/3/3/3 | 3/3/3/3/3 | FAIL |
| N04 | N | M | FAIL | FAIL | 2/3/3/3/3 | 3/3/3/3/3 |

## Pairwise decisions and repairs

**T01 — L over K.** L defines both terms, supplies the operational renderer example, and explicitly permits overlap without M's extra definition of “incomplete” and repeated boundary statements. K is clear but loses that overlap clarification. **Repair:** none.

**T02 — K over M.** “Extends S2 to guitar” directly locates Chapter 6, retains aligned note events, and distinguishes S3's score target without M's longer detour through what audio-only estimation could do. L leaves the S3 distinction implicit. **Repair:** none; preserve the separately planned S3/scope repairs.

**T03 — M over N.** M alone directly answers the note-list comparison while explaining binary input, scalar velocity output, and simultaneous-note structure. This matches Ch3:52–53's F-input/V-target/O-mask roles. N is a good concise alternative but omits note lists. K risks attributing fixed-note preservation to convolution/skip connections rather than the task/output interface. **Repair:** none; preserve the following Problem Setting and detailed representation definitions.

**T04 — K over M.** The useful addition is the explicit boundary that joint note-and-velocity gains are untested. M repeats educational/archival uses already given twice in the chapter. KEEP is credible for avoiding repetition, but leaves that evaluation boundary unstated. **Minimal repair:** delete K's first sentence; retain its sentence beginning “Note detection and velocity estimation…”.

**T05 — M over L.** M acknowledges that level transitions could supply boundaries, then states the actual design choice without claiming an ablated gain. L is accurate but repeats the existing definition of what a change point means. **Repair:** append only the rationale; retain the six classes, frame targets and beat-snapping protocol.

**T06 — L over M.** L names piano pretraining, real-audio adaptation, missing labels and the remaining matching limitation. M's “suitable renderer” is less explicit about acoustic mismatch. N **fails** on unmeasured simplicity and its claim to avoid the domain gap. **Repair:** none; do not substitute an efficiency claim.

**T07 — M over L.** M retains the observed degradation and the exact missing measurements with less elaboration. L is fully defensible but longer. N **fails narrowly**: “which part of that mismatch caused” presupposes mismatch caused the degradation; the evidence establishes consistency, not isolated causation. K offers a mechanism without answering the measurement question. **Repair:** none to M.

**T08 — L over M.** L explicitly separates four co-authored studies from the thesis's unifying question and synthesis. M is terse but less explicit about the relationship. K duplicates the roadmap and bibliographic material; the Declaration also distinguishes publication statuses, so listing conference names should not imply all four are published. **Repair:** none; retain the chapter roadmap and avoid an exhaustive novelty claim.

**T09 — L over N.** L keeps the piano-supervision limitation and gives guitar's renderer-conditioned target and loudness evidence before naming untested instrument families. N is longer and introduces awkward “captured physical velocity labels”. **Minimal repair:** prepend **“Second,”** to preserve the surrounding First/Third/Fourth sequence. This is necessary reinsertion work, not a replacement of the whole limitations section.

**T10 — L over N.** L's “higher mean similarity ratings” and “supplementary perceptual evidence” state the measured outcome with the selected SMD scope. N is nearly tied. M **fails**: confidence-interval width does not establish listener consistency, and these means do not establish a general perceptual superiority claim. **Repair:** none; retain the procedure's rendered human-velocity reference and the citation.

**N01 — L over K.** Both similarity metrics rank GT above Flat. Pearson's .118/.263 and cosine's .052/.047 are numerical gaps under different metric response scales, not calibrated effect sizes. M/N therefore **fail** at “proving insensitive”; GT versus one flat baseline also does not establish sensitivity to fine differences. K is accurate but restates four table entries. **Minimal repair:** change L's opening to “Both similarity metrics score GT above flat velocity” to avoid inferential overtones in “separates”.

**N02 — M over N.** M correctly identifies a renderer intervention as a whole and gives a positive contour-agreement reason for Pearson. K/L **fail** because the swap does not isolate gain, and MAE-versus-correlation magnitudes cannot prove comparative robustness. N's “This supports using r” still leans on that comparison. **Repair:** none to M; limit the evidence to this SoundFont swap. Ch6:336 supplies the independent mathematical rationale concerning global scale and offset.

**T11 — L over K.** L reproduces the author's actual design rationale and evidential boundary. N **fails** because “did not conduct” invents an experimental-history fact from failure to establish superiority. M's onset-contamination rationale is unverified and does not explain an advantage over MAE. **Repair:** retain beta=1 and equal weighting; no new ablation claim.

**N03 — L over M.** L positively names the chosen rendered-contour metric and explicitly labels the supporting diagnostic as piano-based. M is also sound. K/N **fail** by retaining categorical sensitivity/robustness failures. **Repair:** apply N01, N02 and N03 together; otherwise the surviving conclusion contradicts the repaired evidence. No numerical recomputation is needed.

**N04 — N over M.** N names renderer mismatch and states a conditional mechanism. M's “can be influenced” is safe but vague and unnecessarily timid. K/L **fail** on universal gradient dominance. **Repair:** replace only the clause; retain the comparison-space explanation and citations.

The consequential dependencies are the T04 redundancy cut, T09 ordinal restoration and the N01–N03 joint application. The metric table's cross-metric “best/second-best” formatting also deserves an author check: raw separation or drift magnitudes cannot supply a commensurate ranking. This does not require changing any reported number.
