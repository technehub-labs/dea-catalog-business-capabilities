# Financial Resource Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-financial-resource-management-cd3c7c` |
| Entity type | BusinessCapability |
| Version / status | 2.0.0 · active |
| Aliases | Financial Management |
| Record | [capabilities-capability-financial-resource-management-cd3c7c.yaml](capabilities-capability-financial-resource-management-cd3c7c.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to plan, record, control, and report the enterprise's financial resources in the operating cycle.

**Capability-hood** (from the record's `why_capability`):

E4; the operating-cycle counterpart to Financial Stewardship (E5), distinct per the sweep.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Runs the financial cycle; does not set financial constitution (Financial Stewardship) or manage non-financial assets (Asset Management).

**Non-examples** (from the record):

- An ERP finance module (a system)
- A finance department (an organization, CAND-030)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | finance-accounting / operate |
| Secondary | finance-accounting / conceive |

**Rationale** (from the record's `ecf_rationale`):

> Primary operate in finance-accounting; conceive participation (budgeting posture) recorded as secondary. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Accounting regimes (IFRS, GAAP, public-sector frameworks) are external obligation sets, not specializations of the ability.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Financial Stewardship](../financial-stewardship-c7xtfk/capabilities-capability-financial-stewardship-c7xtfk.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Enterprise Performance Management](../enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Until the Relationship Semantics CR (R-1) lands, these entries are untyped references recorded in the canonical data — not typed semantic relationships.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Money is accounted for, budgets hold, and financial reporting is accurate and timely.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-001, SRC-002, SRC-006 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Enterprise-generality demonstrated at E4; evidence trail in docs/research (evidence-register, enterprise-generality-matrix, distinctness-sweep, admission-gate-closeout).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-08-31 | Emmanuel A. Otchere, candidate universe v0.1 (PR #6) |
| observed | 2026-08-31 | Emmanuel A. Otchere, evidence register (PRs #5, #7) |
| corroborated | 2026-08-31 | Emmanuel A. Otchere, enterprise-generality matrix (PR #11) |
| normalized | 2026-08-31 | Emmanuel A. Otchere, normalization register + distinctness sweep (PRs #8, #12) |
| ecf-mapped | 2026-08-31 | Emmanuel A. Otchere, preliminary ECF overlay (PR #7) |
| reviewed | 2026-09-01 | Emmanuel A. Otchere, admission review v0.1 (PR #24) |
| canonical | 2026-09-01 | eaojnr, admission PR (this change) |

## 13. Lifecycle and change history

Current: `v2.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

