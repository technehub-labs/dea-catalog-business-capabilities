// Small helper: write file with mkdir -p, return relative path + size for MANIFEST.

const fs = require('node:fs');
const path = require('node:path');

function writeFile(relPath, content) {
  const full = path.resolve(relPath);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, content);
  return { path: relPath, size: Buffer.byteLength(content, 'utf8') };
}

module.exports = { writeFile };