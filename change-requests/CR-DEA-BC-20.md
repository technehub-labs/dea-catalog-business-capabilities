# CR-DEA-BC-20: Noun-as-Ability Naming Conformance (Rule 7) + Strategy Formulation and Operations Management Renames + Review-Retained Registrations

**Status**: Proposed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-29
**Depends on**: CR-DEA-BC-01 (naming rules); CR-DEA-BC-05 (versioning); CR-DEA-BC-09 (definition template; N-010..N-015)
**Related**: CR-DEA-BC-12 (BC-SR-A001 carrier); CR-DEA-BC-13 (method rule + 26-entry re-evaluation); dea-metamodel ADR-015
**Supersedes**: none
**Companion**: CR-DEA-BC-21 (Analytics and Intelligence recon; deferred from this CR)

---

## 1. What this CR is

A naming conformance pass that closes the **noun-as-ability** gap surfaced during a CR-DEA-BC-09 retrospective (the BC-09 §7 advisory set: Strategy, Analytics and Intelligence, Enterprise Governance, Sourcing and Procurement, Security Management). The user explicitly named "Strategy" as failing the Ability test (`docs/FOUNDATIONS.md` §7) on grounds that "Strategy" reads primarily as a noun-of-discourse (the plan, the document, the position) rather than as an ability or practice.

The user confirmed the principle (DP-A = iii): only entries that fail the noun-as-ability test are renamed. The user confirmed the resolution mode (DP-B = 2): one cumulative CR following the BC-09 / BC-07 / BC-12 pattern.

Three decisions landed:

1. **Add TAXONOMY rule 7: noun-as-ability**. The name reads as an ability or practice. Recognized patterns: `X Management`, `X Planning`, `X Design`, `X Enablement`, `X Stewardship`, `X Formulation`, `X Governance`, `X Conduct`, `X Oversight`, `X Acquisition`, `X Development`, gerund pairs, or single-word gerunds. A name that fails this test is non-conformant unless registered as reviewed-retained in `catalog-research/normalization.yaml` with an N-NNN decision and rationale.
2. **Rename two entries**: `Strategy` to `Strategy Formulation` (N-016); `Operations` to `Operations Management` (N-018). Both are identity changes under `docs/VERSIONING.md §1.2`.
3. **Register one review-retained**: `Enterprise Governance` is registered as N-019 (review-retained) under the new rule 7 exemption registry. The compound object (Decision) cannot be echoed in the name without violating rule 6 (plain business vocabulary) or rule 1 (ability noun phrases) in the same way that N-015 (Security Management) cannot.
4. **Semantic clarification, not rename, for one**: `Sourcing and Procurement`'s `business_object: Purchase Order` is renamed to `business_object: Acquisition Cycle` (N-020). This is a semantic clarification: the ability's object is the supplier-acquisition cycle, not the process artifact. The canonical name is unchanged.
5. **Analytics and Intelligence (N-017) is moved to a dedicated recon** (CR-DEA-BC-21): the user explicitly asked for an ADR-driven investigation into whether the entry should be `Insight Management`, `Intelligence Management`, `Decision Intelligence Management`, or review-retained. The recon will produce the evidence, then the rename lands as a follow-on CR. This keeps BC-20 focused on unambiguous cases.

### 1.1 Outcome

- **Catalog count: 28 -> 28 first-order canonical capabilities** (no admissions; two identity renames).
- **Two entries renamed** (id moves; aliases preserved; version 1.0.0 -> 2.0.0):
  - `dea:capability-strategy` -> `dea:capability-strategy-formulation`
  - `dea:capability-operations` -> `dea:capability-operations-management`
- **Two business_object clarifications** (minor; semantically anchored):
  - `dea:capability-sourcing-and-procurement.business_object`: `Purchase Order` -> `Acquisition Cycle` (N-020)
  - `dea:capability-operations-management.business_object`: unchanged as `Operations` per user direction (DP-D: top-level object; semantic breakdown in definition, not in business_object)
- **One review-retained registration**:
  - `dea:capability-enterprise-governance` registered as N-019 (review-retained)
