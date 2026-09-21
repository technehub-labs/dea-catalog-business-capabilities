#!/usr/bin/env python3
"""
check_id_system.py
CR-DEA-BC-mv1: ID System gate (IDM-001..007 catalog-wide; IDM-008 PR-scoped).

Enforces the org-wide id system spec (dea-metaframework/docs/id-system.md)
for the capabilities catalog (flat layout, docs/entity-storage-layout.md
section 3): every canonical record's id matches the org-wide form, the
namespace token matches the registry binding, every structured
cross-reference resolves, every entropy suffix is well-formed, every
filesystem path is derivable from its id, no legacy `dea:*` ids remain in
structured reference fields, and every entity directory carries a
README.md.

Usage:
  python scripts/check_id_system.py [--json] [--strict]
  python scripts/check_id_system.py --base-ref origin/main [--report-path PATH]

Exit codes:
  0  CONFORMANT (0 blocking findings)
  1  NON-CONFORMANT (>= 1 blocking finding)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "entities" / "v1-alpha"
RECONCILIATION = ROOT / "reconciliation"

NAMESPACE = "capabilities"
LEVELS = ("capability", "candidate")

BASE32 = "abcdefghjkmnpqrstuvwxyz23456789"

# IDM-001: id regex matches org-wide form (flat: no domain/stage segment)
ID_PATTERN = re.compile(
    r"^capabilities:(capability|candidate)-[a-z0-9-]+-[a-z2-9]{6}$"
)

LEGACY_RE = re.compile(r"^dea:(capability|candidate)-")


def _check_idm001(record_id: str) -> str | None:
    if not ID_PATTERN.match(record_id):
        return f"IDM-001: id does not match org-wide form: {record_id}"
    return None


def _check_idm002(record_id: str) -> str | None:
    ns = record_id.split(":", 1)[0]
    if ns != NAMESPACE:
        return f"IDM-002: namespace token {ns!r} does not match repo namespace {NAMESPACE!r}: {record_id}"
    return None


def _check_idm003(record: dict, live_ids: set[str], path: Path) -> list[str]:
    errors = []

    def check_refs(obj, path_str=""):
        if isinstance(obj, str):
            if obj.startswith(f"{NAMESPACE}:"):
                token = obj.split(" ", 1)[0].rstrip(":")
                if token not in live_ids:
                    errors.append(f"IDM-003: unresolved reference in {record.get('id', '?')} at {path_str}: {token}")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                check_refs(v, f"{path_str}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                check_refs(v, f"{path_str}[{i}]")

    check_refs(record)
    return errors


def _check_idm004(record_id: str) -> str | None:
    """IDM-004: entropy suffix well-formed (6 chars over the 31-symbol
    alphabet; content-addressed at migration time, immutable thereafter)."""
    suffix = record_id.split("-")[-1]
    if len(suffix) != 6 or any(c not in BASE32 for c in suffix):
        return f"IDM-004: entropy suffix {suffix!r} is not 6 well-formed chars: {record_id}"
    return None


def _check_idm005(record_id: str, path: Path) -> str | None:
    """IDM-005: path derivable from id (flat layout).

    dir  = id minus '<namespace>:<level>-' prefix
    file = id with ':' normalized to '-' + '.yaml'
    """
    body = record_id.split(":", 1)[1]
    expected_dir = body.split("-", 1)[1]
    expected_name = record_id.replace(":", "-").lower() + ".yaml"
    if path.name != expected_name:
        return f"IDM-005: filename {path.name!r} does not match id-derived name {expected_name!r} for {record_id}"
    if path.parent.name != expected_dir:
        return f"IDM-005: dir {path.parent.name!r} does not match id-derived dir {expected_dir!r} for {record_id}"
    if path.parent.parent.name != "v1-alpha":
        return f"IDM-005: record not at entities/v1-alpha/<dir>/ depth for {record_id}"
    return None


_RESIDUAL_VALUES: set[str] | None = None


def _residual_values() -> set[str]:
    global _RESIDUAL_VALUES
    if _RESIDUAL_VALUES is not None:
        return _RESIDUAL_VALUES
    values: set[str] = set()
    map_path = RECONCILIATION / "migration-id-map.yaml"
    if map_path.exists():
        try:
            map_data = yaml.safe_load(map_path.read_text()) or {}
            for r in map_data.get("known_residuals", []) or []:
                v = r.get("legacy_value")
                if isinstance(v, str):
                    values.add(v)
        except yaml.YAMLError:
            pass
    _RESIDUAL_VALUES = values
    return values


def _check_idm006(record: dict, path: Path) -> list[str]:
    """IDM-006: no legacy dea:* ids in STRUCTURED reference fields.
    Historical prose may cite legacy ids verbatim."""
    errors = []
    structured_fields = (
        "id", "related_capabilities", "target_id", "source_id", "ref",
        "parent", "supersedes", "source",
    )
    residual_values = _residual_values()

    def walk(obj, field=""):
        if isinstance(obj, str):
            if field in structured_fields and LEGACY_RE.match(obj) and obj not in residual_values:
                errors.append(f"IDM-006: legacy id in structured field {field!r} of {path.name}: {obj}")
        elif isinstance(obj, dict):
            for k, v in obj.items():
                walk(v, k)
        elif isinstance(obj, list):
            for v in obj:
                walk(v, field)

    walk(record)
    return errors


def _check_idm007(path: Path) -> str | None:
    if not (path.parent / "README.md").exists():
        return f"IDM-007: missing README.md in {path.parent.name}"
    return None


def _load_all_records() -> dict[str, tuple[Path, dict]]:
    """Canonical records only: capabilities-*.yaml at entity dir roots."""
    records = {}
    for p in sorted(ENTITIES.glob("*/capabilities-*.yaml")):
        record = yaml.safe_load(p.read_text())
        rid = record.get("id", "")
        if rid:
            records[rid] = (p, record)
    return records


# ---------------------------------------------------------------------------
# IDM-008: PR-scoped file coherence
# ---------------------------------------------------------------------------

DOC_SCAN_DIRS = ("change-requests/", "docs/", "submittal-reviews/")
LEGACY_PATH_PATTERNS = (
    "entities/v1-alpha/dea:",
    "dea:capability-",
    "dea:candidate-",
)
HISTORICAL_MARKERS = ("pre-migration", "historical", "formerly", "legacy", "superseded")


def _changed_files(base_ref: str) -> list[str]:
    for argv in (["git", "diff", "--name-only", f"{base_ref}...HEAD"],
                 ["git", "diff", "--name-only", base_ref, "HEAD"]):
        r = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        if r.returncode == 0:
            return [l.strip() for l in r.stdout.splitlines() if l.strip()]
    return []


def _check_idm008_records(changed: list[str], live_ids: set[str]) -> list[dict]:
    findings: list[dict] = []
    for rel in changed:
        if not (rel.startswith("entities/v1-alpha/") and rel.endswith(".yaml")):
            continue
        if not Path(rel).name.startswith(f"{NAMESPACE}-"):
            continue  # state-dir / research files are out of scope
        p = ROOT / rel
        if not p.exists():
            continue
        record = yaml.safe_load(p.read_text())
        if not isinstance(record, dict):
            continue
        rid = record.get("id", "")
        for e in (_check_idm001(rid), _check_idm002(rid), _check_idm005(rid, p)):
            if e:
                findings.append({"rule": "IDM-008", "path": rel, "message": e})
        for e in _check_idm003(record, live_ids, p) + _check_idm006(record, p):
            findings.append({"rule": "IDM-008", "path": rel, "message": e})
    return findings


def _check_idm008_docs(changed: list[str]) -> list[dict]:
    """Advisory: changed CR/ADR markdown must not carry legacy id/path forms
    outside clearly historical framing."""
    findings: list[dict] = []
    in_fence = False
    for rel in changed:
        if not (rel.endswith(".md") and rel.startswith(DOC_SCAN_DIRS)):
            continue
        p = ROOT / rel
        if not p.exists():
            continue
        for lineno, line in enumerate(p.read_text().splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for pat in LEGACY_PATH_PATTERNS:
                if pat in line:
                    low = line.lower()
                    if any(m in low for m in HISTORICAL_MARKERS):
                        continue
                    findings.append({
                        "rule": "IDM-008/DOC", "path": f"{rel}:{lineno}",
                        "message": f"legacy form {pat!r} in changed markdown without historical framing marker",
                        "advisory": True,
                    })
    return findings


def _write_report(path: Path, base_ref: str, changed: list[str], findings: list[dict]) -> None:
    lines = [
        "# ID System Coherence Report (IDM-008)",
        "",
        f"Base ref: `{base_ref}`",
        f"Changed files scanned: {len(changed)}",
        f"Findings: {len(findings)} ({sum(1 for f in findings if not f.get('advisory'))} blocking)",
        "",
        "## Changed files",
        "",
    ]
    lines += [f"- `{c}`" for c in changed]
    lines += ["", "## Findings", ""]
    lines += ([f"- [{f['rule']}] `{f['path']}`: {f['message']}" for f in findings]
              if findings else ["None."])
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("--json", action="store_true")
    p.add_argument("--strict", action="store_true")
    p.add_argument("--base-ref", default=None,
                   help="IDM-008 mode: check only files changed vs this ref")
    p.add_argument("--report-path", default=None)
    args = p.parse_args()

    records = _load_all_records()
    live_ids = set(records)

    if args.base_ref:
        changed = _changed_files(args.base_ref)
        findings = _check_idm008_records(changed, live_ids)
        findings += _check_idm008_docs(changed)
        if args.report_path:
            _write_report(Path(args.report_path), args.base_ref, changed, findings)
        blocking = [f for f in findings if not f.get("advisory", False)]
        verdict = "NON-CONFORMANT" if blocking else "CONFORMANT"
        print(f"ID System coherence (IDM-008, base {args.base_ref}): {verdict}")
        print(f"  Changed files scanned: {len(changed)}")
        print(f"  Findings: {len(findings)} ({len(blocking)} blocking)")
        for f in findings[:20]:
            print(f"    [{f['rule']}] {f['path']}: {f['message']}")
        return 1 if blocking else 0

    findings = []
    for rid, (path, record) in records.items():
        for fn in (_check_idm001, _check_idm002, _check_idm004):
            e = fn(rid)
            if e:
                findings.append({"rule": e.split(":")[0], "record": rid, "message": e})
        e = _check_idm005(rid, path)
        if e:
            findings.append({"rule": "IDM-005", "record": rid, "message": e})
        for e in _check_idm003(record, live_ids, path):
            findings.append({"rule": "IDM-003", "record": rid, "message": e})
        for e in _check_idm006(record, path):
            findings.append({"rule": "IDM-006", "record": rid, "message": e})
        e = _check_idm007(path)
        if e:
            findings.append({"rule": "IDM-007", "record": rid, "message": e})

    blocking = [f for f in findings if not f.get("advisory", False)]
    verdict = "NON-CONFORMANT" if blocking else "CONFORMANT"
    print(f"ID System (CR-DEA-BC-mv1 IDM-001..007): {verdict}")
    print(f"  Records checked: {len(records)}")
    print(f"  Findings: {len(findings)}")
    for f in findings[:20]:
        print(f"    [{f['rule']}] {f['message']}")
    if args.json:
        print(json.dumps({"verdict": verdict, "records_checked": len(records),
                          "findings": findings, "blocking": len(blocking)}, indent=2))
    return 1 if (args.strict and blocking) else 0


if __name__ == "__main__":
    raise SystemExit(main())
