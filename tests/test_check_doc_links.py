"""Tests for scripts/check_doc_links.py (CR-DEA-BC-39 §6.1)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_doc_links.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("check_doc_links_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_external_and_anchor_links_skipped(tmp_path: Path):
    mod = _load_module()
    (tmp_path / "a.md").write_text("[x](https://example.com) [y](mailto:a@b.c) [z](#sec)\n")
    assert mod.find_broken_links(tmp_path) == []


def test_broken_relative_link_fires(tmp_path: Path):
    mod = _load_module()
    (tmp_path / "dir").mkdir()
    (tmp_path / "dir" / "a.md").write_text("[root](../README.md) [dead](../nope.md)\n")
    (tmp_path / "README.md").write_text("r\n")
    findings = mod.find_broken_links(tmp_path)
    assert len(findings) == 1
    assert findings[0]["rule"] == "DL-001"
    assert findings[0]["href"] == "../nope.md"


def test_fragment_on_existing_file_passes(tmp_path: Path):
    mod = _load_module()
    (tmp_path / "a.md").write_text("[x](b.md#section)\n")
    (tmp_path / "b.md").write_text("# B\n")
    assert mod.find_broken_links(tmp_path) == []


def test_url_encoded_target_resolves(tmp_path: Path):
    mod = _load_module()
    (tmp_path / "a.md").write_text("[x](my%20file.md)\n")
    (tmp_path / "my file.md").write_text("# M\n")
    assert mod.find_broken_links(tmp_path) == []


def test_cli_self_test_passes():
    r = subprocess_run("--self-test")
    assert r.returncode == 0, r.stdout + r.stderr


def subprocess_run(*args: str):
    import subprocess
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True, cwd=str(REPO_ROOT))
