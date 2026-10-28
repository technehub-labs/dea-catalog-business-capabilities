# CR-DEA-BC-54: Business Purpose Evidence Reconciliation

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-54 |
| Title | Business Purpose Evidence Reconciliation |
| Status | Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them") |
| Series | CR-DEA-BC |
| Change layer | L2 — Canonical record evidence and completeness |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Predecessors | CR-DEA-BC-41, CR-DEA-BC-42, CR-DEA-BC-43, CR-DEA-BC-46 |
| Primary deliverable | `docs/BUSINESS-CAPABILITY-PURPOSE-RECONCILIATION.md` |
| Supporting deliverable | A machine-readable per-capability findings register |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Completion tranche, Batch A step 2 (investigation; no record changes). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-54-purpose-reconciliation`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** split from the combined tranche grounding; normative content verbatim. Assessment method (§4.2 applied): for each capability, purpose is assessed by derivation from **admitted record evidence** — the `definition` (what) and the `outcome` admitted through the evidence ladder (the E-level recorded in `why_capability`), with the proposed purpose stating why the enterprise requires the ability by bridging definition to outcome. Derivation is not copying: the four concepts (definition/purpose/outcome/why_capability) are kept distinct, and no statement infers from name, coordinate, or generic enterprise assumptions.

## 2. Change Objective

Assess the `purpose` field across all canonical first-order Business Capability records and determine, for each capability, whether a purpose statement can be populated from existing authoritative evidence.

This CR is investigative. It does not authorize canonical record changes.

## 3. Problem Statement

CR-DEA-BC-42 established that `purpose` exists in the schema but is unpopulated across the 29 canonical capability records examined. CR-DEA-BC-43 clarified that purpose population is recommended and must be supported by authored evidence.

A blank field is not proof that a capability lacks purpose. Equally, the existence of `outcome`, `why_capability`, or `definition` does not authorize automatic copying into `purpose`. These fields have distinct semantic responsibilities.

The repository needs an evidence-based disposition for every canonical record before population begins.

## 4. Normative Requirements

### 4.1 Establish the current baseline

Inspect the current canonical inventory and identify every record in scope.

Record:

- Canonical entity identifier.
- Current `purpose` value or absence.
- Existing definition and outcome.
- Existing `why_capability` statement.
- Available evidence and provenance.
- Relevant README content.
- Findings and outstanding questions.

The inventory must be generated from the current repository state, not from a historical record count.

### 4.2 Assess purpose independently

For each capability, determine whether the available evidence supports an explicit purpose statement.

Each assessment must distinguish:

- **Supported:** evidence sufficiently establishes the purpose.
- **Partially supported:** evidence informs purpose but does not establish a complete statement.
- **Unsupported:** available evidence does not justify a purpose assertion.
- **Conflicted:** evidence sources materially disagree.
- **Not assessed:** review has not been completed.

The assessment must explain the disposition. It must not infer purpose solely from the capability's name, ECF coordinate, presumed enterprise universality, or a generic assumption about what enterprises do.

### 4.3 Preserve semantic distinctions

The review must distinguish:

- **Definition:** what the capability is.
- **Purpose:** why the enterprise possesses or requires the capability.
- **Outcome:** what the capability produces, enables, controls, preserves, or realizes.
- **Why capability:** the existing rationale supporting its classification as a capability.

Where these concepts overlap in the available prose, record the issue rather than mechanically duplicating text.

### 4.4 Produce an implementation-ready register

For every capability, record:

- Evidence reviewed.
- Proposed disposition.
- Proposed purpose statement, if sufficiently supported.
- Rationale and evidence references.
- Required human review.
- Conflicts or gaps.
- Whether the record is eligible for BC-55.
- Any evidence-gathering action required.

Do not modify canonical records, schema, README files, or generated views under this CR.

## 5. Acceptance Criteria

1. Every current canonical first-order capability appears exactly once in the reconciliation register.
2. Every record has an explicit assessment state.
3. Every proposed purpose statement is supported by traceable evidence.
4. Unsupported or conflicted cases remain unresolved rather than being filled with generic text.
5. Definition, purpose, outcome, and `why_capability` are assessed as distinct concepts.
6. The report records evidence gaps and human-review requirements.
7. The final register identifies exactly which records are eligible for implementation under BC-55.
8. The analysis introduces no schema changes, canonical record changes, or new mandatory population rule.

## 6. Dependencies and Execution Conditions

CR-DEA-BC-41 defines the documentation requirements. CR-DEA-BC-42 identifies the population gap. CR-DEA-BC-43 establishes the applicable purpose policy, and CR-DEA-BC-46 establishes the README rendering contract.

BC-55 must not begin populating purpose values until the findings of BC-54 have been accepted.

---
