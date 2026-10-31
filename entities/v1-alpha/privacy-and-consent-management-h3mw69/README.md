# Privacy and Consent Management

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-privacy-and-consent-management-h3mw69` |
| Entity type | BusinessCapability |
| Version / status | 1.0.0 · active |
| Record | [capabilities-capability-privacy-and-consent-management-h3mw69.yaml](capabilities-capability-privacy-and-consent-management-h3mw69.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to govern personal-data processing and consent so privacy obligations are met across the information lifecycle.

**Capability-hood** (from the record's `why_capability`):

Object-demand evidence (SRC-026 cluster) plus the cross-catalog control pull: the PII information class mandates lawful-basis and data-subject-rights controls whose obligations need an owning capability; distinct from Regulation Management (external obligation intake) and Security Management (threat-based protection). Enterprise-generality level pending the next generality-matrix refresh (CR-DEA-BC-62 method).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

**Purpose** (from the record; populated at admission from the coverage-gap evidence base):

> The enterprise requires Privacy and Consent Management so personal data is processed on a lawful, consented basis across its lifecycle.

## 4. Scope and boundaries

**Boundary** (from the record):

> Governs personal-data processing and consent; does not manage security events (Security Management) or the information estate (Information Management).

**Non-examples** (from the record):

- A consent form (an artifact)
- A consent-management platform (a system)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | governance-existence / design |
| Secondary | governance-existence / operate |
| Secondary | party-relationship / operate |

**Rationale** (from the record's `ecf_rationale`):

> Mapped at admission under the CR-DEA-BC-13 semantic-center-of-gravity rule. The defining activity of Privacy and Consent Management is privacy-by-design shaping (design); consent operations (governance operate) and the party interface (party-relationship/operate) participate but do not define it. Cell occupancy: governance-existence/{design, operate}, party-relationship/operate (deepened).

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> Privacy regimes (GDPR, CCPA) are specialization; the privacy-governance ability is not.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Regulation Management](../regulation-management-gya4d8/capabilities-capability-regulation-management-gya4d8.yaml) | recorded in `related_capabilities` |
| [Information Management](../information-management-6vjgdh/capabilities-capability-information-management-6vjgdh.yaml) | recorded in `related_capabilities` |
| [Security Management](../security-management-wmzc7c/capabilities-capability-security-management-wmzc7c.yaml) | recorded in `related_capabilities` |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; `information` is now unblockable against `dea:information-asset-*` per the advancement programme). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Personal data is processed lawfully on a consented basis.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-023, SRC-026, SRC-027 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Business-object demand: 2 canonical objects in the cluster (consent-record, party-credential; SRC-026) reference no capability; the information-classes catalog binds PII to lawful-basis and data-subject-rights controls (dea-catalog-controls records) with no owning capability; cross-signal convergence recorded in the coverage-gap register (SRC-027); ability class corroborated against cross-industry process classification (SRC-023).
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-10-31 | Emmanuel A. Otchere, coverage-gap candidate register C-09 (CR-DEA-BC-62) |
| observed | 2026-10-31 | Emmanuel A. Otchere, business-object demand scan (SRC-026): 2 canonical objects in the cluster reference no capability |
| corroborated | 2026-10-31 | Emmanuel A. Otchere, cross-signal convergence in the coverage-gap register (SRC-027): ECF cell + object cluster + process-mirror signals agree |
| normalized | 2026-10-31 | Emmanuel A. Otchere, distinctness pass against neighbouring capabilities recorded in boundary |
| ecf-mapped | 2026-10-31 | Emmanuel A. Otchere, ECF overlay (governance-existence / design) |
| reviewed | 2026-10-31 | Emmanuel A. Otchere, admission review under the CR-DEA-BC-62 tranche method |
| canonical | 2026-10-31 | Emmanuel A. Otchere, admission PR (tranche T3) |

## 13. Lifecycle and change history

Current: `v1.0.0` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md); admitted under the coverage-gap tranche method (CR-DEA-BC-62)
