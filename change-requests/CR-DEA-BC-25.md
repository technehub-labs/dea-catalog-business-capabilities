# CR-DEA-BC-25: H3 outcome-marker linter patch (governance-object exemption)

**Status**: Applied (2026-10-12); 5 advisories (1 new EPM governance-object advisory + 4 pre-existing business-object anchoring advisories); N-024 review-retained verdict retired; linter parity restored

**Filed**: 2026-10-12
**Author**: Emmanuel A. Otchere
**Depends on**: CR-DEA-BC-23 (EPM admission; the trigger), CR-DEA-BC-09 (the original review-retained mechanism for Security Management N-015), CR-DEA-BC-20 (H8 noun-as-ability rule 7; the linter already has the review-retained exemption wired for H8)
**Carrier documents**: `scripts/check_naming.py` (linter patch), `catalog-research/normalization.yaml` (N-024 retired; register_version 0.7.0 -> 0.8.0; cr + compiled lines extended)

## Problem statement

The H3 (rule 4 outcome-free) check in `scripts/check_naming.py` lists `Performance` as a known outcome/state marker. The list was inherited from the BC-09 era and has been a known false-positive source: the word "Performance" is the noun-of-product in "Enterprise Performance Management" (and in "Performance Management" generally), not an outcome state. Other words in the same list (`Risk`, `Insight`, `Information`, `Continuity`) are also governance-object nouns, but they have not been the subject of a false positive in the existing catalog because no entry has a name that puts one of those words in the position where H3 would match (e.g. no "Risk Improvement" entry exists).

BC-23 (admission of Enterprise Performance Management) was the trigger: H3 fired on the word "Performance" in the canonical name, and N-024 was recorded as a review-retained verdict to exempt EPM from H3 by way of the H8 review-retained exemption (which BC-23 extended to the H3 path as a bridge). The right fix is to address the false positive at the source: the linter should distinguish "Performance in 'Performance Management' is the object of governance" from "Performance in 'Performance Improvement' is an outcome state". BC-25 is that fix.

## Recon summary

The H3 path in `scripts/check_naming.py` (CR-DEA-BC-23 commit 9e99ad6) reads:

```python
m = OUTCOME_MARKERS.search(name)
if m:
    is_retained_outcome = review_retained is not None and cid in review_retained
    if not is_retained_outcome:
        errors.append(
            f"{cid}: name '{name}' carries outcome/state marker '{m.group(0)}' (TAXONOMY 1.4)"
        )
```

The OUTCOME_MARKERS regex lists `Satisfaction|Efficiency|Effectiveness|Profitability|Performance|Growth|Quality|Compliance|Resilience`. The first 9 are clearly outcome-state markers (e.g. "Satisfaction" is a state, not a governance object). `Quality` and `Resilience` are also outcome-state markers AND governance-object nouns (Quality Management and Resilience Management/Continuity Management are both real patterns); the BC-25 patch keeps them in the deny-by-default list per the conservative set principle. `Performance` is the false-positive source: it is a governance-object noun, and "Performance Management" is the canonical name in BSC/OKR/OMG BPM literature.

## The patch

The H3 path is extended with a Gate 1 (governance-object exemption) that fires before Gate 2 (review-retained). Gate 1 emits a WARN instead of an error when the marker is the last word of the head noun of a "[Word(s)] Management" name and the last word is in the GOVERNANCE_OBJECTS set.

```python
GOVERNANCE_OBJECTS = frozenset(
    {"Risk", "Insight", "Information", "Continuity", "Performance"}
)
GOVERNANCE_OBJECT_NAME_RE = re.compile(
    r"^([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)*)\s+Management$"
)
```

The regex captures the head noun of "[Word(s)] Management" names. The patch checks `go_match.group(1).split()[-1] in GOVERNANCE_OBJECTS` — that is, the **last word** of the head noun. This is correct for "Enterprise Performance Management" (head "Enterprise Performance" -> last word "Performance" -> GO; emit WARN, not error) and for "Risk Management" (head "Risk" -> GO). It correctly denies for "Quality Management" (head "Quality" -> Quality not in GOVERNANCE_OBJECTS -> error) and for "Performance Improvement" (no Management suffix -> error).

## Side-effects

### Files modified (BC-25 slice)

- `scripts/check_naming.py`:
  - Added `GOVERNANCE_OBJECTS = frozenset({"Risk", "Insight", "Information", "Continuity", "Performance"})`
  - Added `GOVERNANCE_OBJECT_NAME_RE = re.compile(r"^([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)*)\s+Management$")`
  - Modified H3 path: Gate 1 (governance-object exemption) emits WARN for the 5 GO cases; Gate 2 (review-retained) is unchanged and remains as a safety net for non-GO cases.
