#!/usr/bin/env node
//
// CR-DEA-BC-06 publication pipeline entry point.
//
// Usage:
//   node scripts/publish.js latest            # publish mutable latest artifacts
//   node scripts/publish.js <version-label>   # publish versioned artifacts (e.g. v1-alpha.0)
//
// In CI (process.env.CI === 'true'), after writing artifacts the script:
//   - dispatches repository_dispatch 'capabilities-updated' to the central
//     aggregator (technehub-labs/technehub-labs.github.io) for /latest/ builds
//   - dispatches 'capabilities-versioned' for /<version>/ builds
//
// In CI, if the GITHUB_TOKEN is present, this script creates a GitHub Release
// for versioned builds with a zip of all artifacts attached.

const fs = require('node:fs');
const path = require('node:path');

const {
  loadEntities, loadOverlay, loadOverlayRaw,
  loadDeps, loadDepsRaw, loadChangelog,
  indexOverlay, buildCandIndex, currentVersion,
} = require('./lib/load-entities.js');
const { generatePosterSVG } = require('./publish-mockups/poster.js');
const { generateMapSVG }    = require('./publish-mockups/map.js');
const { generateCatalogSVG } = require('./publish-mockups/catalog.js');
const { generateCatalogCSV } = require('./publish-mockups/csv.js');
const { writeFile } = require('./lib/write-files.js');

const ROOT = path.resolve(__dirname, '..');
const target = process.argv[2] || 'latest';

function dispatchEvent(eventType, clientPayload) {
  // Use the GitHub CLI for repository_dispatch since it's already auth'd.
  const { execSync } = require('node:child_process');
  const payload = JSON.stringify(clientPayload);
  try {
    execSync(
      `gh api repos/technehub-labs/technehub-labs.github.io/dispatches -X POST -f event_type="${eventType}" -f client_payload='${payload}'`,
      { stdio: 'inherit', env: { ...process.env } },
    );
    console.log(`dispatched ${eventType} to aggregator`);
  } catch (e) {
    console.warn(`warn: dispatch ${eventType} failed: ${e.message}`);
  }
}

function createGitHubRelease(versionLabel, manifest) {
  const { execSync } = require('node:child_process');
  const zipPath = path.join('out', `${versionLabel}.zip`);
  try {
    execSync(
      `gh release create ${versionLabel} ${zipPath} --repo technehub-labs/dea-catalog-business-capabilities --generate-notes --title "${versionLabel}"`,
      { stdio: 'inherit', env: { ...process.env } },
    );
    console.log(`created release ${versionLabel}`);
  } catch (e) {
    if (String(e.message).includes('already exists')) {
      // Re-upload assets to existing release
      try {
        execSync(
          `gh release upload ${versionLabel} ${zipPath} --repo technehub-labs/dea-catalog-business-capabilities --clobber`,
          { stdio: 'inherit', env: { ...process.env } },
        );
        console.log(`updated existing release ${versionLabel}`);
      } catch (e2) {
        console.warn(`warn: release upload failed: ${e2.message}`);
      }
    } else {
      console.warn(`warn: release create failed: ${e.message}`);
    }
  }
}

