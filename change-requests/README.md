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
| [CR-DEA-BC-06](CR-DEA-BC-06.md) | Publication Pipeline and Versioned Artifacts | Superseded | PR #42 (2026-09-04) | First-generation Node-based pipeline (`scripts/publish.js` + `scripts/publish-mockups/*` + `scripts/render_map_png.mjs`). Produced poster/map/catalog SVG+PNG + catalog CSV/JSON + overlay YAML/JSON + dependencies.yaml + MANIFEST.md (12-file release zip). **Retired 2026-09-09** in favour of the framework Python `scripts/generate_capability_map.py`; see `docs/publication-pipeline.md` "Migration from the BC-06 / BC-10 pipeline" for the consumer-facing migration map. The central-aggregator Pages path was retired by CR-DEA-BC-10 before this CR was itself superseded. |
| [CR-DEA-BC-07](CR-DEA-BC-07.md) | Substrate-Neutral Re-Statement of the Workforce Capabilities | Landed | PR #48 (2026-09-07) | ECF v2.4.0 content reconciliation: Workforce Management and Workforce Planning re-stated substrate-neutrally (human and artificial agents); both entries 1.0.0 -> 1.1.0; names unchanged (N-001 stands). Tag: v1-alpha.1. |
| [CR-DEA-BC-08](CR-DEA-BC-08.md) | Coordinate Technology Management - Resolve N-006 | Landed | PR #53 (2026-09-08) | N-006 superseded by N-006R; Technology Management mapped at `strategy-direction × build`. Also carried a `catalog-conformance` CI fix (full-history branch-tip checkout) for the git-log-based `last_modified` staleness class. |
| [CR-DEA-BC-09](CR-DEA-BC-09.md) | Naming Conformance Refresh and Definition Template | Landed | PR #54 (2026-09-08) | TAXONOMY §1 rule 2 clarified; §1A definition template formalized; five renames (N-010..N-014) + Security retention (N-015); `check_naming.py` wired into entry CI; MCSP view and referencing entries updated atomically. Tag: `v1-alpha.3`. |
| [CR-DEA-BC-10](CR-DEA-BC-10.md) | Retire Dead Pages-Aggregator Dispatch Steps | Superseded | PR #52 (2026-09-09) | Removed the two `Dispatch to Pages aggregator` workflow steps and the `dispatchEvent` function in `scripts/publish.js`. **Both the dispatch step and the BC-06 publication pipeline it lived in were superseded 2026-09-09** by the framework Python `scripts/generate_capability_map.py`. CR-DEA-BC-10 remains a faithful historical record of the decision that ended the central-aggregator Pages path. Originally authored as CR-DEA-BC-08; renumbered to BC-10 before merge because CR-DEA-BC-08 had already shipped as the Technology Management N-006R coordinate (PR #53, 2026-09-08). |
| [CR-DEA-BC-12](CR-DEA-BC-12.md) | Submittal Review BC-SR-A001 — Six High-Confidence ECF Re-Mappings, Three New Investigations, and Repo-Doc Drift Cleanup | Landed | PR #65 (2026-09-10) | Carrier for the substantive recommendations of [BC-SR-A001](../submittal-reviews/BC-SR-A001.md). Lands 6 high-confidence ECF coordinate re-mappings (Strategy, Strategic Planning, Asset, Facility, Supplier, Sourcing & Procurement), opens 3 evidence-led investigation tracks (Organizational Design, Enterprise Performance Management, Relationship Management), and fixes README `Catalog Status: planned` → `populated` drift plus architecture-framework pin clarification. Catalog bump v1-alpha.4 → v1-alpha.5 (Minor). Tag `v1-alpha.5` at `246e010a`. |
| [CR-DEA-BC-13](CR-DEA-BC-13.md) | ECF Primary-Coordinate Rule Refinement — Semantic Center of Gravity + 26-Entry Re-Evaluation + Technology Management Boundary Decision + Tracks A/B/C Evidence Collection | Landed | PR #66 (2026-09-10) | Method-CR codifying the new ECF primary-coordinate rule ("semantic center of gravity") in `METHODOLOGY.md §8`; re-evaluates all 26 entries (4 primary-coordinate moves, 1 secondary fix, 1 Tech Management carve-text); formalizes the Tech-as-Estate vs Tech-as-Enabler carve per BC-SR-A001 §12; starts the actual evidence collection for tracks A/B/C as non-canonical candidate records (no admission). Catalog bump v1-alpha.5 → v1-alpha.6 (Minor). Tag `v1-alpha.6` at `0c943b2d`. |
| [CR-DEA-BC-17](CR-DEA-BC-17.md) | Admit Technology Enablement as a First-Order Canonical Capability | Proposed | (PR pending) | Closes the BC-DEA-BC-13 §11 follow-on queue item (BC-13 §C deferred admission). Admits `dea:capability-technology-enablement` at `enablement-operations/operate` (primary) with `build` and `improve` secondaries. Updates Technology Management (1.2.0 → 1.3.0; boundary-text + related_capabilities), Operations (1.0.0 → 1.0.1; cross-reference patch), Information Management (1.0.0 → 1.0.1; cross-reference patch). Evidence trail in `catalog-research/` (TER-TECHENABLEMENT-001 + ECF overlay + distinctness sweep + admission-gate closeout). Catalog count 26 → 27 first-order caps. Catalog bump v1-alpha.6 → v1-alpha.7 (Minor). |

## Catalog Structure series

Cross-repo mandatory standard applied by every TechNeHub Labs catalog repo (L1 layer). This row tracks this catalog's adoption of the standard.

