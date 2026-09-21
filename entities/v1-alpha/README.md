# v1-alpha Catalog Entries

This directory contains the authoritative `v1-alpha` Business Capability catalog entries for the TechNeHub Labs Digital Enterprise Architecture (DEA) ecosystem.

Capabilities are stored in a **flat layout** under this directory (one subtree per record), per the org-wide entity-storage-layout spec ratified in `CR-DEA-BC-mv1` and the layout-agnostic docs (`dea-metaframework/docs/entity-storage-layout.md`, §3). Capabilities are single-level: each record is a `capability-<slug>-<hash>` subtree containing the record YAML. ECF coordinates (Domain, Stage) are record fields, not directory structure, since capabilities are not decomposition-hierarchical.

This README mirrors the structural template set in technehub-labs/dea-catalog-processes PR #153 (`dea-catalog-processes` entities-root README). The flat-layout sections below replace the containment-tree and ECF-matrix sections that are specific to ECF-coordinated catalogs.

---

## 📁 Directory Topology & Naming Conventions

```
v1-alpha/
├── capability-<slug>-<hash6>/                       # L1 capability subtree (populated)
│   └── capabilities-capability-<slug>-<hash6>.yaml
├── candidates-capability-<slug>-<hash6>/           # candidate subtree (not yet admitted)
│   └── capabilities-candidate-<slug>-<hash6>.yaml
├── capabilities-candidate-<slug>-<hash6>/          # candidate-only variant (when no L1 sibling)
│   └── capabilities-candidate-<slug>-<hash6>.yaml
└── README.md
```

