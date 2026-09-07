#!/usr/bin/env python3
"""Visual domain-label conformance guard.

Follow-up to CR-DEA-BC-07 section 5: the v09 ECF coverage map shipped with all
seven domain axis labels in their pre-v2.3.0 forms, and the STRUCT-08/09 enum
migrations (which sweep code, schemas, entities, and docs) had no coverage for
display surfaces under `visuals/`. This script closes that gap.

Rules, applied to every `visuals/*.svg`:

  R1 (stale-label ban): no retired domain label may appear, in any casing or
     form (space, kebab, PascalCase, lowerCamelCase, display). The retired set
     is historical and constant: the five pre-v2.3.0 domains replaced by
     CR-ECF-006 (see CR-CATALOG-STRUCT-08) and the v2.3.0 Domain 3 replaced by
     CR-ECF-007 (see CR-CATALOG-STRUCT-09).

  R2 (axis completeness): an SVG that references 3 or more distinct canonical
     domains is a domain-axis visual (e.g. a coverage map) and must reference
     all seven. Visuals that cite one or two domains in passing (e.g. v08
     shows a single capability's primary coordinate) are exempt.

The canonical domain set is read from `schemas/entity.schema.json` (the
in-repo vocabulary of record), so the next enum wave only has to change the
schema and this guard follows.

Usage: check_visual_domain_labels.py
Exit 1 on any failure.
"""
import json
import re
import sys
from pathlib import Path

SCHEMA_PATH = "schemas/entity.schema.json"
VISUALS_GLOB = "visuals/*.svg"

# Retired domain labels. Historical constants; extend only when a future ECF
# wave retires another domain. Sources: CR-CATALOG-STRUCT-08 mapping table
# (v2.2.0 -> v2.3.0), dea-metaframework v2.4.0 release notes (CR-ECF-007).
STALE_TERMS = [
    # v2.2.0 forms retired by v2.3.0 (CR-ECF-006)
    "supply-resources", "SupplyAndResources", "supplyResources", "supply resources", "Supply & Resources",
    "customer-demand", "CustomerAndDemand", "customerDemand", "customer demand", "Customer & Demand",
    "product-offering", "ProductAndOffering", "productOffering", "product offering", "Product & Offering",
    "operations-delivery", "OperationsAndDelivery", "operationsDelivery", "operations delivery", "Operations & Delivery",
    "finance-value", "FinanceAndValue", "financeValue", "finance value", "Finance & Value",
    # v2.3.0 Domain 3 retired by v2.4.0 (CR-ECF-007)
    "people-organization", "PeopleAndOrganization", "peopleAndOrganization", "people organization", "People & Organization",
]

# An SVG referencing this many distinct canonical domains is treated as a
# domain-axis visual and must reference all seven (R2).
AXIS_THRESHOLD = 3


def find_canonical_kebab(schema: dict) -> list[str]:
    """Locate the seven-domain kebab-case enum inside the entity schema."""
    def walk(node):
        if isinstance(node, dict):
            enum = node.get("enum")
            if isinstance(enum, list) and "agency-organization" in enum:
                return enum
            for v in node.values():
                found = walk(v)
                if found:
                    return found
        elif isinstance(node, list):
            for v in node:
                found = walk(v)
                if found:
                    return found
        return None

    enum = walk(schema)
    if not enum or len(enum) != 7:
        print(f"FAIL: canonical seven-domain enum not found in {SCHEMA_PATH}")
        sys.exit(1)
    return sorted(enum)


def term_pattern(term: str) -> re.Pattern:
    # Literal match, case-insensitive, not embedded in a longer token.
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])", re.IGNORECASE)


def main() -> int:
    schema = json.loads(Path(SCHEMA_PATH).read_text())
    canonical_kebab = find_canonical_kebab(schema)

    # Canonical reference forms: kebab (as in v08) and space (as in v09).
    canonical_forms = []  # (domain, pattern)
    for dom in canonical_kebab:
        forms = {dom, dom.replace("-", " ")}
        canonical_forms.append((dom, re.compile(
            "|".join(r"(?<![A-Za-z0-9])" + re.escape(f) + r"(?![A-Za-z0-9])" for f in forms),
            re.IGNORECASE)))

    stale_patterns = [(t, term_pattern(t)) for t in STALE_TERMS]

    failures: list[str] = []
    svg_paths = sorted(Path(".").glob(VISUALS_GLOB))
    if not svg_paths:
        print(f"FAIL: no visuals found at {VISUALS_GLOB}")
        return 1

    for svg in svg_paths:
        text = svg.read_text(encoding="utf-8")
        for term, pat in stale_patterns:
            if pat.search(text):
                failures.append(f"{svg}: R1 stale domain label '{term}'")

        hits = {dom for dom, pat in canonical_forms if pat.search(text)}
        if len(hits) >= AXIS_THRESHOLD and len(hits) != 7:
            missing = sorted(set(canonical_kebab) - hits)
            failures.append(
                f"{svg}: R2 domain-axis visual references {len(hits)}/7 canonical "
                f"domains; missing: {', '.join(missing)}")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print(f"PASS: {len(svg_paths)} visuals conform to the canonical domain labels "
          f"({', '.join(canonical_kebab)}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
