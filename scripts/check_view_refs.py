#!/usr/bin/env python3
"""Referential-integrity check for specialization views (CR-DEA-BC-04, D4).

Every specialization parent must resolve to a canonical capability id present
in entities/v1-alpha/ or to a specialization id present in the same view.
Schema shape is validated separately by the dsanders11 action; this script
checks what a schema cannot: cross-file references.

Usage: check_view_refs.py mappings/specializations/view-*.yaml
Exit 1 on any dangling parent reference.
"""
import glob
import sys

import yaml


def main() -> int:
    canonical = set()
    for path in glob.glob("entities/v1-alpha/capability-*.yaml"):
        canonical.add(yaml.safe_load(open(path))["id"])

    failures = 0
    for pattern in sys.argv[1:]:
        for path in sorted(glob.glob(pattern)):
            view = yaml.safe_load(open(path))
            local = {s["id"] for s in view.get("specializations", [])}
            for s in view.get("specializations", []):
                parent = s["parent"]
                if parent not in canonical and parent not in local:
                    print(f"FAIL  {path}: {s['id']} parent {parent} resolves nowhere")
                    failures += 1
            for cid in view.get("inherited", []):
                if cid not in canonical:
                    print(f"FAIL  {path}: inherited id {cid} not in the catalog")
                    failures += 1
            print(f"CHECK {path}: {len(view.get('specializations', []))} specializations, "
                  f"{len(view.get('inherited', []))} inherited, against {len(canonical)} canonical ids")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
