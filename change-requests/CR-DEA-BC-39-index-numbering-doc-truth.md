# CR-DEA-BC-39: Index, Numbering, and Doc-Truth Restoration (+ Recurrence Gates)

**Status**: Accepted (user directive 2026-10-27: "lets proceed with the recommendatiobs to fix the repo")
**Layer**: L1 (catalog governance: CR index, numbering, documentation truth)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-27
**Trigger**: Full-repo review 2026-10-27: the CR series index stopped at BC-19/mv1 while the series ran to BC-36; two CR numbers are double-allocated and one landed CR is filed under the wrong number entirely; 23 relative hrefs are broken across 7 files; README/GOVERNANCE/`dependencies.yaml` contradict the post-reset state of the catalog. Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-39-index-numbering-doc-truth`. Lands after CR-DEA-BC-37 and CR-DEA-BC-38 (sequence is soft; only the CATALOG regeneration arithmetic depends on order).
**Lands against**: `main`

## 1. Problem statement (verified 2026-10-27)

1. **Index drift.** `change-requests/README.md` carries rows only through BC-19/mv1. Missing rows: BC-20, -21, -22, -23, -25, -26, -27, -28, -29, -30, -31, -32, -33 (thirteen landed CRs, PRs #67–#84), BC-34 (authorship slice, PR #85), the misfiled BC-36 (see §2), and BC-35 org-wide (PR #89). The top-table BC-35 entity-system row still reads "**Proposed (this PR)**" although PR #86 merged. The BC-05 row lacks its leading `|`, breaking the table render.
2. **Numbering split-brain.** Files `CR-DEA-BC-34-release-history-reset-and-discipline.md` and `CR-DEA-BC-35-org-wide-id-system-confirmation.md` collide with `CR-DEA-BC-34-authorship-cardinal-rule.md` and `CR-DEA-BC-35-entity-system-business-capabilities.md`. The CHANGELOG's three `[Unreleased]` entries fix the intended identities: BC-34 = authorship, BC-35 = entity-system, BC-36 = release-history reset (PR #88; the CHANGELOG already cites `change-requests/CR-DEA-BC-36-release-history-reset-and-discipline.md` — currently a broken href).
3. **23 broken relative hrefs in 7 files** (manifest in §3), all mechanical: pre-mv1 layout moves and systematic `../../`-depth errors.
4. **Governance docs contradict the data.** README header typo ("inttent"); README "Repository Structure" says "population pending" / entities "empty until then" against a 29-entry populated catalog, and its tree omits `catalog-research/`, `visuals/`, `mappings/`, `classifications/`, `contributions/`, `reconciliation/`, `submittal-reviews/`, `tests/`, `tools/`; README Entity-Definition table and Status paragraph still cite pre-reset versions ("current: v1-alpha.4, tag `570830a`; v1-alpha.5 in CR-DEA-BC-12"); GOVERNANCE §1 claims "`v1-alpha.0`, 26 canonical entries"; GOVERNANCE §2.4 still parks BC-03/BC-04 (both long landed); `dependencies.yaml` pins `ref: v1-alpha.4`, a tag the BC-36 reset withdrew as premature; `docs/governance/cardinal-rules.md:19` cites the processes-repo glob `entities/v1-alpha/**/processes-*.yaml` where this repo's records are `capabilities-*.yaml`.
5. **Four landed CRs carry no machine-readable status** (BC-01, BC-02, BC-06, BC-18), which is why the conservative-open branch of the counter in `regenerate_catalog.py` absorbs them (CR-DEA-BC-38 §2).

## 2. Numbering resolution (per GOVERNANCE §2.1, recorded on the CRs and in the index)

Precedent: CR-DEA-BC-01A (renumbered from an early BC-02 allocation; renumbering recorded on the CR and in the index Numbering section). Unused numbers 11, 15, 16, 24 stay unused (gaps are history; collisions are defects).

| Current file | Renamed to | Rationale |
|---|---|---|
| `CR-DEA-BC-34-release-history-reset-and-discipline.md` | `CR-DEA-BC-36-release-history-reset-and-discipline.md` | Its CHANGELOG `[Unreleased]` entry, PR #88 title, and the CHANGELOG's own citation of the BC-36 filename all fix this CR's identity as BC-36. Heading `# CR-DEA-BC-34:` → `# CR-DEA-BC-36:`; a one-line renumbering note is appended directly under the heading; historical branch names in the Carrier narrative stay verbatim (they are record, not identity). Fixes the CHANGELOG broken href as a side effect. |
| `CR-DEA-BC-35-org-wide-id-system-confirmation.md` | `CR-DEA-BC-35A-org-wide-id-system-confirmation.md` | True collision victim: BC-35 is taken by the entity-system slice (its index row + CHANGELOG entry). Suffix renumbering per the BC-01A precedent. Heading self-ID updated; renumbering note appended. |

