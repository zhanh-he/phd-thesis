#!/usr/bin/env python3
"""Verify protected source hashes and source-grounded workbench locations.

Only Python's standard library is required. This script is read-only; it never
updates the baseline, repairs source text, or infers an author's decision.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent.parent
BASELINE = Path(__file__).with_name("source_baseline.json")
INTENTIONAL_DOCUMENTATION = {"README.md", ".gitignore"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_source(value: str) -> Path:
    p = PurePosixPath(value)
    if p.is_absolute() or ".." in p.parts or "\\" in value:
        raise ValueError(f"unsafe relative source path: {value!r}")
    result = (ROOT / p).resolve()
    if not result.is_relative_to(ROOT):
        raise ValueError(f"source escapes repository: {value!r}")
    return result


def verify_baseline() -> tuple[list[str], int, list[str]]:
    manifest = json.loads(BASELINE.read_text(encoding="utf-8"))
    errors = []
    documentation_changes = []
    for relative, expected in manifest["sha256"].items():
        path = safe_source(relative)
        if not path.is_file():
            errors.append(f"Protected file missing: {relative}")
        elif sha256(path) != expected and relative in INTENTIONAL_DOCUMENTATION:
            documentation_changes.append(relative)
        elif sha256(path) != expected:
            errors.append(f"Protected file changed: {relative}")
    return errors, len(manifest["sha256"]), documentation_changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path,
                        help="Optional workbench seed dataset to validate")
    parser.add_argument("--allow-fixture", action="store_true",
                        help="Allow synthetic UI fixture content; never use for delivery validation")
    args = parser.parse_args()
    errors, count, documentation_changes = verify_baseline()
    summary = {"protectedFiles": count, "protectedFilesUnchanged": not errors,
               "intentionalDocumentationChanges": documentation_changes,
               "errors": errors}
    if args.data:
        summary.update(verify_dataset(args.data, errors, args.allow_fixture))
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return int(bool(errors))


def verify_dataset(path: Path, errors: list[str], allow_fixture: bool = False) -> dict:
    """Normalized UI schema: comments[] with locations[].

    The data must retain reviewer order. All locations must identify a current
    repository text range and an exact, searchable original quote. A non-text
    asset should instead be linked from its enclosing LaTeX location.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    fixture = "fixture" in str(data.get("edition", "")).lower() or any(
        "fixture" in str(c.get("candidateVersion", "")).lower()
        or "测试夹具" in str(c.get("title", ""))
        for c in data.get("comments", []))
    if fixture and not allow_fixture:
        errors.append("Synthetic UI fixture dataset is not valid delivery evidence; replace it with audited source data")
    native_path = ROOT / "revision_workbench/evidence/author_decision_evidence.json"
    native = {}
    native_items = {}
    native_reports = {}
    if native_path.is_file():
        native = json.loads(native_path.read_text(encoding="utf-8"))
        native_items = {item["id"]: item for item in native.get("items", [])}
        native_reports = {report["source_pdf"]: report for report in native.get("reports", [])}
        status = str(native.get("audit_status", ""))
        if not fixture and (not re.search(r"complete|verified|ready", status, re.I)
                            or re.search(r"assembling|pending|incomplete", status, re.I)):
            errors.append(f"Native source audit is not final: audit_status={status!r}")
        if not fixture and any(item.get("locations_complete") is not True for item in native_items.values()):
            errors.append("Native source audit contains incomplete location maps")
    elif not fixture:
        errors.append("Missing copied native author-decision audit evidence")

    def normalized(value: str) -> str:
        return " ".join(unicodedata.normalize("NFKC", value).split())
    comments = data.get("comments", [])
    expected = [f"R1-{n:02d}" for n in range(1, 39)] + [f"R2-{n:02d}" for n in range(1, 6)]
    actual = [c.get("id") for c in comments]
    if actual != expected:
        errors.append("Comment IDs/order must be exactly R1-01…R1-38, then R2-01…R2-05")
    sources = data.get("sources", {})
    embedded_sources_checked = 0
    for relative, embedded in sources.items():
        try:
            source = safe_source(relative)
            source_bytes = source.read_bytes()
            source_text = source_bytes.decode("utf-8")
            if source_text != embedded["text"]:
                errors.append(f"Embedded source text differs: {relative}")
            if hashlib.sha256(source_bytes).hexdigest() != embedded["sha256"]:
                errors.append(f"Embedded source hash differs: {relative}")
            embedded_sources_checked += 1
        except (KeyError, OSError, ValueError, TypeError, UnicodeError) as exc:
            errors.append(f"Embedded source {relative}: {exc}")
    locations_checked = 0
    quote_checks = 0
    pdf_reply_checks = 0
    for comment in comments:
        cid = comment.get("id", "<missing ID>")
        for key in ("original", "meaning", "title", "candidateVersion"):
            if not isinstance(comment.get(key), str) or not comment[key].strip():
                errors.append(f"{cid}: missing/blank {key}")
        expected_reviewer = cid.split("-", 1)[0] if isinstance(cid, str) else None
        if comment.get("reviewer") != expected_reviewer:
            errors.append(f"{cid}: reviewer does not match stable ID")
        report = comment.get("report", {})
        try:
            if not safe_source(report["path"]).is_file():
                errors.append(f"{cid}: report source does not exist")
            if report.get("page") is not None and (not isinstance(report["page"], int) or report["page"] < 1):
                errors.append(f"{cid}: invalid report PDF page number")
        except (KeyError, OSError, ValueError, TypeError) as exc:
            errors.append(f"{cid}: report provenance {exc}")
        locations = comment.get("locations", [])
        if not locations:
            errors.append(f"{cid}: no source locations")
        for i, loc in enumerate(locations):
            label = f"{cid} location {i + 1}"
            try:
                relative = loc["file"]
                source = safe_source(relative)
                text = source.read_text(encoding="utf-8")
                start = loc["lineStart"]
                end = loc["lineEnd"]
                lines = text.splitlines(keepends=True)
                if not (isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines)):
                    raise ValueError(f"invalid line range {start!r}–{end!r}")
                span = "".join(lines[start - 1:end])
                quote = loc["quote"]
                if not isinstance(quote, str) or not quote:
                    raise ValueError("missing exact searchable source quote")
                if quote not in span:
                    errors.append(f"{label}: quote does not occur in declared source lines ({relative}:{start}–{end})")
                else:
                    quote_checks += 1
                expected_hash = loc.get("sourceSha256")
                if expected_hash and hashlib.sha256(source.read_bytes()).hexdigest() != expected_hash:
                    errors.append(f"{label}: sourceSha256 differs from current source")
                if not loc.get("operation"):
                    errors.append(f"{label}: missing operation")
                if not loc.get("section"):
                    errors.append(f"{label}: missing chapter/section")
                for context in ("before", "after"):
                    if context not in loc or not isinstance(loc[context], str):
                        errors.append(f"{label}: missing {context} context field")
                    elif loc[context] and loc[context] not in text:
                        errors.append(f"{label}: {context} context differs from current source")
                if relative not in sources:
                    errors.append(f"{label}: contextual source not embedded in data.sources")
                locations_checked += 1
            except (KeyError, OSError, ValueError, TypeError, UnicodeError) as exc:
                errors.append(f"{label}: {exc}")
        reply = comment.get("authorReply", {})
        if reply.get("decision") not in {"modify", "keep", "pending"}:
            errors.append(f"{cid}: missing/invalid author tri-state")
        if comment.get("assistant", {}).get("decision") not in {"modify", "keep", "pending"}:
            errors.append(f"{cid}: missing/invalid assistant tri-state")
        if reply.get("decision") != "pending" and not (reply.get("prefill") and reply.get("text") and reply.get("sources")):
            errors.append(f"{cid}: explicit author prefill has no reply text/provenance")
        native_item = native_items.get(cid)
        if not fixture and native_item:
            seed = {"no_modify": "keep", "modify": "modify", "pending": "pending"}.get(native_item.get("author_decision_seed"))
            if reply.get("decision") != seed:
                errors.append(f"{cid}: normalized author decision differs from native audited seed")
            if bool(reply.get("prefill")) != (seed in {"modify", "keep"}):
                errors.append(f"{cid}: author prefill marker differs from native audited intent")
            native_original = native_item.get("reviewer_comment", {}).get("text", "")
            if normalized(comment.get("original", "")) != normalized(native_original):
                errors.append(f"{cid}: reviewer original differs from native audited report text")
            native_quotes = native_item.get("author_reply_exact", [])
            if any(quote not in reply.get("text", "") for quote in native_quotes):
                errors.append(f"{cid}: author reply omits or changes an exact native annotation")
            if native_quotes and reply.get("text") != "\n\n".join(native_quotes):
                errors.append(f"{cid}: author reply must contain only the exact native annotations joined by blank lines")
            for actual_reply in native_item.get("author_prefill_evidence", {}).get("actual_replies", []):
                if not any(ref.get("annotationId") == actual_reply.get("annotation_id")
                           and ref.get("pdfPage") == actual_reply.get("pdf_page")
                           and ref.get("quote") == actual_reply.get("exact_quote")
                           for ref in reply.get("sources", [])):
                    errors.append(f"{cid}: missing provenance for a native author annotation")
        elif not fixture:
            errors.append(f"{cid}: missing native audited item")
        for i, ref in enumerate(reply.get("sources", [])):
            try:
                relative = ref["path"]
                source = safe_source(relative)
                if source.suffix.lower() == ".pdf":
                    expected_report = native_reports.get(relative)
                    if not expected_report:
                        raise ValueError("PDF provenance not found in copied native audit reports")
                    if relative != (native_item or {}).get("reviewer_comment", {}).get("report_pdf"):
                        raise ValueError("PDF reply provenance points to the wrong reviewer's report")
                    actual_hash = sha256(source)
                    if ref.get("pdfSha256") != actual_hash or expected_report.get("sha256") != actual_hash:
                        raise ValueError("PDF SHA256 differs from provenance or native audit")
                    native_reply = (native_item or {}).get("author_prefill_evidence", {}).get("actual_replies", [])
                    matched = [r for r in native_reply if r.get("annotation_id") == ref.get("annotationId")
                               and r.get("pdf_page") == ref.get("pdfPage")
                               and r.get("exact_quote") == ref.get("quote")]
                    if len(matched) != 1:
                        raise ValueError("PDF annotation ID/page/exact quote does not match native audited author reply")
                    pdf_reply_checks += 1
                    continue
                lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
                start, end = ref["lineStart"], ref["lineEnd"]
                if not (isinstance(start, int) and isinstance(end, int) and 1 <= start <= end <= len(lines)):
                    raise ValueError("invalid reply provenance line range")
                if ref["quote"] not in "".join(lines[start-1:end]):
                    errors.append(f"{cid} reply provenance {i+1}: quote differs from source lines")
            except (KeyError, OSError, ValueError, TypeError, UnicodeError) as exc:
                errors.append(f"{cid} reply provenance {i+1}: {exc}")
    return {"dataset": str(path), "comments": len(comments),
            "syntheticFixture": fixture,
            "nativeAuditStatus": native.get("audit_status"), "nativePdfReplyChecks": pdf_reply_checks,
            "embeddedSourcesChecked": embedded_sources_checked,
            "locationsChecked": locations_checked, "exactQuoteChecks": quote_checks}


if __name__ == "__main__":
    sys.exit(main())
