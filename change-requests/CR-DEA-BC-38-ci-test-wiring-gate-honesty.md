# CR-DEA-BC-38: CI Test Wiring + Gate Honesty (Open-CR Count Semantics, Full Test Suite, Entity-System Strictness)

**Status**: Accepted (user directive 2026-10-27: "lets proceed with the recommendatiobs to fix the repo")
**Layer**: L1 (catalog operations: regenerator semantics, CI wiring, entity-system gate scope)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Full-repo review 2026-10-27: the regenerator reports `open_change_requests` under a status vocabulary this repo never uses; the test suite is half-wired into CI; and the entity-system gate landed with `continue-on-error: true` while its CHANGELOG entry claims blocking strictness. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-38-ci-test-wiring`. Depends on CR-DEA-BC-37 having landed (gate-count arithmetic and green baseline); park until then (GOVERNANCE §2.4).
**Lands against**: `main`

## 1. Problem statement (verified 2026-10-27)

1. **`count_open_change_requests` counts everything open.** `scripts/regenerate_catalog.py:499-529` treats only `Status**: Merged` as closed. This repo's landed-CR status vocabulary is `Landed / Applied / Accepted / Superseded` — zero CR files say "Merged" — so all 42 files count open and `CATALOG.yaml` reports `open_change_requests: 40`. Line 518 carries a copy-paste bug (`if "Status**: Merged" in head or "Status**: Merged" in head:` — second operand meant to be another closed status; the identical bug was found in the processes repo's `regenerate_catalog.py:466`). Table-format metadata (`| **Status** | … |`, 10 of 42 files) is not parsed at all and conservatively counts open.
2. **pytest is installed, not run.** `catalog-conformance.yml` installs pytest in its dependency step; no step ever invokes it. `tests/test_check_entity_system.py` (32 tests) runs nowhere in CI — only `tests/test_check_authorship.py` runs, inside `validate-authorship.yml`.
3. **The entity-system strict gate cannot block.** `validate-entity-system.yml` runs `check_entity_system.py --strict` with `continue-on-error: true`, so its findings are cosmetic. The CHANGELOG BC-35 entry states the workflow "runs gate under `--strict` on every PR" — currently false in effect. Root cause: the gate sweeps the three pre-admission candidate records in `entities/v1-alpha/{epm-5fxren,relmgmt-nu73v9,orgdesign-a7s8bf}/candidates/`, which are state-directory artifacts, not catalog entries — `validate-entries.yml` already excludes `research/`, `candidates/`, `retired/` per CR-CATALOG-STRUCT-01 §5. The two workflows disagree about what counts as an entry.

## 2. Fix 1 — closed-set + table parsing in `count_open_change_requests`

Replace lines 499-529 of `scripts/regenerate_catalog.py` with:

- Closed set: `{Merged, Landed, Applied, Accepted, Rejected, Superseded, Withdrawn}` (statuses actually used in this repo, plus the standard terminal states for future use).
- Open set: `{Proposed, Draft}`; unparseable or missing status stays conservative-open.
- Parse both metadata shapes within the first 30 lines: bold-line `**Status**: X` and table-row `| **Status** | X |`.
- Delete the duplicated condition (the closed set makes it a single membership test).

Derived expectation at this CR's landing (CR inventory = 42 legacy files + BC-37 + this CR; both carriers carry `Accepted` status per the 2026-10-27 user directive, and BC-39 ships in a later PR):

| Counted open (12 at authoring) | Why |
|---|---|
| CR-DEA-BC-14, -17, -19, -mv1 | bold `Proposed` |
| CR-DEA-BC-01A, -03, -04 | table `Proposed`/`Draft`/`Draft` |
| CR-DEA-BC-35-entity-system | table `Proposed (this PR)` — see BC-39 §2; status also needs an update to reflect PR #86 having merged |
| CR-DEA-BC-01, -02, -06, -18 | no status line at all (conservative open; fixing their metadata is BC-39 §4 scope) |

Everything else closes: 14 `Applied`, 11 `Landed`, 4 `Accepted`, 1 `Superseded` (BC-10). Expected `open_change_requests` after this CR lands: **16** (12 above + BC-37/38/39 themselves). The number is smaller than the current 40 — the semantic is "actually open", which is what the field name promises and what the metaframework catalog-index consumers read.

Regenerate `CATALOG.yaml` in the same PR; `--check` must pass afterwards.

## 3. Fix 2 — run the whole test suite in CI

In `catalog-conformance.yml`, after the dependency-install step, add:

```yaml
      - name: Run test suite (tests/)
        run: python -m pytest tests/ -q
