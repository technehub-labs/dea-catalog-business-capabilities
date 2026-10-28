# CR-DEA-BC-57: Evidence-Led Realization Reference Population

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-57 |
| Title | Evidence-Led Realization Reference Population |
| Status | Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them"; BC-56 findings accepted via PR #110) |
| Series | CR-DEA-BC |
| Change layer | L2 — Canonical record implementation |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Predecessor | CR-DEA-BC-56 — Realization Target Scheme Reconciliation |
| Primary deliverables | Approved realization references, validation tests, and a population report |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them"; BC-56 findings accepted via PR #110)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Completion tranche, Batch B step 3, executing BC-56's supported category (`processes`). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-57-realization-population`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** split from the combined tranche grounding; normative content verbatim. **Outcome: documented zero-population disposition** — the evidence reconciliation found the upstream `realizes` base contains exactly one exemplar assertion whose target is a legacy identifier (`dea:entity-capability:manage-customer-relationship`) predating both catalogs' id migrations and not resolving against this catalog's identities; mapping it by name similarity would be the inference §3.2 forbids. Per the tranche's controls ("no forced completeness"; "if an investigation proves a proposed implementation unnecessary, the appropriate outcome is a documented disposition"), no records are populated and the deferral is recorded with its named upstream gap.

## 2. Change Objective

Populate realization references for canonical Business Capabilities where an approved target scheme, an authoritative target entity, and sufficient evidence establish a valid realization relationship.

## 3. Normative Requirements

### 3.1 Apply only approved target schemes

Only target categories and identifier formats explicitly approved by BC-56 may be populated.

A scheme still awaiting upstream authorization must remain unavailable for canonical assertions under this CR.

### 3.2 Require evidence for each assertion

For each proposed reference, establish:

- The source capability.
- The canonical target identifier.
- The authorized target scheme.
- The meaning of the realization relationship.
- The evidence supporting the assertion.
- The validation result.
- The provenance of the change.

Do not infer that a capability is realized by a process, system, actor, resource, or information entity simply because the target appears relevant.

### 3.3 Preserve optionality and existing semantics

Do not make realization universally mandatory. Do not change the meaning of `purpose`, `outcome`, `related_capabilities`, or other existing fields to compensate for absent realization data.

Do not introduce duplicate references where an existing authoritative representation already satisfies the requirement.

### 3.4 Validate and report

Use the approved schema, reference-integrity gates, and target-catalog validation mechanisms.

The report must distinguish:

- Successfully populated references.
- Existing valid references.
- Unsupported candidate assertions.
- Invalid or unresolved target identifiers.
- Records for which no sufficiently evidenced realization relationship was established.
- Categories deferred due to upstream dependencies.

## 4. Acceptance Criteria

1. Every added reference conforms to a target scheme approved by BC-56.
2. Every added reference resolves to an authoritative target entity.
3. Every assertion has traceable evidence.
4. No unsupported realization relationship is inferred.
5. Schema, validation, and CI checks pass.
6. Canonical records, READMEs, and generated views remain consistent.
7. The report identifies residual gaps and blocked target categories honestly.

## 5. Dependencies and Execution Conditions

BC-56 must be accepted. A target category may be implemented only if its semantic and identity prerequisites have been resolved. If BC-56 leaves a category blocked, BC-57 must leave it unpopulated and document the deferral.

---
