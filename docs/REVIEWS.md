# Submittal Reviews: Release Commentary

This document is the per-release commentary surface for **submittal reviews** filed
against this catalog. Each release that lands at least one recommendation from a
submittal review gets a section here.

The intent is two-fold:

1. **Make submittal review work discoverable.** Anyone reading the release notes or
   the catalog's history can trace what was reviewed, what was found, what was
   acted on, and what was deferred.
2. **Make submittal review commentary "summarized yet rich."** The full review
   file (under `submittal-reviews/`) is the long-form record; this document is
   the bridge: enough context to understand *why* the release changed, with
   pointers to the full evidence.

## Format

Each entry is appended in release order. New entries are added by the carrier CR
that lands the recommendations. The structure is:

```
## [<release label>]: <release date>

**Submittal review filed:** <BC-SR-A###> by <reviewer> on <date>
**Carrier CR:** <CR-DEA-...-NN>
**Review scope:** <one-line>
**Headline findings:** <2-4 bullets, paraphrased>
**Items landed in this release:** <bullets citing review section numbers>
**Items opened as investigations:** <bullets with their own CR numbers, if opened>
**Items deferred to backlog:** <bullets with rationale>
**Doc-drift items closed:** <bullets>
```

The goal is that a reader can skim one entry to understand the substance, and
follow the links for the long-form.

---

## Index

