# Enterprise Performance Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-enterprise-performance-management-5fxren` |
| Entity type | BusinessCapability |
| Version / status | 1.0.2 · active |
| Record | [capabilities-capability-enterprise-performance-management-5fxren.yaml](capabilities-capability-enterprise-performance-management-5fxren.yaml) — authoritative |
| Layer | strategic |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to define, measure, monitor, evaluate, govern, and improve enterprise-wide performance against intended objectives and targets, completing the direction loop that links strategy to adaptation.

**Capability-hood** (from the record's `why_capability`):

Performance measurement against objectives is exercised by every enterprise regardless of industry or implementation (B2B, B2C, G2C demonstrated at admission); identifiable by its outcome (performance known, evaluated, and adapted); passes the anti-invention test via three-source convergence (SRC-020 Kaplan & Norton Balanced Scorecard; SRC-021 OKR framework; SRC-022 OMG Business Performance Management via OCEB 2). The object and outcome tests carry the decision: Enterprise Performance is a governed thing with its own lifecycle (defined, measured, evaluated, improved), and the outcome (the direction loop closed) is distinct from the plan (Strategic Planning), the direction (Strategy Formulation), and the insight derived from measurement (Insight Management).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated per CR-DEA-BC-55 from the accepted BC-54 evidence register):

> The enterprise requires Enterprise Performance Management so performance against intended objectives is defined, measured, evaluated, governed, and adapted — closing the direction loop from strategy through insight to change.

## 4. Scope and boundaries

**Boundary (structured, CR-DEA-BC-29 rich-narrative form).**

Distinguished against:

| Capability | Rationale (from the record) |
|---|---|
| `capabilities:capability-insight-management-ms4n9d` | Insight Management derives decision-grade insight from information; EPM governs enterprise performance against objectives. Distinct objects (Insight vs Enterprise Performance) and complementary outcomes. EPM is the measurement/governance half of the direction loop; Insight Management is the insight half. They are complementary, not overlapping. |
| `capabilities:capability-financial-resource-management-cd3c7c` | Financial Resource Management handles the money side (operating cycle; budgeting; accounting); EPM handles the multi-dimensional enterprise-performance side (financial + operational + strategic). Distinct objects (Financial Resource vs Enterprise Performance). |
| `capabilities:capability-strategy-formulation-sf7q2x` | Strategy Formulation sets the objectives (posture); EPM measures performance against them. Distinct objects (Enterprise direction vs Enterprise Performance against direction). |
| `capabilities:capability-strategic-planning-k3rz7a` | Strategic Planning is the plan; EPM is the measurement against the plan. Distinct objects (Plan vs Enterprise Performance). |
| `capabilities:capability-financial-stewardship-c7xtfk` | Financial Stewardship is the long-horizon financial position; EPM is the multi-dimensional performance measurement. Distinct objects (Financial Position vs Enterprise Performance) and distinct horizons. |
| `capabilities:capability-organizational-design-vanefq` | Organizational Design structures the enterprise; EPM measures how the structured enterprise performs. Distinct objects (Organization Structure vs Enterprise Performance). |

**Loop role.** Direction loop closure (BC-SR-A001 §16): Strategy Formulation -> Strategic Planning -> Performance Management (EPM) -> Insight Management -> Adaptation -> Strategy. EPM and Insight Management are the governance/measurement and insight halves respectively; together they complete the loop that Strategy Formulation opens.

**Non-examples** (from the record):

- A Balanced Scorecard dashboard (a system artifact)
- A KPI catalogue (a measurement artifact)
- An annual performance-review cycle (a process instance)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | strategy-direction / operate |
| Secondary | strategy-direction / improve |
| Secondary | finance-accounting / operate |

