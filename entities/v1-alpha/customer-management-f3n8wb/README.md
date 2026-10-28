# Customer Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-customer-management-f3n8wb` |
| Entity type | BusinessCapability |
| Version / status | 1.0.1 · active |
| Record | [capabilities-capability-customer-management-f3n8wb.yaml](capabilities-capability-customer-management-f3n8wb.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to establish, develop, and end relationships with those the enterprise serves.

**Capability-hood** (from the record's `why_capability`):

The strongest-converged capability in the corpus (E5): every source class carries it under various names.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated per CR-DEA-BC-55 from the accepted BC-54 evidence register):

> The enterprise requires Customer Management so its relationships with those it serves are established, developed, and ended deliberately, yielding a known, managed customer base.

## 4. Scope and boundaries

**Boundary** (from the record):

> Manages the customer relationship; does not create demand (Marketing), manage partners (Partner Management), or manage the workforce (Workforce Management).

**Non-examples** (from the record):

- A CRM system
- A sales call (an activity)
- Customer Service Team (an actor)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | party-relationship / operate |
| Secondary | party-relationship / conceive |
| Secondary | party-relationship / improve |
| Secondary | party-relationship / retire |

**Rationale** (from the record's `ecf_rationale`):

> Primary operate in party-relationship (the relationship lives in operation); conceived, improved, and retired deliberately. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True; recorded industry examples: Telecom Customer Management (SPEC-001), Citizen/Member Relationship (SPEC-002, deferred)

**Specialization boundary** (from the record):

> Who the customer is (subscriber, citizen, member, patient, policyholder) is specialization; the ability to manage the relationship is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Partner Management](../partner-management-cp3vdb/capabilities-capability-partner-management-cp3vdb.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Marketing](../marketing-xmc539/capabilities-capability-marketing-xmc539.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> A known, managed customer base whose lifecycle is deliberate rather than accidental.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-001, SRC-002, SRC-003, SRC-004, SRC-005, SRC-006 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Enterprise-generality demonstrated at E5; evidence trail in docs/research (evidence-register, enterprise-generality-matrix, distinctness-sweep, admission-gate-closeout).
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

Current: `v1.0.1` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

