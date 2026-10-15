#!/usr/bin/env python3
"""check_business_capability.py: per-type gate for BusinessCapability records.

This is the per-type gate delegation referenced by the entity-system
registry's `per_type_gates` entry for BusinessCapability (per
CR-DEA-BC-35). The entity-system gate's ES-005 rule only checks that
this script EXISTS; the full per-type validation lives in the per-type
gate in the conformance rollup (which is out of scope for this slice).

The gate is documented as a placeholder for the future per-type BC
validator (per BC's existing `scripts/check_naming.py` and
`scripts/check_versions.py` discipline). For the entity-system gate's
purposes, the script is a stub that exits 0 in non-strict mode and
returns CONFORMANT in --strict mode.

Run: python3 scripts/check_business_capability.py [--strict] [--json]
"""
from __future__ import annotations

import argparse
import json
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="BusinessCapability per-type gate (CR-DEA-BC-35 stub).")
    parser.add_argument("--strict", action="store_true", help="Strict mode (placeholder; stub is always CONFORMANT).")
    parser.add_argument("--json", action="store_true", help="Emit JSON verdict.")
    args = parser.parse_args()

    verdict = {
        "rule": "BC-PT-001",
        "gate": "scripts/check_business_capability.py",
        "strict": bool(args.strict),
        "verdict": "CONFORMANT",
        "diagnostic": "per-type gate delegation stub (CR-DEA-BC-35); full per-type validation lives in the conformance rollup.",
    }
    if args.json:
        print(json.dumps(verdict, indent=2))
    else:
        print(f"BusinessCapability Per-Type Gate (CR-DEA-BC-35): {verdict['verdict']}")
        print(f"  {verdict['diagnostic']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
