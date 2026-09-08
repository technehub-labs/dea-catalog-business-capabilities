# Business Capability Catalog Changelog

All notable changes to this catalog are recorded here. The format is based
on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) adapted for
CR-DEA-BC-05 versioning: each entry records the bump tier (major / minor /
patch), the scope, the rationale, the PR that landed it, and any tag.

The catalog uses `v<N>-<word>` versioning while in v1 (lettered-suffix
regime) and `v<N>.<M>` semver from v2 onward. See
[`docs/VERSIONING.md`](VERSIONING.md) for the normative procedure.

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

## [v1-alpha.2] - 2026-09-08

**Minor** (CR-DEA-BC-08, PR #49). Coordinate Technology Management - resolve
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

## [Unreleased] - 2026-09-05

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

## [Unreleased] - 2026-09-05

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

## [Unreleased] - 2026-09-04

### Publication pipeline live

The catalog now publishes per-version artifacts (poster.svg + .png, map.svg +
.png, catalog.svg + .png, catalog.csv) plus semantic-data endpoints
(catalog.json, overlay.json, overlay.yaml, dependencies.yaml) to GitHub
Pages via the central aggregator dispatch pattern (CR-DEA-BC-06).

- `scripts/publish.js` generates the four artifacts from the live catalog
  state. Generation is pure-SVG-string composition plus `sharp` rasterisation
  (300 / 96 / 150 DPI for poster / map / catalog respectively).
- Three publication destinations: GitHub Pages (`/latest/`, `/<version>/`),
  GitHub Release (zip attached on tag pushes), semantic-data endpoints.
- Triggers: push to `main` (latest artifacts, mutable) + tag push matching
  `v*` (versioned artifacts, immutable).
- Provenance: CR-DEA-BC-06 (proposal md5 `8f460bcc53e776230724c523d4fa205f`;
  see `docs/publication-pipeline.md` for operations and `decisions.md` for
  the five recorded implementation decisions).
- First retroactive publish: `v1-alpha.0` at `4be5d7e1` lands on first
  invocation of the `publish-versioned` workflow (AC8).
- Scope of this entry: documentation + scripts + workflows. No entity,
  overlay, or dependencies change.

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

[Unreleased]: https://github.com/technehub-labs/dea-catalog-business-capabilities/compare/v1-alpha.0...HEAD
[v1-alpha.0]: https://github.com/technehub-labs/dea-catalog-business-capabilities/releases/tag/v1-alpha.0