All references to the two old filenames are updated in the same PR (including the correction table inside landed CR-DEA-BC-37 §2 — recorded there as a BC-39 correction, per the no-silent-rewrite rule). The index Numbering section gains both renumbering records.

## 3. Broken-href manifest (23 fixes; targets verified to exist)

| File | Count | Fix |
|---|---|---|
| `CHANGELOG.md` | 2 | `(VERSIONING.md)` → `(docs/VERSIONING.md)`; `(release-cut-procedure.md)` → `(docs/release-cut-procedure.md)` |
| `README.md` | 1 | `docs/research/BC-02-CLOSEOUT.md` → `catalog-research/BC-02-CLOSEOUT.md` (moved by CR-CATALOG-STRUCT-03b) |
| `change-requests/CR-DEA-BC-18-track-a-orgdesign-evidence.md` | 4 | `../../METHODOLOGY.md` → `../METHODOLOGY.md`; `../../EVIDENCE.md` → `../EVIDENCE.md`; `../../catalog-research/INV-ORGDESIGN-v0.2.md` → `../catalog-research/INV-ORGDESIGN-v0.2.md`; `../../catalog-research/INV-ORGDESIGN-v0.1.yaml` → `../catalog-research/INV-ORGDESIGN-v0.1.yaml` |
| `change-requests/CR-DEA-BC-17.md` | 1 | pre-mv1 entity path → `../entities/v1-alpha/technology-management-maus5n/capabilities-capability-technology-management-maus5n.yaml` (via `reconciliation/migration-id-map.yaml`) |
| `docs/REVIEWS.md` | 3 | `../../change-requests/CR-DEA-BC-{18,14,19}-*.md` → `../change-requests/…` |
| `docs/publication-pipeline.md` | 3 | `../../change-requests/CR-DEA-BC-{06,10,05}.md` → `../change-requests/…` |
| `catalog-research/VISUALS-v0.1.md` | 9 | `visuals/v0*.svg` → `../visuals/v0*.svg` (moved by CR-CATALOG-STRUCT-03b) |

## 4. Index backfill and status metadata

