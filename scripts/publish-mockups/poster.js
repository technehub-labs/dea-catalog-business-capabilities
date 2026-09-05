// Poster SVG generator (A2 landscape, 1684x1191).
// Matches /home/hermes/dea-work/business-capabilities/18_publication/posters/v1-alpha.0/poster.svg
// structurally: same dimensions, same color tokens, same coordinate math, same sidebar layout.

const { DOMAINS, STAGES, COLORS, layerStyle, domainIndex, stageIndex } = require('../lib/grid.js');

const W = 1684;
const H = 1191;
const GRID_X = 284;          // x of col 0 (Conceive)
const GRID_Y = 164;          // y of row 0 (Governance Existence)
const CELL_W = 141.14285714285714;
const CELL_H = 109.28571428571429;
const TILE_PAD = 4;
const TILE_BASE_W = 133.14285714285714;
const TILE_BASE_H = 16.25714285714286;
const ROWS = DOMAINS.length;
const COLS = STAGES.length;

function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function fmt(n) { return String(Number(n.toFixed(11)).toString().replace(/0+$/,'').replace(/\.$/,'')); }

// Build tiles per cell. Each cell holds 1..N capabilities (overlay gives the CAND-NNN -> entity join).
// The mockup places tiles vertically with a small fixed pitch; tile widths adapt to count so that
// all tiles in a cell share equal width and stack from top with no overlap.
function cellTiles(cellEntries) {
  if (cellEntries.length === 0) return [];
  // Tile width: base if 1, equal split if 2+, capped to TILE_BASE_W per tile (matching mockup).
  // Mockup rule: when 1 tile, w=133.14; when 2-3 tiles stacked, w=133.14 (same width); when 3+ it shrinks.
  // We use a single fixed width TILE_BASE_W for all tiles and stack with pitch = TILE_BASE_H.
  return cellEntries.map((entry, i) => ({
    x: TILE_BASE_W,
    w: TILE_BASE_W,
    y: i * TILE_BASE_H,
    h: TILE_BASE_H,
    entry,
  }));
}

