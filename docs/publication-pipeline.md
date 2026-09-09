# Publication Pipeline

**Status**: Live. The catalog publishes an L0 ⊃ L1 ⊃ L2 nested ECF capability
map (HTML + A3 landscape PNG) on every `v*` tag push. Distribution is via
GitHub Releases only.

This document supersedes the CR-DEA-BC-06 + CR-DEA-BC-10 pipeline
(`scripts/publish.js`, `scripts/publish-mockups/*`, `scripts/render_map_png.mjs`,
`scripts/lib/*`, `.github/workflows/publish-latest.yml`). Those files were
retired on 2026-09-09 in favour of a single canonical artifact family:
the framework Python `scripts/generate_capability_map.py`.

The framework Python reads the catalog's own `entities/v1-alpha/` YAMLs
and the canonical ECF enum baked into `schemas/entity.schema.json`. The
ECF axis is therefore always in lockstep with the schema, and the rendered
map never drifts from the canonical domain / stage vocabulary.

## Architecture

```
dea-catalog-business-capabilities (push of v* tag)
   |
   | .github/workflows/publish-versioned.yml
   |
   |--- 1. python3 scripts/generate_capability_map.py
   |       --label <version> --out capability-map.html --png capability-map-a3.png
   |       writes to out/<version>/ on the workflow runner
   |
   |--- 2. zipped to out/<version>.zip
   |
   |--- 3. uploaded as a workflow-run artifact
   |       (capabilities-versioned-artifacts, retention 30d)
   |
   |--- 4. attached to a GitHub Release at
   |       technehub-labs/dea-catalog-business-capabilities/releases/tag/<label>
```

The catalog's distribution surface is the GitHub Releases list. A
consumer that pins to `dea:catalog/business-capabilities@v1-alpha.1` (Tier
2 of `docs/VERSIONING.md` §3) downloads the release zip from the
corresponding GitHub Release.

## Triggers

| Trigger | Workflow | Publishes to |
|---|---|---|
| push of tag `v*` | `publish-versioned.yml` | workflow-run artifact `capabilities-versioned-artifacts` (30d retention) + GitHub Release with attached zip |

There is no `publish-latest.yml`. Mutable "latest" artifacts are no longer
emitted: every push to `main` triggers the conformance / gate workflows
only. A new tag is required to publish a new artifact bundle.

## Artifacts produced per build

| File | Purpose |
|---|---|
| `capability-map.html` | Nested L0 ⊃ L1 ⊃ L2 capability × ECF poster; self-contained CSS-Grid HTML; no external assets. Renders correctly in any modern browser. |
| `capability-map-a3.png` | A3 landscape rasterisation of the same map, 4961 × 3508 px @ 300 dpi (print-quality). Generated natively via weasyprint + pdftoppm; no Chrome / playwright required. |

## HTML / PNG render pipeline

The framework Python is a single CLI that emits both the HTML and the PNG:

```
python3 scripts/generate_capability_map.py \
    --label <version> \
    --out  <out>/capability-map.html \
    --png  <out>/capability-map-a3.png \
    --dpi  300
```

Internally:

1. Reads `entities/v1-alpha/<id>/<id>.yaml` for each canonical entity.
3. Reads the canonical ECF domain + stage enums from
   `schemas/entity.schema.json#definitions/ecf_coordinate.properties.{domain,stage}.enum`.
4. Builds the 7 × 7 L0 ⊃ L1 ⊃ L2 CSS-Grid matrix (each entity rendered as a
   chip inside the cell matching its `ecf.primary`).
5. Writes `capability-map.html` (self-contained).
6. When `--png` is supplied: composes the HTML to a single-page A3
   landscape PDF via weasyprint, then rasterises the PDF to a PNG via
   `pdftoppm` (poppler) at the requested DPI.

### Dependencies

- Python 3.11+
- `weasyprint` (PyPI)
- `pyyaml` (PyPI; already vendored for the conformance scripts)
- `pdftoppm` (`poppler-utils` system package)

