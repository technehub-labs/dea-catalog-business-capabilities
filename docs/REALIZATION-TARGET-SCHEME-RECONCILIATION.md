# Realization Target Scheme Reconciliation

**Status**: Accepted investigation (CR-DEA-BC-56, 2026-10-28) · **No population under this CR**

---

## 1. Realization model inventory

The schema's `realization` block (CR-40/43) declares five target arrays; population today is 0/29 across all five. Target-category landscape (evidence: the org namespace table; CR-43 M-2; the processes catalog's own relationship contract):

| Category | Owning catalog / authority | Canonical id scheme | Permitted reference form | Validation mechanism | Canonical targets available | Population evidence | Disposition |
|---|---|---|---|---|---|---|---|
| `processes` | `dea-catalog-business-processes` (populated, 3,598 records) | `processes:process-<slug>-<hash6>` (post-mv1, org-wide) | canonical id (schema pattern `^processes:` since CR-43 M-2) | schema pattern (local) + the processes catalog's own record authority | **yes** | the processes catalog records `realizes` relationships targeting this catalog (`cross_catalog_field: identity_scope` per its entity-system registry) — upstream-owned, mined as evidence under BC-57 | **Supported under the existing contract** |
| `services` | `dea-catalog-business-services` (populated, 18 records) | `services:*` (org-wide) | not declared in the realization block | none declared | yes, but the category is **outside the declared realization arrays** — adding it is a model change | n/a | **Requires an approved model change** (out of BC-57 scope) |
| `actors` | `dea-catalog-actors` (Wave 3 scaffold — **empty**) | scheme not yet exercised authoritatively | n/a | n/a | **no** (zero canonical entities) | n/a | **Blocked upstream** (catalog empty; scheme unconfirmed until first admissions) — tracked as U-2 (BC-59) |
| `resources` | **no owning catalog exists** | none | n/a | n/a | no | n/a | **Blocked upstream** (no catalog; would require a new org decision) — U-2 |
| `systems` | **no owning catalog exists** | none | n/a | n/a | no | n/a | **Blocked upstream** (same) — U-2 |
| `information` | **no owning catalog exists** (Information is a business object concept, not a catalog) | none | n/a | n/a | no | n/a | **Blocked upstream** (same; object-catalog coverage is BC-58's U-1 question) — U-2 |

## 2. Semantics discipline (§4.3 of the CR)

Realization distinguishes: the capability (enduring ability) vs the processes through which the enterprise performs it vs the systems/resources/actors that enable execution vs the information used vs the outcomes enabled. Only `processes` carries an authorized, exercised cross-catalog contract today: the processes catalog's `realizes` (process → capability) with `identity_scope` — the BC catalog's `realization.processes` is the capability-side view of that same governed relationship, so population must be **evidenced by the upstream's own assertions** (mined under BC-57), never inferred from name or applicability.

## 3. Bounded implementation recommendation

1. **BC-57 may populate `realization.processes` only**, each entry evidenced by a `realizes` assertion in the processes catalog targeting the capability's id (upstream authority; provenance recorded).
2. `actors` / `resources` / `systems` / `information` remain unpopulated and blocked (BC-59 records the dispositions; no local schemes invented).
3. `services` as a realization category is a model question for a future CR — not authorized here.

## 4. Unresolved dependencies (named)

- **U-2** (actors/resources/systems/information): BC-59 owns the disposition record.
- Processes-catalog semantics: the `realizes` direction and `identity_scope` contract are owned upstream; this catalog consumes, never redefines.