- `catalog-research/normalization.yaml`:
  - N-024 retired (no longer needed; the linter is fixed).
  - register_version 0.7.0 -> 0.8.0.
  - cr field extended with CR-DEA-BC-19 + CR-DEA-BC-23 + CR-DEA-BC-25 references.
  - compiled line extended with v0.8 entry recording the BC-25 close-out.
  - 22 -> 21 decisions.

### Files NOT modified

- `entities/v1-alpha/enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml` (no change; the EPM entity is unchanged)
- All 28 other canonical entities (no change; the patch is linter-only)
- `reconciliation/migration-id-map.yaml` (no change; EPM was admitted at BC-23)
- `catalog-research/candidates.yaml` (no change; CAND-037 already admitted)
- `catalog-research/evidence-register.yaml` (no change; TER-EPM-001 already admitted)
- `catalog-research/distinctness-sweep.yaml` (no change)
- `CATALOG.yaml` (no change; 32 entities unchanged)
- `CHANGELOG.md` (no change; the BC-25 patch is a tooling change, not a catalog change; the per-CR CHANGELOG blocks are reserved for catalog changes)
- `README.md` (no change; same reason)
- `mappings/specializations/view-telecom-mcsp.yaml` and `.md` (no change)
- Capability map (no change; 29 entities, 31 cells unchanged)

## Affected entries (post-patch, advisory only)

The 5 governance-object Management entries now have an H3 advisory (WARN, not error). The H3 advisory joins the existing 4 business-object anchoring advisories (Enterprise Governance, Security Management, Sourcing and Procurement, Strategy Formulation) for a total of 5 advisories on the linter run.

| Entry | Pre-BC-25 H3 status | Post-BC-25 H3 status |
|---|---|---|
| `capability-risk-management-h9uxdw` | PASS (Risk not in OUTCOME_MARKERS) | PASS (H3 advisory suppressed because not in OUTCOME_MARKERS) |
| `capability-insight-management-ms4n9d` | PASS (Insight not in OUTCOME_MARKERS) | PASS (H3 advisory suppressed) |
| `capability-information-management-6vjgdh` | PASS (Information not in OUTCOME_MARKERS) | PASS (H3 advisory suppressed) |
| `capability-continuity-management-v3rn6u` | PASS (Continuity not in OUTCOME_MARKERS) | PASS (H3 advisory suppressed) |
| `capability-enterprise-performance-management-5fxren` | ERROR at BC-23 (N-024 review-retained verdict exempted) | PASS with new H3 governance-object advisory |
| `capability-quality-management` (hypothetical; does not exist) | ERROR (Quality in OUTCOME_MARKERS; no review-retained) | ERROR (Quality not in GOVERNANCE_OBJECTS; default-deny preserved) |

## Gates (post-patch, all PASS)

- `check_naming.py`: 29 entries (5 advisories; +1 from BC-23; same 4 pre-existing business-object advisories). H3 false positive on EPM resolved at the source.
- `check_versions.py`: 29 entries.
- `check_ecf_conformance.py`: 29 + MCSP view.
- `check_view_refs.py`: clean.
- `check_visual_domain_labels.py`: 9 visuals.
- `check_catalog_index.py`: 32 entities.
- `check_id_system.py`: IDM-001..007 CONFORMANT.

## Acceptance criteria

- [x] GOVERNANCE_OBJECTS set defined with 5 entries: Risk, Insight, Information, Continuity, Performance.
- [x] GOVERNANCE_OBJECT_NAME_RE regex defined; matches "[Word(s)] Management" names.
- [x] H3 path emits WARN (not error) for the 5 GO cases.
- [x] H3 path emits error for non-GO outcome-marker words in Management names (Quality Management, Performance Improvement, etc.).
- [x] H3 review-retained path retained as a safety net (Gate 2).
- [x] N-024 retired from normalization.yaml.
- [x] register_version 0.7.0 -> 0.8.0.
- [x] cr and compiled lines extended.
- [x] All 7 structural gates PASS post-commit.
- [x] 29 canonical entities + 3 candidates + 32 CATALOG.yaml (unchanged from BC-23).
- [x] No new canonical entity, no view change, no CHANGELOG block (linter patch is tooling-only).

## Cross-references

- `change-requests/CR-DEA-BC-23.md` (the trigger; N-024 was a bridge)
- `change-requests/CR-DEA-BC-09.md` (N-015 review-retained precedent; the review-retained mechanism this patch keeps as a safety net)
- `change-requests/CR-DEA-BC-20.md` (H8 noun-as-ability rule 7; the linter already had the review-retained exemption wired for H8)
- `catalog-research/normalization.yaml` (N-024 retired; cr + compiled extended)
- `scripts/check_naming.py` (H3 path extended; GOVERNANCE_OBJECTS + GOVERNANCE_OBJECT_NAME_RE)
