# CR-DEA-BC-21: Analytics & Intelligence recon (deferred DP-E from CR-DEA-BC-20)

**Status**: Applied (2026-09-30); recommendation V-A Insight Management; forwarded to ADR-ES-021; user ratified V-A on 2026-09-30; CR-DEA-BC-22 applies the rename
**Filed**: 2026-09-30
**Author**: Coder (for eaojnr)
**Depends on**: CR-DEA-BC-01 (method), CR-DEA-BC-09 (naming advisory set), CR-DEA-BC-12 (noun-as-ability advisory), CR-DEA-BC-20 (rule 7 + H8 hard gate; this CR resolves the DP-E deferred item)
**Carrier documents**: `catalog-research/recon/INV-AI-v0.1.yaml`, `catalog-research/recon/ADR-ES-021.yaml`
**Follow-on**: CR-DEA-BC-22 (rename CR; applied 2026-09-30 on user ratification)

## Problem statement

CR-DEA-BC-20 deferred the noun-as-ability naming question on Analytics and Intelligence (CAND-018) per user DP-E:

> For DP-E, Analytics and Intelligence seems to me that Intelligence will imply having analysis capability, and perhaps vice versa? My key issue is that they are two disciplines with common and yet unique ability characteristics, right? So we perhaps need to dedicate an ADR to research further the direction to take. It's an item you'd need to schedule as part of the recon to enable us fix.

The current name `Analytics and Intelligence` reads as a noun-of-discourse (H8 hard fail at CR-DEA-BC-20). The user wanted a deliberate, source-grounded decision rather than an opportunistic rename. This CR runs that decision.

## Recon procedure executed

`catalog-research/recon/INV-AI-v0.1.yaml` runs five steps:

1. **Three-class source sweep** — Enumerate source classes for the Analytics and Intelligence ability across the corpus; require three independent classes to observe the same name-shape pattern. Sources: BABOK v3, BIZBOK v14, DMBOK 2nd ed., OMG DMN, APQC PCF 7.4, OCEB 2, Forrester Wave Enterprise Insight Platforms, Gartner Decision Intelligence.
2. **Distinctness sweep** — Verify the candidate name does not collide with siblings (information-management, knowledge-management, strategic-planning, enterprise-performance-management, technology-enablement).
3. **Semantic-center-of-gravity test** — Identify the noun-of-product the ability concerns.
4. **ECF placement audit** — Verify the current ECF placement (enablement-operations x operate) is preserved.
5. **User vocabulary test** — Apply TAXONOMY rule 6 (plain business vocabulary) and rule 7 (noun-as-ability).

## Findings: four candidate vectors

| Vector | Name | Recommendation | Key finding |
|---|---|---|---|
| V-A | Insight Management | **PRIMARY** | Three source classes converge on "insight" as the noun-of-product. Management gerund matches rule 7. All siblings partition-distinct. ECF placement preserved. User vocabulary clear. |
| V-B | Intelligence Management | DEPRECATED | "Intelligence" as head noun collapses to "Analytics" under DMBOK 2nd ed. and Forrester. APQC PCF 7.4 reserves "intelligence" for market-research contexts. One source class only. |
| V-C | Decision Intelligence Management | DEPRECATED | Gartner Decision Intelligence is a vendor-class market category, not an enterprise-generic ability. APQC PCF 7.4 does not use the DI arity. |
| V-D | Analytics and Intelligence reviewed-retained | DEPRECATED | H8 hard fail. The only legal override is a verdict review-retained decision. V-A supersedes with a clean rename. |

## Recommendation: V-A Insight Management

**Proposed rename**:
- id: `dea:capability-analytics-and-intelligence` → `capabilities:capability-insight-management-ms4n9d`
- name: `Analytics and Intelligence` → `Insight Management`
- version: `1.0.0` → `2.0.0` (semver-incompatible name change)
- aliases: `[Analytics and Intelligence, Data and Analytics, Insight, Intelligence, Business Intelligence]`
- business_object: `Insight` (unchanged — the rename aligns the name to the object)

**Rationale summary**: Three source classes (BABOK v3, BIZBOK v14, DMBOK 2nd ed. plus OMG DMN and APQC PCF 7.4) converge on "insight" as the noun-of-product. The Management gerund matches the recognized noun-as-ability pattern. All five sibling distinctness neighbors (information-management, knowledge-management, strategic-planning, enterprise-performance-management, technology-enablement) are partition-distinct. ECF placement at `enablement-operations x operate` is preserved. The user-vocabulary test passes.

