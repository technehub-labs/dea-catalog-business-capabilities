# Business Object Identity Reconciliation (U-1)

**Status**: Accepted investigation (CR-DEA-BC-58, 2026-10-28) · **Disposition: U-1 remains blocked upstream** · No record/schema changes

## 1. Upstream contract inspection (2026-10-28)

`dea-catalog-business-objects` is a Wave 3 scaffold: `entities/v1-alpha/` contains **zero entity directories** (verified via the GitHub API at this CR's landing). No canonical Business Object identities exist; the catalog's identity scheme (expected `objects:*` per the org namespace table) has never been exercised by an admission. An identity contract cannot be confirmed from an empty catalog — and this CR may not define the upstream scheme on its behalf.

## 2. Current-value reconciliation register

All 29 records carry populated `business_object` descriptive values; 28 distinct values (register in `reconciliation/business-object-reconciliation-register.yaml`). Classification per value:

| Class | Count | Handling |
|---|---|---|
| Single descriptive value, plausible single future object | 26 | retained as valid descriptive text; no canonical target exists yet |
| Compound expression (`Asset/Information`, `Market/Customer`) | 2 | flagged for **semantic review at the upstream catalog's first admissions** — a compound may resolve to one composite object, two objects, or stay descriptive; no local decision |
| Unresolved / unsupported | 0 | — |

Lexical similarity is not semantic identity: no match is proposed until the upstream catalog provides canonical entities and this record's values are reconciled against them by review.

## 3. Reference strategy (recommended, deferred)

When the objects catalog admits its first entities: reconcile values by semantic review; the likely model is **typed reference plus retained human-readable label** (validates against the objects catalog; keeps prose readability), with compounds resolved by review (possibly multi-reference). Backward-compatible migration, dual-source-of-truth safeguards, and validation against the upstream catalog follow in a separately authorized implementation CR.

## 4. Disposition

**U-1: blocked upstream** — the Business Objects catalog is an empty scaffold; its identity contract is unexercised. Blocker condition for closure: first canonical admissions in `dea-catalog-business-objects`. Until then, `business_object` remains valid descriptive text (its current schema contract).
