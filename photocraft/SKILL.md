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
  (Live mode verified: see the section below.)
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
- Selection: `select.lasso`, `select.refineEdge`, `select.subject`, `select.object`, `select.focusArea`, `select.quick`,
  `edit.fill {"contents":"black|white|color","layer":id,"target":"pixels|mask"}` all ran live: see the background-removal
  section for which ones worked. `select.rect {"x","y","width","height","feather"}` is still unrun.

## Live mode and removing a background (verified on a portrait with a blurred, busy background)

Live mode: the app must be started with `--control PORT --control-token-file FILE --automation-read-root DIR
--automation-write-root DIR` (the user runs it); then the MCP tools `command_run`, `command_batch`, `doc_save`,
`ui_screenshot` work on the open document. **`session_list` in bridge mode returns the app's entire UI state
(~10 KB of JSON): call it once, then use `ui_screenshot {"max_side":800}` and `command_run` results instead.**
`ui_screenshot` is how you SEE the picture; `render_preview` in bridge mode is only the same window screenshot.
To inspect pixels closely, `doc_save` a flattened PNG under the write root, crop it with Python and open the crop
(delete the check file afterwards). The `--automation-*-root` folders confine all file access.

Removing a background, non-destructively:
1. `layer.duplicate {"name":"Cutout"}` first; never edit the original layer.
2. Automatic selections FAILED on this photo (sharp subject, heavily blurred coloured background):
   `select.subject {}` selected the background, not the person; `select.object {"rect":[x,y,w,h]}` cut through
   the face; `select.focusArea` gave patchy strips; `select.quick` with positive then `mode:"subtract"` strokes
   flipped the result. Each returns only `bounds`: **always look at a screenshot, `bounds` can look plausible and be wrong.**
3. What worked: trace the silhouette yourself with `select.lasso {"points":[[x,y],…],"mode":"replace","feather":0}`
   (document pixels, ~20 points; convert from a screenshot with doc_px = (screen_px − canvas_left) × doc_width /
   canvas_width_on_screen), then
   `select.refineEdge {"radius":6,"smartRadius":true,"smooth":8,"feather":1,"contrast":20,"output":"layerMask"}`
   → the layer gets a mask and the selection is consumed (`select.deselect` then fails with "no selection").
   Hide the original with `layer.setProps {"layer":2,"visible":false}`; the checkerboard shows the cut.
4. Check edges on a contrasting colour: `layer.newFillLayer.solidColor {"color":"#2E75B6"}` then
   `layer.moveTo {"layer":4,"target":2,"position":"above"}` (between background and cutout), export a crop.
   Loose traces leave wedges of old background beside the neck and along shoulders.
5. Fix wedges by painting the MASK, not the pixels: `select.lasso` the wedge, then
   `edit.fill {"contents":"black","layer":3,"target":"mask"}` (black hides, white shows).
   **`edit.fillForeground` with `target:"mask"` painted WHITE (the foreground swapped to white when the mask became
   active) and revealed the wedge instead of hiding it: use `edit.fill` with an explicit `contents`.**
6. Inspect EVERY edge, not only the head: after the first pass a dark wedge of background was still left between the
   sleeve and the image border (the user spotted it; I had only checked head and neck). Export the backdrop-coloured
   composite and crop all four sides and the shoulders at 1:1. A lasso with `feather:1` filled black on the mask removed it.
7. Colour fringe / halo (orange bleed on the edge, dark rim) after the mask exists: shrink the mask edge.
   `select.loadSelection {"channel":"mask","layer":3}` → `select.modify.contract {"radius":3}` →
   `layer.layerMask.delete {"layer":3}` → `layer.select {"layer":3}` → `select.refineEdge {"radius":1.5,"smooth":6,
   "feather":0.8,"output":"layerMask"}`. The orange fringe disappeared. **`select.refineEdge` writes the mask to the
   ACTIVE layer, not the one you loaded from: after helper layers were added the active layer was the backdrop fill,
   so the mask landed there (`"layer":4` in the reply). Always `layer.select` the target first and check the
   `layer` in the reply; `edit.undo` reverts it.** A thin dark rim that remains may just be dark hair.
8. **Compare against a known-good cutout when the user has one (what the gap looked like):** extract its silhouette
   (flood-fill the near-white background from the corners with PIL, subject = everything else, so a white shirt is
   kept), scale it onto yours by bounding box and draw a difference map (red = only mine, green = only the
   reference). The overlap was 96%, so outlines were right; the visible faults were NOT in the shape but in edge
   quality (check both with side-by-side crops of neck/collar and hair, on white and on a contrasting colour):
   - a polygon lasso leaves straight stepped segments along jaw and shoulders and a pale sliver where it cut the
     background short: use many more points on curves, then `select.modify.smooth` or refine `smooth`;
   - a wedge fill meant to remove background can bite off real collar or neck (the reference showed a missing
     slice of collar): confirm against the photo before filling the mask black;
   - a hair edge from a lasso is a hard "helmet" with a dark rim; the good result keeps soft edges and single
     stray hairs. A hair-aware pass was tried and FAILED: `select.refineEdge {"radius":10,"smartRadius":true,
     "decontaminate":true,"refineStrokes":[{points along the hairline,"size":45,"mode":"add"}],"output":
     "newLayerWithMask"}` smeared the hair and left ghost shapes (revert: `layer.delete` the new layer). Do not repeat
     it on a blurred dark background; try small radius on the contracted selection (step 7) and accept slightly
     smooth hair, or ask the user whether an AI-generated cutout (as in their reference) is acceptable.
   - the reference was an AI-regenerated image (1024², face and clothing re-rendered, not the same pixels), so use it
     to judge quality and outline, never to copy pixels or masks from.
9. Deliver: hide the helper fill layer, `doc_save {"path":"x.png"}` (RGBA, transparent corners confirmed) and
   `doc_save {"path":"x.pcraft"}` (keeps layer + mask). Never overwrite the source photo.
Hair detail against a dark blur is the weak spot: a traced edge is smooth and slightly hard; `smartRadius` softens it.

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

- 2026-10-24: Live mode via the control bridge; background removal on a blurred-background portrait (lasso +
  refineEdge → layer mask; auto selections failed); mask fill colour trap.
- 2026-10-24: Initial notes: CLI run/info/convert/batch, layers kept in .pcraft/.psd, shapes, type, drop shadow,
  adjustment layer, resize/crop, JPEG/WebP/PSD export (photocraft-cli 0.15.1, Linux).
