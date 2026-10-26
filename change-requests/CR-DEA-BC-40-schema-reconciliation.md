# CR-DEA-BC-40: Entity-Schema Reconciliation for the Post-mv1 Admission Record Shape

**Status**: Accepted (user directive 2026-10-27: "lets proceed with the recommendatiobs to fix the repo"; discovered at PR #90 CI time)
**Layer**: L1 (schema)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: `validate-entries` has been red on `main` since 2026-10-15 (PRs #77/#80 era): the Enterprise Performance Management record — the first admission under the post-mv1 flow (CR-DEA-BC-23) plus the rich-narrative backfill (CR-DEA-BC-29) — carries five schema violations. The governed content is correct; `schemas/entity.schema.json` lags it. This CR reconciles the schema to the shapes the landed CRs introduced. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-40-schema-reconciliation`, stacked after CR-DEA-BC-39.
**Lands against**: `main`

## 1. The five violations (from the CI log, run 40367632022)

| # | Path in `capabilities-capability-enterprise-performance-management-5fxren.yaml` | Violation | Introduced by |
|---|---|---|---|
| 1 | `<root>` | additional property `loop_closure_narrative` | CR-DEA-BC-23 (BC-SR-A001 §16 direction-loop closure record) |
| 2 | `boundary` | object where the schema allows only string | CR-DEA-BC-29 (rich-narrative backfill: `against_capabilities[]`, `loop_role`) |
| 3 | `provenance` | additional properties `admission_cr`, `evidence_seed_cr`, `migration` | CR-DEA-BC-23 / BC-19 (post-mv1 admission provenance) + mv1 |
| 4 | `provenance.ladder_passage[6].stage` | `'evidence-seeded'` not in the ladder enum | CR-DEA-BC-23 |
| 5 | `provenance.ladder_passage[7].stage` | `'admitted'` not in the ladder enum | CR-DEA-BC-23 |

No other record is affected: exactly one of 29 entries uses the structured boundary; only the EPM record carries the new provenance fields and stages.

## 2. The reconciliation (schema-side; no record changes)

1. `boundary`: `oneOf` the legacy plain string (maxLength 2000) **or** the structured object `{against_capabilities: [{id, rationale}], loop_role}` (strict: no additional properties; `against_capabilities` required).
2. `provenance`: optional `admission_cr` (string), `evidence_seed_cr` (string), `migration` (object: `from_id`, `migration_map_ref`; additional properties allowed for map-version notes).
3. Ladder-stage enum extended with `evidence-seeded` and `admitted` (the post-mv1 admission stages, appended after the original seven).
4. Root: optional `loop_closure_narrative` (string).

## 3. NOT-List

- NOT a record change: the EPM entity and every other entry stay byte-identical; the schema moves to meet the governed content, not the reverse.
- NOT a METHODOLOGY change: the evidence ladder itself (Candidate → … → Canonical) is unchanged; the two new enum values name the admission-flow checkpoints the post-mv1 process already records in `ladder_passage`.
- NOT a fixture change: `schemas/fixtures/example-valid.yaml` remains valid under the extended schema (verified).
- NOT a gate addition: `validate-entries` (the inline Draft7 validator) already blocks; this CR makes the live tree pass it honestly.

## 4. Acceptance criteria

1. The workflow's inline validator passes over all 29 canonical entries: `FAIL: 0 schema violation(s)` — verified locally by replicating the validator (29/29, 0 errors).
2. `schemas/fixtures/example-valid.yaml` still validates (no fixture edit needed).
3. All gates from CR-DEA-BC-37 §6 / BC-38 §6 / BC-39 §9 still exit 0; `regenerate_catalog.py --check` exit 0 (CATALOG regenerated in the same PR; count unchanged at 0).
4. CI on the PR shows all six workflows green, including `validate` (validate-entries) — red on `main` since 2026-10-15.
5. The PR diff touches exactly: `schemas/entity.schema.json`, `CATALOG.yaml`, this CR file, `change-requests/README.md` (index row), `CHANGELOG.md`.

## 5. Verification at landing

PR body records: the local 29/29 validator replication output, the before/after CI verdict for `validate-entries`, and live CI URLs.
