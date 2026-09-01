# Evidence: Methodology, Source Stances, Provenance

The evidence methodology established by **CR-DEA-BC-01** (component 4, 13, 15) and executed by **CR-DEA-BC-02**. Normative for how capability evidence is gathered, rated, and recorded. Admission decisions cite this document.

---

## 1. Principle: research, not copy

Established bodies of knowledge are **evidence sources, never templates**. Capabilities are inferred from recurring enterprise work; they are not transcribed from any framework. No single framework is the semantic authority.

The distinction in practice: a source can prove that an ability recurs across enterprises; it cannot prove that its own naming, grouping, or decomposition is the right one for this catalog. Names are decided by TAXONOMY.md; groupings by the admission method in METHODOLOGY.md.

## 2. Source classes and stances

Sources are registered in the evidence register (`docs/research/evidence-register.yaml`) under these classes:

| Class | Examples | Stance |
|---|---|---|
| business-architecture | Business Architecture Guild / BIZBOK | Strong semantic corroboration for capability identity and value-stream grounding. Names never copied. |
| enterprise-architecture | The Open Group / TOGAF capability guidance | Corroborates capability-based planning practice and decomposition with business-object focus. |
| cross-industry-process | APQC PCF (cross-industry) | Explicitly a process taxonomy, not a capability model. Evidences recurring enterprise work from which capabilities are inferred. |
| industry-specific | APQC industry variants; sector frameworks | Evidences specialization boundaries, never first-order membership. |
| government-guidance | Public-sector architecture and capability guidance | Corroborates enterprise-generality beyond commercial models. |
| commercial-capability-models | Vendor and practitioner capability maps | Evidences market recurrence; treated with naming-discipline caution. |
| internal-baseline | OTCHERE Inc and adopting-enterprise structures | Reality check for the anti-invention test; never sufficient alone. |

## 3. Evidence ratings

Candidates carry an ordinal evidence rating, E0 to E5, reflecting depth of independent corroboration:

| Rating | Meaning |
|---|---|
| E5 | Independent convergence across multiple source classes and enterprise contexts; highest confidence. |
| E4 | Corroborated across multiple independent sources. |
| E3 | Appears in credible material with partial independence. |
| E2 | Lower frequency; held as candidate pending cross-industry check. |
| E1 | Single-source mention. |
| E0 | Disambiguation only: cited to record that a source listed the term as a capability; no capability status asserted. |

Ratings inform prioritization; they do not substitute for the admission tests. A high rating does not admit; a low rating does not reject. Admission is decided by METHODOLOGY.md Sections 4 to 6.

## 4. Cross-industry evidence strategy

Evidence gathering deliberately spans materially different enterprise types:

commercial, non-profit, government, professional services, manufacturing, retail, financial services, healthcare, technology, infrastructure.

The question asked of each: **what abilities recur despite radically different business models?**

- Cross-industry material evidences the first-order baseline.
- Industry-specific material evidences specialization boundaries (what a Mobile Communications Service Provider view may refine, for example).
- The enterprise-generality matrix (`docs/research/enterprise-generality-matrix.yaml`) operationalizes this check per candidate.

## 5. Provenance rules

1. Every candidate and every canonical entry carries its evidence trail: sources (`SRC-NNN`), ladder stage transitions, and rationale.
2. Retrieval honesty is mandatory: indirect retrieval (quoted definitions, membership-gated primaries) is recorded as such on the source entry.
3. Rejected and deferred candidates are retained with rationale. They are evidence of the boundary, and they prevent re-litigating settled questions.
4. Normalization decisions (`N-NNN`) record the question, the candidates, the evidence, and the analysis. No merge occurs solely because names are similar.
5. Research artifacts are dual-delivery: a machine-readable YAML register and a persona-readable Markdown summary, versioned together (`register_version` / document version).

## 6. Artifact conventions

| Convention | Rule |
|---|---|
| Source IDs | `SRC-NNN`, assigned in the evidence register, never reused. |
| Candidate IDs | `CAND-NNN`, assigned in the candidate universe, never reused (dissolved candidates keep their ID with disposition recorded). |
| Normalization decision IDs | `N-NNN`, sequential in the normalization register. |
| Versioning | Registers carry `register_version`; each revision notes what changed and why in the header. |
| Status vocabulary | Research artifacts are `draft-for-review` or `candidate-not-canonical` until the method gates their promotion. Nothing is canonical by virtue of existing in `docs/research/`. |

## 7. References

- Method: [`METHODOLOGY.md`](METHODOLOGY.md)
- Live evidence register: `docs/research/evidence-register.yaml` (+ `EVIDENCE-REGISTER-v0.1.md`)
- Live candidate universe: `docs/research/candidates.yaml` (+ `CANDIDATE-UNIVERSE-v0.1.md`)
- Normalization register: `docs/research/normalization.yaml` (+ `NORMALIZATION-v0.1.md`)
- Enterprise-generality matrix: `docs/research/enterprise-generality-matrix.yaml` (+ `GENERALITY-MATRIX-v0.1.md`)
- Distinctness sweep: `docs/research/distinctness-sweep.yaml` (+ `DISTINCTNESS-SWEEP-v0.1.md`)
