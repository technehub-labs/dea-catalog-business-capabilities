# Business Capability Catalog Changelog

> **Layout note (CR-DEA-BC-mv1, 2026-09-21):** This document was authored against the
> pre-migration catalog layout (`entities/v1-alpha/dea:*`) and the legacy `dea:*` id
> family. Ids and paths cited below are historical; see `reconciliation/migration-id-map.yaml`
> for the old-to-new id mapping and dea-metaframework `docs/entity-storage-layout.md` for
> the current layout.

All notable changes to this catalog are recorded here. The format is based
on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) adapted for
CR-DEA-BC-05 versioning: each entry records the bump tier (major / minor /
patch), the scope, the rationale, the PR that landed it, and any tag.

The catalog uses `v<N>-<word>` versioning while in v1 (lettered-suffix
regime) and `v<N>.<M>` semver from v2 onward. See
[`docs/VERSIONING.md`](VERSIONING.md) for the normative procedure and
[`docs/release-cut-procedure.md`](release-cut-procedure.md) for the
release-cut procedure (gated by the pre-release CI verification contract;
GPG-signed; documented in the prior-cut history table).
## [Unreleased]

### CR-DEA-BC-38: CI Test Wiring + Gate Honesty

`count_open_change_requests` in `scripts/regenerate_catalog.py` now parses both metadata shapes (bold-line and table-row) and closes on the status vocabulary this repo actually uses (`Merged/Landed/Applied/Accepted/Rejected/Superseded/Withdrawn`); previously only `Merged` counted closed, so every CR counted open (`open_change_requests: 40`). The duplicated condition at the old line 518 is gone. `open_change_requests` steps 41 -> 12 at this landing. The full test suite (`python -m pytest tests/ -q`) now runs as a named CI step in `catalog-conformance.yml` (pytest was installed but never run; `tests/test_check_entity_system.py` ran nowhere). The entity-system gate's record walk now excludes the per-entity state directories (`research/`, `candidates/`, `retired/`) per CR-CATALOG-STRUCT-01 §5 — parity with `validate-entries.yml` — and `validate-entity-system.yml` drops `continue-on-error: true`, so the strict gate blocks; divergence from the `dea-catalog-processes` original is recorded in the script header for future propagators. New regression test for the state-dir exclusion (54 tests total).

### CR-DEA-BC-37: Main-Red Remediation (Authorship Backfill + CATALOG Freshness + CST Pinning)

Returns `main` to green after PRs #88/#89 merged with red gates. Three AUT-001 authorship corrections, recorded per GOVERNANCE §2.2 (`**Owner**`/`author` values `Coder (for eaojnr)` -> `Emmanuel A. Otchere` in the release-history CR, the org-wide id confirmation CR, and `catalog-research/recon/INV-BC-35-v0.1.yaml`); the fields regressed after the CR-DEA-BC-34 retro-sweep. `CATALOG.yaml` regenerated (committed `open_change_requests: 39` lagged the computed 40; blocking freshness check). The `dea-metaframework` checkout in `catalog-conformance.yml` pinned to release tag `v2.6.0`, satisfying CST-013/CST-014 (reproducible toolchain). No entity, id, schema, or gate-logic changes.

### CR-DEA-BC-36: Release-History Reset (Path B) + Release-Discipline Extensions

Withdraws the nine v1-alpha.x tag set (v1-alpha.0 .. v1-alpha.8) as pre-mature, plus the three pre-tag abandoned sections (STRUCT-03a, STRUCT-03b, v1-alpha.0-pipeline-live). Cross-repo dependency sweep: 0 hits across the 8 sibling repos. Extension set A+B+D+F adopted: pre-release CI verification contract, prior-cut history table (empty post-reset), GPG-signing procedure, doc split to docs/release-cut-procedure.md. Recovery appendix captured in change-requests/CR-DEA-BC-36-release-history-reset-and-discipline.md section 2; fossilised record at docs/release-history-archive.md. No entity records, ids, or gate counts change. PR #88.



