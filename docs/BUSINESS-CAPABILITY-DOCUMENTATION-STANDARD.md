# Business Capability Documentation Standard

**Status**: Normative (established by [CR-DEA-BC-41](../change-requests/CR-DEA-BC-41-business-capability-documentation-standard.md), 2026-10-27)
**Applies to**: every canonical first-order business capability entity in this catalog (`entities/v1-alpha/`)
**Governs**: the documentation contract for capability entities — the canonical structured record, the entity README, and their relationship to other authoritative artifacts
**Keywords**: MUST / MUST NOT / SHOULD / SHOULD NOT / MAY — RFC 2119 semantics

---

## 1. Purpose and scope

This standard defines the semantic, descriptive, structural, traceability, and governance information required to document a business capability as a canonical OpenDEA entity. It establishes a consistent documentation contract that supports human interpretation, semantic interoperability, enterprise architecture use, downstream assessment models, machine-readable catalog consumption, and future automated conformance enforcement.

The standard builds upon the First-Order Business Capability Catalog Method ([CR-DEA-BC-01](../change-requests/CR-DEA-BC-01.md)), the reconciled record shape ([CR-DEA-BC-01A](../change-requests/CR-DEA-BC-01A.md)), the schema and CI foundation ([CR-DEA-BC-03](../change-requests/CR-DEA-BC-03.md)), the rich-narrative expectations ([CR-DEA-BC-29](../change-requests/CR-DEA-BC-29.md)), the organization-wide identity system ([CR-DEA-BC-35A](../change-requests/CR-DEA-BC-35A-org-wide-id-system-confirmation.md)), the entity-system institutionalisation ([CR-DEA-BC-35](../change-requests/CR-DEA-BC-35-entity-system-business-capabilities.md)), the documentation-integrity controls ([CR-DEA-BC-39](../change-requests/CR-DEA-BC-39-index-numbering-doc-truth.md)), and the current canonical entity schema ([CR-DEA-BC-40](../change-requests/CR-DEA-BC-40-schema-reconciliation.md)). It does not replace any of them.

**This standard is the documentation foundation only.** Schema changes, entity README remediation, relationship-model extensions, and automated documentation gates are implemented by subsequent CRs of the enrichment tranche and MUST conform to this standard rather than redefine it.

### 1.1 Out of scope

This standard does not change: the upstream metamodel definition of Business Capability; the OpenDEAM layer or building-block allocation; the World Semantic Foundation's concepts; the ECF definition, coordinates, or conformance contract; the organization-wide identifier system; the canonical record format; any entity's identity, definition, classification, or relationships; or any CI workflow. See [CR-DEA-BC-41 §11](../change-requests/CR-DEA-BC-41-business-capability-documentation-standard.md) for the authoritative exclusion list.

## 2. Normative architectural principles

These principles are restatements of existing catalog law (METHODOLOGY.md, GOVERNANCE.md); the documentation standard consumes them and adds no competing rules.

1. **Capability before classification.** A capability's identity, definition, and existence MUST NOT be generated from ECF coordinates. ECF classification remains an overlay governed by the ECF conformance contract (`dea:ecf@1.0.0`).
2. **Ability, not activity.** A capability definition MUST express an enduring enterprise ability and MUST NOT equate the capability with a process, activity, workflow, organizational unit, application, system, or implementation arrangement.
3. **Evidence before canon.** Documentation completeness MUST NOT substitute for evidence of enterprise generality, semantic distinctness, or any other admission criterion. A well-documented candidate does not become canonical because its documentation satisfies this standard.
4. **Stable identity.** A capability retains its canonical identity independently of changes to its explanatory documentation, organizational assignment, implementation, assessment results, or ECF classification. Identity changes follow the applicable identity and migration rules ([CR-DEA-BC-35A]; `reconciliation/migration-id-map.yaml`).
5. **Canonical data before presentation.** The structured entity record is authoritative for the facts it owns. An entity README MUST NOT establish conflicting identity, definition, classification, relationship, or lifecycle information. Where a README reproduces canonical data, it SHOULD derive it from the record or be validated against it.
6. **Semantic independence.** The capability, its realization, its enabling elements, its intended outcomes, and its assessment results are conceptually distinct. Different realizations do not make a different capability.
7. **Governance without duplication.** This standard consumes existing normative rules and MUST NOT redefine canonical entity identity, foundational ontological concepts, ECF semantics, or organization-wide governance owned upstream.

## 3. The twelve documentation aspects

Every canonical capability's documentation MUST address the following aspects. "Address" means: provide the required information, or record an explicit content state (§5.2) where the information is not applicable or not yet established.

