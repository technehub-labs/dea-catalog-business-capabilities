# CR-DEA-BC-22: Rename Analytics and Intelligence to Insight Management (CR-DEA-BC-21 ratification)

status: "Applied (2026-09-30); user ratified V-A Insight Management on 2026-09-30;
  rename applied with id and name change, version 1.0.0 to 2.0.0, aliases retained,
  and N-022 verdict rename-applied"
**Filed**: 2026-09-30
**Author**: Coder (DEA-Catalog-Business-Capabilities)
**Depends on**: CR-DEA-BC-01 (method), CR-DEA-BC-09 (naming advisory set), CR-DEA-BC-12 (noun-as-ability advisory), CR-DEA-BC-20 (rule 7 + H8 hard gate), CR-DEA-BC-21 (recon + ADR-ES-021)
**Related**: BC-SR-A001 §4 (boundary decision v0.1 preserved), BC-SR-A001 §5 (Analytics carve-out preserved)
**Supersedes**: none (N-017 + N-022 under CR-DEA-BC-20 + CR-DEA-BC-21)
**Companion**: CR-DEA-BC-21 (recon), CR-DEA-BC-20 (parent rule)

## 1. Problem statement

CR-DEA-BC-20 §10 (DP-E) deferred the rename of `dea:capability-analytics-and-intelligence` to a standalone recon because the rename direction depended on resolving a foundational-ability question. CR-DEA-BC-21 conducted the five-step recon and recorded the recommendation in ADR-ES-021: **V-A (Insight Management)**. The user ratified V-A on 2026-09-30.

This CR implements the rename following the BC-09 / BC-12 / BC-20 admission pattern: bump version, update id and name, retain aliases, update CATALOG.yaml, update sibling cross-references, regenerate the canonical capability map.

## 2. Rename specification

| Field | From | To |
|---|---|---|
| id | `dea:capability-analytics-and-intelligence` | `dea:capability-insight-management` |
| name | `Analytics and Intelligence` | `Insight Management` |
| version | `1.0.0` | `2.0.0` (semver-incompatible: name change) |
| aliases | `[Data and Analytics, Insight, Intelligence, Business Intelligence]` | `[Analytics and Intelligence, Data and Analytics, Insight, Intelligence, Business Intelligence]` (legacy alias added for provenance) |
| business_object | `Insight` | `Insight` (unchanged; matches V-A noun-of-product) |
| classification | `BusinessCapability` | `BusinessCapability` (unchanged) |
| domain | `information-management` | `information-management` (unchanged) |
| stages | `[operate]` | `[operate]` (unchanged) |

Rationale for the 2.0.0 major bump: the name change is a semver-incompatible change. Downstream consumers that reference the old id or name must update (or rely on aliases). BC-09 §8 provenance rules require aliases to be retained for cross-reference compatibility.

## 3. Files affected

- `entities/v1-alpha/dea:capability-insight-management/dea:capability-insight-management.yaml` (renamed from `dea:capability-analytics-and-intelligence/`; id, name, version bumped; aliases extended)
- `entities/v1-alpha/` sibling entries' `related_capabilities` + boundary prose references
- `CATALOG.yaml` (Insight Management block replaces Analytics and Intelligence block)
- `schemas/fixtures/example-view-valid.yaml` (id reference)
- `mappings/specializations/view-telecom-mcsp.yaml` (id reference)
- `tools/catalog-index-schema.json` (unchanged; symlink in BC-20 already)
- `OpenDEA_Foundation_Capability_Map_Nested.html` (regenerated; 28 entities, 31 cells)
- `catalog-research/normalization.yaml` (N-022 verdict updated: review-retained-pending-ADR -> reviewed-and-accepted for V-A)
- `catalog-research/evidence-register.yaml` (G11 status updated: open -> closed-on-rename)
- `catalog-research/recon/ADR-ES-021.yaml` (status updated: proposed -> ratified; date recorded)
- `catalog-research/candidates.yaml` (cand_018_vectors V-A marked chosen; V-B/C/D retained for provenance)
- `change-requests/CR-DEA-BC-21.md` (status updated: Proposed -> Ratified; outcome recorded)
- `README.md` (catalog count unchanged at 28; replace Analytics and Intelligence mention with Insight Management; add BC-22 rename note)
- `CHANGELOG.md` (Unreleased Major entry for BC-22)
- `scripts/check_naming.py` (no change; H8 already implemented in BC-20)
- `decisions.md` (D-022 entry: ratification of V-A)

