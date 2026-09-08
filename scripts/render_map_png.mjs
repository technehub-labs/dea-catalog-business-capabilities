#!/usr/bin/env node
//
// Render the self-contained capability-map HTML to a print-quality A3
// landscape PNG (4961 x 3508 px @ 300 DPI) for the versioned release
// pipeline (publish-versioned.yml).
//
// Uses playwright-core with the system Chrome (preinstalled on GitHub
// ubuntu runners and most dev machines; override with CHROME_PATH) and
// sharp (already a publish-pipeline dependency) for the final A3 canvas
// composite.
//
// The poster's grid is fluid (1fr columns), so content height depends on
// viewport width. The renderer picks a viewport width whose laid-out
// aspect matches A3 landscape, then screenshots at a device scale factor
// that maps the CSS width onto the full 4961 px print width — no
// resampling, minimal padding.
//
// Usage:
//   node scripts/render_map_png.mjs <input.html> <output.png>
//   CHROME_PATH=/usr/bin/google-chrome node scripts/render_map_png.mjs in.html out.png

import { chromium } from 'playwright-core';
import sharp from 'sharp';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

// A3 landscape @ 300 DPI
const A3_W = 4961;
const A3_H = 3508;
const A3_ASPECT = A3_W / A3_H; // ~1.4142

async function launchBrowser() {
  const attempts = [];
  if (process.env.CHROME_PATH) attempts.push({ executablePath: process.env.CHROME_PATH });
  attempts.push({ channel: 'chrome' });
  attempts.push({ channel: 'chromium' });
  let lastErr;
  for (const opts of attempts) {
    try {
      return await chromium.launch({ headless: true, ...opts });
    } catch (e) {
      lastErr = e;
    }
  }
  throw new Error(
    `No usable Chromium found. Set CHROME_PATH to a Chrome/Chromium binary. (${lastErr})`
  );
}

async function measure(browser, url, width) {
  const ctx = await browser.newContext({ viewport: { width, height: 1200 } });
  try {
    const page = await ctx.newPage();
    await page.goto(url, { waitUntil: 'networkidle' });
    return await page.evaluate(() => ({
      w: Math.max(document.documentElement.scrollWidth, document.body.scrollWidth),
      h: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight),
    }));
  } finally {
    await ctx.close();
  }
}

async function main() {
  const [input, output] = process.argv.slice(2);
  if (!input || !output) {
    console.error('usage: node scripts/render_map_png.mjs <input.html> <output.png>');
    process.exit(1);
  }
  const url = pathToFileURL(path.resolve(input)).href;
  const outPath = path.resolve(output);

  const browser = await launchBrowser();
  let shot;
  try {
    // Converge on a viewport width whose laid-out aspect matches A3.
    let width = 1600;
    let size = await measure(browser, url, width);
    for (let i = 0; i < 4 && Math.abs(size.w / size.h - A3_ASPECT) > 0.02; i++) {
      width = Math.max(1400, Math.round(size.h * A3_ASPECT));
      size = await measure(browser, url, width);
    }
    const dsf = A3_W / size.w;
    console.log(
      `content: ${size.w}x${size.h} css px (aspect ${(size.w / size.h).toFixed(3)}); ` +
      `deviceScaleFactor=${dsf.toFixed(3)}`
    );
    const ctx = await browser.newContext({
      viewport: { width: size.w, height: size.h },
      deviceScaleFactor: dsf,
    });
    try {
      const page = await ctx.newPage();
      await page.goto(url, { waitUntil: 'networkidle' });
      shot = await page.screenshot({ type: 'png' });
      await page.close();
    } finally {
      await ctx.close();
    }
  } finally {
    await browser.close();
  }

  // Safety: if rendering overshoots the canvas by a rounding margin, fit
  // inside without enlargement; then composite onto the exact A3 canvas.
  const fitted = await sharp(shot)
    .resize({ width: A3_W, height: A3_H, fit: 'inside', withoutEnlargement: true })
    .toBuffer();
  const meta = await sharp(fitted).metadata();
  console.log(`rendered: ${meta.width}x${meta.height} px`);

  const out = sharp({
    create: {
      width: A3_W,
      height: A3_H,
      channels: 3,
      background: { r: 255, g: 255, b: 255 },
    },
  })
    .composite([{ input: fitted, gravity: 'north' }])
    .png();
  // sharp's `.png({ density })` only sets the *intended* density for
  // encoders that surface it; on file output we set density via
  // withMetadata({ density }) so consumers see a real 300 DPI header.
  await out.toFile(outPath);
  await sharp(outPath)
    .withMetadata({ density: 300 })
    .toFile(outPath + '.tmp');
  const fs = await import('node:fs');
  fs.renameSync(outPath + '.tmp', outPath);

  const finalMeta = await sharp(outPath).metadata();
  console.log(
    `wrote ${outPath} (${finalMeta.width}x${finalMeta.height}, density=${finalMeta.density} dpi)`
  );
}

main().catch((err) => {
  console.error('render_map_png: FAIL');
  console.error(err);
  process.exit(1);
});