### 3.1 Identity and classification (BC-DOC-001)

Documentation MUST establish: the canonical identifier; the canonical name; the entity type; the approved definition; the lifecycle status; applicable version information; and the ECF coordinates required by the existing model. Entity identity MUST remain distinguishable from catalog release versions, schema versions, and upstream model versions. The organization-wide identity system is consumed, never redefined.

### 3.2 Definition and semantic interpretation (BC-DOC-002)

Documentation MUST establish: the canonical definition; the intended semantic interpretation; the capability's distinctive characteristics; the meaning of material terms used in the definition; the distinction between the capability and related entity types; and the criteria that distinguish it from adjacent capabilities. Definitions MUST NOT be circular and MUST NOT merely describe an implementation, organizational unit, process, or desired result.

### 3.3 Implementation independence (BC-DOC-003)

Documentation MUST preserve the capability's independence from any particular realization. Statements that couple the capability's meaning to a specific system, platform, vendor, organizational arrangement, or delivery model are prohibited unless explicitly justified by the canonical semantics (§6, prohibited practices).

### 3.4 Scope and semantic boundaries (BC-DOC-004)

Documentation MUST establish a defensible semantic boundary through: included concerns; excluded concerns; boundary conditions; distinguishing criteria; relevant non-examples; adjacent-capability relationships; and material assumptions or applicability constraints. Detail MAY vary with complexity; the obligation to establish the boundary is mandatory. Existing `boundary` and `non_examples` values MUST be preserved and reused where they satisfy these requirements.

### 3.5 Composition and specialization (BC-DOC-005)

Where parent–child or specialization relationships exist, documentation MUST identify the relevant entities and the relationship meanings, distinguishing: first-order canonical capabilities; valid domain or industry specializations; enterprise-specific refinements; and related capabilities that are not subordinate specializations. A specialization refines without silently redefining or replacing the first-order parent (existing `specialization_boundary` field). Universal-completeness or mutual-exclusivity requirements on decompositions MUST NOT be imposed unless justified by an applicable normative model.

### 3.6 Enabling relationships and realization (BC-DOC-006)

Documentation MUST provide for the description of relationships to enabling and realizing entities (processes, activities, roles, organizational units, resources, information, systems, services, policies, requirements — subject to the canonical metamodel). Where documented, relationship semantics MUST be distinguishable. The standard MUST NOT require every capability to carry every relationship category, and MUST NOT equate a capability with its enablers. Canonical relationship types are consumed; competing definitions for upstream entity types are prohibited. (The existing `realization` record block is the current structured carrier; a fuller relationship model is a subsequent tranche CR.)

### 3.7 Outcomes and traceability (BC-DOC-007)

Documentation MUST preserve the distinction between the capability and the outcomes to which it contributes. Where alignment or contribution is claimed, traceable references to the relevant goals, outcomes, requirements, or other canonical entities MUST be provided. Intended contribution MUST remain distinguishable from demonstrated contribution and causal attribution: a claimed relationship is not proof that the capability alone guarantees the result.

### 3.8 Assessment separation (BC-DOC-008)

Documentation MUST distinguish: (a) the capability being assessed; (b) the assessment model and criteria; (c) the resulting findings; and (d) the supporting evidence. Maturity scores, performance observations, and assessment results MUST NOT be incorporated into canonical capability identity. References to applicable assessment models and instruments MAY be provided without absorbing their independently governed scoring logic.

### 3.9 Realization and operational context

Documentation SHOULD support an implementation-independent account of the contexts in which the capability can be realized — realization considerations, operating constraints, dependencies, and supported patterns — without making any particular system, process, structure, or delivery model part of the capability's universal definition.

### 3.10 Governance and accountability

Documentation MUST identify or reference the governance information required by the applicable entity lifecycle: approval status, applicable authority, ownership responsibilities, and change-control information. The authority to approve a canonical semantic definition MUST remain distinguishable from responsibility for implementing, operating, or assessing the capability. Authoritative governance records are reused, not duplicated (GOVERNANCE.md; the Authorship Cardinal Rule CR-BP-118/CR-DEA-BC-34).

### 3.11 Provenance and evidence (BC-DOC-009)

Documentation MUST preserve traceability to the capability's origin, admission, and approval history under the existing methodology (EVIDENCE.md; the `evidence` and `provenance` record blocks; `catalog-research/` registers). Where applicable it MUST support references to evidence sources and disposition, admission rationale, semantic decisions, classification rationale, relationship justification, review findings, and change history. Authoritative sources, external reference material, proposed interpretations, and claims requiring validation MUST remain distinguishable.

