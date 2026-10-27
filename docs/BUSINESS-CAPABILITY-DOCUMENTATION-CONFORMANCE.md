# Business Capability Documentation Conformance

**Status**: Normative validation contract (CR-DEA-BC-45, 2026-10-28)
**Implements**: the deterministically checkable subset of the [Documentation Standard](BUSINESS-CAPABILITY-DOCUMENTATION-STANDARD.md) (CR-41) at the entity-README layer, per the [README Standard](BUSINESS-CAPABILITY-README-STANDARD.md) (CR-44)
**Gate**: `scripts/check_doc_conformance.py` (CI step in `validate-entries.yml`)

---

## 1. What this validates — and what it does not

Five validation layers (CR-45 §5): **structural** (files and section markers), **schema** (delegated — unchanged, `validate-entries` inline Draft7 validator remains authoritative), **referential** (links and id resolution), **cross-artifact** (README ↔ record agreement), and **semantic review** (human; not automatable). This gate implements layers 1, 3, and 4 only. It expressly does **not** prove: enterprise generality, definitional soundness, evidence sufficiency, boundary quality, ECF-rationale correctness, or capability distinctness — those stay with the method gates and human review (CR-41 §9).

## 2. Rule catalogue

Rule IDs `DCV-001..010`, mapped to requirement IDs `BC-DOC-001..012` (no namespace conflict with existing gate codes AUT/ES/IDM/CST/DL/CR-001..005). Authoritative table: the gate script's docstring; summary:

| Rule | Layer | Source | Severity | Check |
|---|---|---|---|---|
| DCV-001 | Structural | BC-DOC-011 | blocking | entity README exists per canonical subtree |
| DCV-002 | Structural | BC-DOC-011 | blocking | all 14 contract sections present |
| DCV-003 | Cross-artifact | BC-DOC-001/012 | blocking | README H1 = record `name` |
| DCV-004 | Cross-artifact | BC-DOC-001/012 | blocking | record `id` rendered exactly |
| DCV-005 | Cross-artifact | BC-DOC-012 | blocking | canonical `definition` quoted verbatim (blockquote) |
| DCV-006 | Cross-artifact | BC-DOC-001/012 | blocking | `version` + `lifecycle_status` rendered and agreeing |
| DCV-007 | Referential | BC-DOC-012 | blocking | README links its own record file; link resolves |
| DCV-008 | Referential | BC-DOC-012 | blocking | record `related_capabilities` ids resolve to canonical records |
| DCV-009 | Structural | BC-DOC-011 | warning | purpose/realization/assessment sections carry an explicit honest state or substantive content |
| DCV-010 | Cross-artifact | BC-DOC-001/012 | blocking | primary ECF coordinate rendered correctly |

Severity is normative (CR-45 §7): blocking = violation of a mandatory structural/referential/cross-artifact requirement; warning = review prompt where automation cannot judge substance. Exceptions are governed per CR-45 §7 — never silent suppression.

## 3. Activation model

Baseline at acceptance (2026-10-28): **523 blocking, 87 warnings** across the 29 pre-standard stub READMEs — recorded as the Phase-A baseline of the CR-DEA-BC-46 remediation. CI runs the gate **advisory** (no `--strict`; blocking findings reported, exit 0) so the pre-existing state does not red `main`. CR-DEA-BC-46 performs the remediation and flips the CI step to `--strict`; from that landing, blocking documentation findings fail `validate-entries`.

## 4. Failure handling

Failures name the rule, the entity, and the artifact; remediation guidance is the README Standard section each rule maps to. Deterministic: identical inputs produce identical findings. No network checks. Regeneration of findings is the reproduction mechanism for any conformance claim.

## 5. Tests

`--self-test` fixtures (conformant + multi-rule-violation cases) and `tests/test_check_doc_conformance.py` cover valid, invalid, and honest-state cases (CR-45 §8.5).
