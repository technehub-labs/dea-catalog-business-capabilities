# CR-DEA-BC-62: Coverage-Gap Candidate Register and Tranche Method

| Field | Value |
|---|---|
| **CR** | CR-DEA-BC-62 |
| **Title** | Coverage-gap candidate register: candidate identification and sequenced admission method |
| **Status** | Landed |
| **Series** | CR-DEA-BC |
| **Change layer** | Research register + method (no record admissions in this CR) |
| **Target repository** | `technehub-labs/dea-catalog-business-capabilities` |
| **Target branch** | main |
| **Dependencies** | CR-DEA-BC-61 (index truth); dea-catalog-business-objects (74 canonical objects, the evidence base); dea-catalog-controls + dea-catalog-information-classes (C-09's cross-catalog control pull) |
| **Primary deliverable** | `catalog-research/COVERAGE-GAP-REGISTER.md` + evidence-register SRC-026/027 + the T1-T4 admission sequence |
| **Decision authority** | Catalog governance (repository owner) |
| **Owner** | Emmanuel A. Otchere |
| **Date** | 2026-10-31 |
| **Trigger** | Following CR-DEA-BC-61's index correction, the repo owner directed a coverage-gap analysis and evidence-based admission of the identified candidates through sequenced tranches. |

## 1. Change objective

Establish the candidate register (C-01..C-12) as a governed research artifact, land its evidence sources, and fix the tranche sequence that admits the candidates through the standard evidence ladder. This CR admits no records; the tranches are CR-DEA-BC-63..66.

## 2. The three signals

1. **ECF coverage:** 15 of 49 cells occupied by the 29 canonical capabilities (corrected arithmetic; the workspace draft's 17 is corrected by erratum in the register).
2. **Object demand:** 70 of 74 canonical business objects are referenced by no capability (SRC-026).
3. **Process mirror:** the processes catalog already structures its corpus as 7 domains × 7 stages — it assumes process content in cells where no capability exists.

## 3. The register (summary; full detail in `catalog-research/COVERAGE-GAP-REGISTER.md`)

C-01 Billing and Revenue Management · C-02 Subscription and Service Management · C-03 Order Management · C-04 Talent Management · C-05 Learning and Development · C-06 Portfolio and Investment Management · C-07 Product Development · C-08 Policy Management · C-09 Privacy and Consent Management · C-10 Audit and Assurance Management · C-11 Incident and Problem Management · C-12 Network and Production Asset Operations (industry-inflection; deferred to a specialization decision, not admitted in this programme).

## 4. Tranche sequence

| Tranche | CR | Candidates | Rationale |
|---|---|---|---|
| T1 | CR-DEA-BC-63 | C-01, C-02, C-04 | Highest object density; two empty operate cells (finance, agency) |
| T2 | CR-DEA-BC-64 | C-03, C-05, C-06 | Order cycle completes the commercial cluster; strategy design cell |
| T3 | CR-DEA-BC-65 | C-07, C-08, C-09 | Product design cell; governance conceive/design pull incl. the PII control obligations |
| T4 | CR-DEA-BC-66 | C-10, C-11 | Governance improve + enablement improve cells; closure |

Each tranche CR: admits its records as canonical with the full 7-stage ladder passage recorded (candidate → observed → corroborated → normalized → ecf-mapped → reviewed → canonical, all evidenced), regenerates `CATALOG.yaml` and the discovery views, and passes the full gate suite.

## 5. Admission evidence standard for the tranches

Every record cites SRC-026 (object-cluster density), SRC-027 (cross-signal convergence), and SRC-023 (cross-industry process class corroboration). `why_capability` records object-demand density and distinctness honestly, with the enterprise-generality level explicitly pending the next generality-matrix refresh (no E-level is claimed without that exercise). Boundaries are argued against named neighbouring capabilities.

## 6. Acceptance criteria

1. `catalog-research/COVERAGE-GAP-REGISTER.md` and evidence-register SRC-026/027 landed.
2. Register row + CHANGELOG entry.
3. No record admissions in this CR (counts unchanged: 29 canonical / 3 candidates).

## 7. NOT-list

1. No capability is admitted by this CR.
2. C-12 is not scheduled; it requires an industry-specialization decision (FOUNDATIONS D7).
3. The three existing candidate-only subtrees are untouched (their promotion is their own research thread).
4. No ECF vocabulary or schema changes.
