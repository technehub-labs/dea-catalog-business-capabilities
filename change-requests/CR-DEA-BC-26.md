# CR-DEA-BC-26: OpenDEA model re-pinning audit (catalog v1-alpha)

**Status**: Applied (2026-10-12); recon complete; 0 blocking drift; 2 follow-ons queued (BC-29a, BC-29b)
**Recon**: `catalog-research/recon/INV-BC-26-v0.1.yaml`
**Filed**: 2026-10-12
**Author**: Emmanuel A. Otchere
**Carrier documents**: `catalog-research/recon/INV-BC-26-v0.1.yaml`, `catalog-research/normalization.yaml` (N-025/N-026/N-027/N-028 added), `catalog-research/candidates.yaml` (CAND-005 retired)

## Summary

Audit of all 29 canonical entries against the metamodel_pin: 1.0.0 contract and the dea-metaframework v2.5.0 framework.

## Findings

1. All 29 entries pass the 16-field required shape check (id, name, version, metamodel_pin, lifecycle_status, capability_layer, outcome, business_object, ecf, ecfConformance, related_capabilities, evidence, provenance, boundary, definition, type).

2. metamodel_pin is uniformly 1.0.0 across all 29 entries; ecfConformance.profile is uniformly dea:ecf@1.0.0.

3. capability_layer values are all in the governed enum (strategic | operational | support).

4. lifecycle_status is uniformly active.

5. version values are semver-conformant (9 distinct values: 1.0.0, 1.0.1, 1.0.2, 1.1.0, 1.1.1, 1.2.0, 1.3.0, 1.3.1, 2.0.0).

6. 28 of 29 entries carry the 5 'rich-narrative' fields (non_examples, specialization, specialization_boundary, ecf_rationale, why_capability). EPM (admitted at BC-23) is the only entry without them. This is the 1 entry-shape drift.

7. metamodel_pin: 1.0.0 is a catalog-internal pin to the v1-alpha shape contract; it is not a pin to a dea-metaframework version (which went 2.0.0 -> 2.5.0 with no 1.x ever released). The docs (VERSIONING.md section 1.4) are ambiguous on this; the actual usage is consistent. This is the 1 docs ambiguity.

8. dea-metaframework v2.5.0 (2026-09-08) is the framework version. The catalog is dea-metaframework-2.5.0-compatible at the ECF level (kebab-case enablement-operations works via the deprecation alias resolution). The metamodel_pin mismatch is a docs issue, not a data issue.

## Follow-ons

- CR-DEA-BC-29a: EPM backfill -- add the 5 legacy narrative fields to capability-enterprise-performance-management-5fxren to restore shape consistency. Estimated scope: 1 entity YAML update, ~50-100 lines of content.
- CR-DEA-BC-29b: docs/VERSIONING.md amendment -- clarify metamodel_pin semantics (catalog-internal shape contract, not dea-metaframework release pin). Estimated scope: 1 docs section update.

## Cross-references

- `catalog-research/recon/INV-BC-26-v0.1.yaml` (the full recon)
- `catalog-research/normalization.yaml` (the normalization decisions)
- `submittal-reviews/BC-SR-A001.md` (the original review; for BC-28)
- `dea-metaframework/CHANGELOG.md` v2.0.0..v2.5.0 (for BC-26)
- `change-requests/CR-DEA-BC-{14,19,23,25}.md` (the prior slices in this batch)