| CR | Title | Status | Notes |
|---|---|---|---|
| [CR-CATALOG-STRUCT-03a](CR-CATALOG-STRUCT-03a.md) | Business Capability Catalog Adoption (Layout + Index) | Landed | commit `39815423` (2026-09-05) | First half of STRUCT-03. Moves 26 flat capability YAMLs into per-entity subtrees; vendors regenerator + gate + schema; commits `CATALOG.yaml` + `TEMPLATE_VERSION`; adds `.github/workflows/catalog-conformance.yml`. 33 research files in `docs/research/` STAY in place; STRUCT-03b handles their distribution. All 16 CSTs pass under `--strict`. |
| [CR-CATALOG-STRUCT-03b](CR-CATALOG-STRUCT-03b.md) | Business Capability Catalog Adoption (Research Distribution) | Landed | commit `c33843d3` (2026-09-05) | Second half of STRUCT-03. Distributes 33 research files: CAND-018 boundary decision (2 files) to `dea:capability-analytics-and-intelligence/research/`; 31 catalog-wide artifacts to new `catalog-research/`; 9 SVG visuals + manifest to new `visuals/`. `docs/research/` removed. Brings the BC catalog from `partial` to `conforming`. |
| [CR-CATALOG-STRUCT-08](CR-CATALOG-STRUCT-08-ecf-domain-enum-v2.3.0-migration.md) | ECF Domain Enum v2.3.0 Migration | Landed | PR #46 (2026-09-07) | Carrier for the v2.3.0 Domain enum migration in this catalog (4th landing in the wave after metaframework, metamodel, process catalog). Five of the seven canonical ECF Domains were renamed in the metaframework (CR-ECF-006 + ADR-ECF-001); the v0.2 overlay remains valid; only the names shifted. Companion to CR-BP-17. |
| [CR-CATALOG-STRUCT-09](CR-CATALOG-STRUCT-09-ecf-domain-enum-agency-migration.md) | ECF Domain Enum v2.4.0 Migration (Agency & Organization) | Landed | PR #47 (2026-09-07) | v2.4.0 migration carrier: Domain 3 renamed from `PeopleAndOrganization` to `AgencyAndOrganization` (Substrate Independence Stress Test; ADR-ECF-002 / CR-ECF-007). Single Domain rename; no content redistribution. Companion to CR-BP-18. |

## Conformance Gate series (cross-repo, CG-001..006 anchor in dea-metaframework)

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-ECF-CG-003](CR-ECF-CG-003.md) | Business Capability Catalog Conformance | Landed | PR #34 (2026-09-01) | Catalog is the validation-and-correction target, not a redesign. Mandates Capability Identity ≠ ECF Coordinate; preserves multiple contextual coordinates; ratifies 26-entry plus MCSP view conformance via a new `ecfConformance` block. Gate is live in `.github/workflows/catalog-conformance.yml`. |

## BC-ECF migration carrier series (cross-repo; metaframework CR-ECF-NNN anchor)

This catalog's migration carriers for metaframework ECF enum bumps. Each row corresponds to a Domain/Stage rename driven by a metaframework ADR + CR; the carrier PR lands the rename in this catalog's `schemas/entity.schema.json` and the canonical entity overlays.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-BC-ECF-03](CR-BC-ECF-03.md) | ECF Domain Enum v2.5.0 Migration (Domain 6 Enablement & Operations) | Landed | PR #56 (2026-09-08) | v2.5.0 migration carrier: Domain 6 renamed from `OperationsAndEnablement` to `EnablementAndOperations` (Domain/Stage Orthogonality Stress Test; ADR-ECF-003 / CR-ECF-008). Single Domain rename; no content redistribution. Companion to CR-BP-23. |

## Numbering

- The series tag is `CR-DEA-BC` (DEA Business Capability).
- CR-DEA-BC-01 is the method CR; CR-DEA-BC-01A was renumbered from an early CR-DEA-BC-02 allocation (2026-08-31) when the number was yielded to the evidence-investigation CR.
- **Decision 2026-09-01 (numbering reconciliation):** CR-DEA-BC-02 section 40 (authored before the method CR) named BC-03 as "First-Order Capability Canonicalization"; CR-DEA-BC-01 (accepted later) names BC-03 as schema + CI and treats canonical admission as BC-02's own execution through the section 38 gate and the method review gates. Decided: **the CR-DEA-BC-01 assignment holds.** Canonical admission of the recommended set is method execution (METHODOLOGY.md section 12), not a separate CR; CR-DEA-BC-03 is the schema + CI reconciliation. Recorded per the renumbering convention (GOVERNANCE.md section 2).

## Corrections to landed CRs

Landed CRs are immutable; corrections are recorded here.

- **CR-DEA-BC-03, decision D8 (2026-09-01):** the CR cites "the actors pattern: ajv-py-action" as the CI mechanism. That action name was a phantom: it never existed on GitHub and had been replaced org-wide on 2026-08-09 (dea-catalog-actors PR #2). The citation came from a stale local checkout of dea-catalog-actors. The implemented and accepted mechanism is `dsanders11/json-schema-validate-action@v2.1.0` with the empty-entities skip guard (the true catalog-wide pattern), plus this catalog's fixture self-exercise step. Decision D8 stands with that substitution.

## Ordering note

CR-DEA-BC-02 executes ahead of CR-DEA-BC-01 by design: the investigation produces raw material; the method CR defines how that material is judged. Acceptance of CR-DEA-BC-01 does not retro-invalidate the research artifacts; it gates their promotion. Nothing becomes canonical until it passes the method.
