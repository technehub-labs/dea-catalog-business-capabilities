# CR-DEA-BC-29: EPM rich-narrative backfill + VERSIONING.md metamodel_pin clarification

**Status**: Applied (2026-10-12)
**Filed**: 2026-10-12
**Author**: Coder (for eaojnr)
**Source**: CR-DEA-BC-26 follow-ons (recon INV-BC-26-v0.1 findings 6 and 7)
**Carrier documents**: this CR; `entities/v1-alpha/enterprise-performance-management-5fxren/` (backfill); `docs/VERSIONING.md` (§1.4 amendment)

## Summary

Two small fixes closing the BC-26 metamodel re-pinning audit findings, landed as one
CR because they are the complete follow-on set from that audit:

- **29a (entry backfill)**: `capability-enterprise-performance-management-5fxren`
  (admitted at BC-23) was the only one of the 29 canonical entries missing the 5
  rich-narrative fields (`non_examples`, `specialization`, `specialization_boundary`,
  `ecf_rationale`, `why_capability`). Backfilled in house style; version bumped
  1.0.0 -> 1.0.1. All 29 entries now carry the full narrative set.
- **29b (docs amendment)**: `docs/VERSIONING.md` §1.4 implied `metamodel_pin` tracks
  a dea-metaframework release version. The framework went 2.0.0 -> 2.5.0 with no 1.x
  release, so that reading is impossible. §1.4 amended to state explicitly that
  `metamodel_pin: 1.0.0` is the catalog-internal v1-alpha entry-shape contract pin;
  framework compatibility is asserted at the ECF contract level (§1.5).

## Findings addressed (from INV-BC-26-v0.1)

1. 28 of 29 entries carried the 5 rich-narrative fields; EPM was the exception
   (admitted under the post-mv1 compressed workflow at BC-23). Resolved by 29a.
2. VERSIONING.md §1.4 ambiguity on `metamodel_pin` semantics. Resolved by 29b.

## Observation recorded (not fixed here)

EPM's `boundary` field is a structured dict (`against_capabilities`, `loop_role`)
while the other 28 entries use a scalar prose string. The structured form is richer
(per-capability rationales) and all gates accept both shapes. Whether the scalar
shape should be generalized to the structured form (or the reverse) is a schema-level
decision for a future CR; this CR does not convert either direction.

## Changes

- `entities/v1-alpha/enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml`:
  added `specialization`, `why_capability`, `ecf_rationale`, `non_examples`,
  `specialization_boundary`; version 1.0.0 -> 1.0.1.
- `docs/VERSIONING.md`: §1.4 rewritten (metamodel_pin semantics clarified).

## Gates

All 7 PASS post-change (naming, versions, ecf-conformance, view-refs,
visual-domain-labels, catalog-index, id-system).

## Cross-references

- `catalog-research/recon/INV-BC-26-v0.1.yaml` (the audit that found both issues)
- `change-requests/CR-DEA-BC-26.md` (parent audit CR)
- `change-requests/CR-DEA-BC-23.md` (EPM admission)
- `docs/VERSIONING.md` §1.4, §1.5
