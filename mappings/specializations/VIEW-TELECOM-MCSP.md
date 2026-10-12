# View: Mobile Communications Service Provider (MCSP)

CR-DEA-BC-04 proving instance. Machine form: `view-telecom-mcsp.yaml`. Baseline: the v1-alpha admission set of 2026-09-02 (29 canonical first-order capabilities as of CR-DEA-BC-23; PR #32 added CAND-018 Analytics and Intelligence (renamed to Insight Management at CR-DEA-BC-22 on 2026-09-30), CAND-023 Resilience (admitted as Resilience Management, renamed to Continuity Management at CR-DEA-BC-09), CAND-029 Innovation (admitted as Innovation Management, renamed to Idea Management at CR-DEA-BC-09); 27 (Technology Enablement, CR-DEA-BC-17); 28 (Organizational Design, CR-DEA-BC-14); 29 (Enterprise Performance Management, CR-DEA-BC-23, admitted 2026-10-12)).

## Coverage

**Enterprise Performance Management (EPM, 29th canonical):** admitted at CR-DEA-BC-23 (2026-10-12); cell strategy-direction x operate; closes the direction loop per BC-SR-A001 §16 (Strategy Formulation -> Strategic Planning -> Performance Management -> Insight Management -> Adaptation). MCSP relevance: performance SLAs (M7) and capacity planning (M4) are key telecom-specialized instantiations of EPM. Sibling cross-references: Operations Management (delivery performance), Information Management (performance data), Strategy Formulation (objectives).

**29 of 29 canonical capabilities accounted for**: 4 admitted specializations, 23 inherited unchanged (added EPM to the inherited list). The 3 entries added at PR #32 (resilience, innovation, analytics-and-intelligence [renamed to insight-management at CR-DEA-BC-22]) are inherited unchanged: they are sector-agnostic, the telecom view adds no specialization for them, and they participate via their canonical coordinates (governance-existence × design + operate, product-value × conceive + design, enablement-operations × operate).

## Admitted specializations

| SPEC | Parent | MCSP name | What the sector narrows or adds |
|---|---|---|---|
| SPEC-001 | Customer Management | Telecom Customer Management (alias: Subscriber Management) | The customer is a subscriber; the relationship anchors in a subscription, a number, a device. Activation, port-in/port-out, SIM change, contractual churn windows. |
| SPEC-004 | Offering Management | Tariff and Bundle Management (alias: Product Catalog Management) | Offerings are tariffs, bundles, add-ons priced on usage dimensions; regulatory notification duties ride the offering lifecycle. |
| SPEC-005 | Partner Management | Roaming and Interconnect Management | Peers are other operators; agreements are roaming and interconnect, with wholesale rates, settlement, coverage footprints. |
| SPEC-006 | Regulation Management | Telecom Regulatory Compliance | License conditions, lawful intercept, emergency services access, number portability duties, universal service, spectrum conditions. |

All four carry sector evidence at E3 (TM Forum business frameworks, BIAN service landscape, GSMA roaming/wholesale practice, sector regulation). Evidence, not authority (EVIDENCE.md).

## Rejected (visible discipline)

**Network Management**: fails the business-object test (D7). The object is technology; technology estate stewardship is already canonical (Technology Management), and network operations is an L5 realization concern. Recording the rejection keeps the industry-serving-technology impostor pattern out of the view.

## Deferred (unchanged by this view)

- SPEC-002 Citizen/Member Relationship: gated on the G5 corpus gap.
- SPEC-003 Claims Management: parent undetermined.

## ECF

All specializations inherit parent coordinates per D6. SPEC-001 carries an industry participation note; no parent mapping is contradicted.
