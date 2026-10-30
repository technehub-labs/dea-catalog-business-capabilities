# Subscription and Service Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-subscription-and-service-management-p3n8rt` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-subscription-and-service-management-p3n8rt.yaml](capabilities-capability-subscription-and-service-management-p3n8rt.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to manage the subscriber and service-instance lifecycle from order through activation, change, suspension, and retirement across commercial service offerings.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence at density 8 (SRC-026 cluster; the catalog's multi-industry corpus carries a full commercial-services flavor) with no owning capability; distinct from Customer Management (the relationship) and Offering Management (the offer, not the provisioned instance). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Subscription and Service Management so each subscriber's services and entitlements stay accurate from acquisition through retirement.

## 4. Scope and boundaries

**Boundary** (from the record):

> Governs the subscriber and service-instance lifecycle; does not design offerings (Offering Management), bill (Billing and Revenue Management), or operate the platforms that deliver the service (Technology Enablement).

**Non-examples** (from the record):

- A subscriber database (an artifact)
- A CRM (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | party-relationship / operate |
| Secondary | product-value / operate |
| Secondary | enablement-operations / operate |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Subscription and Service Management is sustained subscriber and service-instance stewardship (party-relationship/operate); entitlement realization (product-value/operate) and the service-delivery interface (enablement-operations/operate) participate but do not define it. Cell occupancy: party-relationship/operate (deepened), product-value/operate, enablement-operations/operate (deepened).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Service families (mobile, fixed, content) are specialization; the subscriber lifecycle ability is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Customer Management](../customer-management-f3n8wb/capabilities-capability-customer-management-f3n8wb.yaml) | recorded in `related_capabilities` |
| [Offering Management](../offering-management-6egkc8/capabilities-capability-offering-management-6egkc8.yaml) | recorded in `related_capabilities` |
| [Billing and Revenue Management](../billing-and-revenue-management-k7mwq2/capabilities-capability-billing-and-revenue-management-k7mwq2.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Subscribers and service instances are accurate, active, and retired deliberately.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 8 canonical objects in the cluster (subscriber, subscription, service-instance, service-number, sim-profile, tariff-plan, usage-record, prepaid-balance; SRC-026) reference no capability - the densest uncovered cluster; cross-signal convergence recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-02 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 8 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (party-relationship / operate) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T1) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
