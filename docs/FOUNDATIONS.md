# Foundations: First-Order Business Capability Catalog

Principles, decision points, and method direction for `dea-catalog-business-capabilities`. Derived from the catalog review (working folder: `dea-work/business-capabilities/00_inbox/biz-capability-review.md`). This document records direction; it does not constitute the catalog method. The method is established by **CR-DEA-BC-01: First-Order Business Capability Method**, which this document prepares.

---

## 1. The foundational rule: catalog ≠ matrix

The Business Capability Catalog and the Enterprise Composition Framework (ECF) answer different questions.

| Artifact | Question answered |
|---|---|
| Business Capability Catalog | What enduring abilities does an enterprise need to possess or establish to perform as an enterprise? |
| ECF (7 Domains × 7 Stages) | Where does a capability primarily operate within the enterprise's domain/lifecycle structure? |

Consequences:

- No 49 capability buckets are generated from 49 ECF cells.
- The ECF is an organizing framework; capabilities attach to cells. The framework does not require every cell to contain a capability.
- The ECF coordinate of a capability is classification context, not identity.

General principle for **all** DEA catalogs (capabilities, actors, resources, events, business objects, value streams, metrics, systems, information, patterns, guardrails):

> The ECF is the common coordinate system; each catalog contributes entities where its semantics legitimately intersect the framework. "Instantiated by" never means "every cell must be populated by every catalog."

## 2. Business Capability semantics

Canonical definition (candidate form, to be ratified by CR-DEA-BC-01):

> A capability is a durable ability of an enterprise to produce, enable, control, preserve or realize a meaningful business outcome, independent of the particular organization, process, people, technology or implementation used to realize it.

Consistent with the metamodel allocation (`dea:entity-capability`, L3-value-delivery: an ability the business possesses or requires to deliver value) and with OMG's Business Architecture Core Metamodel (ability to produce an outcome without specifying how).

## 3. First-order means something specific

> A First-Order Business Capability is sufficiently fundamental and enterprise-general to be recognized across materially different enterprises without requiring an industry-specific interpretation.

Specialization levels:

```
Level 1   First-Order Business Capability      (this catalog)
Level 2   Enterprise / Domain Specialization
Level 3   Industry / Sector Specialization     (specialization views)
Level 4   Organization-Specific Capability     (adopting enterprise, e.g. OpenDEA adoption)
```

Example: Customer Management → industry specialization → Telecom Customer Management. The telecom form never enters the first-order catalog.

## 4. What a capability is not

| Construct | Marker | Example | Correct home |
|---|---|---|---|
| Process / activity | describes work, a verb phrase | Invoice Customer; Hire Employee | Process catalog |
| Capability | enduring ability | Billing Management; Workforce Acquisition | This catalog |
| Organization | a grouping of people | Customer Service Department | Actor/organization constructs |
| System / technology | a mechanism | CRM System | System catalog |
| Outcome | a result, not an ability | Customer Satisfaction | Outcome/metric constructs |

The ECF itself recognizes Capability, Business Process, Actor and Resource as distinct constructs; the metamodel relates Business Capability to Business Process without equating them.

## 5. Possession semantics

An enterprise may not directly perform an activity (outsourcing) yet still carry the capability requirement. The catalog distinguishes:

```
Capability
   │
   ├── required    (the enterprise must have access to the ability)
   ├── possessed   (the ability exists in-house)
   ├── sourced     (the ability is obtained from outside)
   └── realized    (the ability is actually exercised)
```

This distinction becomes load-bearing for OpenDEA architecture adoption.

## 6. The Capability Evidence Ladder

Safeguard against invented capabilities. Passage is mandatory before canonical admission:

```
Candidate → Observed → Corroborated → Normalized → ECF Mapped → Reviewed → Canonical
```

| Stage | Meaning |
|---|---|
| Candidate | A proposed capability identified from research. |
| Observed | The concept occurs in credible enterprise/business architecture material. |
| Corroborated | It appears independently across multiple sources, industries, or enterprise contexts. |
| Normalized | Different names expressing substantially the same underlying ability are reconciled. |
| ECF Mapped | A defensible primary ECF coordinate is identified. |
| Reviewed | Semantic and architectural review passed. |
| Canonical | Admitted into the DEA first-order capability catalog. |

