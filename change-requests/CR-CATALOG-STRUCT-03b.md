# CR-CATALOG-STRUCT-03b: Business Capability Catalog Research Distribution

**Status**: Proposed
**Layer**: L1 (Business Capability Catalog)
**Owner**: TechNeHub Labs
**Depends on**: CR-CATALOG-STRUCT-03a (merged; PR #44)
**Supersedes**: none
**Related**: CR-CATALOG-STRUCT-03a (preceding slice; PR #44), CR-CATALOG-STRUCT-01 (the standard), CR-CATALOG-STRUCT-07 (cross-repo consumer)

---

## 1. Purpose

Second and final slice of `technehub-labs/dea-catalog-business-capabilities` adoption of the catalog repository standard (CR-CATALOG-STRUCT-01). This CR distributes the 33 research files (formerly under `docs/research/`) into per-entity subtrees, a new `catalog-research/` directory, and a new `visuals/` directory, per the Q1/Q2 decisions in the planning conversation.

After this merges, the BC catalog is fully `conforming` (matching the standard end-to-end).

## 2. Scope

**In scope**:

- **Per-entity distribution (1 entity, 2 files)**: the CAND-018 boundary decision belongs specifically to `dea:capability-analytics-and-intelligence` (the entity CAND-018 was admitted as). Both the YAML record and the MD narrative move from `docs/research/` to `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/`.
- **Catalog-wide research (31 files)**: 14 YAML records + 17 MD narratives covering the CR-DEA-BC-02 execution (admission gates, evidence, distinctness sweep, ECF overlay, corpus patch, candidate universe, normalization, specialization register, BC-02 close-out, research report). Move from `docs/research/` to a new top-level `catalog-research/` directory.
- **Visuals split (9 SVG files + 1 manifest)**: separate the SVG visual assets from the prose documentation. Move from `docs/research/visuals/` to a new top-level `visuals/` directory. The `docs/research/visuals.yaml` manifest stays as catalog-wide metadata (`catalog-research/visuals.yaml`); it travels with the related `VISUALS-v0.1.md` narrative.
- **Provenance READMEs**: per-entity `research/README.md` for the analytics subtree; `catalog-research/README.md`; `visuals/README.md`.

**Out of scope**:

- No entity layout changes (STRUCT-03a already shipped those).
- No new entries or admission work (this CR only moves existing research).
- No new CI workflow (the existing `catalog-conformance.yml` from STRUCT-03a already enforces the standard; this CR brings the catalog to `conforming` under that gate).

## 3. Distribution map

### Per-entity (1 entity, 2 files)

| From | To |
|---|---|
| `docs/research/boundary-decision-cand-018.yaml` | `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/boundary-decision-cand-018.yaml` |
| `docs/research/BOUNDARY-DECISION-CAND-018.md` | `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/BOUNDARY-DECISION-CAND-018.md` |

Provenance README: `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/README.md`.

### Catalog-wide (31 files)

| Theme | Files |
|---|---|
| Admission gates | `admission-gate-precheck.{yaml,md}`, `admission-gate-closeout.{yaml,md}` |
| Admission reviews | `admission-review.{yaml,md}`, `admission-review-supplementary.{yaml,md}` |
| Evidence corpus | `evidence-register.{yaml,md}`, `enterprise-generality-matrix.{yaml,md}` |
| Candidates and distinctness | `candidates.yaml`, `distinctness-sweep.{yaml,md}` |
| Normalization and specialization | `normalization.{yaml,md}`, `specialization-register.{yaml,md}` |
| ECF mapping | `preliminary-ecf-overlay.yaml`, `ecf-overlay-v0.2.{yaml,md}` |
| Corpus | `CORPUS-PATCH-v0.1.md` |
| Methodology execution | `bc-02-closeout.yaml`, `BC-02-CLOSEOUT.md`, `research-report.{yaml,md}` |
| Visuals narrative | `VISUALS-v0.1.md` (the narrative; the assets live in `visuals/`) |

All files move from `docs/research/` to `catalog-research/` at the repo root.

Provenance README: `catalog-research/README.md`.

### Visuals (10 files)

| From | To |
|---|---|
| `docs/research/visuals/v01-evidence-candidate-pipeline.svg` | `visuals/v01-evidence-candidate-pipeline.svg` |
| `docs/research/visuals/v02-candidate-universe-map.svg` | `visuals/v02-candidate-universe-map.svg` |
| `docs/research/visuals/v03-enterprise-comparison-matrix.svg` | `visuals/v03-enterprise-comparison-matrix.svg` |
| `docs/research/visuals/v04-capability-process-boundary.svg` | `visuals/v04-capability-process-boundary.svg` |
| `docs/research/visuals/v05-capability-outcome-relationship.svg` | `visuals/v05-capability-outcome-relationship.svg` |
| `docs/research/visuals/v06-capability-business-object.svg` | `visuals/v06-capability-business-object.svg` |
| `docs/research/visuals/v07-first-order-specialization-pyramid.svg` | `visuals/v07-first-order-specialization-pyramid.svg` |
| `docs/research/visuals/v08-capability-ecf-overlay.svg` | `visuals/v08-capability-ecf-overlay.svg` |
| `docs/research/visuals/v09-ecf-coverage-map.svg` | `visuals/v09-ecf-coverage-map.svg` |
| `docs/research/visuals.yaml` | `catalog-research/visuals.yaml` (manifest stays with the related narrative as catalog-wide metadata) |

Provenance README: `visuals/README.md`.

## 4. Design

### 4.1 Per-entity classification

A research file is "per-entity" when it documents a decision or evidence about one specific canonical entity. The classification method used here:

1. Scan every research file for mentions of `dea:capability-<name>` entity IDs.
2. A file mentioning exactly one entity ID is "per-entity" for that entity.
3. A file mentioning zero or multiple entity IDs is "catalog-wide".

Result: only `boundary-decision-cand-018.yaml` mentions one entity ID (`dea:capability-information-management` as the counterpart). The decision's SUBJECT is CAND-018, which corresponds to `dea:capability-analytics-and-intelligence`. The decision is about the boundary of CAND-018, so it lives with CAND-018's admitted form. Per CR-CATALOG-STRUCT-01 §5, research describes the entity's evidence base; the boundary decision is the canonical evidence for `dea:capability-analytics-and-intelligence`.

### 4.2 Catalog-wide classification

Per the planning conversation's Q1 decision: catalog-wide research lives in `catalog-research/` at the repo root. The standard's §5 requires per-entity `research/` subtrees; it does not explicitly cover catalog-wide research. `catalog-research/` is an extension: it preserves the discoverability of CR-DEA-BC-02 execution artifacts (which document the catalog as a whole, not any one entity) without co-locating them with `docs/` (prose documentation) or per-entity subtrees (canonical records).

The `catalog-research/README.md` documents the categories (admission gates, evidence corpus, candidates and distinctness, normalization, ECF mapping, corpus, methodology execution, visuals narrative) so future catalog authors can place new research correctly.

### 4.3 Visuals split

Per the planning conversation's Q2 decision: visuals are their own asset category and live in `visuals/` at the repo root, separate from `docs/`. The manifest (`MANIFEST.yaml`) travels with the assets. The narrative (`VISUALS-v0.1.md`) is documentation about the visuals and lives in `catalog-research/` (it explains the visual assets, not the catalog as a whole).

The `visuals/` location preserves the distinction between three categories of files:

1. Prose documentation (`docs/`): methodology, foundations, versioning, publication pipeline.
2. Research artifacts (`catalog-research/` and per-entity `research/` subtrees): evidence, decisions, registers, surveys.
3. Visual assets (`visuals/`): SVG illustrations.

### 4.4 Provenance READMEs

Each of the three new locations gets a README explaining:

- The contents of the directory.
- Where the files came from (provenance).
- Why the location was chosen (per the planning decisions).
- Categories or themes within the directory.

The READMEs are required because the directories are now non-empty and the standard's CST-009 mandates `README.md` in non-empty `research/` subtrees (extended to `catalog-research/` and `visuals/` by analogy).

### 4.5 Empty directory cleanup

After all moves:

- `docs/research/` becomes empty (no files, no subdirectories). It is removed.
- `docs/` retains its three existing files (`FOUNDATIONS.md`, `publication-pipeline.md`, `VERSIONING.md`).

The `docs/research/` removal does not affect any existing workflow (no CI step references it after this CR).

## 5. Files

**New** (3):

- `catalog-research/README.md`
- `visuals/README.md`
- `change-requests/CR-CATALOG-STRUCT-03b.md` (this document)

**Modified**:

- `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/README.md` (new provenance doc, written by this CR)
- `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/boundary-decision-cand-018.yaml` (moved)
- `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/BOUNDARY-DECISION-CAND-018.md` (moved)
- `catalog-research/*.yaml` × 14 (moved)
- `catalog-research/*.md` × 17 (moved)
- `visuals/*.svg` × 9 (moved)
- `visuals/MANIFEST.yaml` (moved from `docs/research/visuals.yaml`)
- `CATALOG.yaml` (regenerated; `research_registers[].files` now lists the boundary decision)
- `CHANGELOG.md` (Unreleased entry)
- `change-requests/README.md` (CR-CATALOG-STRUCT-03b row; flip STRUCT-03a status)

**Removed**:

- `docs/research/` (empty after moves)

## 6. Conformance contract

This CR is conformant iff:

1. `docs/research/` does not exist (CST-006: no orphan research dir).
2. `catalog-research/` exists with at least one file and a README.
3. `visuals/` exists with at least one file and a README.
4. `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/` contains the boundary decision + README.
5. Regenerator --check exits 0 (CATALOG.yaml reflects the new research register).
6. Gate --strict exits 0.
7. Conformance --strict exits 0 with 0 warnings.
8. All 3 catalog validators PASS.
9. Dash-clean on new prose.
10. No secrets introduced.

## 7. Decisions log

### D-STRUCT-03b-001: Q1: catalog-wide research lives in `catalog-research/`

Per the planning conversation's Q1 answer. The standard does not explicitly cover catalog-wide research; this CR introduces `catalog-research/` as a sibling of `docs/` and `entities/`. The intent is to preserve discoverability while honoring the standard's per-entity-for-research baseline.

### D-STRUCT-03b-002: Q2: visuals in own top-level `visuals/` directory

Per the planning conversation's Q2 answer. Visuals are their own asset category (not prose, not research, not canonical data). The top-level location separates them from all three existing categories. The manifest (`MANIFEST.yaml`) travels with the assets.

### D-STRUCT-03b-003: CAND-018 boundary decision lives with `dea:capability-analytics-and-intelligence`

The decision's SUBJECT is CAND-018 (which became `dea:capability-analytics-and-intelligence`). The counterpart CAND-017 is mentioned as the boundary delineation reference; the decision is ABOUT CAND-018's admission, not CAND-017's. The boundary decision is the canonical evidence for analytics-and-intelligence; placing it there preserves the standard's "research describes the entity's evidence base" principle.

### D-STRUCT-03b-004: `docs/research/` is removed entirely

After all moves, the directory is empty. Keeping an empty `docs/research/` (with `.gitkeep`) would invite future contributors to add files there, defeating the standard's intent. Removal is permanent.

### D-STRUCT-03b-005: No new CI workflow

The existing `catalog-conformance.yml` from STRUCT-03a already runs the regenerator + gate + conformance suite. The standard's `cross_cutting` field in `CATALOG.yaml` does not enumerate `catalog-research/` or `visuals/`; the gate's cross-cutting sanity check (CST-013/CST-014) does not flag the new directories.

### D-STRUCT-03b-006: Bulk single-commit migration

All 43 file moves + 3 README creations land in one commit. Git's rename detection preserves the history. A single revert restores the prior state.

## 8. Verification

```bash
# Conformance suite (all 16 CSTs pass under --strict)
python /path/to/dea-metaframework/tools/conformance_test_catalog_structure.py \
    --catalog-root . \
    --template-root /path/to/dea-metaframework/tools/catalog-repo-template \
    --strict

# Regenerator + gate
python scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json --check
python scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json

# Existing validators
python scripts/check_ecf_conformance.py
python scripts/check_versions.py
python scripts/check_view_refs.py 'mappings/specializations/view-*.yaml'

# Inventory
ls catalog-research/    # 31 files + README
ls visuals/             # 9 SVG + MANIFEST + README
ls entities/v1-alpha/dea:capability-analytics-and-intelligence/research/  # boundary + README
[ ! -d docs/research ]  # directory removed
```

## 9. Out of scope (deferred)

- **STRUCT-04**: `dea-catalog-digital-business-service-factory` adoption.
- **STRUCT-05**: `dea-catalog-stakeholders` adoption.
- **STRUCT-07**: cross-repo consumer.

## 10. Acceptance criteria

1. All 3 catalog validators PASS.
2. Regenerator --check exits 0.
3. Gate --strict exits 0.
4. Conformance --strict exits 0 with 0 warnings.
5. `docs/research/` does not exist.
6. `catalog-research/`, `visuals/`, and the analytics `research/` each have a README.
7. CR doc is dash-clean.
8. No secrets introduced.
9. CHANGELOG, CR README, and cross-repo adoption tracker updated.
10. CI on the branch is green (all 4 checks).

## 11. Risks

- **R-STRUCT-03b-001**: Future contributors might add research to `docs/research/` again. Mitigation: the directory is removed; the standard's CST-006 fails the build if any orphan research dir reappears.
- **R-STRUCT-03b-002**: The `catalog-research/` extension is not explicitly covered by the standard. Mitigation: the location is documented in the CR and the cross-repo adoption tracker; future standards revisions can ratify or relocate it.

## 12. Open questions

None at authoring time. Resolved during planning:

- Where catalog-wide research lives (D-001).
- Whether visuals share a directory with research (D-002).

## 13. Related

- CR-CATALOG-STRUCT-01 (merged): the standard.
- CR-CATALOG-STRUCT-06a (merged): regenerator + gate + schema.
- CR-CATALOG-STRUCT-06b (merged): conformance suite + template.
- CR-CATALOG-STRUCT-02 (merged): process catalog adoption pattern reference.
- CR-CATALOG-STRUCT-03a (merged): the preceding slice of this adoption.
- CR-DEA-BC-01..06 (all landed): the BC method CRs that produced the research being distributed.

---

## Appendix A: Provenance map

```
docs/research/                                  catalog-research/      (31 files)
├── boundary-decision-cand-018.yaml  ──────►    entities/v1-alpha/dea:capability-analytics-and-intelligence/research/
├── BOUNDARY-DECISION-CAND-018.md     ──────►    entities/v1-alpha/dea:capability-analytics-and-intelligence/research/
├── (29 other catalog-wide files)     ──────►    catalog-research/
└── visuals/                          ──────►    visuals/
    ├── *.svg (× 9)                   ──────►    visuals/*.svg
    └── visuals.yaml                  ──────►    catalog-research/visuals.yaml
```

After this CR:
- `catalog-research/`: 14 YAML + 17 MD = 31 files + README.
- `visuals/`: 9 SVG + MANIFEST + README = 11 entries.
- `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/`: 2 files + README.
- `docs/research/`: removed (empty).
- `docs/`: 3 files unchanged (`FOUNDATIONS.md`, `publication-pipeline.md`, `VERSIONING.md`).
