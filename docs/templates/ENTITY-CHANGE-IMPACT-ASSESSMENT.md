# Entity Change Impact Assessment

<!-- CR-DEA-BC-50 reusable template. Attach to (or embed in) any CR that materially
     changes a canonical entity. Replace {{placeholders}}; keep "no impact identified"
     lines WITH their because-clauses — an honest null is a finding, not an omission.
     Categories, dimensions, and escalation rules: docs/ENTITY-CHANGE-IMPACT-STANDARD.md -->

- **Change identifier:** {{CR-DEA-BC-NN}}
- **Target entity/artefact:** {{id or path}}
- **Current state:** {{…}}
- **Proposed state:** {{…}}
- **Change category:** {{editorial | record-structure | semantic | relationship | lifecycle | identity | governance}} (multiple only with per-category acceptance)
- **Affected entities and artefacts:** {{records · READMEs · indexes · views · registers · gates}}

## Impact dimensions (state each: impact, or "no impact identified, because …")

| Dimension | Assessment |
|---|---|
| Semantic | {{…}} |
| Identity | {{…}} |
| Relationships | {{…}} |
| Documentation | {{…}} |
| Evidence | {{…}} |
| Validation | {{…}} — name the schema/gate authority for any new field value BEFORE landing |
| Lifecycle | {{…}} |
| Derived views | {{…}} (regenerate; freshness gate will fail otherwise) |
| Consumers | {{…}} (unknown is an acceptable, recorded answer) |
| Migration | {{…}} (no fabricated values, ever) |

- **Evidence supporting the assessment:** {{…}}
- **Required approvals:** {{CR review; semantic review; org-wide (identity)…}}
- **Verification requirements:** {{gate commands to run before merge}}
- **Known uncertainties:** {{…}}
- **Deferred work and owning CR:** {{…}}
