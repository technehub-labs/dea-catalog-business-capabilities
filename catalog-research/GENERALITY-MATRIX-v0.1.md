# Enterprise-Generality Matrix v0.1: Summary for Review

CR-DEA-BC-02 §8/§9; deliverable §33 item 6. Date: 2026-08-31.
Machine-readable: `enterprise-generality-matrix.yaml`. Analytical evidence; not the catalog (§9).

## Shape

29 first-order candidates × 10 enterprise types (§8: commercial, professional services, manufacturing, retail, financial services, healthcare, technology, infrastructure, government, non-profit). Cell values per §9: strong / moderate / sector / none. Generality rule: **demonstrated** when strong in 7+ of 10 types.

## Result

| Verdict | Count | Candidates |
|---|---|---|
| demonstrated | 26 | all except the three below |
| partial | 2 | CAND-023 Resilience, CAND-029 Innovation |
| sector-bound | 1 | CAND-006 Citizen/Member Relationship |

## Findings

1. **The matrix converges with the pre-check.** The three candidates that fail "demonstrated" are exactly the three weakest on evidence (E2) or scope: no new failures surfaced, no existing gap was hidden. Two independent axes agreeing is the discipline working.
2. **CAND-006 is sector-bound, not weak.** Citizen/Member is strong in government and non-profit, moderate in healthcare, absent elsewhere. This is the specialization pattern asserting itself: it belongs on the specialization path (CR §29), not in the first-order set. The deferred unification decision (vs CAND-005) now has a matrix position to argue from.
3. **Non-profit is the discriminating column.** Nearly every moderate cell sits in non-profit (and to a lesser degree government): donor-funded and mission-driven enterprises reshape finance, compliance, facilities, and innovation rather than lacking them. This supports the §16 distinction between universally necessary and commonly necessary rather than a binary.
4. **No candidate is universally absent in any column** at the strong/moderate level except CAND-006's sector pattern: the first-order hypothesis that a common enterprise layer exists (CR §36) survives the diversity test.

## Effect on the admission gate

`admission-gate-precheck.yaml` regenerated to v0.2: the generality axis moves from `untested` to `met` for 23 candidates; the same 6 candidates retain gaps (CAND-004/011/018 boundary; CAND-006/023/029 evidence + generality + boundary). Remaining pending artifact: the full pairwise distinctness sweep.

## Carry-forward

1. Pairwise distinctness sweep across the 23 (closes the last `untested` axis)
2. Aggregate question decision (CAND-004, CAND-011): parents-only vs dissolve
3. Corpus patch: continuity + innovation source classes (CAND-023/029 evidence)
4. CAND-006 → specialization register, pending the deferred unification decision
