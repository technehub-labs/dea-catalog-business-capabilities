// catalog.csv generator.
// Columns: candidate_id, capability, capability_layer, primary_ecf,
//          secondary_ecf, related_capabilities, entry_id, lifecycle_status

function csvEscape(s) {
  if (s === null || s === undefined) return '';
  const str = String(s);
  if (/[",\n]/.test(str)) return '"' + str.replace(/"/g, '""') + '"';
  return str;
}

function generateCatalogCSV({entities, overlayIndex, candIndex}) {
  const rows = [];
  rows.push(['candidate_id', 'capability', 'capability_layer', 'primary_ecf', 'secondary_ecf', 'related_capabilities', 'entry_id', 'lifecycle_status']);
  const sorted = [];
  for (const ent of entities) {
    const cand = candIndex.get(ent.id);
    if (!cand) continue;
    sorted.push({ ent, cand });
  }
  sorted.sort((a, b) => a.cand.localeCompare(b.cand, undefined, { numeric: true }));
  for (const { ent, cand } of sorted) {
    const ov = overlayIndex.get(cand) || {};
    const primary = ov.primary ? `${ov.primary.domain} / ${ov.primary.stage}` : 'held-unmapped';
    const secondary = (ov.secondary || []).map(s => `${s.domain} / ${s.stage}`).join('; ');
    const related = (ent.related_capabilities || []).join('; ');
    rows.push([
      cand,
      ent.name,
      ent.capability_layer || '',
      primary,
      secondary,
      related,
      ent.id,
      ent.lifecycle_status || '',
    ]);
  }
  return rows.map(r => r.map(csvEscape).join(',')).join('\n') + '\n';
}

module.exports = { generateCatalogCSV };