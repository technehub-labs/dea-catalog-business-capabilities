# CR-DEA-BC-22: Rename Analytics and Intelligence to Insight Management (CR-DEA-BC-21 ratification)

**Status**: Applied (2026-09-30); user ratified V-A Insight Management on 2026-09-30; rename applied with id, name, version 1.0.0 to 2.0.0, aliases retained, N-022 verdict rename-applied, ADR-ES-021 ratified
**Filed**: 2026-09-30
**Author**: Emmanuel A. Otchere
**Depends on**: CR-DEA-BC-01 (method), CR-DEA-BC-09 (naming advisory set), CR-DEA-BC-12 (noun-as-ability advisory), CR-DEA-BC-20 (rule 7 + H8 hard gate), CR-DEA-BC-21 (recon + ADR-ES-021)
**Carrier documents**: `catalog-research/recon/INV-AI-v0.1.yaml`, `catalog-research/recon/ADR-ES-021.yaml`

## Problem statement

CR-DEA-BC-20 deferred the noun-as-ability naming question on Analytics and Intelligence (CAND-018) per user DP-E:

> For DP-E, Analytics and Intelligence seems to me that Intelligence will imply having analysis capability, and perhaps vice versa? My key issue is that they are two disciplines with common and yet unique ability characteristics, right? So we perhaps need to dedicate an ADR to research further the direction to take. It's an item you'd need to schedule as part of the recon to enable us fix.

CR-DEA-BC-21 ran the recon procedure, evaluated four candidate vectors, and recommended V-A Insight Management. This CR-DEA-BC-22 applies the rename on user ratification.

## Recon ratified (V-A Insight Management)

`catalog-research/recon/INV-AI-v0.1.yaml` ran five steps and evaluated four vectors. The recommendation, recorded in `catalog-research/recon/ADR-ES-021.yaml`, is V-A Insight Management.

User ratified V-A on 2026-09-30 (Discord message id `1554690132228051015`):

> [eaojnr] V-A insight management is adopted

## Rename matrix

| Field | Before | After |
|---|---|---|
| id | `capabilities:capability-analytics-and-intelligence-559tky` | `capabilities:capability-insight-management-ms4n9d` |
| name | `Analytics and Intelligence` | `Insight Management` |
| version | `1.0.0` | `2.0.0` (semver-incompatible name change) |
| business_object | `Insight` | `Insight` (unchanged) |
| aliases | `[]` | `[Analytics and Intelligence, Data and Analytics, Insight, Intelligence, Business Intelligence]` |
| domain (ECF) | `enablement-operations` | `enablement-operations` (unchanged) |
| stage (ECF) | `operate` | `operate` (unchanged) |

## Side-effects

### Files modified (BC-22 slice)

- `entities/v1-alpha/dea:capability-insight-management/` (renamed from `dea:capability-analytics-and-intelligence/`).
  - `dea:capability-insight-management.yaml` (renamed + content patched: id, name, version, aliases).
  - `README.md` (renamed + content patched: title, record id).
  - `research/` (moved with parent; `boundary-decision-cand-018.yaml`, `BOUNDARY-DECISION-CAND-018.md`, `README.md` keep old ids as provenance per BC-09 section 8).
  - `candidates/`, `retired/` (moved; placeholders).