### CR-DEA-BC-35: Entity System Stage 5-6 (BC Slice)

BC slice of the General Entity System institutionalisation (cross-repo cascade T7 of the umbrella programme). New `reconciliation/entity-system-registry.yaml` (BC-specific: 1 profile `BusinessCapability` with required fields `id, type, name, definition, version, metamodel_pin, lifecycle_status`; BC id pattern `^capabilities:capability-[a-z0-9-]+-[a-z2-9]{6}$`; BC lifecycle ladder states `candidate -> observed -> corroborated -> normalized -> ecf-mapped -> reviewed -> canonical -> active -> retired`; per-type gate delegation to `scripts/check_business_capability.py`). New `scripts/check_entity_system.py` (5-rule umbrella gate; copied verbatim from `dea-catalog-processes`). New `scripts/check_business_capability.py` (per-type gate stub; ES-005 existence check only; full per-type validation lives in the conformance rollup). New `tests/test_check_entity_system.py` (32 tests; all pass; copied verbatim). New `.github/workflows/validate-entity-system.yml` (runs gate under `--strict` on every PR). Live posture: 32/32 admitted `BusinessCapability` records pass ES-001..ES-005; 3 pre-admission candidate records (`capabilities:candidate-relmgmt-nu73v9`, `capabilities:candidate-epm-5fxren`, `capabilities:candidate-orgdesign-a7s8bf`) carry advisory ES-001 + ES-002 findings (documented as class-level disposition). No entity, schema, or id changes. D-004 clean. 118a/118b/118c authorship gates remain CONFORMANT.

> Correction (2026-10-27, CR-DEA-BC-38): the workflow as originally landed carried `continue-on-error: true` on the strict step, so the gate was advisory in effect despite the claim above. CR-DEA-BC-38 resolves the three candidate-record findings by excluding state directories from the walk and removes `continue-on-error`; the claim is now true.
 1414f50 (feat: CR-DEA-BC-35 entity-system BC slice)

### CR-DEA-BC-34: Authorship Cardinal Rule (R1, R2) - Org-Wide Propagation Slice

User directive 2026-10-13: "no `Coder` / `Agent` / agent or tool names in any
authorship field of any published artifact". The CR-BP-118 cardinal rules (R1
and R2) are propagated to this repo. New blocking gate
`scripts/check_authorship.py` (CR-BP-118 / AUT-001..003), data-driven from
`reconciliation/authorship-fields.yaml` (allowlist
`{Emmanuel A. Otchere, TechNeHub Labs}`; denylist
`{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}`).
A retroactive sweep rewrites every authorship-metadata hit in the repo:
73 files, ~93 textual replacements. 0 entity content changes; 0 id changes;
0 cross-reference changes. The gate's `prefix_match: true` opt-in is new for
this repo: actor / reviewer values are routinely followed by rich context
(e.g. `actor: "Emmanuel A. Otchere, BC-13 B.1 Track A candidate seeded"`),
and exact-match AUT-003 would false-positive on the trailing context. CI
wiring: new workflow `.github/workflows/validate-authorship.yml` runs the
gate in `--strict` mode on every push and PR. 21/21 `test_check_authorship`
pass on this repo's tree. Carrier:
`change-requests/CR-DEA-BC-34-authorship-cardinal-rule.md`.


## Unreleased (historical)

DEA-BC-20). Renames two entries that fail the noun-as-ability rule (TAXONOMY section 1 rule 7) under the post-mv1 id system.

