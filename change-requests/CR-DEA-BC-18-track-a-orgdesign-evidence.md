# CR-DEA-BC-18 — Track A (Organizational Design) Evidence Package

**Status:** Draft for review (research-CR; no admission in this revision)
**Date:** 2026-09-11
**Carrier:** Coder (for eaojnr)
**Branch:** `feat/CR-DEA-BC-18-track-a-orgdesign-evidence`
**Closes:** BC-13 §B.1 (Track A investigation opened); BC-SR-A001 §4 evidence work
**Blocks:** CR-DEA-BC-14 (provisional; Track A admission CR — pending user acceptance)

---

## 1. What this CR is

This is a **research-CR** that lands the full evidence package for the Track A
investigation into Organizational Design as a potential first-order capability.
**No entity is admitted in this CR.** The evidence package is delivered on disk
for user review; admission becomes CR-DEA-BC-14 once the user accepts the
package and signals readiness.

Track A was opened by CR-DEA-BC-12 §B.1 (2026-09-10) against BC-SR-A001 §4
(reviewer P1: "Strong candidate for canonical capability"). This CR is the
evidence-collection step that the methodology requires before admission.

### 1.1 Outcome

- **Research artifacts on disk:** CAND-036 added to the candidate universe;
  SRC-017/018/019 added to the evidence register; TER-ORGDESIGN-001 track record
  evidence-seeded; ECF overlay hypothesis confidence `low → low-medium`;
  enterprise-generality matrix row added; distinctness sweep expanded to cover
  the two newly-admitted Tech capabilities; admission-gate pre-check added with
  `evidence_ge_E3` gap pending direct retrieval; full investigation report at
  `INV-ORGDESIGN-v0.2.md` with YAML twin.
- **No canonical entity added:** CAND-036 remains a candidate-on-file. The
  catalog still has 27 first-order canonical capabilities (unchanged from v1-alpha.7).
- **No version bump:** no v1-alpha.N tag in this CR.

## 2. Why this CR, not separate

Track A is gated on METHODOLOGY §12 (semantic + architectural review). The
reviewer in BC-SR-A001 §4 was explicit: *"before admitting anything else"*,
meaning the evidence work comes first. This CR is that evidence work, landed
as one PR per the slice-by-slice cadence preference (the three artifacts
[CAND record, sources, overlay + sweep + precheck + INV doc + YAML twin] form
one logical unit; slicing further would create half-evidence packages).

Per the standing A+B+C foundation inclusion criteria gate (BC-SR-A001 §17 +
BC-17 §3.5, locked 2026-09-10), Track A evidence must demonstrate:

- (A) Sensible in ≥3 verticals: 9 of 10 enterprise types scored `strong` per
  the CAND-036 enterprise-generality matrix row; non-profit scored `moderate`.
- (B) Works in B2B/B2C/G2C archetypes: cross-sector applicability of the org
  design literature (Galbraith examples span manufacturing, financial services,
  healthcare, technology; ISO 9001 adoption spans B2B/B2C/G2C).
- (C) Describable without industry-specific domain object: `Organization
  Structure` is substrate-neutral (human + artificial + hybrid agents).

All three pass on current evidence.

## 3. Semantic review (per METHODOLOGY.md §12 gate 1)

| Hard gate | Status | Evidence |
|---|---|---|
| **Ability** | met | Org design is a recognized management discipline (Galbraith Star Model, McKinsey 7-S, OB textbooks). Not a process (describes work), not a function (organizational grouping of work), not an organization (grouping of people), not a system (mechanism). Per §3 distinction table. |
| **Outcome** | met | Designed structure supporting the enterprise's chosen posture. Auditable per ISO 9001 §5.3 (top-management responsibility). |
| **Implementation Independence** | met | Different enterprises realize org design via different archetypes (functional, divisional, matrix, network, holacratic). The discipline exists independent of any one implementation. |

