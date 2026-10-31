# Independent C2 critique

Read the voice card, all 21 entries including N07, the real chapter contexts, the MAESTRO metric table, listening protocol/table, duration results, and genuine R1-33/34 author replies. **No hard factual blocker in the selected set. One minimal clarification below; no further candidate generation needed.** ACCEPT means adopt the proposed change, including a proposed deletion. Existing fact checks and baseline uncertainty remain open.

- **T01 — ACCEPT.** Reverse paraphrase: flattened/coarsened expression and indirect supervision describe different, potentially overlapping information conditions. Placement immediately after the question defines its terms when needed. The following scenario paragraph still requires its separately specified S3/order repairs; this insertion does not validate that unchanged paragraph.

- **T02 — ACCEPT.** Reverse paraphrase: guitar adaptation extends the audio-plus-aligned-notes velocity setting, while audio-only velocity remains untested future work. Ch6 retains VeloEst and aligned events. This short addition answers the scenario question directly without adding an S4 or turning guitar into score-dynamics estimation. 

- **T03 — ACCEPT.** Reverse paraphrase: the method processes a binary pitch–time grid into scalar velocities, using colourisation as an analogy. The note-list sentence accurately describes changing the interface, without claiming a tested advantage over event-list models.

- **T04 — ACCEPT.** Reverse paraphrase: joint note/dynamics modelling could help, but this known-onset experiment does not measure that benefit. Cutting the repeated application introduction improves the reinsertion: the preceding interface explanation already identifies the narrow task. This sentence adds the missing limitation without contradicting the reported velocity gains or implying timing correction.

- **T05 — ACCEPT.** Reverse paraphrase: the separate head supervises boundaries explicitly rather than deriving them only from predicted states. The existing six-class/blank, binary-target and beat-grid definitions remain intact. This is a useful answer to why the head exists; it claims neither measured superiority of the head nor perfect agreement between heads.

- **T06 — ACCEPT.** Reverse paraphrase: real-audio adaptation obtains an indirect training signal without target velocity labels, but renderer mismatch remains possible. It avoids claiming the synthetic-to-real problem disappears. The following discussion explains the interface sufficiently.

- **T07 — ACCEPT.** Reverse paraphrase: degradation is compatible with synthesis mismatch, without isolating reconstruction or gradient fidelity. This follows the genuine author reply closely and preserves the distinction between mechanism and measured cause. Its location after the loss definition is coherent, even though it briefly anticipates the later results.

- **T08 — ACCEPT.** Reverse paraphrase: four co-authored studies supply the technical chapters, and their shared framing/discussion supplies thesis synthesis. It corrects the Ch3–5 omission without asserting that every thesis result was published. Final Ch5 paper/result attribution still needs the existing final-paper verification; this wording does not settle it.

- **T09 — ACCEPT.** Reverse paraphrase: evidence covers piano and exploratory guitar, while sustained/continuous controls in untested instruments exceed the present descriptors. “Second” preserves the First/Second/Third/Fourth sequence. Ch6 retains the detailed rationale, so this concise conclusion paragraph is sufficient. Interpret the final clause as concerning representation of those continuous controls, not impossibility of any onset-level task on those instruments.

- **T10 — ACCEPT.** Reverse paraphrase: U-Net has higher mean reference-similarity ratings within the small, selected listening setup. The table/protocol support the ordering and sample/rendering details. Removing the confidence-interval-to-consistency inference is appropriate. This does not settle the separate timing-preprocessing question or promise population-wide perceptual validation.

- **T11 — ACCEPT.** Reverse paraphrase: Huber was chosen for its local gradient/large-residual behaviour, without established superiority over MAE. The author's actual response supports exactly this distinction. Crucially, “not established” does not falsely become “no comparison was performed”. Beta, averaging, PHE/OSF weighting and both equations remain present.

- **N01 — CHANGE minimally.** Reverse paraphrase: both similarity metrics distinguish the two velocity conditions; numerical gaps alone do not prove a sensitivity ranking. “Measured on different scales” can imply distinct literal units when both are dimensionless similarities. Prefer: **“Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.”** 

- **N02 — ACCEPT.** Reverse paraphrase: changing the entire renderer changes metric values; the experiment does not isolate gain. Reported deltas match the table's summary rows; do not recompute them from rounded cells. The final sentence identifies the purpose of correlation rather than claiming the experiment proved gain caused the MAE drift.

- **N03 — ACCEPT with N01/N02 as one unit.** Reverse paraphrase: correlation is the chosen contour-agreement measure, supported by a limited piano diagnostic. It retains a practical metric choice while dropping universal “fail” and “right trade-off” judgments. Leaving the old concluding paragraph would undo the repair. Neither this diagnostic nor its selection verifies guitar velocity ground truth.

- **N04 — ACCEPT.** Reverse paraphrase: mismatch can redirect waveform-loss gradients away from velocity. Conditional “can” corrects the background's universal dominance claim while preserving the comparison-space explanation, examples and citations. It now agrees with T07's unisolated causal evidence.

- **N05a — ACCEPT.** Reverse paraphrase: the thesis has limitations, detailed next. Deleting the pre-emptive “unfinished implementation” defence loses no limitation or research result; First/Second continuity remains.

- **N05b — ACCEPT.** Reverse paraphrase: the results motivate future research. Removing “rather than repair it” loses only an argumentative defence, and the actual future directions remain.

- **N05c — ACCEPT.** Reverse paraphrase: structural assumptions delimit the studied recovery tasks. The preceding aligned-event and beat-grid conditions remain explicit; the replacement neither denies weaknesses nor expands scope.

- **N06a — ACCEPT.** Reverse paraphrase: tested durations led to the empirical 10-second choice, without a measured phrase-completeness explanation. Deletion preserves T=96, all four tested durations, the reported choice and resolution equation.

- **N06b — ACCEPT.** Reverse paraphrase: the reported duration comparison improves from 20 to 10 seconds and slightly worsens at 5 seconds. The table and this measured result remain; deleting the tempo/bar/complete-phrase story removes an unsupported causal explanation. Apply both N06 deletions together so that story does not survive elsewhere.

- **N07 — ACCEPT.** Reverse paraphrase: the table reports metric values without ranking incomparable raw gaps. Independently matched the proposed `.tex` to the checked proposal and verified identical numeric-token sequences. Removing 12 numeric emphasis wrappers and the best/second-best caption sentence is required for consistency with N01–N03; headers and row labels remain.

Final integrity condition: apply the selected changes together with their named scope/terminology synchronisations, preserve citations/settings/results, and leave author facts unresolved. No thesis source, old decisions or shared proposal files were edited during this critique.
