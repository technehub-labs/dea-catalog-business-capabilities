# CR-DEA-BC-13: ECF Primary-Coordinate Rule Refinement — Semantic Center of Gravity + 26-Entry Re-Evaluation + Technology Management Boundary Decision + Tracks A/B/C Evidence Collection

**Status**: Proposed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-10
**Depends on**: CR-DEA-BC-01 (method, landed); CR-DEA-BC-02 (evidence investigation, landed); CR-DEA-BC-05 (versioning, landed); CR-DEA-BC-12 (BC-SR-A001 carrier, landed 2026-09-10); BC-SR-A001 §14 (rule refinement); BC-SR-A001 §12 (Technology Management boundary)
**Related**: dea-metaframework ADR-ECF-003 (Domain/Stage Orthogonality); dea-metamodel ADR-015
**Supersedes**: none

## 1. What this CR is

This CR is the **method-level refinement** carrier for the ECF primary-coordinate rule, and the **scope bundle** that lands four workstreams in one atomic PR:

1. **§A — Method rule refinement.** Codify the new ECF primary-coordinate rule ("semantic center of gravity") in `METHODOLOGY.md §8`. The pre-CR-13 rule ("earliest initiation point") is preserved as a historical record but is no longer the canonical selection logic.
2. **§B — 26-entry re-evaluation.** Apply the new rule to all 26 canonical entries. Surface which placements survive (21) and which move (4 + 1 carve-only). This satisfies the user's standing request: a single rule applied uniformly across the foundation.
3. **§C — Technology Management boundary decision.** Per BC-SR-A001 §12, formalize the carve between "Technology as Estate" (strategy-direction/build) and "Technology as Enabler" (enablement-operations/operate). This CR's chosen outcome is **carve-text only** — keep `dea:capability-technology-management` as a single first-order entry with a rigorous `boundary` declaration. The "Technology-as-Enabler" sub-concern is flagged as a deferred specialization that a future CR may admit.
4. **§D — Investigation-track evidence collection (A, B, C).** Start the actual evidence work for the three investigation tracks opened by CR-DEA-BC-12. This CR produces the candidate records, evidence register entries, ECF overlay hypotheses, and distinctness sweeps. **No admission** in this CR — admission remains gated on `METHODOLOGY.md §12` review gates per CR-DEA-BC-12's stance.

This is a single-PR scope per the user's CR-13 design decision (Q1: retrospective re-evaluation; Q2: include Technology Management; Q3: start evidence collection for all three tracks).

## 2. Why one CR, not four

Per the user's CR-13 design decision, this is one bundled CR. The four workstreams are coupled:

- §A is meaningless without §B applying it.
- §C cannot be decided in isolation from §B's application to Technology Management under the new rule.
- §D's candidate records need to be authored under §A's new rule; doing them under the old rule would require rework.

Splitting into four CRs (BC-13a/13b/13c/13d) would multiply review surface for no architectural benefit. The bundle is reviewable end-to-end because all four pieces share the same v1-alpha.6 version bump envelope.

## 3. Method rule refinement (§A)

### §3.1 The new rule

> **The primary coordinate marks the capability's semantic center of gravity: the ECF cell where the capability's defining work is sustained, not where its lifecycle begins.**

Codified at `METHODOLOGY.md §8.2` (replaces pre-CR-13 "earliest initiation").

### §3.2 Selection heuristics

Apply in order; first decisive wins. A capability's *defining activity* is what the capability *is*; the selection picks the cell carrying the largest share of the defining activity.

| # | Heuristic | Primary cell | Examples |
|---|---|---|---|
| 1 | Sustained stewardship / execution | `operate` in the capability's domain | Operations, Customer Management, Analytics |
| 2 | Posture / constitutive decision | `conceive` in the capability's domain | Strategy, Risk Management, Financial Stewardship |
| 3 | Designed artifact / pattern / build phase | `design` or `build` in the capability's domain | Continuity Management (design), Workforce Planning (design), Workforce Management (build) |
| 4 | Activation / enforcement | `activate` in the capability's domain | Regulation Management (activate) |

When multiple cells share sustained activity, the cell with the largest share wins the primary slot; the rest move to `secondary`.

