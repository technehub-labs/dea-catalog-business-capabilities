# CR-CATALOG-STRUCT-08: ECF Domain Enum v2.3.0 Migration

**Status**: Accepted
**Layer**: L1 (Business Capability Catalog)
**Owner**: TechNeHub Labs
**Depends on**: CR-DEA-BC-04 (ECF Overlay v0.2); CR-ECF-006; CR-MM-ECF-01; CR-BP-17 (companion migration in dea-catalog-processes)
**Related**: CR-CATALOG-STRUCT-03a/b (the research distribution slice that introduced the v0.2 overlay; pre-existing overlay re-derivation is parked as a follow-up); CR-DEA-BC-04 (the admission tranche; the v0.2 overlay that needs re-derivation)
**Supersedes**: nothing; the v0.2 overlay remains valid (the underlying work is unchanged; only the names shifted)
**Companion to**: CR-BP-17 (parallel migration in dea-catalog-processes; same v2.3.0 scope)
**Author**: Coder (for eaojnr)
**Date**: 2026-09-07

## What this CR is

This CR is the **carrier** for the v2.3.0 Domain enum migration in
`technehub-labs/dea-catalog-business-capabilities`. Five of the seven
canonical ECF Domains were renamed in the metaframework (CR-ECF-006 +
ADR-ECF-001); this repo is the **4th landing in the v2.3.0 wave**
(after metaframework, metamodel, and the process catalog).

The migration is a pure rename. The **ECF Overlay v0.2 re-derivation**
against the v2.3.0 Domain set is a separate task that follows this PR
— parked per eaojnr's direction but ready to dispatch. The overlay's
admitted candidates and dispositions are unchanged; only the names
they reference shift.

## Mapping

| Before (v2.2.0) | After (v2.3.0) |
|------------------|------------------|
| `governance-existence` / `GovernanceAndExistence` | `governance-existence` / `GovernanceAndExistence` (unchanged) |
| `supply-resources` / `SupplyAndResources` | `strategy-direction` / `StrategyAndDirection` |
| `agency-organization` / `AgencyAndOrganization` | `agency-organization` / `AgencyAndOrganization` (unchanged) |
| `customer-demand` / `CustomerAndDemand` | `party-relationship` / `PartyAndRelationship` |
| `product-offering` / `ProductAndOffering` | `product-value` / `ProductAndValue` |
| `operations-delivery` / `OperationsAndDelivery` | `enablement-operations` / `EnablementAndOperations` |
| `finance-value` / `FinanceAndValue` | `finance-accounting` / `FinanceAndAccounting` |

Lowercase `camelCase` (`partyRelationship`, etc.) for the `ecf:`
identifier suffixes also migrated.

## What changed in this repo

- **Schema enum** (`schemas/entity.schema.json`): the `domain` enum
  in `ecfConformance` updated to the v2.3.0 set.
- **CANON_DOMAINS in `scripts/check_ecf_conformance.py`**: 5 of 7
  values updated; the conformance check now PASS on 26 entries + MCSP
  view (verifies post-migration).
- **`DOMAIN_MAP` and `DOMAIN_ID` in `scripts/migrate_ecf_conformance.py`**:
  updated to the v2.3.0 kebab-case and lowerCamelCase mappings.
- **30 entity YAMLs** in `entities/v1-alpha/`: every `ecf.primary.domain`,
  `ecf.secondary.domain`, and `ecfConformance.canonicalReferences[].domain`
  updated to the v2.3.0 kebab-case and PascalCase values.
- **MCSP view** (`mappings/specializations/view-telecom-mcsp.yaml` +
  `VIEW-TELECOM-MCSP.md`): updated.
- **8 catalog-research files** in `catalog-research/`:
  `preliminary-ecf-overlay.yaml`, `admission-review.yaml`,
  `admission-review-supplementary.yaml`,
  `admission-gate-closeout.yaml`, `normalization.yaml`,
  `ECF-OVERLAY-v0.1.md`, `RESEARCH-REPORT-v0.1.md`,
  `ADMISSION-REVIEW-v0.1.md`, `ADMISSION-REVIEW-SUPPLEMENTARY-v0.2.md`.
  Every reference to the v2.2.0 Domain names updated to v2.3.0.
- **1 CR file** (`change-requests/CR-DEA-BC-03.md`): narrative updated.
- **1 doc file** (`docs/FOUNDATIONS.md`): narrative updated.
- **1 lib file** (`scripts/lib/grid.js`): the grid layout labels
  re-keyed to the v2.3.0 display form.

## What did NOT change

- **No new capabilities admitted.** This is a pure rename.
- **The 6 open conflict flags (CAND-008, 010, 017, 018, 019, 028)**
  deliberately held in v0.2 remain unchanged. Their disposition
  references are now keyed to the v2.3.0 Domain names but the
  rationales and decisions are unchanged.
- **The v0.2 ECF Overlay re-derivation** (re-running the candidate
  set against the v2.3.0 Domain taxonomy) is a separate task. The
  overlay's admitted candidates remain valid; the re-derivation is a
  quality improvement, not a correctness fix.
- **The 4 pre-existing build-script path bugs** (regenerate_catalog.py,
  check_catalog_index.py, migrate_ecf_conformance.py all look for
  `tools/catalog-index-schema.json` but the schema lives in
  `catalog-index-schema/`) are pre-existing and not introduced by
  this PR.

## Verification

- `scripts/check_ecf_conformance.py`: **PASS** (26 entries + MCSP view
  conform to ECF Conformance Gate).
- `scripts/check_versions.py` and `scripts/check_view_refs.py`: run as
  expected.
- **No tests directory** in this repo; validation is done via the
  scripts above (the standard pattern for the Business Capability
  catalog; see CR-DEA-BC-03).

## Pause-for-merge

Per CR-programme convention. After you say **Merge**, the v2.3.0
wave will be complete at the metaframework + metamodel + catalogs tier.

Nothing moves until you say Merge.