### 3.12 Lifecycle and conformance (BC-DOC-010)

Documentation MUST support the applicable entity lifecycle, versioning, review, and change-control rules, distinguishing entity identity, entity content version, schema version, catalog release, and upstream model version. Deprecation, retirement, replacement, and migration information MUST be identifiable where applicable. Documentation conformance is a distinct concern that complements — never replaces — schema validation, semantic review, and governance controls.

## 4. Requirement applicability classification

Requirements in this standard carry exactly one applicability class:

| Class | Meaning |
|---|---|
| **Universally mandatory** | Applies to every approved canonical capability: canonical identity; canonical definition; classification and lifecycle status; sufficient semantic interpretation; defensible scope and boundaries; applicable provenance and approval records; conformance with identity and governance standards. |
| **Conditionally mandatory** | Applies when a relevant condition exists or a relationship is asserted: parent/child and specialization references; realization relationships; goal and outcome traceability; assessment-model references; replacement or migration references; additional scope constraints. A conditionally mandatory requirement MUST NOT be treated as satisfied merely because its corresponding field is absent — the condition itself MUST be recorded (§5.2). |
| **Recommended** | Improves interpretation and reuse but is not required: illustrative scenarios; additional diagrams; alternative realization patterns; extended domain commentary; further valid/invalid interpretation examples. |
| **Optional** | Permitted content with no standing expectation. |
| **Prohibited** | See §6. |

## 5. The canonical documentation contract

### 5.1 Section structure

Each capability entity's documentation interface (the entity README, rendered from or validated against the canonical record) MUST provide the following sections, in order:

1. Identity
2. Definition and semantic interpretation
3. Purpose and value contribution
4. Scope and boundaries
5. Classification
6. Composition and specialization
7. Related entities and relationships
8. Realization and operational context
9. Outcomes and traceability
10. Assessment considerations
11. Governance
12. Provenance and evidence
13. Lifecycle and change history
14. Conformance

For each section the standard (and, when implemented, the README template CR) MUST distinguish information rendered from canonical data from information requiring authored explanatory narrative.

### 5.2 Content states

A section MUST NOT be silently omitted because its content is unavailable. Documentation MUST record which of these states holds, and these states are not interchangeable:

| State | Meaning |
|---|---|
| Not applicable | The aspect does not apply to this capability, with the reason recorded |
| Not yet established | The underlying decision or relationship is genuinely open |
| Not yet documented | The information exists in authoritative sources but is not yet presented |
| Established and documented | Rendered and consistent with the canonical record |
| Explicitly unresolved | Deliberately parked, with the owning decision or CR referenced |

### 5.3 Proportionality

No fixed minimum length or identical narrative depth is imposed. The mandatory requirement is sufficiency: enough information to establish the capability's meaning, boundaries, and applicable relationships. Genuine gaps MUST be made visible rather than filled with invented content.

## 6. Prohibited documentation practices

The following are prohibited (enforcement arrives with the documentation-conformance gate CR; they are normative from acceptance of this standard):

- Conflicting canonical definitions across artifacts.
- Unapproved changes to entity identity conventions.
- Treating ECF coordinates as capability identity.
- Treating processes, systems, organizational units, or outcomes as equivalent to capabilities.
- Embedding assessment results into canonical capability identity.
- Presenting unverified or proposed relationships as established facts.
- Introducing industry-specific specialization into a first-order definition without satisfying the existing admission rules.

## 7. Artifact responsibilities

### 7.1 Canonical structured record

The record (`capabilities-*.yaml` under the entity subtree, validated by `schemas/entity.schema.json` per [CR-DEA-BC-40]) remains authoritative for canonical fields: identity, definition, classification, lifecycle status, and existing governed metadata. New structured attributes require a prior gap analysis against the existing schema and the upstream metamodel; this standard authorizes none by itself.

### 7.2 Entity README

The README is the human-readable documentation interface. It MUST explain the capability's meaning, purpose, boundaries, and relevant relationships consistently with the canonical record, and SHOULD navigate directly to relevant records, standards, evidence, and related entities. It MUST NOT maintain an independent, drift-prone copy of canonical facts: reproduced facts are derived from the record or validated against it.

### 7.3 Other authoritative artifacts

Schemas, governance records, evidence registers, relationship records, and assessment models retain their designated responsibilities. This standard defines the relationships among these artifacts without creating duplicate sources of truth.

## 8. Cross-artifact consistency rules (BC-DOC-012)

