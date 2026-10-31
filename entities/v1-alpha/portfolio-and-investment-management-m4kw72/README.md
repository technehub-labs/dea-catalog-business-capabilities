# Portfolio and Investment Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-portfolio-and-investment-management-m4kw72` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-portfolio-and-investment-management-m4kw72.yaml](capabilities-capability-portfolio-and-investment-management-m4kw72.yaml) — authoritative |
| Layer | strategic |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to select, prioritize, fund, and oversee the portfolio of initiatives and investments against strategic direction.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence at density 5 (SRC-026 cluster) with the strategy-direction/design cell empty before admission; distinct from Strategy Formulation (choosing direction), Enterprise Performance Management (measuring outcomes), and Change Management (executing change). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Portfolio and Investment Management so constrained investment flows to the initiatives that best serve the strategy.

## 4. Scope and boundaries

**Boundary** (from the record):

> Selects and oversees the investment portfolio; does not formulate strategy (Strategy Formulation), execute initiatives (Change Management), or measure performance (Enterprise Performance Management).

**Non-examples** (from the record):

- A project plan (an artifact)
- A portfolio-management tool (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | strategy-direction / design |
| Secondary | strategy-direction / build |
| Secondary | finance-accounting / conceive |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Portfolio and Investment Management is portfolio selection and shaping (design); funding (build) and business-case conception (finance-accounting/conceive) participate but do not define it. Cell occupancy: strategy-direction/{design, build}, finance-accounting/conceive (deepened).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Portfolio slices (technology, transformation) are specialization; the investment-selection ability is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Strategic Planning](../strategic-planning-k3rz7a/capabilities-capability-strategic-planning-k3rz7a.yaml) | recorded in `related_capabilities` |
| [Enterprise Performance Management](../enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml) | recorded in `related_capabilities` |
| [Technology Management](../technology-management-maus5n/capabilities-capability-technology-management-maus5n.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> The initiative portfolio traces to strategy and earns its funding.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 5 canonical objects in the cluster (project, business-case, transformation-plan, budget, grant; SRC-026) reference no capability, and the strategy-direction/design cell is empty; cross-signal convergence recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-06 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 5 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (strategy-direction / design) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T2) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
