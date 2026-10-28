# CR-DEA-BC-56: Realization Target Scheme Reconciliation

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-56 |
| Title | Realization Target Scheme Reconciliation |
| Status | Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them") |
| Series | CR-DEA-BC |
| Change layer | L1 — Reference model and cross-catalog semantics |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Predecessors | CR-DEA-BC-42, CR-DEA-BC-43, CR-DEA-BC-48 |
| Related dependencies | U-1 and U-2 from CR-DEA-BC-42 |
| Primary deliverable | `docs/REALIZATION-TARGET-SCHEME-RECONCILIATION.md` |
| Decision authority | Repository CR governance process, with upstream owners for their identity schemes |

**Status**: Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Completion tranche, Batch B step 1 (investigation; no population). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-56-realization-schemes`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** split from the combined tranche grounding; normative content verbatim. The sibling-catalog landscape inspected at landing (per the repo's own namespace table in `entities/v1-alpha/README.md`): processes — populated (3,598 records, org-wide id scheme `processes:*` post-mv1); services — populated (18 records, `services:*`); actors / orgunits / objects / stakeholders — Wave 3 scaffolds (empty). No systems, resources, or information catalogs exist in the org.

## 2. Change Objective

Establish which realization targets may be referenced by a canonical Business Capability, the authoritative identity schemes for those targets, and the validation requirements for each supported target category.

This is an investigation and model-disposition CR. It does not populate realization fields.

## 3. Problem Statement

The canonical schema already provides a `realization` structure, but the records reviewed under CR-DEA-BC-42 had no populated realization references. CR-DEA-BC-43 clarified the `processes` target pattern while leaving other target schemes subject to further guidance and upstream resolution.

A realization reference must identify an entity through its authoritative identity scheme. A label, prose description, guessed identifier, or locally invented prefix is not an adequate substitute.

## 4. Normative Requirements

### 4.1 Inventory the realization model

Inspect the current schema, model documentation, entity-system registry, and any authoritative upstream catalogs.

For every realization target category under consideration, record:

- Target entity kind.
- Intended realization semantics.
- Owning catalog or semantic authority.
- Canonical identifier scheme.
- Permitted reference format.
- Validation mechanism.
- Availability of canonical targets.
- Lifecycle and deprecation behavior.
- Current population and evidence.
- Unresolved dependency or decision.

### 4.2 Separate known schemes from unresolved schemes

The existing `processes:*` reference pattern may be used only within the scope already authorized by CR-DEA-BC-43 and its governing contract.

For other target categories, the investigation must establish whether a canonical scheme exists and whether the BC catalog is authorized to consume it.

Do not assume that all realization targets share the same identifier format.

### 4.3 Clarify realization semantics

The report must distinguish capability realization from related but different concepts, including:

- Activities or tasks that execute work.
- Processes through which an enterprise performs work.
- Systems or resources that enable execution.
- Information or data used or produced.
- Actors that perform or govern work.
- Outcomes that the capability enables or produces.

The relationship between each target category and the capability must be stated only to the degree authorized by the applicable semantic model.

### 4.4 Recommend a bounded implementation

For each target category, recommend one of the following:

- Supported under the existing contract.
- Supported after documentation or validation clarification.
- Requires an approved model change.
- Blocked on an upstream identity or semantic decision.
- Not appropriate as a realization target.

The report must distinguish the evidence supporting a recommendation from unresolved assumptions.

## 5. Scope

**In scope**

- Realization property and target-format analysis.
- Upstream identity and semantic dependency mapping.
- Existing target-catalog inspection.
- Validation and migration recommendations.
- A prioritized implementation backlog.

**Out of scope**

- Populating realization references.
- Creating new identity schemes.
- Modifying upstream catalogs.
- Redefining Business Capability or Process semantics.
- Adding target types without semantic justification.

## 6. Acceptance Criteria

1. Every target category currently declared or proposed for realization is inventoried.
2. Each supported target format is backed by an authoritative scheme.
3. `processes:*` handling is explicitly reconciled with CR-DEA-BC-43.
4. Unresolved target categories have named dependencies and an explicit disposition.
5. The report identifies the smallest required implementation changes.
6. No canonical record, schema, or upstream catalog is changed under this investigation CR.

## 7. Dependencies and Execution Conditions

CR-DEA-BC-43 is the current local model authority for realization guidance. CR-DEA-BC-48 provides relationship-integrity constraints. U-1 and U-2 must be resolved through the relevant catalog owners before dependent reference schemes are adopted.

---
