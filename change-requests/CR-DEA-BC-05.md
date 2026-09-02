---
cr: CR-DEA-BC-05
title: Catalogue Versioning and Change Procedure
status: proposed
date: 2026-09-02
author: technehub-labs (working folder business-capabilities)
target_repo: dea-catalog-business-capabilities
consumer_repos:
- dea-catalog-processes
- dea-catalog-business-capabilities (self)
metamodel_pin: 1.0.0
ecf_contract_pin: dea:ecf@1.0.0
related:
- CR-DEA-BC-01 (method; section 12 review gates; section 33 close-out)
- CR-DEA-BC-01A (record-shape reconciliation; ADR-015)
- CR-DEA-BC-02 (evidence-based first-order investigation; D3 minor-bump rule)
- CR-DEA-BC-03 (schema + CI reconciliation)
- CR-DEA-BC-04 (specialization framework; MCSP proving view)
- CR-DEA-MM-02 (upstream capability schema hygiene)
- CR-ECF-CG-001..006 (ECF Conformance Gate tranche)
- ADR-015 (capability classification reconciliation)
---

# CR-DEA-BC-05: Catalogue Versioning and Change Procedure

## 1. Problem

The catalog has run through five CRs (BC-01, BC-01A, BC-02, BC-03, BC-04) plus the
ECF Conformance Gate tranche plus two supplementary admission reviews plus a
boundary decision plus a corpus patch. Each of these changed the catalog. The
catalog README at present says "23 canonical first-order capabilities" while the
actual entry count is 26 (after PR #32 admitted Resilience, Innovation, and
Analytics and Intelligence). The ECF Conformance Profile pin is `dea:ecf@1.0.0`.
The metamodel pin is 1.0.0. The capability entry version is 1.0.0. The
vocabularies pin is 0.8.0. The migration data pin is 0.8.0. The core entities
and relationships pin is 1.0.0.

What we lack is a single document that says: **what does a version number mean,
what triggers a bump, how do consumers pin, and what does the change procedure
look like from proposal to merge.** Without it, every future change re-litigates
the bump question, and consumers cannot reliably state what they depend on.

## 2. Goal

Establish a single source of truth for catalog versioning and change procedure
that:

- defines version semantics for the catalog, the specialization views, the
  capability entries, and the catalog's pins to the metamodel and ECF contract;
- defines the bump rules (major, minor, patch) and gives consumers a stable
  mental model of what a label like `v1-alpha.3` means;
- defines the consumer pin scheme (three tiers: ECF contract, catalog version
  label, git ref) and the responsibilities at each tier;
- defines the change procedure from CR proposal through merge and tag;
- declares the catalog's current posture: which catalog version, which baseline
  tag, what is admitted, what is parked, what is deferred;
- records this procedure as normative in the method documents so future CRs can
  cite it.

## 3. Non-goals

- **Not a release-engineering overhaul.** This CR ships rules, not infrastructure.
  GitHub Release automation, semver enforcement bots, and signed tags are
  separate work; this CR says "tag every catalog baseline" and stops there.
- **Not a metamodel change.** Metamodel version semantics are owned upstream in
  `dea-metamodel`. This CR's relationship to the metamodel is "pin and respect";
  it does not redefine upstream rules.
- **Not a process-catalog change.** The process catalog (`dea-catalog-processes`)
  is a different catalog. CR-DEA-BC-05 is the procedure for business
  capabilities. The process catalog may adopt a parallel procedure by analogy but
  that is a separate decision.
- **Not a metadata-cleanup PR.** Drift like "23" in README vs "26" in actual
  counts is acknowledged and fixed as part of the implementation, but the CR
  itself is the procedure, not the cleanup.

## 4. Version semantics

### 4.1 Catalog version

The catalog carries a label of the form `v<N>-<word>` where:

- `<N>` is a positive integer (1, 2, 3, ...).
- `<word>` is one of a small named set: `alpha`, `bravo`, `charlie`, ... in NATO
  phonetic order. A lettered suffix indicates "pre-1.0 stability tier" or
  "stability-tier increment within a major". Words are not version numbers; they
  signal the catalog's stability posture to consumers.

The catalog moves from one lettered suffix to the next on every minor bump.
The numeric component advances on every major bump.

