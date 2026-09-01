"""ECF conformance migration: add ecfConformance block to all canonical entries + the MCSP view.

Deterministic, idempotent. Reads the catalog-kebab classification vocabulary (the
catalog's own ecf block) and emits an ecfConformance manifest that references the
canonical PascalCase ECF enums from dea-metaframework.

Run from repo root: python3 scripts/migrate_ecf_conformance.py [--apply]

Without --apply: dry-run. Prints a summary and a JSON diff for the first changed
entry; bails before writing.

The script will never overwrite an existing ecfConformance block (idempotent).
To regenerate, set REGEN=1 in the env (intentional operator override).
"""

from __future__ import annotations
import os, sys, glob, json, yaml
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENT = REPO / 'entities' / 'v1-alpha'
VIEW = REPO / 'mappings' / 'specializations' / 'view-telecom-mcsp.yaml'
REGEN = os.environ.get('REGEN') == '1'
APPLY = '--apply' in sys.argv

# Canonical mapping: catalog kebab (display) -> canonical PascalCase (ECF enum)
# AND lowerCamelCase identifier suffix used in canonical ECF identifiers
# (matches dea-metaframework/schemas/ecf-coordinate.schema.json identifier pattern
#  '^ecf:[a-z][a-zA-Z0-9]*\.[a-z][a-zA-Z0-9]*$').
DOMAIN_MAP = {
    'governance-existence': 'GovernanceAndExistence',
    'supply-resources': 'SupplyAndResources',
    'people-organization': 'PeopleAndOrganization',
    'customer-demand': 'CustomerAndDemand',
    'product-offering': 'ProductAndOffering',
    'operations-delivery': 'OperationsAndDelivery',
    'finance-value': 'FinanceAndValue',
}
DOMAIN_ID = {
    'governance-existence': 'governanceExistence',
    'supply-resources': 'supplyResources',
    'people-organization': 'peopleOrganization',
    'customer-demand': 'customerDemand',
    'product-offering': 'productOffering',
    'operations-delivery': 'operationsDelivery',
    'finance-value': 'financeValue',
}
STAGE_MAP = {
    'conceive': 'Conceive',
    'design': 'Design',
    'build': 'Build',
    'activate': 'Activate',
    'operate': 'Operate',
    'improve': 'Improve',
    'retire': 'Retire',
}
STAGE_ID = {
    'conceive': 'conceive',
    'design': 'design',
    'build': 'build',
    'activate': 'activate',
    'operate': 'operate',
    'improve': 'improve',
    'retire': 'retire',
}
CONTRACT_VERSION = '1.0.0'  # CR-ECF-001..005 series; CG-001..CG-006 conformance gate
PROFILE = 'dea:ecf@1.0.0'
FRAMEWORK = 'EnterpriseConceptFramework'
CANON_DOMAIN_REF = 'https://github.com/technehub-labs/dea-metaframework/schemas/ecf-domain.schema.json'
CANON_STAGE_REF = 'https://github.com/technehub-labs/dea-metaframework/schemas/ecf-stage.schema.json'
CANON_COORD_REF = 'https://github.com/technehub-labs/dea-metaframework/schemas/ecf-coordinate.schema.json'


