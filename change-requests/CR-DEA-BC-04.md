# CR-DEA-BC-04: Industry Specialization Framework and First View (MCSP)

| Field | Value |
|-------|-------|
| **CR** | CR-DEA-BC-04 |
| **Title** | Industry Specialization Framework and First View: Mobile Communications Service Provider |
| **Status** | Draft: awaiting review, then "Proceed" to land as proposal PR |
| **Author** | Coder (for eaojnr) |
| **Date** | 2026-09-01 |
| **Depends on** | CR-DEA-BC-01 (method, accepted), CR-DEA-BC-02 (specialization register v0.1, landed), CR-DEA-BC-03 (schema + CI, landed), the canonical 23 (admitted 2026-09-01) |
| **Boundary** | This catalog only. L1 entries are immutable to views; L4 organization-specific capability instances (OTCHERE and others) live downstream with adopters and never enter this repository. |

## 1. Context

The L1 catalog is populated (23 canonical first-order capabilities). The method (TAXONOMY.md section 4) already frames specialization: views at L2 (enterprise/domain) and L3 (industry/sector) are derived, version-pinned consumers that reference parents and never modify or replace them. The specialization register (BC-02, section 33.9) holds the first candidates: SPEC-001 Telecom Customer Management, SPEC-002 Citizen/Member Relationship (deferred, G5-gated), SPEC-003 Claims Management (parent undetermined).

What does not yet exist is the **framework**: the view record shape, the admission and evidence rules for specializations, the schema and CI that make views machine-checkable, and the proving instance. This CR establishes the framework and ships the first view: Mobile Communications Service Provider (MCSP), the proving ground named since TAXONOMY.md section 4.

## 2. Decisions

- **D1: Views are first-class mapping artifacts.** A view lives at `mappings/specializations/<view-id>.yaml` with a human-readable companion. A view never edits, shadows, or replaces an L1 entry; it references parents by id.
- **D2: Specialization record shape.** Each specialization carries: `id` (SPEC-NNN family, registered in TAXONOMY.md section 5), `parent` (a capability id or parent specialization id), `level` (L2 or L3), `sector`, `name` (industry vocabulary permitted below L1; TAXONOMY.md section 1 rule 5 governs L1 only), `definition_delta` (what the sector narrows or adds), `evidence` (sources + E-rating, per EVIDENCE.md), `status` (candidate or admitted), optional `aliases`.
- **D3: Version pinning.** Each view records the catalog version it was built against. Catalog patch and minor bumps never invalidate views; a major bump triggers view review. Views state compatibility, never enforce it on the catalog.
- **D4: Schema and CI.** `schemas/specialization-view.schema.json` defines the view format; CI extends the org convention (dsanders11/json-schema-validate-action@v2.1.0) with a view-validation job and a fixture. Referential integrity (parent ids resolve, within the catalog or within the view) is checked by the validator step.
- **D5: Evidence discipline.** Sector reference models (TM Forum business frameworks, BIAN, ACORD, sector government models) are evidence, not authority (EVIDENCE.md stance applies unchanged). Every admitted specialization names its sector sources with an E-rating; the anti-invention test applies per specialization: a specialization is recorded because the industry evidence demonstrates it, not because a framework sells it.
- **D6: ECF inheritance.** Specializations inherit parent coordinates. A view may record industry-specific participation notes; it never contradicts the parent mapping. A held-unmapped parent propagates held-unmapped unless the view carries affirmative sector evidence, which is recorded with rationale.
- **D7: MCSP as proving instance.** The implementation phase ships `mappings/specializations/view-telecom-mcsp.yaml`: it consumes SPEC-001, maps the canonical 23 to MCSP vocabulary where sector evidence supports specialization, and records industry-only additions as view-local candidates with their own evidence trail. The boundary tests apply per specialization: a network operations capability whose object is technology fails the business-object test and is rejected from the view, not smuggled in.
- **D8: Deferred items stay deferred.** SPEC-002 remains gated on G5 (government reference models). SPEC-003 remains parent-undetermined; the MCSP view does not force a parent for it.

## 3. Changes (implementation phase, one PR after acceptance)

1. `schemas/specialization-view.schema.json` + fixture.
2. CI: view-validation job wired into the existing entry-validation workflow; referential-integrity check.
3. `mappings/specializations/README.md`: view conventions.
4. `mappings/specializations/view-telecom-mcsp.yaml` + companion doc (the proving instance).
5. `TAXONOMY.md` amendment: section 5 registers the SPEC-NNN and view-id families; the stale "planned, indicative" structure line is corrected (entities/ and schemas/ exist since CR-DEA-BC-03).

## 4. Acceptance criteria

1. The view schema validates the MCSP view and its fixture; referential integrity to the canonical 23 holds.
2. SPEC-001 appears in the MCSP view as admitted, with sector evidence and E-rating.
3. No L1 entry is modified by the view; every specialization references a resolvable parent.
4. TAXONOMY.md section 5 records both ID families; the stale structure line is corrected.
5. No organization-specific (L4) content appears anywhere in the repository.

## 5. Definition of Done (this proposal PR)

Exactly two files: this CR (verbatim) and the change-requests index row. The framework + view implementation is the immediately following phase PR.

## 6. References

TAXONOMY.md section 4 (specialization structure); METHODOLOGY.md sections 4 and 11; EVIDENCE.md; `docs/research/specialization-register.yaml` v0.1; `docs/research/RESEARCH-REPORT-v0.1.md` section 12; CR-DEA-BC-02 section 29 (industry specialization analysis).
