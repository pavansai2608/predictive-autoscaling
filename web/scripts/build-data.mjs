/**
 * Generate everything the static site reads, from the repo's own artefacts.
 *
 * ONE SOURCE OF TRUTH. The site never carries a hand-maintained copy of a
 * number: bench/replay*.json and outputs/results.csv are the originals, and
 * this script is the only thing allowed to derive from them.
 *
 *   node web/scripts/build-data.mjs        (or: make web-data)
 *
 * Writes:
 *   web/public/data/replay.json        ramp runs, minified
 *   web/public/data/replay-step.json   step runs, minified
 *   web/public/data/backtest.json      derived from outputs/results.csv
 *
 * The replay files are re-emitted rather than symlinked because `output:
 * 'export'` copies public/ verbatim and a symlink would not survive.
 */
import { readFileSync, writeFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = join(HERE, "..", "..");
const OUT = join(HERE, "..", "public", "data");
mkdirSync(OUT, { recursive: true });

const kb = (p) => (statSync(p).size / 1024).toFixed(1);

// ---- 1. the recorded benchmark windows -------------------------------------
for (const name of ["replay.json", "replay-step.json"]) {
  const src = join(REPO, "bench", name);
  if (!existsSync(src)) {
    // A scenario whose file is absent is simply not offered by the site, so a
    // missing file is a warning rather than a build failure.
    console.warn(`  ! bench/${name} missing — that scenario will not be offered`);
    continue;
  }
  const parsed = JSON.parse(readFileSync(src, "utf8"));
  const dst = join(OUT, name);
  writeFileSync(dst, JSON.stringify(parsed));      // minified: the source is indent=1
  console.log(`  ${name.padEnd(18)} ${parsed.runs.length} runs   ${kb(src)} KB -> ${kb(dst)} KB`);
}

// ---- 2. the backtest scoreboard --------------------------------------------
// outputs/ is gitignored (regenerable from data/traffic.parquet via
// src/backtest.py), so the derived JSON below is committed instead. This is the
// fix for the Overview page having hardcoded the string "64.5% lower cost".
const csv = join(REPO, "outputs", "results.csv");
const backtestDst = join(OUT, "backtest.json");

if (!existsSync(csv)) {
  if (existsSync(backtestDst)) {
    console.warn("  ! outputs/results.csv missing — keeping the committed backtest.json");
  } else {
    console.error("  ERROR: outputs/results.csv missing and no committed backtest.json.");
    console.error("         Run: python src/backtest.py");
    process.exit(1);
  }
} else {
  const lines = readFileSync(csv, "utf8").trim().split("\n");
  const header = lines[0].split(",");
  const rows = lines.slice(1).map((line) => {
    const cells = line.split(",");
    const o = {};
    header.forEach((h, i) => {
      const v = cells[i];
      o[h === "model" ? "model" : h] = h === "model" ? v : Number(v);
    });
    return o;
  });

  const by = Object.fromEntries(rows.map((r) => [r.model, r]));
  const champion = "gbm_q0.9";
  const baseline = "naive";
  if (!by[champion] || !by[baseline]) {
    console.error(`  ERROR: results.csv lacks '${champion}' or '${baseline}'.`);
    process.exit(1);
  }

  // The headline the Overview page shows. Computed, never asserted.
  const vsNaive = (1 - by[champion].cost / by[baseline].cost) * 100;
  // The project's most instructive pair: lowest MAE is NOT lowest cost.
  const meanModel = by["gbm"];
  const maeDelta = meanModel ? (1 - meanModel.mae / by[champion].mae) * 100 : null;
  const costDelta = meanModel ? (meanModel.cost / by[champion].cost - 1) * 100 : null;

  writeFileSync(
    backtestDst,
    JSON.stringify({
      generatedFrom: "outputs/results.csv",
      champion,
      baseline,
      rows,
      championCost: by[champion].cost,
      baselineCost: by[baseline].cost,
      vsNaivePct: vsNaive,
      meanModelMaeBetterPct: maeDelta,
      meanModelCostWorsePct: costDelta,
    }, null, 1)
  );
  console.log(`  backtest.json      ${rows.length} models   vs naive: ${vsNaive.toFixed(1)}% lower cost`);
}
console.log("  -> web/public/data/");
