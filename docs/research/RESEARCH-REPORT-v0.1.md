# Research Report v0.1: First-Order Business Capability Investigation

CR-DEA-BC-02 capstone deliverable (section 33 item 10; structure per section 34). A synthesis of how the first-order set emerged from evidence. Date: 2026-09-01. Status: candidate-not-canonical; the report explains and recommends; admission remains subject to review (section 38; METHODOLOGY.md section 12).

Machine-readable manifest: `research-report.yaml`. Underlying registers: evidence register v0.2, candidate universe v0.2, normalization register v0.2, enterprise-generality matrix v0.1, preliminary ECF overlay v0.1, distinctness sweep v0.1, admission gate close-out v0.1, specialization register v0.1.

---

## 1. Research Purpose

The investigation answered the section 4 question set: which abilities recur across materially different enterprise types; which apparent capabilities are actually processes, functions, organizational constructs, outcomes, services, resources, or systems; which candidates are industry-specific or specializations; which are synonyms; which have stable business-object focus; and how the survivors relate to the ECF.

The purpose was never to produce a list. It was to establish that a recurring enterprise capability layer exists independently of industry, and to derive its membership from evidence rather than invention (section 41: discover, do not invent).

## 2. Capability Semantics

The investigation operated under the semantics later ratified by CR-DEA-BC-01 and METHODOLOGY.md:

- A capability is a durable ability to produce, enable, control, preserve or realize a meaningful business outcome, independent of organization, process, people, technology or implementation.
- First-order means enterprise-general: recognizable across materially different enterprises without industry interpretation.
- Possession is a spectrum (required / possessed / sourced / realized); outsourcing an activity does not remove the capability requirement.

These semantics were corroborated, not imported: BIZBOK's possess-or-exchange phrasing (SRC-001), TOGAF capability guidance (SRC-002), and SAP LeanIX practice guidance (SRC-003) independently converge on the same identity criteria.

## 3. Evidence Method

Research, not copy (EVIDENCE.md). Sources evidence recurrence; none is a semantic authority. Every observation was registered with its source, its supported CR sections, and its implication; retrieval honesty was recorded (membership-gated primaries and form-gated downloads are marked as such). Candidates carry ordinal evidence ratings E0 to E5 reflecting depth of independent corroboration; E0 marks disambiguation-only citations.

## 4. Source Corpus

Twelve registered sources across seven classes:

| Class | Sources |
|---|---|
| business-architecture | SRC-001 BIZBOK |
| enterprise-architecture | SRC-002 TOGAF, SRC-003 SAP LeanIX, SRC-009 Essential Project, SRC-011 Avolution |
| cross-industry-process | SRC-004 APQC PCF v8.0 |
| industry-specific | SRC-007 BIAN, SRC-012 ACORD |
| government-guidance | SRC-008 UK DfE |
| commercial-capability-models | SRC-005 IF4IT, SRC-006 vendors |
| internal-baseline | SRC-010 repository baseline |

Corpus gaps recorded openly: G1 (IF4IT page cited in CR section 12 not located; site and definition confirmed), G2 (DfE detailed extraction), G3 (APQC full element list behind download form), G4 (primary BIZBOK text membership-gated), G5 (government reference models GRM/GSRM not yet retrieved). G5 is the trigger for the CAND-005/CAND-006 unification decision.

## 5. Enterprise Comparison

The enterprise-generality matrix scored all 29 capability-classified candidates across ten enterprise types (commercial, professional services, manufacturing, retail, financial services, healthcare, technology, infrastructure, government, non-profit) with cell values strong / moderate / none. Declared rule: demonstrated when strong in 7+ of 10 types; partial when strong+moderate in 7+; else sector-bound.

Result: 26 demonstrated, 2 partial (CAND-023 Resilience, CAND-029 Innovation), 1 sector-bound (CAND-006 Citizen / Member Relationship: strong only in government and non-profit).

## 6. Candidate Universe

35 classified entries: 29 capability-classified first-order candidates plus 6 boundary probes. Evidence distribution among first-order candidates: E5 x2 (Customer Management, Workforce Management), E4 x7, E3 x11, E2 x3 (held pending cross-industry check), E0 x3 (disambiguation list: cited to record that a source listed them, not to assert capability status).

The universe is a research population, not a catalog. Nothing in it is canonical by virtue of appearing there (section 30).

## 7. Classification

