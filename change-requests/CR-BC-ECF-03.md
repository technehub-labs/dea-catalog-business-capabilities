# CR-BC-ECF-03: ECF Domain Enum v2.5.0 Migration (Domain 6 Enablement & Operations)

**Status**: Accepted
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-08
**Depends on**: CR-CATALOG-STRUCT-08 (v2.3.0 migration carrier); CR-CATALOG-STRUCT-09 (v2.4.0 migration carrier); dea-metaframework CR-ECF-008; dea-metamodel CR-MM-ECF-03
**Related**: dea-metaframework ADR-ECF-003; dea-catalog-processes CR-BP-23

## 1. What this CR is

This CR is the **v2.5.0 migration carrier** for `technehub-labs/dea-catalog-business-capabilities`. ECF Domain 6 is renamed from `OperationsAndEnablement` (v2.4.0) to `EnablementAndOperations` (v2.5.0), driven by the Domain/Stage Orthogonality Stress Test (`dea-metaframework` ADR-ECF-003 §5; CR-ECF-008). The Domain 6 name shared a lexical root with Stage 5 `Operate`, obscuring the orthogonality that the ECF requires between the Domain axis and the Stage axis. The rename swaps the two nouns: `Enablement` now leads (lexically distinct from any Stage name) and `Operations` trails (the sustained day-to-day concern, not the lifecycle Stage).

The change is a **single Domain rename**; the other six Domains and the cardinality of the seven-Domain × seven-Stage matrix are unchanged. No content redistribution is required (CR-ECF-008 §3.5): all content that previously belonged to `Operations & Enablement` remains in `Enablement & Operations`.

## 2. Mapping

| Old form (v2.4.0) | New form (v2.5.0) |
|---|---|
| `OperationsAndEnablement` (PascalCase canonical domain value) | `EnablementAndOperations` |
| `operations-enablement` (kebab-case in enum) | `enablement-operations` |
| `operationsEnablement` (lowerCamelCase identifier suffix in `ecf:operationsEnablement.<stage>`) | `enablementAndOperations` |
| `Operations & Enablement` (display form) | `Enablement & Operations` |

## 3. Files changed

- **1 schema**: `schemas/entity.schema.json` (kebab-case domain enum).
- **3 check/conformance scripts**: `scripts/check_ecf_conformance.py` (CANON_DOMAINS), `scripts/migrate_ecf_conformance.py` (DOMAIN_MAP), `scripts/lib/grid.js` (DOMAINS id; display labels also corrected — see §5).
- **26 entity YAMLs** under `entities/v1-alpha/` (domain field re-keyed where applicable).
- **7 catalog-research files**: `ECF-OVERLAY-v0.1.md`, `ECF-OVERLAY-v0.2.md`, `RESEARCH-REPORT-v0.1.md`, `ADMISSION-GATE-CLOSEOUT-v0.1.md`, `admission-gate-closeout.yaml`, `ecf-overlay-v0.2.yaml`, `preliminary-ecf-overlay.yaml`.
- **3 CR records** touched (CR-DEA-BC-03, CR-CATALOG-STRUCT-08, CR-CATALOG-STRUCT-09).
- **1 new CR record**: this file (CR-BC-ECF-03).
- **1 CHANGELOG section**: `[2.5.0-migration] - 2026-09-08`.

Total: **44 files modified** + 1 new CR + 1 CHANGELOG section.

## 4. Verification

- `scripts/check_ecf_conformance.py`: **PASS** (26 entries + MCSP view conform to ECF Conformance Gate).
- `scripts/check_versions.py`: **PASS** (26 entries conform to CR-DEA-BC-05 version discipline).
- `scripts/check_view_refs.py`: **PASS** (exit 0).

## 5. Pre-existing bug fixed in passing

`scripts/lib/grid.js` `DOMAINS` display labels were partially updated by CR-CATALOG-STRUCT-09 (Domain 3's display label was fixed). The v2.5.0 migration now requires the same correction for Domain 6's display label (`Operations` → `Enablement`). The fix is in scope here because the Domain-6 display label is part of this migration, and leaving it stale would ship an internally inconsistent artifact.

## 6. What did NOT change

- The cardinality of the seven Domains (7), the matrix M = D × S (49 coordinates), and the no-cell-filling rule are unchanged.
- The v2.3.0 renames (CR-CATALOG-STRUCT-08) and v2.4.0 renames (CR-CATALOG-STRUCT-09) are unchanged.
- No entity directory names are renamed (none encode the domain).
- No content redistribution is required (CR-ECF-008 §3.5).

## 7. Backward compatibility

`dea-metaframework` v2.5.0 preserves the deprecated identifiers in `tools/ecf_coordinates.py:DOMAIN_ALIASES` for at least 2 release cycles (CR-ECF-008 §17):
- `OperationsAndEnablement`
- `operationsAndEnablement`
- `operations-enablement`
- `Operations & Enablement`
- `operations_and_enablement`

The catalog's own `scripts/check_ecf_conformance.py` enforces the canonical domain set directly (no alias support); consumers that import this catalog's data should consult the metaframework's alias resolver if they need to support legacy inputs.

## 8. Companion CRs (downstream cascade)

- `dea-metaframework` CR-ECF-008 (PR #30) — merged 2026-09-08
- `dea-metamodel` CR-MM-ECF-03 (PR #167) — open
- `dea-catalog-processes` CR-BP-23 (PR #61) — open
- `dea-catalog-business-objects` CR-BO-02 — planned (4 file footprint)
- `dea-catalog-organizational-units` CR-OU-02 — planned (3 file footprint)

Repos audited as having zero footprint (no migration needed): `dea-catalog-actors`, `dea-catalog-stakeholders`, `dea-catalog-digital-business-service-factory`, `dea-architecture-framework`.