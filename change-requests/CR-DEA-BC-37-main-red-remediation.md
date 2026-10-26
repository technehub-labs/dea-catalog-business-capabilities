# CR-DEA-BC-37: Main-Red Remediation (Authorship Backfill + CATALOG Freshness + CST Pinning)

**Status**: Accepted (user directive 2026-10-27: "lets proceed with the recommendatiobs to fix the repo")
**Layer**: L1 (catalog operations: CI, index, landed-CR corrections)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Full-repo review 2026-10-27 (user directive: "lets review and enhance this repo") found `main` @ `848b163` red on two blocking workflows. This CR is the minimal carrier that returns `main` to green without changing any catalog content. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1 (CR-BP-118 / CR-DEA-BC-34).
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-37-main-red-remediation`. PR review, not direct push (CR-BP-116 pattern).
**Lands against**: `main`

## 1. Problem statement (verified 2026-10-27, `main` @ `848b163`)

| Check | Command | Result |
|---|---|---|
| Authorship gate | `python scripts/check_authorship.py --strict` | exit 1 — three AUT-001 blocking findings |
| Live-tree tests | `python -m pytest tests/test_check_authorship.py` | 2 failed (the live-tree AUT-001 tests), 21 total |
| Index freshness | `python scripts/regenerate_catalog.py --check` | exit 3 — `CATALOG.yaml` stale (`open_change_requests: 39` vs computed 40) |
| Structure conformance | metaframework CST suite, `--strict` | exit 2 — CST-013 + CST-014 (unpinned `dea-metaframework` checkout) |

`validate-authorship.yml` and `catalog-conformance.yml` run these blocking on every push/PR: PRs #88 and #89 merged red, and every subsequent PR inherits the red.

## 2. Authorship corrections (recorded, not silent rewrites)

GOVERNANCE §2.2: landed CRs are immutable; corrections are recorded by later PRs. This section is that record. The corrections target fields authored 2026-10-13, *after* the CR-DEA-BC-34 retro-sweep had cleaned the tree — i.e. these are regressions against R1 (AUT-001), not sweep misses.

| File | Line | Field | Current value | Corrected value |
|---|---|---|---|---|
| `change-requests/CR-DEA-BC-34-release-history-reset-and-discipline.md` | 5 | `**Owner**` | `Coder (for eaojnr)` | `Emmanuel A. Otchere` |
| `change-requests/CR-DEA-BC-35-org-wide-id-system-confirmation.md` | 5 | `**Owner**` | `Coder (for eaojnr)` | `Emmanuel A. Otchere` |
| `catalog-research/recon/INV-BC-35-v0.1.yaml` | 4 | `author` | `Coder (for eaojnr)` | `Emmanuel A. Otchere` |

The agency narrative is preserved in prose (each affected document already records the 2026-10-13 user directive and ratification in its Trigger/body); only the authorship-of-record value changes. The corrections are also summarized under "Corrections to landed CRs" in `change-requests/README.md`.

## 3. CATALOG.yaml freshness

Regenerate `CATALOG.yaml` (`python scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json`) in the same PR. The committed count (39) lags the computed count (40) because the file was not regenerated when CR files landed; the landing of this CR (one new Proposed CR file) is itself a count-changing event and the regeneration picks it up in the same PR, per the house landing convention.

## 4. CST-013/CST-014: pin the metaframework checkout

`catalog-conformance.yml` step "Fetch catalog index machinery from dea-metaframework" checks out `technehub-labs/dea-metaframework` with no `ref:`. CST-013/CST-014 require a release-tag pin so the toolchain is reproducible. Change:

```yaml
        with:
          repository: technehub-labs/dea-metaframework
          path: .metaframework
          ref: v2.6.0          # latest release tag at authoring; re-verify locally at landing
```

Landing note: the CST suite and the vendored-script preference must be re-verified against the pinned tag locally before merge (the review verified 14/16 CST pass at metaframework `3ad9bdd`, which is v2.6.0 + one chore commit; the two failures are exactly the pin checks this change satisfies).

## 5. NOT-List

- NOT a catalog-content change: no entity, id, schema, mapping, or research-register content changes.
- NOT a fix for the `count_open_change_requests` semantics (closed-set, duplicated condition at `scripts/regenerate_catalog.py:518`, table-format parsing): the mechanical regeneration in §3 uses the regenerator *as-is*; the semantic fix is CR-DEA-BC-38 §2, which re-derives the count and regenerates again. Splitting them keeps each PR's diff auditable (§3 = no logic change; BC-38 §3 = logic change + regeneration).
- NOT a renumbering of the misfiled BC-36 / colliding BC-35 files (CR-DEA-BC-39 §2).
- NOT a CI-dependency pinning sweep (deferred backlog; CR-DEA-BC-39 §8 records it).
- NOT an edit to the authorship gate, its registry, or its denylist.

## 6. Acceptance criteria (all verifiable from a clean clone of the landing PR)

1. `python scripts/check_authorship.py --strict` exits 0 with 0 AUT-001/002/003 findings.
2. `python -m pytest tests/ -q` reports 53 passed, 0 failed.
3. `python scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json` exits 0.
4. The metaframework conformance suite (`conformance_test_catalog_structure.py --catalog-root . --template-root <pinned-tag>/tools/catalog-repo-template --strict`) exits 0 (16/16).
5. `git diff` of the PR touches exactly: the three files in §2, `CATALOG.yaml`, `.github/workflows/catalog-conformance.yml`, `change-requests/README.md` (this CR's row + §2 correction note), `CHANGELOG.md` (`[Unreleased]` entry), and this CR file.
6. GitHub Actions on the PR head shows `validate-authorship`, `catalog-conformance`, `validate-entries`, `validate-entity-system`, `validate-allocation`, `ecf-conformance-consumer` all green (entity-system strict remains advisory via its existing `continue-on-error` until CR-DEA-BC-38 §3).

## 7. Verification at landing

Record in the PR body: gate outputs for §6.1–§6.4, the CST pin tag used, and live CI URLs. Post-merge CI on `main` must be green — this is the acceptance test for the whole CR.
