# Independent QA · PASS

Tested runtime commit: `cd67b582c16647f127f22aee651d236d5cf905ef`.

Tested `START_HERE.html` SHA256: `da8cfb2d653a802903b770010874ff649bfc13b85be1719b06954f96813ae19e`.

This is a portable summary of completed independent checks, not a new validation cycle. [Aggregate and case results](INDEPENDENT_QA_FINAL.json) contain no browser profiles, full backups, private author entries or machine-specific paths.

## Final bounded regression: 6 passed, 0 failed

The actual application file-import handler, its complete preflight, and the actual ledger were exercised with synthetic DOM and in-memory storage. These are runtime checks, **not a current-commit browser rerun**.

| Case | Result |
| --- | --- |
| Malformed draft container object | Rejects before any ledger import, storage write or state change. |
| Null draft row | Rejects before any ledger import, storage write or state change. |
| Valid draft followed by invalid row | Rejects the complete input atomically. |
| Valid prepared draft with invalid ledger | No partial operation or draft commit. |
| Multiline LaTeX, conflicts, unknown IDs/fields and nested extensions | Exact import/export/import retention; unsaved drafts remain distinct from saved operations. |
| Import without draft data | Existing unsaved drafts preserved. |

Rejection messages match the outcome and the original input remains available for recovery. The earlier `NEW01` partial-import defect is fixed. Bounded static review also confirmed that the ledger is unchanged from the preceding snapshot, and the app/ledger embedded in the entry match their modules. No remaining save-safety blocker was found within this regression scope.

## Earlier independent browser and source evidence

Original Q01–Q09 regressions passed on commit `e03bbee4d93d5f8493935bee0ddf4a61f5cc9b61`, entry SHA256 `4fe354d48f03741e8130862c85e5722dea3fdcdfeac589f1e9652fd6d00af5be`. Its independent browser run had 26 cases: 24 passed and two exposed the same `NEW01` malformed-draft defect subsequently fixed above. This historical result is not relabeled as a final-commit browser pass.

Those checks covered missing/corrupt saved keys and recovery, removal of connected-file writes, stale execution/verification records, evidence-pending empty proposals, large backup roundtrips, literal note preservation, oversized-input rescue, unknown fields and separate manuscript identities. Real browser checks also covered restart/reopen, exact multiline LaTeX, old-tab edits, simultaneous same-field edits released through a barrier, old-backup merges, and immediate close after native input.

Desktop/narrow readability evidence for R1-05, R1-21, R1-30 and R1-35 belongs to that earlier snapshot. The native manuscript had zero operations written during those read-only card checks.

The separate source-content audit verified 43 comments in original report order, Benetos first and the Auckland University professor second; author seeds were 9 modify, 0 whole-item keep and 34 pending. R1-21's explicit decision against expanding the project stays separate from the pending manuscript decision. The existing positions/preferences of R1-20/24/29/36 remain visible. The 192 default locations comprise 189 source locations and three image references; five alternate source locations remain in evidence. Evidence-pending protocol candidates are not treated as deletions.

The source auditor's fresh `file://` browser navigation was denied by protocol policy and was not retried or bypassed. That audit used source/data/evidence and frozen screenshot review; it is not counted as a successful new browser session. Its browser limit does not change the separately completed independent browser checks described above.

## Later consistency reminder: static review

The five linked metric explanations—Chapter 2 background, three Chapter 6 paragraphs and the table marking—now remind readers to check consistency together while keeping each edit independently chosen. This text/navigation change was reviewed statically at `7673cb69492d3de04692fedf6578ce1287d027b2` and included in the final bounded static conclusion. No broad browser rerun or new ledger-write behavior is claimed for that reminder.

Independent QA made no target or thesis edits, used no normal author/browser state, and performed no push or publication. No checks remain running. The final verdict applies to the tested snapshot and the stated scopes; later evidence-only commits do not change that runtime identity.
