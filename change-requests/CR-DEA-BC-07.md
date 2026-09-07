# CR-DEA-BC-07: Substrate-Neutral Re-Statement of the Workforce Capabilities

**Status**: Accepted
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-07
**Depends on**: CR-CATALOG-STRUCT-09 (v2.4.0 enum migration); dea-metaframework CR-ECF-007; dea-metaframework ADR-ECF-002
**Related**: CR-DEA-BC-02 (N-001 normalization decision); CR-DEA-BC-05 (versioning and change procedure)

## 1. What this CR is

`dea-metaframework` v2.4.0 renamed ECF Domain 3 from `PeopleAndOrganization` to
`AgencyAndOrganization`, driven by the Substrate Independence Stress Test
(ADR-ECF-002 §5): the domain must remain semantically valid whether the
enterprise's internal agents are biological (humans), artificial (AI systems,
autonomous software agents), or hybrid. The enum migration itself landed in
CR-CATALOG-STRUCT-09 (PR #47).

This CR reconciles the **content** of the two workforce capabilities with the
v2.4.0 rationale. The governing decision (eaojnr, 2026-09-07):

- **Names stay.** `Workforce Management` and `Workforce Planning` are correctly
  termed business capabilities; N-001 (CR-DEA-BC-02) stands. ECF grounding
  coordinates a capability; it does not rename it. A correctly termed business
  capability is not wrong because the domain vocabulary moved.
- **Content moves.** The capabilities manage **all agents, human and
  artificial**. Definitions, outcomes, and specialization boundaries are
  re-stated in substrate-neutral language so the entries survive the same
  Substrate Independence Stress Test the metaframework applied to itself.
- **Provenance stays.** Historical research artifacts (candidate register,
  normalization register, admission records, prior CRs, the v0.1 overlay, and
  the published `out/v1-alpha.0` snapshot) are not rewritten. The change lands
  at the repository tip; the ADR and CR trail carries the justification.

## 2. Scope decision

Three scopes were considered:

- **A. Entities only.** Smallest; leaves visuals and the canonical overlay out
  of step with the entries.
- **B. Entities + live visuals + canonical overlay (chosen).** Updates every
  surface a current reader consumes, without rewriting the historical research
  record.
- **C. Full bundle.** Would additionally edit historical artifacts
  (`candidates.yaml`, `normalization.yaml`, CR-DEA-BC-02 text). Rejected:
  those records exist for provenance.

Under scope B, each candidate surface was inspected for actual substrate claims
before editing:

| Surface | Finding | Action |
|---|---|---|
| `entities/.../dea:capability-workforce-management.yaml` | definition, outcome, specialization_boundary biologically loaded | re-stated (section 3) |
| `entities/.../dea:capability-workforce-planning.yaml` | definition, outcome, boundary, specialization_boundary biologically loaded | re-stated (section 3) |
| `visuals/v09-ecf-coverage-map.svg` | all seven domain axis labels stale (pre-v2.3.0 forms) | re-keyed (section 5) |
| `visuals/v02-candidate-universe-map.svg` | "People / Workforce Management" is the CAND-015 register name (provenance) | no change |
| `visuals/v04-capability-process-boundary.svg` | "Hire Employee" is a process naming example, not a substrate claim | no change |
| `visuals/v06-capability-business-object.svg` | uses kept names only ("Workforce Management", "Workforce") | no change |
| `catalog-research/ECF-OVERLAY-v0.2.md` | canonical overlay lists "People / Workforce Management" for the admitted capability | canonical name applied (section 4) |
| `catalog-research/ECF-OVERLAY-v0.1.md` | candidate-level shorthand matches the CAND-015 register name (provenance) | no change |
| `catalog-research/ecf-overlay-v0.2.yaml` | records are candidate-keyed; `name:` carries the register name (provenance) | no change |

## 3. Entry re-statements

### 3.1 `dea:capability-workforce-management` (version 1.0.0 -> 1.1.0)

| Field | Old | New |
|---|---|---|
| `definition` | The ability to acquire, develop, deploy, and release the enterprise's people. | The ability to acquire, develop, deploy, and release the enterprise's workforce of human and artificial agents. |
| `outcome` | The enterprise has the people it needs, developing, with deliberate entry and exit. | The enterprise has the agents it needs, human and artificial, developing, with deliberate entry and exit. |
| `specialization_boundary` | Workforce forms (employees, contractors, volunteers, uniformed service) are specialization; the ability to manage a workforce is not. | Workforce forms (employees, contractors, volunteers, uniformed service, AI agents, autonomous software agents, robotic systems, hybrid agent teams) are specialization; the ability to manage a workforce is not. |

`name`, `business_object` (`Workforce`), ECF coordinates, aliases, evidence,
provenance ladder, and `ecfConformance` blocks are unchanged. The alias list
retains `People Management` and `People / Workforce Management` as recorded
history of the N-001 decision.

### 3.2 `dea:capability-workforce-planning` (version 1.0.0 -> 1.1.0)

| Field | Old | New |
|---|---|---|
| `definition` | The ability to determine what workforce the enterprise will need and when. | The ability to determine what workforce, human and artificial, the enterprise will need and when. |
| `outcome` | A maintained view of future workforce demand and supply, feeding Workforce Management. | A maintained view of future demand and supply across the human and artificial workforce, feeding Workforce Management. |
| `boundary` | Plans the workforce; does not acquire, develop, or release people (Workforce Management). | Plans the workforce; does not acquire, develop, or release agents (Workforce Management). |
| `specialization_boundary` | Planning horizons and models vary by sector; the ability to plan a workforce does not. | Planning horizons, models, and the mix of human and artificial agents vary by sector; the ability to plan a workforce does not. |

`name`, `business_object` (`Workforce Plan`), ECF coordinates, evidence,
provenance ladder, and `ecfConformance` blocks are unchanged.

## 4. Canonical overlay correction

`catalog-research/ECF-OVERLAY-v0.2.md` (canonical, post-PR-32) listed the
admitted capability under its candidate name. The domain table row now reads:

| ECF Domain | Capabilities (primary coordinate) |
|---|---|
| `agency-organization` | Workforce Management (build); Workforce Planning (design) |

The N-001 citation ("People cluster -> Workforce Management (CAND-015)") is a
reference to the historical decision and is retained verbatim.

## 5. v09 coverage map label re-key (pre-existing drift fixed in passing)

`visuals/v09-ecf-coverage-map.svg` carried all seven domain axis labels in
their pre-v2.3.0 forms; only one was caught by the residual scan
(`people organization`). The full set is re-keyed to the v2.4.0 canonical
set, mirroring the `scripts/lib/grid.js` display-label fix recorded in
CR-CATALOG-STRUCT-09 §5:

| Old label (pre-v2.3.0) | New label (v2.4.0) |
|---|---|
| governance existence | governance existence (unchanged) |
| supply resources | strategy direction |
| people organization | agency organization |
| customer demand | party relationship |
| product offering | product value |
| operations delivery | operations enablement |
| finance value | finance accounting |

## 6. Bump rationale

- **Entry version**: 1.0.0 -> 1.1.0 on both entries. Per `docs/VERSIONING.md`
  §1.2, a substantive change to an entry's `definition` or `outcome` is a
  **minor** bump. The construct is unchanged (identity, business object, and
  ECF coordinates all stable); the re-statement is substantive because it
  changes what the definition claims.
- **Catalog version**: v1-alpha.0 -> **v1-alpha.1** (minor; VERSIONING §2.2:
  an existing entry's definition/outcome changed in a way that alters consumer
  understanding). Tag `v1-alpha.1` is cut at the merge commit of this PR by the
  catalog maintainer (VERSIONING §4 step 6).
- **Pins unchanged**: `metamodel_pin: 1.0.0`; `ecfConformance.profile:
  dea:ecf@1.0.0`. No schema change, no coordinate change, no identity change.

## 7. What is deliberately NOT in this CR

- No rename of either capability; N-001 stands.
- No rewrite of historical research artifacts: `candidates.yaml`,
  `normalization.yaml`, `RESEARCH-REPORT-v0.1.md`, `ECF-OVERLAY-v0.1.md`,
  admission records, and prior CRs keep their original wording as provenance.
- No edit to the published `out/v1-alpha.0` snapshot (immutable per
  CR-DEA-BC-05/06); the v1-alpha.1 publication follows from the tag.
- No change to `dependencies.yaml`: the self-reference label stays `v1-alpha`
  and the `ref` advances to `v1-alpha.1` when the tag exists.
- No new capabilities, no admissions, no specialization view changes.

## 8. Files changed

- 2 entity YAMLs (section 3).
- 1 visual: `visuals/v09-ecf-coverage-map.svg` (section 5).
- 1 research doc: `catalog-research/ECF-OVERLAY-v0.2.md` (section 4).
- `CATALOG.yaml` regenerated (`scripts/regenerate_catalog.py`).
- `CHANGELOG.md`: `[v1-alpha.1]` section.
- 1 new CR record: this file.

## 9. Verification

- `scripts/check_ecf_conformance.py`: PASS expected (coordinates unchanged).
- `scripts/check_versions.py`: PASS expected (semver entry versions; label
  `v1-alpha` count check unaffected at 26 entries).
- `scripts/check_view_refs.py`: PASS expected (no view changes).
- `scripts/check_catalog_index.py`: PASS expected (CATALOG.yaml regenerated).
- Entry schema validation (validate-entries workflow): PASS expected.
- Dash check: `grep -nP '[\x{2013}\x{2014}]'` clean on all touched files.
