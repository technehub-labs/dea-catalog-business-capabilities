#!/usr/bin/env python3
"""Validate catalog entries/fixtures against a JSON Schema (draft-07).

Usage: validate_entries.py <schema.json> <glob> [<glob> ...]

Exit 0 when all matched files validate; exit 1 on any failure.
Globs that match nothing are reported and skipped (the entities/ tree is
legitimately empty until admission PRs land).
"""
import glob
import json
import sys

import yaml
from jsonschema import Draft7Validator


def main() -> int:
    schema_path = sys.argv[1]
    patterns = sys.argv[2:]
    schema = json.load(open(schema_path))
    validator = Draft7Validator(schema)

    failures = 0
    matched = 0
    for pattern in patterns:
        files = sorted(glob.glob(pattern, recursive=True))
        if not files:
            print(f"SKIP  {pattern} (no files)")
            continue
        for path in files:
            matched += 1
            doc = yaml.safe_load(open(path))
            errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
            if errors:
                failures += 1
                for e in errors:
                    where = ".".join(str(p) for p in e.path) or "(root)"
                    print(f"FAIL  {path}: {where}: {e.message}")
            else:
                print(f"PASS  {path}")
    print(f"---\n{matched} file(s) checked, {failures} failure(s), schema: {schema_path}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