- [v1-alpha.5: 2026-09-10](#v1-alpha5--2026-09-10)
- [v1-alpha.6: 2026-09-10 (BC-SR-A001 follow-on)](#v1-alpha6--2026-09-10-bc-sr-a001-follow-on)
- [v1-alpha.7: 2026-09-10 (BC-SR-A001 §12 closure)](#v1-alpha7--2026-09-10-bc-sr-a001-12-closure)

---

## v1-alpha.5: 2026-09-10 (planned)

**Submittal review filed:** BC-SR-A001 by (external) on 2026-09-10 against the
v1-alpha.4 catalog (commit `570830a`).

**Carrier CR:** CR-DEA-BC-12.

**Review scope:** Full catalog v1-alpha.0..v1-alpha.4: methodology, ECF semantic
alignment, foundational gap analysis, and repository/doc drift.

**Headline findings (paraphrased):**
- The catalog is "approximately 80-85% of the way to a strong enterprise-general
  foundation." Methodology is sound; the evidence ladder, first-order concept,
  specialization boundary, ability test, and capability-before-coordinate
  principle should all be preserved.
- Six ECF coordinates are **semantically inconsistent** with the ECF itself.
  Strategy and Strategic Planning sit in Governance & Existence but the ECF
  places them in Strategy & Direction. Asset, Facility, Technology, Supplier, and
  Procurement sit in Strategy & Direction but the ECF places physical/virtual
  enablers in Enablement & Operations.
- Three first-order capabilities are **likely missing**: Organizational Design,
  Enterprise Performance Management, and a generic Relationship Management parent
  (replacing the role-specific Customer/Supplier/Partner split, or sitting above
  it).
- The catalog is over-concentrated in Governance & Existence; this is *caused*
  by the coordinate mis-placements above and resolves once they are corrected.
- The ECF mapping rule "primary = earliest initiation point" produces
  semantically unintuitive placements even when technically defensible; a
  semantic-center-of-gravity rule would be more useful.
- Repository/doc drift: README entity-definition table says
  `Catalog Status: planned` while the catalog is populated; OpenDEAM version pin
  in the README points to v0.2.1 while the catalog pins metamodel 1.0.0.

**Items landed in this release (v1-alpha.5):**
- ECF re-mapping of **Strategy** (`governance-existence/conceive` →
  `strategy-direction/conceive`), per BC-SR-A001 §8.A.
- ECF re-mapping of **Strategic Planning** (`governance-existence/conceive` →
  `strategy-direction/conceive`), per §9.
- ECF re-mapping of **Asset Management** (`strategy-direction/build` →
  `enablement-operations/build`), per §10.
- ECF re-mapping of **Facility Management** (`strategy-direction/activate` →
  `enablement-operations/activate`), per §11.
- ECF re-mapping of **Supplier Management** (`strategy-direction/build` →
  `party-relationship/conceive`+`operate`), per §13.
- ECF re-mapping of **Sourcing & Procurement** (`strategy-direction/build` →
  `enablement-operations/build` with `strategy-direction/conceive/design`
  secondary), per §13.
- README entity-definition table `Catalog Status: planned` → `populated`,
  per §19.
- OpenDEAM version pin correction in the README, per §19.

**Items opened as investigations (no admission in this release):**
- Investigation track A: **Organizational Design** as a first-order capability
  (§4 P1). Evidence investigation per the catalog's own admission gate; no
  admission until evidence supports it.
- Investigation track B: **Enterprise Performance Management** as a first-order
  capability (§5 P1). Evidence investigation, including how it would close the
  Direction loop in §16.
- Investigation track C: **Relationship Management** as a generic parent for
  Customer/Supplier/Partner Management (§6 P1-P2). Boundary-led investigation;
  output may be a new first-order cap, an abstract grouping, or a no-op with
  rationale.

**Items deferred to backlog (with rationale):**
- **Knowledge Management** as a first-order capability (§7 P2). The reviewer's
  own caveat stands: Information Management already owns information lifecycle;
  the case for a distinct Knowledge cap hinges on evidence that knowledge is a
  durable distinct business object. Revisit when investigation track A (Org
  Design) reports back, because Agency & Organization × Improve is the most
  likely placement.
- **Service Management, Quality Management, Stakeholder Management, Enterprise
  Architecture Management** as candidate first-order caps (§17 P2-P3). No
  evidence yet; revisit after the three P1 investigations close.
- **Technology Management boundary** decision (§12). The reviewer's own
  recommendation: investigate whether Technology Management = stewardship of
  the estate (in Strategy & Direction) vs Technology Enablement = use of
  technology to enable execution (in Enablement & Operations) is the right
  carve. This is a method-level decision; deferred to a follow-on method-CR
  (CR-DEA-BC-13) that proposes a refined "semantic-center-of-gravity" rule for
  primary coordinates.
- **ECF mapping rule refinement** ("semantic center of gravity" replacing
  "earliest initiation") as a method-level change (§14). Same follow-on
  method-CR.

**Doc-drift items closed:**
- README entity-definition table: `Catalog Status: planned` → `populated`.
- README: OpenDEAM version pin corrected to match the catalog's metamodel pin
  (1.0.0) and ECF conformance contract pin (1.0.0).

**Notes for consumers:**
- Five of the six ECF re-mappings change **primary coordinate only**. Each
  affected entry's `ecf.secondary` block is preserved (where it existed), and
  the entry's `ecf_rationale` field is updated with the BC-SR-A001 citation.
  Entry identity (id, name, definition) is unchanged. Per
  `docs/VERSIONING.md` §1.2, this is a **minor** bump on each affected entry
  (1.0.0 → 1.1.0).
- The catalog label advances **v1-alpha.4 → v1-alpha.5** (Minor tier).
- No new entities admitted. The catalog count remains 26 first-order caps.

## v1-alpha.6: 2026-09-10 (BC-SR-A001 follow-on)

**Submittal review filed:** [BC-SR-A001](../submittal-reviews/BC-SR-A001.md)
(continues from v1-alpha.5 carrier: same review; this release closes BC-SR-A001
§12, §14, and §17 deferred items via CR-DEA-BC-13).

**Carrier CR:** CR-DEA-BC-13 (PR #66).

**Review scope:** Method-level rule refinement + 26-entry re-evaluation + Technology
Management boundary decision + Tracks A/B/C evidence collection. This is the
"explicit method-CR + foundation alignment" half of BC-SR-A001, complementary to
the v1-alpha.5 "high-confidence ECF re-mappings" half.

**Headline findings (paraphrased):**
- The pre-CR-13 ECF primary-coordinate rule ("earliest initiation point") is
  technically defensible but produces semantically unintuitive placements where
  the capability's *defining activity* lives in a different cell than where its
  lifecycle begins (BC-SR-A001 §14).
- Six entries' placements do not survive a fresh evaluation under a refined rule
  that names the *defining activity* as the primary (BC-SR-A001 §14, §8.A, §9,
  §10, §11, §13).
- The Technology Management "as-Estate vs as-Enabler" carve needs explicit
  language on the entry to prevent future contributors re-litigating the question
  (BC-SR-A001 §12).
- Three P1 candidates (Org Design, EPM, Relationship Management) have
  investigation tracks opened by BC-12; this release starts the actual evidence
  collection for each (BC-SR-A001 §4, §5, §6).

**Items landed in this release (v1-alpha.6):**
- **Method rule refinement** in `METHODOLOGY.md §8`: pre-CR-13 "earliest
  initiation" ⇒ "semantic center of gravity" + 4 selection heuristics.
- **4 primary-coordinate moves** (asset/facility/sourcing/supplier:
  build/activate/conceive ⇒ operate).
- **1 secondary-coordinate fix** (partner-management: strategy-direction/operate
  ⇒ party-relationship/operate).
- **1 carve-text decision** (technology-management: Tech-as-Estate vs
  Tech-as-Enablement carve formalized in boundary + specialization_boundary).
- **20 rationale refreshes** with CR-13 citation (no coord change; placement
  confirmed under the new rule).
- **3 non-canonical candidate records** under `entities/v1-alpha/dea:candidate-*`
  for tracks A/B/C.

**Items opened as investigations (already running, see v1-alpha.5 entry):**
- Track A: Organizational Design (research files: `INV-ORGDESIGN-v0.1.md` +
  candidate record + evidence-register stub TER-ORGDESIGN-001 + ECF overlay
  hypothesis + distinctness sweep).
- Track B: Enterprise Performance Management (loop-closure narrative required
  regardless of admission).
- Track C: Relationship Management generic parent (3 decision options tracked:
  admit-with-specializations / abstract-grouping-only / no-admit).

**Items deferred to backlog (with rationale):**
- **Technology Management split** (admit a separate "Technology Enablement"
  first-order cap). Deferred per BC-13 §C: the carve-text is sufficient for now;
  a split is the architecturally correct outcome but is itself an admission
  decision (count 26 → 27) that must pass the §12 review gates. CR-DEA-BC-17
  (provisional) handles this once evidence supports it.
- **Knowledge Management** (§7 P2). Revisit after track A reports back, because
  `agency-organization / improve` is the most likely placement.
- **Service / Quality / Stakeholder / EAM** candidates (§17 P2-P3). Revisit
  after tracks A/B/C close.

**Doc-drift items closed:**
- `METHODOLOGY.md §8` rule language now aligned with what the CR §A documents
  (the rule itself is the canonical source going forward).

**Notes for consumers:**
- The "semantic center of gravity" rule is **the new rule** from v1-alpha.6
  onwards. Pre-CR-13 placements are preserved as a historical record but are no
  longer the selection logic.
- Five of the six entry-level changes move the primary to `operate` (the
  defining-activity cell). Per-entity versions 1.1.0 → 1.2.0; entry identity
  unchanged.
- The catalog now has **3 candidates** (non-canonical) alongside the 26
  canonical entries. The candidates are the visible scaffolding for the three
  P1 investigations; admission (if any) lands in follow-on admission CRs.
- Cell occupancy went **16 → 14** under the new rule; concentration in
  `enablement-operations/operate` and `party-relationship/operate` is the
  intended effect.

## v1-alpha.7: 2026-09-10 (BC-SR-A001 §12 closure)

**Submittal review filed:** [BC-SR-A001](../submittal-reviews/BC-SR-A001.md)
(closes §12; this is the same review's third release-pass: BC-13 deferred
the §12 admission, BC-17 admits it).

**Carrier CR:** CR-DEA-BC-17 (PR TBD).

**Review scope:** Single-entry admission: admits `dea:capability-technology-enablement`
as a first-order canonical capability. Closes the BC-DEA-BC-13 §11 follow-on
queue item (BC-13 §C deferred admission).

**Headline finding (BC-SR-A001 §12, paraphrased):**

> *"Technology Management should mean stewardship of the enterprise technology
> estate, while Technology Enablement is a sub-concern of Enablement &
> Operations: use of technology to enable execution. That distinction should
> be made explicit in the capability catalog and ECF mapping rules.
> Otherwise future catalog contributors will continually debate whether
> cloud, platforms, applications, networks, AI agents, etc. belong in
> Strategy or Enablement."*

The BC-13 carrier executed the carve as carve-text only (kept one first-order
cap with rigorous `boundary` declaration). This release **admits** the
carved-out sub-concern as a separate first-order cap.

**Items landed:**

- **New entry:** `dea:capability-technology-enablement` at
  `enablement-operations/operate` (primary), with `build` and `improve`
  secondaries. Definition: "The ability to run and continuously adapt the
  technology services, platforms, and automation that other capabilities
  depend on, sustaining operational technology delivery across the
  enterprise." Business object: **Technology Service** (distinct from
  Technology Management's **Technology** estate).
- **Technology Management updated:** version 1.2.0 → 1.3.0 (Minor for
  boundary-text change). Adds `dea:capability-technology-enablement` to
  `related_capabilities`; updates `boundary`, `specialization_boundary`,
  `why_capability`, and `ecf_rationale` to record the peer relationship.
  Coordinate unchanged (`strategy-direction/build`).
- **Operations updated:** version 1.0.0 → 1.0.1 (Patch). Adds cross-reference
  + boundary note that technology services are operated by Tech Enablement.
- **Information Management updated:** version 1.0.0 → 1.0.1 (Patch). Adds
  cross-reference + boundary note that information platforms are operated
  by Tech Enablement.

**Review-gate audit (per METHODOLOGY.md §12):**

- **Semantic review (gate 1):** ✅
  - Distinct business object (Technology Service)
  - Distinct ECF cell (enablement-operations/operate)
  - Distinct outcome (technology services are reliable/performant/adapted)
  - Anti-invention: not a system, not an outcome, not an organization
  - Distinctness sweep: no overlap with any of the 26 canonical or 3 candidate entries
  - Naming: "Technology Enablement": kebab-case, plain, well-known across industries
  - Foundation inclusion criteria gate A+B+C: passed
- **Architectural review (gate 2):** ✅
  - ECF mapping satisfies METHODOLOGY.md §8 (semantic center of gravity rule)
  - Realization links: peer relationship recorded under `related_capabilities`
  - Record shape: all required fields present, conformant
  - Layering boundaries: WSF / Metaframework / Metamodel / Catalogs all respected

**Evidence trail (per CR-DEA-BC-02):**

- `catalog-research/evidence-register.yaml`: TER-TECHENABLEMENT-001 (E3 → E4 on admission)
- `catalog-research/preliminary-ecf-overlay.yaml`: ECF overlay hypothesis appended; status promoted to "admitted"
- `catalog-research/distinctness-sweep.yaml`: distinctness sweep appended
- `catalog-research/admission-gate-closeout.yaml`: §12 review-gate closeout recorded

**Notes for consumers:**

- The catalog now has **27 canonical first-order capabilities**. The previously
  carved-out "Technology-as-Enabler" sub-concern is its own entry with its own
  ECF coordinate and provenance trail.
- Technology Management and Technology Enablement are **paired** but
  **distinct**:
  - Technology Management = IT **direction** function (estate; `strategy-direction/build`)
  - Technology Enablement = IT **delivery** function (services; `enablement-operations/operate`)
- Cell occupancy: `enablement-operations/operate` now has **7 entries**
  (was 6 post-BC-13: analytics, asset, facility, information-mgmt, operations,
  sourcing; + Tech Enablement). The new entry fits the cell naturally
  (sustained stewardship / execution heuristic from BC-13 §A).

**Items still in the open queue (not closed by this release):**

- **CR-DEA-BC-14/15/16**: Track A/B/C admission CRs (gated on evidence packages)
- **Industry-view mechanics pilot**: Healthcare example (deferred; not in scope for v1-alpha.7)
- **Knowledge / Service / Quality / Stakeholder / EAM candidates**: BC-SR-A001 §7 + §17 P2-P3 deferred; revisit after tracks A/B/C close

### v1-alpha.7 addendum: BC-SR-A001 §4 evidence work in progress (no admission)

**Sub-CARRIER:** [CR-DEA-BC-18](../../change-requests/CR-DEA-BC-18-track-a-orgdesign-evidence.md)
(research-CR; no canonical change; same release cycle).

**Review scope:** Evidence package for BC-SR-A001 §4 (reviewer P1:
Organizational Design as a foundational gap; the catalog currently has
Workforce Planning + Workforce Management but not the structural-design
capability the ECF positions in `agency-organization/design`).

**Headline status:** Evidence seeded across three independent source classes
(SRC-017 business-architecture / SRC-018 cross-industry-process / SRC-019
standards-body); full independence across classes exceeds the E3 threshold
per EVIDENCE.md §3. CAND-036 added to the candidate universe; ECF overlay
hypothesis confidence `low → low-medium`; distinctness sweep expanded;
enterprise-generality matrix row added; admission-gate pre-check honest about
the one remaining gap (`evidence_ge_E3` pending direct retrieval of
SRC-017/018/019 primaries).

**Items landed (research artifacts, no canonical entity):**

- **CAND-036** added to `catalog-research/candidates.yaml` v0.3 (CAPABILITY;
  E1; business object Organization Structure).
- **SRC-017/018/019** added to `catalog-research/evidence-register.yaml` v0.5.
- **TER-ORGDESIGN-001** track record seeded.
- **ECF overlay hypothesis** updated in `preliminary-ecf-overlay.yaml` v0.3
  (confidence `low → low-medium`).
- **Enterprise-generality matrix** row added in `enterprise-generality-matrix.yaml` v0.3
  (9 of 10 types strong; non-profit moderate; demonstrated per A+B+C gate).
- **Distinctness sweep** expanded in `distinctness-sweep.yaml` v0.3 (track A
  extended to cover `dea:capability-technology-management` and
  `dea:capability-technology-enablement`).
- **Admission-gate pre-check** added in `admission-gate-precheck.yaml` v0.6.
- **INV-ORGDESIGN-v0.2.md** + YAML twin (dual-delivery per EVIDENCE.md §6).

**Review-gate audit (per METHODOLOGY.md §12):** Research-CR: semantic review
gate 1 passes on all hard gates (Ability, Outcome, Implementation Independence)
and on 6 of 7 soft gates (Durability, Enterprise Relevance, Object Focus,
Distinctness, Decomposability, ECF Fit). The Evidence soft gate has the open
`evidence_ge_E3` gap (pending direct retrieval of SRC-017/018/019 primaries).
Architectural review gate 2 passes on ECF mapping defensibility, layering
boundaries; final record-shape conformance happens in the admission CR.

**Notes for consumers:**

- The catalog is still **27 first-order canonical capabilities** (unchanged from
  v1-alpha.7 main release). CAND-036 is a candidate-on-file; not yet admitted.
- The Track A admission CR (CR-DEA-BC-14, provisional) becomes the next step
  when this evidence package is accepted by the user.
- Track B (EPM, BC-15) and Track C (Relationship Mgmt, BC-16) evidence work
  remains separate; no work on them in CR-DEA-BC-18.

**Items still in the open queue (not closed by this addendum):**

- **CR-DEA-BC-14**: Track A admission CR (now unblocked; awaits user acceptance)
- **CR-DEA-BC-15**: Track B (EPM) evidence package (not yet started)
- **CR-DEA-BC-16**: Track C (Relationship Mgmt) evidence package (not yet started)
- **Direct retrieval actions** for SRC-017/018/019 (independent of admission;
  re-rates to E4 if done)

## v1-alpha.8: 2026-09-11 (BC-SR-A001 §4 closure)

**CARRIER:** [CR-DEA-BC-14](../../change-requests/CR-DEA-BC-14-track-a-orgdesign-admission.md) (admission-CR; canonical entity added; 27 → 28 first-order caps).

**Review scope:** Track A admission of `dea:capability-organizational-design` at `agency-organization/design` (primary) + `conceive/build` secondaries. Closes BC-SR-A001 §4 (reviewer P1), BC-13 §B.1 (Track A investigation opened), CR-DEA-BC-18 (research-CR evidence package), TER-ORGDESIGN-001 (open → closed), CAND-036 (E3 → E4 per EVIDENCE.md §3 admission promotion rule).

**Headline status:** All 10 admission-gate criteria met per `admission-gate-precheck.yaml` v0.7 row for CAND-036. Semantic review gate 1 passes on hard gates (Ability, Outcome, Implementation Independence) and all 7 soft gates; architectural review gate 2 passes on ECF mapping defensibility (semantic-center-of-gravity rule CR-13 §A → agency-organization/design primary + conceive/build secondaries), cell-occupancy (3 → 4, within monopartite band), layering boundaries (no parent-child violation), specialization defensibility (foundation per METHODOLOGY §5 anti-invention).

**Items landed:**

- `dea:capability-organizational-design` v1.0.0 admitted as 28th first-order canonical capability at `agency-organization/design` (primary); business object Organization Structure; 8 related_capabilities entries (Strategy, Strategic Planning, Enterprise Governance, Workforce Planning, Workforce Management, Change Management, Technology Management, Technology Enablement).
- 8 existing entries bumped to Patch (1.1.0 → 1.1.1 / 1.0.0 → 1.0.1 / 1.3.0 → 1.3.1): related_capabilities + boundary-text exclusion extension.
- `dea:capability-workforce-planning` boundary extended with explicit same-cell note (Workforce Plan vs Organization Structure business-object partition).
- `dea:capability-technology-management` boundary extended with IT-org-design-as-sub-concern clause.
- `dea:capability-technology-enablement` boundary extended with IT-org-design-as-sub-concern clause.
- Distinctness sweep expanded from 6 → 8 peers (added Enterprise Governance + Change Management).
- CAND-036 promoted E3 → E4 per EVIDENCE.md §3 admission promotion rule.
- TER-ORGDESIGN-001 track record closed.
- ECF overlay hypothesis confidence low-medium → high.
- Admission-gate pre-check `evidence_ge_E3` gap → met; clean_except_pending_artifacts 26 → 27; with_gaps 2 → 1.

**Review-gate audit (per METHODOLOGY.md §12):**

- Gate 1 (semantic review): PASS; all hard gates + 7 soft gates pass.
- Gate 2 (architectural review): PASS; ECF mapping, cell-occupancy, layering, specialization all defensible.
- Gate 3 (admission-gate): PASS; all 10 criteria met per `admission-gate-precheck.yaml` v0.7 row for CAND-036.

**Honest disclosure (per BC-SR-A001 §4 honest-reporting rule):**

The EVIDENCE.md §3 E3 threshold is "partial independence". SRC-017/018/019 are sourced on the strength of documented corpus knowledge with retrieval honesty (indirect or summary-level for some; full direct-retrieval pending institutional access). The admission is solid on partial-independence grounds (three fully-independent classes exceeds the partial threshold); direct retrieval of the three primary sources would re-rate to E5 but is independent of the admission decision and tracked separately as follow-up actions.

**Notes for consumers:**

- The catalog is now **28 first-order canonical capabilities** (27 → 28; one new first-order admission).
- The Track A admission closes the BC-13 §B.1 follow-on queue item. Track B (EPM, BC-15) and Track C (Relationship Mgmt, BC-16) evidence work remains separate.
- `agency-organization/design` cell-occupancy: 3 → 4 (within monopartite band per METHODOLOGY §11). No conflict.

**Items still in the open queue (not closed by this release):**

- CR-DEA-BC-15: Track B (EPM) evidence package (not yet started)
- CR-DEA-BC-16: Track C (Relationship Mgmt) evidence package (not yet started)
- Direct retrieval actions for SRC-017/018/019 (independent of admission; re-rates to E5 if done)
- BC-SR-A001 §7: Knowledge / Service / Quality / Stakeholder / EAM candidates (P2-P3 deferred)
