# Specialization Register v0.1: Summary for Review

CR-DEA-BC-02 close-out, deliverable section 33 item 9: candidates deferred to industry/sector/enterprise specialization, plus the specialization-boundary evidence (section 29). Machine-readable twin: `specialization-register.yaml`. Date: 2026-09-01.

Status: candidate-not-canonical. Nothing here enters the first-order set; specializations reference parents and never modify or replace them (CR-DEA-BC-01 component 14). New ID family: `SPEC-NNN`.

## Specialization candidates (3)

| ID | Name | Level | Parent | Industry | Disposition |
|---|---|---|---|---|---|
| SPEC-001 | Telecom Customer Management | L3 | CAND-005 Customer Management | Telecommunications | Deferred to CR-DEA-BC-04 (first view: Mobile Communications Service Provider) |
| SPEC-002 | Citizen / Member Relationship | L3 if confirmed | CAND-005 (hypothesis) | Government, non-profit | Deferred; unification decision trigger: government reference models (gap G5) |
| SPEC-003 | Claims Management | L3 | Undetermined (Customer vs Operations adjacency) | Insurance | Deferred to CR-DEA-BC-04; parent hypothesis required before view work |

Notes:

- **SPEC-001** (CAND-034) failed the first-order anti-invention test by carrying an industry qualifier; that is the expected and correct outcome for an industry form.
- **SPEC-002** (CAND-006) is the generality matrix's single sector-bound result: strong in government and non-profit, moderate in healthcare, absent commercially. Two readings are recorded ((a) sector specialization of Customer Management; (b) standalone sector-bound capability); the decision stays deferred with its trigger, per the conservative re-test rule.
- **SPEC-003** was recorded directly from evidence (SRC-011 flags claims management as insurance-flavored; SRC-012 corroborates the domain). It never entered the candidate universe as a first-order candidate.

## Boundary evidence (section 29 analysis)

| Source | Observation | Value to the register |
|---|---|---|
| SRC-007 BIAN (banking) | Capability landscape above discrete non-overlapping service domains; release 14.0 | Models the specialization path this catalog defers to; exemplar, not first-order input |
| SRC-012 ACORD (insurance) | Ten high-level industry capability areas, updated 2025 | Second industry reference model; candidate source for insurance specialization |
| SRC-004 APQC PCF | Cross-industry and industry-specific variants maintained separately | Industry variants feed this register; the cross-industry variant feeds first-order hypotheses |
| SRC-006 vendor models | Industry models for automotive, hospital, medical devices, P&C insurance, retail banking | Candidate sources for future specialization views; commercial bias acknowledged |

## Deferred decisions

| ID | Question | Trigger |
|---|---|---|
| SPEC-D1 | CAND-005/CAND-006 unification: is Citizen / Member Relationship a specialization of Customer Management? | Government reference models (evidence register gap G5) |

## DoD rows closed by this artifact

- Industry-specialization candidates identified (CR section 39).

Remaining CR-DEA-BC-02 DoD rows: unresolved-questions roll-up, research report (section 34), visual research artifacts (section 35), OTCHERE-only canonical examples check.
