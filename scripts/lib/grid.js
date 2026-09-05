// CR-DEA-BC-06 publication pipeline
// Pure SVG string composition (no D3) matching the v1-alpha.0 mockup templates.
//
// Layout grid (7 domains x 7 stages), color tokens, capability-layer mapping.
// Domain order matches the ECF canonical enum (CR-ECF-005) in PascalCase form;
// stage order matches the canonical lifecycle (CR-ECF-005). Display strings
// used in the SVGs are the kebab-case display form per the catalog's
// conformant-with-extension posture (CR-ECF-CG-003 §5).

const DOMAINS = [
  { id: 'governance-existence',   display: 'Governance Existence' },
  { id: 'customer-demand',        display: 'Customer Demand' },
  { id: 'supply-resources',        display: 'Supply Resources' },
  { id: 'product-offering',       display: 'Product Offering' },
  { id: 'operations-delivery',    display: 'Operations Delivery' },
  { id: 'finance-value',          display: 'Finance Value' },
  { id: 'people-organization',    display: 'People Organization' },
];

const STAGES = [
  { id: 'conceive',  display: 'CONCEIVE' },
  { id: 'design',    display: 'DESIGN' },
  { id: 'build',     display: 'BUILD' },
  { id: 'activate',  display: 'ACTIVATE' },
  { id: 'operate',   display: 'OPERATE' },
  { id: 'improve',   display: 'IMPROVE' },
  { id: 'retire',    display: 'RETIRE' },
];

const COLORS = {
  // Poster
  POSTER_BG: '#fafbfc',
  HEADER_BAND_POSTER: '#0f172a',
  HEADER_BAND_MAP: '#1e293b',
  HEADER_BAND_CATALOG: '#0f172a',
  VERSION_BADGE_BG: '#1e293b',
  VERSION_BADGE_STROKE: '#475569',
  VERSION_BADGE_LABEL: '#94a3b8',
  VERSION_BADGE_VALUE: '#fef3c7',
  HEADER_TEXT: '#ffffff',
  HEADER_SUBTITLE: '#cbd5e1',
  HEADER_MUTED: '#94a3b8',
  CELL_BORDER: '#e5e7eb',
  CELL_BG: '#ffffff',
  DOMAIN_LABEL: '#1f2933',
  TILE_STRATEGIC_BG: '#dbeafe',
  TILE_STRATEGIC_STROKE: '#1e3a8a',
  TILE_STRATEGIC_TEXT: '#1e3a8a',
  TILE_OPERATIONAL_BG: '#d1fae5',
  TILE_OPERATIONAL_STROKE: '#065f46',
  TILE_OPERATIONAL_TEXT: '#065f46',
  TILE_SUPPORT_BG: '#fed7aa',
  TILE_SUPPORT_STROKE: '#7c2d12',
  TILE_SUPPORT_TEXT: '#7c2d12',
  MAP_ID_TEXT: '#0f766e',
  SIDEBAR_BG: '#ffffff',
  SIDEBAR_LABEL: '#6b7280',
  SIDEBAR_MUTED: '#9ca3af',
  FOOTER_BAND: '#1e293b',
  FOOTER_TEXT: '#ffffff',
  FOOTER_MUTED: '#cbd5e1',
  FOOTER_DIM: '#64748b',
  // Catalog
  CATALOG_ROW_ALT: '#f9fafb',
  CATALOG_HEADER_BG: '#1e293b',
  CATALOG_HEADER_TEXT: '#ffffff',
  CATALOG_ROW_TEXT: '#374151',
  CATALOG_NAME_TEXT: '#1f2933',
  CATALOG_RELATED: '#9ca3af',
  CATALOG_ID: '#0f766e',
};

function layerStyle(layer) {
  switch (layer) {
    case 'strategic':   return { bg: COLORS.TILE_STRATEGIC_BG,   stroke: COLORS.TILE_STRATEGIC_STROKE,   text: COLORS.TILE_STRATEGIC_TEXT };
    case 'operational': return { bg: COLORS.TILE_OPERATIONAL_BG, stroke: COLORS.TILE_OPERATIONAL_STROKE, text: COLORS.TILE_OPERATIONAL_TEXT };
    case 'support':     return { bg: COLORS.TILE_SUPPORT_BG,     stroke: COLORS.TILE_SUPPORT_STROKE,     text: COLORS.TILE_SUPPORT_TEXT };
    default:            return { bg: COLORS.CELL_BG,              stroke: COLORS.CELL_BORDER,             text: COLORS.DOMAIN_LABEL };
  }
}

function domainIndex(id) { return DOMAINS.findIndex(d => d.id === id); }
function stageIndex(id)  { return STAGES.findIndex(s => s.id === id);  }
function domainByIndex(i) { return DOMAINS[i]; }
function stageByIndex(i)  { return STAGES[i];  }

module.exports = {
  DOMAINS, STAGES, COLORS,
  layerStyle,
  domainIndex, stageIndex, domainByIndex, stageByIndex,
};