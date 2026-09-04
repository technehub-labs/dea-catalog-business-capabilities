# Business Capability Catalog Changelog

All notable changes to this catalog are recorded here. The format is based
on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) adapted for
CR-DEA-BC-05 versioning: each entry records the bump tier (major / minor /
patch), the scope, the rationale, the PR that landed it, and any tag.

The catalog uses `v<N>-<word>` versioning while in v1 (lettered-suffix
regime) and `v<N>.<M>` semver from v2 onward. See
[`docs/VERSIONING.md`](VERSIONING.md) for the normative procedure.

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