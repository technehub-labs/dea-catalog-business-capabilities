# CR-DEA-BC-31: TER-RELMGMT-001 retirement (resolved-retired, opt 2)

**Status**: Applied (2026-10-12)
**Filed**: 2026-10-12
**Author**: Coder (for eaojnr)
**Recon**: `catalog-research/recon/INV-BC-31-v0.1.yaml`
**Trigger**: TER-RELMGMT-001 (Track C; Relationship Management generic parent) is now structurally resolvable at the completion of the N-018 / N-025 / N-029 decision chain
**Carrier documents**: this CR; `catalog-research/recon/INV-BC-31-v0.1.yaml`; `catalog-research/evidence-register.yaml` (TER-RELMGMT-001 resolution block); `catalog-research/normalization.yaml` (N-030; register_version 0.11.0)

## Summary

TER-RELMGMT-001 (registered 2026-09-10 under CR-DEA-BC-13 D.3) is retired as resolved. All three open evidence questions are answered by the completed N-018 / N-025 / N-029 decision chain:

- **Q1 (durable business object)**: No. CAND-004 reclassified to grouping_parent per N-018 (boundary test fails; no boundary for the generic parent that is not exactly the union of its children).
- **Q2 (parent-child relationship)**: opt 2 (abstract grouping only). CAND-005 admitted at v1-alpha.0 (N-025 retired the stale record). CAND-006 merged into CAND-005 (N-029). CAND-007 and CAND-008 remain uninvestigated under the grouping parent.
- **Q3 (enterprise-generality)**: The generic parent did not survive. The object-specific child (Customer Management) did, with cross-source convergence (BIZBOK, TOGAF, SAP LeanIX, IF4IT, APQC, and the government reference-model class via SRC-026/027/028).

## Decisions

- **N-030 verdict**: TER-RELMGMT-001 status: `evidence-pending` -> `resolved-retired` (opt 2; abstract grouping only).
- **No further action** on the generic-parent question. CAND-007 and CAND-008 recon, when scheduled, open new TERs (TER-PARTNER-001, TER-MEMBER-001) if evidence is non-trivial.

## Evidence trail (the closed chain)

- **N-018** (2026-09-30): CAND-004 (Relationship Management) reclassified from first-order candidate to grouping_parent. The admission-gate boundary test fails for the aggregate.
- **N-025** (2026-10-12, CR-DEA-BC-27): CAND-005 (Customer Management) stale candidate record retired; the canonical entity at `capabilities:capability-customer-management-f3n8wb` is the source of truth (admitted at v1-alpha.0, 2026-09-02, E5).
- **N-029** (2026-10-12, CR-DEA-BC-30): CAND-006 (Citizen / Member Relationship) merged into CAND-005. Evidence E2 -> E4 via three government reference models (TOGAF GRM SRC-026, GoC BTEP GSRM SRC-027, US FEA CRM v2.3 SRC-028). All three converge on customer-vocabulary for the citizen interface.
- **N-030** (2026-10-12, this CR): TER-RELMGMT-001 retired. All three open questions answered.

## Follow-ons (out of scope)

- CAND-007 (Partner Relationship, B2B specialization) recon: not part of this CR.
- CAND-008 (Member Relationship, membership-org specialization) recon: not part of this CR.

## Changes

- `catalog-research/evidence-register.yaml`: TER-RELMGMT-001 `resolution` block added (closed_on, closing_cr, verdict, answers, status, note). Status: `evidence-pending` -> `resolved-retired`. Three closure evidence sources (SRC-026/027/028) recorded under `sources_consulted`.
- `catalog-research/normalization.yaml`: N-030 added. 26 -> 27 decisions. `register_version: 0.10.0 -> 0.11.0`. `cr` field extended with the BC-26/27/28/29/30/31 lineage. `compiled` field extended with v0.11 entry.
- `catalog-research/recon/INV-BC-31-v0.1.yaml`: new recon document.

## Gates

All 7 PASS post-change (naming, versions, ecf-conformance, view-refs, visual-domain-labels, catalog-index, id-system). CATALOG.yaml regenerated (32 entities; 29 canonical).

## Cross-references

- `catalog-research/recon/INV-BC-31-v0.1.yaml` (the full recon)
- `catalog-research/recon/INV-BC-30-v0.1.yaml` (G5 closure; the SRC-026/027/028 evidence that answered Q3)
- `change-requests/CR-DEA-BC-30.md` (N-029; CAND-006 merge)
- `change-requests/CR-DEA-BC-27.md` (N-025; CAND-005 stale-record retirement)
- `change-requests/CR-DEA-BC-18.md` (N-018; CAND-004 reclassification to grouping_parent)
- `submittal-reviews/BC-SR-A001.md` (section 6: P1-P2 Relationship Management)
- `submittal-reviews/TER-RELMGMT-001` (the original TER; resolved at this CR)
