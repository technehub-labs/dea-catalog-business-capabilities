# Change Requests: CR-DEA-BC Series

Change requests for the Business Capability catalog. CRs land verbatim on acceptance (md5-verified against the reviewed source); they are not edited in place after landing. Status changes are recorded by the PR that lands or amends the CR, not by rewriting the CR document.

| CR | Title | Status | Landed | Notes |
|---|---|---|---|---|
| CR-DEA-BC-01 | First-Order Business Capability Method | Landed | PR #13 (2026-09-01) | Method and documentation only: semantics, admission criteria, evidence lifecycle, ECF overlay rules, governance. Phase 1 method documents landed via PR #14. |
| CR-DEA-BC-01A | Capability classification reconciliation: ADR-015 alignment | Landed | PR #3 (2026-08-31) | Record shape: kind by entity specialization, governed `capability_layer`, `capability_type` deprecated. Constrains one record field, not the method. |
| CR-DEA-BC-02 | Evidence-Based First-Order Capability Investigation | Landed, execution complete | PR #4 (2026-08-31) | Evidence corpus, candidate universe, normalization, generality matrix, distinctness sweep, admission. Research artifacts under `docs/research/`; close-out: 19/19 DoD rows verified (PR #19). |
| CR-DEA-BC-03 | Catalog Schema and CI Reconciliation | Landed | PR #21 (2026-09-01) | `schemas/entity.schema.json` + entry CI reconciled with dea-metamodel (ADR-015 lineage) and the catalog-wide CI conventions (D8 correction recorded below). Ships no entries. |
| CR-DEA-BC-04 | Industry Specialization Framework and First View (MCSP) | Landed | PR #27 (2026-09-01) | Views as mapping artifacts; SPEC-NNN record shape; version pinning; view schema + CI; evidence discipline; ECF inheritance; MCSP proving instance. |
| CR-DEA-BC-05 | Catalogue Versioning and Change Procedure | Landed | PR #39 (2026-09-02) | Three-tier pin scheme (ECF contract, catalog version label, git ref); bump rules (major/minor/patch); change procedure; tag format `v<N>-<word>.<P>`; CHANGELOG from merged PRs. |
| [CR-DEA-BC-06](CR-DEA-BC-06.md) | Publication Pipeline and Versioned Artifacts | Accepted (proposal), implementation PR pending | PR #42 (2026-09-04) | Three artifacts per tag (poster, map, catalog); Node + js-yaml + sharp generation (D3 was the proposal default but was rejected as unnecessary; see `decisions.md` D-2026-09-04-02); central-aggregator Pages via `repository_dispatch` (Pattern A, matches `dea-metamodel` PR #151 + `dea-metaframework` PR #7; the proposal's §5.1 `actions/deploy-pages@v4` text was superseded by D-2026-09-04-01); semantic-data endpoints + MANIFEST.md. Implementation ships scripts, two workflows, decisions log, and operations doc; no entity or overlay changes. **The central-aggregator Pages path was retired by CR-DEA-BC-10 (2026-09-07); see the v1-alpha.1 row for details. Current distribution is GitHub Releases only.** |
| [CR-DEA-BC-07](CR-DEA-BC-07.md) | Substrate-Neutral Re-Statement of the Workforce Capabilities | Landed | PR #48 (2026-09-07) | ECF v2.4.0 content reconciliation: Workforce Management and Workforce Planning re-stated substrate-neutrally (human and artificial agents); both entries 1.0.0 -> 1.1.0; names unchanged (N-001 stands). Tag: v1-alpha.1. |
| [CR-DEA-BC-08](CR-DEA-BC-08.md) | Coordinate Technology Management - Resolve N-006 | Landed | PR #53 (2026-09-08) | N-006 superseded by N-006R; Technology Management mapped at `strategy-direction × build`. Also carried a `catalog-conformance` CI fix (full-history branch-tip checkout) for the git-log-based `last_modified` staleness class. |
| [CR-DEA-BC-09](CR-DEA-BC-09.md) | Naming Conformance Refresh and Definition Template | Landed | PR #54 (2026-09-08) | TAXONOMY §1 rule 2 clarified; §1A definition template formalized; five renames (N-010..N-014) + Security retention (N-015); `check_naming.py` wired into entry CI; MCSP view and referencing entries updated atomically. Tag: `v1-alpha.3`. |
| [CR-DEA-BC-10](CR-DEA-BC-10.md) | Retire Dead Pages-Aggregator Dispatch Steps | Landed | PR #52 (2026-09-09) | Removes the two `Dispatch to Pages aggregator` workflow steps and the `dispatchEvent` function in `scripts/publish.js` after the v1-alpha.1 release surfaced three failures: the aggregator repo never wired up a `sync-capabilities.yml` workflow for `capabilities-updated`/`capabilities-versioned`; `secrets.DISPATCH_TOKEN` was unprovisioned; the dispatch was the final step (artifact generation, zip, and GitHub Release all succeeded regardless). Rewrites `docs/publication-pipeline.md` to record the actual current distribution path (workflow-run artifacts + GitHub Releases only). Originally authored as CR-DEA-BC-08; renumbered to BC-10 before merge because CR-DEA-BC-08 had already shipped as the Technology Management N-006R coordinate (PR #53, 2026-09-08). |

