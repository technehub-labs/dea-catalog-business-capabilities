# Candidate Universe v0.1: Index for Review

CR-DEA-BC-02 staged delivery, step 2: Candidate Universe (CR §33 items 3+4).
Date: 2026-08-31. Status: **candidate-not-canonical**. Machine-readable: `candidates.yaml` (same folder).

## Counts

| Classification | Count |
|---|---|
| CAPABILITY (first-order candidates) | 29 |
| SPECIALIZATION (recorded per §29) | 1 |
| PROCESS (disambiguation evidence) | 1 |
| ORGANIZATION (disambiguation evidence) | 1 |
| ACTOR (disambiguation evidence) | 1 |
| SYSTEM (disambiguation evidence) | 1 |
| UNRESOLVED (open question) | 1 |
| **Total** | **35** |

All entries cite back to the evidence register by source ID. Every entry carries `canonical: false` in its provenance.

## Coverage map (theme × count)

| Theme (§30) | First-order candidates |
|---|---|
| Enterprise Direction | Strategy, Strategic Planning, Enterprise Governance (3) |
| Stakeholder Relationship | Stakeholder Relationship Management, Customer Management, Citizen/Member Relationship, Supplier Management, Partner Management (5) |
| Offering | Offering Management, Marketing (2) |
| Value Delivery | Value Delivery, Operations (2) |
| Financial Stewardship | Financial Stewardship, Financial Management (2) |
| People | People/Workforce Management, Workforce Planning (2) |
| Information | Information Management, Analytics and Intelligence (2) |
| Technology | Technology Management (1) |
| Risk and Assurance | Risk, Compliance, Legal, Resilience, Security Management (5) |
| Sourcing and External Provision | Sourcing and Procurement (1) |
| Assets and Resources | Asset Management, Facility Management (2) |
| Change and Improvement | Change Management, Innovation Management (2) |

12 themes mapped; 4 themes get only 1 candidate (Technology, Sourcing, Value Delivery as aggregate, Offering as aggregate). The aggregate-level candidates (Value Delivery, Offering, Stakeholder Relationship) carry decomposition immediately per CR §15 (too-broad guard).

## Disambiguation entries (kept on file per §19)

- CAND-030 Finance Department (ORGANIZATION)
- CAND-031 Invoice Processing (PROCESS)
- CAND-032 CRM System (SYSTEM)
- CAND-033 Customer Service Team (ACTOR)

Each is recorded with the source that conflated it with a capability and the classification decision. Per CR §5 these are evidence, not decisions.

## Specialization register (one entry as exemplar)

- CAND-034 Telecom Customer Management: records the path from CAND-005 to industry reality. Tracked so CR-DEA-BC-03 has the on-ramp; never enters first-order set.

## UNRESOLVED

- CAND-035 Common Good Production: §8 enterprise diversity requires explicit non-profit/government study. Current coverage thin. Carry into next pass with a deeper government-capability literature sweep (GRM, GSRM).

## Evidence strength distribution (first-order only)

| Rating | Count | Notes |
|---|---|---|
| E5 | 2 | Customer Management, People/Workforce Management: highest convergence |
| E4 | 7 | Financial Stewardship, Operations, Sourcing/Procurement, Compliance, Risk, Marketing, Information, Asset |
| E3 | 11 | Strategy, Strategic Planning, Enterprise Governance, Stakeholder Relationship Management, Supplier Management, Partner Management, Workforce Planning, Workforce Planning, Legal, Security, Change, Asset, Facility |
| E2 | 3 | Citizen/Member, Resilience, Innovation: lower frequency; held as candidates pending cross-industry check |

The E0 entries (CAND-030/032/033) are the disambiguation list: cited only to record that the source listed them as capabilities, not to assert capability status.

## Confidence distribution

The §24 confidence axis is tracked separately from evidence strength. High confidence currently co-occurs with high evidence (Customer Management, People/Workforce Management); low confidence with low frequency (Citizen/Member, Innovation). One Strong-evidence + Low-confidence pattern has not yet surfaced; the discipline that produced the separation remains untested.

## Universal-necessity check (CR §16)

Every first-order candidate has been assessed against §16: would a bounded value-exchanging enterprise meaningfully lack this ability and still operate as the same kind of enterprise? The current universe shows all 29 first-order candidates clearing "Commonly necessary". Two remain to be promoted to "Universally necessary" pending deeper cross-industry check: Legal Management and Compliance Management. Both depend on the regulated vs unregulated distinction (a non-profit in many jurisdictions operates with limited compliance surface; a bank cannot).

## What this universe does NOT contain

- **Canonical capability records**. CR §38 admission gate is untouched.
- **ECF overlays**. CR §25: ECF mapping follows candidate evaluation.
- **Per-candidate normalization decisions**. CR §20 normalization pass is the next step (CR-DEA-BC-02 §33 item 5).
- **Enterprise-generality matrix**. CR §33 item 6: classification pass next.

## Carry-forward list (next pass)

1. **Normalization decisions** for the candidate pairs that vendors/sources name differently: People/Workforce Management (Human Capital Management vs Workforce vs HR); Marketing (under Customer vs Offering); Analytics and Intelligence (under Information vs standalone); Sourcing and Procurement (vs Supplier Management).
2. **ECF overlay** for the E4+ first-order candidates (§25 to §28).
3. **Enterprise-generality matrix** (§33 item 6) built from the §8 diversity list.
4. **Gate-close per candidate** against §38 admission rules.
5. **Rejections and deferrals register** (per CR §33 item 13: rejected and deferred candidates documented).

## Provenance

- `candidates.yaml` carries `evidence_register: docs/research/evidence-register.yaml`
- Every candidate record carries `provenance.research_artifact: true; canonical: false`
- Every source link is a register ID (SRC-NNN); no orphan references