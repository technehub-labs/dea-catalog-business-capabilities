"""Tests for scripts/check_cr_index.py (CR-DEA-BC-39 §6.2)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_cr_index.py"


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
