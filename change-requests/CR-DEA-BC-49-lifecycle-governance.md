# CR-DEA-BC-49: Capability Lifecycle Governance

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-49 |
| Title | Capability Lifecycle Governance |
| Status | Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement") |
| Series | CR-DEA-BC |
| Change layer | L2 — Entity lifecycle and governance |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Dependencies | Existing lifecycle conventions; organization-wide entity governance; accepted CR-41 documentation requirements |
| Primary deliverable | Canonical Capability Lifecycle Governance Standard |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Governance tranche step 2. AC-01 evidence inspected at landing: the schema `lifecycle_status` enum is the upstream vocabulary (proposed/planned/active/deprecated/retired; dea-metamodel lifecycle.yaml); the entity-system registry carries the 9-state admission ladder (candidate→…→retired, retired terminal; informational ladder in `provenance`, ES-004 not enforced for BC by construction); all 29 records are currently `active`; CR-status conventions govern the change layer. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-49-lifecycle-governance`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. The standard formalizes the EXISTING two-axis model (admission ladder vs record status) without schema changes; no new status values are introduced.

## 2. Change Objective

Establish explicit governance for the lifecycle of canonical Business Capability entities, including admission, maintenance, review, supersession, retirement, and archival where those states are supported by existing repository policy.

The CR must clarify permitted lifecycle transitions, required evidence, decision authority, and the effects of each transition on references and derived catalog views.

It must not introduce lifecycle states that conflict with existing repository conventions.

## 3. Problem Statement

A canonical entity is not governed solely by its initial admission. Its definition, supporting evidence, relationships, and relevance may change over time.

Without explicit lifecycle rules, contributors may interpret status values differently, modify canonical records without appropriate review, or remove entities whose identifiers are still referenced elsewhere.

Lifecycle governance must therefore define what changes are permitted, who or what authorizes them, and how the catalog preserves historical traceability.

## 4. Scope

### In scope

1. Inventory existing entity status and lifecycle conventions.
2. Define lifecycle states and their meanings, reusing established values where possible.
3. Define permitted state transitions.
4. Identify the evidence and approvals required for each transition.
5. Define how supersession and retirement affect canonical identifiers and references.
6. Clarify the treatment of historical records and audit trails.
7. Establish lifecycle conformance checks.
8. Document lifecycle responsibilities for maintainers and reviewers.

### Out of scope

- Changing the organization-wide identity system.
- Redefining the canonical schema without a separate model CR.
- Deleting historical change requests.
- Automatically retiring entities based on usage or popularity.
- Introducing a new versioning or release policy.
- Changing capability semantics merely to justify a lifecycle transition.

## 5. Lifecycle Governance Principles

### 5.1 Identity survives lifecycle change

An entity's canonical identity must not be silently reassigned to a different semantic concept.

Where an entity is superseded or retired, existing references and history must remain interpretable under the established identity policy.

### 5.2 Status must have defined meaning

A status value must indicate a governed lifecycle condition, not an informal quality judgment.

For example, a lifecycle status must not be used as a substitute for a documentation-conformance result unless existing governance explicitly defines that relationship.

### 5.3 Transition requires authorization

Every lifecycle transition must have an identifiable authority and a traceable decision.

### 5.4 Retirement is not deletion

Retiring an entity must not automatically erase its provenance, historical decisions, or references.

The exact representation of retired entities must follow the existing schema and identity policy.

## 6. Required Lifecycle Model

The analysis must inspect the current status field and repository lifecycle conventions before prescribing state names.

The standard must document, for each supported state:

- State identifier.
- Meaning.
- Entry conditions.
- Permitted outgoing transitions.
- Required evidence.
- Approval authority.
- Reference-handling rules.
- Effect on discovery views.
- Validation requirements.

A transition table must identify permitted transitions and prohibited shortcuts.

The standard may consider admission, active maintenance, supersession, retirement, and archival concepts only where they can be reconciled with existing conventions. It must not force these labels into the canonical schema without a justified model decision.

## 7. Lifecycle Transition Requirements

Each governed transition must identify:

1. The entity affected.
2. The previous and resulting states.
3. The reason for the transition.
4. The approving CR or other authorized decision.
5. Any required evidence or review.
6. The effect on related entities and references.
7. Any required documentation or generated-view updates.
8. The verification needed to establish a valid transition.

If a transition requires schema support that does not exist, the gap must be handled through the applicable model-change process.

## 8. Supersession and Retirement

The standard must distinguish between:

- A correction to an entity that retains its meaning and identity.
- A revision that changes its meaning but may retain identity under the established versioning policy.
- A split into distinct concepts.
- A merge of previously distinct concepts.
- Supersession by another canonical entity.
- Retirement without replacement.

The standard must not assume that all of these operations are equivalent.

Where an entity is superseded, the record must preserve sufficient traceability to explain the transition. Replacement relationships may only be represented using an authorized mechanism.

## 9. Required Deliverables

- Capability Lifecycle Governance Standard.
- Lifecycle state and transition matrix.
- Required evidence and approval rules.
- Guidance for supersession, retirement, and historical traceability.
- Lifecycle conformance requirements.
- Documented dependencies requiring separate model or identity changes.

Proposed document path:

`docs/CAPABILITY-LIFECYCLE-GOVERNANCE-STANDARD.md`

## 10. Acceptance Criteria

- **AC-01:** Existing lifecycle fields and conventions are inspected before changes are proposed.
- **AC-02:** Every supported lifecycle state has an explicit meaning.
- **AC-03:** Permitted and prohibited transitions are documented.
- **AC-04:** Transition authorization and evidence requirements are defined.
- **AC-05:** Identity preservation and historical traceability are addressed.
- **AC-06:** Supersession is distinguished from deletion and retirement.
- **AC-07:** Relationship and discovery-view impacts are addressed.
- **AC-08:** No incompatible status values are introduced.
- **AC-09:** Any required schema changes are separately authorized.
- **AC-10:** Lifecycle documentation is indexed and verifiable.

## 11. Definition of Done

The lifecycle standard and transition matrix are complete, consistent with existing repository governance, and reviewable. Any unresolved schema or identity dependency is explicitly recorded.

## 12. Acceptance Decision

**Requested decision:** Approve the formalization of canonical capability lifecycle governance.

Approval establishes lifecycle rules only within the authority of this repository. It does not authorize changes to organization-wide identity or upstream semantic foundations.