# Organizational Design

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-organizational-design-vanefq` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-organizational-design-vanefq.yaml](capabilities-capability-organizational-design-vanefq.yaml) — authoritative |
| Layer | strategic |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to structure the enterprise into roles, units, reporting lines, authorities, and coordination patterns that fit the work the enterprise must do, and to revise that structure when the work changes.

**Capability-hood** (from the record's `why_capability`):

E4 (foundation-grade per A+B+C gate; promotion from E3 at admission per EVIDENCE.md 3 admission promotion rule). BC-SR-A001 4 explicitly recommended this admission. CR-DEA-BC-13 B.1 carved Track A as a follow-on investigation; CR-DEA-BC-18 (research-CR) seeded the evidence package across three independent source classes (business-architecture / cross-industry-process / standards-body) and registered TER-ORGDESIGN-001 track record at E3; this CR closes the 4 evidence work and promotes to E4 on admission. Distinct business object (Organization Structure vs Workforce Management's Workforce Plan / Workforce Mgmt's Agent lifecycle / Strategy's Enterprise). Distinct ECF cell (agency-organization/design vs Workforce Planning at the same cell; distinctness passes by business-object partition; Organization Structure vs Workforce Plan).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Designs the enterprise's roles, units, reporting lines, authorities, and coordination patterns. DOES NOT set direction (Strategy; the structural design serves the strategy, does not define it). DOES NOT plan the workforce against the structure (Workforce Planning; separate planning ability against the designed structure). DOES NOT execute the agent lifecycle (Workforce Management; operates the workforce against the structure). DOES NOT govern the enterprise (Enterprise Governance; sets the authority framework, OrgDesign implements it operationally). DOES NOT manage change processes (Change Management; operates change initiatives; structural redesign is one trigger of change, not the change process itself). DOES NOT steward the technology estate (Technology Management; IT strategy and acquisition). DOES NOT run technology services (Technology Enablement; IT delivery). The defining distinction: Organizational Design is the structural-design function; Workforce Planning is the workforce-demand-supply-planning function; Workforce Management is the agent-execution function.

**Non-examples** (from the record):

- An organization chart (an artifact; the document of a structural decision)
- A reporting line (an artifact; one element of a structural decision)
- A specific role profile (an artifact; one role within a structure)
- A re-org event (a process; the act of implementing a structural change)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | agency-organization / design |
| Secondary | agency-organization / conceive |
| Secondary | agency-organization / build |

**Rationale** (from the record's `ecf_rationale`):

> Admitted 2026-09-11 under CR-DEA-BC-14. Under the semantic-center-of-gravity rule (CR-DEA-BC-13 A), the defining activity is sustained structuring of roles, authorities, units, and coordination patterns, squarely in the design axis of Agency & Organization. Secondaries: conceive (diagnostic/re-design) and build (operationalization). Distinct from Workforce Planning (same primary coordinate agency-organization/design) by business object; Organizational Design structures the enterprise (Organization Structure: roles, units, authorities), Workforce Planning sizes the demand-supply picture (Workforce Plan: capability and capacity at horizon). Peers; both inputs to Workforce Management.

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Structural archetypes (functional, divisional, matrix, network, holacratic, ambidextrous), governance patterns (centralized, federated, hub-and-spoke), and coordination mechanisms (hierarchies, communities-of-practice, platform teams, cells, squads) vary by enterprise context; the ability to design and revise a structure does not. Specializations include enterprise architecture for the structure's information flows, HR-organization design for the role architecture, IT-organization design for the IT org structure (a sub-concern that Tech Mgmt coordinates per CR-DEA-BC-13 C), and post-merger integration for transition structures.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Strategy Formulation](../strategy-formulation-sf7q2x/capabilities-capability-strategy-formulation-sf7q2x.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Strategic Planning](../strategic-planning-k3rz7a/capabilities-capability-strategic-planning-k3rz7a.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Enterprise Governance](../enterprise-governance-uas48u/capabilities-capability-enterprise-governance-uas48u.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Workforce Planning](../workforce-planning-b43rhm/capabilities-capability-workforce-planning-b43rhm.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Workforce Management](../workforce-management-9e8d8s/capabilities-capability-workforce-management-9e8d8s.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Change Management](../change-management-hukdeq/capabilities-capability-change-management-hukdeq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Technology Management](../technology-management-maus5n/capabilities-capability-technology-management-maus5n.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Technology Enablement](../technology-enablement-y6nkws/capabilities-capability-technology-enablement-y6nkws.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Enterprise Performance Management](../enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Until the Relationship Semantics CR (R-1) lands, these entries are untyped references recorded in the canonical data — not typed semantic relationships.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> The enterprise has a structure whose roles, authorities, and coordination patterns align with its strategy and operating context, and can be revised deliberately rather than drifting.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-017, SRC-018, SRC-019 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Admission per CR-DEA-BC-14 (Track A of CR-DEA-BC-13 B.1 / BC-SR-A001 4). Evidence trail: BC-SR-A001 4 (reviewer's P1; the catalog had Strategy + Strategic Planning + Workforce Planning + Workforce Management but not the structural-design capability the ECF positions in agency-organization/design); CR-DEA-BC-13 B.1 (Track A investigation opened); CR-DEA-BC-13 D.1 (ECF overlay hypothesis + track record stub); CR-DEA-BC-18 (research-CR evidence package; no admission); CR-DEA-BC-14 3 (semantic review gate) + 4 (architectural review gate) + 5 (admission-gate closeout). Enterprise-generality demonstrated at E3 (organization-design literature is universal across B2B/B2C/G2C enterprises per foundation inclusion criteria gate A+B+C; 9 of 10 types strong in enterprise-generality matrix, 1 moderate; cross-industry evidence in SRC-017 Galbraith, SRC-018 APQC PCF Organization category, SRC-019 ISO 9001 5.3 organizational roles). Evidence trail on disk: catalog-research/{candidates, evidence-register, enterprise-generality-matrix, distinctness-sweep, admission-gate-precheck, preliminary-ecf-overlay, INV-ORGDESIGN-v0.2, INV-ORGDESIGN-v0.1.yaml}.
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-09-10 | Emmanuel A. Otchere, BC-13 B.1 Track A candidate seeded (BC-13 carrier) |
| observed | 2026-09-10 | Emmanuel A. Otchere, BC-SR-A001 4 + Galbraith/APQC/ISO 9001 evidence seeding |
| corroborated | 2026-09-11 | Emmanuel A. Otchere, CR-DEA-BC-18 enterprise-generality matrix (B2B/B2C/G2C sweep) |
| normalized | 2026-09-11 | Emmanuel A. Otchere, CR-DEA-BC-18 distinctness sweep vs Strategy / Strategic Planning / Workforce Planning / Workforce Management / Tech Mgmt / Tech Enablement |
| ecf-mapped | 2026-09-11 | Emmanuel A. Otchere, ECF overlay hypothesis: agency-organization/design (primary); conceive + build secondaries |
| reviewed | 2026-09-11 | Emmanuel A. Otchere, CR-DEA-BC-14 3 (semantic review gate 1) + 4 (architectural review gate 2) |
| canonical | 2026-09-11 | eaojnr, admission PR (this change) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