### §3.3 Why this is the right rule

- **Pre-CR-13 rule ("earliest initiation point")** maps the primary to the first lifecycle stage the capability enters. This produces semantically unintuitive placements where the *defining* activity is in a different cell (e.g. Asset Management placed at `build` because the asset is acquired there, but the defining activity — stewardship of the asset base — is sustained at `operate`).
- **New rule ("semantic center of gravity")** maps the primary to the cell where the capability's defining work is sustained. The lifecycle still participates honestly via `secondary` coordinates; the primary simply names where the capability *is*.
- **Backward compatibility:** the four entries that move (§B) preserve all their `secondary` coordinates. No entry's identity (id, name, definition, business_object, outcome) changes. The moves are coordinate-only.
- **Foundation-purity discipline:** the new rule makes the catalog more honest under the ECF's own framing — the ECF's Domain axis names the *what*, the Stage axis names the *where in the lifecycle*; "semantic center of gravity" picks the cell that is *most this capability*, not the cell that *sees it first*.

### §3.4 What does NOT change

- ECF coordinate *identifier* rules (PascalCase domain, camelCase identifier, multiple contextual coordinates, held-unmapped) — unchanged.
- The "ECF primary + honest secondaries" rule — unchanged.
- The catalog's stance that ECF coordinates are classification metadata, not capability identity — unchanged.
- The pre-CR-13 placements are preserved as a historical record in the §B audit table; nothing is rewritten in a way that loses the rule-history.

## 4. 26-entry re-evaluation (§B)

The new rule applied to all 26 canonical entries. Per-cell verdict:

