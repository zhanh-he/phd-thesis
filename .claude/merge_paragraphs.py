#!/usr/bin/env python3
"""Merge soft line breaks inside LaTeX prose paragraphs.

Rules:
- Blank lines separate paragraphs and are preserved.
- Lines that start a structural macro (chapter/section/etc., \\begin, \\end,
  \\label, \\caption, \\includegraphics, table rules, \\paragraph, etc.) are
  preserved on their own line.
- Lines inside math/table/figure/list environments are preserved as-is.
- Comment lines (% ...) and lines ending with \\\\ (tabular row terminator)
  are preserved.
- All other consecutive prose lines are joined with single spaces.
"""

import re
import sys
from pathlib import Path

PRESERVED_ENVS = {
    "equation", "equation*", "align", "align*", "eqnarray", "eqnarray*",
    "gather", "gather*", "multline", "multline*", "aligned", "cases",
    "array", "tabular", "tabular*", "tabularx", "longtable",
    "figure", "figure*", "table", "table*", "subequations",
    "itemize", "enumerate", "description", "matrix", "pmatrix", "bmatrix",
    "verbatim", "lstlisting", "minted",
}

STRUCTURAL_PATTERNS = [
    r"\\chapter\b", r"\\section\b", r"\\subsection\b", r"\\subsubsection\b",
    r"\\paragraph\{", r"\\subparagraph\{",
    r"\\label\{", r"\\caption\b", r"\\includegraphics\b", r"\\centering\b",
    r"\\toprule\b", r"\\midrule\b", r"\\bottomrule\b", r"\\cmidrule\b",
    r"\\hline\b", r"\\multicolumn\b", r"\\multirow\b",
    r"\\fontsize\b", r"\\setlength\b", r"\\renewcommand\b", r"\\newcommand\b",
    r"\\definecolor\b", r"\\arrayrulewidth\b", r"\\arraystretch\b",
    r"\\newcolumntype\b", r"\\vskip\b", r"\\vspace\b", r"\\hspace\b",
    r"\\noindent\b", r"\\item\b", r"\\footnote\{",
    r"\\\[", r"\\\]",
]
STRUCTURAL_RE = re.compile(r"^\s*(?:" + "|".join(STRUCTURAL_PATTERNS) + r")")

BEGIN_RE = re.compile(r"^\s*\\begin\{([^}]+)\}")
END_RE = re.compile(r"^\s*\\end\{([^}]+)\}")


def process(text: str) -> str:
    lines = text.split("\n")
    output = []
    buf = []
    env_stack = []

    def flush():
        if buf:
            output.append(" ".join(buf).rstrip())
            buf.clear()

    for line in lines:
        stripped = line.strip()

        m = BEGIN_RE.match(line)
        if m:
            flush()
            output.append(line.rstrip())
            env_stack.append(m.group(1).rstrip("*"))
            continue

        m = END_RE.match(line)
        if m:
            flush()
            output.append(line.rstrip())
            if env_stack and env_stack[-1] == m.group(1).rstrip("*"):
                env_stack.pop()
            continue

        in_preserved = any(e in PRESERVED_ENVS for e in env_stack)
        if in_preserved:
            flush()
            output.append(line.rstrip())
            continue

        if not stripped:
            flush()
            output.append("")
            continue

        if stripped.startswith("%"):
            flush()
            output.append(line.rstrip())
            continue

        if STRUCTURAL_RE.match(line):
            flush()
            output.append(line.rstrip())
            continue

        if stripped.endswith("\\\\"):
            flush()
            output.append(line.rstrip())
            continue

        buf.append(stripped)

    flush()
    return "\n".join(output)


def main():
    if len(sys.argv) < 2:
        print("usage: merge_paragraphs.py <file.tex> [<file.tex> ...]")
        sys.exit(1)
    for path in sys.argv[1:]:
        p = Path(path)
        original = p.read_text(encoding="utf-8")
        processed = process(original)
        if processed != original:
            p.write_text(processed, encoding="utf-8")
            print(f"updated: {path}")
        else:
            print(f"no change: {path}")


if __name__ == "__main__":
    main()
