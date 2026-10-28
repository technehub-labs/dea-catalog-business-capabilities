# Realization Reference Population Report

**Status**: Implementation record (CR-DEA-BC-57, 2026-10-28) · **Scheme authority**: BC-56 (PR #110) · **Outcome: zero population, documented deferral**

## 1. Evidence reconciliation (processes category — the only BC-56-supported target)

The mining basis was the processes catalog's own governed assertions: `relationships[].relationship_type: realizes` with `identity_scope: dea-catalog-business-capabilities` (upstream-owned contract). Inspection of `dea-catalog-business-processes` @ `5b95ae56` (3,598 process records):

| Evidence question | Finding |
|---|---|
| How many `realizes` assertions target this catalog? | **1** (an exemplar: `processes:process-pr-operate-bbe384` "Manage Customer Relationship") |
| Does its target resolve here? | **No** — target `dea:entity-capability:manage-customer-relationship` predates both catalogs' id migrations; no entry in `reconciliation/migration-id-map.yaml`; not a `capabilities:capability-*` id |
| Could it be mapped by name similarity? | Rejected — §3.2 forbids inferring realization from apparent relevance; mapping "manage-customer-relationship" ≈ Customer Management would be exactly that inference |
| Evidence basis for population at scale | **Absent** — one non-resolving exemplar across 3,598 records |

## 2. Outcome classes (per §3.4)

| Class | Count |
|---|---|
| Successfully populated | 0 |
| Existing valid references | 0 |
| Unsupported candidate assertions | 1 (the exemplar — recorded, not asserted here) |
| Invalid / unresolved target identifiers | 1 (as above) |
| Records with no evidenced realization relationship | 29 (all — no evidence base) |
| Categories deferred (upstream dependencies) | 4 (actors/resources/systems/information — BC-59 blockers) |

## 3. Deferral record (residual gap, honestly open)

`realization.processes` remains unpopulated pending an **upstream gap**: realizes-coverage at scale in the processes catalog, with targets aligned to this catalog's post-mv1 identities (`capabilities:capability-<slug>-<hash>`). The processes-side exemplar itself needs alignment (its target id predates two migrations) — recorded here as a cross-repo coordination item for the processes catalog's maintainers, not a local fix (no upstream redefinition from this repo). When upstream coverage exists, a successor CR re-runs this reconciliation and populates from the same evidence class.

No inference, no forced completeness: blank stays blank where evidence is absent.