- The README's canonical name, identifier, definition, and displayed ECF coordinates MUST match the canonical record.
- Related-capability references MUST resolve to canonical records in this catalog.
- Repository-level counts and inventory claims MUST match the generated catalog inventory (`CATALOG.yaml`) — the class of drift documented and gated by [CR-DEA-BC-39] (`check_doc_links.py`, `check_cr_index.py`).
- A README MUST NOT claim an unapproved relationship exists.
- Reproduced canonical values MUST NOT silently diverge from the structured record (drift-checked, per §7.2).

## 9. Documentation conformance model

Documentation conformance is assessed along five distinguishable dimensions, complementary to (never conflated with) the existing schema, identity (`check_id_system.py`), entity-system (`check_entity_system.py`), ECF (`check_ecf_conformance.py`), authorship (`check_authorship.py`), and catalog-integrity gates:

| Dimension | Requirement |
|---|---|
| Structural completeness | Required documentation information is represented in the applicable artifacts |
| Semantic completeness | Meaning, purpose, boundaries, and distinctions are sufficiently established |
| Referential integrity | Declared references resolve to valid canonical entities or explicitly governed external sources |
| Cross-artifact consistency | README, canonical record, and authoritative artifacts do not contradict one another |
| Governance traceability | Required approval, provenance, lifecycle, and change-control information is available |

Structural and referential violations are objectively testable and become blocking when the gate CR lands. Semantic findings (activity-shaped definitions, unclear adjacent boundaries, rationale-less relationships, apparent duplicates, unsupported specializations, outcomes presented as guaranteed effects) are review findings — flagged for semantic review, not automatic build failures. **Semantic correctness cannot be established through structural validation alone.**

## 10. Normative requirement identifiers

These identifiers are local to this standard and are deliberately distinct from existing gate rule codes (AUT-*, ES-*, IDM-*, CST-*, DL-*, CR-001..005):

| ID | Normative subject | Aspect |
|---|---|---|
| BC-DOC-001 | Canonical identity and classification | §3.1 |
| BC-DOC-002 | Definition and semantic interpretation | §3.2 |
| BC-DOC-003 | Implementation independence | §3.3 |
| BC-DOC-004 | Scope and semantic boundaries | §3.4 |
| BC-DOC-005 | Composition and specialization | §3.5 |
| BC-DOC-006 | Enabling relationships and realization | §3.6 |
| BC-DOC-007 | Outcomes and traceability | §3.7 |
| BC-DOC-008 | Assessment separation | §3.8 |
| BC-DOC-009 | Provenance and governance | §3.10, §3.11 |
| BC-DOC-010 | Lifecycle and conformance | §3.12 |
| BC-DOC-011 | README completeness | §5, §7.2 |
| BC-DOC-012 | Cross-artifact consistency | §8 |

Where an existing normative requirement establishes the same obligation, the existing requirement governs and this standard references it; no competing rule is created.

## 11. Relationship to existing foundations

| Foundation | Relationship |
|---|---|
| [CR-DEA-BC-01](../change-requests/CR-DEA-BC-01.md) | Preserves the First-Order Business Capability Catalog Method |
| [CR-DEA-BC-01A](../change-requests/CR-DEA-BC-01A.md) | Preserves the reconciled record shape and upstream metamodel alignment |
| [CR-DEA-BC-03](../change-requests/CR-DEA-BC-03.md) | Consumes the schema + CI foundation; does not replace it |
| [CR-DEA-BC-29](../change-requests/CR-DEA-BC-29.md) | Preserves the rich-narrative expectations |
| [CR-DEA-BC-35](../change-requests/CR-DEA-BC-35-entity-system-business-capabilities.md) | Preserves entity-system institutionalisation and lifecycle controls |
| [CR-DEA-BC-35A](../change-requests/CR-DEA-BC-35A-org-wide-id-system-confirmation.md) | Preserves the confirmed organization-wide identity system |
| [CR-DEA-BC-39](../change-requests/CR-DEA-BC-39-index-numbering-doc-truth.md) | Preserves index, numbering, and documentation-integrity controls |
| [CR-DEA-BC-40](../change-requests/CR-DEA-BC-40-schema-reconciliation.md) | Preserves the current canonical entity schema and reconciled record shape |

## 12. Implementation sequence

This standard is the foundation CR (BC-41) of the enrichment tranche. Subsequent tranche CRs implement it in dependency order — entity model enrichment (gap analysis first), relationship semantics, README template + reference entity (Asset Management), documentation conformance gate, catalog-wide remediation, discovery and relationship views — and MUST implement the accepted standard rather than independently redefine its requirements. The grounding assessment for the tranche is preserved in the programme workspace (`CR-DEA-BC-DOC-000.md`).
