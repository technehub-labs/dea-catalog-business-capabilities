# CR-DEA-BC-68: Candidate-Register Reconciliation

| Field | Value |
|---|---|
| **CR** | CR-DEA-BC-68 |
| **Title** | Candidate-register reconciliation: the three investigation records carry their closure verdicts |
| **Status** | Landed |
| **Series** | CR-DEA-BC |
| **Change layer** | Research-record status truth (no admissions, no retirements) |
| **Target repository** | `technehub-labs/dea-catalog-business-capabilities` |
| **Target branch** | main |
| **Dependencies** | CR-DEA-BC-61 (index truth); CR-DEA-BC-62 (the coverage-gap register whose relation to Track C is recorded here) |
| **Primary deliverable** | The three candidate records' statuses reflect their actual closure verdicts |
| **Decision authority** | Catalog governance (repository owner) |
| **Owner** | Emmanuel A. Otchere |
| **Date** | 2026-10-31 |
| **Trigger** | Owner direction: address the three research candidates for coverage clarity. Investigation found all three CR-DEA-BC-13 tracks closed long ago, while the records still read `status: candidate-not-canonical` — the candidate state in the index is a preservation artifact (BC-09 §8), not an open investigation. |

## 1. The dispositions (evidence-first)

| Candidate | Track | Verdict (evidence) | Status now |
|---|---|---|---|
| `candidate-epm-5fxren` | B | **Admitted**: hypothesis confirmed at E3; `capabilities:capability-enterprise-performance-management-5fxren` canonical under CR-DEA-BC-23 (2026-10-12; the then-29th canonical; direction loop closed per BC-SR-A001 §16). The canonical record's provenance cites this path as the preserved prior artifact (BC-09 §8). | `closed-admitted` |
| `candidate-orgdesign-a7s8bf` | A | **Admitted**: `capabilities:capability-organizational-design-vanefq` canonical under CR-DEA-BC-14 (CAND-036; E3; evidence trail INV-ORGDESIGN + SRC-017/018/019). | `closed-admitted` |
| `candidate-relmgmt-nu73v9` | C | **Not admitted, by explicit verdict**: evidence-register Track C records "opt 2 (abstract grouping only); no separate first-order Relationship Management capability" — the role-level capabilities (Customer, Supplier, Partner Management) are the first-order set. The coverage-gap register (CR-DEA-BC-62) deliberately operated at role level and did not reopen this question. | `closed-not-admitted` |

Each record gains `status`, `disposition` (with the closing evidence), `disposition_cr: CR-DEA-BC-68`, and `disposition_date`. The records stay at their original paths: the canonical EPM's provenance cites the epm preservation path, and the investigation trails are part of the catalog's research history.

## 2. Coverage clarity statement

After this CR, the candidate register carries **zero open investigations**: every CR-DEA-BC-13 track is closed (two by admission, one by explicit non-admission verdict), and the coverage-gap programme (CR-DEA-BC-62..66) admitted all eleven of its candidates. The three candidate-state subtrees in the index are **closed investigations preserved by design** (BC-09 §8) — the index's `candidates: 3` counts preservation, not pending work. No first-order coverage question is open in this catalog.

## 3. Scope

In scope: the three candidate records' status/disposition fields; this CR; register row; CHANGELOG.

Out of scope: moving any record (preservation paths are cited by canonical provenance); the regenerator's state inference (directory-based by design); any new admission; C-12 (its specialization decision stands).

## 4. Acceptance criteria

1. All three records carry truthful status + disposition.
2. Gates green; index regenerated (counts unchanged: 40 canonical / 3 candidate-preserved / 0 retired).
3. The coverage question is documented as fully closed.

## 5. NOT-list

1. No records move, no admissions, no retirements.
2. No schema or gate changes.
3. The Track C verdict is not relitigated (it is cited, not re-decided).
