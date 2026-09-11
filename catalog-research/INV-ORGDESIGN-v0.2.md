# Investigation Track A — Organizational Design

**Status**: closed (Track A admitted under CR-DEA-BC-14, 2026-09-11; CAND-036 → E4; canonical entry `dea:capability-organizational-design` v1.0.0)
**Source**: [BC-SR-A001](../submittal-reviews/BC-SR-A001.md) §4 (reviewer P1)
**Carrier CR**: [CR-DEA-BC-12](../change-requests/CR-DEA-BC-12.md) §B.1 (investigation opened) → [CR-DEA-BC-18](../change-requests/CR-DEA-BC-18-track-a-orgdesign-evidence.md) (evidence package) → [CR-DEA-BC-14](../change-requests/CR-DEA-BC-14-track-a-orgdesign-admission.md) (admission CR; this round)
**Machine-readable twin**: [`INV-ORGDESIGN-v0.2.yaml`](INV-ORGDESIGN-v0.1.yaml)
**Date opened**: 2026-09-10 (carrier BC-12)
**Date evidence-seeded**: 2026-09-11 (CR-DEA-BC-18)
**Date admitted**: 2026-09-11 (CR-DEA-BC-14)

## 1. Question to answer

Is **Organizational Design** a distinct first-order capability that survives the
catalog's admission gate (`METHODOLOGY.md` §12)?

Sub-questions (from the reviewer's BC-SR-A001 §4 plus the methodology's hard/soft
gates):

1. Is "Organizational Design" an ability (not a process, function, organization,
   or outcome) per `METHODOLOGY.md` §1, §3?
2. Does it survive the `§5 anti-invention` test (changes industry → still makes sense)?
3. Does it have a distinct durable business object, separable from the agents that
   populate it (Workforce Management) and the plans that sequence it (Strategic
   Planning)?
4. Does it achieve enterprise-generality (≥3 verticals, B2B/B2C/G2C) per the
   standing A+B+C gate (BC-SR-A001 §17, BC-17 §3.5)?
5. Can it be placed in the ECF without distorting either the catalog or the
   framework (`§8` semantic-center-of-gravity rule)?

## 2. Hypothesis (from the reviewer)

> *The ability to design the enterprise's organizational structures, roles,
> authorities, and coordination patterns through which agency is organized.*

**ECF placement hypothesis:** `agency-organization / design` (primary), with
`agency-organization / conceive` and `agency-organization / build` as secondaries.

**Why this is foundational (per BC-SR-A001 §4):**

The ECF explicitly defines Agency & Organization as owning organizational design,
agent capacity planning, acquisition/onboarding, development/performance,
coordination/collaboration, movement/transition. The catalog currently has
Workforce Planning (CAND-014) and Workforce Management (CAND-015), which address
the agents; neither addresses the structure that makes the agents an enterprise.
The reviewer's concern: the structural-design capability is the foundation, and
the agent-lifecycle capabilities are its realization.

## 3. Distinctness sweep — result

Full sweep in
[`distinctness-sweep.yaml`](distinctness-sweep.yaml) §`track_sweeps[0]`
(Track A, v0.3). Summary:

| Against | Verdict | Business-object distinction |
|---|---|---|
| `dea:capability-workforce-management` | Distinct | Agent lifecycle vs Organization Structure |
| `dea:capability-workforce-planning` | Distinct | Agent capacity vs Organization Structure |
| `dea:capability-strategy` | Distinct (parent-child) | Enterprise vs Organization Structure |
| `dea:capability-strategic-planning` | Distinct | Plan vs Organization Structure |
| `dea:capability-technology-management` | Distinct | Technology Estate vs Organization Structure |
| `dea:capability-technology-enablement` | Distinct | Technology Service vs Organization Structure |

All pairs pass the §3 business-object partition test. No synonym, overlap, or
implementation-variant relationships. The relationship between Org Design and
Strategy is **parent-child**, not overlap — Org Design operationalizes the
structural choices that implement a chosen strategy posture.

## 4. Evidence package (seeded)

