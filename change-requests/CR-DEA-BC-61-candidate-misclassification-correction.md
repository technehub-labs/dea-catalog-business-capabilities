# CR-DEA-BC-61: Candidate Misclassification Correction (Regenerator infer_state)

| Field | Value |
|---|---|
| **CR** | CR-DEA-BC-61 |
| **Title** | Candidate misclassification correction: index truth restored (29 canonical records re-classified) |
| **Status** | Landed |
| **Series** | CR-DEA-BC |
| **Change layer** | Toolchain correction + index regeneration (no record content change) |
| **Target repository** | `technehub-labs/dea-catalog-business-capabilities` |
| **Target branch** | main |
| **Dependencies** | dea-metaframework infer_state fix (PR #58, CR-CATALOG-STRUCT-06a amendment) |
| **Primary deliverable** | Regenerated `CATALOG.yaml` with truthful state classification: 29 canonical / 3 candidates |
| **Decision authority** | Catalog governance (repository owner) |
| **Owner** | Emmanuel A. Otchere |
| **Date** | 2026-11-02 |
| **Trigger** | The catalog advancement programme's closure audit questioned the 0-canonical/32-candidate posture. Investigation found the vendored regenerator's `infer_state` canonical-file lookup checked only the colon-form filename, while the mv1 id migration (CR-DEA-BC-mv1) renamed every record file to the normalized hyphen form. Every lookup missed, precedence fell through to the candidates/ rule (all subtrees carry a template `.gitkeep` there), and 29 canonical records were counted as candidates since the migration. CI stayed green throughout because `--check` deterministically reproduces the same misclassification. |

## 1. Change objective

Restore index truth: records at their subtree roots with `lifecycle_status: active` classify canonical again; the index paths point at the real record files instead of `candidates/.gitkeep`. No record content changes; no admission or retirement semantics change.

## 2. What this corrects

- The committed index (and every regeneration since the mv1 migration) recorded all 29 populated records as `state: candidate` with `path: entities/v1-alpha/<subtree>/candidates/.gitkeep`.
- Downstream misreadings caused by the same counts: metamodel CR-MET-014 recorded `dea:BusinessCapability` lifecycle `scaffold` (corrected separately, metamodel PR following this CR); the governance portfolio register v4 recorded the repo as skeleton (corrected to populated in register v5); the enrichment closure report's "0/29 populated realization" posture remains unaffected (that recorded relationship arrays, not index state).
- RRR-2026-01's Ready verdict described record content, which was never in doubt; the index now agrees with it.

## 3. The three candidates that remain candidates

The three candidate-only subtrees (`enterprise-performance-management-5fxren`, `orgdesign-a7s8bf`, `relmgmt-nu73v9`) correctly remain `state: candidate`: they carry records only under `candidates/` with no root canonical file. Their promotion is unchanged research-process work.

## 4. Named follow-up (not fixed here)

`CR-DEA-BC-06` carries its status in YAML frontmatter (`status: superseded`) — a third metadata shape the regenerator's status-token parser (bold-line and table forms) cannot see, so it is conservatively counted open (`open_change_requests: 1`). The record is genuinely superseded. Extending the parser to frontmatter is a metaframework-side follow-up; this CR does not alter the landed CR.

## 5. Scope

In scope: `scripts/regenerate_catalog.py` re-vendored from dea-metaframework (infer_state fix); regenerated `CATALOG.yaml`; this CR; `change-requests/README.md` row; `CHANGELOG.md` entry.

Out of scope: record content; the three candidates' promotion; release cutting (RRR-2026-01 process governs); the frontmatter parser extension; any downstream catalog.

## 6. Acceptance criteria

1. `regenerate_catalog.py --check` exits 0 (index current).
2. Counts: canonical 29, candidates 3, entities 32, retired 0.
3. Every canonical entry's `path` ends in the record's real filename (no `.gitkeep` paths for canonical states).
4. Record files untouched (`git diff` shows only the index, regenerator, and CR/register/CHANGELOG files).

## 7. NOT-list

1. No records are admitted, promoted, retired, or edited.
2. No gate scripts other than the re-vendored regenerator change.
3. No release is cut.
4. Landed CRs' recorded history is not rewritten (this CR records the correction; the misclassification era stands as history).
