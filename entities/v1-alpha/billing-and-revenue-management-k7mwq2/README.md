# Billing and Revenue Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-billing-and-revenue-management-k7mwq2` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-billing-and-revenue-management-k7mwq2.yaml](capabilities-capability-billing-and-revenue-management-k7mwq2.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to compute, issue, collect, and reconcile customer charges and invoices so rendered services convert into recognized revenue.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence at density 4 (SRC-026 cluster) with the finance-accounting/operate cell's revenue-cycle scope unoccupied before admission; distinct from Financial Resource Management (stewardship of the money) and Customer Management (the relationship, not the charge). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Billing and Revenue Management so rendered services convert reliably into collected, recognized revenue with a defensible audit trail.

## 4. Scope and boundaries

**Boundary** (from the record):

> Converts rendered service into cash; does not set prices (Offering Management), manage the customer relationship (Customer Management), or steward the money once collected (Financial Resource Management).

**Non-examples** (from the record):

- An invoice template (an artifact)
- A billing system (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | finance-accounting / operate |
| Secondary | finance-accounting / improve |
| Secondary | party-relationship / operate |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Billing and Revenue Management is the sustained billing and collection of charges (operate); rating design (improve) and the customer-account interface (party-relationship/operate) participate but do not define it. Cell occupancy: finance-accounting/{operate, improve}.

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Billing models (prepaid, postpaid, converged) are specialization; the ability to convert service into collected revenue is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Customer Management](../customer-management-f3n8wb/capabilities-capability-customer-management-f3n8wb.yaml) | recorded in `related_capabilities` |
| [Financial Resource Management](../financial-resource-management-cd3c7c/capabilities-capability-financial-resource-management-cd3c7c.yaml) | recorded in `related_capabilities` |
| [Sourcing and Procurement](../sourcing-and-procurement-esucp4/capabilities-capability-sourcing-and-procurement-esucp4.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Charges are billed accurately, collected on time, and reconciled to revenue.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 4 canonical objects in the cluster (invoice, credit-note, payment, tax-record; SRC-026) reference no capability; cross-signal convergence (ECF cell, object cluster, process mirror) recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-01 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 4 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (finance-accounting / operate) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T1) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
