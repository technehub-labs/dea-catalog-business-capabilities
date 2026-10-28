# CR-DEA-BC-53: Canonical Relationship Semantics and Schema Alignment

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-53 |
| Title | Canonical Relationship Semantics and Schema Alignment |
| Status | Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them") |
| Series | CR-DEA-BC |
| Change layer | L1 — Canonical data model and schema |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Predecessors | CR-DEA-BC-42, CR-DEA-BC-43, CR-DEA-BC-48 |
| Related governance | CR-DEA-BC-35A, CR-DEA-BC-45, CR-DEA-BC-47 |
| Primary deliverables | Relationship model decision, schema alignment, migration plan, validation and test evidence |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Completion tranche, Batch A step 1; resolves R-1 under CR-42 §10.1 and BC-48's findings register. Landing inspection found a latent gate defect that shapes the design: `check_entity_system.py` ES-003 reads a hardcoded `relationships` record key, ignoring the registry's `field: related_capabilities` declaration (why ES-003 has never fired for BC records). The alignment therefore honors the registry config: `related_capabilities` remains the single authoritative carrier (per the registry's own declaration), extended to a typed-capable form; the gate is fixed to read its configured field. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-53-relationship-semantics`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** split from the combined tranche grounding (workspace `CR-DEA-BC-53-to-60-TRANCHE-GROUNDING.md`); normative content verbatim; house block adapted on landing. Landing decisions recorded in §8.

## 2. Change Objective

Resolve finding R-1 by establishing a machine-expressible, semantically explicit representation for canonical Business Capability relationships, aligned with the existing entity-system registry and the applicable upstream semantic authority.

The change shall make it possible to distinguish relationship types without inferring meaning from an untyped list of references.

## 3. Problem Statement

The current canonical record model contains `related_capabilities`, represented as a list of capability identifiers. The entity-system registry already declares relationship types including `depends-on`, `realizes`, and `specializes`, but the existing list representation cannot express those types.

CR-DEA-BC-48 established reference integrity checks without inventing semantics. CR-DEA-BC-47 likewise renders the existing references as untyped associations.

This CR addresses that representation gap. It must not treat the registry's declaration as permission to invent additional types or assume that every existing association has a known type.

## 4. Normative Requirements

### 4.1 Establish relationship semantics

For each relationship type authorized by the applicable registry and upstream semantic authority, document:

- Canonical type identifier.
- Definition and intended interpretation.
- Source and target entity kinds.
- Directionality.
- Cardinality, where governed.
- Whether reciprocity is required, permitted, or not specified.
- Applicable identity and reference rules.
- Evidence required to assert the relationship.
- Lifecycle and deprecation implications.
- Validation requirements.

If an attribute lacks an authoritative definition, record it as unresolved. Do not invent a value to complete the table.

### 4.2 Align the record model

Define the smallest backward-compatible representation that can express authorized relationship types.

The design must consider the existing `related_capabilities` field and the registry's ES-003 contract. It must not introduce a competing relationship system or maintain two independently authoritative representations of the same assertion.

If migration from an untyped list is necessary, establish a deterministic migration procedure. An existing untyped association must not be automatically converted to `depends-on`, `realizes`, or `specializes` without supporting evidence and an approved disposition.

### 4.3 Preserve integrity controls

Retain the valid requirements established by CR-DEA-BC-48:

- Every asserted reference resolves to its canonical target.
- Structured boundary references retain their rationale requirements.
- Reciprocity is not imposed universally.
- Acyclicity is not imposed without authority.
- ECF co-location is not interpreted as a relationship.
- Evidence references are not treated as semantic relationships.

Update `scripts/check_relationship_integrity.py` and related conformance checks only to enforce rules justified by the approved model.

### 4.4 Update derived views

Update the discovery views established by CR-DEA-BC-47 to render typed relationships only when their types are explicitly recorded.

The views must distinguish:

- Typed and validated relationships.
- Legacy associations whose semantics remain unresolved.
- Invalid references.
- Relationship types that remain outside the supported model.

No inferred relationship graph may be published as canonical fact.

## 5. Scope

**In scope**

- Relationship semantic definitions and their authority traceability.
- Record schema and model documentation changes justified by the approved design.
- Affected canonical records and migration.
- Registry alignment, validation, tests, and generated views.
- A migration report identifying typed, unresolved, corrected, and rejected assertions.

**Out of scope**

- New relationship types without semantic authority.
- Upstream WSF or metamodel changes not separately approved by their owners.
- Capability additions, removals, or renames.
- Universal reciprocity or acyclicity rules.
- Reclassification based on names, ECF co-location, or other indirect evidence.

## 6. Acceptance Criteria

1. R-1 has an explicit disposition supported by a documented model decision.
2. Every supported relationship type has an authoritative definition and declared constraints.
3. The canonical schema and entity-system registry agree on the supported representation.
4. Migration does not fabricate relationship types for previously untyped associations.
5. Every migrated assertion has traceable evidence or is explicitly retained as unresolved.
6. Automated tests cover valid typed assertions, invalid types, invalid references, and legacy or unresolved cases.
7. The relationship-integrity gate remains effective.
8. Generated views display only the semantics actually present in the canonical records.
9. All schema, migration, and validation changes are documented and tested.
10. Any upstream semantic dependency that remains unresolved is recorded as a blocker to the affected relationship type, not silently bypassed.

## 7. Dependencies and Execution Conditions

CR-DEA-BC-42 and CR-DEA-BC-43 provide the model analysis and existing model decisions. CR-DEA-BC-48 defines the current integrity baseline.

Before implementation, the CR author must verify the current ES-003 registry contract and any upstream semantic authority required for the proposed representation. If the necessary relationship semantics are not authorized, this CR may implement only the independently authorized subset; the remainder must be deferred explicitly.

---
---

## 8. Landing Decisions and Migration Record (2026-10-28)

1. **Representation (§4.2):** `related_capabilities` items become `oneOf`: the legacy bare canonical id (retained verbatim — backward compatible) OR a typed object `{id, type, rationale}` (strict: `additionalProperties: false`; `type` enum limited to the registry's canonical types `depends-on / realizes / specializes`; non-empty `rationale` required).
2. **Registry alignment (§4.1):** `reconciliation/entity-system-registry.yaml` gains `type_field: type` under `relationships`; `check_entity_system.py` ES-003 now reads the registry-configured field and type key (fixing the latent hardcode defect; divergence note extended). The registry declaration — not the schema alone — is the type authority.
3. **Migration (§4.2):** the 72 existing associations are retained as bare ids — **legacy/unresolved class; zero auto-conversions** (no evidence disposition exists for typing them; conversion requires per-assertion evidence in a future CR). No record content changed in this landing.
4. **Integrity (§4.3):** new RI-005 (typed assertions: type within the registry's canonical set; rationale non-empty; id resolves); RI-004's observation updates from "not expressible" to "expressible since BC-53; population evidence outstanding". RI-001..003 unchanged.
5. **Views (§4.4):** `RELATED-CAPABILITIES.md` renders a Type column distinguishing typed assertions from legacy untyped associations; the no-graph rule stands until typed population justifies one.
6. **READMEs:** the 29 remediated READMEs' §7 legacy sentence updated to state that typed assertions are now representable while these associations remain untyped pending evidence.
7. **Type semantics table:** documented in the Relationship Integrity Standard §2a with attribute-level honesty — cardinality and reciprocity per type are recorded as unresolved (no authority invents them); evidence required per assertion is the registry type + rationale.
