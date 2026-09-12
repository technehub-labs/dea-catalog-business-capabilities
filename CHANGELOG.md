# Business Capability Catalog Changelog

All notable changes to this catalog are recorded here. The format is based
on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) adapted for
CR-DEA-BC-05 versioning: each entry records the bump tier (major / minor /
patch), the scope, the rationale, the PR that landed it, and any tag.

The catalog uses `v<N>-<word>` versioning while in v1 (lettered-suffix
regime) and `v<N>.<M>` semver from v2 onward. See
[`docs/VERSIONING.md`](VERSIONING.md) for the normative procedure.

## [v1-alpha.8] - 2026-09-11

**Minor** (CR-DEA-BC-14, PR pending). Admission-CR closing the BC-SR-A001 §4 evidence work (reviewer P1: "the catalog had Strategy + Strategic Planning + Workforce Planning + Workforce Management but not the structural-design capability the ECF positions in `agency-organization/design`"). Admits `dea:capability-organizational-design` as the **28th first-order canonical capability** at `agency-organization/design` (primary), with `agency-organization/{conceive, build}` as secondaries. OrgDesign is the structural-design function (roles, units, reporting lines, authorities, coordination patterns that fit the work the enterprise must do); it is the peer of Workforce Planning (same primary coordinate `agency-organization/design`, distinct by business-object partition: Organization Structure vs Workforce Plan). Track A of CR-DEA-BC-13 §B.1 closed.

### Affected entries

- **New entry:** `dea:capability-organizational-design` v1.0.0 (first canonical release).
- **Strategy:** 1.1.0 → **1.1.1** (Patch for related_capabilities + boundary-text exclusion extension).
- **Strategic Planning:** 1.1.0 → **1.1.1** (Patch).
- **Workforce Management:** 1.1.0 → **1.1.1** (Patch).
- **Workforce Planning:** 1.1.0 → **1.1.1** (Patch; explicit same-cell note added).
- **Change Management:** 1.0.0 → **1.0.1** (Patch).
- **Technology Management:** 1.3.0 → **1.3.1** (Patch).
- **Technology Enablement:** 1.0.0 → **1.0.1** (Patch).
- **Enterprise Governance:** 1.0.0 → **1.0.1** (Patch).
- **Other 19 entries:** unchanged.

### Track A closure

- TER-ORGDESIGN-001 track record closed; CAND-036 promoted E3 → E4 per EVIDENCE.md §3 admission promotion rule.
- ECF overlay hypothesis confidence low-medium → high.
- Distinctness sweep extended to cover all 8 peers (added Enterprise Governance + Change Management in this CR).
- Admission-gate pre-check `evidence_ge_E3` gap → met.
- Follow-up direct-retrieval actions for SRC-017/018/019 primaries recorded as independent of admission (would re-rate to E5 if done).

### Research-CR addendum (CR-DEA-BC-19, same release cycle; no version bump)

**Track B (Enterprise Performance Management) evidence package**. Research-CR; no canonical entity admitted in this CR. Seeds CAND-037 in the candidate universe (E1 → E3 confirmed across SRC-020/021/022 three-source convergence); adds SRC-020 (Kaplan and Norton Balanced Scorecard; business-architecture class), SRC-021 (OKR framework; commercial-capability-models class), SRC-022 (OMG Business Performance Management standards via OCEB 2; standards-body class). Closes TER-EPM-001 evidence-pending → evidence-seeded. Distinctness sweep expanded 4 → 8 peers (added Workforce Management + Technology Management + Technology Enablement + Organizational Design). ECF overlay confidence low → low-medium. Admission-gate pre-check added with all 10 gates met on current evidence (CAND-037 row; promotion to E4 contingent on admission in CR-DEA-BC-15 provisional). Direction Loop closure narrative recorded per BC-DEA-BC-13 §D.2 explicit decision (loop closes if EPM is admitted; loop remains open if EPM is not admitted; the missing link is governance of outcomes, partly absorbed into Analytics today). Catalog count unchanged at 28 first-order caps.

## Unreleased

**Housekeeping** (no version bump; pre-release cleanup). Removes en/em dashes from every GitHub-visible artifact in the repo (32 files; 213 em-dashes + 24 en-dashes removed from Markdown; 23 em-dashes from YAML prose). The punctuation policy now lives in memory; the artifact layer reflects it without stating it. Change-requested under user instruction 2026-09-11.

## [v1-alpha.7] - 2026-09-10

**Minor** (CR-DEA-BC-17, PR pending). Admission-CR closing the BC-DEA-BC-13 §11 follow-on queue item. Admits `dea:capability-technology-enablement` as the 27th first-order canonical capability at `enablement-operations/operate` (primary), with `enablement-operations/{build, improve}` as secondaries. The new entry is the IT **delivery** function (running technology services, platforms, automation for the rest of the enterprise); Technology Management remains the IT **direction** function (stewarding the technology estate). The carve BC-SR-A001 §12 asked us to make explicit is now formalized as a peer relationship between two first-order capabilities rather than as a deferred specialization.

### Affected entries

