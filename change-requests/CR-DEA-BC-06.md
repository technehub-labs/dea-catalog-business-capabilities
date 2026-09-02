---
cr: CR-DEA-BC-06
title: Publication Pipeline and Versioned Artifacts
status: proposed
date: 2026-09-02
author: technehub-labs (working folder business-capabilities)
target_repo: dea-catalog-business-capabilities
consumer_repos:
- dea-catalog-business-capabilities (self, primary)
- dea-catalog-processes (parallel consumer; may adopt by analogy)
metmodel_pin: 1.0.0
ecf_contract_pin: dea:ecf@1.0.0
mockups:
- poster: business-capabilities/18_publication/posters/v1-alpha.0/poster.svg
- map: business-capabilities/18_publication/maps/v1-alpha.0/map.svg
- catalog: business-capabilities/18_publication/catalogs/v1-alpha.0/catalog.svg
related:
- CR-DEA-BC-01 (method; section 35 visuals precedent)
- CR-DEA-BC-02 (research artifacts; section 35 nine data-derived SVGs)
- CR-DEA-BC-04 (specialization framework; MCSP view precedent)
- CR-DEA-BC-05 (catalogue versioning and change procedure; bump rules, three-tier pin scheme, tag format)
- CR-ECF-CG-001..006 (ECF Conformance Gate tranche)
- CR-DEA-MM-02 (upstream capability schema hygiene)
---

# CR-DEA-BC-06: Publication Pipeline and Versioned Artifacts

## 1. Problem

The catalog has 26 canonical first-order capabilities, an MCF (ECF) overlay,
a specialization view, and a version discipline (CR-DEA-BC-05). What it does
not yet have is a way to **publish** that catalog as a versioned artifact set
that:

- consumers (catalog users, downstream tooling, governance reviewers) can
  browse and bookmark without checking out the repo;
- governance reviewers can hand to non-engineering stakeholders as a
  self-contained, versioned reference (no "go look at the YAML");
- the org can archive per version with the rest of the release assets;
- the catalog can evolve without breaking consumers pinned to a specific
  version label.

CR-DEA-BC-02 §35 already produced nine data-derived SVGs as research
artifacts, but those were catalog-state-of-the-time research visuals, not
publishable artifacts. They are useful as evidence, not as deliverables.

## 2. Goal

Establish a publication pipeline that, per catalog version (CR-DEA-BC-05
`v<N>-<word>.<P>`), produces and publishes three artifacts:

1. **Poster**: a print-quality A2 visual with the ECF 7×7 grid backdrop and
   capability tiles (ID + name + capability_layer color stripe), sidebar
   status panel, header + footer bands with version + provenance.
2. **Map**: a screen-friendly A4-landscape reference with the ECF grid
   backdrop and capability IDs only, for quick lookup and embedding in
   documents.
3. **Catalog index**: a tabular reference (A4 portrait SVG + CSV) of all
   canonical entries with primary/secondary ECF coordinates,
   capability_layer, related_capabilities, evidence sources.

Each artifact is published to:

- a **GitHub Pages** site at `https://technehub-labs.github.io/dea-catalog-business-capabilities/v<N>-<word>.<P>/`;
- a **GitHub Release** at `v<N>-<word>.<P>` with the artifacts attached as a
  zip;
- **semantic-data endpoints** alongside the catalog (`catalog.json`,
  `overlay.json`, `dependencies.yaml`) so consumers can fetch the canonical
  state programmatically.

The pipeline triggers on every push to `main` (latest artifacts always live)
AND on every `v<N>-<word>.<P>` tag (immutable archive at the version).

## 3. Non-goals

- **Not a metamodel change.** Metamodel version semantics are owned upstream.
  This CR's relationship to the metamodel is "pin and respect".
- **Not a process-catalog change.** The process catalog may adopt by
  analogy, but CR-DEA-BC-06 ships the procedure for business capabilities.
- **Not a release-engineering overhaul for the whole org.** Other repos may
  adopt the pattern in their own CRs; this CR is the business-capability
  case study, not an org-wide mandate.
- **Not a content editorial process.** This CR is the publication
  *infrastructure*; what to publish and how to curate the content is owned
  by CR-DEA-BC-01 (method) and CR-DEA-BC-05 (versioning).
- **Not a redesign of the catalog schema.** The artifacts are derived
  views; the source of truth remains the entries in `entities/v1-alpha/`
  plus the overlay v0.2 YAML.

## 4. Artifact specifications

### 4.1 Poster (A2 landscape, 1684×1191 at 100 DPI; 300 DPI print-ready)

Source-of-truth SVG generated from `entities/v1-alpha/*.yaml` +
`docs/research/ecf-overlay-v0.2.yaml` + `dependencies.yaml`. Layout:

- Header band (~130px): catalog title + subtitle + version badge
  (e.g., `v1-alpha.0`).
- Body grid (~880px): 7 ECF domains × 7 ECF stages, capability tiles stacked
  in cells.
- Sidebar (~280px): canonical entry count, cells used, specializations,
  deferred, held-unmapped, capability_layer legend.
