# CR-DEA-BC-21: Analytics and Intelligence Recon (companion to CR-DEA-BC-20)

**Status**: Proposed (carried from CR-DEA-BC-20 §10 companion-CR slot)
**Filed**: 2026-09-30
**Author**: Coder (DEA-Catalog-Business-Capabilities)
**Depends on**: CR-DEA-BC-01 (method), CR-DEA-BC-02 (evidence), CR-DEA-BC-09 (naming advisory set), CR-DEA-BC-20 (noun-as-ability rule 7 + N-017 deferral)
**Related**: BC-SR-A001 §6 (open)
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

## 3. Recon procedure (proposed)

1. **Source sweep (3 classes per METHODOLOGY.md EVIDENCE.md §3)**:
   - Business-architecture class: BABOK v3 knowledge area "Business Analysis Planning"; BIZBOK Part III Analytics capability map; APQC PCF level-3 analytics process group.
   - Standards-body class: ISO/IEC 38505 (data governance), OMG DMN (decision modeling), OMG OCEB 2 (business intelligence content), NIST SP 800-90 (information quality).
   - Commercial-capability-models class: Gartner BI/Analytics Magic Quadrant taxonomy; Forrester Wave Analytics; TDWI analytics maturity model.
2. **Distinctness sweep**: expand distinctness peers to include Strategic Planning (planning direction), Strategy Formulation (formulating direction), Information Management (information stewardship), Enterprise Performance Management (EPM/CAND-037 in research track; outcome-governance role). Convergent or divergent?
3. **Semantic-center-of-gravity test** (BC-13 §A rule): is the defining activity *producing* insight, *stewarding* intelligence as an asset, *informing* decisions, or something else? The recon produces 2-3 sentences each for the four candidate readings.
4. **ECF placement audit**: confirm or revise the current placement `strategy-direction/conceive`. Does "Intelligence" imply a different ECF center of gravity? Does "Insight" imply placement in `product-value` or `enablement-operations`? The recon re-runs the placement rule.
5. **User vocabulary test**: which of the four candidate names does an executive recognize without explanation? Survey N=5 internal reviewers per EVIDENCE.md §6 evidence-pending rules.

## 4. ADR

The recon emits **ADR-ES-021** (companion to the BC-21 CR) titled "Analytics and Intelligence: ability direction." The ADR records:

- The semantic-center-of-gravity decision (Vector A vs B vs C vs D).
- The ECF placement decision.
- The business_object decision (current value is `Insight`; this recon may revise).
- The recommended rename target name and id slug, OR the rationale for review-retained retention.

The ADR follows the promotion ritual (header + body Status + Acceptance section) per ADR-ES-001 §10-§11.

## 5. Deliverable

A follow-on CR (CR-DEA-BC-21A or BC-22 depending on the recon outcome) that executes the rename (or registers the review-retained decision) under the BC-09 / BC-12 / BC-20 admission pattern. The follow-on CR inherits H8 hard-gate enforcement from CR-DEA-BC-20; any rename that fails noun-as-ability must register an N-NNN review-retained exemption.

## 6. Acceptance criteria (for this CR — the recon CR)

- [ ] Three-class source sweep complete with at least 2 sources per class recorded in `catalog-research/INV-AI-v0.<n>.md` (or `.yaml`).
- [ ] Distinctness sweep expanded per §3 step 2; documented.
- [ ] Semantic-center-of-gravity test executed per §3 step 3; documented.
- [ ] ECF placement audit completed per §3 step 3; documented.
- [ ] User vocabulary test conducted per §3 step 5; documented.
- [ ] ADR-ES-021 written; promotion ritual observed; recommended Vector selected with rationale.
- [ ] Follow-on CR drafted (CR-DEA-BC-21A or BC-22) with the rename or review-retained decision; presented for user review.
- [ ] N-017 verdict recorded in `catalog-research/normalization.yaml` (rename or `verdict: review-retained`).

## 7. Out of scope (carries forward)

- The actual rename (this CR; the follow-on CR does it).
- EPM admission (CR-DEA-BC-15 provisional; separate track).
- Relationship Management recon (BC-SR-A001 §6; separate track).

## 8. References

- `docs/FOUNDATIONS.md` §2 (capability definition) and §7 (noun-as-ability test).
- `TAXONOMY.md` section 1 rules 1.1-1.7 and section 1A.3 (machine-enforcement scope).
- `scripts/check_naming.py` H8 hard gate (BC-20 §6).
- `catalog-research/normalization.yaml` N-015 (Security Management review-retained), N-019 (Enterprise Governance review-retained) — analogous retention patterns.
- BC-SR-A001 §6 (open submittal review item).
- `entities/v1-alpha/dea:capability-analytics-and-intelligence/dea:capability-analytics-and-intelligence.yaml` — current entry under recon.