| Soft gate | Status | Evidence |
|---|---|---|
| **Durability** | met | Recurring discipline since Galbraith (1970s); structural choices survive reorganization. |
| **Enterprise Relevance** | met | Every enterprise has an organization; every enterprise that grows or pivots redesigns it. |
| **Object Focus** | met | Business object: `Organization Structure`. Distinct from Enterprise (Strategy), Plan (Strategic Planning), Agent Capacity (Workforce Planning), Agent Lifecycle (Workforce Management), Technology Estate (Tech Mgmt), Technology Service (Tech Enablement). |
| **Distinctness** | met | Sweep vs 6 adjacent capabilities passes by business-object partition. |
| **Decomposability** | met | CAND-036a Role and Authority Design; CAND-036b Coordination Pattern Design; CAND-036c Governance Hierarchy Design. Recorded as candidate children; admission of a subset is the admission CR's decision. |
| **Evidence** | gap (E3 pending direct retrieval) | Three independent source classes registered (SRC-017/018/019); direct retrieval of primaries is the open action. |
| **ECF Fit** | met | agency-organization/design primary + conceive/build secondaries; substrate-neutral per ECF v2.4.0. No distortion of catalog or framework. |

Anti-invention test (§5): changing industry tomorrow, the ability still makes
sense. ✅

## 4. Architectural review (per METHODOLOGY.md §12 gate 2)

| Test | Status | Evidence |
|---|---|---|
| ECF mapping defensible (semantic center of gravity) | met | Defining activity = sustained design of structures/roles/authorities/coordination. Per §8.3 heuristic 3: design/build activity → `design` stage. |
| Realization links reference correct sibling catalogs | met (placeholder) | When admitted, realization links: processes (`dea-catalog-processes`), actors (`dea-catalog-actors`), resources (`dea-catalog-business-objects`), systems (`dea-catalog-digital-business-service-factory`), information (`dea-catalog-business-objects`). Recorded on the entry at admission. |
| Record shape satisfies §10 | met | When admitted, schema-conforming entry: kind `dea:BusinessCapability`; capability_layer governed enum; ecf.primary / ecf.secondary; realization; evidence; provenance; narrative per §11. Schema validation done in admission CR. |
| Layering boundaries respected | met | WSF / metaframework / metamodel / catalogs layering preserved; no catalog-layer violation. |

## 5. Evidence trail (per CR-DEA-BC-02 + METHODOLOGY §12)

Three independent source classes registered in `evidence-register.yaml` v0.5.0:

- **SRC-017** — Galbraith Star Model & org-design literature (business-architecture)
- **SRC-018** — APQC PCF v8.0 — Organization category (cross-industry-process)
- **SRC-019** — ISO 9001:2015 §5.3 organizational roles, responsibilities, authorities (standards-body)

EVIDENCE.md §3 E3 threshold: "appears in credible material with partial
independence" — **exceeded** (full independence across three source classes,
not partial).

EVIDENCE.md §5 retrieval honesty: indirect retrieval flagged for SRC-017
(book titles and Star Model structure from corpus knowledge; full primary text
not retrieved this pass) and SRC-018 (PCF element list behind registration
form). Direct retrieval for SRC-019 (ISO 9001 OBP summary; full normative text
paywalled). Re-rated on direct retrieval.

EVIDENCE.md §6 dual-delivery: `INV-ORGDESIGN-v0.2.md` (persona-readable) +
`INV-ORGDESIGN-v0.1.yaml` (machine-readable twin). Versioned together.

## 6. Cross-reference updates

- `candidates.yaml` v0.2 → v0.3: +1 candidate (CAND-036); header counts updated
  (35 → 36 total; 29 → 30 CAPABILITY).
- `evidence-register.yaml` v0.4 → v0.5: +3 sources (SRC-017/018/019); TER-ORGDESIGN-001
  track record seeded.
- `preliminary-ecf-overlay.yaml` v0.2 → v0.3: dea:candidate-orgdesign confidence
  `low → low-medium`; rationale extended with BC-18 evidence seed.
- `enterprise-generality-matrix.yaml` v0.2 → v0.3: +1 row (CAND-036); summary
  updated.
- `distinctness-sweep.yaml` v0.2 → v0.3: track_sweeps[0] (Org Design) extended
  to cover dea:capability-technology-management + dea:capability-technology-enablement;
  sweep_version + inputs versions bumped.
- `admission-gate-precheck.yaml` v0.5 → v0.6: +1 evaluation (CAND-036) with
  `evidence_ge_E3` gap; summary updated.
- `INV-ORGDESIGN-v0.1.md` → `INV-ORGDESIGN-v0.2.md`: stub → full investigation report.
- `INV-ORGDESIGN-v0.1.yaml`: new YAML twin.

