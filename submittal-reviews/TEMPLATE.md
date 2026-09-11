# Submittal Review Template

This is the canonical **submittal review** template for any catalog published by a
TechNeHub Labs catalog repository. It is derived from `BC-SR-A001` (the first
submittal review filed in `dea-catalog-business-capabilities`) and is intended to
be reused verbatim by any reviewer filing feedback against a published catalog
release.

The structure is deliberately **assessment-style**, not proposal-style. A submittal
review is filed *after* a release is cut, against an artifact that is already
considered canonical by its own admission gates. Its job is to surface what a
reviewer thinks the artifact got right and wrong, with enough rigour that the
catalog owner can triage each item into "fix in the next carrier CR", "open an
investigation", or "defer to backlog with rationale".

---

## File naming

`<CATALOG-PREFIX>-SR-A<NNN>.md`

| Prefix | Catalog |
|---|---|
| `BC` | `dea-catalog-business-capabilities` |
| `MF` | `dea-metaframework` |
| `MM` | `dea-metamodel` |
| `CP` | `dea-catalog-processes` |
| `CA` | `dea-catalog-actors` |

`A<NNN>` is the sequential id assigned by the catalog owner when the file is
filed. Sequence is per-catalog; zero-padded to three digits.

## Front-matter

```yaml
---
id: <CATALOG-PREFIX>-SR-A<NNN>
catalog: <repo name>
catalog_release_under_review: <version label, e.g. v1-alpha.4>
catalog_release_commit: <full 40-char sha>
reviewer: <name or handle>
reviewer_affiliation: <organisation, optional>
date_filed: <YYYY-MM-DD>
filing_repo: <path to receiving catalog repo, e.g. technehub-labs/dea-catalog-business-capabilities>
carrier_cr: <CR-DEA-...-NN> # the CR this review is being triaged into, if known
status: filed | triaged | partially-actioned | fully-actioned
scope: <one-line summary of what was reviewed>
---
```

## Required sections

The template has **20 numbered sections**. Each section maps to a recurring
question a reviewer should answer about any catalog release. Sections are
numbered to preserve stable cross-references in carrier CRs (carrier CRs cite
review items by section number, e.g. "BC-SR-A001 §8.A").

### §1. Executive assessment
A 2-4 paragraph executive summary. State (a) the overall verdict (acceptable /
needs fixes / has foundational problems), (b) the headline strengths, (c) the
headline gaps, (d) the most important next step. The catalog owner reads this
section first; everything else is evidence for it.

### §2. What the catalog gets right
A bulleted enumeration of strengths. Be specific: cite section numbers,
record ids, or filenames. The owner needs to know what to *preserve* as much
as what to fix. Strengths not captured here are at risk of accidental
regression in the carrier CR.

### §3. Current foundational landscape
A domain-by-domain table mapping the catalog's current content to the ECF
domains (or the equivalent meta-framework coordinate system, where ECF is not
applicable). Each row records the domain, the entities currently placed in it,
and a one-line assessment (balanced / under-represented / overloaded / semantically
questionable). This table is the diagnostic for §4-§7.

### §4-§7. Foundational gaps
Each gap gets its own numbered subsection (§4 Gap #1, §5 Gap #2, …). For each
gap:

- **What is missing and why it is foundational.** The case for admission as a
  first-order entity. Cite external references where possible (industry
  frameworks, metamodel docs, ECF domain definitions).
- **ECF placement hypothesis.** Recommended primary coordinate, possible
  secondary coordinates, with rationale.
- **Evidence requirement.** What evidence would be required to recommend
  admission through the catalog's own admission gate. The reviewer does not
  produce this evidence: they identify what is required.
- **Priority.** P1 (strong candidate for canonical admission), P2 (borderline,
  evidence-gated), P3 (investigation on backlog).

### §8-§14. ECF coordinate alignment issues
Each mis-placement gets its own numbered subsection. For each:

- **Current placement.** Domain × stage, with the entity id.
- **Recommended placement.** Domain × stage, with rationale grounded in the ECF
  domain definition (or the equivalent meta-framework coordinate semantics).
- **Confidence.** High / medium / low. High-confidence corrections can land in
  the carrier CR with light re-justification; medium-confidence corrections
  need an investigation; low-confidence corrections are deferred to backlog.
- **Cross-references.** Any related entities or ECF axes affected.

### §15. ECF coordinate philosophy refinement
This section is the meta-critique of the catalog's ECF mapping rules themselves,
not the individual placements. If the reviewer thinks the rule used to assign
primary coordinates (e.g. "earliest initiation point") is producing
semantically unintuitive placements even where it is technically defensible,
this is the section to argue for a refined rule. Recommend the refined rule;
the catalog owner decides whether to adopt it as a method-level change.

### §16. Closed-loop capability structure
A proposed set of interacting capability loops (direction, value, resource,
enterprise protection, external ecosystem). This is the architectural view
the catalog should express, not a literal restructuring proposal. The owner
uses this as input to §17 (gap prioritisation).

### §17. Recommended foundational additions
A summary table. Columns: priority, candidate, recommendation (admit / investigate
/ do not add). Sorted by priority. This is the section the carrier CR cites
when it decides which investigations to open.

### §18. Recommended ECF corrections
A summary table. Columns: entity, current coordinate, recommended coordinate,
confidence. The carrier CR's §"ECF re-mapping" scope is built directly from
this table.

### §19. Repository / documentation drift
Anything in the repository itself (not the catalog content) that needs cleanup.
Examples: README status field out of sync with catalog state, version pins
against the wrong metamodel, CHANGELOG entries missing, scripts whose output
diverges from what the README claims.

### §20. Overall verdict and recommended next step
A short closing section. State the recommended first carrier CR scope: which
items from §17 + §18 + §19 to include, which to defer, and what sequence. The
owner typically uses this as the starting point for the carrier CR draft.

## Writing guidance

- **Ground claims in the catalog's own documents.** Cite entity ids, CR
  numbers, ECF section numbers, metamodel ADR numbers. A reviewer who
  asserts "Strategy is in the wrong domain" without citing the ECF domain
  definition has not done the work; the owner will bounce it.
- **Distinguish "I think this is wrong" from "this is wrong."** Use confidence
  levels. The catalog's own admission gate uses an evidence ladder; the
  reviewer should mirror it.
- **Do not propose implementation details.** A submittal review is not a CR.
  The carrier CR draft is the owner's responsibility.
- **Do not propose adding entities that bypass the admission gate.** Even a
  P1 recommendation is still a *recommendation*. Admission remains the
  owner's call through the catalog's own gates.
- **Length is not a virtue.** A 600-line review that misses the headline
  findings is worse than a 200-line review that nails them. Aim for the
  density of an external technical review, not the volume of an internal
  audit.

## Filing a review

1. Fork or branch the receiving catalog repository.
2. Create `submittal-reviews/<CATALOG-PREFIX>-SR-A<NNN>.md` from this template.
3. Open a PR titled `chore: file submittal review <CATALOG-PREFIX>-SR-A<NNN>`.
4. The catalog owner triages in the PR thread; assigns the carrier CR; flips
   the `status:` front-matter to `triaged`.
5. The carrier CR is opened in `change-requests/`; its body cites the
   relevant review sections (§8.A, §17 P1, etc.).
6. When the carrier CR lands, the review's `status:` flips to
   `partially-actioned` or `fully-actioned` and the index in
   `submittal-reviews/README.md` is updated.

## See also

- The first review filed under this template:
  [`BC-SR-A001.md`](BC-SR-A001.md) in this folder.
- The carrier CR derived from it: `change-requests/CR-DEA-BC-12.md`.