Every entry was classified against the 16-class taxonomy (CAPABILITY, PROCESS, FUNCTION, ACTOR, SERVICE, OUTCOME, RESOURCE, INFORMATION, SYSTEM, TECHNOLOGY, POLICY, RULE, SPECIALIZATION, ORGANIZATION, DUPLICATE, UNRESOLVED). The six boundary probes resolved as: CAND-030 ORGANIZATION, CAND-031 PROCESS, CAND-032 SYSTEM, CAND-033 ACTOR, CAND-034 SPECIALIZATION, CAND-035 UNRESOLVED. Section 13 and 14 give their dispositions.

## 8. Normalization

Nine recorded decisions (N-001 to N-009) under the rule that no merge occurs on name similarity alone. Highlights:

- N-001: the people cluster (Human Capital Management vs Workforce vs HR) resolved to **Workforce Management**; HR names the organization, not the ability.
- N-002: Marketing stands distinct from both Customer Management and Offering Management.
- N-004: Sourcing and Procurement distinct from Supplier Management.
- N-005: Customer Management over CRM-named variants (CRM is system-flavored vocabulary).
- N-007: CAND-004 Stakeholder Relationship Management kept as **grouping parent**, withdrawn from the admission track.
- N-008: CAND-011 Value Delivery **dissolved**; children re-rooted (its business object failed the noun-anchor test).
- N-009: the Analytics re-test (trigger: matrix completion) closed confirming the status quo; the boundary objection against Information Management is carried, not resolved.
- Deferred: CAND-005/CAND-006 unification (trigger: government reference models, gap G5).

## 9. Capability Boundaries

The pairwise distinctness sweep enumerated the complete pair space programmatically (C(27,2) = 351 pairs) after excluding the two removed aggregates. Method: business-object partition first, explicit-pair escalation where partitions meet. Result: 318 pairs distinct by partition, 21 distinct by explicit decision, 11 parent-child, 1 deferred (the CAND-005/CAND-006 pair). Verdict: distinctness demonstrated for 26 of 27 on-track candidates; no unresolved synonyms or overlaps.

Boundary gaps that remain: CAND-018 Analytics and Intelligence vs CAND-017 Information Management (carried into deferral); the three E2 candidates (boundary defensibility unproven on current evidence).

## 10. Enterprise-General Findings

The section 36 initial finding is confirmed with evidence: a recurring enterprise capability layer exists independently of industry. The strongest convergence (E5/E4) sits in nine families: customer, workforce, finance, operations, sourcing, compliance, risk, marketing, information. Industry-specific models (BIAN, ACORD, APQC variants) add specialized capabilities above that common layer rather than replacing it; vendor lists themselves warn that generic lists are unfit without enterprise deliberation (SRC-006), corroborating the section 13 rule that commonality is not sufficient.

## 11. ECF Overlay

28 of 29 capability-classified candidates received preliminary coordinates under the earliest-initiation rule (primary = first initiation stage, not heaviest operation). CAND-019 Technology Management is **held unmapped**: no ECF domain carries technology (technology is an L5 layer concern, not a domain), and the mapping is recorded as legitimately absent per the section 38 clause, with the N-006 open question carried (business capability with a domain, or cross-cutting governance concern). Empty cells are documented as legitimate results (section 27; no forced coverage): governance-existence x build/activate, finance-value x design/build/activate/retire, and people-organization x conceive/retire are empty at this granularity without semantic damage.

Six mappings carry open conflict flags (CAND-008, CAND-010, CAND-017, CAND-018, CAND-019, CAND-028), flagged not smoothed (section 26). Each is a case where earliest initiation is arguable between two stages or domains; the flags ride into the review package with the close-out.

## 12. Specialization Findings

The specialization register (v0.1) records three candidates (SPEC-001 Telecom Customer Management, SPEC-002 Citizen / Member Relationship, SPEC-003 Claims Management) with parent traceability or an explicit undetermined-parent note, plus boundary evidence from BIAN (banking) and ACORD (insurance): mature industries layer specialized capabilities over common ones, which is exactly the path this catalog defers to specialization views (first view: Mobile Communications Service Provider, CR-DEA-BC-04).

## 13. Rejected Candidates

| Candidate | Name | Classification | Correct home |
|---|---|---|---|
| CAND-011 | Value Delivery | CAPABILITY (dissolved aggregate) | Children re-rooted (N-008) |
| CAND-030 | Finance Department | ORGANIZATION | Organization constructs |
| CAND-031 | Invoice Processing | PROCESS | dea-catalog-processes |
| CAND-032 | CRM System | SYSTEM | System catalog |
| CAND-033 | Customer Service Team | ACTOR | dea-catalog-actors |

