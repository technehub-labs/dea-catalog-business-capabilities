# CR-DEA-BC-44: Canonical Capability README and Documentation Template

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-44 |
| Title | Canonical Capability README and Documentation Template |
| Status | Accepted (user directive 2026-10-28: "the next three CRs are attached. Take them for implementation") |
| Series | CR-DEA-BC |
| Change layer | L2 — Entity documentation and authoring conventions |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Normative foundation | CR-DEA-BC-41 — Business Capability Documentation Standard |
| Analysis dependency | CR-DEA-BC-42 — Canonical Record Model Gap Analysis |
| Model dependency | CR-DEA-BC-43 — Canonical Record Model Enrichment, subject to its accepted disposition |
| Reference entity | `entities/v1-alpha/asset-management-judtwr` |
| Primary deliverables | Canonical README template, documentation-authoring guidance, reference-entity conformance assessment |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "the next three CRs are attached. Take them for implementation")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Tranche step 4; implements the README interface layer identified by CR-DEA-BC-42 (BC-DOC-011 finding, backlog R-3), aligned to the accepted model outcome of CR-DEA-BC-43 (no additional populated properties assumed). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-44-readme-standard-template`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Landing decisions recorded here: (a) the template's section hierarchy implements the 14-section contract of CR-41 §5.1, folding this CR's §7.10/§7.11 into sections 7 and 14 respectively, per §7's reconciliation requirement; (b) the reference-entity assessment is delivered as a separate artefact `docs/BUSINESS-CAPABILITY-REFERENCE-ENTITY-ASSESSMENT-ASSET-MANAGEMENT.md` per §6.4; (c) remediation actions it classifies are executed by the catalog-wide remediation CR (R-5) — none are applied under this CR.

**Dependency condition:** The documentation template must align with the accepted outcome of CR-42 and, where applicable, the final model established through CR-43. If CR-43 is closed without model changes, this CR must use the accepted existing model rather than assume that additional properties exist.

## 2. Change Objective

Establish a normative, reusable structure for documenting canonical Business Capability entities so that every entity README communicates the capability's meaning, boundaries, relationships, evidence, and governance context consistently.

The README must function as the human-readable interface to the canonical record. It must make the entity understandable and reviewable without creating an independent semantic definition or duplicating the entire structured record.

This CR shall establish:

1. A standard README structure for canonical Business Capability entities.
2. Rules governing the relationship between the README and canonical structured record.
3. Guidance for documenting each applicable aspect of the Business Capability Documentation Standard.
4. Explicit requirements for completeness, clarity, and cross-artifact consistency.
5. A reference-entity assessment using `asset-management-judtwr`.
6. A controlled basis for subsequent catalog-wide adoption.

## 3. Problem Statement

Canonical capability records need to serve both machine processing and human interpretation.

The structured record provides governed identity, properties, relationships, evidence, provenance, and conformance information. The README provides the explanatory context needed by reviewers, catalog users, model maintainers, and future contributors.

Without a common documentation structure, entity READMEs can vary in completeness, terminology, section ordering, explanation depth, and treatment of boundaries. A README may omit important information, repeat record fields inconsistently, or present an assertion without explaining its evidential basis.

A template alone is insufficient if it merely lists headings. The repository needs a documentation contract that defines the purpose of each section, its relationship to the canonical record, when it is required, and how conformance is evaluated.

## 4. Normative Principles

### 4.1 Canonical record remains authoritative

The structured record is authoritative for its governed fields and relationships.

The README must not redefine the entity's canonical ID, name, definition, classification, or other structured values. Where these values are rendered in the README, they must agree with the record.

### 4.2 Explanation, not duplication

The README should explain the significance of canonical information rather than reproduce every property without interpretation.

For example, a capability's boundary section should explain what the capability includes and excludes, not merely repeat field names from the record.

### 4.3 Capability semantics before implementation

The documentation must describe the enduring ability represented by the capability, not reduce it to a process, project, organizational unit, software application, role, or resource.

Implementation examples may clarify realization, but must not redefine the capability as one specific implementation.

### 4.4 Evidence-backed claims

Claims concerning enterprise generality, semantic classification, boundaries, specialization, and admission must remain consistent with the repository's evidence and methodology requirements.

The README must not imply stronger evidence or broader applicability than the canonical record and its supporting artefacts establish.

### 4.5 Conditional completeness

Not every documentation aspect requires an independent section for every entity.

The template must distinguish universally required information from conditional information, recommended explanatory material, and information governed by another authoritative artefact.

An absent section must not automatically be interpreted as proof that a capability lacks the corresponding property.

### 4.6 No competing governance system

The README standard must reuse the repository's existing methodology, identity conventions, CR process, evidence rules, ECF conformance requirements, and versioning policy.

It must not introduce a parallel entity governance model.

## 5. Scope

### 5.1 In scope

This CR authorizes:

1. Definition of the canonical capability README structure.
2. Section-level content requirements and authoring guidance.
3. Rules for rendering canonical record values in the README.
4. Requirements for documenting semantic boundaries and non-examples.
5. Guidance for explaining outcomes, relationships, specialization, evidence, and provenance.
6. Requirements for handling conditional and inapplicable documentation.
7. Cross-artifact consistency requirements.
8. Assessment of the `asset-management-judtwr` README against the template.
9. Identification of concrete changes needed to bring the reference README into conformance.
10. Documentation of conformance and review expectations.
11. Updates to relevant repository indexes and authoring guidance.

### 5.2 Out of scope

This CR does not authorize:

- Changes to the canonical capability schema.
- Changes to canonical entity IDs or the organization-wide identity system.
- Changes to capability definitions or classifications solely to improve presentation.
- Changes to ECF coordinates or conformance rules.
- New relationship types or metamodel constructs.
- Changes to admission evidence or methodology.
- Automatic rewriting of every entity README.
- Catalog-wide record migration.
- New CI gates or workflows unless separately authorized.
- Changes to the capability inventory.
- Changes to upstream WSF, OpenDEAM, or DEA metamodel semantics.

Any substantive correction to a canonical capability record discovered during the documentation assessment must be recorded separately and handled through the applicable repository change process.

## 6. Required Deliverables

The CR must establish the following artefacts, using repository conventions and existing documentation locations where possible.

### 6.1 Canonical README template

Proposed path:

`docs/templates/BUSINESS-CAPABILITY-README-TEMPLATE.md`

The final path must be reconciled with the repository's current documentation organization before implementation.

The template must provide:

- A stable section hierarchy.
- Guidance for each section.
- Indications of mandatory and conditional content.
- Clear placeholders for record-derived values.
- Instructions for linking authoritative evidence and related entities.
- Instructions for handling inapplicable information.
- A conformance checklist for authors and reviewers.

The template must not include fabricated capability-specific facts or encourage contributors to copy placeholder text into canonical entity documentation.

### 6.2 README authoring standard

Proposed path:

`docs/BUSINESS-CAPABILITY-README-STANDARD.md`

The standard must define the purpose of each section, expected content, information sources, conditionality, and conformance criteria.

If an existing document already governs the relevant requirements, the CR must extend or reference it instead of creating a competing normative document.

### 6.3 Reference-entity assessment

The CR must assess:

`entities/v1-alpha/asset-management-judtwr/README.md`

The assessment must identify:

- Sections already satisfying the proposed standard.
- Required information that is missing or insufficiently explained.
- Content that duplicates or conflicts with the canonical record.
- Ambiguous or unsupported claims.
- References that are absent, invalid, or insufficiently informative.
- Recommended corrections, classified by whether they are editorial, documentation-structural, or require a separate semantic change.

The assessment must be evidence-based. The CR must not assume deficiencies without inspecting the current README and corresponding canonical record.

### 6.4 Conformance assessment record

The reference assessment must be retained in a reviewable form, either as part of the authoring standard or as a separate assessment artefact if repository conventions support it.

It must map each applicable requirement to the relevant README section and identify any outstanding issue.

## 7. Canonical README Structure

The following structure is the proposed baseline. During implementation, section names and ordering must be reconciled with existing repository conventions and the accepted standard under CR-41.

### 7.1 Entity identity

Purpose: establish which canonical entity the README documents.

Required content:

- Canonical name.
- Canonical entity identifier.
- Entity type or classification where defined by the current model.
- Relevant lifecycle or status information where governed by the record.
- Link or reference to the authoritative canonical structured record.

Identity values must agree with the structured record and must not be independently assigned in the README.

### 7.2 Definition

Purpose: state the canonical meaning of the capability.

Required content:

- The authoritative capability definition.
- A concise explanation of the enduring ability represented.
- Clarification of the intended meaning where the definition could reasonably be misinterpreted.

The canonical definition must not be paraphrased in a way that changes its meaning. Explanatory text must be distinguishable from the authoritative definition.

### 7.3 Purpose and business significance

Purpose: explain why the capability matters in enterprise terms.

Where supported by the canonical record and its evidence, this section should explain:

- The business outcome or outcomes the capability enables.
- The business object or domain context it concerns.
- The form of value it is intended to enable, preserve, control, or realize.
- The relevant stakeholders or beneficiaries, where established.

The section must not assert enterprise-specific benefits as universal properties of the capability without supporting evidence.

### 7.4 Scope and boundaries

Purpose: establish what the capability represents and distinguish it from adjacent concepts.

Required content must explain the applicable boundary information already established by the canonical record.

Where relevant, this includes:

- What the capability covers.
- What it does not cover.
- Non-examples that could be mistaken for the capability.
- Distinctions from closely related capabilities.
- Conditions under which an apparent overlap is legitimate.

The README must not introduce a boundary that conflicts with the canonical record.

### 7.5 Composition and specialization

Purpose: explain the capability's relationship to other capabilities and its permitted specialization.

Where supported by the model, this section should describe:

- Relevant parent, child, or related capabilities.
- The semantic nature of those relationships.
- Any established specialization boundary.
- How a specialized capability differs in meaning or scope.

A relationship must not be inferred from naming similarity alone. Any relationship absent from the canonical record or authoritative source must be treated as unresolved rather than presented as canonical fact.

### 7.6 ECF classification and rationale

Purpose: explain the entity's governed ECF alignment.

Where the canonical record contains ECF classification information, the README should explain:

- The assigned coordinate or coordinates as governed by the current model.
- The rationale for the assignment.
- The relationship between the capability's intent and the classification.
- Any relevant conformance reference.

The README must not redefine the ECF or substitute a locally invented classification scheme.

### 7.7 Enabling and realization context

Purpose: explain how the capability may be realized without equating it with a particular implementation.

Where relevant and supported, document:

- Enabling elements or related constructs already represented in the model.
- Relevant relationships to processes, roles, information, resources, systems, or other concepts where those relationships are authorized.
- Contextual examples that clarify how the capability may be realized.
- The distinction between the enduring capability and the mechanisms used to realize it.

This section must not invent new metamodel relationships or make a specific implementation universally mandatory.

### 7.8 Evidence and provenance

Purpose: make the basis for the capability's canonical admission and interpretation transparent.

Where required by existing methodology and record conventions, the README must link to or summarize the relevant evidence and provenance.

It must distinguish:

- Evidence supporting the capability's existence or enterprise generality.
- Rationale supporting its semantic classification.
- Provenance describing the origin of the record.
- Explanatory examples that are illustrative rather than evidential.

The README must not present an unsupported assertion as verified evidence.

### 7.9 Conformance and governance references

Purpose: identify the governing contracts and review context relevant to the entity.

Where applicable, document references to:

- Canonical record validation.
- ECF conformance information.
- Relevant admission or change records.
- Authoritative methodology or governance documents.
- Lifecycle information already established by repository conventions.

This section must link to the authoritative governance artefacts rather than restate them as a parallel local policy.

### 7.10 Related entities and references

Purpose: support navigation and semantic discovery.

List relevant canonical entities and authoritative references where they are established by the record or governed supporting artefacts.

Each link must resolve to the intended entity or source. The README must not imply that a navigational link is itself a formally defined semantic relationship.

### 7.11 Documentation completeness and exceptions

Purpose: make unresolved or inapplicable documentation requirements transparent.

Where the template requires a section that does not apply, the README must follow the approved standard for indicating non-applicability.

Where information is unknown or unresolved, it must not be silently replaced by a fabricated value or a generic assertion.

The standard must define when an explicit exception, an omitted section, or a reference to another artefact is appropriate.

## 8. README and Canonical Record Responsibilities

The standard must explicitly define the relationship between the structured record and its README.

| Information | Primary authority | README responsibility |
|---|---|---|
| Canonical identity | Canonical record and organization-wide identity rules | Display identity consistently |
| Canonical definition | Canonical record under the governing metamodel | Present the definition faithfully and explain it where necessary |
| Classification and ECF rationale | Canonical record and ECF conformance contract | Explain the established assignment |
| Boundaries and non-examples | Canonical record and applicable methodology | Make distinctions understandable |
| Related capabilities | Canonical relationships and authorized references | Explain and link established relationships |
| Admission evidence | Existing evidence and provenance mechanisms | Link to or summarize the supporting basis |
| Lifecycle and governance | Repository governance artefacts | Reference the authoritative decisions |
| Implementation examples | Evidence-backed explanatory documentation | Clarify meaning without redefining the capability |
| Assessment results | Authoritative assessment sources | Reference where appropriate; do not duplicate or redefine them |

Where a field is represented in the structured record and repeated in the README, the README must not become a competing source of truth.

If a mismatch is found, the author must determine which artefact is authoritative under existing governance and resolve the inconsistency through the appropriate process.

## 9. Documentation Requirement Classes

The README standard must use the following requirement classes.

### 9.1 Universally mandatory

Content required for every canonical capability README.

Examples include identification of the documented entity, its authoritative definition, and a reference to its canonical structured record, subject to reconciliation with existing repository requirements.

### 9.2 Conditionally mandatory

Content required when the corresponding information exists, applies to the entity, or is required by another governing contract.

The condition must be stated explicitly. For example, a README must explain a specialization relationship when one is established and relevant, but must not invent a specialization solely to populate the section.

### 9.3 Recommended

Content that improves understanding but is not required for every entity.

Examples may include illustrative realization scenarios or additional explanatory context, provided they are clearly distinguished from canonical facts.

### 9.4 Prohibited

Content that creates ambiguity, conflicts with the record, or violates repository governance.

Examples include:

- A competing entity identifier.
- A redefinition of the canonical capability.
- Unsupported relationships.
- Fabricated evidence or provenance.
- Enterprise-specific implementation assumptions presented as universal properties.
- Duplicated governance rules that conflict with the authoritative process.
- New semantic claims introduced only to make a README appear complete.

## 10. Reference-Entity Assessment: Asset Management

The implementation must inspect the current files for `asset-management-judtwr`, including its README, canonical structured record, and relevant evidence or governance references.

The assessment must not assume that a section's absence is automatically a defect. It must determine whether the requirement is already satisfied elsewhere, is conditional, or is genuinely missing.

For every finding, record:

| Attribute | Required content |
|---|---|
| Finding ID | Stable identifier within the assessment |
| Requirement | Applicable standard requirement |
| Current state | What the README and canonical record actually contain |
| Evidence | Exact section, field, or reference supporting the finding |
| Assessment | Conformant, partially conformant, nonconformant, or not applicable |
| Required action | Editorial correction, structural change, cross-artifact correction, or separate CR |
| Acceptance condition | Observable condition for resolution |

The assessment must pay particular attention to:

- Consistency between the README and canonical definition.
- Clarity of capability boundaries and non-examples.
- Explanation of the existing ECF coordinate and rationale.
- Evidence and provenance traceability.
- Relationship and specialization claims.
- Distinction between capability semantics and implementation examples.
- Validity of links to authoritative repository artefacts.

Any proposed change to the canonical capability's meaning, classification, or relationships must be separated from editorial and template work.

## 11. Conformance and Review

The README standard must define a repeatable review procedure.

At minimum, the reviewer must verify:

1. The README documents the intended canonical entity.
2. Canonical values agree with the structured record.
3. Mandatory sections are present and meaningful.
4. Conditional requirements are handled according to the stated rules.
5. Boundaries and non-examples do not conflict with the record.
6. Relationships and references are supported by authoritative sources.
7. Evidence and provenance are traceable.
8. ECF references remain consistent with the applicable contract.
9. Explanatory text does not redefine capability semantics.
10. Links to governing artefacts resolve correctly.
11. Exceptions and unresolved information are represented honestly.
12. No prohibited duplication or unsupported assertion has been introduced.

The review procedure must be designed so that future automation can check structural and link-related conditions where feasible, without pretending that all semantic judgments can be automated.

This CR does not itself authorize new CI gates. Any additional automated enforcement must follow the repository's established change process.

## 12. Acceptance Criteria

CR-DEA-BC-44 is complete only when all applicable criteria are satisfied.

### AC-01 — Normative alignment

The README standard aligns with the accepted Business Capability Documentation Standard and the final model decisions resulting from CR-42 and CR-43.

### AC-02 — Template established

A reusable canonical README template exists at the approved repository path and includes authoring guidance.

### AC-03 — Section purposes defined

Each prescribed section has a defined purpose, content expectation, information source, and requirement class.

### AC-04 — Source-of-truth responsibilities explicit

The standard distinguishes the canonical record from explanatory documentation and other authoritative artefacts.

### AC-05 — Conditionality explicit

Mandatory, conditionally mandatory, recommended, and prohibited content are distinguishable.

### AC-06 — Capability semantics preserved

The standard distinguishes capability from activity, process, implementation, organizational structure, system, and resource.

### AC-07 — Boundary and relationship guidance complete

The template explains how to document boundaries, non-examples, specialization, and related capabilities without inventing semantics.

### AC-08 — Evidence and provenance traceable

The template establishes how evidence and provenance are referenced without duplicating or replacing existing governance mechanisms.

### AC-09 — Reference entity assessed

`asset-management-judtwr` has been assessed against the standard, with findings supported by the actual repository artefacts.

### AC-10 — Remediation bounded

Any required changes to the reference README are classified and authorized. Substantive semantic changes are not hidden inside documentation edits.

### AC-11 — Cross-artifact consistency addressed

The standard defines how to detect and resolve conflicts between the README and canonical structured record.

### AC-12 — No unapproved enforcement changes

No new CI gates, validators, or schema changes are introduced under this CR unless explicitly included in its approved scope.

### AC-13 — Repository discoverability preserved

The new standard and template are linked from the appropriate documentation indexes and relevant authoring guidance.

### AC-14 — Governance integrity maintained

The CR register, change history, and repository integrity controls are updated in accordance with existing conventions.

### AC-15 — Scope respected

No unrelated entity changes, capability inventory changes, or upstream semantic changes are introduced.

## 13. Risks and Controls

| Risk | Control |
|---|---|
| README becomes a second source of truth | Define authority and cross-artifact consistency rules |
| Template becomes a checklist of empty headings | Require meaningful content and section-level guidance |
| Authors invent information to complete sections | Define conditionality and explicit handling of unknown or inapplicable information |
| Documentation changes alter capability semantics | Separate editorial changes from canonical semantic changes |
| Template conflicts with the final schema | Require reconciliation with accepted CR-42 and CR-43 outcomes |
| Asset Management is treated as a universal implementation pattern | Use it as a conformance reference, not as the source of general capability semantics |
| Semantic review is over-automated | Separate structural checks from human semantic judgment |
| Catalog-wide remediation becomes implicit | Restrict this CR to the standard, template, and reference assessment |

## 14. Definition of Done

This CR is done when:

1. The README standard and reusable template are complete.
2. Each section has clear purpose and conformance requirements.
3. The source-of-truth responsibilities are explicit.
4. The `asset-management-judtwr` assessment is complete.
5. Findings and required reference-entity changes are documented.
6. Substantive semantic changes are separated from documentation work.
7. The template aligns with the accepted canonical record model.
8. Repository documentation indexes and registers are updated.
9. Required checks pass or permitted exceptions are documented.
10. No unauthorized schema, inventory, or upstream changes have been introduced.

## 15. Acceptance Decision

**Requested decision:** Approve CR-DEA-BC-44 to establish the canonical Business Capability README standard, reusable template, and reference-entity conformance assessment.

Approval does not authorize a catalog-wide README rewrite, schema modification, new CI enforcement, or unapproved semantic changes.

The scope is limited to the documentation contract, the reusable template, the assessment of `asset-management-judtwr`, and the specifically authorized documentation corrections required to complete this CR.