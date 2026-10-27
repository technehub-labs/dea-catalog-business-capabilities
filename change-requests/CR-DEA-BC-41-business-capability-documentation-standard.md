# CR-DEA-BC-41: Business Capability Documentation Standard

**Status**: Accepted (user directive 2026-10-27: "I want to enhance the Business Capability. Refer to the attached to get the grounding ... along with the first CR in the tranche to establish the enrichment documentation foundation to implement them.")
**Series**: `CR-DEA-BC`
**Layer**: L1 — Normative documentation and semantic specification
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Enrichment-programme grounding assessment (workspace `CR-DEA-BC-DOC-000.md`, 2026-10-27): the catalog's admission metadata is strong, but entity documentation is not yet a normative contract — a capability's record supports its admission, while its README should let a reader understand, apply, and govern the capability without reconstructing it from repository documents. This CR is the first of the enrichment tranche and establishes that documentation foundation. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-41-documentation-standard`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)
**Predecessors**: CR-DEA-BC-01, CR-DEA-BC-01A, CR-DEA-BC-03, CR-DEA-BC-29, CR-DEA-BC-35A, CR-DEA-BC-40
**Related foundations**: OpenDEAM v0.2.1; `dea-metamodel` 1.0.0; ECF conformance profile `dea:ecf@1.0.0`; the organization-wide entity identity and storage-layout standards.

> **Format note (landing, 2026-10-27):** this CR was authored outside the repository (grounding tranche) and is landed with its normative content verbatim; only the metadata block was adapted to the repository's house CR format.

## 1. Primary Objective

Establish a normative Business Capability Documentation Standard for the canonical first-order business capabilities maintained by `dea-catalog-business-capabilities`.

The standard MUST define the semantic, descriptive, structural, traceability, and governance information required to document a business capability as a canonical OpenDEA entity.

It MUST establish a consistent documentation contract that supports human interpretation, semantic interoperability, enterprise architecture, downstream assessment models, machine-readable catalog consumption, and future automated conformance enforcement.

The standard MUST build upon the existing First-Order Business Capability Catalog Method, canonical entity model, evidence and provenance methodology, taxonomy, identity system, and conformance controls.

It MUST NOT replace these foundations or establish a competing entity governance model.

**This CR establishes the normative documentation foundation only.** Schema changes, individual entity README remediation, relationship-model extensions, and new automated conformance gates are separate implementation concerns to be addressed by subsequent CRs.

## 2. Background and Problem Statement

The repository already establishes a canonical method for identifying, investigating, normalizing, reviewing, and admitting first-order business capabilities.

The current method establishes, among other things:

- Capability as an enduring enterprise ability rather than an activity.
- Enterprise generality as a condition of first-order capability admission.
- Evidence before canonical admission.
- Implementation independence.
- A distinction between capabilities, processes, functions, services, outcomes, systems, and organizational structures.
- ECF as a classification framework rather than a generator of capability identities.
- Explicit specialization boundaries.
- Canonical identifiers, provenance, and controlled lifecycle management.

These principles remain authoritative.

However, the completeness of the documentation presented for an individual capability is not equivalent to the completeness of its canonical admission record.

The current entity model already captures important information, including definitions, outcomes, business-object focus, classification coordinates, related capabilities, evidence, provenance, boundary statements, non-examples, specialization boundaries, and ECF rationale.

The problem is therefore not an absence of all relevant information. It is the absence of a single, comprehensive normative contract establishing:

1. Which documentation aspects MUST exist for every approved capability.
2. Which information is mandatory, conditional, recommended, or optional.
3. What each documentation aspect is intended to establish.
4. How semantic distinctions MUST be expressed.
5. How documentation relates to the canonical record and other authoritative artifacts.
6. How documentation completeness is determined without requiring unnecessary prose.
7. How documentation requirements can subsequently be translated into schemas, templates, and conformance gates.

Without this contract, individual READMEs can vary in completeness, contributors can interpret the same documentation requirement differently, and future automation risks enforcing a structure that has not been formally agreed.

This CR resolves that foundational issue before implementing the dependent changes.

## 3. Normative Architectural Principles

### 3.1 Capability before classification

The business capability is a canonical semantic entity in its own right.

Its identity, definition, and existence MUST NOT be generated from ECF coordinates.

ECF classification remains an overlay governed by the applicable ECF conformance contract.

### 3.2 Ability, not activity

A business capability MUST express an enduring enterprise ability.

Its definition MUST NOT equate the capability with a particular process, activity, workflow, organizational unit, application, system, or implementation arrangement.

### 3.3 Evidence before canon

The documentation standard MUST preserve the existing evidence-led admission process.

Documentation completeness MUST NOT be treated as a substitute for evidence of enterprise generality, semantic distinctness, or any other existing admission criterion.

A well-documented candidate does not become canonical merely because its documentation satisfies this standard.

### 3.4 Stable identity

A capability MUST retain its canonical identity independently of changes to its explanatory documentation, organizational assignment, implementation, assessment result, or ECF classification.

Identity changes MUST follow the applicable entity identity and migration rules.

### 3.5 Canonical data before presentation

The canonical structured entity record remains authoritative for the facts it owns.

An entity README MUST NOT establish conflicting identity, definition, classification, relationship, or lifecycle information.

Where the README reproduces canonical data, it SHOULD derive that information from the canonical record or be validated against it.

### 3.6 Semantic independence

The capability, its realization, its enabling elements, its intended outcomes, and its assessment results MUST remain conceptually distinct.

A capability may be realized through different operating models, processes, resources, systems, and organizational arrangements without necessarily becoming a different capability.

### 3.7 Governance without duplication

The documentation standard MUST consume existing normative rules wherever those rules are already established.

It MUST NOT redefine canonical entity identity, foundational ontological concepts, ECF semantics, or organization-wide governance requirements owned by upstream specifications.

## 4. Normative Scope

The standard MUST establish the documentation requirements for the following twelve aspects.

### 4.1 Identity and classification

Documentation MUST establish:

- Canonical identifier.
- Canonical name.
- Entity type.
- Approved definition.
- Lifecycle status.
- Applicable version information.
- Classification and ECF coordinates, as required by the existing model.
- Applicable identity and classification rules.

The standard MUST distinguish entity identity from catalog release versions, schema versions, and upstream model versions.

It MUST reference the existing organization-wide identity system rather than introduce a capability-specific identifier convention.

### 4.2 Definition and semantics

Documentation MUST establish:

- The canonical definition.
- The intended semantic interpretation.
- The distinctive characteristics of the capability.
- The meaning of material terms used in its definition.
- The distinction between the capability and related entity types.
- The criteria necessary to distinguish it from adjacent capabilities.

Definitions MUST be consistent with the existing OpenDEA semantic foundation and capability admission methodology.

The standard MUST prohibit circular definitions and definitions that merely describe an implementation, organizational unit, process, or desired result.

### 4.3 Purpose and value contribution

Documentation MUST distinguish the capability's purpose from its definition and intended outcome.

It MUST establish the rationale for the capability's existence and, where applicable, its contribution to enterprise value.

Where the capability's value contribution is described, the documentation SHOULD identify relevant beneficiaries, value contexts, and intended effects.

The standard MUST NOT require unsupported claims that a capability independently guarantees a business outcome.

### 4.4 Scope and semantic boundaries

Documentation MUST establish sufficient scope information to distinguish the capability from related concepts.

It MUST provide for:

- Included concerns.
- Excluded concerns.
- Boundary conditions.
- Distinguishing criteria.
- Relevant non-examples.
- Adjacent capability relationships.
- Material assumptions and applicability constraints.

The amount of detail MAY vary with the complexity of the capability, but the requirement to establish a defensible semantic boundary is mandatory.

Existing boundary statements and non-examples MUST be preserved and reused where they satisfy the requirements.

### 4.5 Capability composition and specialization

Documentation MUST establish the applicable composition and specialization semantics.

Where parent-child relationships exist, the documentation MUST identify the relevant entities and relationship meanings.

It MUST distinguish:

- First-order canonical capabilities.
- Valid domain or industry specializations.
- Enterprise-specific refinements.
- Related capabilities that are not subordinate specializations.

The standard MUST preserve the existing rule that specialization does not silently redefine or replace the first-order parent.

It MUST NOT impose universal completeness or mutual-exclusivity requirements on capability decompositions unless those requirements are justified by an applicable normative model.

### 4.6 Enabling elements and realization relationships

Documentation MUST provide for the description of relevant relationships between capabilities and the entities that enable or realize them.

These MAY include processes, activities, roles, organizational units, resources, information, data, systems, services, policies, and requirements, subject to the canonical metamodel.

Where applicable relationships are documented, their semantics MUST be distinguishable.

The standard MUST NOT equate a capability with its enablers or require every capability to have every possible relationship category.

It MUST consume canonical relationship types where available and MUST NOT introduce competing definitions for upstream entity types.

### 4.7 Outcomes, goals, value, and traceability

Documentation MUST preserve the distinction between a capability and the outcomes to which it contributes.

Where alignment or contribution is claimed, the documentation MUST provide for traceable references to the relevant goals, outcomes, requirements, or other canonical entities.

The standard MUST distinguish intended contribution from demonstrated contribution and causal attribution.

A claimed relationship MUST NOT be interpreted as proof that the capability alone guarantees the associated result.

### 4.8 Realization and operational context

Documentation MUST support an implementation-independent description of the contexts in which the capability can be realized.

Where relevant, it SHOULD describe realization considerations, operating constraints, dependencies, and supported realization patterns.

It MUST NOT make a particular system, process, organizational structure, or delivery model part of the capability's universal definition unless that characteristic is explicitly justified by the canonical semantics.

### 4.9 Assessment and performance

Documentation MUST establish the distinction between:

1. The capability being assessed.
2. The assessment model and criteria.
3. The resulting assessment findings.
4. The evidence supporting those findings.

The standard MUST NOT incorporate maturity scores, performance observations, or assessment results into canonical capability identity.

It MUST provide for references to applicable assessment models and instruments without absorbing their independently governed scoring logic into the capability definition.

Assessment interfaces MUST respect the ownership and semantics of the relevant assessment repository and metamodel.

### 4.10 Governance and accountability

Documentation MUST identify or reference the governance information required by the applicable entity lifecycle.

This includes approval status, applicable authority, ownership responsibilities, and relevant change-control information.

The standard MUST distinguish the authority to approve a canonical semantic definition from the responsibility for implementing, operating, or assessing the capability.

It MUST reuse authoritative governance records where those records already exist rather than require unnecessary duplication.

### 4.11 Provenance and evidence

Documentation MUST preserve traceability to the capability's origin, admission, and approval history under the existing methodology.

Where applicable, it MUST support references to:

- Evidence sources.
- Evidence disposition.
- Admission rationale.
- Semantic decisions.
- Classification rationale.
- Relationship justification.
- Relevant review findings.
- Change history.

The standard MUST preserve the existing evidence ladder and admission controls.

It MUST distinguish authoritative sources, external reference material, proposed interpretations, and claims requiring further validation.

### 4.12 Lifecycle and conformance

Documentation MUST support the applicable entity lifecycle, versioning, review, and change-control rules.

The standard MUST distinguish entity identity, entity content version, schema version, catalog release, and upstream model version.

It MUST provide for the identification of deprecation, retirement, replacement, and migration information where applicable.

The standard MUST define documentation conformance as a distinct concern that complements, rather than replaces, structural schema validation, semantic review, and governance controls.

## 5. Documentation Requirement Classification

The standard MUST classify requirements according to their applicability.

### 5.1 Universally mandatory

These requirements apply to every approved canonical business capability.

They include:

- Canonical identity.
- Canonical definition.
- Entity classification and lifecycle status.
- Sufficient semantic interpretation.
- Defensible scope and boundaries.
- Applicable provenance and approval records.
- Conformance with the existing identity and governance standards.

### 5.2 Conditionally mandatory

These requirements apply when a relevant condition exists or a relationship is asserted.

Examples include:

- Parent and child relationships.
- Specialization references.
- Realization relationships.
- Goal and outcome traceability.
- Assessment model references.
- Replacement or migration references.
- Additional scope constraints.

The standard MUST define how conditional applicability is established and recorded.

A conditionally mandatory requirement MUST NOT be treated as satisfied merely because its corresponding field is absent.

### 5.3 Recommended

Recommended documentation improves interpretation and reuse but is not required for every capability.

Examples may include:

- Illustrative scenarios.
- Additional explanatory diagrams.
- Alternative realization patterns.
- Extended domain-specific commentary.
- Additional examples of valid and invalid interpretations.

The standard SHOULD explain when these additions are useful.

### 5.4 Prohibited

The standard MUST identify prohibited documentation practices, including:

- Conflicting canonical definitions across artifacts.
- Unapproved changes to entity identity conventions.
- Treating ECF coordinates as capability identity.
- Treating processes, systems, organizational units, or outcomes as equivalent to capabilities.
- Embedding assessment results into canonical capability identity.
- Presenting unverified relationships as established facts.
- Introducing industry-specific specialization into the first-order definition without satisfying the existing admission rules.

## 6. Normative Documentation Contract

The standard MUST establish a canonical documentation contract for individual capability entities.

The contract MUST define a consistent section structure covering:

1. Identity.
2. Definition and semantic interpretation.
3. Purpose and value contribution.
4. Scope and boundaries.
5. Classification.
6. Composition and specialization.
7. Related entities and relationships.
8. Realization and operational context.
9. Outcomes and traceability.
10. Assessment considerations.
11. Governance.
12. Provenance and evidence.
13. Lifecycle and change history.
14. Conformance.

The standard MUST define the required information for each section and distinguish information rendered from canonical data from information requiring explanatory narrative.

A section MUST NOT be omitted merely because its content is not currently available. The documentation contract MUST distinguish:

- Not applicable.
- Not yet established.
- Not yet documented.
- Established and documented.
- Explicitly unresolved.

These states MUST NOT be treated as interchangeable.

The standard MUST NOT impose a fixed minimum word count or require every capability to have identical narrative depth.

It MUST require sufficient information to establish the capability's meaning, boundaries, and applicable relationships.

## 7. Canonical Record and README Responsibilities

The standard MUST define the responsibilities of the canonical structured record and the entity README.

### 7.1 Canonical record

The structured record remains authoritative for canonical fields, including identity, definition, classification, lifecycle status, and existing governed metadata.

Any additional structured attributes required by this CR MUST first be evaluated against the existing schema and upstream metamodel.

This CR does not itself authorize new schema fields.

### 7.2 Entity README

The README MUST serve as the human-readable documentation interface for the capability.

It MUST explain the capability's meaning, purpose, boundaries, and relevant relationships in a manner consistent with the canonical record.

It SHOULD provide direct navigation to relevant canonical records, standards, evidence, and related entities where those references exist.

### 7.3 Other authoritative artifacts

Schemas, governance records, evidence registers, relationship records, and assessment models MUST retain their designated responsibilities.

The documentation standard MUST define the relationships among these artifacts without creating duplicate sources of truth.

## 8. Conformance Model

The standard MUST define five complementary documentation conformance dimensions.

| Dimension | Requirement |
|---|---|
| Structural completeness | Required documentation information is represented in the applicable artifacts |
| Semantic completeness | The capability's meaning, purpose, boundaries, and distinctions are sufficiently established |
| Referential integrity | Declared references resolve to valid canonical entities or explicitly governed external sources |
| Cross-artifact consistency | The README, canonical record, and applicable authoritative artifacts do not contradict one another |
| Governance traceability | Required approval, provenance, lifecycle, and change-control information is available |

These dimensions MUST remain distinguishable from existing schema, identity, entity-system, ECF, authorship, and catalog-integrity conformance gates.

This CR establishes the conformance contract. Implementation of new automated checks is deferred to a subsequent CR.

The standard MUST explicitly acknowledge that semantic correctness cannot be established through structural schema validation alone.

## 9. Normative Requirement Identifiers

The standard MUST assign stable identifiers to its normative requirements.

The following initial identifiers are proposed for the documentation standard. They are local requirement identifiers, not new Change Request identifiers.

| Requirement | Normative subject |
|---|---|
| BC-DOC-001 | Canonical identity and classification |
| BC-DOC-002 | Definition and semantic interpretation |
| BC-DOC-003 | Implementation independence |
| BC-DOC-004 | Scope and semantic boundaries |
| BC-DOC-005 | Composition and specialization |
| BC-DOC-006 | Enabling relationships and realization |
| BC-DOC-007 | Outcomes and traceability |
| BC-DOC-008 | Assessment separation |
| BC-DOC-009 | Provenance and governance |
| BC-DOC-010 | Lifecycle and conformance |
| BC-DOC-011 | README completeness |
| BC-DOC-012 | Cross-artifact consistency |

The final standard MUST reconcile these identifiers with existing requirements and conformance registers before adoption.

Where an existing normative requirement already establishes the same obligation, the standard MUST reference it rather than create a competing rule.

## 10. Relationship to Existing CRs and Normative Foundations

| Existing foundation | Relationship to this CR |
|---|---|
| CR-DEA-BC-01 | Preserves the First-Order Business Capability Catalog Method |
| CR-DEA-BC-01A | Preserves the reconciled capability record shape and upstream metamodel alignment |
| CR-DEA-BC-03 | Consumes the existing schema and CI foundation; does not replace it |
| CR-DEA-BC-29 | Preserves the established rich-narrative expectations and their applicable clarifications |
| CR-DEA-BC-35A | Preserves the confirmed organization-wide identity system |
| CR-DEA-BC-35 | Preserves the catalog's entity-system institutionalization and lifecycle controls |
| CR-DEA-BC-39 | Preserves change-request index, numbering, and documentation-integrity controls |
| CR-DEA-BC-40 | Preserves the current canonical entity schema and its reconciled record shape |

The final standard MUST be reviewed against these existing foundations before acceptance.

It MUST NOT silently reverse or supersede their established decisions.

## 11. Scope Exclusions

This CR MUST NOT:

1. Change the canonical definition of the Business Capability entity in the upstream metamodel.
2. Change the OpenDEAM layer or building-block allocation.
3. Redefine the World Semantic Foundation's foundational concepts.
4. Modify the ECF definition, coordinates, or conformance contract.
5. Change the organization-wide entity identifier system.
6. Introduce a competing canonical entity record format.
7. Add or rename canonical business capability entities.
8. Change existing capability definitions, classifications, or relationships.
9. Rewrite existing entity READMEs.
10. Add new canonical schema fields or change `schemas/entity.schema.json`.
11. Implement new relationship types or change upstream relationship semantics.
12. Introduce new assessment dimensions, maturity models, or scoring rules.
13. Implement new CI workflows or automated documentation gates.
14. Perform catalog-wide remediation.
15. Generate new capability maps, indexes, or visualizations.

These changes require separate CRs after the documentation foundation has been accepted.

## 12. Proposed Deliverable

The principal deliverable is:

`docs/BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md`

The document MUST contain:

- The normative purpose and scope.
- The twelve documentation aspects.
- Mandatory, conditionally mandatory, recommended, and prohibited requirements.
- The canonical documentation contract.
- Responsibilities of the canonical record and README.
- Cross-artifact consistency rules.
- The documentation conformance model.
- Normative requirement identifiers.
- References to existing authoritative foundations.

The document MUST be discoverable from the repository root README and the relevant documentation index.

The implementation MUST follow the repository's established CR landing procedure, including the required CR index entry, change-log treatment, and applicable documentation-integrity checks.

No unrelated repository changes are authorized by this CR.

## 13. Definition of Done

This CR is complete when all of the following conditions are satisfied.

1. The normative documentation standard exists at the designated path.
2. All twelve documentation aspects are explicitly defined.
3. Mandatory and conditional requirements are distinguishable.
4. The standard defines the required information for each aspect.
5. The standard defines the responsibilities of canonical data, README content, and other authoritative artifacts.
6. The standard establishes explicit rules for semantic boundaries, implementation independence, and related-entity distinctions.
7. The standard preserves the existing evidence-led admission and canonical identity systems.
8. The standard defines documentation conformance without conflating it with schema validation or semantic approval.
9. The proposed normative requirement identifiers have been reconciled with existing requirements.
10. The standard has been reviewed against CR-DEA-BC-01, CR-DEA-BC-01A, CR-DEA-BC-29, CR-DEA-BC-35A, CR-DEA-BC-39, and CR-DEA-BC-40.
11. The repository root README and applicable documentation index provide discoverability.
12. The CR register and CHANGELOG accurately reflect the change.
13. Applicable repository documentation-integrity and conformance checks pass.
14. No schema, canonical entity, identifier, or unrelated runtime changes are introduced.
15. The accepted CR is landed according to the repository's established change-control procedure.

## 14. Acceptance Decision

Acceptance of CR-DEA-BC-41 authorizes establishment of the Business Capability Documentation Standard as the normative foundation for subsequent documentation enrichment.

It does not authorize automatic changes to canonical capability records, schema structures, entity relationships, or CI behavior.

Subsequent CRs MUST implement the accepted standard rather than independently redefining its requirements.

The standard becomes the governing documentation contract for future canonical capability entity READMEs and for the controlled remediation of existing entities.

**Decision requested:** Accept CR-DEA-BC-41 as the foundation CR for the Business Capability Documentation and Conformance enrichment programme.