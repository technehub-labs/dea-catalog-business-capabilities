# Entity Change Impact Management Standard

**Status**: Normative (CR-DEA-BC-50, 2026-10-28)
**Template**: [`docs/templates/ENTITY-CHANGE-IMPACT-ASSESSMENT.md`](templates/ENTITY-CHANGE-IMPACT-ASSESSMENT.md)
**Scope**: every CR that materially changes a canonical entity (or the governance that governs them). Assessment template lives with the CR (referenced or embedded); it does not replace CR approval.

---

## 1. Change categories

| Category | Definition | Typical review floor |
|---|---|---|
| **Editorial** | presentation only; canonical meaning untouched (README render fixes, link repairs) | gate suite |
| **Record-structure** | representation/constraints of canonical data (schema, registry) | model CR + gap-analysis lineage (CR-42 precedent) |
| **Semantic** | definition, boundary, classification, specialization, or interpretation changes | semantic review (METHODOLOGY §12 gates) + affected-neighbor re-checks |
| **Relationship** | adds/removes/changes an authorized relationship representation | RI rules + R-1 boundary (no unauthorized typing) |
| **Lifecycle** | governed status/state transition | CR-49 standard (evidence + approval per transition) |
| **Identity** | ids, canonical naming, storage layout, org-wide references | **escalates to org-wide governance** (CR-35A; never a catalog-only approval) |
| **Governance/validation** | rules, checks, approvals, evidence mechanisms | this CR series' precedents; gates preserved (never weakened silently) |

A CR may span categories only with explicit dependencies and acceptance per category.

## 2. Required impact assessment (dimensions)

Every in-scope CR states, per applicable dimension, the impact **or an explicit "no impact identified, because …"**:

| Dimension | Question | Where the answer is checked |
|---|---|---|
| Semantic | meaning/scope/interpretation changed? | semantic review; boundary/related re-checks |
| Identity | ids or canonical references affected? | id-system gate; migration map |
| Relationships | related entities/constraints affected? | RI-001..003 |
| Documentation | READMEs/templates/indexes to update? | DCV rules; template render |
| Evidence | evidential basis or provenance altered? | EVIDENCE.md; ladder |
| Validation | which checks are affected? | gate suite; this repo's 8 gates + CST |
| Lifecycle | state transition or historical record needed? | CR-49 |
| Derived views | which generated outputs go stale? | views `--check` (freshness gate) |
| Consumers | known downstream dependencies affected? | consumer registry (dependencies.yaml; sibling catalogs) |
| Migration | must records/references transform? | migration evidence; no fabricated values |

**Unknown ≠ absent**: unknown impacts are recorded as unknown (AC-07), never assumed away.

## 3. Escalation conditions

Additional review/authority is required when a change: alters upstream semantic meaning; touches org-wide identity rules; changes the meaning of an existing relationship; needs an unsupported schema construct; breaks known consumers; cannot be assessed for missing evidence; or bundles independent changes with materially different approval requirements.

## 4. Worked example — CR-DEA-BC-23 (EPM admission), assessed retrospectively

- **Category**: Semantic (+ Lifecycle admission; + Relationship by boundary assertions).
- **Semantic**: new 29th capability; definition/boundary admitted via evidence ladder (E3) and review gates. **Identity**: new org-wide id; no existing id affected. **Relationships**: 6 structured-boundary distinctness assertions added (now RI-002/003-governed). **Documentation**: entity README (now BC-46-rendered); index rows. **Evidence**: TER-EPM-001 track + SRC-020/021/022. **Validation**: schema extended later via BC-40 (the gap this process now front-loads: an impact assessment at BC-23 time would have flagged "schema does not admit the post-mv1 record shape" → BC-40's five violations would have been caught pre-landing). **Lifecycle**: ladder evidence-seeded → admitted; status active. **Derived views**: capability map + CATALOG regenerated (did land). **Consumers**: direction-loop closure recorded. **Migration**: none.
- The lesson is institutionalized: the validation dimension must name the schema authority for any new field value **before** landing.