Examples:

- `v1-alpha.0`: initial v1-alpha baseline (the current state).
- `v1-alpha.1`: first minor bump within v1-alpha (additive changes only).
- `v1-alpha.7`: seventh minor bump within v1-alpha.
- `v1-bravo.0`: first minor bump within v1-bravo (a new stability tier was
  declared; this could happen at a major bump or as a stability-tier transition
  without a major bump).
- `v2.0`: first major version (semver-clean; the catalog is stable enough to
  drop the lettered suffix).

The lettered-suffix regime is **only for v1**. From v2 onward the catalog uses
plain `v<N>.<M>` semver (the D3 rule already implies this; the alpha/bravo
suffix is a transitional aid while the catalog is still firming up its
identity). This rule prevents an unbounded vocabulary drift in suffix names.

### 4.2 Capability entry version

Every entry in `entities/v1-alpha/` carries `version: 1.0.0`. This is the
**identity version**, not the catalog version. It advances per semver on the
entry alone:

- **Patch**: corrections to non-identity fields (typos, source citations,
  rationale wording, ECF coordinate refinements that do not change the entry's
  identity).
- **Minor**: substantive change to one entry's definition, business_object,
  outcome, or ECF primary/secondary coordinates (any change that would make a
  consumer's understanding of the entry different in kind, not in degree).
- **Major**: change to entry identity (renamed, split into two, merged with
  another, deprecated-with-replacement).

Identity changes are rare. Most updates will be minor or patch.

### 4.3 Specialization view version

Specialization views (e.g., `mappings/specializations/view-telecom-mcsp.yaml`)
carry their own label of the form `<view-id>@v<N>-<word>.<P>`. The view label
advances independently of the catalog label; an MCSP view at `v1-alpha.0` may
have its content updated without the catalog bumping if the consumer-visible
shape is unchanged.

### 4.4 Metamodel pin

The catalog pins to a specific metamodel version via the top-level
`metamodel_pin: 1.0.0` field on every entry (and on the catalog README). When
the metamodel releases a new major version (e.g., 2.0.0), the catalog must
either upgrade its pin (minor or major catalog bump depending on breaking
changes) or document the incompatibility and refuse the metamodel upgrade until
the catalog is ready.

### 4.5 ECF contract pin

The catalog pins to `dea:ecf@1.0.0` via the `ecfConformance.profile` block on
every entry. This is the **hard pin**: a metamodel-level change that breaks the
ECF contract is a catalog-level major bump, period. This rule is non-negotiable
because the CG-006 consumer-side enforcement gate fails the catalog build on
any drift in `dea:ecf@1.0.0`.

## 5. Bump rules

### 5.1 Patch

A patch bump (e.g., `v1-alpha.0` to `v1-alpha.1` because `<P>` is incremented
in `v1-alpha.<P>`, OR `v1-alpha.0` stays and a tag is cut) is the simplest
case. Anything that does not change a consumer's understanding of the catalog
in kind is a patch: metadata fixes, source citation corrections, prose
clarifications, alignment with the metamodel's bug fixes (not features).

### 5.2 Minor

A minor bump is required when:

- a new canonical first-order capability is admitted (the existing D3 rule);
- a new specialization view is added (e.g., healthcare, financial services,
  public sector beyond MCSP);
- an existing entry's definition, business_object, outcome, or ECF
  primary/secondary coordinates change in a way that alters consumer understanding;
- the schema in `schemas/entity.schema.json` changes in a backwards-compatible
  way (adds a new optional field; relaxes a constraint).

### 5.3 Major

A major bump is required when:

- an existing canonical first-order capability is removed (definition invalidated;
  identity invalidated);
- an existing canonical capability is split into two distinct capabilities;
- two existing canonical capabilities are merged into one (identity changed
  for both);
- the schema in `schemas/entity.schema.json` changes in a backwards-incompatible
  way (removes a field, tightens a constraint, changes a type);
- the metamodel pin changes from 1.x to 2.x;
- the ECF contract pin changes from `dea:ecf@1.0.0` to `dea:ecf@2.0.0`.

Note: bumping a major version is rare in practice. The D3 rule already ensures
additive changes are the common path.

## 6. Consumer pin scheme (three tiers)

Consumers depend on the catalog at three tiers, each stronger than the last:

### Tier 1: ECF contract version (hard pin)

`dea:ecf@1.0.0` is the **contract**. Any catalog content that violates this
contract fails the CG-006 consumer hook on every PR. This is the strongest
guarantee a consumer can have: the catalog content is ECF-conformant. A consumer
that depends only on the ECF contract level gets the strongest stability but
the least specificity (the catalog could add new entries; consumers would need
to handle the new entries).

### Tier 2: Catalog version label (soft pin)

`dea:catalog/business-capabilities@v1-alpha` is the **content pin**. This is
what most consumers want: a specific catalog baseline that has been admitted,
reviewed, and tagged. A consumer that pins to `v1-alpha` knows exactly which 26
canonical entries they get. When the catalog advances to `v1-bravo`, the
consumer must explicitly upgrade.

### Tier 3: Git ref (exact pin)

A specific commit SHA, tag, or branch is the **exact pin**. This is the
strongest specificity a consumer can express. It is brittle (the commit may be
rewritten) but it gives the consumer a frozen contract at the byte level.

### Pin selection guidance

- Tier 1 (ECF contract only) is appropriate for tooling that consumes ECF
  semantics and is content-agnostic.
- Tier 2 (catalog version label) is the recommended default for most
  consumers; it gives stability and is human-readable.
- Tier 3 (git ref) is appropriate when reproducing an exact research result or
  when a consumer has a regulatory need to pin a frozen baseline.

### Manifest expression

Catalog version pinning is declared in a `dependencies.yaml` (or equivalent)
in the consumer repo. The schema for the manifest is part of this CR's
implementation. Manifest fields:

- `ecf_contract`: string, e.g., `dea:ecf@1.0.0` (required).
- `catalogs`: list of catalog pin entries (zero or more).
- `catalogs[].id`: string, e.g., `dea:catalog/business-capabilities`.
- `catalogs[].version`: string, e.g., `v1-alpha`.
- `catalogs[].ref`: optional git ref (tag, SHA, branch).

## 7. Change procedure

Every catalog change follows this procedure:

1. **CR proposal**. A change request is authored under
   `01_change-requests/` in the working folder. The CR specifies the bump tier
   (major, minor, patch) and the rationale. The CR is a doc-only PR landing in
   `change-requests/`; the implementation PRs follow.
2. **Review and acceptance**. The proposal CR is merged into
   `change-requests/`. Acceptance is signified by the merge commit.
3. **Implementation PR(s)**. Each implementation PR carries one logical change
   (one new entry, one metadata fix, one schema change). Implementation PRs
   cite the CR by ID in the body.
4. **CI green**. All CI gates pass on each implementation PR (validate-entries,
   validate-allocation, ecf-conformance-consumer). The drift detector must
   remain `PASS: 0 hard failures, 0 soft warning(s)` (or fewer soft warnings
   than the previous baseline).
5. **CHANGELOG entry**. A new line is added to `CHANGELOG.md` summarising the
   change: tier, scope, rationale, PR number. The CHANGELOG entry is part of
   the implementation PR that triggers the bump.
6. **Tag**. A git tag is cut at the merge commit of the implementation PR that
   triggered the bump. Tag format: `v<N>-<word>.<P>` for lettered-suffix
   versions, `v<N>.<M>` for plain semver. The tag is annotated with the
   CHANGELOG entry's content.
7. **Manifest bump (consumer-side)**. Consumers that pin to the catalog's
   version label advance their pin in lockstep, or explicitly opt to remain on
   the previous label (in which case they accept that they are now behind the
   upstream tip).

The CR author is responsible for steps 1-5. The catalog maintainer is
responsible for step 6. Consumers are responsible for step 7.

## 8. Current posture (initial state)

This CR declares the catalog's current state as:

- **Catalog version**: `v1-alpha`.
- **Patch counter**: `0`.
- **Tag**: `v1-alpha.0` (to be cut as part of this CR's implementation).
- **Canonical entries**: 26 (admitted via PR #32).
- **Specialization views**: 1 (`view-telecom-mcsp`, L3, telecom).
- **Deferred decisions**: 1 (SPEC-D1 CAND-005/CAND-006 unification; G5-gated).
- **Held-unmapped**: 1 (CAND-019 Technology Management; ECF overlay v0.2).
- **ECF contract pin**: `dea:ecf@1.0.0`.
- **Metamodel pin**: 1.0.0.
- **Method**: CR-DEA-BC-01 (method docs normative).
- **Schema**: `schemas/entity.schema.json` (CR-DEA-BC-03).

The current posture section is **imperative**: this CR records the actual
state at the time of acceptance. Future CRs reference this section as the
baseline.

## 9. Implementation plan

The implementation of CR-DEA-BC-05 (a separate PR(s) after the proposal is
accepted) does the following:

1. Add `docs/VERSIONING.md` (this CR's content, lifted from the CR).
2. Add `CHANGELOG.md` with the v1-alpha.0 entry recording the catalog's
   current state.
3. Add `dependencies.yaml` schema and the catalog's own manifest declaring
   its ECF pin, metamodel pin, and version label.
4. Cut the `v1-alpha.0` tag on `main` after the implementation merges.
5. Reconcile drift: update `README.md` from "23 canonical" to "26 canonical"
   and any other stale "23" references found in `*.md` / `*.yaml` (excluding
   historical documents that record the v0.1 admission of 23 entries).
6. Add `scripts/check_versions.py` (CI guard): asserts every entry has
   `version`, the catalog's documented baseline matches the actual entry
   count, and every entry's `ecfConformance.profile` matches the declared
   ECF contract pin.

The implementation is the **only place** where drift fixes land. The CR itself
does not carry the fixes; the CR carries the rules and the current-state
declaration.

## 10. Acceptance criteria

The CR is accepted when:

| AC | Criterion | Status |
|---|---|---|
| AC1 | `docs/VERSIONING.md` exists and is normative | proposed |
| AC2 | `CHANGELOG.md` exists with v1-alpha.0 entry | proposed |
| AC3 | `dependencies.yaml` schema declared in VERSIONING.md | proposed |
| AC4 | Catalog manifest declares ECF pin, metamodel pin, version label | proposed |
| AC5 | `v1-alpha.0` tag is cut on `main` post-implementation | proposed |
| AC6 | Drift fixes (23 → 26, etc.) are scoped and landed | proposed |
| AC7 | `scripts/check_versions.py` is a CI gate | proposed |
| AC8 | Method documents (METHODOLOGY.md, GOVERNANCE.md) cite VERSIONING.md | proposed |
| AC9 | The bump rules in section 5 hold for the next 5 admitted changes | open (verified over time) |

## 11. Open questions for review

| # | Question | Proposed answer | Decision |
|---|---|---|---|
| Q1 | What triggers a catalog major version (v1-alpha → v2)? | Removing, splitting, or merging existing canonical entries; schema breaking change; metamodel 2.x; ECF contract 2.x. | **default proposed; reviewer confirm** |
| Q2 | What triggers a catalog minor version (v1-alpha → v1-bravo)? | Adding a new canonical entry (D3); adding a new specialization view; backwards-compatible schema change. | **default proposed; reviewer confirm** |
| Q3 | How should consumers pin? | Three tiers: ECF contract (hard), catalog version label (soft), git ref (exact). | **confirmed 2026-09-02** |
| Q4 | Tag every catalog baseline? | Yes; tag format `v1-alpha.<P>`; CHANGELOG generated from merged PRs. | **confirmed 2026-09-02** |

Reviewer: please confirm or override Q1 and Q2 before this CR is merged.

## 12. References

- `dea-metamodel/metamodel/dea-metamodel.yaml`; top-level metamodel version 1.0.0.
- `dea-metaframework/...`; ECF contract 1.0.0 (CR-ECF-CG-001).
- `dea-catalog-business-capabilities/CHANGELOG.md` (to be created); version timeline.
- `dea-catalog-business-capabilities/docs/VERSIONING.md` (to be created); normative procedure.
- `dea-catalog-business-capabilities/dependencies.yaml` (to be created); catalog manifest.
- `dea-catalog-business-capabilities/scripts/check_versions.py` (to be created); CI guard.
- `dea-catalog-business-capabilities/entities/v1-alpha/*.yaml`; canonical entries.
- `dea-catalog-business-capabilities/mappings/specializations/view-telecom-mcsp.yaml`; first specialization view.