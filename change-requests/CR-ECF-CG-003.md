# CR-ECF-CG-003: Business Capability Catalog Conformance

| Field | Value |
|-------|-------|
| **CR** | CR-ECF-CG-003 |
| **Title** | Business Capability Catalog Conformance |
| **Status** | Proposed |
| **Type** | Catalog Conformance |
| **Repository** | technehub-labs/dea-catalog-business-capabilities |
| **Implements** | CR-ECF-CG-001 |
| **Depends On** | CR-ECF-005, CR-ECF-CG-002 |
| **Author** | Coder (for eaojnr) |
| **Date** | 2026-09-01 |

## 1. Purpose

Verify that the Business Capability Catalog consumes ECF Coordinates as classification context without making ECF Coordinates the source of capability identity or capability enumeration.

The existing capability repository is already largely aligned, so this is a validation and correction CR, not a redesign.

## 2. Mandatory Principle

The catalog shall preserve:

Capability Identity
        ≠
ECF Coordinate

An ECF Coordinate contextualizes a capability.

It does not create the capability.

## 3. Prohibited Interpretation

The following shall not be implemented:

49 ECF Coordinates
       ↓
49 required capabilities

Nor:

one ECF Coordinate
       ↓
one capability

The catalog may contain zero, one, or many capabilities associated with an ECF context.

## 4. Coordinate Assignment

Each capability's ECF association shall be supported by semantic evidence.

A primary coordinate shall mean:

the governed principal contextual placement of the capability within the ECF.

It shall not be defined by ECF itself as an intrinsic "earliest lifecycle initiation" property.

If earliest initiation remains useful, it shall be documented as a catalog-specific classification heuristic.

## 5. Multiple Contexts

The catalog shall permit a capability to have multiple legitimate ECF contextual associations without creating multiple capability identities.

## 6. Boundary Validation

The catalog shall explicitly distinguish:

Capability
Function
Process
Activity
Task
Service
Resource

ECF coordinates shall not be used to collapse these concepts.

## 7. Evidence

Every canonical capability shall have:

Capability Definition
Identity
Outcome / Value Rationale
ECF Context
Evidence / Provenance

where applicable.

## 8. Acceptance Criteria

- [ ] Capability identity is independent of ECF Coordinate.
- [ ] No 49-cell population rule exists.
- [ ] Coordinate assignments are evidence-based.
- [ ] Multiple contextual coordinates are supported where justified.
- [ ] Primary-coordinate semantics are catalog-specific and documented.
- [ ] Capability/process/function boundaries remain explicit.
- [ ] Canonical ECF identifiers resolve to dea-metamodel.
- [ ] Catalog documentation conforms to CR-ECF-001..005.

## 9. Definition of Done (this proposal PR)

Two files: this CR (verbatim against the source tranche) and the change-requests index row. Implementation PR (the migration script + the 26 entry updates + the MCSP view update + the CI gate + the catalog README profile declaration) ships on subsequent acceptance.

## 10. References

CR-ECF-CG-001 (gate definition); CR-ECF-CG-002 (metamodel conformance); CR-DEA-BC-01 (catalog method, accepted); CR-DEA-BC-02 (evidence investigation, complete); CR-DEA-BC-04 (specialization framework, accepted).