- **New entry:** `dea:capability-technology-enablement` v1.0.0 (first canonical release).
- **Technology Management:** 1.2.0 → **1.3.0** (Minor for boundary-text change + related_capabilities addition).
- **Operations:** 1.0.0 → **1.0.1** (Patch for cross-reference addition).
- **Information Management:** 1.0.0 → **1.0.1** (Patch for cross-reference addition).
- **Other 23 entries:** unchanged.

### Evidence trail

- `catalog-research/evidence-register.yaml` v0.5.0: TER-TECHENABLEMENT-001 (E3 → E4 on admission).
- `catalog-research/preliminary-ecf-overlay.yaml` v0.3.0: ECF overlay hypothesis appended; status promoted to "admitted".
- `catalog-research/distinctness-sweep.yaml` v0.3.0: distinctness sweep appended against Operations, Tech Mgmt, IM, A&I.
- `catalog-research/admission-gate-closeout.yaml`: §12 review-gate closeout recorded.

### Foundation inclusion criteria gate A+B+C (locked 2026-09-10)

- (A) Sensible in ≥3 verticals: ✅ Universal IT delivery function across B2B/B2C/G2C and every industry archetype.
- (B) Works in B2B/B2C/G2C archetypes: ✅ Every archetype has an IT delivery function.
- (C) Describable without industry-specific domain object: ✅ "Technology Service" is substrate-neutral.

### Catalog count

**26 → 27 first-order canonical capabilities** (first-order admission).

