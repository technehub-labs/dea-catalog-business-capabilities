#!/usr/bin/env python3
"""
migrate_to_new_ids.py
CR-DEA-BC-mv1: id system migration (org-wide Wave 2, flat-layout repo).

Rewrites every canonical record's id from the legacy `dea:capability-*` /
`dea:candidate-*` form to `capabilities:capability-<slug>-<hash>` /
`capabilities:candidate-<slug>-<hash>` (hash per dea-metaframework
docs/id-system.md section 2.5), moves every entity directory to the
flat-layout form `<slug>-<hash>/`, rewrites every structured
cross-reference repo-wide, generates a README.md per entity dir
(IDM-007), and emits the migration id map.

Usage:
  python scripts/migrate_to_new_ids.py [--dry-run] [--execute]

Idempotent: re-running on a migrated tree no-ops (no legacy ids found).
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "entities" / "v1-alpha"
RECONCILIATION = ROOT / "reconciliation"

NAMESPACE = "capabilities"
BASE32 = "abcdefghjkmnpqrstuvwxyz23456789"

LEGACY_PREFIXES = ("dea:capability-", "dea:candidate-")

# Structured YAML files whose id references are rewritten (markdown
# artifacts are bannered verbatim instead; see CR-DEA-BC-mv1).
STRUCTURED_SWEEP = (
    "mappings/",
    "schemas/fixtures/",
    "catalog-research/",
)


def _content_hash(text: str) -> str:
    h = hashlib.sha256(text.encode("utf-8")).digest()
    val = int.from_bytes(h[:4], "big")
    chars = []
    for _ in range(6):
        chars.append(BASE32[val % 31])
        val //= 31
    return "".join(reversed(chars))


def _new_id(old_id: str, content: str) -> str:
    for prefix in LEGACY_PREFIXES:
        if old_id.startswith(prefix):
            level = prefix[len("dea:"):-1]
            slug = old_id[len(prefix):]
            return f"{NAMESPACE}:{level}-{slug}-{_content_hash(content)}"
    raise ValueError(f"Unknown legacy id form: {old_id}")


def _dir_name(new_id: str) -> str:
    """entities/v1-alpha/<dir>/ for a new id: id minus '<ns>:<level>-'."""
    body = new_id.split(":", 1)[1]
    return body.split("-", 1)[1]


def _file_name(new_id: str) -> str:
    return new_id.replace(":", "-").lower() + ".yaml"


def _rewrite_text(text: str, id_map: dict[str, str]) -> str:
    """Replace every legacy id occurrence (whole-token) via the id map."""
    for old in sorted(id_map, key=len, reverse=True):
        text = re.sub(rf"(?<![a-z0-9:-]){re.escape(old)}(?![a-z0-9-])",
                      lambda _: id_map[old], text)
    return text


def _collect_records() -> list[dict]:
    """Enumerate canonical capability records and candidate records."""
    out = []
    for d in sorted(ENTITIES.iterdir()):
        if not d.is_dir() or not d.name.startswith("dea:"):
            continue
        if d.name.startswith("dea:capability-"):
            canonical = d / f"{d.name}.yaml"
            if canonical.is_file():
                out.append({"kind": "capability", "dir": d,
                            "yaml": canonical,
                            "old_id": f"dea:capability-{d.name[len('dea:capability-'):]}"})
        elif d.name.startswith("dea:candidate-"):
            for cand in sorted((d / "candidates").glob("*.yaml")):
                data = yaml.safe_load(cand.read_text())
                out.append({"kind": "candidate", "dir": d,
                            "yaml": cand,
                            "old_id": data.get("id", "")})
    return out


def _readme(record: dict, new_id: str, kind: str) -> str:
    name = record.get("name", new_id)
    definition = str(record.get("definition", "")).strip()
    first_sentence = definition.split(". ")[0].strip()
    if first_sentence and not first_sentence.endswith("."):
        first_sentence += "."
    coord = ""
    ecf = record.get("ecf") or {}
    primary = ecf.get("primary") or {}
    if primary.get("domain"):
        coord = (f"\n**ECF primary coordinate**: {primary['domain']} / "
                 f"{primary.get('stage', '?')}\n")
    return (
        f"# {name}\n\n"
        f"**Level**: BusinessCapability ({kind})\n"
        f"**Record id**: `{new_id}`\n{coord}\n"
        f"{first_sentence}\n"
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    p.add_argument("--execute", action="store_true",
                   help="apply changes (default is dry-run)")
    args = p.parse_args()

    records = _collect_records()
    if not records:
        print("No legacy records found; tree already migrated (no-op).")
        return 0

    # Pass 1: compute the id map (hash of the pre-migration canonical text).
    id_map: dict[str, str] = {}
    for rec in records:
        content = rec["yaml"].read_text()
        id_map[rec["old_id"]] = _new_id(rec["old_id"], content)

    dupes = [i for i in id_map.values() if list(id_map.values()).count(i) > 1]
    if dupes:
        print(f"FATAL: hash collision in new ids: {sorted(set(dupes))}")
        return 2

    print(f"Records to migrate: {len(records)}")
    if not args.execute:
        for old, new in sorted(id_map.items()):
            print(f"  {old} -> {new}")
        print("Dry run. Re-run with --execute to apply.")
        return 0

    # Pass 2: rewrite + move every entity dir.
    for rec in records:
        old_id = rec["old_id"]
        new_id = id_map[old_id]
        old_dir = rec["dir"]
        new_dir = ENTITIES / _dir_name(new_id)

        # Rewrite the canonical/candidate record text (id + refs).
        text = rec["yaml"].read_text()
        text = _rewrite_text(text, id_map)
        data = yaml.safe_load(text)
        data["id"] = new_id
        # Re-dump would churn formatting; instead patch the id line in text.
        text = re.sub(rf"^id: {re.escape(old_id)}$", f"id: {new_id}",
                      text, count=1, flags=re.M)

        if old_dir != new_dir:
            old_dir.rename(new_dir)
        if rec["kind"] == "capability":
            target = new_dir / _file_name(new_id)
            (new_dir / rec["yaml"].name).rename(target)
            (new_dir / "README.md").write_text(_readme(data, new_id, "canonical"))
        else:
            target = new_dir / "candidates" / rec["yaml"].name
            (new_dir / "README.md").write_text(_readme(data, new_id, "candidate"))
        target.write_text(text)

    # Pass 3: sweep structured YAML fixtures/mappings/research registers.
    for sub in STRUCTURED_SWEEP:
        base = ROOT / sub
        if not base.exists():
            continue
        for f in sorted(base.rglob("*.yaml")):
            new_text = _rewrite_text(f.read_text(), id_map)
            if new_text != f.read_text():
                f.write_text(new_text)

    # Pass 4: emit the id map.
    RECONCILIATION.mkdir(exist_ok=True)
    lines = [
        "version: 1",
        f"namespace: {NAMESPACE}",
        "migrated_at: '2026-09-21'",
        "carrier_cr: CR-DEA-BC-mv1",
        "id_map:",
    ]
    for old, new in sorted(id_map.items()):
        lines.append(f"  {old}: {new}")
    lines.append("known_residuals: []")
    (RECONCILIATION / "migration-id-map.yaml").write_text(
        "\n".join(lines) + "\n")

    print(f"Migrated {len(records)} records. Id map: "
          f"reconciliation/migration-id-map.yaml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
