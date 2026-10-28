# CR-DEA-BC-59: Cross-Catalog Actor, Resource, System, and Information Reference Reconciliation

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-59 |
| Title | Cross-Catalog Actor, Resource, System, and Information Reference Reconciliation |
| Status | Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them") |
| Series | CR-DEA-BC |
| Change layer | L1 — Cross-catalog identity and semantic alignment |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Related predecessor | CR-DEA-BC-56 — Realization Target Scheme Reconciliation |
| Primary deliverable | `docs/CROSS-CATALOG-REFERENCE-SCHEME-RECONCILIATION.md` |
| Decision authority | Repository CR governance process and the respective upstream catalog owners |

**Status**: Accepted (user directive 2026-10-28: "Attached is BC-53 to BC-60 that will complete our CR round for this objective. Save, read and implement them")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Completion tranche, Batch B step 2 (dependency resolution). Upstream inspection at landing (GitHub API, 2026-10-28): `dea-catalog-actors` contains **zero entity directories** (Wave 3 scaffold); `resources`, `systems`, and `information` have **no owning catalog in the org at all**. Scope derived from BC-56's category inventory.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-58-59-upstream-dependencies` (two investigation CRs, independent dispositions, one carrier per the grounding's parallelism note). PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** split from the combined tranche grounding; normative content verbatim; investigation only — no canonical record or schema changes.

## 2. Change Objective

Resolve U-2 by establishing the authoritative identity and reference contracts for any Actor, Resource, System, or Information target category that the Business Capability catalog is authorized to reference.

The result must make unresolved reference schemes explicit and prevent local approximations from being treated as canonical identities.

## 3. Problem Statement

CR-DEA-BC-42 identified unresolved upstream schemes for actor, resource, system, and information concepts. CR-DEA-BC-43 left associated realization guidance subject to further resolution, while CR-DEA-BC-56 is responsible for identifying the target categories relevant to the realization model.

A target type may be conceptually relevant but still lack a stable identity contract, a canonical catalog, or a validated cross-catalog reference mechanism. Relevance alone does not authorize a canonical reference.

## 4. Normative Requirements

### 4.1 Establish the actual dependency set

Inspect the accepted findings of BC-56 and identify which target categories are genuinely needed by the Business Capability catalog.

Do not expand the scope to every possible entity category merely because it exists in the wider semantic model.

### 4.2 Reconcile each required scheme

For every in-scope target category, document:

- Authoritative catalog or semantic owner.
- Canonical entity type and identifier scheme.
- Reference syntax and resolution contract.
- Definition and semantic boundaries.
- Lifecycle behavior.
- Validation responsibilities.
- Consumer compatibility.
- Current availability and unresolved decisions.

The investigation must distinguish a formally established scheme from an expected, proposed, or merely observed convention.

### 4.3 Coordinate with upstream owners

Where a scheme is missing or ambiguous, record the exact decision required from the upstream owner.

Do not create a substitute local identifier scheme, silently normalize identifiers, or declare a cross-catalog reference valid without an authoritative resolution mechanism.

### 4.4 Produce a dependency disposition

For each category, assign one disposition:

- **Resolved:** authoritative scheme and reference contract confirmed.
- **Resolved with constraints:** use is authorized under explicit conditions.
- **Blocked upstream:** required authority or scheme is missing.
- **Not required:** no supported use case justifies adoption in the Business Capability catalog.
- **Deferred:** the dependency is acknowledged but not yet ready for decision.

Each disposition must include its rationale and evidence.

## 5. Acceptance Criteria

1. The scope is derived from documented Business Capability use cases and accepted BC-56 findings.
2. Every in-scope target category has an explicit dependency disposition.
3. Every resolved scheme is traceable to its authoritative owner.
4. No local replacement identity scheme is introduced.
5. The report identifies required upstream decisions and their impact on the BC catalog.
6. The findings distinguish technical reference validity from semantic validity.
7. No canonical record or schema changes occur under this CR.

## 6. Dependencies and Execution Conditions

BC-56 must provide the target-category inventory relevant to realization. Each upstream catalog retains authority over its own identity and semantic contract.

Any subsequent implementation must be scoped to the categories formally resolved by this CR or an approved successor. A blocked category must not be treated as available simply to achieve apparent completeness.

### Batch C: Programme closure and evidence-based disposition
