# v1-alpha Catalog Entries

This directory holds Business Capability catalog entries. **It is empty until the first admission PR**: entries appear only after a candidate passes the review gates (METHODOLOGY.md section 12) on the recommendation set produced by CR-DEA-BC-02 (gate close-out v0.1).

## Entry conventions

- One file per capability: `capability-<slug>.yaml` (TAXONOMY.md section 5).
- `id` is `dea:capability-<slug>`; `type` is the constant `BusinessCapability` (kind by specialization, dea-metamodel ADR-015).
- `capability_type` never appears (deprecated upstream; CR-DEA-BC-01A).
- `capability_layer` is optional; values are exactly `strategic | operational | support`.
- ECF coordinates live under `ecf` (`primary` = earliest initiation; `secondary` = legitimate participation). A capability whose mapping is legitimately absent sets `held_unmapped: true` with a `note` instead (CAND-019 precedent).
- `evidence.sources` cites the evidence register (`SRC-NNN`); `provenance` records the full seven-stage ladder passage and the origin candidate (`CAND-NNN`).
- Every entry carries the narrative fields (`why_capability`, `boundary`, `non_examples`, `specialization_boundary`) per METHODOLOGY.md section 11.

## Shape (illustration, not canonical)

```yaml
id: dea:capability-customer-management
type: BusinessCapability
name: Customer Management
definition: ...
outcome: ...
business_object: Customer
version: 1.0.0
ecf:
  primary: { domain: customer-demand, stage: operate }
  secondary:
    - { domain: customer-demand, stage: conceive }
evidence:
  sources: [SRC-001, SRC-002]
  rationale: ...
provenance:
  candidate_ref: CAND-005
  ladder_passage: [...]
```

The binding definition is the schema: [`../../schemas/entity.schema.json`](../../schemas/entity.schema.json), reconciled with the [DEA Metamodel capability schema](https://github.com/technehub-labs/dea-metamodel/blob/main/schemas/entities/capability.json) per CR-DEA-BC-03.
