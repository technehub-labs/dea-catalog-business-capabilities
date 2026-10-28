# Technology Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-technology-management-maus5n` |
| Entity type | BusinessCapability |
| Version / status | 1.3.2 · active |
| Record | [capabilities-capability-technology-management-maus5n.yaml](capabilities-capability-technology-management-maus5n.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to direct, invest in, and steward the enterprise's technology estate.

**Capability-hood** (from the record's `why_capability`):

E4; N-006R resolved at BC-08: a business capability whose object is Technology, not a cross-cutting concern. The technology estate is a stable subject with lifecycle; stewardship of the estate is the deliberate direction of an enterprise resource, which is the semantic anchor of Strategy & Direction. Per CR-DEA-BC-17 (2026-09-10): the "Technology-as-Enabler" sub-concern (technology-as-enabler, the use of technology by other capabilities to execute) is admitted as a distinct first-order capability `capabilities:capability-technology-enablement-y6nkws` at enablement-operations/operate. The two capabilities are paired: Technology Management directs and stewards the estate; Technology Enablement runs the services for the enterprise.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated per CR-DEA-BC-55 from the accepted BC-54 evidence register):

> The enterprise requires Technology Management so its technology estate is directed, invested in, and stewarded deliberately: choices funded, lifecycle-managed, answerable to strategy.

## 4. Scope and boundaries

**Boundary** (from the record):

> Stewards the enterprise technology estate (the set of platforms, applications, networks, data, and AI agents the enterprise uses). Does not execute operations through technology (Operations); does not derive insight from information (Analytics & Intelligence); does not govern information lifecycles (Information Management); does not run technology services and platforms for the rest of the enterprise (`capabilities:capability-technology-enablement-y6nkws`: admitted 2026-09-10 under CR-DEA-BC-17), or design the IT organization structure (Organizational Design: IT org design is a sub-concern). The defining distinction: this entry is the IT direction function (the estate); `capabilities:capability-technology-enablement-y6nkws` is the IT delivery function (the services).

**Non-examples** (from the record):

- An IT department (an organization)
- A specific platform (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | strategy-direction / build |
| Secondary | strategy-direction / operate |
| Secondary | strategy-direction / improve |

**Rationale** (from the record's `ecf_rationale`):

> CR-DEA-BC-13 §A re-evaluation: under the new "semantic center of gravity" rule, Technology Management's primary stays at strategy-direction/build because the *defining* activity is acquiring and constituting the technology estate (a direction-setting act: what technology bets the enterprise is making); secondaries strategy-direction/operate and strategy-direction/improve record the lifecycle participation. The carve-text update (CR-DEA-BC-13 §C) addresses BC-SR-A001 §12's concern: the "Technology-as-Enabler" sub-concern was deferred at that time. Per CR-DEA-BC-17 (2026-09-10): the deferred sub-concern is now admitted as a distinct first-order capability (`capabilities:capability-technology-enablement-y6nkws`) at enablement-operations/operate. Coordinate change remains carve-text only for THIS entry (primary unchanged); the companion admission of Technology Enablement is recorded under `related_capabilities`. Supersedes the pre-CR-13 rationale (N-006R / BC-08 "earliest legitimate initiation").

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Technology domains (network, cloud, OT, AI agents) are specialization of this capability (the estate). The "use of technology to enable execution" sub-concern is NOT a specialization of this capability; it is a separate first-order capability `capabilities:capability-technology-enablement-y6nkws` (admitted 2026-09-10 under CR-DEA-BC-17).

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Information Management](../information-management-6vjgdh/capabilities-capability-information-management-6vjgdh.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Technology Enablement](../technology-enablement-y6nkws/capabilities-capability-technology-enablement-y6nkws.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Organizational Design](../organizational-design-vanefq/capabilities-capability-organizational-design-vanefq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Technology choices are deliberate, funded, lifecycle-managed, and answerable to strategy.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-002, SRC-004, SRC-005 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Enterprise-generality demonstrated at E4; N-006 resolved at BC-08: technology is an estate, not an enabler of execution; stewardship of the estate belongs in Strategy & Direction, parallel to Asset Management and Facility Management. Evidence trail in docs/research (evidence-register, enterprise-generality-matrix, distinctness-sweep, admission-gate-closeout). Per CR-DEA-BC-17 (2026-09-10): the "Technology-as-Enabler" sub-concern BC-SR-A001 §12 carved out is admitted as a separate first-order capability (`capabilities:capability-technology-enablement-y6nkws`); this entry's relationship to that capability is recorded under `related_capabilities`.
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

Current: `v1.3.2` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

