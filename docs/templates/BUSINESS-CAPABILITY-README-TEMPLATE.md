# Business Capability README Template

<!-- CR-DEA-BC-44. Normative template implementing the 14-section contract
     (CR-41 §5.1) at README layer. Rules:
     - {{PLACEHOLDERS}} mark record-derived values; render them FROM the canonical
       record, never hand-type them from memory.
     - Do not copy this template's guidance text into entity READMEs; replace it.
     - Where a section's information does not exist, record the honest state
       (Not applicable / Not yet established / Not yet documented / Explicitly
       unresolved) — never fabricate, never delete the section.
     - Full section specs: docs/BUSINESS-CAPABILITY-README-STANDARD.md -->

# {{name}}

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `{{id}}` |
| Entity type | {{type}} |
| Version / status | {{version}} · {{lifecycle_status}} |
| Record | `{{record-filename}}` — link the record file (authoritative) |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> {{definition}}

**Interpretation.** {{one-to-three paragraphs: what the enduring ability is; the meaning of material terms; what distinguishes it from its nearest neighbors — authored narrative, clearly not canonical text}}

## 3. Purpose and value contribution

{{purpose — from record `purpose` where populated; otherwise state honestly, e.g. "Not yet established: `purpose` is unpopulated in the record; backfill is scheduled through the remediation CR (R-5)." Relate to `outcome` without guarantee language.}}

## 4. Scope and boundaries

{{Explain the record's `boundary` and `non_examples` — includes, excludes, and why the boundary sits where it does.}}

- **In scope:** {{…}}
- **Out of scope:** {{…}}
- **Non-examples:** {{render `non_examples`, each with its one-line why}}
- **Adjacent distinctions:** {{from boundary exclusions / why_capability}}

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | {{ecf.primary}} |
| Secondary | {{ecf.secondary…}} |

**Rationale.** {{summarize `ecf_rationale`; coordinates are classification context, never identity}}

## 6. Composition and specialization

{{If parents/children exist in the record: list with meaning. Otherwise: "No parent or child capabilities in the first-order set (flat by design)." Then render `specialization_boundary` and what a specialization may refine vs. what stays invariant.}}

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| `{{related-id}}` (link the related record) | {{why — from boundary exclusions, why_capability, or evidence; if no basis is recorded, say so}} |

{{Until the Relationship Semantics CR (R-1) lands, related_capabilities entries are untyped references — do not present them as typed semantics.}}

## 8. Realization and operational context

{{Render `realization` if populated (canonical sibling ids). If unpopulated: "Not yet established — realization links await canonical sibling targets (U-2). Optional illustrative patterns: {{implementation-independent example}}, clearly marked illustrative, never definitional."}}

## 9. Outcomes and traceability

**Intended outcome** (contribution, not guarantee): {{outcome}}

## 10. Assessment considerations

{{Standard state today: "Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008)." Update only when an assessment authority exists.}}

## 11. Governance

- Change control: [GOVERNANCE.md](../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** {{evidence.sources + rationale summary; link catalog-research registers}}
- **Ladder:** {{provenance.ladder_passage stages with dates — candidate → … → canonical}}
- **Why a capability:** {{why_capability}}

## 13. Lifecycle and change history

{{version history from the record's provenance/change record; each change cited by CR}}

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI)
- ECF: {{ecfConformance.status}} under `dea:ecf@1.0.0`
- Entity-system / id-system / naming gates: green at last landing
- This README: conformant to the [README Standard](../BUSINESS-CAPABILITY-README-STANDARD.md); open items: {{none | list}}

---

### Author checklist (delete before landing)

- [ ] Every {{placeholder}} rendered from the record (no hand-typed canonical values)
- [ ] Definition verbatim and attributed; interpretation separate
- [ ] Every section present or carrying an explicit honest state
- [ ] All links resolve (DL-001 checks this)
- [ ] Related-capability bases evidenced; nothing typed until R-1
- [ ] No guaranteed-outcome language; no implementation in the definition
- [ ] Conformance section reflects actual gate status
