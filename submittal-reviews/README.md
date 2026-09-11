# Submittal Reviews

This folder holds **submittal review feedback** received for **released catalogs** in
this repository. A submittal review is a structured external (or internal-cross-repo)
assessment of a published catalog release against the canonical admission gate and the
ECF semantic-alignment contract; it is the analog of a peer review for a published
artifact rather than for an in-flight proposal.

## Lifecycle

1. **A catalog release is cut** (e.g. `v1-alpha.4`).
2. **A reviewer submits feedback** using `TEMPLATE.md` in this folder. The
   submission lands here as `BC-SR-A###.md` (BC = Business Capability, SR =
   Submittal Review, A### = sequential id).
3. **Triage by the catalog owner.** Each item in the submission is classified:
   - **P1: high confidence, in-scope** (recommended fix lands in a CR)
   - **P2: borderline, evidence-gated** (opens an investigation; no admission)
   - **P3: investigation** (placed on a backlog; not acted on until a higher-priority
     CR clears it)
4. **The carrier CR for the recommendations is opened** in `change-requests/`
   (CR-DEA-BC-NN). Each item in the review is referenced by section number and
   either (a) included in the carrier's scope, (b) opened as a follow-on
   investigation CR, or (c) deferred to backlog with a written rationale.
5. **Submittal review is referenced in the next release's docs.** Each release
   that lands at least one recommendation from a submittal review includes a
   summary entry in `docs/REVIEWS.md` linked from the repository `README.md`
   `## Submittal Reviews` section, and a `Submittal Reviews` row in `CHANGELOG.md`
   pointing back to the review file and the carrier CR.

## Index

| ID | Date | Reviewer | Scope | Status | Carrier CR | Released in |
|----|------|----------|-------|--------|-----------|-------------|
| [BC-SR-A001](BC-SR-A001.md) | 2026-09-10 | (external) | Full catalog v1-alpha.0..v1-alpha.4: methodology, ECF semantic alignment, foundational gap analysis, repository/doc drift | Triaged; carrier opened | CR-DEA-BC-12 | (target v1-alpha.5) |

## Naming convention

`BC-SR-A<NNN>.md`

- `BC`: catalog prefix. Other catalogs use their own prefix:
  - `DEA-MF-SR-...` for `dea-metaframework`
  - `DEA-MM-SR-...` for `dea-metamodel`
  - `DEA-CP-SR-...` for `dea-catalog-processes`
  - `DEA-CA-SR-...` for `dea-catalog-actors`
  - (`DEA-` is the org prefix; cross-repo consumers of this convention are documented
    in the org-wide submittal-review standard.)
- `SR`: submittal review (constant).
- `A<NNN>`: sequential id, zero-padded to three digits, assigned by the receiving
  catalog owner when the submission is filed. Sequence is per-catalog (BC starts at
  A001, MM starts at A001 independently).

## File structure

Each submittal review file follows `TEMPLATE.md`. The template is derived from
BC-SR-A001 (the first review filed in this catalog) and is intended to be reused
verbatim across all TechNeHub Labs catalogs.

## Cross-references

- `TEMPLATE.md`: the reusable cross-repo template for submitting review feedback.
- `change-requests/README.md`: index of carrier CRs that landed recommendations
  from submittal reviews.
- `CHANGELOG.md`: per-release entries referencing submittal reviews and their
  carrier CRs.
- `README.md`: `## Submittal Reviews` section with the running summary.
- `docs/REVIEWS.md`: per-release submittal review commentary underpinning
  changes in a summarized yet rich form for the next imaged release.