**Tag**: `v1-alpha.7` (target at this CR's merge commit).

### Research-CR addendum (same release cycle, no version bump)

**CR-DEA-BC-18** (research-CR; no admission). Begins the evidence-collection work
for BC-SR-A001 §4 (Track A: Organizational Design). Lands on disk:

- CAND-036 added to candidate universe (CAPABILITY classification; evidence
  rating E1 pending direct retrieval; promotes to E3 on independent
  corroboration across three source classes).
- SRC-017/018/019 added to evidence register (business-architecture /
  cross-industry-process / standards-body classes respectively; full
  independence across classes).
- TER-ORGDESIGN-001 track record seeded.
- ECF overlay hypothesis confidence `low → low-medium`.
- Enterprise-generality matrix row added (9 of 10 types strong; non-profit
  moderate; demonstrated per A+B+C gate).
- Distinctness sweep expanded to cover the two newly-admitted Tech capabilities.
- Admission-gate pre-check added with honest gap disclosure (`evidence_ge_E3`
  pending direct retrieval of SRC-017/018/019 primaries).
- Full investigation report: `catalog-research/INV-ORGDESIGN-v0.2.md` + YAML
  twin `INV-ORGDESIGN-v0.1.yaml`.

**No canonical entity admitted** in CR-DEA-BC-18. Catalog still 27 first-order.
Track A admission remains the next step (provisional CR-DEA-BC-14, triggered on
user acceptance of this evidence package).

## [v1-alpha.6] - 2026-09-10

**Minor** (CR-DEA-BC-13, PR #66). Method-CR for the ECF primary-coordinate rule: replaces the pre-CR-13 "earliest initiation point" rule with "semantic center of gravity" (METHODOLOGY.md §8), re-evaluates all 26 canonical entries under the new rule, formalizes the Technology Management carve per BC-SR-A001 §12, and starts the actual evidence collection for the three investigation tracks (Organizational Design, Enterprise Performance Management, Relationship Management) as non-canonical candidate records (no admission in this release).

### §A. Method rule refinement

`METHODOLOGY.md §8.2` codified with the new rule and four selection heuristics (sustained stewardship / posture / design / activation). The pre-CR-13 "earliest initiation point" rule is preserved as a historical record but is no longer the canonical selection logic. Backward-compatible: only the 4 primary-coordinate moves change; all secondaries preserved; no entry identity changes.

### §B. 26-entry re-evaluation

| Entry | Pre-CR-13 primary | Post-CR-13 primary | Move? |
|---|---|---|---|
| asset-management | enablement-operations/build | enablement-operations/**operate** (build → secondary) | **Yes** |
| facility-management | enablement-operations/activate | enablement-operations/**operate** (activate → secondary) | **Yes** |
| sourcing-and-procurement | enablement-operations/build | enablement-operations/**operate** (build → secondary) | **Yes** |
| supplier-management | party-relationship/conceive | party-relationship/**operate** (conceive → secondary) | **Yes** |
| partner-management | party-relationship/conceive (+strategy-direction/operate) | party-relationship/conceive (+party-relationship/operate) | **Partial** (secondary fix only) |
| technology-management | strategy-direction/build | strategy-direction/build (no coord change; carve-text added) | **Carve-text only** |
| (other 20) | unchanged | unchanged | **No** |

Versions bumped: asset/facility/sourcing/supplier 1.1.0 → 1.2.0; technology 1.1.0 → 1.2.0; partner 1.0.0 → 1.1.0; others unchanged.

### §C. Technology Management boundary decision

Per BC-SR-A001 §12 and the user's CR-13 design decision (Q2): carve-text only. `dea:capability-technology-management/boundary` and `specialization_boundary` expanded to make the Tech-as-Estate vs Tech-as-Enabler carve explicit. The "Technology Enablement" sub-concern is recorded as a deferred specialization that a future CR may admit. Coordinate change: none. Version 1.1.0 → 1.2.0.

### §D. Investigation tracks A/B/C: evidence collection started

Three non-canonical candidate records created under `entities/v1-alpha/dea:candidate-{orgdesign,epm,relmgmt}/candidates/`:
- **Track A: Organizational Design**: ECF overlay `agency-organization/design` (E3 preliminary).
- **Track B: Enterprise Performance Management**: ECF overlay `strategy-direction/operate` (E3 preliminary); loop-closure narrative required (BC-SR-A001 §16).
- **Track C: Relationship Management generic parent**: ECF overlay `party-relationship/conceive` (E2 early); three decision options evaluated (admit-with-specializations / abstract-grouping-only / no-admit).

No admission. Each track's evidence-record stub and ECF overlay hypothesis appended to `catalog-research/{evidence-register,preliminary-ecf-overlay,distinctness-sweep}.yaml`.

**Tag**: `v1-alpha.6` (cut at this CR's merge commit; landed).

## [v1-alpha.5] - 2026-09-10

**Minor** (CR-DEA-BC-12, PR #65). Submittal-review driven ECF
re-alignment. Carrier for the substantive recommendations of submittal
review [BC-SR-A001](submittal-reviews/BC-SR-A001.md), filed 2026-09-10
against the released v1-alpha.4 catalog (commit `570830a`).

**Six high-confidence ECF re-mappings** (per-entity version: 1.0.0 → 1.1.0;
catalog version: v1-alpha.4 → v1-alpha.5; tag at merge commit):

| Entry | Old primary | New primary | Review § |
|---|---|---|---|
| Strategy | `governance-existence / conceive` | `strategy-direction / conceive` | §8.A |
| Strategic Planning | `governance-existence / conceive` | `strategy-direction / conceive` | §9 |
| Asset Management | `strategy-direction / build` | `enablement-operations / build` | §10 |
| Facility Management | `strategy-direction / activate` | `enablement-operations / activate` | §11 |
| Supplier Management | `strategy-direction / build` | `party-relationship / conceive+operate` | §13 |
| Sourcing & Procurement | `strategy-direction / build` | `enablement-operations / build` (+`strategy-direction / conceive+design` secondaries) | §13 |

Each re-mapping is justified in its entry's `ecf_rationale` field by
quoting the relevant ECF domain definition; no entry's identity (id, name,
definition, business_object, outcome) changes.

**Three investigation tracks opened** (no admission in this release):

- Investigation Track A: [Organizational Design](catalog-research/INV-ORGDESIGN-v0.1.md) (BC-SR-A001 §4 P1).
- Investigation Track B: [Enterprise Performance Management](catalog-research/INV-EPM-v0.1.md) (BC-SR-A001 §5 P1).
- Investigation Track C: [Relationship Management](catalog-research/INV-RELMGMT-v0.1.md) (BC-SR-A001 §6 P1-P2).

Each opens a research-led evidence investigation; admission is gated on the
catalog's own §12 review gates in a follow-on CR if the evidence supports it.

**Submittal-review infrastructure introduced:**
- New top-level folder [`submittal-reviews/`](submittal-reviews/) with
  README (lifecycle), TEMPLATE (cross-repo reusable template derived from
  BC-SR-A001), and the BC-SR-A001 review itself.
- New [`docs/REVIEWS.md`](docs/REVIEWS.md) per-release submittal-review
  commentary; linked from the README's `## Submittal Reviews` section.

**Repository/doc drift closed:**
- `README.md` Entity Definition table: `Catalog Status: planned` → `populated`.
- `metamodel-pointer.yaml` `catalog.status: planned` → `populated`.
- `README.md` Entity Definition table now disambiguates the three version
  pins (catalog version / metamodel pin / ECF conformance contract pin /
  architecture framework pin), addressing the apparent version-pin confusion
  BC-SR-A001 §19 raised. (The reviewer flagged "OpenDEAM v0.2.1" as a
  conflict; on investigation it is the architecture-framework pin, a
  separate version axis from the metamodel pin 1.0.0. Both pins are correct
  as written; the README now makes this explicit.)

**Deferred (not in this release):**
- Technology Management coordinate (BC-SR-A001 §12; medium-confidence; needs
  a formal boundary decision).
- ECF mapping rule refinement ("semantic center of gravity" vs "earliest
  initiation", BC-SR-A001 §14; method-level change).
- Knowledge Management candidate (BC-SR-A001 §7 P2; revisit after track A).
- Service / Quality / Stakeholder / EAM candidates (BC-SR-A001 §17 P2-P3;
  revisit after tracks A/B/C close).

**Tag**: `v1-alpha.5` (cut at this CR's merge commit).

## [v1-alpha.4] - 2026-09-09

**Patch** (CR-DEA-BC-11, PR #62). Release-pipeline consolidation: the
first-generation Node-based publication pipeline (CR-DEA-BC-06 +
CR-DEA-BC-10) is superseded by the framework Python
`scripts/generate_capability_map.py`, which natively emits the L0 ⊃ L1 ⊃ L2
capability × ECF map (HTML + A3 landscape PNG) via weasyprint + pdftoppm.
No Node, no Chrome, no playwright, no sharp. The release zip shrinks
from 12 files to 2 (`capability-map.html` + `capability-map-a3.png`).

**Consumer-facing migration:** any consumer pinned to retired artifacts
(`poster.svg/png`, `map.svg/png`, `catalog.svg/png`, `catalog.csv`,
`catalog.json`, `overlay.yaml/json`, `dependencies.yaml`, `MANIFEST.md`)
must migrate. See `docs/publication-pipeline.md` § "Migration from the
BC-06 / BC-10 pipeline" for the full replacement table. The framework
will gain a `--emit-sidecars` mode in a follow-up CR if any consumer
needs the lost machine-readable endpoints.

**Operational changes:** `scripts/publish.js`, `scripts/publish-mockups/`,
`scripts/lib/`, `scripts/render_map_png.mjs`, and
`.github/workflows/publish-latest.yml` are deleted from the live tree
(remain in git history). `package.json` becomes Python-only metadata;
`package-lock.json` is removed. The framework Python grows three new
CLI flags (`--png`, `--dpi`, `--page-{w,h}-mm`) for the native PNG
render path.

**Why a supersede (not an edit):** CR-DEA-BC-06 and CR-DEA-BC-10 are not
edited in place; their status flips to `Superseded` and a `superseded_by`
pointer is recorded. Per the standing CR-hygiene rule, landed CRs are
immutable.

**Catalog content:** no changes to entries, schema, or ECF enum. Patch
tier reflects tooling-only scope.

Tag: `v1-alpha.4`.

## [v1-alpha.3] - 2026-09-08

**Minor** (CR-DEA-BC-09, PR pending). Naming conformance refresh and
definition template formalization. TAXONOMY.md section 1 rule 2 clarified
(anchoring is semantic, not literal token containment; N-001/N-015 precedent
recorded); new section 1A formalizes the definition template ("The ability to
..." single sentence naming the business object) and the outcome-restatement
ban; sections 6/7 refreshed to the post-STRUCT-03 layout. Five entries renamed
to satisfy the clarified object-anchoring rule (normalization decisions
N-010..N-014; each renamed entry bumps 1.0.0 -> 2.0.0 per VERSIONING section
1.2, former names recorded in aliases, former ids not reused):

- Compliance Management -> Regulation Management
- Financial Management -> Financial Resource Management
- Innovation Management -> Idea Management
- Legal Management -> Legal Matter Management
- Resilience Management -> Continuity Management

Security Management reviewed-retained (N-015): the compound business object
(Asset/Information) precludes plain object-literal naming. MCSP view
references, overlay v0.2 canonical names, README narratives, and cross-referencing
entries (Risk, Financial Stewardship, Asset, Strategic Planning) updated
atomically. New `scripts/check_naming.py` enforces TAXONOMY sections 1/1A at
CI time (object-anchoring advisory only). Consumers pinning by entry id must
remap the five retired ids; consumers pinning the catalog label or the ECF
contract are unaffected. Tag: v1-alpha.3.

- Nested-capability-map release artifact: `scripts/generate_capability_map.py`
  + `scripts/render_map_png.mjs` wired into `publish-versioned.yml`. On every
  v* tag push the pipeline now emits `out/<label>/capability-map.html` (self-
  contained CSS-grid poster) and `out/<label>/capability-map-a3.png` (4961 x
  3508 px @ 300 dpi). Both flow into the release zip. The map reads ECF axes
  from `schemas/entity.schema.json` (canonical v2.5.0 enum); matrix row order
  mirrors `scripts/lib/grid.js` so the two never drift.

## [v1-alpha.2] - 2026-09-08

**Minor** (CR-DEA-BC-08, PR #53). Coordinate Technology Management - resolve
N-006. The N-006 held-unmapped decision was incorrect against the framework's
canonical grounding (`dea-metaframework/framework/domain-grounding.md` §3.6
and §3.2); technology is an enterprise **estate** whose stewardship belongs
in Strategy & Direction, parallel to Asset Management and Facility Management.
This change supersedes N-006 with **N-006R**: `dea:capability-technology-management`
moves to `strategy-direction × build` (primary) with secondaries at
`operate` and `improve`. Entry bumps 1.0.0 -> 1.1.0. The canonical ECF
overlay v0.2 (markdown + YAML) is updated to drop the held-unmapped
footnote and the `strategy-direction` row now carries Technology Management.
Provenance strikes: R-004 in `ADMISSION-REVIEW-v0.1.md` and the carried
forward item in `BC-02-CLOSEOUT.md` are marked superseded by N-006R.
Historical research artifacts (`candidates.yaml`, `normalization.yaml`,
`RESEARCH-REPORT-v0.1.md`, `ECF-OVERLAY-v0.1.md`, the v0.1 overlay YAML)
and the published `out/v1-alpha.0` snapshot are deliberately untouched
(provenance). Distinct primary coordinates rise 15 -> 16; held-unmapped
count falls 1 -> 0. No schema or CI change. Tag: v1-alpha.2.

## [v1-alpha.1] - 2026-09-07

**Minor** (CR-DEA-BC-07, PR #48). Substrate-neutral re-statement of the two
workforce capabilities, reconciling catalog content with the dea-metaframework
v2.4.0 rationale (ADR-ECF-002 section 5; CR-ECF-007). Names, business objects,
ECF coordinates, aliases, and pins unchanged (N-001 stands):
`dea:capability-workforce-management` and `dea:capability-workforce-planning`
now define the workforce as human and artificial agents, with the
specialization boundary enumerating biological and artificial workforce forms.
Both entries bump 1.0.0 -> 1.1.0. Also in this change:
`visuals/v09-ecf-coverage-map.svg` domain axis labels re-keyed to the v2.4.0
canonical set (six of seven were stale from pre-v2.3.0; same bug class as the
grid.js fix in CR-CATALOG-STRUCT-09 section 5), and the canonical ECF overlay
v0.2 domain table now cites the admitted capability by its canonical name.
Historical research artifacts and the `out/v1-alpha.0` snapshot are
deliberately untouched (provenance). Tag: v1-alpha.1.

### Operational follow-up (post-release)

- **PR #50 (CR-DEA-BC-07 §5 follow-up)**: adds `scripts/check_visual_domain_labels.py`
  and wires it into `catalog-conformance.yml`. R1 bans retired domain labels in
  any casing/form on `visuals/*.svg`; R2 requires any domain-axis visual (3+
  canonical domains referenced) to reference all seven. Canonical set is read
  from `schemas/entity.schema.json`, so the next enum wave only changes the
  schema and the guard follows.
- **PR #51 (publication pipeline code fix)**: three pre-existing bugs in
  `scripts/lib/load-entities.js` (hardcoded `docs/research/` paths; flat
  `capability-*.yaml` filter ignoring the STRUCT-03a nested layout) and
  `scripts/publish-mockups/{map,poster}.js` (missing `esc()` on
  `STAGES[c].display` and `DOMAINS[r].display` interpolations, causing Sharp
  PNG rasterization to fail on `xmlParseEntityRef`). Pipeline now produces
  11/11 artifacts for both `latest` and versioned targets; verified end-to-end
  on the `v1-alpha.1` tag push.
- **PR #52 (CR-DEA-BC-10)**: retires the `Dispatch to Pages aggregator` step
  from `publish-latest.yml` and `publish-versioned.yml` and the
  `dispatchEvent()` function from `scripts/publish.js`. The central aggregator
  repo never wired up a `sync-capabilities.yml` consumer for `capabilities-updated`
  /`capabilities-versioned`, and `secrets.DISPATCH_TOKEN` was unprovisioned,
  so the dispatch step failed on every run since at least 2026-09-05.
  Current distribution path is GitHub Releases only; `docs/publication-pipeline.md`
  is rewritten to record that and preserves the original Pattern A reference as
  §6 Historical reference. CR-DEA-BC-10 was originally numbered CR-DEA-BC-08
  on authorship; renumbered to BC-10 before merge because BC-08 had already
  shipped as the Technology Management N-006R coordinate (PR #53, 2026-09-08).
  Reissue note: this operational follow-up should appear under `[v1-alpha.1]`
  in any pre-2026-09-08 viewer; new viewers see it appended to the existing
  BC-01 wave.

## [v2.5.0-migration] - 2026-09-08

CR-BC-ECF-03 implementation: ECF Domain enum migration to the v2.5.0 canonical Domain set (carried by `technehub-labs/dea-metaframework` v2.5.0; CR-ECF-008 + ADR-ECF-003). One of seven Domains renamed: Domain 6 `OperationsAndEnablement` → `EnablementAndOperations` (kebab-case `operations-enablement` → `enablement-operations`; lowerCamelCase `operationsEnablement` → `enablementAndOperations`), driven by the Domain/Stage Orthogonality Stress Test. 44 files re-keyed (1 schema, 3 scripts, 26 entity YAMLs, 7 catalog-research files, 3 CR records). Also fixes the Domain 6 display label in `scripts/lib/grid.js` (the Domain-3 fix from CR-CATALOG-STRUCT-09 left Domain-6 stale). No content redistribution required (CR-ECF-008 §3.5).

**Files touched**: 44 files + 1 new CR carrier. See `change-requests/CR-BC-ECF-03.md` for the full mapping table and validation evidence.

**Unchanged**: Domain number (6), matrix position, semantic anchor (`Execution`), seven-Domain partition, seven lifecycle Stages, Stage 5 name (`Operate`), and the `ECF = Domain × Stage = 49 coordinates` construction.

## [v2.4.0-migration] - 2026-09-07

CR-CATALOG-STRUCT-09 implementation: ECF Domain enum migration to the
v2.4.0 canonical Domain set (carried by `technehub-labs/dea-metaframework`
v2.4.0; CR-ECF-007 + ADR-ECF-002). One of seven Domains renamed: Domain 3
`PeopleAndOrganization` -> `AgencyAndOrganization` (kebab-case
`people-organization` -> `agency-organization`), driven by the Substrate
Independence Stress Test. 39 files re-keyed (1 schema, 3 scripts, 26 entity
YAMLs, 7 catalog-research files, 2 CR records). Also fixes a pre-existing
bug in `scripts/lib/grid.js` where the six other Domain display labels were
stale from pre-v2.3.0. No content redistribution required (CR-ECF-007 §6.3).

## [v2.3.0-migration] - 2026-09-07

CR-CATALOG-STRUCT-08 implementation: ECF Domain enum migration to the
v2.3.0 canonical Domain set (carried by
`technehub-labs/dea-metaframework` v2.3.0; CR-ECF-006 + ADR-ECF-001).
Five of seven Domains renamed; one Domain replaced (Supply & Resources
-> Strategy & Direction). 53 files modified; no new entities admitted.

This is the **4th and final landing in the v2.3.0 wave** at the
metaframework + metamodel + catalogs tier (after metaframework,
metamodel, and the process catalog).

### Changed

- **Schema enum** (`schemas/entity.schema.json`): the `domain` enum in
  `ecfConformance` updated to the v2.3.0 set.
- **`scripts/check_ecf_conformance.py`**: `CANON_DOMAINS` set updated;
  5 of 7 values flipped; the conformance check now PASS on 26
  entries + MCSP view (verified post-migration).
- **`scripts/migrate_ecf_conformance.py`**: `DOMAIN_MAP` (kebab -> Pascal)
  and `DOMAIN_ID` (kebab -> lowerCamelCase) updated to the v2.3.0 set.
- **30 entity YAMLs** in `entities/v1-alpha/`: every
  `ecf.primary.domain`, `ecf.secondary.domain`, and
  `ecfConformance.canonicalReferences[].domain` updated to the v2.3.0
  kebab-case and PascalCase values.
- **MCSP view** (`mappings/specializations/view-telecom-mcsp.yaml` +
  `VIEW-TELECOM-MCSP.md`): updated.
- **8 catalog-research files** in `catalog-research/`:
  `preliminary-ecf-overlay.yaml`, `admission-review.yaml`,
  `admission-review-supplementary.yaml`,
  `admission-gate-closeout.yaml`, `normalization.yaml`,
  `ECF-OVERLAY-v0.1.md`, `RESEARCH-REPORT-v0.1.md`,
  `ADMISSION-REVIEW-v0.1.md`, `ADMISSION-REVIEW-SUPPLEMENTARY-v0.2.md`.
  Every reference to the v2.2.0 Domain names updated to v2.3.0.
- **1 CR file** (`change-requests/CR-DEA-BC-03.md`): narrative updated.
- **1 doc file** (`docs/FOUNDATIONS.md`): narrative updated.
- **1 lib file** (`scripts/lib/grid.js`): the grid layout labels
  re-keyed to the v2.3.0 display form.

### Not changed (out of scope for the v2.3.0 migration)

- **No new capabilities admitted.** The v2.3.0 wave is a pure rename.
- **The 6 open conflict flags (CAND-008, 010, 017, 018, 019, 028)**
  deliberately held in v0.2 remain unchanged. Their disposition
  references are now keyed to the v2.3.0 Domain names but the
  rationales and decisions are unchanged.
- **The v0.2 ECF Overlay re-derivation** (re-running the candidate
  set against the v2.3.0 Domain taxonomy) is a separate task that
  follows this PR. Parked but ready to dispatch.
- **The 4 pre-existing build-script path bugs** (regenerate_catalog.py,
  check_catalog_index.py, migrate_ecf_conformance.py all look for
  `tools/catalog-index-schema.json` but the schema lives in
  `catalog-index-schema/`) are pre-existing and not introduced by
  this PR.

### Verification

- `scripts/check_ecf_conformance.py`: **PASS** (26 entries + MCSP view
  conform).
- `scripts/check_versions.py`: **PASS** (26 entries conform to
  CR-DEA-BC-05 version discipline).
- `scripts/check_view_refs.py`: runs as expected.

## [STRUCT-03b] - 2026-09-05

### CR-CATALOG-STRUCT-03b: catalog repository standard adoption (research distribution)

Second half of the Business Capability catalog's adoption of the
catalog repository standard (CR-CATALOG-STRUCT-01). Completes the
migration by distributing the 33 research files formerly under
`docs/research/` into per-entity subtrees, `catalog-research/`, and
`visuals/`. After this CR, the BC catalog is fully `conforming`.

Distribution:
- 2 files (CAND-018 boundary decision, YAML + MD) move to
  `entities/v1-alpha/dea:capability-analytics-and-intelligence/research/`.
  The decision is the canonical evidence for analytics-and-intelligence.
- 31 catalog-wide files (CR-DEA-BC-02 execution artifacts: admission
  gates, evidence corpus, candidates, distinctness sweep, ECF overlay,
  corpus patch, normalization, specialization register, BC-02
  close-out, research report) move to a new top-level
  `catalog-research/` directory.
- 9 SVG visuals + 1 manifest move to a new top-level `visuals/`
  directory, separate from `docs/`. The manifest travels with the
  assets as `visuals/MANIFEST.yaml`.

Provenance:
- Per-entity `research/README.md` records the CAND-018 decision's origin.
- `catalog-research/README.md` documents the 8 research categories.
- `visuals/README.md` documents the 9 visual artifacts.

Directory cleanup:
- `docs/research/` becomes empty after all moves and is removed.

Catalog index:
- `CATALOG.yaml` regenerated; `research_registers[].files` for
  `dea:capability-analytics-and-intelligence` now lists the
  boundary decision + provenance README.

Verification:
- All 3 catalogue validators PASS.
- Regenerator --check exits 0.
- Gate --strict exits 0.
- Conformance --strict: 16/16 CSTs passed, 0 warnings.

## [STRUCT-03a] - 2026-09-05

### CR-CATALOG-STRUCT-03a: catalog repository standard adoption (layout + index)

First half of the Business Capability catalog's adoption of the
catalog repository standard (CR-CATALOG-STRUCT-01). Brings the catalog
to "conforming-but-research-not-distributed"; CR-CATALOG-STRUCT-03b
distributes the 33 research files into per-entity subtrees.

Step 1 (layout):
- 26 canonical entities moved from flat `entities/v1-alpha/capability-*.yaml`
  to per-entity subtrees `entities/v1-alpha/dea:capability-<name>/`.
- Each subtree has empty `research/`, `candidates/.gitkeep`, `retired/.gitkeep`
  state directories per the standard's section 5.

Catalog index + CI gate:
- `CATALOG.yaml` (machine-generated, ~7 KB) committed.
- `TEMPLATE_VERSION` (`0.1.0`) written; matches the canonical template.
- `scripts/regenerate_catalog.py`, `scripts/check_catalog_index.py`, and
  `catalog-index-schema/catalog-index-schema.json` vendored from
  `dea-metaframework/tools/` (CST-013/CST-014).
- New CI workflow `.github/workflows/catalog-conformance.yml` runs the
  standard's regenerator check, gate (--strict), and cross-repo
  conformance suite (CST-001..CST-016). The five existing workflows
  (`validate-entries`, `validate-allocation`, `ecf-conformance-consumer`,
  `publish-versioned`, `publish-latest`) are unchanged.
- `metamodel-pointer.yaml` extended with additive top-level catalog
  identity block (id/name/abbreviation/version/status/metamodel_version/owner).
  Existing nested `metamodel:` and `catalog:` blocks plus the existing
  root-level `description:` are untouched.

Bug fixes:
- `scripts/check_ecf_conformance.py` and `scripts/check_versions.py` now
  walk the subtree layout recursively and skip files under
  `research/`, `candidates/`, `retired/` per the standard's section 5.
- Empty `classifications/` and `contributions/` directories created
  with `.gitkeep` so the gate's cross-cutting sanity check passes.

Verification:
- All 3 catalog validators PASS (`check_ecf_conformance`: 26 entries,
  `check_versions`: 26 entries C0..C5, `check_view_refs`: no errors).
- Regenerator --check exits 0.
- Gate --strict exits 0.
- Conformance --strict: 16/16 CSTs passed, 0 warnings.

## [v1-alpha.0-pipeline-live] - 2026-09-04

### Publication pipeline live (CR-DEA-BC-06)

The catalog now publishes per-version artifacts (poster.svg + .png, map.svg +
.png, catalog.svg + .png, catalog.csv) plus semantic-data endpoints
(catalog.json, overlay.json, overlay.yaml, dependencies.yaml).

- `scripts/publish.js` generates the four artifacts from the live catalog
  state. Generation is pure-SVG-string composition plus `sharp` rasterisation
  (300 / 96 / 150 DPI for poster / map / catalog respectively).
- Distribution destinations: workflow-run artifacts (debug, every push) and
  GitHub Release (zip attached on `v*` tag pushes).
- Triggers: push to `main` (latest artifacts, mutable) + tag push matching
  `v*` (versioned artifacts, immutable).
- Provenance: CR-DEA-BC-06 (proposal md5 `8f460bcc53e776230724c523d4fa205f`;
  see `docs/publication-pipeline.md` for operations and `decisions.md` for
  the five recorded implementation decisions).
- First retroactive publish: `v1-alpha.0` at `4be5d7e1` lands on first
  invocation of the `publish-versioned` workflow (AC8).
- Scope of this entry: documentation + scripts + workflows. No entity,
  overlay, or dependencies change.
- Note: this section was originally filed as `[Unreleased]`; renamed to
  `[v1-alpha.0-pipeline-live]` on 2026-09-09 once CR-DEA-BC-06's
  implementation landed (commit `a632363b`). The distribution path was
  further amended on 2026-09-09 by CR-DEA-BC-10 (PR #52): the central-
  aggregator Pages `repository_dispatch` flow is retired; current
  distribution is GitHub Releases + workflow-run artifacts only. See the
  `[v1-alpha.1]` row's "Operational follow-up (post-release)" sub-list for
  the retirement record.

## [v1-alpha.0] - 2026-09-02

### Initial v1-alpha baseline

The catalog's first tagged baseline. Records the catalog's posture at the
moment CR-DEA-BC-05 (Catalogue Versioning and Change Procedure) was
accepted. 26 canonical first-order capabilities admitted, 1 specialization
view (MCSP) live, conformance gate enforced on every PR.

### Admitted (26)

The following 26 entries are admitted as `v1.0.0` per-entry identity versions
under `entities/v1-alpha/`:

| # | Capability | PR | Notes |
|---|---|---|---|
| 1 | Strategy | #25 | Admitted 2026-09-01 via CR-DEA-BC-02 + section 12 review. |
| 2 | Strategic Planning | #25 | Admitted 2026-09-01. |
| 3 | Enterprise Governance | #25 | Admitted 2026-09-01. |
| 4 | Customer Management | #25 | Admitted 2026-09-01. |
| 5 | Supplier Management | #25 | Admitted 2026-09-01. |
| 6 | Partner Management | #25 | Admitted 2026-09-01. |
| 7 | Offering Management | #25 | Admitted 2026-09-01. |
| 8 | Marketing | #25 | Admitted 2026-09-01. |
| 9 | Operations | #25 | Admitted 2026-09-01. |
| 10 | Financial Stewardship | #25 | Admitted 2026-09-01. |
| 11 | Financial Management | #25 | Admitted 2026-09-01. |
| 12 | People/Workforce Management | #25 | Admitted 2026-09-01. |
| 13 | Workforce Planning | #25 | Admitted 2026-09-01. |
| 14 | Information Management | #25 | Admitted 2026-09-01. |
| 15 | Risk Management | #25 | Admitted 2026-09-01. |
| 16 | Compliance Management | #25 | Admitted 2026-09-01. |
| 17 | Legal Management | #25 | Admitted 2026-09-01. |
| 18 | Security Management | #25 | Admitted 2026-09-01. |
| 19 | Sourcing and Procurement | #25 | Admitted 2026-09-01. |
| 20 | Asset Management | #25 | Admitted 2026-09-01. |
| 21 | Facility Management | #25 | Admitted 2026-09-01. |
| 22 | Change Management | #25 | Admitted 2026-09-01. |
| 23 | Technology Management | #25 | Admitted 2026-09-01; held-unmapped in ECF overlay v0.2. |
| 24 | Resilience Management | #32 | Supplementary admission (R-006); corpus patch SRC-013/014. |
| 25 | Innovation Management | #32 | Supplementary admission (R-007); corpus patch SRC-015/016. |
| 26 | Analytics and Intelligence | #32 | Supplementary admission (R-008); CAND-018 boundary decision. |

### Specialization views (1)

- `view-telecom-mcsp` (`view-telecom-mcsp@v1-alpha.0`): Mobile Communications
  Service Provider view. 4 admitted specializations (SPEC-001, SPEC-004,
  SPEC-005, SPEC-006); 22 inherited capabilities; 1 deferred decision
  (SPEC-D1). Maintained via CR-DEA-BC-04 (PR #27) and post-PR-#32
  inheritance update (PR #38).

### Conformance

- ECF Conformance Profile: `dea:ecf@1.0.0`. Conformance Gate (CG-001..006)
  live on every PR across this catalog and `dea-catalog-processes`. Drift
  detector: `PASS: 0 hard failures, 0 soft warning(s)`.
- Metamodel pin: `1.0.0`. Metamodel-side detector lives in
  `dea-metamodel/scripts/detect_drift.py`.

### Catalogs excluded from this changelog

This catalog declares a single dependency entry. The ECF contract pin
(`dea:ecf@1.0.0`) is held by the upstream `dea-metaframework`; the
metamodel pin (`1.0.0`) is held by `dea-metamodel`. Both are recorded in
[`dependencies.yaml`](dependencies.yaml).

### Deferred

- SPEC-D1 (CAND-005/CAND-006 unification): blocked on G5 reference corpus
  (Government Reference Models). See
  `docs/research/specialization-register.yaml` for the deferred-decisions
  registry.

### CRs that produced this baseline

- CR-DEA-BC-01 (First-Order Business Capability Method). Landed PR #13,
  PR #14. Method docs normative.
- CR-DEA-BC-01A (Capability classification reconciliation). Landed PR #3.
- CR-DEA-BC-02 (Evidence-Based First-Order Capability Investigation).
  Landed PR #4. Close-out: 19/19 DoD rows verified (PR #19).
- CR-DEA-BC-03 (Catalog Schema and CI Reconciliation). Landed PR #21,
  PR #22, PR #23.
- CR-DEA-BC-04 (Industry Specialization Framework). Landed PR #26,
  PR #27.
- CR-DEA-BC-05 (Catalogue Versioning and Change Procedure). Landed
  PR #39. This CHANGELOG is part of CR-DEA-BC-05's implementation.
- CR-DEA-MM-02 (upstream capability schema hygiene). Landed PR #158,
  PR #159.
- CR-ECF-CG-001..006 (ECF Conformance Gate tranche). Landed PR #9,
  PR #154, PR #155, PR #156, PR #35, PR #7.
- Supplementary admission review (CAND-023/029 fair run, CAND-018
  boundary). Landed PR #28, PR #29, PR #30, PR #31.
- Boundary decision (CAND-018). Landed PR #29.
- Corpus patch (continuity + innovation sources). Landed PR #28.
- Canonical admission of 23 first-order entries. Landed PR #25.
- Canonical admission of 24/25/26 (Resilience, Innovation, Analytics).
  Landed PR #32.

[v1-alpha.0]: https://github.com/technehub-labs/dea-catalog-business-capabilities/releases/tag/v1-alpha.0