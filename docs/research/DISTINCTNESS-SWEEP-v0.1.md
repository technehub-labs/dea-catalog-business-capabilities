# Distinctness Sweep v0.1: Summary for Review

CR-DEA-BC-02 section 20 / section 38; carry-forward from the generality matrix. Date: 2026-09-01.
Machine-readable: `distinctness-sweep.yaml`. Research artifact; not the catalog.

## Scope and method

27 on-track candidates after the aggregate decisions below; 351 pairs evaluated. Primary test: business-object distinctness. Candidates are partitioned into 12 business-object families; cross-family pairs classify Distinct by the partition rule, and every within-family or semantically adjacent pair carries an explicit decision. No pair rests on name similarity alone (CR section 20).

## Aggregate decisions (the carried question)

| Candidate | Question | Decision | Ground |
|---|---|---|---|
| CAND-004 Stakeholder Relationship Management | candidate, parents-only, or dissolve | **Parents-only** grouping parent; withdrawn from the admission track | No boundary independent of the union of children; the common relationship pattern stays documented for the section 29 specialization path and the deferred CAND-005/006 unification |
| CAND-011 Value Delivery | candidate, parents-only, or dissolve | **Dissolved**; rejected aggregate per section 39 | Business object Outcome fails the noun-anchor test; the durable abilities are the children. CAND-012 Operations re-rooted first-order; Service Delivery, Fulfilment, Production re-attached under it |

The two aggregates get different outcomes for a stated reason: CAND-004 carries a grouping pattern the programme still needs; CAND-011 does not.

## Sweep result

| Relationship | Pairs | Notes |
|---|---|---|
| Parent-Child | 11 | hierarchy confirmed, including N-003 re-test (CAND-017 to CAND-018) closed as N-009 |
| Distinct (explicit) | 21 | adjacency pairs argued on evidence, incl. N-002, N-004 carried forward |
| Distinct (partition) | 318 | different business-object families |
| Deferred | 1 | CAND-005/CAND-006 unification (trigger: government reference models, gap G5) |
| Synonyms / overlaps unresolved | 0 | |

**Verdict: distinctness demonstrated for 26 of 27 on-track candidates.** No hidden duplicates surfaced; the 29-name list survives the pairwise test with exactly one known deferred decision.

## Findings that matter

1. **The assurance family is the densest cluster** (Risk, Compliance, Legal, Resilience, Security): five siblings, all distinguishable by object (uncertainty, obligation, legal matter, continuity, protection posture). The hierarchy under Risk Management holds, but each sibling's distinctness is now argued, not assumed
2. **Name similarity failed silently where it should**: Strategic Planning vs Workforce Planning share a word and nothing else; the section 20 rule caught them as Distinct by object. The partition rule plus explicit-pair escalation is doing the work
3. **N-003 re-test closed conservatively**: the generality matrix removed the generality objection to standalone Analytics, but corpus treatment is still split (theme vs fold-in vs standalone) at E3/low confidence. Parent-Child retained; CAND-018's boundary gap is carried, not resolved
4. **The pre-check cleans up**: CAND-006's stale `untested: enterprise_generality` entries from v0.2 are gone; v0.3 reflects exactly one pending artifact (the deferred unification)

## Effect on the admission gate

`admission-gate-precheck.yaml` regenerated to v0.3:

- 27 candidates on track (CAND-004 reclassified, CAND-011 dissolved; both boundary gaps resolved by decision)
- Distinctness `met` for 26; `untested` only for CAND-006 pending the deferred unification
- Remaining gaps sit on 4 candidates: CAND-006 (evidence, generality, boundary), CAND-018 (boundary), CAND-023 and CAND-029 (evidence, generality, boundary)
- 23 candidates clean on every axis

## Carry-forward

1. Corpus patch: continuity + innovation source classes (CAND-023/029 evidence and generality gaps)
2. CAND-018 boundary work: Analytics vs Information boundary, informed by N-009
3. Government reference models (gap G5): closes the CAND-005/006 unification, the last pending distinctness artifact
4. Research report assembly (section 33 item 10, section 34 structure)