1. Add index rows (Title / Status / Landed / Notes) for the fifteen missing CRs listed in §1.1, sourced from each CR's own metadata, the CHANGELOG entries, and the landing PRs (#67–#85, #88, #89). The BC-35 entity-system row's status becomes "Landed (PR #86)". The BC-05 row regains its leading `|`.
2. **Status-truth backfill across the whole series**, as recorded corrections (evidence rule: a CR is `Landed` iff git history shows its landing PR; every backfill cites its PR). Twelve files changed: bold-line Proposed → Landed (BC-14 PR #71, BC-17 PR #67, BC-19 PR #72, BC-mv1 PR #73); table Proposed/Draft → Landed (BC-01A, BC-03, BC-04, BC-35-entity PR #86); no-status/malformed-status → bold Landed/Superseded (BC-01 PR #13, BC-02 unbolded Proposed → Landed PR #4, BC-06 frontmatter-only → bold Superseded PR #42, BC-18 PR #68). Eight further files had their withdrawal pointers retargeted BC-34 → BC-36 (BC-05/07/08/09/12/13/14/17). The index rows for BC-14/17/18/19/mv1 flip from "Proposed (PR pending)" to their true landed state. `open_change_requests` steps 12 → **0** at this CR's landing (regenerate `CATALOG.yaml` in the same PR): the truthful state — nothing in the series is open once the three remediation carriers land.
3. Add this CR's own row per GOVERNANCE §2.3, and mark BC-37/BC-38's rows Landed (they merge ahead of this stacked PR).

## 5. Documentation truth

- **README**: fix the header typo ("inttent" → "intent"); rewrite "Repository Structure" to the actual current tree (29 canonical entries under `entities/v1-alpha/<slug>-<hash>/`, plus `catalog-research/`, `visuals/`, `mappings/`, `classifications/`, `contributions/`, `reconciliation/`, `submittal-reviews/`, `schemas/fixtures/`, `tests/`, `tools/`, and the seven workflows); align the Status paragraph and the Entity-Definition "Catalog Version" row with the post-reset posture declared by `docs/VERSIONING.md` + `CHANGELOG.md` (BC-36 reset: tags v1-alpha.0..v1-alpha.8 withdrawn; current baseline per VERSIONING §"v1-alpha.0: initial v1-alpha baseline (the current state)" with 29 canonical entries). Retire the pre-reset version/tag claims ("current: v1-alpha.4, tag `570830a`", "v1-alpha.5 in CR-DEA-BC-12").
- **GOVERNANCE §1**: "(v1-alpha.0, 26 canonical entries)" → the post-reset posture (29 canonical entries; tags withdrawn pending the first post-reset cut per `docs/release-cut-procedure.md`). **§2.4**: replace the stale parked-successors list (BC-03/BC-04 landed 2026-09-01) with the current park order (BC-38 parks behind BC-37; BC-39 follows).
- **`dependencies.yaml`**: the `ref: v1-alpha.4` pin targets a withdrawn tag. Drop the `ref:` line (Tier-3 pin is optional per the file's own schema) with a comment: "tag pin re-added at the first post-reset release cut (docs/release-cut-procedure.md)". Keep `version: v1-alpha`.
- **`docs/governance/cardinal-rules.md:19`**: `processes-*.yaml` → `capabilities-*.yaml` (processes-repo copy-paste; this repo's records are `capabilities-*.yaml` per `validate-entries.yml` and CR-CATALOG-STRUCT-01 §5).

## 6. Recurrence gates (new)

1. **`scripts/check_doc_links.py`** — validates every relative href in every `*.md` resolves to an existing path (the review's checker, productized: markdown-link regex, skip `#`/`http`/`mailto`, URL-decode, repo-root relative). Blocking, wired into `validate-entries.yml` (named step, DL-001), with `--self-test` fixtures. Zero findings at landing (§3 makes this true).
2. **`scripts/check_cr_index.py`** (rules CR-001..005) — bidirectional index discipline over `change-requests/README.md`: CR-001 every `CR-*.md` file has an index row linking it; CR-002 every row href resolves; CR-003 row id matches the target file's self-identified heading id; CR-004 table rows must start with `|`; CR-005 unlinked rows must carry the documented-gap marker "No standalone CR file" (the BC-20 case). Blocking, wired into `validate-entries.yml` with `--self-test` fixtures. Zero findings at landing (§4 makes this true).

Both gates get `--strict` parity and a short self-test each, added to `tests/` and the full-suite step from CR-DEA-BC-38 §3.

## 7. NOT-List

- NOT renumbering anything else; gaps (11, 15, 16, 24) remain as history.
- NOT rewriting landed-CR bodies beyond: the two §2 renumbering notes, the four §4.2 status lines, and the BC-37 §2 filename-reference update — each is a recorded correction in a landing PR, per GOVERNANCE §2.2/§2.1.
- NOT a catalog-content change: no entity, candidate, schema, mapping, view, or research-register content changes.
- NOT re-cutting releases or creating tags (the first post-reset tag is governed by `docs/release-cut-procedure.md` and is out of scope).
- NOT the CI dependency-pinning/timeout backlog (recorded below, deferred deliberately).

## 8. Deferred backlog (recorded, no carrier)

Pin pip dependencies and Python versions per workflow; add `timeout-minutes` to all jobs; consider SHA-pinning the two `dsanders11/json-schema-validate-action` steps. Same class as the processes repo's CI-hygiene findings; folded out of BC-37/38/39 to keep carriers reviewable.

## 9. Acceptance criteria

1. The §3 checker (as productized in §6.1) reports 0 broken relative hrefs repo-wide; run `python scripts/check_doc_links.py` → exit 0.
2. `python scripts/check_cr_index.py` → exit 0: 45 CR files all linked by index rows (42 legacy + BC-37/38/39), zero unresolved hrefs, zero malformed rows, zero unmarked gap rows (BC-20's row carries the gap marker).
3. The two old filenames from §2 no longer exist; `git log --follow` shows the renames; the CHANGELOG's BC-36 href resolves.
4. README/GOVERNANCE/`dependencies.yaml` contain no pre-reset version claims: `grep -rn "v1-alpha\.[1-8]" README.md GOVERNANCE.md dependencies.md dependencies.yaml` returns only historical/fossilized contexts (`docs/release-history-archive.md`, CHANGELOG history), none asserting current posture.
5. `cardinal-rules.md` contains no `processes-*` glob.
6. `open_change_requests` in the regenerated `CATALOG.yaml` equals **0** (the full §4.2 status-truth pass plus the three Accepted carriers), and `regenerate_catalog.py --check` exits 0.
7. All gates from CR-DEA-BC-37 §6 and CR-DEA-BC-38 §6 still pass (no regression from the renames/edits); CI green on the PR and on `main` post-merge.

## 10. Verification at landing

PR body records: rename log (`git log --follow --name-status`), the before/after outputs of both new gates, the recomputed open-count manifest, and live CI URLs.
