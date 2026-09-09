# CR-DEA-BC-09: Naming Conformance Refresh and Definition Template

**Status**: Landed
**Layer**: Catalog (business capabilities)
**Owner**: Coder (for eaojnr)
**Date**: 2026-09-08
**Landing commit**: `04945946ff85a66c29c5bda4ba4a762762e6964e` (PR #54)
**Tag**: `v1-alpha.3`
**Depends on**: CR-DEA-BC-01 (naming rules); CR-DEA-BC-05 (versioning); CR-CATALOG-STRUCT-03a/03b (layout)
**Related**: CR-DEA-BC-02 (normalization register; N-010..N-015 appended); CR-DEA-BC-04 (MCSP view reference updates)

## 1. What this CR is

A naming conformance pass over the canonical 26, plus the formalization of the
definition template that the catalog already follows de facto.

Two triggers:

1. A documented-rules refresh: TAXONOMY.md section 6/7 had drifted from the
   post-STRUCT-03 repository layout (`docs/research/` pointer, "the canonical
   23", flat-layout sketch), and section 1 rule 2 (business-object anchored)
   needed clarification on whether anchoring means literal token containment.
2. A retroactive conformance sweep (eaojnr, 2026-09-08): apply the naming rules
   to the existing 26 entries and fix what fails; formalize the definition
   template so the de facto "The ability to ..." convention becomes an
   enforceable rule.

The sweep found zero rule-1/3/4/5 violations (no verb-led names, no
implementation references, no outcome names, no industry qualifiers) and six
rule-2 candidates. Of the six, five fail anchoring under the clarified rule
and are renamed; the sixth (Security Management) is reviewed-retained per the
N-001 precedent because its compound business object cannot be named literally
without violating rule 6.

## 2. Rule clarification (TAXONOMY.md section 1, rule 2)

Anchoring is semantic, not literal token containment. The name identifies the
object class the ability manages. Literal containment is not required where the
plain-vocabulary name of the ability-domain is the standard corpus term (N-001:
Workforce Management; N-015: Security Management). Conversely, a name whose
head noun is a state, quality, act, or outcome rather than the object class
fails anchoring, as does a name that carries only the object's adjective.

Rule 4 is extended in kind: a state or quality the enterprise has (Compliance,
Resilience) is outcome-adjacent and disqualifying as the head noun.

## 3. Definition and outcome shape (new TAXONOMY.md section 1A)

The definition rule the user assumed existed did exist semantically
(METHODOLOGY.md section 11: "Definition - per Section 1 semantics") but had no
syntactic template. Section 1A formalizes the converged convention:

- **Definition template**: a single sentence opening "The ability to <verb-phrase>
  ...", naming the business object (or its plain-vocabulary domain term) and the
  scope of the ability; no organization, system, vendor, or technology
  reference; no outcome language.
- **Outcome shape**: a result sentence describing the state that obtains when
  the ability operates; never restates the ability.

All 26 definitions already conformed to the template before this CR; section 1A
makes the convention enforceable (`scripts/check_naming.py`, wired into
`validate-entries.yml`).

## 4. Renames (N-010..N-015)

| # | Candidate | Old name | New name | Basis |
|---|---|---|---|---|
| N-010 | CAND-021 | Compliance Management | Regulation Management | "Compliance" is a conformity state (rules 2, 4); object is Regulation |
| N-011 | CAND-014 | Financial Management | Financial Resource Management | object adjective only (rule 2); matches BIZBOK source term |
| N-012 | CAND-029 | Innovation Management | Idea Management | "innovation" reads as act (rule 1) or produced novelty (rule 4); object is Idea |
| N-013 | CAND-022 | Legal Management | Legal Matter Management | object adjective only (rule 2); legal-operations vocabulary |
| N-014 | CAND-023 | Resilience Management | Continuity Management | "resilience" is a property (rule 4); object is Continuity |
| N-015 | CAND-024 | Security Management | **retained** | compound object (Asset/Information) precludes plain object-literal naming; N-001 precedent |

Each renamed entry:

- `id` moves with the name (TAXONOMY section 5 ties id to slug):
  `dea:capability-compliance-management` -> `dea:capability-regulation-management`,
  and likewise for the other four. The former id is not reused (section 2.3).
- `aliases` records the former canonical name (section 2.1).
- `version` 1.0.0 -> 2.0.0 (identity change; VERSIONING section 1.2 major).
- `definition` is lightly re-anchored to echo the object (the template's
  object-naming requirement); semantics unchanged.
- ECF coordinates, capability_layer, outcome, evidence, provenance ladder, and
  ecfConformance blocks are unchanged.

N-012 note: changing `business_object` from Idea to Innovation was considered
and deferred. A business_object change is an evidence-bearing semantic change,
out of scope for a naming conformance pass. Parked.

## 5. Reference updates

- `mappings/specializations/view-telecom-mcsp.yaml`: SPEC-006 parent and four
  inherited references updated to the new ids. View content otherwise unchanged.
- `mappings/specializations/VIEW-TELECOM-MCSP.md`: SPEC-006 parent name.
- Referencing entries: `dea:capability-risk-management` (related_capabilities
  ids + boundary prose), `dea:capability-financial-stewardship`
  (related_capabilities id + three prose mentions), `dea:capability-asset-management`
  (boundary prose), `dea:capability-strategic-planning` (non-example prose).
  Cross-references between the renamed pair (Regulation <-> Legal Matter)
  updated in both directions.
- `catalog-research/ECF-OVERLAY-v0.2.md` (canonical overlay): coverage table
  and reading paragraph cite the new canonical names, with a CR-DEA-BC-09
  provenance note. `catalog-research/ecf-overlay-v0.2.yaml` keeps the candidate
  register names (candidate-keyed provenance; CR-DEA-BC-07 precedent).
- `catalog-research/normalization.yaml`: N-010..N-015 appended; register header
  noted.
- `README.md` and `entities/v1-alpha/README.md`: the PR-32 admission narrative
  cites current canonical names with the rename noted.
- `CHANGELOG.md`: v1-alpha.3 entry.
- `CATALOG.yaml`: regenerated (never hand-edited).

## 6. Version bump

Catalog label: `v1-alpha.2` -> **v1-alpha.3** (minor within the lettered
regime). Tag `v1-alpha.3` to be cut at the merge commit.

Bump rationale (VERSIONING section 2): no capability is removed, split, merged,
or admitted; the five identity renames are recorded with alias continuity and
normalization-register traceability. The lettered-suffix regime exists for
exactly this class of pre-stability identity correction (section 1.1). Entry
versions for the five renamed entries advance 1.0.0 -> 2.0.0 per section 1.2
(identity change). Consumers pinning by entry id (tier 2/3) must remap the five
ids; consumers pinning the catalog label or the ECF contract are unaffected.

## 7. Enforcement

`scripts/check_naming.py` (new) enforces at CI time: verb-led name detection
(rule 1), disqualifying markers (rule 3), outcome markers (rule 4), industry
qualifiers (rule 5), the definition template (section 1A.1), and the
outcome-restatement ban (section 1A.2). Object-anchoring (rule 2) is advisory
only: the lint warns when the business_object is not echoed in name or aliases.
Rule 2 and rule 6 remain semantic-review judgments (METHODOLOGY.md section 12,
Gate 1). Wired into `.github/workflows/validate-entries.yml` as a new step.

Post-CR advisory set (5, all documented in the script docstring): Strategy
(Enterprise), Analytics and Intelligence (Insight), Enterprise Governance
(Decision), Sourcing and Procurement (Purchase Order), Security Management
(Asset/Information; N-015).

## 8. Deliberately NOT in this CR

- No rename of Security Management (N-015 reviewed-retained).
- No `business_object` changes (N-012's Idea -> Innovation question is parked
  as evidence-bearing, not a naming question).
- No edits to historical research artifacts: `candidates.yaml`,
  `ECF-OVERLAY-v0.1.md`, `preliminary-ecf-overlay.yaml`, admission records,
  prior CRs, and the candidate-keyed `ecf-overlay-v0.2.yaml` name fields are
  provenance.
- No edit to published `out/` snapshots (immutable per CR-DEA-BC-05/06).
- `dependencies.yaml` self-ref stays at `v1-alpha.2` in this PR; it advances to
  `v1-alpha.3` when the tag is cut (VERSIONING section 4 step 6, maintainer
  action at merge).

## 9. Verification (all local, pre-push)

- `scripts/check_naming.py`: PASS (26 entries; 5 advisories, the documented set)
- `scripts/check_ecf_conformance.py`: PASS (26 entries + MCSP view)
- `scripts/check_versions.py`: PASS
- `scripts/check_view_refs.py`: PASS (SPEC-006 parent resolves)
- `scripts/check_catalog_index.py --schema ...`: OK (26 entities)
- `scripts/check_visual_domain_labels.py`: PASS
- Entry schema validation (jsonschema draft-07, CI-equivalent): 26/26 clean
- Dash check (no en/em dashes): clean on all touched files
- `git diff --check`: clean
- Secret-pattern scan: clean

## 10. Pause-for-merge

Per CR-programme convention. After you say **Merge**, I will:

1. Merge this PR to main.
2. Cut the `v1-alpha.3` tag at the merge commit.
3. Advance `dependencies.yaml` self-ref to `v1-alpha.3` (maintainer action at
   merge).

Nothing moves until you say Merge.
