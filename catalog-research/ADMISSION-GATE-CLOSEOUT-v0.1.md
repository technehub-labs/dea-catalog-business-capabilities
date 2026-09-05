# Admission Gate Close-out v0.1: Section 38 Recommendations

CR-DEA-BC-02 close-out: per-candidate evaluation against the section 38 canonical admission gate. Machine-readable twin: `admission-gate-closeout.yaml`. Date: 2026-09-01.

Status: candidate-not-canonical. This artifact **recommends**; it admits nothing. Final canonical admission remains subject to review (CR section 38; METHODOLOGY.md section 12). Supersedes `admission-gate-precheck.yaml` as the section 38 record; the pre-check remains the dry-run history.

## The gate

A candidate may be recommended only if all ten axes pass: evidence >= E3, classification = CAPABILITY, enterprise-generality demonstrated, durability demonstrated, implementation-independence demonstrated, outcome identifiable, boundary defensible, distinctness demonstrated, specialization not required for interpretation, ECF mapping defensible or legitimately absent.

Inputs: pre-check v0.3, preliminary ECF overlay v0.1, enterprise-generality matrix v0.1, distinctness sweep v0.1, normalization register v0.2, candidate universe v0.2, evidence register v0.2.

## Recommended for canonical admission (23)

All ten axes met on current evidence. ECF primary coordinate per overlay v0.1 (earliest-initiation rule); conflicts flagged, not smoothed (CR section 26) ride into the review package.

| Candidate | Name | ECF primary (domain x stage) | ECF conflict flag |
|---|---|---|---|
| CAND-001 | Strategy | governance-existence x conceive |  |
| CAND-002 | Strategic Planning | governance-existence x conceive |  |
| CAND-003 | Enterprise Governance | governance-existence x conceive |  |
| CAND-005 | Customer Management | customer-demand x operate |  |
| CAND-007 | Supplier Management | supply-resources x build |  |
| CAND-008 | Partner Management | customer-demand x conceive | flagged |
| CAND-009 | Offering Management | product-offering x conceive |  |
| CAND-010 | Marketing | customer-demand x conceive | flagged |
| CAND-012 | Operations | operations-delivery x operate |  |
| CAND-013 | Financial Stewardship | finance-value x conceive |  |
| CAND-014 | Financial Management | finance-value x operate |  |
| CAND-015 | Workforce Management | people-organization x build |  |
| CAND-016 | Workforce Planning | people-organization x design |  |
| CAND-017 | Information Management | operations-delivery x operate | flagged |
| CAND-019 | Technology Management | ? x ? | flagged |
| CAND-020 | Risk Management | governance-existence x conceive |  |
| CAND-021 | Compliance Management | governance-existence x activate |  |
| CAND-022 | Legal Management | governance-existence x conceive |  |
| CAND-024 | Security Management | governance-existence x design |  |
| CAND-025 | Sourcing and Procurement | supply-resources x build |  |
| CAND-026 | Asset Management | supply-resources x build |  |
| CAND-027 | Facility Management | supply-resources x activate |  |
| CAND-028 | Change Management | governance-existence x improve | flagged |

Full coordinates per candidate: `admission-gate-closeout.yaml` (machine-checkable against `preliminary-ecf-overlay.yaml`).

## Deferred (4)

Not recommended in this pass. Gaps are carried, not resolved (conservative re-test rule); each deferral names its trigger.

| Candidate | Name | Carried gaps | Trigger |
|---|---|---|---|
| CAND-006 | Citizen / Member Relationship | evidence_ge_E3; enterprise_generality; boundary_defensible; distinctness (pending unification decision) | Government reference models (gap G5): CAND-005/CAND-006 unification decision deferred; evidence below E3 on the current corpus |
| CAND-018 | Analytics and Intelligence | boundary_defensible | Boundary delineation decision against CAND-017 Information Management; N-009 re-test closed confirming status quo, boundary objection carried |
| CAND-023 | Resilience Management | evidence_ge_E3; enterprise_generality; boundary_defensible | Cross-industry corpus expansion (government, non-profit, infrastructure reference models); E2 evidence held pending cross-industry check |
| CAND-029 | Innovation Management | evidence_ge_E3; enterprise_generality; boundary_defensible | Same as CAND-023 |

## Removed from the admission track (2)

| Candidate | Name | Disposition |
|---|---|---|
| CAND-004 | Stakeholder Relationship Management | Reclassified grouping parent (N-007); withdrawn from the admission track; boundary gap resolved by reclassification |
| CAND-011 | Value Delivery | Dissolved as first-order candidate (N-008); rejected aggregate; boundary gap resolved by dissolution |

## Rejected: non-capability constructs (4)

Classification rejections from the candidate universe; referred to their correct homes per the distinctions table (METHODOLOGY.md section 3).

| Candidate | Name | Classification | Correct home |
|---|---|---|---|
| CAND-030 | Finance Department | ORGANIZATION | Organization constructs (actor catalogs) |
| CAND-031 | Invoice Processing | PROCESS | dea-catalog-processes |
| CAND-032 | CRM System | SYSTEM | System catalog |
| CAND-033 | Customer Service Team | ACTOR | dea-catalog-actors |

## Specialized (1)

| Candidate | Name | Disposition |
|---|---|---|
| CAND-034 | Telecom Customer Management | Industry specialization view (CR-DEA-BC-04); parent: CAND-005 Customer Management. Industry forms never enter the first-order set. |

## Unresolved (1)

| Candidate | Name | Note |
|---|---|---|
| CAND-035 | Common Good Production | Classification unresolved between capability and outcome; trigger: non-profit and government reference models. Carried to the research report open-questions section. |

## Summary

| Measure | Count |
|---|---|
| Universe total | 35 |
| Admission-track candidates | 27 |
| Recommended for admission | 23 |
| Deferred | 4 |
| Removed from track | 2 |
| Rejected (non-capability) | 4 |
| Specialized | 1 |
| Unresolved | 1 |

## DoD rows closed by this artifact

- Canonical admission recommendations documented (CR section 39).
- Rejected and deferred candidates documented (CR section 39).

Remaining CR-DEA-BC-02 DoD rows after this phase: specialization register (section 33 item 9; CAND-034 plus specialization-boundary findings), unresolved questions roll-up, research report (section 34 structure), visual research artifacts (section 35), OTCHERE-only canonical examples check.
