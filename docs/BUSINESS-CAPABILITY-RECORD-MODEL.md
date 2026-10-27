# Business Capability Record Model

**Status**: Normative model documentation (CR-DEA-BC-43 M-4, 2026-10-28; derived from [CR-DEA-BC-42](../change-requests/CR-DEA-BC-42-record-model-gap-analysis.md) findings)
**Authoritative artefact**: `schemas/entity.schema.json` — this document explains the model; where any divergence appears, the schema and the governing CRs decide, and the divergence is a defect to file
**Standard context**: [Business Capability Documentation Standard](BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md) (CR-DEA-BC-41); gap analysis [BUSINESS-CAPABILITY-RECORD-MODEL-GAP-ANALYSIS.md](BUSINESS-CAPABILITY-RECORD-MODEL-GAP-ANALYSIS.md)

---

## 1. Property reference

Requirement classes: **M** universally mandatory (schema-enforced), **CM** conditionally mandatory (rule-enforced when the condition holds), **R** recommended, **O** optional, **G** governed elsewhere (record must not carry it).

| Property | Class | Semantic definition (and distinctions) |
|---|---|---|
| `id` | M | Org-wide canonical identity (`capabilities:capability-<slug>-<hash>`; CR-DEA-BC-35A; enforced IDM-001..008). Never a path, name, or ECF coordinate. |
| `type` | M | Always `BusinessCapability` (kind by entity specialization, ADR-015 lineage). |
| `name` | M | Canonical name under TAXONOMY naming rules (H-gates). Aliases never replace it. |
| `definition` | M | The authoritative semantic definition: an enduring ability, never an activity, system, org unit, or outcome. Interpretive narrative belongs to the README, not here. |
| `version` | M | Entity content version (semver; distinct from catalog release, schema version, upstream model version). |
| `lifecycle_status` | M | Entity lifecycle (BC ladder; entity-system ES-004 exempt by construction per the registry). |
| `metamodel_pin` | M | Upstream metamodel pin. |
| `capability_layer` | O | Governed vocabulary (strategic/operational/support). |
| `purpose` | R | Why the capability exists — distinct from `definition` (what it is) and `outcome` (what it contributes to). **Population policy (M-1)**: authored, evidence-backed narrative only; never bulk-generated; backfill happens per-record through the remediation CR. Absence is an honest state, not a defect. |
| `outcome` | M | The intended result the capability contributes to; contribution, never a guarantee. |
| `business_object` | M | The governed object focus, as a plain label today. Cross-catalog canonical reference awaits the business-objects identity decision (escalation **U-1**); compound values (`Asset/Information`) remain valid prose until then. |
| `ecf` (+ `ecf_rationale`, `ecfConformance`) | M | Classification overlay: primary (earliest initiation) + secondaries, with rationale and conformance metadata. Coordinates are never identity (CR-DEA-BC-01; ECF contract `dea:ecf@1.0.0`). |
| `evidence` | M | Admission evidence (sources + rationale) under EVIDENCE.md. |
| `provenance` | M | Ladder passage (candidate→…→canonical; post-mv1 admission checkpoints `evidence-seeded`/`admitted` per BC-40) + `candidate_ref`/`normalization_refs`/`admission_cr`/`evidence_seed_cr`/`migration`. |
| `why_capability` | M | Why this is a durable ability rather than a process, unit, or technology (distinct from `purpose`: this justifies capability-hood, not business value). |
| `boundary` | M | What the capability includes/excludes. Two forms (BC-40): plain string (default) or structured `{against_capabilities[], loop_role}` — the structured form applies only where a BC-29 rich-narrative justification exists (**M-3** guidance). |
| `non_examples` | M | Things that must not be read as this capability. |
| `specialization_boundary` | M | What a specialization may refine without redefining the parent. |
| `related_capabilities` | CM | Canonical sibling references. Today: bare id list (schema-enforced pattern). The entity-system registry designates this field the ES-003 relationship carrier with types `depends-on/realizes/specializes`; the typed form is **not yet expressible** and is reserved to the Relationship Semantics CR (**R-1**) — do not improvise typed objects locally. |
| `realization` | CM | Cross-catalog realization links: `processes` (pattern `^processes:` — confirmed sibling scheme, **M-2**), `actors`/`resources`/`systems`/`information` (canonical sibling ids when available; id schemes pending **U-2**). Populate only with resolvable canonical targets; prose is not accepted in `processes`. Absence (current state, 0/29) is honest until targets exist. |
| `aliases` | CM | Rename-lineage aliases; required when a rename has occurred (N-register lineage). |
| `loop_closure_narrative` | CM | Required when a loop obligation is explicitly closed (BC-SR-A001 §16 class). |
| `tags`, `external_references`, `maturity`, `metadata`, `children`, `parents` | O | Declared, currently unpopulated (0/29). `children`/`parents` stay empty while the first-order set is flat by design. |

## 2. Deliberately absent (record must not carry)

Governance ownership, approval actors, authorship (GOVERNANCE.md + authorship registry); assessment constructs (BC-DOC-008: separation preserved until an assessment authority exists); `scope.*` sub-fields, `value_contribution`, `beneficiaries`, `constraints`, `assumptions`, `governance`, `documentation_profile` (rejected as duplicate sources of truth — CR-42 §6/§8; README narrative or governed artefacts own them).

## 3. Open dependencies

- **R-1** Relationship Semantics CR: typed/rationaled `related_capabilities` (registry-aligned schema oneOf + ES-003 enforcement).
- **U-1** business-objects catalog identity scheme (enables canonical `business_object` references).
- **U-2** actors/resources/systems/information catalog identity schemes (completes `realization` target formats; `processes:*` resolved).

## 4. Verification

Schema validation (`validate-entries` inline Draft7 validator), id-system, entity-system, ECF, naming, and version gates remain the enforcement surface; this document adds none and changes none.
