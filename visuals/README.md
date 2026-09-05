# Visuals: technehub-labs/dea-catalog-business-capabilities

This directory holds SVG visual artifacts produced during CR-DEA-BC-02
execution and the admission process. The visuals illustrate the
candidate universe, the evidence pipeline, the enterprise comparison
matrix, capability boundaries, and the ECF coverage map.

## Provenance

All SVG files were moved from `docs/research/visuals/` to `visuals/`
(top-level repo directory, separate from `docs/`) by
CR-CATALOG-STRUCT-03b. Visuals are their own asset category: they are
neither prose documentation (which lives in `docs/`) nor per-entity
research (which lives in entity `research/` subtrees) nor
catalog-wide research (which lives in `catalog-research/`).
Co-locating them with `docs/` would conflate them with the methodology
documentation; co-locating them with `catalog-research/` would
overload the research directory with non-research assets. The
top-level `visuals/` location preserves the distinction.

The companion manifest stayed in `catalog-research/visuals.yaml`
(moved from `docs/research/visuals.yaml` as a catalog-wide artifact)
because it is metadata about the visual asset set rather than an
asset itself. The narrative `VISUALS-v0.1.md` (which explains the
visual artifacts) is also in `catalog-research/`.

## Files

| File | Topic |
|---|---|
| `v01-evidence-candidate-pipeline.svg` | Evidence-to-candidate pipeline diagram. |
| `v02-candidate-universe-map.svg` | The 35-candidate universe classified into the 16-class taxonomy. |
| `v03-enterprise-comparison-matrix.svg` | Cross-enterprise capability coverage matrix. |
| `v04-capability-process-boundary.svg` | Capability-vs-process boundary illustration. |
| `v05-capability-outcome-relationship.svg` | Capability-outcome relationship model. |
| `v06-capability-business-object.svg` | Object Focus test (METHODOLOGY.md section 4) illustration. |
| `v07-first-order-specialization-pyramid.svg` | First-order specialization hierarchy. |
| `v08-capability-ecf-overlay.svg` | Capability coverage of the Enterprise Concept Framework. |
| `v09-ecf-coverage-map.svg` | ECF coverage map (canonical capabilities by domain and stage). |

The manifest lives at `catalog-research/visuals.yaml`; it records the
version, source, and provenance for each SVG.
