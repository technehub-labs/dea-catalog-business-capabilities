# Taxonomy: Structure, Naming, Alias Policy

Structure and naming rules for the first-order catalog, established by **CR-DEA-BC-01**; section 1 clarified and section 1A added by **CR-DEA-BC-09** (2026-09-08). Normative for entry naming, alias handling, definition shape, hierarchy, and specialization structure.

---

## 1. Naming rules

1. **Ability noun phrases.** A capability name names an enduring ability: `Customer Management`, `Financial Stewardship`, `Workforce Acquisition`. It never names work: `Invoice Customer` is a process name and fails the Ability test.
2. **Business-object anchored.** The name's object is the business object the ability is concerned with (Customer, Workforce, Asset, Information). Decomposition retains the parent's object focus. Clarification (CR-DEA-BC-09): anchoring is semantic, not literal token containment. The name identifies the object class the ability manages. Literal containment is not required where the plain-vocabulary name of the ability-domain is the standard corpus term (N-001 precedent: Workforce Management; N-015 precedent: Security Management). Conversely, a name whose head noun is a state, quality, act, or outcome rather than the object class fails anchoring (N-010: Compliance -> Regulation; N-014: Resilience -> Continuity), as does a name that carries only the object's adjective (N-011: Financial -> Financial Resource; N-013: Legal -> Legal Matter).
3. **Implementation-free.** Names contain no organization, system, vendor, or technology reference (`CRM`, `Department`, `Platform` are disqualifying markers).
4. **Outcome-free.** Names do not name results (`Customer Satisfaction` is an outcome, not a capability). A state or quality the enterprise has (Compliance, Resilience) is outcome-adjacent and likewise disqualifying as the head noun; the name must anchor on the object the ability manages.
5. **Industry-free at first order.** No industry qualifier appears in a first-order name. `Telecom Customer Management` lives in a specialization view, not here.
6. Names use plain business vocabulary; archaic process-maturity-era coinages are avoided in favor of terms a modern digital enterprise actually uses.

## 1A. Definition and outcome shape (CR-DEA-BC-09)

1. **Definition template.** The `definition` field is a single sentence of the form "The ability to <verb-phrase> ...", naming the business object the ability concerns (or the object's plain-vocabulary domain term), and naming the scope of the ability. It contains no organization, system, vendor, or technology reference, and no outcome language (what results is the `outcome` field's job).
2. **Outcome shape.** The `outcome` field is a result sentence describing the state that obtains when the ability operates. It never restates the ability ("the ability to ..." in the outcome field fails the test).
3. **Machine enforcement.** `scripts/check_naming.py` enforces rules 1.1-1.5 structurally (verb-led detection, disqualifying markers, outcome markers, industry qualifiers) and section 1A.1 (definition opens "The ability to "; single sentence) at CI time. Rule 2 anchoring and rule 6 plainness remain semantic-review judgments (METHODOLOGY.md section 12, Gate 1); the lint's object-anchoring heuristic is advisory only.

## 2. Alias policy

1. Alternate names for the same underlying ability are recorded in the entry's `aliases` field. An alias never becomes a separate entry. A retired former canonical name is recorded as an alias (CR-DEA-BC-09: N-010..N-014 renames; the former names remain resolvable history).
2. Alias reconciliation is a normalization decision (`N-NNN`), recorded in the normalization register with evidence. No merge occurs solely because names are similar; the underlying ability must be shown to be the same. A canonical rename is likewise a normalization decision (N-010..N-014 precedent).
3. Dissolved candidates keep their `CAND-NNN` ID with disposition recorded (N-008 precedent: CAND-011 dissolved, CAND-012 re-rooted). IDs are never reused. A renamed capability keeps its `CAND-NNN` lineage; the entry `id` moves with the canonical name (TAXONOMY section 5 ties id to slug), and the former id is not reused.
4. A source-specific name (APQC, BIZBOK, vendor) cited as evidence stays in the evidence register; the canonical name is decided by Section 1, independent of any source's naming.

## 3. Hierarchy rules

