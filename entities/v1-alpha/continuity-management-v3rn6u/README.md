# Continuity Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-continuity-management-v3rn6u` |
| Entity type | BusinessCapability |
| Version / status | 2.0.0 · active |
| Aliases | Resilience Management |
| Record | [capabilities-capability-continuity-management-v3rn6u.yaml](capabilities-capability-continuity-management-v3rn6u.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to maintain continuity of product and service delivery at an acceptable predefined capacity during disruption, and to recover.

**Capability-hood** (from the record's `why_capability`):

E4; the continuity business object and the boundary against Risk and Security are drawn by ISO 22301, not by assertion; BCI GPG 7.0 carries an explicit all-sector applicability claim.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Manages continuity of delivery through disruption; does not treat uncertainty (Risk Management) or apply protective control (Security Management).

**Non-examples** (from the record):

- A business continuity plan (an artifact)
- A crisis management team (an organization)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | governance-existence / design |
| Secondary | governance-existence / operate |

**Rationale** (from the record's `ecf_rationale`):

> Primary governance-existence x design (continuity posture is designed into the enterprise); operated continuously through disruption response. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Sector continuity regimes (financial operational resilience under DORA, clinical service continuity) are specialization; the ability to continue delivery is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Risk Management](../risk-management-h9uxdw/capabilities-capability-risk-management-h9uxdw.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Security Management](../security-management-wmzc7c/capabilities-capability-security-management-wmzc7c.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Delivery continues at acceptable predefined capacity through disruption; response and recovery are prepared, exercised, and validated.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-002, SRC-004, SRC-013, SRC-014 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Enterprise-generality demonstrated at E4 after the corpus patch (SRC-013 ISO 22301, SRC-014 BCI GPG 7.0); evidence trail in docs/research (evidence-register v0.3, enterprise-generality-matrix v0.2, distinctness-sweep, admission-gate-closeout, admission-review-supplementary).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-08-31 | Emmanuel A. Otchere, candidate universe v0.1 (PR #6) |
| observed | 2026-08-31 | Emmanuel A. Otchere, evidence register (PRs #5, #7) |
| corroborated | 2026-09-01 | Emmanuel A. Otchere, enterprise-generality matrix v0.1/v0.2 (PRs #11, #28) |
| normalized | 2026-09-01 | Emmanuel A. Otchere, normalization register + distinctness sweep (PRs #8, #12) |
| ecf-mapped | 2026-09-01 | Emmanuel A. Otchere, preliminary ECF overlay + gate close-out v0.1 (PRs #7, #15) |
| reviewed | 2026-09-01 | Emmanuel A. Otchere, supplementary admission review v0.1 (PR #30; R-006) |
| canonical | 2026-09-01 | eaojnr, admission PR (this change) |

## 13. Lifecycle and change history

Current: `v2.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

