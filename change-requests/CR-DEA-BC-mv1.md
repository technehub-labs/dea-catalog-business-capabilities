# CR-DEA-BC-mv1: ID System Migration (org-wide Wave 2, capabilities)

**Status**: Proposed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-21
**Depends on**: dea-metaframework docs (`id-system.md`, `entity-storage-layout.md`, PR #31); Wave 1 (dea-catalog-business-processes PR #149); Wave 2 decision review (eaojnr 2026-09-21: D2-1..D2-5 confirmed)

## 1. Summary

Migrates this catalog to the org-wide id system and storage layout
(dea-metaframework canonical specs). Every record's `id:` moves from the
legacy `dea:capability-*` / `dea:candidate-*` family to
`capabilities:capability-<slug>-<hash>` / `capabilities:candidate-<slug>-<hash>`
(31 records; hash per id-system.md section 2.5). Entity directories move
from `entities/v1-alpha/dea:<id>/` to `entities/v1-alpha/<slug>-<hash>/`
(flat layout, entity-storage-layout.md section 3). Every structured
cross-reference (`related_capabilities`, specialization-view parents,
fixtures, research registers) is rewritten through the migration id map.

## 2. Decision basis (Wave 2 review, 2026-09-21)

- D2-1: flat layout (single-level catalog; no decomposition hierarchy to
  contain). Spec amended accordingly (metaframework PR #31).
- D2-2: capability ids carry no domain/stage; ECF coordinates stay as
  record fields (`ecf.primary` / `ecf.secondary`). Spec section 2
  clarified.
- D2-3: candidate records become `capabilities:candidate-<slug>-<hash>`;
  the candidate-only dir shape is retained (CST-003-conformant).

## 3. What changes

- `scripts/migrate_to_new_ids.py`: the migration script (idempotent;
  dry-run by default). Emits `reconciliation/migration-id-map.yaml`
  (31 entries + 7 documented `known_residuals` for dead pre-rename /
  retired-candidate ids cited in historical research registers).
- 31 record files moved + rewritten; README.md per entity dir (IDM-007).
- `scripts/check_id_system.py` (new): IDM-001..007 catalog-wide gate +
  IDM-008 PR-scoped coherence mode with per-PR report artifact. Wired
  into `catalog-conformance.yml`.
- Vendored STRUCT tools ported to the dual-family id system:
  `check_catalog_index.py` (id pattern, subtree resolution via declared
  path, record-id orphan check), `regenerate_catalog.py` (id pattern,
  content-derived entity ids, id-derived canonical filenames, subtree
  paths), `catalog-index-schema/catalog-index-schema.json` (id patterns).
  Upstream equivalents: dea-metaframework PR #34.
- `schemas/entity.schema.json`: id patterns to the new family;
  `ecf_rationale` maxLength 1000 -> 1280 (namespaced ids are ~20 chars
  longer and rationale prose cites them inline; one record would
  otherwise exceed the bound at 1,007 chars). Fixtures updated.
- `scripts/generate_capability_map.py`: tree discovery ported to the
  id-derived filenames.
- `.github/workflows/validate-entries.yml`: canonical-file glob ported.
- Living docs updated in place: `TAXONOMY.md` (id form + layout),
  `entities/v1-alpha/README.md` (conventions + ids).
- Historical artifacts (52 markdown artifacts scanned; see
  `reconciliation/cross-check-mv1.md`): 36 carry legacy forms and were
  bannered `Layout note (CR-DEA-BC-mv1, 2026-09-21)` with content
  verbatim; 16 CLEAN; 0 NEEDS-FRAMING. Three research YAML registers and
  one entity research YAML carry a header-comment equivalent.

## 4. Verification

- `check_id_system.py --strict`: CONFORMANT, 28 canonical records, 0 findings.
- `check_catalog_index.py --strict`: OK (31 entities).
- `regenerate_catalog.py --check`: CATALOG.yaml current.
- CST suite (dea-metaframework main, post-#33/#34): 16/16 pass --strict.
- `check_ecf_conformance.py`: PASS (28 entries + MCSP view).
- `check_naming.py`: PASS (5 pre-existing advisories unchanged).
- `check_versions.py`: PASS (28 entries).
- `check_visual_domain_labels.py`: PASS.
- Schema validation: all 28 canonical records + both fixtures validate
  against the updated `entity.schema.json`.
- Migration idempotence: `migrate_to_new_ids.py` re-run is a no-op.

## 5. Out of scope

- Services-repo references to these capability ids are rewritten in the
  services migration (Wave 2b, CR-SVC-mv1), which consumes this id map.
- `dea:component-*` / `dea:principle-*` / `dea:pattern-*` references in
  OTHER repos: namespaces not in the ratified registry; documented as
  known residuals in the consuming repo's id map.
