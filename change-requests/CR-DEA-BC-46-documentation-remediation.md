# CR-DEA-BC-46: Canonical Entity Documentation Remediation

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-46 |
| Title | Canonical Entity Documentation Remediation |
| Status | Accepted (user directive 2026-10-28: "BC-45 to BC-47 are attached to implement") |
| Series | CR-DEA-BC |
| Change layer | L2 — Catalog-wide documentation adoption and conformance |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Normative dependencies | Accepted CR-DEA-BC-41 and CR-DEA-BC-44 |
| Validation dependency | Accepted CR-DEA-BC-45, or an explicitly approved interim review procedure |
| Primary deliverable | Catalog-wide entity documentation conformance and remediation record |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "BC-45 to BC-47 are attached to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Tranche step 6; executes CR-DEA-BC-42 backlog R-5 with the accepted validation mechanism (CR-DEA-BC-45, PR #98: gate live, baseline recorded 523 blocking / 87 warnings) and the accepted standard + template (CR-DEA-BC-44, PR #97; assessment F-01..F-16 for the reference entity). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-46-documentation-remediation`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Landing decisions: (a) remediation renders every README deterministically from its canonical record (the BC-44 template's own philosophy) — canonical values are never hand-typed, honest states are rendered where the record is unpopulated (purpose per the M-1 no-bulk-generation policy, realization pending U-2, assessment standing state); (b) zero canonical records are modified under this CR; (c) the known count drift in `entities/v1-alpha/README.md` (31/34 vs actual 29 canonical + 3 candidates) is corrected as a documentation-only finding; (d) the CR-DEA-BC-45 CI step flips to `--strict` in this PR (0 blocking / 0 warnings at head).

**Dependency condition:** The accepted README standard and template must be available before remediation begins. The validation mechanism must be available or an approved manual conformance procedure must be defined. This CR does not authorize changes to canonical entity meaning merely to make documentation conform.

## 2. Objective

Bring the catalog's canonical Business Capability entity READMEs into conformance with the accepted documentation standard, using a controlled, evidence-based, and auditable remediation process.

The goal is not to make every README longer or force every entity into identical explanatory prose. The goal is consistent documentation completeness, faithful representation of canonical records, explicit treatment of applicable requirements, and traceable resolution of material deficiencies.

## 3. Problem Statement

A common template and validation contract establish the required documentation practice, but the existing catalog may contain entity READMEs written under different conventions or at different levels of completeness.

Uncontrolled catalog-wide editing can introduce semantic drift, accidental changes to canonical definitions, unsupported assertions, broken references, or unnecessary duplication.

Remediation must therefore proceed from inventory and assessment to bounded corrections, with a clear distinction between documentation-only changes and changes requiring separate semantic or data-model authorization.

## 4. Scope

### 4.1 In scope

1. Establish a complete inventory of canonical capability records and associated READMEs within the approved catalog scope.
2. Assess each README against the accepted documentation standard.
3. Identify structural, explanatory, referential, and cross-artifact deficiencies.
4. Prioritize remediation according to severity and dependency.
5. Correct documentation-only defects.
6. Align README presentation with the canonical structured record.
7. Resolve broken or inaccurate internal links where the intended target is unambiguous.
8. Record exceptions and unresolved issues.
9. Validate remediated entities using the accepted validation mechanism.
10. Produce a catalog-wide remediation summary and residual backlog.

### 4.2 Out of scope

- Adding or removing canonical capabilities.
- Changing entity IDs or names without separate authorization.
- Rewriting canonical definitions to suit a template.
- Changing ECF assignments or rationale without an approved semantic decision.
- Inventing evidence, provenance, outcomes, relationships, or specialization rules.
- Modifying the schema outside the scope of an accepted model CR.
- Replacing the admission methodology.
- Changing upstream metamodel or governance foundations.
- Generating derived discovery views, which belong to CR-47.
- Automatically accepting entities that have not passed applicable governance review.

## 5. Remediation Principles

### 5.1 Canonical fidelity

Every remediation must preserve the authoritative meaning of the structured record.

If the README and record conflict, the discrepancy must be investigated. The README must not be changed blindly when the underlying record may itself be incorrect.

### 5.2 Evidence before assertion

Remediation must not fill missing sections with invented facts or generic claims.

Where required information is absent from the record and its authoritative sources, the finding must be recorded for separate resolution.

### 5.3 Smallest justified correction

Each correction must be limited to the deficiency being addressed. Broad stylistic rewrites must not obscure the substantive changes.

### 5.4 Separate documentation and semantic changes

Every finding must be classified as one of:

- Documentation-only correction.
- Reference or link correction.
- Cross-artifact consistency issue.
- Canonical record issue.
- Semantic or governance issue requiring another CR.
- Permitted exception or unresolved dependency.

Only authorized categories may be corrected under this CR.

### 5.5 Reproducible completion

A remediation is not complete merely because a README has been edited. It must satisfy the applicable acceptance conditions and pass the prescribed review or validation.

## 6. Required Remediation Inventory