## Catalog Structure series

Cross-repo mandatory standard applied by every TechNeHub Labs catalog repo (L1 layer). This row tracks this catalog's adoption of the standard.

| CR | Title | Status | Notes |
|---|---|---|---|
| [CR-CATALOG-STRUCT-03a](CR-CATALOG-STRUCT-03a.md) | Business Capability Catalog Adoption (Layout + Index) | Landed | commit `39815423` (2026-09-05) | First half of STRUCT-03. Moves 26 flat capability YAMLs into per-entity subtrees; vendors regenerator + gate + schema; commits `CATALOG.yaml` + `TEMPLATE_VERSION`; adds `.github/workflows/catalog-conformance.yml`. 33 research files in `docs/research/` STAY in place; STRUCT-03b handles their distribution. All 16 CSTs pass under `--strict`. |
| [CR-CATALOG-STRUCT-03b](CR-CATALOG-STRUCT-03b.md) | Business Capability Catalog Adoption (Research Distribution) | Landed | commit `c33843d3` (2026-09-05) | Second half of STRUCT-03. Distributes 33 research files: CAND-018 boundary decision (2 files) to `dea:capability-analytics-and-intelligence/research/`; 31 catalog-wide artifacts to new `catalog-research/`; 9 SVG visuals + manifest to new `visuals/`. `docs/research/` removed. Brings the BC catalog from `partial` to `conforming`. |

## Conformance Gate series (cross-repo, CG-001..006 anchor in dea-metaframework)

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-ECF-CG-003](CR-ECF-CG-003.md) | Business Capability Catalog Conformance | Proposed (this PR) | Catalog is the validation-and-correction target, not a redesign. Mandates Capability Identity ≠ ECF Coordinate; preserves multiple contextual coordinates; ratifies 26-entry plus MCSP view conformance via a new `ecfConformance` block. |

## Numbering

- The series tag is `CR-DEA-BC` (DEA Business Capability).
- CR-DEA-BC-01 is the method CR; CR-DEA-BC-01A was renumbered from an early CR-DEA-BC-02 allocation (2026-08-31) when the number was yielded to the evidence-investigation CR.
- Successors are parked, not scheduled: CR-DEA-BC-03 (schema + CI reconciliation with dea-metamodel), CR-DEA-BC-04 (industry specialization framework; first view: Mobile Communications Service Provider).
- **Decision 2026-09-01 (numbering reconciliation):** CR-DEA-BC-02 section 40 (authored before the method CR) named BC-03 as "First-Order Capability Canonicalization"; CR-DEA-BC-01 (accepted later) names BC-03 as schema + CI and treats canonical admission as BC-02's own execution through the section 38 gate and the method review gates. Decided: **the CR-DEA-BC-01 assignment holds.** Canonical admission of the recommended set is method execution (METHODOLOGY.md section 12), not a separate CR; CR-DEA-BC-03 is the schema + CI reconciliation. Recorded per the renumbering convention (GOVERNANCE.md section 2).

## Corrections to landed CRs

Landed CRs are immutable; corrections are recorded here.

- **CR-DEA-BC-03, decision D8 (2026-09-01):** the CR cites "the actors pattern: ajv-py-action" as the CI mechanism. That action name was a phantom: it never existed on GitHub and had been replaced org-wide on 2026-08-09 (dea-catalog-actors PR #2). The citation came from a stale local checkout of dea-catalog-actors. The implemented and accepted mechanism is `dsanders11/json-schema-validate-action@v2.1.0` with the empty-entities skip guard (the true catalog-wide pattern), plus this catalog's fixture self-exercise step. Decision D8 stands with that substitution.

## Ordering note

CR-DEA-BC-02 executes ahead of CR-DEA-BC-01 by design: the investigation produces raw material; the method CR defines how that material is judged. Acceptance of CR-DEA-BC-01 does not retro-invalidate the research artifacts; it gates their promotion. Nothing becomes canonical until it passes the method.
