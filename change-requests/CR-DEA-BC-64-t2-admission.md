# CR-DEA-BC-64: T2 Admission (Order Management, Learning and Development, Portfolio and Investment Management)

| Field | Value |
|---|---|
| **CR** | CR-DEA-BC-64 |
| **Title** | T2 admission: Order Management, Learning and Development, Portfolio and Investment Management |
| **Status** | Landed |
| **Series** | CR-DEA-BC |
| **Change layer** | Record admissions (coverage-gap tranche 2) |
| **Target repository** | `technehub-labs/dea-catalog-business-capabilities` |
| **Target branch** | main |
| **Dependencies** | CR-DEA-BC-62 (register and tranche method); CR-DEA-BC-63 (T1 records are related-capability targets) |
| **Primary deliverable** | `capabilities:capability-order-management-t6wm3h`, `capabilities:capability-learning-and-development-b8qw5n`, `capabilities:capability-portfolio-and-investment-management-m4kw72` canonical; index + discovery views regenerated |
| **Decision authority** | Catalog governance (repository owner) |
| **Owner** | Emmanuel A. Otchere |
| **Date** | 2026-10-31 |
| **Landing** | PR #118 (squash ad4f818) |
| **Trigger** | Tranche 2 of the CR-DEA-BC-62 sequence. |

## 1. Admissions

- **C-03 Order Management** (party-relationship/operate) admitted. Completes the commercial cluster (order, quote, price-list, contract, purchase-order, return).
- **C-05 Learning and Development** (agency-organization/build) admitted. Fills the agency-organization build cell (training-program, course-section, education-program).
- **C-06 Portfolio and Investment Management** (strategy-direction/design) admitted. Fills the strategy-direction design cell (project, business-case, transformation-plan, budget, grant).

Each record carries the full 7-stage ladder passage (candidate, observed, corroborated, normalized, ecf-mapped, reviewed, canonical) with SRC-023/026/027 evidence per the CR-DEA-BC-62 standard, argued boundaries against named neighbours, and `why_capability` recording object-demand density with the enterprise-generality level honestly pending the generality-matrix refresh.

## 2. Acceptance criteria

1. Full gate suite green with the tranche records included.
2. `CATALOG.yaml` and the four discovery views regenerated in the landing PR.

## 3. NOT-list

1. No schema, vocabulary, or ECF changes.
2. No other records admitted.
