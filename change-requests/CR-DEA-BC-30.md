# CR-DEA-BC-30: close gap G5; CAND-006 unification verdict (merged into CAND-005)

**Status**: Applied (2026-10-12)
**Filed**: 2026-10-12
**Author**: Emmanuel A. Otchere
**Recon**: `catalog-research/recon/INV-BC-30-v0.1.yaml`
**Trigger**: gap G5 closure; re-evaluation of the CAND-006 vs CAND-005 unification question carried forward from CR-DEA-BC-27 (N-026)
**Carrier documents**: this CR; `catalog-research/recon/INV-BC-30-v0.1.yaml`; `catalog-research/evidence-register.yaml` (SRC-026/027/028 + G5 closed); `catalog-research/candidates.yaml` (CAND-006 marked MERGED-INTO-CAND-005; universe_version 0.5.4); `catalog-research/normalization.yaml` (N-029; register_version 0.10.0)

## Summary

Three government reference models (TOGAF GRM, GoC BTEP GSRM, US FEA CRM v2.3) retrieved. All three converge on customer-vocabulary for the citizen interface; no distinct citizen-relationship capability is posited. CAND-006 (Citizen / Member Relationship) is merged into CAND-005 (Customer Management). The 29 first-order canonical count is unchanged. Gap G5 is closed.

## Decisions

- **N-029 verdict**: CAND-006 merged into CAND-005. No separate first-order canonical entry is admitted. Citizen is a customer-segment specialization under CAND-005.
- **evidence_strength E2 -> E4**: 3 independent new sources + 5 corpus sources; cross-source agreement.
- **Gap G5 status**: open -> closed-by-evidence.
- **CAND-006 classification**: CAPABILITY -> MERGED-INTO-CAND-005.

## Evidence trail

- SRC-026 (TOGAF Government Reference Model). 11 sectors, 3-level taxonomy. Sector "General Government (Customer Service, Customer Operations) and Local Services" uses CUSTOMER vocabulary for the citizen interface.
- SRC-027 (Government of Canada BTEP Government Service Reference Model). ~17 service types, no party-type distinction. Generic service-pattern vocabulary.
- SRC-028 (US OMB FEA Consolidated Reference Model v2.3). BRM names "Services for Citizens" but SRM section 5.1 is "Customer Services Domain". Machinery uses CUSTOMER vocabulary.

All three are independent of the BIZBOK/TOGAF/SAP LeanIX/IF4IT/APQC baseline corpus. The government reference-model class (a source class the baseline corpus did not sample from) is now represented.

## Follow-ons (out of scope of this CR)

- CAND-007 (Partner Relationship): not investigated; B2B specialization of CAND-005; same evidence path would apply.
- CAND-008 (Member Relationship): not investigated; membership-organization specialization of CAND-005; ASAE/AMC frameworks would inform.
- TER-RELMGMT-001: the original TER is now resolved at the structural level (N-018 grouping_parent + N-029 CAND-006 merge + CAND-005 admission pre-existing). The TER can be retired in a follow-on (TERs are a separate update; not part of this CR).

## Changes

- `catalog-research/evidence-register.yaml`:
  - SRC-026, SRC-027, SRC-028 added (3 new sources).
  - G5 status: open -> closed-by-evidence.
- `catalog-research/candidates.yaml`:
  - CAND-006 marked MERGED-INTO-CAND-005; merged_into_canonical_id; merged_cr.
  - CAND-006 evidence_strength E2 -> E4; confidence low -> high.
  - universe_version 0.5.3 -> 0.5.4.
- `catalog-research/normalization.yaml`:
  - N-029 added (verdict merged-into-CAND-005).
  - 25 -> 26 decisions.
  - register_version 0.9.0 -> 0.10.0.
  - deferred: [...] -> deferred: [] (the only deferred item is now resolved).
- `catalog-research/recon/INV-BC-30-v0.1.yaml`: new recon document.

## Gates

All 7 PASS post-change (naming, versions, ecf-conformance, view-refs, visual-domain-labels, catalog-index, id-system). CATALOG.yaml regenerated (32 entities; 29 canonical).

## Cross-references

- `catalog-research/recon/INV-BC-30-v0.1.yaml` (the full recon)
- `catalog-research/recon/INV-BC-27-v0.1.yaml` (the prior slice that deferred this)
- `change-requests/CR-DEA-BC-27.md` (parent slice)
- `change-requests/CR-DEA-BC-28.md` (the BC-SR-A001 P1 re-audit; reclassified Relationship Management P1 -> P2 at N-027)
- `submittal-reviews/BC-SR-A001.md` section 6 (P1-P2 Relationship Management)
- `submittal-reviews/TER-RELMGMT-001` (the original TER; to be retired in a follow-on)
