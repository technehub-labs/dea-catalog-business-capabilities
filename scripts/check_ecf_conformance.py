"""ECF conformance gate: validate every catalog entry's ecfConformance block.

Validates, per CR-ECF-CG-003:
  1. block presence on every canonical entry;
  2. framework + contractVersion + profile + status fields;
  3. canonicalReferences resolve to canonical PascalCase Domain/Stage enums;
  4. identifier matches the canonical lowerCamelCase pattern
     (^ecf:[a-z][a-zA-Z0-9]*\\.[a-z][a-zA-Z0-9]*$);
  5. held-unmapped state is documented with rationaleRef N-006;
  6. MCSP view carries ecfConformance;
  7. extension items declare doesNotRedinef (no silent redefinition).

Exit code: 0 on full pass, 1 on any failure. Designed for GitHub Actions.
"""

from __future__ import annotations
import glob, os, re, sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
ENT = REPO / 'entities' / 'v1-alpha'
VIEW = REPO / 'mappings' / 'specializations' / 'view-telecom-mcsp.yaml'
CONTRACT_VERSION = '1.0.0'
PROFILE = 'dea:ecf@1.0.0'
FRAMEWORK = 'EnterpriseConceptFramework'
CANON_DOMAINS = {
    'GovernanceAndExistence', 'SupplyAndResources', 'PeopleAndOrganization',
    'CustomerAndDemand', 'ProductAndOffering', 'OperationsAndDelivery',
    'FinanceAndValue',
}
CANON_STAGES = {'Conceive', 'Design', 'Build', 'Activate', 'Operate', 'Improve', 'Retire'}
ID_PATTERN = re.compile(r'^ecf:[a-z][a-zA-Z0-9]*\.[a-z][a-zA-Z0-9]*$')
STATUSES = {'conformant', 'conformant-with-extension', 'non-conformant', 'not-yet-assessed'}


def check_entry(e: dict, fp: str, errors: list):
    cid = e.get('id') or fp
    blk = e.get('ecfConformance')
    if blk is None:
        errors.append(f"{cid}: missing ecfConformance block")
        return
    for k in ('framework', 'contractVersion', 'profile', 'status'):
        if k not in blk:
            errors.append(f"{cid}: ecfConformance missing field '{k}'")
    if blk.get('framework') != FRAMEWORK:
        errors.append(f"{cid}: framework '{blk.get('framework')}' != canonical '{FRAMEWORK}'")
    if blk.get('contractVersion') != CONTRACT_VERSION:
        errors.append(f"{cid}: contractVersion '{blk.get('contractVersion')}' != '{CONTRACT_VERSION}'")
    if blk.get('profile') != PROFILE:
        errors.append(f"{cid}: profile '{blk.get('profile')}' != '{PROFILE}'")
    if blk.get('status') not in STATUSES:
        errors.append(f"{cid}: status '{blk.get('status')}' not in {STATUSES}")

    aff = blk.get('affiliation')
    if aff == 'held-unmapped':
        if blk.get('rationaleRef') != 'N-006':
            errors.append(f"{cid}: held-unmapped missing rationaleRef=N-006")
        if blk.get('canonicalReferences'):
            errors.append(f"{cid}: held-unmapped must have empty canonicalReferences")
        return
    if aff != 'mapped':
        errors.append(f"{cid}: affiliation '{aff}' must be 'mapped' or 'held-unmapped'")

    for ref in blk.get('canonicalReferences') or []:
        if ref.get('kind') != 'coordinate':
            errors.append(f"{cid}: reference kind '{ref.get('kind')}' not 'coordinate'")
            continue
        d = ref.get('domain')
        s = ref.get('stage')
        if d not in CANON_DOMAINS:
            errors.append(f"{cid}: canonical reference domain '{d}' not in canonical enum")
        if s not in CANON_STAGES:
            errors.append(f"{cid}: canonical reference stage '{s}' not in canonical enum")
        ident = ref.get('identifier') or ''
        if not ID_PATTERN.match(ident):
            errors.append(f"{cid}: identifier '{ident}' does not match canonical pattern")

    for ext in blk.get('extensions') or []:
        if 'doesNotRedefine' not in ext:
            errors.append(f"{cid}: extension '{ext.get('name')}' missing doesNotRedefine")
        if ext.get('doesNotRedefine') is False:
            errors.append(f"{cid}: extension '{ext.get('name')}' doesNotRedefine=false is prohibited by CG-001")


def check_view(blk: dict, fp: str, errors: list):
    cid = f"view:{fp}"
    if blk is None:
        errors.append(f"{cid}: missing ecfConformance block")
        return
    for k in ('framework', 'contractVersion', 'profile', 'status', 'affiliation'):
        if k not in blk:
            errors.append(f"{cid}: ecfConformance missing field '{k}'")
    if blk.get('framework') != FRAMEWORK:
        errors.append(f"{cid}: framework '{blk.get('framework')}' != canonical '{FRAMEWORK}'")
    if blk.get('contractVersion') != CONTRACT_VERSION:
        errors.append(f"{cid}: contractVersion '{blk.get('contractVersion')}' != '{CONTRACT_VERSION}'")
    if blk.get('profile') != PROFILE:
        errors.append(f"{cid}: profile '{blk.get('profile')}' != '{PROFILE}'")
    if blk.get('status') not in STATUSES:
        errors.append(f"{cid}: status '{blk.get('status')}' not in {STATUSES}")


def main():
    files = sorted(glob.glob(str(ENT / 'capability-*.yaml')))
    errors: list[str] = []
    for fp in files:
        try:
            e = yaml.safe_load(open(fp))
        except yaml.YAMLError as ex:
            errors.append(f"{fp}: YAML parse error: {ex}")
            continue
        if not e:
            errors.append(f"{fp}: empty document")
            continue
        check_entry(e, fp, errors)
    if VIEW.exists():
        v = yaml.safe_load(open(VIEW))
        check_view(v.get('ecfConformance') if v else None, str(VIEW), errors)
    if errors:
        print(f"FAIL: {len(errors)} conformance error(s):", file=sys.stderr)
        for e in errors:
            print(' -', e, file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {len(files)} entries + MCSP view conform to ECF Conformance Gate.")


if __name__ == '__main__':
    main()