- **`dea:capability-strategy` -> `dea:capability-strategy-formulation`.** Renamed (N-016). New id `capabilities:capability-strategy-formulation-sf7q2x`. Version 1.1.1 -> **2.0.0** (Major per VERSIONING section 1.1: name change is a breaking identity change for callers; `aliases: [Strategy]` preserves the colloquial reference). The new name reads as an ability rather than as a noun-of-discourse; parallels Strategic Planning (kept; passes noun-as-ability with the Planning suffix). Related entries updated: Organizational Design, Enterprise Governance, Strategic Planning, Technology Enablement (related_capabilities + boundary prose).
- **`dea:capability-operations` -> `dea:capability-operations-management`.** Renamed (N-018). New id `capabilities:capability-operations-management-pm3w8k`. Version 1.0.1 -> **2.0.0** (Major). `business_object: Operation` (singular) -> `business_object: Operations` (plural) per DP-D (top-level concept retained; semantic breakdown of Production and Service Delivery added to the definition prose). `aliases: [Operations, Production Management, Service Delivery Management]` added for discoverability. The naming change parallels Customer Management, Asset Management, Risk Management. Related entries updated: Technology Enablement, Offering Management (related_capabilities + boundary prose).
- **Enterprise Governance retention (N-019).** `verdict: review-retained`. Version 1.0.1 -> **1.0.2** (Patch; VERSIONING section 1.2 minor = advisory-clearance bump). Rationale: `governance` reads as an ability verb; the entry's `business_object` `Decision` is the *subject of governing* not the *ability-object noun*.
- **Sourcing and Procurement `business_object` clarification (N-020).** `business_object: Purchase Order` -> `business_object: Acquisition Cycle` (Purchase Order is a process artifact, not the ability-object noun; Acquisition Cycle names the sustained activity). Version 1.2.0 -> **1.3.0** (Minor). The capability name itself is unchanged; it already passes noun-as-ability as a gerund pair.
- **Linter hardening.** `scripts/check_naming.py` gains H8 (noun-as-ability; structural hard check with suffix-pattern library + single-gerund + gerund-pair regex) and a review-retained exemption registry that reads `catalog-research/normalization.yaml` for `verdict: review-retained` decisions (resolved by `affected_entry` under the post-mv1 id system). Default exit code unchanged (0 on PASS; 1 on H1-H8 violations). The lint was previously advisory on the noun-as-ability axis (BC-09 section 7); it is now a hard gate, with the only legal override being a registered N-NNN review-retained decision. CI calls `check_naming.py` without `--strict`; A1 (object-anchoring heuristic) remains advisory as it is semantic-review territory per TAXONOMY section 1A.3.
- **TAXONOMY rule 7 codified** at section 1 (noun-as-ability); section 1A.3 machine-enforcement scope updated to include rule 7.
- **reconciliation/migration-id-map.yaml extended**: version 1 -> 2; 3 new id_map entries (`dea:capability-strategy-formulation`, `dea:capability-operations-management`, `dea:capability-insight-management` for BC-22 follow-on); 3 new known_residuals for the pre-rename slugs (`dea:capability-strategy`, `dea:capability-operations`, `dea:capability-analytics-and-intelligence`).

### Affected entries (BC-20)

- **Renamed (Major):** Strategy 1.1.1 -> Strategy Formulation 2.0.0; Operations 1.0.1 -> Operations Management 2.0.0.
- **Bumped (Patch/Minor; no name change):** Enterprise Governance 1.0.1 -> 1.0.2; Sourcing and Procurement 1.2.0 -> 1.3.0.
- **CATALOG.yaml** regenerated to reflect id/path/version/last_modified for the four affected entries.
- **Catalog count** unchanged at 28 first-order canonical capabilities.
- **Normalization register** version 0.2 -> 0.3; decisions N-015 verdict formalized, N-016, N-018, N-019, N-020 appended; N-017 deferred to CR-DEA-BC-21 recon.

**Research-CR** (CR-DEA-BC-21). Closes the DP-E deferred item from CR-DEA-BC-20: the recon procedure for Analytics and Intelligence (CAND-018) ran five steps (three-class source sweep, distinctness sweep, semantic-center-of-gravity test, ECF placement audit, user vocabulary test) and evaluated four candidate vectors. Recommendation: V-A Insight Management (PRIMARY).

