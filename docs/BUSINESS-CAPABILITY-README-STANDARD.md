# Business Capability README Standard

**Status**: Normative (CR-DEA-BC-44, 2026-10-28)
**Implements**: the 14-section documentation contract of the [Business Capability Documentation Standard](BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md) (CR-DEA-BC-41 §5.1) at the entity-README layer, on the model outcome of [CR-DEA-BC-43](../change-requests/CR-DEA-BC-43-record-model-enrichment.md) ([gap analysis](BUSINESS-CAPABILITY-RECORD-MODEL-GAP-ANALYSIS.md), CR-DEA-BC-42)
**Template**: [`docs/templates/BUSINESS-CAPABILITY-README-TEMPLATE.md`](templates/BUSINESS-CAPABILITY-README-TEMPLATE.md)
**Reference assessment**: [`BUSINESS-CAPABILITY-REFERENCE-ENTITY-ASSESSMENT-ASSET-MANAGEMENT.md`](BUSINESS-CAPABILITY-REFERENCE-ENTITY-ASSESSMENT-ASSET-MANAGEMENT.md)

---

## 1. Purpose

The entity README is the human-readable documentation interface to the canonical record ([CR-41 §7.2](BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md)). It makes a capability understandable, reviewable, and navigable — without becoming a second source of truth. This standard defines each section's purpose, expected content, information source, requirement class, and conformance criteria.

## 2. Section specification (the 14-section contract at README layer)

Requirement classes: **UM** universally mandatory; **CM** conditionally mandatory (condition stated); **REC** recommended; **PROH** prohibited. Content states (from CR-41 §5.2, never interchangeable): not applicable / not yet established / not yet documented / established and documented / explicitly unresolved.

| # | Section | Purpose | Source | Class | Conformance criterion |
|---|---|---|---|---|---|
| 1 | Identity | Establish which canonical entity this documents | record: `id`, `name`, `type`, `version`, `lifecycle_status` | UM | Values byte-consistent with the record; links to the record file |
| 2 | Definition and semantic interpretation | State the canonical meaning; explain the enduring ability and material terms | record: `definition` (verbatim, marked authoritative); narrative: interpretation | UM | Definition verbatim and attributed; interpretation clearly distinguishable from it |
| 3 | Purpose and value contribution | Why the capability exists; value and beneficiaries | record: `purpose` (where populated; else content state), `outcome` | UM as section; content may be a recorded state | No fabricated purpose; no universal-benefit claims without evidence |
| 4 | Scope and boundaries | What it covers/excludes; non-examples; adjacent distinctions | record: `boundary`, `non_examples` | UM | Explains (not merely repeats) the record's boundary; no conflicting boundary |
| 5 | Classification | ECF primary + secondaries with rationale | record: `ecf`, `ecf_rationale`, `ecfConformance` | UM | Coordinates match record; rationale explained, coordinates never presented as identity |
| 6 | Composition and specialization | Parent/child/related structure; specialization boundary | record: `specialization_boundary`, `children`/`parents` (where populated) | CM (when relationships exist) | Only record-established relationships; untyped links not presented as typed semantics (R-1 pending) |
| 7 | Related entities and relationships | Navigation to related capabilities with why | record: `related_capabilities` | CM (when populated; the field is populated 29/29 today) | Each listed id resolves; rationale given from record evidence (e.g. boundary exclusions, why_capability); navigation ≠ semantic claim |
| 8 | Realization and operational context | How the ability may be realized without equating it to an implementation | record: `realization` (0/29 today → recorded state); narrative patterns | CM (when populated) | No invented relationships; capability/realization distinction preserved |
| 9 | Outcomes and traceability | The outcome contributed to; contribution ≠ guarantee | record: `outcome` | UM | Contribution language; no guaranteed-effect claims |
| 10 | Assessment considerations | Assessment interfaces without embedding results | none in record (BC-DOC-008 = G) | CM (section present; usually the recorded state "not applicable — no assessment authority") | No maturity scores or performance observations in identity |
| 11 | Governance | Ownership, approval, change control | GOVERNANCE.md, CR process, authorship registry | UM (as references) | Links to authoritative governance artefacts; no parallel local policy |
| 12 | Provenance and evidence | Admission basis, ladder, evidence links | record: `evidence`, `provenance`; `catalog-research/` registers | UM | Distinguishes evidence vs rationale vs provenance vs illustration; unsupported assertions PROH |
| 13 | Lifecycle and change history | Version, status, change record | record: `version`, `lifecycle_status`, provenance dates | UM | Consistent with record; changes cited by CR |
| 14 | Conformance | Which contracts the entity satisfies; this README's own state | gates; `ecfConformance`; this standard | UM | Honest conformance statement incl. open findings; exceptions per §4 |

## 3. Source-of-truth responsibilities

Per CR-41 §7 and CR-44 §8: the canonical record owns identity, definition, classification, boundary values, relationships, evidence, lifecycle; the README renders, explains, and navigates; governance artefacts keep governance; assessment sources (when they exist) keep assessment. On any mismatch: the record (or the owning artefact) is authoritative; the README is corrected through the normal PR process; a record defect is a separate CR-class change, never a README edit.

## 4. Conditionality and honest gaps

Sections are always present; their content may be a recorded state. Rendering rules: state the state explicitly (e.g. "Realization links: not yet established — targets pending sibling-catalog identity (U-2)") — never fabricate, never silently omit, never substitute generic filler. An absent section is nonconformant; an honest state is conformant.

## 5. Prohibited content

Competing identifiers or definitions; unsupported relationships; fabricated evidence/provenance; enterprise-specific implementations presented as universal; duplicated governance rules; new semantic claims introduced for completeness (CR-41 §6 applies in full).

## 6. Review procedure (human, automation-assistable)

A reviewer verifies: (1) correct entity documented; (2) canonical values agree with the record; (3) mandatory sections present and meaningful; (4) conditional rules applied; (5) boundaries conflict-free; (6) relationships evidenced; (7) provenance traceable; (8) ECF statements consistent; (9) explanation does not redefine semantics; (10) links resolve; (11) exceptions honest; (12) no prohibited content. Structural/link checks (2, 10) are automatable; semantic checks (5, 6, 9, 12) are human review — the future documentation-conformance gate (R-4) enforces only the former class and flags the latter.

## 7. Adoption

The [template](templates/BUSINESS-CAPABILITY-README-TEMPLATE.md) applies to new admissions immediately; existing entities adopt via the catalog-wide remediation CR (R-5) in evidence-backed order — Asset Management first, per the [reference assessment](BUSINESS-CAPABILITY-REFERENCE-ENTITY-ASSESSMENT-ASSET-MANAGEMENT.md). No CI gate is added by this standard (CR-44 §11).
