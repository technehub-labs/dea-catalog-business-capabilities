# CR-CATALOG-STRUCT-03a: Business Capability Catalog Adoption (Layout + Index)

**Status**: Proposed
**Layer**: L1 (Business Capability Catalog)
**Owner**: TechNeHub Labs
**Depends on**: CR-CATALOG-STRUCT-01 (merged), CR-CATALOG-STRUCT-06a/b (merged), CR-CATALOG-STRUCT-02 (merged; pattern reference)
**Supersedes**: none
**Related**: CR-CATALOG-STRUCT-03b (research distribution; future), CR-CATALOG-STRUCT-04..05 (other adoptions), CR-CATALOG-STRUCT-07 (cross-repo consumer)
**Authority**: Mandatory; enforced by CI on every PR

---

## 1. Purpose

First half of `technehub-labs/dea-catalog-business-capabilities` adoption of the catalog repository standard (CR-CATALOG-STRUCT-01). This CR covers Step 1 (layout) and Step 3 (catalog index + CI gate) for all 26 canonical Business Capability entries. Step 2 (research distribution) lands in CR-CATALOG-STRUCT-03b.

The BC catalog is the largest adoption by content volume: 26 canonical entries + 33 research files. Splitting the adoption into two PRs keeps review surface bounded. This CR (03a) brings the catalog to "conforming-but-research-not-distributed"; 03b finishes the migration.

## 2. Scope

**In scope**:

- **Step 1: per-entity subtree layout for all 26 entities**. Move each `entities/v1-alpha/capability-*.yaml` into `entities/v1-alpha/dea:capability-*/dea:capability-*.yaml` with empty `research/`, `candidates/`, `retired/` state directories.
- **Catalog index + CI gate**: vendor `scripts/regenerate_catalog.py`, `scripts/check_catalog_index.py`, `catalog-index-schema/catalog-index-schema.json` from `dea-metaframework/tools/`. Generate and commit `CATALOG.yaml`. Write `TEMPLATE_VERSION` (`0.1.0`).
- **`metamodel-pointer.yaml` augmentation**: add top-level catalog identity block (id/name/abbreviation/version/status/metamodel_version/owner). The existing nested `metamodel:` and `catalog:` blocks remain untouched. The existing root-level `description:` field (placed after the `catalog:` block) is the one the regenerator picks up.
- **New CI workflow**: `.github/workflows/catalog-conformance.yml` runs the standard's regenerator + gate + cross-repo conformance suite (CST-001..CST-016). The five existing workflows (`validate-entries`, `validate-allocation`, `ecf-conformance-consumer`, `publish-versioned`, `publish-latest`) are unchanged.
- **Bug fix in `scripts/check_ecf_conformance.py`**: walk the subtree layout recursively; skip files under `research/`, `candidates/`, `retired/`.
- **Bug fix in `scripts/check_versions.py`**: same recursive walk + state-directory filter.
- **Empty cross-cutting directories**: `classifications/`, `contributions/` get `.gitkeep` so the gate's cross-cutting sanity checks pass (the catalog never had these directories).

**Out of scope (deferred to CR-CATALOG-STRUCT-03b)**:

- Distribution of the 33 research files in `docs/research/` into per-entity `research/` subdirs.
- Per-entity `research/README.md` provenance docs.

## 3. Definitions

- **Per-entity subtree**: `entities/v1-alpha/dea:capability-<name>/`. The 26 capability IDs were already canonical (CR-BP-04 alignment was done before this CR); the move is purely structural.
- **State directory**: empty `research/`, `candidates/`, `retired/` per subtree. Standard §5 allows empty dirs; CST-009 fires only when non-empty state dirs lack `README.md`.
- **Hand-rolled adoption**: `TEMPLATE_VERSION` is written manually (`0.1.0`), matching the canonical template at the time of authoring. The standard's §13 retroactive schedule allows hand-rolling; bootstrap-in-place would lose the BC-01..BC-06 commit history attribution.

## 4. Design

### 4.1 Layout migration (Step 1)

All 26 entities move in one commit. The capability IDs (`dea:capability-*`) are unchanged; only the file path changes. The git `mv` preserves rename detection in `git log --follow`.

| Before | After |
|---|---|
| `entities/v1-alpha/capability-<name>.yaml` | `entities/v1-alpha/dea:capability-<name>/dea:capability-<name>.yaml` |
| (does not exist) | `entities/v1-alpha/dea:capability-<name>/research/` |
| (does not exist) | `entities/v1-alpha/dea:capability-<name>/candidates/.gitkeep` |
| (does not exist) | `entities/v1-alpha/dea:capability-<name>/retired/.gitkeep` |