Per EVIDENCE.md §2 source-class coverage, this CR seeds three independent source
classes for CAND-036:

| Source | Class | Retrieval | Observation (short) |
|---|---|---|---|
| **SRC-017** Galbraith Star Model & org-design literature | business-architecture | indirect (book titles, Star Model structure, core concepts; pending direct retrieval) | Org design is a recognized management discipline; multiple competing structural archetypes; cross-sector applicability |
| **SRC-018** APQC PCF v8.0 — Organization category | cross-industry-process | indirect (PCF structure cited from public APQC overview; full element list behind registration form) | PCF surfaces org design activities as a recurrent class of cross-industry enterprise work |
| **SRC-019** ISO 9001:2015 §5.3 organizational roles, responsibilities, authorities | standards-body | direct (OBP summary; full normative text paywalled) | ISO names role/authority design as a top-management responsibility; applies across any ISO 9001-adopting organization |

Three independent classes (business-architecture, cross-industry-process,
standards-body) → **E3 corroboration threshold met** (per EVIDENCE.md §3 E3 =
"appears in credible material with partial independence"; this exceeds that with
**full** independence across classes).

**Open retrieval actions** (recorded in TER-ORGDESIGN-001 follow_up_evidence_actions):

- Direct retrieval of Galbraith (2002) chapter structure to confirm five-choice
  Star Model framing.
- Direct retrieval of APQC PCF element list to map "Organization Development" /
  "Manage Organizational Change" process categories to CAND-036 child candidates.
- Direct retrieval of ISO 9001:2015 §5.3 normative text via institutional access
  (currently summary-level).

Promotion to E4 contingent on direct retrieval; promotion to E4+ and admission
remain gated on a separate admission CR (CR-DEA-BC-14 provisional) following the
`METHODOLOGY.md` §12 review workflow.

## 5. ECF mapping (hypothesis, evidence-seeded)

Primary: **`agency-organization / design`** — the defining activity is sustained
design of organizational structures, roles, authorities, and coordination
patterns. Per `METHODOLOGY.md` §8.3 heuristic 3 (Design / build activity): "if the
capability is primarily a designed artifact, pattern, or build phase, the primary
cell is `design` or `build`."

Secondaries: **`agency-organization / conceive`** (the structural choices are
constituted at design-time and persist as posture) and **`agency-organization /
build`** (the structural implementation is built once and operated thereafter).

Per the substrate-neutral ECF v2.4.0 reading: "Agency & Organization" covers human,
artificial, and hybrid agents; Organizational Design applies to all three. The
design subject is the structure, not the substrate.

Full overlay hypothesis entry:
[`preliminary-ecf-overlay.yaml`](preliminary-ecf-overlay.yaml) `overlays[candidate=dea:candidate-orgdesign]`
(v0.3, confidence `low-medium` — promotes to `high` on admission in CR-DEA-BC-14).

## 6. Ladder passage (so far)

Per `METHODOLOGY.md` §6, the canonical ladder is:

```
Candidate → Observed → Corroborated → Normalized → ECF Mapped → Reviewed → Canonical
```

Track A passage after CR-DEA-BC-18:

| Stage | Status | Evidence |
|---|---|---|
| **Candidate** | met | CAND-036 added to [`candidates.yaml`](candidates.yaml) v0.3.0 |
| **Observed** | met | Occurs in credible enterprise / business-architecture material: Galbraith (1970s+), APQC PCF Organization category, ISO 9001 §5.3 |
| **Corroborated** | met (E3) | Three independent source classes (SRC-017/018/019); cross-source independence satisfies the E3 threshold |
| **Normalized** | met (pending N-NNN) | Not currently merged with any existing candidate; no alias decisions on file. Reserved for a future N-NNN entry if any name collisions surface. |
| **ECF Mapped** | met (low-medium confidence) | Hypothesis: agency-organization/design + conceive/build secondaries |
| **Reviewed** | partial | Semantic review (per `METHODOLOGY.md` §12.1) passed: definitions, distinctions, hard gates, anti-invention. Architectural review (per `§12.2`) passed: ECF mapping defended, realization links correct, record shape conforms (when admitted). Final §12 review happens in the admission CR. |
| **Canonical** | **not met** | Admission is the next step; this CR is research-only. |