```

The venv already installs pytest; no new dependencies. `validate-authorship.yml` keeps its focused run (it also serves as the gate's canary under `if: always()`); the duplication is one cheap step and keeps each workflow self-diagnosing.

## 4. Fix 3 — entity-system gate scope, then honest strictness

1. `scripts/check_entity_system.py`: exclude state directories (`research/`, `candidates/`, `retired/`) from the record sweep, mirroring `validate-entries.yml`'s exclusion and citing CR-CATALOG-STRUCT-01 §5 in the exclusion comment. The three `capabilities:candidate-*` ES-001/ES-002 findings disappear because their files leave scope; the 29 canonical `capabilities:capability-*` records still pass ES-001..ES-005.
2. `tests/test_check_entity_system.py`: add a regression test asserting records under `candidates/` are not swept (fixture: a minimal candidate-shaped record with `type: Candidate`).
3. `.github/workflows/validate-entity-system.yml`: remove `continue-on-error: true` from the strict step. Update the CHANGELOG BC-35 entry's claim by appending a dated correction line (landed CRs are not rewritten in place; the correction is recorded, per GOVERNANCE §2.2).
4. **Divergence note**: `check_entity_system.py` was copied verbatim from `dea-catalog-processes` (CR-BP-123 umbrella). This change creates a deliberate local divergence; the same exclusion should be upstreamed to the processes repo (it has the same state-directory convention). Record the divergence in the script header comment so the next verbatim-copy propagator sees it.

## 5. NOT-List

- NOT renaming or editing any capability entity, candidate record, or research artifact (the candidate records stay exactly as they are; they simply leave the gate's scope, as CR-CATALOG-STRUCT-01 §5 already classifies them).
- NOT changing the authorship gate or registry (BC-37 §2 handles the live violations).
- NOT resolving the five naming advisories (check_naming non-strict remains the CI posture; the advisories — `business_object` echo gaps on 4 entries plus the BC-25-exempted EPM marker — are recorded here as a content backlog and stay out of this operational CR).
- NOT the doc-truth restoration (broken hrefs, README/GOVERNANCE staleness, index backfill, renumbering): CR-DEA-BC-39.
- NOT a general dependency-pinning sweep (deferred backlog).

## 6. Acceptance criteria

1. `python scripts/regenerate_catalog.py` produces `open_change_requests` equal to the §2 table recomputed at landing (16 at authoring: 12 legacy + BC-37/38/39), and `--check` exits 0 after commit.
2. `python -m pytest tests/ -q` passes (53 + 1 new regression test) both locally and as a named CI step in `catalog-conformance.yml` (visible in the PR's Actions run).
3. `python scripts/check_entity_system.py --strict` exits 0 with 0 findings on the live tree, and the workflow step no longer carries `continue-on-error`.
4. The CHANGELOG BC-35 entry carries a dated correction note matching the actual blocking posture.
5. `python scripts/check_id_system.py --strict`, `check_versions.py`, `check_ecf_conformance.py`, `check_catalog_index.py --strict` all still exit 0 (scope change must not perturb them).
6. The script header of `check_entity_system.py` records the state-directory divergence from the processes-repo original.

## 7. Verification at landing

PR body records: recomputed open-count manifest (per-file status → open/closed), full pytest output, entity-system gate output before/after the scope change, and live CI URLs for all workflows green with the strict step blocking.
