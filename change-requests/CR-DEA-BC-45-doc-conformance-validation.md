# CR-DEA-BC-45: Documentation Conformance Validation

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-45 |
| Title | Documentation Conformance Validation |
| Status | Accepted (user directive 2026-10-28: "BC-45 to BC-47 are attached to implement") |
| Series | CR-DEA-BC |
| Change layer | L3 — Validation, conformance, and repository quality controls |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Normative dependencies | Accepted CR-DEA-BC-41; accepted findings from CR-DEA-BC-42; final model disposition from CR-DEA-BC-43; accepted documentation standard and template from CR-DEA-BC-44 |
| Primary deliverable | Documentation conformance validation specification and its approved implementation |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "BC-45 to BC-47 are attached to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Tranche step 5; implements CR-DEA-BC-42 backlog R-4 (BC-DOC-011/012 enforcement). Upstream decisions landed: BC-41 standard (PR #94), BC-42 findings (PR #95, incl. the model-sufficient disposition), BC-43 model (PR #96 — no schema changes beyond clarifications; validation targets the accepted existing schema), BC-44 standard + template (PR #97). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-45-doc-conformance-validation`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Landing decision (§8/§4.1.10): the gate ships with rule IDs DCV-001..010 (reconciled to requirement IDs BC-DOC-001..012, no namespace conflict) and is wired into CI in **advisory mode** (no `--strict`) because the 29 existing READMEs predate the BC-44 standard; CR-DEA-BC-46 performs the remediation and flips this step to `--strict` (blocking). Severity assignments are normative from acceptance; only the CI activation is staged.

**Dependency condition:** Implementation must not begin until the governing requirements and template are accepted. If the model gap analysis or model-enrichment CR results in no schema changes, validation must target the accepted existing schema and conventions.

## 2. Objective

Establish repeatable checks that determine whether canonical Business Capability records and their associated README documentation satisfy the accepted structural, referential, and cross-artifact requirements.

The validation system must distinguish mechanically verifiable conditions from semantic judgments requiring human review.

It must report failures accurately, preserve existing repository controls, and avoid treating a successful structural check as proof that a capability is semantically valid or sufficiently evidenced.

## 3. Problem Statement

A documentation standard is not reliably enforceable if conformance depends entirely on reviewers remembering every requirement.

However, indiscriminate automation is equally problematic. A script that checks only for headings may report an incomplete README as compliant, while an overly strict validator may force contributors to invent data or create redundant fields to satisfy mechanical rules.

The repository needs a validation contract that identifies:

- What can be checked deterministically.
- What must be checked against the canonical record.
- What requires reference or link integrity checks.
- What requires human semantic review.
- How failures are reported and resolved.
- Which existing checks remain authoritative.

## 4. Scope

### 4.1 In scope

1. Define validation rules derived from the accepted standards and schema.
2. Classify each rule by validation method and severity.
3. Validate required README structure and content markers where deterministically checkable.
4. Verify consistency between canonical identity and README identity.
5. Check references and links where feasible.
6. Validate schema conformance using the repository's existing model and validators.
7. Detect selected cross-artifact inconsistencies.
8. Define a machine-readable validation report where consistent with repository conventions.
9. Add tests for valid, invalid, conditional, and exceptional cases.
10. Integrate checks into the existing validation process if explicitly authorized by the accepted CR scope.
11. Document limitations and human-review requirements.

### 4.2 Out of scope

- Redefining capability semantics.
- Replacing the accepted documentation standard.
- Replacing existing schema or ECF conformance controls.
- Automatic approval of entities.
- Automated admission or retirement of capabilities.
- Inferring missing facts or generating unsupported evidence.
- Catalog-wide remediation, which belongs to CR-46.
- Generated discovery views, which belong to CR-47.
- New upstream metamodel constructs.
- Weakening or bypassing existing repository gates.

## 5. Validation Architecture

The implementation must classify checks into the following layers.

### 5.1 Structural validation

Checks whether required files and structural elements exist in the expected locations and conform to accepted conventions.

Examples include:

- Canonical record file exists.
- README file exists.
- Required sections or section markers are present.
- Required identifiers are syntactically valid.
- Files use the approved record format.

Structural presence alone must not be interpreted as semantic completeness.

### 5.2 Schema validation

Checks canonical records against the accepted schema and model constraints.

It must reuse the repository's authoritative schema and existing validation mechanisms wherever possible.

It must not introduce a parallel schema or contradictory validation rules.

### 5.3 Referential integrity

Checks whether references resolve to the expected canonical entity or authoritative artefact.

Examples include:

- Related capability references point to known entities.
- Internal documentation links resolve.
- Required source references are present.
- Entity IDs and referenced identifiers follow the established identity rules.

