# Release History Archive (dea-catalog-business-capabilities)

**Status**: Fossilised record (CR-DEA-BC-34, 2026-10-13)
**Owner**: Coder (for eaojnr)

This file is the audit record for the v1-alpha.x cuts that were withdrawn by CR-DEA-BC-34 on 2026-10-13. The v1-alpha.x tag set was immature; the carrier CRs and the tag bodies are preserved here in full so that the history is not silently destroyed. The active prior-cut history table is in `docs/VERSIONING.md`; that table records *successful* cuts, not withdrawals.

## v1-alpha.0 (cut 2026-09-02)

- **Tag**: `v1-alpha.0` (annotated)
- **Tag SHA**: `4be5d7e16fcf113c0cec9e0cb18718a320fc1293`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-02 11:15:23 +0800
- **Body (full)**: "Initial v1-alpha baseline (CR-DEA-BC-05). 26 canonical first-order capabilities admitted, 1 specialization view (view-telecom-mcsp), conformance gate enforced on every PR (CG-001..006). Admitted entries (26): Strategy, Strategic Planning, Enterprise Governance, Customer Management, Supplier Management, Partner Management, Offering Management, Marketing, Operations, Financial Stewardship, Financial Management, People/Workforce Management, Workforce Planning, Information Management, Risk Management, Compliance Management, Legal Management, Security Management, Sourcing and Procurement, Asset Management, Facility Management, Change Management, Technology Management (held-unmapped), Resilience Management, Innovation Management, Analytics and Intelligence. ECF contract pin: dea:ecf@1.0.0; Metamodel pin: 1.0.0. See CHANGELOG.md for the full timeline and docs/VERSIONING.md for the normative procedure."
- **Carrier CR**: `change-requests/CR-DEA-BC-05.md`
- **Withdrawal reason**: Pre-mature; the 26 entries listed in the tag body are the v0 corpus names, not the post-rename canonical names. The v0.x class of release tags is the same incident class as the `v0.1.0 / v0.3.0` withdrawals in `dea-catalog-processes` (CR-BP-116).

## v1-alpha.1 (cut 2026-09-07)

- **Tag**: `v1-alpha.1` (annotated)
- **Tag SHA**: `fc07ba7665f94d39d6b47e557e21c0175bab74c0`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-07 23:05:59 +0800
- **Body (full)**: "Substrate-neutral re-statement of workforce capabilities. Catalog version v1-alpha.0 -> v1-alpha.1 (minor, VERSIONING.md section 2.2). Reconciles catalog content with dea-metaframework v2.4.0 (Agency & Organization; ADR-ECF-002 section 5 Substrate Independence Stress Test; CR-ECF-007). Names, business objects, ECF coordinates, aliases, and pins unchanged (N-001 stands): dea:capability-workforce-management and dea:capability-workforce-planning now define the workforce as human and artificial agents, with the specialization boundary enumerating biological and artificial workforce forms. Both entries bump 1.0.0 -> 1.1.0. Includes: CR-DEA-BC-07 substrate-neutral re-statement (PR #48); visual domain-label conformance guard (PR #50); publication pipeline fix: nested entities + escaped display text (PR #51). Historical research artifacts and out/v1-alpha.0/ snapshot untouched (provenance). 26 canonical first-order capabilities admitted. 1 specialization view."
- **Carrier CR**: `change-requests/CR-DEA-BC-07.md`

## v1-alpha.2 (cut 2026-09-08)

- **Tag**: `v1-alpha.2` (annotated)
- **Tag SHA**: `e22840d374f33ef3113c53d1429b1d0f19c92dd0`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-08 10:04:49 +0800
- **Subject line (full)**: "v1-alpha.2 (CR-DEA-BC-08, PR #53): Technology Management coordinated at strategy-direction x build; N-006 superseded by N-006R; 0 held-unmapped; 16 distinct primary coordinates"
- **Body**: empty beyond subject line.
- **Carrier CR**: `change-requests/CR-DEA-BC-08.md`

## v1-alpha.3 (cut 2026-09-08)

- **Tag**: `v1-alpha.3` (annotated)
- **Tag SHA**: `04945946ff85a66c29c5bda4ba4a762762e6964e`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-08 17:50:02 +0800
- **Subject line (full)**: "v1-alpha.3 (CR-DEA-BC-09, PR #54): naming conformance refresh; 5 renames (N-010..N-014); Security retained (N-015); TAXONOMY section 1 rule 2 clarified + section 1A definition template; check_naming.py wired into entry CI"
- **Body**: empty beyond subject line.
- **Carrier CR**: `change-requests/CR-DEA-BC-09.md`

