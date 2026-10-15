# CR-DEA-BC-28: BC-SR-A001 P1 backlog re-audit (4 remaining P1 items post-BC-23)

**Status**: Applied (2026-10-12); 2 of 3 P1 items closed (OrgDesign at BC-14; EPM at BC-23); 1 P1-P2 item reclassified to P2 (N-027); 1 P3 item retired (N-028); 1 follow-on CR queued (BC-30)
**Recon**: `catalog-research/recon/INV-BC-28-v0.1.yaml`
**Filed**: 2026-10-12
**Author**: Emmanuel A. Otchere
**Carrier documents**: `catalog-research/recon/INV-BC-28-v0.1.yaml`, `catalog-research/normalization.yaml` (N-025/N-026/N-027/N-028 added), `catalog-research/candidates.yaml` (CAND-005 retired)

## Summary

Re-audit of the BC-SR-A001 P1/P2/P3 list. The P1 list is 100% resolved; the P2 list has 4 items (none blocking); the P3 list has 1 item and 1 retired.

## Findings

1. P1 Organizational Design: CLOSED 2026-09-11 under CR-DEA-BC-14. Canonical entry: capability-organizational-design-vanefq.

2. P1 Enterprise Performance Management: CLOSED 2026-10-12 under CR-DEA-BC-23. Canonical entry: capability-enterprise-performance-management-5fxren. BC-SR-A001 section 16 (closed-loop capability structure) satisfied.

3. P1-P2 Relationship Management: RECLASSIFIED to P2 (N-027). The P1 push was for the 28-canonical era; the 29-canonical era is the closed-cell era. The Relationship Management question is research-led, not admission-led.

4. P2 Knowledge Management: DEFERRED. No candidate. No TER. Research-led, not admission-led.

5. P2 Service Management: DEFERRED. No candidate. The post-BC-20 boundary between Service Management and Operations Management is implicit; an explicit decision would require a new TER.

6. P2 Quality Management: DEFERRED. No candidate. The H8 noun-as-ability rule (BC-20) treats Quality as a known outcome-state marker; a Quality Management canonical would need a review-retained verdict (N-024 mechanism extended at BC-25, but Quality is intentionally NOT in the GOVERNANCE_OBJECTS set).

7. P3 Stakeholder Management: DEFERRED. Likely specialization of Relationship Management (or post-N-018, alias for the CAND-004 grouping_parent).

8. P3 Enterprise Architecture Management: RETIRED (N-028). EAM is a model construct, not a first-order business capability. The dea-metaframework v2.5.0 is the metamodel; the catalog is a consumer; EAM is the management of the metamodel. The dea-architecture-framework repo is the cross-repo governance home.

## Follow-ons

- CR-DEA-BC-30: Close gap G5 -- retrieve GRM and GSRM; re-evaluate CAND-006 unification (parallel to BC-27 follow-on). Estimated scope: 4-8 hours of research; 1 normalization decision; 1 admission CR or 1 deferred verdict; 1 PR.

## Cross-references

- `catalog-research/recon/INV-BC-28-v0.1.yaml` (the full recon)
- `catalog-research/normalization.yaml` (the normalization decisions)
- `submittal-reviews/BC-SR-A001.md` (the original review; for BC-28)
- `dea-metaframework/CHANGELOG.md` v2.0.0..v2.5.0 (for BC-26)
- `change-requests/CR-DEA-BC-{14,19,23,25}.md` (the prior slices in this batch)
