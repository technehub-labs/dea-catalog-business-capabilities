# CR-CATALOG-STRUCT-09: ECF Domain Enum v2.4.0 Migration (Agency & Organization)

**Status**: Accepted
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-07
**Depends on**: CR-CATALOG-STRUCT-08 (v2.3.0 migration carrier); dea-metaframework CR-ECF-007; dea-metamodel CR-MM-ECF-02
**Related**: dea-metaframework ADR-ECF-002; dea-catalog-processes CR-BP-18

## 1. What this CR is

This CR is the **v2.4.0 migration carrier** for `technehub-labs/dea-catalog-business-capabilities`. ECF Domain 3 is renamed from `PeopleAndOrganization` (v2.3.0) to `AgencyAndOrganization` (v2.4.0), driven by the Substrate Independence Stress Test (`dea-metaframework` ADR-ECF-002 §5; CR-ECF-007). The domain must remain semantically valid whether the enterprise's internal agents are biological (humans), artificial (AI systems, autonomous software agents), or hybrid.

The change is a **single Domain rename**; the other six Domains and the cardinality of the seven-Domain × seven-Stage matrix are unchanged. No content redistribution is required (CR-ECF-007 §6.3): all content that previously belonged to `People & Organization` remains in `Agency & Organization`.

## 2. Mapping

| Old form (v2.3.0) | New form (v2.4.0) |
|---|---|
| `PeopleAndOrganization` (PascalCase) | `AgencyAndOrganization` |
| `people-organization` (kebab-case) | `agency-organization` |
| `People & Organization` (display) | `Agency & Organization` |

## 3. Files changed

- **1 schema**: `schemas/entity.schema.json` (kebab-case domain enum).
- **3 check/conformance scripts**: `scripts/check_ecf_conformance.py` (CANON_DOMAINS), `scripts/migrate_ecf_conformance.py` (DOMAIN_MAP), `scripts/lib/grid.js` (DOMAINS id; display labels also corrected: see §5).
- **26 entity YAMLs** under `entities/v1-alpha/` (domain field re-keyed where applicable).
- **7 catalog-research files**: `ECF-OVERLAY-v0.1.md`, `ECF-OVERLAY-v0.2.md`, `RESEARCH-REPORT-v0.1.md`, `ADMISSION-GATE-CLOSEOUT-v0.1.md`, `admission-gate-closeout.yaml`, `ecf-overlay-v0.2.yaml`, `preliminary-ecf-overlay.yaml`.
- **2 CR records** touched (CR-DEA-BC-03, CR-CATALOG-STRUCT-08).
- **1 new CR record**: this file (CR-CATALOG-STRUCT-09).
- **1 CHANGELOG section**: `[2.4.0-migration] - 2026-09-07`.

Total: **39 files modified** + 1 new CR + 1 CHANGELOG section.

## 4. Verification

- `scripts/check_ecf_conformance.py`: **PASS** (26 entries + MCSP view conform to ECF Conformance Gate).
- `scripts/check_versions.py`: **PASS** (26 entries conform to CR-DEA-BC-05 version discipline).
- `scripts/check_view_refs.py`: **PASS** (exit 0).

## 5. Pre-existing bug fixed in passing

`scripts/lib/grid.js` `DOMAINS` display labels were stale from pre-v2.3.0 (`party-relationship` displayed `Customer Demand`; `strategy-direction` displayed `Supply Resources`; etc.). The v2.3.0 migration (CR-CATALOG-STRUCT-08) updated the `id` fields but not the `display` fields. This CR corrects all seven display labels to the v2.4.0 canonical names. The fix is in scope here because the Domain-3 display label (`People Organization` -> `Agency & Organization`) is part of this migration, and leaving the other six stale would have shipped an internally inconsistent artifact.

## 6. What did NOT change

- The cardinality of the seven Domains (7), the matrix M = D × S (49 coordinates), and the no-cell-filling rule are unchanged.
- The v2.3.0 renames (CR-CATALOG-STRUCT-08) are unchanged.
- No entity directory names are renamed (none encode the domain).
- No content redistribution is required (CR-ECF-007 §6.3).

## 7. Backward compatibility

`dea-metaframework` v2.4.0 preserves the deprecated identifiers in `tools/ecf_coordinates.py:DOMAIN_ALIASES` for at least 2 release cycles.
