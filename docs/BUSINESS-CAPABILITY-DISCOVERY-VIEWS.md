# Business Capability Discovery Views

**Status**: Normative derivation contracts (CR-DEA-BC-47, 2026-10-28)
**Generator**: `scripts/generate_discovery_views.py` (deterministic; `--check` freshness gate in CI)
**Outputs**: committed under `docs/views/` (clearly marked GENERATED; never hand-edited)

Every view derives from canonical records only. No relationship, hierarchy, or equivalence is inferred from names, shared classification, outcomes, or co-occurrence. Views never redefine the model and are never a source of identity or definitions.

## Derivation contracts

| View | Purpose (discovery question) | Inputs | Selection | Transformation | Output | Freshness | Known limitations |
|---|---|---|---|---|---|---|---|
| `CAPABILITY-INDEX.md` | What capabilities exist, and where is each one? | all canonical records (29) | every `type: BusinessCapability` entry | name-ordered table: name→README link, primary ECF, definition (truncated 180 chars), ladder summary, record link | committed markdown | `--check` in `catalog-conformance.yml` (drift fails CI) | definition truncated for table width; full definition in the record/README |
| `ECF-CLASSIFICATION.md` | Which capabilities are governed at each coordinate? | records' `ecf.primary` | entities with a primary coordinate | grouped list by domain/stage, name-ordered | committed markdown | as above | secondaries not listed (records hold them); same-cell co-location implies nothing |
| `RELATED-CAPABILITIES.md` | Which recorded references exist between capabilities? | records' `related_capabilities` | entities with ≥1 reference | from→to table with README links; unresolved targets marked | committed markdown | as above | **untyped references until R-1** — no graph emitted (would fabricate relationship semantics); no rationale column (lives in records/boundaries) |
| `OUTCOMES-OVERVIEW.md` | What outcome/business object does each concern? | records' `outcome`, `business_object` | all entities | name-ordered table | committed markdown | as above | `business_object` is a prose label until U-1 (no canonical object refs); shared values imply no dependency |

**Not emitted, with reason:** a typed relationship graph — `related_capabilities` is untyped until the Relationship Semantics CR (R-1); emitting typed edges would violate the no-inference principle (CR-47 §4.3/§8.4). Evidence navigation folds into the index's provenance column (full evidence in records + `catalog-research/`).

## Maintenance

Regenerate: `python scripts/generate_discovery_views.py`. CI (`catalog-conformance.yml`) runs `--check`; stale views fail the build. Determinism: fixed ordering (by name), fixed rendering; identical records produce identical output. The generator never modifies canonical records.