## 7. Admission tests

| Test | Question |
|---|---|
| Ability | Is this actually an ability rather than an activity? |
| Outcome | What meaningful outcome does it enable? |
| Durability | Would the ability remain recognizable if processes or technology changed? |
| Enterprise Relevance | Does it apply broadly across enterprises? |
| Implementation Independence | Can different organizations realize it differently? |
| Object Focus | What business object/domain is it concerned with? |
| Distinctness | Is it materially different from another capability? |
| Decomposability | Can it legitimately have subordinate capabilities? |
| Evidence | Do independent sources or real enterprise structures support it? |
| ECF Fit | Can it be placed in the ECF without distorting either model? |

A candidate failing **Ability**, **Outcome**, or **Implementation Independence** is not a capability.

## 8. Anti-invention test

Before acceptance, ask of the candidate:

> If an adopting enterprise changed its industry tomorrow, would this ability still make semantic sense as an enterprise capability?

| Answer | Classification |
|---|---|
| Yes | First-order candidate |
| Only within the industry | Industry-specific (specialization view) |
| Only for a particular implementation | Implementation-specific |
| Describes work | Process |
| Describes an organizational grouping | Organization |
| Describes a technological mechanism | System / Technology |
| Describes an outcome | Outcome |

## 9. Evidence strategy: research, not copy

Established bodies of knowledge are evidence sources, not templates:

- **APQC PCF**: explicitly a taxonomy of business processes, with cross-industry and industry-specific variants. Cross-industry material evidences recurring enterprise work from which capabilities are inferred; industry-specific material evidences specialization boundaries.
- **Business Architecture Guild**: capabilities as business building blocks, identified through value streams; capability defined as ability/capacity to achieve a purpose or outcome.
- **OMG business architecture material**: Business Capabilities as a distinct view alongside strategy, value streams, knowledge and organization; capability defined around ability to produce an outcome without specifying how.

Triangulation across independent sources grounds the catalog; no single framework is the semantic authority.

Evidence gathering spans materially different enterprise types (commercial, non-profit, government, professional services, manufacturing, retail, financial services, healthcare, technology, infrastructure) and asks: what abilities recur despite radically different business models?

## 10. Candidate lifecycle and record populations

Three distinct sets, so the research process stays visible:

| Set | Contents |
|---|---|
| Candidate Universe | Everything plausible discovered during investigation. |
| Normalized Capability Set | Duplicates, aliases, near-equivalents reconciled. |
| Canonical First-Order Set | Only capabilities passing the admission criteria. |

Candidate dispositions: `accepted` / `merged` / `rejected` / `deferred` / `specialized`. Rejected and deferred candidates are retained as evidence.

## 11. ECF overlay rules

1. Capabilities are derived from enterprise reality; ECF coordinates them. ECF does not manufacture capabilities.
2. Each canonical capability carries a **primary** ECF coordinate and may carry **secondary** coordinates.
3. The primary coordinate marks **earliest initiation** (the ECF lifecycle rule: capabilities map to the stage where they are first initiated), not the stage of heaviest operation.
4. Secondary coordinates record legitimate participation across other stages.
5. Depth is achieved by **recursion**: any ECF cell may decompose into a further 7×7 matrix, providing depth without changing the top-level framework and without an enormous flat capability hierarchy.

Worked example (illustrative, not canonical):

```
Customer Management
Primary:    Customer & Demand × Operate / Deliver
Secondary:  Customer & Demand × Conceive
            Customer & Demand × Improve
            Customer & Demand × Retire / Renew
```

## 12. Canonical capability record (conceptual)

Target shape, to be reconciled with `dea-metamodel` and catalog CI conventions by CR-DEA-BC-01; **no schema change precedes the CR**:

```yaml
id:
name:
definition:
purpose:
outcome:
business_object:
capability_layer:   # optional; governed enum: strategic | operational | support (dea-metamodel ADR-015).
                    # capability_type is deprecated upstream (CR-016): kind is the entity type
                    # (dea:BusinessCapability), not a per-entry field. See CR-DEA-BC-02.
status:
maturity:
ecf:
  primary: {domain:, stage:}
  secondary: []
parents: []
children: []
related_capabilities: []
realization:
  processes: []
  actors: []
  resources: []
  systems: []
  information: []
evidence:
  sources: []
  rationale:
specialization:
  allowed: true
  industry_examples: []
aliases: []
provenance:
version:
```

