#!/usr/bin/env python3
"""check_doc_conformance.py: entity-documentation conformance gate (CR-DEA-BC-45).

Enforces the deterministically checkable subset of the Business Capability
Documentation Standard (CR-DEA-BC-41) at the entity-README layer, per the
README Standard (CR-DEA-BC-44). What it does NOT prove: semantic correctness,
evidence sufficiency, boundary quality, ECF-rationale soundness — those remain
human semantic review (README Standard §6; CR-41 §9).

Rule catalogue (IDs DCV-*, mapped to requirement IDs BC-DOC-001..012 — no
namespace conflicts; existing gates AUT/ES/IDM/CST/DL/CR-001..005 stand
unchanged and are not reimplemented here):

| Rule | Layer | Normative source | Severity | Check |
|---|---|---|---|---|
| DCV-001 | Structural | BC-DOC-011 (S1) | blocking | canonical entity subtree has a README.md |
| DCV-002 | Structural | BC-DOC-011 (contract §5.1) | blocking | all 14 section headings present |
| DCV-003 | Cross-artifact | BC-DOC-001/012 (S1) | blocking | README H1 equals record `name` |
| DCV-004 | Cross-artifact | BC-DOC-001/012 (S1) | blocking | README renders the record `id` exactly |
| DCV-005 | Cross-artifact | BC-DOC-012 (S2) | blocking | README quotes the canonical `definition` verbatim (whitespace-normalized) |
| DCV-006 | Cross-artifact | BC-DOC-001/012 (S1/S13) | blocking | README renders `version` and `lifecycle_status` agreeing with the record |
| DCV-007 | Referential | BC-DOC-012 (S1) | blocking | README links its own canonical record file and the link resolves |
| DCV-008 | Referential | BC-DOC-012 (record) | blocking | every record `related_capabilities` id resolves to a canonical record |
| DCV-009 | Structural | BC-DOC-011 (S3/S8/S10 states) | warning | purpose/realization/assessment sections carry an explicit honest state or record-derived content |
| DCV-010 | Cross-artifact | BC-DOC-001/012 (S5) | blocking | README renders the record's primary ECF coordinate correctly |

Activation (CR-45 landing decision): CI runs advisory (no --strict) until
CR-DEA-BC-46 lands the catalog-wide remediation and enables --strict.

Run: python3 scripts/check_doc_conformance.py [--strict] [--self-test]
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ENTITIES = REPO_ROOT / "entities" / "v1-alpha"

SECTIONS = [
    "1. Identity", "2. Definition and semantic interpretation",
    "3. Purpose and value contribution", "4. Scope and boundaries",
    "5. Classification", "6. Composition and specialization",
    "7. Related entities and relationships", "8. Realization and operational context",
    "9. Outcomes and traceability", "10. Assessment considerations",
    "11. Governance", "12. Provenance and evidence",
    "13. Lifecycle and change history", "14. Conformance",
]
HONEST_STATES = ("Not yet established", "Not applicable", "Not yet documented",
                 "Explicitly unresolved", "not yet established", "not applicable")


def canonical_entities(root: Path) -> list[tuple[Path, dict, Path]]:
    """(record_path, record_dict, entity_dir) for every canonical entry."""
    out = []
    entities_dir = root / "entities" / "v1-alpha"
    for d in sorted(entities_dir.iterdir()):
        if not d.is_dir():
            continue
        for f in sorted(d.glob("capabilities-*.yaml")) + sorted(d.glob("capabilities-*.json")):
            doc = yaml.safe_load(f.read_text(encoding="utf-8")) if f.suffix == ".yaml" \
                else yaml.safe_load(f.read_text(encoding="utf-8"))
            if isinstance(doc, dict) and doc.get("type") == "BusinessCapability":
                out.append((f, doc, d))
    return out


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def check_entity(record_path: Path, rec: dict, ent_dir: Path,
                 all_ids: set[str]) -> list[dict]:
    findings: list[dict] = []
    readme = ent_dir / "README.md"

    def add(rule: str, sev: str, msg: str):
        findings.append({"rule": rule, "severity": sev,
                         "entity": rec.get("id", str(ent_dir.name)), "message": msg})

    # DCV-001
    if not readme.is_file():
        try:
            rel = str(readme.relative_to(REPO_ROOT))
        except ValueError:
            rel = str(readme)
        add("DCV-001", "blocking", f"missing entity README at {rel}")
        return findings
    text = readme.read_text(encoding="utf-8")

    # DCV-002
    for s in SECTIONS:
        if not re.search(rf"^## {re.escape(s)}\s*$", text, re.M):
            add("DCV-002", "blocking", f"missing section heading '## {s}'")

    # DCV-003
    h1 = re.search(r"^# (.+?)\s*$", text, re.M)
    if not h1:
        add("DCV-003", "blocking", "no H1 title")
    elif _norm(h1.group(1)) != _norm(str(rec.get("name", ""))):
        add("DCV-003", "blocking",
            f"H1 {h1.group(1)!r} != record name {rec.get('name')!r}")

    # DCV-004
    rid = str(rec.get("id", ""))
    if rid not in text:
        add("DCV-004", "blocking", f"canonical id {rid!r} not rendered in README")

    # DCV-005
    defn = _norm(str(rec.get("definition", "")))
    quotes = [_norm(q) for q in re.findall(r"^>\s*(.+?)\s*$", text, re.M)]
    if defn and defn not in quotes:
        add("DCV-005", "blocking", "canonical definition not quoted verbatim in a blockquote")

    # DCV-006
    ver, life = str(rec.get("version", "")), str(rec.get("lifecycle_status", ""))
    if ver and ver not in text:
        add("DCV-006", "blocking", f"record version {ver!r} not rendered")
    if life and not re.search(rf"\b{re.escape(life)}\b", text):
        add("DCV-006", "blocking", f"record lifecycle_status {life!r} not rendered")

    # DCV-007
    links = re.findall(r"\]\(([^)#\s]+\.yaml)\)", text)
    if not any((ent_dir / lp).resolve().exists() and (ent_dir / lp).resolve() == record_path.resolve()
               for lp in links):
        add("DCV-007", "blocking",
            f"README does not link its canonical record ({record_path.name}) via a resolving relative link")

    # DCV-008 (record-level; checked per entity for locality of reporting)
    for rel in rec.get("related_capabilities") or []:
        if rel not in all_ids:
            add("DCV-008", "blocking", f"related capability {rel!r} does not resolve to a canonical record")

    # DCV-009
    for sec, label in ((SECTIONS[2], "purpose"), (SECTIONS[7], "realization"), (SECTIONS[9], "assessment")):
        m = re.search(rf"^## {re.escape(sec)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        body = _norm(m.group(1)) if m else ""
        if not body:
            add("DCV-009", "warning", f"section '{sec}' is empty")
        elif len(body) < 25 and not any(st in body for st in HONEST_STATES):
            add("DCV-009", "warning",
                f"section '{sec}' has neither an explicit honest state nor substantive content ({label})")

    # DCV-010
    ecf = (rec.get("ecf") or {}).get("primary") or {}
    coord = f"{ecf.get('domain', '')} / {ecf.get('stage', '')}" if ecf else ""
    if coord and coord not in text:
        alt = f"{ecf.get('domain', '')}/{ecf.get('stage', '')}"
        if alt not in text:
            add("DCV-010", "blocking", f"primary ECF coordinate {coord!r} not rendered")
    return findings


def evaluate(root: Path) -> list[dict]:
    ents = canonical_entities(root)
    all_ids = {rec.get("id") for _, rec, _ in ents if rec.get("id")}
    return [f for rp, rec, d in ents for f in check_entity(rp, rec, d, all_ids)]


def self_test() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        ent = root / "entities" / "v1-alpha" / "cap-x-aaaaaa"
        ent.mkdir(parents=True)
        rec = ent / "capabilities-capability-cap-x-aaaaaa.yaml"
        rec.write_text(
            "id: capabilities:capability-cap-x-aaaaaa\ntype: BusinessCapability\n"
            "name: Cap X\ndefinition: The ability to test.\nversion: 1.0.0\n"
            "lifecycle_status: active\nrelated_capabilities: []\n"
            "ecf:\n  primary:\n    domain: governance-existence\n    stage: operate\n")
        (ent / "README.md").write_text(
            "# Cap X\n\n## 1. Identity\n\n| Field | Value |\n|---|---|\n"
            "| Canonical ID | `capabilities:capability-cap-x-aaaaaa` |\n"
            "| Version / status | 1.0.0 · active |\n"
            f"| Record | [{rec.name}]({rec.name}) |\n\n"
            "## 2. Definition and semantic interpretation\n\n> The ability to test.\n\n"
            "## 3. Purpose and value contribution\n\nNot yet established (record `purpose` unpopulated).\n\n"
            "## 4. Scope and boundaries\n\nIn scope: testing.\n\n"
            "## 5. Classification\n\nPrimary: governance-existence / operate\n\n"
            "## 6. Composition and specialization\n\nNone.\n\n"
            "## 7. Related entities and relationships\n\nNone recorded.\n\n"
            "## 8. Realization and operational context\n\nNot yet established (U-2).\n\n"
            "## 9. Outcomes and traceability\n\nOutcome.\n\n"
            "## 10. Assessment considerations\n\nNot applicable.\n\n"
            "## 11. Governance\n\nSee GOVERNANCE.md.\n\n"
            "## 12. Provenance and evidence\n\nLadder.\n\n"
            "## 13. Lifecycle and change history\n\n1.0.0 active.\n\n"
            "## 14. Conformance\n\nConformant.\n")
        findings = evaluate(root)
        assert findings == [], findings
        # break several rules
        (ent / "README.md").write_text("# Wrong Name\n\n## 1. Identity\n\nno id, no link\n")
        findings = evaluate(root)
        rules = {f["rule"] for f in findings}
        assert {"DCV-002", "DCV-003", "DCV-004", "DCV-005", "DCV-006", "DCV-007"} <= rules, rules
    print("self-test PASS (2 cases)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="blocking findings exit non-zero (advisory otherwise)")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    findings = evaluate(REPO_ROOT)
    blocking = [f for f in findings if f["severity"] == "blocking"]
    warnings = [f for f in findings if f["severity"] != "blocking"]
    mode = "STRICT" if args.strict else "ADVISORY"
    print(f"Documentation Conformance (CR-DEA-BC-45; DCV-001..010) [{mode}]: "
          f"{len(blocking)} blocking, {len(warnings)} warning(s)")
    for f in findings:
        print(f"  [{f['rule']}/{f['severity']}] {f['entity']}: {f['message']}")
    if blocking and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
