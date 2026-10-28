# CR-DEA-BC-51: Catalog Integrity and Conformance Reporting

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-51 |
| Title | Catalog Integrity and Conformance Reporting |
| Status | Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement") |
| Series | CR-DEA-BC |
| Change layer | L3 — Catalog-wide integrity and reporting |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Dependencies | Accepted validation rules from CR-45; relationship controls from CR-48; lifecycle governance from CR-49; remediation results from CR-46 where available |
| Primary deliverable | Catalog Integrity and Conformance Reporting Specification and report |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Here are CR's BC-48 to BC-52 to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Governance tranche step 4; aggregates the landed control surface (CR-45 validation, CR-48 relationship controls, CR-49 lifecycle governance, CR-46 remediation results). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-51-integrity-reporting`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Implementation: `scripts/generate_catalog_integrity_report.py` regenerates the report on demand by invoking the authoritative gates (never reimplementing them) and writing `docs/reports/CATALOG-INTEGRITY-REPORT.md` with the source revision recorded. The report is a committed snapshot (no CI freshness gate by design: a revision-stamped report would be stale on every commit; reproduction = run the generator at the revision under assessment). This is the evidence instrument CR-52 consumes.

## 2. Change Objective

Establish a consolidated and reproducible view of the catalog's structural, referential, documentation, and governance integrity.

The report must show what has been verified, what remains unresolved, and which results require human semantic review.

It must not collapse all dimensions into a single misleading score or treat automated conformance as proof of semantic quality.

## 3. Problem Statement

Individual validators and entity-level reviews can establish whether specific checks pass, but they may not provide a coherent view of the catalog's overall condition.

Maintainers need to understand:

- Whether the canonical inventory is internally consistent.
- Whether records conform to the accepted schema.
- Whether documentation meets the governing standard.
- Whether relationships and references resolve.
- Whether lifecycle and governance records are traceable.
- Which failures block publication.
- Which findings remain open for human review.

A consolidated report can provide this view if its measures are precisely defined and derived from authoritative results.

## 4. Scope

### In scope

1. Define catalog-level integrity dimensions.
2. Aggregate authoritative validator and review results.
3. Establish a consistent reporting structure.
4. Identify unresolved and blocking findings.
5. Distinguish automated results from human-reviewed outcomes.
6. Provide traceability from summary findings to affected entities and rules.
7. Define reporting freshness and reproducibility requirements.
8. Document limitations and exceptions.

### Out of scope

- Replacing existing validators.
- Creating a new semantic scoring model.
- Automatically determining capability quality.
- Changing the canonical schema.
- Creating a maturity or benchmarking framework.
- Publishing an external dashboard or service.
- Altering governance status based solely on report results.

## 5. Integrity Dimensions

The report must cover applicable dimensions supported by existing controls.

### 5.1 Inventory integrity

Reports the consistency of the canonical entity inventory and its expected record and documentation artefacts.

### 5.2 Schema conformance

Reports the outcomes of authoritative schema validation.

### 5.3 Documentation conformance

Reports README and documentation results under the accepted standard.

### 5.4 Referential integrity

Reports invalid or unresolved canonical references and authorized relationships.

### 5.5 Cross-artifact consistency

Reports detectable mismatches between records, READMEs, indexes, and derived outputs.

### 5.6 Governance traceability

Reports missing or unresolved governance references where such references are required.

### 5.7 Lifecycle integrity

Reports lifecycle-state or transition violations covered by accepted lifecycle rules.

### 5.8 Semantic review status

Reports whether required human semantic reviews have been completed, remain outstanding, or have resulted in unresolved findings.

This dimension must not be presented as an automated semantic correctness score.

## 6. Reporting Contract

The reporting specification must define:

- Reporting scope and inventory baseline.
- Source validators and review records.
- Result classifications.
- Counting rules.
- Treatment of conditional requirements.
- Treatment of approved exceptions.
- Treatment of unresolved findings.
- Report timestamp or source revision.
- Links to detailed findings.
- Known coverage limitations.

Each report must identify the source revision or equivalent reproducible input state used to generate it.

## 7. Result Classification

The report must distinguish at least:

- **Pass:** the applicable check completed successfully.
- **Fail:** a defined requirement was violated.
- **Not assessed:** the check was not performed.
- **Not applicable:** the requirement does not apply under the accepted rules.
- **Exception:** an authorized exception governs the finding.
- **Unresolved:** the result requires further evidence, decision, or review.

These states must not be conflated. In particular, `not assessed` must never be counted as `pass`.

## 8. Reporting and Prioritization

The report must provide:

1. A catalog-level summary.
2. Results by integrity dimension.
3. A list of blocking findings.
4. A list of unresolved semantic or governance decisions.
5. Entity-level traceability.
6. Approved exceptions.
7. A residual remediation backlog.
8. The source revision and reporting method.

If percentages or aggregate counts are included, the denominator and treatment of conditional and inapplicable requirements must be stated.

A composite score must not be introduced unless a separately approved specification defines its meaning and limitations.

## 9. Implementation Requirements

The reporting mechanism must:

- Consume existing authoritative validation results wherever possible.
- Avoid reimplementing validation rules.
- Produce reproducible output.
- Link findings to entities and governing requirements.
- Distinguish automated checks from manual review.
- Identify stale or incomplete source results.
- Preserve existing repository gates.
- Avoid making unauthorized changes to entity records.

The output may be a generated Markdown report or another repository-compatible format. The final format must be selected based on existing tooling and maintenance cost.

## 10. Acceptance Criteria

- **AC-01:** Integrity dimensions and their sources are documented.
- **AC-02:** The report identifies the source revision or input state.
- **AC-03:** Automated and human-review results are distinguished.
- **AC-04:** Pass, fail, not assessed, not applicable, exception, and unresolved states are distinct.
- **AC-05:** Aggregate measures have explicit denominators and counting rules.
- **AC-06:** Findings link to affected entities and governing requirements.
- **AC-07:** Blocking and unresolved findings are visible.
- **AC-08:** Existing validators are reused rather than duplicated.
- **AC-09:** Reporting is reproducible.
- **AC-10:** The report does not claim to prove semantic correctness through structural checks.
- **AC-11:** No unapproved scoring or benchmarking model is introduced.
- **AC-12:** Documentation and repository indexes are updated.

## 11. Definition of Done

The catalog integrity report can be regenerated from identifiable authoritative inputs, its measures are defined, and its findings are traceable. Limitations and unresolved issues are visible.

## 12. Acceptance Decision

**Requested decision:** Approve a consolidated catalog integrity and conformance reporting mechanism.

Approval does not authorize a new semantic quality score, maturity model, external reporting service, or automatic governance decision.