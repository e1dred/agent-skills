---
name: photocraft
description: Verified working knowledge for driving the PhotoCraft image editor (storytold/photocraft) from an AI agent: the headless photocraft-cli (convert, info, run, batch), the MCP bridge to a running app, exact command parameter formats, recipes and traps. Load before any PhotoCraft or image-editing task on this machine, and add what you learn at the end of it.
---

# PhotoCraft

Field notes from real tasks, tested on **photocraft-cli 0.15.1** (Linux AppImage). PhotoCraft is an early-alpha,
Photoshop-style editor in Rust: layers, masks, adjustment layers, layer styles, type, vector shapes, PSD read/write.
Everything the UI does is an *engine command*, and the CLI, the MCP server and the app's control channel all run
the same commands. If `photocraft-cli --version` is newer, re-check anything below before relying on it.

## Keep this file growing

At the end of every PhotoCraft task: add each command, parameter format, recipe or trap you verified (render it and
look, or read it back with `info`), fix anything here that proved wrong, keep it general (no personal data, names or
machine paths), and add a dated log line. Mark guesses as unverified.

## Background reading (not copied)

The ArtCraft skill set (https://github.com/midasmatterhorn/artcraft-skills, MIT, written against macOS) has a long
feature catalog for PhotoCraft; use it to learn *what exists*, and trust this file for *what was run here*.
Official docs: `docs/control-protocol.md`, `docs/mcp.md` in https://github.com/storytold/photocraft.

## Setup

- **CLI:** extract it from the AppImage (`photocraft.appimage --appimage-extract`, copy `usr/bin/photocraft-cli`
  somewhere stable); it is self-contained and needs no window. Subcommands: `convert`, `info`, `run`, `batch`,
  `droplet`, `commands`, `mcp`, `serve`. An unknown flag is a usage error.
- **MCP, headless:** `claude mcp add photocraft -- photocraft-cli mcp --automation-read-root DIR --automation-write-root DIR`
  (file access is confined to those folders).
- **MCP, live (watch edits in the window):** start the app with `--control PORT --control-token-file FILE
  --automation-read-root DIR --automation-write-root DIR`, then register
  `photocraft-cli mcp --bridge 127.0.0.1:PORT --control-token-file FILE`. Bridge-only tools: `ui_*`, `control_call`.
  (Live mode itself is untested in this file.)
- Without MCP tools in the session, everything below works from a shell with `photocraft-cli`.

## CLI essentials (verified)

```
photocraft-cli run --new '{"width":800,"height":500,"background":"#ffffff"}' \
    --cmd <id> --params '<json>' --cmd <id2> --params '<json2>' --out file.png|jpg|webp|psd|pcraft
photocraft-cli run in.pcraft --cmd … --out out.pcraft       # open, edit, save
photocraft-cli info file [--compact]                         # JSON: size, mode, depth, layers[] with id/name/kind/opacity/bounds
photocraft-cli convert in out [--quality 1-100] [--format ext]
photocraft-cli batch --actions act.json --in DIR --out DIR2 --format jpg --quality 85
photocraft-cli commands --json --filter <text>               # find ids; each has a "params" signature string
```
- Each `--params` applies to the `--cmd` before it; `run` prints every command's JSON result (new layer ids,
  bounds) — read them. `file.new` params: `width`, `height`, `mode`, `depth`, `background` (`white|black|transparent|#rrggbb`).
- **Keep layers by saving `.pcraft`.** `--out x.png|jpg` flattens and prints `warning: N layer(s) flattened`;
  `.psd` keeps layers (checked: names and kinds survive) but warns "resolution (DPI) not supported".
- `.pcraft` is the native layered format; reopen it with `run file.pcraft`, edit layers by **id** from `info`.
- `batch`: an actions file is a JSON list of `[id, params]` steps (`[["image.imageSize",{"width":300}],
  ["filter.blur.gaussianBlur",{"radius":2}]]`); output name = input name with the new extension; the summary line says
  `N succeeded, M failed`. An `--out` folder equal to `--in` is refused (`--in-place` overrides).
