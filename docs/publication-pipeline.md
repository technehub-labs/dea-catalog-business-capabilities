# Publication Pipeline

**Status**: Live (CR-DEA-BC-06, landed 2026-09-04; CR-DEA-BC-10, landed
2026-09-07, retired the dead central-aggregator dispatch steps). The
catalog publishes per-build artifacts (poster, map, catalog index,
semantic-data endpoints) on every push to `main` and every `v*` tag push.
CR-DEA-BC-10 was originally authored as CR-DEA-BC-08; renumbered to
BC-10 before merge because CR-DEA-BC-08 had already shipped as the
Technology Management N-006R coordinate (PR #53, 2026-09-08).
**Current distribution path**: workflow-run artifacts (debug) and GitHub
Releases. The previously-documented central-aggregator Pages path via
`repository_dispatch` is preserved as historical reference only; see
§6.

This document covers the operational procedure: how artifacts are produced,
where they are published, how to cut a new catalog version, and how to roll
back. The implementation spec is in
[`change-requests/CR-DEA-BC-06.md`](../../change-requests/CR-DEA-BC-06.md).
The dispatch retirement is in
[`change-requests/CR-DEA-BC-08.md`](../../change-requests/CR-DEA-BC-08.md).

## Architecture

```
dea-catalog-business-capabilities (push to main or v* tag)
   |
   | .github/workflows/publish-latest.yml
   | .github/workflows/publish-versioned.yml
   |
   |--- 1. node scripts/publish.js <target>
   |       writes to out/<target>/ on the workflow runner
   |
   |--- 2. latest build:
   |       uploaded as a workflow-run artifact
   |       (capabilities-latest-artifacts, retention 7d)
   |
   |--- 3. versioned build:
   |       zipped to out/<version-label>.zip
   |       uploaded as a workflow-run artifact
   |       (capabilities-versioned-artifacts, retention 30d)
   |       attached to a GitHub Release at
   |         technehub-labs/dea-catalog-business-capabilities/releases/tag/<label>
```

The catalog's distribution surface is the GitHub Releases list. A
consumer that pins to `dea:catalog/business-capabilities@v1-alpha.1` (Tier
2 of `docs/VERSIONING.md` §3) downloads the release zip from the
corresponding GitHub Release.

## Triggers

| Trigger | Workflow | Publishes to |
|---|---|---|
| push to `main` | `publish-latest.yml` | workflow-run artifact `capabilities-latest-artifacts` (7d retention) |
| push of tag `v*` | `publish-versioned.yml` | workflow-run artifact `capabilities-versioned-artifacts` (30d retention) + GitHub Release with attached zip |

## Artifacts produced per build

| File | Purpose |
|---|---|
| `poster.svg` + `poster.png` | A2 landscape print-ready poster, 300 DPI |
| `map.svg` + `map.png` | A4 landscape reference with capability IDs only, 96 DPI |
| `catalog.svg` + `catalog.png` | A4 portrait tabular reference, 150 DPI |
| `catalog.csv` | Machine-readable mirror of catalog rows |
| `catalog.json` | Flattened JSON of all entities |
| `overlay.json` | ECF overlay v0.2 verbatim |
| `overlay.yaml` | ECF overlay v0.2 verbatim (YAML source) |
| `dependencies.yaml` | Catalog manifest verbatim |
| `capability-map.html` | Nested L0 ⊃ L1 ⊃ L2 capability × ECF poster (self-contained CSS grid; versioned builds only) |
| `capability-map-a3.png` | A3 landscape rasterisation of the same map, 4961 × 3508 px @ 300 dpi (versioned builds only) |
| `MANIFEST.md` | Build summary + file inventory |

## How to cut a new catalog version

Follow [`docs/VERSIONING.md`](VERSIONING.md) §4 (the seven-step procedure),
specifically step 6:

1. Land the implementation PR(s) that triggered the bump. Verify CI green:
   `validate-entries`, `validate-allocation`, `ecf-conformance-consumer`.
2. Add a CHANGELOG.md row per the §4 step 5 rule.
3. **Tag**: `git tag -a v<N>-<word>.<P> -m "..." <merge-commit-sha>`
   (annotated tag per §4 step 6).
4. `git push origin v<N>-<word>.<P>`
5. The `publish-versioned.yml` job fires automatically:
   - generates `/v<N>-<word>.<P>/` artifacts
   - uploads the zip as a workflow-run artifact
   - creates or updates the GitHub Release at
     `releases/tag/v<N>-<word>.<P>` with the zip attached
6. Verify the release at
   `https://github.com/technehub-labs/dea-catalog-business-capabilities/releases/tag/v<N>-<word>.<P>`

## Version semantics

This catalog uses lettered-suffix versioning while in v1 (`v1-alpha.0`,
`v1-alpha.1`, `v1-bravo.0`, ...) and plain semver from v2 onward
(`v2.0`, `v2.1`, ...). See [`docs/VERSIONING.md`](VERSIONING.md) §1.1 for
the full rule and §2 for bump tiers.

## How to roll back

The pipeline is opt-in and stateless. To disable:

1. Delete or disable `.github/workflows/publish-latest.yml` and
   `.github/workflows/publish-versioned.yml`.
2. Existing published artifacts remain available as long as their
   GitHub Releases and workflow-run artifacts are not manually deleted.
   Retention for workflow artifacts is 7 days (latest) or 30 days
   (versioned); releases are indefinite until manually deleted.
3. Tag `v1-alpha.0` (`4be5d7e1`) is **immutable**; do not delete or rewrite
   it. If a `v1-alpha.0` publish was incorrect, delete the GitHub Release
   and (if reissued) tag the corrected build at a new patch label
   (`v1-alpha.1`).

## Operational notes

- The pipeline triggers on the path-filtered push events. If you push commits
  that don't touch `entities/`, `dependencies.yaml`, or `catalog-research/`,
  the workflow still fires but produces the same artifacts (idempotent).
- PNG rasterisation uses `sharp` (native Node). PDF generation is deferred
  to a follow-up CR (was scoped out of MVP per implementation decision
  D-2026-09-04-03).
- The versioned build zips `out/<label>/` into `out/<label>.zip`. The
  workflow-run artifact captures both, so consumers can download either
  form for as long as the artifact retention window allows.

## 6. Historical reference: central-aggregator Pages path

CR-DEA-BC-06 (proposal) specified Pattern A: a central aggregator
(`technehub-labs/technehub-labs.github.io`) that received
`repository_dispatch` events from this repo and copied artifacts into
`/capabilities/<label>/` for GitHub Pages hosting. The pattern matched
`dea-metamodel` PR #151 and `dea-metaframework` PR #7.

CR-DEA-BC-10 (2026-09-07) retired this path after the v1-alpha.1 release
surfaced three failures:

1. The aggregator repo had no `sync-capabilities.yml` workflow; the two
   dispatched events (`capabilities-updated`, `capabilities-versioned`)
   had no consumer.
2. The `secrets.DISPATCH_TOKEN` secret was unprovisioned on this repo;
   the dispatch step failed on every run with `GH_TOKEN: ` empty.
3. The dispatch was the final step; artifact generation, zipping, and
   the GitHub Release all succeeded regardless. The dead dispatch
   silently failed the workflow run on every push since at least
   2026-09-05.

The aggregator workflow file (`sync-capabilities.yml`) was never authored
in the aggregator repo. If a future CR revives this pattern, the path is
documented in the original CR-DEA-BC-06 §5.1 and the dispatch templates
in git history at tag `v1-alpha.0`. CR-DEA-BC-10 does not delete the
historical dispatch code from `scripts/publish.js` git history (only from
the live tree); the GitHub Actions workflows on `main` post-CR-DEA-BC-10
do not dispatch.

## References

- CR-DEA-BC-06 (proposal): [`change-requests/CR-DEA-BC-06.md`](../../change-requests/CR-DEA-BC-06.md)
- CR-DEA-BC-05 (versioning): [`change-requests/CR-DEA-BC-05.md`](../../change-requests/CR-DEA-BC-05.md)
- CR-ECF-CG-001 (gate definition): [`technehub-labs/dea-metaframework/change-requests/CR-ECF-CG-001.md`](https://github.com/technehub-labs/dea-metaframework/blob/main/change-requests/CR-ECF-CG-001.md)
- Proven precedent: [`dea-metamodel/.github/workflows/notify-pages.yml`](https://github.com/technehub-labs/dea-metamodel/blob/main/.github/workflows/notify-pages.yml)
- Central aggregator: [`technehub-labs/technehub-labs.github.io`](https://github.com/technehub-labs/technehub-labs.github.io)