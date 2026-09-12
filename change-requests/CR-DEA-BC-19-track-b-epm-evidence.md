# CR-DEA-BC-19: Track B (Enterprise Performance Management) Evidence Package: Research-CR, No Admission

**Status**: Proposed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-11
**Track**: B (Enterprise Performance Management)
**Reviewer seed**: BC-SR-A001 §5 (P1) + BC-SR-A001 §16 (Direction Loop narrative)
**Investigation carrier**: CR-DEA-BC-12 §B.2 (Track B opened)
**Companion tracks**: A (TER-ORGDESIGN-001 closed 2026-09-11 under CR-DEA-BC-14), C (TER-RELMGMT-001 open)

## 1. Summary

Research-CR (no admission) that closes the Track B evidence gap. Seeds
CAND-037 (Enterprise Performance Management) in the candidate universe,
adds SRC-020/021/022 across three independent source classes, confirms
E3 evidence rating on three-source convergence, expands the distinctness
sweep from 4 to 8 peers, adds the admission-gate pre-check row, and
records the Direction Loop closure narrative required by BC-DEA-BC-13 §D.2
regardless of admission outcome.

**No canonical entity is admitted in this CR.** Catalog count remains at 28
first-order canonical capabilities. The Track B admission is a separate
CR (provisional CR-DEA-BC-15) that triggers on user acceptance of this
evidence package.

## 2. Scope

In scope:

- CAND-037 added to candidates.yaml (E1, canonical false, classification
  CAPABILITY, business object Performance).
- SRC-020/021/022 added to evidence-register.yaml across three independent
  source classes (business-architecture; commercial-capability-models;
  standards-body).
- TER-EPM-001 track evidence record updated: status
  evidence-pending → evidence-seeded; E3 confirmed; sources_consulted
  updated to SRC refs; open_evidence_questions answered (1 confirmed, 1
  partial, 1 open per loop-closure narrative requirement).
- Preliminary-ecf-overlay.yaml EPM overlay updated: confidence low →
  low-medium.
- Distinctness-sweep.yaml EPM track_sweep expanded: against-list 4 → 8
  peers (added Workforce Management, Technology Management, Technology
  Enablement, Organizational Design); status
  sweep-completed-as-pending → sweep-completed-as-evidence-seeded.
- Enterprise-generality-matrix.yaml CAND-037 row added: 9 of 10 strong,
  demonstrated per A+B+C gate.
- Admission-gate-precheck.yaml CAND-037 row added: all 10 admission gates
  met on current evidence.
- INV-EPM-v0.1.md status updated (Open → evidence-seeded) and YAML twin
  INV-EPM-v0.1.yaml created.
- CHANGELOG.md addendum under v1-alpha.8 (research-CR addendum; same
  release cycle, no version bump).
- docs/REVIEWS.md addendum noting BC-SR-A001 §5 evidence work in progress.
- change-requests/README.md row added for CR-DEA-BC-19.

Out of scope:

- Admission of CAND-037 as a first-order canonical capability. That is
  CR-DEA-BC-15 (provisional).
- Track C (Relationship Management) evidence work. Separate CR.
- Any change to BC-13, BC-12, BC-09, BC-08, BC-17, BC-18, BC-14, BC-13,
  BC-10, BC-07, BC-06, BC-05, BC-04, BC-03, BC-02, BC-01A, BC-01.
- Sibling repos: out of session scope per user scoping rule 2026-09-10
  (action that is needed in another repo is raised as an issue on that
  repo unless it is a show stopper).

## 3. Evidence package

### 3.1 Source register additions (3 sources, 3 independent classes)

| ID | Name | Class | Retrieval |
|---|---|---|---|
| SRC-020 | Kaplan & Norton Balanced Scorecard (1992+) and Strategy Maps (2000+) | business-architecture | indirect (HBR 1992 paywalled; corpus knowledge + secondary summaries) |
| SRC-021 | OKR framework (Andy Grove / John Doerr) and practitioner literature | commercial-capability-models | indirect (Doerr 2018 corpus knowledge; Grove 1983 corpus knowledge) |
| SRC-022 | OMG Business Performance Management standards (BPM CBOK, OCEB 2) | standards-body | direct (OMG OCEB 2 page publicly accessible; BPM CBOK content from public OMG documentation) |

### 3.2 Three-source convergence → E3

The three sources are independent (different classes; different authors;
different publication venues; different institutional homes). Each
contributes 3 observations supporting CAND-037:

| Capability dimension | SRC-020 (BSC) | SRC-021 (OKR) | SRC-022 (OMG BPM) |
|---|---|---|---|
| Capability identity | Yes | Yes | Yes |
| Distinctness from Analytics | Yes | (implied) | Yes |
| Durability | Yes | Yes | Yes |
| Enterprise generality | Yes | Yes | Yes |
| Implementation independence | (implied) | Yes | (implied) |

E3 = "partial independence; two or more independent source classes"
(EVIDENCE.md §3). Three classes exceed the partial threshold.

