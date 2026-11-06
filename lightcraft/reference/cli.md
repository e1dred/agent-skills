# CLI: subcommands, run/script forms, output

## Commands worth running from a shell

| Subcommand | What it does (as verified) |
|---|---|
| `run [--demo\|--library DIR] [--import PATH] [--keep-going] COMMAND k=v …` | one process, many commands, one JSON line each |
| `run --script FILE\|- …` | same, from JSON lines `{"command": id, "params": {…}}` (or `{"method": …}` for control methods) |
| `render IN -o OUT [--set ctl=v]… [--settings FILE] [--preset ID] [--size N] [--quality Q] [--opt k=v]…` | develop one file and write .jpg/.png/.tif/.webp/.avif/.jxl/.psd/.dng |
| `merge hdr\|panorama\|hdr-panorama\|hdr-batch FILES…` | writes `<first>-HDR.dng` / `-Pano.dng` next to the first file; options `--deghost`, `--projection`, `--auto-crop`, `--preview OUT.png` |
| `synth-merge hdr\|panorama -o DIR` | writes synthetic inputs: `bracket-0..2.dng` (verified 3 files) / `view-0..4.png` (verified 5 files) |
| `commands [--json]`, `controls [--json]` | 389 command ids (0.19.0) with params; 122 develop controls with min/max/default |
| `snapshot [--demo\|--library DIR] -o OUT.png --script FILE` | full app UI rasterised offscreen through the control protocol (NOT exercised here: it drives the UI, not the engine) |
| `mcp [--demo\|--library DIR] [--compact]` | MCP server over stdio, same commands as tools |
| `calibrate`, `denoise-serve` | camera profiles from raws; remote denoise tiles (not exercised) |

## Modes

- `--demo`: procedural library, 24 photos (ids 1…24, stable between runs, titles like "Lake at first light"),
  camera "Synthetic S1/X2", capture dates 2026-03-01 … 2026-09-20. Every photo is generated: no file on disk.
  Demo state (edits, presets, albums, keywords) does **not** survive the process.
- `--library DIR`: creates (`library.info.load.created: true`) or opens a library. Edits, presets, albums,
  keywords, print/slideshow templates persist. A `--library` run also persists imports.
- `--import PATH` (repeatable): import before the first command, like `library.import mode=add`.

## Output

- Each command prints `{"command", "ms", "ok": true, "result": …}` or
  `"ok": false, "error": "…"`. Exit status is non-zero when any command failed.
- `result` is often the read-back object of the action (`{"added":1,"skipped":0}`), sometimes `null`
  (`version.create`, `edit.undo`) even on success — read the effect with a second command.
- Errors name a parameter or a missing thing: `invalid parameters for \`x\`: missing number \`x\``,
  `command \`x\` is not available right now: <reason>`, `unknown control \`light.vibrance\``. Read the error and
  add exactly what it names (ids from `list`/`inspect`, enums from the docs).

## render

- `--set` takes develop **control ids** only (`controls`), never command names: `--set light.exposure=1.0`.
- Sizes: `--size 480` gave 480×360 for a 1600×1200 source (long edge, aspect kept).
- Verified pixel effect: exposure +1 changed 172,800 of 172,800 pixels of the 480×360 render; vignette −50
  changed 103,946; `--set light.vibrance` refused — the control is `color.vibrance`.
- `--settings FILE` merges a partial develop-settings JSON (a `crop` block in `{"crop":{"aspect":[1,1]}}` did
  not change the render — use `develop.set`/`crop.aspect` in a library run instead, or `--set crop.angle`).
- `--opt` passes `app.export` options (`colorSpace=displayP3`, `bitDepth=16`, `percent=50`, `ppi=300`,
  `format=original`, `metadata=none`).

## merge from the shell

- `synth-merge hdr -o DIR` wrote 3 bracketed DNGs (~4–5 MB each); `synth-merge panorama -o DIR` wrote 5 PNG views.
- `merge panorama` on the 5 synthetic views wrote a 7.8 MB `view-4-Pano.dng` and added it to the library.
- `merge hdr-batch` on the 3 synthetic brackets merged one set and reported the rest as `failed` (see
  `reference/merge-and-models.md`).
