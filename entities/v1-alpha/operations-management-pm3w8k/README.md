# Operations Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-operations-management-pm3w8k` |
| Entity type | BusinessCapability |
| Version / status | 2.0.0 · active |
| Aliases | Operations, Production Management, Service Delivery Management |
| Record | [capabilities-capability-operations-management-pm3w8k.yaml](capabilities-capability-operations-management-pm3w8k.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to run the enterprise's day-to-day production and delivery of value.

**Capability-hood** (from the record's `why_capability`):

E4; N-008 dissolved Value Delivery as a separate first-order capability and re-rooted Operations as the value-execution capability.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Runs delivery; does not manage the offerings delivered (Offering Management) or change how delivery works (Change Management). Operates the value stream; technology services and platforms that value stream depends on are operated by `capabilities:capability-technology-enablement-y6nkws` (admitted 2026-09-10 under CR-DEA-BC-17).

**Non-examples** (from the record):

- A production line (a resource)
- An operations department (an organization)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | enablement-operations / operate |
| Secondary | enablement-operations / improve |

**Rationale** (from the record's `ecf_rationale`):

> Primary operate in enablement-operations; improve participation is honest and recorded. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> What is operated (a network, a factory, a caseload) is specialization; the ability to operate is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Offering Management](../offering-management-6egkc8/capabilities-capability-offering-management-6egkc8.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Technology Enablement](../technology-enablement-y6nkws/capabilities-capability-technology-enablement-y6nkws.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Until the Relationship Semantics CR (R-1) lands, these entries are untyped references recorded in the canonical data — not typed semantic relationships.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Offerings are delivered, continuously, at the quality the enterprise commits to.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-001, SRC-002, SRC-004, SRC-006 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
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

