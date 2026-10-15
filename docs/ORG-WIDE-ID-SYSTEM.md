# Org-Wide ID System (dea-catalog-business-capabilities)

**Status**: Confirmed (CR-DEA-BC-35, 2026-10-13)
**Owner**: Coder (for eaojnr)
**Depends on**: `change-requests/CR-DEA-BC-mv1.md` (the migration); `dea-metaframework/docs/id-system.md` (the upstream spec); `dea-metaframework/docs/entity-storage-layout.md` (the upstream flat-layout spec)

This document captures the current id-system posture of the dea-catalog-business-capabilities catalog. It is the single point of reference for any future wave of id-system work (e.g., the dea-catalog-business-objects / dea-catalog-organizational-units wave 3-4 work; any new admission under the org-wide id system; any PR-scoped id-coherence review).

## 1. The post-mv1 id format

### 1.1 Canonical capability entries

| Property | Value |
|---|---|
| Namespace | `capabilities` |
| Format | `capabilities:capability-<slug>-<hash>` |
| Slug | lower-kebab-case, derived from the capability name (the post-rename name; e.g. `enterprise-performance-management`) |
| Hash | 6 hex characters; per `dea-metaframework/docs/id-system.md` section 2.5; deterministic for the slug |
| Example | `capabilities:capability-customer-management-f3n8wb` |

### 1.2 Candidate records (research register)

| Property | Value |
|---|---|
| Namespace | `capabilities` |
| Format | `capabilities:candidate-<slug>-<hash>` |
| Slug | lower-kebab-case, derived from the candidate name |
| Hash | 6 hex characters; same hash logic as canonical |
| Example | `capabilities:candidate-relmgmt-nu73v9` (CAND-004 Stakeholder Relationship Management) |

### 1.3 Specialization views and other record types

The catalog also carries specialization views (e.g. `view-telecom-mcsp`). The post-mv1 id format for views is in the catalog-index schema; see `catalog-index-schema/catalog-index-schema.json` for the id pattern library.

## 2. The migration (CR-DEA-BC-mv1)

