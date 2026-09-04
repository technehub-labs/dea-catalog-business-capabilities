# Decisions log

Each entry records a material choice made during implementation, with the
date, the rationale, and the relevant CR(s). Pattern mirrors the org
convention (see `dea-metamodel/CHARTER.md`, `dea-architecture-framework/CHARTER.md`).

## D-2026-09-04-01 : Pages pattern: central aggregator dispatch

Chose central-aggregator Pages over per-repo `gh-pages` + `actions/deploy-pages@v4`.

Rationale:
- Aligns with the proven org pattern (`dea-metmodel` PR #151 +
  `dea-metaframework` PR #7).
- `DISPATCH_TOKEN` and `CROSS_REPO_TOKEN` secrets are already in use
  org-wide; per-repo Pages would require separate Pages provisioning per
  repo.
- Single source of truth for Pages host (`technehub-labs.github.io`) makes
  navigation + branding consistent.

Cost: one extra repo (the aggregator) is in the deployment chain. Mitigated
by the pattern being proven twice already.

Affected: CR-DEA-BC-06 (proposal diverged in §5.1 from this decision; the
implementation here supersedes the proposal's literal text).

## D-2026-09-04-02 : Generation stack: Node.js + js-yaml + sharp

Chose Node.js + `js-yaml` + `sharp` for SVG generation + rasterisation.
Rejected the proposal's "Node + D3.js" default.

Rationale:
- The mockup templates are pure SVG string composition (no D3 runtime
  features used; no transitions, no interactivity for the production
  artifacts).
- D3 brings ~ ~10 MB of `node_modules` for zero benefit on this output.
- `sharp` is native Node + native libvips; SVG-to-PNG rasterisation at
  arbitrary DPI is direct.

Affected: CR-DEA-BC-06 §7 (the proposal listed D3 as the chosen stack; this
implementation uses pure SVG composition instead). The decision is recorded
here for traceability.

## D-2026-09-04-03 : Rasteriser: sharp for SVG-to-PNG; PDF deferred

Chose `sharp` for SVG-to-PNG at 300 / 96 / 150 DPI. PDF generation deferred
to a follow-up CR.

Rationale:
- `sharp` rasterises SVG via `librsvg`; no browser binary required.
- Playwright PDF (the proposal's default) downloads ~ ~300 MB of browser
  binaries for a single PDF output. Not justified for a single-page PDF of
  the catalog table.
- PDF generation can be added in a follow-up using a small SVG-to-PDF
  tool or by reusing `sharp` (via `libvips` + a thin PDF wrapper).

Affected: CR-DEA-BC-06 §4.3 (catalog.pdf was listed as a deliverable;
deferred to a follow-up CR).

## D-2026-09-04-04 : Trigger semantics

Chose `push: branches: [main]` for `/latest/` and `push: tags: ['v*']` for
versioned builds. Two separate event types
(`capabilities-updated`, `capabilities-versioned`) flow to the aggregator.

Rationale:
- Mirrors CR-DEA-BC-05 §4 step 6 (the tag is the version bump; main pushes
  are in-flight development).
- Two event types allow independent rollback: a main-push regression
  doesn't disturb immutable versioned artifacts, and vice versa.

Affected: CR-DEA-BC-06 §6 (which proposed a single workflow with two jobs;
this implementation uses two workflows for clearer permission scopes and
dispatch semantics).

## D-2026-09-04-05 : Retroactive first publish

The `v1-alpha.0` tag (`4be5d7e1`) predates this pipeline. The first
`publish-versioned` job invocation publishes the artifacts for that
existing tag, satisfying AC8 of the proposal.

Rationale:
- Avoids requiring a new tag cut just to demonstrate the pipeline.
- Aligns with AC8 of CR-DEA-BC-06.

Affected: CR-DEA-BC-06 §10 AC8.