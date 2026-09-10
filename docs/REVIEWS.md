# Submittal Reviews — Release Commentary

This document is the per-release commentary surface for **submittal reviews** filed
against this catalog. Each release that lands at least one recommendation from a
submittal review gets a section here.

The intent is two-fold:

1. **Make submittal review work discoverable.** Anyone reading the release notes or
   the catalog's history can trace what was reviewed, what was found, what was
   acted on, and what was deferred.
2. **Make submittal review commentary "summarized yet rich."** The full review
   file (under `submittal-reviews/`) is the long-form record; this document is
   the bridge — enough context to understand *why* the release changed, with
   pointers to the full evidence.

## Format

Each entry is appended in release order. New entries are added by the carrier CR
that lands the recommendations. The structure is:

```
## [<release label>] — <release date>

**Submittal review filed:** <BC-SR-A###> by <reviewer> on <date>
**Carrier CR:** <CR-DEA-...-NN>
**Review scope:** <one-line>
**Headline findings:** <2–4 bullets, paraphrased>
**Items landed in this release:** <bullets citing review section numbers>
**Items opened as investigations:** <bullets with their own CR numbers, if opened>
**Items deferred to backlog:** <bullets with rationale>
**Doc-drift items closed:** <bullets>
```

The goal is that a reader can skim one entry to understand the substance, and
follow the links for the long-form.

---

## Index

- [v1-alpha.5 — 2026-09-10](#v1-alpha5--2026-09-10)
- [v1-alpha.6 — 2026-09-10 (BC-SR-A001 follow-on)](#v1-alpha6--2026-09-10-bc-sr-a001-follow-on)

---

## v1-alpha.5 — 2026-09-10 (planned)

**Submittal review filed:** BC-SR-A001 by (external) on 2026-09-10 against the
v1-alpha.4 catalog (commit `570830a`).

**Carrier CR:** CR-DEA-BC-12.

**Review scope:** Full catalog v1-alpha.0..v1-alpha.4 — methodology, ECF semantic
alignment, foundational gap analysis, and repository/doc drift.

**Headline findings (paraphrased):**
- The catalog is "approximately 80–85% of the way to a strong enterprise-general
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
- Investigation track A — **Organizational Design** as a first-order capability
  (§4 P1). Evidence investigation per the catalog's own admission gate; no
  admission until evidence supports it.
- Investigation track B — **Enterprise Performance Management** as a first-order
  capability (§5 P1). Evidence investigation, including how it would close the
  Direction loop in §16.
- Investigation track C — **Relationship Management** as a generic parent for
  Customer/Supplier/Partner Management (§6 P1–P2). Boundary-led investigation;
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
  Architecture Management** as candidate first-order caps (§17 P2–P3). No
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

## v1-alpha.6 — 2026-09-10 (BC-SR-A001 follow-on)

**Submittal review filed:** [BC-SR-A001](../submittal-reviews/BC-SR-A001.md)
(continues from v1-alpha.5 carrier — same review; this release closes BC-SR-A001
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
- Track A — Organizational Design (research files: `INV-ORGDESIGN-v0.1.md` +
  candidate record + evidence-register stub TER-ORGDESIGN-001 + ECF overlay
  hypothesis + distinctness sweep).
- Track B — Enterprise Performance Management (loop-closure narrative required
  regardless of admission).
- Track C — Relationship Management generic parent (3 decision options tracked:
  admit-with-specializations / abstract-grouping-only / no-admit).

**Items deferred to backlog (with rationale):**
- **Technology Management split** (admit a separate "Technology Enablement"
  first-order cap). Deferred per BC-13 §C: the carve-text is sufficient for now;
  a split is the architecturally correct outcome but is itself an admission
  decision (count 26 → 27) that must pass the §12 review gates. CR-DEA-BC-17
  (provisional) handles this once evidence supports it.
- **Knowledge Management** (§7 P2). Revisit after track A reports back, because
  `agency-organization / improve` is the most likely placement.
- **Service / Quality / Stakeholder / EAM** candidates (§17 P2–P3). Revisit
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
