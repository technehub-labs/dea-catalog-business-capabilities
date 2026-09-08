#!/usr/bin/env python3
"""Naming and definition-shape lint for catalog entries (CR-DEA-BC-09).

Enforces the structurally checkable parts of TAXONOMY.md at CI time:

  Hard checks (exit 1 on any failure):
    H1. name is not verb-led (TAXONOMY section 1 rule 1: ability noun phrases;
        an imperative or work-verb opening names a process, not a capability)
    H2. name carries no disqualifying markers (rule 3: implementation-free;
        organization, system, vendor, or technology references)
    H3. name carries no outcome markers (rule 4: outcome-free)
    H4. name carries no industry qualifier (rule 5: industry-free at first order)
    H5. definition opens with "The ability to " (section 1A.1 template)
    H6. definition is a single sentence (section 1A.1)
    H7. outcome does not open with "The ability to " (section 1A.2: the outcome
        never restates the ability)

  Advisory (warn, non-blocking):
    A1. business-object anchoring heuristic (rule 2): warn when no token of the
        business_object appears in the name and no alias contains one. Rule 2
        is semantic, not literal (section 1 clarification, CR-DEA-BC-09), so
        this check can only advise. Known advisory set post-CR-DEA-BC-09:
        Strategy (Enterprise), Analytics and Intelligence (Insight),
        Enterprise Governance (Decision), Sourcing and Procurement (Purchase
        Order), Security Management (Asset/Information; N-015 retention).

Scope: canonical entries only (the subtree root file). State-directory files
(research/, candidates/, retired/) are not catalog entries and are skipped,
matching check_ecf_conformance.py's traversal rule (CR-CATALOG-STRUCT-01 §5).

Usage: check_naming.py [--strict]   (--strict promotes advisories to failures)
Exit codes: 0 pass, 1 failure.
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
ENT = REPO / "entities" / "v1-alpha"

# H1: imperative / work-verb openings. The capability name is a noun phrase;
# a verb opening is the process-catalog shape (Invoice Customer, Hire Employee).
VERB_LED = re.compile(
    r"^(Invoice|Hire|Fire|Run|Operate|Build|Make|Create|Sell|Buy|Pay|Deliver|"
    r"Manage|Plan|Design|Develop|Acquire|Conduct|Perform|Execute|Produce)\b",
    re.I,
)

# H2: disqualifying markers (rule 3). Vendor/system/organization references.
DISQUALIFYING = re.compile(
    r"\b(CRM|ERP|SAP|Oracle|Microsoft|Salesforce|Workday|Department|Division|"
    r"Platform|System|Tool|Software|Application|Database)\b",
    re.I,
)

# H3: outcome markers (rule 4). Results, states, and qualities the enterprise
# has are not names of abilities.
OUTCOME_MARKERS = re.compile(
    r"\b(Satisfaction|Efficiency|Effectiveness|Profitability|Performance|"
    r"Growth|Quality|Compliance|Resilience)\b",
    re.I,
)

# H4: industry qualifiers (rule 5). First-order names are industry-free.
INDUSTRY_QUALIFIERS = re.compile(
    r"\b(Telecom|Telecommunications|Banking|Insurance|Retail|Healthcare|"
    r"Government|Manufacturing|MCSP|Utilities|Energy|Pharma|Automotive)\b",
    re.I,
)

# H5: definition template opening (section 1A.1).
DEFINITION_OPENING = "The ability to "

# H7: outcome must not restate the ability (section 1A.2).
OUTCOME_RESTATEMENT = "The ability to"


def is_state_dir_file(path: str) -> bool:
    parts = Path(path).parts
    return any(p in ("research", "candidates", "retired") for p in parts)


def check_entry(doc: dict, fp: str, errors: list, warnings: list) -> None:
    cid = doc.get("id") or fp
    name = doc.get("name") or ""
    definition = (doc.get("definition") or "").replace("\n", " ").strip()
    outcome = (doc.get("outcome") or "").replace("\n", " ").strip()
    business_object = doc.get("business_object") or ""
    aliases = doc.get("aliases") or []

    if VERB_LED.search(name):
        errors.append(f"{cid}: name '{name}' is verb-led (TAXONOMY 1.1)")
    m = DISQUALIFYING.search(name)
    if m:
        errors.append(
            f"{cid}: name '{name}' carries disqualifying marker '{m.group(0)}' (TAXONOMY 1.3)"
        )
    m = OUTCOME_MARKERS.search(name)
    if m:
        errors.append(
            f"{cid}: name '{name}' carries outcome/state marker '{m.group(0)}' (TAXONOMY 1.4)"
        )
    m = INDUSTRY_QUALIFIERS.search(name)
    if m:
        errors.append(
            f"{cid}: name '{name}' carries industry qualifier '{m.group(0)}' (TAXONOMY 1.5)"
        )
    if not definition.startswith(DEFINITION_OPENING):
        errors.append(
            f"{cid}: definition does not open with 'The ability to ' (TAXONOMY 1A.1)"
        )
    # Single-sentence check: no internal sentence boundary ('. ' after a word
    # char). Terminal period is required by convention but not enforced here.
    if re.search(r"\w\.\s+\w", definition):
        errors.append(f"{cid}: definition is not a single sentence (TAXONOMY 1A.1)")
    if outcome.startswith(OUTCOME_RESTATEMENT):
        errors.append(
            f"{cid}: outcome restates the ability (TAXONOMY 1A.2: outcome is a result, not the ability)"
        )

    # A1 (advisory): business-object anchoring heuristic.
    if business_object and name:
        tokens = [t.lower() for t in re.split(r"[/\s]+", business_object) if len(t) >= 4]
        haystacks = [name.lower()] + [a.lower() for a in aliases]
        anchored = any(
            any(t in h or h_part in t for h in haystacks for h_part in h.split())
            for t in tokens
        )
        if not anchored:
            warnings.append(
                f"{cid}: business_object '{business_object}' not echoed in name '{name}' "
                f"or aliases (advisory; TAXONOMY 1.2 is semantic, rule 6 plainness may govern)"
            )


def main() -> int:
    strict = "--strict" in sys.argv
    files = sorted(glob.glob(str(ENT / "**" / "*.yaml"), recursive=True))
    files = [
        f
        for f in files
        if "/README" not in f and "/readme" not in f and not is_state_dir_file(f)
    ]
    errors: list[str] = []
    warnings: list[str] = []
    for fp in files:
        try:
            doc = yaml.safe_load(open(fp))
        except yaml.YAMLError as ex:
            errors.append(f"{fp}: YAML parse error: {ex}")
            continue
        if not doc:
            errors.append(f"{fp}: empty document")
            continue
        check_entry(doc, fp, errors, warnings)

    for w in warnings:
        print(f"WARN: {w}", file=sys.stderr)
    if errors:
        print(f"FAIL: {len(errors)} naming/definition error(s):", file=sys.stderr)
        for e in errors:
            print(" -", e, file=sys.stderr)
        return 1
    if strict and warnings:
        print(f"FAIL: {len(warnings)} advisory warning(s) under --strict:", file=sys.stderr)
        for w in warnings:
            print(" -", w, file=sys.stderr)
        return 1
    print(
        f"PASS: {len(files)} entries conform to TAXONOMY naming and definition-shape rules"
        f" ({len(warnings)} advisory warning(s))."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
