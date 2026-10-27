"""Tests for scripts/check_doc_conformance.py (CR-DEA-BC-45)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_doc_conformance.py"


def _load():
    spec = importlib.util.spec_from_file_location("cdc_test", SCRIPT)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


SECTIONS = None  # loaded from module


def _make_entity(root: Path, name: str = "Cap X", slug: str = "cap-x-aaaaaa") -> tuple[Path, dict, Path]:
    ent = root / "entities" / "v1-alpha" / slug
    ent.mkdir(parents=True, exist_ok=True)
    rec_path = ent / f"capabilities-capability-{slug}.yaml"
    rec = {
        "id": f"capabilities:capability-{slug}", "type": "BusinessCapability",
        "name": name, "definition": "The ability to test.", "version": "1.0.0",
        "lifecycle_status": "active", "related_capabilities": [],
        "ecf": {"primary": {"domain": "governance-existence", "stage": "operate"}},
    }
    import yaml
    rec_path.write_text(yaml.safe_dump(rec, sort_keys=False))
    return rec_path, rec, ent


def _conformant_readme(rec_path: Path, mod) -> str:
    secs = mod.SECTIONS
    bodies = {
        secs[0]: "| Canonical ID | `capabilities:capability-cap-x-aaaaaa` |\n| Version / status | 1.0.0 · active |\n"
                 f"| Record | see [{rec_path.name}]({rec_path.name}) |",
        secs[1]: "> The ability to test.\n\nInterpretation: the capability-hood rationale.",
        secs[2]: "Not yet established (record `purpose` unpopulated).",
        secs[3]: "In scope: testing; out of scope: everything else.",
        secs[4]: "Primary: governance-existence / operate.",
        secs[5]: "No parent or child capabilities (first-order set is flat).",
        secs[6]: "None recorded.",
        secs[7]: "Not yet established (U-2).",
        secs[8]: "Contribution, not guarantee: things get tested.",
        secs[9]: "Not applicable (no assessment authority).",
        secs[10]: "See GOVERNANCE.md.",
        secs[11]: "Ladder recorded in the record.",
        secs[12]: "1.0.0 · active.",
        secs[13]: "Conformant to the README Standard.",
    }
    out = ["# Cap X\n"]
    for s in secs:
        out.append(f"## {s}\n\n{bodies[s]}\n")
    return "\n".join(out)


def test_conformant_entity_has_no_findings(tmp_path: Path):
    mod = _load()
    rp, rec, ent = _make_entity(tmp_path)
    (ent / "README.md").write_text(_conformant_readme(rp, mod))
    assert mod.check_entity(rp, rec, ent, {rec["id"]}) == []


def test_wrong_name_and_missing_definition_fire(tmp_path: Path):
    mod = _load()
    rp, rec, ent = _make_entity(tmp_path)
    text = _conformant_readme(rp, mod).replace("# Cap X", "# Wrong")
    text = text.replace("> The ability to test.\n\n", "")
    (ent / "README.md").write_text(text)
    rules = {f["rule"] for f in mod.check_entity(rp, rec, ent, {rec["id"]})}
    assert {"DCV-003", "DCV-005"} <= rules


def test_unresolvable_related_capability_fires_dcv008(tmp_path: Path):
    mod = _load()
    rp, rec, ent = _make_entity(tmp_path)
    rec["related_capabilities"] = ["capabilities:capability-ghost-zzzzzz"]
    (ent / "README.md").write_text(_conformant_readme(rp, mod))
    rules = {f["rule"] for f in mod.check_entity(rp, rec, ent, {rec["id"]})}
    assert "DCV-008" in rules


def test_honest_states_satisfy_dcv009(tmp_path: Path):
    mod = _load()
    rp, rec, ent = _make_entity(tmp_path)
    findings = mod.check_entity(rp, rec, ent, {rec["id"]})
    assert not any(f["rule"] == "DCV-009" for f in findings)


def test_missing_readme_fires_dcv001(tmp_path: Path):
    mod = _load()
    rp, rec, ent = _make_entity(tmp_path)  # no README written
    findings = mod.check_entity(rp, rec, ent, {rec["id"]})
    assert findings[0]["rule"] == "DCV-001" and len(findings) == 1


def test_cli_self_test_passes():
    import subprocess
    r = subprocess.run([sys.executable, str(SCRIPT), "--self-test"],
                       capture_output=True, text=True, cwd=str(REPO_ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
