# Catalog-wide research: technehub-labs/dea-catalog-business-capabilities

This directory holds research artifacts that document the catalog as a
whole rather than any one entity. They cover the CR-DEA-BC-02 execution
(admission, evidence, distinctness sweep, ECF overlay, corpus patch,
candidate universe) plus ongoing catalog governance.

## Provenance

All files in this directory were moved from `docs/research/` to
`catalog-research/` by CR-CATALOG-STRUCT-03b. The original location
predated the catalog repository standard (CR-CATALOG-STRUCT-01). The
standard requires research to live in per-entity `research/` subtrees;
catalog-wide research (which is about the catalog rather than any one
entity) is an extension that the standard does not explicitly cover.
The location choice (`catalog-research/` at the repo root, sibling of
`docs/` and `entities/`) preserves the discoverability of the artifacts
without co-locating them with `docs/` (which holds prose documentation).

## Conventions

- **YAML files** (lowercase-kebab-case) are machine-readable records:
  evidence register, admission gate close-out, distinctness sweep,
  ECF overlay, candidates universe, etc.
- **MD files** (UPPERCASE-KEBAB-CASE-with-v0.X.md) are human-readable
  narratives paired with the YAML records. The two formats travel
  together; when one is updated, the other is too.

## Categories

| Theme | YAML | MD |
|---|---|---|
| Admission gates | `admission-gate-precheck.yaml`, `admission-gate-closeout.yaml` | `ADMISSION-GATE-PRECHECK-v0.1.md`, `ADMISSION-GATE-CLOSEOUT-v0.1.md` |
| Admission reviews | `admission-review.yaml`, `admission-review-supplementary.yaml` | `ADMISSION-REVIEW-v0.1.md`, `ADMISSION-REVIEW-SUPPLEMENTARY-v0.2.md` |
| Evidence corpus | `evidence-register.yaml`, `enterprise-generality-matrix.yaml` | `EVIDENCE-REGISTER-v0.1.md`, `GENERALITY-MATRIX-v0.1.md` |
| Candidates and distinctness | `candidates.yaml`, `distinctness-sweep.yaml` | `CANDIDATE-UNIVERSE-v0.1.md`, `DISTINCTNESS-SWEEP-v0.1.md` |
| Normalization and specialization | `normalization.yaml`, `specialization-register.yaml` | `NORMALIZATION-v0.1.md`, `SPECIALIZATION-REGISTER-v0.1.md` |
| ECF mapping | `preliminary-ecf-overlay.yaml`, `ecf-overlay-v0.2.yaml` | `ECF-OVERLAY-v0.1.md`, `ECF-OVERLAY-v0.2.md` |
| Corpus | (none) | `CORPUS-PATCH-v0.1.md` |
| Methodology execution | `bc-02-closeout.yaml`, `research-report.yaml` | `BC-02-CLOSEOUT.md`, `RESEARCH-REPORT-v0.1.md` |
| Visuals manifest | (lives with the SVGs in `visuals/MANIFEST.yaml`) | `VISUALS-v0.1.md` |

## Out of scope

- **Per-entity research**: `dea:capability-analytics-and-intelligence/research/` holds the CAND-018 boundary decision, which is specifically about that entity. Future per-entity research (if any is added) lives with the entity, not here.
- **SVG visuals**: moved to `visuals/` (repo-root top-level directory) per CR-CATALOG-STRUCT-03b; visuals are their own asset category, separate from research and from prose documentation.
