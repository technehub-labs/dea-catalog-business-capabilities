# Investigation Track C: Relationship Management

**Candidate id:** `dea:candidate-relmgmt`
**Status:** candidate-not-canonical (non-admitted research artifact)
**Investigation track:** C
**Source:** [BC-SR-A001](../submittal-reviews/BC-SR-A001.md) §6 (reviewer P1-P2)
**Carrier CR:** [CR-DEA-BC-13](../change-requests/CR-DEA-BC-13.md) §D.3
**Opened:** 2026-09-10

This subtree holds the **non-canonical candidate record** for Relationship
Management as a **generic parent** capability, of which Customer / Supplier /
Partner Management may be specializations.

This track has **three decision options** to evaluate, and the investigation
must produce evidence for one of them:

1. **Admit Relationship Management as a first-order cap** with role-specific
   specializations. Surface change: 26 → 27 caps. Customer / Supplier / Partner
   become its specializations.
2. **Admit as abstract grouping only** (no canonical cap; the grouping lives in
   the specialization register as a non-canonical entry). Surface change: 26
   caps unchanged.
3. **Do not admit.** Role-specific caps are MECE-complete; rationale recorded
   as a durable no-admit decision. Surface change: 26 caps unchanged.

Per CR-DEA-BC-12 §B.3, the investigation must produce evidence for one of these
three options. **Option 3 is the simplest and is the catalog's current state.**

**What this is:** a research artifact, not a canonical catalog entry. The
candidate YAML under `candidates/relmgmt.yaml` is excluded from canonical
enumeration by the catalog's regenerator.

**What this is not:** an admitted capability. Per CR-DEA-BC-12 §B.3, admission
(if any) lands in a follow-on CR (provisional CR-DEA-BC-16).

See `catalog-research/INV-RELMGMT-v0.1.md` for the investigation's question,
hypothesis, evidence-required-for-admission, and deliverables.

**Files in this subtree:**

- `candidates/relmgmt.yaml`: the candidate record (ECF overlay hypothesis,
  evidence requirement, distinctness sweep, decision options, open evidence
  questions).
