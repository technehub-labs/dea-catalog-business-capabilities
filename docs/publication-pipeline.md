# Publication Pipeline

**Status**: Live (CR-DEA-BC-06, landed 2026-09-04). The catalog now publishes
per-version artifacts (poster, map, catalog index, semantic-data endpoints) on
every push to `main` and every `v*` tag push.

This document covers the operational procedure: how artifacts are produced,
where they are published, how to cut a new catalog version, and how to roll
back. The implementation spec is in
[`change-requests/CR-DEA-BC-06.md`](../../change-requests/CR-DEA-BC-06.md).

## Architecture

Pattern A: central-aggregator Pages with `repository_dispatch`. Matches the
proven pattern in `dea-metamodel` PR #151 and `dea-metaframework` PR #7.

```
dea-catalog-business-capabilities (push to main or v* tag)
   |
   | .github/workflows/publish-latest.yml
   | .github/workflows/publish-versioned.yml
   |
   |--- 1. node scripts/publish.js <target>
   |       writes to out/<target>/
   |
   |--- 2. repository_dispatch (event-type: capabilities-updated
   |                         or capabilities-versioned)
   |       token: secrets.DISPATCH_TOKEN
   |
   v
technehub-labs/technehub-labs.github.io
   |
   | .github/workflows/sync-capabilities.yml
   |
   |--- 3. checkout both repos
   |       copy artifacts from out/<target>/ into /capabilities/<target>/
   |       commit to aggregator main
   |
   v
GitHub Pages: https://technehub-labs.github.io/capabilities/<target>/
```

## Triggers

| Trigger | Workflow | Event type | Publishes to |
|---|---|---|---|
| push to `main` | `publish-latest.yml` | `capabilities-updated` | `/capabilities/latest/` (mutable) |
| push of tag `v*` | `publish-versioned.yml` | `capabilities-versioned` | `/capabilities/v<N>-<word>.<P>/` (immutable) |

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
   - creates or updates the GitHub Release
   - dispatches `capabilities-versioned` to the aggregator
6. Verify at `https://technehub-labs.github.io/capabilities/v<N>-<word>.<P>/`

## Version semantics

This catalog uses lettered-suffix versioning while in v1 (`v1-alpha.0`,
`v1-alpha.1`, `v1-bravo.0`, ...) and plain semver from v2 onward
(`v2.0`, `v2.1`, ...). See [`docs/VERSIONING.md`](VERSIONING.md) §1.1 for
the full rule and §2 for bump tiers.

## How to roll back

The pipeline is opt-in and stateless. To disable:

1. Delete or disable `.github/workflows/publish-latest.yml` and
   `.github/workflows/publish-versioned.yml`.
2. Existing published artifacts remain live at `/capabilities/<version>/`
   until the aggregator commits are reverted (or until the GitHub Pages cache
   expires).
3. Tag `v1-alpha.0` (`4be5d7e1`) is **immutable**; do not delete or rewrite
   it. If a `v1-alpha.0` publish was incorrect, delete the GitHub Release and
   revert the aggregator's `capabilities/v1-alpha.0/` commit.

## Operational notes

- The pipeline triggers on the path-filtered push events. If you push commits
  that don't touch `entities/`, `dependencies.yaml`, or `docs/research/`, the
  workflow still fires but produces the same artifacts (idempotent).
- Two events (`capabilities-updated`, `capabilities-versioned`) are
  intentionally separate: `/latest/` rebuilds should not retrigger
  versioned-page regeneration, and vice versa.
- The `secrets.DISPATCH_TOKEN` secret must be set on this repo. Without it,
  the dispatch step fails but the local artifacts still emit. The aggregator
  sync is best-effort.
- PNG rasterisation uses `sharp` (native Node). PDF generation is deferred
  to a follow-up CR (was scoped out of MVP per implementation decision
  D-2026-09-04-03).

## References

- CR-DEA-BC-06 (proposal): [`change-requests/CR-DEA-BC-06.md`](../../change-requests/CR-DEA-BC-06.md)
- CR-DEA-BC-05 (versioning): [`change-requests/CR-DEA-BC-05.md`](../../change-requests/CR-DEA-BC-05.md)
- CR-ECF-CG-001 (gate definition): [`technehub-labs/dea-metaframework/change-requests/CR-ECF-CG-001.md`](https://github.com/technehub-labs/dea-metaframework/blob/main/change-requests/CR-ECF-CG-001.md)
- Proven precedent: [`dea-metamodel/.github/workflows/notify-pages.yml`](https://github.com/technehub-labs/dea-metamodel/blob/main/.github/workflows/notify-pages.yml)
- Central aggregator: [`technehub-labs/technehub-labs.github.io`](https://github.com/technehub-labs/technehub-labs.github.io)