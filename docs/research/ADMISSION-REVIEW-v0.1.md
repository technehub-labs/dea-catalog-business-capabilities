# Admission Review v0.1: Gate Record for the Recommendation Set

CR-DEA-BC-02 execution: the two review gates of METHODOLOGY.md section 12, executed on the 23-candidate recommendation set (gate close-out v0.1). Machine-readable twin: `admission-review.yaml`. Date: 2026-09-01.

Status: review record. This register clears candidates for admission; the canonical transition executes in the admission PR after steward acceptance. Reviewer of record: Coder (for eaojnr).

## Gate results

**23 reviewed, 23 cleared, 0 held.**

Every candidate passed both gates:

- **Semantic gate**: hard gates (Ability, Outcome, Implementation Independence) re-confirmed from the section 38 record; naming conformance per TAXONOMY.md section 1 (ability noun phrases, industry-free, implementation-free); anti-invention classification re-confirmed.
- **Architectural gate**: ECF mapping decision per candidate (below); record shape conformance against `schemas/entity.schema.json` (CR-DEA-BC-03); layering boundaries respected (no WSF, metaframework, or metamodel redefinition).

## Conflict-flag resolutions (review-time decisions)

Five of the six open ECF conflict flags belonged to recommended candidates and are resolved here:

| ID | Candidate | Decision | Rationale (abbreviated) |
|---|---|---|---|
| R-001 | CAND-008 Partner Management | Defensible as recorded | Partnering is first initiated when the enterprise conceives demand-side relationships; supply-side operation is legitimate participation. Dual-home tension expressed, not smoothed. |
| R-002 | CAND-010 Marketing | Defensible as recorded | N-002 settled placement (Marketing distinct from Customer and Offering); primary customer-demand x conceive is honest. |
| R-003 | CAND-017 Information Management | Defensible; secondaries deliberately empty | The span of information across domains is a property of the business object, not of initiation. Enumerating all domains would violate honest-not-exhaustive. |
| R-004 | CAND-019 Technology Management | N-006 resolved: business capability, business object Technology; ECF legitimately absent | Enterprise-general ability (technology investment, lifecycle, sourcing). No ECF domain carries technology (L5 concern); the section 38 legitimately-absent clause covers this exactly. Entry carries `held_unmapped` with note. |
| R-005 | CAND-028 Change Management | Defensible as recorded | Earliest initiation governance-existence x improve; cross-domain applicability is an object property, not a mapping defect. |

The sixth flag belongs to **CAND-018 Analytics and Intelligence**, which is not in the recommendation set; its flag is owned by its deferral (boundary delineation against CAND-017) and is out of scope here.

## What happens next

The admission PR writes the 23 entries into `entities/v1-alpha/`, each carrying: the CR-DEA-BC-03 record shape, its evidence trail (SRC/CAND/N references), the full ladder passage including the `reviewed` transition recorded here, and the `canonical` transition executed by that PR. Entry CI (validate-entries) must be green.

## Carry-forward (unchanged)

- G5 corpus gap (government reference models): moves CAND-006/023/029/035.
- CAND-018 boundary delineation: targeted decision.
- Overlay regeneration to v0.2 (applies N-007/N-008 and R-001..R-005 to the map).
- U1-U3 upstream findings to dea-metamodel.
