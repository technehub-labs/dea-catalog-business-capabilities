# CR-DEA-BC-35: Entity System Stage 5-6 (BC Slice)

| Field | Value |
|-------|-------|
| **CR** | CR-DEA-BC-35 |
| **Title** | Entity System Stage 5-6 (Catalog Adoption + Institutionalisation) - BC Slice |
| **Status** | Proposed (this PR) |
| **Layer** | L1 (Business Capability Catalog) |
| **Depends on** | CR-BP-121..125 (the 6-stage institutionalisation in dea-catalog-processes) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-15 |

## 1. Purpose

This is the BC slice of the General Entity System institutionalisation
programme (CR-BP-121..125 in `dea-catalog-processes`). The pilot
implementation in the processes catalog is the reference; this PR ports
the pattern to `dea-catalog-business-capabilities` (32 admitted
`BusinessCapability` records in `entities/v1-alpha/`).

The slice ships:

1. The 5-rule umbrella gate `scripts/check_entity_system.py` (copied
   verbatim from `dea-catalog-processes/scripts/check_entity_system.py`).
2. The BC-specific data-driven registry
   `reconciliation/entity-system-registry.yaml`.
3. The per-type gate delegation stub
   `scripts/check_business_capability.py` (ES-005 only checks the
   script EXISTS; the full per-type validation lives in the per-type
   gate in the conformance rollup).
4. The 32-test suite `tests/test_check_entity_system.py` (copied
   verbatim; all pass).
5. The CI workflow `.github/workflows/validate-entity-system.yml` that
   runs the gate under `--strict` on every PR.

After this slice: every new `BusinessCapability` admission must conform
to the entity-system standard or carry an exception per the EGV-011
escape hatch.

## 2. The BC-specific profile

BC has a bespoke lifecycle model: `lifecycle_status` is a flat string
(nested under no parent block) with the BC ladder states
`candidate -> observed -> corroborated -> normalized -> ecf-mapped ->
reviewed -> canonical -> active -> retired`. The BP-123 ES-004 rule
splits the `lifecycle_state_field` on "." and requires a nested block;
the BC profile therefore OMITS `lifecycle_state_field` so ES-004 skips
BC records by construction. The registry's `lifecycle` block still
documents the BC ladder (valid states, transition table, terminal
states, provenance shape) for human and audit reference.

The BC profile's required fields (per the entity contract EC-001..EC-004):

- `id`, `type`, `name`, `definition`, `version`, `metamodel_pin`,
  `lifecycle_status`

All 32 admitted `BusinessCapability` records carry these 7 fields, so
ES-002 is CONFORMANT for the live tree (modulo pre-admission candidate
records documented under §3).

The relationships section follows the BP standard: 3 stored types
(`depends-on`, `realizes`, `specializes`) + 1 forbidden (`part-of`),
with `identity_scope` for cross-catalog references. BC records
currently do not declare `related_capabilities`; the relationship gate
(ES-003) is vacuously CONFORMANT for the live tree.

## 3. Pre-admission candidate records

The BC tree contains 3 pre-admission candidate records
(`capabilities:candidate-relmgmt-nu73v9`,
`capabilities:candidate-epm-5fxren`,
`capabilities:candidate-orgdesign-a7s8bf`) in
`catalog-research/candidates.yaml` (per CR-DEA-BC-02). These predate
the entity-system standard and are not admitted records. They are
flagged by ES-001 (id pattern) and ES-002 (type Candidate is not in the
profile). Per the BP-123 design, these findings are advisory in
Stage 3-4 / Stage 5 and become blocking only when the record is
promoted to admission (which requires the entity-system profile to be
satisfied, possibly via a per-record exception).

## 4. The gate posture (live, 2026-10-15)

```
$ python3 scripts/check_entity_system.py --self-test
self-test PASS (5 cases)

$ python3 scripts/check_entity_system.py --strict
Entity System Gate (CR-BP-123): NON-CONFORMANT
  [ES-001] capabilities:candidate-relmgmt-nu73v9: id ... does not match canonical pattern
  [ES-002] capabilities:candidate-relmgmt-nu73v9: type 'Candidate' is not in the valid types list
  ... (3 candidate records, 6 findings total)
```

