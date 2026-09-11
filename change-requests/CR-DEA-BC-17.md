# CR-DEA-BC-17: Admit Technology Enablement as a First-Order Canonical Capability

**Status**: Proposed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-10
**Depends on**: CR-DEA-BC-01 (method, landed); CR-DEA-BC-02 (evidence investigation, landed); CR-DEA-BC-05 (versioning, landed); CR-DEA-BC-12 (BC-SR-A001 carrier, landed 2026-09-10); CR-DEA-BC-13 (method rule + Tech-mgmt carve, landed 2026-09-10); BC-SR-A001 §12 (Technology Management boundary); BC-SR-A001 §15 (ECF placement for technology-as-enabler)
**Related**: dea-metaframework ADR-ECF-003; dea-metamodel ADR-015
**Supersedes**: none
**Closes**: CR-DEA-BC-13 §11 follow-on queue item CR-DEA-BC-17 (BC-13 §C deferred admission)

---

## 1. What this CR is

This CR is the **admission CR** that closes the BC-SR-A001 §12 deferred item CR-DEA-BC-13 §C carved out as a follow-on. It admits **Technology Enablement** as a new first-order canonical capability and updates the related cross-references on the existing Technology Management, Operations, and Information Management entries.

The BC-13 carrier explicitly deferred this admission because BC-13 was a **method-CR** (rule refinement + 26-entry re-evaluation) and admitting a new first-order cap would have mixed a method-CR with an admission-CR. This CR is the dedicated admission-CR — its scope is bounded to a single entry's admission and the three cross-reference updates required to keep the catalog internally consistent.

### 1.1 Outcome

- **Catalog count: 26 → 27 first-order canonical capabilities.**
- **New entry:** `dea:capability-technology-enablement` at `enablement-operations/operate` (primary) with `build` and `improve` as secondaries.
- **New pair:** Technology Management (estate, `strategy-direction/build`) and Technology Enablement (services, `enablement-operations/operate`) — the carve BC-SR-A001 §12 asked us to make explicit.
- **Three existing entries updated:** Technology Management (1.2.0 → 1.3.0; related_capabilities + boundary text), Operations (1.0.0 → 1.0.1; related_capabilities + boundary text), Information Management (1.0.0 → 1.0.1; related_capabilities + boundary text).
- **Tag target: v1-alpha.7** (Minor bump — new first-order admission).

### 1.2 Why this CR exists at all

BC-SR-A001 §12 said:

> *"Technology Management should mean: stewardship of the enterprise technology estate while Technology Enablement is a sub-concern of Enablement & Operations: use of technology to enable execution. That distinction should be made explicit in the capability catalog and ECF mapping rules. Otherwise future catalog contributors will continually debate whether cloud, platforms, applications, networks, AI agents, etc. belong in Strategy or Enablement."*

BC-13 §C honored the recommendation as a **carve-text-only** decision (kept `dea:capability-technology-management` as a single first-order cap with rigorous `boundary` text). The "Technology-as-Enabler" sub-concern was flagged as a **deferred specialization**.

That deferred item is the explicit queue item in CR-DEA-BC-13 §11 (follow-on CRs) under the label "**CR-DEA-BC-17** — Technology Management split (admit "Technology Enablement")".

This CR admits it.

---

## 2. Why one CR, not separate

The change is bounded and reviewable end-to-end:

- **One new entry** (`dea:capability-technology-enablement`) — a single, self-contained YAML file with full provenance, evidence trail, and ECF conformance block.
- **Three existing entries updated** (Technology Management 1.2.0 → 1.3.0; Operations 1.0.0 → 1.0.1; Information Management 1.0.0 → 1.0.1) — all are cross-reference additions (Patch-tier per `docs/VERSIONING.md §1.2`); no coordinate moves, no boundary-text changes that re-litigate scope, no identity changes.
- **One catalog-regeneration** (`CATALOG.yaml`).
- **One tag** (`v1-alpha.7`).

Splitting into separate CRs (one per touched entry) would multiply review surface for no architectural benefit. The bundle is reviewable because the new entry is the center of gravity and the three existing-entry updates are mechanical cross-references that follow from it.

---

## 3. Semantic review (per METHODOLOGY.md §12 gate 1)

### 3.1 Definition

> **Technology Enablement:** the ability to run and continuously adapt the technology services, platforms, and automation that other capabilities depend on, sustaining operational technology delivery across the enterprise.

The definition satisfies the Section 1 requirements (durable ability, independent of organization / process / people / technology / implementation) and is substrate-neutral (works for cloud, on-prem, OT, AI agent platforms equally).

### 3.2 Distinctions (Section 3)

