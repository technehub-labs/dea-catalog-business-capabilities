"""Tests for scripts/generate_discovery_views.py (CR-DEA-BC-47)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "generate_discovery_views.py"


def _load():
    spec = importlib.util.spec_from_file_location("gdv_test", SCRIPT)
    assert spec and spec.loader
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _entity(root: Path, slug: str, name: str, rel=None):
    ent = root / "entities" / "v1-alpha" / slug
    ent.mkdir(parents=True, exist_ok=True)
    rec = {
        "id": f"capabilities:capability-{slug}", "type": "BusinessCapability",
        "name": name, "definition": f"The ability to {name}.", "version": "1.0.0",
        "lifecycle_status": "active", "outcome": f"{name} outcome.", "business_object": "X",
        "related_capabilities": rel or [],
        "ecf": {"primary": {"domain": "d-one", "stage": "s-one"}},
        "provenance": {"ladder_passage": [{"stage": "canonical", "date": "2026-09-01", "actor": "test"}]},
    }
    import yaml
    (ent / f"capabilities-capability-{slug}.yaml").write_text(yaml.safe_dump(rec, sort_keys=False))
    return rec


def test_deterministic_and_complete(tmp_path: Path):
    mod = _load()
    _entity(tmp_path, "cap-a-aaaaaa", "Cap A", ["capabilities:capability-cap-b-bbbbbb"])
    _entity(tmp_path, "cap-b-bbbbbb", "Cap B")
    out = mod.generate(tmp_path)
    assert set(out) == {"CAPABILITY-INDEX.md", "ECF-CLASSIFICATION.md", "RELATED-CAPABILITIES.md", "OUTCOMES-OVERVIEW.md"}
    assert out == mod.generate(tmp_path)  # deterministic
    assert "[Cap B]" in out["RELATED-CAPABILITIES.md"]  # A->B recorded
    assert "d-one / s-one" in out["ECF-CLASSIFICATION.md"]


def test_unresolved_reference_is_marked_not_dropped(tmp_path: Path):
    mod = _load()
    _entity(tmp_path, "cap-a-aaaaaa", "Cap A", ["capabilities:capability-ghost-zzzzzz"])
    out = mod.generate(tmp_path)
    assert "unresolved" in out["RELATED-CAPABILITIES.md"]


def test_generated_views_are_not_marked_authoritative(tmp_path: Path):
    mod = _load()
    _entity(tmp_path, "cap-a-aaaaaa", "Cap A")
    for content in mod.generate(tmp_path).values():
        assert "GENERATED" in content
        assert "Do not edit" in content


def test_cli_self_test_passes():
    import subprocess
    r = subprocess.run([sys.executable, str(SCRIPT), "--self-test"],
                       capture_output=True, text=True, cwd=str(REPO_ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
