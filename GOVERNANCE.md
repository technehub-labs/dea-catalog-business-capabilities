# Governance: Change Control, Roles, Acceptance

Catalog governance established by **CR-DEA-BC-01** (components 17 and 18). Normative for how this repository changes.

---

## 1. Change control

| Change | Requirement |
|---|---|
| Catalog method (this document set: METHODOLOGY, EVIDENCE, GOVERNANCE, TAXONOMY) | Change Request (`CR-DEA-BC-*`) |
| Canonical capability admission or removal | Evidence ladder + review per METHODOLOGY.md |
| Research artifacts (`docs/research/`) | PR per CR-DEA-BC-02 deliverable plan; versioned registers |
| `metamodel-pointer.yaml` | Regenerated from the OpenDEAM root model fan-out only; never hand-edited |
| ECF definition | Owned by `dea-metaframework`; this catalog references, never modifies |
| Record shape | Owned by `dea-metamodel` (ADR-015 lineage); reconciled here via CR (CR-DEA-BC-01A precedent) |
| Catalog version + change procedure | Owned by [`docs/VERSIONING.md`](docs/VERSIONING.md) (CR-DEA-BC-05); bump tier (major/minor/patch), three-tier consumer pin scheme, change procedure, tag format `v<N>-<word>.<P>`. The current posture (`v1-alpha.0`, 26 canonical entries) is recorded in `CHANGELOG.md` and `dependencies.yaml`. |

## 2. Change Request conventions

1. **Series tag.** `CR-DEA-BC` (DEA Business Capability). Numbers are sequential; renumbering is recorded on the CR itself (CR-DEA-BC-01A precedent).
2. **Land as authored.** An accepted CR ships verbatim to `change-requests/CR-DEA-BC-NN.md`, md5-verified against the reviewed source. No silent rewrites; status changes are recorded by later PRs, not by editing the landed CR.
3. **Proposal PR shape.** A CR proposal PR ships exactly: the CR document, the `change-requests/README.md` index row, and the README pointer. Nothing else.
4. **Sequential execution.** One CR (or CR phase) at a time; the next is parked until the current ships. Parked successors: CR-DEA-BC-03 (schema + CI), CR-DEA-BC-04 (industry specialization framework).
5. **One phase per PR.** Each phase ships a visible, checked-in deliverable; the PR body states deliverables, verification, and live URLs.

## 3. Roles

| Role | Responsibility |
|---|---|
| Catalog steward | Owns the method documents, the CR pipeline, and promotion decisions. Currently: eaojnr, with Coder as engineering agent. |
| Research compiler | Executes evidence gathering and candidate analysis under CR-DEA-BC-02; compiles registers with honest retrieval notes. |
| Semantic reviewer | Gate 1 (METHODOLOGY.md §12): definitions, distinctions, hard gates, anti-invention classification, naming conformance. |
| Architectural reviewer | Gate 2 (METHODOLOGY.md §12): ECF mapping, realization links, record shape, layering boundaries. |

One person may hold multiple roles; the gates and their recording are mandatory regardless.

## 4. Acceptance recording

1. Every lifecycle transition is recorded on the candidate's provenance trail (stage, date, actor, rationale).
2. Canonical admission is executed by a promotion PR that cites METHODOLOGY.md, the candidate's full evidence trail, and both review outcomes.
3. Post-merge CI must be green; the allocation validator (`validate-allocation.yml`) is the standing check.
4. A shipped CR closes with an objective scorecard: deliverables table, verification results, live URLs. No subjective summaries.

## 5. External authorities

| Authority | Owns | This catalog |
|---|---|---|
| `dea-architecture-framework` (OpenDEAM) | Layer and building-block allocation (L3-value-delivery) | Consumes via pinned model tag; pointer regenerates from fan-out |
| `dea-metamodel` | Entity and relationship structure; record shape; governed vocabularies | Consumes; reconciles via CR, never redefines |
| `dea-metaframework` | ECF 7×7 definition and recursion rule | References; never modifies |
| WSF | Foundational semantics (`wsf:Capability` lineage) | Aligns; does not assert |

## 6. Writing conventions

All shipped documents use Design Specification tone (declarative, no "we should"). No en or em dashes; colons and semicolons carry the load. These conventions are checked before every PR ships.

## 7. References

- Method: [`METHODOLOGY.md`](METHODOLOGY.md)
- CR index: [`change-requests/README.md`](change-requests/README.md)
- Foundations and decision register: [`docs/FOUNDATIONS.md`](docs/FOUNDATIONS.md)
- Versioning and change procedure: [`docs/VERSIONING.md`](docs/VERSIONING.md) (CR-DEA-BC-05)
- Version timeline: [`CHANGELOG.md`](CHANGELOG.md)
