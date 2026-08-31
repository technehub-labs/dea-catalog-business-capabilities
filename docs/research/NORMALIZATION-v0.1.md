# Normalization Register v0.1: Summary for Review

CR-DEA-BC-02 staged delivery, step 4: Candidate Normalization (CR §20; §33 item 5).
Date: 2026-08-31. Machine-readable: `normalization.yaml`. Rule applied throughout: no merge solely because names are similar (§20).

## Decisions

### N-001: People cluster → Workforce Management
Human Capital Management and People Management are **synonyms** of the same construct; the canonical candidate name is **Workforce Management** (noun-anchored on the Workforce business object, without the asset framing of "capital"). **Human Resources / HR is rejected as a capability name**: it names the function or organization (the CAND-030 pattern), not the ability. CAND-015 renamed; aliases recorded.

### N-002: Marketing is Distinct, not a child
Marketing's business object is demand creation in a market: not the customer relationship (CAND-005) and not the offering (CAND-009). APQC places it as its own category. **Distinct, standalone first-order candidate**; parent chain cleared. Diversity edge noted: government/non-profit equivalents (outreach, enrollment communication) feed the §8 test.

### N-003: Analytics stays a provisional child of Information Management
Analytics' business object is the insight, not the information, but the corpus is inconsistent (some models make it a theme, others fold it in). E3 evidence + low confidence means splitting now would outrun the evidence. **Parent-child retained**; re-test trigger recorded against the enterprise-generality matrix.

### N-004: Sourcing/Procurement and Supplier Management are Distinct
Different business objects (the acquisition vs the relationship), demonstrably separable in practice (spot buying without relationship management; alliance management without current spend). **No merge.** Confidence: high.

### N-005: The §20 example resolved
Customer Relationship Management is a **synonym** of Customer Management (and doubles as a system category, already disambiguated at CAND-032). Customer Administration is **overlapping**: a child-scope fragment, not a synonym. Aliases recorded on CAND-005.

### N-006: Technology Management stands; its coordinate does not
The ECF overlay conflict resolves by the §38 clause: the capability is real (durable business object: Technology), but no ECF domain carries technology because ECF domains are business-semantic and technology is an L5 layer concern. **ECF mapping declared legitimately absent.** This is the first exercise of the "defensible or legitimately absent" clause of the admission gate.

## Deferred

- Citizen/Member (CAND-006) unification with Customer Management: awaits government reference models (gap G5)
- Analytics standalone re-test (N-003): awaits the enterprise-generality matrix

## State after this pass

- 29 first-order candidates, all named per the noun-anchor discipline, synonyms absorbed as aliases
- Overlay conflicts from v0.1 reduced: CAND-010 and CAND-019 resolved; CAND-008, CAND-017/018, CAND-028 remain open
- Next per CR §33: enterprise-generality matrix (item 6), then the §38 admission-gate evaluation
