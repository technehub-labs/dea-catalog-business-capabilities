# Taxonomy: Structure, Naming, Alias Policy

Structure and naming rules for the first-order catalog, established by **CR-DEA-BC-01**. Normative for entry naming, alias handling, hierarchy, and specialization structure.

---

## 1. Naming rules

1. **Ability noun phrases.** A capability name names an enduring ability: `Customer Management`, `Financial Stewardship`, `Workforce Acquisition`. It never names work: `Invoice Customer` is a process name and fails the Ability test.
2. **Business-object anchored.** The name's object is the business object the ability is concerned with (Customer, Workforce, Asset, Information). Decomposition retains the parent's object focus.
3. **Implementation-free.** Names contain no organization, system, vendor, or technology reference (`CRM`, `Department`, `Platform` are disqualifying markers).
4. **Outcome-free.** Names do not name results (`Customer Satisfaction` is an outcome, not a capability).
5. **Industry-free at first order.** No industry qualifier appears in a first-order name. `Telecom Customer Management` lives in a specialization view, not here.
6. Names use plain business vocabulary; archaic process-maturity-era coinages are avoided in favor of terms a modern digital enterprise actually uses.

## 2. Alias policy

1. Alternate names for the same underlying ability are recorded in the entry's `aliases` field. An alias never becomes a separate entry.
2. Alias reconciliation is a normalization decision (`N-NNN`), recorded in the normalization register with evidence. No merge occurs solely because names are similar; the underlying ability must be shown to be the same.
3. Dissolved candidates keep their `CAND-NNN` ID with disposition recorded (N-008 precedent: CAND-011 dissolved, CAND-012 re-rooted). IDs are never reused.
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
| Canonical entries | ID assigned at admission; one file per entry, `entities/v1-alpha/capability-<slug>.yaml` (per CR-DEA-BC-03 schema, when landed) |
| Research artifacts | Dual delivery: YAML register + Markdown summary, versioned together |

## 6. Repository structure

Current (post CR-DEA-BC-01 Phase 1):

```
dea-catalog-business-capabilities/
├── metamodel-pointer.yaml     ← allocation (auto-generated, do not edit)
├── README.md
├── METHODOLOGY.md             ← the method (this Phase 1 set)
├── EVIDENCE.md
├── GOVERNANCE.md
├── TAXONOMY.md
├── change-requests/           ← landed CRs + index
├── docs/
│   ├── FOUNDATIONS.md         ← rationale and decision register
│   └── research/              ← CR-DEA-BC-02 artifacts (YAML + MD)
└── .github/workflows/
    └── validate-allocation.yml
```

Planned (later phases, indicative): `entities/v1-alpha/`, `schemas/`, `mappings/ecf/`, `mappings/specializations/`, `mappings/synonyms/`. Adoption is reconciled with catalog-wide conventions before any directory is created; nothing here pre-empts CR-DEA-BC-03.

## 7. References

- Method: [`METHODOLOGY.md`](METHODOLOGY.md)
- Naming decisions in force: `docs/research/normalization.yaml`
- Record shape: [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md) §12 as amended by CR-DEA-BC-01A