## 4. Acceptance criteria

- [ ] `dea:capability-analytics-and-intelligence` directory renamed to `dea:capability-insight-management`; inside file renamed to match; id, name, version updated; aliases extended.
- [ ] CATALOG.yaml block updated: id, path, version 2.0.0, last_modified '2026-09-30'.
- [ ] All 7 sibling entries' `related_capabilities` + boundary prose updated (Information Management, Knowledge Management, Strategic Planning, Enterprise Performance Management, Technology Management, etc.).
- [ ] `schemas/fixtures/example-view-valid.yaml` and `mappings/specializations/view-telecom-mcsp.yaml` references updated.
- [ ] `OpenDEA_Foundation_Capability_Map_Nested.html` regenerated; 28 entities, 31 cells.
- [ ] All 6 structural gates PASS (check_naming, check_versions, check_ecf_conformance, check_view_refs, check_catalog_index, check_visual_domain_labels).
- [ ] H8 fixture test: the renamed entry `dea:capability-insight-management` passes H8 (Management suffix); no review-retained exemption needed.
- [ ] N-022 verdict updated from `review-retained-pending-ADR` to a final verdict (the simplest: rename target recorded; verdict closes on rename application).
- [ ] ADR-ES-021 status: `proposed` -> `ratified`; ratification date 2026-09-30 recorded.
- [ ] CR-DEA-BC-21 status: `Proposed` -> `Ratified`.
- [ ] README.md updated; CHANGELOG.md updated with Unreleased Major entry.
- [ ] 3 atomic commits: commit 1 (renames + cross-refs + CATALOG); commit 2 (decision-register + ADR-ES-021 ratification + CHANGELOG); commit 3 (README + map + CR-DEA-BC-22 document + CR-DEA-BC-21 ratification).
- [ ] No bare-noun entries remain as canonical (4 reviewed-retained: Strategy Formulation, Operations Management, Enterprise Governance, Security Management, Sourcing and Procurement).

## 5. Out of scope

- EPM admission (CR-DEA-BC-15 provisional; separate track).
- Relationship Management recon (BC-SR-A001 §6; separate track).
- CIT-MGMT unification with CUST-MGMT (deferred per BC-09 §8).
- Changes to BC-13/BC-14/BC-17 admitted entries beyond cross-references.

## 6. References

- `docs/FOUNDATIONS.md` §2 (capability definition) and §7 (noun-as-ability test).
- `TAXONOMY.md` section 1 rules 1.1-1.7 and section 1A.3 (machine-enforcement scope).
- `scripts/check_naming.py` H8 hard gate (BC-20 §6).
- `catalog-research/normalization.yaml` N-015..N-022.
- `catalog-research/evidence-register.yaml` SRC-023/024/025 + G11.
- `catalog-research/recon/INV-AI-v0.1.yaml` (recon inventory).
- `catalog-research/recon/ADR-ES-021.yaml` (recommendation ADR).
- `catalog-research/candidates.yaml` CAND-018 + cand_018_vectors.
- BC-SR-A001 §4 (boundary decision v0.1) and §5 (Analytics carve-out).
- `entities/v1-alpha/dea:capability-analytics-and-intelligence/dea:capability-analytics-and-intelligence.yaml` — current entry (renamed under BC-22).
- CR-DEA-BC-20 §10 (DP-E deferral) and §3.7 (BC-09 advisory set).
- CR-DEA-BC-21 (recon CR; companion).
- `decisions.md` D-022 ratification entry.
- `OpenDEA_Foundation_Capability_Map_Nested.html` — regenerated.