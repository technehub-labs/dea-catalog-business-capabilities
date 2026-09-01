# CR-DEA-BC-03: Catalog Schema and CI Reconciliation

| Field | Value |
|-------|-------|
| **CR** | CR-DEA-BC-03 |
| **Title** | Establish `schemas/entity.schema.json` and entry-validation CI for the Business Capability catalog, reconciled with dea-metamodel (ADR-015 lineage) and catalog-wide CI conventions |
| **Status** | Draft: awaiting review, then "Proceed" to land as proposal PR |
| **Date** | 2026-09-01 |
| **Author** | Coder (for eaojnr) |
| **Depends on** | CR-DEA-BC-01 (method, landed), CR-DEA-BC-01A (record shape, landed), CR-DEA-BC-02 (evidence investigation, execution complete), dea-metamodel ADR-015 / CR-016 (capability classification by specialization), numbering decision 2026-09-01 (change-requests/README.md) |
| **Scope** | Schema file, entry CI, `entities/v1-alpha/` conventions, upstream reconciliation notes. Docs + schema + CI only |
| **Out of scope** | Canonical admission of any capability (method execution, METHODOLOGY.md section 12); changes to dea-metamodel (upstream feedback only); specialization views (CR-DEA-BC-04); ECF definition changes |

---

## 1. Context

