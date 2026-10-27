# Catalogue Versioning and Change Procedure

**Status**: Normative (CR-DEA-BC-05, landed 2026-09-02). Read by every
contributor to this catalog and by every consumer that pins the catalog.

This document lifts sections 4 through 8 of CR-DEA-BC-05 from
`change-requests/CR-DEA-BC-05.md`. The CR is the authoritative source; this
document is the working form. Future CRs that change version semantics cite
this document.

## 1. Version semantics

The catalog carries four orthogonal version dimensions and two pins. They
must not be conflated.

### 1.1 Catalog version

The catalog carries a label of the form `v<N>-<word>`:

- `<N>` is a positive integer (1, 2, 3, ...).
- `<word>` is one of `alpha`, `bravo`, `charlie`, ... (NATO phonetic order).

A lettered suffix indicates a stability tier. The catalog moves from one
lettered suffix to the next on every minor bump. The numeric component
advances on every major bump.

Examples:

- `v1-alpha.0`: initial v1-alpha baseline (the current state).
- `v1-alpha.1`: first minor bump within v1-alpha (additive changes only).
- `v1-bravo.0`: a new stability tier declared within the same major.
- `v2.0`: first major version (semver-clean; the lettered suffix is dropped).

The lettered-suffix regime is **only for v1**. From v2 onward the catalog
uses plain `v<N>.<M>` semver. The lettered suffix is a transitional aid
while the catalog is still firming up its identity.

### 1.2 Capability entry version

Every entry in `entities/v1-alpha/` carries `version: 1.0.0`. This is the
**identity version**, not the catalog version. It advances per semver on the
entry alone:

- **Patch**: corrections to non-identity fields (typos, source citations,
  rationale wording, ECF coordinate refinements that do not change identity).
- **Minor**: substantive change to one entry's definition, business_object,
  outcome, or ECF primary/secondary coordinates.
- **Major**: change to entry identity (renamed, split, merged, deprecated).

Identity changes are rare. Most updates will be minor or patch.

### 1.3 Specialization view version

Specialization views (e.g., `mappings/specializations/view-telecom-mcsp.yaml`)
carry their own label `<view-id>@v<N>-<word>.<P>`. The view label advances
independently of the catalog label.

### 1.4 Metamodel pin

Every entry carries a top-level `metamodel_pin: 1.0.0` field. This pin is a
**catalog-internal shape contract**, not a pin to a dea-metaframework release
version: it asserts that the entry conforms to the catalog's v1-alpha entry
shape (the 16-field required structure and its governed field semantics, as
enforced by the conformance gates in `scripts/`). The `1.0.0` value denotes
the first stable revision of that shape contract.

This distinction matters because the dea-metaframework release line is
independent: the framework went 2.0.0 -> 2.5.0 with no 1.x release, so a
`metamodel_pin` value of `1.0.0` cannot be read as a framework version. The
catalog's compatibility with a given dea-metaframework release is asserted
at the ECF contract level (§1.5), not by this field.

When the catalog's entry shape contract itself changes in a breaking way
(e.g., a required field is added, removed, or re-typed across all entries),
the pin advances (e.g., to `2.0.0`) as part of the catalog-level migration CR,
and every entry is re-pinned in the same change. Compatibility with a new
dea-metaframework major version is assessed separately: if the framework
change breaks the ECF contract, §1.5 governs (catalog-level major bump); if
it does not, no `metamodel_pin` change is implied by the framework release
alone.

### 1.5 ECF contract pin

The catalog pins to `dea:ecf@1.0.0` via the `ecfConformance.profile` block on
every entry. This is the **hard pin**: any metamodel-level change that breaks
the ECF contract is a catalog-level major bump, period. The CG-006
consumer-side enforcement gate fails the catalog build on any drift in
`dea:ecf@1.0.0`.

## 2. Bump rules

### 2.1 Patch

Anything that does not change a consumer's understanding of the catalog in
kind is a patch: metadata fixes, source citation corrections, prose
clarifications, alignment with metamodel bug fixes (not features).

### 2.2 Minor

A minor bump is required when:

