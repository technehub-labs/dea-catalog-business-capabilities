# CR-DEA-BC-42: Canonical Record Model Gap Analysis

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-42 |
| Title | Canonical Record Model Gap Analysis |
| Status | Accepted (user directive 2026-10-28: "the next three CRs are attached. Take them for implementation") |
| Series | CR-DEA-BC |
| Change layer | L1 — Canonical data model and schema analysis |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Predecessor | CR-DEA-BC-41 — Business Capability Documentation Standard |
| Related foundations | CR-DEA-BC-01, CR-DEA-BC-01A, CR-DEA-BC-03, CR-DEA-BC-29, CR-DEA-BC-35A, CR-DEA-BC-40 |
| Upstream dependencies | `dea-metamodel` 1.0.0; OpenDEAM v0.2.1; ECF conformance contract `dea:ecf@1.0.0`; organization-wide entity identity standards |
| Primary deliverable | `docs/BUSINESS-CAPABILITY-RECORD-MODEL-GAP-ANALYSIS.md` |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "the next three CRs are attached. Take them for implementation")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Enrichment tranche step 2 (grounding `CR-DEA-BC-DOC-000.md` §3; CR-DEA-BC-41 §3.6/§7.1 gate schema work on a gap analysis). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-42-record-model-gap-analysis`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme and landed with normative content verbatim; the metadata table's Status row and this house block were adapted on landing.

**Dependency condition:** CR-DEA-BC-41 must be accepted, or its final normative requirements must be explicitly confirmed by the repository's CR governance process, before this CR's requirements mapping is treated as authoritative.

## 2. Change Objective

Establish an evidence-based assessment of whether the current canonical business capability record model can express the requirements of the Business Capability Documentation Standard without ambiguity, duplication, or loss of semantic integrity.

The assessment shall distinguish between:

1. Requirements already supported by existing fields and structures.
2. Requirements supported by existing fields but inadequately defined or constrained.
3. Requirements supported by references to other governed artefacts.
4. Requirements that cannot be represented adequately in the current model.
5. Requirements that belong outside the canonical record and must remain in documentation, governance, evidence, or other authoritative artefacts.

The result shall be a controlled model-enrichment specification identifying which changes, if any, merit a subsequent implementation CR.

## 3. Problem Statement

The repository already has an established canonical record shape, entity identity conventions, evidence and provenance mechanisms, boundary and specialization information, and ECF conformance controls.

The Business Capability Documentation Standard introduces a more explicit account of the information a complete capability definition must communicate. That does not automatically imply that the record schema needs an equivalent number of new fields.

A direct conversion of each documentation aspect into a schema property would risk:

- Duplicating information already represented by existing properties.
- Introducing competing sources of truth.
- Mixing semantic definitions with presentation and governance metadata.
- Adding relationships that have no approved metamodel semantics.
- Making fields mandatory when they are only relevant to particular capability types or circumstances.
- Duplicating upstream metamodel or ECF responsibilities.
- Increasing record complexity without improving semantic precision or machine validation.

The repository therefore requires a documented mapping from normative requirements to the current model before schema expansion or catalog-wide migration is authorized.

## 4. Intended Outcome

This CR shall produce a traceable model gap analysis and a set of precise recommendations for the next implementation decision.

The analysis must establish, for every applicable documentation requirement:

- Its normative source.
- Its semantic intent.
- The existing record field, relationship, reference, or artefact that satisfies it.
- Whether the representation is direct, indirect, conditional, or absent.
- Any ambiguity, constraint deficiency, or consistency risk.
- Whether a schema change is necessary.
- The expected benefit and migration impact of any proposed change.
- The validation required to prove conformance.

The output is a model decision artefact, not an assumption that every identified gap must result in a new property.

## 5. Normative Principles

### 5.1 Preserve canonical semantics

The repository's established definition of Business Capability remains authoritative unless a separately approved change establishes otherwise.

The current definition must not be rewritten as a side effect of this analysis.

### 5.2 Reuse before extension

An existing property, relationship, controlled vocabulary, or authoritative reference must be reused when it adequately expresses the requirement.

A new property must not be introduced merely to make a record resemble the headings of its README.

### 5.3 Separate semantics from presentation

The canonical structured record carries the authoritative machine-readable semantics assigned to it by the existing repository conventions.

The README explains those semantics to human readers. It must not become an alternative source of canonical field values.

### 5.4 Respect upstream authority

This CR must not independently redefine:

- The canonical Capability construct or other upstream metamodel constructs.
- Enterprise Concept Framework coordinates or conformance semantics.
- Organization-wide entity identity and storage-layout rules.
- Assessment-model constructs owned by the relevant assessment repositories.

Where a proposed enrichment would require an upstream semantic decision, the analysis must identify that dependency rather than silently establish a local definition.

### 5.5 Evidence-based model changes

Every recommended schema addition or modification must be supported by a specific requirement that cannot be adequately satisfied by the existing model.

The recommendation must identify the use case, semantic meaning, validation implications, and migration consequences.

### 5.6 Backward compatibility must be explicit

The analysis must assess existing canonical records and consumers before recommending changes.

It must distinguish additive changes from changes that alter existing field meaning, validity, or interpretation.

## 6. Scope

### 6.1 In scope

The CR shall:

1. Inspect the current canonical capability record schema and representative records.
2. Review the applicable documentation, methodology, evidence, governance, taxonomy, and conformance artefacts.
3. Map the Business Capability Documentation Standard requirements to the current model.
4. Identify semantic and structural gaps.
5. Identify redundant or overlapping representations.
6. Assess whether each gap requires a schema change, a constraint change, improved guidance, a reference, or no change.
7. Assess conditional and mandatory field requirements.
8. Evaluate backward compatibility and migration implications.
9. Produce an ordered model-enrichment backlog with acceptance criteria.
10. Identify dependencies that must be resolved outside this repository.
11. Recommend whether each candidate should proceed as a separate implementation CR.

### 6.2 Out of scope

This CR does not authorize:

- Direct modification of the canonical schema.
- Direct modification of canonical capability records.
- A catalog-wide README rewrite.
- Addition, deletion, renaming, merging, or retirement of capabilities.
- Changes to the organization-wide entity identity system.
- Changes to the upstream DEA metamodel.
- Changes to WSF or OpenDEAM semantic foundations.
- Changes to ECF coordinates or the ECF conformance contract.
- Introduction of new relationship types without the required semantic authority.
- Changes to assessment models, scoring, or benchmark bands.
- New CI gates or workflows.
- Release, tag, or version-history changes.
- Regeneration or restructuring of unrelated catalog artefacts.

Any implementation discovered to be necessary must be proposed through the applicable subsequent CR, with explicit scope and acceptance criteria.

## 7. Analysis Requirements

### 7.1 Requirement-to-model traceability

The analysis must use the final accepted requirement identifiers from CR-DEA-BC-41, after reconciling them against existing repository identifiers.

For each requirement, record at least:

| Attribute | Required content |
|---|---|
| Requirement ID | Stable identifier from the governing standard |
| Requirement summary | Concise statement of the required information or behavior |
| Normative source | Standard section or other governing artefact |
| Current representation | Existing property, relationship, reference, README section, or governance mechanism |
| Coverage classification | Direct, indirect, conditional, absent, or not applicable |
| Gap description | Specific limitation, if any |
| Recommended disposition | Retain, clarify, constrain, reference, extend, or escalate upstream |
| Schema impact | None, documentation-only, additive, or potentially breaking |
| Migration impact | None, selective, or catalog-wide |
| Verification method | Test, validator, reference check, manual review, or upstream decision |

The mapping must account for all applicable requirements. Unresolved mappings must be explicitly marked rather than silently omitted.

### 7.2 Existing model inventory

Inspect the actual current schema and record format. Do not infer the model solely from README prose or from a single entity.

The analysis must explicitly evaluate the existing representations for:

- Identity and classification.
- Definition and semantic grounding.
- Capability layer and ECF coordinates.
- Business outcome.
- Business object.
- Related capabilities.
- Evidence and provenance.
- Boundary and non-examples.
- Specialization rules and specialization boundaries.
- ECF rationale and conformance metadata.
- Version, status, and lifecycle information.
- Any other properties currently defined by the canonical schema.

The above list is an inspection checklist, not a directive to add or rename fields.

### 7.3 Documentation aspects requiring coverage assessment

The analysis must assess how the current model and its associated artefacts support each of the following aspects.

1. Identity and classification.
2. Definition and semantics.
3. Purpose and value contribution.
4. Scope and boundaries.
5. Composition and specialization.
6. Enabling elements and realization relationships.
7. Outcomes, goals, value, and traceability.
8. Realization and operational context.
9. Assessment and performance.
10. Governance and accountability.
11. Provenance and evidence.
12. Lifecycle and conformance.

The assessment must distinguish between information that defines the capability itself and information that documents its governance, realization, evaluation, or usage.

### 7.4 Classification of model gaps

Every identified gap must be assigned one of the following dispositions.

**A. Existing model is sufficient**

The requirement is already expressed adequately. No schema change is justified.

**B. Definition or constraint gap**

The required property or relationship exists, but its meaning, allowed values, cardinality, conditionality, or validation rules require clarification.

**C. Documentation gap**

The model supports the requirement, but the documentation does not explain how it should be populated or interpreted.

**D. Reference or relationship gap**

The requirement should be satisfied by an existing authoritative artefact or relationship, but the reference or linkage needs clarification.

**E. Candidate schema gap**

The requirement cannot be represented adequately using the current model. A schema change may be justified, subject to semantic and compatibility review.

**F. Upstream dependency**

The requirement cannot be resolved locally without an upstream metamodel, semantic, identity, or conformance decision.

**G. Not applicable to the canonical record**

The information belongs in another authoritative artefact, or it does not apply universally to a canonical business capability.

A classification of E or F must include a written rationale. Neither classification independently authorizes implementation.

### 7.5 Mandatory versus conditional information

The analysis must determine whether each proposed property or constraint is:

- Universally mandatory.
- Conditionally mandatory under a stated rule.
- Recommended but optional.
- Prohibited as a duplicate or competing representation.

Conditionality must be expressed in testable terms wherever possible.

The analysis must not make a property universally mandatory simply because it is useful for some capabilities.

### 7.6 Relationship and reference integrity

The analysis must distinguish between:

- Properties that describe the capability directly.
- Relationships to other canonical entities.
- References to evidence or provenance.
- Links to external or upstream semantic authorities.
- Human-readable explanatory content.

A proposed relationship must not be treated as a new metamodel relationship merely because it would improve documentation.

Where the current model does not support a relationship required by the standard, the analysis must identify the semantic authority and decision needed to establish it.

### 7.7 Assessment and performance separation

The analysis must determine how capability documentation can refer to assessment, measurement, or performance information without improperly embedding an assessment model into the canonical capability definition.

It must preserve the distinction between:

- The capability being described.
- The outcomes or value it is intended to enable.
- Evidence that supports its definition or admission.
- An assessment of its maturity, effectiveness, or realization.
- Measured performance in a specific enterprise context.

Any proposed fields or references must respect the existing governance boundaries for assessment models.

### 7.8 Migration and compatibility

For every candidate schema change, assess:

- Whether existing records remain valid.
- Whether consumers depend on the current field structure.
- Whether the change alters field meaning or only adds expressiveness.
- Whether default values would misrepresent unknown information.
- Whether migration can be automated safely.
- Whether manual evidence or semantic review is required.
- Whether the schema version or release process would be affected.
- Whether a staged migration is preferable to a single catalog-wide change.

The analysis must not recommend fabricated values to satisfy a newly identified requirement.

## 8. Required Deliverable

Create:

`docs/BUSINESS-CAPABILITY-RECORD-MODEL-GAP-ANALYSIS.md`

The document must contain the following sections.

1. Purpose and decision context.
2. Scope and exclusions.
3. Governing requirements and source versions.
4. Inspected schema and artefact inventory.
5. Requirement-to-model traceability matrix.
6. Existing model coverage assessment.
7. Identified gaps and their classifications.
8. Redundancy and source-of-truth risks.
9. Mandatory and conditionality recommendations.
10. Relationship and reference integrity findings.
11. Assessment and performance boundary findings.
12. Backward-compatibility and migration assessment.
13. Ordered model-enrichment recommendations.
14. Proposed follow-on CR boundaries.
15. Unresolved upstream dependencies.
16. Verification and review record.

The document must identify the exact files and versions inspected. Findings must be reproducible from repository artefacts rather than relying on assumptions or memory.

## 9. Follow-on CR Recommendations

The deliverable must recommend which changes merit separate implementation CRs. Candidate categories include:

- Schema property or constraint changes.
- Relationship or reference representation changes.
- Canonical record population rules.
- README and documentation template alignment.
- Validator and conformance checks.
- Catalog-wide remediation.
- Generated discovery or relationship views.

These are candidate categories, not pre-approved CRs. The analysis must not assume that every category requires implementation.

Each recommended follow-on CR must have a bounded scope, an explicit dependency statement, and acceptance criteria that can be verified independently.

## 10. Acceptance Criteria

CR-DEA-BC-42 is complete only when all of the following conditions are satisfied.

### AC-01 — Governing requirements reconciled

The analysis uses the accepted Business Capability Documentation Standard and identifies its governing version.

### AC-02 — Actual model inspected

The current schema, representative canonical records, and relevant repository governance artefacts have been inspected directly.

### AC-03 — Complete traceability

Every applicable documentation requirement is mapped to an existing representation, a documented gap, an upstream dependency, or a justified non-applicability classification.

### AC-04 — Existing fields assessed

The analysis evaluates existing properties and mechanisms before recommending new ones.

### AC-05 — No automatic field proliferation

No new property is recommended solely to mirror a documentation heading or to duplicate an existing source of truth.

### AC-06 — Gap classifications justified

Every candidate schema gap and upstream dependency has a specific rationale and impact statement.

### AC-07 — Conditionality established

The analysis distinguishes universally mandatory information from conditional and optional information.

### AC-08 — Relationship authority respected

No new relationship semantics or upstream constructs are established implicitly.

### AC-09 — Assessment boundary preserved

Recommendations maintain the separation between capability definitions and separately governed assessment or performance information.

### AC-10 — Migration impacts documented

Each candidate schema change includes a compatibility and migration assessment.

### AC-11 — Follow-on work bounded

Recommended implementation work is partitioned into independently reviewable CRs with clear scope and acceptance criteria.

### AC-12 — Documentation discoverable

The deliverable is linked from the appropriate repository documentation index and relevant governing documentation without creating a competing normative standard.

### AC-13 — Repository integrity preserved

Applicable repository checks pass. Any failure unrelated to this CR is recorded and handled according to the existing repository governance process rather than concealed or bypassed.

### AC-14 — Scope respected

No schema, canonical record, capability inventory, identity rule, ECF rule, or CI behavior is changed under this CR.

## 11. Verification at Landing

Before landing, the implementer must verify:

- The deliverable exists at the prescribed path.
- All governing requirement identifiers resolve to the authoritative standard.
- Referenced schema and documentation paths exist.
- Every requirement has a recorded disposition.
- Candidate schema changes have documented rationale and impact.
- Proposed follow-on CRs do not overlap unnecessarily.
- The repository change-request register and documentation indexes are updated according to existing conventions.
- Applicable repository checks and integrity controls pass.

The final CR status must be recorded through the repository's established change process. The CR document must not be rewritten in place after landing contrary to repository governance.

## 12. Risks and Controls

| Risk | Control |
|---|---|
| Schema expands to mirror every documentation aspect | Require field-by-field gap evidence and reuse analysis |
| Existing fields acquire conflicting meanings | Preserve definitions; propose semantic changes separately |
| Canonical records become redundant with README content | Maintain explicit source-of-truth responsibilities |
| Local schema changes conflict with upstream metamodel semantics | Record upstream dependencies and escalate where necessary |
| Assessment details become embedded in capability definitions | Preserve assessment ownership and reference boundaries |
| Migration invents unsupported facts | Require evidence-based population and permit unknown or inapplicable states where governed |
| Gap analysis becomes an implementation bundle | Keep schema, data migration, documentation, and CI changes separately authorized |
| Repository status or index becomes inconsistent | Apply existing register, index, and integrity controls |

## 13. Definition of Done

This CR is done when:

1. The model gap analysis is complete and reviewable.
2. The traceability matrix covers every applicable requirement.
3. Existing model capabilities and deficiencies are distinguished clearly.
4. Every recommended schema change has a documented justification.
5. Migration and compatibility impacts are recorded.
6. Upstream dependencies and unresolved decisions are explicit.
7. Follow-on implementation CRs are proposed with bounded scopes.
8. Repository indexes and governance records are updated.
9. Required checks pass or permitted exceptions are documented.
10. No unauthorized schema or canonical record changes have been introduced.

## 14. Acceptance Decision

**Requested decision:** Approve the canonical record model gap analysis.

Approval authorizes inspection, documentation, traceability, and recommendations only. It does not authorize schema modification, record migration, new relationship semantics, catalog-wide remediation, or changes to upstream foundations.

Those changes require separate authorization through the repository's CR process.