- Footer band (~180px): provenance (ECF contract pin, metamodel pin,
  method CR, specialization CR), source URL, semantic note about empty
  cells.

Capability tile content:

- `CAND-NNN` (monospace, capability_layer border color).
- Capability name (truncated to 24 characters).
- "+N sec" badge if secondary coordinates exist.

PNG rasterisation at 300 DPI for archival print.

### 4.2 Map (A4 landscape, 1400×800)

Lighter weight: same ECF grid, capability IDs only, no names. Single-page
reference for embedding in slide decks, papers, governance documents. PNG
plus SVG. Slim header with the catalog version + summary stats; slim footer
with provenance URL and held-unmapped note.

### 4.3 Catalog index (A4 portrait, 1240×1754)

Tabular reference. Columns:

- `candidate_id` (CAND-NNN)
- `Capability` (display name)
- `capability_layer` (strategic / operational / support)
- `Primary ECF` (domain / stage)
- `Secondary` (domain / stage, comma-separated)
- `Related capabilities` (top 3, comma-separated)
- (CSV: full `entry_id`, `lifecycle_status`)

26 rows; alternating row fill for eye-tracking; held-unmapped entry shows
`held-unmapped` in the Primary ECF column.

CSV mirror at `catalog.csv`: same fields plus machine-readable extras
(`entry_id`, `lifecycle_status`, evidence source IDs). Used by downstream
consumers as a fetch-stable machine form.

## 5. Publication destinations

### 5.1 GitHub Pages

Per-version site at `v<N>-<word>.<P>/`. Index page lists the three artifacts
with links to the SVG, PNG, CSV, and PDF (catalog only). Latest artifacts
live at `/latest/` (mutable; reflects the most recent push to `main`).

Pages is built by `actions/deploy-pages@v4` from the `gh-pages` branch
populated by the publication workflow. No custom domain required; the
default `technehub-labs.github.io` host is sufficient.

### 5.2 GitHub Releases

On every `v<N>-<word>.<P>` tag, the publication workflow creates (or
updates) a GitHub Release with the artifacts attached as a single zip:
`dea-catalog-business-capabilities-v<N>-<word>.<P>.zip` containing
`poster.svg`, `poster.png`, `map.svg`, `map.png`, `catalog.svg`,
`catalog.pdf`, `catalog.csv`, plus a `MANIFEST.md` listing all artifacts
and their generation timestamps.

Release notes are auto-generated from CHANGELOG.md between the previous
tag and the current tag.

### 5.3 Semantic-data endpoints

Three machine-readable files exposed at the versioned URL:

- `catalog.json`: full content of every entry under `entities/v1-alpha/`
  (flattened to a single JSON document).
- `overlay.json`: content of `docs/research/ecf-overlay-v0.2.yaml`.
- `dependencies.yaml`: verbatim copy of `dependencies.yaml` (CR-DEA-BC-05).

These are exposed for programmatic consumption (downstream tooling can
fetch `https://.../v1-alpha.0/catalog.json` instead of cloning).
They are not a content source; the YAML in the repo remains canonical.

## 6. Pipeline triggers

Two trigger paths, both feeding the same generation job:

### 6.1 Push to `main`

A merge to `main` regenerates the three artifacts from the current
catalog state and publishes them to the `/latest/` Pages path. The
artifacts in `/latest/` always reflect the most recent merge.

This is fast feedback. The latest artifacts are mutable.

### 6.2 Push of `v<N>-<word>.<P>` tag

A tag push regenerates the artifacts and publishes them to the
`/v<N>-<word>.<P>/` Pages path, **and** creates/updates a GitHub Release.
Tag-pushed artifacts are immutable; the version becomes an archival
reference point.

The tag is cut manually per CR-DEA-BC-05 §7 step 6 (after the
implementation PR merges). The publication workflow owns step 7 (the
artifact publish + release).

## 7. Generation stack

User-confirmed (2026-09-02): **Node.js + D3.js**.

- **Why Node + D3**: more expressive SVG (interactive on hover for the
  map, JSON-driven from the overlay YAML, future-proof for animated
  transitions if asked for). The CI workflow can run a Node step natively.
- **Source-of-truth inputs**: `entities/v1-alpha/*.yaml` (parsed to JSON
  via `js-yaml`), `docs/research/ecf-overlay-v0.2.yaml`, `dependencies.yaml`,
  `CHANGELOG.md` (for release-notes generation).
- **Outputs**: SVG (via D3-driven text generation), PNG (via
  `sharp`/`@resvg/resvg-js` or Playwright headless screenshot), PDF (via
  Playwright `page.pdf()` or `puppeteer`).
- **Build orchestrator**: a single `scripts/publish.js` entry point that
  takes a target (latest, tag-name) and runs the full generation pipeline.
- **CI step**: a new workflow `publish-artifacts.yml` with two jobs, one
  per trigger path, both calling `node scripts/publish.js`.

### 7.1 Mockup source

