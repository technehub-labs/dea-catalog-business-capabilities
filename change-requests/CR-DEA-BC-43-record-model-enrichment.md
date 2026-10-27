# CR-DEA-BC-43: Canonical Record Model Enrichment

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-43 |
| Title | Canonical Record Model Enrichment |
| Status | Accepted (user directive 2026-10-28: "the next three CRs are attached. Take them for implementation") |
| Series | CR-DEA-BC |
| Change layer | L1 — Canonical record model and schema |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Predecessor | CR-DEA-BC-42 — Canonical Record Model Gap Analysis |
| Normative foundation | CR-DEA-BC-41 — Business Capability Documentation Standard |
| Related foundations | CR-DEA-BC-01, CR-DEA-BC-01A, CR-DEA-BC-03, CR-DEA-BC-29, CR-DEA-BC-35A, CR-DEA-BC-40 |
| Primary deliverables | Approved schema changes, canonical record-model documentation, and associated verification evidence, where justified by CR-42 |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "the next three CRs are attached. Take them for implementation")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Tranche step 3; executes CR-DEA-BC-42's R-2 scope under that CR's execution condition (findings accepted via PR #95). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-43-record-model-enrichment`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim plus the §15 approved manifest appended on landing (per §7).

**Execution condition:** This CR must not be implemented until CR-DEA-BC-42 has been completed and its findings have been accepted. The approved findings must identify the exact model changes authorized under this CR. If CR-42 finds no justified schema changes, this CR must be revised, superseded, or closed without introducing unnecessary model changes.

## 2. Change Objective

Enrich the canonical Business Capability record model where the accepted findings of CR-DEA-BC-42 demonstrate that the current model cannot adequately express a normative requirement of CR-DEA-BC-41.

The objective is to improve the model's semantic precision, expressiveness, integrity, and machine verifiability without duplicating existing representations or exceeding the authority of the repository.

The change must establish an explicit relationship between:

1. The normative documentation requirement.
2. The identified deficiency in the current model.
3. The approved model change.
4. The schema and validation rules implementing the change.
5. The affected canonical records, if any.
6. The tests demonstrating that the change behaves as intended.

This CR is not authorization for general schema expansion. Every implemented change must be traceable to an accepted finding.

## 3. Problem Statement

The Business Capability Documentation Standard defines the information that a canonical capability must communicate. The subsequent model gap analysis determines which requirements the current schema and associated artefacts already satisfy and which require additional representation or stronger constraints.

Where a genuine model deficiency exists, leaving the deficiency unresolved can lead to inconsistent entity definitions, ambiguous relationships, incomplete machine-readable records, and dependence on prose for information that should be governed structurally.

Conversely, introducing properties without a demonstrated semantic need can fragment the source of truth, increase record complexity, and create divergence from upstream semantic foundations.

The repository therefore needs a controlled implementation mechanism that converts approved gap findings into minimal, testable model changes.

## 4. Intended Outcome

The intended outcome is a canonical record model that can represent the approved requirements identified by CR-42 while preserving existing repository contracts.

Where implementation is justified, the resulting changes must provide:

- Explicit and stable property semantics.
- Defined value types and constraints.
- Clear mandatory, conditional, and optionality rules.
- Unambiguous relationships to existing canonical concepts.
- Consistent interaction with evidence, provenance, boundaries, and conformance metadata.
- Deterministic validation behavior.
- A migration strategy for affected canonical records.
- Documentation sufficient for authors and maintainers to use the model correctly.

The resulting model must remain a specialization of the established semantic foundation rather than a competing capability metamodel.

## 5. Governing Principles

### 5.1 Findings before implementation

CR-42 is the authoritative source for the gaps this CR is permitted to address.

A change that is absent from the accepted CR-42 findings must not be introduced under this CR without a formally approved scope amendment.

### 5.2 Minimal sufficient change

Implement the smallest model change that adequately resolves each accepted gap.

A new property must not be added if an existing property, relationship, controlled value, or authoritative reference can satisfy the requirement without ambiguity.

### 5.3 Semantic precision

Each new or modified property must have a documented meaning that distinguishes it from neighboring concepts.

Names, descriptions, value types, cardinality, constraints, and examples must be mutually consistent.

Where the semantic meaning cannot be established without an upstream decision, implementation must stop for that item until the decision is resolved.

### 5.4 Canonical source of truth

The canonical structured record remains authoritative for the semantics assigned to its fields under the repository's existing conventions.

The README and supporting documentation must explain the model rather than establish competing values for the same facts.

### 5.5 Compatibility and migration discipline

Existing canonical records must remain valid unless an explicitly approved migration changes their representation.

The change must not satisfy new requirements by fabricating unsupported facts, evidence, relationships, or enterprise-specific information.

### 5.6 Existing governance remains binding

This CR must preserve the established entity identity system, CR process, conformance contract, versioning policy, and repository integrity requirements.

It must not silently modify upstream metamodel or ECF semantics.

## 6. Scope

### 6.1 In scope

Subject to accepted CR-42 findings, this CR may authorize:

1. Addition of explicitly justified canonical schema properties.
2. Modification of existing property definitions or constraints.
3. Formalization of mandatory, conditional, and optionality rules.
4. Clarification of value types, cardinality, enumerations, or validation behavior.
5. Changes to canonical record examples needed to demonstrate the approved model.
6. Migration of existing records where required by an approved schema change.
7. Updates to model documentation and record-authoring guidance.
8. Tests and validators necessary to enforce the implemented model.
9. Documentation of compatibility and migration outcomes.
10. Updates to repository indexes and registers required by the established governance process.

Each authorized change must be listed in the approved change manifest described in Section 7.

### 6.2 Out of scope

This CR does not authorize:

- Changes unsupported by accepted CR-42 findings.
- Redefinition of Business Capability or Capability semantics.
- Changes to upstream DEA metamodel constructs.
- Changes to WSF or OpenDEAM semantic foundations.
- Changes to the organization-wide entity identity or storage-layout system.
- Changes to the ECF coordinate system or conformance contract.
- Creation of new relationship semantics without the required authority.
- Changes to the catalog's capability inventory.
- New capability admissions, retirements, merges, or renames.
- General-purpose README rewriting unrelated to the approved model changes.
- Changes to assessment-model ownership, scoring, or benchmark definitions.
- Unrelated CI, release, tagging, or repository restructuring.

Any item outside these boundaries must be proposed through a separate CR or an explicitly approved scope amendment.

## 7. Required Change Manifest

Before implementation begins, the CR must contain an approved change manifest derived from CR-42.

The manifest must identify every model change covered by this CR.

| Field | Required content |
|---|---|
| Change ID | Stable identifier for the individual model change |
| Source requirement | Requirement identifier from CR-41 |
| Gap finding | Exact finding reference from CR-42 |
| Current limitation | Why the existing model is insufficient |
| Proposed change | Specific property, constraint, relationship representation, or model rule |
| Semantic definition | Intended meaning and distinction from existing concepts |
| Data representation | Type, structure, cardinality, and allowed values, where applicable |
| Requirement class | Mandatory, conditional, optional, or prohibited |
| Conditionality rule | Explicit condition where the requirement is not universal |
| Compatibility assessment | Effect on existing records and consumers |
| Migration approach | Required migration or explicit statement that none is needed |
| Validation | Test or check that proves the change is correct |
| Authority dependencies | Required upstream decisions, if any |
| Acceptance criteria | Observable conditions for successful implementation |

No property or constraint may be implemented solely because it appears in a proposed design. It must have a traceable entry in this manifest.

If CR-42 identifies multiple independent changes, the repository governance process may determine that they should be separated into distinct CRs rather than bundled together.

## 8. Implementation Requirements

### 8.1 Property definitions

For each approved new or modified property, document:

- Canonical property name.
- Semantic definition.
- Data type and structure.
- Cardinality.
- Allowed values or value constraints.
- Whether the property is mandatory, conditional, optional, or prohibited.
- Any dependencies on other properties.
- Whether the value is local, a canonical reference, or an external reference.
- Examples of valid and invalid representations, where useful.
- Relationship to existing properties and authoritative artefacts.

A property must not be added if its intended meaning cannot be distinguished from another property without introducing an explicit semantic decision.

### 8.2 Conditionality and validation

Where a requirement applies only under certain conditions, those conditions must be defined precisely enough to support consistent authoring and validation.

The implementation must distinguish:

- Missing information.
- Explicitly unknown information.
- Inapplicable information.
- Invalid information.
- Information represented by an authoritative reference.

These states must not be conflated or represented through invented values. The exact representation must follow the accepted model design and repository conventions.

### 8.3 Relationships and references

Any approved relationship or reference change must identify:

- The concepts being related.
- The intended semantic meaning.
- The applicable target identity or reference format.
- Cardinality and integrity constraints.
- Whether the relationship is internal to the catalog or points to an external authority.
- The validation method.
- Any required upstream approval.

This CR must not create a new relationship type merely to simplify presentation or fill a documentation section.

### 8.4 Evidence and provenance

Changes involving evidence or provenance must preserve the distinction between:

- Evidence supporting the admission or definition of a capability.
- Provenance describing the origin or history of information.
- Relationships describing the capability's semantic context.
- Assessment results describing an evaluation.
- Performance data describing observed operation.

The implementation must not merge these responsibilities into one undifferentiated property.

### 8.5 Boundaries and specialization

Where the accepted gap analysis justifies changes related to boundaries or specialization, the implementation must preserve the distinction between:

- What a capability represents.
- What falls outside its scope.
- Examples that must not be interpreted as separate capabilities.
- Rules governing legitimate specializations.
- Relationships to related capabilities.

Existing properties must be reused where they already express these distinctions adequately.

### 8.6 Schema and record compatibility

The implementation must assess the effect of each change on existing records.

For additive changes, the CR must specify whether existing records remain valid and how conditionality is enforced.

For changes to existing fields, it must document:

- The previous interpretation.
- The new interpretation.
- The reason the change is necessary.
- Whether existing values require transformation.
- How downstream consumers are affected.
- Whether a schema version or release decision is required.

Breaking changes must not be disguised as additive changes.

### 8.7 Canonical record migration

Where migration is required, it must be limited to records affected by the approved changes.

Migration rules must be deterministic wherever the source data permits.

Where human judgment or new evidence is required, the record must remain unresolved until the required evidence or decision is obtained. Migration must not infer facts solely to satisfy schema constraints.

The CR must record:

- The affected record set.
- The migration method.
- Any manual review required.
- Validation before and after migration.
- A summary of changes.
- Exceptions and unresolved records.

## 9. Verification Requirements

Verification must demonstrate both structural validity and semantic consistency.

### 9.1 Schema verification

Tests must demonstrate that:

- Valid records conform to the updated schema.
- Invalid representations are rejected.
- Required properties are enforced under the correct conditions.
- Optional and inapplicable properties behave as specified.
- Existing valid records remain valid unless explicitly subject to an approved migration.
- Reference and relationship constraints are enforced where supported.

### 9.2 Canonical record verification

Where records are modified, verification must establish that:

- Existing entity identities are preserved.
- Existing definitions are not altered without authorization.
- New values are supported by source evidence or approved decisions.
- Relationships resolve correctly.
- Provenance remains traceable.
- ECF conformance remains valid.
- No unrelated record changes have been introduced.

### 9.3 Cross-artifact verification

The updated schema, authoring guidance, examples, README documentation, and conformance rules must describe the same model.

Where a property is documented in multiple places, the repository must preserve a clear authority hierarchy and avoid conflicting definitions.

### 9.4 Regression verification

Existing applicable repository checks must continue to pass.

The implementation must not weaken, bypass, or remove existing controls merely to accommodate the new model.

Any unrelated pre-existing failure must be recorded and handled according to the repository's established governance process.

## 10. Required Deliverables

Subject to the approved change manifest, deliver the applicable items below:

1. Updated canonical schema.
2. Updated model documentation and authoring guidance.
3. Updated canonical records, only where authorized and required.
4. Migration instructions or migration evidence, where applicable.
5. Schema and validator tests.
6. Cross-artifact consistency verification.
7. Compatibility and regression test results.
8. Updated repository documentation indexes and change registers.
9. A verification summary linking each manifest item to its implementation and test evidence.

A deliverable that is not required by the approved change manifest must not be added merely to make the CR appear more comprehensive.

## 11. Acceptance Criteria

CR-DEA-BC-43 may be accepted only when all applicable criteria are satisfied.

### AC-01 — CR-42 findings accepted

The implementation is traceable to an accepted CR-42 analysis. Each implemented change has an explicit finding reference.

### AC-02 — Change manifest approved

The CR contains a complete, approved manifest identifying every property or constraint change in scope.

### AC-03 — Semantic definitions complete

Every new or modified property has an unambiguous definition, data representation, constraints, and relationship to existing concepts.

### AC-04 — No unjustified duplication

No implemented change duplicates an existing property, relationship, authoritative reference, or governance mechanism without a documented reason.

### AC-05 — Conditionality explicit

Mandatory, conditional, optional, and prohibited representations are distinguished and enforced as specified.

### AC-06 — Upstream authority preserved

No unapproved upstream metamodel, WSF, OpenDEAM, identity, or ECF changes are introduced.

### AC-07 — Relationship semantics authorized

Every new or changed relationship representation is covered by an accepted finding and has the required semantic authority.

### AC-08 — Compatibility assessed

The effects on existing records, schema consumers, and repository conventions are documented.

### AC-09 — Migration controlled

Every required migration is bounded, traceable, and verified. No unsupported values have been invented.

### AC-10 — Canonical records remain coherent

Affected records conform to the updated model and preserve identity, definition, evidence, provenance, and ECF conformance except where an explicitly approved change states otherwise.

### AC-11 — Tests enforce the model

Applicable schema, validator, reference-integrity, and regression checks pass.

### AC-12 — Documentation is consistent

The schema, examples, authoring guidance, and relevant README material describe the same model and respect the repository's source-of-truth rules.

### AC-13 — Repository governance is preserved

The CR register, documentation indexes, and integrity controls are updated in accordance with existing conventions.

### AC-14 — Scope is respected

No unapproved capability inventory changes, upstream semantic changes, or unrelated repository modifications are introduced.

### AC-15 — No-op outcome is permitted

If the accepted CR-42 analysis identifies no justified model changes, this CR must not introduce speculative schema modifications. The repository governance process must record the disposition and determine whether the CR should be closed or replaced with a more appropriate implementation CR.

## 12. Risks and Controls

| Risk | Control |
|---|---|
| Premature schema expansion | Require accepted CR-42 findings and an approved change manifest |
| Duplicate sources of truth | Require explicit reuse analysis for each property |
| Semantic ambiguity | Require formal property definitions and relationship constraints |
| Unintended breaking changes | Require compatibility analysis and explicit migration authorization |
| Fabricated migration values | Require evidence-backed population and explicit handling of unresolved information |
| Upstream semantic drift | Require upstream dependencies to be resolved before implementation |
| Assessment and capability semantics become conflated | Preserve existing ownership and representation boundaries |
| Existing controls are weakened | Require regression tests and preserve repository integrity gates |
| Excessive bundling | Permit independent implementation CRs for changes with different dependencies or risk profiles |

## 13. Definition of Done

This CR is complete when:

1. The accepted CR-42 findings have been translated into an approved change manifest.
2. Every authorized model change is implemented and traceable to a requirement.
3. Schema and authoring documentation are consistent.
4. Required canonical record migrations are complete and verified, where applicable.
5. Validation demonstrates structural and referential integrity.
6. Existing conformance and governance controls remain effective.
7. Compatibility and regression evidence is recorded.
8. Repository indexes and the CR register are updated.
9. No unauthorized changes have been introduced.
10. The repository's prescribed landing and verification process is complete.

## 14. Acceptance Decision

**Requested decision:** Approve CR-DEA-BC-43 as a conditional implementation CR, subject to completion and acceptance of CR-DEA-BC-42 and approval of the resulting change manifest.

Approval of this draft alone does not authorize implementation of unspecified schema changes.

Implementation is limited to the changes explicitly identified and approved through the CR-42 findings and this CR's final manifest. Any additional model changes require a scope amendment or a separate CR under the repository's established governance process.

---

## 15. Approved Change Manifest (landing, 2026-10-28; derived from CR-DEA-BC-42 R-2)

Per §7 and the execution condition, implementation is limited to the manifest below, each item traceable to an accepted CR-42 finding:

| Change ID | Source | Finding (CR-42 §) | Change | Class | Compatibility / migration | Validation |
|---|---|---|---|---|---|---|
| M-1 purpose conditionality | BC-DOC-003 (CR-41 §3.3) | §5 row BC-DOC-003-adjacent; §6 `purpose` (B/C) | schema description amended: `purpose` is recommended, populate only with authored evidence; no bulk fabrication; population deferred to remediation CR R-5 | Recommended (not mandatory) | Additive description only; 0/29 records affected; no migration | schema loads; 29/29 records + fixture still validate |
| M-2 realization formats | BC-DOC-006 | §5 row BC-DOC-006; §6 `realization` (C+D); §10.2 | `realization.processes` items constrained to `^processes:` (confirmed sibling scheme); other arrays carry target-format guidance (U-2 pending for actors/resources/systems/information) | Conditionally mandatory when populated | Additive constraint on an unpopulated field (0/29) — non-breaking today; future prose values rejected by design | fixture exercises `processes:process-…` form; invalid-form fixture case |
| M-3 boundary-form applicability | BC-DOC-004 | §5 row BC-DOC-004 (B) | schema description note: structured `boundary` form applies when the BC-29 rich-narrative justification exists (e.g. governance-object/loop contexts); plain string otherwise | Guidance | None | schema loads; both forms still validate |
| M-4 record-model documentation | CR-43 §8.1 | §4 inventory | `docs/BUSINESS-CAPABILITY-RECORD-MODEL.md`: per-property semantic definitions, requirement classes, conditionality rules | Documentation | None | doc-links gate |
| M-5 escalations recorded | CR-43 §5.1/5.6 | §6 `relationship_assertions` (E->R-1), `business_object_ref` (F->U-1), assessment candidates (G) | explicit statements in the model doc; no local implementation | Record-only | None | manifest cross-references resolve |

**Explicitly out of this CR** (routed per CR-42 §13): relationship typing (R-1), business-object cross-references (U-1), README/template work (R-3/BC-44), gates (R-4), population backfill (R-5), views (R-6). No canonical record is modified; no migration occurs (CR-42 §12).
