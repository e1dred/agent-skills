# Newer commands / versions

## 0.18.1 (2026-11-04)

First commanded round for this skill; no earlier version was available to diff. What exists in 0.18.1:

- 383 command ids (`lightcraft-cli commands`), 122 develop controls (`lightcraft-cli controls`).
- Subcommands: `run`, `mcp`, `render`, `snapshot`, `merge`, `synth-merge`, `denoise-serve`, `commands`,
  `controls`, `calibrate`.
- Families: activity, album(s), app, beforeAfter, catalog, crop, curve, denoise, develop, edit, export, faces,
  filter, focus, folder, geometry, history, journal, keyword, label, lens, library, mask, merge, metadata,
  photo, pointColor, preset(s), print, profile(s), redeye, segment, slideshow, spot, stack, version.
- Evidence for every id: `results.jsonl`; status per id: `skill/reference/command-catalogue.md`; refusals and
  why: `REPORT.md`.
- Not tested: `snapshot` (drives the UI), the control channel (`--connect`, `ui.*`), MCP transport, raw decoding,
  any model download or AI model (none installed).

## 0.19.0 (checked 2026-11-06)

`lightcraft-cli commands` lists **389 ids** (383 in 0.18.1): 6 added, none removed, 13 with changed parameter docs.
A scripted round (one `--demo` process running catalogue/develop/metadata/filter/album/export; a fresh `--library`
import → edit → rating → filter → export; the single-shot `render`) ran on both versions with every command ok.
`develop.get` now reports `"process": 6` (was 2), `library.info` gained `lowDiskSpace`, and the exported JPEGs differ
slightly (mean 0.35–0.45 of 255 per channel, max 23) — the process-version render change, not a break.

- **`app.hotPixelLimit {"percent"}`** sets the share of photosites Remove Hot Pixels may replace (0.001–100 %, default 0.2 %) → `{percent, default}`; 0.2 → 0.5 read back.
- **`prefs.backgroundPrep {}`** → `{app, library|null, settings, own, building}`: what each mode prepares in the background (culling/library: `previews`, `ahead`, `eyeAhead`, `scope all|marked|onScreen`; develop: `ahead`, `scope`). **`prefs.setBackgroundPrep {"library":true,"settings":{"culling":{"scope":"marked"}}}`** → the same shape; with a library open, scope went all → marked and `own` false → true. In `--demo` mode it refuses "no library is open".
- **`preset.saveRecipe {"name","group","recipe":[{id,value}]}`** saves a batch-edit recipe as a user preset → `{id, name}` (id `user.import-recipes-mini-recipe`). The recipe must name plain develop controls (no white balance, geometry or crop); `library.import` takes the same shape as `recipe` and applies it as each photo is imported (an import with exposure 0.4 / contrast 15 read back exactly that).
- **Camera profiles (`.dcp`):** `profiles.camera {}` → `{profiles:[{id,name,cameraModel,file}]}`; `profile.import` now takes `.dcp` files as well as `.cube`; `profile.deleteImported` accepts `dcp:…` ids and `profile.deleteCamera {"id":"dcp:…"}` removes one. Not verified with a real `.dcp` (none on the test machine): `deleteCamera` refused with "no imported camera profile", and a `.cube` import still imported (`lut:imported-t`), then deleted.
- **Denoise:** `denoise.models.select {"id":null}` → `{model:null}` and `denoise.status` still reports `model {id:"builtin", name:"Built-in"}` — **null now means the built-in BM3D denoiser, not off**. `denoise.status` no longer has a `noModel` state; `denoise.toggle` still refuses a JPEG ("applies to raw photos developed from their sensor data").
- **Process version:** `develop.get` reports `"process": 6`, and `develop.updateProcess` answers "already on the current process (version 6)" for a fresh library. Renders change slightly, so compare pixels with a tolerance rather than by hash across versions.
- **Library and previews:** `library.buildPreviews` takes `force`, `from`, `backward`, `background` and `row` (a build started with `{force:true,from:1,row:true}` → `{total:1, running:true, …}`); `library.previewProgress` gained `skipped`, `shared`, `background`; `library.importPreview` returns `scanLimited` and `skipped {unreadable, unsupported}` (a folder scan of test images: scanned 600, duplicates 55, unsupported 138); `library.smartPreviews` builds the previews of all photos in view only when more than one is selected.
- `metadata.downloadPlaceNames` no longer takes `dataset`; place names always download into the settings folder (not run: a 3 MB network download).