## v1-alpha.4 (cut 2026-09-09)

- **Tag**: `v1-alpha.4` (annotated)
- **Tag SHA**: `ead021de0ef1558482a7769162d2b431a9de0a7a`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-09 21:58:57 +0800
- **Body (full)**: "v1-alpha.4 (CR-DEA-BC-11, PR #62): release-pipeline consolidation on the framework Python. Patch (CR-DEA-BC-11, PR #62). Release-pipeline consolidation: the first-generation Node-based publication pipeline (CR-DEA-BC-06 + CR-DEA-BC-10) is superseded by the framework Python scripts/generate_capability_map.py, which natively emits the L0 ⊃ L1 ⊃ L2 capability × ECF map (HTML + A3 landscape PNG) via weasyprint + pdftoppm. No Node, no Chrome, no playwright, no sharp. The release zip shrinks from 12 files to 2 (capability-map.html + capability-map-a3.png). Consumer-facing migration: any consumer pinned to retired artifacts (poster.svg/png, map.svg/png, catalog.svg/png, catalog.csv, catalog.json, overlay.yaml/json, dependencies.yaml, MANIFEST.md) must migrate. See docs/publication-pipeline.md section 'Migration from the BC-06 / BC-10 pipeline' for the full replacement table. The framework will gain a --emit-sidecars mode in a follow-up CR if any consumer needs the lost machine-readable endpoints. Operational changes: scripts/publish.js, scripts/publish-mockups/, scripts/lib/, scripts/render_map_png.mjs, and the Node-based publication tooling are removed. The framework Python tooling lives in dea-metaframework and is invoked as a library."
- **Carrier CR**: `change-requests/CR-DEA-BC-11.md`

## v1-alpha.5 (cut 2026-09-10)

- **Tag**: `v1-alpha.5` (annotated)
- **Tag SHA**: `246e010a3765309d22269daee6484e091cfd3054`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-10 06:35:51 +0800
- **Body (full)**: "Carrier: CR-DEA-BC-12 (PR #65). Six high-confidence ECF coordinate re-mappings per BC-SR-A001 section 8.A, section 9, section 10, section 11, section 13 (Strategy, Strategic Planning, Asset, Facility, Supplier, Sourcing & Procurement). Each affected entry advances 1.0.0 -> 1.1.0. Identity unchanged. Three evidence-led investigation tracks opened (no admission in this release): Track A: Organizational Design (BC-SR-A001 section 4 P1); Track B: Enterprise Performance Management (BC-SR-A001 section 5 P1); Track C: Relationship Management generic parent (BC-SR-A001 section 6 P1-P2). Submittal-review infrastructure introduced: submittal-reviews/ (README, TEMPLATE, BC-SR-A001); docs/REVIEWS.md (per-release submittal-review commentary). Doc drift closed: README + metamodel-pointer.yaml: Catalog Status planned -> populated; README: three-version-pin disambiguation (catalog / metamodel / ECF conformance contract / architecture framework)."
- **Carrier CR**: `change-requests/CR-DEA-BC-12.md`

## v1-alpha.6 (cut 2026-09-10)

- **Tag**: `v1-alpha.6` (annotated)
- **Tag SHA**: `0c943b2bc8a01b573a4a81328a98465e7073d19b`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-10 07:43:50 +0800
- **Body (full)**: "Carrier: CR-DEA-BC-13 (PR #66). Method-CR codifying BC-SR-A001 section 14's ECF primary-coordinate rule refinement. Replaces the pre-CR-13 'earliest initiation point' rule with 'semantic center of gravity' in METHODOLOGY.md section 8, and re-evaluates all 26 canonical entries under the new rule. Six entries changed: asset-management, facility-management, sourcing-and-procurement, supplier-management: primary moves to operate (the defining activity of these caps is sustained stewardship, not the build/activate/conceive event); partner-management: secondary fix (strategy-direction/operate -> party-relationship/operate); technology-management: carve-text only (Tech-as-Estate vs Tech-as-Enabler formalized per BC-SR-A001 section 12). Per-entity versions: asset/facility/sourcing/supplier/technology 1.1.0 -> 1.2.0; partner 1.0.0 -> 1.1.0; others unchanged. Three investigation tracks opened under candidates/ (non-canonical, no admission): Track A Organizational Design; Track B Enterprise Performance Management; Track C Relationship Management."
- **Carrier CR**: `change-requests/CR-DEA-BC-13.md`

