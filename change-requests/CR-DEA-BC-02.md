# CR-DEA-BC-02: Capability classification reconciliation: ADR-015 alignment

| Field | Value |
|-------|-------|
| **CR** | CR-DEA-BC-02 |
| **Title** | Reconcile the catalog record shape with dea-metamodel ADR-015/CR-016: kind by entity specialization, governed capability_layer, capability_type deprecated |
| **Status** | Proposed |
| **Date** | 2026-08-31 |
| **Author** | Coder (for eaojnr) |
| **Depends on** | dea-metamodel ADR-015 (capability classification by specialization), dea-metamodel CR-016 (implementation, merged), CR-DEA-BC-01 (catalog method; this CR constrains one record field, not the method) |
| **Scope** | Docs-only reconciliation: update the conceptual record shape in `docs/FOUNDATIONS.md` §12 and record migration guidance for the deprecated `capability_type` field |
| **Out of scope** | Catalog population; schema files and CI (follow CR-DEA-BC-01); any change to ECF overlay rules; creation of non-business capability catalogs |

---

## 1. Context

dea-metamodel ADR-015 (2026-08-31) decided that capability kinds are
expressed by specialization of a new abstract root `dea:Capability`, not
by a classifier field. CR-016 (merged 2026-08-31) implemented the
decision:

- `dea:Capability` is the abstract Core root, aligned 1:1 with
  `wsf:Capability` (WSF ADR-WSF-07).
- `dea:BusinessCapability` specializes it; sibling kinds
  (`dea:SystemCapability`, `dea:InfrastructureCapability`,
  `dea:AIAugmentedCapability`) live in profiles.
- `Capability.capability_layer` (`strategic | operational | support`) is
  a governed enumeration attribute, registered in the controlled
  vocabulary (E005).
- `Capability.capability_type` (`business | technical | hybrid`) is
  deprecated in `schemas/entities/capability.json`: kind is now the
  entity type. The field is retained for backwards compatibility;
  existing values remain valid.

The catalog's conceptual record (`docs/FOUNDATIONS.md` §12) still lists
`capability_type:` as a target field. Without reconciliation the method
CR (CR-DEA-BC-01) would ratify a field the metamodel has already
deprecated.

## 2. Decision

1. The canonical capability record SHALL NOT carry `capability_type`.
   Every entry in this catalog is a `dea:BusinessCapability` by virtue of
   catalog scope; kind needs no per-entry field.
2. The record SHALL carry an optional `capability_layer` field whose
   values are exactly the governed enumeration
   (`strategic | operational | support`).
3. ECF coordinates remain classification metadata on the entry
   (`ecf.primary` / `ecf.secondary`); they are never a kind classifier
   (ADR-015 §6).
4. If a future catalog-side instance set is found carrying legacy
   `capability_type` values, the migration is: `business` maps to no
   field (kind is the entity type); `technical` and `hybrid` are
   escalated for review, because in this catalog they indicate either a
   mis-scoped entry (a system or AI-augmented capability, which belongs
   to a different kind) or a pre-ADR-015 annotation that should be
   re-expressed as `capability_layer` plus evidence notes.
5. This CR constrains the record shape only; the admission method,
   evidence ladder, and lifecycle remain the province of CR-DEA-BC-01.

## 3. Changes

- `docs/FOUNDATIONS.md` §12: replace `capability_type:` with
  `capability_layer:` in the target record shape; add a note recording
  the deprecation and this CR.
- No other file changes. README continues to point at CR-DEA-BC-01 as
  the method gate.

## 4. Acceptance criteria

1. `docs/FOUNDATIONS.md` §12 shows no live `capability_type` field.
2. The deprecation and the migration rule (§2 item 4) are discoverable
   from the record shape comment.
3. No schema, CI, or population change accompanies this CR.

## 5. References

- dea-metamodel ADR-015: Capability classification: specialization over
  classifier entities
- dea-metamodel CR-016: implementation (merged, PR #152)
- dea-metamodel `schemas/entities/capability.json` and
  `metamodel/vocabularies/classifications.yaml` (governed enumeration)
- dea-metamodel `mappings/wsf/mapping.yaml` (WSF federation mapping)
- WSF `wsf/concepts/capability.md` (`odea:BusinessCapability`
  specialization precedent)
