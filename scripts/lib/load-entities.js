// Load entities, overlay, dependencies, CHANGELOG for the publication pipeline.
// Reads YAML via js-yaml, joins overlay entries by candidate id (CAND-NNN).

const fs = require('node:fs');
const path = require('node:path');
const yaml = require('js-yaml');

function loadEntities(rootDir) {
  const dir = path.join(rootDir, 'entities', 'v1-alpha');
  const out = [];
  for (const name of fs.readdirSync(dir).sort()) {
    if (!name.startsWith('capability-') || !name.endsWith('.yaml')) continue;
    const doc = yaml.load(fs.readFileSync(path.join(dir, name), 'utf8'));
    if (!doc || !doc.id) continue;
    out.push(doc);
  }
  return out;
}

function loadOverlay(rootDir) {
  const p = path.join(rootDir, 'docs', 'research', 'ecf-overlay-v0.2.yaml');
  return yaml.load(fs.readFileSync(p, 'utf8'));
}

function loadDeps(rootDir) {
  const p = path.join(rootDir, 'dependencies.yaml');
  return yaml.load(fs.readFileSync(p, 'utf8'));
}

function loadDepsRaw(rootDir) {
  return fs.readFileSync(path.join(rootDir, 'dependencies.yaml'), 'utf8');
}

function loadOverlayRaw(rootDir) {
  return fs.readFileSync(path.join(rootDir, 'docs', 'research', 'ecf-overlay-v0.2.yaml'), 'utf8');
}

function loadChangelog(rootDir) {
  return fs.readFileSync(path.join(rootDir, 'CHANGELOG.md'), 'utf8');
}

// Index overlay by candidate id -> { name, primary, secondary, status, ... }
function indexOverlay(overlay) {
  const map = new Map();
  for (const o of overlay.overlays || []) {
    map.set(o.candidate, o);
  }
  return map;
}

// Map entity -> CAND-NNN using overlay (overlay name -> candidate).
function buildCandIndex(entities, overlayIndex) {
  const out = new Map(); // entity.id -> CAND-NNN
  // invert: iterate overlay; for each, find the entity whose name matches the overlay name
  for (const [cand, ov] of overlayIndex.entries()) {
    const ent = entities.find(e => e.name === ov.name || e.name === (ov.name || '').replace(' / ', ' / '));
    if (ent) out.set(ent.id, cand);
  }
  return out;
}

// Resolve the catalog's current version label from CHANGELOG header
function currentVersion(changelogText) {
  // The first occurrence of "## [<version>] - <date>" is the current baseline.
  const m = changelogText.match(/^## \[(v[^\]]+)\]\s*-\s*\d{4}-\d{2}-\d{2}/m);
  return m ? m[1] : 'v0.0.0';
}

module.exports = {
  loadEntities, loadOverlay, loadDeps, loadDepsRaw, loadOverlayRaw, loadChangelog,
  indexOverlay, buildCandIndex, currentVersion,
};