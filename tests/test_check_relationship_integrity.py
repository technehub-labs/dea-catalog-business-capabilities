"""Tests for scripts/check_relationship_integrity.py (CR-DEA-BC-48)."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_relationship_integrity.py"


def _load():
    spec = importlib.util.spec_from_file_location("cri_test", SCRIPT)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _entity(root: Path, slug: str, rel=None, boundary=None):
    e = root / "entities" / "v1-alpha" / slug
    e.mkdir(parents=True, exist_ok=True)
    import yaml
    rec = {"id": f"capabilities:capability-{slug}", "type": "BusinessCapability", "name": slug}
    if rel is not None:
        rec["related_capabilities"] = rel
    if boundary is not None:
        rec["boundary"] = boundary
    (e / f"capabilities-capability-{slug}.yaml").write_text(yaml.safe_dump(rec, sort_keys=False))
    return rec["id"]


def test_resolving_references_pass(tmp_path: Path):
    mod = _load()
    b = _entity(tmp_path, "cap-b-bbbbbb")
    _entity(tmp_path, "cap-a-aaaaaa", rel=[b],
            boundary={"against_capabilities": [{"id": b, "rationale": "distinct objects"}]})
    findings, obs = mod.evaluate(tmp_path)
    assert findings == [] and obs == []


def test_unresolved_and_rationale_findings(tmp_path: Path):
    mod = _load()
    _entity(tmp_path, "cap-a-aaaaaa", rel=["capabilities:capability-ghost-zzzzzz"],
            boundary={"against_capabilities": [{"id": "capabilities:capability-ghost2-yyyyyy", "rationale": ""}]})
    findings, _ = mod.evaluate(tmp_path)
    assert {f["rule"] for f in findings} == {"RI-001", "RI-002", "RI-003"}


def test_self_reference_is_observation_not_finding(tmp_path: Path):
    mod = _load()
    a = _entity(tmp_path, "cap-a-aaaaaa")
    _entity(tmp_path, "cap-a-aaaaaa2" if False else "cap-b-bbbbbb", rel=None)
    # rewrite a to self-reference
    import yaml
    p = tmp_path / "entities" / "v1-alpha" / "cap-a-aaaaaa" / "capabilities-capability-cap-a-aaaaaa.yaml"
    rec = yaml.safe_load(p.read_text())
    rec["related_capabilities"] = [a]
    p.write_text(yaml.safe_dump(rec, sort_keys=False))
    findings, obs = mod.evaluate(tmp_path)
    assert findings == [] and len(obs) == 1 and "self-reference" in obs[0]


def test_cli_self_test():
    r = subprocess.run([sys.executable, str(SCRIPT), "--self-test"],
                       capture_output=True, text=True, cwd=str(REPO_ROOT))
    assert r.returncode == 0, r.stdout + r.stderr


def test_typed_assertions_ri005(tmp_path: Path):
    mod = _load()
    b = _entity(tmp_path, "cap-b-bbbbbb")
    # the registry is the type authority; provide a minimal one in the fixture tree
    reg = tmp_path / "reconciliation"
    reg.mkdir()
    (reg / "entity-system-registry.yaml").write_text(
        "relationships:\n  field: related_capabilities\n  type_field: type\n"
        "  canonical_types: [depends-on, realizes, specializes]\n")
    _entity(tmp_path, "cap-a-aaaaaa", rel=[
        {"id": b, "type": "depends-on", "rationale": "A relies on B"},
        {"id": "capabilities:capability-ghost-zzzzzz", "type": "depends-on", "rationale": "r"},
        {"id": b, "type": "wobbles", "rationale": "r"},
        {"id": b, "type": "realizes"},
        b,  # duplicate of typed target in bare form
    ])
    findings, _ = mod.evaluate(tmp_path)
    rules = [f["rule"] for f in findings]
    assert rules.count("RI-005") == 4, rules  # unresolved target, bad type, missing rationale, dual form
