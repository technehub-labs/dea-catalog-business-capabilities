# Information Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-information-management-6vjgdh` |
| Entity type | BusinessCapability |
| Version / status | 1.0.2 · active |
| Record | [capabilities-capability-information-management-6vjgdh.yaml](capabilities-capability-information-management-6vjgdh.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to govern, structure, and steward the enterprise's information across its lifecycle.

**Capability-hood** (from the record's `why_capability`):

E4; span across domains resolved at review (R-003): the span is a property of the business object, not of initiation.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated per CR-DEA-BC-55 from the accepted BC-54 evidence register):

> The enterprise requires Information Management so its information is governed, structured, and stewarded across lifecycle: findable, trustworthy, correctly retained, and deliberately disposed.

## 4. Scope and boundaries

**Boundary** (from the record):

> Manages information; does not manage the technology that carries it (Technology Management) or produce analytics from it (Insight Management, formerly Analytics and Intelligence; renamed under CR-DEA-BC-22 on 2026-09-30 after ADR-ES-021 ratification of V-A). Information platforms and data infrastructure that information management depends on are operated by `capabilities:capability-technology-enablement-y6nkws` (admitted 2026-09-10 under CR-DEA-BC-17).

**Non-examples** (from the record):

- A database (technology)
- A report (an artifact)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | enablement-operations / operate |

**Rationale** (from the record's `ecf_rationale`):

> R-003: primary enablement-operations x operate; secondaries deliberately empty (honest-not-exhaustive). CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Information classes (health records, call detail records, case files) are specialization; the ability to manage information is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Technology Management](../technology-management-maus5n/capabilities-capability-technology-management-maus5n.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Technology Enablement](../technology-enablement-y6nkws/capabilities-capability-technology-enablement-y6nkws.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Information is findable, trustworthy, retained correctly, and disposed of deliberately.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-002, SRC-004 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
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

Current: `v1.0.2` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

