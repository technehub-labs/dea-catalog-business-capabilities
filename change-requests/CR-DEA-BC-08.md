# CR-DEA-BC-08: Coordinate Technology Management - Resolve N-006

**Status**: Accepted
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-08
**Depends on**: CR-DEA-BC-02 (N-006 normalization decision); CR-DEA-BC-04 (overlay v0.2); CR-ECF-CG-003 (catalog conformance gate)
**Related**: CR-DEA-BC-07 (substrate-neutral re-statement); `dea-metaframework` CR-ECF-006 (Strategy & Direction rename from Supply & Resources)

## 1. What this CR is

CR-DEA-BC-02 §N-006 recorded that Technology Management (object: Technology;
outcome: deliberate, funded, lifecycle-managed stewardship of the technology
estate) carries no ECF coordinate, on the rationale that "no ECF domain carries
technology."

That rationale is incorrect against the framework's own canonical grounding
(`dea-metaframework/framework/domain-grounding.md` §3.6 and §3.2):

- §3.6 (Operations & Enablement) names **Technology Enablement** as an internal
  MECE sub-concern, but immediately clarifies: "Technology, platforms, and
  physical assets are positioned as enablers of execution, **not as ends in
  themselves**." The framework is explicit that technology-as-an-enabler is
  owned by Operations; technology-as-an-estate (a manageable subject with its
  own lifecycle) is not.

- §3.2 (Strategy & Direction) records the prior "Supply & Resources" domain
  was removed *because* resource stewardship at the strategic level belongs in
  S&D: "physical resources moved to Operations & Enablement (as enablers);
  financial resources moved to Finance & Accounting; human resources stay in
  Agency & Organization." The vacated "persists (as deliberate steering)"
  axiom slot maps cleanly to Strategy & Direction.

The peer capability `dea:capability-asset-management` already encodes the
pattern in its boundary statement: "Stewards assets; does not manage money
(Financial Management), **technology as an estate (Technology Management)**, or
facilities specifically (Facility Management)." Asset Management (object:
Asset, outcome: assets deliver value over their lifecycle) lives in
`strategy-direction × build` for exactly this reason. Technology Management is
the technology-estate peer.

This CR resolves N-006 by placing Technology Management at
`strategy-direction × build`, parallel to Asset Management, and supersedes
the N-006 held-unmapped state with a normal canonical mapping. N-006R is the
new normalization identifier (resolved, not withdrawn).

## 2. Scope decision

Three scopes were considered:

- **A. Entities + overlay + provenance docs only (chosen).** Updates the
  entity YAML, the canonical overlay (markdown + yaml), the BC-02 closeout's
  open-item list, the admission-review R-004 entry, and the change-requests
  index. Does not rewrite historical research artifacts (`candidates.yaml`,
  `normalization.yaml`, `RESEARCH-REPORT-v0.1.md`, `ECF-OVERLAY-v0.1.md`,
  prior CR text). The provenance trail carries the rationale.
- **B. Full bundle.** Would also rewrite the historical N-006 / R-004
  references inside `candidates.yaml`, `normalization.yaml`, and the
  `preliminary-ecf-overlay.yaml`. Rejected: those records exist for
  provenance; the correction is in the canonical overlay and the new CR.
- **C. Entities only.** Smallest; leaves overlay, change-requests index, and
  BC-02 closeout open items out of step. Rejected: the catalog ships with
  internal inconsistency if the overlay still says "unmapped."

Under scope A, each candidate surface was inspected before editing:

| Surface | Finding | Action |
|---|---|---|
| `entities/.../dea:capability-technology-management.yaml` | `ecf.held_unmapped: true`; `ecfConformance.affiliation: held-unmapped`; N-006 rationale note | flip primary to `strategy-direction × build`; drop `held_unmapped`; add canonical reference block; bump 1.0.0 → 1.1.0 |
| `catalog-research/ECF-OVERLAY-v0.2.md` | Headline says "1 held-unmapped"; coverage map row puts TM under `<unmapped>`; carried-forward list still lists CAND-019 N-006 | rewrite headline; move TM to `strategy-direction` row; strike CAND-019 from carried-forward |
| `catalog-research/ecf-overlay-v0.2.yaml` | `CAND-019.primary: null`, `status: admitted-with-held-unmapped`; `held_unmapped: [CAND-019]` in admission_summary | primary → `strategy-direction × build`; status → `admitted`; drop `held_unmapped_rationale` |
| `catalog-research/ADMISSION-REVIEW-v0.1.md` | R-004 row says "N-006 resolved: ... ECF legitimately absent" | strike R-004; add footnote that N-006 is superseded by N-006R (CR-DEA-BC-08) |
| `catalog-research/BC-02-CLOSEOUT.md` | Open item #5 "N-006 carried question: Technology Management as domain capability vs cross-cutting concern" | strike open item #5 |
| `catalog-research/ECF-OVERLAY-v0.1.md` | Historical preliminary overlay (provenance) | no change |
| `catalog-research/preliminary-ecf-overlay.yaml` | Historical preliminary overlay (provenance) | no change |
| `catalog-research/candidates.yaml` | Historical candidate register (provenance) | no change |
| `catalog-research/normalization.yaml` | Historical normalization register (provenance) | no change |
| `visuals/v09-ecf-coverage-map.svg` | Has a held-unmapped footnote for CAND-019 | re-render with the cell at `strategy-direction × build` populated and the unmapped footnote removed |
| `change-requests/README.md` | New BC-08 row | add |
| `CHANGELOG.md` | New `v1-alpha.2` section | add |

