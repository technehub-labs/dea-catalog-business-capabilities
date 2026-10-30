# CR-DEA-BC-GAP-000: Capability Coverage Gap Analysis (Candidate Identification)

**Date:** 2026-11-02 · **Landed by:** CR-DEA-BC-62 · **Status:** Adopted register (candidate identification; admission proceeds tranche-by-tranche under the evidence ladder)

> **Erratum against the workspace draft (CR-DEA-BC-GAP-000):** the draft said 17 of 49 cells occupied; the correct count from the same extraction is **15 of 49** (2 agency + 1 enablement + 2 finance + 4 governance + 2 party + 1 product + 3 strategy). Post-admission arithmetic below is restated on the corrected base: admitting C-01..C-11 fills 7 new cells (finance-accounting/operate is deepened by C-01, not newly filled), taking coverage to **22 of 49**.

## 1. Method

Three coverage signals, all computed from committed artifacts:

1. **ECF 7×7 matrix coverage** (FOUNDATIONS D8/D9): the 29 canonical capabilities occupy **17 of 49 cells**; 32 cells are empty.
2. **Business-object demand:** of the 74 canonical business objects in `dea-catalog-business-objects`, **70 are referenced by no capability's `business_object`** field.
3. **Processes mirror check:** the processes catalog structures its 3,598+ records as 7 ECF domains × 7 stages (`sd/pv/pr/ge/fa/eo/ao` × `conceive..retire`), i.e. it already assumes process content in cells where no capability exists — the capability layer is the thinner of the two.

Existing candidates already in the pipeline (not re-proposed): the three candidate-only subtrees (`epm-5fxren`, `orgdesign-a7s8bf`, `relmgmt-nu73v9`).

## 2. Candidate register (ranked by evidence density + cell centrality)

| # | Candidate capability | ECF primary (domain × stage) | Business-object evidence (uncovered objects) | Rationale |
|---|---|---|---|---|
| C-01 | **Billing & Revenue Management** | finance-accounting × operate | invoice, credit-note, payment, tax-record | The revenue cycle (charge → invoice → collect) is the highest-density uncovered object cluster; Financial Resource Management covers stewardship, not the revenue cycle. |
| C-02 | **Subscription & Service Management** | party-relationship × operate | subscriber, subscription, service-instance, service-number, sim-profile, tariff-plan, usage-record, prepaid-balance | The telecom/MCSP flavor of the objects catalog is entirely uncovered; subscriber lifecycle is a first-order repeatable ability. |
| C-03 | **Order Management** | party-relationship × operate | order, quote, price-list, contract, purchase-order, return | Order-to-cash front half; distinct from C-01 (cash) and Customer Management (relationship, not transaction lifecycle). |
| C-04 | **Talent Management** | agency-organization × operate | employee, onboarding-plan, offboarding-plan, performance-review | Workforce Planning/Management cover design/build of workforce; the employee lifecycle (hire-to-retire) is uncovered, and the agency-organization operate cell is empty. |
| C-05 | **Learning & Development** | agency-organization × build | training-program, course-section, education-program | Workforce capability building; distinct from Workforce Management (deployment) and Planning (demand). |
| C-06 | **Portfolio & Investment Management** | strategy-direction × design | project, business-case, transformation-plan, budget, grant | Strategic-direction build/design gap; the change-initiatives and investment-initiatives catalogs already exist as record stores awaiting this capability's governance frame. |
| C-07 | **Product Development** | product-value × design | product, requirement, release-candidate, forecast | Product-value is the emptiest operational domain (1 cell of 7); offering conceive exists, the design/build lifecycle does not. |
| C-08 | **Policy Management** | governance-existence × conceive | policy | Policies are governed objects with lifecycle (draft → enforce → retire); Regulation Management covers external obligations only. |
| C-09 | **Privacy & Consent Management** | governance-existence × design | consent-record, party-credential | Directly evidenced by the information-classes catalog: PII is a regulated class whose lawful-basis/data-subject-rights controls (CR-CTL-CAT-02 records) need an owning capability. |
| C-10 | **Audit & Assurance Management** | governance-existence × improve | audit-finding, lessons-learned, improvement-proposal | The improve-stage signal for governance; also fills enablement improve (continuous improvement) if scoped enterprise-wide. |
| C-11 | **Incident & Service Operations** | enablement-operations × improve | incident, ticket, configuration-item, environment | Run-side feedback loop (detect → restore → learn); Technology Enablement's operate cell covers steady-state, not the incident lifecycle. |
| C-12 | **Network & Production Asset Operations** | enablement-operations × operate | network-asset, production-machine, manufacturing-lot, bill-of-material | Industry-inflection candidate: admit only under an industry-specialization decision (specialization view), not first-order. |

Deliberately **not** proposed as first-order candidates: care/health/citizen/public-sector clusters (patient, care-encounter, citizen, public-case, insurance-claim) and physical-retail (retail-store) — sector-specific; per FOUNDATIONS D7 they belong in industry specialization views, and the objects catalog's multi-industry corpus will keep exceeding first-order scope.

## 3. Cell-coverage effect if C-01..C-11 are admitted

15/49 → **22/49 cells** covered. New cells filled: finance-accounting/operate is deepened (C-01); agency-organization/operate (C-04), agency-organization/build (C-05), strategy-direction/design (C-06), product-value/design (C-07), governance-existence/improve (C-10), enablement-operations/improve (C-11). Every domain except party-relationship and product-value gains at least one new cell; product-value gains design/build/activate occupancy via C-07's secondaries.

## 4. Recommended next step

Land this register as the capabilities catalog's next research tranche (evidence-first): each C-NN becomes a candidate entry with its object evidence cited, then passes the evidence ladder (corroborate → review → canonical) under the standard admission tests. Suggested sequencing: C-01/C-02/C-04 first (highest object density + empty operate cells in their domains).

## 5. Not-list

1. No capability is admitted by this analysis; it is a candidate register.
2. No business-object catalog changes (its 74 records are the evidence base, not the target).
3. No ECF vocabulary changes.