## v1-alpha.7 (cut 2026-09-10)

- **Tag**: `v1-alpha.7` (annotated)
- **Tag SHA**: `1a6bc6ba7a9a399de21e1548253920fe55699123`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-10 16:31:21 +0800
- **Body (full)**: "Carrier: CR-DEA-BC-17 (PR #67). Admission-CR closing BC-SR-A001 section 12. Admits dea:capability-technology-enablement as the 27th first-order canonical capability at enablement-operations/operate (primary), with enablement-operations/{build, improve} as secondaries. New entry: dea:capability-technology-enablement v1.0.0 (Tech delivery function). Tech Mgmt: 1.2.0 -> 1.3.0 (Minor; boundary-text + related_capabilities). Operations: 1.0.0 -> 1.0.1 (Patch; cross-reference patch). Info Mgmt: 1.0.0 -> 1.0.1 (Patch; cross-reference patch). Others: unchanged. The carve BC-SR-A001 section 12 asked us to make explicit is now a peer relationship between two first-order capabilities rather than as a deferred specialization. Tech Mgmt = IT direction (estate; strategy-direction/build). Tech Enablement = IT delivery (services; enablement-operations/operate). enablement-operations/operate cell occupancy: 6 -> 7. Also note: CR-DEA-BC-18 research-CR lands as a v1-alpha.7 addendum (BC-SR-A001 section 4 Track A evidence package; no canonical change). Unblocks CR-DEA-BC-14."
- **Carrier CR**: `change-requests/CR-DEA-BC-17.md`

## v1-alpha.8 (cut 2026-09-11)

- **Tag**: `v1-alpha.8` (annotated)
- **Tag SHA**: `7140cf8809e62913cecc858c29b85dcb8aaf6196`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-11 01:43:50 +0800
- **Body (full)**: "CR-DEA-BC-14 (PR #71): Admit Organizational Design as the 28th first-order canonical capability at agency-organization/design (primary) + agency-organization/{conceive, build} (secondaries). Closes BC-SR-A001 section 4 (reviewer P1), BC-13 section B.1 (Track A investigation opened), TER-ORGDESIGN-001 (open -> closed), CAND-036 (E3 -> E4 per EVIDENCE.md section 3 admission promotion rule). Catalog: 27 -> 28 first-order canonical capabilities. agency-organization/design cell-occupancy 3 -> 4 (within monopartite band per METHODOLOGY section 11). 8 existing entries updated (Patch-tier; related_capabilities + boundary-text exclusion extension): strategy 1.1.0 -> 1.1.1; strategic-planning 1.1.0 -> 1.1.1; workforce-management 1.1.0 -> 1.1.1; workforce-planning 1.1.0 -> 1.1.1; change-management 1.0.0 -> 1.0.1; technology-management 1.3.0 -> 1.3.1; technology-enablement 1.0.0 -> 1.0.1; enterprise-governance 1.0.0 -> 1.0.1. Distinctness sweep extended 6 -> 8 peers (added Enterprise Governance + Change Management). Research-artifact bookkeeping bumped (candidates.yaml v0.4.0; evidence-register.yaml v0.6.0; preliminary-ecf-overlay.yaml v0.4.0; distinctness-sweep.yaml v0.4.0; admission-gate-precheck.yaml v0.7.0; INV-ORGDESIGN-v0.2.yaml v0.2.0)."
- **Carrier CR**: `change-requests/CR-DEA-BC-14-track-a-orgdesign-admission.md`

## Pre-tag abandoned sections (withdrawn from CHANGELOG.md)

- `## [v1-alpha.0-pipeline-live] - 2026-09-04` (was CHANGELOG.md line 582-612)
- `## [STRUCT-03a] - 2026-09-05` (was CHANGELOG.md line 537-581)
- `## [STRUCT-03b] - 2026-09-05` (was CHANGELOG.md line 495-536)

These were pre-tag state markers; no tags were ever cut on top of them. Withdrawn 2026-10-13 as part of the v1-alpha.x reset.

## Cross-reference

The active prior-cut history table is in `docs/VERSIONING.md` (it is empty post-reset; future successful cuts append rows). The reset procedure that produced this archive is documented in `change-requests/CR-DEA-BC-34-release-history-reset-and-discipline.md`. The companion process-repo reset (CR-BP-116) is the reference procedure.
