# CR-DEA-BC-32: CAND-007/CAND-008 retirement (already-canonical; CAND-004 cell closed)

**Status**: Applied (2026-10-12)
**Filed**: 2026-10-12
**Author**: Emmanuel A. Otchere
**Recon**: `catalog-research/recon/INV-BC-32-v0.1.yaml`
**Carrier documents**: this CR; `catalog-research/candidates.yaml` (CAND-007, CAND-008 marked CAPABILITY-CANONICAL); `catalog-research/normalization.yaml` (N-031, N-032; register_version 0.12.0)

## Summary

The CAND-004 (Relationship Management grouping_parent) research cell is closed. CAND-007 (Supplier Management) and CAND-008 (Partner Management) are already canonical first-order capabilities (admitted 2026-09-01 at the v1-alpha baseline); the stale candidate records are retired. With this CR, all four CAND-004 children are resolved and no live candidate children remain.

## Findings

1. **CAND-007 (Supplier Management)**: canonical at `capabilities:capability-supplier-management-d6fuj4` (admitted 2026-09-01, E4 evidence, full ladder passage). The Track C dependency note on the canonical entry is voided by N-030 (opt 2: no parent admitted); no follow-on migration CR applies.
2. **CAND-008 (Partner Management)**: canonical at `capabilities:capability-partner-management-cp3vdb` (admitted 2026-09-01, E3 evidence, full ladder passage). Distinct from Supplier Management (supply base) and Customer Management (demand side) per the canonical boundary.
3. **CAND-004 (grouping_parent)**: all four children now resolved (CAND-005 admitted at v1-alpha.0; CAND-006 merged into CAND-005 at N-029; CAND-007 and CAND-008 retired as already-canonical at this CR). The grouping_parent record is retained as the research-register structural artifact per N-007 / N-018.

## Decisions

- **N-031**: CAND-007 retired as already-canonical (Supplier Management). Verdict: `retired`. Same pattern as N-025 (CAND-005).
- **N-032**: CAND-008 retired as already-canonical (Partner Management). Verdict: `retired`. Same pattern as N-025 (CAND-005).

## Changes

- `catalog-research/candidates.yaml`:
  - CAND-007 marked CAPABILITY-CANONICAL; canonical_id pointer; promotion_history entry; notes updated.
  - CAND-008 marked CAPABILITY-CANONICAL; canonical_id pointer; promotion_history entry; notes updated.
  - CAND-004 notes updated: all four children resolved; grouping_parent record retained as the research-register structural artifact.
  - universe_version 0.5.4 -> 0.5.5.
- `catalog-research/normalization.yaml`:
  - N-031, N-032 added (both verdict `retired`).
  - 27 -> 29 decisions. register_version 0.11.0 -> 0.12.0. cr + compiled lineage extended.
- `catalog-research/recon/INV-BC-32-v0.1.yaml`: new recon document.

## Gates

All 7 PASS post-change (naming, versions, ecf-conformance, view-refs, visual-domain-labels, catalog-index, id-system). CATALOG.yaml regenerated (32 entities; 29 canonical).

## Cross-references

- `catalog-research/recon/INV-BC-32-v0.1.yaml` (the full recon)
- `change-requests/CR-DEA-BC-27.md` (N-025; the CAND-005 stale-record precedent)
- `change-requests/CR-DEA-BC-30.md` (N-029; the CAND-006 merge)
- `change-requests/CR-DEA-BC-31.md` (N-030; the TER-RELMGMT-001 retirement that closes Track C)
