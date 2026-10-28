# Strategy Formulation

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-strategy-formulation-sf7q2x` |
| Entity type | BusinessCapability |
| Version / status | 2.0.0 · active |
| Aliases | Strategy |
| Record | [capabilities-capability-strategy-formulation-sf7q2x.yaml](capabilities-capability-strategy-formulation-sf7q2x.yaml) — authoritative |
| Layer | strategic |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to set the enterprise's direction: where it will compete, what it will become, and what it will not do.

**Capability-hood** (from the record's `why_capability`):

Direction-setting is exercised by every enterprise regardless of industry or implementation, is identifiable by its outcome, and passes the anti-invention test: every corpus source carries it.

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Sets direction; does not plan its pursuit (Strategic Planning), govern its execution (Enterprise Governance), or deliver value (Operations), or design its structure (Organizational Design).

**Non-examples** (from the record):

- A strategic plan document (an artifact of Strategic Planning)
- A board decision (an act of Enterprise Governance)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | strategy-direction / conceive |
| Secondary | strategy-direction / improve |

**Rationale** (from the record's `ecf_rationale`):

> Re-mapped 2026-09-10 (BC-SR-A001 §8.A, CR-DEA-BC-12 §A.1): the ECF Strategy & Direction domain explicitly owns "purpose and ambition, environmental sensing, strategic choices, objectives and targets, strategic planning, and strategic adaptation"; governance-existence only authorizes, it does not direct. Primary strategy-direction/conceive; secondary strategy-direction/improve for strategy adaptation. CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> What is being strategized (a product line, a nation, a network) is specialization; the ability to strategize is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Strategic Planning](../strategic-planning-k3rz7a/capabilities-capability-strategic-planning-k3rz7a.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Enterprise Governance](../enterprise-governance-uas48u/capabilities-capability-enterprise-governance-uas48u.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Organizational Design](../organizational-design-vanefq/capabilities-capability-organizational-design-vanefq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Enterprise Performance Management](../enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> An explicit, current statement of enterprise direction that constrains and guides every other capability.

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

Current: `v2.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