- `convert --quality` for JPEG/WebP prints `warning: lossy compression`.

## Commands that worked (exact parameter formats)

- Fill: `layer.newFillLayer.gradient {"from":"#1F3864","to":"#2E75B6","angle":90,"style":"linear"}` (with angle 90
  the `to` colour ended at the TOP), `layer.newFillLayer.solidColor {"color":"#rrggbb"}`.
- Shapes: `shape.create {"kind":"rect|roundedRect|ellipse|polygon|star|line","rect":[x,y,w,h],"radii":24,"fill":"#F2F2F2"}`
  → `{layer,bounds,…}`; `shape.edit`, `shape.info`, `shape.rasterize`.
- Type: `type.create {"x":90,"y":160,"text":"…","font":"Arial","size":36,"color":"#1F3864"}` (x,y = baseline anchor in
  px; paragraph text with `"box":[x,y,w,h]`); returns the layer id and bounds.
- Layer style: `layer.layerStyle.dropShadow {"color":"#000000","opacity":60,"distance":8,"size":12}` applies to the
  active layer (the one just created) or `{"layer":id,…}`. Other styles exist as `layer.layerStyle.*`.
- Adjustment layers: `layer.newAdjustmentLayer.hueSaturation {"hue":0,"saturation":10,"lightness":0}`,
  `…brightnessContrast {"brightness","contrast"}`; ids for the other 14 via `commands --filter newAdjustmentLayer`.
  Destructive versions: `image.adjustments.levels|desaturate|brightnessContrast`.
- Layer props: `layer.setProps {"layer":4,"opacity":0.6,"name":"Sun","blend":"Multiply","visible":true}`
  (opacity is 0–1 here; drop-shadow opacity is 0–100). Select: `layer.select {"name":"Sun"}`; delete:
  `layer.delete {"layer":id}`; reorder: `layer.moveTo {"layer":id,"target":id,"position":"above|below|into"}`.
- Image: `image.imageSize {"width":400}` (keeps aspect: 800×500 → 400×250), `image.canvasSize`,
  `image.crop {"x","y","width","height"}`, `filter.blur.gaussianBlur {"radius":2}`, `filter.sharpen.sharpen {}`.
- Selection (UNVERIFIED, signatures from `commands --json` only, not yet run): `select.rect {"x","y","width","height","feather"}`,
  `select.subject {}`, `edit.fill {"contents":"color","color":"#rrggbb"}`.

## Traps

- **Flattening is silent except for one warning line:** exporting to PNG/JPG/WebP drops layers. Always also save a
  `.pcraft` if the user may edit again.
- A command that takes `"layer"` uses the numeric id from the earlier `run` output or `info`, and ids are not
  reused after deletes: re-read `info` before targeting a layer in a long chain.
- Automation is fail-closed: commands that read or write arbitrary paths (`file.open`, `file.saveAs`, …) are refused
  over MCP/control; use `doc_open`/`doc_save` MCP tools or the CLI `--out`.
- 935 commands exist; do not guess ids: `commands --json --filter <word>` and read the `params` string
  (ranges and defaults are in it, e.g. `"radius":0.1..1000=1`).

## Verify before reporting

`photocraft-cli info out.pcraft --compact` (layer list, kinds, bounds) and look at a rendered PNG: the first
gradient test would have looked fine in `info` but had its colours the wrong way round.

## Recipes

- Card with shadow and caption (800×500): gradient fill → `shape.create` rounded rect → `layer.layerStyle.dropShadow`
  → `type.create` → `hueSaturation` adjustment → `--out card.png` (rendered correctly).
- Batch thumbnails: `batch` with `image.imageSize {"width":300}` over a folder, `--format jpg --quality 85`.

## Log

- 2026-10-24: Initial notes: CLI run/info/convert/batch, layers kept in .pcraft/.psd, shapes, type, drop shadow,
  adjustment layer, resize/crop, JPEG/WebP/PSD export (photocraft-cli 0.15.1, Linux).
