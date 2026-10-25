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

- 2026-10-24: Second background-removal run with a dense, grid-read trace + smooth/contract: IoU vs a good reference
  95.9% → 98.1%, collar and edges fixed; hair strands still not reproduced.
- 2026-10-24: Live mode via the control bridge; background removal on a blurred-background portrait (lasso +
  refineEdge → layer mask; auto selections failed); mask fill colour trap.
- 2026-10-24: Initial notes: CLI run/info/convert/batch, layers kept in .pcraft/.psd, shapes, type, drop shadow,
  adjustment layer, resize/crop, JPEG/WebP/PSD export (photocraft-cli 0.15.1, Linux).
- 2026-10-25: everyday-edits table (crop/resize/rotate/adjustments/denoise/sharpen), selection→mask, watermark, batch webp, format support verified headless.
- 2026-10-26: live bridge session (doc_open, command_batch steps, screenshot), paint/filters/content-aware fill, silent-unknown-param trap verified.
- 2026-10-26: retouch (heal/clone/dodge/burn), selective colour, gradient map, clipping, saved selections, liquify, smart filters, perspective crop, layer comps, quick export verified.
