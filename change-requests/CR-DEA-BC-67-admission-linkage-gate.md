# CR-DEA-BC-67: CR-006 Admission-Linkage Gate

| Field | Value |
|---|---|
| **CR** | CR-DEA-BC-67 |
| **Title** | CR-006 admission-linkage gate: no canonical record lands without its CR document |
| **Status** | Landed |
| **Series** | CR-DEA-BC |
| **Change layer** | Conformance gate (tooling) + incidental tooling correction |
| **Target repository** | `technehub-labs/dea-catalog-business-capabilities` |
| **Target branch** | main |
| **Dependencies** | CR-DEA-BC-66 §3 (the process correction this gate makes unrepeatable); IDM-008 (the PR-scoped gate precedent it mirrors) |
| **Primary deliverable** | `check_cr_index.py` CR-006 + `--base-ref` PR mode; workflow step; git-fixture test suite |
| **Decision authority** | Catalog governance (repository owner) |
| **Owner** | Emmanuel A. Otchere |
| **Date** | 2026-10-31 |
| **Trigger** | The T1-T3 admissions (PRs #117/#118/#119) landed eleven canonical records without CR documents; the retrospective CR files were carried by CR-DEA-BC-66. The CR-index gate (CR-001..005) validates CR-files-to-rows but nothing required a CR file to exist for new records - the gap is structural, so the fix is structural. |

## 1. Change objective

Make the admission-without-CR landing shape fail CI in the PR that creates it, using the same PR-scoped mechanism the id-system gate pioneered.

## 2. The gate

`check_cr_index.py` gains `CR-006` and a `--base-ref` PR mode (mirroring `check_id_system.py` IDM-008's diff acquisition and report-artifact pattern):

- Changed-file acquisition: `git diff --name-only base...HEAD` (two-dot fallback; graceful empty on non-git contexts).
- "New canonical record" = an **added** file matching the IDM-008 filter (`entities/v1-alpha/<subtree>/<namespace>-*.yaml`, four path parts) — state dirs, views, CATALOG.yaml, and schemas are excluded by construction. The record id is read from the file's own `id:` field.
- Fires (blocking) when a new canonical record's id is not referenced by any **added or changed** `change-requests/CR-*.md` in the same diff.
- The repo-wide `evaluate(root)` CR-001..005 sweep is unchanged; CR-006 lives only in PR mode.
- Workflow step in `catalog-conformance.yml` beside the IDM-008 step, with its own report artifact.

## 3. Incidental tooling correction (scoped here)

`scripts/migrate_ecf_conformance.py` DOMAIN_MAP: `'enablement-operations': 'operationsEnablement'` → `'enablementAndOperations'` — the map predated CR-ECF-012's identifier finalization and carried the deprecated form. No data changes (capabilities entities are clean per the CR-MET-018 census).

## 4. Tests

`tests/test_check_cr_index.py` extends with the org's first two-commit git fixture (init → base commit → branch → PR commit), covering: CR-006 fires for an uncovered record (asserting the id in the diagnostic); passes when a CR file references the id; ignores non-record changes; ignores state-dir files; and the CLI `--base-ref` mode end-to-end via a copied gate script. 12/12.

## 5. Acceptance criteria

1. Both gate modes green locally; the fixture suite green.
2. Workflow step present beside IDM-008 with report artifact.
3. CR-index discipline still CONFORMANT (CR-001..005 unchanged).

## 6. NOT-list

1. No catalog data changes.
2. No promotion of the gate to other catalogs in this CR (the check_id_system vendoring path is the named propagation route).
3. No change to CR-001..005 semantics.