- **V-A Insight Management chosen.** Three source classes converge on `insight` as the noun-of-product: BABOK v3 (knowledge/insights/recommendations), BIZBOK v14 (insight lifecycle practice area), DMBOK 2nd ed. (insights from data) plus OMG DMN (decision insight) and APQC PCF 7.4 (process 7.7.8.2 "Develop insights into workforce analytics outcomes"). Note: APQC PCF 7.4 has no process named "Business Intelligence" -- the PCF has moved past that label. Forrester analyst vocabulary has shifted from "BI Platforms" to "Enterprise Insight Platforms".
- **V-B Intelligence Management deprecated.** "Intelligence" as head noun collapses to "Analytics" under DMBOK 2nd ed. and Forrester; APQC PCF 7.4 reserves "intelligence" for market-research contexts. One source class only.
- **V-C Decision Intelligence Management deprecated.** Gartner Decision Intelligence is a vendor-class market category, not an enterprise-generic ability. APQC PCF 7.4 does not use the DI arity.
- **V-D Analytics and Intelligence reviewed-retained deprecated.** H8 hard fail; the only legal override is a verdict review-retained decision. V-A supersedes with a clean rename.
- **User ratified V-A on 2026-09-30** (Discord message id `1554690132228051015`; "V-A insight management is adopted"). Promotes ADR-ES-021 status from `proposed` to `ratified (2026-09-30)`.
- **Recon artifacts**: `catalog-research/recon/INV-AI-v0.1.yaml` (5-step procedure; 4 vectors), `catalog-research/recon/ADR-ES-021.yaml` (recommendation ADR; status ratified 2026-09-30).
- **Normalization register** version 0.3 -> 0.4; N-022 appended (verdict `review-retained-pending-ADR`; closes to `rename-applied` on user ratification of V-A; recommendation V-A Insight Management).
- **Evidence register** version 0.7.0 -> 0.8.0; SRC-023 (APQC PCF 7.4; cross-industry-process class), SRC-024 (Forrester Wave Enterprise Insight Platforms; BIZBOK v14; business-architecture class), SRC-025 (DMBOK 2nd ed.; OMG DMN; IIBA BABOK v3; standards-body class) added; G11 (BC-21 recon closure) appended.
- **Candidates register** version 0.5.0 -> 0.5.1; `cand_018_vectors` extension (V-A/B/C/D) appended.

**Major** (CR-DEA-BC-22). Applies the BC-21 recon V-A rename on 2026-09-30. Closes the BC-09 named-advisories list (down from 5 to 4 review-retained entries; the Analytics and Intelligence advisory is the one that goes away).

- **`dea:capability-analytics-and-intelligence` -> `dea:capability-insight-management`.** Renamed (N-022; verdict closes `review-retained-pending-ADR` -> `rename-applied`). New id `capabilities:capability-insight-management-ms4n9d`. Version 1.0.0 -> **2.0.0** (Major; semver-incompatible name change). `aliases: [Analytics and Intelligence, Data and Analytics, Insight, Intelligence, Business Intelligence]` retained for provenance and discoverability. `business_object: Insight` retained (it was already `Insight` in the prior entry; the rename aligns the name to the object). The new name reads as an ability (Management gerund); the noun-of-product `Insight` is the cross-domain pattern observed in BABOK v3 (knowledge/insights/recommendations), BIZBOK v14 (insight lifecycle), DMBOK 2nd ed. (insights from data), OMG DMN (decision insight), and APQC PCF 7.4 (process 7.7.8.2 "Develop insights into workforce analytics outcomes"). Related entries updated: Information Management (boundary prose), Technology Enablement (related_capabilities + boundary prose). CR-DEA-BC-21 recon procedure and recommendation ADR are recorded; ADR-ES-021 status `ratified (2026-09-30)`.

### Affected entries (BC-22)