The three mockups in `business-capabilities/18_publication/` (poster.svg,
map.svg, catalog.svg) are the visual reference for the publication style.
The Node generator must produce equivalent output, not a regression.

## 8. Current posture (publication state at CR-acceptance)

This section declares the initial publication state:

- **Source**: `technehub-labs/dea-catalog-business-capabilities@main` (tag
  `v1-alpha.0`; merge commit `4be5d7e`).
- **Mockups**: three SVGs already generated in `business-capabilities/18_publication/v1-alpha.0/`:
  - `poster.svg` (24,515 bytes; 14 of 49 cells used; 26 capabilities).
  - `map.svg` (12,857 bytes; IDs only).
  - `catalog.svg` (17,621 bytes; 26 rows tabular; + `catalog.csv` 5,457 bytes).
- **Publication pipeline**: not yet built; this CR's implementation builds
  it.
- **Pages site**: not yet provisioned; this CR's implementation provisions
  it.
- **Releases**: not yet cut; the `v1-alpha.0` tag exists
  (`4be5d7e`) but the GitHub Release is created by this CR's
  implementation.

## 9. Implementation plan

The implementation of CR-DEA-BC-06 (separate PR(s) after this proposal is
accepted) does the following:

1. **`scripts/publish.js`**: Node entry point. Reads YAML inputs, runs D3
   generators for poster / map / catalog, rasterises to PNG (300 DPI for
   poster; 96 DPI for map; 150 DPI for catalog), generates PDF for
   catalog, emits semantic-data JSON files (`catalog.json`, `overlay.json`,
   copies `dependencies.yaml`), and emits a `MANIFEST.md`.
2. **`.github/workflows/publish-artifacts.yml`**: two-job workflow:
   `publish-latest` (push to main → publish mutable latest to Pages),
   `publish-versioned` (tag push → publish immutable versioned + create
   GitHub Release).
3. **`scripts/publish-mockups/`**: the three mockup generators, kept in
   sync with `scripts/publish.js` so that the design and the production
   generator share the same input layer.
4. **Pages site**: `gh-pages` branch populated with `/latest/` and
   `/v<N>-<word>.<P>/` directories. Index page lists all three artifacts.
5. **First publish**: tag `v1-alpha.0` already exists (`4be5d7e`); the
   implementation PR triggers the publish-versioned job which retroactively
   publishes `v1-alpha.0` artifacts + creates the GitHub Release.
6. **CHANGELOG entry**: the implementation adds a row to CHANGELOG.md
   declaring the publication pipeline is live and the `v1-alpha.0`
   artifacts are available.

## 10. Acceptance criteria

| AC | Criterion |
|---|---|
| AC1 | `scripts/publish.js` runs end-to-end with no errors |
| AC2 | Three artifacts (poster, map, catalog) match the mockup style |
| AC3 | PNG rasterisation produces valid 300/96/150 DPI outputs |
| AC4 | Semantic-data endpoints (`catalog.json`, `overlay.json`, `dependencies.yaml`) match the in-repo sources |
| AC5 | Push-to-main trigger publishes to `/latest/` and is idempotent |
| AC6 | Tag-push trigger publishes to `/v<N>-<word>.<P>/` AND creates GitHub Release with zip |
| AC7 | Pages site is provisioned and the index page lists the artifacts |
| AC8 | First publish retroactively publishes `v1-alpha.0` (the existing tag at `4be5d7e`) |
| AC9 | CHANGELOG entry declares the publication pipeline is live |
| AC10 | The pipeline holds for the next 5 catalog version bumps |

## 11. Open questions for review

| # | Question | Proposed default |
|---|---|---|
| Q1 | Rasteriser library? | sharp + @resvg/resvg-js for SVG; Playwright for PDF (catalog only). |
| Q2 | Pages site theme? | Minimal CSS; no framework. The artifacts carry the design. |
| Q3 | Pages site custom domain? | Default `technehub-labs.github.io/dea-catalog-business-capabilities`. Custom domain is a separate decision. |
| Q4 | Should the publication job run on PRs (preview deploys)? | Yes (per-PR previews at `/pr/<num>/`). Optional; can be deferred. |
| Q5 | Should the catalog also publish an EPUB or other mobile format? | No (not requested; can be added later). |

## 12. References

- `dea-catalog-business-capabilities/entities/v1-alpha/*.yaml`: catalog entries
- `dea-catalog-business-capabilities/docs/research/ecf-overlay-v0.2.yaml`: ECF overlay
- `dea-catalog-business-capabilities/dependencies.yaml`: manifest
- `dea-catalog-business-capabilities/CHANGELOG.md`: version timeline
- `dea-catalog-business-capabilities/docs/VERSIONING.md`: versioning procedure
- `business-capabilities/18_publication/posters/v1-alpha.0/poster.svg`: poster mockup
- `business-capabilities/18_publication/maps/v1-alpha.0/map.svg`: map mockup
- `business-capabilities/18_publication/catalogs/v1-alpha.0/catalog.svg`: catalog mockup
- `business-capabilities/18_publication/catalogs/v1-alpha.0/catalog.csv`: catalog CSV mirror