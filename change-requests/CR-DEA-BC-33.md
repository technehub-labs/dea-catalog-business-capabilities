# CR-DEA-BC-33: per-cell ECF placement review (29 populated cells; no movements)

**Status**: Applied (2026-10-12)
**Filed**: 2026-10-12
**Author**: Emmanuel A. Otchere
**Recon**: `catalog-research/recon/INV-BC-33-v0.1.yaml`
**Trigger**: BC-28 surfaced the per-cell placement review as the only remaining BC-SR-A001 sub-question; this CR closes it
**Carrier documents**: this CR; `catalog-research/recon/INV-BC-33-v0.1.yaml`; updated `ecf_rationale` notes on Supplier Management and Partner Management

## Summary

Per-cell placement review of the 29/49 populated ECF cells against the CR-DEA-BC-13 §A semantic-center-of-gravity rule. **All 29 entries are aligned with one of the four heuristics; no movements required.** Two narrative updates (Supplier Management v1.2.0 -> 1.2.1; Partner Management v1.1.0 -> 1.1.1) reflect closure of the Track C dependency at N-030 (no parent admitted per opt 2); no placement change.

## Method

- Rule source: CR-DEA-BC-13 §A semantic-center-of-gravity (the primary coordinate marks the capability's defining work, not where its lifecycle begins).
- Heuristics: (1) sustained stewardship -> operate; (2) posture / constitutive decision -> conceive; (3) designed artifact / pattern / build phase -> design or build; (4) activation / enforcement -> activate.
- Three automated checks: (1) all 29 entries carry a BC-13 / semantic-center-of-gravity reference in the ecf_rationale field; (2) by-name dominant heuristic classification aligns with the current primary coordinate for all 29 entries; (3) no cell placement predates the rule without a recorded re-evaluation note.

## Findings

- **F1**: All 29 entries carry an explicit BC-13 / semantic-center-of-gravity reference in `ecf_rationale`. No entry is un-documented post-BC-13. EPM's `ecf_rationale` was backfilled at CR-DEA-BC-29.
- **F2**: All 29 entries align with one of the four heuristics under the rule. No misplacements detected.
- **F3**: Track C dependency notes on Supplier Management (`party-relationship/operate`) and Partner Management (`party-relationship/conceive`) carried a "may become a specialization in a follow-on migration CR" note. Track C closed 2026-10-12 at N-030 (opt 2: no parent admitted); the notes are voided. The placements themselves are unchanged; only the dependency notes are updated.

## Decision

- **No movements required.** The 29 populated cells are confirmed against the rule.
- Supplier Management `ecf_rationale` updated to reflect Track C closure; version 1.2.0 -> 1.2.1.
- Partner Management `ecf_rationale` updated to reflect Track C closure; version 1.1.0 -> 1.1.1.

## Sample of the review table (29 rows in the recon)

| name | primary | heuristic | verdict |
|---|---|---|---|
| Asset Management | enablement-operations/operate | 1 (stewardship) | aligned |
| Change Management | governance-existence/improve | 1 (stewardship; the change is sustained at improve) | aligned |
| Continuity Management | governance-existence/design | 3 (designed pattern) | aligned |
| Customer Management | party-relationship/operate | 1 | aligned |
| Enterprise Governance | governance-existence/conceive | 2 (constitutive) | aligned |
| Enterprise Performance Management | strategy-direction/operate | 1 (direction-loop closure) | aligned |
| Marketing | party-relationship/conceive | 2 (demand creation is constituted) | aligned |
| Regulation Management | governance-existence/activate | 4 (activation) | aligned |
| Supplier Management | party-relationship/operate | 1 (supply base management) | aligned |
| Technology Management | strategy-direction/build | 3 (technology estate) | aligned |
| ... | ... | ... | ... |

The full 29-row table is in `catalog-research/recon/INV-BC-33-v0.1.yaml`.

## Changes

- `entities/v1-alpha/supplier-management-d6fuj4/capabilities-capability-supplier-management-d6fuj4.yaml`: `ecf_rationale` updated to reflect Track C closure (N-030); no placement change. Version 1.2.0 -> 1.2.1.
- `entities/v1-alpha/partner-management-cp3vdb/capabilities-capability-partner-management-cp3vdb.yaml`: `ecf_rationale` updated to reflect Track C closure (N-030); no placement change. Version 1.1.0 -> 1.1.1.
- `catalog-research/recon/INV-BC-33-v0.1.yaml`: new recon document.

## Gates

All 7 PASS post-change (naming, versions, ecf-conformance, view-refs, visual-domain-labels, catalog-index, id-system). CATALOG.yaml regenerated (32 entities; 29 canonical).

## Cross-references

- `catalog-research/recon/INV-BC-33-v0.1.yaml` (the full review)
- `change-requests/CR-DEA-BC-13.md` (the rule source; §A semantic-center-of-gravity)
- `change-requests/CR-DEA-BC-28.md` (BC-SR-A001 P1 re-audit; surfaced this review)
- `change-requests/CR-DEA-BC-29.md` (EPM backfill; the backfilled `ecf_rationale` was a prerequisite)
- `change-requests/CR-DEA-BC-31.md` (N-030; the Track C closure that voided the Supplier/Partner dependency notes)
