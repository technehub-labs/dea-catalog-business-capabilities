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
import subprocess
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


# ---------------------------------------------------------------------------
# CR-006: admission-CR linkage (PR-scoped; CR-DEA-BC-67)
# ---------------------------------------------------------------------------

CANONICAL_RECORD_DIR = "entities/v1-alpha/"
CR_DIR_PREFIX = "change-requests/"
CR_FILE_RE = re.compile(r"^CR-[A-Za-z]+-[A-Za-z0-9._-]+\.md$")


def _changed_files(root: Path, base_ref: str) -> tuple[list[str], list[str]]:
    """Return (added_files, all_changed_files) between base_ref and HEAD.

    Mirrors check_id_system.py's IDM-008 diff acquisition (three-dot first,
    two-dot fallback, empty on failure so a non-git context degrades to a
    skip rather than a false block).
    """
    added: list[str] = []
    for argv in (
        ["git", "diff", "--name-only", "--diff-filter=A", f"{base_ref}...HEAD"],
        ["git", "diff", "--name-only", "--diff-filter=A", base_ref, "HEAD"],
    ):
        res = subprocess.run(argv, cwd=str(root), capture_output=True, text=True)
        if res.returncode == 0:
            added = [ln.strip() for ln in res.stdout.splitlines() if ln.strip()]
            break
    res = subprocess.run(
        ["git", "diff", "--name-only", f"{base_ref}...HEAD"],
        cwd=str(root), capture_output=True, text=True,
    )
    changed = [ln.strip() for ln in res.stdout.splitlines() if ln.strip()] if res.returncode == 0 else []
    return added, changed


def _record_id_from_path(root: Path, rel: str) -> str | None:
    """Canonical record id from a changed file path, or None.

    The IDM-008 filter: entities/v1-alpha/<subtree>/<namespace>-*.yaml at
    the subtree root (four path parts). State dirs (research/candidates/
    retired) never sit at the subtree root, so they are excluded by
    construction. The id is read from the file's own `id:` field.
    """
    if not rel.startswith(CANONICAL_RECORD_DIR) or not rel.endswith(".yaml"):
        return None
    parts = Path(rel).parts
    if len(parts) != 4 or parts[1] != "v1-alpha":
        return None
    body = (root / rel).read_text(encoding="utf-8", errors="replace")
    for line in body.splitlines()[:10]:
        m = re.match(r"^id:\s*(\S+)\s*$", line)
        if m:
            return m.group(1)
    return None


def check_admission_linkage(root: Path, base_ref: str) -> list[dict]:
    """CR-006: every added canonical record must be covered by a CR file
    in the same diff that references the record's id.

    Motivating incident (CR-DEA-BC-67): three admission PRs (#117/#118/#119)
    landed eleven canonical records without CR documents; the retrospective
    CR files were carried by a later PR. This rule makes that landing shape
    fail CI in the PR that creates it.
    """
    added, changed = _changed_files(root, base_ref)
    if not added and not changed:
        return findings_empty()  # non-git or empty diff: degrade to skip

    new_records: dict[str, str] = {}
    for rel in added:
        rid = _record_id_from_path(root, rel)
        if rid:
            new_records[rid] = rel
    if not new_records:
        return []

    cr_bodies: list[str] = []
    for rel in changed:
        if rel.startswith(CR_DIR_PREFIX) and CR_FILE_RE.match(Path(rel).name):
            p = root / rel
            if p.exists():
                cr_bodies.append(p.read_text(encoding="utf-8", errors="replace"))

    findings: list[dict] = []
    for rid, rel in sorted(new_records.items()):
        if not any(rid in body for body in cr_bodies):
            findings.append({
                "rule": "CR-006",
                "file": rel,
                "diagnostic": (
                    f"new canonical record {rid} has no change-request document in this PR "
                    f"(no added change-requests/CR-*.md references it); every admission lands "
                    f"with its CR file (house discipline; motivating incident CR-DEA-BC-67)"
                ),
            })
    return findings


def findings_empty() -> list[dict]:
    return []


def main_pr_mode(root: Path, base_ref: str, report_path: str | None) -> int:
    findings = check_admission_linkage(root, base_ref)
    if report_path:
        added, changed = _changed_files(root, base_ref)
        lines = [
            "# CR Admission-Linkage Report (CR-006)",
            "",
            f"Base ref: `{base_ref}`",
            f"Changed files: {len(changed)}; added files: {len(added)}",
            f"Findings: {len(findings)} (all blocking)",
            "",
            "## Findings",
            "",
        ]
        lines += ([f"- [{f['rule']}] `{f['file']}`: {f['diagnostic']}" for f in findings]
                  if findings else ["None."])
        Path(report_path).write_text("\n".join(lines) + "\n")
    for f in findings:
        print(f"[{f['rule']}] {f['file']}: {f['diagnostic']}")
    verdict = "NON-CONFORMANT" if findings else "CONFORMANT"
    print(f"CR Admission-Linkage (CR-DEA-BC-67; CR-006): {verdict}")
    print(f"  blocking finding(s): {len(findings)}")
    return 1 if findings else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero on any finding (findings always exit non-zero)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the embedded self-test fixtures")
    parser.add_argument("--base-ref", default=None,
                        help="CR-006 mode: admission-linkage check on files changed vs this ref")
    parser.add_argument("--report-path", default=None,
                        help="CR-006 mode: write the linkage report here")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.base_ref:
        return main_pr_mode(REPO_ROOT, args.base_ref, args.report_path)

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
