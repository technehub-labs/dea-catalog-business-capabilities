# Supplementary Admission Review v0.1: CAND-023 and CAND-029

CR-DEA-BC-02 execution; METHODOLOGY.md section 12 gates. Date: 2026-09-01.
Machine-readable: `admission-review-supplementary.yaml`. Supplements `admission-review.yaml` v0.1; review record, not a canonical transition.

## Why this review exists

The admission gate close-out (v0.1) deferred CAND-023 Resilience Management and CAND-029 Innovation Management with a named trigger: cross-industry corpus expansion. The corpus patch (PR #28; SRC-013 ISO 22301, SRC-014 BCI GPG 7.0, SRC-015 ISO 56002, SRC-016 Oslo Manual 2018) executed that trigger. This review re-runs both section 12 gates on the two candidates with the new evidence.

Honesty note: the named trigger also listed government, non-profit, and infrastructure reference models; the gaps closed on standards-body applicability claims instead. CAND-006 still requires government reference models proper (gap G5).

## Gate results

| Gate | CAND-023 Resilience Management | CAND-029 Innovation Management |
|---|---|---|
| Semantic: ability | met (continue delivery at predefined capacity during disruption; ISO 22301) | met (idea-to-value stream; ISO 56002) |
| Semantic: outcome | met (continuity of delivery, identifiable) | met (innovation introduced to market or brought into use; nationally surveyed per Oslo Manual) |
| Semantic: implementation independence | met (management-system framing by construction) | met (management-system framing by construction) |
| Semantic: naming | conformant | conformant |
| Semantic: anti-invention | first-order confirmed (pre-check v0.4; R-006) | first-order confirmed (pre-check v0.4; R-007) |
| Architectural: ECF | accepted (governance-existence x design; secondary operate) | accepted (product-offering x conceive; secondary design) |
| Architectural: record shape | conforms to entity.schema.json | conforms to entity.schema.json |
| Architectural: layering | no violation | no violation |
| **Overall** | **cleared_for_admission** | **cleared_for_admission** |

## Resolutions recorded

- **R-006** (CAND-023): deferral lifted; ISO 22301 draws the boundary against Risk (uncertainty treatment) and Security (protection); BCI GPG 7.0 carries the all-sector applicability claim; evidence E4, generality 8/10 strong
- **R-007** (CAND-029): deferral lifted; ISO 56002 draws the boundary against Change Management (innovation originates the new; change institutionalizes it); Oslo Manual 2018 names innovation management as a distinct activity class; evidence E4, generality 8/10 strong

## Effect

- Recommendation set grows from 23 to **25** pending steward acceptance
- Still deferred: CAND-006 (trigger: gap G5, government reference models) and CAND-018 (trigger: boundary delineation vs CAND-017, carried per N-009)
- The landed close-out v0.1 and admission review v0.1 stand unamended as historical records; this register supplements them

## Next

The admission PR for catalog entries 24 (Resilience Management) and 25 (Innovation Management) under the CR-DEA-BC-03 schema, citing this register and the full evidence trail (METHODOLOGY.md section 12: acceptance is recorded in the promotion PR).
