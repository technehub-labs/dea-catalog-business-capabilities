# CR-DEA-BC-47: Canonical Capability Discovery Views

## 1. Change Request Metadata

| Field | Value |
|---|---|
| CR ID | CR-DEA-BC-47 |
| Title | Canonical Capability Discovery Views |
| Status | Accepted (user directive 2026-10-28: "BC-45 to BC-47 are attached to implement") |
| Series | CR-DEA-BC |
| Change layer | L4 — Derived catalog views and semantic discovery |
| Target repository | `technehub-labs/dea-catalog-business-capabilities` |
| Target branch | `main` |
| Semantic dependencies | Accepted CR-DEA-BC-41 and final record-model disposition from CR-DEA-BC-42/43 |
| Documentation dependency | Accepted CR-DEA-BC-44 |
| Validation dependency | Accepted CR-DEA-BC-45 |
| Catalog adoption dependency | Accepted CR-DEA-BC-46, or an explicitly approved authoritative inventory baseline |
| Primary deliverable | Governed specification and implementation of derived capability discovery views |
| Decision authority | Repository CR governance process |

**Status**: Accepted (user directive 2026-10-28: "BC-45 to BC-47 are attached to implement")
**Owner**: Emmanuel A. Otchere
**Date**: 2026-10-28
**Trigger**: Tranche step 7; executes CR-DEA-BC-42 backlog R-6 with all dependencies landed: BC-41/42/43 model decisions (PRs #94-96: no unpopulated properties assumed present), BC-44 documentation layer (PR #97), BC-45 validation (PR #98), BC-46 catalog adoption with the authoritative inventory baseline (PR #99 + #100 regen fix). Prepared by the review agent under eaojnr's direction; authorship of record per cardinal rule R1.
**Carrier**: Single PR on feature branch `feat/CR-DEA-BC-47-discovery-views`. PR review, not direct push.
**Lands against**: `main` (repository `technehub-labs/dea-catalog-business-capabilities`)

> **Format note (landing, 2026-10-28):** authored in the enrichment programme; landed with normative content verbatim. Landing scope decision (§6): four views implemented — capability index, ECF classification, related-capabilities reference list (untyped, R-1 limitation stated), outcomes/business-object overview; the evidence view folds into the index (provenance column); no graph/diagram is emitted because the relationship model is untyped until R-1 (§4.4 limitation reporting). Generated outputs are committed under `docs/views/` with a `--check` freshness gate wired into `catalog-conformance.yml`.

**Dependency condition:** The views must be generated from the accepted canonical catalog and its authoritative relationships. If the preceding CRs establish that particular relationships or fields do not exist, this CR must not invent them to populate a view.

## 2. Change Objective

Establish a controlled mechanism for producing useful discovery and relationship views from the canonical Business Capability catalog.

The views should make the catalog easier to explore, understand, and maintain while preserving a strict separation between authoritative entity data and derived presentation.

The implementation must support discovery of canonical capabilities, their established classifications, relevant outcomes, and authorized relationships where the source data supports those views.

## 3. Problem Statement

A canonical catalog can be structurally valid and well documented while still being difficult to navigate as a connected semantic resource.

Readers may need to discover capabilities by classification, understand related entities, inspect boundaries, or trace links to authoritative records without opening every entity README individually.

Manually maintained summary tables and diagrams tend to drift from canonical data. Automatically generated views can reduce that risk, but only if their derivation rules are explicit and their limitations are clear.

The repository therefore needs governed discovery outputs that improve usability without becoming an alternative source of entity definitions, relationships, or classification decisions.

## 4. Normative Principles

### 4.1 Canonical data is authoritative

Every generated view must be derived from authoritative canonical records or explicitly approved source artefacts.

Generated output must never be treated as the source of truth for entity identity, definitions, classifications, relationships, or evidence.

### 4.2 Derivation must be reproducible

The same canonical inputs and generation rules must produce equivalent outputs.

The process must document its inputs, transformation rules, and output destinations.

### 4.3 No semantic inference without authority

The generator must not infer a formal relationship from naming similarity, shared words, common classification, or apparent conceptual proximity.

Only established relationships and explicitly authorized derivation rules may be represented as semantic facts.

### 4.4 Views must expose limitations

Where the source catalog does not contain enough information to produce a particular view, the implementation must report the limitation or omit that view.

It must not fabricate missing nodes, links, classifications, outcomes, or relationship types.

### 4.5 Presentation must not redefine the model

A diagram or summary table may simplify the display of canonical data, but it must not silently alter the meaning of the source.

Any filtering, aggregation, grouping, or omission must be documented.

## 5. Scope

### 5.1 In scope

Subject to source-data availability and approved requirements, this CR may establish:

1. A discovery view of canonical capability entities.
2. A classification-oriented view based on existing governed classification data.
3. A relationship view based on explicitly represented canonical relationships.
4. A navigable index linking generated entries to canonical records and READMEs.
5. A documented generation process.
6. Integrity checks for generated outputs.
7. Reproducibility and stale-output detection.
8. Documentation of supported views and their limitations.
9. A controlled location for generated artefacts.
10. Tests verifying that outputs reflect the authoritative inputs.

### 5.2 Out of scope

This CR does not authorize:

- New canonical capabilities.
- New semantic relationships.
- Changes to entity identity or classification.
- Changes to the canonical record schema unless separately authorized.
- Inference of missing relationships.
- A new ontology or metamodel.
- A replacement for existing canonical indexes or governance registers.
- An interactive application or external hosted service.
- An enterprise digital twin or simulation environment.
- A new assessment or maturity model.
- A new ECF conformance system.
- Manual editing of generated outputs as the normal maintenance process.
- A catalog-wide change to capability definitions or evidence.

Any additional visualization platform or application must be proposed separately if it materially expands the repository's technical scope.

## 6. Candidate Discovery Views

The following views are candidates, not a requirement to generate every possible representation. The implementation must prioritize those that can be derived faithfully from available canonical data.

### 6.1 Canonical capability index

Purpose: provide a navigable inventory of canonical capabilities.

Potential contents include:

- Canonical ID.
- Canonical name.
- Definition or concise description where appropriate.
- Existing classification values.
- Links to the canonical record and README.
- Relevant lifecycle information where authoritative.

The index must derive entity membership from the canonical inventory and must not become a separately maintained list.

### 6.2 Classification view

Purpose: allow readers to explore capabilities using existing classification information, including governed ECF coordinates where appropriate.

The view must preserve the semantics and terminology of the source classification system.

It must not imply that capabilities within the same classification are equivalent, hierarchically related, or interchangeable unless the source model explicitly establishes that relationship.

### 6.3 Capability relationship view

Purpose: expose established relationships among canonical capabilities.

The view must:

- Use only authorized relationship data.
- Distinguish relationship types where the source model defines them.
- Link nodes to their canonical records.
- Handle missing or unresolved targets explicitly.
- Avoid interpreting simple references or co-occurrence as formal semantic relationships.

If the current catalog does not support a sufficiently defined relationship graph, the view must be limited to the relationships that are actually authorized and represented.

### 6.4 Outcome-oriented discovery view

Purpose: support discovery based on established capability outcomes or business objects, where the canonical model supports such grouping.

The view must preserve the distinction between a capability and the outcome it enables.

Shared outcomes or business objects must not be used to infer capability dependencies or hierarchy.

### 6.5 Evidence and provenance navigation

Purpose: improve navigation from a canonical capability to its supporting evidence and provenance references, where those references are available and suitable for presentation.

The view must preserve evidence ownership and provenance semantics. It must not summarize missing evidence as though it were present.

### 6.6 Additional views

Additional representations may be considered only where:

- A defined user need exists.
- The source model can support the representation.
- The transformation rules are explicit.
- The view adds value beyond existing authoritative documentation.
- Maintenance and validation costs are justified.

## 7. Source and Derivation Contract

The implementation must establish a derivation contract for every generated view.

| Attribute | Requirement |
|---|---|
| View ID | Stable identifier for the generated view |
| Purpose | Discovery question the view answers |
| Authoritative inputs | Exact source records or artefacts |
| Selection rules | Which entities and relationships are included |
| Transformation rules | How source data is rendered or aggregated |
| Omission rules | Which information is intentionally excluded |
| Output format | Approved generated format |
| Output location | Repository path consistent with existing conventions |
| Generation method | Script, existing tooling, or other approved mechanism |
| Validation | Checks proving the output is internally consistent |
| Freshness rule | How stale output is detected |
| Known limitations | Unsupported queries, missing source information, or display constraints |

The derivation contract must identify whether each view is generated at validation time, committed to the repository, or produced through another approved process.

The implementation must not introduce an unnecessary runtime dependency when a deterministic repository-generated artefact is sufficient.

## 8. Generation and Maintenance Requirements

### 8.1 Deterministic generation

The generation process must:

- Use defined authoritative inputs.
- Produce stable output ordering.
- Avoid dependence on uncontrolled external services.
- Handle missing or invalid source data predictably.
- Provide actionable error messages.
- Avoid modifying canonical records as a side effect.
- Document the command or process needed to regenerate outputs.

### 8.2 Generated artefact ownership

Generated files must be clearly identifiable as generated outputs.

Where the repository commits generated files, the generation procedure must define how reviewers verify that the committed outputs match the source data and generation logic.

Where outputs are not committed, the repository must document how users access or reproduce them.

### 8.3 Freshness and integrity

The implementation must define a way to detect when a generated view no longer reflects the current canonical source.

The chosen method must fit the repository's existing tooling and governance.

It must not silently accept stale views as authoritative.

### 8.4 Error handling

The generator must fail or report a clear warning when required source data is invalid or incomplete, according to the severity of the condition.

A failure to generate a semantically meaningful relationship view must not be concealed by emitting an empty or misleading diagram.

### 8.5 Accessibility and usability

Generated views must be understandable without requiring users to infer undocumented conventions.

Where visual diagrams are used, the repository should provide a textual index or equivalent navigable representation so that core discovery does not depend exclusively on an image.

Labels must use canonical names or clearly identified derived labels. The view must retain links or references to authoritative source entities where the output format supports them.

## 9. Validation Requirements

Validation must demonstrate that generated views faithfully represent their source data.

The tests must cover:

1. Every included entity resolves to a canonical source.
2. Every displayed identifier matches the canonical identifier.
3. Every displayed classification is derived from authoritative data.
4. Every displayed semantic relationship is authorized and present in the source.
5. Every internal link resolves to its intended target.
6. Missing or invalid source data is handled as specified.
7. Generation is deterministic for equivalent inputs.
8. Stale generated outputs can be detected.
9. Regeneration does not alter canonical records.
10. Generated outputs do not introduce new semantic assertions.

Where a view depends on a field or relationship that the final canonical model does not provide, that view must be omitted, narrowed, or proposed through a separate CR.

## 10. Acceptance Criteria

- **AC-01:** Each implemented view has a defined discovery purpose.
- **AC-02:** Every view has an explicit derivation contract.
- **AC-03:** Inputs are authoritative and identifiable.
- **AC-04:** Generation is reproducible.
- **AC-05:** Canonical identities and source links remain accurate.
- **AC-06:** No unsupported relationship or classification is inferred.
- **AC-07:** Missing data is handled transparently.
- **AC-08:** Generated outputs are distinguishable from authoritative source records.
- **AC-09:** Stale output can be detected under the approved maintenance model.
- **AC-10:** Tests demonstrate source fidelity and deterministic generation.
- **AC-11:** The generation process does not modify canonical records.
- **AC-12:** Views link back to authoritative entities where supported.
- **AC-13:** Textual discovery remains available where visual output is introduced.
- **AC-14:** Documentation explains supported views and known limitations.
- **AC-15:** Repository indexes and change records are updated under existing conventions.
- **AC-16:** Existing schema, evidence, identity, ECF, and repository integrity controls remain effective.
- **AC-17:** No unapproved metamodel, inventory, or relationship changes are introduced.

## 11. Definition of Done

The CR is complete when each approved view is generated from authoritative inputs, its transformation rules are documented, its output is validated, and its maintenance process is reproducible.

The delivered views must improve discovery without creating a second catalog or obscuring gaps in the canonical source data.

## 12. Acceptance Decision

**Requested decision:** Approve the bounded implementation of canonical capability discovery views derived from authoritative catalog data.

Approval does not authorize new canonical fields, relationship types, entity admissions, or semantic inferences. Additional views that require unsupported source information must be deferred or proposed through a separate CR.