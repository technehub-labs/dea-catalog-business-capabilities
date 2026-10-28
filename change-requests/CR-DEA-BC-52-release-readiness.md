# CR-DEA-BC-52: Catalog Release Readiness and Publication

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-52 |
| Title | Catalog Release Readiness and Publication |
| Status | Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement") |
| Series | CR-DEA-BC |
| Change layer | L4 — Release governance and publication readiness |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Dependencies | Accepted integrity reporting from CR-51; existing repository versioning and release policy; accepted lifecycle and conformance controls |
| Primary deliverable | Catalog Release Readiness Standard |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Governance tranche step 5 (final); consumes CR-51's reporting instrument and aligns with the existing release policy (docs/VERSIONING.md + docs/release-cut-procedure.md, post-reset posture per CR-DEA-BC-36: no tags until the first post-reset cut). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-52-release-readiness`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Landing note: this CR establishes readiness criteria only — **no release, tag, or publication action is taken**; the decision vocabulary (Ready / Ready with approved exceptions / Not ready / Not assessed) is new to this document and does not alter existing governance states.

## 2. Change Objective

Establish explicit criteria for determining whether a particular canonical Business Capability catalog state is ready for release, publication, or other formally designated distribution.

The standard must ensure that release decisions are based on traceable evidence of catalog integrity and governance compliance, while preserving the repository's existing versioning and release policy.

It must distinguish the readiness of a catalog state from the semantic quality of every individual capability.

## 3. Problem Statement

A catalog may pass individual validation checks yet still be unsuitable for a particular release or publication purpose because required documentation is incomplete, unresolved changes remain, generated outputs are stale, or the proposed release state cannot be reproduced.

Conversely, the existence of non-blocking findings does not necessarily mean a catalog cannot be published. Readiness criteria must therefore define which conditions are blocking, which permit an explicit exception, and which are informational.

This CR establishes a controlled decision framework rather than introducing an independent release lifecycle.

## 4. Scope

### In scope

1. Define catalog release-readiness criteria.
2. Identify required validation and integrity evidence.
3. Define treatment of blocking findings and approved exceptions.
4. Establish a release-readiness checklist.
5. Require identification of the exact source state being evaluated.
6. Verify that generated artefacts correspond to the evaluated source state.
7. Record the release decision and its supporting evidence.
8. Align readiness assessment with existing versioning and release governance.
9. Define how failed readiness assessments are recorded and reconsidered.

### Out of scope

- Replacing existing repository versioning policy.
- Reintroducing or changing tags withdrawn under an earlier CR.
- Creating a new versioning scheme.
- Automatically publishing releases.
- Changing canonical records merely to meet an arbitrary release date.
- Defining maturity benchmarks or semantic quality scores.
- Overriding upstream metamodel or ECF governance.
- Declaring a release ready solely because all automated tests pass.

## 5. Readiness Principles

### 5.1 Readiness is evidence-based

A release decision must reference actual validation results, review outcomes, and the source state evaluated.

### 5.2 Readiness is purpose-specific

The repository must state what type of release or publication is being considered and which requirements apply.

A development snapshot and a formally designated catalog release may have different rules only where the existing release policy explicitly permits that distinction.

### 5.3 Blocking findings cannot be concealed

A blocking failure must prevent a positive readiness decision unless the governing policy explicitly permits a formally authorized exception.

### 5.4 Exceptions must be explicit

An exception must identify the finding, authority, rationale, scope, and any conditions imposed on publication.

### 5.5 Release state must be reproducible

The evaluated catalog state, validation inputs, and generated outputs must be identifiable so that the readiness decision can be audited.

### 5.6 Existing release governance remains authoritative

This CR must not independently establish new tag, version, or release-history behavior. Any required changes to those conventions must be separately authorized.

## 6. Release-Readiness Requirements

The standard must assess the following dimensions, where applicable.

### 6.1 Canonical inventory integrity

The catalog inventory must be reconciled against the authoritative entity records and repository conventions.

### 6.2 Schema and identity conformance

Canonical records must satisfy the accepted schema and organization-wide identity rules.