The directory `entities/v1-alpha/README.md` (catalog README for the entities tree) is preserved as-is.

### 4.2 metamodel-pointer.yaml augmentation

The file is marked "Auto-generated from OpenDEAM v0.2.1; do not edit manually" for the nested `metamodel:` and `catalog:` blocks (allocation data). Catalog identity (`id`/`name`/`abbreviation`/`version`/`status`/`metamodel_version`/`owner`) is the catalog author's concern, not the root model's. The standard's regenerator reads top-level keys, so the augmentation adds the identity block at the top.

The existing root-level `description:` field (placed after the `catalog:` block) is the description the regenerator picks up. The augmentation does NOT add a second `description:` (which would cause a YAML duplicate-key error); the existing field is authoritative.

### 4.3 Catalog index + CI gate

The standard's machinery is vendored under `scripts/` and `catalog-index-schema/`. CI runs:

1. `python scripts/regenerate_catalog.py --check` (CST-001..005 via regenerator).
2. `python scripts/check_catalog_index.py --strict` (schema + structural sanity).
3. `python .metaframework/tools/conformance_test_catalog_structure.py --strict` (CST-001..CST-016).

The workflow sets the canonical git origin URL (`https://github.com/${GITHUB_REPOSITORY}.git`) before running the regenerator; `actions/checkout@v4` sets origin without a `.git` suffix, which would otherwise produce stale-CATALOG.yaml CI failures (same fix as the process catalog's STRUCT-02 PR #21).

The five existing workflows (`validate-entries`, `validate-allocation`, `ecf-conformance-consumer`, `publish-versioned`, `publish-latest`) are not modified. They continue to do their specialized work; the new `catalog-conformance` workflow is additive.

### 4.4 Bug fix in catalog-specific validators

`scripts/check_ecf_conformance.py` and `scripts/check_versions.py` both used flat globs (`capability-*.yaml`). After Step 1, those globs match zero files. Both now use recursive globs with the standard's state-directory filter.

`scripts/check_ecf_conformance.py` previously reported "no entries found" or passed with 0 entries; it now finds all 26 entries and verifies each carries the `ecfConformance` block per CR-ECF-CG-003. The fix is purely structural (no logic change beyond the file discovery).

### 4.5 Cross-cutting directory creation

The standard's `cross_cutting` section enumerates `classifications/`, `schemas/`, `validators/`, `contributions/`, `change-requests/` as required paths. The BC catalog has `schemas/` and `scripts/` (validators) and `change-requests/` already; `classifications/` and `contributions/` did not exist. Both are created with a `.gitkeep` placeholder so the gate's cross-cutting sanity check (`cross_cutting.<label>: path ... not found`) passes.

## 5. Files

**New** (5):

- `CATALOG.yaml` (machine-generated; ~7 KB; lists 26 entities).
- `TEMPLATE_VERSION` (`0.1.0`).
- `scripts/regenerate_catalog.py` (vendored from `dea-metaframework/tools/`).
- `scripts/check_catalog_index.py` (vendored).
- `catalog-index-schema/catalog-index-schema.json` (vendored).
- `.github/workflows/catalog-conformance.yml` (new CI workflow; runs regenerator + gate + conformance suite).
- `change-requests/CR-CATALOG-STRUCT-03a.md` (this document).
- `entities/v1-alpha/dea:capability-<each>/{research/, candidates/.gitkeep, retired/.gitkeep}` × 26 (empty state dirs).

**Modified** (4):

- `metamodel-pointer.yaml` (additive top-level identity block).
- `scripts/check_ecf_conformance.py` (recursive walk + state-directory filter).
- `scripts/check_versions.py` (same).
- `CHANGELOG.md` (`[Unreleased]` entry).
- `change-requests/README.md` (CR-CATALOG-STRUCT-03a row; flips existing CRs as needed).

**Empty directory created with `.gitkeep`**: `classifications/`, `contributions/`.

## 6. Conformance contract

This CR is conformant iff:

1. All 3 existing catalog validators (`check_ecf_conformance`, `check_versions`, `check_view_refs`) PASS.
2. `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json` exits 0.
3. `python scripts/check_catalog_index.py --strict --schema ...` exits 0.
4. `python .metaframework/tools/conformance_test_catalog_structure.py --strict` exits 0 with 0 warnings.
5. `git diff --check` clean.
6. Dash-clean on all new prose.
7. No secrets introduced.

## 7. Decisions log

### D-STRUCT-03a-001: Split into 03a (this) + 03b (research distribution)

Per the planning conversation's Path 2 recommendation: 26 entities is too many to review in a single PR when research distribution (33 files) is also in flight. Splitting keeps review surface bounded; the standard allows transient non-conformance during a migration.

### D-STRUCT-03a-002: All 26 entities in one commit

Per the planning conversation's Q2 decision (b): one commit per migration state. Step 1 is one commit; Step 2 (research) is in 03b's single commit. Atomic per state.

### D-STRUCT-03a-003: New `catalog-conformance.yml` workflow, not modifying existing

The 5 existing workflows (`validate-entries`, `validate-allocation`, `ecf-conformance-consumer`, `publish-versioned`, `publish-latest`) have specialized purposes. Adding a 6th workflow keeps their contracts intact and isolates the standard's machinery. Adoption CRs do not modify existing workflows unless required.

### D-STRUCT-03a-004: `--strict` from day one

Per the planning conversation's Q3 decision (a): the standard is the standard. Soft-landing costs discipline. If a follow-up needs an exception, that's a separate CR with rationale.

### D-STRUCT-03a-005: Cross-cutting dirs created with `.gitkeep`

The standard's `cross_cutting` section requires the dirs to exist. The BC catalog didn't have `classifications/` or `contributions/`. Creating them with `.gitkeep` is the cheapest path to conformance.

### D-STRUCT-03a-006: Empty state dirs use `.gitkeep`; non-empty dirs use `README.md`

Per the standard's CST-009: `research/`, `candidates/`, `retired/` directories with files require a `README.md`. Empty dirs (this CR's state) use `.gitkeep` because git doesn't track empty dirs.

