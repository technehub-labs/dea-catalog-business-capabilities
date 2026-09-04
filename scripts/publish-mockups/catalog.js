// Catalog index SVG generator (A4 portrait, 1240x1754).
// Tabular reference of all canonical entries.

const { COLORS } = require('../lib/grid.js');

const W = 1240;
const H = 1754;
const ROW_H = 38;
const ROWS_PER_PAGE = 1; // single page; 26 rows fit comfortably

function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

function generateCatalogSVG({ entities, overlayIndex, candIndex, version: ver }) {
  const out = [];
  // Build sorted rows by candidate
  const rows = [];
  for (const ent of entities) {
    const cand = candIndex.get(ent.id);
    if (!cand) continue;
    rows.push({ ent, cand });
  }
  rows.sort((a, b) => a.cand.localeCompare(b.cand, undefined, { numeric: true }));

  out.push('<?xml version="1.0" encoding="UTF-8"?>');
  out.push(`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`);
  out.push('<defs><style>text{font-family:-apple-system,Helvetica,Arial,sans-serif}</style></defs>');
  out.push(`<rect width="${W}" height="${H}" fill="#ffffff"/>`);
  out.push(`<rect x="0" y="0" width="${W}" height="130" fill="${COLORS.HEADER_BAND_CATALOG}"/>`);
  out.push(`<text x="50" y="56" font-size="28" font-weight="700" fill="${COLORS.HEADER_TEXT}">Business Capability Catalog: ${esc(ver)}</text>`);
  out.push(`<text x="50" y="86" font-size="15" fill="${COLORS.HEADER_SUBTITLE}">${rows.length} canonical first-order capabilities: tabular reference</text>`);
  out.push(`<text x="50" y="110" font-size="11" fill="${COLORS.HEADER_MUTED}">dea:catalog/business-capabilities@${esc(ver)}  \u00b7  dea:ecf@1.0.0  \u00b7  CR-DEA-BC-05</text>`);

  // Column header row
  out.push(`<rect x="50" y="160" width="850" height="32" fill="${COLORS.CATALOG_HEADER_BG}"/>`);
  out.push(`<text x="58" y="181" font-size="12" font-weight="700" fill="${COLORS.CATALOG_HEADER_TEXT}">ID</text>`);
  out.push(`<text x="128" y="181" font-size="12" font-weight="700" fill="${COLORS.CATALOG_HEADER_TEXT}">Capability</text>`);
  out.push(`<text x="348" y="181" font-size="12" font-weight="700" fill="${COLORS.CATALOG_HEADER_TEXT}">Layer</text>`);
  out.push(`<text x="448" y="181" font-size="12" font-weight="700" fill="${COLORS.CATALOG_HEADER_TEXT}">Primary ECF</text>`);
  out.push(`<text x="678" y="181" font-size="12" font-weight="700" fill="${COLORS.CATALOG_HEADER_TEXT}">Secondary</text>`);
  out.push(`<text x="908" y="181" font-size="12" font-weight="700" fill="${COLORS.CATALOG_HEADER_TEXT}">Related</text>`);

  // Data rows
  let rowY = 192;
  for (let i = 0; i < rows.length; i++) {
    const { ent, cand } = rows[i];
    const ov = overlayIndex.get(cand) || {};
    const altFill = (i % 2 === 0) ? COLORS.CATALOG_ROW_ALT : '#ffffff';
    out.push(`<rect x="50" y="${rowY}" width="850" height="${ROW_H}" fill="${altFill}" stroke="${COLORS.CELL_BORDER}"/>`);

    const rowCenter = rowY + 24;

    // ID
    out.push(`<text x="58" y="${rowCenter}" font-size="11" font-weight="700" fill="${COLORS.CATALOG_ID}">${cand}</text>`);

    // Capability name
    out.push(`<text x="128" y="${rowCenter}" font-size="12" font-weight="600" fill="${COLORS.CATALOG_NAME_TEXT}">${esc(ent.name)}</text>`);

    // Layer
    out.push(`<text x="348" y="${rowCenter}" font-size="11" fill="${COLORS.CATALOG_ROW_TEXT}">${esc(ent.capability_layer || '')}</text>`);

    // Primary ECF
    let primaryText;
    if (!ov.primary) primaryText = 'held-unmapped';
    else primaryText = `${ov.primary.domain} / ${ov.primary.stage}`;
    out.push(`<text x="448" y="${rowCenter}" font-size="10" fill="${COLORS.CATALOG_ROW_TEXT}">${esc(primaryText)}</text>`);

    // Secondary
    let secText;
    if (!ov.secondary || ov.secondary.length === 0) secText = '\u2014';
    else secText = ov.secondary.map(s => `${s.domain} / ${s.stage}`).join(', ');
    out.push(`<text x="678" y="${rowCenter}" font-size="10" fill="${COLORS.CATALOG_ROW_TEXT}">${esc(secText)}</text>`);

    // Related capabilities (top 2)
    const related = (ent.related_capabilities || []).slice(0, 2).join(', ');
    out.push(`<text x="908" y="${rowCenter}" font-size="9" fill="${COLORS.CATALOG_RELATED}">${esc(related)}</text>`);

    rowY += ROW_H;
  }

  // Footer note
  out.push(`<text x="50" y="1704" font-size="10" fill="${COLORS.HEADER_MUTED}">Empty ECF cells are legitimate results, not gaps. Held-unmapped: CAND-019 Technology Management.</text>`);
  out.push(`<text x="1190" y="1722" font-size="9" fill="${COLORS.HEADER_MUTED}" text-anchor="end">Source: technehub-labs/dea-catalog-business-capabilities@${esc(ver)}</text>`);

  out.push('</svg>');
  return out.join('\n');
}

module.exports = { generateCatalogSVG };