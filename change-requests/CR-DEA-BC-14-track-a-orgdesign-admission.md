# CR-DEA-BC-14 — Admit Organizational Design as a First-Order Canonical Capability

**Status**: Proposed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-11
**Depends on**: CR-DEA-BC-01 (method, landed); CR-DEA-BC-02 (evidence investigation, landed); CR-DEA-BC-05 (versioning, landed); CR-DEA-BC-12 (BC-SR-A001 carrier, landed 2026-09-10); CR-DEA-BC-13 (method rule + Tech-mgmt carve + Track A/B/C stubs, landed 2026-09-10); CR-DEA-BC-18 (Track A evidence package, landed 2026-09-11); BC-SR-A001 §4 (reviewer P1)
**Related**: dea-metaframework ADR-ECF-003 (agency-organization/design definition); dea-metamodel ADR-015 (agency-organization domain)
**Supersedes**: none
**Closes**: CR-DEA-BC-13 §B.1 follow-on queue item CR-DEA-BC-14 (Track A admission, provisional); BC-SR-A001 §4 evidence work; TER-ORGDESIGN-001 track record (open → closed)

---

## 1. What this CR is

This CR is the **admission CR** that closes the BC-SR-A001 §4 deferred item (reviewer's P1: "the catalog has Strategy + Strategic Planning + Workforce Planning + Workforce Management but not the structural-design capability the ECF positions in `agency-organization/design`"). It admits **Organizational Design** as a new first-order canonical capability, updates the eight peer entries that now have a structural-design neighbor, and closes the Track A evidence loop started by CR-DEA-BC-13 §B.1 and seeded by CR-DEA-BC-18.

The CR-DEA-BC-18 research-CR landed the evidence package on disk (CAND-036; SRC-017/018/019 across three independent source classes; TER-ORGDESIGN-001 track record at E3; ECF overlay hypothesis; enterprise-generality matrix row; admission-gate pre-check with `evidence_ge_E3` disclosed as `gap`). This CR closes that gap (E3 → E4 per EVIDENCE.md §3 admission promotion rule) and admits the entry.

### 1.1 Outcome

- **Catalog count: 27 → 28 first-order canonical capabilities.**
- **New entry:** `dea:capability-organizational-design` at `agency-organization/design` (primary) with `agency-organization/conceive` and `agency-organization/build` as secondaries.
- **New pair:** Organizational Design (structure, `agency-organization/design`) and Workforce Planning (workforce plan, `agency-organization/design`) — same ECF primary coordinate, distinct by business object (Organization Structure vs Workforce Plan).
- **Eight existing entries updated (Patch-tier; related_capabilities + boundary-text exclusion extension):**
  - Strategy (1.1.0 → 1.1.1)
  - Strategic Planning (1.1.0 → 1.1.1)
  - Workforce Management (1.1.0 → 1.1.1)
  - Workforce Planning (1.1.0 → 1.1.1)
  - Change Management (1.0.0 → 1.0.1)
  - Technology Management (1.3.0 → 1.3.1)
  - Technology Enablement (1.0.0 → 1.0.1)
  - Enterprise Governance (1.0.0 → 1.0.1)
- **Track A closed:** TER-ORGDESIGN-001 status `evidence-seeded` → `closed`; CAND-036 E3 → E4; admission-gate pre-check `evidence_ge_E3` → `met`.
- **Tag target: v1-alpha.8** (Minor bump — new first-order admission).

### 1.2 Why this CR exists at all

BC-SR-A001 §4 said:

> *"The catalog currently has Strategy, Strategic Planning, Workforce Planning, and Workforce Management, but not Organizational Design — the structural-design capability the ECF positions in `agency-organization/design`. Per METHODOLOGY §5 anti-invention test, this is a foundational gap; an adopting enterprise that changes industry tomorrow still requires an organizational design capability."*

The reviewer flagged it as **P1** (immediate). BC-13 §B.1 carved Track A as a follow-on investigation; BC-18 seeded the evidence package. This CR admits it.

---

## 2. Why one CR, not separate

The change is bounded and reviewable end-to-end:

- **One new entry** (`dea:capability-organizational-design`) — a single, self-contained YAML file with full provenance, evidence trail, and ECF conformance block.
- **Eight existing entries updated** — all are cross-reference additions + boundary-text exclusion extensions (Patch-tier per `docs/VERSIONING.md §1.2`); no coordinate moves, no identity changes.
- **One catalog-regeneration** (`CATALOG.yaml`; canonical count 27 → 28; 6 entries bumped to 1.0.1/1.1.1/1.3.1).
- **One research-artifact bookkeeping pass** (candidates/evidence-register/overlay/sweep/precheck/INV bumped to closed/admitted state).
- **One tag** (`v1-alpha.8`).

Splitting into separate CRs (one per touched entry) would multiply review surface for no architectural benefit. The bundle is reviewable because the new entry is the center of gravity and the eight existing-entry updates are mechanical cross-references that follow from it.

---

## 3. Semantic review (per METHODOLOGY.md §12 gate 1)

### 3.1 Definition

> **Organizational Design:** the ability to structure the enterprise into roles, units, reporting lines, authorities, and coordination patterns that fit the work the enterprise must do, and to revise that structure when the work changes.

The definition satisfies the Section 1 requirements (durable ability, independent of organization / process / people / technology / implementation) and is substrate-neutral (works for human-only, AI-agent, and hybrid enterprises equally).

### 3.2 Distinctions (Section 3)

| Distinction | Pass? | Why |
|---|---|---|
| Object Focus | ✅ | Business object is "Organization Structure" (distinct from Strategy's Enterprise, Strategic Planning's Plan, Workforce Planning's Workforce Plan, Workforce Management's Agent lifecycle, Change Management's Change, Tech Mgmt's Technology Estate, Tech Enablement's Technology Service, Enterprise Governance's Decision). |
| Outcome focus | ✅ | Outcome is "structure aligns with strategy and operating context, and can be revised deliberately rather than drifting" — a distinct outcome. |
| Implementation Independence | ✅ | Different enterprises realize it as functional, divic, network, holacratic, ambidextrous, matrix, etc. — the capability is the *what*, not the *how*. |
| Anti-invention classification | ✅ | Not a System (structures are operated by systems), not an Outcome (the outcome is alignment-with-strategy), not an Organization (CAND-030 disambiguation exemplar). |
| Not duplicating any existing entry | ✅ | See §3.3 (8-pair sweep). |

### 3.3 Distinctness sweep (extended to 8 pairs in this CR)

| Compared to | Distinct because |
|---|---|
| Strategy | Strategy sets the posture (Enterprise object); OrgDesign implements it structurally (Organization Structure object). Parent-child. |
| Strategic Planning | Strategic Planning sequences initiatives (Plan object); OrgDesign designs the structure they operate within. Distinct business object. |
| Workforce Management | Workforce Management runs the agent lifecycle (Agent lifecycle object); OrgDesign designs the structure those agents populate. Distinct business object. |
| Workforce Planning | Workforce Planning sizes the demand-supply picture (Workforce Plan object); OrgDesign designs the structure the plan fits. **Same primary ECF coordinate** (`agency-organization/design`) — distinct by business-object partition (Workforce Plan vs Organization Structure); the two are peers. |
| Enterprise Governance | Enterprise Governance sets the authority framework (Decision object); OrgDesign implements it operationally as roles, units, and reporting lines. Parent-child. |
| Change Management | Change Management operates change initiatives (Change object); OrgDesign designs the structure that may result from a change. Parent-child in the other direction. |
| Technology Management | Technology Management stewards the technology estate (Technology Estate object); OrgDesign designs the IT organization's structure (e.g., CIO reporting line, IT department shape). Distinct business object. |
| Technology Enablement | Technology Enablement runs technology services (Technology Service object); OrgDesign designs the structure of the function that delivers those services (sourcing model, team topology). Distinct business object. |

### 3.4 Anti-invention test (Section 5)

Change industry → still makes sense. A retail enterprise tomorrow still needs an organizational design capability. A government department tomorrow still needs an organizational design capability. A hospital tomorrow still needs an organizational design capability. **Passes.** Foundation-grade.

### 3.5 Foundation inclusion criteria (A+B+C gate)

- **A. Sensible in ≥3 verticals:** commercial, professional-services, government, healthcare, technology, manufacturing, financial-services, infrastructure, retail = 9 strong; non-profit = moderate. Passes (≥3 strong).
- **B. Works in B2B/B2C/G2C:** all three. Passes.
- **C. Describable without industry-specific domain object:** "structure the enterprise into roles, units, reporting lines, authorities, coordination patterns" — substrate-neutral. Passes.

### 3.6 Evidence (EVIDENCE.md §3)

| Rating | Status | Source |
|---|---|---|
| E0 | met | hypothesis on disk (CAND-036 registered 2026-09-10) |
| E1 | met | ≥1 cited source (SRC-017, SRC-018, SRC-019 cited under CR-DEA-BC-18) |
| E3 | met | independent corroboration across 3 source classes (business-architecture / cross-industry-process / standards-body) per EVIDENCE.md §3 partial-independence threshold |
| **E4** | **met (this CR)** | admission as canonical per EVIDENCE.md §3 admission promotion rule |
| E5 | independent of admission | direct retrieval of SRC-017 Galbraith (2002) chapter structure, SRC-018 APQC PCF element list, SRC-019 ISO 9001:2015 §5.3 normative text — would re-rate to E5 if done (follow-up actions recorded in TER-ORGDESIGN-001) |

**Honest disclosure (per BC-SR-A001 §4 honest-reporting rule):** the EVIDENCE.md §3 E3 threshold is "partial independence" — SRC-017/018/019 are sourced on the strength of documented corpus knowledge with retrieval honesty (`indirect` or summary-level for some; full direct-retrieval pending institutional access). The admission is solid on partial-independence grounds (three fully-independent classes exceeds the partial threshold); direct retrieval of the three primary sources would re-rate to E5 but is independent of the admission decision and tracked separately.

---

## 4. Architectural review (per METHODOLOGY.md §12 gate 2)

### 4.1 ECF mapping defensibility

- Primary `agency-organization/design` — under CR-DEA-BC-13 §A's semantic-center-of-gravity rule, OrgDesign's defining activity is the sustained design of organizational structures, roles, authorities, and coordination patterns; squarely in the design axis of Agency & Organization. **Defensible.**
- Secondaries `agency-organization/conceive` and `agency-organization/build` — conceive covers the diagnostic / re-design conceptualization phase; build covers the operationalization of roles and reporting lines immediately following the structural decision. Both are legitimate secondary placements (CG-003 §5 multiple-contextual-coordinates extension; uses the catalog's documented extension). **Defensible.**

### 4.2 Cell-occupancy effect

`agency-organization/design` cell occupancy: **3 → 4** (Workforce Planning, Workforce Management, Strategy's structural sub-concern, + Organizational Design). Cell remains in the `monopartite` density band (≤6 primary occupants per METHODOLOGY §11). **No conflict.**

### 4.3 Layering boundaries

- OrgDesign is `capability_layer: strategic` — same as Strategy / Strategic Planning / Change Management. **Consistent with peer-capability layer.**
- OrgDesign's business object (Organization Structure) is distinct from all 27 existing business objects. **No layering violation.**
- OrgDesign's 8 related_capabilities entries are all in agency-organization (4), strategy-direction (1), governance-existence (1), enablement-operations (2) — cross-domain, but each is a legitimate peer (no `parent-child` violation since OrgDesign is a peer, not a parent or child of any existing entry).

### 4.4 Specialization defensibility

OrgDesign is foundation-grade per §3.4 anti-invention test; no specialization required at admission time. **Specializations** (per `specialization_boundary`): structural archetypes (functional/divisional/matrix/network/holacratic/ambidextrous); governance patterns (centralized/federated/hub-and-spoke); coordination mechanisms (hierarchies/communities-of-practice/platform teams/cells/squads); enterprise architecture for information flows; HR-organization design for role architecture; IT-organization design for IT org structure; post-merger integration for transition structures. All are legitimate specialization candidates — none absorbed into the entry.

---

## 5. Admission-gate closeout (per METHODOLOGY.md §12 gate 3)

Per `admission-gate-precheck.yaml` v0.7 row for CAND-036: **all gates met**. See the precheck YAML for per-gate reasoning.

- `evidence_ge_E3`: met (E3 confirmed across three independent source classes; E4 admission per EVIDENCE.md §3 promotion rule)
- `classification_capability`: met (CAPABILITY classification; not PROCESS, not ORGANIZATION)
- `enterprise_generality`: met (9 of 10 strong; non-profit moderate; demonstrated per A+B+C gate)
- `durability`: met (recurring discipline since Galbraith 1970s; McKinsey 7-S, Weick's organizing, APQC PCF, ISO 9001 §5.3)
- `implementation_independence`: met (Galbraith Star / McKinsey 7-S / Holacracy / Functional archetypes — all are realizations of the same capability)
- `outcome_identifiable`: met ("structure aligns with strategy and operating context, can be revised deliberately")
- `boundary_defensible`: met (Organization Structure business object distinct from all 27 existing)
- `distinctness`: met (8-pair sweep; all pairs pass by business-object partition)
- `specialization_not_required`: met (foundation-grade per §3.4 anti-invention)
- `ecf_mapping`: met (agency-organization/design primary + conceive/build secondaries; defensible per §4.1)

---

## 6. File inventory

### 6.1 New

- `entities/v1-alpha/dea:capability-organizational-design/dea:capability-organizational-design.yaml` (28th first-order canonical; v1.0.0; 21 top-level fields; all required fields present per `schemas/entity.schema.json`)

### 6.2 Modified (Patch-tier)

- `entities/v1-alpha/dea:capability-strategy/dea:capability-strategy.yaml` (1.1.0 → 1.1.1; related + boundary)
- `entities/v1-alpha/dea:capability-strategic-planning/dea:capability-strategic-planning.yaml` (1.1.0 → 1.1.1; related + boundary)
- `entities/v1-alpha/dea:capability-workforce-management/dea:capability-workforce-management.yaml` (1.1.0 → 1.1.1; related + boundary)
- `entities/v1-alpha/dea:capability-workforce-planning/dea:capability-workforce-planning.yaml` (1.1.0 → 1.1.1; related + boundary; explicit same-cell note)
- `entities/v1-alpha/dea:capability-change-management/dea:capability-change-management.yaml` (1.0.0 → 1.0.1; related + boundary)
- `entities/v1-alpha/dea:capability-technology-management/dea:capability-technology-management.yaml` (1.3.0 → 1.3.1; related + boundary)
- `entities/v1-alpha/dea:capability-technology-enablement/dea:capability-technology-enablement.yaml` (1.0.0 → 1.0.1; related + boundary)
- `entities/v1-alpha/dea:capability-enterprise-governance/dea:capability-enterprise-governance.yaml` (1.0.0 → 1.0.1; related + boundary)

### 6.3 Research-artifact bookkeeping

- `catalog-research/candidates.yaml` v0.4.0 — CAND-036 promoted E3 → E4; canonical true; admitted_by field; promotion_history recorded; pending_promotion cleared
- `catalog-research/evidence-register.yaml` v0.6.0 — TER-ORGDESIGN-001 status `evidence-seeded` → `closed`; candidate_id updated; admitted_by recorded; follow_up_evidence_actions clarified as independent of admission
- `catalog-research/preliminary-ecf-overlay.yaml` v0.4.0 — OrgDesign entry `dea:candidate-orgdesign` → `dea:capability-organizational-design`; confidence low-medium → high; cr field records CR-DEA-BC-14
- `catalog-research/distinctness-sweep.yaml` v0.4.0 — Track A against-list 6 → 8 (added Enterprise Governance and Change Management); `dea:candidate-orgdesign` → `dea:capability-organizational-design`; status sweep-completed-as-evidence-seeded → sweep-completed-as-admitted
- `catalog-research/admission-gate-precheck.yaml` v0.7.0 — CAND-036 `evidence_ge_E3` gap → met; pre_check_notes rewritten; summary clean_except_pending_artifacts 26 → 27, with_gaps 2 → 1
- `catalog-research/INV-ORGDESIGN-v0.2.md` — status closed; carrier_cr extended; date_admitted added
- `catalog-research/INV-ORGDESIGN-v0.1.yaml` — inv_version 0.1.0 → 0.2.0; status closed; ladder_passage canonical met; normalized extended to 8-entry sweep

### 6.4 Catalog index

- `CATALOG.yaml` regenerated — canonical_count 27 → 28; entities_count 30 → 31; last_modified dates updated for 9 entries; OrgDesign entry listed in alphabetical position

### 6.5 Paperwork

- `CHANGELOG.md` — v1-alpha.8 entry (Minor bump)
- `docs/REVIEWS.md` — v1-alpha.8 commentary (BC-SR-A001 §4 closure)
- `change-requests/README.md` — CR-14 row added
- `change-requests/CR-DEA-BC-14-track-a-orgdesign-admission.md` — this document

---

## 7. Local CI gates (verified at branch HEAD before PR)

- schema validator: **28 entries, 0 errors**
- naming lint: **28 entries, 5 pre-existing advisory warnings** (no new warnings introduced by BC-14)
- ECF conformance: **PASS — 28 entries + MCSP view conform to ECF Conformance Gate**
- version discipline: **PASS — 28 entries conform to CR-DEA-BC-05**
- view refs: **PASS**
- catalog index regenerator: **PASS — CATALOG.yaml is current**

(Remote CI to be verified post-push.)

---

## 8. Follow-on (after this CR lands)

- **Tag** `v1-alpha.8` at this CR's merge commit.
- **BC-SR-A001 §4 closure note** added to `submittal-reviews/BC-SR-A001.md` (Track A evidence work closed 2026-09-11).
- **Direct-retrieval actions** for SRC-017/018/019 primaries (independent of admission; tracked separately; would re-rate to E5 if done).
- **Next open queue items (per CR-DEA-BC-13 §B + BC-SR-A001 §5/§6/§7):**
  - Track B (EPM, BC-15) evidence package — research-CR; not yet started
  - Track C (Relationship Mgmt, BC-16) — research-CR; CAND-004 exists; not yet started
  - BC-SR-A001 §7 (Knowledge / Service / Quality / Stakeholder / EAM candidates, P2-P3) — deferred

---

## 9. Refs

- BC-SR-A001 §4 (reviewer P1)
- CR-DEA-BC-13 §B.1 (Track A investigation opened) + §D.1 (ECF overlay hypothesis)
- CR-DEA-BC-18 (research-CR evidence package; SRC-017/018/019 + TER-ORGDESIGN-001 seed)
- METHODOLOGY.md §12 (semantic + architectural + admission-gate review)
- EVIDENCE.md §3 (evidence ratings E0-E5; admission promotion rule E3 → E4)
- docs/VERSIONING.md §1.2 (Patch-tier cross-reference add + boundary-text extension)
- dea-metaframework ADR-ECF-003 (agency-organization/design definition)
- dea-metamodel ADR-015 (agency-organization domain)

---

**Closes**: BC-13 §B.1 Track A queue item CR-DEA-BC-14 (provisional → active); BC-SR-A001 §4 evidence work (open → closed); TER-ORGDESIGN-001 (open → closed); CAND-036 (E3 → E4).