- **One new rule**: TAXONOMY §1 rule 7 (noun-as-ability)
- **One new hard check**: `scripts/check_naming.py` H8 (noun-as-ability structural test) + exemption registry honoring `normalization.yaml` review-retained verdicts
- **One new exit code path**: `--strict` is replaced by the structural H8 check (H1-H7 + H8 are always hard; A1 is advisory; N-NNN review-retained entries are exempt from H8)
- **Tag target**: `v1-alpha.X+1` (Minor bump; lettered minor per BC-09 precedent for identity corrections)

### 1.2 Why this CR exists at all

BC-09 (PR #54) explicitly listed five advisories and did not rename them:

> Post-CR advisory set (5, all documented in the script docstring): Strategy (Enterprise), Analytics and Intelligence (Insight), Enterprise Governance (Decision), Sourcing and Procurement (Purchase Order), Security Management (Asset/Information; N-015).

Only N-015 (Security Management) was formally registered as review-retained in `normalization.yaml`. The other four remained advisory-by-comment, which made them structurally invisible to CI: the `check_naming.py` `--strict` flag surfaced them as warnings, but the default run returned `PASS`. The user's standing principle ("name gating must perform a test to ensure adherent compliance to the convention for naming") is the principle the BC-09 advisory set violated: a check that is structurally advisory is not a gate.

This CR codifies the noun-as-ability rule as TAXONOMY §1 rule 7, codifies the review-retained exemption as a `normalization.yaml`-driven registry, and resolves two of the four advisories (N-016 Strategy Formulation, N-018 Operations Management, N-019 Enterprise Governance review-retained, N-020 Sourcing and Procurement business_object semantic clarification). The fifth advisory (Analytics and Intelligence) moves to CR-DEA-BC-21 for a dedicated recon.

---

## 2. Why one CR, not four

Per the user's DP-B choice, this is one bundled CR. The renames, the rule addition, and the enforcement are coupled:

- The rule addition (rule 7) is meaningless without enforcement (H8).
- The enforcement (H8) is meaningless without an exemption registry.
- The exemption registry is meaningless without N-019 (Enterprise Governance review-retained).
- N-016 and N-018 renames are the headline changes that prove the rule works end-to-end.

Splitting into separate CRs (BC-20a rule, BC-20b renames, BC-20c enforcement) would multiply review surface for no architectural benefit. The bundle is reviewable end-to-end because all pieces share the same v1-alpha.X+1 version bump envelope.

---

## 3. Method rule addition

### 3.1 TAXONOMY §1 rule 7 (new)

Added at the end of `TAXONOMY.md §1`:

> **7. Noun-as-ability.** The canonical name reads as an ability or practice, not as an artifact, output, state, or noun-of-discourse. Recognized patterns: `X Management`, `X Planning`, `X Design`, `X Enablement`, `X Stewardship`, `X Formulation`, `X Governance`, `X Conduct`, `X Oversight`, `X Acquisition`, `X Development`, gerund pairs (`Sourcing and Procurement`), or single-word gerunds (`Marketing`). A name that fails this test is non-conformant unless the entry is registered as reviewed-retained in `catalog-research/normalization.yaml` with an N-NNN decision and rationale (N-015, N-019 precedent).

A reference to N-019 is added in `TAXONOMY.md §1A.3` (machine enforcement section): the lint's noun-as-ability check (H8) honors the N-NNN `review-retained` registry; non-N-NNN entries that fail H8 fail CI.

### 3.2 Rationale

The BC-09 advisory set demonstrated that rule 1 (ability noun phrases) and rule 2 (business-object anchored) do not, on their own, prevent the noun-of-discourse failure. "Strategy" is an ability noun phrase in the grammatical sense; it fails the Ability test (`docs/FOUNDATIONS.md` §7) at the semantic level because the unmarked noun reads primarily as the artifact. Rule 7 codifies that test at the structural level: the name must sound like a practice, not a noun-of-discourse.

### 3.3 Pattern library (TAXONOMY §1 rule 7 follow-up)

The recognized-pattern list (rule 7 first sentence) is **exhaustive for the corpus to date**, not normative for future patterns. A future entry whose name uses an unrecognized pattern (e.g. `X Acquisition`, `X Sourcing`) requires a `normalization.yaml` registration that names the pattern as recognized. This keeps the rule specific without locking future naming choices.

---

## 4. Renames (N-016, N-018, N-019, N-020)

### 4.1 N-016: Strategy -> Strategy Formulation

| Field | Value |
|---|---|
| Old name | `Strategy` |
| New name | `Strategy Formulation` |
| Old id | `dea:capability-strategy` |
| New id | `dea:capability-strategy-formulation` |
| Aliases | `[Strategy]` |
| Definition | unchanged ("The ability to set the enterprise's direction: where it will compete, what it will become, and what it will not do.") |
| business_object | unchanged (`Enterprise`) |
| ECF coordinates | unchanged (`strategy-direction/conceive` primary + `strategy-direction/improve` secondary) |
| capability_layer | unchanged (`strategic`) |
| Version | 1.1.1 -> 2.0.0 |
| Rationale | "Strategy" out of context reads as noun-of-discourse (the plan, the document, the position). "Strategy Formulation" is the recognized ability noun: formulation = the act/ability of formulating. N-001 / N-015 / BC-09 naming-style precedent: rename + alias. |

### 4.2 N-018: Operations -> Operations Management

| Field | Value |
|---|---|
| Old name | `Operations` |
| New name | `Operations Management` |
| Old id | `dea:capability-operations` |
| New id | `dea:capability-operations-management` |
| Aliases | `[Operations, Production Management (corpus), Service Delivery Management (corpus)]` |
| Definition | lightly re-anchored: "The ability to run the enterprise's day-to-day production and service delivery." (Object-naming requirement; semantics unchanged from the BC-13 §3.2 re-evaluation.) |
| business_object | unchanged (`Operations`) per user direction DP-D (single top-level object; semantic breakdown provided in definition) |
| ECF coordinates | unchanged (`enablement-operations/operate` primary + `enablement-operations/improve` secondary) |
| capability_layer | unchanged (`operational`) |
| Version | 1.0.0 -> 2.0.0 |
| Rationale | noun-as-ability test fails on bare plural noun. "Operations Management" is the corpus-standard form (APQC cat. 4 "Operate", BIZBOK "Operations Management", BA Guild "Operations and Support"). Parallels Customer / Asset / Workforce Management. |

### 4.3 N-019: Enterprise Governance -> review-retained

| Field | Value |
|---|---|
| Name | `Enterprise Governance` |
| Id | `dea:capability-enterprise-governance` (unchanged) |
| Aliases | unchanged |
| Definition | unchanged |
| business_object | unchanged (`Decision`) |
| ECF coordinates | unchanged |
| Version | 1.0.1 -> 1.0.2 (advisory-clearance bump; non-identity per VERSIONING §1.2) |
| Review-retained rationale | "Governance" reads as an ability verb (the act of governing), not as a noun-of-discourse; the unmarked noun-as-ability test passes. The rule-2 object-anchoring heuristic is advisory because the ability's object is the act of constituting decisions across the enterprise, which is not a literal token in "Enterprise Governance" but is the semantic subject. N-015 precedent: compound object that cannot be named literally without violating rule 6 (plain vocabulary) or rule 1 (ability noun phrases) is exempt. |

The advisory-clearance version bump records the registration. The entry is exempt from H8 via the `normalization.yaml` registry.

### 4.4 N-020: Sourcing and Procurement business_object semantic clarification

| Field | Value |
|---|---|
| Name | `Sourcing and Procurement` (unchanged) |
| Id | `dea:capability-sourcing-and-procurement` (unchanged) |
| business_object | `Purchase Order` -> `Acquisition Cycle` |
| Version | 1.2.0 -> 1.3.0 (semantic clarification; minor bump) |
| Rationale | "Purchase Order" is a process artifact (a document), not the ability's business object. The ability's object is the supplier-acquisition cycle: the sustained activity of identifying suppliers, qualifying them, transacting with them, and managing the resulting supply relationships. "Acquisition Cycle" names the sustained object; the artifacts (purchase orders, contracts, invoices) are realization outputs (`scripts/check_naming.py` A1 advisory cleared). |

This is a semantic clarification, not a rename. The id and name are unchanged. The version bump reflects the semantic change per `VERSIONING.md §1.2` (clarification bumps minor).

---

## 5. Reference updates

### 5.1 N-016 (Strategy Formulation)

Cross-referencing entries: `dea:capability-change-management`, `dea:capability-enterprise-governance`, `dea:capability-organizational-design`, `dea:capability-strategic-planning`. Each gets:
- `related_capabilities` id updated where present
- boundary prose mentions of "Strategy" updated to "Strategy Formulation"

### 5.2 N-018 (Operations Management)

Cross-referencing entries: `dea:capability-analytics-and-intelligence` (boundary prose); `dea:capability-information-management` (boundary prose); `dea:capability-strategic-planning` (boundary prose); `dea:capability-technology-management` (boundary prose); `dea:capability-technology-enablement` (boundary prose). Each gets:
- `related_capabilities` id updated where present
- boundary prose mentions of "Operations" updated to "Operations Management"

### 5.3 N-020 (Sourcing and Procurement business_object)

`scripts/check_naming.py` A1 advisory cleared. No cross-references change.

### 5.4 Catalog and overlay

- `CATALOG.yaml` regenerated.
- `catalog-research/ECF-OVERLAY-v0.2.md` coverage table and reading paragraph cite the new canonical names with a CR-DEA-BC-20 provenance note. `catalog-research/ecf-overlay-v0.2.yaml` keeps the candidate register names (candidate-keyed provenance; CR-DEA-BC-07 precedent; BC-09 §5 reaffirmed).
- `catalog-research/normalization.yaml` appended with N-016, N-018, N-019, N-020.
- `README.md` and `entities/v1-alpha/README.md`: PR-narrative cites current canonical names with the rename noted.
- `CHANGELOG.md`: v1-alpha.X+1 entry.
- `docs/REVIEWS.md`: entry appended.

### 5.5 Files NOT changed

Per BC-09 §8 precedent (reaffirmed):
- No edits to historical research artifacts: `candidates.yaml`, `ECF-OVERLAY-v0.1.md`, `preliminary-ecf-overlay.yaml`, admission records, prior CRs, and the candidate-keyed `ecf-overlay-v0.2.yaml` name fields are provenance.
- No edit to published `out/` snapshots (immutable per CR-DEA-BC-05/06).
- `dependencies.yaml` self-ref stays at `v1-alpha.X` in this PR; it advances to `v1-alpha.X+1` when the tag is cut (VERSIONING section 4 step 6, maintainer action at merge).

---

## 6. Enforcement

### 6.1 `scripts/check_naming.py` H8 (new hard check)

Pattern test: extract the canonical name, tokenize on whitespace, check that the last token is one of:

- `Management`, `Planning`, `Design`, `Enablement`, `Stewardship`, `Formulation`, `Governance`, `Conduct`, `Oversight`, `Acquisition`, `Development`, `Procurement`, `Sourcing`, `Marketing`

OR that the full name is a gerund pair (matches `r'^[A-Z][a-z]+ and [A-Z][a-z]+$'` after stripping connectors) or a single-word gerund (matches `r'^[A-Z][a-z]+ing$'`).

### 6.2 Normalization registry exemption

`scripts/check_naming.py` reads `catalog-research/normalization.yaml` at startup and builds a set of `(id -> exemption)` mappings for entries registered as `verdict: review-retained`. An entry with a registered exemption is exempt from H8.

Exemption registry schema (per entry):
- `verdict: review-retained`
- `id: dea:capability-<slug>`
- `basis: <short rationale>`

N-019 (Enterprise Governance) is the first such registration. N-015 (Security Management, registered in BC-09) is the second.

### 6.3 Lint behavior change

- **Pre-CR-20 behavior**: `check_naming.py` returns `PASS: 28 entries conform` with 4 advisory warnings (Analytics and Intelligence; Enterprise Governance; Sourcing and Procurement; Strategy). `--strict` promotes advisories to failures; **deprecated**.
- **Post-CR-20 behavior**: `check_naming.py` returns `PASS: 28 entries conform` with the same 4 A1 advisories (rule-2 object-anchoring heuristic, semantic-review territory per TAXONOMY section 1A.3) plus 1 A1 advisory on Security Management (N-015 retention). H8 is hard: a new entry that fails the noun-as-ability test without registering an N-NNN review-retained exemption fails CI. The BC-09 advisory set's *noun-as-ability* axis is closed for the renamed/retained entries (N-015, N-016, N-018, N-019, N-020); the rule-2 object-anchoring axis is unchanged because that axis is semantic-review territory by design.

### 6.4 Wired into CI

`.github/workflows/validate-entries.yml` step that runs `check_naming.py` is unchanged in name; the script behavior changes. The step fails CI on H8 violations or any other H1-H7 violation.

---

## 7. Version bump

Per `docs/VERSIONING.md §2`:

- **Catalog label**: `v1-alpha.X` -> **v1-alpha.X+1** (Minor within the lettered regime; per BC-09 §6 precedent).
- **Affected entry versions**:
  - `dea:capability-strategy-formulation`: 1.1.1 -> 2.0.0 (identity rename)
  - `dea:capability-operations-management`: 1.0.0 -> 2.0.0 (identity rename)
  - `dea:capability-enterprise-governance`: 1.0.1 -> 1.0.2 (advisory-clearance)
  - `dea:capability-sourcing-and-procurement`: 1.2.0 -> 1.3.0 (business_object semantic clarification)
- **Total canonical entry count**: 28 -> 28 (no admissions; two id renames).
- **Specialization views**: `view-telecom-mcsp` references updated to new ids where the renamed entries are referenced; SPEC-006 parent unaffected.
- **Catalog label consumer impact**: consumers pinning by catalog label (`v1-alpha.X+1`) get the renames automatically; consumers pinning by entry id (`dea:capability-strategy`, `dea:capability-operations`) must remap to the new ids. Tier-1 consumers (entry id pin) are not the documented primary mode per `docs/VERSIONING.md §3`.

---

## 8. Acceptance criteria

- [ ] `TAXONOMY.md §1` rule 7 added with the recognized-pattern list and exemption reference.
- [ ] `TAXONOMY.md §1A.3` cross-ref updated to cite the N-NNN exemption registry.
- [ ] `dea:capability-strategy-formulation/dea:capability-strategy-formulation.yaml` exists at version 2.0.0 with alias `Strategy`.
- [ ] `dea:capability-operations-management/dea:capability-operations-management.yaml` exists at version 2.0.0 with aliases `Operations`, `Production Management`, `Service Delivery Management`.
- [ ] `dea:capability-strategy/dea:capability-strategy-formulation.yaml` does NOT exist (former id retired; not reused per TAXONOMY §2.3).
- [ ] `dea:capability-operations/dea:capability-operations.yaml` does NOT exist.
- [ ] `dea:capability-enterprise-governance` at version 1.0.2.
- [ ] `dea:capability-sourcing-and-procurement` at version 1.3.0 with `business_object: Acquisition Cycle`.
- [ ] 4 cross-referencing entries updated for N-016 (`change-management`, `enterprise-governance`, `organizational-design`, `strategic-planning`).
- [ ] 5 cross-referencing entries updated for N-018 (`analytics-and-intelligence`, `information-management`, `strategic-planning`, `technology-management`, `technology-enablement`).
- [ ] `CATALOG.yaml` regenerated and committed.
- [ ] `catalog-research/normalization.yaml` appended with N-016, N-018, N-019, N-020 (each with the schema fields named in §6.2 for N-019 review-retained).
- [ ] `scripts/check_naming.py` H8 implemented with N-NNN exemption registry read.
- [ ] `scripts/check_naming.py` default run returns `PASS: 28 entries conform` post-CR. H8 is enforced; the BC-09 advisory set is closed for entries that have been renamed or registered review-retained (N-015, N-019). The remaining A1 advisories are the rule-2 object-anchoring heuristic, which is semantic-review territory per TAXONOMY section 1A.3: Analytics and Intelligence (moved to CR-DEA-BC-21 recon), Enterprise Governance (object Decision echoes the governed act not the noun), Security Management (N-015 retention), Sourcing and Procurement (object Acquisition Cycle is the sustained activity not the noun), Strategy Formulation (object Enterprise is the governed entity not a noun token in the name).
- [ ] `scripts/check_naming.py --strict` returns the same `PASS` (deprecated flag; not a different gate).
- [ ] `scripts/check_ecf_conformance.py`: PASS.
- [ ] `scripts/check_versions.py`: PASS.
- [ ] `scripts/check_view_refs.py`: PASS.
- [ ] `scripts/check_catalog_index.py --schema ...`: OK (28 entities).
- [ ] `scripts/check_visual_domain_labels.py`: PASS.
- [ ] Entry schema validation (jsonschema draft-07, CI-equivalent): 28/28 clean.
- [ ] `git diff --check`: clean.
- [ ] Secret-pattern scan: clean.
- [ ] `CHANGELOG.md` has the `[v1-alpha.X+1]` section.
- [ ] `change-requests/README.md` has the CR-DEA-BC-20 row.
- [ ] `docs/REVIEWS.md` has the v1-alpha.X+1 entry.

## 9. Parked-items rollup (informational)

This CR is the **convergence point** for the noun-as-ability gate. Other parked items in the catalog are tracked here for the next cadence. Each is a separate, queued CR.

| Item | Source | State | Next action |
|---|---|---|---|
| Analytics and Intelligence naming recon | BC-09 §7 advisory; CR-DEA-BC-20 §1 companion CR | Open | **CR-DEA-BC-21** (separate, dedicated recon; ADR-driven; chooses between Insight Management / Intelligence Management / Decision Intelligence Management / review-retained) |
| Track B (EPM) admission | BC-13 §11 follow-on queue; BC-SR-A001 §5; BC-19 research-CR landed | Evidence seeded; admission pending | **CR-DEA-BC-15** (admission CR after user acceptance of BC-19 evidence package) |
| Track C (Relationship Management) investigation | BC-13 §11 follow-on queue; BC-SR-A001 §6; INV-RELMGMT-v0.1.md | E2 (early stage); needs >=2 industry corpus sources | **CR-DEA-BC-22** (Track C evidence package, mirroring BC-18/19) |
| Knowledge / Learning Management | BC-SR-A001 §7 (parked with "needs stronger evidence") | Unstarted | **CR-DEA-BC-23** (new investigation; A+B+C gate) |
| CAND-005 / CAND-006 unification (SPEC-D1) | BC-02 §33.10 deferred; G5 trigger | Deferred | Reopens when G5 corpus available; current bias is BC-13 §6.3 option 3 (no generic parent) |
| D-2026-09-04-03 PDF generation | decisions.md D-03 | Deferred follow-on | Add to next cadence as a follow-on; small SVG-to-PDF wrapper using sharp/libvips |
| CR-MM-02 capability schema hygiene (U1/U2/U3) | `business-capabilities/01_change-requests/upstream/CR-MM-02-capability-schema-hygiene.md` | Pending since 2026-09-01; targets `dea-metamodel` | Open issue on `dea-metamodel` with CR-MM-02 attached; not a current blocker |

---

## 10. Tag

`v1-alpha.X+1` is cut at this CR's merge commit per CR-DEA-BC-05. Tag signing: project GPG signing setup; see the standing protocol.

## 11. Pause-for-merge

Per CR-programme convention. After you say **Merge**, I will:

1. Merge this PR to main.
2. Cut the `v1-alpha.X+1` tag at the merge commit.
3. Advance `dependencies.yaml` self-ref to `v1-alpha.X+1` (maintainer action at merge).
4. Surface CR-DEA-BC-21 (Analytics recon) as the next-slice proposal.

Nothing moves until you say Merge.

## 12. References

- CR-DEA-BC-09 (naming conformance refresh; the advisory set this CR closes)
- CR-DEA-BC-12 (BC-SR-A001 carrier; submittal review surfaced the noun-as-ability gap)
- CR-DEA-BC-13 (§3.2 selection heuristics; §11 follow-on queue)
- CR-DEA-BC-17 (Tech Enablement admission; closed)
- CR-DEA-BC-14 (Org Design admission; closed)
- CR-DEA-BC-18, CR-DEA-BC-19 (Track A and Track B evidence packages)
- BC-SR-A001 (submittal review)
- `docs/FOUNDATIONS.md` §2 (capability definition) and §7 (admission tests)
- `TAXONOMY.md` §1 (rules 1-6), §1A (definition and outcome shape), §2 (alias policy)
- `docs/VERSIONING.md` §1.2 (identity changes bump major within same tier), §3 (pin modes), §4 (release procedure)