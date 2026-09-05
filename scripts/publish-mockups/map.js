// Map SVG generator (A4 landscape, 1400x800).
// IDs only. Matches the v1-alpha.0 mockup structurally.

const { DOMAINS, STAGES, COLORS } = require('../lib/grid.js');

const W = 1400;
const H = 800;
const GRID_X = 232;
const GRID_Y = 82;
const CELL_W = 158.85714285714286;
const CELL_H = 90.28571428571429;
const CELL_GAP_X = 4;        // mockup: 232 + 158.86 = 390.86; next cell at 394.86; gap = 4
const CELL_GAP_Y = 4;        // mockup: 82 + 90.29 = 172.29; next at 176.29; gap = 4
const HEADER_HEIGHT = 60;
const ROWS = DOMAINS.length;
const COLS = STAGES.length;

function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

function generateMapSVG({ entities, overlayIndex, candIndex, version: ver }) {
  const out = [];
  out.push('<?xml version="1.0" encoding="UTF-8"?>');
  out.push(`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`);
  out.push('<defs><style>text{font-family:-apple-system,Helvetica,Arial,sans-serif}</style></defs>');
  out.push(`<rect width="${W}" height="${H}" fill="#ffffff"/>`);
  out.push(`<rect x="0" y="0" width="${W}" height="${HEADER_HEIGHT}" fill="${COLORS.HEADER_BAND_MAP}"/>`);
  out.push(`<text x="30" y="36" font-size="20" font-weight="700" fill="${COLORS.HEADER_TEXT}">Capability Map: ECF Coverage ${esc(ver)}</text>`);
  out.push(`<text x="1370" y="36" font-size="14" font-weight="600" fill="${COLORS.VERSION_BADGE_VALUE}" text-anchor="end">26 caps / 14 cells / 1 held-unmapped</text>`);

  // Column headers (y=74, x = cellCenter)
  for (let c = 0; c < COLS; c++) {
    const hx = GRID_X + CELL_W * c + CELL_W / 2 + CELL_GAP_X * c;
    out.push(`<text x="${hx}" y="74" font-size="13" font-weight="600" fill="${COLORS.DOMAIN_LABEL}" text-anchor="middle">${STAGES[c].display}</text>`);
  }

  // Cells (rows)
  for (let r = 0; r < ROWS; r++) {
    const rowY = GRID_Y + CELL_H * r + CELL_GAP_Y * r + 50.14285714285714; // mockup row header y: 132.14 (r=0), 226.43 (r=1)
    // The mockup row header is at y = (cellY) + 50.142857; cellY for r=0 = 82 -> header y = 132.14
    out.push(`<text x="40" y="${rowY}" font-size="12" font-weight="600" fill="${COLORS.DOMAIN_LABEL}">${DOMAINS[r].display}</text>`);

    for (let c = 0; c < COLS; c++) {
      // Cell container rect: mockup draws ALL 49 cells (even empty ones).
      const cellX = GRID_X + CELL_W * c + CELL_GAP_X * c;
      const cellY = GRID_Y + CELL_H * r + CELL_GAP_Y * r;
      out.push(`<rect x="${cellX}" y="${cellY}" width="${CELL_W}" height="${CELL_H}" rx="4" fill="#ffffff" stroke="${COLORS.CELL_BORDER}"/>`);

      // find entries
      const cellEntries = [];
      for (const ent of entities) {
        const cand = candIndex.get(ent.id);
        if (!cand) continue;
        const ov = overlayIndex.get(cand);
        if (!ov || !ov.primary) continue;
        if (ov.primary.domain === DOMAINS[r].id && ov.primary.stage === STAGES[c].id) {
          cellEntries.push({ ent, cand });
        }
      }
      cellEntries.sort((a, b) => a.cand.localeCompare(b.cand, undefined, { numeric: true }));

      // IDs centered vertically; the mockup uses ~17.26px line pitch (matches: 96.628, 113.886, 131.143, 148.4, 165.657)
      // First ID baseline = cellY + 14.62857142857143
      const firstY = cellY + 14.62857142857143;
      const pitch = 17.25714285714287;
      for (let i = 0; i < cellEntries.length; i++) {
        const ty = firstY + i * pitch;
        const tx = cellX + CELL_W / 2;
        out.push(`<text x="${tx}" y="${ty}" font-size="10" font-weight="600" fill="${COLORS.MAP_ID_TEXT}" text-anchor="middle">${cellEntries[i].cand}</text>`);
      }
    }
  }

  // Footer
  out.push(`<text x="30" y="784" font-size="10" fill="${COLORS.HEADER_MUTED}">dea:catalog/business-capabilities@${esc(ver)}  \u00b7  dea:ecf@1.0.0  \u00b7  CR-DEA-BC-05</text>`);
  out.push(`<text x="1370" y="784" font-size="10" fill="${COLORS.HEADER_MUTED}" text-anchor="end">Held unmapped: CAND-019 Technology Management</text>`);

  out.push('</svg>');
  return out.join('\n');
}

module.exports = { generateMapSVG };