**Evidence register additions**:
- SRC-023: APQC PCF 7.4 (cross-industry-process class). Process 20959 "Develop, manage, and deliver analytics"; 7.7.8.2 "Develop insights into workforce analytics outcomes"; 3.1.1 "Perform customer and market intelligence analysis". **No "Business Intelligence" PCF process** — APQC is moving away from "BI".
- SRC-024: Forrester Wave Enterprise Insight Platforms; BIZBOK v14 (business-architecture class).
- SRC-025: DMBOK 2nd ed.; OMG DMN; IIBA BABOK v3 (standards-body class).

**New gap entry**: G11 (BC-21 recon results; closes on CR-DEA-BC-22 application).

**Candidates extension**: `cand_018_vectors` (V-A/B/C/D) appended to `catalog-research/candidates.yaml`.

**Normalization**: N-022 appended (verdict `review-retained-pending-ADR`; affected_entry `dea:capability-analytics-and-intelligence`; recommendation V-A; closes to `rename-applied` on user ratification).

**ADR**: `catalog-research/recon/ADR-ES-021.yaml` (recommendation ADR; status `proposed` at this filing; promotes to `ratified` on user ratification).

## User ratification (2026-09-30)

User ratified V-A on 2026-09-30 (Discord message id `1554690132228051015`):

> [eaojnr] V-A insight management is adopted

This ratification:
- Promotes ADR-ES-021 status from `proposed` to `ratified (2026-09-30)`.
- Closes N-022 verdict from `review-retained-pending-ADR` to `rename-applied`.
- Authorizes CR-DEA-BC-22 to apply the rename.

## Acceptance criteria

All 9 acceptance criteria checked:

- [x] Recon procedure executed and recorded in `catalog-research/recon/INV-AI-v0.1.yaml`.
- [x] Four candidate vectors evaluated (V-A, V-B, V-C, V-D).
- [x] Three source classes surveyed; SRC-023, SRC-024, SRC-025 added to evidence register.
- [x] New gap entry G11 appended (BC-21 recon closure).
- [x] V-A recommendation recorded in `catalog-research/recon/ADR-ES-021.yaml`.
- [x] N-022 appended to `catalog-research/normalization.yaml` (verdict review-retained-pending-ADR; closes to rename-applied on ratification).
- [x] `cand_018_vectors` extension appended to `catalog-research/candidates.yaml`.
- [x] User ratification of V-A on 2026-09-30.
- [x] CR-DEA-BC-22 follow-on rename CR applied on 2026-09-30 (id, name, version 2.0.0, aliases, N-022 closure, ADR-ES-021 status ratified).

## Follow-on

- **CR-DEA-BC-22**: applied 2026-09-30; rename Analytics and Intelligence to Insight Management; CATALOG + CHANGELOG + README + capability map updated; reconciliation/migration-id-map.yaml extended (3 new id_map entries; 1 new known_residual for the pre-rename slug).
- **Linter state**: H8 advisory count drops from 5 to 4 (the Analytics and Intelligence advisory is gone; the renamed entry passes cleanly). The remaining 4 advisories are rule-2 axis (semantic-review territory; unchanged from BC-20).
- **BC-09 advisory set closure**: all 5 named advisories resolved (Strategy → Strategy Formulation, Operations → Operations Management, Analytics and Intelligence → Insight Management; Enterprise Governance and Sourcing and Procurement review-retained / clarification-applied).

## Cross-references

- `catalog-research/recon/INV-AI-v0.1.yaml` (5-step recon procedure; 4 vectors)
- `catalog-research/recon/ADR-ES-021.yaml` (recommendation ADR; ratified 2026-09-30)
- `catalog-research/normalization.yaml` N-022 (verdict rename-applied)
- `catalog-research/evidence-register.yaml` SRC-023/024/025 + G11 (v0.8.0)
- `catalog-research/candidates.yaml` cand_018_vectors extension (v0.5.1)
- `change-requests/CR-DEA-BC-20.md` (rule 7 + H8 hard gate; the deferred item this CR resolves)
- `change-requests/CR-DEA-BC-22.md` (the follow-on rename CR; applied 2026-09-30)