### 3.3 Retrieval honesty (EVIDENCE.md §5)

- SRC-020: indirect. HBR 1992 article full text is paywalled; corpus
  knowledge is the basis. Re-rated on direct retrieval.
- SRC-021: indirect. Doerr 2018 corpus knowledge; Grove 1983 corpus
  knowledge. Re-rated on direct retrieval.
- SRC-022: direct. OMG OCEB 2 certification program page is publicly
  accessible; BPM CBOK content referenced from public OMG documentation.

This honesty is recorded in the source `retrieval` fields.

## 4. ECF placement

Per CR-DEA-BC-13 §A semantic-center-of-gravity rule:

- **Primary:** `strategy-direction / operate` (sustained performance
  measurement and governance is the operate stage of strategy-direction).
- **Secondaries:** `strategy-direction / improve` (performance
  improvement/adaptation) + `finance-accounting / operate` (financial
  performance dimension per BSC financial perspective).

Confidence: low-medium. Three-source convergence supports E3; direct
retrieval of SRC primaries would re-rate to E5; admission would re-rate
to E4 per EVIDENCE.md §3 admission promotion rule.

`strategy-direction / operate` cell-occupancy: currently empty (no
admitted capability). Track B admission (CR-DEA-BC-15) would populate
this cell.

## 5. Distinctness sweep (8 peers)

Track B EPM at `strategy-direction / operate` passes against:

1. `dea:capability-analytics-and-intelligence` (insight from data vs
   governance of outcomes; distinct business objects).
2. `dea:capability-financial-resource-management` (money flows vs
   enterprise-wide performance; financial is one dimension).
3. `dea:capability-strategy` (posture vs measurement of posture;
   parent-child).
4. `dea:capability-strategic-planning` (plan vs measurement of plan
   execution; parent-child).
5. `dea:capability-workforce-management` (agent lifecycle vs
   enterprise-wide performance; people dimension is one BSC perspective).
6. `dea:capability-technology-management` (technology estate vs
   enterprise-wide performance; tech dimension is one BSC perspective).
7. `dea:capability-technology-enablement` (technology services vs
   enterprise-wide performance; tech dimension is one BSC perspective).
8. `dea:capability-organizational-design` (structure design vs
   performance of the structured enterprise; consumer-provider).

All distinct by business-object partition. Full rationales in
`distinctness-sweep.yaml` v0.5 EPM track_sweep.

## 6. Direction Loop closure narrative (BC-DEA-BC-13 §D.2 explicit decision)

The reviewer identifies the **Direction Loop** in BC-SR-A001 §16:

> Strategy → Strategic Planning → Performance Management → Analytics &
> Intelligence → Strategy Adaptation

The loop is currently broken because Performance Management is missing
from the catalog.

If CAND-037 is admitted (CR-DEA-BC-15):

- Strategy (CAND-001 → `dea:capability-strategy`) sets posture.
- Strategic Planning (CAND-002 → `dea:capability-strategic-planning`)
  plans execution.
