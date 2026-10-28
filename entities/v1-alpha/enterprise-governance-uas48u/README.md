# Enterprise Governance

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-enterprise-governance-uas48u` |
| Entity type | BusinessCapability |
| Version / status | 1.0.2 · active |
| Record | [capabilities-capability-enterprise-governance-uas48u.yaml](capabilities-capability-enterprise-governance-uas48u.yaml) — authoritative |
| Layer | strategic |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to direct and control the enterprise: decision rights, accountability, oversight, and policy across the whole.

**Capability-hood** (from the record's `why_capability`):

Governance of the enterprise-as-a-whole is enterprise-general and implementation-independent; distinct from Risk, Compliance, and Legal by the distinctness sweep.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Governs the enterprise; does not manage specific obligation classes (Compliance, Legal), exposure (Risk), or change (Change Management), or design the structure (Organizational Design).

**Non-examples** (from the record):

- A board meeting (an event)
- A policy document (an artifact)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | governance-existence / conceive |
| Secondary | governance-existence / operate |
| Secondary | governance-existence / improve |

**Rationale** (from the record's `ecf_rationale`):

> Primary conceive in governance-existence (governance is constituted with the enterprise); exercised continuously at operate and improve. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Governance instruments (boards, councils, assemblies) vary by sector and ownership form; the ability to govern does not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Strategy Formulation](../strategy-formulation-sf7q2x/capabilities-capability-strategy-formulation-sf7q2x.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Risk Management](../risk-management-h9uxdw/capabilities-capability-risk-management-h9uxdw.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Organizational Design](../organizational-design-vanefq/capabilities-capability-organizational-design-vanefq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Decisions are made by the right authority, recorded, and enforced; the enterprise remains answerable to its principals.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-001, SRC-002, SRC-004 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Enterprise-generality demonstrated at E3; evidence trail in docs/research (evidence-register, enterprise-generality-matrix, distinctness-sweep, admission-gate-closeout).
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