**Rationale** (from the record's `ecf_rationale`):

> Admitted 2026-10-12 (CR-DEA-BC-23; overlay hypothesis per CR-DEA-BC-19): the ECF Strategy & Direction domain owns objectives-and-targets and strategic adaptation; performance governance against those objectives is the operate-stage half of the direction loop (BC-SR-A001 §16). Primary strategy-direction/operate; secondaries strategy-direction/improve (performance feeds adaptation) and finance-accounting/operate (financial performance measurement interlocks with the operating cycle). Placement reviewed under the BC-13 semantic-center-of-gravity rule at admission; no re-evaluation needed post-admission.

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Sector performance regimes (clinical quality metrics, regulatory capital adequacy, safety-critical KPI frameworks) are specialization; the ability to define, measure, and govern enterprise performance against objectives is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Strategy Formulation](../strategy-formulation-sf7q2x/capabilities-capability-strategy-formulation-sf7q2x.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Strategic Planning](../strategic-planning-k3rz7a/capabilities-capability-strategic-planning-k3rz7a.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Insight Management](../insight-management-ms4n9d/capabilities-capability-insight-management-ms4n9d.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Financial Resource Management](../financial-resource-management-cd3c7c/capabilities-capability-financial-resource-management-cd3c7c.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Financial Stewardship](../financial-stewardship-c7xtfk/capabilities-capability-financial-stewardship-c7xtfk.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Organizational Design](../organizational-design-vanefq/capabilities-capability-organizational-design-vanefq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Enterprise performance is defined, measured, evaluated, governed, and adapted against objectives, closing the direction loop that links strategy to insight to change.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-020, SRC-021, SRC-022, SRC-001, SRC-002, SRC-004, SRC-005, SRC-006 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Admission per CR-DEA-BC-23 (Track B of CR-DEA-BC-13 B.2 + BC-SR-A001 §5 P1). Evidence trail: TER-EPM-001 (admitted; 2026-10-12); three-source convergence across business-architecture (SRC-020 Kaplan & Norton Balanced Scorecard), commercial-capability-models (SRC-021 OKR framework per Andy Grove / John Doerr), standards-body (SRC-022 OMG Business Performance Management via OCEB 2); E3 at admission. Enterprise-generality demonstrated across B2B, B2C, G2C archetypes; foundation-grade under BC-SR-A001 §17. Closes the direction loop (BC-SR-A001 §16): Strategy Formulation -> Strategic Planning -> Performance Management -> Insight Management -> Adaptation. ECF placement per CR-DEA-BC-13 §D.2 + CR-DEA-BC-19: strategy-direction/operate primary; strategy-direction/improve + finance-accounting/operate secondaries. H8 noun-as-ability: Management gerund passes cleanly. No review-retained exemption needed. Prior research artifacts preserved at entities/v1-alpha/epm-5fxren/candidates/epm.yaml per BC-09 §8 provenance discipline; research/ subdirectory inherited for new artifacts at this canonical id.
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-09-10 | Emmanuel A. Otchere, under CR-DEA-BC-13 §D.2 (investigation Track B; BC-SR-A001 §5 P1) |
| observed | 2026-09-11 | Emmanuel A. Otchere, evidence register v0.7 (PR #72, CR-DEA-BC-19) |
| corroborated | 2026-09-11 | Emmanuel A. Otchere, enterprise-generality matrix v0.3 + distinctness sweep v0.5 |
| normalized | 2026-09-11 | Emmanuel A. Otchere, normalization register v0.5 + distinctness sweep v0.5 |
| ecf-mapped | 2026-09-11 | Emmanuel A. Otchere, CR-DEA-BC-19 ECF overlay hypothesis (strategy-direction/operate primary) |
| reviewed | 2026-09-11 | BC-SR-A001 §5 (reviewer P1; loop-closure narrative required per §D.2) |
| evidence-seeded | 2026-09-11 | Emmanuel A. Otchere, TER-EPM-001 evidence-seeded; CAND-037 E1 -> E3 |
| admitted | 2026-10-12 | Emmanuel A. Otchere, CR-DEA-BC-23 admission; 29th first-order canonical capability |

- **admission_cr:** CR-DEA-BC-23

- **evidence_seed_cr:** CR-DEA-BC-19

## 13. Lifecycle and change history

Current: `v1.0.2` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

