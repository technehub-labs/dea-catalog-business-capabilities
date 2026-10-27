#!/usr/bin/env python3
"""check_doc_links.py: documentation-link gate (CR-DEA-BC-39 §6.1).

Validates that every relative href in every markdown file resolves to an
existing path. Catches the drift class where layout migrations (docs/research/
-> catalog-research/, visuals/ relocation, entity-dir renames, ../../ depth
errors) leave stale links behind.

Rules:
- DL-001 (blocking): a relative markdown href whose target path does not
  exist on disk.

Scope notes:
- Absolute/external targets (http://, https://, mailto:) and pure same-file
  anchors (#section) are out of scope; same-file heading anchors are not
  validated.
- Targets are URL-decoded before resolution; #fragments on file targets are
  stripped and the file part must exist.

Run: python3 scripts/check_doc_links.py [--strict] [--self-test]
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "node_modules", "__pycache__"}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def find_broken_links(root: Path) -> list[dict]:
    """Return a finding dict per broken relative href under root."""
    findings: list[dict] = []
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            findings.append({
                "rule": "DL-001",
                "file": str(path.relative_to(root)),
                "href": "<unreadable>",
                "diagnostic": f"could not read file: {exc}",
            })
            continue
        for m in LINK_RE.finditer(text):
            href = m.group(2)
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / urllib.parse.unquote(target)).resolve()
            if not resolved.exists():
                findings.append({
                    "rule": "DL-001",
                    "file": str(path.relative_to(root)),
                    "href": href,
                    "diagnostic": f"relative href target does not exist: {target}",
                })
    return findings


def self_test() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "docs").mkdir()
        (root / "docs" / "page.md").write_text(
            "[good](../README.md) and [bad](../missing.md) and [skip](https://x.y) "
            "and [anchor](#sec) and [frag](../README.md#sec)\n"
        )
        (root / "README.md").write_text("root\n")
        findings = find_broken_links(root)
        assert len(findings) == 1, findings
        assert findings[0]["href"] == "../missing.md", findings
    print("self-test PASS (1 case)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero on any finding (findings always exit non-zero)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the embedded self-test fixtures")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    findings = find_broken_links(REPO_ROOT)
    if findings:
        print(f"Documentation Links (CR-DEA-BC-39; DL-001): NON-CONFORMANT")
        for f in findings:
            print(f"  [DL-001] {f['file']}: [{f['href']}] {f['diagnostic']}")
        return 1
    print("Documentation Links (CR-DEA-BC-39; DL-001): CONFORMANT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
