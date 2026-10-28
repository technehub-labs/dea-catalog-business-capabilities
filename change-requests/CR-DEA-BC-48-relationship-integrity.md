# CR-DEA-BC-48: Canonical Relationship Integrity

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-48 |
| Title | Canonical Relationship Integrity |
| Status | Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement") |
| Series | CR-DEA-BC |
| Change layer | L1 — Semantic relationships and referential integrity |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Dependencies | Accepted canonical model; applicable findings from CR-42/43; accepted validation contract from CR-45 |
| Primary deliverable | Canonical Relationship Integrity Standard and verified relationship inventory |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Governance tranche step 1; executes within the accepted model (CR-42/43: relationship typing deferred to R-1 — this CR governs the integrity of relationship representations AS THEY EXIST, inventing no new types) and the accepted validation contract (CR-45). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-48-relationship-integrity`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Evidence base gathered at landing: 72 directed `related_capabilities` references across 29 records (32 reciprocal pairs; reciprocity observed but not required by the model); 6 structured-boundary references (all resolving); 0 self-references; `parents`/`children` unused (0/29); registry ES-003 declaration present with types not yet expressible (the R-1 gap, recorded as a finding, not a failure).


## 2. Change Objective

Establish a controlled method for verifying the integrity, interpretation, and traceability of relationships represented in the canonical Business Capability catalog.

The CR shall ensure that relationships between capabilities are supported by the canonical model, have an unambiguous interpretation, resolve to valid targets, and do not imply unsupported hierarchy, dependency, equivalence, or specialization.

## 3. Problem Statement

Relationships improve semantic discovery only when their meaning is stable and their representation is trustworthy.

A catalog can contain syntactically valid references that are semantically ambiguous, point to invalid entities, or imply a relationship that has not been established through the repository's governance process.

Generated views can amplify these defects by presenting relationships as authoritative facts.

The repository therefore needs explicit controls distinguishing a valid reference from a formally governed semantic relationship.

## 4. Scope

### In scope

1. Inventory the relationship types already supported by the canonical model.
2. Document their established semantics and constraints.
3. Verify relationship targets and reference integrity.
4. Identify ambiguous, unsupported, or inconsistent relationships.
5. Define rules for reciprocal relationships where required by the existing model.
6. Establish relationship-level validation and review criteria.
7. Record unresolved semantic questions for separate CRs.
8. Ensure generated discovery views use only authorized relationship data.

### Out of scope

- Inventing new relationship types.
- Redefining upstream metamodel relationships.
- Changing the ECF or organization-wide identity standard.
- Creating new capabilities to resolve apparent relationship gaps.
- Inferring relationships from names, shared classifications, or proximity in a diagram.
- Introducing a new ontology or graph platform.

## 5. Normative Principles

### 5.1 References are not automatically relationships

A link to another entity is not necessarily a formal semantic relationship. The interpretation must follow the existing model and the authority of the source.

### 5.2 Relationship semantics must be explicit

Every formally represented relationship must have a defined meaning, valid target, and applicable constraints.

### 5.3 No unsupported inference

The implementation must not infer parent-child, dependency, equivalence, specialization, or other semantic relationships without an authorized basis.

### 5.4 Canonical sources remain authoritative

Any relationship inventory or graph is derived from canonical data. It must not become an independent source of relationship truth.

## 6. Required Analysis

The implementation must inventory each relationship representation currently used by canonical records.

For each supported relationship, record:

| Attribute | Required content |
|---|---|
| Relationship identifier | Existing canonical type or field name |
| Semantic definition | Meaning established by the governing model |
| Source and target | Permitted entity types |
| Cardinality | Constraints defined by the model |
| Directionality | Directed, reciprocal, or not applicable |
| Integrity rules | Required target and consistency checks |
| Authority | Governing schema or semantic specification |
| Validation method | Automated or manual |
| Known limitations | Unresolved or unsupported cases |

The inventory must distinguish formally governed relationships from simple references and explanatory links.

## 7. Integrity Controls

Where supported by the existing model, validation must check:

1. Referenced entity identifiers exist.
2. References resolve to the intended entity.
3. Relationship values conform to the accepted schema.
4. Directionality is interpreted consistently.
5. Required reciprocal representations are present where the model mandates them.
6. Prohibited self-references or cycles are rejected only where the existing semantics prohibit them.
7. Relationships do not contradict established specialization boundaries.
8. Generated views do not introduce relationships absent from canonical sources.

The validator must not impose a universal acyclic-graph rule unless the governing relationship semantics require it.

## 8. Required Deliverables

- Canonical Relationship Integrity Standard.
- Inventory of existing relationship representations.
- Relationship validation rules.
- Findings register for ambiguous or invalid relationships.
- Tests for applicable integrity constraints.
- Documentation updates for relationship authors and maintainers.

Proposed document path:

`docs/CANONICAL-RELATIONSHIP-INTEGRITY-STANDARD.md`

The final path must follow the repository's documentation conventions.

## 9. Acceptance Criteria

- **AC-01:** All existing relationship representations in scope are inventoried.
- **AC-02:** Each formal relationship has a traceable semantic authority.
- **AC-03:** References and formal relationships are distinguished.
- **AC-04:** Target integrity is validated where deterministic.
- **AC-05:** Directionality and reciprocal requirements follow the actual model.
- **AC-06:** No unsupported relationship type is introduced.
- **AC-07:** Ambiguous relationships are recorded for separate resolution.
- **AC-08:** Generated views consume only authorized relationship data.
- **AC-09:** Tests cover valid and invalid relationship cases.
- **AC-10:** Existing schema, identity, ECF, and repository integrity controls remain effective.

## 10. Definition of Done

The relationship standard, inventory, applicable validation rules, and tests are complete and discoverable. Unresolved semantic questions are documented rather than silently converted into new relationship rules.

## 11. Acceptance Decision

**Requested decision:** Approve the controlled verification and governance of existing canonical capability relationships.

Approval does not authorize new relationship semantics or upstream metamodel changes. Any such change requires separate authorization.