# CR-DEA-BC-01: First-Order Business Capability Method

## Status

- **State:** Draft: awaiting review, then "Proceed" to land as proposal PR.
- **Series tag:** `CR-DEA-BC` (DEA Business Capability).
- **Numbering convention:** CR-DEA-BC-01 is the method CR. Landed siblings: CR-DEA-BC-01A (record-shape reconciliation, ADR-015 alignment), CR-DEA-BC-02 (evidence-based first-order capability investigation, in execution). Further CRs continue the series (`CR-DEA-BC-03` schema + CI, `CR-DEA-BC-04` industry specialization framework).
- **Primary repo:** `technehub-labs/dea-catalog-business-capabilities` (existing, public, scaffold).
- **Predecessors:** none in this series. Grounding PR: `dea-catalog-business-capabilities#2` (README alignment + `docs/FOUNDATIONS.md`, merged 2026-08-31).
- **Sibling CRs (landed):** CR-DEA-BC-01A (constrains the canonical record shape per dea-metamodel ADR-015/CR-016; explicitly leaves the admission method, evidence ladder, and lifecycle to this CR), CR-DEA-BC-02 (references this CR as predecessor; executes the evidence investigation and candidate universe).
- **Successors (parked):** CR-DEA-BC-03 (schema + CI), CR-DEA-BC-04 (industry specialization framework).
- **Sibling tracks:** CR-ESA series (semantic architecture), CR-EO series (enterprise ontology), CR-CM series (concepts model). Cross-reference only; no shared phase plan.

## Relationship to in-flight work

CR-DEA-BC-02 is already executing ahead of this method CR (Evidence Register v0.1 and Candidate Universe v0.1 are staged for review as research artifacts). That ordering is deliberate: the investigation produces raw material; this CR defines the method by which that material is judged. Acceptance of this CR does not retro-invalidate the research artifacts; it gates their promotion. Nothing becomes canonical until it passes the method defined here.

## Primary objective

Establish the **First-Order Business Capability Catalog Method** for `dea-catalog-business-capabilities`: the semantics, admission criteria, evidence process, lifecycle, ECF overlay rules, and governance by which first-order business capabilities are discovered, tested, normalized, mapped, reviewed, and admitted to the canonical catalog.

This CR changes **method and documentation only**. It ships no capability entries, no schema, no CI changes. Population begins only after the method is accepted, per the phase plan.

## Why now