The validator must distinguish an invalid reference from an unavailable external resource when it cannot reliably determine the cause.

### 5.4 Cross-artifact consistency

Checks deterministically verifiable agreement between canonical records and their README files.

Potential checks include:

- Canonical identifier agreement.
- Canonical name agreement.
- Definition agreement where the README is expected to reproduce the authoritative definition.
- Consistency of explicitly rendered classification values.
- Consistency of links to the canonical record.

The final set of checks must be based on the accepted standard, not assumptions about the current documentation format.

### 5.5 Semantic review

Requirements that depend on meaning, evidence quality, enterprise generality, or defensible boundaries must remain subject to human review unless a reliable, authorized method exists.

The validator must not claim to prove:

- That a capability is genuinely enterprise-general.
- That its definition is conceptually sound.
- That its admission evidence is sufficient.
- That its boundaries are semantically complete.
- That its ECF rationale is correct.
- That two related capabilities are appropriately distinct.

Where appropriate, the report may indicate that a manual review is required.

## 6. Rule Catalogue

The implementation must establish a rule catalogue with a stable identifier for each validation rule.

Each rule must define:

| Attribute | Requirement |
|---|---|
| Rule ID | Stable and unique |
| Normative source | Governing standard or schema requirement |
| Validation layer | Structural, schema, reference, cross-artifact, or human review |
| Target artefact | Record, README, reference, or repository |
| Condition | Explicit condition under which the rule applies |
| Severity | Blocking, warning, or informational |
| Failure message | Actionable explanation |
| Remediation guidance | Reference to the relevant standard or procedure |
| Test coverage | Evidence that the rule behaves as specified |

Rule IDs must be reconciled with existing repository identifiers before implementation. This CR must not introduce conflicting requirement namespaces.

## 7. Failure Severity and Exceptions

The validation contract must distinguish:

- **Blocking:** a violation of an accepted mandatory requirement or integrity constraint.
- **Warning:** a potential issue requiring review, where the available evidence does not justify automatic rejection.
- **Informational:** a non-blocking observation, recommendation, or review reminder.

Severity must follow the governing requirement. It must not be assigned merely according to implementation convenience.

Exceptions must be explicit, traceable, and governed. A validator must not silently suppress a failure because a record is difficult to correct.

Where an exception is permitted, the implementation must define its scope, justification, authority, and review conditions.

## 8. Implementation Requirements

The implementation must:

1. Reuse existing schema and conformance checks.
2. Avoid duplicate implementations of rules already enforced authoritatively.
3. Provide deterministic outputs for identical inputs.
4. Use clear failure messages identifying the affected artefact and rule.
5. Test both successful and failing cases.
6. Test conditional requirements and permitted exceptions.
7. Preserve the existing repository's identity and path conventions.
8. Avoid network-dependent checks where deterministic local validation is sufficient.
9. Handle external link checks in a way that distinguishes temporary unavailability from invalid repository references.
10. Document what the validator does not prove.

Any CI integration must be explicitly included in the accepted implementation scope and must preserve existing gate behavior unless an approved change authorizes otherwise.

## 9. Acceptance Criteria

- **AC-01:** Every automated rule maps to an accepted normative requirement or integrity contract.
- **AC-02:** Rule identifiers do not conflict with existing repository conventions.
- **AC-03:** Structural checks are distinguished from semantic review.
- **AC-04:** Existing schema and ECF conformance mechanisms are reused.
- **AC-05:** Canonical identity and applicable README consistency checks are implemented.
- **AC-06:** Reference checks report actionable failures.
- **AC-07:** Blocking, warning, and informational results have defined meanings.
- **AC-08:** Conditional requirements and approved exceptions are handled explicitly.
- **AC-09:** Tests cover valid, invalid, conditional, and exceptional cases.
- **AC-10:** Validation does not fabricate or infer missing canonical facts.
- **AC-11:** Existing repository gates are preserved or changed only through explicit authorization.
- **AC-12:** Limitations and manual-review requirements are documented.
- **AC-13:** Applicable repository checks pass.
- **AC-14:** The rule catalogue and relevant documentation indexes are updated.

## 10. Definition of Done

The CR is complete when the accepted validation contract is implemented, tested, documented, discoverable, and integrated only as authorized. Validation results must be reproducible, failures actionable, and semantic limitations explicit.

## 11. Acceptance Decision

**Requested decision:** Approve the documentation conformance validation contract and its bounded implementation, subject to completion of the upstream documentation and model decisions.

This CR does not authorize catalog-wide remediation or generated discovery outputs. It does not make automated validation a substitute for semantic review or admission governance.