Subdirectory names follow `<level>-<slug>-<hash6>`. The 6-character hash is content-derived (first 4 bytes of the record file's SHA-256, base-31 over the alphabet `a-z` minus `i`, `l`, `o` plus digits `2-9`). See `dea-metaframework/docs/id-system.md` §2.5.

---

## 📄 Entity Anatomy: Capabilities and Candidates

Per the DEA Metamodel, `dea:Capability` is an abstract kernel; concrete instances in this catalog are specialized to business capabilities (`dea:BusinessCapability`).

### Canonical id forms

| Level | id form |
| :--- | :--- |
| L1: Capability | `capabilities:capability-<slug>-<hash6>` |
| Candidate | `capabilities:candidate-<slug>-<hash6>` |

Each record file's id is content-addressed: changing the file's contents (without renaming the file) changes its hash. This is what makes the catalog content-addressed rather than directory-addressed.

### Canonical YAML Shape

```yaml
# id pattern: capabilities:capability-<slug>-<hash6>
id: capabilities:capability-customer-management-f3n8wb
name: Customer Management
definition: >
  The capability to manage the customer lifecycle: acquisition, onboarding,
  retention, win-back.
domain: PartyAndRelationship              # canonical ECF Domain (v2.4.x)
ecf_coordinate:
  domain: PartyAndRelationship
  layers:
    level: manage
related_capabilities:
  - capabilities:capability-customer-analytics-xxxxxx
```

ECF coordinates (Domain, Stage, Level) live in the record's `ecf_coordinate` field per the canonical ECF contract ratified through `CR-BP-ECF-08` and `CR-BP-ECF-09` (current enum: v2.4.x). Cross-catalog references use the org-wide id form.

---

## 📈 Population Snapshot

| Level | Count |
| :--- | ---: |
| L1 (Business Capability) | 31 |
| Candidates | 3 |
| **Total** | **34** *(31 capabilities + 3 candidates)* |

The L1 vs Candidate split is the canonical two-lane progression: an admission starts as a `candidate`, is ratified by CR, and migrates to a `capability` subtree on acceptance.

---

## 🛡 Governance & Conformance Gates

This catalog is protected by an automated CI pipeline with the following gates. All gates run on every PR via `.github/workflows/catalog-conformance.yml` (and adjacent workflows):

1. **`validate-entries`** (CI job)
   Validates every record file against `schemas/entity.schema.json` and the cell-charter contract.
   *Why it matters:* Catches malformed records and structural drift before they reach the catalog.

2. **ECF Conformance Consumer** (where applicable; `scripts/check_ecf_conformance.py`)
   Validates that `domain` and ECF coordinate references match the canonical ECF Domain Enum (current: v2.4.x).
   *Why it matters:* Prevents taxonomy drift across the seven catalog repositories.

3. **Catalog Conformance Suite** (CST, layout-agnostic, from `dea-metaframework/tools/conformance_test_catalog_structure.py`)
   Runs the 16-test CST suite that checks id-pattern conformance, content-derived hash correctness, and the flat-layout invariants.
   *Why it matters:* Enforces the org-wide id-system contract across all 7 catalog repositories.

4. **ID System Gate** (`scripts/check_id_system.py`)
   Runs IDM-001..007 (catalog-wide) plus IDM-008 (PR-scoped coherence via `id-system-coherence-report.md` artifact).
   *Why it matters:* Catches id drift between branches and the canonical baseline before merge.

5. **Register Audit Gate** (`scripts/check_register_audit.py`)
   Walks the catalog register and confirms every record's `audit_status: landed` vs `pending`.
   *Why it matters:* Keeps the catalog register honest as a single source of truth.

6. **CR Metadata Gate** (`scripts/check_cr_metadata.py --strict`)
   Verifies that any structural change, new admission, or migration is explicitly tied to an approved Change Request (CR) markdown file in `change-requests/`.
   *Why it matters:* Enforces the "no undocumented mutations" rule. Every change must have an auditable governance trail.

7. **`allocate / validate`** (CI job)
   Generates a per-record allocation matrix and validates it against the catalog register.
   *Why it matters:* Detects orphan or duplicated records that escape the schema-level checks.

---

## 🔄 Lifecycle, Reconciliation, and Baselines

This directory is the source of truth for the repository's reconciliation artifacts under `reconciliation/`:

* **`CATALOG.yaml`** (repo root): Automatically refreshed to reflect the current state of all entities in this tree. The CI gate runs `scripts/regenerate_catalog.py --check` and fails on any drift.
* **`reconciliation/inventory.yaml`**: Flat inventory of every entity, indexed by id.
* **`reconciliation/baseline/v1.yaml`**: Byte-identical, round-trip verifiable snapshot of the catalog at the last accepted baseline.
* **`reconciliation/conformance_report.yaml`**: Last CST run output.
* **`reconciliation/migration-id-map.yaml`**: Id map from the Wave 2 migration (legacy `dea:capability-*` to `capabilities:capability-...-hash`).
* **`reconciliation/cross-check-org-wide.md`**: Cross-check report for the most recent structural CR.

When modifying this directory, contributors must run the reconciliation build scripts to ensure the baseline remains consistent with the committed tree. CI enforces this.

---

## 🔗 Cross-Repo References

This catalog is one of seven in the DEA ecosystem. Records reference other catalogs using the org-wide id form `<namespace>:<level>-...-<hash6>`:

| Namespace | Catalog | Status |
| --- | --- | --- |
| `actors:` | `technehub-labs/dea-catalog-actors` | Wave 3 scaffold (empty, ready for first admissions) |
| `orgunits:` | `technehub-labs/dea-catalog-organizational-units` | Wave 3 scaffold |
| `objects:` | `technehub-labs/dea-catalog-business-objects` | Wave 3 scaffold |
| `stakeholders:` | `technehub-labs/dea-catalog-stakeholders` | Wave 3 scaffold |
| `capabilities:` | `technehub-labs/dea-catalog-business-capabilities` | This catalog (31 records) |
| `services:` | `technehub-labs/dea-catalog-business-services` | Populated (18 records, Wave 2b) |
| `processes:` | `technehub-labs/dea-catalog-business-processes` | Populated (3,598 records) |

This catalog has secondary references to the `dea:catalog-*` self-identity records, which remain in the legacy form on purpose.

---

## 🚀 Contributor Workflow

To add or modify a capability in this catalog:

1. **Identify the candidate.** If you have a new capability, start as a `candidate` subtree. If the candidate is already ratified, edit the `capability` subtree directly.
2. **File a Change Request (CR).** Create or reference an existing CR in `change-requests/` (e.g., `CR-DEA-BC-NN-<title>.md`).
3. **Create/Update the YAML.** Place the file at the correct flat-layout subtree. Compute the content-derived hash for the id. Use the org-wide id form for cross-catalog references.
4. **Run Local Conformance.** Execute `scripts/check_id_system.py --strict` and the CST suite locally. The CI pipeline runs the same gates on every PR.
5. **Regenerate Reconciliation Artifacts.** Run `scripts/regenerate_catalog.py --check --schema catalog-index-schema/catalog-index-schema.json`.
6. **Submit PR.** Link the PR to the CR. The CI pipeline enforces the gates described above.

For deeper metamodel definitions and the canonical id-system / entity-storage-layout specs, refer to:

* `technehub-labs/dea-metaframework` → `docs/id-system.md` (org-wide id contract)
* `technehub-labs/dea-metaframework` → `docs/entity-storage-layout.md` (§3 flat-layout-for-non-ECF)
* `technehub-labs/dea-metaframework` → `docs/conformance.md` (CST suite reference)
* `schemas/entity.schema.json` (record schema)
