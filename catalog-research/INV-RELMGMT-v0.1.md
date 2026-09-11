# Investigation Track C: Relationship Management (Generic Parent)

**Status**: Open (boundary-led investigation)
**Source**: [BC-SR-A001](../submittal-reviews/BC-SR-A001.md) §6 (reviewer P1-P2)
**Carrier CR**: [CR-DEA-BC-12](../change-requests/CR-DEA-BC-12.md) §B.3
**Machine-readable twin**: (to be added when evidence work begins)
**Date opened**: 2026-09-10

## Question to answer

Is there a **generic Relationship Management** first-order capability of which
Customer / Supplier / Partner Management are specializations? Or are the
role-specific capabilities already MECE-complete and the generic parent is
unnecessary abstraction?

This is the hardest of the three investigation tracks because the answer
might legitimately be **"no generic parent is warranted"**: and that is a
valid output. The investigation must produce the rationale either way.

## Hypothesis (from the reviewer)

> *The ability to establish, govern, develop, and terminate relationships with
> external parties across their lifecycle.*

**ECF placement hypothesis:** `party-relationship / conceive` (primary), with
`party-relationship / operate` and `party-relationship / improve` as
secondaries.

**Why this might be foundational (per BC-SR-A001 §6):**

The ECF Party & Relationship domain is MECE-complete for the external
environment: customer, supplier, partner, regulator, community. The catalog
organizes the domain around roles (Customer, Supplier, Partner). The ECF
organizes it around party/relationship as the underlying semantic subject.
These are not the same cut. The reviewer's question is which cut is
canonical for an enterprise-general foundation.

## Distinctness sweep: required against

- `dea:capability-customer-management` (customer relationship)
- `dea:capability-supplier-management` (supplier relationship; note: this
  track is independent of the §A.5 ECF re-mapping in CR-DEA-BC-12, which
  moves the coordinate but does not pre-judge this investigation)
- `dea:capability-partner-management` (peer relationships)
- `dea:capability-marketing` (customer acquisition, possibly adjacent)

## Boundary options to consider

1. **Generic parent admitted as first-order cap.** Customer / Supplier /
   Partner become its specializations. Most architecturally aligned with the
   ECF; biggest catalog surface change.
2. **Generic parent exists as abstract grouping only.** Specialization
   register entry, not a canonical cap. Preserves the catalog's
   first-order-concept discipline (no abstraction without durable
   business object). Smallest catalog surface change.
3. **No generic parent.** Role-specific caps are MECE-complete; rationale
   recorded and the investigation closed. No catalog change.

## ECF re-mapping pre-commitment

CR-DEA-BC-12 §A.5 (Supplier Management coordinate re-mapping from
`strategy-direction / build` to `party-relationship / conceive+operate`) lands
independently of this track. Track C may conclude that Supplier Management
should additionally become a specialization of a future Relationship
Management cap; that would be a follow-on migration CR, not part of this CR.

## Evidence required for admission (catalog's admission gate)

- Evidence rating E3 or higher.
- Enterprise-generality across at least 3 vertical industries.
- A **distinct business object** that survives the admission gate's
  "no abstraction without durable business object" rule (this is the
  load-bearing test for this track).
- Boundary defensible against each of the three role-specific caps.
- Distinctness demonstrated.

## Deliverables when the investigation reports back

1. One of three boundary options, decided with rationale.
2. If option 1: candidate record + full evidence package.
3. If option 2: specialization register entry; rationale for not admitting.
4. If option 3: durable rationale for no-admit; this file becomes the
   record.

If option 1 is taken and evidence supports it, a separate admission CR is
opened (provisional CR-DEA-BC-16).

## Progress log

- 2026-09-10: Investigation opened. No evidence work yet.
