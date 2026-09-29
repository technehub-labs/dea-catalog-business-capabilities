#!/usr/bin/env python3
"""Naming and definition-shape lint for catalog entries (CR-DEA-BC-09, extended by CR-DEA-BC-20).

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
    H8. name is a recognized noun-as-ability pattern (section 1 rule 7,
        CR-DEA-BC-20): X Management / X Planning / X Design / X Enablement /
        X Stewardship / X Formulation / X Governance / X Conduct / X Oversight /
        X Acquisition / X Development / X Sourcing / X Procurement / X Marketing
        / gerund pair / single-word gerund. Exemption: entries registered as
        verdict: review-retained in catalog-research/normalization.yaml are
        exempt (N-015 Security Management, N-019 Enterprise Governance).

  Advisory (warn, non-blocking):
    A1. business-object anchoring heuristic (rule 2): warn when no token of the
        business_object appears in the name and no alias contains one. Rule 2
        is semantic, not literal (section 1 clarification, CR-DEA-BC-09), so
        this check can only advise. Known advisory set post-CR-DEA-BC-20:
        Analytics and Intelligence (Insight; moved to CR-DEA-BC-21 recon).

Scope: canonical entries only (the subtree root file). State-directory files
(research/, candidates/, retired/) are not catalog entries and are skipped,
matching check_ecf_conformance.py's traversal rule (CR-CATALOG-STRUCT-01 section 5).

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

# H8: noun-as-ability pattern library (TAXONOMY section 1 rule 7,
# CR-DEA-BC-20). The last token of the name must be one of these OR the
# full name must match the gerund-pair or single-gerund patterns.
NOUN_AS_ABILITY_SUFFIXES = {
    "Management", "Planning", "Design", "Enablement", "Stewardship",
    "Formulation", "Governance", "Conduct", "Oversight", "Acquisition",
    "Development", "Sourcing", "Procurement", "Marketing",
}
GERUND_PAIR = re.compile(r"^[A-Z][a-z]+(?:\s+(?:and|of|the)\s+[A-Z][a-z]+)+$")
SINGLE_GERUND = re.compile(r"^[A-Z][a-z]+ing$")


def is_state_dir_file(path: str) -> bool:
    parts = Path(path).parts
    return any(p in ("research", "candidates", "retired") for p in parts)


def load_review_retained_registry() -> set[str]:
    """Load entry ids registered as verdict: review-retained in the
    normalization register. These entries are exempt from H8 (noun-as-ability)
    per TAXONOMY section 1 rule 7 (CR-DEA-BC-20 section 6.2).

    The normalization register stores decisions as a list of dicts under the
    top-level `decisions` key. A review-retained decision may carry the
    affected entry id in either of two fields:
      - affected_entry: dea:capability-<slug>  (explicit override)
      - id: dea:capability-<slug>             (when the decision itself is
                                                keyed by the entry id)
    Decisions keyed by N-NNN + CAND-NNN are mapped via candidates.yaml.
    """
    reg_path = REPO / "catalog-research" / "normalization.yaml"
    if not reg_path.exists():
        return set()
    try:
        doc = yaml.safe_load(open(reg_path))
    except yaml.YAMLError:
        return set()
    if not doc:
        return set()

    # CAND-NNN -> entry id map. candidates.yaml records admitted candidates
    # with a canonical_entry pointer; this is the authoritative mapping.
    candidates_yaml = REPO / "catalog-research" / "candidates.yaml"
    cand_to_entry: dict[str, str] = {}
    if candidates_yaml.exists():
        try:
            cdoc = yaml.safe_load(open(candidates_yaml))
        except yaml.YAMLError:
            cdoc = None
        if isinstance(cdoc, dict):
            for c in cdoc.get("candidates") or []:
                if not isinstance(c, dict):
                    continue
                cand_id = c.get("id") or c.get("candidate")
                if cand_id and c.get("canonical_entry"):
                    cand_to_entry[str(cand_id)] = str(c["canonical_entry"])

    retained: set[str] = set()
    decisions = doc.get("decisions") or []
    if isinstance(decisions, list):
        for d in decisions:
            if not isinstance(d, dict):
                continue
            if (d.get("verdict") or "").strip().lower() != "review-retained":
                continue
            cid = d.get("id") or d.get("entry_id")
            if isinstance(cid, str) and cid.startswith("dea:capability-"):
                retained.add(cid)
            affected = d.get("affected_entry") or d.get("entry")
            if isinstance(affected, str) and affected.startswith("dea:capability-"):
                retained.add(affected)
            for c in d.get("candidates") or []:
                cstr = str(c)
                if cstr in cand_to_entry:
                    retained.add(cand_to_entry[cstr])
    return retained


def is_noun_as_ability(name: str) -> bool:
    """Check if `name` matches a recognized noun-as-ability pattern.

    TAXONOMY section 1 rule 7 (CR-DEA-BC-20). The check accepts:
      - Last token in NOUN_AS_ABILITY_SUFFIXES (X Management, X Planning, ...)
      - Single-word gerund matching SINGLE_GERUND (e.g., Marketing)
      - Gerund-pair matching GERUND_PAIR (e.g., Sourcing and Procurement)
    """
    if not name:
        return False
    tokens = name.strip().split()
    if not tokens:
        return False
    last = tokens[-1]
    if last in NOUN_AS_ABILITY_SUFFIXES:
        return True
    if SINGLE_GERUND.match(name.strip()):
        return True
    if GERUND_PAIR.match(name.strip()):
        return True
    return False


def check_entry(
    doc: dict, fp: str, errors: list, warnings: list,
    review_retained: set[str] | None = None,
) -> None:
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

    # H8 (TAXONOMY 1 rule 7, CR-DEA-BC-20): noun-as-ability structural test.
    # Exempt entries are review-retained in normalization.yaml.
    is_retained = review_retained is not None and cid in review_retained
    if not is_retained and not is_noun_as_ability(name):
        errors.append(
            f"{cid}: name '{name}' does not match a recognized noun-as-ability pattern "
            f"(TAXONOMY 1 rule 7; register an N-NNN review-retained exemption in "
            f"catalog-research/normalization.yaml to override)"
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
    review_retained = load_review_retained_registry()
    for fp in files:
        try:
            doc = yaml.safe_load(open(fp))
        except yaml.YAMLError as ex:
            errors.append(f"{fp}: YAML parse error: {ex}")
            continue
        if not doc:
            errors.append(f"{fp}: empty document")
            continue
        check_entry(doc, fp, errors, warnings, review_retained=review_retained)

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