| Entry | Pre-CR-13 primary | Post-CR-13 primary | Move? | Rationale (one line) |
|---|---|---|---|---|
| analytics-and-intelligence | enablement-operations/operate | enablement-operations/operate | **No** | Sustained insight-generation. |
| asset-management | enablement-operations/build (+operate,improve,retire) | enablement-operations/**operate** (build/improve/retire → secondary) | **Yes** | Center = ongoing stewardship of the asset base, not the build event. |
| change-management | governance-existence/improve | governance-existence/improve | **No** | Sustained improvement of the controlled state. |
| continuity-management | governance-existence/design (+operate) | governance-existence/design (+operate) | **No** | Continuity is designed (resilience patterns), then operated. |
| customer-management | party-relationship/operate (+conceive,improve,retire) | party-relationship/operate (+conceive,improve,retire) | **No** | Customer relationship is sustained. |
| enterprise-governance | governance-existence/conceive (+operate,improve) | governance-existence/conceive (+operate,improve) | **No** | Governance is constituted and sustained. |
| facility-management | enablement-operations/activate (+operate) | enablement-operations/**operate** (activate → secondary) | **Yes** | Center = ongoing operation of places; activate is one-time go-live. |
| financial-resource-management | finance-accounting/operate (+conceive) | finance-accounting/operate (+conceive) | **No** | Ongoing financial resource movements. |
| financial-stewardship | finance-accounting/conceive (+operate) | finance-accounting/conceive (+operate) | **No** | Stewardship posture, constituted and sustained. |
| idea-management | product-value/conceive (+design) | product-value/conceive (+design) | **No** | Idea generation is the defining work. |
| information-management | enablement-operations/operate | enablement-operations/operate | **No** | Sustained information stewardship. |
| legal-matter-management | governance-existence/conceive (+operate) | governance-existence/conceive (+operate) | **No** | Legal posture is constituted and sustained. |
| marketing | party-relationship/conceive (+operate) | party-relationship/conceive (+operate) | **No** | Marketing is upstream demand/conception work. |
| offering-management | product-value/conceive (+design,build,improve,retire) | product-value/conceive (+design,build,improve,retire) | **No** | Offering is conceived and sustained across the lifecycle. |
| operations | enablement-operations/operate (+improve) | enablement-operations/operate (+improve) | **No** | Operations IS sustained execution. |
| partner-management | party-relationship/conceive (+strategy-direction/**operate**) | party-relationship/conceive (+party-relationship/**operate**) | **Partial** (secondary fix only) | The `strategy-direction/operate` secondary is semantically wrong; revise to `party-relationship/operate` to match Customer/Supplier convention. |
| regulation-management | governance-existence/activate (+operate) | governance-existence/activate (+operate) | **No** | Regulation is activated (enforced), then operated. |
| risk-management | governance-existence/conceive (+operate,improve) | governance-existence/conceive (+operate,improve) | **No** | Risk posture is constituted at conceive. |
| security-management | governance-existence/design (+operate) | governance-existence/design (+operate) | **No** | Security is designed, then operated. |
| sourcing-and-procurement | enablement-operations/build (+strategy-direction/conceive,design,enablement-operations/operate) | enablement-operations/**operate** (build/conceive/design → secondary) | **Yes** | Center = ongoing acquisition execution; build is one event in a sustained buying cycle. |
| strategic-planning | strategy-direction/conceive | strategy-direction/conceive | **No** | Planning is constituted and renewed. |
| strategy | strategy-direction/conceive (+improve) | strategy-direction/conceive (+improve) | **No** | Strategy is constituted and revised. |
| supplier-management | party-relationship/conceive (+operate,improve) | party-relationship/**operate** (conceive/improve → secondary) | **Yes** | Center = ongoing management of the supply base; conceive (on-boarding) is upstream. |
| technology-management | strategy-direction/build (+operate,improve) | strategy-direction/build (+enablement-operations/operate) | **Carve-text only** (see §C) | Boundary is sharper than the coordinate move; see §C. |
| workforce-management | agency-organization/build (+operate,improve) | agency-organization/build (+operate,improve) | **No** | Workforce is acquired (built), then operated; build is the lifecycle pivot. |
| workforce-planning | agency-organization/design (+build) | agency-organization/design (+build) | **No** | Planning is design activity. |

**Result:** 21 of 26 placements survive unchanged under the new rule. **5 entries change**: 4 primary-coordinate moves (asset, facility, sourcing, supplier) + 1 secondary-coordinate fix (partner-management) + 1 carve-text update (technology-management).

**Cell occupancy after §B (post-CR-13):**

| Domain | conceive | design | build | activate | operate | improve |
|---|---|---|---|---|---|---|
| governance-existence | 3 | 2 | 0 | 1 | 0 | 1 |
| strategy-direction | 2 | 0 | 1 (tech-mgmt) | 0 | 0 | 0 |
| agency-organization | 0 | 1 | 1 | 0 | 0 | 0 |
| party-relationship | 2 | 0 | 0 | 0 | **2** | 0 |
| product-value | 2 | 0 | 0 | 0 | 0 | 0 |
| enablement-operations | 0 | 0 | 0 | 0 | **6** | 0 |
| finance-accounting | 1 | 0 | 0 | 0 | 1 | 0 |

(Note: total = 14 unique ECF cells, down from 16 after CR-DEA-BC-12. The four primary-coordinate moves (asset, facility, sourcing, supplier) consolidated into cells that were already occupied by canonical entries — the catalog's coordinate space became *more* concentrated under the new rule. Cell concentration is the intended effect: the post-CR-13 heatmap reflects what the catalog *is*, not where it starts.)

### §4.1 Pre-CR-13 vs post-CR-13 ECF heatmap

The post-CR-13 catalog is more concentrated in `operate` cells (the natural semantic center for sustained abilities) and less concentrated in `build`/`activate` cells. This is the explicit intended effect of the rule change — the ECF heatmap now *reads* the catalog the way a reader expects: things that are sustained are placed where they are sustained.

## 5. Technology Management boundary decision (§C)

### §5.1 The question (BC-SR-A001 §12)

> "Technology Management should mean: stewardship of the enterprise technology estate while Technology Enablement is a sub-concern of Enablement & Operations: use of technology to enable execution. That distinction should be made explicit in the capability catalog and ECF mapping rules. Otherwise future catalog contributors will continually debate whether cloud, platforms, applications, networks, AI agents, etc. belong in Strategy or Enablement."

### §5.2 Three options considered

| Option | Decision rule | Surface change |
|---|---|---|
| (a) Move Technology Management to enablement-operations/operate | Coordinate-only | 1 file |
| (b) Split Technology Management into two first-order caps (Technology Estate Management + Technology Enablement) | Two new canonical caps; admission gated on §12 review | 2+ files; count 26→28 |
| (c) Keep current coordinate + carve-text in `boundary` field + defer "Technology Enablement" specialization | Carve-text only; one cap | 1 file; deferred admission |

### §5.3 Chosen outcome: option (c) — carve-text only

**Rationale:**

- Option (b) — splitting into two first-order caps — is the architecturally correct outcome but is itself an admission decision (count 26 → 27), which must pass the §12 review gates. Doing it in this CR would mix a method-CR with an admission-CR, which is the very split that BC-12 §B explicitly avoided.
- Option (a) — moving to enablement-operations/operate — would lose the "estate" framing the reviewer explicitly endorsed. The `strategy-direction/build` placement honors the "stewardship of the technology estate" semantic; moving to operate would re-confuse Tech-as-Enablement with Tech-as-Estate, which is exactly the carve the reviewer asks to make explicit.
- Option (c) — carve-text only — honors the reviewer's recommendation *without* admission. The carve is recorded in `dea:capability-technology-management`'s `boundary` and `specialization_boundary` fields; a future CR may admit "Technology Enablement" as a new first-order cap if evidence supports it.

### §5.4 Carve-text (added to `dea:capability-technology-management/boundary` and `specialization_boundary`)

> **Boundary:** Stewards the enterprise technology estate (the set of platforms, applications, networks, data, and AI agents the enterprise uses). Does not execute operations through technology (Operations); does not derive insight from information (Analytics & Intelligence); does not govern information lifecycles (Information Management). The "use of technology to enable execution" sub-concern is **not** part of this capability's first-order scope and is recorded as a deferred specialization below.
>
> **Specialization boundary:** What is stewarded (cloud platforms, on-prem applications, networks, AI agents) is specialization of this capability. The "Technology Enablement" sub-concern (technology-as-enabler, the use of technology by other capabilities to execute) is **not** a specialization of this capability; it is a separate first-order candidate that may be admitted in a future CR if evidence supports it.

## 6. Investigation-track evidence collection (§D)

Per CR-DEA-BC-12 §B, three investigation tracks were opened:
- Track A — Organizational Design (P1)
- Track B — Enterprise Performance Management (P1)
- Track C — Relationship Management generic parent (P1–P2)

This CR starts the actual evidence work for all three. Each track produces:

1. **Candidate record** under `entities/v1-alpha/candidates/<candidate-id>/` (per the standard's `candidates/` directory layout, NOT canonical — the directory is non-canonical by design).
2. **Evidence register entry** in `catalog-research/evidence-register.yaml`.
3. **ECF overlay hypothesis** in `catalog-research/preliminary-ecf-overlay.yaml` (appended).
4. **Distinctness sweep** in `catalog-research/distinctness-sweep.yaml` (appended).

**No entity is admitted in this CR.** Admission remains gated on `METHODOLOGY.md §12` review gates; admission happens in follow-on admission CRs (provisional CR-DEA-BC-14/15/16 per BC-12 §9) when the evidence package is complete.

### §6.1 Track A — Organizational Design

**Candidate record:** `entities/v1-alpha/candidates/cand-orgdesign/` (this directory is excluded from canonical entry enumeration by `scripts/regenerate_catalog.py` and the `check_ecf_conformance.py` walk; see conformance suite for the exclude rule).

**ECF placement hypothesis:** `agency-organization/design` (primary), with `agency-organization/conceive` and `agency-organization/build` as secondaries. Under the new §A rule, this is the *sustained* activity of structuring roles, authorities, and coordination patterns — squarely in the design axis of Agency & Organization.

**Evidence register entry:** E3 (preliminary; the workforces-sweep and at least one industry corpus are needed to push to E4 before admission).

**Distinctness sweep:** against `dea:capability-workforce-management` (workers, not structure), `dea:capability-workforce-planning` (capacity, not structure), `dea:capability-strategy` (strategic posture, not structure), `dea:capability-strategic-planning` (planning, not structure).

**Open evidence questions:**
- Does the candidate have a distinct durable business object? (Initial hypothesis: "Organizational Structure" — to be tested.)
- Is the capability substrate-neutral (human + AI agents per the Agency & Organization v2.4.0 stress test)?
- Does it survive the enterprise-generality test across ≥3 verticals?

### §6.2 Track B — Enterprise Performance Management

**Candidate record:** `entities/v1-alpha/candidates/cand-epm/`.

**ECF placement hypothesis:** `strategy-direction/operate` (primary), with `strategy-direction/improve` and `finance-accounting/operate` as secondaries. Under the new §A rule, EPM is the sustained performance measurement + governance activity; the primary is `operate`, secondary `improve` for the closed-loop adaptation.

**Evidence register entry:** E3 (preliminary; needs corroboration across OMG/Prometheus/Balanced Scorecard sources to push to E4).

**Distinctness sweep:** against `dea:capability-analytics-and-intelligence` (insight from information, not performance governance), `dea:capability-financial-resource-management` (financial performance specifically, not enterprise-wide), `dea:capability-strategy` (posture, not measurement), `dea:capability-strategic-planning` (plan, not measurement).

**Open evidence questions:**
- Is "Performance" a durable distinct business object, distinct from "Insight" (Analytics), "Outcome" (Operations), and "Decision" (Governance)?
- Does EPM close the Direction loop (Strategy → Planning → Performance → Insight → Adaptation) without collapsing into Analytics?
- Cross-industry universality test (B2B/B2C/G2C per the foundation inclusion criteria).

### §6.3 Track C — Relationship Management

**Candidate record:** `entities/v1-alpha/candidates/cand-relmgmt/`.

**ECF placement hypothesis:** `party-relationship/conceive` (primary), with `party-relationship/operate` and `party-relationship/improve` as secondaries. Under the new §A rule, Relationship Management is the *constituted* ability to establish, govern, develop, and terminate external-party relationships across the lifecycle; it is constituted at conceive and sustained.

**Evidence register entry:** E2 (early-stage; needs evidence across at least 2 industry corpus sources to push to E3).

**Distinctness sweep:** against `dea:capability-customer-management` (customer-specific), `dea:capability-supplier-management` (supplier-specific), `dea:capability-partner-management` (partner-specific), `dea:capability-marketing` (demand-side acquisition).

**Open evidence questions:**
- Is "Relationship" (party/relationship as the underlying semantic subject, per the ECF's own framing) a distinct durable business object? Or is it an abstraction over the role-specific caps?
- If admitted, do the role-specific caps become specializations (BC-12 §B.3 option 1), or does the generic parent exist as abstract grouping only (option 2), or is no parent warranted (option 3)?
- Cross-industry universality test (B2B/B2C/G2C).

**Decision bias:** the three options have unequal a priori plausibility. Option 3 (no generic parent) is the simplest and is the catalog's current state. Option 1 (admit generic parent) is the most architecturally aligned with the ECF but adds a first-order cap. Option 2 (abstract grouping only) preserves the first-order-concept discipline but produces a non-canonical entry (the abstract grouping has no business object of its own). The investigation must produce evidence for one of these.

## 7. Files changed

### §A. Method rule refinement

- `METHODOLOGY.md` — §8.2 rule text replaced; §3.2 selection heuristics added; §3.3 backward-compatibility note added.

### §B. 26-entry re-evaluation

- **4 entity YAMLs** with primary-coordinate moves: `asset-management`, `facility-management`, `sourcing-and-procurement`, `supplier-management`. Each: `version 1.1.0 → 1.2.0`; `ecf.primary` updated; `ecf.secondary` rotated (former primary becomes secondary where applicable); `ecf_rationale` rewritten to cite CR-DEA-BC-13 + the new rule; `ecfConformance.canonicalReferences` updated.
- **1 entity YAML** with secondary-coordinate fix: `partner-management` (drop `strategy-direction/operate` secondary; add `party-relationship/operate` secondary). `version 1.0.0 → 1.1.0`.
- **21 entity YAMLs** with rationale refresh only (no coordinate change): each gets an `ecf_rationale` update that cites CR-DEA-BC-13 and confirms the placement survives the new rule. Versions unchanged (1.0.0 or 1.1.0 already).
- `CATALOG.yaml` — regenerated.

### §C. Technology Management boundary

- **1 entity YAML** with carve-text: `dea:capability-technology-management`. `boundary` field expanded with the Tech-as-Estate vs Tech-as-Enablement carve; `specialization_boundary` field expanded. `version 1.1.0 → 1.2.0`.

### §D. Investigation tracks A/B/C

- **3 candidate subtrees** under `entities/v1-alpha/candidates/`: `cand-orgdesign/`, `cand-epm/`, `cand-relmgmt/`. Each contains a candidate record YAML + a brief `README.md` with the candidate's distinctness-sweep against the existing 26.
- `catalog-research/evidence-register.yaml` — appended with 3 new entries.
- `catalog-research/preliminary-ecf-overlay.yaml` — appended with 3 new overlay hypotheses.
- `catalog-research/distinctness-sweep.yaml` — appended with 3 new sweeps.

### §E. Carrier CR + paperwork

- `change-requests/CR-DEA-BC-13.md` (this file).
- `change-requests/README.md` — row added.
- `CHANGELOG.md` — `[v1-alpha.6]` section added.
- `docs/REVIEWS.md` — entry appended for this release (submittal-review-driven follow-on to BC-SR-A001).

## 8. Version bump

Per `docs/VERSIONING.md` §2.2 (Minor for coordinate changes):

- **Catalog label:** v1-alpha.5 → v1-alpha.6 (Minor).
- **Affected entry versions:**
  - 4 entries with primary moves: 1.1.0 → 1.2.0 (asset, facility, sourcing, supplier).
  - 1 entry with secondary fix: 1.0.0 → 1.1.0 (partner).
  - 1 entry with carve-text: 1.1.0 → 1.2.0 (technology).
  - 21 entries with rationale refresh: version unchanged.
  - Candidate records (under `candidates/`): have no version (non-canonical).
- **Specialization views:** unchanged.
- **Total canonical entry count:** 26 → 26 (no admission; candidates under `candidates/` are non-canonical).

## 9. Acceptance criteria

- [ ] `METHODOLOGY.md §8.2` codified with the new rule and selection heuristics.
- [ ] All 26 entity YAMLs in `entities/v1-alpha/` reviewed under the new rule.
- [ ] 4 entries with primary-coordinate moves have new coordinates + new rationales + version 1.2.0.
- [ ] 1 entry (partner-management) has secondary-coordinate fix + version 1.1.0.
- [ ] 1 entry (technology-management) has carve-text in `boundary` + `specialization_boundary` + version 1.2.0.
- [ ] 21 entries with rationale refresh only have CR-DEA-BC-13 citation in `ecf_rationale`.
- [ ] `CATALOG.yaml` regenerated and committed.
- [ ] `scripts/check_ecf_conformance.py` passes.
- [ ] `scripts/check_naming.py` shows no NEW warnings beyond the existing 5 advisories.
- [ ] `scripts/check_versions.py` passes.
- [ ] `scripts/check_visual_domain_labels.py` passes.
- [ ] All 3 investigation-track candidate records exist under `entities/v1-alpha/candidates/`.
- [ ] All 3 evidence-register entries exist.
- [ ] All 3 ECF overlay hypotheses exist.
- [ ] All 3 distinctness sweeps exist.
- [ ] `CHANGELOG.md` has the `[v1-alpha.6]` section.
- [ ] `change-requests/README.md` has the CR-DEA-BC-13 row.
- [ ] `docs/REVIEWS.md` has the v1-alpha.6 entry.

## 10. Tag

`v1-alpha.6` is cut at this CR's merge commit per CR-DEA-BC-05. Tag signing: project GPG signing setup; see the standing protocol.

## 11. Follow-on (not in this CR)

| Follow-on CR | Scope | Source |
|---|---|---|
| CR-DEA-BC-14 (provisional) | Track A admission CR (only if Track A evidence supports it) | BC-SR-A001 §4 |
| CR-DEA-BC-15 (provisional) | Track B admission CR (only if Track B evidence supports it) | BC-SR-A001 §5 |
| CR-DEA-BC-16 (provisional) | Track C admission CR (only if Track C evidence supports it) | BC-SR-A001 §6 |
| CR-DEA-BC-17 (provisional) | Technology Management split (admit "Technology Enablement" as a separate first-order cap), only if evidence supports it | BC-SR-A001 §12, BC-13 §5 |
