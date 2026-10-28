#!/usr/bin/env python3
"""check_relationship_integrity.py: canonical relationship integrity gate
(CR-DEA-BC-48; rules RI-001..004 per
docs/CANONICAL-RELATIONSHIP-INTEGRITY-STANDARD.md).

RI-001 (blocking): every `related_capabilities` id resolves to a canonical record.
RI-002 (blocking): every structured `boundary.against_capabilities[].id` resolves.
RI-003 (blocking): structured-boundary entries carry non-empty `rationale`.
RI-004 (finding, never failing): registry ES-003 types expressible in the schema —
      reports the open R-1 gap (declared types vs bare-list pattern).

Deliberately NOT imposed: acyclicity, reciprocity, self-reference prohibition
(no authority in the model; a self-reference, if ever observed, is reported as
an observation for semantic review).

Run: python3 scripts/check_relationship_integrity.py [--strict] [--self-test]
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_entities(root: Path) -> list[dict]:
    out = []
    ent_dir = root / "entities" / "v1-alpha"
    for d in sorted(ent_dir.iterdir()):
        if not d.is_dir():
            continue
        for f in sorted(d.glob("capabilities-*.yaml")):
            rec = yaml.safe_load(f.read_text(encoding="utf-8"))
            if isinstance(rec, dict) and rec.get("type") == "BusinessCapability":
                out.append(rec)
    return out


def evaluate(root: Path) -> tuple[list[dict], list[str]]:
    findings: list[dict] = []
    observations: list[str] = []
    recs = load_entities(root)
    ids = {r.get("id") for r in recs}

    def add(rule: str, entity: str, msg: str):
        findings.append({"rule": rule, "entity": entity, "message": msg})

    reg = {}
    reg_path = root / "reconciliation" / "entity-system-registry.yaml"
    if reg_path.is_file():
        reg = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
    canonical_types = ((reg.get("relationships") or {}).get("canonical_types")) or []

    for r in recs:
        rid = r.get("id", "?")
        bare_seen = set()
        for rel in r.get("related_capabilities") or []:
            if isinstance(rel, dict):
                # RI-005 (CR-DEA-BC-53): typed assertions
                tid = rel.get("id")
                if tid not in ids:
                    add("RI-005", rid, f"typed assertion target {tid!r} does not resolve")
                if canonical_types and rel.get("type") not in canonical_types:
                    add("RI-005", rid, f"typed assertion type {rel.get('type')!r} not in registry canonical types")
                if not str(rel.get("rationale") or "").strip():
                    add("RI-005", rid, f"typed assertion target {tid!r} lacks rationale")
            else:
                if rel not in ids:
                    add("RI-001", rid, f"related capability {rel!r} does not resolve")
                elif rel == rid:
                    observations.append(f"self-reference observed at {rid} (semantic-review item; not auto-failed)")
                bare_seen.add(rel)
        # no duplicate assertion of the same target in both forms
        typed_ids = {rel.get("id") for rel in (r.get("related_capabilities") or []) if isinstance(rel, dict)}
        for dup in bare_seen & typed_ids:
            add("RI-005", rid, f"target {dup!r} asserted in both bare and typed forms")
        b = r.get("boundary")
        if isinstance(b, dict):
            for a in b.get("against_capabilities") or []:
                if a.get("id") not in ids:
                    add("RI-002", rid, f"boundary against_capabilities id {a.get('id')!r} does not resolve")
                if not str(a.get("rationale") or "").strip():
                    add("RI-003", rid, f"boundary against_capabilities id {a.get('id')!r} lacks rationale")

    # RI-004: registry types vs schema expressibility (report only)
    schema = root / "schemas" / "entity.schema.json"
    registry = root / "reconciliation" / "entity-system-registry.yaml"
    if schema.is_file() and registry.is_file():
        import json
        schema_json = json.loads(schema.read_text(encoding="utf-8"))
        items = ((schema_json.get("properties") or {}).get("related_capabilities") or {}).get("items") or {}
        typed_expressible = "oneOf" in items or "properties" in items
        reg = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
        types = ((reg.get("relationships") or {}).get("canonical_types")) or []
        if types and not typed_expressible:
            observations.append(
                "RI-004: registry declares relationship types " + ", ".join(types)
                + " but is now expressible since CR-DEA-BC-53; population evidence outstanding (R-1 implementation phase)")
    return findings, observations


def self_test() -> int:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        e = root / "entities" / "v1-alpha" / "cap-a-aaaaaa"
        e.mkdir(parents=True)
        (e / "capabilities-capability-cap-a-aaaaaa.yaml").write_text(
            "id: capabilities:capability-cap-a-aaaaaa\ntype: BusinessCapability\n"
            "name: A\nrelated_capabilities: [capabilities:capability-ghost-zzzzzz]\n")
        f2 = root / "entities" / "v1-alpha" / "cap-b-bbbbbb"
        f2.mkdir()
        (f2 / "capabilities-capability-cap-b-bbbbbb.yaml").write_text(
            "id: capabilities:capability-cap-b-bbbbbb\ntype: BusinessCapability\nname: B\n"
            "boundary:\n  against_capabilities:\n  - {id: capabilities:capability-ghost2-yyyyyy, rationale: ''}\n")
        findings, obs = evaluate(root)
        rules = sorted({f["rule"] for f in findings})
        assert rules == ["RI-001", "RI-002", "RI-003"], rules
    print("self-test PASS (1 case)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="findings exit non-zero (default behaviour for CI)")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()

    findings, observations = evaluate(REPO_ROOT)
    print(f"Relationship Integrity (CR-DEA-BC-48/53; RI-001..005): "
          f"{len(findings)} finding(s), {len(observations)} observation(s)")
    for f in findings:
        print(f"  [{f['rule']}] {f['entity']}: {f['message']}")
    for o in observations:
        print(f"  [obs] {o}")
    if findings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
