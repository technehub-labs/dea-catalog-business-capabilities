# Preliminary ECF Overlay v0.1: Summary for Review

CR-DEA-BC-02 staged delivery, step 3: Preliminary ECF Overlay (CR §33 item 8, rules per §25:§28).
Date: 2026-08-31. Status: candidate-not-canonical. Machine-readable: `preliminary-ecf-overlay.yaml`.

## Rules applied

- Primary coordinate marks earliest legitimate initiation (FOUNDATIONS §11, ECF lifecycle rule)
- Secondary coordinates record legitimate participation only
- No forced coverage: empty cells are valid results (CR §27)
- Semantic conflicts are flagged, not smoothed (CR §26)

## Coverage map (first-order candidates only, 29)

| ECF Domain | Candidates (primary) |
|---|---|
| governance-existence | Strategy, Strategic Planning, Enterprise Governance, Risk, Compliance, Legal, Resilience, Security, Change (9) |
| customer-demand | Stakeholder Relationship Mgmt, Customer Mgmt, Citizen/Member, Partner Mgmt, Marketing (5) |
| product-offering | Offering Management, Innovation (2) |
| operations-delivery | Value Delivery, Operations, Information Mgmt, Analytics (4) |
| finance-value | Financial Stewardship, Financial Management (2) |
| supply-resources | Supplier Mgmt, Sourcing/Procurement, Asset Mgmt, Facility Mgmt (4) |
| people-organization | People/Workforce Mgmt, Workforce Planning (2) |

One candidate held unmapped: Technology Management (CAND-019), see conflicts.

## Semantic conflicts flagged (CR §26)

1. **CAND-019 Technology Management**: no ECF domain carries technology (technology is a layer concern, L5, not an ECF domain). Mapping to any domain would be forced. Held unmapped with the open question: is Technology Management a business capability with a domain, or a cross-cutting governance concern? Carried to the normalization pass.
2. **CAND-017 Information Management / CAND-018 Analytics**: mapped to operations-delivery × operate, but both span domains (information flows everywhere). Flag: if the span is legitimate, secondary coordinates grow; if not, the candidate may be cross-cutting like technology. Pending.
3. **CAND-028 Change Management**: stage-anchored (improve) but cross-domain by nature. Mapped governance-existence × improve with conflict note: change is an enterprise-wide concern that may not own a domain.
4. **CAND-008 Partner Management**: partners sit between supply-resources (they supply) and customer-demand (they demand). Mapped customer-demand × conceive with a weak-mapping flag.

## Empty cells (legitimate, per CR §27)

- governance-existence × build, activate: no candidate initiates there; governance conceives, then operates. Legitimately empty.
- finance-value × design, build, activate, improve, retire (except secondary participation): financial stewardship conceives and operates; the enterprise does not "design" finance as a stage. Legitimately empty.
- people-organization × conceive, retire: workforce is built, then operated and improved. Legitimately empty.

## Reading the overlay

The overlay is evidence, not architecture: the governance-existence cluster (9 candidates) says the corpus sees governance/direction/assurance as the densest first-order region; the thin product-offering row (2) says offering-side candidates are fewer but not missing. Neither observation fills a cell; both inform the normalization and admission passes.

## Carry-forward

1. Resolve CAND-019 (Technology Management) domain question in the normalization pass
2. Re-test CAND-017/018/028 after normalization decisions
3. Overlay feeds CR-DEA-BC-03 coordinate assignment only after admission gate §38
