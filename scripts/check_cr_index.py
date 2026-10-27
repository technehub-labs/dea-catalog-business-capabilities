#!/usr/bin/env python3
"""check_cr_index.py: CR-index discipline gate (CR-DEA-BC-39 §6.2).

Bidirectional consistency between change-requests/CR-*.md files and the
series index tables in change-requests/README.md. Catches the drift class
where CRs land without index rows, rows reference missing files, or table
rows are malformed (missing leading pipe).

Rules:
- CR-001 (blocking): a CR-*.md file in change-requests/ with no index row
  linking it.
- CR-002 (blocking): a row href that does not resolve to an existing file.
- CR-003 (blocking): a row whose displayed CR id differs from the target
  file's self-identified id (first heading, e.g. "# CR-DEA-BC-36: ...").
- CR-004 (blocking): a table row line inside a CR table block that does not
  start with "|" (malformed row; breaks table rendering).
- CR-005 (blocking): a row with no href at all (documented-gap rows must
  carry the marker "No standalone CR file" to be accepted).

Run: python3 scripts/check_cr_index.py [--strict] [--self-test]
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX = REPO_ROOT / "change-requests" / "README.md"
GAP_MARKER = "No standalone CR file"

ROW_CELL_RE = re.compile(r"^\|\s*(?:\[(CR-[A-Za-z0-9-]+)\]\(([^)]+)\)|\*\*(CR-[A-Za-z0-9-]+)\*\*|(CR-[A-Za-z0-9-]+))")
HEADING_ID_RE = re.compile(r"^\s*#*\s*(CR-[A-Z][A-Za-z0-9-]*[A-Za-z0-9])\s*:")
BARE_ROW_START_RE = re.compile(r"^CR-[A-Za-z0-9-]+\s*\|")


def file_self_id(path: Path) -> str | None:
    """The CR's self-identified id: first heading line of the document."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in text.splitlines()[:25]:
        m = HEADING_ID_RE.match(line)
        if m:
            return m.group(1)
    return None


def collect_rows(index_text: str) -> list[tuple[int, str, str | None, str | None]]:
    """Rows in CR tables: (line_no, displayed_id, href, line)."""
    rows: list[tuple[int, str, str | None, str | None]] = []
    lines = index_text.splitlines()
    in_cr_table = False
    for i, line in enumerate(lines, start=1):
        if line.startswith("|") and " CR " in line and "Status" in line:
            in_cr_table = True
            continue
        if in_cr_table:
            if not line.strip():
                in_cr_table = False
                continue
            m = ROW_CELL_RE.match(line) if line.startswith("|") else None
            if m:
                disp = m.group(1) or m.group(3) or m.group(4)
                rows.append((i, disp, m.group(2), line))
            elif BARE_ROW_START_RE.match(line):
                rows.append((i, "", None, line))  # malformed: no leading pipe
            elif line.startswith("|"):
                pass  # header underline / non-CR table row
            else:
                in_cr_table = False
    return rows


def evaluate(root: Path) -> list[dict]:
    findings: list[dict] = []
    root = root.resolve()
    index = root / "change-requests" / "README.md"
    if not index.is_file():
        return [{"rule": "CR-002", "file": "change-requests/README.md",
                 "diagnostic": "index file missing"}]
    rows = collect_rows(index.read_text(encoding="utf-8", errors="replace"))

    cr_files = sorted((root / "change-requests").glob("CR-*.md"))
    hrefs_by_file: dict[str, int] = {}
    for ln, disp, href, line in rows:
        if href is None:
            if not line.startswith("|"):
                findings.append({"rule": "CR-004", "file": f"change-requests/README.md:{ln}",
                                 "diagnostic": f"table row missing leading pipe: {line[:60]}"})
            elif GAP_MARKER not in line:
                findings.append({"rule": "CR-005", "file": f"change-requests/README.md:{ln}",
                                 "diagnostic": f"row for {disp or '?'} has no href and no gap marker"})
            continue
        target = (root / "change-requests" / href).resolve()
        hrefs_by_file[href] = hrefs_by_file.get(href, 0) + 1
        try:
            rel = target.relative_to(root)
        except ValueError:
            findings.append({"rule": "CR-002", "file": f"change-requests/README.md:{ln}",
                             "diagnostic": f"row href escapes repo: {href}"})
            continue
        if not target.exists():
            findings.append({"rule": "CR-002", "file": f"change-requests/README.md:{ln}",
                             "diagnostic": f"row href does not resolve: {href}"})
            continue
        self_id = file_self_id(target)
        if self_id and disp and self_id != disp:
            findings.append({"rule": "CR-003", "file": f"change-requests/README.md:{ln}",
                             "diagnostic": f"row id {disp} != file self-id {self_id} ({href})"})

    for f in cr_files:
        if f.name == "README.md":
            continue
        if f.name not in hrefs_by_file:
            findings.append({"rule": "CR-001", "file": f"change-requests/{f.name}",
                             "diagnostic": "no index row links this CR file"})
    return findings


def self_test() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        crdir = root / "change-requests"
        crdir.mkdir()
        (crdir / "CR-DEA-BC-01.md").write_text("# CR-DEA-BC-01: One\n")
        (crdir / "CR-DEA-BC-02.md").write_text("# CR-DEA-BC-02: Two\n")
        (crdir / "CR-DEA-BC-07.md").write_text("# CR-DEA-BC-07: Unlinked\n")
        (crdir / "README.md").write_text(
            "| CR | Title | Status | Notes |\n|---|---|---|---|\n"
            "| [CR-DEA-BC-01](CR-DEA-BC-01.md) | One | Landed | ok |\n"
            "| [CR-DEA-BC-09](CR-DEA-BC-09.md) | Ghost | Landed | dead href |\n"
            "| [CR-DEA-BC-08](CR-DEA-BC-02.md) | Wrong id | Landed | id mismatch |\n"
            "CR-DEA-BC-03 | Bad row | Landed | no pipe |\n"
            "| CR-DEA-BC-04 | Gap row, no marker | Landed | no href |\n"
        )
        findings = evaluate(root)
        rules = sorted(f["rule"] for f in findings)
        assert rules == ["CR-001", "CR-002", "CR-003", "CR-004", "CR-005"], rules
    print("self-test PASS (5 cases)")
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

    findings = evaluate(REPO_ROOT)
    if findings:
        print("CR Index Discipline (CR-DEA-BC-39; CR-001..005): NON-CONFORMANT")
        for f in findings:
            print(f"  [{f['rule']}] {f['file']}: {f['diagnostic']}")
        return 1
    print("CR Index Discipline (CR-DEA-BC-39; CR-001..005): CONFORMANT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
