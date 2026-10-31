# Checks actually run

Read `source_independent.md` first for editorial findings; `grs_audit.md` for the later GRS check. This folder contains supporting evidence, not another author decision form.

- `check_sources.py` hashes seven current chapter files and records case-insensitive raw-source term matches. `source_checks.json` contains exact matched lines. Results: 13 lines with renderer-conditioned, 14 structural-preservation pattern matches, 5 controlled/constrained-setting phrase matches, and 8 image-colourisation phrase matches. These are lexical counts, not quality verdicts.
- `prose_diagnostics.py` screens prose-like source lines for sentences of at least 45 approximate words. Eight sentences were flagged; `prose_diagnostics.json` gives exact anchors. Formula-containing sentences yield noisy counts. Ch5:409 is a 59-word semicolon list that is coherent in its summary context: **KEEP unless a separate scope/factual concern justifies revision**. Ch5:58 is architecture specification, where definitions account for much of the length; do not compress away the dimensions. Thus the check prevented cosmetic edits rather than requiring them.
- The same script extracts GRS English blockquotes and screens for completed-revision claims. 48 quote blocks, 43 item headings, zero such regex flags; every extracted block then manually read. `grs_status_checks.json` records them. Unknown run facts remain unknown.
- Installed-tool probe: system Python has none of textstat, language_tool_python, pypdf, pdfplumber, spacy, nltk, pylatexenc; shell PATH has none of Vale, LanguageTool, detex, latexdiff, pdftotext, pdfinfo. Python, Git and Java are present. Bundled workspace-dependency lookup returned “Workspace dependency tools are only supported for local threads”. No packages installed, no unknown-source code run, and no external API or thesis upload used.

## How tool findings affect recommendations

1. Exact-anchor verification corrected two scratch-note line references (Intro:62 and :153); `quote_checks.json` contains the current actual source anchors. Local term search identifies the Intro's “universal loudness variable” for repair against the thesis's own more precise Ch2/6 statements. Avoid adding duplicate renderer caveats.
2. Repeated controlled-setting hits identify every local synchronisation point for replacing an ambiguous epistemic ranking with direct input/structure conditions.
3. Sentence-length screening does not expose a general readability crisis. It supports narrow editing, keeping meaningful technical lists intact.
4. GRS screening credits existing proposal/completion separation, while preserving fact blockers and preventing premature finalisation.

Re-run from the task workspace: `python3 tool_checks/check_sources.py` then `python3 tool_checks/prose_diagnostics.py`. The scripts read thesis only and write this evidence directory. Source LaTeX is never changed.