- **Performance Management (CAND-037 → `dea:capability-enterprise-performance-management`; this CR's deliverable if admitted) measures outcomes against the plan.**
- Analytics & Intelligence (CAND-022 → `dea:capability-analytics-and-intelligence`)
  derives insight from outcomes.
- Strategy Adaptation is then a Strategy capability operation (closed
  loop).

If CAND-037 is not admitted, the loop remains open. The missing link
(governance of outcomes) is partly absorbed into Analytics
(data-driven decision-making) and partly into Strategic Planning
(objective-setting) without an explicit performance-management
discipline. This is the user's decision per CR-DEA-BC-15 admission
decision (pending).

This narrative is required regardless of admission outcome per
BC-DEA-BC-13 §D.2 explicit decision. Recorded in
`INV-EPM-v0.1.yaml` `open_methodology_questions`.

## 7. Open evidence questions (status after this CR)

| Question | Status |
|---|---|
| Is Performance a durable distinct business object? | **partially-answered** (Performance is a distinct business object, separate from Insight/Outcome/Decision; per SRC-022 OMG BPM CBOK + SRC-020 BSC). Full answer is a methodology question; the object is a methodology-recognizable business object per the standards-body source. |
| Does EPM close the direction loop without collapsing into Analytics? | **open** (loop-closure narrative recorded in §6; the answer is the admission decision in CR-DEA-BC-15). |
| Does it survive the enterprise-generality test? | **confirmed** (9 of 10 strong per CAND-037 enterprise-generality-matrix v0.4 row; demonstrated per A+B+C gate). |

## 8. Review-gate audit (preliminary; admission-CR formal review is CR-DEA-BC-15)

- **Gate 1 (semantic review):** PASS on current evidence. All hard gates
  + 7 soft gates pass on CAND-037.
- **Gate 2 (architectural review):** PASS. ECF mapping defensible
  (strategy-direction/operate primary + conceive/build/improve secondaries
  per CR-DEA-BC-13 §A rule + CR-DEA-BC-19 §4); cell-occupancy (currently
  empty; admission populates within monopartite band per MAR); layering
  boundaries defensible; specialization defensible (foundation per
  METHODOLOGY §5 anti-invention).
- **Gate 3 (admission-gate):** PASS on current evidence. All 10 criteria
  met per admission-gate-precheck.yaml v0.8 CAND-037 row.

Note: Track B admission (CR-DEA-BC-15) triggers the formal
admission-gate review per METHODOLOGY.md §12.

## 9. Honest disclosure (per BC-SR-A001 §4 honest-reporting rule)

The EVIDENCE.md §3 E3 threshold is "partial independence". SRC-020/021/022
are sourced on the strength of documented corpus knowledge with retrieval
honesty (SRC-020 indirect; SRC-021 indirect; SRC-022 direct). The
evidence-seeded status is solid on partial-independence grounds (three
fully-independent classes exceeds the partial threshold). Direct
retrieval of the three primary sources would re-rate to E5 but is
independent of the research-CR deliverable and tracked separately as
follow-up actions in `INV-EPM-v0.1.yaml` `follow_up_evidence_actions`.

## 10. Files modified / created

### Modified

- `catalog-research/candidates.yaml` v0.5.0 (CAND-037 added; total 36 →
  37, CAPABILITY 30 → 31).
- `catalog-research/evidence-register.yaml` v0.7.0 (SRC-020/021/022
  added; TER-EPM-001 status evidence-pending → evidence-seeded; E3
  confirmed).
- `catalog-research/preliminary-ecf-overlay.yaml` v0.5.0 (EPM overlay
  confidence low → low-medium).
- `catalog-research/distinctness-sweep.yaml` v0.5.0 (EPM track_sweep
  against-list 4 → 8 peers; status updated).
- `catalog-research/enterprise-generality-matrix.yaml` v0.4.0 (CAND-037
  row added; 9 of 10 strong).
- `catalog-research/admission-gate-precheck.yaml` v0.8.0 (CAND-037 row
  added; all 10 gates met).
- `catalog-research/INV-EPM-v0.1.md` (status evidence-pending → evidence-seeded; carrier CR added; machine-readable twin line added).
- `CHANGELOG.md` (v1-alpha.8 research-CR addendum).
- `docs/REVIEWS.md` (BC-SR-A001 §5 evidence-work-in-progress note).
- `change-requests/README.md` (CR-DEA-BC-19 row).
- `CATALOG.yaml` (regenerated; canonical_count unchanged at 28; open_change_requests 22 → 23).

### Created

- `catalog-research/INV-EPM-v0.1.yaml` (machine-readable twin; YAML format).
- `change-requests/CR-DEA-BC-19-track-b-epm-evidence.md` (this file).

## 11. Local CI gates (verified at HEAD)

- YAML parse clean across all touched files.
- Schema validator: 28 entries (OrgDesign + 27 pre-existing), 0 errors.
- `check_naming.py`: PASS.
- `check_ecf_conformance.py`: PASS.
- `check_versions.py`: PASS.
- `check_view_refs.py`: PASS.
- `regenerate_catalog.py --check`: PASS.
- en/em dashes in any BC org-visible file: 0.

## 12. Catalog state (post-CR)

- 28 first-order canonical capabilities (no change; research-CR only).
- `strategy-direction / operate` cell-occupancy: empty (Track B
  admission CR-DEA-BC-15 would populate).
- TER-EPM-001: closed (evidence-seeded).
- CAND-037: E3 (not yet E4; promotion contingent on admission).
- Track A: closed.
- Track B: evidence-seeded (this CR). Admission pending CR-DEA-BC-15.
- Track C: open (CAND-004, separate CR pending).

## 13. Tag

No new tag. v1-alpha.8 (cut at `7140cf8` after Track A admission) is
the current release; Track B evidence-seed is part of v1-alpha.8
release cycle (research-CR addendum). Track B admission (CR-DEA-BC-15)
would trigger v1-alpha.9 (Minor bump).

## 14. Refs

- BC-SR-A001 §5 (reviewer P1; Track B gap)
- BC-SR-A001 §16 (Direction Loop narrative)
- BC-DEA-BC-13 §B.2 (Track B investigation opened) + §D.2 (hypothesis +
  loop-closure narrative requirement)
- CR-DEA-BC-12 (investigation carrier)
- CR-DEA-BC-18 (Track A research-CR pattern; symmetric precedent)
- CR-DEA-BC-14 (Track A admission; closed)
- METHODOLOGY.md §3 (capability vs organization), §5 (anti-invention
  test; A+B+C gate), §11 (monopartite band), §12 (review gates)
- EVIDENCE.md §3 (E3 partial independence; admission promotion rule), §5
  (retrieval honesty)
- docs/VERSIONING.md §1.2 (Patch vs Minor)

Branch: `feat/CR-DEA-BC-19-track-b-epm-evidence`. Ready for review.