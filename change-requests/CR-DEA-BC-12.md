# CR-DEA-BC-12: Submittal Review BC-SR-A001: Six High-Confidence ECF Re-Mappings, Three New Investigations, and Repo-Doc Drift Cleanup

**Status**: Landed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-10
**Landing commit**: `246e010a3765309d22269daee6484e091cfd3054` (PR #65, squash-merged)
**Tag**: `v1-alpha.5` (signed; cut at merge commit)
**Depends on**: CR-DEA-BC-01 (method, landed); CR-DEA-BC-02 (evidence investigation, landed); CR-DEA-BC-05 (versioning, landed); BC-SR-A001 (submittal review, filed 2026-09-10)
**Related**: dea-metaframework ADR-ECF-003 (Domain/Stage Orthogonality); dea-metaframework CR-ECF-008 (Domain 6 rename); dea-metamodel ADR-015
**Supersedes**: none
**Superseded by**: none

## 1. What this CR is

This CR is the carrier for the **substantive recommendations** of submittal
review [BC-SR-A001](../submittal-reviews/BC-SR-A001.md), filed 2026-09-10 against
the released v1-alpha.4 catalog (commit `570830a`). It bundles three kinds of
work:

1. **Six high-confidence ECF re-mappings** (§A): coordinate corrections where
   the existing placement contradicts the ECF domain definitions. Lands as a
   Minor-tier catalog bump (v1-alpha.4 → v1-alpha.5); affected entries advance
   1.0.0 → 1.1.0.
2. **Three new investigation tracks** (§B): for the P1 foundational gaps
   (Organizational Design, Enterprise Performance Management, Relationship
   Management). This CR opens the investigations; **no entity is admitted in
   this release.** Each investigation produces its own follow-on evidence
   package and, if the evidence supports it, its own admission CR.
3. **Repository / documentation drift cleanup** (§C): README entity-definition
   table status field, OpenDEAM version pin in the README.

The CR also seeds a new top-level folder `submittal-reviews/` and the cross-repo
submittal-review template. The folder is structurally inert (no schema, no
gate, no CI); it is a documentation surface, like `change-requests/` and
`catalog-research/`.

## 2. Why this is one CR, not four

The reviewer's §20 ("Recommended next step") proposes: first correct the six
high-confidence mappings, then investigate the three P1 gaps. That ordering is
correct, but the four pieces of work are inseparable in practice: the
submittal-review folder exists *because of* this CR; the investigations are
*opened by* this CR; the doc-drift cleanup is small enough to ride along;
and the ECF re-mappings share the same version-bump envelope.

Splitting into four CRs would multiply review surface for no architectural
benefit. The alternative (split ECF re-mapping off as BC-12, investigations as
BC-13/14/15) was considered and rejected: see the carrier-PR options in the
parent thread for the rejected alternatives.

## 3. Scope

### §A. Six high-confidence ECF re-mappings

All six corrections come from BC-SR-A001 §8-§11, §13. Each entry's id, name,
definition, business_object, and outcome are unchanged; only the ECF coordinate
(primary; secondaries preserved where they existed) and the `ecf_rationale`
field are updated.

| # | Entry | Current primary | Recommended primary | Review section | Confidence |
|---|---|---|---|---|---|
| 1 | dea:capability-strategy | `governance-existence / conceive` | `strategy-direction / conceive` (with `strategy-direction / improve` secondary) | §8.A | High |
| 2 | dea:capability-strategic-planning | `governance-existence / conceive` | `strategy-direction / conceive` (with `strategy-direction / improve` secondary) | §9 | High |
| 3 | dea:capability-asset-management | `strategy-direction / build` (with `operate`, `retire` secondaries) | `enablement-operations / build` (with `operate`, `improve`, `retire` secondaries) | §10 | High |
| 4 | dea:capability-facility-management | `strategy-direction / activate` (with `operate` secondary) | `enablement-operations / activate` (with `operate` secondary) | §11 | High |
| 5 | dea:capability-supplier-management | `strategy-direction / build` | `party-relationship / conceive` + `party-relationship / operate` (as secondaries, since `party-relationship` does not have a `build` stage) | §13 | High |
| 6 | dea:capability-sourcing-and-procurement | `strategy-direction / build` | `enablement-operations / build` (with `strategy-direction / conceive` and `strategy-direction / design` as secondaries for "strategic sourcing") | §13 | High |

**Cross-cutting note:** correction #5 (Supplier Management) sits squarely on
BC-SR-A001 §6's broader argument for a generic Relationship Management parent
cap. Investigation track C (§B.3 below) will determine whether Supplier
Management should become a specialization of a future Relationship Management
cap, or stand on its own. The correction in this CR is coordinate-only and
makes no commitment either way; track C's outcome will be reflected in a
follow-on admission/migration CR.

**Not in this CR** (deliberately excluded):

- **Technology Management** re-mapping. BC-SR-A001 §12 is medium-confidence
  (the reviewer recommends a formal boundary decision before moving). This CR
  does NOT move Technology Management. See §B.4 below for the deferred work.
- **ECF mapping rule refinement** ("semantic center of gravity" vs "earliest
  initiation"). BC-SR-A001 §14. This is a method-level change and belongs in a
  follow-on method-CR (CR-DEA-BC-13, to be opened after this lands). The
  re-mappings in §A are performed using the **current** method rule, with the
  reviewer's reasoning recorded in each entry's `ecf_rationale` field; the
  method-CR can subsequently ratify the change in rule and apply it
  retroactively.

### §B. Three new investigation tracks

Each track opens a **research-led evidence investigation** under
`catalog-research/`. None of them admits a new entity in this CR. Each track
produces an evidence package; if the evidence supports admission, a separate
admission CR is opened, gating on the catalog's existing admission gate
(`METHODOLOGY.md` §12).

#### §B.1 Investigation Track A: Organizational Design

**Source:** BC-SR-A001 §4 (reviewer P1).

**Question to answer:** Is Organizational Design a distinct first-order
capability that survives the catalog's admission gate?

**Hypothesis (from the reviewer):** *The ability to design the enterprise's
organizational structures, roles, authorities, and coordination patterns
through which agency is organized.* ECF placement hypothesis:
`agency-organization / design` (with `agency-organization / conceive` and
`agency-organization / build` as secondaries).

**Investigation artifact:** `catalog-research/INV-ORGDESIGN-v0.1.md` plus a
machine-readable twin. Mirrors the CR-DEA-BC-02 artifact pattern
(`admission-gate-precheck.yaml`, `enterprise-generality-matrix.yaml`).

**Deliverables when the investigation reports back:**
- Candidate record (id, name, definition, business_object, outcome).
- Evidence register entry (E0..E5 ratings on the catalog's evidence ladder).
- ECF overlay hypothesis with rationale.
- Distinctness sweep against the existing 26.
- Admission-gate pre-check.

**Go/no-go decision** rests on the catalog owner applying the §12 review
gates. Investigation has no deadline; parked until evidence package is
substantial.

#### §B.2 Investigation Track B: Enterprise Performance Management

**Source:** BC-SR-A001 §5 (reviewer P1).

**Question to answer:** Is Enterprise Performance Management distinct from
Analytics & Intelligence, and does it close the Direction loop that the
reviewer identifies in §16 (Strategy → Planning → Performance → Insight →
Adaptation → Change)?

**Hypothesis (from the reviewer):** *The ability to define, monitor, evaluate,
and improve enterprise performance against intended objectives and targets.*
ECF placement hypothesis: `strategy-direction / operate` (with
`strategy-direction / improve`, `finance-accounting / operate` as secondaries).

**Investigation artifact:** `catalog-research/INV-EPM-v0.1.md` plus twin.

**Deliverables when the investigation reports back:** same as §B.1, plus an
explicit boundary statement against Analytics & Intelligence
(`dea:capability-analytics-and-intelligence`) and any existing capabilities in
the `strategy-direction` cells.

#### §B.3 Investigation Track C: Relationship Management

**Source:** BC-SR-A001 §6 (reviewer P1-P2).

**Question to answer:** Is there a generic Relationship Management
first-order capability, of which Customer/Supplier/Partner Management are
specializations? Or are the role-specific capabilities already MECE-complete
and the generic parent is unnecessary abstraction?

**Hypothesis (from the reviewer):** *The ability to establish, govern, develop,
and terminate relationships with external parties across their lifecycle.*
ECF placement hypothesis: `party-relationship / conceive` (with `operate`,
`improve` secondaries).

**Investigation artifact:** `catalog-research/INV-RELMGMT-v0.1.md` plus twin.

**Deliverables when the investigation reports back:** same as §B.1, plus a
boundary statement against each of the three existing role-specific caps
(Customer, Supplier, Partner) and a decision record on whether the generic
parent is admitted, deferred, or rejected as abstraction.

**Note:** the ECF re-mapping of Supplier Management in §A.5 above does not
pre-judge this investigation. Track C may conclude that a generic parent is
not warranted and Supplier Management stands on its own.

#### §B.4 Deferred items (not investigations in this CR)

- **Knowledge Management** (§7 P2). The reviewer's own caveat stands; revisit
  after track A reports back, because `agency-organization / improve` is the
  most likely placement.
- **Service Management / Quality Management / Stakeholder Management /
  Enterprise Architecture Management** (§17 P2-P3). No evidence. Revisit after
  the three P1 investigations close.
- **Technology Management boundary** (§12). Method-level decision; follow-on
  method-CR (CR-DEA-BC-13).
- **ECF mapping rule refinement** (§14). Method-level; same CR-DEA-BC-13.

### §C. Repository / documentation drift cleanup

| # | Item | Source | Action |
|---|---|---|---|
| 1 | README entity-definition table: `Catalog Status: planned` while catalog is populated | BC-SR-A001 §19 | Update `README.md` Entity Definition table status field to `populated`. |
| 2 | README: OpenDEAM version pin (v0.2.1) inconsistent with catalog's metamodel pin (1.0.0) and ECF contract pin (1.0.0) | BC-SR-A001 §19 | Add an explicit `Metamodel pin: 1.0.0` and `ECF conformance contract: 1.0.0` line in the README Status section; resolve the v0.2.1 reference (decide whether to drop it, replace it, or document it as a historical pointer). |

## 4. Out of scope

- No new entities admitted (the three investigations may admit entities in
  follow-on CRs; none do in this CR).
- No schema changes (`schemas/entity.schema.json` is unchanged; the re-mappings
  use existing enum values).
- No CI workflow changes.
- No changes to TAXONOMY, METHODOLOGY, EVIDENCE, or GOVERNANCE documents in
  this CR. The "semantic center of gravity" rule refinement (§14) belongs in
  CR-DEA-BC-13.
- No changes to the existing 20 entities that are NOT in the §A table.

## 5. Files changed

- **5 entity YAMLs** with primary coordinate re-mapping: strategy,
  strategic-planning, asset-management, facility-management,
  supplier-management, sourcing-and-procurement. (Six re-mappings, but
  strategic-planning and supplier-management may share an edit if they
  currently sit in adjacent files: verified at implementation time.)
- **Each of those 5 YAMLs**: `ecf.primary` updated; `ecf.secondary` array
  edited where applicable; `ecf_rationale` field updated to cite BC-SR-A001
  §X and quote the relevant ECF domain definition.
- **README.md**: entity-definition table status field; OpenDEAM version pin
  clarification.
- **submittal-reviews/** (new folder): `README.md`, `TEMPLATE.md`, `BC-SR-A001.md`.
- **docs/REVIEWS.md** (new): per-release submittal review commentary.
- **change-requests/CR-DEA-BC-12.md** (this file).
- **change-requests/README.md**: row added for CR-DEA-BC-12.
- **CHANGELOG.md**: `[v1-alpha.5]` section added.

## 6. Version bump

Per `docs/VERSIONING.md` §2.2 (Minor): *"substantive change to one entry's
definition, business_object, outcome, or ECF primary/secondary coordinates"*.

- **Catalog label:** v1-alpha.4 → v1-alpha.5 (Minor).
- **Affected entry versions:** 6 entries advance 1.0.0 → 1.1.0
  (per-entity Minor for coordinate changes).
- **Unaffected entries:** 20 entries remain at 1.0.0.
- **Specialization views:** unchanged. The MCSP Telecom view is not affected
  by these re-mappings.

## 7. Acceptance criteria

- [ ] Each of the 6 entity YAMLs in §A has the recommended primary coordinate.
- [ ] Each of those 6 YAMLs has its `ecf_rationale` field updated to cite the
      BC-SR-A001 section and quote the relevant ECF domain definition.
- [ ] `scripts/check_ecf_conformance.py` passes (`PASS: 26 entries + MCSP view
      conform to ECF Conformance Gate`).
- [ ] `scripts/check_naming.py` shows no NEW warnings beyond the existing 5
      advisory warnings (existing taxonomy-semantic warnings are unchanged
      because no names or definitions change).
- [ ] `scripts/check_versions.py` passes (`PASS: 26 entries conform to
      CR-DEA-BC-05 version discipline`).
- [ ] `submittal-reviews/` folder contains `README.md`, `TEMPLATE.md`,
      `BC-SR-A001.md`.
- [ ] `docs/REVIEWS.md` exists with the v1-alpha.5 entry.
- [ ] README entity-definition table `Catalog Status` is `populated`.
- [ ] README OpenDEAM / metamodel / ECF contract version pins are
      internally consistent.
- [ ] Investigation-track stubs (`catalog-research/INV-ORGDESIGN-v0.1.md`,
      `INV-EPM-v0.1.md`, `INV-RELMGMT-v0.1.md`) exist with the Question,
      Hypothesis, and Deliverables sections, even if the evidence work is
      incomplete. The stubs establish the track and prevent it from being
      forgotten.
- [ ] `change-requests/README.md` has the CR-DEA-BC-12 row.
- [ ] `CHANGELOG.md` has the `[v1-alpha.5]` section with a Submittal Reviews
      pointer.

## 8. Tag

`v1-alpha.5` is cut at this CR's merge commit per CR-DEA-BC-05. Tag signing:
use the project GPG signing setup; see the standing protocol.

## 9. Follow-on (not in this CR)

| Follow-on CR | Scope | Source |
|---|---|---|
| CR-DEA-BC-13 | Method-CR: refined ECF primary-coordinate rule ("semantic center of gravity"); applies retroactively to the 6 re-mappings in §A. | BC-SR-A001 §14 |
| CR-DEA-BC-14 (provisional) | Investigation track A admission CR (only if track A evidence supports it) | BC-SR-A001 §4 |
| CR-DEA-BC-15 (provisional) | Investigation track B admission CR (only if track B evidence supports it) | BC-SR-A001 §5 |
| CR-DEA-BC-16 (provisional) | Investigation track C admission CR (only if track C evidence supports it) | BC-SR-A001 §6 |
| CR-DEA-BC-17 (provisional) | Technology Management boundary decision (only if §14 rule refinement creates new clarity) | BC-SR-A001 §12 |