def build_entry_conformance(entry: dict) -> dict:
    """Build the ecfConformance block from an entry's existing ecf classification."""
    ecf = entry.get('ecf') or {}
    if not ecf or ecf.get('primary') is None:
        # held_unmapped: legitimate absence of ECF affiliation (N-006 for CAND-019).
        return {
            'framework': FRAMEWORK,
            'contractVersion': CONTRACT_VERSION,
            'profile': PROFILE,
            'status': 'conformant-with-extension',
            'affiliation': 'held-unmapped',
            'rationaleRef': 'N-006',
            'canonicalReferences': [],
            'extensions': [
                {
                    'name': 'held-unmapped',
                    'kind': 'classification-state',
                    'description': (
                        'Capability legitimately carries no ECF Coordinate; the '
                        'catalog-specific held-unmapped state is documented in '
                        'METHODOLOGY.md and REVIEW-LOG (N-006).'
                    ),
                    'doesNotRedefine': True,
                },
                {
                    'name': 'kebab-case-domain-vocabulary',
                    'kind': 'display-vocabulary',
                    'description': (
                        'Catalog-side kebab-case labels for the seven ECF Domains '
                        '(see mapping). Display-only; resolves to canonical '
                        'PascalCase enums for the gate.'
                    ),
                    'doesNotRedefine': True,
                    'mapping': DOMAIN_MAP,
                },
            ],
        }

    primary = ecf.get('primary') or {}
    secondary = ecf.get('secondary') or []

    # Resolve primary coordinate to canonical PascalCase values.
    d_cat = primary.get('domain')
    s_cat = primary.get('stage')
    d_canon = DOMAIN_MAP.get(d_cat)
    s_canon = STAGE_MAP.get(s_cat)
    if not d_canon or not s_canon:
        raise ValueError(f"unknown kebab in primary: domain={d_cat} stage={s_cat} (entry {entry.get('id')})")

    canon_refs = [
        {
            'kind': 'coordinate',
            'domain': d_canon,
            'stage': s_canon,
            'identifier': f"ecf:{DOMAIN_ID[d_cat]}.{STAGE_ID[s_cat]}",
            'schema': CANON_COORD_REF,
            'role': 'primary',
        }
    ]
    for sec in secondary:
        ds_cat = sec.get('domain'); ss_cat = sec.get('stage')
        ds_canon = DOMAIN_MAP.get(ds_cat); ss_canon = STAGE_MAP.get(ss_cat)
        if not ds_canon or not ss_canon:
            raise ValueError(f"unknown kebab in secondary: domain={ds_cat} stage={ss_cat} (entry {entry.get('id')})")
        canon_refs.append({
            'kind': 'coordinate',
            'domain': ds_canon,
            'stage': ss_canon,
            'identifier': f"ecf:{DOMAIN_ID[ds_cat]}.{STAGE_ID[ss_cat]}",
            'schema': CANON_COORD_REF,
            'role': 'secondary',
        })

    return {
        'framework': FRAMEWORK,
        'contractVersion': CONTRACT_VERSION,
        'profile': PROFILE,
        'status': 'conformant-with-extension',
        'affiliation': 'mapped',
        'canonicalReferences': canon_refs,
        'extensions': [
            {
                'name': 'kebab-case-domain-vocabulary',
                'kind': 'display-vocabulary',
                'description': (
                    'Catalog-side kebab-case labels for the seven ECF Domains '
                    'and seven ECF Stages (see mapping). Display-only; resolves '
                    'to canonical PascalCase enums for the gate.'
                ),
                'doesNotRedefine': True,
                'mapping': {**DOMAIN_MAP, **{f'_stage_{k}': v for k, v in STAGE_MAP.items()}},
            },
            {
                'name': 'multiple-contextual-coordinates',
                'kind': 'catalog-specific-relation',
                'description': (
                    'A capability may have one primary and zero-or-more '
                    'secondary canonical coordinates without identity duplication '
                    '(CG-003 §5).'
                ),
                'doesNotRedefine': True,
            },
            {
                'name': 'held-unmapped',
                'kind': 'classification-state',
                'description': (
                    'State for capabilities with no ECF affiliation by design '
                    '(N-006); does not appear on this entry because primary is set.'
                ),
                'doesNotRedefine': True,
            },
        ],
    }


def build_view_conformance(view: dict) -> dict:
    """Build the ecfConformance block for the MCSP view."""
    return {
        'framework': FRAMEWORK,
        'contractVersion': CONTRACT_VERSION,
        'profile': PROFILE,
        'status': 'conformant-with-extension',
        'affiliation': 'inherits-catalog',
        'canonicalReferences': [
            {
                'kind': 'baseline-catalog',
                'baselineVersion': view.get('catalog_baseline'),
                'schema': CANON_COORD_REF,
                'role': 'inherited-baseline',
            }
        ],
        'extensions': [
            {
                'name': 'sector-context',
                'kind': 'view-specific-relation',
                'description': (
                    'The view carries sector context (Telecommunications mobile '
                    'services) on top of the catalog baseline. Sector context is '
                    'not a substitute for canonical ECF references; the '
                    'underlying entries retain their canonical affiliations.'
                ),
                'doesNotRedefine': True,
            },
        ],
    }


def main():
    files = sorted(glob.glob(str(ENT / 'capability-*.yaml')))
    n_changed = 0
    n_skipped = 0
    n_held = 0
    diffs = []
    for fp in files:
        with open(fp) as f:
            e = yaml.safe_load(f)
        if not e:
            print(f"  skip (empty): {fp}")
            n_skipped += 1
            continue
        if 'ecfConformance' in e and not REGEN:
            n_skipped += 1
            continue
        new_block = build_entry_conformance(e)
        # capture pre-state for first diff
        if len(diffs) == 0:
            diffs.append({'file': fp, 'id': e.get('id'), 'before': dict(e), 'after_block': new_block})
        if e.get('ecf') is None or e.get('ecf', {}).get('primary') is None:
            n_held += 1
        e['ecfConformance'] = new_block
        if APPLY:
            with open(fp, 'w') as f:
                yaml.safe_dump(e, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
            n_changed += 1

    # MCSP view
    if VIEW.exists():
        with open(VIEW) as f:
            v = yaml.safe_load(f)
        if 'ecfConformance' not in v or REGEN:
            v['ecfConformance'] = build_view_conformance(v)
            if APPLY:
                with open(VIEW, 'w') as f:
                    yaml.safe_dump(v, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
                n_changed += 1

    print(f"entries seen: {len(files)} | changed: {n_changed} | skipped (already conformant): {n_skipped} | held-unmapped: {n_held}")
    if not APPLY:
        print("(dry-run; pass --apply to write)")
        if diffs:
            print("\nfirst diff sample (file=" + diffs[0]['file'] + "):")
            print("  before ecfConformance: <absent>")
            print("  after ecfConformance:  (see structured output above)")


if __name__ == '__main__':
    main()