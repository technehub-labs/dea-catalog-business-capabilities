# ECF Overlay v0.2: Canonical Posture

CR-DEA-BC-04 stage; post-PR-32. Status: **admitted-canonical-overlay** (replaces preliminary v0.1). Machine-readable: `ecf-overlay-v0.2.yaml`.

## Headline

- **26 canonical first-order capabilities** (23 from BC-04 admission + 3 admitted at PR #32: CAND-018 Analytics and Intelligence, CAND-023 Resilience, CAND-029 Innovation).
- **1 held-unmapped**: CAND-019 Technology Management (N-006: business capability stands, ECF legitimately absent).
- **2 candidates withdrawn** from the first-order track per normalization: CAND-004 (N-007, reclassified as grouping parent; children admitted separately) and CAND-011 (N-008, dissolved; CAND-012 Operations is the surviving first-order child).
- **14 distinct primary coordinates** referenced out of 49 canonical coordinates; **no forced coverage** (per CG-005 Invariant 7).

## Rules applied (carried from v0.1)

- Primary coordinate marks earliest legitimate initiation (FOUNDATIONS section 11, ECF lifecycle rule).
- Secondary coordinates record legitimate participation only.
- No forced coverage: empty cells are valid results (CR section 27).
- Semantic conflicts are flagged, not smoothed (CR section 26).

## Decisions applied

### Normalization (N-001..N-009)

- **N-001**: People cluster -> Workforce Management (CAND-015)
- **N-002**: Marketing is distinct, not a child (CAND-010)
- **N-003**: Analytics stays a provisional child of Information Management (later resolved by R-008 as distinct)
- **N-004**: Sourcing/Procurement and Supplier Management are distinct (CAND-025 vs CAND-007)
- **N-005**: Section 20 example resolved
- **N-006**: Technology Management stands; its coordinate does not (held_unmapped)

### Review (R-001..R-008)

- **R-001** (CAND-008, Partner Management dual-home tension): defensible-as-recorded.
  - Partnering initiated at customer-demand × conceive; supply-side operation is legitimate participation; dual-home tension expressed, not smoothed.
- **R-002** (CAND-010, Marketing placement): defensible-as-recorded.
  - N-002 settled Marketing distinct from Customer and Offering; primary customer-demand × conceive is honest.
- **R-003** (CAND-017, Information Management span): defensible-secondaries-deliberately-empty.
  - The span of information across domains is a property of the business object, not of initiation; enumerating all domains would violate honest-not-exhaustive.
- **R-004** (CAND-019, Technology Management unmapped): N-006-resolved.
  - Business capability, business object Technology; ECF legitimately absent (L5 concern, no domain carries technology). Section 38 legitimately-absent clause applies.
- **R-005** (CAND-028, Change Management cross-domain): defensible-as-recorded.
  - Earliest initiation governance-existence × improve; cross-domain applicability is an object property, not a mapping defect.
- **R-006** (CAND-023, Resilience boundary vs Risk/Security): deferral-lifted; admitted-at-PR-32.
  - ISO 22301 draws the boundary against Risk (uncertainty treatment) and Security (protection); BCI GPG 7.0 carries the all-sector applicability claim; evidence E4, generality 8/10 strong.
- **R-007** (CAND-029, Innovation boundary vs Change): deferral-lifted; admitted-at-PR-32.
  - ISO 56002 draws the boundary against Change Management (innovation originates the new; change institutionalizes it); Oslo Manual 2018 names innovation management as a distinct activity class; evidence E4, generality 8/10 strong.
- **R-008** (CAND-018, Analytics boundary vs Information): distinct-first-order; admitted-at-PR-32.
  - Reading A: stewardship ends where derivation begins; operations-delivery × operate (primary), secondaries empty per R-003 parity; record shape conforms; no layering violation. Boundary decision: docs/research/boundary-decision-cand-018 v0.1, PR #29.
- **N-007** (CAND-004, Stakeholder Relationship Mgmt grouping): reclassified-as-grouping-parent; withdrawn-from-admission.
  - Aggregate parent; children admitted separately (CAND-005 Customer Mgmt, CAND-006 Citizen/Member, CAND-007 Supplier Mgmt, CAND-008 Partner Mgmt). Non-redundancy rule (BIZBOK SRC-001) applies.
- **N-008** (CAND-011, Value Delivery aggregate): dissolved-as-first-order.
  - Aggregate candidate; boundary dissolved when children admitted (CAND-012 Operations is the first-order child that survives).

## Coverage map (canonical, 27 entries: 26 admitted + 1 held-unmapped)

| ECF Domain | Capabilities (primary coordinate) |
|---|---|
| governance-existence | Change Management (improve); Compliance Management (activate); Enterprise Governance (conceive); Legal Management (conceive); Resilience Management (design); Risk Management (conceive); Security Management (design); Strategic Planning (conceive); Strategy (conceive) |
| supply-resources | Asset Management (build); Facility Management (activate); Sourcing and Procurement (build); Supplier Management (build) |
| operations-delivery | Analytics and Intelligence (operate); Information Management (operate); Operations (operate) |
| customer-demand | Citizen / Member Relationship (operate); Customer Management (operate); Marketing (conceive); Partner Management (conceive) |
| finance-value | Financial Management (operate); Financial Stewardship (conceive) |
| product-offering | Innovation Management (conceive); Offering Management (conceive) |
| people-organization | People / Workforce Management (build); Workforce Planning (design) |
| <unmapped> | Technology Management (<unmapped>) |

## Empty cells (legitimate, per CR section 27)

- governance-existence x build, activate
- finance-value x design, build, activate, retire (primary)
- people-organization x conceive, retire (primary)

## Conflicts carried forward (CR section 26)

- CAND-008
- CAND-010
- CAND-017
- CAND-018
- CAND-019
- CAND-028

## Coordinate coverage (canonical 7x7 = 49)

- Referenced (primary + secondary): 27 of 49
- Unreferenced: 22
- Per CG-005 Invariant 7, unreferenced coordinates are legitimate; the catalog is not required to populate all 49.

## Reading the overlay

The overlay is now canonical, anchored in the admitted 26-entry catalog. The 14 distinct primary coordinates used (with secondaries expanding to 17 unique coordinates) cluster in governance-existence (9 entries: Strategy, Strategic Planning, Enterprise Governance, Risk, Compliance, Legal, Resilience, Security, Change) and supply-resources (4: Supplier Mgmt, Sourcing/Procurement, Asset Mgmt, Facility Mgmt). Customer-demand holds 4 (Customer Mgmt, Citizen/Member, Partner Mgmt, Marketing); operations-delivery holds 3 (Operations, Information Mgmt, Analytics and Intelligence); finance-value holds 2 (Financial Stewardship, Financial Management); people-organization holds 2 (Workforce Mgmt, Workforce Planning); product-offering holds 2 (Offering Mgmt, Innovation). Technology Management is the only held-unmapped entry, with the rationale locked by N-006.

## Carried forward from v0.1 (open items)

- CAND-019 (N-006): business capability stands, ECF legitimately absent; reflected in catalog as `held_unmapped` with the rationale note. No further action.
- CAND-017 (Information Management) span: R-003 records that secondaries are deliberately empty; the span is a property of the business object, not of initiation. No further action.
- CAND-028 (Change Management) cross-domain applicability: R-005 records as object property, not mapping defect. No further action.

## Cross-references

- **ECF Conformance Profile**: `dea:ecf@1.0.0` (CR-ECF-CG-003). Each entry carries an `ecfConformance` block reconciling its kebab-case classification to canonical PascalCase enums.
- **CG-005 Invariant 7**: no cell population requirement. Unreferenced coordinates are legitimate.
- **CG-001 Conformance Gate**: catalog is **CONFORMANT-WITH-EXTENSION**; this overlay is the governance record behind the gate verdict.
