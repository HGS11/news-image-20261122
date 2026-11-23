import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath: string = fileURLToPath(import.meta.url);
const scriptDir: string = path.dirname(scriptPath);
const srcFile: string = path.join(scriptDir, "entry.png");

if (!fs.existsSync(srcFile)) {
  console.error("Error: entry.png not found at " + srcFile);
  process.exit(1);
}

const outDirEnv: string | undefined = process.env.MAKEFUN_OUTPUT_DIR;
const outDir: string = outDirEnv && outDirEnv.length > 0 ? outDirEnv : "/output";

fs.mkdirSync(outDir, { recursive: true });

const destFile: string = path.join(outDir, "entry.png");
fs.copyFileSync(srcFile, destFile);

const stats = fs.statSync(destFile);
console.log("Copied entry.png to " + destFile + " (" + String(stats.size) + " bytes)");
