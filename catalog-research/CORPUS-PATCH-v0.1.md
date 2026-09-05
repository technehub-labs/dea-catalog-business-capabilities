# Corpus Patch v0.1: Continuity and Innovation Sources; CAND-023/029 Fair Run

CR-DEA-BC-02; carry-forward from the distinctness sweep. Date: 2026-09-01.
Machine-readable: `evidence-register.yaml` v0.3, `enterprise-generality-matrix.yaml` v0.2, `admission-gate-precheck.yaml` v0.4. Research artifact; not the catalog.

## What the patch adds

Two source classes were missing for the two weakest-evidence candidates. Added four sources, all retrieved 2026-09-01:

| Source | Class | Grounds |
|---|---|---|
| SRC-013 ISO 22301:2019 (Business continuity management systems) | standards-body (new class) | CAND-023 identity, outcome, boundary, durability, generality |
| SRC-014 BCI Good Practice Guidelines 7.0 | professional-body (new class) | CAND-023 generality, durability |
| SRC-015 ISO 56002:2019 (Innovation management system) | standards-body | CAND-029 identity, outcome, boundary, generality |
| SRC-016 OECD/Eurostat Oslo Manual 2018 | government-guidance | CAND-029 identity, outcome, boundary, generality |

Corpus now covers 9 of 9 source classes.

## Fair run result

| Axis | CAND-023 Resilience | CAND-029 Innovation |
|---|---|---|
| Evidence | E2 → **E4** (4 external sources incl. ISO standard + professional body) | E2 → **E4** (ISO standard + intergovernmental measurement standard) |
| Boundary | gap → **met**: ISO 22301 draws it; continuity of delivery at predefined capacity vs risk treatment vs protection | gap → **met**: idea-to-value stream (ISO 56002); innovation originates the new, change institutionalizes it |
| Generality | gap → **met**: matrix row re-scored, 8 of 10 strong (retail and professional-services upgraded on BCI all-sector applicability + APQC 11.0 + DORA cascade) | gap → **met**: 8 of 10 strong (government and retail upgraded on ISO 56002 all-sectors scope + Oslo Manual cross-sector note) |
| Distinctness | met (sweep) | met (sweep) |

Both candidates now pass every gate axis on the pre-check.

## Why the re-score is honest, not convenient

1. **The upgraded cells cite explicit applicability claims**, not inference: BCI GPG 7.0 states applicability to all organizations regardless of size, industry sector, or geography; ISO 56002 states all types of organizations regardless of type, sector, or size. These are the strongest generality statements in the corpus
2. **The upgrades are conservative**: two cells per candidate, both from moderate to strong; non-profit and infrastructure stay moderate for innovation (the Oslo Manual is business-sector focused, and infrastructure innovation is less institutionalized)
3. **The deltas are documented per cell** in `enterprise-generality-matrix.yaml` v0.2 (`v02_delta` keys), so the change is auditable rather than silent

## Effect on the admission gate (pre-check v0.4)

- 27 on track; **25 clean on every axis** (was 23)
- Remaining gaps sit on exactly 2 candidates: CAND-006 Citizen/Member (evidence, generality, boundary; plus the deferred unification) and CAND-018 Analytics (boundary, carried per N-009)
- One pending artifact: CAND-005/006 unification decision (trigger: government reference models, gap G5)

## Carry-forward

1. Government reference models (gap G5): closes CAND-006 and the last pending distinctness artifact in one move
2. CAND-018 boundary work: Analytics vs Information, informed by N-009
3. Research report assembly (section 33 item 10, section 34 structure)