The CR must produce a machine-readable or otherwise consistently structured inventory using the repository's established conventions.

For each entity, record:

| Attribute | Required content |
|---|---|
| Entity ID | Existing canonical identifier |
| Entity name | Canonical name |
| README path | Path to the entity README |
| Record path | Path to the canonical structured record |
| Assessment status | Not assessed, assessed, remediated, exception, or unresolved |
| Conformance result | Result from the approved validator or review procedure |
| Findings | Stable finding identifiers and descriptions |
| Remediation classification | Documentation, reference, record, semantic, or exception |
| Authorized changes | Summary of changes permitted under this CR |
| Verification evidence | Relevant test or review result |
| Outstanding dependencies | Any unresolved decision or separate CR |

The inventory must not create a competing entity identity system. Existing canonical IDs remain authoritative.

## 7. Remediation Procedure

### 7.1 Phase A — Inventory and baseline

1. Identify the canonical entity records within scope.
2. Identify their corresponding READMEs.
3. Detect missing or orphaned documentation.
4. Run the accepted validator or perform the approved baseline review.
5. Record the initial state without modifying entity content.

The baseline must be retained so that the repository can distinguish pre-existing deficiencies from defects introduced during remediation.

### 7.2 Phase B — Assessment and classification

Assess each entity against the accepted README standard.

Each finding must reference the relevant requirement and identify the actual source of the deficiency.

A missing README section must not automatically trigger content creation if the underlying requirement is conditional or belongs in another authoritative artefact.

### 7.3 Phase C — Prioritization

Prioritize findings using the governing severity model.

At minimum, distinguish:

- Blocking conformance or identity issues.
- Material semantic inconsistencies.
- Missing mandatory documentation.
- Broken authoritative references.
- Non-blocking explanatory improvements.

The priority order must not override dependencies. For example, a README must not be updated to reproduce a field whose semantics remain unresolved.

### 7.4 Phase D — Controlled correction

Apply authorized documentation-only corrections.

For each correction:

1. Preserve canonical identity.
2. Verify source values against the record.
3. Use evidence-backed explanatory content.
4. Keep conditional and inapplicable information distinct.
5. Preserve valid references and provenance.
6. Avoid unrelated formatting or prose changes.
7. Record any issue that cannot be resolved within this CR.

### 7.5 Phase E — Validation and review

Run the accepted validation process over the affected entities.

Where semantic review is required, retain the review result and identify the reviewer or governed decision reference according to repository conventions.

Any unresolved failure must remain visible in the inventory.

### 7.6 Phase F — Closure and residual backlog

Produce a summary containing:

- Total entities in scope.
- Total entities assessed.
- Total entities remediated.
- Conformance results before and after remediation.
- Findings resolved.
- Approved exceptions.
- Outstanding issues requiring separate CRs.
- Any validation limitations.

Counts must be derived from the actual inventory and validation results rather than estimated.

## 8. Exception Handling

An exception is permitted only where the governing standard allows it and the exception has an explicit rationale.

The exception record must include:

- The entity and requirement concerned.
- The reason the requirement cannot be satisfied as written.
- The authoritative decision or approval.
- Any alternative evidence or reference.
- The scope and duration of the exception, where applicable.
- The condition for reconsideration, where applicable.

Exceptions must not be used to conceal missing evidence, bypass identity constraints, or make an invalid record appear compliant.

## 9. Acceptance Criteria

- **AC-01:** The in-scope entity and README inventory is complete and reconciled against the canonical catalog.
- **AC-02:** Every in-scope entity has a recorded assessment status.
- **AC-03:** Findings map to accepted documentation requirements.
- **AC-04:** Documentation-only corrections are distinguished from semantic or record changes.
- **AC-05:** No unsupported facts or evidence are introduced.
- **AC-06:** Canonical identities remain unchanged.
- **AC-07:** README values agree with authoritative record values.
- **AC-08:** Required references are valid or recorded as unresolved.
- **AC-09:** Remediated entities pass the accepted validation process or have an explicitly governed exception.
- **AC-10:** Unresolved semantic and model issues are assigned to separate CRs or documented dependencies.
- **AC-11:** The final remediation report is reproducible from the inventory and validation results.
- **AC-12:** Repository indexes and change records are updated under existing governance.
- **AC-13:** Existing admission, schema, ECF, and integrity controls remain effective.
- **AC-14:** No unapproved inventory, schema, identity, or upstream semantic changes are introduced.

## 10. Definition of Done

The CR is complete when the catalog-wide assessment has been performed over the defined scope, all authorized corrections have been applied, all entities have a recorded outcome, and the residual issues are explicitly documented.

Completion does not require pretending that every entity is fully conformant. A genuine unresolved semantic issue must remain visible rather than being hidden by a superficial documentation edit.

## 11. Acceptance Decision

**Requested decision:** Approve catalog-wide documentation assessment and controlled remediation against the accepted standard.

Approval does not authorize changes to canonical capability meaning, inventory, schema, identity, ECF assignment, or upstream foundations. Those changes require the relevant separate CR and approval.