function generatePosterSVG({ entities, overlayIndex, candIndex, version: ver }) {
  const out = [];
  out.push('<?xml version="1.0" encoding="UTF-8"?>');
  out.push(`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`);
  out.push('<defs><style>text{font-family:-apple-system,Helvetica,Arial,sans-serif}</style></defs>');
  out.push(`<rect width="${W}" height="${H}" fill="${COLORS.POSTER_BG}"/>`);
  out.push(`<rect x="0" y="0" width="${W}" height="130" fill="${COLORS.HEADER_BAND_POSTER}"/>`);
  out.push(`<text x="60" y="58" font-size="34" font-weight="700" fill="${COLORS.HEADER_TEXT}">First-Order Business Capability Catalog</text>`);
  out.push(`<text x="60" y="92" font-size="20" fill="${COLORS.HEADER_SUBTITLE}">Poster: Enterprise Concept Framework backdrop, 26 canonical first-order capabilities</text>`);
  out.push(`<rect x="1324" y="34" width="300" height="62" rx="6" fill="${COLORS.VERSION_BADGE_BG}" stroke="${COLORS.VERSION_BADGE_STROKE}"/>`);
  out.push(`<text x="1334" y="62" font-size="13" fill="${COLORS.VERSION_BADGE_LABEL}">Catalog version</text>`);
  out.push(`<text x="1334" y="86" font-size="22" font-weight="700" fill="${COLORS.VERSION_BADGE_VALUE}">${esc(ver)}</text>`);

  // Column (Conceive..Retire) headers
  for (let c = 0; c < COLS; c++) {
    const x = GRID_X + CELL_W * c + CELL_W / 2 + 4 * c; // mockup header x uses per-cell-center + slight offset
    // mockup header x for CONCEIVE is 354.57142857142856 = GRID_X + CELL_W/2 + 4*0 (approx) for c=0
    // We compute as: GRID_X + CELL_W * c + (CELL_W / 2) + 4 * c (matches mockup).
    const hx = GRID_X + CELL_W * c + CELL_W / 2 + 4 * c;
    out.push(`<text x="${hx}" y="146" font-size="18" font-weight="600" fill="${COLORS.DOMAIN_LABEL}" text-anchor="middle">${STAGES[c].display}</text>`);
  }

  // Cells (49: 7 rows x 7 cols)
  for (let r = 0; r < ROWS; r++) {
    const rowDomain = DOMAINS[r];
    // row header text
    const rowY = GRID_Y + CELL_H * r + 59.64285714285714; // mockup uses y = 223.64285714285714 for r=0 (= 164+59.642857)
    out.push(`<text x="70" y="${rowY}" font-size="14" font-weight="600" fill="${COLORS.DOMAIN_LABEL}">${rowDomain.display}</text>`);

    for (let c = 0; c < COLS; c++) {
      const cx = GRID_X + CELL_W * c + 4 * c; // cell x for (0,0) is 284 (matches mockup)
      const cy = GRID_Y + CELL_H * r + 8.0 * r; // mockup cell y for (0,0) is 164 (matches)
      // The mockup cell y values: 164, 281.29, 398.57, 515.86, 633.14, 750.43, 867.71
      // That is GRID_Y=164 + CELL_H(=109.29) * r + 8 * r (gaps between cells).
      const cellX = GRID_X + CELL_W * c + 4 * c;
      const cellY = GRID_Y + CELL_H * r + 8 * r;

      // Find entries whose primary == (thisDomain, thisStage)
      const cellEntries = [];
      for (const ent of entities) {
        const cand = candIndex.get(ent.id);
        if (!cand) continue;
        const ov = overlayIndex.get(cand);
        if (!ov || !ov.primary) continue;
        if (ov.primary.domain === rowDomain.id && ov.primary.stage === STAGES[c].id) {
          cellEntries.push({ ent, cand });
        }
      }
      cellEntries.sort((a, b) => a.cand.localeCompare(b.cand, undefined, { numeric: true }));

      // Cell container rect: ALWAYS draw (even empty cells per mockup).
      out.push(`<rect x="${cellX}" y="${cellY}" width="${CELL_W}" height="${CELL_H}" rx="6" fill="${COLORS.CELL_BG}" stroke="${COLORS.CELL_BORDER}"/>`);

      // Tiles stacked vertically inside cell
      for (let i = 0; i < cellEntries.length; i++) {
        const { ent, cand } = cellEntries[i];
        const sty = layerStyle(ent.capability_layer);
        const tx = cellX + TILE_PAD;
        const ty = cellY + TILE_PAD + i * TILE_BASE_H;
        const tw = TILE_BASE_W;
        const th = TILE_BASE_H;
        out.push(`<rect x="${tx}" y="${ty}" width="${tw}" height="${th}" rx="4" fill="${sty.bg}" stroke="${sty.stroke}" stroke-width="1.5"/>`);
        out.push(`<text x="${tx + 6}" y="${ty + 16}" font-size="11" font-weight="700" fill="${sty.text}">${cand}</text>`);
        // name (truncated to 24 chars)
        const name = (ent.name || '').length > 24 ? (ent.name.slice(0, 23) + '') : ent.name;
        out.push(`<text x="${tx + 6}" y="${ty + 32}" font-size="11" fill="${COLORS.DOMAIN_LABEL}">${esc(name)}</text>`);
        // secondary badge
        const ov = overlayIndex.get(cand);
        const secCount = (ov && ov.secondary) ? ov.secondary.length : 0;
        if (secCount > 0) {
          out.push(`<text x="${tx + TILE_BASE_W + 0}" y="${ty + 16}" font-size="10" font-weight="600" fill="${sty.text}" text-anchor="end">+${secCount} sec</text>`);
        }
      }
    }
  }

  // Sidebar (right): canonical count, cells used, specializations, deferred, capability_layer legend, held-unmapped
  const SX = 1354, SY = 160, SW = 300, SH = 821;
  out.push(`<rect x="${SX}" y="${SY}" width="${SW}" height="${SH}" rx="8" fill="${COLORS.SIDEBAR_BG}" stroke="${COLORS.CELL_BORDER}"/>`);
  out.push(`<text x="${SX + 20}" y="${SY + 32}" font-size="16" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">Status</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 70}" font-size="13" fill="${COLORS.SIDEBAR_LABEL}">Canonical entries</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 95}" font-size="28" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">26</text>`);
  out.push(`<text x="${SX + 130}" y="${SY + 70}" font-size="13" fill="${COLORS.SIDEBAR_LABEL}">ECF cells used</text>`);
  out.push(`<text x="${SX + 130}" y="${SY + 95}" font-size="28" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">14 / 49</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 140}" font-size="13" fill="${COLORS.SIDEBAR_LABEL}">Specializations</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 165}" font-size="22" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">1 (MCSP)</text>`);
  out.push(`<text x="${SX + 170}" y="${SY + 140}" font-size="13" fill="${COLORS.SIDEBAR_LABEL}">Deferred</text>`);
  out.push(`<text x="${SX + 170}" y="${SY + 165}" font-size="22" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">1</text>`);
  out.push(`<line x1="${SX + 20}" y1="${SY + 195}" x2="${SX + SW - 20}" y2="${SY + 195}" stroke="${COLORS.CELL_BORDER}"/>`);
  out.push(`<text x="${SX + 20}" y="${SY + 225}" font-size="14" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">Capability layer</text>`);
  // Legend swatches
  out.push(`<rect x="${SX + 20}" y="${SY + 245}" width="24" height="24" rx="4" fill="${COLORS.TILE_STRATEGIC_BG}" stroke="${COLORS.TILE_STRATEGIC_STROKE}" stroke-width="1.5"/>`);
  out.push(`<text x="${SX + 56}" y="${SY + 263}" font-size="14" fill="${COLORS.DOMAIN_LABEL}">strategic</text>`);
  out.push(`<rect x="${SX + 20}" y="${SY + 281}" width="24" height="24" rx="4" fill="${COLORS.TILE_OPERATIONAL_BG}" stroke="${COLORS.TILE_OPERATIONAL_STROKE}" stroke-width="1.5"/>`);
  out.push(`<text x="${SX + 56}" y="${SY + 299}" font-size="14" fill="${COLORS.DOMAIN_LABEL}">operational</text>`);
  out.push(`<rect x="${SX + 20}" y="${SY + 317}" width="24" height="24" rx="4" fill="${COLORS.TILE_SUPPORT_BG}" stroke="${COLORS.TILE_SUPPORT_STROKE}" stroke-width="1.5"/>`);
  out.push(`<text x="${SX + 56}" y="${SY + 335}" font-size="14" fill="${COLORS.DOMAIN_LABEL}">support</text>`);
  out.push(`<line x1="${SX + 20}" y1="${SY + 370}" x2="${SX + SW - 20}" y2="${SY + 370}" stroke="${COLORS.CELL_BORDER}"/>`);
  out.push(`<text x="${SX + 20}" y="${SY + 400}" font-size="14" font-weight="700" fill="${COLORS.DOMAIN_LABEL}">Held unmapped</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 420}" font-size="11" fill="${COLORS.SIDEBAR_LABEL}">CAND-019 Technology Management</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 460}" font-size="10" fill="${COLORS.SIDEBAR_MUTED}">Legitimately absent; technology is L5,</text>`);
  out.push(`<text x="${SX + 20}" y="${SY + 474}" font-size="10" fill="${COLORS.SIDEBAR_MUTED}">not first-order business capability.</text>`);

  // Footer band
  out.push(`<rect x="0" y="1011" width="${W}" height="180" fill="${COLORS.FOOTER_BAND}"/>`);
  out.push(`<text x="60" y="1049" font-size="15" font-weight="700" fill="${COLORS.FOOTER_TEXT}">Provenance</text>`);
  out.push(`<text x="60" y="1071" font-size="12" fill="${COLORS.FOOTER_MUTED}">ECF Conformance Profile: dea:ecf@1.0.0  \u00b7  Metamodel pin: 1.0.0  \u00b7  Method: CR-DEA-BC-01  \u00b7  Specialization framework: CR-DEA-BC-04</text>`);
  out.push(`<text x="60" y="1091" font-size="12" fill="${COLORS.FOOTER_MUTED}">Layer 3 (value delivery); ECF coordinates are classification context, not capability identity (CG-001 \u00a74)</text>`);
  out.push(`<text x="60" y="1116" font-size="12" fill="${COLORS.HEADER_MUTED}">Source: technehub-labs/dea-catalog-business-capabilities@${esc(ver)}  \u00b7  CR-DEA-BC-05 \u00a75 (initial posture)</text>`);
  out.push(`<text x="60" y="1136" font-size="11" fill="${COLORS.FOOTER_DIM}">Empty cells are legitimate results, not gaps. See docs/VERSIONING.md for catalog version semantics.</text>`);

  out.push('</svg>');
  return out.join('\n');
}

module.exports = { generatePosterSVG };