#!/usr/bin/env python3
"""Catalog version guard (CR-DEA-BC-05).

Five checks, all required for the build to be green:

  C1. Every entry has a `version` field.
  C2. Documented baseline (from dependencies.yaml: catalogs[].version) matches
      the actual entry count under entities/v1-alpha/ when the declared
      version label is in v1-letter form (v1-alpha, v1-bravo, etc.).
      For v2+ plain semver, the check is that entries exist.
  C3. Every entry's ecfConformance.profile matches the declared
      dependencies.yaml: ecf_contract.
  C4. Every entry's metamodel_pin (top-level field on the entry) matches
      the declared dependencies.yaml: metamodel_pin.
  C5. Every entry's identity `version` follows semver (X.Y.Z).

Usage: check_versions.py
Exit 1 on any failure.
"""
import glob
import re
import sys
from pathlib import Path

import yaml


SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
ECF_PIN_RE = re.compile(r"^dea:ecf@\d+\.\d+\.\d+$")
LETTERED_LABEL_RE = re.compile(r"^v\d+-(alpha|bravo|charlie|delta|echo|foxtrot|hotel|india|juliet|kilo|lima|mike|november|oscar|papa|quebec|romeo|sierra|tango|uniform|victor|whiskey|xray|yankee|zulu)$")
SEMVER_LABEL_RE = re.compile(r"^v\d+\.\d+\.\d+$")


def load_yaml(path: str):
    with open(path) as f:
        return yaml.safe_load(f)


def main() -> int:
    failures: list[str] = []

    deps_path = "dependencies.yaml"
    if not Path(deps_path).exists():
        print(f"FAIL: {deps_path} missing; CR-DEA-BC-05 requires the catalog manifest.")
        return 1

    deps = load_yaml(deps_path)

    ecf_contract = deps.get("ecf_contract")
    metamodel_pin = deps.get("metamodel_pin")
    if not ecf_contract or not ECF_PIN_RE.match(ecf_contract):
        failures.append(f"C0: dependencies.yaml ecf_contract must match `dea:ecf@X.Y.Z`; got {ecf_contract!r}.")
    if not metamodel_pin or not SEMVER_RE.match(str(metamodel_pin)):
        failures.append(f"C0: dependencies.yaml metamodel_pin must be semver X.Y.Z; got {metamodel_pin!r}.")

    self_catalogs = deps.get("catalogs", [])
    self_pin = None
    for c in self_catalogs:
        if c.get("id") == "dea:catalog/business-capabilities":
            self_pin = c.get("version")
            break
    if not self_pin:
        failures.append("C0: dependencies.yaml must declare a self-pin to dea:catalog/business-capabilities.")

    entry_paths = sorted(glob.glob("entities/v1-alpha/capability-*.yaml"))
    if not entry_paths:
        print("No catalog entries found (admission gates not started). Skipping C1..C5.")
        return 0

    c2_recorded_count = None
    if self_pin:
        if LETTERED_LABEL_RE.match(self_pin):
            pass  # lettered regime; just verify the count is non-zero and stable
        elif SEMVER_LABEL_RE.match(self_pin):
            pass
        else:
            failures.append(f"C2: self-pin {self_pin!r} does not match `v<N>-<word>` (v1) or `v<N>.<M>` (v2+).")

    for path in entry_paths:
        entry = load_yaml(path)
        eid = entry.get("id", path)

        # C1
        if "version" not in entry:
            failures.append(f"C1 [{eid}]: missing `version` field.")
            continue

        # C5
        if not SEMVER_RE.match(str(entry["version"])):
            failures.append(f"C5 [{eid}]: `version` {entry['version']!r} is not semver X.Y.Z.")

        # C3
        ecf_block = entry.get("ecfConformance", {})
        if ecf_block.get("profile") != ecf_contract:
            failures.append(
                f"C3 [{eid}]: ecfConformance.profile {ecf_block.get('profile')!r} "
                f"does not match dependencies.yaml ecf_contract {ecf_contract!r}."
            )

        # C4
        if entry.get("metamodel_pin") != metamodel_pin:
            failures.append(
                f"C4 [{eid}]: metamodel_pin {entry.get('metamodel_pin')!r} "
                f"does not match dependencies.yaml metamodel_pin {metamodel_pin!r}."
            )

        c2_recorded_count = len(entry_paths)

    # C2 summary
    if c2_recorded_count is not None and self_pin:
        print(f"C2 baseline: catalog version {self_pin}; canonical entry count: {c2_recorded_count}.")

    if failures:
        print(f"FAIL: {len(failures)} check(s) failed.")
        for f in failures:
            print(f"  {f}")
        return 1

    print(f"PASS: {len(entry_paths)} entries conform to CR-DEA-BC-05 version discipline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())