- **Renamed (Major):** Analytics and Intelligence 1.0.0 -> Insight Management 2.0.0 (id, name, aliases appended).
- **CATALOG.yaml** regenerated for `dea:capability-insight-management` block (id, name, path, version 2.0.0, last_modified 2026-09-30). The research sub-folder (containing `boundary-decision-cand-018.yaml`, `BOUNDARY-DECISION-CAND-018.md`, `README.md`) is moved with the parent directory and is listed in the catalog research refs against the new id.
- **Catalog count** unchanged at 28 first-order canonical capabilities (rename, not admission).
- **Normalization register** version 0.4 -> 0.5; N-022 verdict `review-retained-pending-ADR` -> `rename-applied`; `affected_entry` updated to `capabilities:capability-insight-management-ms4n9d`; `prior_affected_entry` recorded for provenance.
- **ADR-ES-021** status `proposed` -> `ratified (2026-09-30)`; user ratification timestamp recorded.
- **Capability map** regenerated (28 entities, 31 cells; cell `enablement-operations x operate` now shows Insight Management).

**Major** (CR-DEA-BC-23). Admits Enterprise Performance Management (CAND-037) as the 29th first-order canonical capability.

- **`dea:candidate-epm-5fxren` -> `capabilities:capability-enterprise-performance-management-5fxren`.** Admitted (N-023 verdict admitted; TER-EPM-001 evidence-pending -> admitted). New id under the post-mv1 id system. Version 1.0.0 (admission is the first release). metamodel_pin 1.0.0 (org-wide pin). The capability was carried at E3 from BC-19 (Track B research-CR; SRC-020 Kaplan & Norton Balanced Scorecard; SRC-021 OKR framework; SRC-022 OMG Business Performance Management via OCEB 2 -- three-source convergence). Enterprise-generality demonstrated across B2B, B2C, G2C archetypes; foundation-grade under BC-SR-A001 §17.
- **Cell populated**: `strategy-direction x operate` (primary); `strategy-direction x improve` + `finance-accounting x operate` (secondaries). ECF placement per CR-DEA-BC-13 §D.2 + CR-DEA-BC-19 (BC-23 carries the placement forward unchanged).
- **Direction loop closure (BC-SR-A001 §16)**: Strategy Formulation -> Strategic Planning -> Performance Management (EPM) -> Insight Management -> Adaptation. EPM and Insight Management are the governance/measurement and insight halves respectively; together they complete the loop that Strategy Formulation opens. Loop-closure narrative recorded on the entity's `boundary.loop_role` field.
- **H8 noun-as-ability**: Management gerund passes cleanly. H3 (rule 4 outcome-free) was firing on the word "Performance"; N-024 records the review-retained verdict (the marker is the noun-of-product of a recognized governance ability, parallel to Risk Management's Risk; the linter's OUTCOME_MARKERS regex is the known false-positive source and the BC-25 follow-on linter patch is the right fix). The linter's H3 outcome-marker path was extended in this commit to read the review-retained exemption registry (N-024), bringing the linter into parity with H8.
- **Sourcing and Procurement business_object Acquisition Cycle** (BC-20 N-020) and **Sourcing and Procurement** (BC-20) are unaffected.
- **Siblings updated**: Strategy Formulation, Strategic Planning, Insight Management, Financial Resource Management, Financial Stewardship, Organizational Design (related_capabilities + boundary prose). view-telecom-mcsp.yaml inherited[] updated; VIEW-TELECOM-MCSP.md coverage section updated.
- **reconciliation/migration-id-map.yaml** extended (v2 -> v3): 3 new id_map entries (`dea:candidate-epm-5fxren` -> canonical, `dea:capability-enterprise-performance-management` -> canonical, `dea:capability-epm` -> canonical). 1 new known_residual for the pre-admission candidate id.
- **CATALOG.yaml regenerated**: 32 entities (29 canonical + 3 candidates). Capability map regenerated.
- **Distinctness sweep** v0.6.0: Track B (EPM) admitted; 4 -> 8 peers; sweep-completed-as-admitted.
- **Evidence register** v0.9.0: TER-EPM-001 admitted; CAND-037 E3 confirmed; loop_closure_status closed; status field updated.
- **Candidates** v0.5.2: CAND-037 evidence_strength E1 -> E3; canonical true; admitted 2026-10-12; admitted_cr CR-DEA-BC-23.
- **Normalization** v0.7.0: N-023 (admission verdict); N-024 (review-retained verdict for H3 outcome-marker false positive on the word "Performance" in the canonical name). 22 decisions total.

