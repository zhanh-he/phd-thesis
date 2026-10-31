#!/usr/bin/env python3
"""Read-only verification of the complete thesis delivery after a Git checkout.

Place this file beside source_manifest.json in delivery_sync_20261031/.
Historical absolute paths in archived evidence are preserved, not executed.
Only --report writes a file; the thesis, reader and decision records are untouched.
"""
import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WORK = "revision_workshop_20261031_v5"
READER = WORK + "/reader"
EXPECTED = {
    WORK + "/READER_PACKET_REVIEWED_v5.json":
        "9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17",
    READER + "/index.html":
        "d7fc933840be7049f0d17cc472568b2584a1a01fef7965c0e4f8da5115148f37",
}
PATH_KEYS = {
    "sourceFile", "decisionPath", "reviewFile", "candidateFile", "commentFile",
    "originalImage", "recommendationSource", "writerFile", "externalCycle1",
    "externalCycle2", "verdict", "externalReviewFile", "writerAgreementFile",
    "contextDependenciesFile", "finalSelectionFile", "overviewSource", "path",
    "file", "legacyReference", "candidateEvidenceByOption",
}
PROJECT_PREFIXES = ("Chapter_", "revision_", "main.tex")


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_file(relative):
    """Return an existing regular file inside this checkout, without traversal."""
    if not isinstance(relative, str) or not relative:
        raise ValueError("Empty/non-string path")
    plain = relative.split("#", 1)[0]
    p = PurePosixPath(plain)
    if p.is_absolute() or ".." in p.parts or ".git" in p.parts:
        raise ValueError("Unsafe repository path: " + relative)
    target = (ROOT / plain).resolve()
    if not target.is_relative_to(ROOT) or not target.is_file():
        raise ValueError("Missing/outside checkout: " + relative)
    return target


class ReaderHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.packet_parts = []
        self.capture_packet = False
        self.packet_count = 0
        self.references = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "script" and attributes.get("id") == "packet":
            self.capture_packet = True
            self.packet_count += 1
        for key in ("href", "src"):
            if attributes.get(key):
                self.references.append(attributes[key])

    def handle_endtag(self, tag):
        if tag == "script":
            self.capture_packet = False

    def handle_data(self, data):
        if self.capture_packet:
            self.packet_parts.append(data)


