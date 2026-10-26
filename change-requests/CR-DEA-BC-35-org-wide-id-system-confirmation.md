# CR-DEA-BC-35: Org-Wide ID System Confirmation (BC-mv1 follow-up audit)

**Status**: Applied (2026-10-13)
**Layer**: Catalog (business capabilities); id-system governance
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-13
**Trigger**: User directive 2026-10-13, eaojnr: "i'd like to confirm if the ID system for business capabilities can leverage the orgwide id system implemented. As a rule, seed these as cards to work on and then let's review the plan of work." User ratified 2026-10-13 with "go".
**Recon**: `catalog-research/recon/INV-BC-35-v0.1.yaml`
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-35-org-wide-id-system-confirmation`. PR review (not direct-push).

## 1. Summary

The business-capability catalog's id system is already on the org-wide id system. CR-DEA-BC-mv1 (2026-09-21) implemented the migration; the audit at this CR confirms the migration is end-to-end (catalog content; PR review; release-cut procedure). No new id changes are needed. The deliverable is a 1-doc addition (`docs/ORG-WIDE-ID-SYSTEM.md`) that captures the current posture explicitly so that future waves land on the documented system.

## 2. Audit findings (6)

1. **F1 — Canonical id format**: All 29 canonical entries use the post-mv1 id format (`capabilities:capability-<slug>-<hash>`, hash per `dea-metaframework/docs/id-system.md` section 2.5). 29/29 PASS.
2. **F2 — Candidate id format**: The candidates register has 37 records: 27 active CAPABILITY; 3 CAPABILITY-CANONICAL (CAND-005, -007, -008 retired as already-canonical at CR-DEA-BC-27 and CR-DEA-BC-32); 1 MERGED-INTO-CAND-005 (CAND-006 retired as merged at CR-DEA-BC-30); 6 non-CAPABILITY.
3. **F3 — Structured cross-references**: 0 legacy `dea:capability-*` references in structured cross-reference fields (related_capabilities, ecf, aliases, non_examples, specialization) across all 29 canonical entity YAMLs.
4. **F4 — IDM-001..008 gate**: `scripts/check_id_system.py` is present (12235 bytes; IDM-001..008 all referenced). Local run: exit 0; `ID System (CR-DEA-BC-mv1 IDM-001..007): CONFORMANT; Records checked: 29; Findings: 0`. CI workflow runs the gate in `--strict` mode on every push and PR.
5. **F5 — Migration id map**: `reconciliation/migration-id-map.yaml` is at version 3, namespace `capabilities`, with 38 id_map entries and 11 known_residuals. The map is idempotent; new admissions add entries; new known_residuals append. Last extended 2026-10-12 (CR-DEA-BC-32/BC-30/BC-27 batch).
6. **F6 — Cross-repo coordination**: The `dea-catalog-release-cut` skill (CR-DEA-BC-36 §11) records the cross-repo coordination pitfall: any release that lands a `capabilities:*` id set change or moves the ECF version triggers the sweep at CR-DEA-BC-36 §3 for the next cut cycle.

## 3. Decision

**Confirmation: no migration needed.** The catalog's id system is on the org-wide id system. The deliverable is `docs/ORG-WIDE-ID-SYSTEM.md` (a 1-doc addition that captures the current posture explicitly).

## 4. Changes

- `docs/ORG-WIDE-ID-SYSTEM.md`: new doc. 9 sections covering: the post-mv1 id format (canonical + candidate + view); the CR-DEA-BC-mv1 migration; the current posture (29 canonical; 37 candidates; IDM-001..007 CONFORMANT; 0 legacy refs in structured fields); worked example of a new admission (EPM at CR-DEA-BC-23); worked example of a retirement (CAND-006 at CR-DEA-BC-30); what the gates enforce (IDM-001..008); cross-repo coordination (the 8 sibling repos); open follow-ons; references.
- `catalog-research/recon/INV-BC-35-v0.1.yaml`: new recon document. 6 audit findings + decision + follow-ons + cross-references.

## 5. Gates

All 7 PASS post-change: check_naming.py, check_versions.py, check_ecf_conformance.py, check_view_refs.py, check_visual_domain_labels.py, check_catalog_index.py, check_id_system.py. CATALOG.yaml regenerated (32 entities; 29 canonical).

## 6. Cross-references

- `catalog-research/recon/INV-BC-35-v0.1.yaml` (the full audit)
- `change-requests/CR-DEA-BC-mv1.md` (the migration; the source of the post-mv1 id format)
- `reconciliation/migration-id-map.yaml` (v3; 38 id_map entries; 11 known_residuals)
- `reconciliation/cross-check-mv1.md` (the 52-artifact audit at CR-DEA-BC-mv1)
- `scripts/check_id_system.py` (IDM-001..007 + IDM-008)
- `dea-metaframework/docs/id-system.md` (the upstream spec)
- `dea-metaframework/docs/entity-storage-layout.md` (the upstream flat-layout spec)
- `change-requests/CR-DEA-BC-36-release-history-reset-and-discipline.md` §11 (the cross-repo coordination pitfall)
