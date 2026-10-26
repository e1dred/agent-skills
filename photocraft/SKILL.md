---
name: photocraft
description: Verified working knowledge for driving the PhotoCraft image editor (storytold/photocraft) from an AI agent: the headless photocraft-cli (convert, info, run, batch), the MCP bridge to a running app, exact command parameter formats, recipes and traps. Load before any PhotoCraft or image-editing task on this machine, and add what you learn at the end of it.
---

# PhotoCraft

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, tested on **photocraft-cli 0.15.1, re-checked and extended on 0.16.0** (Linux AppImage; 0.16.0 is the version for everything dated after 2026-10-25). PhotoCraft is an early-alpha,
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

> **Versions:** 0.15.1 (2026-10-24); the bridge arguments changed in 0.16.0 (see 'Version 0.16.0 notes').

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

> **Versions:** 0.15.1; `run`, `info`, `convert`, `batch` behave the same on 0.16.0 in every pipeline below.

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

> **Versions:** 0.15.1; the same commands appear in the pipelines that were re-run 2026-10-25 on 0.15.1 and 0.16.0.

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

> **Versions:** 0.15.1 app and CLI (2026-10-24). The live bridge was re-verified on 0.16.0 (see 'Version 0.16.0 notes'); `select.subject` was re-tested on 0.16.0 and still fails on this kind of photo.

Helper when the `photocraft` MCP tools are not loaded in the session: `python3 -I tools/pcmcp.py PORT calls.json` (see its docstring) runs the same tool calls through the bridge from the shell and saves screenshots.
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

### Better method, measured (second run on the same photo: overlap with the reference 95.9% → 98.1%)

Use this order instead of steps 2–5 above; it fixed the neck/collar, fringe and wedge problems in one pass:
1. Read the ORIGINAL file (under the read root) with PIL, not window screenshots: write gridded crops (yellow vertical /
   cyan horizontal lines every 25–50 px, labels every 100, scale 1.3–2.7×) of the head, both jaw sides, collar,
   both shoulders and both lower edges, view each, and read edge points in document pixels
   (doc = box_origin + shown_px / scale). ~70 points were enough.
2. `layer.duplicate`, then ONE `select.lasso` with all points (`feather:0`), `select.modify.smooth {"radius":2}`,
   `select.modify.contract {"radius":1}` (heavier values 4/2 also work but pull the edge in; see the comparison below).
3. `layer.select` the cutout (the duplicate), then `select.refineEdge {"radius":1.5,"smooth":6,"feather":0.8,
   "output":"layerMask"}`; hide the original; `doc_save` a transparent PNG and a `.pcraft`.
4. Score and look: silhouette overlap with the reference, and close-up crops on a contrasting colour. Result: no
   orange fringe or dark rim, the collar kept, smooth jaw and shoulder curves; remaining flaws were a thin pale sliver
   along one jaw edge and hair without any flyaway strands (the lasso edge is smooth). Fixing the hair needs a different
   technique than anything tried here.