- `entities/v1-alpha/information-management-6vjgdh/` (related_capabilities + boundary prose).
- `entities/v1-alpha/technology-enablement-y6nkws/` (related_capabilities + boundary prose).
- `mappings/specializations/view-telecom-mcsp.yaml` (inherited[]; catalog_baseline note).
- `mappings/specializations/VIEW-TELECOM-MCSP.md` (already updated via view-telecom-mcsp regeneration; see PR #73).
- `CATALOG.yaml` (regenerated via `scripts/regenerate_catalog.py`; Insight Management block + research refs).
- `CHANGELOG.md` (Unreleased Major block for BC-22).
- `README.md` (catalog status paragraph updated; 28 first-order canonical capabilities; renames recorded).
- `OpenDEA_Foundation_Capability_Map_Nested.html` (regenerated; cell `enablement-operations x operate` now shows Insight Management).
- `catalog-research/normalization.yaml` (N-022 verdict `review-retained-pending-ADR` -> `rename-applied`; `affected_entry` updated; `prior_affected_entry` recorded for provenance; `register_version` 0.4.0 -> 0.5.0).
- `catalog-research/recon/ADR-ES-021.yaml` (status `proposed` -> `ratified (2026-09-30)`).

### Files NOT modified (provenance preserved)

Per BC-09 section 8, candidate research artifacts keep old ids as provenance. The following files retain the pre-rename id `dea:capability-analytics-and-intelligence`:

- `entities/v1-alpha/epm-5fxren/candidates/epm.yaml` (CAND-037 EPM evidence; boundary defense narrative).
- `catalog-research/distinctness-sweep.yaml` (research sweep narrative).
- `catalog-research/INV-EPM-v0.1.yaml` (research inventory narrative).

Historical CR docs and CHANGELOG historical sections (v1-alpha.0..v1-alpha.8; STRUCT-03a/b) preserve "Analytics and Intelligence" as historical truth. The post-mv1 migration-id-map `known_residuals` records the pre-rename slug.

## Gates (post-rename, all PASS)

- `check_naming.py`: 28 entries conform (4 advisories; down from 5 pre-BC-22). The Analytics and Intelligence advisory is gone; the renamed entry passes H8 cleanly.
- `check_versions.py`: catalog v1-alpha; 28 entries.
- `check_ecf_conformance.py`: 28 entries + MCSP view conform.
- `check_view_refs.py`: clean.
- `check_visual_domain_labels.py`: 9 visuals conform.
- `check_catalog_index.py`: CATALOG.yaml validates (31 entities).
- `check_id_system.py`: IDM-001..007 CONFORMANT.

## Commit plan

The BC-22 slice lands on `feat/CR-DEA-BC-20-21-22-mv1-noun-as-ability` (branched from `origin/main` post-mv1) as the fourth atomic commit in a four-commit series with the BC-20/BC-21 work:

1. `feat(check-naming): add H8 noun-as-ability hard gate + review-retained registry (post-mv1 id system)` -- BC-20 procedural; linter changes; N-016/18/19/20.
2. `feat(catalog): rename Strategy to Strategy Formulation; Operations to Operations Management (post-mv1)` -- BC-20 renames; entity dirs; sibling cross-refs; CATALOG; tools/ symlink; migration-id-map extension.
3. `research(catalog): CR-DEA-BC-21 Analytics and Intelligence recon; V-A Insight Management; ADR-ES-021 ratified; N-022 rename-applied` -- BC-21 recon artifacts; INV-AI; ADR-ES-021; evidence register; candidates; N-022; CR-21 doc.
4. (this commit) `feat(catalog): rename Analytics and Intelligence to Insight Management; Insight Management entry; sibling cross-refs; capability map; CHANGELOG; README` -- BC-22 rename; entity dir; sibling cross-refs; CHANGELOG; README; capability map; CR-22 doc.

## Acceptance criteria

All criteria met on 2026-09-30:

- [x] User ratified V-A Insight Management on 2026-09-30 (message id `1554690132228051015`).
- [x] `dea:capability-analytics-and-intelligence` renamed to `dea:capability-insight-management` under the post-mv1 id system.
- [x] `name: Analytics and Intelligence` -> `Insight Management`.
- [x] `version: 1.0.0` -> `2.0.0` (semver-incompatible name change).
- [x] `aliases` retained for provenance and discoverability.
- [x] `business_object: Insight` retained.
- [x] Sibling cross-references updated: information-management, technology-enablement.
- [x] CATALOG.yaml regenerated; Insight Management block present.
- [x] N-022 verdict `review-retained-pending-ADR` -> `rename-applied`; `affected_entry` updated; `prior_affected_entry` recorded.
- [x] ADR-ES-021 status `proposed` -> `ratified (2026-09-30)`.
- [x] reconciliation/migration-id-map.yaml extended with `dea:capability-insight-management` entry + `known_residual` for the pre-rename slug.
- [x] CHANGELOG.md, README.md, capability map updated.
- [x] All 7 structural gates PASS.

## Cross-references

- `change-requests/CR-DEA-BC-20.md` (rule 7 + H8 hard gate; the deferred item this CR resolves).
- `change-requests/CR-DEA-BC-21.md` (recon CR; this CR applies the rename on user ratification).
- `catalog-research/recon/INV-AI-v0.1.yaml` (5-step recon procedure; 4 vectors).
- `catalog-research/recon/ADR-ES-021.yaml` (recommendation ADR; ratified 2026-09-30).
- `catalog-research/normalization.yaml` N-022 (verdict rename-applied).
- `reconciliation/migration-id-map.yaml` (version 2; 3 new id_map entries; 1 new known_residual for the pre-rename slug).
- `entities/v1-alpha/dea:capability-insight-management/` (the renamed entry).
