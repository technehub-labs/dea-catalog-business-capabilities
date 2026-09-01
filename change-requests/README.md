# Change Requests: CR-DEA-BC Series

Change requests for the Business Capability catalog. CRs land verbatim on acceptance (md5-verified against the reviewed source); they are not edited in place after landing. Status changes are recorded by the PR that lands or amends the CR, not by rewriting the CR document.

| CR | Title | Status | Landed | Notes |
|---|---|---|---|---|
| CR-DEA-BC-01 | First-Order Business Capability Method | Proposed | This PR | Method and documentation only: semantics, admission criteria, evidence lifecycle, ECF overlay rules, governance. No entries, no schema, no CI changes. |
| CR-DEA-BC-01A | Capability classification reconciliation: ADR-015 alignment | Landed | PR #3 (2026-08-31) | Record shape: kind by entity specialization, governed `capability_layer`, `capability_type` deprecated. Constrains one record field, not the method. |
| CR-DEA-BC-02 | Evidence-Based First-Order Capability Investigation | Landed, in execution | PR #4 (2026-08-31) | Evidence corpus, candidate universe, normalization, generality matrix, distinctness sweep, admission. Research artifacts land under `docs/research/`. |

## Numbering

- The series tag is `CR-DEA-BC` (DEA Business Capability).
- CR-DEA-BC-01 is the method CR; CR-DEA-BC-01A was renumbered from an early CR-DEA-BC-02 allocation (2026-08-31) when the number was yielded to the evidence-investigation CR.
- Successors are parked, not scheduled: CR-DEA-BC-03 (schema + CI reconciliation with dea-metamodel), CR-DEA-BC-04 (industry specialization framework; first view: Mobile Communications Service Provider).
- **Decision 2026-09-01 (numbering reconciliation):** CR-DEA-BC-02 section 40 (authored before the method CR) named BC-03 as "First-Order Capability Canonicalization"; CR-DEA-BC-01 (accepted later) names BC-03 as schema + CI and treats canonical admission as BC-02's own execution through the section 38 gate and the method review gates. Decided: **the CR-DEA-BC-01 assignment holds.** Canonical admission of the recommended set is method execution (METHODOLOGY.md section 12), not a separate CR; CR-DEA-BC-03 is the schema + CI reconciliation. Recorded per the renumbering convention (GOVERNANCE.md section 2).

## Ordering note

CR-DEA-BC-02 executes ahead of CR-DEA-BC-01 by design: the investigation produces raw material; the method CR defines how that material is judged. Acceptance of CR-DEA-BC-01 does not retro-invalidate the research artifacts; it gates their promotion. Nothing becomes canonical until it passes the method.