async function main() {
  const isCI = process.env.CI === 'true';
  const outDir = path.join(ROOT, 'out', target);

  console.log(`publish: target=${target} outDir=${outDir} ci=${isCI}`);

  // Load
  const entities    = loadEntities(ROOT);
  const overlay     = loadOverlay(ROOT);
  const overlayRaw  = loadOverlayRaw(ROOT);
  const deps        = loadDeps(ROOT);
  const depsRaw     = loadDepsRaw(ROOT);
  const changelog   = loadChangelog(ROOT);
  const overlayIndex = indexOverlay(overlay);
  const candIndex   = buildCandIndex(entities, overlayIndex);
  const versionLabel = target === 'latest' ? currentVersion(changelog) : target;

  console.log(`publish: ${entities.length} entities, ${overlay.overlays.length} overlays, version=${versionLabel}`);

  // Generate
  const posterSvg  = generatePosterSVG({ entities, overlayIndex, candIndex, version: versionLabel });
  const mapSvg     = generateMapSVG({ entities, overlayIndex, candIndex, version: versionLabel });
  const catalogSvg = generateCatalogSVG({ entities, overlayIndex, candIndex, version: versionLabel });
  const catalogCsv = generateCatalogCSV({ entities, overlayIndex, candIndex });
  const catalogJson = JSON.stringify(
    Object.fromEntries(entities.map(e => [e.id, e])),
    null, 2
  ) + '\n';
  const overlayJson = JSON.stringify(overlay, null, 2) + '\n';

  // Write
  const writes = [];
  writes.push(writeFile(path.join(outDir, 'poster.svg'),  posterSvg));
  writes.push(writeFile(path.join(outDir, 'map.svg'),     mapSvg));
  writes.push(writeFile(path.join(outDir, 'catalog.svg'), catalogSvg));
  writes.push(writeFile(path.join(outDir, 'catalog.csv'), catalogCsv));
  writes.push(writeFile(path.join(outDir, 'catalog.json'),  catalogJson));
  writes.push(writeFile(path.join(outDir, 'overlay.json'),  overlayJson));
  writes.push(writeFile(path.join(outDir, 'dependencies.yaml'), depsRaw));
  // mirror the raw overlay yaml for byte-equality with the in-repo source
  writes.push(writeFile(path.join(outDir, 'overlay.yaml'),  overlayRaw));

  // Rasterise PNGs (sharp)
  // Lazy require so the script works in environments where sharp install failed.
  let sharp;
  try { sharp = require('sharp'); } catch (e) {
    console.warn('warn: sharp not available, skipping PNG rasterisation: ' + e.message);
  }

  const DPI = { poster: 300, map: 96, catalog: 150 };
  const TARGET_W = { poster: 1684, map: 1400, catalog: 1240 };

  if (sharp) {
    for (const [stem, svg, dpi, width] of [
      ['poster',  posterSvg,  DPI.poster,  TARGET_W.poster],
      ['map',     mapSvg,     DPI.map,     TARGET_W.map],
      ['catalog', catalogSvg, DPI.catalog, TARGET_W.catalog],
    ]) {
      const buf = await sharp(Buffer.from(svg, 'utf8'), { density: Math.round(dpi * 1.5) })
        .resize({ width, withoutEnlargement: false })
        .png({ density: dpi })
        .toBuffer();
      writes.push(writeFile(path.join(outDir, `${stem}.png`), buf));
    }
  }

  // MANIFEST.md
  const manifestBody = [];
  manifestBody.push('# Publication manifest\n');
  manifestBody.push(`- Version: ${versionLabel}\n`);
  manifestBody.push(`- Generated: ${new Date().toISOString()}\n`);
  manifestBody.push(`- Catalog source: technehub-labs/dea-catalog-business-capabilities@${versionLabel}\n`);
  manifestBody.push(`- Pipeline: scripts/publish.js (CR-DEA-BC-06)\n\n`);
  manifestBody.push('## Files\n\n');
  for (const w of writes) {
    manifestBody.push(`- \`${path.relative(ROOT, w.path)}\` (${w.size} bytes)\n`);
  }
  writes.push(writeFile(path.join(outDir, 'MANIFEST.md'), manifestBody.join('')));

  // Zip (for GitHub Release)
  if (isCI && target !== 'latest') {
    try {
      const { execSync } = require('node:child_process');
      execSync(`cd "${outDir}" && zip -qr "${ROOT}/out/${versionLabel}.zip" .`, { stdio: 'inherit' });
      console.log(`zipped ${versionLabel}.zip`);
    } catch (e) {
      console.warn(`warn: zip failed: ${e.message}`);
    }
  }

  console.log('publish: done');
  for (const w of writes) {
    console.log(`  ${path.relative(ROOT, w.path)} (${w.size} bytes)`);
  }

  // CI dispatch
  if (isCI) {
    const commit = process.env.GITHUB_SHA || 'unknown';
    if (target === 'latest') {
      dispatchEvent('capabilities-updated', { source: 'dea-catalog-business-capabilities', commit, version: versionLabel });
    } else {
      dispatchEvent('capabilities-versioned', { source: 'dea-catalog-business-capabilities', commit, version: versionLabel });
      createGitHubRelease(versionLabel);
    }
  }
}

main().catch(err => {
  console.error('publish: FAIL');
  console.error(err);
  process.exit(1);
});