# Technology Enablement

## 1. Identity

| Field | Value |
|---|---|
| Canonical ID | `capabilities:capability-technology-enablement-y6nkws` |
| Entity type | BusinessCapability |
| Version / status | 1.0.1 · active |
| Record | [capabilities-capability-technology-enablement-y6nkws.yaml](capabilities-capability-technology-enablement-y6nkws.yaml) — authoritative |
| Layer | support |

## 2. Definition and semantic interpretation

**Canonical definition** (from the record):

> The ability to run and continuously adapt the technology services, platforms, and automation that other capabilities depend on, sustaining operational technology delivery across the enterprise.

**Capability-hood** (from the record's `why_capability`):

E3 (foundation-grade per A+B+C gate). BC-SR-A001 §12 explicitly recommended this admission. CR-DEA-BC-13 §C carved out the Technology-as-Enabler sub-concern; this CR admits it as a first-order capability. Distinct business object (Technology Service vs Technology Estate) and distinct ECF cell (enablement-operations/operate vs strategy-direction/build) from Technology Management. Distinct from Operations (delivery of value vs delivery of technology for value delivery).

The interpretation above renders record content; scope distinctions from neighbouring capabilities are treated in §4.

## 3. Purpose and value contribution

Not yet established: `purpose` is unpopulated in the record. Per the population policy (CR-DEA-BC-43 M-1) it will be authored with evidence on substantive record change — never bulk-generated. The intended outcome the capability contributes to is recorded in §9.

## 4. Scope and boundaries

**Boundary** (from the record):

> Runs technology services, platforms, automation, and observability for the rest of the enterprise. DOES NOT build/acquire the technology estate (Technology Management: strategic posture and acquisition); DOES NOT derive insight from information (Insight Management); DOES NOT steward information lifecycles (Information Management); DOES NOT run business operations (Operations Management: value delivery), or design the IT organization structure (Organizational Design: IT org design is a sub-concern). The defining distinction: Technology Enablement is the IT delivery function; Technology Management is the IT direction function.

**Non-examples** (from the record):

- An IT department (an organization: the function may be performed by one)
- A specific platform (a system: the capability operates platforms but is not one)
- An SLO (an artifact: the outcome, not the capability)

## 5. Classification

| Coordinate | Domain × Stage |
|---|---|
| Primary (semantic center of gravity) | enablement-operations / operate |
| Secondary | enablement-operations / build |
| Secondary | enablement-operations / improve |

**Rationale** (from the record's `ecf_rationale`):

> Admitted 2026-09-10 under CR-DEA-BC-17. Under the new semantic-center-of-gravity rule (CR-DEA-BC-13 §A), the defining activity of Technology Enablement is sustained IT service and platform delivery (operate): running, monitoring, adapting technology services for the capabilities that depend on them. Secondary coordinates: build (provisioning new services as demand requires) and improve (SRE/platform engineering iteration). Distinct from Technology Management (strategy-direction/build): Technology Management stewards the estate (what technology the enterprise has); Technology Enablement runs the services (how that technology operates for others). The ECF places technology as enablers of execution (BC-SR-A001 §15 quote: 'Technology, platforms, and physical infrastructure are positioned as enablers of execution'), which is exactly the enablement-operations domain and the operate stage.

Coordinates are classification context, never capability identity.

## 6. Composition and specialization

No parent or child capabilities in the first-order set (flat by design; depth comes by ECF recursion, not a subdivision tree).

- Specialization allowed: True (none recorded yet)

**Specialization boundary** (from the record):

> IT service management (incident, problem, change), platform engineering (internal developer platforms, paved roads), site reliability engineering (SLOs, error budgets, on-call), automation engineering (RPA, workflow automation, agentic automation), and data platform engineering are specializations of this capability. The ability to run technology services is NOT a specialization of any other capability.

A specialization refines scope or context; it never redefines the parent capability.

## 7. Related entities and relationships

| Related capability | Basis |
|---|---|
| [Technology Management](../technology-management-maus5n/capabilities-capability-technology-management-maus5n.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Operations Management](../operations-management-pm3w8k/capabilities-capability-operations-management-pm3w8k.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Information Management](../information-management-6vjgdh/capabilities-capability-information-management-6vjgdh.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Insight Management](../insight-management-ms4n9d/capabilities-capability-insight-management-ms4n9d.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |
| [Organizational Design](../organizational-design-vanefq/capabilities-capability-organizational-design-vanefq.yaml) | recorded in `related_capabilities`; see the boundary in §4 of both records |

Typed relationship assertions (CR-DEA-BC-53: depends-on / realizes / specializes, with rationale) are representable in the canonical data; the associations listed above remain untyped pending evidence-led typing.

## 8. Realization and operational context

Not yet established: the record's `realization` block is unpopulated. Realization links will carry canonical sibling-catalog ids (the `processes` scheme `processes:*` is confirmed; others await U-2). The capability itself is implementation-independent by definition (§2).

## 9. Outcomes and traceability

**Intended outcome** (from the record; contribution, not guarantee):

> Technology services and platforms are reliable, available, performant, and adapted to changing demand from the capabilities that depend on them.

## 10. Assessment considerations

Not applicable — no assessment authority or model is established for this catalog; assessment results never form part of capability identity (BC-DOC-008).

## 11. Governance

- Change control: [GOVERNANCE.md](../../../GOVERNANCE.md) — changes land via CR (`CR-DEA-BC-*`)
- Method: [METHODOLOGY.md](../../../METHODOLOGY.md) · Evidence: [EVIDENCE.md](../../../EVIDENCE.md) · Naming: [TAXONOMY.md](../../../TAXONOMY.md)

## 12. Provenance and evidence

- **Admission evidence:** SRC-005, SRC-006 (register: [`catalog-research/evidence-register.yaml`](../../../catalog-research/evidence-register.yaml))
- **Evidence rationale:** Admission per CR-DEA-BC-17. The 'Technology-as-Enabler' sub-concern carved out by CR-DEA-BC-13 §C is here promoted to a first-order canonical capability. Evidence trail: BC-SR-A001 §12 (reviewer's recommendation to formalize the Tech-as-Estate vs Tech-as-Enabler carve); CR-DEA-BC-13 §C (carve-text-only deferral); CR-DEA-BC-17 §3 (full evidence package for admission). Enterprise-generality demonstrated at E3 (cross-industry IT service delivery function is universal across B2B/B2C/G2C enterprises per foundation inclusion criteria gate A+B+C); evidence trail in catalog-research/{evidence-register, enterprise-generality-matrix, distinctness-sweep}.
- **Ladder passage** (from the record's `provenance`):

| Stage | Date | Actor |
|---|---|---|
| candidate | 2026-09-10 | Emmanuel A. Otchere, BC-17 candidate record derived from BC-13 carve |
| observed | 2026-09-10 | Emmanuel A. Otchere, BC-SR-A001 §12 + carve-text evidence |
| corroborated | 2026-09-10 | Emmanuel A. Otchere, enterprise-generality matrix (B2B/B2C/G2C sweep) |
| normalized | 2026-09-10 | Emmanuel A. Otchere, distinctness sweep vs Operations / Tech Mgmt / IM / A&I |
| ecf-mapped | 2026-09-10 | Emmanuel A. Otchere, ECF overlay hypothesis: enablement-operations/operate (primary) |
| reviewed | 2026-09-10 | Emmanuel A. Otchere, CR-DEA-BC-17 §3 (semantic review) + §4 (architectural review) |
| canonical | 2026-09-10 | eaojnr, admission PR (this change) |

## 13. Lifecycle and change history

Current: `v1.0.1` · `active`. Entity content changes land via CR and are cited in the repository record of change requests; the ladder above records the admission history.

## 14. Conformance

- Schema: `schemas/entity.schema.json` (validated in CI; CR-DEA-BC-40/43 model)
- ECF: conformant-with-extension under `dea:ecf@1.0.0`
- Id-system / entity-system / naming / doc-links / CR-index gates: enforced in CI
- This README: rendered from the canonical record per the [README Standard](../../../docs/BUSINESS-CAPABILITY-README-STANDARD.md) (CR-DEA-BC-46 remediation); open items: none known at landing

