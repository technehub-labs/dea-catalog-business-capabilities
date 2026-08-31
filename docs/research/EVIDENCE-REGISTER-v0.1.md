# Evidence Register v0.1: Summary for Review

CR-DEA-BC-02 staged delivery, step 1: Evidence Corpus + Evidence Register (CR §33, items 1:2).
Date: 2026-08-31. Status: draft-for-review. Machine-readable register: `evidence-register.yaml` (same folder).

## Corpus

| ID | Source | Class | Retrieval | Role |
|----|--------|-------|-----------|------|
| SRC-001 | BA Guild / BIZBOK v13 | business-architecture | indirect (quoted; primary text membership-gated) | capability identity, business-object focus |
| SRC-002 | Open Group / TOGAF Business Capabilities Guide | enterprise-architecture | indirect (quoted) | definition convergence, stability |
| SRC-003 | SAP LeanIX capability guidance | enterprise-architecture | direct | durability, implementation independence, mutual exclusivity |
| SRC-004 | APQC PCF v8.0 cross-industry | cross-industry-process | direct (full download behind form) | recurrence discovery; contamination guard |
| SRC-005 | IF4IT capability model | business-architecture | pending | frequency signal (per CR §12) |
| SRC-006 | Capstera / Ciopages vendor models | commercial-capability-models | direct | frequency signal; industry specialization sources |
| SRC-007 | BIAN Service Landscape 14.0 | industry-specific | direct | specialization-path exemplar (banking) |
| SRC-008 | UK DfE business architecture guidance | government-guidance | direct (detailed extract pending) | abstraction-level warning; government context |
| SRC-009 | Essential Project capability modelling | enterprise-architecture | direct | naming heuristic (Noun/Verb vs Verb/Noun) |
| SRC-010 | Repo internal baseline | internal-baseline | direct | tenets, record shape (ADR-015 reconciled) |

## Key convergent findings

1. **Definition convergence is high** across three independent sources (BIZBOK, TOGAF, SAP LeanIX): a capability is a possess-or-exchange ability, what-not-how, stable over time, non-redundant. The DEA definition (CR §3) sits inside this consensus without importing any taxonomy.
2. **The possess-or-exchange phrasing** (BIZBOK/TOGAF) independently corroborates the repo's required/possessed/sourced/realized spectrum (CR §17).
3. **Mutual exclusivity is operationalizable** (SAP LeanIX BP-1): unambiguous child assignment as the distinctness test feeds admission gate §38.
4. **The vendors warn against their own product** (SRC-006): generic lists are starting points, not answers. External corroboration of CR §13 (commonality is not sufficient) from the class with the most incentive to claim otherwise.
5. **APQC PCF confirmed as process taxonomy** (13 categories, 1000+ processes, explicit benchmarking purpose): usable for recurrence discovery, structurally barred from capability naming (CR §6.3, §37).
6. **Industry layering exists in practice** (BIAN 14.0: capability landscape over non-overlapping service domains): a working exemplar of the specialization path the first-order catalog defers to (CR §29).

## Register gaps (carried forward)

- G1: IF4IT direct retrieval pending
- G2: DfE full-page extract pending; GRM/GSRM to add for the government diversity arm
- G3: APQC PCF 8.0 full element list behind download form
- G4: BIZBOK primary text membership-gated; proceeding on quoted definitions

## Corpus assessment

All 7 source classes of CR §6 covered. Definition convergence high. **Ready for**: candidate universe construction (CR §21, §30). **Not ready for**: canonical admission: no candidate has been classified or tested; the §38 gate is untouched.

## Next pass (on your go)

Candidate Universe v0.1: derive candidates from the §30 hypothesis map against this corpus, classify each per §19 (CAPABILITY / PROCESS / ... / UNRESOLVED), record per §22 with evidence links into this register, and rate evidence per §23 (E0:E5). Delivered for review before any ECF overlay.