## 3. Entry re-statement

### 3.1 `dea:capability-technology-management` (version 1.0.0 → 1.1.0)

| Field | Old | New |
|---|---|---|
| `version` | 1.0.0 | 1.1.0 |
| `ecf` | `{ held_unmapped: true, note: "..." }` | `{ primary: { domain: strategy-direction, stage: build }, secondary: [ { domain: strategy-direction, stage: operate }, { domain: strategy-direction, stage: improve } ] }` |
| `ecfConformance.affiliation` | held-unmapped | mapped |
| `ecfConformance.rationaleRef` | N-006 | N-006R (N-006 resolved) |
| `ecfConformance.canonicalReferences` | `[]` | 3 entries: primary, 2 secondaries - all `strategy-direction` x { build, operate, improve } |
| `ecfConformance.extensions` | includes `held-unmapped` classification-state | replaced with `multiple-contextual-coordinates` rationale + kebab-case display vocabulary (matching peer entries) |
| `evidence.rationale` | ends "...distinctness-sweep, admission-gate-closeout)." | extended: "Enterprise-generality demonstrated at E4; N-006 resolved at BC-08: technology is an estate, not an enabler of execution; stewardship of the estate belongs in Strategy & Direction, parallel to Asset Management and Facility Management. Evidence trail in docs/research (evidence-register, enterprise-generality-matrix, distinctness-sweep, admission-gate-closeout)." |
| `why_capability` | ends "...ECF legitimately absent: no ECF domain carries technology (an L5 layer concern)." | extended: "E4; N-006R resolved at BC-08: a business capability whose object is Technology, not a cross-cutting concern. The technology *estate* is a stable subject with lifecycle; stewardship of the estate is the deliberate direction of an enterprise resource, which is the semantic anchor of Strategy & Direction. Distinct from Operations & Enablement §3.6 sub-concern 'Technology Enablement', which positions technology as a means of execution, not as an end." |
| `ecf_rationale` | "R-004: held unmapped with recorded reason; the section 38 legitimately-absent clause applies." | "N-006R / BC-08: strategy-direction × build. Earliest legitimate initiation of technology-estate stewardship is build (the enterprise acquires/stands-up technology here, just as it does with assets); secondaries record legitimate participation at operate (running the estate) and improve (evolving it). Mirrors the Asset Management placement." |
| `boundary` | "Stewards the technology estate; does not manage the information it carries (Information Management) or operate delivery (Operations)." | unchanged (the boundary is correct; the ECF affiliation was the missing piece) |
| `non_examples` | "An IT department (an organization)"; "A specific platform (a system)" | unchanged |
| `specialization_boundary` | "Technology domains (network, cloud, OT) are specialization of the estate, not of the ability." | unchanged |
| `aliases` | (none recorded) | unchanged |
| `metamodel_pin` | 1.0.0 | unchanged |

`name`, `business_object` (Technology), and `capability_layer` (support) are
unchanged. `related_capabilities` (`dea:capability-information-management`) is
unchanged.

## 4. Canonical overlay corrections

### 4.1 `catalog-research/ECF-OVERLAY-v0.2.md`

Headline rewrites:
- `1 held-unmapped` → `0 held-unmapped`
- `14 distinct primary coordinates referenced out of 49` → `15 distinct primary coordinates referenced out of 49`

Coverage-map table:
- `<unmapped> | Technology Management (<unmapped>)` → `strategy-direction | Asset Management (build); Facility Management (activate); Sourcing and Procurement (build); Supplier Management (build); **Technology Management (build)**`

"N-006 carried question" line in `## Carried forward from v0.1` → removed.
Footnote about N-006 at the bottom of the reading section → updated to
reference N-006R resolution.

### 4.2 `catalog-research/ecf-overlay-v0.2.yaml`

