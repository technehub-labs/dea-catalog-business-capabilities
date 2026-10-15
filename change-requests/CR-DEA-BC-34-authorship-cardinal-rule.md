# CR-DEA-BC-34: Authorship Cardinal Rule (Org-Wide Propagation Slice)

| Field | Value |
|-------|-------|
| **CR** | CR-DEA-BC-34 |
| **Title** | Authorship Cardinal Rule (R1, R2) - Org-Wide Propagation Slice (dea-catalog-business-capabilities) |
| **Status** | Accepted (per user directive 2026-10-13: "no Coder/Agent anywhere") |
| **Layer** | L1 (Business Capability Catalog) |
| **Depends on** | CR-BP-118 (org-wide authorship cardinal rule, main authority) |
| **Companion to** | CR-DEA-BC-34 (sibling slices in dea-catalog-business-objects, dea-catalog-organizational-units, dea-metaframework) |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-13 |

## 1. The cardinal rule (pinned)

Two cardinal rules from CR-BP-118 (org-wide authority) are propagated to this
repo (dea-catalog-business-capabilities):

- **R1 (Authorship-field cardinal rule)**: every authorship-bearing field must
  carry a value from the allowlist `{Emmanuel A. Otchere, TechNeHub Labs}`.
  Substring matches against the denylist
  `{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}` are
  blocking (AUT-001).
- **R2 (Named-role file cardinal rule)**: any file or field whose purpose is
  to name a person playing a named role must carry the canonical identity.

The rules are CR-level (immutable by a gate change) and governance-doc-level
(immutable by a code change).

## 2. The retro sweep (BC-repo scope)

| Field set | Hits replaced | Notes |
|---|---:|---|
| `**Owner**` (markdown) | 12 | change-requests/CR-*.md |
| `**Author**` (markdown) | 13 | change-requests/CR-*.md |
| `**Carrier:**` (markdown) | 1 | CR-DEA-BC-18 |
| Table-row `\| **Author** \| Coder ...` | 4 | ECF-CG-003, BC-01A, BC-03, BC-04 |
| `actor:` (YAML) | 4 | catalog-research/candidates.yaml |
| `reviewer:` (YAML) | 23 + 3 | catalog-research/admission-review*.yaml |
| `author:` (YAML) | 1 | catalog-research/recon/INV-AI-v0.1.yaml |
| `compiled_by:` (YAML) | 1 | evidence-register.yaml |
| `registered_by:` (YAML) | 3 | evidence-register.yaml |
| `evidence_seeded_by:` (YAML) | 1 | evidence-register.yaml |
| `admitted_by:` (YAML) | 1 | evidence-register.yaml |
| Single-quoted multi-line `actor: 'Coder ...'` | 22 | entity capability YAML |
| Prose `Reviewer of record: Coder (for eaojnr).` | 1 | catalog-research/ADMISSION-REVIEW-v0.1.md |
| Prose `with Coder as engineering agent` | 1 | GOVERNANCE.md (dropped) |

Total: 73 files, ~93 textual replacements. 0 entity content changes; 0 id
changes; 0 cross-reference changes.

## 3. The gate (BC-repo, blocking)

- **AUT-001 (blocking)**: substring denylist against
  `{Coder, Agent, Hermes, Claude, GPT, Cline, OpenAI, MiniMax, MiniMax-M3}`.
- **AUT-002 (blocking)**: parent-block present but field empty.
- **AUT-003 (advisory, blocking under --strict)**: value not in allowlist.

Data-driven from `reconciliation/authorship-fields.yaml`. Fields registered
for the BC repo (per the field shape this repo uses):

| Path | file_glob | prefix_match |
|---|---|---|
| `**Owner**` | `change-requests/CR-*.md` | (default: exact) |
| `**Author**` | `change-requests/CR-*.md` | (default: exact) |
| `actor` | `catalog-research/candidates.yaml` | true |
| `reviewer` | `catalog-research/admission-review*.yaml` | true |
| `compiled_by` | `catalog-research/evidence-register.yaml` | true |
| `registered_by` | `catalog-research/evidence-register.yaml` | true |
| `evidence_seeded_by` | `catalog-research/evidence-register.yaml` | true |
| `admitted_by` | `catalog-research/evidence-register.yaml` | true |
| `author` | `catalog-research/*.yaml` | true |

The `prefix_match: true` opt-in is new for the BC repo: actor / reviewer
values are routinely followed by rich context (e.g.
`actor: "Emmanuel A. Otchere, BC-13 B.1 Track A candidate seeded"`), and
exact-match AUT-003 would false-positive on the trailing context. The
118a (dea-catalog-business-processes) gate still uses exact-match because
its fields don't carry the same trailing context.

The gate value-extractor strips surrounding quote characters before
allowlist comparison. This is a gate change vs. 118a: 118a's values are
unquoted and didn't surface the bug, but the BC repo's `actor: "..."` and
`registered_by: "..."` quoted values would otherwise false-positive. The
behavior change is documented in the gate's docstring.

## 4. CI wiring

A new workflow `.github/workflows/validate-authorship.yml` runs the gate
in `--strict` mode on every push and PR. The gate has its own per-repo
test module `tests/test_check_authorship.py` (21 tests, 21/21 pass on
the BC repo's tree).

## 5. Out of scope (CR-118c, deferred)

Prose-content occurrences of `Agent` / `Coder` / etc. in record `name` /
`definition` / `description` fields (not the authorship-metadata fields)
are inventoried for the 118c follow-on but not rewritten in this slice.

## 6. Test posture

- 21/21 `test_check_authorship` pass (incl. the bounded-walker regression
  test carried from 118a, the registry-loads test relaxed to per-repo
  baseline, and the per-field round-trip tests).
- Gate `--strict` exit 0 against the live BC tree.
- Gate non-strict 0 blocking, 0 advisory.

## 7. Carrier

This document. Plus the CHANGELOG `[Unreleased]` entry and the new
`.github/workflows/validate-authorship.yml` workflow.
