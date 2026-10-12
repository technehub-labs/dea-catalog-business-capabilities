# CR-DEA-BC-27: CAND-005/CAND-006 unification (re-evaluation under G5)

**Status**: Applied (2026-10-12); CAND-005 retired (N-025); CAND-006 unification remains deferred (N-026); 1 follow-on CR queued (BC-30)
**Recon**: `catalog-research/recon/INV-BC-27-v0.1.yaml`
**Filed**: 2026-10-12
**Author**: Coder (for eaojnr)
**Carrier documents**: `catalog-research/recon/INV-BC-27-v0.1.yaml`, `catalog-research/normalization.yaml` (N-025/N-026/N-027/N-028 added), `catalog-research/candidates.yaml` (CAND-005 retired)

## Summary

Re-evaluation of the CAND-005/CAND-006 unification question. CAND-005 is already admitted; CAND-006 unification is blocked on gap G5.

## Findings

1. CAND-005 (Customer Management) is already a canonical first-order capability (capabilities:capability-customer-management-f3n8wb, admitted at v1-alpha.0 on 2026-09-02). The candidate record in candidates.yaml is stale. N-025 records the retirement.

2. CAND-006 (Citizen / Member Relationship) remains open at E2 with low confidence. G5 (government reference models: GRM, GSRM) is still OPEN in evidence-register.yaml. BC-27 cannot resolve the unification question without G5. N-026 records the deferral continuation.

3. dea-metaframework v2.5.0 alignment: ECF Domain 4 (party-relationship) is the correct ECF home for any future CAND-006 admission. The distinction from Customer Management is in the business_object (Citizen vs Customer), not the cell placement.

4. CAND-005 retirement action: marked CAND-005 as CAPABILITY-CANONICAL in candidates.yaml; added canonical_id pointer; added promotion_history entry for the retirement; bumped universe_version 0.5.2 -> 0.5.3.

## Follow-ons

- CR-DEA-BC-30: Close gap G5 -- retrieve GRM and GSRM; re-evaluate CAND-006 unification; admission CR if evidence rises to E3. Estimated scope: 4-8 hours of research; 1 normalization decision; 1 admission CR or 1 deferred verdict; 1 PR.

## Cross-references

- `catalog-research/recon/INV-BC-27-v0.1.yaml` (the full recon)
- `catalog-research/normalization.yaml` (the normalization decisions)
- `submittal-reviews/BC-SR-A001.md` (the original review; for BC-28)
- `dea-metaframework/CHANGELOG.md` v2.0.0..v2.5.0 (for BC-26)
- `change-requests/CR-DEA-BC-{14,19,23,25}.md` (the prior slices in this batch)