The method (CR-DEA-BC-01) is accepted and its documents landed (PR #14). The evidence investigation (CR-DEA-BC-02) is complete: 23 candidates recommended, awaiting the review gates. What does not yet exist is the machine form of an entry: there is no `schemas/entity.schema.json`, no entry CI, and no `entities/v1-alpha/` convention in this repository.

CR-DEA-BC-01 design constraint 3 binds this CR: the schema is reconciled against `dea-metamodel` and the catalog-wide CI conventions, not invented locally.

Two authorities are reconciled:

1. **dea-metamodel** `schemas/entities/capability.json` (metamodel_version 1.0.0): the capability entity schema, carrying the ADR-015 lineage (`capability_layer` governed enumeration, E005; `capability_type` deprecated).
2. **Catalog-wide convention** (dea-catalog-actors precedent): the catalog schema mirrors the metamodel entity schema; `entities/v1-alpha/README.md` documents the entry shape; CI validates `entities/**/*.yaml` and `entities/**/*.json` against the schema via the ajv-py-action reusable step.

## 2. Reconciliation findings (upstream)

Inspection of dea-metamodel `capability.json` (main, 2026-09-01) surfaced three tensions this CR does not silently work around:

- **U1.** `capability_type` is both **required** and **deprecated** (ADR-015). A catalog entry that complies with CR-DEA-BC-01A (never carries `capability_type`) would fail the upstream schema. Resolution here: the catalog schema excludes the field entirely (BC-01A decision 1). Upstream feedback: drop the requirement in a future metamodel CR.
- **U2.** `maturity_level` is **required** but has no property definition in `capability.json` and no governed vocabulary in `metamodel/vocabularies/`. Resolution here: the catalog schema carries an optional `maturity` field (FOUNDATIONS §12 name) with no invented scale; the upstream requirement-versus-definition gap is reported, not patched locally. No maturity scale is designed in this CR.
- **U3.** No `business-capability.json` specialization schema exists; kind is expressed only by the `type` constant convention. Resolution here: the catalog schema sets `type` to the constant `BusinessCapability` (ADR-015: kind by entity specialization; every entry in this catalog is a `dea:BusinessCapability` by catalog scope).

## 3. Decisions

- **D1. Mirror, then extend.** The catalog schema mirrors the upstream field conventions (`id` pattern, `name`, `description`, `version` semver, `lifecycle_status` enum, `external_references`, `metadata`) and adds the catalog's method blocks as explicit extensions.
- **D2. Kind by type constant.** `type` is the constant `BusinessCapability`. No per-entry kind field exists.
- **D3. `capability_type` absent.** The field never appears on an entry (CR-DEA-BC-01A). The schema does not define it.
- **D4. `capability_layer` optional, governed.** Values exactly `strategic | operational | support` (ADR-015 §5, E005).
- **D5. ECF as classification metadata.** An `ecf` block carries `primary` (required) and `secondary` (array, possibly empty); each coordinate is `{domain, stage}` with the governed 7x7 vocabulary: domains `governance-existence | customer-demand | supply-resources | product-offering | operations-delivery | finance-value | people-organization`; stages `conceive | design | build | activate | operate | improve | retire`. A `held_unmapped` flag with mandatory `note` covers the legitimately-absent case (CAND-019 precedent); an entry with `held_unmapped: true` omits `primary`.
- **D6. Method blocks.** `outcome`, `business_object`, `aliases` (array), `realization` (arrays of cross-catalog ids: processes, actors, resources, systems, information), `evidence` (`sources` as SRC-NNN references plus `rationale`), `provenance` (ladder passage record: stage transitions with dates and actors), `specialization` (`allowed` boolean plus `industry_examples`), and the entry narrative fields (why_capability, boundary, non_examples, specialization_boundary) per METHODOLOGY.md section 11.
- **D7. Identifier convention.** `id` follows the catalog pattern and the upstream example lineage: `dea:capability-<slug>`; one file per entry at `entities/v1-alpha/capability-<slug>.yaml` (TAXONOMY.md section 5).
- **D8. CI per catalog convention.** Entry validation adopts the actors pattern: ajv-py-action against `entities/**/*.yaml` and `entities/**/*.json`, on push to main and on PRs. The existing allocation validator (`validate-allocation.yml`) remains untouched. A schema exercise fixture keeps CI honest while the entity directory is empty (section 4, item 4).
- **D9. No entries ship in this CR.** The first real entries arrive only through admission PRs after the review gates (METHODOLOGY.md section 12).

## 4. Changes

1. `schemas/entity.schema.json`: new, per section 3.
2. `.github/workflows/validate-entries.yml`: new, per D8 (actors ci.yml pattern, names adjusted to this catalog).
3. `entities/v1-alpha/README.md`: entry conventions and a documented example shape (actors precedent), explicitly marked non-canonical illustration.
4. `schemas/fixtures/example-valid.yaml`: one valid fixture exercising every required block; validated by CI so the schema is never untested while `entities/` is empty. The fixture is marked `status: fixture-not-canonical` and lives outside `entities/` so it can never be mistaken for a catalog entry.
5. `README.md`: Repository Structure and Status pointers updated (schema + CI landed; population still gated on the review gates).
6. `docs/research/` untouched. No research artifact changes.

## 5. Acceptance criteria

1. The schema validates the fixture in CI (green on the proposal PR itself).
2. No entry carries or may carry `capability_type` (the schema rejects it: `additionalProperties: false` on the entry object).
3. `capability_layer` accepts exactly the governed enumeration; other values fail validation.
4. ECF coordinates validate against the 7x7 vocabulary; `held_unmapped` entries without `primary` validate; entries with neither `primary` nor `held_unmapped` fail.
5. The allocation validator remains green; no pointer change.
6. The upstream reconciliation notes U1 to U3 are recorded in the CR (this document, section 2) for the next dea-metamodel CR.

## 6. Definition of Done for the proposal PR

The proposal PR ships ONLY: this CR verbatim to `change-requests/CR-DEA-BC-03.md`, the `change-requests/README.md` index row, and the README pointer. The implementation (section 4 items 1 to 5) ships as the immediately following phase PR per the one-phase-per-PR convention, exactly as CR-DEA-BC-01 separated proposal (Phase 0) from method documents (Phase 1).

## 7. References

- CR-DEA-BC-01 (method; design constraint 3), CR-DEA-BC-01A (record shape), CR-DEA-BC-02 (evidence execution)
- dea-metamodel: `schemas/entities/capability.json`, ADR-015, CR-016, `metamodel/vocabularies/classifications.yaml` (E005)
- dea-metaframework: ECF 7x7 vocabulary (domain and stage names)
- Catalog CI precedent: dea-catalog-actors `.github/workflows/ci.yml`
- FOUNDATIONS.md section 12 (conceptual record, as amended by CR-DEA-BC-01A); TAXONOMY.md section 5 (identifier and file conventions)