## 13. "Why this capability exists"

Every canonical entry eventually carries, in addition to its record fields:

- **Why capability**: why this is a durable ability rather than a process, unit, or technology.
- **ECF rationale**: why the primary coordinate is what it is.
- **Boundary**: what it includes and excludes.
- **Non-examples**: adjacent constructs explicitly out of scope (e.g. for Customer Management: Customer Support Process, CRM System, Customer Service Department).
- **Specialization boundary**: what industry specializations may legitimately refine.

## 14. Layering of the stack

```
WSF                      foundational semantics
  │
DEA Metaframework        enterprise organizing logic (ECF)
  │
DEA Metamodel            formal entity/relationship structure
  │
DEA Catalogs             canonical instances            ← this repository
  │
Enterprise Specialization   OpenDEA / organization / industry views
```

The metaframework positions itself as the conceptual skeleton above metamodel and catalogs, instantiated by the catalogs. Refinement adopted here: instantiation is selective per catalog semantics (Section 1).

## 15. Repository architecture direction

Indicative target, to be reconciled with existing catalog conventions before adoption:

```
dea-catalog-business-capabilities/
├── README.md
├── GOVERNANCE.md
├── METHODOLOGY.md
├── EVIDENCE.md
├── TAXONOMY.md
├── entities/v1-alpha/
├── evidence/
│   ├── cross-industry/
│   ├── business-architecture/
│   ├── enterprise-analysis/
│   └── research/
├── mappings/
│   ├── ecf/
│   ├── specializations/
│   └── synonyms/
├── diagrams/
├── schemas/
└── .github/workflows/
```

Not built yet: population, schema, and CI changes all follow CR-DEA-BC-01.

## 16. Decision points register

| # | Decision | Position adopted |
|---|---|---|
| D1 | Catalog vs matrix | Catalog answers "what abilities"; ECF answers "where". No cell-driven generation. |
| D2 | First increment | Establish the method (CR-DEA-BC-01) before populating entries. |
| D3 | Capability definition | Durable ability producing/enabling/controlling/preserving/realizing outcomes; implementation-independent. |
| D4 | First-order scope | Enterprise-general only; industry/organization forms live in specialization levels 2 to 4. |
| D5 | Possession | required / possessed / sourced / realized; outsourcing does not remove requirement. |
| D6 | Admission | Evidence ladder (7 stages) + 10 admission tests; Ability/Outcome/Implementation-Independence are hard gates. |
| D7 | External frameworks | Evidence sources (APQC, BA Guild, OMG), never templates. |
| D8 | ECF coordinates | Primary (earliest initiation) + secondary (legitimate participation). |
| D9 | Depth | ECF recursion over flat hierarchy. |
| D10 | Research visibility | Candidate Universe, Normalized Set, Canonical Set kept distinct; rejections retained. |
| D11 | Schema | No schema change before CR-DEA-BC-01; reconcile with dea-metamodel and catalog CI conventions first. |
| D12 | Cross-catalog principle | ECF is the common coordinate system; each catalog contributes where its semantics legitimately intersect. |

## 17. Sequence

```
CR-DEA-BC-01  First-Order Business Capability Method
        ↓
Evidence Investigation
        ↓
Candidate Capability Universe
        ↓
Normalization
        ↓
Canonical First-Order Set
        ↓
ECF Mapping
        ↓
Schema / CI Implementation
        ↓
Catalog Population
        ↓
Industry Specialization Framework
```

CR-DEA-BC-01 scope (18 items): capability semantics; first-order definition; admission criteria; evidence methodology; candidate→canonical lifecycle; capability vs process; capability vs outcome; capability vs function; capability vs service; capability vs specialization; ECF overlay rules; primary/secondary coordinate semantics; cross-industry evidence strategy; industry specialization boundary; provenance and evidence representation; canonical capability record; catalog governance; review and acceptance workflow.