The CI installs all three on the GitHub-hosted ubuntu runner. See
`.github/workflows/publish-versioned.yml` for the exact `pip` /
`apt-get` calls.

## How to cut a new catalog version

Follow [`docs/VERSIONING.md`](VERSIONING.md) §4 (the seven-step procedure),
specifically step 6:

1. Land the implementation PR(s) that triggered the bump. Verify CI green:
   `validate-entries`, `validate-allocation`, `ecf-conformance-consumer`,
   `catalog-conformance`.
2. Add a CHANGELOG.md row per the §4 step 5 rule.
3. **Tag**: `git tag -a v<N>-<word>.<P> -m "..." <merge-commit-sha>`
   (annotated tag per §4 step 6).
4. `git push origin v<N>-<word>.<P>`
5. The `publish-versioned.yml` job fires automatically:
   - generates `out/v<N>-<word>.<P>/capability-map.html`
   - generates `out/v<N>-<word>.<P>/capability-map-a3.png`
   - zips both into `out/v<N>-<word>.<P>.zip`
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

1. Delete or disable `.github/workflows/publish-versioned.yml`.
2. Existing published artifacts remain available as long as their
   GitHub Releases and workflow-run artifacts are not manually deleted.
   Retention for workflow artifacts is 30 days; releases are indefinite
   until manually deleted.
3. Tag `v1-alpha.0` is **immutable**; do not delete or rewrite it. If a
   `v1-alpha.0` publish was incorrect, delete the GitHub Release and (if
   reissued) tag the corrected build at a new patch label (`v1-alpha.1`).

## Operational notes

- The pipeline triggers on every `v*` tag push. Path filters are not
  applied: every tag produces a new artifact bundle.
- The PNG rasterisation path is **deterministic** (no Chrome / browser
  involvement). Two CI runs of the same tag produce byte-ident PNGs.
- The HTML file is self-contained (no external CSS / image references).
  It renders identically in Chrome, Firefox, Safari, Edge, and any modern
  print-aware browser.

## Migration from the BC-06 / BC-10 pipeline (for consumers)

Consumers that pinned to retired artifacts must migrate:

| Retired artifact | Replacement |
|---|---|
| `poster.svg` / `poster.png` | `capability-map.html` (the L0 ⊃ L1 ⊃ L2 grid renders the same capability inventory with ECF primary + secondary coordinates) |
| `map.svg` / `map.png` | `capability-map.html` (capability IDs only are also visible in the grid cells) |
| `catalog.svg` / `catalog.png` | `capability-map.html` (per-entity metadata is in the chip's tooltip / cell content) |
| `catalog.csv` | none (no machine-readable row inventory is emitted by the new pipeline) |
| `catalog.json` | none (no flattened JSON endpoint is emitted by the new pipeline) |
| `overlay.yaml` / `overlay.json` | none (the ECF overlay is internal to the schema; not redistributed) |
| `dependencies.yaml` | none (catalog manifest is internal; consumers declare their own `dependencies.yaml` if they need the pins) |
| `MANIFEST.md` | none (the zip contains exactly 2 files; no manifest needed) |

If your consumer pinned to any of the retired machine-readable endpoints
(`catalog.csv`, `catalog.json`, `overlay.yaml/json`), file an issue
against this repo and the framework will gain a `--emit-sidecars` mode
in a follow-up CR.

## References

- CR-DEA-BC-06 (retired): [`change-requests/CR-DEA-BC-06.md`](../../change-requests/CR-DEA-BC-06.md)
- CR-DEA-BC-10 (retired): [`change-requests/CR-DEA-BC-10.md`](../../change-requests/CR-DEA-BC-10.md)
- CR-DEA-BC-05 (versioning): [`change-requests/CR-DEA-BC-05.md`](../../change-requests/CR-DEA-BC-05.md)
- Framework reference: `doc_50b584c18547_generate_opendea_nested_cap_map_by_release_v1.py`
  (saved under the agent cache; the in-repo edition is
  `scripts/generate_capability_map.py`)