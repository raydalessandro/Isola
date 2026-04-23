// Generates PWA icons: a terracotta circle with a white "I" serif letter.
// Run with: node scripts/generate-icons.mjs
import sharp from "sharp";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT_DIR = resolve(__dirname, "..", "public");

function iconSvg({ size, bg, fg, padding = 0 }) {
  const r = size / 2 - padding;
  const fontSize = size * 0.58;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">
  <rect width="${size}" height="${size}" fill="${bg}"/>
  <circle cx="${size / 2}" cy="${size / 2}" r="${r}" fill="${fg}"/>
  <text x="50%" y="50%"
        dominant-baseline="central" text-anchor="middle"
        font-family="Georgia, 'Cormorant Garamond', serif"
        font-size="${fontSize}" font-style="italic"
        fill="#f5ead5">I</text>
</svg>`;
}

async function make(filename, { size, bg, fg, padding = 0 }) {
  const svg = iconSvg({ size, bg, fg, padding });
  const out = resolve(OUT_DIR, filename);
  await sharp(Buffer.from(svg)).png().toFile(out);
  console.log("wrote", out);
}

await make("icon-192.png", {
  size: 192,
  bg: "#f5ead5",
  fg: "#c8532c",
  padding: 8,
});
await make("icon-512.png", {
  size: 512,
  bg: "#f5ead5",
  fg: "#c8532c",
  padding: 24,
});
// Maskable (padded safe area ~10%) per W3C spec
await make("icon-512-maskable.png", {
  size: 512,
  bg: "#c8532c",
  fg: "#c8532c",
  padding: 0,
});

// Also write a favicon-sized version
await make("favicon-32.png", {
  size: 32,
  bg: "#f5ead5",
  fg: "#c8532c",
  padding: 2,
});
