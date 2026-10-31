# Independent R2 integrity check

**PASS for writer R2 integrity; external cycle 2 remains pending.** This check does not constitute a new editorial round, author approval, source implementation or final baseline confirmation.

## Seven requested changes

Compared `FINAL_SELECTION_R2.json` directly with frozen `FINAL_SELECTION.json` and the seven IDs in `evaluator_cycle1_post_reveal.json`. Exactly **T01, T03, T07, T11, N02, N03, N05a** changed selected English. No other selected text changed and no IDs were added.

T01/T03/T07/T11/N05a match the evaluator's suggested English exactly. N02/N03 preserve the requested substance with an explicitly reasoned integration: N02 removes redundant table deltas and identifies whole-renderer intervention; the correlation-purpose/absolute-level sentence appears once in N03. The response document explains that choice accurately. No gain-only causality or cross-metric superiority claim was reintroduced.

T10's selected English and V4 provenance remain byte-for-byte unchanged. N05a restores the original first sentence “The thesis has several boundaries.” while deleting its defensive continuation. The other accepted selections remain unchanged. Fig6.2's complete figure environment is identical in the in-memory combined preview, and its actual image bytes remain unchanged.

## Source and context checks

- Hashed **58 frozen files** before/while preparation: previous v5 final/C1/evidence files, source chapters, main/authorship sources, old DECISIONS/SUPPLEMENTS, both candidate baseline PDFs and Fig6.2 image. Every recorded hash remains unchanged. Newly created R2 filenames are separate.
- All 20 selected original/source-insertion anchors uniquely match real current sources. No original replacement intervals overlap.
- Independently reconstructed the combined proposal **left to right**, without executing the writer script. All **44 operations** match their exact source intervals and named new text: 20 selected passages, 23 declared v4 dependencies and N07. No overlaps.
- Every one of the 20 `reinserted_context_r2` views is a unique contiguous excerpt of that independently reconstructed proposal, starts at a full paragraph boundary, and contains its selected text once (or implements the exact deletion). N01/N02/N03 carry the same complete metric subsection, including N07.
- Independently source-checked the 19 clause-level named carry-forwards requested by the evaluator: eight Intro definition changes, S3/scope pair, four listening comparator/reference-similarity synchronisations, five Ch6 causal-language actions. All source originals uniquely match; all are represented in the combined preview. The declared 23 dependencies additionally include the already proposed motivation/S1 synchronisations; their origins and unapproved status are explicit.
- N07 matches the previously checked table proposal exactly. Numeric-token sequence is unchanged, including reported 0.193; no rounding-based recomputation occurred. The cross-metric best/second-best wrappers are removed in the preview.

## Version and status checks

The three required R2 files (`FINAL_SELECTION_R2.json`, `CANDIDATE_PACKET_R2_FULL_CONTEXT.md`, `WRITER_REVISION_RESPONSE_R2.md`) have identical local/shared bytes. The context packet says explicitly that this is a proposal preview assuming 20 selections + N07 + 23 named v4 dependencies; it does not claim all 43 reviewer items were implemented or finally harmonised. Response and reader input preserve pending external cycle 2, pending author approval, unresolved formal PDF baseline and fact/provenance checks. Internal and external review counts remain separate.

No remaining integrity blocker found. The external reviewer still needs to assess the R2 text; author facts and final implementation remain pending.

## Reproducible evidence

`frozen_before_r2.json`; `check_r2.py` / `r2_check_results.json`; `check_sync_sources.py` / `named_v4_sync_sources.json`; `check_r2_context.py` / `r2_context_results.json`. All scripts read protected sources and write only this integrity directory. No thesis, old decisions, frozen candidate or shared proposal file was edited by this check.