- `applied_decisions.normalization.N-006` → `N-006R (N-006 resolved by CR-DEA-BC-08; technology is an estate, not an enabler of execution; stewardship lives in Strategy & Direction, parallel to Asset Management)`
- `review_decisions[].id == R-004` → struck (decision was superseded by N-006R)
- `overlays[]` CAND-019 entry: `primary: { domain: strategy-direction, stage: build }`; `secondary: [strategy-direction.operate, strategy-direction.improve]`; `confidence: high`; `status: admitted`; drop `held_unmapped_rationale`
- `coverage.canonical_coordinates_referenced` adds `strategy-direction.build` (already present, count unchanged at 27 → 28 referenced)
- `admission_summary.held_unmapped: []`; `admitted_total: 26` (unchanged - was already 26)
- `applied_decisions.normalization.N-006` entry is rewritten as `N-006R`
- `empty_cells_legitimate` block: unchanged (the BC-08 move does not affect the legitimate-empty-cell list; `strategy-direction × build` was already populated)

### 4.3 Provenance strikes

- `catalog-research/ADMISSION-REVIEW-v0.1.md` R-004 row: marked `[superseded by N-006R; see CR-DEA-BC-08]`
- `catalog-research/BC-02-CLOSEOUT.md` open item #5: removed

## 5. Visual re-render

`visuals/v09-ecf-coverage-map.svg` is regenerated. The `strategy-direction ×
build` cell gains a `019` marker; the bottom-of-page "held unmapped" footnote
is removed. The `ci/visual-domain-label-guard` job (PR #50) continues to
enforce axis-label conformance and is re-run on this PR.

## 6. Version bump

Catalog label: `v1-alpha.1` → **`v1-alpha.2`**. Tag `v1-alpha.2` to be cut
at the merge commit.

Bump rationale (VERSIONING section 2.2 - minor):

- Content change: an entity's ECF affiliation moves from held-unmapped to
  mapped; the canonical coverage map changes; the held-unmapped footnote
  disappears.
- Distinctness: the new mapping strengthens the boundary against Asset
  Management and Facility Management (they are now visibly siblings in the
  same domain × stage neighborhood).
- No schema change, no CI change, no metamodel pin change. Catalog label
  advances one letter-suffix step.

Entry-level: TM bumps 1.0.0 → 1.1.0. All other entries unchanged.

## 7. Bump rationale (recorded per VERSIONING §1.2)

The catalog label advances from `v1-alpha.1` (BC-07) to `v1-alpha.2` (BC-08).
The set of admitted canonical capabilities is unchanged at 26; the
held-unmapped count drops from 1 to 0; the distinct primary coordinates
referenced rises from 15 to 16. Historical research artifacts and the
`out/v1-alpha.0` snapshot are deliberately untouched (provenance).

## 8. Verification (all local, pre-push)

- `scripts/check_ecf_conformance.py`: PASS (26 entries + MCSP view; TM
  affiliation transitions from held-unmapped to mapped without redefinition)
- `scripts/check_versions.py`: PASS (TM entry 1.1.0; others unchanged; metamodel_pin 1.0.0; ecf_contract dea:ecf@1.0.0)
- `scripts/check_view_refs.py`: PASS
- `scripts/check_catalog_index.py`: PASS (CATALOG.yaml validates; 26 entities)
- `scripts/check_visual_domain_labels.py`: PASS (regenerated v09 has all
  seven axis labels in v2.4.0 form)
- Entry schema validation (jsonschema draft-07, CI-equivalent): 26/26 clean
- Dash check (no en/em dashes): clean on all touched files
- Secret-pattern scan: clean

## 9. What did NOT change

- The cardinality of the seven Domains (7), the matrix M = D × S (49
  coordinates), and the no-cell-filling rule (CG-005 Invariant 7) are
  unchanged.
- The set of admitted canonical capabilities is unchanged at 26 (TM was
  always admitted; only its affiliation changed).
- The schema, the metamodel pin, the ECF contract pin, and the entity
  template are unchanged.
- Historical research artifacts (`candidates.yaml`, `normalization.yaml`,
  `RESEARCH-REPORT-v0.1.md`, `ECF-OVERLAY-v0.1.md`, admission records,
  prior CRs) and the published `out/v1-alpha.0` snapshot are deliberately
  untouched (provenance).
- `dependencies.yaml` self-ref advances from `v1-alpha.1` → `v1-alpha.2` at
  the merge commit (VERSIONING §4 step 6, maintainer action at merge).

## 10. Pause-for-merge

Per CR-programme convention. After you say **Merge**, I will:

1. Merge this PR to main.
2. Cut the `v1-alpha.2` tag at the merge commit.
3. Advance `dependencies.yaml` self-ref to `v1-alpha.2` (maintainer action
   at merge).

Nothing moves until you say Merge.