def packet_references(value):
    found = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in PATH_KEYS and isinstance(child, str):
                if child.startswith(PROJECT_PREFIXES):
                    found.add(child)
            found.update(packet_references(child))
    elif isinstance(value, list):
        for child in value:
            found.update(packet_references(child))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path,
                        help="Optionally write the same JSON report to this path")
    args = parser.parse_args()
    errors = []
    excluded_paths = set()
    report = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(ROOT),
        "read_only": True,
        "manifest": {},
        "delivery_manifest": {"present": False},
        "exact_reviewed_hashes": [],
        "readers": [],
        "exclusions": [],
        "errors": errors,
    }

    try:
        manifest = json.loads((HERE / "source_manifest.json").read_text())
        rows = manifest["files"]
        exclusions = manifest.get("exclusions", [])
        if not isinstance(rows, list) or not rows:
            raise ValueError("Manifest files must be a nonempty list")
        paths = set()
        verified_bytes = 0
        verified_files = 0
        for row in rows:
            name = row.get("path")
            try:
                if name in paths:
                    raise ValueError("Duplicate included path")
                paths.add(name)
                path = safe_file(name)
                size = path.stat().st_size
                if size != row["bytes"]:
                    raise ValueError("Byte count differs")
                if sha256(path) != row["sha256"]:
                    raise ValueError("SHA256 differs")
                verified_files += 1
                verified_bytes += size
            except (KeyError, OSError, TypeError, ValueError) as exc:
                errors.append({"check": "source_file", "path": name, "error": str(exc)})
        excluded_paths = set()
        for row in exclusions:
            name = row.get("path")
            reason = row.get("reason")
            if (not isinstance(name, str) or name in excluded_paths or name in paths
                    or not isinstance(reason, str) or not reason.strip()):
                errors.append({"check": "exclusion", "path": name,
                               "error": "Invalid, duplicate, overlapping or unexplained exclusion"})
            excluded_paths.add(name)
            report["exclusions"].append({
                "path": name, "reason": reason, "bytes": row.get("bytes"),
            })
        report["manifest"] = {
            "source_head": manifest.get("source_head"),
            "source_generated_utc": manifest.get("generated_utc"),
            "included_files": len(rows),
            "included_bytes": sum(row.get("bytes", 0) for row in rows),
            "verified_files": verified_files,
            "verified_bytes": verified_bytes,
            "excluded_files": len(exclusions),
            "excluded_bytes": sum(row.get("bytes", 0) for row in exclusions),
            "total_source_inventory_files": len(rows) + len(exclusions),
        }
    except (KeyError, OSError, TypeError, ValueError) as exc:
        errors.append({"check": "source_manifest", "error": str(exc)})

    delivery_manifest = HERE / "delivery_manifest.json"
    if delivery_manifest.exists():
        try:
            delivery = json.loads(delivery_manifest.read_text())
            delivery_rows = delivery["files"]
            declared = set()
            verified_bytes = 0
            for row in delivery_rows:
                name = row["path"]
                if name in declared:
                    raise ValueError("Duplicate delivery path: " + name)
                declared.add(name)
                target = safe_file(name)
                if target.stat().st_size != row["bytes"] or sha256(target) != row["sha256"]:
                    raise ValueError("Delivery bytes/hash differ: " + name)
                verified_bytes += target.stat().st_size
            observed = set()
            for parent, directories, leaves in os.walk(ROOT):
                directories[:] = [item for item in directories if item != ".git"]
                for leaf in leaves:
                    path = Path(parent) / leaf
                    if path == delivery_manifest:
                        continue
                    relative = path.relative_to(ROOT).as_posix()
                    if relative not in excluded_paths:
                        observed.add(relative)
            if declared != observed:
                raise ValueError("Delivery coverage differs: " + json.dumps({
                    "undeclared_files": sorted(observed - declared),
                    "declared_but_not_observed": sorted(declared - observed),
                }, ensure_ascii=False))
            report["delivery_manifest"] = {"present": True, "passed": True,
                "files_verified": len(declared), "bytes_verified": verified_bytes,
                "all_non_git_files_covered_except_explicit_source_exclusions": True,
                "self_manifest_excluded": delivery_manifest.relative_to(ROOT).as_posix()}
        except (KeyError, OSError, TypeError, ValueError) as exc:
            report["delivery_manifest"] = {"present": True, "passed": False}
            errors.append({"check": "delivery_manifest", "error": str(exc)})

    for name, expected in EXPECTED.items():
        try:
            actual = sha256(safe_file(name))
            ok = actual == expected
            report["exact_reviewed_hashes"].append({"path": name, "sha256": actual,
                                                     "matches": ok})
            if not ok:
                errors.append({"check": "reviewed_hash", "path": name,
                               "error": "Exact reviewed bytes changed"})
        except (OSError, ValueError) as exc:
            errors.append({"check": "reviewed_hash", "path": name, "error": str(exc)})

    for leaf in ("index.html", "legacy_v3_v4.html", "provisional.html", "provisional_r2.html"):
        name = READER + "/" + leaf
        summary = {"path": name}
        report["readers"].append(summary)
        try:
            html_path = safe_file(name)
            html = html_path.read_text()
            parsed = ReaderHTML()
            parsed.feed(html)
            parsed.close()
            if parsed.packet_count != 1:
                raise ValueError("Expected exactly one embedded packet")
            packet = json.loads("".join(parsed.packet_parts))
            references = packet_references(packet)
            for relative in references:
                safe_file(relative)
            literal_count = 0
            for raw in parsed.references:
                url = urlsplit(raw)
                if url.scheme or url.netloc:
                    if url.scheme == "data":
                        continue
                    raise ValueError("Nonportable/external literal reference: " + raw)
                if not url.path:
                    continue
                target = (html_path.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.is_file():
                    raise ValueError("Missing/outside literal reference: " + raw)
                literal_count += 1
            provenance = packet.get("provenance", [])
            for row in provenance:
                if sha256(safe_file(row["path"])) != row["sha256"]:
                    raise ValueError("Reader provenance mismatch: " + row["path"])
            if "/Users/" in html:
                raise ValueError("Reader contains an absolute Mac user path")
            summary.update({"embedded_project_references": len(references),
                            "literal_file_references": literal_count,
                            "provenance_hashes_verified": len(provenance),
                            "absolute_user_paths": 0, "passed": True})
            if leaf == "index.html":
                if re.search(r"(?:fetch\(|XMLHttpRequest|localStorage|sessionStorage|indexedDB|<form\b)", html):
                    raise ValueError("Main reader contains network/persistent-state/form code")
                if packet.get("packetStatus") != "jointly-reviewed-v5":
                    raise ValueError("Main reader has wrong proposal version status")
                agreement = packet.get("reviewAgreement", {})
                if agreement.get("authorApproval") is not False or agreement.get("sourceImplementation") is not False:
                    raise ValueError("Reader no longer states proposals are unapproved/unimplemented")
                summary["network_or_persistent_state_code"] = False
        except (KeyError, OSError, TypeError, ValueError) as exc:
            summary["passed"] = False
            errors.append({"check": "reader", "path": name, "error": str(exc)})

    report["passed"] = not errors
    report["historical_absolute_paths"] = "Archived logs/manifests retain original paths; they are not executed by this verifier."
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.write_text(output)
    sys.stdout.write(output)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