Rejections are retained as evidence of the boundary. The E0 disambiguation entries served the same function during classification: they record that a source used the term, not that the term names a capability.

## 14. Unresolved Candidates

| Candidate | Name | State |
|---|---|---|
| CAND-006 | Citizen / Member Relationship | Deferred: sector-bound; unification with CAND-005 awaits government reference models (G5) |
| CAND-018 | Analytics and Intelligence | Deferred: boundary delineation against CAND-017 undecided |
| CAND-023 | Resilience Management | Deferred: E2 evidence; generality partial; corpus expansion needed |
| CAND-029 | Innovation Management | Deferred: E2 evidence; generality partial; corpus expansion needed |
| CAND-035 | Common Good Production | Unresolved classification (capability vs outcome); non-profit reference models needed |

## 15. Preliminary First-Order Set

The admission gate close-out (v0.1) recommends 23 candidates, each with all ten section 38 axes met:

| Candidate | Capability | ECF primary |
|---|---|---|
| CAND-001 | Strategy | governance-existence x conceive |
| CAND-002 | Strategic Planning | governance-existence x conceive |
| CAND-003 | Enterprise Governance | governance-existence x conceive |
| CAND-005 | Customer Management | customer-demand x operate |
| CAND-007 | Supplier Management | supply-resources x build |
| CAND-008 | Partner Management | customer-demand x conceive (conflict flag) |
| CAND-009 | Offering Management | product-offering x conceive |
| CAND-010 | Marketing | customer-demand x conceive (conflict flag) |
| CAND-012 | Operations | operations-delivery x operate |
| CAND-013 | Financial Stewardship | finance-value x conceive |
| CAND-014 | Financial Management | finance-value x operate |
| CAND-015 | Workforce Management | people-organization x build |
| CAND-016 | Workforce Planning | people-organization x design |
| CAND-017 | Information Management | operations-delivery x operate (conflict flag) |
| CAND-019 | Technology Management | held unmapped (legitimately absent; N-006 open question, conflict flag) |
| CAND-020 | Risk Management | governance-existence x conceive |
| CAND-021 | Compliance Management | governance-existence x activate |
| CAND-022 | Legal Management | governance-existence x conceive |
| CAND-024 | Security Management | governance-existence x design |
| CAND-025 | Sourcing and Procurement | supply-resources x build |
| CAND-026 | Asset Management | supply-resources x build |
| CAND-027 | Facility Management | supply-resources x activate |
| CAND-028 | Change Management | governance-existence x improve (conflict flag) |

Full coordinates: `admission-gate-closeout.yaml` and `preliminary-ecf-overlay.yaml`. The set size is an output of the analysis, not a target (section 31); 23 grounded capabilities are preferable to 40 invented ones.

## 16. Open Questions

1. **G5 corpus gap**: government reference models (GRM/GSRM) unretrieved; gates the CAND-005/CAND-006 unification and the CAND-006 evidence rating.
2. **CAND-018 boundary**: Analytics and Intelligence vs Information Management delineation needs a decision input the current corpus does not provide.
3. **E2 pair**: Resilience and Innovation need cross-industry corpus expansion (government, non-profit, infrastructure) before their evidence and generality axes can move.
4. **CAND-035 classification**: capability vs outcome for non-profit value production; unresolved.
5. **Six ECF conflict flags**: earliest-initiation arguable between adjacent stages/domains for CAND-008, 010, 017, 018, 019, 028; review-time decisions.
6. **N-006 carried note**: whether Technology Management reads as a business capability with a domain or a cross-cutting concern; resolved as capability for this pass, reviewable.
7. **Corpus gaps G1-G4**: retrieval-limited; none blocks admission, all recorded.

## 17. Recommendations

1. Review the 23-candidate recommendation set (semantic then architectural gate, METHODOLOGY.md section 12) as the promotion package for CR-DEA-BC-03 canonicalization.
2. Expand the corpus toward government and non-profit reference models (closes G5, moves CAND-006/023/029/035).
3. Commission the Analytics/Information boundary delineation as a targeted decision, not a research phase.
4. Keep the specialization register as the single intake for industry forms; CR-DEA-BC-04 builds the first view from it.
5. Leave empty ECF cells empty; revisit only if a candidate with legitimate semantics appears.

---

## DoD rows closed by this artifact

- Unresolved questions documented (section 39).
- Research report published (section 39; section 33 item 10).

Remaining section 39 rows: visual research artifacts (section 35); OTCHERE Inc examples and no-ACME verification. Illustrative examples in this report use OTCHERE Inc where any appear; no ACME examples exist in the research line.