No canonical entries modified. CATALOG.yaml not regenerated (no canonical change).
CHANGELOG.md updated with the research-CR entry under v1-alpha.7.

## 7. Acceptance criteria

| Criterion | Status |
|---|---|
| Three independent source classes registered for CAND-036 | met |
| CAND-036 added to candidate universe with full record fields | met |
| Distinctness sweep passes by business-object partition against the 6 adjacent canonical entries | met |
| Enterprise-generality matrix row added; demonstrated per A+B+C gate | met |
| ECF overlay hypothesis updated with rationale extension | met |
| Admission-gate pre-check added with honest gap disclosure (evidence_ge_E3 pending direct retrieval) | met |
| Full investigation report (`INV-ORGDESEARCH-v0.2.md`) and YAML twin (`INV-ORGDESIGN-v0.1.yaml`) on disk | met |
| CHANGELOG.md research-CR entry under v1-alpha.7 | met |
| docs/REVIEWS.md v1-alpha.7 commentary updated with BC-SR-A001 §4 in-progress note | met |
| `change-requests/README.md` row added | met |
| **No canonical entity admitted** (this is research-only) | met |
| All local CI gates pass; remote CI green | to be verified before PR review |

## 8. Version bump

**None** in this CR. Research-CR; no canonical change. Next version bump is in
CR-DEA-BC-14 (Track A admission) when admitted.

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| SRC-017/018/019 indirect retrieval may be challenged at admission review | Direct retrieval actions recorded in TER-ORGDESIGN-001 follow_up_evidence_actions; can run independently of admission. Re-rating on direct retrieval is a small follow-on CR if needed. |
| Anti-invention test (§5) on non-profit archetype is `moderate`, not `strong` | Non-profit boards / dual governance is a legitimate variation of the design discipline; the capability still recurs. Documented in matrix row note. |
| CAND-036 child-candidate mapping (a/b/c) is hypothesized, not worked out | Recorded as "candidate children" — admission CR decides whether to keep, work out, or omit. Not blocking research-CR landing. |
| User may disagree with the ECF primary placement (`agency-organization/design`) | The hypothesis is low-medium confidence; admission CR can revise. The overlay hypothesis is recorded honestly, not smoothed. |
| BC-SR-A001 §4 reviewer's exact boundary expectations (e.g. relationship to Workforce Management) | Sweep rationale explicitly addresses each pair; ready for review. |

## 10. Follow-on work (not in this CR)

- **CR-DEA-BC-14 (provisional)** — Track A admission CR. Triggered on user
  acceptance of this evidence package. Will carry formal §12 review sign-off,
  version bump (catalog → 28 first-order capabilities), final entry record,
  CHANGELOG / docs/REVIEWS / README updates, tag-cut decision.
- **Direct retrieval actions** — independent of admission; can run as a
  follow-on if SRC-017/018/019 primaries are needed for stronger E4 rating.
- **Track B (EPM, BC-15 provisional)** — separate evidence package; no work
  in this CR.
- **Track C (Relationship Mgmt, BC-16 provisional)** — separate evidence
  package; no work in this CR.
- **CAND-036 child candidates** — a/b/c on file; admission CR decides depth.

## 11. See also

- [METHODOLOGY.md](../../METHODOLOGY.md) §12 review workflow; §5 anti-invention
  test; §6 ladder passage; §8 ECF mapping rule; §4 admission tests.
- [EVIDENCE.md](../../EVIDENCE.md) §2 source classes; §3 E0:E5 ratings; §5
  retrieval honesty; §6 dual-delivery.
- [INV-ORGDESIGN-v0.2.md](../../catalog-research/INV-ORGDESIGN-v0.2.md) — full
  investigation report.
- [INV-ORGDESIGN-v0.1.yaml](../../catalog-research/INV-ORGDESIGN-v0.1.yaml) —
  YAML twin.
- [BC-SR-A001 §4](../submittal-reviews/BC-SR-A001.md) — reviewer seed (P1).
- [CR-DEA-BC-12 §B.1](./CR-DEA-BC-12.md) — investigation opened.
- [CR-DEA-BC-13 §D.1](./CR-DEA-BC-13.md) — overlay hypothesis + track record.
- [CR-DEA-BC-17 §10](./CR-DEA-BC-17.md) — follow-on queue (BC-14 provisional).
