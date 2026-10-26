# CR-DEA-BC-34: Release-History Reset (Path B) + Release-Discipline Extensions

**Status**: Applied (2026-10-13)
**Layer**: Cross-cutting (catalog governance) + release discipline
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-13
**Trigger**: User directive 2026-10-13, eaojnr: "Refer to CR-BP-116 release-history reset; and let adopt same reset rationale for the business capability releases. In addition, i'd like to confirm if the ID system for business capabilities can leverage the orgwide id system implemented. As a rule, seed these as cards to work on and then let's review the plan of work." User ratified 2026-10-13: "proceed the sequence A to F" (the A+B+D+F extension set from CR-BP-116's candidate list).
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-34-release-history-reset`. Recovery appendix (§2) is captured into this CR file before any destructive operation runs. PR review (not direct-push) per CR-BP-116 pattern.

## 1. Scope

The minimal Path B is the release-history reset (withdraw v1-alpha.0 .. v1-alpha.8 tags; rewrite CHANGELOG and docs/VERSIONING.md release-history surface; relabel abandoned-cut carriers). This CR extends that with the four release-discipline hardenings (A + B + D + F) from the CR-BP-116 candidate list:

- **A — Pre-release CI verification contract**: the proposed tag SHA must carry a fresh CI run with all 3 workflows SUCCESS on the exact SHA, verified before `git tag -s`. Catches the v0.1.0 / v0.3.0-class race where web edits land after the carrier PR merges and the tag ends up pointing at a SHA the catalog was regenerated against a different version of.
- **B — Prior-cut history table**: `docs/VERSIONING.md` gains a numbered, append-only table that records the date, cut CR, commit SHA, gate count, and post-mortem link for every release tag ever cut. Starts empty post-reset. New row per future cut.
- **D — GPG-signing procedure**: the release-cut step names the active key fingerprint (`B2FD3524B35CBDD34251ABE07969C942DB14B2F2`, per the secure-notes procedure note) and requires `git tag -v vN.M.P` verification immediately after signing. Verification status is added to the release manifest.
- **F — Doc split**: the release-cut procedure moves from `docs/VERSIONING.md` into a new `docs/release-cut-procedure.md`; the pre-release history (now-removed) section is moved to `docs/release-history-archive.md` as a fossilised record. `docs/VERSIONING.md` keeps the rules + version-trigger table + prior-cut history table from B.

A cross-repo dependency sweep (§3) and a sister-repo coordination note in the `dea-catalog-release-cut` skill (§11) are also in scope. C (pre-cut admission discipline) and G (tag-signing commit message template) are explicitly deferred to their own CRs (matching the CR-BP-116 deferral pattern).

**Out of scope (deferred)**:
- CITATION.cff reset: no CITATION.cff exists in this repo (CR-BP-116 had one). The next real release cut will create CITATION.cff.
- The CR-DEA-BC-35 org-wide id-system confirmation work: that is its own CR; it does not depend on the release-history reset.

## 2. Recovery appendix (captured BEFORE any destructive operation)

This appendix is the audit trail for what is being withdrawn. Captured into this CR file as the first concrete step on the feature branch, before any tag deletion runs. If the reset is wrong, the appendix is the recovery path.

### 2.1 v1-alpha.0 (cut 2026-09-02; tag SHA + summary)

- **Tag**: `v1-alpha.0` (annotated)
- **Tag SHA**: `4be5d7e16fcf113c0cec9e0cb18718a320fc1293` (lightweight; dereferences to merge commit `4be5d7e`)
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-02 11:15:23 +0800
- **Body (excerpt)**: "Initial v1-alpha baseline (CR-DEA-BC-05). 26 canonical first-order capabilities admitted, 1 specialization view (view-telecom-mcsp), conformance gate enforced on every PR (CG-001..006). Admitted entries (26): Strategy, Strategic Planning, Enterprise Governance, Customer Management, Supplier Management, Partner Management, Offering Management, Marketing, Operations, Financial Stewardship, Financial Management, People/Workforce Management, Workforce Planning, Information Management, Risk Management, Compliance Management, Legal Management, Security Management, Sourcing and Procurement, Asset Management, Facility Management, Change Management, Technology Management (held-unmapped), Resilience Management, Innovation Management, Analytics and Intelligence. ECF contract pin: dea:ecf@1.0.0; Metamodel pin: 1.0.0."
- **Carrier CR**: `change-requests/CR-DEA-BC-05.md` (release-cut procedure; pre-mv1 id system)
- **Recovery**: The tag will be deleted by this CR. The full tag body is preserved in the deletion log at `docs/release-history-archive.md` §v1-alpha.0.

### 2.2 v1-alpha.1 (cut 2026-09-07; tag SHA + summary)

- **Tag**: `v1-alpha.1` (annotated)
- **Tag SHA**: `fc07ba7665f94d39d6b47e557e21c0175bab74c0`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-07 23:05:59 +0800
- **Body (excerpt)**: "Substrate-neutral re-statement of workforce capabilities. Catalog version v1-alpha.0 -> v1-alpha.1 (minor, VERSIONING.md section 2.2). Reconciles catalog content with dea-metaframework v2.4.0 (Agency & Organization; ADR-ECF-002 section 5 Substrate Independence Stress Test; CR-ECF-007). Names, business objects, ECF coordinates, aliases, and pins unchanged (N-001 stands): dea:capability-workforce-management and dea:capability-workforce-planning now define the workforce as human and artificial agents. Both entries bump 1.0.0 -> 1.1.0. Includes: CR-DEA-BC-07 substrate-neutral re-statement (PR #48); visual domain-label conformance guard (PR #50); publication pipeline fix: nested entities + escaped display text (PR #51)."
- **Carrier CR**: `change-requests/CR-DEA-BC-07.md`
- **Recovery**: The tag will be deleted by this CR. Full body preserved at `docs/release-history-archive.md` §v1-alpha.1.

### 2.3 v1-alpha.2 (cut 2026-09-08; tag SHA + summary)

- **Tag**: `v1-alpha.2` (annotated)
- **Tag SHA**: `e22840d374f33ef3113c53d1429b1d0f19c92dd0`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-08 10:04:49 +0800
- **Subject line**: "v1-alpha.2 (CR-DEA-BC-08, PR #53): Technology Management coordinated at strategy-direction x build; N-006 superseded by N-006R; 0 held-unmapped; 16 distinct primary coordinates"
- **Body (excerpt)**: The full tag body is empty beyond the subject line. The substance is in `change-requests/CR-DEA-BC-08.md` and CHANGELOG.md §[v1-alpha.2].
- **Carrier CR**: `change-requests/CR-DEA-BC-08.md`
- **Recovery**: The tag will be deleted by this CR. Subject line preserved at `docs/release-history-archive.md` §v1-alpha.2.

### 2.4 v1-alpha.3 (cut 2026-09-08; tag SHA + summary)

- **Tag**: `v1-alpha.3` (annotated)
- **Tag SHA**: `04945946ff85a66c29c5bda4ba4a762762e6964e`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-08 17:50:02 +0800
- **Subject line**: "v1-alpha.3 (CR-DEA-BC-09, PR #54): naming conformance refresh; 5 renames (N-010..N-014); Security retained (N-015); TAXONOMY section 1 rule 2 clarified + section 1A definition template; check_naming.py wired into entry CI"
- **Body**: empty beyond subject line. Substance in `change-requests/CR-DEA-BC-09.md`.
- **Carrier CR**: `change-requests/CR-DEA-BC-09.md`
- **Recovery**: Tag will be deleted; subject line preserved at `docs/release-history-archive.md` §v1-alpha.3.

### 2.5 v1-alpha.4 (cut 2026-09-09; tag SHA + summary)

- **Tag**: `v1-alpha.4` (annotated)
- **Tag SHA**: `ead021de0ef1558482a7769162d2b431a9de0a7a`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-09 21:58:57 +0800
- **Body (excerpt)**: "v1-alpha.4 (CR-DEA-BC-11, PR #62): release-pipeline consolidation on the framework Python. Patch (CR-DEA-BC-11, PR #62). Release-pipeline consolidation: the first-generation Node-based publication pipeline (CR-DEA-BC-06 + CR-DEA-BC-10) is superseded by the framework Python scripts/generate_capability_map.py, which natively emits the L0 ⊃ L1 ⊃ L2 capability × ECF map (HTML + A3 landscape PNG) via weasyprint + pdftoppm. No Node, no Chrome, no playwright, no sharp. The release zip shrinks from 12 files to 2 (capability-map.html + capability-map-a3.png). Consumer-facing migration: any consumer pinned to retired artifacts (poster.svg/png, map.svg/png, catalog.svg/png, catalog.csv, catalog.json, overlay.yaml/json, dependencies.yaml, MANIFEST.md) must migrate. See docs/publication-pipeline.md § 'Migration from the BC-06 / BC-10 pipeline' for the full replacement table."
- **Carrier CR**: `change-requests/CR-DEA-BC-11.md` (note: file is `CR-DEA-BC-11-chore-cut-v140-release.md`; see §9)
- **Recovery**: Tag will be deleted; full body preserved at `docs/release-history-archive.md` §v1-alpha.4.

### 2.6 v1-alpha.5 (cut 2026-09-10; tag SHA + summary)

- **Tag**: `v1-alpha.5` (annotated)
- **Tag SHA**: `246e010a3765309d22269daee6484e091cfd3054`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-10 06:35:51 +0800
- **Body (excerpt)**: "Carrier: CR-DEA-BC-12 (PR #65). Six high-confidence ECF coordinate re-mappings per BC-SR-A001 §8.A, §9, §10, §11, §13 (Strategy, Strategic Planning, Asset, Facility, Supplier, Sourcing & Procurement). Each affected entry advances 1.0.0 -> 1.1.0. Identity unchanged. Three evidence-led investigation tracks opened (no admission in this release): Track A: Organizational Design (BC-SR-A001 §4 P1); Track B: Enterprise Performance Management (BC-SR-A001 §5 P1); Track C: Relationship Management generic parent (BC-SR-A001 §6 P1-P2)."
- **Carrier CR**: `change-requests/CR-DEA-BC-12.md`
- **Recovery**: Tag will be deleted; full body preserved at `docs/release-history-archive.md` §v1-alpha.5.

### 2.7 v1-alpha.6 (cut 2026-09-10; tag SHA + summary)

- **Tag**: `v1-alpha.6` (annotated)
- **Tag SHA**: `0c943b2bc8a01b573a4a81328a98465e7073d19b`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-10 07:43:50 +0800
- **Body (excerpt)**: "Carrier: CR-DEA-BC-13 (PR #66). Method-CR codifying BC-SR-A001 §14's ECF primary-coordinate rule refinement. Replaces the pre-CR-13 'earliest initiation point' rule with 'semantic center of gravity' in METHODOLOGY.md §8, and re-evaluates all 26 canonical entries under the new rule. Six entries changed: asset-management, facility-management, sourcing-and-procurement, supplier-management: primary moves to operate; partner-management: secondary fix; technology-management: carve-text only (Tech-as-Estate vs Tech-as-Enabler formalized per BC-SR-A001 §12). Per-entity versions: asset/facility/sourcing/supplier/technology 1.1.0 -> 1.2.0; partner 1.0.0 -> 1.1.0; others unchanged."
- **Carrier CR**: `change-requests/CR-DEA-BC-13.md`
- **Recovery**: Tag will be deleted; full body preserved at `docs/release-history-archive.md` §v1-alpha.6.

### 2.8 v1-alpha.7 (cut 2026-09-10; tag SHA + summary)

- **Tag**: `v1-alpha.7` (annotated)
- **Tag SHA**: `1a6bc6ba7a9a399de21e1548253920fe55699123`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-10 16:31:21 +0800
- **Body (excerpt)**: "Carrier: CR-DEA-BC-17 (PR #67). Admission-CR closing BC-SR-A001 §12. Admits dea:capability-technology-enablement as the 27th first-order canonical capability at enablement-operations/operate (primary), with enablement-operations/{build, improve} as secondaries. New entry: dea:capability-technology-enablement v1.0.0 (Tech delivery function). Tech Mgmt: 1.2.0 -> 1.3.0 (Minor; boundary-text + related_capabilities). Operations: 1.0.0 -> 1.0.1 (Patch; cross-reference patch). Info Mgmt: 1.0.0 -> 1.0.1 (Patch). The carve BC-SR-A001 §12 asked us to make explicit is now a peer relationship between two first-order capabilities rather than as a deferred specialization."
- **Carrier CR**: `change-requests/CR-DEA-BC-17.md`
- **Recovery**: Tag will be deleted; full body preserved at `docs/release-history-archive.md` §v1-alpha.7.

### 2.9 v1-alpha.8 (cut 2026-09-11; tag SHA + summary)

- **Tag**: `v1-alpha.8` (annotated)
- **Tag SHA**: `7140cf8809e62913cecc858c29b85dcb8aaf6196`
- **Tagger**: Emmanuel A. Otchere <emmanuel@otchere.com> 2026-09-11 01:43:50 +0800
- **Body (excerpt)**: "CR-DEA-BC-14 (PR #71): Admit Organizational Design as the 28th first-order canonical capability at agency-organization/design (primary) + agency-organization/{conceive, build} (secondaries). Closes BC-SR-A001 §4 (reviewer P1), BC-13 §B.1 (Track A investigation opened), TER-ORGDESIGN-001 (open -> closed), CAND-036 (E3 -> E4 per EVIDENCE.md §3 admission promotion rule). Catalog: 27 -> 28 first-order canonical capabilities. agency-organization/design cell-occupancy 3 -> 4. 8 existing entries updated (Patch-tier)."
- **Carrier CR**: `change-requests/CR-DEA-BC-14-track-a-orgdesign-admission.md`
- **Recovery**: Tag will be deleted; full body preserved at `docs/release-history-archive.md` §v1-alpha.8.

## 3. Pre-execution cross-repo dependency sweep

Before any tag deletion, verify no sibling repo in the org pins `dea-catalog-business-capabilities@v1-alpha.*`:

```bash
gh search code "dea-catalog-business-capabilities@v1-alpha" --owner technehub-labs
# Sibling repos to consider explicitly:
# - technehub-labs/dea-metaframework
# - technehub-labs/dea-architecture-framework
# - technehub-labs/dea-catalog-processes
# - technehub-labs/dea-catalog-business-objects
# - technehub-labs/dea-catalog-organizational-units
# - technehub-labs/dea-catalog-actors
# - technehub-labs/dea-catalog-business-services
# - technehub-labs/dea-catalog-stakeholders
```

**Sweep result (executed 2026-10-13)**: 0 hits across all 8 sibling repos (local-repo grep across `/home/hermes/dea-catalog-*`). The `gh search code` API timed out on this date; the local sweep is the verification path for this CR. The reset is safe to execute.

A self-reference to `dea-catalog-business-capabilities@main` (tag `v1-alpha.0`; merge commit `4be5d7e`) exists at `change-requests/CR-DEA-BC-06.md` line 243, but this is a historical pre-v0 reference to a now-stale source tag and does not constitute a downstream consumer pin.

## 4. CHANGELOG.md rewrites

Drop the following sections in this exact order:

- `## [v1-alpha.8] - 2026-09-11` (line 18-46)
- `## [v1-alpha.7] - 2026-09-10` (line 119-174)
- `## [v1-alpha.6] - 2026-09-10` (line 175-211)
- `## [v1-alpha.5] - 2026-09-10` (line 212-272)
- `## [v1-alpha.4] - 2026-09-09` (line 273-308)
- `## [v1-alpha.3] - 2026-09-08` (line 309-343)
- `## [v1-alpha.2] - 2026-09-08` (line 344-363)
- `## [v1-alpha.1] - 2026-09-07` (line 364-411)
- `## [v1-alpha.0] - 2026-09-02` (line 613-...)
- `## [v1-alpha.0-pipeline-live] - 2026-09-04` (line 582-...)
- `## [STRUCT-03a]` and `## [STRUCT-03b]` (lines 537-581 and 495-536)

Keep:

- The `## Unreleased` block (line 47-118), which carries the post-v1-alpha.8 record of work (BC-20/21/22/23/mv1/cleanup). This block becomes the only top-of-file entry.
- `## [v2.5.0-migration] - 2026-09-08`, `## [v2.4.0-migration] - 2026-09-07`, `## [v2.3.0-migration] - 2026-09-07` (pre-v1-alpha.0 ECF migration prose; describes how the repo responded to upstream vocabulary changes; not release-layer).

Result: a CHANGELOG that opens with `[Unreleased]` (now headlined) and has only pre-v1-alpha.0 ECF migration prose beneath. The next release cut moves `[Unreleased]` to `[v0.x.y] - YYYY-MM-DD` and adds a fresh empty `[Unreleased]` block on top.

## 5. docs/VERSIONING.md rewrites (release-history side)

Replace the existing version-trigger prose and any pre-release history section with:

- **Release history** section (empty) + prior-cut history table (empty)
- Pointer to `docs/release-cut-procedure.md` for the full procedure
- Version-trigger table retained
- The release-history side moves the prior-cut history into `docs/release-history-archive.md` as a fossilised record.

## 6. docs/release-cut-procedure.md (new, from F)

The full release-cut procedure, including the extensions A + D:

1. Decide a target version per the version-trigger table in `docs/VERSIONING.md`. Document the rationale in `change-requests/CR-DEA-BC-NNN.md` (the carrier CR).
2. The carrier PR adds a `release-notes/vN.M.P.md` file with: trigger CR reference, the 7-gate posture (blocking + advisory CONFORMANT counts), the proposed tag SHA, and a one-paragraph user-facing summary of the release.
3. **Pre-release CI verification contract (A)**: the proposed tag SHA is `git rev-parse origin/main` captured at the moment of tagging. A fresh CI run on that exact SHA (the carrier PR's push) must complete with all 3 workflows (`validate`, `ecf-conformance-consumer`, `id-system-coherence`) SUCCESS. If any workflow is red, fix it before tagging; do not tag a red-SHA release.
4. `python3 scripts/check_naming.py` exit 0.
5. `python3 scripts/check_versions.py` exit 0.
6. `python3 scripts/check_ecf_conformance.py` exit 0.
7. `python3 scripts/check_view_refs.py` exit 0.
8. `python3 scripts/check_visual_domain_labels.py` exit 0.
9. `python3 scripts/check_catalog_index.py` exit 0.
10. `python3 scripts/check_id_system.py` exit 0 (IDM-001..007 CONFORMANT).
11. **GPG-signing procedure (D)**: `gpg --list-secret-keys --keyid-format LONG` shows the active key fingerprint `B2FD3524B35CBDD34251ABE07969C942DB14B2F2` (per `~/.hermes/profiles/coder/secure-notes/gpg-signing-setup.md`). `git tag -s vN.M.P -m "<commit-message-template>" <carrier-merge-sha>` immediately followed by `git tag -v vN.M.P` to verify the signature. The verification status is added to the release manifest in step 14.
12. `git push --tags` to `origin`.
13. `gh release create vN.M.P --repo technehub-labs/dea-catalog-business-capabilities --title "vN.M.P" --notes-file release-notes/vN.M.P.md` (if the first release is not a GitHub release, omit this step; record the rationale in the carrier CR).
14. Update the prior-cut history table in `docs/VERSIONING.md` (§8) with the new row.
15. Cross-repo coordination: any release that lands a `capabilities:*` id set change or moves the ECF version triggers the sweep in §3 of CR-DEA-BC-34 for the next cut cycle.

The carrier PR is merged only after step 10 verification. The tag is cut only after the carrier PR is on main.

## 7. docs/versioning.md prior-cut history table (B)

A new table, immediately below the version-trigger table:

```
| version | date | cut by CR | commit SHA | gates (blocking+advisory CONFORMANT) | post-mortem |
| ------- | ---- | --------- | ---------- | ------------------------------------ | ----------- |
```

Starts empty. Append one row per future cut when the release lands. The post-mortem column is optional; if a cut later gets a retrospective, link it. (The v1-alpha.x withdrawals of CR-DEA-BC-34 deliberately do not appear here — this table records *successful* cuts, not withdrawals; the recovery appendix in §2 is the audit record for those.)

## 8. docs/release-history-archive.md (new, from F)

Fossilised record of the 9 withdrawn v1-alpha.x cuts and the 3 abandoned pre-tag sections. The body is the tag-subject + tag-body + carrier CR for each withdrawn cut (reproduced from §2 above). The file is the audit record; the prior-cut history table (§7) is the active record.

## 9. Carrier CR relabel (release-cut rows + Status headers)

`change-requests/README.md` rows for CR-DEA-BC-05, -07, -08, -09, -11, -12, -13, -14, -17 get a `[WITHDRAWN 2026-10-13 — see CR-DEA-BC-34]` suffix in the title cell. The Status cell stays `**Merged**` (the PR did merge; the release it carried was later withdrawn — these are two different facts).

The carrier CR doc Status header on each of those nine files gets a one-line addendum:

```
**Status**: Merged (PR #N); release withdrawn 2026-10-13, see CR-DEA-BC-34.
```

Body text otherwise untouched. The body is the historical truth at the time of writing and rewriting it is silent history destruction.

## 10. CHANGELOG entry for CR-DEA-BC-34 + CATALOG.yaml posture

CHANGELOG `[Unreleased]` gains a CR-DEA-BC-34 entry summarizing the withdrawal + the discipline extensions. CATALOG.yaml regenerated to include CR-DEA-BC-34 in `open_change_requests` (N -> N+1). All other counts unchanged.

## 11. Cross-repo coordination note (E, light, from candidate list)

The `dea-catalog-release-cut` skill gains one new pitfall line: any release of `dea-catalog-business-capabilities` that lands a `capabilities:*` id set change or moves the ECF version triggers a sweep of sibling repos for downstream breaks; cf. CR-BP-116 §11 (the processes-repo equivalent). This makes the cross-repo concern a recurring check.

## 12. Conformance + Test Posture

- 7-gate rollup CONFORMANT (no gate-count change; CR-DEA-BC-34 touches CHANGELOG, docs, and the skill; the validator scripts are unchanged).
- `python3 scripts/check_naming.py` exit 0.
- `python3 scripts/check_versions.py` exit 0.
- `python3 scripts/check_ecf_conformance.py` exit 0.
- `python3 scripts/check_view_refs.py` exit 0.
- `python3 scripts/check_visual_domain_labels.py` exit 0.
- `python3 scripts/check_catalog_index.py` exit 0.
- `python3 scripts/check_id_system.py` exit 0.
- D-004 sweep on the new files: `docs/release-cut-procedure.md`, `docs/release-history-archive.md`, the CHANGELOG entry, the prior-cut history table. No `;;;`, no en/em-dashes in the new content.
- No new tests (this CR is documentation + tag/release layer; the existing test surface covers the validator side).

## 13. NOT-List

- No record-content changes. Entity records are untouched.
- No id changes. The repo's current `capabilities:*` id set is the source of truth for the first real cut.
- No gate-count changes. CR-DEA-BC-34 is doc + discipline + tag/release layer only.
- No cross-repo scope. Sibling repos are notified via the cross-repo coordination note (§11) but no sibling repo state is changed in this CR.
- No new release tag cut. The first real release is its own CR after this reset lands.
- C (pre-cut admission discipline) and G (tag-signing commit message template) deferred to their own CRs.
- CITATION.cff does not exist; no reset needed. The first real release cut will create CITATION.cff.
- CR-DEA-BC-35 (org-wide id system confirmation) is a separate CR; it does not depend on this CR.

## 14. Acceptance Criteria

- All v1-alpha.x release-layer state withdrawn per §1-§9; recovery appendix (§2) complete and committed.
- `git ls-remote origin --tags` shows no `v1-alpha.*` tags.
- `gh release list --repo technehub-labs/dea-catalog-business-capabilities` shows no `v1-alpha.*` releases.
- `docs/VERSIONING.md` has the new "Release history" section, the prior-cut history table (empty), and a pointer to `docs/release-cut-procedure.md`.
- `docs/release-cut-procedure.md` exists and contains the full procedure with steps A and D inlined.
- `docs/release-history-archive.md` exists and contains the fossilised record of the 9 withdrawn cuts.
- The nine carrier CRs (CR-DEA-BC-05/-07/-08/-09/-11/-12/-13/-14/-17) carry the withdrawal addendum on their Status header and the row title in `change-requests/README.md`.
- CHANGELOG.md has a single `[Unreleased]` at the top, no v1-alpha version sections, no STRUCT-03 sections, and the CR-DEA-BC-34 entry.
- `CATALOG.yaml` regenerated; `open_change_requests` reflects CR-DEA-BC-34.
- 7-gate rollup CONFORMANT; CI green on the merged PR.
- `dea-catalog-release-cut` skill has the cross-repo coordination pitfall line.

## 15. Result

The catalogue's release-layer goes from a state of nine pre-mature v1-alpha.x cuts and three abandoned pre-tag sections to a clean slate: no prior releases, the carrier CRs clearly relabelled as withdrawn, and a forward-discipline package (pre-release CI verification, prior-cut history table, GPG-signing procedure, doc split) that prevents the v1-alpha.x-class incidents from recurring. The first real release can stand on its own.
