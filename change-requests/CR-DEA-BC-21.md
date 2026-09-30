# CR-DEA-BC-21: Analytics and Intelligence Recon (companion to CR-DEA-BC-20)

**Status**: Proposed (2026-09-30); recon complete; ADR-ES-021 drafted; ratification pending
**Filed**: 2026-09-30
**Author**: Coder (DEA-Catalog-Business-Capabilities)
**Depends on**: CR-DEA-BC-01 (method), CR-DEA-BC-02 (evidence), CR-DEA-BC-09 (naming advisory set), CR-DEA-BC-12 (noun-as-ability advisory), CR-DEA-BC-20 (noun-as-ability rule 7 + N-017 deferral)
**Related**: BC-SR-A001 §6 (open; pending CR-DEA-BC-21 outcome)
**Supersedes**: none
**Companion**: CR-DEA-BC-20 (this CR answers the DP-E question that BC-20 explicitly deferred)

## 1. Problem statement

CR-DEA-BC-09 §7 surfaced Analytics and Intelligence as a noun-as-ability advisory: "Analytics" reads as an activity (the act of analyzing) rather than as an ability, and "Intelligence" is ambiguous (does it denote the capability of *being intelligent about* something, or the *product* of analysis?). Both senses are partially valid and partially overlapping; this is the BC-09 advisory's tension.

CR-DEA-BC-20 §10 (DP-E) explicitly deferred the rename to a standalone recon because the rename direction depends on resolving the underlying semantic question: is the entry a single ability with two vocabulary tokens (Analytics and Intelligence as one capability, two faces), two peer abilities (Analytics *and* Intelligence, semantically distinct), or one ability whose canonical name best reflects the dominant direction (and whether the secondary face is in scope at all)?

The user direction recorded in DP-E: "Analytics and Intelligence seems to me that Intelligence will imply having analysis capability, and perhaps vice versa? My key issue is that they are two disciplines with common and yet unique ability characteristics, right? So we perhaps need to dedicate an ADR to research further the direction to take. It's an item you'd need to schedule as part of the recon to enable us fix."

The recon is therefore not a routine rename; it is a foundational-ability question that may require an ADR before a rename can be specified.

## 2. Recon scope

The recon investigates four candidate direction vectors:

| Vector | Candidate rename | Reading | Notes |
|---|---|---|---|
| A | `dea:capability-insight-management` | Single ability: turn data into insight | Insight is the business object; Management is the noun-as-ability suffix |
| B | `dea:capability-intelligence-management` | Single ability: institutional intelligence | Carries the existing "Intelligence" token; risk of ambiguity with AI |
| C | `dea:capability-decision-intelligence-management` | Single ability: intelligence in service of decisions | Anchors the ability to its decision purpose; longest, most explicit |
| D | (no rename) | Reviewed-retained as `Analytics and Intelligence` | Same path as N-015 Security Management and N-019 Enterprise Governance; rationale would need to defend the bare-noun reading |

The recon considers but does not commit to one vector. It emits an ADR and a recommended direction; the rename (or retention) lands in a follow-on CR that re-uses the BC-09 / BC-12 / BC-20 admission pattern.

## 3. Recon procedure (executed 2026-09-30)

1. **Source sweep (3 classes per METHODOLOGY.md EVIDENCE.md §3)**:
   - **Cross-industry-process (SRC-023, APQC PCF 7.4)**: Naming pattern is verb-led; process 20959 is "Develop, manage, and deliver analytics". Sub-process 7.7.8.2 uses "insights" as the noun-of-product. **No "Business Intelligence" PCF process**. "Intelligence" appears only in market-research context (10106).
   - **Business-architecture (SRC-024, BIZBOK v14 + Forrester)**: BIZBOK v14 introduces "Insights" as a discipline alongside capabilities, value, organization, information, metrics. Forrester treats insights as the firm-wide DataOps/ModelOps output (Insights-Driven Business maturity model).
   - **Standards-body (SRC-025, DMBOK 2nd ed. + OMG DMN + BABOK v3)**: DMBOK subordinates BI to data management. OMG DMN does not name "decision intelligence" as an enterprise ability. BABOK does not name Analytics or Intelligence as a knowledge area.
2. **Distinctness sweep**: expanded distinctness peers to include Strategic Planning (planning direction), Strategy Formulation (formulating direction), Information Management (information stewardship), Enterprise Performance Management (EPM/CAND-037 in research track; outcome-governance role). Vector A preserves distinctness from each neighbor. Vector B collapses against Market Intelligence as a sub-capability. Vector C would shift ECF cell from information-management x operate to governance-existence x activate, breaking BC-SR-A001.
3. **Semantic-center-of-gravity test** (BC-13 §A rule): the recon produces 2-3 sentences each for the four candidate readings. "Insight" has the cleanest center-of-gravity for the ability: it is the noun-of-product of the analytics activity. "Analytics" alone names the activity, not the ability. "Intelligence" is divided between activity and capability noun (ambiguous with AI as a software category). "Decision Intelligence" reads as "intelligence about decisions", closer to software support than to enterprise ability.
4. **ECF placement audit**: confirmed the current placement `information-management x design/operate` (with operate as the dominant stage; per BC-SR-A001 section 4 boundary decision v0.1). Vector A preserves this peer-of-Information-Management boundary. Vector B would weaken the peer-of-substrate reading. Vector C would break BC-SR-A001.
5. **User vocabulary test**: "Insight Management" is widely recognized (BIZBOK, Forrester, vendor naming). "Intelligence Management" is narrower (market research, AI ambiguity). "Decision Intelligence Management" reads as vendor platform category.

