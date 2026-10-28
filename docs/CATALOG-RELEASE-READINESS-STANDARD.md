# Catalog Release Readiness Standard

**Status**: Normative (CR-DEA-BC-52, 2026-10-28)
**Evidence instrument**: the [Catalog Integrity Report](reports/CATALOG-INTEGRITY-REPORT.md) (CR-51; regenerate at the assessed revision)
**Existing policy remains authoritative**: [VERSIONING.md](VERSIONING.md) and [release-cut-procedure.md](release-cut-procedure.md) govern versions, tags, cuts, and signing; the post-reset posture per CR-DEA-BC-36 (no tags until the first post-reset cut) stands. This standard adds the readiness **decision layer** only. Landing this CR declares no release.

---

## 1. Principles

Evidence-based (actual validation results + the evaluated source state) · purpose-specific (the intended release class is stated; distinctions between release classes are only those the existing policy permits) · blocking findings cannot be concealed (they prevent a positive decision unless a formally authorized exception governs them) · exceptions are explicit (finding, authority, rationale, scope, publication conditions) · the evaluated state is reproducible (revision + evidence) · existing release governance is untouched.

## 2. Readiness criteria (each mapped to its authoritative evidence)

| # | Dimension | Required evidence | Blocking? |
|---|---|---|---|
| C-1 | Canonical inventory integrity | Integrity report: index freshness + catalog-index schema rows | yes |
| C-2 | Schema and identity conformance | Integrity report: schema, id-system (IDM), entity-system (ES) rows; entry-level schema validation green in CI (`validate`) | yes |
| C-3 | Documentation conformance | Integrity report: DCV row (0 blocking); remediation inventory current | yes |
| C-4 | Relationship and reference integrity | Integrity report: RI row (0 findings); DL-001 row | yes |
| C-5 | Governance traceability | authorship (AUT) row; CR-index row (0 open ≠ required — open CRs disclosed, not blocking by themselves); lifecycle decisions per CR-49 recorded | yes (AUT/CR-index) |
| C-6 | Generated-artifact freshness | views-freshness row; CATALOG freshness row (C-1) | yes |
| C-7 | CI on the evaluated revision | the six workflows green on the exact commit under assessment | yes |
| C-8 | Outstanding findings disclosed | unresolved semantic-review items, warnings (e.g. naming advisories), RI-004/R-1, U-1/U-2 dependencies listed | disclosure (not inherently blocking) |
| C-9 | Reproducibility | report's source revision == evaluated commit; report regenerated at that revision | yes |
| C-10 | Versioning alignment | the release follows VERSIONING.md + release-cut-procedure.md (tag format, verification contract, GPG signing, prior-cut history) | yes |

**Explicitly not readiness criteria**: semantic quality of every capability (human-review dimension — disclosed, never "passed" structurally); absence of all warnings (warnings are disclosed; only governed exceptions can cover a *blocking* finding); calendar (no date-driven readiness).

## 3. Decision vocabulary

| State | Meaning |
|---|---|
| **Ready** | all blocking criteria satisfied at the evaluated revision |
| **Ready with approved exceptions** | blocking criteria satisfied except findings governed by recorded exceptions (finding, authority, rationale, scope, conditions) |
| **Not ready** | ≥1 blocking condition unresolved |
| **Not assessed** | no completed readiness assessment exists for the state in question |

## 4. Checklist (12 steps, per CR-52 §8)

1. ☐ Evaluated source state identified (commit SHA; matches the integrity report's stamp).
2. ☐ Inventory integrity assessed (C-1).
3. ☐ Schema and identity checks completed (C-2).
4. ☐ Documentation conformance results available (C-3).
5. ☐ Relationship and reference integrity assessed (C-4).
6. ☐ Governance and lifecycle decisions traceable (C-5).
7. ☐ Generated outputs current or excluded from the release (C-6).
8. ☐ Blocking findings resolved or under formally authorized exceptions.
9. ☐ Unresolved semantic decisions disclosed (C-8).
10. ☐ The validation report is reproducible (C-9: regenerate at the revision).
11. ☐ Versioning and release steps follow the existing policy (C-10).
12. ☐ The decision recorded through governance (template below; CR or release-cut record).

## 5. Decision record

Use [`docs/templates/RELEASE-READINESS-DECISION-RECORD.md`](templates/RELEASE-READINESS-DECISION-RECORD.md): evaluated state, release purpose, evidence reviewed (integrity report + CI runs), blocking findings, exceptions, outstanding non-blocking findings, decision + authorization, limitations. Failed assessments record the blocking conditions and their owning CRs/processes; **reassessment always evaluates the updated state** — earlier results are never reused for a materially different state without justification (§9 of the CR).

## 6. Current posture (at this CR's landing — informational, not a decision)

The catalog has not been assessed for release under this standard (state: **Not assessed**). The first release cut remains governed by release-cut-procedure.md under the post-reset posture (no tags since the CR-DEA-BC-36 withdrawal). When a cut is intended: regenerate the integrity report at the tip commit, complete the checklist, record the decision.
