# Regulation Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-regulation-management-gya4d8` |
| Entity type | BusinessCapability |
| Version / status | 2.0.1 · active |
| Aliases | Compliance Management |
| Record | [capabilities-capability-regulation-management-gya4d8.yaml](capabilities-capability-regulation-management-gya4d8.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to know the enterprise's obligations and to conform to them demonstrably.

**Capability-hood** (from the record's `why_capability`):

E4; distinct from Risk (exposure) and Legal (counsel) per the sweep.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated per CR-DEA-BC-55 from the accepted BC-54 evidence register):

> The enterprise requires Regulation Management so its obligations are identified, interpreted, met, and the conformance demonstrably provable.

## 4. Scope and boundaries

**Boundary** (from the record):

> Manages conformance; does not assess exposure (Risk Management) or conduct legal work (Legal Matter Management).

**Non-examples** (from the record):

- A compliance tool (a system)
- An audit (an assurance event)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | governance-existence / activate |
| Secondary | governance-existence / operate |

**Rationale** (from the record's `ecf_rationale`):

> Primary activate in governance-existence (compliance is activated when obligations bind); operated thereafter. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Obligation sets (telecom license conditions, HIPAA, PSD2) are specialization; the ability to comply is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Risk Management](../risk-management-h9uxdw/capabilities-capability-risk-management-h9uxdw.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Obligations are identified, interpreted, met, and the conformance is provable.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-001, SRC-002, SRC-004, SRC-005 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
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

Current: `v2.0.1` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

