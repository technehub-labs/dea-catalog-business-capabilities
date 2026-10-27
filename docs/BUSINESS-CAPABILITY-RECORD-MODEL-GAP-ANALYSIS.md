# Business Capability Record Model Gap Analysis

**Status**: Accepted analysis (CR-DEA-BC-42, 2026-10-28)
**Governing requirement source**: [Business Capability Documentation Standard](BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md) (CR-DEA-BC-41), requirement IDs BC-DOC-001..012
**Purpose**: decision artifact determining which record-model changes, if any, merit implementation CRs — not an assumption that every gap becomes a field

---

## 1. Purpose and decision context

CR-DEA-BC-41 established the documentation contract. Before any schema expansion, that contract must be mapped against the model that actually exists. This analysis performs that mapping with direct inspection evidence, and partitions the outcome into: sufficient (A), definition/constraint gap (B), documentation gap (C), reference gap (D), candidate schema gap (E), upstream dependency (F), and not-applicable-to-record (G) — per CR-DEA-BC-42 §7.4.

## 2. Scope and exclusions

Analysis and recommendations only. No schema, record, identity, ECF, CI, or inventory changes (CR-DEA-BC-42 §6.2).

## 3. Governing requirements and source versions

- Standard: `docs/BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md` (CR-DEA-BC-41, landed PR #94, commit `cc77c53`, 2026-10-27).
- Requirements BC-DOC-001..012 as defined in that standard §10.

## 4. Inspected schema and artefact inventory

Inspected directly (2026-10-28, `main` @ `cc77c53`):

| Artefact | Path | Notes |
|---|---|---|
| Canonical entity schema | `schemas/entity.schema.json` | post-BC-40 shape: 30 root properties incl. `purpose`, `realization`, two-form `boundary`, `loop_closure_narrative` |
| All canonical records | `entities/v1-alpha/*/capabilities-*.yaml` | 29 records, full-population statistics below |
| Entity-system registry | `reconciliation/entity-system-registry.yaml` | declares `relationships.field: related_capabilities`, canonical types `depends-on/realizes/specializes`, `cross_catalog_field: identity_scope` (ES-003 carrier) |
| Authorship registry | `reconciliation/authorship-fields.yaml` | governs authorship-bearing fields |
| Method documents | `METHODOLOGY.md`, `EVIDENCE.md`, `GOVERNANCE.md`, `TAXONOMY.md` | admission method, naming, boundary rules |
| Gates | `scripts/check_*.py` (13), `validate-entries.yml` inline Draft7 validator | conformance surface |
| Reference entity | `entities/v1-alpha/asset-management-judtwr/` | record + 6-line README (assessed further under CR-DEA-BC-44) |

**Field population evidence (29/29 records unless stated):** populated everywhere — `outcome`, `business_object`, `why_capability`, `boundary`, `non_examples`, `specialization_boundary`, `related_capabilities`, `evidence`, `provenance`, `ecf`, `ecf_rationale`, `version`, `lifecycle_status`, `capability_layer`. Schema-declared but **0/29 populated**: `purpose`, `realization`, `tags`, `external_references`, `maturity`, `metadata`, `children`, `parents`. Partially populated: `aliases` (9/29), `loop_closure_narrative` (1/29), structured `boundary` form (1/29, `enterprise-performance-management-5fxren`). `business_object` values are 28 distinct free-form strings (including compounds `Asset/Information`, `Market/Customer`).

## 5. Requirement-to-model traceability matrix

| Req | Summary | Current representation | Coverage | Gap | Disposition | Schema impact | Migration |
|---|---|---|---|---|---|---|---|
| BC-DOC-001 | Identity and classification | `id`, `name`, `type`, `version`, `lifecycle_status`, `capability_layer`, `ecf`, `metamodel_pin`; org-wide id system (BC-35A); IDM-001..008 gate | Direct | none | **A** | none | none |
| BC-DOC-002 | Definition and semantic interpretation | `definition` (canonical); `why_capability`, `boundary`, `non_examples` carry distinctness; interpretive narrative is README responsibility (Standard §7.2) | Direct for definition; indirect for interpretation (by design) | none structural | **A** (+C guidance in BC-44) | none | none |
| BC-DOC-003 | Implementation independence | Rule-based: METHODOLOGY ability-tests, naming gate, prohibited-practices list (Standard §6) | Direct (as rules, correctly not a field) | none | **A** | none | none |
| BC-DOC-004 | Scope and semantic boundaries | `boundary` (29/29; plain or structured post-BC-40), `non_examples` (29/29) | Direct | when the structured form applies is undocumented | **B** (guidance) | none | none |
| BC-DOC-005 | Composition and specialization | `specialization_boundary` (29/29); `children`/`parents` optional and 0/29 (correct: the first-order set is flat by design; recursion tenet); MCSP view carries specializations | Direct | none structural | **A** | none | none |
| BC-DOC-006 | Enabling relationships and realization | `realization` block (schema) but **0/29 populated** and no target-id formats; `related_capabilities` (29/29) is a flat id list — untyped, no rationale — while the registry already designates it the ES-003 carrier with types `depends-on/realizes/specializes` that the bare-list form cannot express (schema pattern `^capabilities:capability-…$` forbids the typed form) | Indirect / partial | population gap + reference-format gap + typing gap | **C + D** for realization; **E** for relationship typing — routed to dedicated follow-on CR R-1 (see §13) | none in BC-43 | none |
| BC-DOC-007 | Outcomes and traceability | `outcome` (29/29); contribution-vs-guarantee distinction is a Standard rule; typed goal/outcome links would follow R-1's relationship machinery | Direct for outcome | typed outcome links are R-1 dependent | **A** (typed links deferred to R-1) | none | none |
| BC-DOC-008 | Assessment separation | No assessment constructs in the record — correct separation; no assessment authority/catalog exists in the org yet | Not applicable (correctly) | none | **G** | none | none |
| BC-DOC-009 | Provenance and governance | `evidence` + `provenance` (29/29; ladder, admission_cr, evidence_seed_cr, migration post-BC-40); `catalog-research/` registers; CR process + GOVERNANCE.md own governance (correctly not record fields) | Direct | none | **A** (governance-field candidates are **G**) | none | none |
| BC-DOC-010 | Lifecycle and conformance | `version`, `lifecycle_status`, `ecfConformance`, `metamodel_pin`; entity-system lifecycle ladder; check gates | Direct | none | **A** | none | none |
| BC-DOC-011 | README completeness | Entity READMEs are 6-line stubs (identity + coordinate + definition) — documentation interface, not record | Absent (documentation layer) | the Standard's 14-section contract has no template/assessment yet | **G/C** → CR-DEA-BC-44 (R-3) + remediation CR (R-5) | none | none |
| BC-DOC-012 | Cross-artifact consistency | `check_doc_links.py`, `check_cr_index.py` cover doc links + CR index; **no README-vs-record drift check exists** | Partial | record↔README consistency unenforced | **D** → documentation conformance gate CR (R-4) | none (gate CR) | none |

## 6. Grounding-document field candidates (CR-DEA-BC-DOC-000 §3.1) — dispositions

| Candidate | Verdict | Evidence |
|---|---|---|
| `purpose` | **B/C** — property exists in schema; 0/29 populated; no conditionality or population guidance | schema properties; population stats |
| `scope.inclusions/exclusions/distinguishing_criteria` | **A (retain)** — represented by two-form `boundary` + `non_examples` (29/29); structured elaboration already possible via the BC-40 form | boundary forms |
| `business_object_ref` | **F** — canonical Asset entity lives in the sibling `dea-catalog-business-objects` catalog; a typed cross-catalog reference requires that catalog's identity confirmation (escalation U-1); current `business_object` prose (28 distinct values incl. compounds) remains valid | business_object values |
| `relationship_assertions` | **E → R-1** — see BC-DOC-006; carrier is the registry/ES-003 + coordinated schema oneOf, its own CR | registry lines 42–49 |
| `realization` | **C + D** — exists, 0/29, no target-id guidance; `processes:*` scheme is known (sibling processes catalog, post-mv1) | schema; stats |
| `value_contribution`, `beneficiaries` | **G** — README narrative (Standard §3.3 via §7.2); `purpose` + `outcome` cover record-level need | — |
| `constraints`, `assumptions` | **G** — conditional narrative; no universal need evidenced across 29 records | — |
| `assessment_profile_refs` | **G** — no assessment authority exists; premature | — |
| `governance` | **G** — GOVERNANCE.md + CR process + authorship registry own it; duplication prohibited (Standard §3.7) | — |
| `documentation_profile` | **G** — owned by the README standard (BC-44) | — |

## 7. Existing model coverage assessment

The current model is materially stronger than the grounding document assumed at the time of writing (it predates BC-40): `purpose`, `realization`, two-form `boundary`, and the admission-provenance fields all exist. Twelve of the twelve documentation aspects are either directly represented, correctly rule-based, or correctly deferred to other artefacts. The genuine deficiencies are: **population** (purpose, realization), **guidance** (structured-boundary applicability; realization target formats), **relationship typing** (registry-declared but inexpressible), and **README/interface layer** (stub READMEs; no drift enforcement).

## 8. Redundancy and source-of-truth risks

Adding `scope.*`, `governance`, `documentation_profile`, `value_contribution`, or `beneficiaries` as record fields would create competing sources of truth with `boundary`/`non_examples`, GOVERNANCE.md, the README standard, and README narrative respectively. Recommendation: do not add.

## 9. Mandatory and conditionality recommendations

- Universally mandatory (already enforced by schema `required` + gates): identity, definition, outcome, business_object, ecf, evidence, provenance, why_capability, boundary, non_examples, specialization_boundary.
- Conditionally mandatory (rule to be codified): `aliases` when a rename occurred (N-register lineage); `loop_closure_narrative` when a loop obligation is closed; structured `boundary` when the BC-29 rich-narrative form is justified; `related_capabilities` entries remain valid bare references until R-1.
- Recommended: `purpose` (populate on substantive touch / remediation with authored evidence — **never fabricated**); `realization` entries when canonical sibling targets exist.
- Prohibited: any duplicate/competing representation (§8); typed relationship objects before R-1 lands.

## 10. Relationship and reference integrity findings

1. `related_capabilities` is the registry-designated ES-003 relationship field, but the record form (bare id list) cannot carry the declared types (`depends-on/realizes/specializes`) or rationale, and the schema pattern forbids the object form. **Coordinated change required** (registry semantics + schema `items: oneOf`) — R-1, its own CR, because it alters relationship semantics (BC-43 §5.6 boundary).
2. `realization.*` entries have no target-id format. `processes:*` is confirmed; actors/resources/systems/information schemes are unconfirmed sibling-catalog identities (U-1/U-2).
3. `business_object` is free prose with compound values; canonical cross-reference requires U-1.

## 11. Assessment and performance boundary findings

The record correctly contains no assessment constructs (BC-DOC-008 = G). Any future assessment references must wait for an assessment authority; nothing to implement now.

## 12. Backward-compatibility and migration assessment

- No BC-43 change touches populated fields → existing 29 records remain valid; no migration.
- The only population-affecting backlog item (purpose/realization backfill) belongs to the remediation CR (R-5) and must be evidence-authored per record, not bulk-generated.
- R-1's schema oneOf is additive by design (bare ids remain valid) — assessed when R-1 is authored.

## 13. Ordered model-enrichment recommendations (follow-on CR boundaries)

| # | Follow-on | Scope boundary | Dependencies |
|---|---|---|---|
| R-1 | **Relationship Semantics CR** | typed `related_capabilities` (registry-aligned oneOf: `{id, type, rationale}`; ES-003 enforcement; migration rule for existing bare entries) | CS-011 standard; BC-42 finding §10.1 |
| R-2 | **CR-DEA-BC-43 (this tranche)** | minimal model clarifications: `purpose`/`realization` conditionality + format guidance (incl. `processes:*` pattern), structured-boundary applicability note, per-property model documentation; **no record changes, no relationship typing** | this analysis |
| R-3 | **CR-DEA-BC-44 (this tranche)** | README standard + template + asset-management reference assessment | BC-41; this analysis's BC-DOC-011 finding |
| R-4 | Documentation Conformance Gate CR | README-section presence + README-vs-record drift checks (BC-DOC-011/012 enforcement) | R-3 |
| R-5 | Catalog-wide Remediation CR | purpose/realization population (evidence-authored), README adoption, known doc drift (incl. `entities/v1-alpha/README.md` 31-vs-29 count) | R-2, R-3 |
| R-6 | Discovery and Relationship Views CR | generated index/views from canonical data | R-1 (for relationship views) |

## 14. Unresolved upstream dependencies

- **U-1**: canonical `dea-catalog-business-objects` identity scheme for `business_object` cross-references (blocks business_object_ref).
- **U-2**: actors/resources/systems/information catalog identity schemes for `realization` target formats (partially blocks M-2 pattern work; `processes:*` resolved).

## 15. Verification and review record

- Population statistics and boundary-form census reproduced by script from the 29 records (2026-10-28); registry relationships block read directly (lines 42–49).
- AC check: AC-01 ✓ (BC-41 version cited); AC-02 ✓ (§4 inventory); AC-03 ✓ (all 12 mapped); AC-04 ✓ (§6 reuse verdicts); AC-05 ✓ (five candidates rejected as duplicates); AC-06 ✓ (E/F rationales §10, §14); AC-07 ✓ (§9); AC-08 ✓ (typing routed to R-1, not implicit); AC-09 ✓ (§11); AC-10 ✓ (§12); AC-11 ✓ (§13); AC-12 (landing: linked from the Documentation Standard's implementation-sequence section and the CR index); AC-13/AC-14 ✓ (gates at landing; no model changes).