Detailed evidence recorded in `catalog-research/recon/INV-AI-v0.1.yaml` (5 procedure steps; 4 vectors evaluated; recommendation recorded in section `recommendation`).

## 4. ADR

The recon emits **ADR-ES-021** (companion to the BC-21 CR) titled "Analytics and Intelligence: rename to Insight Management under TAXONOMY rule 7" at `catalog-research/recon/ADR-ES-021.yaml`. The ADR records:

- The semantic-center-of-gravity decision: **V-A Insight Management** chosen (highest evidence convergence; cleanest center-of-gravity).
- The ECF placement decision: V-A preserves the current ECF cell (information-management x operate) without re-litigation.
- The business_object decision: unchanged at "Insight" (current value matches V-A's noun product).
- The recommended rename target name (`Insight Management`) and id slug (`dea:capability-insight-management`).
- Three deprecation rationales (V-B, V-C, V-D).

The ADR follows the promotion ritual (header + body Status + Acceptance section) per ADR-ES-001 §10-§11.

## 5. Recommendation

**Vector A (Insight Management)** is the recon's recommendation:

- new_id: `dea:capability-insight-management`
- new_name: `Insight Management`
- current_id: `dea:capability-analytics-and-intelligence` (unchanged until follow-on rename CR lands)
- aliases retained: `Analytics and Intelligence` (legacy noun-of-discourse; preserved for provenance); `Data and Analytics` (BC-12); `Insight` (BC-12); `Intelligence` (BC-12; evidence-register compatibility); `Business Intelligence` (legacy DMBOK vocabulary)
- version: 1.1.0 → 2.0.0 (semver-incompatible name change; bump under CR-DEA-BC-22)

## 6. Deliverable

A follow-on CR (CR-DEA-BC-22, "Analytics and Intelligence rename to Insight Management") that executes the rename under the BC-09 / BC-12 / BC-20 admission pattern. CR-DEA-BC-22 is blocked on user ratification of V-A and inherits H8 hard-gate enforcement from CR-DEA-BC-20. Any rename that fails noun-as-ability must register an N-NNN review-retained exemption; Insight Management with the Management suffix passes H8 cleanly, so no exemption is needed.

## 7. Acceptance criteria (for this CR — the recon CR)

- [x] Three-class source sweep complete with 3 sources recorded in `catalog-research/recon/INV-AI-v0.1.yaml` (cross-industry-process SRC-023; business-architecture SRC-024; standards-body SRC-025).
- [x] Distinctness sweep expanded per §3 step 2; documented.
- [x] Semantic-center-of-gravity test executed per §3 step 3; documented.
- [x] ECF placement audit completed per §3 step 4; documented.
- [x] User vocabulary test conducted per §3 step 5; documented.
- [x] ADR-ES-021 written at `catalog-research/recon/ADR-ES-021.yaml`; promotion ritual observed; recommended Vector A selected with rationale.
- [x] Follow-on CR drafted (CR-DEA-BC-22) with the rename; presented for user review (this CR §5-§6).
- [x] N-022 verdict recorded in `catalog-research/normalization.yaml` as `review-retained-pending-ADR` with `affected_entry: dea:capability-analytics-and-intelligence` and `recommendation: V-A Insight Management`.
- [x] CAND-018 vector extension recorded in `catalog-research/candidates.yaml` (4 vectors V-A/B/C/D with recommendation fields).
- [x] Evidence-register.yaml updated: SRC-023/024/025 added (3 new sources); register_gaps G11 added; register_version 0.7.0 → 0.8.0; compiled 2026-09-30.

## 8. Out of scope (carries forward)

- The actual rename (this CR; the follow-on CR-DEA-BC-22 does it).
- EPM admission (CR-DEA-BC-15 provisional; separate track).
- Relationship Management recon (BC-SR-A001 §6; separate track).

## 9. References

- `docs/FOUNDATIONS.md` §2 (capability definition) and §7 (noun-as-ability test).
- `TAXONOMY.md` section 1 rules 1.1-1.7 and section 1A.3 (machine-enforcement scope).
- `scripts/check_naming.py` H8 hard gate (BC-20 §6).
- `catalog-research/normalization.yaml` N-015 (Security Management review-retained), N-019 (Enterprise Governance review-retained) — analogous retention patterns; N-022 (Analytics and Intelligence review-retained-pending-ADR; recommendation V-A).
- `catalog-research/evidence-register.yaml` SRC-023 (APQC PCF 7.4), SRC-024 (BIZBOK v14 + Forrester), SRC-025 (DMBOK 2nd ed. + OMG DMN + BABOK v3), G11 (BC-21 recon gap).
- `catalog-research/candidates.yaml` CAND-018 (current) and `cand_018_vectors` extension (V-A/B/C/D).
- `catalog-research/recon/INV-AI-v0.1.yaml` (the recon evidence inventory).
- `catalog-research/recon/ADR-ES-021.yaml` (the recommendation ADR).
- BC-SR-A001 §4 (boundary decision v0.1) and §5 (Analytics carve-out).
- `entities/v1-alpha/dea:capability-analytics-and-intelligence/dea:capability-analytics-and-intelligence.yaml` — current entry under recon (version 1.1.0 unchanged).
- CR-DEA-BC-20 §10 (DP-E deferral) and §3.7 (BC-09 advisory set).
- `OpenDEA_Foundation_Capability_Map_Nested.html` — regenerated after BC-20; pending regeneration after CR-DEA-BC-22 lands.