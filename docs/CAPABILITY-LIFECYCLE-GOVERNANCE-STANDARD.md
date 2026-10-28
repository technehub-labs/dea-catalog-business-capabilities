# Capability Lifecycle Governance Standard

**Status**: Normative (CR-DEA-BC-49, 2026-10-28)
**Reconciles** (AC-01, inspected at landing): the schema `lifecycle_status` enum (upstream vocabulary: proposed / planned / active / deprecated / retired — `dea-metamodel` lifecycle.yaml) **and** the entity-system registry's 9-state admission ladder (candidate → observed → corroborated → normalized → ecf-mapped → reviewed → canonical → active → retired; `retired` terminal; ladder carried informationally in `provenance.ladder_passage`, ES-004 not enforced for BC by construction). Current population: all 29 records `active`.
**Introduces**: no new status values; no schema changes (AC-08/09).

---

## 1. The two-axis model

| Axis | Field | Meaning | Authority | Conformance |
|---|---|---|---|---|
| **Admission ladder** | `provenance.ladder_passage` (stages) | How the entity earned canonical status — history, append-only | EVIDENCE.md method; registry transition table | informational; audited per-CR (registry notes ES-004 exemption) |
| **Record status** | `lifecycle_status` | The entity's current governed state | upstream vocabulary (schema enum); changed only by CR | schema validation (enum); governance review |

The ladder is history; the status is state. A transition on one axis never silently rewrites the other: admission ends at `canonical`/`admitted` in the ladder while the record status is set at admission (all current records: `active`).

## 2. Record-status state model (`lifecycle_status`)

| State | Meaning | Entry conditions | Outgoing | Evidence & approval | References/views on entry |
|---|---|---|---|---|---|
| `proposed` | A first admission in progress (pre-canonical) | landing of the admission CR's entity record | `planned`, `active` (on admission), withdrawal (record removed with the CR rejected) | admission CR + evidence ladder through `reviewed` | not in views until canonical admission (views read canonical records only) |
| `planned` | Admitted, not yet exercised in any governed context | model decision | `active`, `deprecated` | CR | included in views (canonical) |
| `active` | Admitted and maintained (current population: 29/29) | admission CR | `deprecated`, `retired` | — | included |
| `deprecated` | Still canonical; flagged for future retirement/supersession; consumers should plan migration | deprecation CR stating the reason and successor path (if any) | `active` (reversal by CR), `retired` | deprecation CR; semantic review | included, marked; discovery views regenerated with the state visible |
| `retired` | Terminal: no longer canonical; preserved for traceability | retirement CR | — (terminal) | retirement CR; reference sweep (BC-48 rules + DL-001) proving resolution of inbound references or their recorded migration | excluded from discovery views' active set; retained in records/history; `retired` state subtrees follow the storage-layout conventions |

**Prohibited shortcuts** (no authority): `active` → `retired` without a deprecation step is not automatic, but a CR may combine deprecation+retirement **only** with an explicit supersession/retirement rationale and a reference sweep — the combination must be visible in the CR, not implied.

## 3. Admission-ladder transitions (registry table, restated)

candidate → observed → corroborated → normalized → ecf-mapped → reviewed → canonical (admission; post-mv1 admissions append `evidence-seeded`/`admitted` checkpoints per BC-40) → active (record-status pairing) → retired. Ladder entries are append-only provenance: stages are never rewritten; corrections land as new provenance or via CR-recorded corrections.

## 4. Supersession and retirement distinctions (§8 of the CR)

| Operation | Identity | Ladder/status effect | Traceability requirement |
|---|---|---|---|
| Correction (meaning retained) | unchanged | none (version bump) | CR + record change history |
| Revision (meaning changes, identity retained) | unchanged under versioning policy | status may stay `active` | semantic review; boundary/related re-checks (RI rules) |
| Split into distinct concepts | parent retired or deprecated; new entities admitted via full ladder | both axes affected | split CR maps old id → successor ids; migration map if ids change |
| Merge | merged-away entities retired; survivor revised | both axes | merge CR with equivalence rationale + reference migration |
| Supersession by another canonical entity | superseded → `deprecated` then `retired` | status axis | supersession CR; successor referenced in the retirement CR (no unauthorized replacement-relationship mechanism exists — R-1 pending) |
| Retirement without replacement | → `retired` (terminal) | status axis | retirement CR + inbound-reference sweep |

Retirement is not deletion: records, provenance, CRs, and history remain; only canonical standing ends (registry: `retired` terminal; storage layout keeps state subtrees).

## 5. Identity survival

An id is never silently reassigned to a different concept (registry identity block; migration map governs any id change; CR-35A). Reference-handling on any status change: run `check_relationship_integrity.py` (RI rules), `check_doc_conformance.py` (DCV-004/007), and the doc-links gate; regenerate discovery views (freshness gate enforces).

## 6. Conformance mapping

Schema enum (authoritative for values) · registry ladder (authoritative for admission history) · this standard (authoritative for transitions, evidence, and effects) · gates unchanged (no new gate in this CR; ES-004's BC exemption stands by construction). Any future state requiring schema support goes through a model CR (AC-09 recorded).
