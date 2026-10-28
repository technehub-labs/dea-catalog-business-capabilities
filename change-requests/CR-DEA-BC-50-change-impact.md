# CR-DEA-BC-50: Canonical Entity Change Impact Management

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-50 |
| Title | Canonical Entity Change Impact Management |
| Status | Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement") |
| Series | CR-DEA-BC |
| Change layer | L2 — Change governance and dependency management |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Dependencies | Existing CR governance; organization-wide entity identity standard; accepted lifecycle governance from CR-49 |
| Primary deliverable | Canonical Entity Change Impact Management Standard |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Governance tranche step 3; builds on the landed control surface (gates AUT/ES/IDM/CST/DL/CR/DCV/RI; regeneration + views freshness; lifecycle standard CR-49). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-50-change-impact`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Deliverables: the standard at `docs/ENTITY-CHANGE-IMPACT-STANDARD.md`, the reusable assessment template at `docs/templates/ENTITY-CHANGE-IMPACT-ASSESSMENT.md`, and a worked example (CR-DEA-BC-23, the EPM admission) embedded in the standard.

## 2. Change Objective

Establish a repeatable process for assessing the effects of proposed changes to canonical Business Capability entities before those changes are accepted.

The process must identify affected records, relationships, documentation, evidence, validators, generated views, and downstream consumers where known.

It must ensure that changes are scoped, traceable, and reviewed according to their actual semantic and operational impact.

## 3. Problem Statement

A change to a canonical capability can affect more than its own record. Renaming an entity may affect links and indexes. Revising its definition may change the interpretation of related capabilities. Changing a relationship may affect discovery views. Retiring an entity may leave unresolved references.

A CR that lists only the file to be edited may fail to capture these dependencies.

The repository needs a consistent impact-assessment practice that helps reviewers understand what changes, what remains invariant, and what must be verified before landing.

## 4. Scope

### In scope

1. Define an impact-assessment procedure for canonical entity changes.
2. Identify change categories and their expected review requirements.
3. Require identification of affected canonical records and artefacts.
4. Establish semantic, referential, documentation, validation, and lifecycle impact categories.
5. Define evidence requirements for change decisions.
6. Establish rules for unresolved downstream impacts.
7. Provide a reusable impact-assessment template.
8. Clarify when separate CRs are required.

### Out of scope

- Replacing the repository's existing CR process.
- Changing identity or versioning policy.
- Automatically approving changes based on an impact score.
- Automatically inferring semantic consequences.
- Changing upstream metamodels.
- Requiring a new external dependency-tracking platform.

## 5. Change Categories

The standard must distinguish at least the following categories.

### 5.1 Editorial change

Changes presentation without changing canonical meaning.

### 5.2 Record-structure change

Changes the representation or constraints of canonical data.

### 5.3 Semantic change

Changes the definition, boundary, classification, specialization, or interpretation of a capability.

### 5.4 Relationship change

Adds, removes, or changes an authorized semantic relationship.

### 5.5 Lifecycle change

Changes an entity's governed status or lifecycle state.

### 5.6 Identity change

Affects identifiers, canonical naming, storage layout, or references governed by organization-wide policy.

Identity changes must follow the relevant higher-level governance rules and must not be approved solely through a capability-catalog CR.

### 5.7 Governance or validation change

Changes the rules, checks, approval requirements, or evidence used to maintain the catalog.

A single CR may cover more than one category only when their dependencies and acceptance conditions remain manageable and explicit.

## 6. Required Impact Assessment

Every CR that materially changes a canonical entity must assess applicable impacts across the following dimensions:

| Dimension | Questions to resolve |
|---|---|
| Semantic | Does the entity's meaning, scope, or interpretation change? |
| Identity | Are identifiers or canonical references affected? |
| Relationships | Which related entities or relationship constraints are affected? |
| Documentation | Which READMEs, templates, indexes, or guidance require updates? |
| Evidence | Does the change alter the evidential basis or provenance? |
| Validation | Which schema, integrity, or conformance checks are affected? |
| Lifecycle | Does the change require a state transition or historical record? |
| Derived views | Which generated indexes or diagrams become stale? |
| Consumers | Which known downstream users or artefacts depend on the changed representation? |
| Migration | Must existing records or references be transformed? |

For each applicable dimension, the CR must state the expected impact or explicitly record that no impact was identified and why.

## 7. Impact Assessment Artefact

Each applicable CR must contain or reference an impact assessment recording:

- Change identifier.
- Target entity or artefact.
- Current state.
- Proposed state.
- Change category.
- Affected entities and artefacts.
- Evidence supporting the assessment.
- Required approvals.
- Verification requirements.
- Known uncertainties.
- Deferred work and its owning CR, where applicable.

The repository should adopt an appropriate reusable template, using existing conventions rather than creating a competing change-management process.

## 8. Review and Escalation

The standard must define when a change requires additional review.

Escalation is required when a proposed change:

- Alters upstream semantic meaning.
- Affects organization-wide identity rules.
- Changes the meaning of an existing relationship.
- Requires an unsupported schema construct.
- Creates incompatible changes for known consumers.
- Cannot be assessed because essential evidence is missing.
- Combines independent changes with materially different approval requirements.

The assessment must support decisions; it must not replace the repository's existing approval authority.

## 9. Acceptance Criteria

- **AC-01:** Applicable entity changes include an impact assessment.
- **AC-02:** Change categories have clear definitions.
- **AC-03:** Semantic and structural changes are distinguished.
- **AC-04:** Identity and upstream dependencies are explicitly recognized.
- **AC-05:** Affected records, references, documentation, and validators are identified where known.
- **AC-06:** Migration and downstream impacts are assessed.
- **AC-07:** Unknown impacts are recorded rather than assumed absent.
- **AC-08:** Escalation conditions are explicit.
- **AC-09:** The standard integrates with existing CR governance.
- **AC-10:** A reusable template and examples are available.
- **AC-11:** No external platform or new automation is required without separate authorization.

## 10. Definition of Done

The impact-management standard and reusable assessment format are complete, indexed, and consistent with existing repository governance. The standard provides an auditable basis for scoping and reviewing canonical entity changes.

## 11. Acceptance Decision

**Requested decision:** Approve the canonical entity change impact-management standard and associated template.

Approval does not replace existing CR approval requirements or authorize automated semantic decisions.