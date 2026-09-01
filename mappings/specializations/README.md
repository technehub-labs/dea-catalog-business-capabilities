# Specialization Views

Derived, version-pinned consumers of the first-order catalog (TAXONOMY.md section 4; CR-DEA-BC-04). A view records how an industry or domain specializes the canonical capabilities. **Views never modify, shadow, or replace L1 entries.**

## View conventions

- **File**: `view-<sector>-<name>.yaml`, one view per file.
- **IDs**: view ids `view-<sector>-<name>`; specialization ids from the SPEC-NNN family (TAXONOMY.md section 5).
- **Parents**: every specialization references a canonical capability id or a parent specialization id; CI enforces referential integrity (`scripts/check_view_refs.py`).
- **Coverage accounting**: `specializations` + `inherited` should account for the full canonical set; gaps are stated, not silent.
- **Evidence**: sector references are evidence, not authority (EVIDENCE.md). Each admitted specialization carries sources and an E-rating.
- **Rejections are records**: candidates that fail the boundary tests (typically the business-object test) are listed under `rejected` with the reason, so the discipline is visible.
- **Deferred items** stay deferred with their triggers; a view does not force them.

## Views

| View | Sector | Specializations | Inherited | Status |
|---|---|---|---|---|
| [view-telecom-mcsp](view-telecom-mcsp.yaml) | Telecommunications (mobile services) | 4 admitted | 19 | v0.1 proving instance (CR-DEA-BC-04) |

## Validation

- Schema shape: `schemas/specialization-view.schema.json` via the org-convention action in `validate-entries.yml`.
- Referential integrity: `scripts/check_view_refs.py` (parents resolve to the catalog or within the view; inherited ids resolve to the catalog).