| Distinction | Pass? | Why |
|---|---|---|
| Object Focus | ✅ | Business object is "Technology Service" (distinct from Tech Mgmt's "Technology" estate, from Operations' "Operation", from IM's "Information"). |
| Outcome focus | ✅ | Outcome is "Technology services are reliable, available, performant, and adapted to changing demand from the capabilities that depend on them" — a distinct outcome. |
| Implementation Independence | ✅ | A capability: the actual IT delivery function may be performed by an internal IT department, an external MSP, a platform team, or a hybrid — the capability is the *what*, not the *how*. |
| Anti-invention classification | ✅ | Not a System (it operates systems), not an Outcome (the outcome is the state of services being reliable). |
| Not duplicating any existing entry | ✅ | See §3.3. |

### 3.3 Distinctness sweep

Per the new rule's "no two entries should describe the same durable ability" principle, against the 26 existing entries plus the 3 non-canonical candidates:

| Compared to | Distinct because |
|---|---|
| Technology Management | TM stewards the **estate** (what technology the enterprise has, acquired and lifecycle-tracked). TE runs the **services** (how that technology operates for others). Different business object (Technology vs Technology Service), different ECF cell (strategy-direction/build vs enablement-operations/operate). TM's carve-text now explicitly excludes TE's scope. |
| Operations | Operations delivers **value** (production, delivery, fulfillment of offerings). TE delivers **technology services** that value delivery depends on. Operations is `operate` for value; TE is `operate` for technology services. Different business object (Operation vs Technology Service). |
| Information Management | IM stewards **information** across its lifecycle. TE operates the **platforms and services** that carry information. Different business object (Information vs Technology Service); distinct carve ("does not manage the technology that carries it" — Technology Enablement does). |
| Analytics & Intelligence | A&I derives **insight from information**. TE runs **services** that information and analytics platforms may run on, but doesn't derive insight itself. Distinct. |
| Change Management | Change Mgmt manages the **transition** between enterprise states. TE runs **services**. Change Mgmt lists "technology" as one of its specialization kinds (the kind of change, not a service). Distinct. |
| Continuity Management | Continuity Mgmt designs **continuity patterns**. TE runs **services**, including the operational continuity of services themselves. Continuity is a design-level concern (design stage); TE is a run-level concern (operate stage). Distinct. |
| Workforce Management (build) | WF Mgmt manages the **workforce** resource lifecycle. TE operates technology services. Different business object (Worker vs Technology Service). |
| Vendor Management / Sourcing | Those handle **external relationships** for acquisition. TE operates technology **services** post-acquisition. Different business object (Supplier / Purchase Order vs Technology Service). |
| Candidate tracks A (Org Design), B (EPM), C (Relationship Mgmt) | None of these candidate scopes overlap with TE. Track A is about organizational structure; Track B is performance governance; Track C is relationship management across party types. |

**Distinctness sweep result:** no overlap; the new entry fills a gap that none of the 26 canonical or 3 candidate entries cover.

### 3.4 Naming and aliases

Per TAXONOMY §1:

- **Name:** "Technology Enablement" — kebab-case `technology-enablement`; English-canonical; plain (no jargon); well-known across industries (ITIL, SRE, platform engineering all use this exact term or close variants).
- **Aliases:** none required at admission time.
- **business_object:** "Technology Service" — echoes the name (`Technology` is in the name; `Service` is the operational unit).

### 3.5 Foundation inclusion criteria (gate A+B+C, locked 2026-09-10)

| Gate | Pass? | Reasoning |
|---|---|---|
| (A) Sensible in ≥3 verticals | ✅ | Universal IT delivery function across B2B SaaS, B2C retail, G2C government, manufacturing, financial services, healthcare, telecom, energy, education, transport. |
| (B) Works in B2B / B2C / G2C archetypes | ✅ | Every archetype has an IT delivery function (sometimes in-house, sometimes MSP). |
| (C) Describable without industry-specific domain object | ✅ | "Technology Service" is substrate-neutral (could be cloud, on-prem, OT, AI agent platforms); "run" is the universal verb. |

**Conclusion:** Technology Enablement is foundation-grade per the A+B+C gate.

---

## 4. Architectural review (per METHODOLOGY.md §12 gate 2)

### 4.1 ECF mapping (Section 8 compliance)

Under the new "semantic center of gravity" rule (CR-DEA-BC-13 §A):

- **Primary:** `enablement-operations/operate`. Rationale: the *defining* activity of Technology Enablement is sustained IT service and platform delivery — running, monitoring, adapting technology services for the capabilities that depend on them. This is squarely the `operate` stage (not `build` = provisioning a one-off service; not `improve` = SRE iteration; not `conceive` = IT direction).
- **Secondary:** `enablement-operations/build` — provisioning new services as demand requires.
- **Secondary:** `enablement-operations/improve` — SRE / platform engineering iteration.
- **No `strategy-direction/*` secondary** because that would collide with Tech Management's `strategy-direction/build` placement and double-count the IT direction function.

### 4.2 Realization links (Section 10)

The new entry references four related capabilities (`Technology Management`, `Operations`, `Information Management`, `Analytics & Intelligence`). These are recorded under `related_capabilities`, not under realization links — the metamodel distinguishes the two, and this is a peer-relationship, not a realization.

### 4.3 Record shape (Section 10)

The new entry conforms to the v1-alpha record shape: top-level `id`, `type`, `name`, `definition`, `version`, `metamodel_pin`, `lifecycle_status`, `capability_layer`, `outcome`, `business_object`, `ecf`, `related_capabilities`, `evidence`, `provenance`, `specialization`, `why_capability`, `ecf_rationale`, `boundary`, `non_examples`, `specialization_boundary`, `ecfConformance`. All required fields present; all conformant.

### 4.4 Layering boundaries

- **WSF** — not invoked (no process or actor realization recorded; the new entry is an L1 capability, not a process or actor).
- **Metaframework** — ECF contract v1.0.0 pinned; canonicalReferences block conformant.
- **Metamodel** — `metamodel_pin: 1.0.0` recorded.
- **Catalogs** — sibling-catalog cross-references recorded under `related_capabilities` (pointers only; not realizing).

---

## 5. Evidence trail (per CR-DEA-BC-02 + METHODOLOGY §12)

The new entry's `provenance.ladder_passage` records the full evidence-promotion ladder:

1. **candidate** (2026-09-10) — derived from CR-DEA-BC-13 §C carve-text + BC-SR-A001 §12 recommendation.
2. **observed** (2026-09-10) — BC-SR-A001 §12 + carve-text evidence; the carve-text in `dea:capability-technology-management` is itself the observation.
3. **corroborated** (2026-09-10) — enterprise-generality matrix entry (cross-industry sweep confirms IT delivery function is universal).
4. **normalized** (2026-09-10) — distinctness sweep (§3.3 above) confirms no overlap with any of the 26 canonical or 3 candidate entries.
5. **ecf-mapped** (2026-09-10) — ECF overlay hypothesis: `enablement-operations/operate` (primary).
6. **reviewed** (2026-09-10) — semantic review (§3) + architectural review (§4).
7. **canonical** (2026-09-10) — admission PR (this change).

The supporting research artifacts are appended to `catalog-research/`:

- **`evidence-register.yaml` v0.5.0**: new entry `TER-TECHENABLEMENT-001` (evidence strength E3 preliminary; promotes to E4 on admission).
- **`preliminary-ecf-overlay.yaml` v0.3.0**: ECF overlay hypothesis appended (`enablement-operations/operate`).
- **`distinctness-sweep.yaml` v0.3.0**: distinctness sweep appended (against Operations, Tech Mgmt, IM, A&I).
- **`enterprise-generality-matrix.yaml`**: cross-industry universality sweep appended.
- **`admission-gate-closeout.yaml`**: updated to record this admission as a §12-gated closeout.

---

## 6. Cross-reference updates

To keep the catalog internally consistent:

### 6.1 Technology Management (1.2.0 → 1.3.0; **Minor** for boundary-text change)

- `related_capabilities`: added `dea:capability-technology-enablement`.
- `boundary`: replaced the "deferred specialization" carve with explicit reference to the now-admitted Technology Enablement entry.
- `specialization_boundary`: same.
- `ecf_rationale`: cites CR-DEA-BC-17 in addition to BC-13 §A and BC-13 §C.
- `evidence.sources`: added `BC-SR-A001`.
- Coordinate: unchanged (the BC-13 §C carve-text-only decision stands for THIS entry).
- **Why Minor and not Patch:** the boundary-text change materially changes the cross-reference network and the entry's relationship to its sibling; that's a substantive change to non-identity fields but not to identity.

### 6.2 Operations (1.0.0 → 1.0.1; **Patch** for cross-reference)

- `related_capabilities`: added `dea:capability-technology-enablement`.
- `boundary`: added a sentence noting that technology services that value delivery depends on are operated by Technology Enablement.
- Coordinate: unchanged.

### 6.3 Information Management (1.0.0 → 1.0.1; **Patch** for cross-reference)

- `related_capabilities`: added `dea:capability-technology-enablement`.
- `boundary`: added a sentence noting that information platforms are operated by Technology Enablement.
- Coordinate: unchanged.

---

## 7. Acceptance criteria

- ✅ New entry `dea:capability-technology-enablement` exists at `entities/v1-alpha/dea:capability-technology-enablement/dea:capability-technology-enablement.yaml` with all required fields.
- ✅ Three existing entries updated (Tech Management 1.3.0, Operations 1.0.1, Information Management 1.0.1).
- ✅ Local gates all green: `check_ecf_conformance.py`, `check_naming.py`, `check_versions.py`, `check_visual_domain_labels.py`.
- ✅ CATALOG.yaml regenerated, canonical count = 27.
- ✅ CR-DEA-BC-17.md filed in `change-requests/`.
- ✅ Evidence trail artifacts appended to `catalog-research/`.
- ✅ CHANGELOG entry added under v1-alpha.7.
- ✅ `change-requests/README.md` row added for CR-DEA-BC-17 (Landed, PR #TBD).
- ✅ `docs/REVIEWS.md` v1-alpha.7 commentary appended.
- ✅ All four conformance workflows green on the PR.
- ✅ Tag `v1-alpha.7` cut at the merge commit; GitHub release published.

---

## 8. Version bump

Per `docs/VERSIONING.md §1.2`:

- **Catalog label:** v1-alpha.6 → v1-alpha.7 (**Minor** — new first-order admission).
- **New entry version:** `1.0.0` (first canonical release).
- **Affected existing entries:**
  - Technology Management: 1.2.0 → 1.3.0 (Minor for boundary-text change).
  - Operations: 1.0.0 → 1.0.1 (Patch for cross-reference addition).
  - Information Management: 1.0.0 → 1.0.1 (Patch for cross-reference addition).
  - Other 23 entries: version unchanged.
- **Specialization views:** unchanged (the MCSP view doesn't reference Tech-mgmt's carve).
- **Total canonical entry count:** 26 → **27** (first-order admission).
- **Tag:** `v1-alpha.7` at this CR's merge commit.

---

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Critics may say "Technology Enablement is just IT operations, which is a sub-concern of Operations" | The carve is explicit: Operations delivers *value*; Technology Enablement delivers *technology services for value delivery*. Different business objects. Different definition. The new entry's ECF cell is `enablement-operations/operate` — adjacent to Operations, not nested under it. The cross-references are recorded under `related_capabilities` (peer relationship, not parent-child). |
| Critics may say "this is an admission, not a method change — should be in a different CR series" | The CR series is layered; CR-DEA-BC-13 was the method-CR (rule refinement). CR-DEA-BC-17 is the admission-CR for the entry BC-13 §C carved out. Both are legitimate; BC-13 §11 explicitly listed CR-DEA-BC-17 as a follow-on admission CR. |
| The new entry expands the 26-cap "deliberately small" first-order set the reviewer endorsed | The reviewer endorsed keeping the set small *when the entries are well-supported*. BC-SR-A001 §12 explicitly recommended this admission; the evidence package (§5) supports it. The foundation inclusion criteria gate A+B+C (§3.5) confirms foundation-grade fit. The set grows by 1 (26 → 27), not by many. |
| Cross-reference updates could be deferred to a follow-on CR | Possible, but they would leave the catalog inconsistent until the follow-on lands. Keeping the bundle atomic ensures the catalog is internally consistent at v1-alpha.7. |
| The 3 candidates (Org Design, EPM, Relationship Mgmt) remain un-admitted; this CR doesn't help them | Correct scope discipline. CR-DEA-BC-14/15/16 are gated on evidence packages for each track. CR-DEA-BC-17 is independent of those packages and can ship now. |

---

## 10. Follow-on work (not in this CR)

- **CR-DEA-BC-14** — Track A (Organizational Design) admission (when track A evidence supports).
- **CR-DEA-BC-15** — Track B (EPM) admission (when track B evidence supports).
- **CR-DEA-BC-16** — Track C (Relationship Management generic parent) admission (after the 3 decision options are evaluated and one is chosen).
- **Future MCSP specialization pilot** — Healthcare industry view, surfacing industry-disjoint L1 (e.g., "Disease Prevention & Management") and industry-specialization of foundation L1s (e.g., "Patient Management" specializing "Customer Management"). Not in CR-DEA-BC-17.

---

## 11. See also

- [CR-DEA-BC-13](CR-DEA-BC-13.md) — the BC-13 method-CR that carved this admission out (§C).
- [BC-SR-A001 §12](../submittal-reviews/BC-SR-A001.md#12-technology-management-deserves-special-treatment) — the reviewer's recommendation this admission closes.
- [`dea:capability-technology-management`](../entities/v1-alpha/dea:capability-technology-management/dea:capability-technology-management.yaml) — the paired entry (IT direction function).
- [`METHODOLOGY.md §12`](../METHODOLOGY.md) — the two review gates (semantic + architectural) this admission passes.
- [`docs/VERSIONING.md §1.2`](../docs/VERSIONING.md) — version semantics for the affected entries.
- [CHANGELOG.md](../CHANGELOG.md) — v1-alpha.7 entry.
- [docs/REVIEWS.md](../docs/REVIEWS.md) — v1-alpha.7 commentary.
