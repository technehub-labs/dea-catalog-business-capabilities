# CR-DEA-BC-10: Retire Dead Pages-Aggregator Dispatch Steps

**Status**: Landed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-09
**Landing commit**: `4d5067ea041efa824b1cc079b915dfaa4be87e28` (PR #52)
**Depends on**: CR-DEA-BC-06 (publication pipeline, accepted 2026-09-04); CR-DEA-BC-07 (v1-alpha.1 release, 2026-09-07)
**Related**: PRs #48, #50, #51 (the v1-alpha.1 wave)

## 1. What this CR is

The publication pipeline (CR-DEA-BC-06) ships two CI workflows that, after
generating artifacts, dispatch `repository_dispatch` events to a central
GitHub Pages aggregator (`technehub-labs/technehub-labs.github.io`):

- `publish-latest.yml` dispatches `capabilities-updated` on push to `main`.
- `publish-versioned.yml` dispatches `capabilities-versioned` on push of `v*` tags.

This CR retires those dispatch steps. Three findings from the v1-alpha.1
release made the dispatch path untenable as the publication record:

1. **The aggregator does not listen.** `technehub-labs/technehub-labs.github.io`
   has workflows `sync-metaframework.yml` and `sync-metamodel.yml` only; there
   is no `sync-capabilities.yml`. The two events the catalog dispatches
   (`capabilities-updated`, `capabilities-versioned`) have no consumer.
2. **The dispatch secret is unprovisioned.** Both workflows read
   `secrets.DISPATCH_TOKEN`, which has never been set on this repo.
   Verified empirically by inspecting the GitHub Actions secrets list
   (2026-09-07); the `Dispatch to Pages aggregator` step has been failing
   on every run since at least 2026-09-05 with `GH_TOKEN: ` empty and
   `gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN
   environment variable`.
3. **The publish workflow's *core job* succeeded regardless.** The
   artifact generation, zip, and GitHub Release creation all completed
   cleanly on the v1-alpha.1 run. Only the final dispatch step failed.
   `gh release list` shows `v1-alpha.1` with a 488KB zip attached. The
   catalog is being published correctly; the dispatch was dead
   infrastructure.

The conclusion: the dispatch steps document a path that does not exist in
the live org, fail every run, and were carried forward as a stale artifact
of the original CR-DEA-BC-06 proposal. The catalog's actual current
publication path is **GitHub Releases only** (plus the workflow-run
artifact for debugging). This CR removes the dead steps and rewrites the
docs to record the actual path.

## 2. Goal

- Remove the two `Dispatch to Pages aggregator` steps (workflows and the
  `dispatchEvent` function in `scripts/publish.js`).
- Rewrite `docs/publication-pipeline.md` to record the actual current
  publication path: workflow artifacts + GitHub Releases. The Pages
  aggregator pattern is preserved as historical reference, not the
  present state.
- Update the `change-requests/README.md` line for CR-DEA-BC-06 to mark
  the dispatch path as retired by this CR (CR-DEA-BC-10).
- Add a `## Changelog` style entry to the CHANGELOG.

## 3. Non-goals

- No re-provisioning of `secrets.DISPATCH_TOKEN`. That requires a
  maintainer decision on whether the aggregator pattern will be revived
  in another form. This CR is the honest "retire" choice per user
  direction (eaojnr, 2026-09-07).
- No changes to artifact generation, schema, entities, or coordinates.
- No rebuild of `out/v1-alpha.1/` or `out/latest/`; both are local to
  workflow runners and were never pushed as branches. The v1-alpha.1
  release asset remains at
  https://github.com/technehub-labs/dea-catalog-business-capabilities/releases/tag/v1-alpha.1.

## 4. Change set

- `.github/workflows/publish-latest.yml`: drop the `Dispatch to Pages
  aggregator` step and update the workflow's header comment.
- `.github/workflows/publish-versioned.yml`: same.
- `scripts/publish.js`: drop `dispatchEvent()`, its two call sites, and
  update the file's header comment.
- `docs/publication-pipeline.md`: rewrite §1 (Architecture), the
  `Triggers` table, the §5 step 5 entry, and the §Operational notes to
  remove the aggregator from the current path.
- `change-requests/README.md`: add CR-DEA-BC-10 row and update the
  CR-DEA-BC-06 row's "central-aggregator Pages" note.
- `CHANGELOG.md`: add a `v1-alpha.1` post-release entry noting the
  dispatch retirement (the v1-alpha.1 catalog version itself stands;
  this is an operational follow-up).

## 5. Verification

- `gh run list --workflow=publish-versioned.yml --limit 1` and
  `publish-latest.yml` after merge should both show `success` (the
  failures will vanish because the failing step is gone).
- The GitHub Release for `v1-alpha.1` continues to exist with its zip.
- `node scripts/publish.js latest` locally runs cleanly and emits no
  dispatch warnings.

## 6. References

- CR-DEA-BC-06 (publication pipeline, accepted 2026-09-04).
- PR #48 (CR-DEA-BC-07 substrate-neutral re-statement; v1-alpha.1 tag).
- PR #50 (visual domain-label conformance guard).
- PR #51 (publication pipeline code fix: nested entities + escaped display text).
- `docs/publication-pipeline.md` (this CR rewrites it).