- a new canonical first-order capability is admitted (the existing D3 rule);
- a new specialization view is added;
- an existing entry's definition, business_object, outcome, or ECF
  primary/secondary coordinates change in a way that alters consumer
  understanding;
- the schema in `schemas/entity.schema.json` changes in a backwards-compatible
  way (adds a new optional field; relaxes a constraint).

### 2.3 Major

A major bump is required when:

- an existing canonical first-order capability is removed (definition or
  identity invalidated);
- an existing canonical capability is split into two distinct capabilities;
- two existing canonical capabilities are merged into one;
- the schema in `schemas/entity.schema.json` changes in a
  backwards-incompatible way (removes a field, tightens a constraint,
  changes a type);
- the metamodel pin changes from 1.x to 2.x;
- the ECF contract pin changes from `dea:ecf@1.0.0` to `dea:ecf@2.0.0`.

Major bumps are rare in practice. The D3 rule already makes additive changes
the common path.

## 3. Consumer pin scheme (three tiers)

Consumers depend on the catalog at three tiers, each stronger than the last.

### Tier 1: ECF contract version (hard pin)

`dea:ecf@1.0.0` is the **contract**. Any catalog content that violates this
contract fails the CG-006 consumer hook on every PR. This is the strongest
guarantee a consumer can have.

### Tier 2: Catalog version label (soft pin)

`dea:catalog/business-capabilities@v1-alpha` is the **content pin**. A
consumer that pins to `v1-alpha` knows exactly which 26 canonical entries
they get. When the catalog advances to `v1-bravo`, the consumer must
explicitly upgrade.

### Tier 3: Git ref (exact pin)

A specific commit SHA, tag, or branch is the **exact pin**. Strongest
specificity; brittle but frozen at the byte level.

### Pin selection guidance

- **Tier 1** is appropriate for tooling that consumes ECF semantics and is
  content-agnostic.
- **Tier 2** is the recommended default for most consumers; it gives
  stability and is human-readable.
- **Tier 3** is appropriate when reproducing an exact research result or
  when a consumer has a regulatory need to pin a frozen baseline.

### Manifest expression

Catalog version pinning is declared in a `dependencies.yaml` (or equivalent)
in the consumer repo. Fields:

- `ecf_contract`: string, e.g., `dea:ecf@1.0.0` (required).
- `metamodel_pin`: string, e.g., `1.0.0` (required).
- `catalogs`: list of catalog pin entries (zero or more).
- `catalogs[].id`: string, e.g., `dea:catalog/business-capabilities`.
- `catalogs[].version`: string, e.g., `v1-alpha`.
- `catalogs[].ref`: optional git ref (tag, SHA, branch).

## 4. Change procedure

Every catalog change follows this seven-step procedure. Steps 1-5 are the CR author; step 6 (release cut) is the catalog maintainer and is governed by the full procedure in [`docs/release-cut-procedure.md`](release-cut-procedure.md) (the A+B+D+F extensions from CR-DEA-BC-36: pre-release CI verification contract, prior-cut history table, GPG-signing procedure, doc split). Step 7 is the consumer.

1. **CR proposal**. A change request is authored under
   `change-requests/`. The CR specifies the bump tier (major, minor, patch) and the rationale. The CR is a doc-only PR landing in `change-requests/`.
2. **Review and acceptance**. The proposal CR is merged into
   `change-requests/`. Acceptance is signified by the merge commit.
3. **Implementation PR(s)**. Each implementation PR carries one logical
   change (one new entry, one metadata fix, one schema change). Implementation
   PRs cite the CR by ID in the body.
4. **CI green**. All CI gates pass on each implementation PR: the 7
   validator scripts in `scripts/` (naming, versions, ecf-conformance,
   view-refs, visual-domain-labels, catalog-index, id-system). The id-system
   check enforces IDM-001..007 (org-wide id system). The drift detector
   must remain `PASS`.
5. **CHANGELOG entry**. A new line is added to `CHANGELOG.md` summarising
   the change: tier, scope, rationale, PR number. The CHANGELOG entry is
   part of the implementation PR that triggers the bump.
