# Sourcing and Procurement

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-sourcing-and-procurement-esucp4` |
| Entity type | BusinessCapability |
| Version / status | 1.3.0 · active |
| Record | [capabilities-capability-sourcing-and-procurement-esucp4.yaml](capabilities-capability-sourcing-and-procurement-esucp4.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to acquire goods and services: sourcing choices, purchasing, and receipt.

**Capability-hood** (from the record's `why_capability`):

E4; distinct from Supplier Management (the relationship) per the sweep; object is the Purchase Order.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Executes acquisition; does not manage supplier relationships (Supplier Management) or the acquired assets (Asset Management).

**Non-examples** (from the record):

- A procurement suite (a system)
- Invoice Processing (a process, CAND-031)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | enablement-operations / operate |
| Secondary | enablement-operations / build |
| Secondary | strategy-direction / conceive |
| Secondary | strategy-direction / design |

**Rationale** (from the record's `ecf_rationale`):

> Re-mapped 2026-09-10 under CR-DEA-BC-13 §A new rule (semantic center of gravity). The defining activity of Sourcing & Procurement is sustained acquisition execution (operate); the build event (an individual purchase) and the upstream strategic-sourcing posture (conceive, design) participate but are not where the capability is defined. Originally mapped at strategy-direction/build under the pre-CR-13 "earliest initiation" rule; re-mapped to enablement-operations/build under CR-DEA-BC-12 §A.6; re-mapped again here from build to operate under the CR-13 rule. Cleanly separates Strategy (decides sourcing posture), Party & Relationship (Supplier Management owns the relationship), Enablement & Operations (executes acquisition), Finance (accounts for monetary exchange).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Acquisition regimes (public tendering, framework agreements) are obligation sets, not specializations of the ability.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Supplier Management](../supplier-management-d6fuj4/capabilities-capability-supplier-management-d6fuj4.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Until the Relationship Semantics CR (R-1) lands, these entries are untyped references recorded in the canonical data — not typed semantic relationships.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> The enterprise obtains what it needs, at deliberate terms, with a clean acquisition record.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-002, SRC-004, SRC-005 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
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

Current: `v1.3.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

