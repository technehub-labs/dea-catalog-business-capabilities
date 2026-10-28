# CR-DEA-BC-58: Cross-Catalog Business Object Identity Reconciliation

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-58 |
| Title | Cross-Catalog Business Object Identity Reconciliation |
| Status | Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them") |
| Series | CR-DEA-BC |
| Change layer | L1 — Cross-catalog identity and semantic alignment |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Upstream dependency | `technehub-labs/dea-catalog-business-objects` |
| Primary deliverable | `docs/BUSINESS-OBJECT-IDENTITY-RECONCILIATION.md` |
| Decision authority | Repository CR governance process and the owning Business Objects catalog |

**Status**: Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Completion tranche, Batch B step 2 (dependency resolution; no migration). Upstream inspection at landing (GitHub API, 2026-10-28): `dea-catalog-business-objects` `entities/v1-alpha/` contains **zero entity directories** — the catalog is a Wave 3 scaffold with no admissions, so no authoritative identity contract has been exercised.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-58-59-upstream-dependencies` (two investigation CRs, independent dispositions, one carrier per the grounding's parallelism note). PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** split from the combined tranche grounding; normative content verbatim; investigation only — no canonical record or schema changes.

## 2. Change Objective

Resolve U-1 by determining whether and how Business Capability records may reference canonical Business Objects through the authoritative identity system of the Business Objects catalog.

## 3. Problem Statement

The Business Capability catalog currently uses `business_object` as a populated descriptive field. CR-DEA-BC-42 found multiple distinct values, including compound expressions, and identified the sibling Business Objects catalog as the potential authority for canonical business-object identities.

Replacing these descriptions with typed references without verifying target identity would create false referential precision. Conversely, leaving descriptive values indefinitely without a governed disposition could limit cross-catalog traceability.

## 4. Normative Requirements

### 4.1 Inspect the authoritative catalog

Determine the current status and contract of the Business Objects catalog, including:

- Canonical entity identity scheme.
- Entity lifecycle and admission status.
- Definition and scope of a Business Object.
- Handling of compound or composite concepts.
- Cross-catalog reference contract.
- Validation or resolution mechanism.
- Ownership and change-control rules.

If the upstream catalog does not provide a sufficiently stable or authoritative identity contract, record U-1 as unresolved.

### 4.2 Reconcile current values

Inventory the `business_object` values across the canonical capability records.

For each value, record whether it is:

- Matched to one authoritative Business Object.
- Matched to multiple possible objects.
- A compound expression requiring semantic review.
- A valid descriptive value with no established canonical target.
- Unresolved or unsupported.

Do not equate lexical similarity with semantic identity.

### 4.3 Recommend a reference strategy

Evaluate whether the appropriate future model is:

- Continued descriptive text.
- A canonical typed reference.
- A reference plus a retained human-readable label.
- A structured multi-object reference, if authorized by the model.
- A deferred disposition because the upstream contract is not ready.

The recommendation must account for backward compatibility, compound values, validation, and the risk of creating two sources of truth.

### 4.4 Do not perform unauthorized migration

This CR is an investigation and dependency-resolution CR. It must not replace current values or change the schema unless a separately authorized implementation CR explicitly approves those changes.

## 5. Acceptance Criteria

1. The upstream identity contract is documented and its authority confirmed.
2. Every current `business_object` value is accounted for in the reconciliation register.
3. Ambiguous and compound values receive explicit dispositions.
4. No reference is proposed as canonical without a resolvable target and semantic justification.
5. U-1 is either resolved with an approved reference strategy or explicitly remains blocked with a documented reason.
6. No canonical record or schema changes occur under this CR.

## 6. Dependencies and Execution Conditions

The Business Objects catalog is the authoritative source for its own identity scheme. This CR may not define or override that scheme. Any implementation arising from its findings requires a separate CR with an approved migration and compatibility plan.

---
