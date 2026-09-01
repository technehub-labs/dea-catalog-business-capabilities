# Methodology: First-Order Business Capability Catalog

The catalog method established by **CR-DEA-BC-01** (accepted 2026-09-01, PR #13). This document is normative: admission, promotion, and review decisions are made against it. [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md) retains the rationale and the decision points register (D1 to D12) behind these rules; where the two differ, this document governs.

Companion documents: [`EVIDENCE.md`](EVIDENCE.md) (evidence methodology and provenance), [`GOVERNANCE.md`](GOVERNANCE.md) (change control and roles), [`TAXONOMY.md`](TAXONOMY.md) (structure, naming, alias policy).

---

## 1. Definitions

**Business Capability.** A durable ability of an enterprise to produce, enable, control, preserve or realize a meaningful business outcome, independent of the particular organization, process, people, technology or implementation used to realize it.

Consistent with the OpenDEAM allocation (`dea:entity-capability`, L3-value-delivery: an ability the business possesses or requires to deliver value) and with OMG business architecture material (ability to produce an outcome without specifying how the outcome is produced).

**First-Order Business Capability.** A capability sufficiently fundamental and enterprise-general to be recognized across materially different enterprises without requiring an industry-specific interpretation.

## 2. The architectural principle

**The catalog answers "what"; the ECF answers "where."**

> Capabilities are derived from enterprise reality; the ECF coordinates them. The ECF does not manufacture capabilities.

Binding consequences:

1. No capability entries are generated from ECF cells. The 7×7 matrix is an organizing framework; capabilities attach where semantics legitimately intersect.
2. The ECF coordinate is classification context, not capability identity. A capability has its own identity, business purpose, outcome, and business object focus independent of its coordinate.
3. General rule for all DEA catalogs: the ECF is the common coordinate system; each catalog contributes entities where its semantics legitimately intersect the framework. "Instantiated by" never means "every cell must be populated."

## 3. Distinctions

A candidate that is one of the following constructs is rejected from this catalog and referred to the correct home.

| Construct | Marker | Example | Correct home |
|---|---|---|---|
| Process / activity | describes work; a verb phrase | Invoice Customer; Hire Employee | Process catalog |
| Capability | enduring ability; survives reorganization and re-platforming | Billing Management; Workforce Acquisition | This catalog |
| Outcome | a result, not an ability | Customer Satisfaction | Outcome/metric constructs |
| Function | organizational or structural grouping of work | Finance Function | Organization constructs |
| Service | offered unit of value exchange with a consumer | Customer Support Service | Service constructs |
| Organization | a grouping of people | Customer Service Department | Actor/organization constructs |
| System / technology | a mechanism | CRM System | System catalog |

The metamodel relates Business Capability to Business Process, Actor, Resource, System and Information without equating them. Realization links to those constructs are recorded on the entry (Section 10); they never redefine it.

**Capability vs specialization.** Specialization levels:

| Level | Population | Home |
|---|---|---|
| L1 | First-Order Business Capability | This catalog |
| L2 | Enterprise / Domain Specialization | Specialization views |
| L3 | Industry / Sector Specialization | Specialization views (first view: Mobile Communications Service Provider, CR-DEA-BC-04) |
| L4 | Organization-Specific Capability | Adopting enterprise (OpenDEA adoption) |

Industry and organization forms never enter the first-order set. Specializations reference their parents; they never modify or replace them.

## 4. Admission criteria

Every candidate is tested against ten questions.

| Test | Question | Gate |
|---|---|---|
| Ability | Is this actually an ability rather than an activity? | Hard |
| Outcome | What meaningful outcome does it enable? | Hard |
| Durability | Would the ability remain recognizable if processes or technology changed? | Soft |
| Enterprise Relevance | Does it apply broadly across enterprises? | Soft |
| Implementation Independence | Can different organizations realize it differently? | Hard |
| Object Focus | What business object or domain is it concerned with? | Soft |
| Distinctness | Is it materially different from another capability? | Soft |
| Decomposability | Can it legitimately have subordinate capabilities? | Soft |
| Evidence | Do independent sources or real enterprise structures support it? | Soft |
| ECF Fit | Can it be placed in the ECF without distorting either model? | Soft |

Failure on a hard gate (Ability, Outcome, Implementation Independence) rejects the candidate. Soft-gate failures are recorded with rationale and may defer rather than reject.

## 5. Anti-invention classification

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

## 6. Candidate to canonical lifecycle

Passage through all seven stages is mandatory and recorded. No stage is skipped; no entry reaches Canonical without the full recorded passage.

```
Candidate → Observed → Corroborated → Normalized → ECF Mapped → Reviewed → Canonical
```

| Stage | Meaning |
|---|---|
| Candidate | A proposed capability identified from research. |
| Observed | The concept occurs in credible enterprise or business architecture material. |
| Corroborated | It appears independently across multiple sources, industries, or enterprise contexts. |
| Normalized | Different names expressing substantially the same underlying ability are reconciled. |
| ECF Mapped | A defensible primary ECF coordinate is identified (Section 8). |
| Reviewed | Semantic and architectural review passed (Section 12). |
| Canonical | Admitted into the first-order catalog. |

The safeguard this enforces: "we think every enterprise needs X" never becomes "DEA says every enterprise needs X" without the ladder.

## 7. Populations and dispositions

Three distinct populations keep the research process visible:

| Set | Contents |
|---|---|
| Candidate Universe | Everything plausible discovered during investigation (`CAND-NNN`). |
| Normalized Capability Set | Duplicates, aliases and near-equivalents reconciled (`N-NNN` decisions). |
| Canonical First-Order Set | Only capabilities that passed the admission criteria and review. |

Candidate dispositions: `accepted` / `merged` / `rejected` / `deferred` / `specialized`. Rejected and deferred candidates are retained with rationale; they are evidence, not waste.

## 8. ECF overlay rules

1. Each canonical capability carries a **primary** ECF coordinate (`ecf.primary`: domain × stage) and may carry **secondary** coordinates (`ecf.secondary`).
2. The primary coordinate marks **earliest initiation**: the ECF lifecycle rule that a capability maps to the stage where it is first initiated, not the stage of heaviest operation.
3. Secondary coordinates record legitimate participation in other stages. They are honest, not exhaustive.
4. Depth is achieved by **recursion**: any ECF cell may decompose into a further 7×7 matrix. The catalog does not build an enormous flat subdivision tree.

## 9. Possession semantics

The catalog distinguishes four possession states; an enterprise may require a capability without performing it (outsourcing does not remove the requirement):

| State | Meaning |
|---|---|
| required | The enterprise must have access to the ability. |
| possessed | The ability exists in-house. |
| sourced | The ability is obtained from outside. |
| realized | The ability is actually exercised. |

Possession states describe an adopting enterprise's relationship to a capability; the first-order catalog records the capability itself, not any one enterprise's state.

## 10. Canonical capability record

The conceptual record shape is defined by [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md) §12 as amended by **CR-DEA-BC-01A**:

- `kind` is the entity type (`dea:BusinessCapability` by catalog scope); there is no per-entry kind classifier. `capability_type` is deprecated upstream (dea-metamodel ADR-015/CR-016) and never appears on an entry.
- `capability_layer` is optional; values are exactly the governed enumeration (`strategic | operational | support`).
- ECF coordinates are classification metadata (`ecf.primary` / `ecf.secondary`), never a kind classifier.
- `realization` links processes, actors, resources, systems and information from their own catalogs.
- `evidence` carries sources and rationale; `provenance` carries the ladder passage.

The machine schema (`schemas/entity.schema.json`) is deferred to **CR-DEA-BC-03** and reconciled against `dea-metamodel` and catalog-wide CI conventions; it is not invented locally.

## 11. Entry narrative

Every canonical entry carries, in addition to its record fields:

| Element | Content |
|---|---|
| Definition | Per Section 1 semantics. |
| Why capability | Why this is a durable ability rather than a process, unit, or technology. |
| Outcome | The meaningful outcome it enables. |
| Evidence | Sources and corroboration (per EVIDENCE.md). |
| ECF rationale | Why the primary coordinate is what it is. |
| Boundary | What it includes and excludes. |
| Non-examples | Adjacent constructs explicitly out of scope. |
| Specialization boundary | What industry specializations may legitimately refine. |

## 12. Review and acceptance workflow

Two review gates sit between ECF Mapped and Canonical:

1. **Semantic review.** The candidate satisfies the definitions (Section 1), the distinctions (Section 3), the hard gates (Section 4) and the anti-invention classification (Section 5). Naming and alias conformance per TAXONOMY.md.
2. **Architectural review.** The ECF mapping satisfies Section 8; realization links reference the correct sibling catalogs; the record shape satisfies Section 10; layering boundaries (WSF, metaframework, metamodel, catalogs) are respected.

Review outcome and reviewers are recorded on the candidate's provenance trail. Acceptance is the transition to Canonical; it is recorded in the promotion PR, which cites this document and the candidate's full evidence trail.

Roles and change control are defined in GOVERNANCE.md.

## 13. References

- CR-DEA-BC-01 (this method): [`change-requests/CR-DEA-BC-01.md`](change-requests/CR-DEA-BC-01.md)
- CR-DEA-BC-01A (record shape): [`change-requests/CR-DEA-BC-01A.md`](change-requests/CR-DEA-BC-01A.md)
- CR-DEA-BC-02 (evidence investigation): [`change-requests/CR-DEA-BC-02.md`](change-requests/CR-DEA-BC-02.md)
- Rationale and decision register: [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md)
- ECF definition and recursion rule: [dea-metaframework](https://github.com/technehub-labs/dea-metaframework)
- Entity allocation: [dea-architecture-framework](https://github.com/technehub-labs/dea-architecture-framework) (OpenDEAM)
- Record shape authority: [dea-metamodel](https://github.com/technehub-labs/dea-metamodel) (ADR-015, CR-016)
