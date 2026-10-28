# Canonical Relationship Integrity Standard

**Status**: Normative (CR-DEA-BC-48, 2026-10-28)
**Gate**: `scripts/check_relationship_integrity.py` (rules RI-001..004; CI step in `validate-entries.yml`)
**Model context**: relationship **typing** is deferred to the Relationship Semantics CR (R-1, per CR-42 §10.1). This standard governs the integrity of relationship representations **as they exist** — it invents no semantics.

---

## 1. Principles

1. **A reference is not automatically a relationship.** `related_capabilities` entries are recorded associations; until R-1, they carry no type, and no hierarchy/dependency/equivalence/specialization may be inferred from them (CR-47 §4.3 enforced in views).
2. **Semantics must be explicit where they exist.** The structured `boundary.against_capabilities[].rationale` is the one representation carrying explicit per-target semantics today ("distinguished against, because …"); it is governance-grade and must resolve.
3. **No unsupported inference** by any validator or view (no universal acyclicity, no reciprocity mandate, no name-similarity matching).
4. **Canonical sources remain authoritative** — every inventory or view is derived (CR-47).

## 2. Inventory of relationship representations (evidence: 29 records, 2026-10-28)

| Representation | Form | Semantics (authority) | Cardinality/direction | Integrity rule | Authority | Validation |
|---|---|---|---|---|---|---|
| `related_capabilities` | list of canonical ids (72 directed refs; 32 reciprocal pairs) | recorded association, **untyped until R-1** | 0..n, directed; reciprocity observed, not required | every id resolves to a canonical record | schema (CR-40); registry ES-003 designates the field as the future typed carrier | RI-001 (automated); DCV-008 (README-layer duplicate, kept for locality) |
| `boundary.against_capabilities[]` | `{id, rationale}` objects (6 refs, all EPM) | "distinguished against, because …" — explicit distinctness semantics with per-target rationale | 0..n, symmetric in intent (distinctness is mutual) | every id resolves; rationale present | CR-DEA-BC-29/40 structured boundary | RI-002, RI-003 (automated) |
| `parents` / `children` | declared, **unused (0/29)** | none exercised; first-order set is flat by design (CR-41 §3.5) | — | none while unused; any future use requires a model decision | schema | not assessed (recorded) |
| `realization.*` | declared, **unused (0/29)**; `processes` pattern `^processes:` | cross-catalog realization links (BC-DOC-006) | 0..n per array | format rule when populated | CR-43 M-2 | not assessed while unpopulated (recorded) |
| Registry ES-003 types (`depends-on/realizes/specializes`) | registry declaration only | **declared but not yet expressible** — the bare-list schema pattern forbids the typed form | — | — | entity-system registry (CS-011) | RI-004 (reporting finding: open R-1 gap) |

**Distinguished from these**: ECF co-location (classification, never relationship); view links (navigation, CR-47 contracts); evidence source refs (provenance, not semantics).

## 2a. Typed relationship semantics (CR-DEA-BC-53)

`related_capabilities` accepts typed assertions `{id, type, rationale}` alongside legacy bare ids. The registry (ES-003) is the type authority; the schema enum mirrors it and must never lead it.

| Attribute | `depends-on` | `realizes` | `specializes` |
|---|---|---|---|
| Definition (registry authority; prose normative only to the registry) | a capability's functioning relies on another | a capability's effect is delivered through another (cross-catalog direction per upstream semantics) | a capability refines another within the specialization boundary rules |
| Source / target kinds | BusinessCapability → BusinessCapability (as configured) | per registry `type_constraints` (none declared for BC — unresolved) | per registry (none declared — unresolved) |
| Cardinality | unresolved (no authority) | unresolved | unresolved |
| Reciprocity | not specified | not specified | not specified |
| Evidence per assertion | `type` from the registry set + non-empty `rationale` (RI-005) | same | same |
| Validation | RI-005 + ES-003 canonical-type membership | same | same |

Unresolved attributes (cardinality, reciprocity, constraint tables) are recorded as unresolved — recorded here, not invented. **Population status: zero typed assertions at landing** — the 72 legacy associations remain bare pending per-assertion evidence; a future CR may propose typings with dispositions.

## 3. Integrity rules (RI-*)

| Rule | Check | Severity | Basis |
|---|---|---|---|
| RI-001 | every `related_capabilities` id resolves to a canonical record | blocking | §5.2 explicit semantics; DCV parity |
| RI-002 | every structured `boundary.against_capabilities[].id` resolves | blocking | CR-29 governance-grade rationale pairs |
| RI-003 | structured-boundary entries carry non-empty `rationale` | blocking | same |
| RI-004 | registry-declared relationship types are expressible in the schema | finding (reported, not failing) | the R-1 gap — recorded, never silently converted into a rule |
| RI-005 | typed assertions: type within the registry canonical set; rationale non-empty; id resolves; no target asserted in both forms in one record | blocking | CR-DEA-BC-53 typed form |

Deliberately **not** imposed (no authority): universal acyclicity; reciprocity; prohibition of self-reference (none exists; if one appears it is a semantic-review item, not an automatic failure — recorded as a warning-level observation).

## 4. Findings register

| Finding | Status | Disposition |
|---|---|---|
| Registry ES-003 types not expressible (bare-list pattern) | **Resolved 2026-10-28 (CR-DEA-BC-53)** — schema oneOf + registry `type_field` + ES-003 config fix | Residual: population evidence (72 associations untyped; typing requires per-assertion evidence via future CR) |
| Reciprocity gap: 40 of 72 directed references lack a recorded reverse reference | Observed, not a defect | The model does not require reciprocity; semantic review may assess case-by-case; no action without a model decision |

## 5. Generated views

Views consume only canonical relationship data (CR-47 contracts). `RELATED-CAPABILITIES.md` renders `related_capabilities` and `boundary.against_capabilities` as recorded associations with the untyped limitation stated; the gate's findings are the drift backstop.

## 6. Maintenance

Run `python scripts/check_relationship_integrity.py --strict` (CI-enforced). Any new relationship representation requires: inventory entry here, integrity rule if deterministic, and — if it changes semantics — R-1 or a successor model CR.