1. A capability may have subordinate capabilities (`children`) when it passes the Decomposability test: subordinates must themselves satisfy the Ability test and retain the parent's business-object focus.
2. The hierarchy stays shallow by design. Depth below the first-order set is provided by ECF recursion (any cell may decompose into a further 7×7), not by an enormous flat subdivision tree inside the catalog.
3. Grouping parents are permitted where a cluster of candidates shares one enduring ability at first order (N-007 precedent: CAND-004 as grouping parent). A grouping parent must pass the full admission method like any other entry.

## 4. Specialization structure

| Level | Population | Rules |
|---|---|---|
| L1 | First-Order Business Capability | This catalog. Enterprise-general only. |
| L2 | Enterprise / Domain Specialization | Specialization views. Reference the L1 parent. |
| L3 | Industry / Sector Specialization | Specialization views (first: Mobile Communications Service Provider, CR-DEA-BC-04). Reference the parent chain. |
| L4 | Organization-Specific Capability | The adopting enterprise. Never upstreamed. |

Specializations reference parents; they never modify or replace them. A specialization view is a derived consumer of this catalog, version-pinned, in the same sense that this catalog is a derived consumer of the OpenDEAM root model.

## 5. Identifier and file conventions

| Item | Convention |
|---|---|
| Research candidates | `CAND-NNN` (candidate universe; never reused) |
| Sources | `SRC-NNN` (evidence register) |
| Normalization decisions | `N-NNN` (normalization register) |
| Canonical entries | ID `dea:capability-<slug>`; one file per entry, `entities/v1-alpha/capability-<slug>.yaml` (CR-DEA-BC-03 schema) |
| Specializations | `SPEC-NNN` (three digits, sequential; register: `docs/research/specialization-register.yaml`); exist only inside views |
| Specialization views | `mappings/specializations/view-<sector>-<name>.yaml`; view id `view-<sector>-<name>` (CR-DEA-BC-04) |
| Research artifacts | Dual delivery: YAML register + Markdown summary, versioned together |

## 6. Repository structure

Current (post CR-CATALOG-STRUCT-03a/03b, per-entity subtree layout):

```
dea-catalog-business-capabilities/
├── metamodel-pointer.yaml     ← allocation (auto-generated, do not edit)
├── README.md
├── METHODOLOGY.md             ← the method set (CR-DEA-BC-01 Phase 1)
├── EVIDENCE.md
├── GOVERNANCE.md
├── TAXONOMY.md
├── CATALOG.yaml               ← regenerated index (CR-CATALOG-STRUCT-06a; never hand-edited)
├── dependencies.yaml          ← pin manifest (CR-DEA-BC-05)
├── change-requests/           ← landed CRs + index
├── schemas/                   ← entity + specialization-view schemas, fixtures (CR-DEA-BC-03/04)
├── entities/v1-alpha/         ← the canonical 26, one subtree per entry
│   └── dea:capability-<slug>/
│       ├── dea:capability-<slug>.yaml
│       ├── candidates/        ← state directory
│       ├── retired/           ← state directory
│       └── research/          ← per-entity research (e.g., boundary decisions)
├── mappings/specializations/  ← views (CR-DEA-BC-04; first: MCSP)
├── catalog-research/          ← CR-DEA-BC-02 artifacts (YAML + MD, dual delivery)
├── visuals/                   ← data-derived SVGs (CR-DEA-BC-02 §34)
├── docs/
│   ├── FOUNDATIONS.md         ← rationale and decision register
│   └── VERSIONING.md          ← bump rules and pin scheme (CR-DEA-BC-05)
└── .github/workflows/         ← allocation, entries, conformance, catalog-conformance,
                                 publication
```

Still planned, indicative: `mappings/ecf/`, `mappings/synonyms/`. Adopted only when a CR creates them.

## 7. References

- Method: [`METHODOLOGY.md`](METHODOLOGY.md)
- Naming decisions in force: [`catalog-research/normalization.yaml`](catalog-research/normalization.yaml) (N-001..N-015)
- Record shape: [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md) §12 as amended by CR-DEA-BC-01A
