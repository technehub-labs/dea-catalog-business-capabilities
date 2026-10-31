# Incident and Problem Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-incident-and-problem-management-c2wk96` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-incident-and-problem-management-c2wk96.yaml](capabilities-capability-incident-and-problem-management-c2wk96.yaml) — authoritative |
| Layer | operational |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to detect, triage, resolve, and learn from incidents and problems so service disruption is minimized and root causes are addressed.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence at density 4 (SRC-026 cluster) with the enablement-operations/improve cell empty before admission; distinct from Operations Management (steady-state run) and Continuity Management (major-disruption survivability). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Incident and Problem Management so service disruption is contained quickly and recurrence is engineered out.

## 4. Scope and boundaries

**Boundary** (from the record):

> Restores and learns; does not run steady-state operations (Operations Management), manage technology platforms (Technology Enablement), or survive major disruption (Continuity Management).

**Non-examples** (from the record):

- A ticket queue (an artifact)
- An IT service-management tool (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | enablement-operations / improve |
| Secondary | enablement-operations / operate |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Incident and Problem Management is learning from disruption (improve); restoration work (operate) participates but the root-cause elimination is the center of gravity. Cell occupancy: enablement-operations/{improve, operate} (operate deepened).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Incident classes (service, security) are specialization; the restore-and-learn ability is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Operations Management](../operations-management-pm3w8k/capabilities-capability-operations-management-pm3w8k.yaml) | recorded in `related_capabilities` |
| [Technology Enablement](../technology-enablement-y6nkws/capabilities-capability-technology-enablement-y6nkws.yaml) | recorded in `related_capabilities` |
| [Continuity Management](../continuity-management-v3rn6u/capabilities-capability-continuity-management-v3rn6u.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Incidents are resolved fast and problems do not recur.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 4 canonical objects in the cluster (incident, ticket, configuration-item, environment; SRC-026) reference no capability, and the enablement-operations/improve cell is empty; cross-signal convergence recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-11 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 4 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (enablement-operations / improve) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T4) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