The 6 findings are the 3 pre-admission candidates (each flagged twice:
once for ES-001 id format, once for ES-002 type). No findings on the
32 admitted records.

## 5. The exception mechanism (the EGV-011 escape hatch)

The exception mechanism (CS-008/CS-009) consults
`reconciliation/normalization.yaml` for `review-retained` verdicts.
This slice ships no exceptions; if a specific candidate record needs
individual treatment beyond the class-level disposition documented in
§3, the carrier CR for that record's admission can add a
`review-retained` exception.

## 6. Repository changes

| Path | Status | Notes |
|---|---|---|
| `reconciliation/entity-system-registry.yaml` | NEW | BC-specific registry: 1 profile (BusinessCapability); BC id pattern; BC lifecycle ladder |
| `scripts/check_entity_system.py` | NEW | Copied verbatim from `dea-catalog-processes` (5 rules; --self-test + --strict + --json) |
| `scripts/check_business_capability.py` | NEW | Per-type gate stub (ES-005 existence check) |
| `tests/test_check_entity_system.py` | NEW | Copied verbatim; 32 tests; all pass |
| `.github/workflows/validate-entity-system.yml` | NEW | Runs the gate under --strict on every PR |
| `change-requests/CR-DEA-BC-35-entity-system-business-capabilities.md` | NEW | This file (the carrier CR) |
| `change-requests/README.md` | MOD | New row at top of table |
| `CHANGELOG.md` | MOD | [Unreleased] entry |

## 7. Acceptance criteria

- AC-01 The registry is filed under `reconciliation/entity-system-registry.yaml`; data-driven from the registry.
- AC-02 The 5-rule umbrella gate is in place (`scripts/check_entity_system.py`); the BC profile is registered.
- AC-03 The per-type gate stub exists at `scripts/check_business_capability.py` (ES-005 passes).
- AC-04 The 32-test suite passes (`tests/test_check_entity_system.py`).
- AC-05 The CI workflow runs the gate under `--strict` on every PR.
- AC-06 D-004 (no en/em-dash, no U+2E3B) is clean across all new/modified files.
- AC-07 The 118a/b/c authorship gates remain CONFORMANT (no overlap with this slice).
- AC-08 The 32 admitted BusinessCapability records pass ES-001, ES-002, ES-003 (vacuously), ES-004 (skipped by profile design), ES-005 (script exists).
- AC-09 Pre-admission candidate records (3 records) carry advisory findings only; per CR-BP-124's disposition-register pattern, they will be addressed when each is promoted to admission.

## 8. Out-of-scope follow-ons

- **T8 of umbrella programme** (Legacy ID reconciliation): per-repo disposition registers + cross-catalog URI form (U-01 resolution) + IDM-001 pattern fix.
- **CR-DEA-BC-36** (forthcoming, BC scope): the per-record disposition register for BC + the cross-catalog URI form.
- **Metamodel slice** (CR-MM-ECF-04): the metamodel's entity-type definitions conform to the General Entity System standard.

## 9. Cross-references

- **CR-BP-121** (Stage 1): the 4 doc outputs.
- **CR-BP-122** (Stage 2): the 5 normative spec docs.
- **CR-BP-123** (Stage 3-4): the 5-rule umbrella gate.
- **CR-BP-124** (Stage 5): the disposition register + cross-catalog resolution.
- **CR-BP-125** (Stage 6): the doctrine doc + cardinal-rules update + CONTRIBUTING + envelope template + exception process.
- **DEA-ID-000**: the foundation paper in `dea-governance/docs/design/entity-system-foundation.md`.
- **CR-012**: the org-wide governance CR in `dea-governance/change-requests/CR-012-org-wide-entity-governance.md`.
- **CR-DEA-BC-34**: the prior authorship slice (T2 of the umbrella programme).
- **CR-DEA-BC-mv1**: the entity storage and id migration.
- **T7 of umbrella programme**: the cross-repo cascade (this PR is one slice).
