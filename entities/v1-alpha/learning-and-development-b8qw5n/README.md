# Learning and Development

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-learning-and-development-b8qw5n` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-learning-and-development-b8qw5n.yaml](capabilities-capability-learning-and-development-b8qw5n.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to build workforce capability through structured learning programs, courses, and curricula tied to skill needs.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence at density 3 (SRC-026 cluster) with the agency-organization/build cell empty before admission; distinct from Talent Management (the employment lifecycle) and Workforce Management (deployment). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Learning and Development so skill gaps close systematically through programs rather than ad hoc training spend.

## 4. Scope and boundaries

**Boundary** (from the record):

> Builds workforce capability through programs; does not manage the employment lifecycle (Talent Management) or plan skill demand (Workforce Planning).

**Non-examples** (from the record):

- A course catalog (an artifact)
- A learning-management system (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | agency-organization / build |
| Secondary | agency-organization / operate |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Learning and Development is building workforce capability through programs (build); delivery of learning (operate) participates but does not define it. Cell occupancy: agency-organization/{build, operate}.

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Program modalities (formal, on-the-job) are specialization; the capability-building ability is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Talent Management](../talent-management-v2qw9c/capabilities-capability-talent-management-v2qw9c.yaml) | recorded in `related_capabilities` |
| [Workforce Management](../workforce-management-9e8d8s/capabilities-capability-workforce-management-9e8d8s.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Workforce skills close the gap to need through governed programs.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 3 canonical objects in the cluster (training-program, course-section, education-program; SRC-026) reference no capability, and the agency-organization/build cell is empty; cross-signal convergence recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-05 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 3 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (agency-organization / build) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T2) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