CR-DEA-BC-mv1 (2026-09-21; PR #149) migrated the catalog from the legacy `dea:*` id family to the org-wide id system. The migration covered:

- 31 record files (29 canonical capabilities + the then-active candidates): all rewritten to the post-mv1 id format.
- Entity directory layout: `entities/v1-alpha/dea:<id>/` -> `entities/v1-alpha/<slug>-<hash>/` (flat layout per `dea-metaframework/docs/entity-storage-layout.md` section 3).
- Structured cross-references: every `related_capabilities`, specialization-view parent, fixture, and research-register cross-reference rewritten through the migration id map.
- 36 historical artifacts (CHANGELOG, CR docs, catalog-research YAMLs) bannered with the `Layout note (CR-DEA-BC-mv1, 2026-09-21)` note and content kept verbatim. The audit at `reconciliation/cross-check-mv1.md`: 52 artifacts scanned, 16 CLEAN, 36 HISTORICAL-ONLY, 0 NEEDS-FRAMING.
- New blocking gate `scripts/check_id_system.py` (IDM-001..007 + IDM-008 PR-scoped) wired into `catalog-conformance.yml`.
- Vendored STRUCT tools ported to the dual-family id system: `check_catalog_index.py`, `regenerate_catalog.py`, `catalog-index-schema/catalog-index-schema.json`.
- Entity schema `ecf_rationale` maxLength 1000 -> 1280 (the post-mv1 ids are longer; 1280 is the documented length).

The migration id map is at `reconciliation/migration-id-map.yaml` (v3; 38 id_map entries; 11 known_residuals; namespace `capabilities`). The map is idempotent: new admissions add entries; new known_residuals append.

## 3. The current posture (2026-10-13)

| Dimension | Value |
|---|---|
| Canonical capability entries | 29 (all post-mv1 id format) |
| Candidate records | 37 (27 active CAPABILITY; 3 CAPABILITY-CANONICAL; 1 MERGED-INTO-CAND-005; 6 non-CAPABILITY) |
| Specialization views | 1 (`view-telecom-mcsp`, L3, telecom) |
| Legacy `dea:*` ids in structured cross-references | 0 |
| Legacy `dea:*` ids in bannered historical artifacts | 36 (intentional; per the CR-DEA-BC-mv1 audit) |
| IDM-001..007 conformance | CONFORMANT (gate exit 0; 29 records; 0 findings) |
| IDM-008 PR-scoped coherence | wired into CI; the PR review surface |
| CI workflow | `catalog-conformance.yml` (or equivalent; runs `check_id_system.py` in `--strict` mode on every push and PR) |
| Cross-repo coordination | `dea-catalog-release-cut` skill §11 (CR-DEA-BC-36): any release that lands a `capabilities:*` id set change or moves the ECF version triggers the cross-repo sweep |

## 4. What a new admission looks like (worked example: EPM at CR-DEA-BC-23)

The 29th canonical capability (Enterprise Performance Management) was admitted at CR-DEA-BC-23 (2026-10-12). The id-system flow:

1. The candidate record at `catalog-research/candidates.yaml` had the post-mv1 candidate id `capabilities:candidate-epm-5fxren` (5 hex characters per the candidate format).
2. The admission CR (CR-DEA-BC-23) promoted the candidate to canonical: new id `capabilities:capability-enterprise-performance-management-5fxren` (note: the 5fxren hash is preserved across the candidate-to-canonical promotion for traceability).
3. The entity YAML was written at `entities/v1-alpha/enterprise-performance-management-5fxren/capabilities-capability-enterprise-performance-management-5fxren.yaml` (flat layout; id-derived filename).
4. The migration id map was extended (v2 -> v3): 3 new id_map entries (`dea:candidate-epm-5fxren` -> canonical, `dea:capability-enterprise-performance-management` -> canonical, `dea:capability-epm` -> canonical) + 1 new known_residual for the pre-admission candidate id.
5. CATALOG.yaml regenerated; the open_change_requests count incremented; IDM-001..007 conformance confirmed by `check_id_system.py`.

This is the canonical pattern for the next 5-10 admissions.

## 5. What a retirement looks like (worked example: CAND-006 at CR-DEA-BC-30)

A candidate may be retired as either:

- **merged-into** (the construct exists; the candidate is absorbed into an already-admitted capability): the candidate record is marked `MERGED-INTO-<other-candidate-id>` and carries a `merged_into_canonical_id` pointer. Example: CAND-006 (Citizen / Member Relationship) merged into CAND-005 (Customer Management) at N-029 (CR-DEA-BC-30).
- **retired as already-canonical** (the construct is already admitted; the candidate record is the stale pre-admission research record): the candidate record is marked `CAPABILITY-CANONICAL` and carries a `canonical_id` pointer. Example: CAND-005 (Customer Management) at N-025 (CR-DEA-BC-27); CAND-007 (Supplier Management) and CAND-008 (Partner Management) at N-031, N-032 (CR-DEA-BC-32).

Neither retirement changes the canonical id; the canonical id is the source of truth. The candidate record becomes a research-register structural artifact.

## 6. What the gates enforce

`scripts/check_id_system.py` enforces the IDM-001..007 conformance class:

- **IDM-001**: every record in the catalog has an id matching the post-mv1 format (`capabilities:capability-<slug>-<hash>` for canonical; `capabilities:candidate-<slug>-<hash>` for candidate).
- **IDM-002**: the entity directory path is the id-derived slug-hash form (`entities/v1-alpha/<slug>-<hash>/`).
- **IDM-003**: the entity YAML filename is `capabilities-capability-<slug>-<hash>.yaml` (canonical) or `capabilities-candidate-<slug>-<hash>.yaml` (candidate).
- **IDM-004**: the namespace prefix in the id matches the catalog namespace (`capabilities`).
- **IDM-005**: the hash is deterministic and unique for the slug (the 6-hex hash per `dea-metaframework/docs/id-system.md` section 2.5).
- **IDM-006**: cross-references in structured fields use the post-mv1 id (no legacy `dea:*` ids in non-historical context).
- **IDM-007**: each entity dir has a README.md that names the canonical id (per the IDM-007 spec).
- **IDM-008**: PR-scoped coherence (the live check at the PR review surface; reports any id-coherence drift introduced by the PR).

The gate runs in `--strict` mode on every push and PR.

## 7. Cross-repo coordination

The `dea-catalog-release-cut` skill (edited at CR-DEA-BC-36 §11) records the cross-repo coordination pitfall: any release of this catalog that lands a `capabilities:*` id set change or moves the ECF version triggers the cross-repo sweep at CR-DEA-BC-36 §3 for the next cut cycle. The sweep is `gh search code "dea-catalog-business-capabilities@vN.M.P" --owner technehub-labs` (or the local-repo grep equivalent if the API is unreachable).

The 8 sibling repos that may pin a business-capability tag are:

- `technehub-labs/dea-metaframework`
- `technehub-labs/dea-architecture-framework`
- `technehub-labs/dea-catalog-processes`
- `technehub-labs/dea-catalog-business-objects`
- `technehub-labs/dea-catalog-organizational-units`
- `technehub-labs/dea-catalog-actors`
- `technehub-labs/dea-catalog-business-services`
- `technehub-labs/dea-catalog-stakeholders`

The sweep is the audit record for any future id-set change.

## 8. Open follow-ons

- The `capabilities` namespace may need a sibling `capability-type` extension if the next wave of work introduces a new record type (e.g. a `capability-tier` for L0/L1/L2/L3 cross-references). No current need; the catalog-index schema is the spec.
- The 11 known_residuals in `reconciliation/migration-id-map.yaml` are documented and intentional. They are the pre-mv1 ids that survived the migration because they appear in research registers (CHANGELOG, CR docs, catalog-research YAMLs) where rewriting the historical id would be silent history destruction. The bannered-legacy pattern is the standard.
- A future wave (dea-catalog-business-objects, dea-catalog-organizational-units) will need the same org-wide id-system treatment. The pattern is documented here for reuse.

## 9. References

- `change-requests/CR-DEA-BC-mv1.md` (the migration; the source of the post-mv1 id format)
- `change-requests/CR-DEA-BC-35-org-wide-id-system-confirmation.md` (this confirmation audit; the recon `catalog-research/recon/INV-BC-35-v0.1.yaml`)
- `reconciliation/migration-id-map.yaml` (v3; 38 id_map entries; 11 known_residuals)
- `reconciliation/cross-check-mv1.md` (the 52-artifact audit at CR-DEA-BC-mv1)
- `scripts/check_id_system.py` (IDM-001..007 + IDM-008)
- `catalog-index-schema/catalog-index-schema.json` (the id pattern library)
- `dea-metaframework/docs/id-system.md` (the upstream spec)
- `dea-metaframework/docs/entity-storage-layout.md` (the upstream flat-layout spec)
- `change-requests/CR-DEA-BC-36-release-history-reset-and-discipline.md` §11 (the cross-repo coordination pitfall for id-set changes)