6. **Release cut**. The release cut is the maintainer's step and is
   governed by the full procedure in `docs/release-cut-procedure.md`
   (gated by the pre-release CI verification contract; GPG-signed;
   documented in the prior-cut history table below). Tag format: `v<N>-<word>.<P>`
   for lettered-suffix versions, `v<N>.<M>` for plain semver. The tag is
   annotated with the CHANGELOG entry's content.
7. **Manifest bump (consumer-side)**. Consumers that pin to the catalog's
   version label advance their pin in lockstep, or explicitly opt to remain
   on the previous label (in which case they accept that they are now
   behind the upstream tip).

The CR author is responsible for steps 1 through 5. The catalog maintainer
is responsible for step 6. Consumers are responsible for step 7.

### 4.1 Prior-cut history table

A numbered, append-only table of every release tag ever cut on this
catalog. Starts empty post-reset (the v1-alpha.x withdrawals of
CR-DEA-BC-34 deliberately do not appear here; this table records
*successful* cuts; the recovery appendix in CR-DEA-BC-36 section 2 +
`docs/release-history-archive.md` are the audit records for those).

| version | date | cut by CR | commit SHA | gates (blocking+advisory CONFORMANT) | post-mortem |
| ------- | ---- | --------- | ---------- | ------------------------------------ | ----------- |

## 5. Current posture (initial state)

This section records the catalog's posture as of CR-DEA-BC-36 (2026-10-13; renumbered from the filed BC-34 by CR-DEA-BC-39 §2).
Future CRs reference this section as the baseline.

| Dimension | Value |
|---|---|
| Catalog version | `v1-alpha` (lettered-suffix regime; pre-reset) |
| Tag | none (post-reset; the v1-alpha.0 .. v1-alpha.8 tag set was withdrawn 2026-10-13 per CR-DEA-BC-36) |
| Canonical entries | 29 |
| Specialization views | 1 (`view-telecom-mcsp`, L3, telecom) |
| Open change requests | N (regenerated by `scripts/regenerate_catalog.py`; CR-DEA-BC-36 is the most recent) |
| ECF contract pin | `dea:ecf@1.0.0` |
| Metamodel pin | `1.0.0` (catalog-internal shape contract per CR-DEA-BC-26 / CR-DEA-BC-29b) |
| Method | CR-DEA-BC-01 (method docs normative); BC-13 §A semantic-center-of-gravity rule (per CR-DEA-BC-33 review) |
| Schema | `schemas/entity.schema.json` (CR-DEA-BC-03); updated at CR-DEA-BC-mv1 for the post-mv1 id system |
| Conformance gate | the 7-gate rollup (scripts/check_*.py); CR-DEA-BC-25 H3 outcome-marker path governance-object-aware |
| ID system | org-wide (CR-DEA-BC-mv1; `capabilities:capability-<slug>-<hash>` for canonical; `capabilities:candidate-<slug>-<hash>` for candidate) |
| Release procedure | `docs/release-cut-procedure.md` (gated by the pre-release CI verification contract; GPG-signed) |

## 6. References

- `change-requests/CR-DEA-BC-05.md` (the authoritative source for the v1-alpha versioning scheme).
- `change-requests/CR-DEA-BC-36-release-history-reset-and-discipline.md` (the release-history reset; the audit record for the v1-alpha.x withdrawals; the source for the A+B+D+F extension set adopted in the release-cut procedure).
- `change-requests/CR-DEA-BC-mv1.md` (the org-wide id system migration; the post-mv1 id format).
- `CHANGELOG.md` (version timeline; pre-v1-alpha.0 ECF migration prose + `Unreleased` block).
- `docs/release-cut-procedure.md` (the full release-cut procedure; the source of truth for steps 1-12).
- `docs/release-history-archive.md` (the fossilised record of the v1-alpha.x withdrawals).
- `dependencies.yaml` (catalog manifest).
- `scripts/check_versions.py` (CI guard).
- `dea-metamodel/metamodel/dea-metamodel.yaml` (top-level metamodel version 1.0.0).
- `dea-metaframework/...` (ECF contract 1.0.0; CR-ECF-CG-001).
- `entities/v1-alpha/*.yaml` (canonical entries).
- `mappings/specializations/view-telecom-mcsp.yaml` (first specialization view).