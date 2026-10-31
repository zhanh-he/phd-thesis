# Final reviewed-v5 integration integrity

**PASS.** This was a bounded integrity check of the two already reviewed integration repairs, not a third editorial review. No thesis source, proposal text, earlier decision or frozen review file was edited by this check.

## Exact adoption

- All **20 selected English SHA-256 hashes** match `evaluator_cycle2_verdict.json`; their selected text is unchanged from accepted R2.
- The corrected dependencies preserve the evaluator's exact `id/file/line/old/new` fields. The only artifact-level difference is the **status metadata** for all 23 dependencies, now recording writer/evaluator agreement for author choice while explicitly remaining author-unapproved and unimplemented. No replacement English or source mapping differs.
- `N07_TABLE_MARKUP_REVIEWED_v5.tex` is **byte-for-byte identical** to the external evaluator's corrected table artifact. The shared GT–Flat upward arrow is removed; the **58 numeric tokens remain identical and in order**, including reported 0.193.
- Compared the final operation manifest with frozen R2: exactly **V4-R2-04-sync-3 and N07** changed. The former expands the original range to consume “Supported by listening tests,” and uses the accepted “It…” replacement. There are still **44 operations and zero overlaps**.

## Independent reconstruction and protection

Reconstructed the combined proposal left to right from the real, unchanged source text, independently of the writer script. All eight virtual document hashes match the external evaluator's corrected-overlay hashes. The actual final operation manifest exactly matches this independent reconstruction.

Every one of the 20 `reinserted_context_final` excerpts is uniquely contiguous in the corrected overlay, starts at a full paragraph boundary, and contains the exact selected passage once or its precise deletion. The final Markdown packet contains all 20 exact contexts. The metric contexts include the corrected table; the roadmap context includes the corrected full sentence.

All **86 pre-recorded frozen files** remain hash-identical: C1/prior finals, shared and local R2 files, source/decision records and protected source assets. The eight real source hashes also match the external review's source provenance. No baseline selection or author fact has been inferred.

## Reader-input bindings

The delivery manifest's 12 file hashes match actual bytes. The reader packet's hash matches both its delivery manifest and the writer's declared `9496ad5e…f3c4c17` hash.

All six reader-input cards use the final selection and `reinserted_context_final`; recommended English and contexts match exactly, and original/follow-through quotations occur in the real sources. The N01 card correctly binds N01/N02/N03 plus corrected N07 and N04 as the five-range consistency group. N05b/c remain independent optional passages and are absent from N05a's automatic follow-through. KEEP-FIG62 remains a source-backed KEEP. Author approval and source implementation remain false.

**No integration blocker remains.** Final reader UI/interaction testing is the integrator's separate task; this report certifies its data bindings, not its rendered UI. Formal submitted baseline, run/table/checkpoint provenance, guitar GT and other fact-pending items remain unresolved as documented.

## Reproducible evidence

- `frozen_before_final.json`: 86 protected-file hashes.
- `expected_repairs_precheck.json`: independent exact-artifact overlay precheck.
- `check_final_reviewed.py` / `final_check_results.json`: selected hashes, exact source operations, table tokens, protected files and full contexts.
- `check_final_bindings.py` / `final_binding_results.json`: final manifest, reader-input and five-range/optional-choice bindings.

All checker output is confined to this `final_integrity` directory.