The repository is a scaffold with an accepted direction (PR #2: FOUNDATIONS.md). Without an accepted method, population would be ad-hoc: capabilities invented rather than evidenced, the ECF matrix treated as a generator of 49 buckets, external frameworks copied as templates, and industry-specific content leaking into the first-order set. Each failure mode is cheap to prevent now and expensive to unwind after entries exist.

The catalog is also the first DEA catalog to move from scaffold to population. The method it establishes (evidence ladder, candidate lifecycle, ECF overlay discipline) becomes the reusable pattern for every other catalog in the federation.

## Architectural principle

**The catalog answers "what"; the ECF answers "where".**

> Capabilities are derived from enterprise reality; ECF coordinates them. The ECF does not manufacture capabilities.

Consequences that bind every phase of this CR:

1. No capability entries are generated from ECF cells. The 7×7 matrix is an organizing framework; capabilities attach where semantics legitimately intersect.
2. The ECF coordinate is classification context, not capability identity. A capability has its own identity, business purpose, outcome, and business object focus independent of its coordinate.
3. General rule for all DEA catalogs: the ECF is the common coordinate system; each catalog contributes entities where its semantics legitimately intersect the framework. "Instantiated by" never means "every cell must be populated."

## Scope

The method established by this CR comprises 18 components:

1. **Business Capability semantics.** A capability is a durable ability of an enterprise to produce, enable, control, preserve or realize a meaningful business outcome, independent of the particular organization, process, people, technology or implementation used to realize it. Consistent with the OpenDEAM allocation (`dea:entity-capability`, L3-value-delivery: an ability the business possesses or requires to deliver value).
2. **First-order definition.** A First-Order Business Capability is sufficiently fundamental and enterprise-general to be recognized across materially different enterprises without requiring an industry-specific interpretation.
3. **Admission criteria.** The ten tests: Ability, Outcome, Durability, Enterprise Relevance, Implementation Independence, Object Focus, Distinctness, Decomposability, Evidence, ECF Fit. Ability, Outcome, and Implementation Independence are hard gates: failure on any one rejects the candidate.
4. **Evidence methodology.** Research, not copy. Established bodies of knowledge (Business Architecture Guild/BIZBOK, TOGAF capability guidance, OMG business architecture material, APQC PCF, and successors per the CR-DEA-BC-02 evidence register) are evidence sources, never templates. No single framework is the semantic authority.
5. **Candidate to canonical lifecycle.** Candidate, Observed, Corroborated, Normalized, ECF Mapped, Reviewed, Canonical. Passage is mandatory and recorded.
6. **Capability vs process distinction.** Processes describe work (verb phrases: "Invoice Customer"); capabilities describe enduring ability ("Billing Management"). The metamodel relates Business Capability to Business Process without equating them.
7. **Capability vs outcome distinction.** An outcome is a result; a capability is the ability to produce it. Customer Satisfaction is an outcome; Customer Management is a capability.
8. **Capability vs function distinction.** A function is an organizational or structural grouping of work; a capability is implementation-independent and survives reorganization.
9. **Capability vs service distinction.** A service is an offered unit of value exchange with a consumer; a capability is the ability that may underpin many services.
10. **Capability vs specialization distinction.** Specialization levels: L1 first-order (this catalog), L2 enterprise/domain specialization, L3 industry/sector specialization (specialization views), L4 organization-specific (adopting enterprise). Industry forms never enter the first-order set.
11. **ECF overlay rules.** Primary coordinate plus optional secondary coordinates. No cell-driven generation. Depth by ECF recursion (any cell may decompose into a further 7×7), not by flat catalog hierarchy.
12. **Primary/secondary coordinate semantics.** The primary coordinate marks earliest initiation (the ECF lifecycle rule: capabilities map to the stage where they are first initiated), not the stage of heaviest operation. Secondary coordinates record legitimate participation in other stages.
13. **Cross-industry evidence strategy.** Deliberate span of materially different enterprise types: commercial, non-profit, government, professional services, manufacturing, retail, financial services, healthcare, technology, infrastructure. The question asked of each: what abilities recur despite radically different business models? Cross-industry material evidences the baseline; industry-specific material evidences specialization boundaries.
14. **Industry specialization boundary.** Industry, sector, and organization specializations refine first-order capabilities through specialization views (for example a Mobile Communications Service Provider view). Specializations reference parents; they never modify or replace them.
15. **Provenance and evidence representation.** Every candidate and canonical entry carries its evidence trail: sources, ladder stage transitions, rationale. Rejected and deferred candidates are retained as evidence.
16. **Canonical capability record.** Conceptual record shape per `docs/FOUNDATIONS.md` §12 as amended by CR-DEA-BC-01A: kind is the entity type (`dea:BusinessCapability` by catalog scope); the record carries the governed `capability_layer` enumeration (`strategic | operational | support`) and never the deprecated `capability_type`; ECF coordinates are classification metadata (`ecf.primary` / `ecf.secondary`), never a kind classifier. Machine schema reconciled with `dea-metamodel` and catalog CI conventions under CR-DEA-BC-03.
17. **Catalog governance.** Change control table: method changes via CR; canonical admission/removal via the ladder plus review; `metamodel-pointer.yaml` regenerated from the root model fan-out only.
18. **Review and acceptance workflow.** Semantic and architectural review gates between ECF Mapped and Canonical; review criteria, reviewer roles, and acceptance recording.

## Non-goals

- No capability entries, candidate lists, or ECF mappings ship in this CR (that is CR-DEA-BC-02's execution line).
- No JSON Schema, validation, or CI changes (CR-DEA-BC-03).
- No changes to `metamodel-pointer.yaml` or to the OpenDEAM root model.
- No changes to the ECF definition in `dea-metaframework`.
- No industry or sector capability content (CR-DEA-BC-04 and later).
- No tooling, viewer, or runtime work.

## Boundaries with sibling tracks

| Concern | Owner | Cross-ref |
|---|---|---|
| Capability entity formal structure (entity/relationship types, ADR-015 kind-by-specialization) | `dea-metamodel` | This CR consumes; never redefines |
| Record-shape reconciliation (capability_layer, capability_type deprecation) | CR-DEA-BC-01A (landed) | This CR ratifies the amended shape in its method documents |
| Evidence corpus, candidate universe, normalization, canonical admission execution | CR-DEA-BC-02 (in execution) | This CR defines the method that judges its outputs |
| Layer/building-block allocation (L3-value-delivery) | `dea-architecture-framework` (OpenDEAM) | Pointer regenerates from fan-out only |
| ECF 7×7 definition and recursion rule | `dea-metaframework` | This CR references; never modifies |
| Business processes | `dea-catalog-processes` | Distinct construct; realization links only |
| Actors, resources, systems, information | Their catalogs | Realization links only |
| Foundational semantics | WSF | Upstream layer; this CR aligns, does not assert |
| Capability assessment/maturity instruments | `Assessment-Models/dea-catalog-assessment-tools` | Downstream consumer of canonical capabilities |
| Meaning organization, vocabulary governance | CR-ESA series | Orthogonal; capability names may cite ESA vocabulary patterns later |

## Design constraints

1. **Land as authored.** On acceptance, this CR ships verbatim to `change-requests/CR-DEA-BC-01.md` (md5-verified against the reviewed draft). No silent rewrites.
2. **Method before population.** No `entities/v1-alpha/` entries exist until the method documents land (Phase 1) and the CR-DEA-BC-02 evidence cycle completes its admission stages.
3. **No schema before method.** `schemas/entity.schema.json` is deferred to CR-DEA-BC-03 and must be reconciled against `dea-metamodel` and the catalog-wide CI conventions, not invented locally.
4. **Evidence ladder is mandatory.** No entry reaches Canonical without a recorded passage through all seven stages. "We think every enterprise needs X" never becomes "DEA says every enterprise needs X" without the ladder.
5. **External frameworks are evidence, not authority.** Capabilities are inferred from recurring enterprise work, not transcribed from any framework.
6. **First-order scope discipline.** The anti-invention test (would this ability still make semantic sense if the enterprise changed industry tomorrow?) classifies every candidate: first-order, industry-specific, implementation-specific, process, organization, system, or outcome.
7. **ECF overlay discipline.** Primary coordinate equals earliest initiation. Secondaries are honest, not exhaustive. Recursion provides depth.
8. **Possession semantics.** The catalog distinguishes required / possessed / sourced / realized. Outsourcing an activity does not remove the capability requirement.
9. **Visible research trail.** Candidate Universe, Normalized Set, and Canonical Set are distinct populations; rejections and deferrals are retained with rationale.
10. **ADR-015 record alignment.** The canonical record carries `capability_layer` (governed enumeration) and never `capability_type`; kind is expressed by entity specialization, not by a classifier field (CR-DEA-BC-01A).
11. **One phase per PR.** Each phase ships a visible, checked-in deliverable; the catalog CHANGELOG shows the prior to new delta per PR.
12. **Writing conventions.** Design Specification tone; no en or em dashes in any shipped document.

## Phase plan

Each phase is one future PR. Later phases may shift in detail; the boundaries hold.

| Phase | Scope | First deliverable | CR line |
|---|---|---|---|
| **0** (this proposal) | Land this CR verbatim + `change-requests/README.md` row + README pointer | `change-requests/CR-DEA-BC-01.md` | CR-DEA-BC-01 |
| **1** | Method documents per this spec: `METHODOLOGY.md` (semantics, admission tests, lifecycle, distinctions, review workflow), `EVIDENCE.md` (evidence methodology, source stances, provenance rules), `GOVERNANCE.md` (change control, roles), `TAXONOMY.md` (structure rules, naming, alias policy) | `METHODOLOGY.md` | CR-DEA-BC-01 |

Continuation of the program (already defined by landed CRs):

| Program step | Owner CR | State |
|---|---|---|
| Evidence corpus + candidate universe + classification | CR-DEA-BC-02 | Landed; executing (Evidence Register v0.1, Candidate Universe v0.1 staged) |
| Normalization, first-order candidates, canonical admission | CR-DEA-BC-02 | Executing per its own section 33 |
| Schema + CI reconciliation with dea-metamodel | CR-DEA-BC-03 | Parked |
| Industry specialization framework (first view: Mobile Communications Service Provider) | CR-DEA-BC-04 | Parked |

**Recommended first phase after merge:** Phase 1 (method documents). CR-DEA-BC-02's admission stages cite these documents; landing them keeps promotion decisions conformant from the first candidate.

## Definition of Done for the proposal PR

The proposal PR ships ONLY:

1. `change-requests/CR-DEA-BC-01.md`: this document, verbatim (md5-verified against the accepted draft).
2. `change-requests/README.md`: index table with this CR's row (the existing CR-DEA-BC-01A and CR-DEA-BC-02 entries remain).
3. `README.md`: Status section pointer updated to name the landed method CR.

No other files change. No runtime, no schema, no entries. The existing allocation CI (`validate-allocation.yml`) must remain green.

## Acceptance

Acceptance of this CR constitutes acceptance of: the 18 method components (Scope), the binding consequences of the architectural principle, the design constraints, and the phase plan boundaries. Phase-level detail inside the boundaries may evolve per phase PR review.
