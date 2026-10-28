# Cross-Catalog Reference Scheme Reconciliation (U-2)

**Status**: Accepted investigation (CR-DEA-BC-59, 2026-10-28) · **No record/schema changes** · Scope derived from BC-56's category inventory (no scope expansion to every conceivable category)

## 1. Dependency dispositions

| Category | Owner | Evidence at inspection | Disposition | Required upstream decision |
|---|---|---|---|---|
| `actors` | `dea-catalog-actors` | Wave 3 scaffold, **0 entities** (GitHub API, 2026-10-28) | **Blocked upstream** | first admissions exercising the `actors:*` scheme; then a cross-catalog reference contract |
| `resources` | none | **no owning catalog exists in the org** | **Blocked upstream** (deeper: requires a new org-level decision to create the catalog) | org decision on whether a resources catalog should exist at all |
| `systems` | none | no owning catalog exists | **Blocked upstream** (same) | same |
| `information` | none | no owning catalog exists; Information is a business-object concept (coverage question belongs to U-1/BC-58) | **Blocked upstream** (same) | same, plus the objects-catalog outcome |
| (`services` — noted, out of BC-56 scope) | `dea-catalog-business-services` | populated (18 records, `services:*`) | **Not required** for the current realization model (category outside the declared arrays); revisit only via a model CR | none |
| (`processes` — resolved for contrast) | `dea-catalog-business-processes` | populated; `processes:*`; `realizes` contract | **Resolved** (BC-56/BC-57) | none |

## 2. Discipline recorded

Technical reference validity (a resolvable id) is separate from semantic validity (an authorized relationship): even when schemes exist, population remains evidence-gated. **No local substitute identity scheme is introduced**; no silent normalization; blocked categories remain unpopulated regardless of completeness pressure.

## 3. Residual

U-2 stays open as a tracked dependency with named blockers; `realization.processes` proceeds under its own resolved contract (BC-57).
