# Order Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-order-management-t6wm3h` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-order-management-t6wm3h.yaml](capabilities-capability-order-management-t6wm3h.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to capture, validate, fulfil, and close customer orders across their commercial lifecycle.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence at density 6 (SRC-026 cluster) with the order-to-fulfilment lifecycle unowned; distinct from Offering Management (the offer) and Billing and Revenue Management (the charge). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Order Management so committed customer orders are fulfilled accurately and closed without revenue leakage.

## 4. Scope and boundaries

**Boundary** (from the record):

> Owns the order lifecycle; does not negotiate the offer (Offering Management), bill the order (Billing and Revenue Management), or source the goods (Sourcing and Procurement).

**Non-examples** (from the record):

- An order form (an artifact)
- An order-management system (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | party-relationship / operate |
| Secondary | finance-accounting / operate |
| Secondary | product-value / operate |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Order Management is order lifecycle management (party-relationship/operate); the billing handoff (finance-accounting/operate) and fulfilment interface (product-value/operate) participate but do not define it. Cell occupancy: party-relationship/operate (deepened), finance-accounting/operate (deepened), product-value/operate (deepened).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Order kinds (sales, purchase, return) are specialization; the order lifecycle ability is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Customer Management](../customer-management-f3n8wb/capabilities-capability-customer-management-f3n8wb.yaml) | recorded in `related_capabilities` |
| [Billing and Revenue Management](../billing-and-revenue-management-k7mwq2/capabilities-capability-billing-and-revenue-management-k7mwq2.yaml) | recorded in `related_capabilities` |
| [Supplier Management](../supplier-management-d6fuj4/capabilities-capability-supplier-management-d6fuj4.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Orders are fulfilled completely, accurately, and on time.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 6 canonical objects in the cluster (order, quote, price-list, contract, purchase-order, return; SRC-026) reference no capability; cross-signal convergence recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-03 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 6 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (party-relationship / operate) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T2) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