### 6.3 Documentation conformance

Applicable documentation requirements must pass the accepted validation or review procedure, subject to explicitly governed exceptions.

### 6.4 Relationship and reference integrity

Required references and authorized relationships must satisfy the applicable integrity rules.

### 6.5 Governance traceability

Required change records, provenance, and lifecycle decisions must be traceable.

### 6.6 Generated artefact freshness

Any generated discovery views, indexes, or reports included in the release must correspond to the evaluated canonical source state.

### 6.7 Outstanding findings

The readiness assessment must list unresolved blocking findings, warnings, exceptions, and semantic-review items.

### 6.8 Reproducibility

The source revision and verification evidence must be sufficient to reproduce the readiness assessment under the repository's established process.

## 7. Readiness Decision

The standard must define a controlled decision vocabulary consistent with existing repository governance.

It may use states such as:

- **Ready:** all required conditions are satisfied.
- **Ready with approved exceptions:** permitted exceptions are documented and authorized.
- **Not ready:** one or more blocking conditions remain unresolved.
- **Not assessed:** the required readiness assessment has not been completed.

These labels are proposed and must be reconciled with existing repository conventions before adoption.

A readiness decision must include:

- The catalog state evaluated.
- The intended release or publication purpose.
- The validation evidence reviewed.
- Blocking findings.
- Approved exceptions.
- Outstanding non-blocking findings.
- The decision and its authorization.
- Any applicable limitations.

## 8. Release-Readiness Checklist

Before a readiness decision, verify:

1. The evaluated source state is identified.
2. Canonical inventory integrity has been assessed.
3. Schema and identity checks have been completed.
4. Documentation conformance results are available.
5. Relationship and reference integrity has been assessed.
6. Required governance and lifecycle decisions are traceable.
7. Generated outputs are current or excluded from the release.
8. Blocking findings are resolved or handled under an explicitly authorized exception.
9. Unresolved semantic decisions are disclosed.
10. The validation report is reproducible.
11. Versioning and release steps follow the existing policy.
12. The final decision is recorded through the established governance process.

The checklist must not imply that every semantic question can be resolved by automated tests.

## 9. Failed Readiness and Reassessment

When a readiness assessment fails, the record must identify the blocking conditions and their owning CRs or review processes.

A failed assessment must not silently change canonical entities or bypass the validation process.

After remediation, readiness must be reassessed against the actual updated source state. Results from an earlier state must not be reused as proof of conformance for a materially different state without justification.

## 10. Required Deliverables

- Catalog Release Readiness Standard.
- Release-readiness checklist.
- Decision record template or equivalent repository-conformant mechanism.
- Mapping between readiness criteria and authoritative validation results.
- Guidance for exceptions and failed assessments.
- Documentation of versioning and release-policy dependencies.

Proposed document path:

`docs/CATALOG-RELEASE-READINESS-STANDARD.md`

## 11. Acceptance Criteria

- **AC-01:** Readiness criteria are explicit and traceable to governing requirements.
- **AC-02:** The evaluated source state is identifiable.
- **AC-03:** Required validation evidence is specified.
- **AC-04:** Blocking findings and approved exceptions are distinguished.
- **AC-05:** Human semantic review is not replaced by structural validation.
- **AC-06:** Generated artefacts are checked for freshness where applicable.
- **AC-07:** Failed assessments produce traceable remediation actions.
- **AC-08:** Reassessment evaluates the updated source state.
- **AC-09:** Existing versioning and release policy remains authoritative.
- **AC-10:** No unauthorized tag, version, or release-history changes are introduced.
- **AC-11:** The decision record is reproducible and auditable.
- **AC-12:** The standard is linked from the appropriate repository documentation indexes.

## 12. Definition of Done

The release-readiness standard and checklist are complete, their evidence requirements are explicit, and the decision process is consistent with existing repository governance. No release is declared or published merely as a consequence of landing this CR.

## 13. Acceptance Decision

**Requested decision:** Approve the catalog release-readiness standard and its associated decision procedure.

Approval establishes readiness criteria only. It does not authorize a catalog release, tag creation, version change, or publication action.