### Affected entries (BC-23)

- **Admitted (Major; first release)**: Enterprise Performance Management 1.0.0 at `capabilities:capability-enterprise-performance-management-5fxren`.
- **Sibling cross-references updated**: 6 entries (Strategy Formulation, Strategic Planning, Insight Management, Financial Resource Management, Financial Stewardship, Organizational Design).
- **Catalog count**: 28 -> 29 first-order canonical capabilities.
- **All 7 structural gates PASS post-commit**: check_naming (29 entries, 4 advisories -- unchanged); check_versions (29); check_ecf_conformance (29 + MCSP view); check_view_refs (clean); check_visual_domain_labels (9 visuals); check_catalog_index (32 entities); check_id_system (IDM-001..007 CONFORMANT).

**Major** (CR-DEA-BC-mv1). Org-wide id system migration (Wave 2): all 31 records (28 canonical capabilities + 3 candidates) move from the legacy `dea:*` family to `capabilities:capability-<slug>-<hash>` / `capabilities:candidate-<slug>-<hash>`; entity dirs move to `entities/v1-alpha/<slug>-<hash>/` (flat layout); every structured cross-reference rewritten; README.md per entity dir (IDM-007); new blocking gate `scripts/check_id_system.py` (IDM-001..007 + IDM-008 PR-scoped) wired into catalog-conformance CI; vendored STRUCT tools and catalog-index schema ported to the dual-family id system (upstream: dea-metaframework PR #34); `ecf_rationale` maxLength 1000 -> 1280 in the entity schema (namespaced ids are longer); 36 historical artifacts bannered with the CR-DEA-BC-mv1 layout note (content verbatim; see `reconciliation/cross-check-mv1.md`); migration id map at `reconciliation/migration-id-map.yaml` with 7 documented known residuals.


**Housekeeping** (no version bump; pre-release cleanup). Removes en/em dashes from every GitHub-visible artifact in the repo (32 files; 213 em-dashes + 24 en-dashes removed from Markdown; 23 em-dashes from YAML prose). The punctuation policy now lives in memory; the artifact layer reflects it without stating it. Change-requested under user instruction 2026-09-11.


## [v2.5.0-migration] - 2026-09-08

CR-BC-ECF-03 implementation: ECF Domain enum migration to the v2.5.0 canonical Domain set (carried by `technehub-labs/dea-metaframework` v2.5.0; CR-ECF-008 + ADR-ECF-003). One of seven Domains renamed: Domain 6 `OperationsAndEnablement` → `EnablementAndOperations` (kebab-case `operations-enablement` → `enablement-operations`; lowerCamelCase `operationsEnablement` → `enablementAndOperations`), driven by the Domain/Stage Orthogonality Stress Test. 44 files re-keyed (1 schema, 3 scripts, 26 entity YAMLs, 7 catalog-research files, 3 CR records). Also fixes the Domain 6 display label in `scripts/lib/grid.js` (the Domain-3 fix from CR-CATALOG-STRUCT-09 left Domain-6 stale). No content redistribution required (CR-ECF-008 §3.5).

**Files touched**: 44 files + 1 new CR carrier. See `change-requests/CR-BC-ECF-03.md` for the full mapping table and validation evidence.

**Unchanged**: Domain number (6), matrix position, semantic anchor (`Execution`), seven-Domain partition, seven lifecycle Stages, Stage 5 name (`Operate`), and the `ECF = Domain × Stage = 49 coordinates` construction.

## [v2.4.0-migration] - 2026-09-07

CR-CATALOG-STRUCT-09 implementation: ECF Domain enum migration to the
v2.4.0 canonical Domain set (carried by `technehub-labs/dea-metaframework`
v2.4.0; CR-ECF-007 + ADR-ECF-002). One of seven Domains renamed: Domain 3
`PeopleAndOrganization` -> `AgencyAndOrganization` (kebab-case
`people-organization` -> `agency-organization`), driven by the Substrate
Independence Stress Test. 39 files re-keyed (1 schema, 3 scripts, 26 entity
YAMLs, 7 catalog-research files, 2 CR records). Also fixes a pre-existing
bug in `scripts/lib/grid.js` where the six other Domain display labels were
stale from pre-v2.3.0. No content redistribution required (CR-ECF-007 §6.3).

## [v2.3.0-migration] - 2026-09-07

CR-CATALOG-STRUCT-08 implementation: ECF Domain enum migration to the
v2.3.0 canonical Domain set (carried by
`technehub-labs/dea-metaframework` v2.3.0; CR-ECF-006 + ADR-ECF-001).
Five of seven Domains renamed; one Domain replaced (Supply & Resources
-> Strategy & Direction). 53 files modified; no new entities admitted.

This is the **4th and final landing in the v2.3.0 wave** at the
metaframework + metamodel + catalogs tier (after metaframework,
metamodel, and the process catalog).

### Changed

- **Schema enum** (`schemas/entity.schema.json`): the `domain` enum in
  `ecfConformance` updated to the v2.3.0 set.
- **`scripts/check_ecf_conformance.py`**: `CANON_DOMAINS` set updated;
  5 of 7 values flipped; the conformance check now PASS on 26
  entries + MCSP view (verified post-migration).
- **`scripts/migrate_ecf_conformance.py`**: `DOMAIN_MAP` (kebab -> Pascal)
  and `DOMAIN_ID` (kebab -> lowerCamelCase) updated to the v2.3.0 set.
- **30 entity YAMLs** in `entities/v1-alpha/`: every
  `ecf.primary.domain`, `ecf.secondary.domain`, and
  `ecfConformance.canonicalReferences[].domain` updated to the v2.3.0
  kebab-case and PascalCase values.
- **MCSP view** (`mappings/specializations/view-telecom-mcsp.yaml` +
  `VIEW-TELECOM-MCSP.md`): updated.
- **8 catalog-research files** in `catalog-research/`:
  `preliminary-ecf-overlay.yaml`, `admission-review.yaml`,
  `admission-review-supplementary.yaml`,
  `admission-gate-closeout.yaml`, `normalization.yaml`,
  `ECF-OVERLAY-v0.1.md`, `RESEARCH-REPORT-v0.1.md`,
  `ADMISSION-REVIEW-v0.1.md`, `ADMISSION-REVIEW-SUPPLEMENTARY-v0.2.md`.
  Every reference to the v2.2.0 Domain names updated to v2.3.0.
- **1 CR file** (`change-requests/CR-DEA-BC-03.md`): narrative updated.
- **1 doc file** (`docs/FOUNDATIONS.md`): narrative updated.
- **1 lib file** (`scripts/lib/grid.js`): the grid layout labels
  re-keyed to the v2.3.0 display form.

### Not changed (out of scope for the v2.3.0 migration)

- **No new capabilities admitted.** The v2.3.0 wave is a pure rename.
- **The 6 open conflict flags (CAND-008, 010, 017, 018, 019, 028)**
  deliberately held in v0.2 remain unchanged. Their disposition
  references are now keyed to the v2.3.0 Domain names but the
  rationales and decisions are unchanged.
- **The v0.2 ECF Overlay re-derivation** (re-running the candidate
  set against the v2.3.0 Domain taxonomy) is a separate task that
  follows this PR. Parked but ready to dispatch.
- **The 4 pre-existing build-script path bugs** (regenerate_catalog.py,
  check_catalog_index.py, migrate_ecf_conformance.py all look for
  `tools/catalog-index-schema.json` but the schema lives in
  `catalog-index-schema/`) are pre-existing and not introduced by
  this PR.

### Verification

- `scripts/check_ecf_conformance.py`: **PASS** (26 entries + MCSP view
  conform).
- `scripts/check_versions.py`: **PASS** (26 entries conform to
  CR-DEA-BC-05 version discipline).
- `scripts/check_view_refs.py`: runs as expected.