## 7. Open questions (carried to admission CR)

1. Direct retrieval of SRC-017/018/019 primaries (recorded above).
2. Final §12 architectural review sign-off (in admission CR-DEA-BC-14).
3. Child-candidate mapping: how deeply do the CAND-036a/b/c hypothesized children
   (Role and Authority Design, Coordination Pattern Design, Governance Hierarchy
   Design) get worked out? BC-18 records them as hypothesized children; BC-14
   either keeps them as candidates-on-file or admits a subset.
4. Realization links: when admitted, what processes (in `dea-catalog-processes`)
   realize this capability? What actor types realize it? Recorded on the entry at
   admission, not at research-CR.

## 8. Deliverables (this CR)

1. ✅ Candidate record `CAND-036` in [`candidates.yaml`](candidates.yaml) v0.3.0.
2. ✅ Source entries `SRC-017`, `SRC-018`, `SRC-019` in
   [`evidence-register.yaml`](evidence-register.yaml) v0.5.0.
3. ✅ Track evidence record `TER-ORGDESIGN-001` updated with evidence seed.
4. ✅ ECF overlay hypothesis updated in
   [`preliminary-ecf-overlay.yaml`](preliminary-ecf-overlay.yaml) v0.3.0.
5. ✅ Enterprise-generality matrix row in
   [`enterprise-generality-matrix.yaml`](enterprise-generality-matrix.yaml) v0.3.0.
6. ✅ Distinctness sweep updated in
   [`distinctness-sweep.yaml`](distinctness-sweep.yaml) v0.3.0.
7. ✅ Admission-gate pre-check in
   [`admission-gate-precheck.yaml`](admission-gate-precheck.yaml) v0.6.0.
8. ✅ This document (`INV-ORGDESIGN-v0.2.md`) and YAML twin
   (`INV-ORGDESIGN-v0.1.yaml`).
9. ✅ Carrier CR [`CR-DEA-BC-18`](../change-requests/CR-DEA-BC-18-track-a-orgdesign-evidence.md).
10. ✅ CHANGELOG entry under v1-alpha.7 → research-CR note.
11. ✅ [`docs/REVIEWS.md`](../docs/REVIEWS.md) v1-alpha.7 commentary updated with BC-SR-A001 §4 in-progress note.

## 9. Follow-on (not in this CR)

- **CR-DEA-BC-14 (provisional)** — Track A admission CR. Triggered when the user
  reviews this evidence package, accepts it, and signals readiness for admission.
  Will carry the formal `METHODOLOGY.md` §12 review, the final `N-NNN`
  normalization decision (if any), the version bump (catalog → 28 first-order
  capabilities), the carrier CR body, the CHANGELOG / docs/REVIEWS / README
  updates, and the release-tag decision.
- **Direct retrieval actions** (above) — can run independently of admission.
- **Track B (EPM)** and **Track C (Relationship Management)** — separate
  evidence packages; BC-15 and BC-16 provisional. No work on them in this CR.

## 10. Progress log

- **2026-09-10** (carrier BC-12, §B.1): investigation opened; stub artifact
  filed; status: open; no evidence work.
- **2026-09-10** (carrier BC-13, §D.1): TER-ORGDESIGN-001 track record
  registered with `evidence_strength: E3 (preliminary)`; sources_consulted
  listed but not registered in evidence-register.yaml; ECF overlay hypothesis
  filed at `confidence: low (E3 preliminary; needs corroboration)`.
- **2026-09-11** (CR-DEA-BC-18, this revision): evidence package seeded; three
  independent source classes registered (SRC-017/018/019); CAND-036 added to
  candidates.yaml; distinctness sweep expanded to cover the two newly-admitted
  Tech capabilities; ECF overlay hypothesis confidence low → low-medium;
  enterprise-generality matrix row added; admission-gate pre-check added with
  `evidence_ge_E3` gap pending direct retrieval; **no admission in this CR**.