## 8. Usage

After this CR merges:

```bash
# Verify conformance locally
python /path/to/dea-metaframework/tools/conformance_test_catalog_structure.py \
    --catalog-root . \
    --template-root /path/to/dea-metaframework/tools/catalog-repo-template \
    --strict

# Refresh CATALOG.yaml after adding/removing entities
python scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json

# Validate the committed index
python scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json

# Run the full local validator suite
python scripts/check_ecf_conformance.py
python scripts/check_versions.py
python scripts/check_view_refs.py
```

CI runs the same steps on every PR; failures block merge.

## 9. Out of scope (deferred)

- **STRUCT-03b**: research distribution (33 files into per-entity `research/` subdirs with provenance READMEs).
- **STRUCT-04..05**: other catalog adoptions.
- **STRUCT-07**: cross-repo consumer.

## 10. Acceptance criteria

1. All 3 existing validators PASS.
2. Regenerator --check exits 0.
3. Gate --strict exits 0.
4. Conformance --strict exits 0 with 0 warnings.
5. CR doc is dash-clean.
6. No secrets introduced.
7. CHANGELOG, CR README, and adoption tracker updated.
8. CI on the branch is green (5 existing workflows + 1 new workflow = 6 checks).

## 11. Risks

- **R-STRUCT-03a-001**: Vendored regenerator/gate drift from `dea-metaframework` `main`. Mitigation: re-vendor on every `TEMPLATE_VERSION` bump; CI's fetch step refreshes if the vendored copy is missing.
- **R-STRUCT-03a-002**: `metamodel-pointer.yaml` is "auto-generated from OpenDEAM"; manual edits could be lost on next regeneration. Mitigation: the catalog identity block is separated from the allocation block by an explicit comment; future OpenDEAM regenerators should preserve top-level scalar keys.

## 12. Open questions

None at authoring time. Resolved during planning:

- One-shot vs two stacked PRs (D-001).
- Single commit per state (D-002).
- New workflow vs modify existing (D-003).
- `--strict` from day one (D-004).

## 13. Related

- CR-CATALOG-STRUCT-01 (merged): the standard this CR implements.
- CR-CATALOG-STRUCT-06a (merged): the regenerator + gate + schema.
- CR-CATALOG-STRUCT-06b (merged): the conformance suite + template + bootstrap.
- CR-CATALOG-STRUCT-02 (merged): pattern reference (process catalog adoption).
- CR-CATALOG-STRUCT-03b (planned): research distribution follow-up.
- CR-DEA-BC-01..06 (all landed): the BC method CRs that produced the 26 entries being moved.

---

## Appendix A: Per-entity move map

All 26 entries follow the same pattern:

| Before | After |
|---|---|
| `entities/v1-alpha/capability-analytics-and-intelligence.yaml` | `entities/v1-alpha/dea:capability-analytics-and-intelligence/dea:capability-analytics-and-intelligence.yaml` |
| `entities/v1-alpha/capability-asset-management.yaml` | `entities/v1-alpha/dea:capability-asset-management/dea:capability-asset-management.yaml` |
| `entities/v1-alpha/capability-change-management.yaml` | `entities/v1-alpha/dea:capability-change-management/dea:capability-change-management.yaml` |
| `entities/v1-alpha/capability-compliance-management.yaml` | `entities/v1-alpha/dea:capability-compliance-management/dea:capability-compliance-management.yaml` |
| `entities/v1-alpha/capability-customer-management.yaml` | `entities/v1-alpha/dea:capability-customer-management/dea:capability-customer-management.yaml` |
| `entities/v1-alpha/capability-enterprise-governance.yaml` | `entities/v1-alpha/dea:capability-enterprise-governance/dea:capability-enterprise-governance.yaml` |
| `entities/v1-alpha/capability-facility-management.yaml` | `entities/v1-alpha/dea:capability-facility-management/dea:capability-facility-management.yaml` |
| `entities/v1-alpha/capability-financial-management.yaml` | `entities/v1-alpha/dea:capability-financial-management/dea:capability-financial-management.yaml` |
| `entities/v1-alpha/capability-financial-stewardship.yaml` | `entities/v1-alpha/dea:capability-financial-stewardship/dea:capability-financial-stewardship.yaml` |
| `entities/v1-alpha/capability-information-management.yaml` | `entities/v1-alpha/dea:capability-information-management/dea:capability-information-management.yaml` |
| `entities/v1-alpha/capability-innovation-management.yaml` | `entities/v1-alpha/dea:capability-innovation-management/dea:capability-innovation-management.yaml` |
| `entities/v1-alpha/capability-legal-management.yaml` | `entities/v1-alpha/dea:capability-legal-management/dea:capability-legal-management.yaml` |
| `entities/v1-alpha/capability-marketing.yaml` | `entities/v1-alpha/dea:capability-marketing/dea:capability-marketing.yaml` |
| `entities/v1-alpha/capability-offering-management.yaml` | `entities/v1-alpha/dea:capability-offering-management/dea:capability-offering-management.yaml` |
| `entities/v1-alpha/capability-operations.yaml` | `entities/v1-alpha/dea:capability-operations/dea:capability-operations.yaml` |
| `entities/v1-alpha/capability-partner-management.yaml` | `entities/v1-alpha/dea:capability-partner-management/dea:capability-partner-management.yaml` |
| `entities/v1-alpha/capability-resilience-management.yaml` | `entities/v1-alpha/dea:capability-resilience-management/dea:capability-resilience-management.yaml` |
| `entities/v1-alpha/capability-risk-management.yaml` | `entities/v1-alpha/dea:capability-risk-management/dea:capability-risk-management.yaml` |
| `entities/v1-alpha/capability-security-management.yaml` | `entities/v1-alpha/dea:capability-security-management/dea:capability-security-management.yaml` |
| `entities/v1-alpha/capability-sourcing-and-procurement.yaml` | `entities/v1-alpha/dea:capability-sourcing-and-procurement/dea:capability-sourcing-and-procurement.yaml` |
| `entities/v1-alpha/capability-strategic-planning.yaml` | `entities/v1-alpha/dea:capability-strategic-planning/dea:capability-strategic-planning.yaml` |
| `entities/v1-alpha/capability-strategy.yaml` | `entities/v1-alpha/dea:capability-strategy/dea:capability-strategy.yaml` |
| `entities/v1-alpha/capability-supplier-management.yaml` | `entities/v1-alpha/dea:capability-supplier-management/dea:capability-supplier-management.yaml` |
| `entities/v1-alpha/capability-technology-management.yaml` | `entities/v1-alpha/dea:capability-technology-management/dea:capability-technology-management.yaml` |
| `entities/v1-alpha/capability-workforce-management.yaml` | `entities/v1-alpha/dea:capability-workforce-management/dea:capability-workforce-management.yaml` |
| `entities/v1-alpha/capability-workforce-planning.yaml` | `entities/v1-alpha/dea:capability-workforce-planning/dea:capability-workforce-planning.yaml` |

Each entry's subtree also gets `research/` (empty), `candidates/.gitkeep`, and `retired/.gitkeep` per the standard.
