# Idea Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-idea-management-86dckf` |
| Entity type | BusinessCapability |
| Version / status | 2.0.1 · active |
| Aliases | Innovation Management |
| Record | [capabilities-capability-idea-management-86dckf.yaml](capabilities-capability-idea-management-86dckf.yaml) — authoritative |
| Layer | strategic |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to originate, develop, and realize ideas into new or improved products, services, processes, and models.

**Capability-hood** (from the record's `why_capability`):

E4; repeatable organization-wide idea-to-value ability (ISO 56002); the outcome is identifiable and measured by national statistical agencies (Oslo Manual 2018 names innovation management as a distinct activity class).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated per CR-DEA-BC-55 from the accepted BC-54 evidence register):

> The enterprise requires Idea Management so ideas are originated, developed, and realized into products, services, processes, and models actually introduced to use — not merely ideated.

## 4. Scope and boundaries

**Boundary** (from the record):

> Originates the new; does not institutionalize enterprise change (Change Management) or manage the offering lifecycle (Offering Management).

**Non-examples** (from the record):

- An ideas portal (a system)
- An R&D lab (an organization)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | product-value / conceive |
| Secondary | product-value / design |

**Rationale** (from the record's `ecf_rationale`):

> Primary product-value x conceive (the ability is first exercised where the new is conceived); design participation follows; boundary against Change Management drawn by standard text (originates vs institutionalizes). CR-DEA-BC-13 §A re-evaluation 2026-09-10 under the new semantic-center-of-gravity rule, placement confirmed (no coordinate change).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Innovation kinds (product, process, business model) and sector programs are specialization; the ability to innovate is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Change Management](../change-management-hukdeq/capabilities-capability-change-management-hukdeq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Offering Management](../offering-management-6egkc8/capabilities-capability-offering-management-6egkc8.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Innovations are introduced to the market or brought into use, not merely ideated.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-002, SRC-004, SRC-015, SRC-016 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Enterprise-generality demonstrated at E4 after the corpus patch (SRC-015 ISO 56002, SRC-016 Oslo Manual 2018); evidence trail in docs/research (evidence-register v0.3, enterprise-generality-matrix v0.2, distinctness-sweep, admission-gate-closeout, admission-review-supplementary).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-08-31 | Emmanuel A. Otchere, candidate universe v0.1 (PR #6) |
| observed | 2026-08-31 | Emmanuel A. Otchere, evidence register (PRs #5, #7) |
| corroborated | 2026-09-01 | Emmanuel A. Otchere, enterprise-generality matrix v0.1/v0.2 (PRs #11, #28) |
| normalized | 2026-09-01 | Emmanuel A. Otchere, normalization register + distinctness sweep (PRs #8, #12) |
| ecf-mapped | 2026-09-01 | Emmanuel A. Otchere, preliminary ECF overlay + gate close-out v0.1 (PRs #7, #15) |
| reviewed | 2026-09-01 | Emmanuel A. Otchere, supplementary admission review v0.1 (PR #30; R-007) |
| canonical | 2026-09-01 | eaojnr, admission PR (this change) |

## 13. Lifecycle and change history

Current: `v2.0.1` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

