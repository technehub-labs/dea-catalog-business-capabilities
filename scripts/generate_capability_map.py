#!/usr/bin/env python3
"""
OpenDEAM Nested Entity x ECF Map Generator (release-pipeline edition)
=====================================================================
Builds an L0 ⊃ L1 ⊃ L2 CSS-Grid HTML poster from live catalog YAML and
ECF axis definitions.

This copy lives in the catalog repo and is wired into
`.github/workflows/publish-versioned.yml`: on every versioned tag push it
renders `capability-map.html` into `out/<label>/`, where `publish.js`
picks it up into the release zip. A companion renderer
(`scripts/render_map_png.mjs`) rasterises the HTML to an A3 PNG.

Defaults are CI-oriented: the catalog source is the local repo checkout
and the ECF axis is read from the local `schemas/entity.schema.json`
enums (canonical domain/stage set). Git/URL sources remain available for
standalone use.

Usage
-----
  # In-repo / CI (local checkout, local schema axis):
  python3 scripts/generate_capability_map.py --label v1-alpha.3 \\
      -o out/v1-alpha.3/capability-map.html

  # Standalone, from git remotes:
  python3 scripts/generate_capability_map.py \\
      --catalog-url https://github.com/technehub-labs/dea-catalog-business-capabilities.git \\
      --catalog-ref main \\
      --ecf-url https://github.com/technehub-labs/dea-metaframework.git \\
      --ecf-ref main

  python3 scripts/generate_capability_map.py \\
      --local-catalog /path/to/catalog-repo \\
      --local-ecf /path/to/dea-metaframework

  python3 scripts/generate_capability_map.py \\
      --ecf-domains-url https://raw.githubusercontent.com/.../ecf-domain.schema.json \\
      --ecf-stages-url  https://raw.githubusercontent.com/.../ecf-stage.schema.json

  python3 scripts/generate_capability_map.py \\
      --entity-urls https://raw.../a.yaml,https://raw.../b.yaml

Layout
------
  Top-left  H1: OpenDEAM
  Center    H2: <Catalog title>
  Center    fine type: version · count · date · refs
  Bottom-left:  legend
  Bottom-right: attribution
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG_GIT = "https://github.com/technehub-labs/dea-catalog-business-capabilities.git"
DEFAULT_ECF_GIT = "https://github.com/technehub-labs/dea-metaframework.git"
DEFAULT_REF = "main"
USER_AGENT = "OpenDEAM-Map-Generator/2.0"

# Canonical display order, mirroring scripts/lib/grid.js (DOMAINS). The
# entity.schema.json enum is a set; the matrix row order is governed here
# and in grid.js, and the two must stay in lockstep.
CANONICAL_DOMAIN_ORDER = [
    "governance-existence",
    "party-relationship",
    "strategy-direction",
    "product-value",
    "enablement-operations",
    "finance-accounting",
    "agency-organization",
]
CANONICAL_STAGE_ORDER = [
    "conceive", "design", "build", "activate", "operate", "improve", "retire",
]

FALLBACK_DOMAINS = [
    ("governance-existence", "Governance\n& Existence"),
    ("party-relationship", "Party &\nRelationship"),
    ("strategy-direction", "Strategy\n& Direction"),
    ("product-value", "Product\n& Value"),
    ("enablement-operations", "Enablement\n& Operations"),
    ("finance-accounting", "Finance &\nAccounting"),
    ("agency-organization", "Agency &\nOrganization"),
]
FALLBACK_STAGES = [
    ("conceive", "Conceive"),
    ("design", "Design"),
    ("build", "Build"),
    ("activate", "Activate"),
    ("operate", "Operate"),
    ("improve", "Improve"),
    ("retire", "Retire"),
]
STAGE_LABEL_FIX = {k: v for k, v in FALLBACK_STAGES}
LAYER_FIELDS = ("capability_layer", "process_layer", "entity_layer", "layer")


def http_get(url: str, timeout: int = 90) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def git_clone_or_update(url: str, ref: str, dest: Path) -> Path:
    dest = dest.resolve()
    if dest.exists() and (dest / ".git").is_dir():
        print(f"  updating {dest.name} @ {ref} …")
        subprocess.run(
            ["git", "-C", str(dest), "fetch", "--depth", "1", "origin", ref],
            check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(dest), "checkout", "-f", "FETCH_HEAD"],
            check=True, capture_output=True,
        )
    else:
        if dest.exists():
            shutil.rmtree(dest)
        print(f"  cloning {url} @ {ref} …")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", ref, url, str(dest)],
            check=True, capture_output=True,
        )
    return dest


def load_yaml_or_json_bytes(data: bytes) -> Any:
    text = data.decode("utf-8")
    if text.lstrip().startswith("{"):
        return json.loads(text)
    return yaml.safe_load(text)


def load_url(url: str) -> Any:
    print(f"  GET {url}")
    return load_yaml_or_json_bytes(http_get(url))


def to_kebab(s: str) -> str:
    s = s.strip()
    if "-" in s and s == s.lower():
        return s
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", s)
    return s.replace("_", "-").replace(" ", "-").lower()


def display_from_kebab(kebab: str) -> str:
    # Prefer "Governance & Existence" over "Governance And Existence"
    k = kebab.replace("-and-", "-")
    parts = [p.title() for p in k.split("-")]
    if len(parts) == 2:
        return f"{parts[0]}\n& {parts[1]}"
    if len(parts) > 2:
        mid = len(parts) // 2
        return " ".join(parts[:mid]) + "\n& " + " ".join(parts[mid:])
    return kebab.replace("-", " ").title()


def parse_enum_list(doc: Any) -> list[str]:
    if isinstance(doc, list):
        return [str(x) for x in doc]
    if isinstance(doc, dict):
        if "enum" in doc and isinstance(doc["enum"], list):
            return [str(x) for x in doc["enum"]]
        if "items" in doc and isinstance(doc["items"], dict) and "enum" in doc["items"]:
            return [str(x) for x in doc["items"]["enum"]]
        for key in ("domains", "stages", "values", "items"):
            if key in doc and isinstance(doc[key], list):
                out = []
                for x in doc[key]:
                    if isinstance(x, dict):
                        out.append(str(x.get("id") or x.get("name") or x))
                    else:
                        out.append(str(x))
                return out
    raise ValueError(f"Cannot parse enum list from {type(doc)}")


def load_ecf_axis_from_schemas(domains_doc: Any, stages_doc: Any):
    raw_d = parse_enum_list(domains_doc)
    raw_s = parse_enum_list(stages_doc)
    domains = [(to_kebab(d), display_from_kebab(to_kebab(d))) for d in raw_d]
    stages = [(to_kebab(s), STAGE_LABEL_FIX.get(to_kebab(s), to_kebab(s).title())) for s in raw_s]
    return domains, stages


def _find_ecf_enums(node: Any) -> tuple[list[str] | None, list[str] | None]:
    """Locate the ecf_coordinate domain/stage enums anywhere in a schema tree."""
    found: dict[str, list[str] | None] = {"domain": None, "stage": None}

    def walk(n: Any) -> None:
        if isinstance(n, dict):
            props = n.get("properties")
            if isinstance(props, dict):
                for axis in ("domain", "stage"):
                    sub = props.get(axis)
                    if isinstance(sub, dict) and isinstance(sub.get("enum"), list):
                        found[axis] = [str(x) for x in sub["enum"]]
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)

    walk(node)
    return found["domain"], found["stage"]


def load_ecf_axis_from_entity_schema(schema_path: Path):
    """Read the ECF axis from the catalog's own entity.schema.json enums.

    The schema enums are unordered sets, so rows/columns are re-ordered to
    the canonical matrix order (CANONICAL_DOMAIN_ORDER / CANONICAL_STAGE_ORDER,
    mirroring scripts/lib/grid.js). Any enum value not in the canonical
    order is appended in enum order so a future domain/stage addition still
    renders instead of being silently dropped.
    """
    doc = json.loads(schema_path.read_text(encoding="utf-8"))
    raw_d, raw_s = _find_ecf_enums(doc)
    if not raw_d or not raw_s:
        raise ValueError(f"No ecf_coordinate domain/stage enums in {schema_path}")
    kd = [to_kebab(d) for d in raw_d]
    ks = [to_kebab(s) for s in raw_s]

    def ordered(keys: list[str], canon: list[str]) -> list[str]:
        out = [k for k in canon if k in keys]
        out += [k for k in keys if k not in canon]
        return out

    domains = [(d, display_from_kebab(d)) for d in ordered(kd, CANONICAL_DOMAIN_ORDER)]
    stages = [(s, STAGE_LABEL_FIX.get(s, s.title())) for s in ordered(ks, CANONICAL_STAGE_ORDER)]
    return domains, stages


def load_ecf_from_git(repo: Path):
    ds = repo / "schemas" / "ecf-domain.schema.json"
    ss = repo / "schemas" / "ecf-stage.schema.json"
    if not ds.is_file() or not ss.is_file():
        raise FileNotFoundError(f"ECF schemas missing under {repo}/schemas/")
    return load_ecf_axis_from_schemas(
        json.loads(ds.read_text(encoding="utf-8")),
        json.loads(ss.read_text(encoding="utf-8")),
    )


def resolve_ecf_axis(args, cache: Path, catalog_root: Path | None):
    if args.ecf_domains_url and args.ecf_stages_url:
        ddoc = load_url(args.ecf_domains_url)
        sdoc = load_url(args.ecf_stages_url)
        domains, stages = load_ecf_axis_from_schemas(ddoc, sdoc)
        return domains, stages, f"domains+stages URLs"
    if args.local_ecf:
        domains, stages = load_ecf_from_git(Path(args.local_ecf))
        return domains, stages, str(Path(args.local_ecf).resolve())
    # CI default: the catalog's own entity schema is the axis source of truth.
    if catalog_root:
        schema = catalog_root / "schemas" / "entity.schema.json"
        if schema.is_file():
            domains, stages = load_ecf_axis_from_entity_schema(schema)
            return domains, stages, f"{schema}"
    try:
        dest = cache / "dea-metaframework"
        git_clone_or_update(args.ecf_url, args.ecf_ref, dest)
        domains, stages = load_ecf_from_git(dest)
        return domains, stages, f"{args.ecf_url} @ {args.ecf_ref}"
    except Exception as e:
        print(f"  warn: ECF fetch failed ({e}); using fallback axis", file=sys.stderr)
        return list(FALLBACK_DOMAINS), list(FALLBACK_STAGES), "fallback-axis"


def find_entities_dir(root: Path) -> Path:
    # Prefer nested entities/v1-alpha over repo root (root may contain CATALOG.yaml etc.)
    candidates = [
        root / "entities" / "v1-alpha",
        root / "entities" / "v1",
        root / "v1-alpha",
        root,
    ]
    for c in candidates:
        if not c.is_dir():
            continue
        if any(c.glob("dea:*")):
            return c
        # flat capability yaml only (not repo-level config yaml)
        if any(c.glob("capability-*.yaml")) or any(c.glob("dea:capability-*.yaml")):
            return c
    raise FileNotFoundError(f"No entity catalog under {root}")


def iter_entity_yaml_paths(entities_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for d in sorted(entities_dir.iterdir()):
        if d.is_dir() and ":" in d.name:
            paths.extend(sorted(d.glob("*.yaml")))
    if paths:
        return paths
    return [p for p in sorted(entities_dir.glob("*.yaml")) if not p.name.lower().startswith("readme")]


def load_entities_from_dir(entities_dir: Path) -> list[dict[str, Any]]:
    caps = []
    for path in iter_entity_yaml_paths(entities_dir):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  warn: {path}: {e}", file=sys.stderr)
            continue
        if isinstance(doc, dict) and doc.get("name"):
            caps.append(doc)
    print(f"  loaded {len(caps)} entities from {entities_dir}")
    return caps


def load_entities_from_url_list(urls: list[str]) -> list[dict[str, Any]]:
    caps = []
    for url in urls:
        try:
            doc = load_url(url)
        except Exception as e:
            print(f"  warn: {url}: {e}", file=sys.stderr)
            continue
        if isinstance(doc, dict) and doc.get("name"):
            caps.append(doc)
        elif isinstance(doc, list):
            for item in doc:
                if isinstance(item, dict) and item.get("name"):
                    caps.append(item)
    print(f"  loaded {len(caps)} entities from URLs")
    return caps


def infer_title(ents: list[dict[str, Any]], default: str) -> str:
    types = {str(e.get("type") or "") for e in ents}
    types.discard("")
    if len(types) == 1:
        t = types.pop()
        spaced = re.sub(r"([a-z])([A-Z])", r"\1 \2", t)
        return f"{spaced} Map"
    return default


def infer_title_from_repo(root: Path, ents: list[dict[str, Any]]) -> str:
    readme = root / "README.md"
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines()[:15]:
            if line.startswith("# "):
                name = line[2:].strip()
                if name and len(name) < 80:
                    return name if name.lower().endswith("map") else f"{name} Map"
    return infer_title(ents, "Business Capability Map")


def resolve_entities(args, cache: Path):
    """Returns (entities, catalog_note, title, catalog_root|None)."""
    if args.entity_urls:
        urls = [u.strip() for u in args.entity_urls.split(",") if u.strip()]
        ents = load_entities_from_url_list(urls)
        return ents, "entity-urls", infer_title(ents, "Entity Map"), None
    if args.catalog_url:
        dest = cache / "catalog"
        git_clone_or_update(args.catalog_url, args.catalog_ref, dest)
        entities_dir = find_entities_dir(dest)
        ents = load_entities_from_dir(entities_dir)
        title = infer_title_from_repo(dest, ents)
        return ents, f"{args.catalog_url} @ {args.catalog_ref}", title, dest
    root = Path(args.local_catalog) if args.local_catalog else REPO_ROOT
    entities_dir = find_entities_dir(root)
    ents = load_entities_from_dir(entities_dir)
    return ents, str(entities_dir.resolve()), infer_title_from_repo(root, ents), root


def entity_layer(doc: dict[str, Any]) -> str:
    for f in LAYER_FIELDS:
        v = doc.get(f)
        if isinstance(v, str) and v.lower() in ("strategic", "operational", "support"):
            return v.lower()
    return "support"


def evidence_level(doc: dict[str, Any]) -> int:
    sources = (doc.get("evidence") or {}).get("sources") or []
    n = len(sources) if isinstance(sources, list) else 0
    if n >= 5:
        return 3
    if n >= 3:
        return 2
    return 1


def short_name(name: str) -> str:
    mapping = {
        "Enterprise Governance": "Ent. Governance",
        "Strategic Planning": "Strat. Planning",
        "Financial Stewardship": "Fin. Stewardship",
        "Financial Management": "Fin. Management",
        "Analytics and Intelligence": "Analytics & Intel.",
        "Information Management": "Info. Management",
        "Sourcing and Procurement": "Sourcing & Proc.",
        "Workforce Planning": "Workforce Plan.",
        "Innovation Management": "Innovation",
        "Resilience Management": "Resilience",
        "Compliance Management": "Compliance",
        "Change Management": "Change Mgmt",
        "Customer Management": "Customer Mgmt",
        "Partner Management": "Partner Mgmt",
        "Supplier Management": "Supplier Mgmt",
        "Offering Management": "Offering Mgmt",
        "Asset Management": "Asset Mgmt",
        "Facility Management": "Facility Mgmt",
        "Security Management": "Security Mgmt",
        "Risk Management": "Risk Mgmt",
        "Legal Management": "Legal Mgmt",
        "Workforce Management": "Workforce Mgmt",
        "Technology Management": "Technology Mgmt",
    }
    return mapping.get(name, name.replace("Management", "Mgmt"))


def normalize_domain_key(d: str, domain_keys: set[str]) -> str | None:
    k = to_kebab(d)
    if k in domain_keys:
        return k
    # Schema PascalCase → kebab often inserts "-and-" (GovernanceAndExistence
    # → governance-and-existence) while catalogs use governance-existence.
    variants = [
        k,
        k.replace("-and-", "-"),
        k.replace("-and-", "&").replace("&", "-"),  # no-op safety
    ]
    aliases = {
        "customer-demand": "party-relationship",
        "product-offering": "product-value",
        "operations-delivery": "enablement-operations",
        "supply-resources": "strategy-direction",
        "finance-value": "finance-accounting",
        "people-organization": "agency-organization",
        "governance-and-existence": "governance-existence",
        "strategy-and-direction": "strategy-direction",
        "agency-and-organization": "agency-organization",
        "party-and-relationship": "party-relationship",
        "product-and-value": "product-value",
        "operations-and-enablement": "enablement-operations",
        "enablement-and-operations": "enablement-operations",
        "finance-and-accounting": "finance-accounting",
        # pre-v2.5.0 domain-6 spellings (historical snapshots)
        "operations-enablement": "enablement-operations",
        # reverse (catalog kebab → schema-with-and)
        "governance-existence": "governance-and-existence",
        "strategy-direction": "strategy-and-direction",
        "agency-organization": "agency-and-organization",
        "party-relationship": "party-and-relationship",
        "product-value": "product-and-value",
        "enablement-operations": "enablement-and-operations",
        "finance-accounting": "finance-and-accounting",
    }
    for v in variants:
        if v in domain_keys:
            return v
        a = aliases.get(v)
        if a and a in domain_keys:
            return a
    return None


def build_matrix(ents, domain_order, stage_order):
    domain_keys = set(domain_order)
    stage_keys = set(stage_order)
    matrix = defaultdict(list)
    bo_map, evidence, span = {}, {}, defaultdict(set)
    held_unmapped = []

    for doc in ents:
        name = doc["name"]
        layer = entity_layer(doc)
        bo_map[name] = str(doc.get("business_object") or doc.get("object") or "")
        evidence[name] = evidence_level(doc)
        ecf = doc.get("ecf") or {}
        if ecf.get("held_unmapped"):
            held_unmapped.append(name)
            continue
        prim = ecf.get("primary") or {}
        if prim.get("domain") and prim.get("stage"):
            d = normalize_domain_key(str(prim["domain"]), domain_keys)
            s = to_kebab(str(prim["stage"]))
            if d and s in stage_keys:
                matrix[(d, s)].append((name, True, layer))
                span[name].add(d)
        for sec in ecf.get("secondary") or []:
            if sec.get("domain") and sec.get("stage"):
                d = normalize_domain_key(str(sec["domain"]), domain_keys)
                s = to_kebab(str(sec["stage"]))
                if d and s in stage_keys:
                    matrix[(d, s)].append((name, False, layer))
                    span[name].add(d)

    dual = {n for n, ds in span.items() if len(ds) > 1}
    dual |= {"Partner Management", "Marketing", "Information Management"}
    for key in matrix:
        matrix[key].sort(key=lambda t: (not t[1], t[0]))
    return dict(matrix), bo_map, evidence, dual, held_unmapped


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def evidence_html(level: int) -> str:
    return '<span class="evidence">' + "".join(
        f'<i class="{"on" if i < level else "off"}"></i>' for i in range(3)
    ) + "</span>"


def chip_html(name, is_pri, layer, bo_map, evidence, dual):
    short = short_name(name)
    bo = bo_map.get(name, "")
    role = "primary" if is_pri else "secondary"
    dual_m = '<span class="dual">◇</span>' if name in dual else ""
    bo_h = f'<div class="l2-bo">{esc(bo)}</div>' if bo else ""
    return (
        f'<div class="l2 {role} {layer}">'
        f'<div class="l2-text"><div class="l2-name">{esc(short)}</div>{bo_h}</div>'
        f'<div class="l2-meta">{evidence_html(evidence.get(name, 1))}{dual_m}</div>'
        f"</div>"
    )


def cell_html(domain, stage, domain_labels, stage_labels, matrix, bo_map, evidence, dual):
    items = matrix.get((domain, stage), [])
    dlab = domain_labels.get(domain, domain).replace("\n", " ").split("&")[0].strip()
    slab = stage_labels.get(stage, stage.title())
    parent = f"L0 · {dlab} × {slab}"
    dense = " dense" if len(items) >= 4 else ""
    if not items:
        return f'<div class="l0 empty{dense}"><div class="l0-parent">{esc(parent)}</div></div>'
    chips = "\n".join(chip_html(n, p, ly, bo_map, evidence, dual) for n, p, ly in items)
    return (
        f'<div class="l0{dense}"><div class="l0-parent">{esc(parent)}</div>'
        f'<div class="l1"><div class="l1-parent">L1 · Entities in cell</div>{chips}</div></div>'
    )


def css(n_stages: int) -> str:
    cols = f"minmax(140px, 11%) repeat({n_stages}, minmax(120px, 1fr))"
    return f"""
  :root {{
    --bg: #fff; --black: #101010; --dark: #222; --mid: #555; --light: #888;
    --ultra: #f0f0f0; --deep-red: #8b0000; --red-wash: #ffe6e6;
    --strategic: #8b0000; --operational: #282828; --support: #5f5f5f;
    --l0-border: 3px solid #2a2a2a; --l1-border: 2px solid #707070;
    --font: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg); color: var(--black); font-family: var(--font);
    padding: 16px 20px 24px; min-width: 1400px;
  }}
  .topbar {{
    display: grid; grid-template-columns: 1fr auto 1fr; align-items: start;
    border-top: 5px solid var(--deep-red); padding-top: 12px; margin-bottom: 14px; gap: 8px;
  }}
  .brand {{
    justify-self: start; font-size: 1.65rem; font-weight: 800;
    letter-spacing: -0.03em; color: var(--deep-red); line-height: 1;
  }}
  .brand span {{ color: var(--black); font-weight: 700; }}
  .titles {{ justify-self: center; text-align: center; max-width: 40rem; }}
  .titles h2 {{
    font-size: 1.15rem; font-weight: 600; color: var(--dark);
    letter-spacing: -0.01em; margin: 0;
  }}
  .titles .fine {{
    margin-top: 4px; font-size: 0.68rem; font-weight: 400;
    color: var(--light); letter-spacing: 0.02em;
  }}
  .topbar-spacer {{ justify-self: end; }}
  .matrix {{
    display: grid; grid-template-columns: {cols};
    grid-auto-rows: minmax(88px, auto); gap: 0; border: 1px solid #ccc; width: 100%;
  }}
  .stage-head {{
    background: var(--dark); color: #fff; font-weight: 700; font-size: 0.85rem;
    text-align: center; padding: 10px 4px; border-left: 1px solid #444;
  }}
  .stage-head:nth-child(even) {{ background: #383838; }}
  .corner {{ background: var(--deep-red); border-bottom: 1px solid #5a0000; }}
  .domain-label {{
    background: var(--deep-red); color: #fff; font-weight: 700; font-size: 0.78rem;
    line-height: 1.25; display: flex; align-items: center; justify-content: center;
    text-align: center; padding: 8px 6px; border-top: 1px solid #5a0000;
  }}
  .l0 {{
    border: var(--l0-border); border-radius: 8px; margin: 3px; background: #fafafa;
    display: flex; flex-direction: column; min-height: 84px; overflow: hidden;
  }}
  .l0.dense {{ background: var(--red-wash); }}
  .l0.empty {{ align-items: center; justify-content: center; }}
  .l0.empty::after {{
    content: ""; width: 7px; height: 7px; border-radius: 50%; background: #b0b0b0;
  }}
  .l0-parent {{
    font-size: 0.62rem; font-weight: 600; color: var(--mid);
    padding: 3px 6px 2px; border-bottom: 1px solid #ddd; background: #f3f3f3;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex-shrink: 0;
  }}
  .l0.dense .l0-parent {{ background: #f8dede; color: #6a3030; }}
  .l1 {{
    border: var(--l1-border); border-radius: 6px; background: #f7f7f7;
    margin: 4px; padding: 4px; flex: 1; display: flex; flex-direction: column; gap: 3px;
  }}
  .l1-parent {{
    font-size: 0.58rem; font-weight: 700; color: var(--mid); text-transform: uppercase;
    letter-spacing: 0.04em; padding: 0 2px 2px;
  }}
  .l2 {{
    border-radius: 5px; padding: 5px 8px; display: flex; align-items: center;
    justify-content: space-between; gap: 6px; min-height: 28px; flex: 1 1 auto;
  }}
  .l2.primary {{ color: #fff; }}
  .l2.primary.strategic {{ background: var(--strategic); }}
  .l2.primary.operational {{ background: var(--operational); }}
  .l2.primary.support {{ background: var(--support); }}
  .l2.secondary {{ background: #fff; border: 2px solid; }}
  .l2.secondary.strategic {{ border-color: var(--strategic); color: var(--strategic); }}
  .l2.secondary.operational {{ border-color: var(--operational); color: var(--operational); }}
  .l2.secondary.support {{ border-color: var(--support); color: var(--support); }}
  .l2-text {{ min-width: 0; flex: 1; }}
  .l2-name {{
    font-size: 0.78rem; font-weight: 700; line-height: 1.15;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }}
  .l2-bo {{
    font-size: 0.65rem; opacity: 0.85; margin-top: 1px;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }}
  .l2-meta {{ display: flex; align-items: center; gap: 4px; flex-shrink: 0; }}
  .evidence {{ display: flex; gap: 3px; }}
  .evidence i {{ width: 6px; height: 6px; border-radius: 50%; display: inline-block; }}
  .l2.primary .evidence i.on {{ background: #fff; }}
  .l2.primary .evidence i.off {{ border: 1px solid rgba(255,255,255,0.7); }}
  .l2.secondary.strategic .evidence i.on {{ background: var(--strategic); }}
  .l2.secondary.strategic .evidence i.off {{ border: 1px solid var(--strategic); }}
  .l2.secondary.operational .evidence i.on {{ background: var(--operational); }}
  .l2.secondary.operational .evidence i.off {{ border: 1px solid var(--operational); }}
  .l2.secondary.support .evidence i.on {{ background: var(--support); }}
  .l2.secondary.support .evidence i.off {{ border: 1px solid var(--support); }}
  .dual {{ font-size: 0.7rem; }}
  .bottombar {{
    display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-start;
    gap: 12px 24px; margin-top: 12px; padding-top: 10px;
    border-bottom: 4px solid var(--deep-red); padding-bottom: 10px;
  }}
  .legend {{
    display: flex; flex-wrap: wrap; align-items: center; gap: 10px 14px;
    font-size: 0.68rem; color: var(--dark); justify-content: flex-start; max-width: 70%;
  }}
  .legend-item {{ display: flex; align-items: center; gap: 5px; }}
  .swatch {{ width: 12px; height: 10px; border-radius: 2px; display: inline-block; }}
  .swatch.pri {{ background: var(--deep-red); }}
  .swatch.sec {{ background: #fff; border: 2px solid var(--mid); }}
  .attribution {{
    margin-left: auto; text-align: right; font-size: 0.65rem;
    color: var(--light); line-height: 1.35; max-width: 28%;
  }}
  @media print {{ body {{ padding: 0; min-width: 0; }} }}
""".strip()


def build_html(*, catalog_title, matrix, bo_map, evidence, dual, held_unmapped,
               domains, stages, n_ents, label, catalog_note, ecf_note):
    today = date.today().isoformat()
    domain_order = [d for d, _ in domains]
    stage_order = [s for s, _ in stages]
    domain_labels = dict(domains)
    stage_labels = dict(stages)
    primary_cells = sum(1 for items in matrix.values() if any(p for _, p, _ in items))
    referenced = len(matrix)
    total = len(domain_order) * len(stage_order)
    empties = max(0, total - referenced)
    unmapped = len(held_unmapped)
    fine = (
        f"{label} · {n_ents} entities · ECF {len(domain_order)}×{len(stage_order)} · "
        f"{primary_cells} primary · {referenced} referenced · {empties} empty · "
        f"{unmapped} unmapped · generated {today}"
    )
    stage_heads = "\n".join(
        f'<div class="stage-head">{esc(stage_labels.get(s, s))}</div>' for s in stage_order
    )
    rows = []
    for d in domain_order:
        parts = domain_labels.get(d, d).split("\n")
        rows.append('<div class="domain-label">' + "<br />".join(esc(p) for p in parts) + "</div>")
        for s in stage_order:
            rows.append(cell_html(d, s, domain_labels, stage_labels, matrix, bo_map, evidence, dual))
    unmapped_note = f"<br />held_unmapped: {esc(', '.join(held_unmapped))}" if held_unmapped else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>OpenDEAM — {esc(catalog_title)}</title>
<style>
{css(len(stage_order))}
</style>
</head>
<body>
<header class="topbar">
  <h1 class="brand">OpenDEA<span>M</span></h1>
  <div class="titles">
    <h2>{esc(catalog_title)}</h2>
    <div class="fine">{esc(fine)}</div>
  </div>
  <div class="topbar-spacer"></div>
</header>
<div class="matrix" role="grid" aria-label="ECF domain by stage map">
  <div class="corner"></div>
  {stage_heads}
  {chr(10).join(rows)}
</div>
<footer class="bottombar">
  <div class="legend">
    <div class="legend-item">
      <div style="display:inline-flex;border:3px solid #2a2a2a;border-radius:6px;padding:3px;background:#fafafa">
        <div style="border:2px solid #707070;border-radius:4px;background:#f5f5f5;padding:2px">
          <span style="background:#8b0000;color:#fff;font-size:0.6rem;font-weight:700;padding:1px 5px;border-radius:3px">L2</span>
        </div>
      </div>
      <span><strong>L0</strong> cell ⊃ <strong>L1</strong> group ⊃ <strong>L2</strong> entity</span>
    </div>
    <div class="legend-item"><span class="swatch" style="background:var(--strategic)"></span> Strategic</div>
    <div class="legend-item"><span class="swatch" style="background:var(--operational)"></span> Operational</div>
    <div class="legend-item"><span class="swatch" style="background:var(--support)"></span> Support</div>
    <div class="legend-item"><span class="swatch pri"></span> Primary</div>
    <div class="legend-item"><span class="swatch sec"></span> Secondary</div>
    <div class="legend-item">●●● Evidence</div>
    <div class="legend-item">◇ multi-domain</div>
  </div>
  <div class="attribution">
    Attribution: emmanuel@otchere.com<br />
    Catalog: {esc(catalog_note)}<br />
    ECF axis: {esc(ecf_note)}{unmapped_note}
  </div>
</footer>
</body>
</html>
"""


def main() -> None:
    p = argparse.ArgumentParser(description="OpenDEAM nested ECF map generator (release-pipeline edition)")
    p.add_argument("-o", "--out", type=Path, default=Path("OpenDEA_Foundation_Capability_Map_Nested.html"))
    p.add_argument("--label", default="v1-alpha",
                   help="Catalog version label for the fine print (e.g. v1-alpha.3)")
    p.add_argument("--catalog-url", default=None,
                   help="Git URL of the catalog repo (omit to use the local checkout)")
    p.add_argument("--catalog-ref", default=DEFAULT_REF)
    p.add_argument("--ecf-url", default=DEFAULT_ECF_GIT)
    p.add_argument("--ecf-ref", default=DEFAULT_REF)
    p.add_argument("--ecf-domains-url", default=None)
    p.add_argument("--ecf-stages-url", default=None)
    p.add_argument("--local-catalog", type=Path, default=None,
                   help="Catalog repo path (default: this script's repo root)")
    p.add_argument("--local-ecf", type=Path, default=None)
    p.add_argument("--entity-urls", default=None, help="Comma-separated entity YAML/JSON URLs")
    p.add_argument("--cache-dir", type=Path, default=None)
    p.add_argument("--title", default=None, help="Override H2 catalog title")
    p.add_argument("--png", default=None, help="Optional: also render to this PNG path")
    p.add_argument("--dpi", type=int, default=300, help="PNG DPI (default 300)")
    p.add_argument("--page-w-mm", type=float, default=420.0,
                   help="PNG page width in millimetres (default 420 = A3 long edge)")
    p.add_argument("--page-h-mm", type=float, default=297.0,
                   help="PNG page height in millimetres (default 297 = A3 short edge)")
    args = p.parse_args()

    cache = args.cache_dir or Path(tempfile.gettempdir()) / "opendeam-map-cache"
    cache.mkdir(parents=True, exist_ok=True)

    print("Resolving catalog entities …")
    ents, catalog_note, title, catalog_root = resolve_entities(args, cache)
    if args.title:
        title = args.title
    if not ents:
        print("No entities loaded — aborting.", file=sys.stderr)
        sys.exit(1)

    print("Resolving ECF axis …")
    domains, stages, ecf_note = resolve_ecf_axis(args, cache, catalog_root)
    domain_order = [d for d, _ in domains]
    stage_order = [s for s, _ in stages]
    print(f"  domains ({len(domains)}): {domain_order}")
    print(f"  stages  ({len(stages)}): {stage_order}")

    matrix, bo_map, evidence, dual, held = build_matrix(ents, domain_order, stage_order)

    html_doc = build_html(
        catalog_title=title,
        matrix=matrix,
        bo_map=bo_map,
        evidence=evidence,
        dual=dual,
        held_unmapped=held,
        domains=domains,
        stages=stages,
        n_ents=len(ents),
        label=args.label,
        catalog_note=catalog_note,
        ecf_note=ecf_note,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html_doc, encoding="utf-8")
    print(f"Wrote {args.out.resolve()} ({len(html_doc):,} bytes)")
    print(f"  title={title!r}  entities={len(ents)}  cells={len(matrix)}  unmapped={held or '—'}")

    # Optional: render A3 landscape PNG via weasyprint + pdftoppm.
    if args.png:
        render_png(html_doc, args.out, Path(args.png), page_mm=(args.page_w_mm, args.page_h_mm),
                   dpi=args.dpi)


def render_png(html_doc: str, html_src: Path, png_out: Path, *,
               page_mm: tuple[float, float], dpi: int) -> None:
    """Render the HTML poster to a print-quality PNG using weasyprint + pdftoppm.

    weasyprint composes the CSS-Grid HTML to a single PDF page at the requested
    paper size. pdftoppm (poppler) rasterises the PDF to a PNG at the chosen
    DPI. Both are pure dependencies (no Chrome / playwright / sharp required).

    Falls back gracefully if either dependency is missing: a clear error message
    names the missing system package and points the operator at the README.
    """
    import shutil
    import subprocess
    import tempfile

    try:
        from weasyprint import HTML as WP_HTML, CSS as WP_CSS  # noqa: F401
    except ImportError:
        sys.exit("weasyprint not installed; run `pip install weasyprint` "
                 "or use the HTML output without --png.")

    if not shutil.which("pdftoppm"):
        sys.exit("pdftoppm not found; install poppler-utils "
                 "(e.g. `sudo apt install poppler-utils`).")

    width_mm, height_mm = page_mm
    png_out.parent.mkdir(parents=True, exist_ok=True)

    # CSS that pins the page to the chosen paper size with zero margins so the
    # poster's CSS-Grid fills the entire sheet. orientation=landscape is set by
    # choosing width >= height (A3 landscape: 420mm x 297mm).
    a3_css = (
        f"@page {{ size: {width_mm}mm {height_mm}mm; margin: 0; }}"
        f"html, body {{ width: {width_mm}mm; height: {height_mm}mm; }}"
    )
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as pdf_f:
        pdf_path = Path(pdf_f.name)
    try:
        WP_HTML(string=html_doc, base_url=str(html_src.parent)).write_pdf(
            target=str(pdf_path),
            stylesheets=[WP_CSS(string=a3_css)],
        )
        # pdftoppm writes single-page PNGs as <stem>-1.png; redirect to a
        # single named output via -singlefile.
        subprocess.run(
            ["pdftoppm", "-r", str(dpi), "-png", "-singlefile",
             str(pdf_path), str(png_out.with_suffix(""))],
            check=True,
        )
        print(f"Wrote {png_out.resolve()} ({png_out.stat().st_size:,} bytes, "
              f"{width_mm:g}x{height_mm:g}mm @ {dpi} dpi)")
    finally:
        pdf_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
