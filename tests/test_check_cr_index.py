"""Tests for scripts/check_cr_index.py (CR-DEA-BC-39 §6.2)."""
from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_cr_index.py"
GATE_SRC = SCRIPT


def _load_module():
    spec = importlib.util.spec_from_file_location("check_cr_index_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _make_tree(tmp_path: Path, files: dict[str, str], index: str):
    crdir = tmp_path / "change-requests"
    crdir.mkdir(parents=True, exist_ok=True)
    for name, body in files.items():
        (crdir / name).write_text(body)
    (crdir / "README.md").write_text(index)
    return tmp_path


HEAD = "| CR | Title | Status | Notes |\n|---|---|---|---|\n"


def test_clean_index_has_no_findings(tmp_path: Path):
    mod = _load_module()
    root = _make_tree(tmp_path,
                      {"CR-DEA-BC-01.md": "# CR-DEA-BC-01: One\n"},
                      HEAD + "| [CR-DEA-BC-01](CR-DEA-BC-01.md) | One | Landed | ok |\n")
    assert mod.evaluate(root) == []


def test_unlinked_file_fires_cr_001(tmp_path: Path):
    mod = _load_module()
    root = _make_tree(tmp_path,
                      {"CR-DEA-BC-01.md": "# CR-DEA-BC-01: One\n",
                       "CR-DEA-BC-02.md": "# CR-DEA-BC-02: Two\n"},
                      HEAD + "| [CR-DEA-BC-01](CR-DEA-BC-01.md) | One | Landed | ok |\n")
    rules = [f["rule"] for f in mod.evaluate(root)]
    assert rules == ["CR-001"]


def test_dead_href_fires_cr_002(tmp_path: Path):
    mod = _load_module()
    root = _make_tree(tmp_path, {},
                      HEAD + "| [CR-DEA-BC-09](CR-DEA-BC-09.md) | Ghost | Landed | x |\n")
    rules = [f["rule"] for f in mod.evaluate(root)]
    assert rules == ["CR-002"]


def test_id_mismatch_fires_cr_003(tmp_path: Path):
    mod = _load_module()
    root = _make_tree(tmp_path,
                      {"CR-DEA-BC-02.md": "# CR-DEA-BC-02: Two\n"},
                      HEAD + "| [CR-DEA-BC-08](CR-DEA-BC-02.md) | Wrong | Landed | x |\n")
    rules = [f["rule"] for f in mod.evaluate(root)]
    assert rules == ["CR-003"]


def test_row_without_pipe_fires_cr_004(tmp_path: Path):
    mod = _load_module()
    root = _make_tree(tmp_path,
                      {"CR-DEA-BC-03.md": "# CR-DEA-BC-03: Three\n"},
                      HEAD + "| [CR-DEA-BC-03](CR-DEA-BC-03.md) | Three | Landed | ok |\n"
                            "CR-DEA-BC-04 | Bad row | Landed | no pipe |\n")
    rules = [f["rule"] for f in mod.evaluate(root)]
    assert rules == ["CR-004"]


def test_unlinked_row_needs_gap_marker_cr_005(tmp_path: Path):
    mod = _load_module()
    root = _make_tree(tmp_path, {},
                      HEAD + "| CR-DEA-BC-04 | Gap, no marker | Landed | x |\n")
    rules = [f["rule"] for f in mod.evaluate(root)]
    assert rules == ["CR-005"]
    root2 = _make_tree(tmp_path.parent / "idx_gap_ok",
                       {},
                       HEAD + "| CR-DEA-BC-04 | Gap | Landed | No standalone CR file landed. |\n")
    assert mod.evaluate(root2) == []


def test_cli_self_test_passes():
    import subprocess
    r = subprocess.run([sys.executable, str(SCRIPT), "--self-test"],
                       capture_output=True, text=True, cwd=str(REPO_ROOT))
    assert r.returncode == 0, r.stdout + r.stderr


# ---------------------------------------------------------------------------
# CR-006: admission-CR linkage (CR-DEA-BC-67) -- two-commit git fixture
# ---------------------------------------------------------------------------

import subprocess


def _git(cwd, *argv):
    res = subprocess.run(["git", *argv], cwd=str(cwd), capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    return res.stdout.strip()


def _commit_tree(root, files):
    if not (root / ".git").exists():
        _git(root, "init", "-q", "-b", "main")
    for rel, body in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    _git(root, "add", "-A")
    _git(root, "-c", "user.email=gate@example.com", "-c", "user.name=gate", "commit", "-qm", "tree")


RECORD = (
    "id: capabilities:capability-gap-candidate-x1h2j3\n"
    "type: BusinessCapability\n"
    "name: Gap Candidate\n"
    "version: 1.0.0\n"
    "lifecycle_status: active\n"
)
CR_COVERING = "# CR-DEA-BC-99: Test admission\n\nAdmits `capabilities:capability-gap-candidate-x1h2j3`.\n"
CR_OTHER = "# CR-DEA-BC-98: Unrelated\n\nNo records.\n"


_mod = None


def _gate():
    global _mod
    if _mod is None:
        _mod = _load_module()
    return _mod


def test_cr006_fires_for_record_without_cr(tmp_path):
    _commit_tree(tmp_path, {"README.md": "base\n"})
    _git(tmp_path, "checkout", "-qb", "pr")
    _commit_tree(tmp_path, {"entities/v1-alpha/gap-candidate-x1h2j3/capabilities-capability-gap-candidate-x1h2j3.yaml": RECORD})
    findings = _gate().check_admission_linkage(tmp_path, "main")
    assert any(f["rule"] == "CR-006" for f in findings), findings
    assert "capabilities:capability-gap-candidate-x1h2j3" in findings[0]["diagnostic"]


def test_cr006_passes_when_cr_references_record(tmp_path):
    _commit_tree(tmp_path, {"README.md": "base\n"})
    _git(tmp_path, "checkout", "-qb", "pr")
    _commit_tree(tmp_path, {
        "entities/v1-alpha/gap-candidate-x1h2j3/capabilities-capability-gap-candidate-x1h2j3.yaml": RECORD,
        "change-requests/CR-DEA-BC-99-test-admission.md": CR_COVERING,
    })
    assert _gate().check_admission_linkage(tmp_path, "main") == []


def test_cr006_ignores_non_record_changes(tmp_path):
    _commit_tree(tmp_path, {"README.md": "base\n"})
    _git(tmp_path, "checkout", "-qb", "pr")
    _commit_tree(tmp_path, {
        "change-requests/CR-DEA-BC-98-unrelated.md": CR_OTHER,
        "docs/views/CAPABILITY-INDEX.md": "regenerated\n",
        "entities/v1-alpha/gap-candidate-x1h2j3/candidates/.gitkeep": "",
    })
    assert _gate().check_admission_linkage(tmp_path, "main") == []


def test_cr006_ignores_state_dir_records(tmp_path):
    _commit_tree(tmp_path, {"README.md": "base\n"})
    _git(tmp_path, "checkout", "-qb", "pr")
    _commit_tree(tmp_path, {
        "entities/v1-alpha/gap-candidate-x1h2j3/candidates/capabilities-capability-gap-candidate-x1h2j3.yaml": RECORD,
    })
    assert _gate().check_admission_linkage(tmp_path, "main") == []


def test_cr006_cli_base_ref(tmp_path):
    _commit_tree(tmp_path, {"README.md": "base\n"})
    _git(tmp_path, "checkout", "-qb", "pr")
    _commit_tree(tmp_path, {"entities/v1-alpha/gap-candidate-x1h2j3/capabilities-capability-gap-candidate-x1h2j3.yaml": RECORD})
    # the gate script resolves REPO_ROOT from its own location; copy it into
    # the fixture scripts/ so REPO_ROOT == tmp_path
    scripts = tmp_path / "scripts"
    scripts.mkdir(exist_ok=True)
    shutil.copy(GATE_SRC, scripts / "check_cr_index.py")
    res = subprocess.run(
        [sys.executable, str(scripts / "check_cr_index.py"), "--base-ref", "main"],
        cwd=str(tmp_path), capture_output=True, text=True,
    )
    assert res.returncode == 1, res.stdout + res.stderr
    assert "CR-006" in res.stdout
