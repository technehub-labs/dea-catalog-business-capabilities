# Investigation Track B: Enterprise Performance Management

**Status**: Open (evidence-led investigation)
**Source**: [BC-SR-A001](../submittal-reviews/BC-SR-A001.md) §5 (reviewer P1)
**Carrier CR**: [CR-DEA-BC-12](../change-requests/CR-DEA-BC-12.md) §B.2
**Machine-readable twin**: (to be added when evidence work begins)
**Date opened**: 2026-09-10

## Question to answer

Is **Enterprise Performance Management** a distinct first-order capability,
or is it subsumed by Analytics & Intelligence? And does it close the
**Direction loop** that the reviewer identifies in BC-SR-A001 §16:

> Strategy → Strategic Planning → Performance Management → Analytics &
> Intelligence → Strategy Adaptation

: which is currently broken?

## Hypothesis (from the reviewer)

> *The ability to define, monitor, evaluate, and improve enterprise
> performance against intended objectives and targets.*

**ECF placement hypothesis:** `strategy-direction / operate` (primary), with
`strategy-direction / improve` and `finance-accounting / operate` as secondaries.

**Why this is foundational (per BC-SR-A001 §5):**

The catalog currently has Analytics & Intelligence, which is explicitly
*deriving decision-grade insight from information*. That is intelligence, not
performance management. The enterprise also needs an enduring ability to
define, measure, evaluate, govern, and adapt performance: which is the
Measure / Reassess half of the broader OpenDEAM cycle.

## Distinctness sweep: required against

- `dea:capability-analytics-and-intelligence` (insight from information)
- `dea:capability-financial-resource-management` (financial performance)
- `dea:capability-strategy` (strategic posture)
- `dea:capability-strategic-planning` (planning at strategic level)
- Any existing capability in the `strategy-direction` cells.

## Evidence required for admission (catalog's admission gate)

- Evidence rating E3 or higher.
- Enterprise-generality across at least 3 vertical industries.
- Boundary defensible against Analytics & Intelligence (the hardest question
  on this track; both work with measurement, but the objects differ).
- ECF mapping defensible.

## Deliverables when the investigation reports back

1. Candidate record: id, name, definition, business_object, outcome.
2. Evidence register entry (E0..E5 ratings).
3. ECF overlay hypothesis with rationale.
4. Distinctness sweep against the existing 26.
5. Admission-gate pre-check.
6. Explicit boundary statement against Analytics & Intelligence
   (`dea:capability-analytics-and-intelligence`).
7. **Loop-closure narrative:** how the candidate, if admitted, would close
   the direction loop from BC-SR-A001 §16. This is required even if the
   candidate is not admitted: it informs whether the loop is closed by
   other means or remains open.

If the evidence supports admission, a separate admission CR is opened
(provisional CR-DEA-BC-15).

## Progress log

- 2026-09-10: Investigation opened. No evidence work yet.