Shrink/smooth settings compared (same dense trace, same refine; three layers in one document, one mask each, by
`select.saveSelection {"name":"raw"}` once and `select.loadSelection {"channel":"raw"}` + modify + refine per layer, always
`layer.select {"name":…}` the target before refining): tight (smooth 4, contract 2) IoU 0.9813, light (smooth 2,
contract 1) 0.9818, loose (no modify) 0.9821; mask area differs only 0.7%, and no variant showed a colour fringe at 2×.
So with an accurate trace use LIGHT (smooth 2, contract 1) or none; the heavier shrink was only needed for the
loose first trace (about 8 px off), where it hid the fringe. The user noticed the marching-ants selection sat
slightly "inside" the subject: that is the contract plus smoothing rounding convex curves inward.
The user A/B-flipped the tight and light results by switching tabs: the light one was "very slightly better, almost
imperceptible", matching the 0.7% area difference: the accurate trace, not these settings, made the big difference.
Ready-to-reuse scoring: flood-fill the reference's near-white background (all channels ≥ 241) from the 4 corners,
subject = the rest, crop to its bbox, resize to your alpha bbox, then intersection-over-union.
(Without numpy, PIL's `ImageChops` + `ImageDraw.floodfill` do it.)

### Watch for AI selection (not available yet)

photocraft-cli 0.15.1 has NO AI commands (`commands --filter ai`, `segment`, `neural` return nothing relevant); `select.subject`
is classical. The Craft AI layer (https://github.com/storytold/craft-ai-integrations, Apache-2.0/MIT, "first draft") contains
SAM 2.1/SAM 3 engines and a ComfyUI `image.segment` role that would give real subject selection. When a newer PhotoCraft
exposes it, re-test the portrait background removal above before using the manual lasso method.

## Everyday photo edits (verified headless, 0.15.1)

> **Versions:** 0.15.1 (2026-10-25); re-run 2026-10-25 on 0.15.1 and 0.16.0 (crop, exposure, vibrance, levels, curves, denoise, sharpen, resize; masked adjustment + type; rotate/canvas/photo filter/place/blend/mask/shape/stroke): **pixel-identical** output and identical layer lists.

Run a whole retouch in one go: `photocraft-cli run photo.jpg --cmd ID --params JSON … --out out.jpg` (an opened JPEG is the
background `Pixel` layer, id 2). Commands that return `null` succeeded. Parameter docs: `commands --json` (each item has
`id` and `params`; ranges and defaults are in the string).

| Goal | Command + params |
|---|---|
| crop | `image.crop {"x":100,"y":50,"width":1000,"height":700}` (also `angle`, `targetWidth/Height`, `contentAware`) |
| resize | `image.imageSize {"width":800}` (keeps aspect; or `percent`, `resample`) |
| canvas / borders | `image.canvasSize {"width":820,"height":1280,"anchor":"center","extensionColor":"#ffffff"}` → `{offset}` |
| rotate / flip | `image.imageRotation.90cw|90ccw|180|flipCanvasHorizontal|flipCanvasVertical` (no params) |
| exposure | `image.adjustments.exposure {"exposure":0.3,"offset":0,"gamma":1}` |
| brightness/contrast | `image.adjustments.brightnessContrast {"brightness":-150..150,"contrast":-50..100}` |
| levels | `image.adjustments.levels {"inBlack":8,"gamma":1.1,"inWhite":245,"outBlack":0,"outWhite":255}` (per channel under `red/green/blue`) |
| curves | `image.adjustments.curves {"points":[[0,0],[64,56],[192,200],[255,255]]}` (0..255 pairs; `red/green/blue` per channel) |
| vibrance / saturation | `image.adjustments.vibrance {"vibrance":30,"saturation":5}`; `…hueSaturation {"hue","saturation","lightness"}` |
| warm/cool | `image.adjustments.photoFilter {"filter":"warming85|cooling80|sepia|…","density":20}` |
| B&W | `image.adjustments.blackWhite {}` (channel mixers `reds`…`magentas`), `…desaturate`, `…threshold {"level":128}` |
| shadows/highlights | `image.adjustments.shadowsHighlights {"shadowAmount":35,"highlightAmount":0}` |
| denoise / noise | `filter.noise.reduceNoise {"strength":4}`, `filter.noise.addNoise {"amount":12.5,"distribution":"gaussian"}` |
| sharpen | `filter.sharpen.unsharpMask {"amount":80,"radius":1.2,"threshold":2}`, `…smartSharpen {"amount","radius","reduceNoise"}` |
| blur | `filter.blur.gaussianBlur {"radius":2}`, `…motionBlur {"angle","distance"}` |

Non-destructive versions are `layer.newAdjustmentLayer.<name>` with the same parameter names; destructive ones are `image.adjustments.*`.

**Selection → mask (verified, render checked):** make a selection first and a new adjustment layer takes it as its mask:
`select.rect {"x":300,"y":200,"width":600,"height":400,"ellipse":true,"feather":40}` then
`layer.newAdjustmentLayer.hueSaturation {"saturation":-80}` → the layer reports `hasMask:true`; the effect applies inside the feathered
ellipse only. Other selection ids: `select.colorRange`, `select.grow`, `select.modify.feather {"radius"}`, `select.inverse`, `select.deselect`.
For an existing layer: `select.rect …` then `layer.layerMask.revealSelection` (or `hideSelection`, `revealAll`, `hideAll`, `delete`, `apply`).

**Watermark / logo:** `file.placeEmbedded {"path":"/abs/mark.png","scale":100,"center":[700,1200]}` → a Smart Object layer; then
`layer.setProps {"blend":"Overlay","opacity":0.8}`. Text: `type.create {"x":40,"y":770,"text":"© Studio","font":"Arial","size":28,"color":"#ffffff"}`.
Shape + stroke: `shape.create {…}` then `layer.layerStyle.stroke {"color":"#ffffff","size":3}`.

**Output formats checked:** `.jpg/.webp` (lossy warning, `--quality`), `.png`, `.tiff` (2.9 MB for 1200×800), `.psd` (layers kept, DPI warning),
`.pcraft`. **AVIF cannot be written** ("unsupported: AVIF cannot be written in this build"). `batch --actions act.json --in DIR --out DIR2
--format webp --quality 80` → "N succeeded, M failed".

Live mode needs the app started with `--control 47821` plus the token file; it was not running this session, so live recipes
are still unverified.

## Version 0.16.0 notes (2026-10-25)

> **Versions:** 0.16.0 (2026-10-25).

- App 0.16.0 needs the **0.16.0 `photocraft-cli`** for the live bridge. With the old 0.15.1 CLI against the 0.16.0 app, authenticated
  bridge calls timed out after 55 s ("app was not drawing frames") and the bridge never worked; the 0.16.0 CLI (extracted from the new
  AppImage: `./photocraft.appimage --appimage-extract`, binary at `squashfs-root/usr/bin/photocraft-cli`) answered at once.
- **Bridge flags changed:** `photocraft-cli mcp --bridge PORT --control-token-file FILE` — `--automation-read-root/--automation-write-root` are now
  *refused* with `--bridge` (set the roots on the desktop app instead: start it with `--control PORT --control-token-file FILE
  --automation-read-root DIR --automation-write-root DIR`). Roots stay valid for headless `mcp`.
- A raw JSON-line client on the control port answers "authentication required" without the right handshake; use the MCP bridge.
- Verified live on 0.16.0: `doc_new`, `command_run` (`layer.newFillLayer.gradient`, `type.create`), `ui_screenshot`, `jobs_list`.
- **AI selection re-tested on 0.16.0** (portrait, dark suit, blurred green/yellow background): `select.subject {}` → `{bounds:[0,0,1225,1494],changed:true}`; rendered over magenta via
  `layer.duplicate` → `select.subject` → `layer.layerMask.revealSelection` it **kept the left-hand plants, the lamp and the face but removed the whole dark suit and the right half** —
  still wrong (same failure class as 0.15.1). Keep using the manual `select.lasso` + `select.refineEdge` method below. Judge any cutout by compositing over a loud colour
  (`layer.newFillLayer.solidColor {"color":"#ff00ff"}` then `layer.moveTo {"layer":id,"target":cutoutId,"position":"below"}`); transparent and a dark suit both look black on a PNG viewer.
- **`type.fillPath {"layer"?:id,"shape"?:layerId}`** (verified): wraps a type layer's text inside a shape layer's outline (default: the work path) → `{layer,subpaths}`.
  Make a paragraph type layer with `"box":[x,y,w,h]` first; the text re-flows to the ellipse (top-aligned, ragged to the outline); keep the shape layer.
- **Style presets as ASL** (verified): `style.presets.list {}` → groups (Basics 8, Text Effects 7, Buttons 6 = 21 built-ins);
  `style.presets.exportAsl {"path":"x.asl","group"?,"styles"?}` → `{count:21,bytes,patterns,warnings}` (31 KB);
  `style.presets.importAsl {"path":"x.asl","group":"Name","replace":true}` → imports 21; a name clashing with a built-in group gets " 2" appended, built-ins are never replaced.
  `help.checkForUpdates {}` / `updates.status {}` take no params.
- New commands in 0.16.0: `type.fillPath`, `style.presets.importAsl/exportAsl`, `help.checkForUpdates`, `updates.status` (935 → 940). Nothing removed; every recipe
  above (crop, curves, unsharp mask, resize, saves) gave the same results on both CLIs. `select.subject/object/focusArea/quick` parameter docs are unchanged.

## Live session and wider toolbox (verified, 0.16.0)

> **Versions:** 0.16.0 only (2026-10-25); live bridge session, not re-run on 0.15.1 (its bridge needs the matching CLI).

**Live bridge session (MCP server `photocraft` → app on 47825):** `doc_open {"path":"~/Pictures/x.png"}` (under the read root) → `{name,path,warnings}`;
`command_batch {"steps":[{"id":…,"params":…},…]}` (the argument is **`steps`**, not `commands`) → `{completed,failed,results:[{ok,result}]}` (one history step each);
`command_run {"id","params","wait"?}`; `ui_screenshot {"max_side":700}` (returns an image); `jobs_list {}`; `doc_save`/`doc_export` write under the write root.
A seven-step batch (duplicate layer, vibrance, high-pass, Overlay blend, radial gradient fill as a Multiply "Vignette", brush stroke) ran with 0 failures and the screenshot showed the Layers panel updated.
- **Edits land on the *active* layer.** A `paint.stroke` right after `layer.newFillLayer.*` painted that fill layer's *mask*, not pixels, so nothing showed. Select or create a pixel layer first
  (`layer.new.layer {"name":"Paint"}` or `layer.select {"name":…}`), or use `"target":"pixels"` where offered.
- High-pass on a duplicate set to Overlay (the sharpening recipe) looks flat grey in the Layers thumbnail; that is normal.
- The live document becomes dirty; the user's file is untouched until `doc_save`. Do not save over the user's source image — export a copy.

**Unknown parameter names are silently ignored** (unlike GridCraft/DeckCraft, which error): `select.modify.expand {"pixels":6}` returned `{selected:true}` but used the default radius 1 — the parameter is `radius`.
Always read the `params` doc from `commands --json` and confirm the effect.

Headless batch checked on a photo: `select.colorRange {"select":"sampledColors","color":"#c89670","fuzziness":60}` → `select.modify.expand {"radius":6}` → `edit.contentAwareFill {}` (→ `{filled:186639,…}`) →
`filter.stylize.oilPaint {}` (stylization 4, cleanliness 5, scale 1, lighting true) → `filter.distort.spherize {"amount":30,"mode":"normal"}`, all ok. Other families present (counts in 0.16.0): `paint.*` 26 (`paint.stroke {"points":[[x,y,pressure?…]],"size","hardness","opacity","color"}`,
`paint.pencil`, `paint.bucket {"x","y","tolerance","color"}`, `paint.gradient {"from":[x,y],"to":[x,y],"style","colors"}`, mixer brush, magic eraser), `filter.stylize` 9, `filter.distort` 9, `filter.noise` 5, `filter.other` 7
(`highPass {"radius"}`), `filter.render` 9 (`clouds`, `lensFlare`, `pictureFrame {"frame":"…"}`), `channel.*` 22, `layerComp.*` 14, `history.*` 13, `brush.*` 17.

## Retouching, compositing and selections (verified headless on a portrait, 0.16.0; renders checked)

> **Versions:** first run on 0.16.0 (2026-10-25); the heal/clone/dodge/burn/selective-colour/gradient-map/clipping pipeline and the saved-selection pipeline were also run on 0.15.1: pixel-identical.

Each ran on a copy of a 1600×1600 portrait; every command returned `ok` and the final renders looked right.
- **Heal / clone / dodge / burn** paint on the *active pixel layer* with `points:[[x,y],…]`: `paint.spotHealing {"points","size":40,"type":"contentAware","sampleAllLayers":true}` → `{damage:[x,y,w,h]}`;
  `paint.cloneStamp {"points","size":60,"source":[900,1200],"sampleLayer":"currentAndBelow"}` (→ `offset`, `aligned`); `paint.healingBrush` takes the same `source`/`offset`;
  `paint.dodge|burn {"points","size":120,"range":"shadows|midtones|highlights","exposure":20}`. Do dodge/burn on a duplicate of the Background (`layer.select {"name":"Background"}` → `layer.duplicate {"name":"Dodge&Burn"}`) to stay non-destructive.
- **Colour**: `layer.newAdjustmentLayer.selectiveColor {"colors":"blues","cyan":-20,"black":10}`, `…gradientMap {"stops":[[0,"#1a1a40"],[1,"#ffd9a8"]]}` then `layer.setProps {"blend":"SoftLight","opacity":0.4}`;
  destructive `image.adjustments.replaceColor {"color":"#3a8fd8","fuzziness":50,"hue":-90,"saturation":10}` (also `matchColor {"source":docIndex,…}`).
- **Clipping**: `layer.createClippingMask {"layer":id}` clips that layer to the one below it (`clipped:true` in `info`); `layer.releaseClippingMask`.
- **Saved selections as channels**: `select.rect {…,"ellipse":true,"feather":20}` → `select.saveSelection {"name":"Face"}` → `{channel:0}` (alpha channel in `info.channels.alpha`), later
  `select.loadSelection {"channel":"Face","invert":true}` (+ `"operation":"add|subtract|intersect"`). Verified: brightness −40 on the inverted selection, then an Exposure adjustment layer with the
  non-inverted selection (it becomes that layer's mask) lifted the face and darkened the surroundings.
- **Liquify**: `filter.liquify {"strokes":[{"tool":"bloat|forwardWarp|pucker|twirlCw|smooth|reconstruct…","size":80,"points":[[800,520]],"pressure":50}]}` → `{changed,maxDisplacement}`.
- **Smart objects / smart filters**: `layer.smartObjects.convertToSmartObject {}` → `{layer}`; a following filter (e.g. `filter.blur.gaussianBlur`) becomes a smart filter; edit it with
  `layer.smartFilter.setParams {"index":0,"params":{"radius":2}}`. `image.perspectiveCrop` rasterizes smart objects (the layer came back as a plain Pixel layer) — do it first or keep a copy.
- **Perspective crop**: `image.perspectiveCrop {"corners":[tl,tr,br,bl],"width":800,"height":1000}` maps the quad onto an upright canvas (all layers, one undo step).
- **Layer comps**: `layerComp.new {"name":"Soft"}` → `{comp}`, `layerComp.apply {"comp":"Soft"}`, listed in `info.layerComps`.
- **Quick export**: `file.export.quickExport {"path":"/abs/out.jpg"}` → `{path,format,bytes,warnings}` (format by extension; honours Export Preferences). `layer.quickExportAsPng {"layer","path"}` for one layer.
- Remaining unverified: `paint.mixerBrush`, `filter.cameraRaw`, Actions recording/`.atn` playback via the app, `droplet`, panorama/HDR merges.

## Next-tier workflows (verified headless, 0.16.0; renders checked where noted)

> **Versions:** 0.16.0 (2026-10-25). Camera Raw, lens correction and tilt-shift were also run on 0.15.1 (pixel-identical). Layer-style stacking, modes/formats, Actions/droplets, contact sheet, content-aware scale and path text were run on 0.16.0 only.

**Layer styles stack with `"add":true`** (without it a new style call replaces the layer's effects). Verified on a type layer over a gradient (render checked):
`layer.layerStyle.stroke {"size":4,"position":"outside","color":"#0b1d3a"}` → `…outerGlow {"color":"#ffd966","opacity":70,"size":24,"spread":10,"add":true}` →
`…bevelEmboss {"style":"inner","depth":120,"size":6,"add":true}` → `…dropShadow {"distance":10,"size":12,"opacity":55,"add":true}`; also `innerShadow`, `colorOverlay`, `gradientOverlay {"from","to","style":"linear|radial|…","angle"}`.
Gradient fill on pixels: `paint.gradient {"from":[0,0],"to":[900,420],"style":"linear|radial|angle|reflected|diamond","colors":["#1F3864","#2E75B6"]}`; patterns: `pattern.list`, `edit.fill {"contents":"pattern","pattern":"Checkerboard"}`.

**Photo-lab filters:** `filter.cameraRaw {"temperature":15,"exposure":0.3,"contrast":10,"highlights":-30,"shadows":25,"clarity":20,"vibrance":15}` (also texture, dehaze, whites/blacks, point curves per channel),
`filter.lensCorrection {"profile":"generic|auto|none","correctVignette":true,"vignetteAmount":-30,"correctDistortion"…}`, `filter.blurGallery.tiltShift {"blur":12,"angle":0,"focus":0.25}`; colour looks `image.adjustments.colorLookup.list` (Warm Filter, Teal & Orange, Bleach Bypass, Faded Film…) with `layer.newAdjustmentLayer.colorLookup`.

**Modes and output (all verified by `info` of the saved file):** `image.mode.grayscale` → Gray 8; `image.mode.cmyk` → saved TIFF reports CMYK 8 (and back with `image.mode.rgb`); `image.mode.bits16` → depth 16 (TIFF);
`image.mode.indexedColor {"colors":32,"palette":"adaptive"}` → "written as an 8-bit palette PNG (32 colours)"; `image.imageSize {"width":2400,"resolution":300}` → 2400×1600 at 300 ppi.
`convert in out` options: `--jpeg-format progressive --quality 85`, `--tiff-layers --tiff-compression lzw`, `.webp --quality 80`, `.bmp`, `.tga`, `.exr`, `.pdf` ("saved flattened"); BMP/TGA/PDF drop the DPI with a warning.

**Actions (record, save, replay) and droplets:** in one `run`: `actions.record {"name":"Web look"}` → the commands to record → `actions.stop` (→ `{steps:3}`) → `actions.assignSet {"action":"Web look","set":"My Actions"}` →
`actions.save {"path":"web.atn","set":"My Actions"}`. **`actions.save` with a `set` fails ("no actions in a set named …") unless the action was assigned to that set; with no `set` it saves everything as "PhotoCraft Actions".**
Replay over a folder: `photocraft-cli batch --actions web.atn --action "Web look" --in DIR --out DIR2 --format jpg --quality 85` → "3 succeeded"; replay inside a document: `actions.load {"path"}` then `actions.play {"action"}` → `{ran:3}`.
Droplets: `file.automate.createDroplet {"path":"web.pcdroplet","steps":[["image.imageSize",{"width":400}],["filter.sharpen.unsharpMask",{"amount":60,"radius":1}]],"name":"Web small","output":"DIR","format":"jpg","shim":false}`, run with `photocraft-cli droplet web.pcdroplet in-folder --out DIR`.
Other automation: `file.automate.fitImage {"width":500,"height":500}` (keeps aspect: 1200×800 → 500×333), `file.automate.contactSheetII {"input":"DIR","width":8,"height":6,"columns":3,"rows":1,"resolution":100}` → one document with all pictures,
`file.automate.photomerge {"paths":"DIR","layout":"auto"}` needs REAL overlapping photographs: my synthetic strips failed with "couldn't find enough matching detail" (untested on real photos).

**Transforms and type:** `edit.contentAwareScale {"width":800}` scales the *layer content* (bounds `[0,0,800,800]`) and leaves the canvas size unchanged, so crop or `image.canvasSize` afterwards; `edit.transform {"scaleX":55,"scaleY":55,"rotate":-8,"dx":150,"dy":60}` on a duplicated layer makes a tilted "card" you can style;
`type.warpText {"style":"arc|flag|wave|fish|…","bend":45}` (render checked); text on a path: create the shape layer first, then `type.attachToPath {"layer":5,"shape":4,"start":20}` (needs a shape layer id or a work path; the text then runs along the outline). `type.paragraphStyle.new/apply/list` manage reusable paragraph styles.
`timeline.create {"duration":2,"fps":5}` + `timeline.info` work and a `.gif` is written (palette-quantized, 256 colours), but animated *frames* from layer keyframes were not tested.

## Paths and channels (verified headless, 0.16.0; path render checked)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1.

- **Paths:** `path.set {"path":{"subpaths":[{"closed":true,"knots":[[x,y],{"anchor":[x,y],"in":[x,y],"out":[x,y],"smooth":true},…]},{"closed":true,"op":"subtract","knots":[…]}]}}` makes the *work path*
  (plain `[x,y]` knots are corners; a second subpath with `"op":"subtract"` punches a hole). `path.rename {"to":"Arch"}` saves it (`path.list` → `paths:[{name,knots,subpaths}]`).
  `path.fill {"name":"Arch","color":"#2E75B6","opacity":80}` and `path.stroke {"name":"Arch","size":8,"hardness":1,"color":"#C00000"}` paint on the ACTIVE pixel layer (`layer.new.layer` first;
  stroke returns `{damage}`); `path.toSelection {"name":"Arch","feather":3}` then `edit.fill`. Render checked: arch with a cut-out triangle, red outline, soft-edged green copy.
  `path.transform {"name":…,"matrix":[a,b,c,d,e,f]}` rewrites the saved path in place (matrix `[0.5,0,0,0.5,300,200]` scaled it about the origin and moved it).
  Also listed, not run: `path.moveAnchors/moveHandle/bendSegment/convertPoint/addAnchor/deleteAnchor`, `path.clippingPath.set/clear`, `path.style.copy*/paste*`.
- **Channels:** `select.saveSelection {"name":"Alpha A"}` → `{channel:0}`; `channel.duplicate {"channel":"red","name":"Red copy"}` and `channel.new {"name":"Mask B","fill":"white"}` return only the new index;
  `channel.rename {"channel":"Mask B","name":"Renamed"}`; `channel.options {"channel":…,"color":"#00ff00","opacity":40}` returns the whole `channel.list` (`alpha[]` with index/name/colour/opacity/indicates/visible, `colors[]`, `target`).
  **Trap:** `channel.options` made that alpha channel the *target* and hid the composite RGB channels in the live state (`compositeVisible:false`); `channel.target {"channel":"composite"}` or `channel.target.composite {}` restores it. `info.channels` shows the same data.
  Not run: `channel.newSpot/mergeSpot/split/merge/move/delete`, `channel.target.slotN`.

## Brushes and paint tools (verified headless, 0.16.0; render checked)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1.

All on one new pixel layer (`layer.new.layer`), strokes from a sine path, `points:[[x,y,pressure],…]` (pressure 0..1 as the third value):
- `paint.stroke {"points","preset":"Chalk","size":40,"color":"#333333","opacity":0.6,"flow":0.5,"seed":7,"erase":true,"mode":"multiply|…|clear","smoothing","target":"pixels|mask|quickMask|{channel:i}"}` → `{damage:[x,y,w,h]}`.
  Opacity/flow are **0..1 here** but 1..100 in `paint.cloneStamp/dodge/burn/sponge/blur/smudge…` (hardness 0..1 vs 0..100 likewise). `paint.pencil` is the aliased pencil; `"erase":true` with opacity 0.5 halves what is below.
- **Presets:** `brush.presets.list {}` → 36 built-ins (Hard Round, Soft Round, Hard Round Pressure Size, Airbrush Soft, Calligraphy Flat, Hard/Soft Pencil, Chalk, Charcoal, Pastel, …; `tip:"sampled"` ones are textured).
  Render: "Hard Round Pressure Size" tapers with the pressure values (thin ends, fat middle); "Chalk" is grainy and varies with `seed`; "Airbrush Soft" with `flow:0.5` is a soft wide band; a `size` given with a preset overrides its size.
  `brush.presets.save {"name":"My Marker","brush":{"size":22,"hardness":0.8}}` → `{count:37}`, then `"preset":"My Marker"` works in strokes. `brush.get {}` dumps all brush settings (dynamics, dual brush, scattering, mixer, pose, locks…).
  Also listed: `.update/.delete/.setCurrent/.rename/.move`, group commands, `brush.presets.importAbr {"path"}`, `importImage {"path"}`, `brush.defineFromSelection {"name"}`, `brush.texturePattern`.
- **Symmetry:** `paint.setSymmetry {"mode":"vertical","center":[350,0]}` mirrored one stroke into two (verified); `paint.symmetryDisable {}` turns it off (`symmetryFromPath` not run).
- **Other tools run:** `paint.bucket {"x","y","tolerance","color","sampleAllLayers":true}` (→ `{filled}`; with sampleAllLayers a bucket click on an empty paint layer fills by the composite), `paint.magicEraser {"x","y","tolerance"}` → `{erased}`,
  `paint.smudge`, `paint.sponge {"points","size"}`, `paint.colorReplacement {"points","size","mode":"hue"}`: **it paints in the FOREGROUND colour (default black), so my "recolour" turned a red stroke dark grey; pass `"color"` or set the foreground first.**
- **Second batch (render checked):** `paint.mixerBrush {"points","size":90,"wet":80,"mix":60,"load":50,"flow":80,"sampleAllLayers":true}` smeared a red/teal pair of shapes into a gradient but the load colour defaults to the black foreground, so the start of the stroke is a dark smear: `brush.mixer.load {"color":"#e63946"}` first, `brush.mixer.clean {}` after (→ `{amount,color,pickup,reservoir}`).
  `paint.patternStamp {"points","size","pattern":"Checkerboard"}` → `{aligned,pattern:<uuid>,phase}` (the checkerboard looks like a transparency grid). `paint.backgroundEraser {"points","size"}` → `{erased}`.
  **Own brush tip:** `select.rect` over *painted* pixels → `brush.defineFromSelection {"name":"Stamp1"}` → `{width,height}`; it errors "the pixels contain no paint (all white or transparent)" on an empty region. A stroke with `"preset":"Stamp1"` stamps the shape (a solid blob gave a solid bar in the chosen colour).
  `path.set` an open 2-knot line, then `paint.symmetryFromPath {"name":"work"}` → `{enabled:true,segments:1,source}`: a stroke was mirrored across the line (verified).
  `paint.redEye {"x","y"}` errors "no red-eye pixels near the click" on anything that is not red pupils (a correct refusal, not a bug).
- Not run: `paint.patch`, `paint.contentAwareMove`, `paint.remove`, `paint.historyBrush`, `.abr`/`importImage` brushes, real red-eye.

## Filter families, layer comps, history and smart filters (verified headless, 0.16.0; contact sheets checked)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1.

- **Every filter ran with `{}` (defaults) without error: 65 ids** (blur 11 + blurGallery 5, sharpen 5, noise 5, pixelate 7, stylize 9, distort 8, render 6, other 7, video 2) on a flattened 260² test picture (`layer.flattenImage` first; the id is `layer.flattenImage`, not `image.flatten`). Rendered, so each does visibly what its name says:
  - *Barely visible at defaults (raise the parameters):* `blur.blur`, `blurMore`, `boxBlur`, `gaussianBlur` (radius 1), `surfaceBlur`, `smartBlur`, `noise.despeckle/median/dustAndScratches/reduceNoise`, `sharpen.*`, `pixelate.facet`, `distort.zigZag/shear`, `other.custom`, `video.*`.
  - *Replace the picture, not modify it:* `render.clouds` and `render.fibers` (greyscale/foreground-background noise, use a new layer or a selection), `blur.average` (one flat colour).
  - *Surprises:* `other.colorToAlpha` defaults to white → keeps colour on black; `other.hsbHsl` swaps colour channel meaning (hue-shifted look); `distort.polarCoordinates` default is rectangular→polar (circular warp); `pixelate.colorHalftone`/`mezzotint` are loud; `stylize.findEdges/traceContour` give white line-art; `render.lightingEffects`/`relight`/`lensFlare` add light on top.
  - `filter.distort.displace` needs `mapPath` or `mapDocument` ("Displace needs a displacement map"). `filter.render.pictureFrame {"frame":"waves"}` (draws a wavy green border, 445 primitives), `filter.render.tree {"baseTreeType":3}` (a pine, new look per type 1..34), `filter.render.flame {}` (a flame at the work path or the bottom): all return `{bounds,layer,newLayer:false,primitives}` and paint on the active layer.
  - Parameter ranges for a few: `radialBlur {"amount","method":"spin|zoom"}`, `motionBlur {"angle","distance"}`, `lensBlur {"radius","shape":"hexagon|…"}`, `shapeBlur {"radius","shape":"heart|star|…"}`, `crystallize/pointillize {"cellSize","seed"}`, `mosaic {"cellSize"}`, `oilPaint`, `tiles {"count","fill"}`, `wave`, `ripple {"amount","size"}`, `twirl {"angle"}`, `filter.other.offset {"horizontal","vertical","undefinedAreas":"wrap|repeat|transparent"}`.
- **Layer comps:** `layerComp.new {"name":"Red on","comment":"…"}` → `{comp:1}` (id numbers); `layerComp.apply {"comp":"Red on"}` → `{comp,missingLayers}`, `next`/`previous` step, `rename`, `setOptions {"comp","position":false}` (what the comp records: visibility/position/appearance),
  `duplicate` → new id, `reorder {"comp","index"}`, `delete` → `{deleted}`, `list` → `{comps:[{id,name,comment,visibility,position,appearance,layers,missingLayers}],lastApplied}`, `updateWarnings` → `{count,warnings}`, `update {"comp":"*","what":"all"}`.
- **History and snapshots:** `history.newSnapshot {"name":"Snap1","from":"fullDocument"}` → `{snapshot:1,…}` (**snapshot ids start at 1; `snapshot:0` is an error**); `history.selectSnapshot {"snapshot":1}` returns to it as a new state; `stepBackward/stepForward` → `{current,label,states}`;
  `history.selectState {"state":1}` (0 = oldest); `history.setSource {"state":2}` then `paint.historyBrush {"points","size"}` paints back from that state (→ `{damage}`); `history.clear` drops the old states (Edit > Undo restores them).
  **Trap:** `history.newDocument {"name"}` makes the new document ACTIVE, so a following `history.renameSnapshot` on the old document's snapshot fails with "no snapshot 1" (the new document has none). Do snapshot management first.
- **Smart filters:** `layer.smartObjects.convertToSmartObject` (→ `{layer}`, a NEW layer id: a shape layer 3 became 6) then each `filter.*` is a smart filter; `layer.smartFilter.setParams {"index":0,"params":{"radius":3}}` (merged), `blendingOptions {"index":0,"blend":"Multiply","opacity":0.5}`,
  `setVisible {"index":1,"visible":false}`, `move {"index":0,"to":1}`, `delete {"index":1}`, `disableSmartFilters {"enabled":false|true}`; also `deleteFilterMask`, `disableFilterMask`, `clearSmartFilters`, `transfer {"from","to","copy"}`. `info` lists `smartFilters:[{command,params,blend,opacity,visible}]` and `smartFiltersEnabled`.
  `filter.convertForSmartFilters` is refused on a layer that already is a smart object.
- Not run: the 47 `filter.gallery.*` artistic/sketch/texture filters, `filter.filterGallery`, `filter.vanishingPoint`, `filter.adaptiveWideAngle`, `filter.lastFilter`, filter masks, `layerComp.restoreLastDocumentState`, `history.deleteState`.

## Filter Gallery, every layer style, all adjustment layers (verified headless, 0.16.0; contact sheets checked)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1.

- **All 47 `filter.gallery.*` filters ran with `{}`** on a flattened 260² test picture and each looked like its name (artistic: coloredPencil, cutout, dryBrush, filmGrain, fresco, neonGlow, paintDaubs, paletteKnife, plasticWrap, posterEdges, roughPastels, smudgeStick, sponge, underpainting, watercolor;
  brush strokes: accentedEdges, angledStrokes, crosshatch, darkStrokes, inkOutlines, spatter, sprayedStrokes, sumiE; distort: diffuseGlow, glass, oceanRipple; sketch: basRelief, chalkCharcoal, charcoal, chrome, conteCrayon, graphicPen, halftonePattern, notePaper, photocopy, plaster, reticulation, stamp, tornEdges, waterPaper;
  stylize: glowingEdges; texture: craquelure, grain, mosaicTiles, patchwork, stainedGlass, texturizer). The **sketch family uses the foreground/background colours** (`foreground`/`background` params, default black/white), so on a colour picture they turn it black and white with big areas of white or black (stamp, photocopy, tornEdges, notePaper, plaster, chrome): pass colours or run on a duplicate layer and lower its opacity.
  Parameter docs per filter are in `commands --json` (e.g. `paintDaubs {"brushSize","sharpness","brushType":"simple|lightRough|…"}`, `texturizer {"texture":"canvas|brick|burlap|sandstone","scaling","relief","light"}`, `grain {"grainType":"regular|soft|sprinkles|clumped|…"}`). Texture-style filters add visible mesh at default scale.
- **Layer styles, each alone on a rounded rectangle (render checked):** `layer.layerStyle.` + `dropShadow {"distance":10,"size":12,"opacity":70}`, `innerShadow {"distance":8,"size":10}`, `outerGlow {"color","size":20,"spread":20}`, `innerGlow {"color":"#ffffff","size":20}`, `stroke {"size":6,"color","position":"outside"}`, `colorOverlay {"color","opacity":70}`,
  `gradientOverlay {"from","to","angle":90}` (angle 90: `to` at the TOP), `patternOverlay {"opacity":60}` (default pattern = a checkerboard), `bevelEmboss {"style":"inner","depth":150,"size":10}`, `satin {"opacity":60,"distance":20,"size":25}`. Stack with `"add":true`.
  Also run: `copyLayerStyle {}` / `pasteLayerStyle {}` (to the active layer), `scaleEffects {"scale":200}`, `globalLight {"angle":45,"altitude":50}`, `blendingOptions {"opacity":80,"fillOpacity":50}` (also `blend`, `blendIf`), `hideAllEffects/showAllEffects`, `contours.list {}`.
  **`layer.layerStyle.createLayer {}` turns the effects into real layers** ("Ellipse 1's Drop Shadow", "…'s Stroke") and the original layer loses its effects (`info.layers[].effects` was gone afterwards). `info` lists effects as `effects:{enabled,items:[{kind:"Drop Shadow",enabled}]}`.
  Not run: `replace {"layer","effects":[…]}`, `makeDefault/defaultFor`, `clear {"effect":index}`, `transferEffects {"from","to","copy"}`, the contour save/load commands.
- **All 16 adjustment layers** (`layer.newAdjustmentLayer.` + `brightnessContrast, levels, curves, exposure, vibrance, hueSaturation, colorBalance, blackWhite, photoFilter, channelMixer, invert, posterize, threshold, gradientMap, selectiveColor, colorLookup`): every one runs with `{}` (defaults are a no-op for most; `invert`, `posterize`, `threshold`, `blackWhite`, `gradientMap` visibly change at defaults).
  With parameters each changed the picture (mean pixel difference against the no-op version, 255 scale): colorBalance `{"shadows":[20,0,-20],"midtones":[30,-10,-30]}` 26, channelMixer `{"red":[0,100,0,0],"green":[100,0,0,0],"blue":[0,0,100,0]}` 40 (red/green swap), colorLookup `{"lut":"tealOrange"}` 15 (luts: warm, cool, tealOrange, bleachBypass, fadedFilm, dayForNight, monoContrast, crossProcess),
  blackWhite `{"reds":100,"yellows":100,"greens":0,"cyans":0,"blues":-100,…}` 46, selectiveColor `{"colors":"reds","cyan":60,"magenta":-40}` 5, photoFilter `{"filter":"cooling80","density":50}` 13, hueSaturation `{"hue":120}` 57, levels `{"inBlack":40,"gamma":1.4,"inWhite":220}` 20, curves with a `red` channel curve 21, exposure `{"exposure":1}` 38, gradientMap 26, vibrance 9, posterize `{"levels":3}` 34, threshold `{"level":90}` 124, brightnessContrast 43.
  Most also accept `"path"` (work path or saved path name) to make the adjustment's **vector mask** from a path; otherwise an active selection becomes the layer mask.

## Type, transforms, swatches, smart objects, vector masks, video, view and preferences (verified headless, 0.16.0; renders checked)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1. Colours and texts are invented.

- **Type** (render checked): `type.create {"x","y","text","font","size","color","name","align","orientation":"vertical","box":[x,y,w,h]}` (box = paragraph text, **overflow is clipped** at the box height). Character/paragraph formatting in one command: `type.setStyle {"range":[0,6],"color","weight":700,"italic":true,"underline":true,"tracking":100,"leading":28,"baselineShift","caps":"small|all","baseline":"superscript","fauxBold","features":{"ss01":1},"variations":{"wght":650},
  paragraph keys "align":"justify","firstLineIndent":24,"startIndent","spaceBefore","spaceAfter":6,"hyphenate":true}` → full layout (`lines`, `paragraphs`, `bounds`). `type.edit {"replace":{"start":0,"end":9,"text":"Body copy"}}` (styles kept), `type.insertText {"text":" [added]","at":9}` → `{caret}`, `type.pasteLoremIpsum {}`, `type.info {}`, `type.hitTest {"x","y"}` → `{index,line,inside}`, `type.fonts {}` (installed families), `type.convertToParagraphText/PointText`.
  OpenType: `type.openType.standardLigatures|fractions|ordinals|oldstyle|swash|…  {"on":true}` → `{feature:"liga",on:true}` (Arial has no frac/ordn/onum glyphs, so nothing changed visibly: the call succeeds anyway; use a font that has the feature).
  Styles: `type.characterStyle.new {"name":"Hot","attrs":{"size":22,"color":"#E63946","weight":700}}` → `{id,name}`, `.list`, `.apply {"id"}`; same for `type.paragraphStyle.*` (`attrs {"align":"left","spaceAfter":10}`, id 0 = Basic Paragraph).
  Conversion/effects: `type.createWorkPath {}` → `{subpaths:12}`, `type.convertToShape {}` (type → shape layer, keeps the look), `type.warpText {"style":"flag","bend":40}`, `type.createSelection`, `type.antiAlias.*`, `type.attachToPath`/`fillPath` (earlier section).
- **Transforms:** `edit.transform {"scaleX":150,"scaleY":100,"rotate":15,"dx":40,"dy":10}` (scale/rotate about the frame centre, then move; a plain shape layer stays editable as a shape), `{"quad":[[x,y]×4]}` (clockwise from top-left) distorts to a trapezoid (works on a smart object), `{"matrix":[a,b,c,d,e,f]}`; `edit.transform.flipHorizontal/Vertical`, `rotate90Cw/Ccw`, `rotate180` take `"target":"pixels|mask|…"` and return the rect.
  **`edit.transform.again` / `againCopy` fail headless with "the last transform can't be repeated"** (they replay a transform made in the live app). `edit.transform.warp {"style":"arc","value":40}` on a smart object → `{changed,layer,rect}` (render: the star arched), `layer.smartObjects.perspectiveWarp {"planes":[{"src":[[x,y]×4],"dst":[[x,y]×4]}]}` and `puppetWarp {"pins":[{"src","dst"}],"mode"}` need the ACTIVE layer to be a smart object ("not available right now" otherwise).
- **Swatches:** `swatches.list {}` → groups (Grays …, 46 swatches); `swatches.add {"color":"#0E7C86","name":"Brand teal"}` or `{"color":{"model":"cmyk","values":[80,20,0,10]}}` → `{group,index,name}` (lands in the first group); `swatches.newGroup {"name":"Brand","swatches":[…]}` → `{moved:2}`, `rename`, `renameGroup`, `use {"swatch","target":"foreground"}` (→ `{hex}`; the next `paint.stroke` painted in it), `delete`, `reset {}`.
  `swatches.export {"format":"ase","path":"brand.ase","group":"Brand"}` → `{bytes:132,count:2}` (ASE keeps groups; `.aco` "has no groups; saved as one list", 48 swatches), `swatches.import {"path":"brand.ase"}` → creates group "Brand 1" (a clashing name gets a number). Paths relative to the working folder in the CLI.
- **Smart objects:** `convertToSmartObject` → `{layer}` (a NEW id), `newSmartObjectViaCopy`, `replaceContents {"path":"swap.png"}` → `{instances:[7],warnings:[]}`, `exportContents {"path":"exp.png"}` → `{bytes,converted,fileName}`, `convertToLayers {}` → `{group:false,layer,discardedSmartFilters}`, `rasterize`, `stackMode.median` / `stackMode.none` → `{stackMode}`.
  **`convertToLinked {"path":"linked.png"}` failed with "the smart object's contents are unavailable (missing linked file?)"** on a fresh smart object made from a shape layer (twice); `editContents`/`saveContents` need a window. Not run: `relinkToFile`, `updateModifiedContent`.
- **Vector masks:** with a work path set (`path.set`), `layer.vectorMask.add {"name":"work"}` → `{density,enabled,feather,layer,linked,path}`; `edit {"feather":8,"density":90}`, `linked {"linked":false}`, `enabled {"enabled":false}`, `info {}`, `delete` (→ null), `hideAll` (empty path, `inverted:true`), `revealAll`, `currentPath {"name":"work"}`, `fromPath`.
- **Video layers:** `layer.videoLayers.newBlankVideoLayer {}` → `{layer}`, `insertBlankFrame` → `{frames:2}`, `duplicateFrame` → `{frames:3}`, `rasterize` → `{rasterized:true}`. Footage commands (`newVideoLayerFromFile`, `replaceFootage`, `interpretFootage`) were not run.
- **View:** `view.newGuide {"orientation":"vertical","position":100,"color":"cyan"}` (also `"1in"`), `moveGuide {"index","position"}`, `clearGuides`, `view.newGuideLayout {"columns":3,"gutter":10,"rows":2}` → `{horizontal:4,vertical:6}` (guide counts), `setRulerOrigin {"x","y"}`/`resetRulerOrigin`, `view.colorSamplers.add {"x","y"}` → `{index,point:{rgb,cmyk}}` (max 10) + `.list`,
  `view.proofSetup.colorBlindnessProtanopia {}` (→ `{proof,proofColors:true}`; also deuteranopia, working plates), `view.proofColors {"on":false}`, `view.gamutWarning {"on":true,"threshold":4}` → `{fraction,outOfGamut}`, `view.layerMask {"mode":"off|gray|overlay"}`, `view.lockSlices`, `view.clearSlices`.
- **Preferences** are readable as JSON: `edit.preferences.general {}` → `{section,title,values:{…}}` (e.g. `alwaysCreateSmartObjectsWhenPlacing:true`), `edit.preferences.export {}` → `{jpegQuality:85,quickExportFormat:"png",webpLossless:true,convertToSrgb:true…}`; 18 sections (interface, tools, fileHandling, performance, unitsAndRulers, type, …). Setting them was not tested.

## Layer management, edit and file/export commands (verified headless, 0.16.0)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1. Test pictures were invented.

**Step-by-step on one file:** `photocraft-cli run f.pcraft --cmd id --params '{…}' --out f.pcraft --in-place` (without `--in-place`: "the result would replace the original"). **The layer SELECTION is saved in the `.pcraft`**, so a following run starts from it; the clipboard is NOT (per process), so copy and paste must share one `run`.
- **Layers:** `layer.renameLayer {"layer","name"}`, `layer.setLabelColor {"color":"red"}` → `{changed,layers}`, `layer.arrange.bringToFront|sendToBack|sendBackward|bringForward|reverse` (`sendToBack` on the lowest layer: "layer can't move further"), `layer.translate {"layer","dx","dy"}`,
  `layer.groupLayers {"layer","name"}` → `{layer:<group id>}`, `layer.new.groupFromLayers`, `layer.ungroupLayers`, `layer.setExpanded {"expanded":true,"all":true}`, `layer.lockLayers {"layer","position":true,"transparency":true}` → `{layers:1}`, `layer.toggleLockTransparency`, `layer.hideLayers/showLayers`, `layer.showOnly {}` (⌥-click eye; second call restores),
  selection helpers `layer.selectTop|selectBottom|selectAbove|selectBelow|addAboveToSelection|addBelowToSelection` → `{layer,selected:[…]}`, `layer.pickAt {"x","y"}`, `layer.selectInRect`, `layer.mergeLayers` (one layer = merge down), `layer.mergeVisible`, `layer.stampVisible` → `{layer}` (a merged copy on top), `layer.new.layerViaCopy` → `{layer}` ("Rectangle 1 copy"),
  `layer.new.layerFromBackground {"ifPresent":true}`, `layer.new.backgroundFromLayer`, `layer.delete.hiddenLayers` → `{deleted}`, `layer.rasterize.shape|allLayers|layerStyle|vectorMask` (each says why it can't run: "layer has no vector mask", "no selected layer has layer effects").
  Align/distribute need a multi-layer selection: `layer.align.leftEdges {"to":"layers"}` → `{moved}`; `layer.distribute.*` "select three or more layers"; `layer.linkLayers` "select two or more"; `layer.selectLinkedLayers` only when linked.
- **Masks and shapes:** `layer.layerMask.hideAll|revealAll {"layer"}`, `enabled {"enabled":false}`, `linked {"linked":false}`, `edit {"density":80,"feather":5}`, `layer.toggleMaskOverlay {"layer"}` → `{mode:"overlay"}`, `layer.maskAllObjects {}` → `{bounds}`; `layer.layerMask.apply/fromTransparency` and `layer.matting.defringe|removeBlackMatte|removeWhiteMatte|colorDecontaminate`, `layer.removeBackground` **only on pixel layers** (a Fill or Shape layer answers "not available right now: … is a Fill layer, not a pixel layer"; rasterize first).
  `layer.combineShapes.unite|subtractFrontShape|intersectShapeAreas|excludeOverlappingShapes|mergeShapeComponents`, `layer.rasterize.shape` → `{layer}`. `layer.layerContentOptions {}` → `{editor:"shape"}`, `layer.xmpMetadata {"layer"}` → `{rawData}`.
- **Artboards and frames:** `layer.new.artboard {"rect":[0,0,300,200],"name":"A1"}` (the name did not stick on the second call: it came out "Artboard 1"), `layer.artboard.addBeside {"side":"right"}` → `{layer,rect:[400,0,300,200]}`, `layer.new.frame {"x","y","width","height","shape":"ellipse"}` → `{frame}`; all appear as Group layers. `layer.newLayerBasedSlice` on an empty layer: "the layer is empty".
- **Edit:** `edit.copy`/`copyMerged` → `{bounds}`, `edit.pasteSpecial.pasteInPlace` → `{layer,offset:[0,0]}`, `pasteInto {"center":[420,260]}` → new layer with `offset`, `pasteOutside`; "the clipboard is empty" when pasted from another process. `edit.purge.clipboard|histories|undo|videoCache|all` (refuse when empty).
  `edit.definePattern {"name":"Tile1"}` (from the selection) → `{info:{id,width,height,inLibrary:true}}` (only in that process), `edit.defineBrushPreset {"name"}` → `{width,height}`, `edit.defineCustomShape {"name","path":"work"}` needs a path or shape layer, `edit.fillBackground`, `edit.fillForegroundPreserve`, `edit.fillBackgroundPreserve`, `edit.deleteAndFillSelection` → `{filled,layer,window}`, `edit.fillHistory`.
  Colour: `edit.profileInfo {}` → `{builtins:[srgb, display-p3, adobe-rgb-compat, prophoto-compat, linear-srgb, rec2020…]}`, `edit.installedProfiles {}` (scans /usr/share/color/icc etc.), `edit.assignProfile {"profile":"display-p3"}`, `edit.convertToProfile {"profile":"srgb"}` → `{bpc:true,intent:"relative",mode,profile}`, `edit.colorSettings {}`.
  `edit.findAndReplaceText`/`edit.checkSpelling` "the document has no type layers" otherwise; `edit.presets.presetManager {"action":"list","kind":"patterns"}` → `{patterns:[Checkerboard, Diagonal Lines, Dots, Grid, Bricks, Weave, Paper Noise]}`; `edit.toggleLastState`, `edit.redo` ("nothing to redo"). Not run: `edit.autoAlignLayers/autoBlendLayers` (need overlapping photos), `edit.keyboardShortcuts/menus/toolbar`, `edit.presets.exportImportPresets/migratePresets`.
- **Export family:** `file.export.artboardsToFiles {"dir","format":"png","prefix"}` → `{files:["out/ab/ab_0000_A2.png",…]}` (numbered, **topmost artboard first**), `artboardsToPdf {"path"}` → `{pages:2}`, `layerCompsToFiles {"dir","format":"jpg"}` (`Untitled_0000_One.jpg`), `layersToFiles {"dir","format","prefix"}` (one file per layer incl. Background, `{files,skipped}`),
  `file.export.presets.save {"name":"Web","settings":{"format":"webp","quality":80}}` / `.list` / `.get` / `.delete` (full settings come back: embedProfile, resample, scale, metadata…), `file.export.saveForWebLegacy {"preset":"PNG-24","path"}` → `{bytes,width,height}`, `file.export.colorLookupTables {"path":"look.cube","size":17}` → a 3D `.cube` LUT of the visible adjustment layers (**needs at least one adjustment layer**, else "no visible adjustment layers"),
  `file.export.pathsToIllustrator {"path":"p.ai","paths":"work"}` → an EPS-style `.ai` with BoundingBox, `file.export.exportPreferences {}` (reads the Export prefs), `file.saveACopy {"path":"copy.jpg","quality":8}` (a copy; warns about flattening and lossy; the open document stays bound to its own file), `file.package {"dir"}` → `<dir>/<Name>/<Name>.pcraft`.
  Scripts: `file.fileInfo {"title","author","description"}` (→ full info block incl. `copyright`, `camera`), `file.scripts.deleteAllEmptyLayers` → `{deleted}`, `flattenAllLayerEffects` → `{flattened}`, `flattenAllMasks` → `{flattened,skipped}`, `file.scripts.loadFilesIntoStack {"paths":[…]}` → `{document:1,layers:3}` (a NEW document with each file as a layer),
  `file.scripts.imageProcessor {"input":[files],"output":"dir","format":"jpg","quality":8,"resize":{"width":60}}` → `{files,errors}`, `file.scripts.statistics` needs `"input"` (files or a folder), not run further.
- Not run: `file.openAs/placeLinked/closeAll`, printing, EXR parts, HDR/lens-correction automation, `file.generate.imageAssets`, `layer.copyToDocument`, `layer.new.artboardFromGroup`.

## Image commands, selections, tools, actions, timeline and type styles (verified headless, 0.16.0)

> **Versions:** 0.16.0 (2026-10-25), CLI only; not re-run on 0.15.1. Pictures were synthetic. Step-by-step form: `photocraft-cli run f.pcraft --cmd id --params json --out f.pcraft --in-place` (the layer selection and the selection are saved in the file; the clipboard and tool state are not).

- **Image (destructive):** `image.autoTone|autoContrast|autoColor {}`, `image.adjustments.equalize|invert|posterize {"levels"}|threshold {"level"}|hdrToning {}` (all return `null`), `image.rotation.arbitrary {"angle":5,"direction":"cw"}` → the new size (`{width:425,height:334}` from 400×300: the canvas grows), `image.imageRotation.180|90ccw|flipCanvasHorizontal|flipCanvasVertical`, `image.trim {"basedOn":"transparent|topLeft|bottomRight"}` → `{x,y,width,height}`, `image.revealAll` → `{changed}`, `image.duplicate {"name":"copy","mergedOnly":true}` → `{document:1,name}` (a second document), `image.detectFaces {}` → `{faces:[{score,rect}]}` (empty on a synthetic picture).
  Modes: `image.mode.bits32|bits8` (null), `image.mode.lab` → `{profile:"Lab D50 identity (PhotoCraft)",intent,bpc}`, `image.mode.multichannel` → `{channels:["Cyan","Magenta","Yellow"]}` and back with `image.mode.rgb` → `{converted:"channels",from:"multichannel"}`; **`image.mode.duotone` "needs a Grayscale image"**: `image.mode.grayscale` first. Not run: `bitmap`, `colorTable`, `image.trap` (CMYK).
  `image.calculations {"source1":{"layer":"merged","channel":"red"},"source2":{…"blue"},"blending":"multiply"}` → `{channel:0}` (a new alpha channel); `image.applyImage` needs a pixel layer ("active layer is a Group"). Not run: `image.adjustments.matchColor`.
- **Measurement and notes:** `image.analysis.setMeasurementScale {"pixelLength":100,"logicalLength":10,"units":"cm"}` → `{factor:0.1,text:"100 pixels = 10.0000 cm"}`, `image.analysis.rulerTool {"start":[10,10],"end":[110,10]}` → `{info:{length:10.0,angle,w,h,units}}`, `recordMeasurements {"source":"ruler"}` → `{rows:[{id,values}]}`, `placeScaleMarker {}` → `{bar,group,label:"5 cm"}` (adds layers), `image.analysis.info {}`;
  `notes.add {"x","y","text","author"}` → `{index,note}`, `notes.list`, `notes.set {"index","text"}`, `notes.delete {"index"|"all":true}` → `{deleted,remaining}`; `image.variables.define {"defs":[]}` / `image.applyDataSet {"name"}` for variable data (earlier section).
- **Selections:** `select.all|deselect|inverse`, `select.reselect` ("no selection to restore" until one existed and was dropped), `select.magicWand {"x","y","tolerance":32}`, `select.similar {"tolerance"}`, `select.modify.border {"radius":6}` → `{selected:true}`, `select.transformSelection {"rect":[x0,y0,x1,y1]}` → `{changed,selected}`, `select.magneticLasso {"points":[≥3 fastening points]}` → `{points:41,selected:true}` (it snaps to edges, so the 4 given points became a 41-point outline),
  `select.toWorkPath {"tolerance":2}` → `{subpaths:2,knots:18}` (`path.list` then shows `workPath`), `select.convertToShape {"tolerance":2}` → a new shape layer (fill black, kind path), `select.loadLuminosity` → `{selected:true}`, `select.editInQuickMaskMode {"on":true|false}` → `{quickMask}`, `select.sky {}` → `{changed:false,message:"No sky was detected"}` on a non-sky picture, `select.float {"dx","dy","copy"}` (needs a layer with pixels) + `select.drop` → `{dropped}`,
  layers: `select.allLayers` → `{selected:2}`, `select.findLayers {"name":"Ellipse"}` → `{selected:[3]}`, `select.deselectLayers`, `select.isolateLayers {"on":true}` → `{isolated:true,layers:[4]}`.
- **Tools and colours:** `tools.setColors {"foreground":"#e63946","background":"#1d3557"}` (also `[r,g,b,a]`, `foregroundCmyk`), `tools.swapColors`, `tools.defaultColors`, `tools.setBrush {"preset":"Soft Round","size":60}` (→ the full brush), `tools.increaseBrushSize|decreaseBrushSize|increaseBrushHardness|decreaseBrushHardness`, `tools.nextBrush|previousBrush|firstBrush|lastBrush` → `{preset}` (36 presets, wraps from "Hard Round" back to "Dual Grain"), `tools.rotateBrush {"degrees":30}` → `angle:30`.
- **Actions:** `actions.record {"name":"Glow"}` → …commands… → `actions.stop` → `{action,steps:1}`; `actions.list` → `{actions:[{name,set,steps}],recording}`, `actions.get {"action"}` → `{steps:[[id,params]],disabled,dialogs,color}`, `actions.rename {"action","name"}`, `actions.setColor {"action","color":"blue"}`, `actions.insert {"action","id":"layer.layerStyle.dropShadow","params":{…},"at"}` → `{step,steps}`, `actions.move {"action","step":1,"to":0}`, `actions.toggle {"action","step","enabled":false}` → `{disabled:[0]}`, `actions.dialog {"action","step","enabled"}` → `{dialogs:[1]}`, `actions.stopMessage {"message","allowContinue":true}` → `{continued:true}`, `actions.conditional {"if":"hasSelection","then":"Name","else":null}` → `{holds,played}`, `actions.delete {"action","step"?}`.
- **Timeline:** `timeline.create {"duration":2,"fps":5}`, `timeline.setProps {"fps":10}`, `timeline.setFrame {"frame":3}` (clamped: `current:1` with a 2 s clip at 10 fps was reported), `timeline.nextFrame|previousFrame`, `timeline.delete` → `{timeline:null}`. Each answers `{timeline:{current,duration,fps,time,workStart,workEnd}}`.
- **Type styles and layout:** `type.increaseSize|decreaseSize|increaseSizeMore|decreaseSizeMore {"by":2}` (steps the size; the layout block comes back), `type.antiAlias.none|sharp|crisp|strong|smooth|windows|windowsLcd` → `{antialias}`, `type.orientation.vertical|horizontal`, `type.characterStyle.new {"name","attrs":{"size":40}}` → `{id}`, `.set {"id","attrs"}`, `.apply {"id"}`, `.rename`, `.duplicate` → `{id:2,name:"Hotter copy"}`, `.clearOverride`, `.redefine`, `.delete`; same for `type.paragraphStyle.*` (`attrs {"align":"center"}`);
  `type.caret {"index":3}` → `{line,segment:[[x,y],[x,y]]}`, `type.navigate {"index":3,"move":"wordNext"}` → `{index:5}`, `type.resolveMissingFonts {}` → `{missing:[]}`, `type.saveDefaultTypeStyles` / `loadDefaultTypeStyles` → `{font,size}`, `type.updateAllTextLayers` → `{updated}`, `type.rasterize` → `{layer}`; `type.convertToPointText` on point text: "the type layer is already point text".
- **Layer-style defaults and replace:** `layer.layerStyle.defaultFor {"kind":"stroke"}` → `{params,user:false}`; `makeDefault {"kind","params":{"size":5}}` then `defaultFor` → `{user:true}` **within the same run only** (a new run reported `user:false`: nothing was written to the preferences headless); `layer.layerStyle.replace {"layer":3,"effects":[{"kind":"dropShadow","params":{"distance":6}}]}` → `{effects:1}`, `layer.layerStyle.clear {"layer","effect":0}`, `contours.list` → `{count:0}` (no custom contours). **`layer.layerStyle.transferEffects` needs real layer ids ("no such layer 3")**: after a smart-object conversion the layer ids change (6, 7): read `info` first.
- Not run: `actions.photoshopStep` (needs a `.atn` step), `image.mode.bitmap|colorTable`, `image.trap`, `image.adjustments.matchColor`, `select.magneticLasso` with `trace:false`, `edit.preferences.*` setters, `tools` live pointer tools.

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

## Everyday layer and edit commands, full ids (verified headless, 0.16.0, 2026-10-26; render checked)
> **Versions:** 0.16.0 only. Invented shapes on a 400×300 canvas, one `run`.
- **Layer order and visibility:** `layer.arrange.sendBackward {}` and `layer.arrange.bringForward {}` move the active layer one step (`null`; they undo each other), `layer.hideLayers {}` hides it, `layer.showLayers {}` shows it again (`hideLayers` toggles back when everything targeted is already hidden). Each takes an optional `{"layer":id}`.
- **`layer.mergeDown {}`** merges the active layer into the one below: a star shape merged into an ellipse shape left ONE `Pixel` layer named after the lower layer (the shapes stop being editable); `info` showed `Ellipse 1` as Pixel.
- **`edit.stroke {"width":6,"color":"#000000","location":"center"}`** outlines the active SELECTION on the active layer (a rectangular `select.rect` gave a black frame); `location` is `inside|center|outside`, plus `mode`, `opacity`, `preserveTransparency`. Make a pixel layer first (`layer.new.layer`).
- **`gradient.fill.create {"from":[200,0],"to":[200,300],"style":"linear","stops":[[0,"#ffffff"],[1,"#2a9d8f"]],"opacity":35}`** makes a Gradient Fill layer (`{layer}`); with a selection active the fill layer is masked to it (the render showed the pale teal gradient only inside the selected rectangle). `layer.newAdjustmentLayer.levels {"inBlack":20,"gamma":1.2,"inWhite":235}` → `{layer}` (Adjustment).
- **`edit.copy {}` → `edit.paste {"center":[300,230]}`** must share one `run` (the clipboard is not saved); `edit.copy` needs a layer WITH PIXELS ("the active layer has no pixels" for a shape/adjustment layer: `layer.select` a pixel layer first) → `{bounds}`, then `edit.paste` → `{layer,offset}` (a new layer; 7 layers afterwards).
- **Undo/redo only work inside the run that made the change:** `history.undo {}` / `history.redo {}` (same as `edit.undo` / `edit.redo`) returned `true` after a `shape.create` in the same run, but on a reopened `.pcraft` they fail with "nothing to undo".
- **`image.adjustments.hueSaturation {"hue":60,"saturation":30}`** (destructive; also `lightness`, `colorize`, per-range `reds…magentas`) and **`filter.sharpen.smartSharpen {"amount":120,"radius":1.2,"reduceNoise":20}`** (returns the applied filter parameters) both ran after `layer.flattenImage {}` (one Background layer, new id).

## Slices, preset libraries, count tool, clone source, path editing (verified headless, 0.16.0, 2026-10-26; renders checked)
> **Versions:** 0.16.0 only, CLI only (`run`; a failed command stops the run, so read the last line). Invented shapes on 300–400 px canvases.
- **Slices:** `slice.new {"rect":[0,0,200,150],"name":"Top","kind":"image","url":"…"}` → `{number,slice}`; `slice.divide {"number":1,"horizontal":1,"vertical":2}` → `{count,slices}` (the pieces are user slices, the rest of the canvas stays "auto" slices in `slice.list`); `slice.set {"number":2,"name","alt",…}` (an auto slice is promoted); `slice.promote {"number":3}`; `slice.delete {"number":3}` → `{deleted:1}`;
  `slice.fromGuides {}` replaces every slice with the guide grid (**errors "the document has no guides inside the canvas" without a guide**: `view.newGuide {"orientation":"vertical","position":200}` first) → `{slices:2}`.
- **Gradient presets:** `gradient.presets.list` (group Basics…), `gradient.presets.new {"name","stops":[[0,"#ff5e62"],[1,"#ff9966"]],"transparency"?}` → `{group,name}`, `gradient.presets.apply {"preset","style":"radial","angle":0,"scale","reverse"}` → `{layer}` (a Gradient Fill layer), `gradient.presets.edit {"action":"rename","preset","name"}` (also delete/move/newGroup/renameGroup/deleteGroup), `reset`, `importGrd {"path"}`.
  **`gradient.presets.stop {"action":"add","location":0.5,"color":"#ffffff"}` edits the Gradient tool's CURRENT gradient (it was "Foreground to Background"), not the preset you just made or any layer**; use `gradient.presets.select {"preset"}` first, or edit a layer with `gradient.fill.*`.
  **Gradient Fill layers:** `gradient.fill.create` (earlier) → `gradient.fill.get {}` → `{style,angle,scale,offset,reverse,dither,align,from,to,stops,transparency,midpoints}`, `gradient.fill.set {"angle":45,"reverse":true}` (merges; `from/to` are recomputed from angle), `gradient.fill.stop {"action":"color|add|move|delete|opacity|midpoint","index":1,"color":"#ff0000"}`.
- **Pattern presets:** `pattern.presets.list` (group Geometric… with ids), `pattern.presets.apply {"pattern":"Dots","scale":200,"angle":15}` → `{layer}` (Pattern Fill layer; **it covers the whole canvas, opaque**, so put it below or lower its opacity); `pattern.presets.new {"name":"TmpPat","rect":[0,0,20,20]}` → `{pattern:<uuid>}` (Define Pattern); `pattern.export {"path":"x.pat","patterns":["TmpPat"]}` → `{bytes:530,count:1}`; `pattern.rename {"pattern","name"}`; `pattern.delete {"pattern"}`; `pattern.import {"path":"x.pat"}` → `{imported:[uuid],count}` (same uuid back).
- **Shape presets:** `shape.presets.new {"name":"Tri","path":"M 0 0 L 100 0 L 50 80 Z"}` (the preset path language, or `"work"` / a saved path name) → `{group:"Symbols",name}`; `shape.presets.place {"preset":"Tri","rect":[220,160,120,100],"fill":"#C00000"}` → a shape layer (keepAspect default true: the 120×100 box gave 120×96); `list`, `edit`, `reset`.
- **Tool presets:** `tool.presets.new {"name":"Soft marker","tool":"brush"}` (captures the current brush), `tool.presets.list` (5 built-ins: Soft Round 100 px, Hard Round 12 px, Soft Eraser 60 px, Radial Gradient, Clone Soft 40 px), `tool.presets.select {"preset"}` → `{name,tool,options:{brush:{…}}}`, `edit {"action":"rename|delete"}`, `reset`.
- **Style presets (layer styles):** style a layer (drop shadow + stroke), `style.presets.new {"name":"Card X","group":"Mine"}` → `{effects:2,group}`, then `style.presets.apply {"preset":"Card X","group":"Mine"}` on another layer (render: the ellipse got the same shadow and outline) → `{layers:[5],style}`; `style.presets.edit {"action":"rename",…}`. `path.style.copyFill/copyStroke/pasteFill/pasteStroke` run (null).
- **Count tool:** `count.newGroup {"name","color"}`, `count.add {"x","y"}` → `{number,total,groups}`, `count.setGroup {"name":"Seeds","markerSize":4}`, `count.move {"index":0,"to":[60,60]}`, `count.remove {"index":1}`; `image.analysis.countTool {}` lists the groups. (`count.clear`/`deleteGroup` not run.)
- **Clone source (5 slots):** `cloneSource.set {"index":1,"source":[100,100],"scale":[50,50],"rotation":20}` (selects it), `cloneSource.list` → `{active,sources[5],overlay}`, `cloneSource.overlay {"show":true,"opacity":40}`, `cloneSource.resetTransform {"index":1}` (scale back to 100, rotation 0; the source point stays).
- **Documents:** `document.presets.save {"name","settings":{"width","height","resolution":144}}` / `get` (→ params for `file.new`) / `delete`; `document.recent.list` is empty headless; `document.pixel {"x","y"}` and `document.sampleColor {"x","y","size":5}` return **floats 0..1** `[r,g,b,a]` of the composite (the colour samplers return 0..255 ints); `document.inspect {}` = the `info` block incl. history names.
- **Path editing** (on the work path of a square, then `path.rename {"to":"Blob"}`): `path.addAnchor {"subpath":0,"knot":0,"t":0.5}` (a corner on a straight segment; result has `anchor`), `path.moveAnchors {"anchors":[[0,1]],"move":[0,-40]}`, `path.convertPoint {"subpath":0,"knot":2,"out":[300,120]}`, `path.moveHandle {"subpath","knot","handle":"out","to":[330,90]}`, `path.bendSegment {"subpath":0,"knot":3,"move":[0,40]}`, `path.deleteAnchor {"subpath":0,"knot":4}`, `path.info {}`, `path.clippingPath.set {"name":"Blob","flatness":1}` / `.clear`, `path.delete {"name"}`; then `path.fill` + `path.stroke` painted the edited blob (render: a bulging blue shape with a red outline).
- **Management commands:** `brush.presets.rename {"name","newName"}` (NOT `preset`/`to`), `setCurrent {"name"}`, `update {"name","brush":{"size":30}}`, `delete {"name"}` → `{count:36}`; `view.editGuide {"orientation","index","position","color"}`, `view.deleteGuide {"orientation","index"}` (index per orientation), `view.newGuidesFromShape {}` → `{bounds}`, `view.colorSamplers.move/list/delete`; `swatches.rename/delete {"swatch":name}`; `plugin.list {}` → `{folder:null,plugins:[]}` (no plug-ins installed); `tools.firstBrush/lastBrush` → Hard Round / Dual Grain.
- Not run: `.grd`/`.abr` imports, `count.clear`, `plugin.install/run` (needs a `.wasm`), `slice` export (`file.export.*`), `tool.presets` with a live tool switch.

## Log

- 2026-10-24: Second background-removal run with a dense, grid-read trace + smooth/contract: IoU vs a good reference
  95.9% → 98.1%, collar and edges fixed; hair strands still not reproduced.
- 2026-10-24: Live mode via the control bridge; background removal on a blurred-background portrait (lasso +
  refineEdge → layer mask; auto selections failed); mask fill colour trap.
- 2026-10-24: Initial notes: CLI run/info/convert/batch, layers kept in .pcraft/.psd, shapes, type, drop shadow,
  adjustment layer, resize/crop, JPEG/WebP/PSD export (photocraft-cli 0.15.1, Linux).
- 2026-10-25: everyday-edits table (crop/resize/rotate/adjustments/denoise/sharpen), selection→mask, watermark, batch webp, format support verified headless.
- 2026-10-26: live bridge session (doc_open, command_batch steps, screenshot), paint/filters/content-aware fill, silent-unknown-param trap verified.
- 2026-10-26: retouch (heal/clone/dodge/burn), selective colour, gradient map, clipping, saved selections, liquify, smart filters, perspective crop, layer comps, quick export verified.
- 2026-10-25 (3): layer-style stacking, Camera Raw/lens/tilt-shift, colour modes and formats, Actions (.atn) + droplets + fit image + contact sheet, content-aware scale, transform, warped and path text verified headless.
- 2026-10-25 (5): six pipelines re-run on 0.15.1 and 0.16.0 (pixel-identical); version labels added per section.
- 2026-10-25 (6): paths (set/rename/fill/stroke/toSelection/transform) and channels (new/duplicate/rename/options) verified headless on 0.16.0.
- 2026-10-25 (7): brush presets (list/save/use), pressure strokes, pencil, erase, symmetry, bucket, magic eraser, smudge, sponge, colour replacement verified headless on 0.16.0.
- 2026-10-25 (8): 65 filters rendered on a contact sheet, layer comps, history/snapshots/history brush, smart filters verified headless on 0.16.0.
- 2026-10-25 (9): all 47 Filter Gallery filters, ten layer styles plus copy/paste/scale/global light/create layer, and all 16 adjustment layers verified headless on 0.16.0.
- 2026-10-25 (10): type styles/OpenType/warp/convert, transforms and warps, swatches (+ASE/ACO), smart-object commands, vector masks, video layers, guides/samplers/proof/preferences verified headless on 0.16.0.
- 2026-10-25 (11): layer arrangement/grouping/locking/selection, masks, artboards and frames, clipboard and paste variants, fills, colour profiles, export family (artboards, comps, layers, presets, LUT, Illustrator), file scripts verified headless on 0.16.0.
- 2026-10-25 (12): image auto adjustments/modes/measurement/notes, selection tools, brush tool state, actions editing, timeline, type styles and layer-style defaults verified headless on 0.16.0.
- 2026-10-26: gap round: layer order/visibility/merge down, stroke, gradient fill, copy/paste, undo/redo scope, hue/saturation, smart sharpen, levels adjustment layer named with full ids.
- 2026-10-26 (2): slices, gradient/pattern/shape/tool/style presets, gradient fill layers, count tool, clone source, document presets, path editing, brush/guide/sampler/swatch management verified headless on 0.16.0.
