# Independent QA fixes

The independent review found real edge cases in the earlier frozen implementation. These fixes retain the operation ledger and personal text; they do not change thesis files. The final browser report records the exact built-entry SHA256 tested.

| Finding | Earlier behavior | Final behavior and regression evidence |
| --- | --- | --- |
| Q01: storage keys removed or corrupted | Cached persistence flags could still claim saved; reopen lost the deleted record. | Refresh reconciles actual valid keys. Missing/corrupt records become unsaved while memory retains text. The visible retry action restores missing keys; corrupt bytes are durably archived before explicit repair. Unit tests and real-browser deletion/corruption/reopen tests cover both paths. |
| Q02: asynchronous connected-file overwrite | An older write could close last and replace a newer portable backup. | Removed in-place connected-file writes and their UI/docs. Every ordinary backup is a separate timestamped download; there is no asynchronous overwrite handler. Browser regression verifies those controls and APIs are absent. |
| Q03: execution claims carried to a new proposal | An old `verified` state appeared current after the proposal changed. | Execution and verification bind to the source/proposal revision and actual-text operation head. Old records/text remain intact, but current execution becomes unconfirmed with a visible warning. Tests change both the proposed version and actual text, then check the report. |
| Q04: empty pending text mistaken for deletion | Empty verification text could say “delete this range.” | Only explicit `delete`/`deletion` operations present deletion. Missing/empty evidence-pending drafts show a request for records and no replacement. Synthetic regressions check pending versus explicit deletion; native R1-30 has no invented draft. |
| Q05: legitimate large backup rejected on import | Repeated current-value snapshots exceeded the metadata value limit. | Source context is static; personal text/history live in operations. Metadata has a separate larger bound, and unsupported aggregate export fails visibly. The exact 2 MiB / legacy >8 MiB repro now round-trips. |
| Q06: text interpreted as decision labels | Literal `keep`, `modify`, `pending`, or `constructor` could be changed in history/conflicts. | Label conversion applies only to decision fields and own dictionary keys. Literal-note history regression preserves those strings. |
| Q07: rejected large input still looked saved | Validation could throw while the textarea showed text absent from the ledger. | Input validation is caught. Exact rejected text stays in a marked memory draft, appears in backup, and has a visible rescue-download action. A real 9 MiB input, navigation, backup/import and later valid correction are tested. |
| Q08: future operation `encoding` collided with internal storage | Import succeeded but reopen could lose the field. | Internal storage uses an unambiguous versioned envelope; raw legacy operations and old deltas remain readable. Unknown fields survive export/import/reopen. Original independent Node reproductions now show zero reproduced bugs. |
| Q09: second manuscript used thesis identities | Labels/counts were hardcoded. | Reviewer identity/order/count and manuscript metadata come from data. A second manuscript with a different reviewer structure and overlapping comment IDs stays isolated; foreign imports reject atomically. |

Author-intent recheck is separate: R1-21 visibly records the scoped “do not expand the current project” decision while its manuscript-text decision remains pending. R1-20/24/29/36 retain their qualified stances. Original PDF reply provenance remains available; no whole-item no-change decision was fabricated.

Supporting files: `browser_validation.json`, `browser-r1-05/21/30/35*.png` and `.txt`, `../tests/ledger.test.cjs`, `../tests/browser.mjs`, and `../tests/test_build.py`. Screenshots/text use the native source-seeded page, with personal note fields empty. All browser tests use isolated temporary profiles.

## Post-freeze consistency reminder

Source QA requested one plain reminder linking the Chapter 2 background, three Chapter 6 interpretations and the table marks. The new optional data group and same-page jumps preserve all existing comment objects, candidates, English text and independent choices byte-for-byte. The browser report/screenshots retain their original tested-entry hash; this small post-freeze update has static source/target validation only while parent independent review is pending. The source QA file-protocol navigation denial was not retried or bypassed.

## NEW01: atomic draft preflight

The file-input handler now validates the complete known draft container/rows and prepares both draft stores before calling `ledger.importJSON`. A malformed object container, `[null]`, or a later invalid row rejects with zero ledger calls, zero storage writes and unchanged ledger/draft state. Valid unknown fields/extensions and conflicting drafts remain intact. The new `import-preflight.test.cjs` executes the actual helper, file-input handler and export function: 31 targeted Node checks pass. Evidence: `import_preflight.json`. No browser navigation was attempted for this targeted fix; parent bounded independent import checks are pending.
