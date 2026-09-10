# Investigation Track B — Enterprise Performance Management

**Candidate id:** `dea:candidate-epm`
**Status:** candidate-not-canonical (non-admitted research artifact)
**Investigation track:** B
**Source:** [BC-SR-A001](../submittal-reviews/BC-SR-A001.md) §5 (reviewer P1)
**Carrier CR:** [CR-DEA-BC-13](../change-requests/CR-DEA-BC-13.md) §D.2
**Opened:** 2026-09-10

This subtree holds the **non-canonical candidate record** for Enterprise
Performance Management as a first-order business capability. The candidate is
being investigated under the catalog's admission gate (`METHODOLOGY.md §12`).

**What this is:** a research artifact, not a canonical catalog entry. The
candidate YAML under `candidates/epm.yaml` is excluded from canonical
enumeration by the catalog's regenerator.

**What this is not:** an admitted capability. Per CR-DEA-BC-12 §B.2, admission
remains gated on the catalog's own §12 review gates; admission, if any, lands in
a follow-on CR (provisional CR-DEA-BC-15).

**Distinctive feature of this track:** the candidate is being investigated not
only for boundary defensibility against existing caps but also for whether it
closes the **direction loop** identified in BC-SR-A001 §16 — Strategy →
Strategic Planning → Performance → Insight → Adaptation. The candidate record's
`evidence_requirement.loop_closure_narrative_required` flag is set, and the
investigation must report on the loop's status even if the candidate is not
admitted.

See `catalog-research/INV-EPM-v0.1.md` for the investigation's question,
hypothesis, evidence-required-for-admission, and deliverables.

**Files in this subtree:**

- `candidates/epm.yaml` — the candidate record (ECF overlay hypothesis,
  evidence requirement, distinctness sweep, open evidence questions).
