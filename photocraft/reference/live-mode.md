# PhotoCraft reference: live mode

Part of the photocraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

> Not re-checked: the live bridge, window tools and AI selection below (the headless CLI was re-run; see `everyday-edits.md`, "Newer commands and options").

## Live mode and removing a background (verified on a portrait with a blurred, busy background)


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

## Live session and wider toolbox (verified)


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

## Live UI tools: pointer, tools, straighten, remove, perspective crop (verified live, app on port 47825, 2026-10-26; screenshots checked)
> The window must be visible and the screen unlocked. Test photos: a landscape with a clear sky, a hillside with a sloping tree line, power lines over a field, a phone photo of a framed certificate on a dark blanket, a wide-angle building, prints lying on a wooden table. No photo content is recorded here.
- **Paths for the live tools:** `doc_open {"path":"/abs/file"}` needs an ABSOLUTE path (`~` is not expanded: "automation read … NotFound"). `doc_save`, like `doc_open`, works under the app's read/write roots (here the Pictures folder): **a `doc_save` aimed at a scratch name saved into the user's photo folder**: use a name you delete afterwards, or a subfolder meant for results. `doc_new {"width","height","background"}` → `{document}`; the new document becomes the active tab.
- **`ui_set {"fields":{"tool":"Name","brushSize":14}}`** switches tool (an unknown name answers "unknown tool `x`" without listing the valid ones). Tool names that WORK: Move, Lasso, MagneticLasso, QuickSelection, MagicWand, ObjectSelection, Crop, PerspectiveCrop, Slice, Eyedropper, ColorSampler, Ruler, Note, Count, SpotHealing, Healing, Patch, ContentAwareMove, RedEye, Remove, Brush, Pencil, MixerBrush, CloneStamp, PatternStamp, HistoryBrush, Eraser, BackgroundEraser, MagicEraser, Gradient, PaintBucket, Blur, Sharpen, Smudge, Dodge, Burn, Sponge, Pen, FreeformPen, CurvaturePen, Type, VerticalType, DirectSelection, Rectangle, Ellipse, Line, Polygon, CustomShape, Hand, Zoom, Artboard, Frame. **NOT valid:** Marquee, RectangularMarquee, EllipticalMarquee, PolygonalLasso, HealingBrush, Path, Rotate (try other spellings). Other `ui.set` fields are listed in the tool description (zoom, center, theme, crop overlay, eyedropper sample…); an unknown field is an error.
- **`ui_pointer {"events":[{"kind":"down|move|up","x","y","pressure"?}]}`** sends document-pixel events to the ACTIVE tool; the reply is only `{status}` (the status-bar text, often stale: ignore it), so verify by `ui_inspect` (`document.history`, `measurement`, `selectionBounds`) or a screenshot. Every stroke needs a `down`, a few `move`s and an `up`; a straight wire needs ~15 interpolated points. **`ui_screenshot {"max_side":800}`** is how you see the result; screenshots are numbered by call order in the helper's output (`/tmp/pcshot_<call>_0.png`).
- **Commit with a key:** `control_call {"method":"ui.key","params":{"key":"Enter"}}` → `null` commits the Perspective Crop (and presumably Crop/transforms); `ui.commit`, `ui.apply`, `ui.confirm`, `ui.press` do not exist. `control_call` with `ui.menu.list` returns the whole menu tree (105 KB, saved to a file by the harness); `ui.tools.list` and `document.inspect` are NOT control methods (use `command_run {"id":"document.inspect"}`).
- **Tools exercised by pointer (renders checked):** QuickSelection stroke over a sky selected the whole sky down to the horizon. **`select.sky {}` (command) selected only 68% of the image and left out the deep-blue upper-left corner of the sky** (`{bounds:[0,0,1280,464],coverage:0.68}`; marching ants cut diagonally): check its result or fix with QuickSelection. Gradient tool drag from corner to corner made a "Gradient Fill 1" layer in the colours set by `tools.setColors`; Brush strokes on a new layer (`layer.new.layer` first) with `pressure:0.1…1…0.1` made a tapered stroke; Lasso with 5 points made a selection; Rectangle drag made a "Rectangle 1" shape layer in the foreground colour.
- **Straighten with the Ruler (verified):** `ui_set tool Ruler`, drag along the line that should be level (`down` start, a few `move`, `up` end) → the line is stored (`ui_inspect` → `document.measurement.ruler {start,end}`; `image.analysis.info` → `ruler.info {angle:-9.1762,length,w,h}`), then `image.analysis.straightenLayer {"crop":true}` → `{angle,cropped:true,height:667,width:1512}` from 1600×900: the canvas is rotated by the angle and cropped to the picture, the tree line came out level. **The ruler line is consumed**, so `image.analysis.recordMeasurements` afterwards says "no ruler line to measure": record first.
- **Remove and Spot Healing by pointer:** `ui_set {"tool":"Remove","brushSize":14}` then one stroke along a power line (document px) removed the wire in ~0.5 s (`jobs_list` → `paint.remove … state:"done", result.damage`); a faint trace and a small dark spot remain at the stroke start. **Remove is an asynchronous job: the next stroke fails with "command `paint.spotHealing` is not available right now: “Remove” is still running on this document" until `jobs_list` shows it `done`** (poll or wait ~1 s). `SpotHealing` (size 16, a 17-point stroke) cleared a pair of wires, leaving a faint dotted trail where the lines were.
- **Perspective Crop by pointer (verified, with a mistake corrected):** `ui_set {"tool":"PerspectiveCrop"}`, then four click pairs (`down`+`up` at each corner, document px, quad shown with a grid) → `ui.key Enter` → history shows "Perspective Crop". **My first attempt cut off the left of the page and showed background below it: I had read the corners off a shrunken screenshot (tens of px off) and in the wrong order.** Do not eyeball corners: find them from the pixels with `tools/pagecorners.py` (below), pass them to `image.perspectiveCrop {"corners":[tl,tr,br,bl],"width","height"}` (same result as the tool, exact), and LOOK at the result: straight, parallel page borders mean the keystone is gone.
- **Perspective crop of a tilted page (verified on a phone photo of a framed certificate, 2170×1636 result):**
  1. `photocraft-cli convert photo.jpg upright.png` — **phone JPEGs carry an EXIF orientation tag (here 6: stored 4032×3024, shown 3024×4032). PhotoCraft applies it, PIL does not**: any pixel measurement made on the raw file lands in the wrong frame (my first detection put the box in empty blanket).
  2. `python3 -I tools/pagecorners.py upright.png` (PIL only) → four corners, the four side lengths and `overlay.png`; open the overlay and check the red quad hugs the page on ALL four sides. **It must be the page's true quad, not a rotated box: my second attempt used the minimal-area rotated rectangle around the page, which only rotates it, so the result looked warped (a keystone/trapezoid distortion remained; the page was photographed at an angle and the near side is longer: sides 2066/2169 and 1450/1634 px).** The script now fits a straight line along each side of the page's OUTER silhouette (inner dark lines such as a printed border must not count: with every mask edge the quad hugged the inner border and cut off the left) and intersects neighbouring lines.
  3. Order the corners for an UPRIGHT page: top-left is the corner where the text starts and the page top is (work out the reading direction from the text; this page's text ran up-left, so the order was bottom, left, top, right corners). A wrong order gives a page rotated by 90° or 180° (fix with `image.imageRotation.90cw|90ccw|180`).
  4. `image.perspectiveCrop {"corners":[…]}` (width/height omitted = the mean of the opposite sides: 2117×1542 here; pass them only to force a paper ratio) also works on the live document via `command_run`. Verified result: the page upright, borders parallel and straight, the four corner shapes the same size, no background left or cut off. **`Perspective Crop` (tool or command) IS the trapezoid/keystone correction**: it maps any convex four-corner quad onto a rectangle.
- **`file.automate.cropAndStraightenPhotos {}`** (`command_run` on the active document) → `{photos:[{angle,center,document,height,width}]}` and a new "… copy 1" document per found photo. **It found ONE "photo" (the whole 604×400 image, angle 0) for six prints lying on a wooden table**: it needs prints on a plain, uniform scanner background; it cannot separate prints from a textured table.
- **`filter.lensCorrection {"profile":"generic","distortion":40,"vignetteAmount":30}`** (headless `run` on the JPEG) → `{profile:"Generic Lens (50 mm equivalent)",scale,layer,ms}`; on a wide-angle building photo `+40` straightened the bowed roofline and `-40` with `autoScale:true` bowed it more; look at the roofline/horizon, there is no automatic profile from EXIF here (`"profile":"auto"` was not run).
- **Housekeeping after live tests:** each opened photo stays as a tab, modified ones show a dot: tell the user to close them WITHOUT saving (my edits were on the open copies; the files on disk are untouched). Remove any scratch file saved to the Pictures folder.

## More live tools: marquees, polygon lasso, crop, pen, type, move, clone stamp (verified live, 2026-10-26)
> Live bridge (`ui_set`, `ui_pointer`, `control_call`), results read back with `command_run {"id":"document.inspect"}` (history names, `selectionBounds`, layer list) and screenshots. Test images: a landscape photo and a blank 500×350 document.
- **Tool names that fix the earlier "not valid" list:** `RectMarquee`, `EllipseMarquee`, `SingleRowMarquee`, `SingleColumnMarquee`, `PolygonLasso`, `PathSelection`, `RotateView`, `ColorReplacement`, `MoveTool` are accepted. **`Ellipse` selected the Elliptical Marquee here** (history "Elliptical Marquee", no shape layer), while `Rectangle` earlier made a shape layer: check `document.inspect` → `history` after the first stroke with a tool name you have not used before; the history label is the real tool.
- **`selectionBounds` is `[x, y, width, height]`:** a RectMarquee drag from (100,60) to (500,300) gave `[100,60,400,240]`, an EllipseMarquee drag (700,100)→(1000,300) gave `[700,100,300,200]`; `hasSelection:true`, history "Rectangular Marquee"/"Elliptical Marquee".
- **PolygonLasso:** one click pair (`down`+`up`) per vertex, the last click on the first vertex closes it → history "Lasso", `selectionBounds [200,330,250,150]` for a 4-vertex shape.
- **Crop tool:** `ui_set tool Crop`, drag (150,50)→(1150,500) on a 1280×555 photo, `ui.key Enter` → history "Crop", canvas 450 px high (the drag area). Remember the commit key.
- **Pen tool:** `ui_set tool Pen`; click pairs add corner points and a `down … move … up` drag pulls out smooth handles; `ui.key Enter` finishes: `path.list` → `workPath {knots:4,subpaths:1}`, history "Work Path" (the blue outline shows on the canvas).
- **Type tool:** `ui_set tool Type`, click at the position (a text box starts), then **`control_call {"method":"ui.type","params":{"text":"Hello"}}`** typed the text and created a type layer named "Hello" (history "New Type Layer", `type.info` → bounds, `lines[…].end:5`); `ui.text` is not a method. `ui.key` with a letter (`H`, `i`) did NOT append characters to the text (it stayed 5 characters), and `ui.key Escape` ended the edit with the Type tool still active.
- **Move tool:** a drag of (+150,−50) from a point on the type layer moved that layer by exactly that (type bounds `[63,225,175,262]` → `[213,175,325,212]`; history "Move"); with `move_auto_select` the layer under the pointer is picked.
- **Clone Stamp with Alt-click:** `ui_pointer {"modifiers":{"alt":true},"events":[click at the source]}` → status "Clone source set at 100, 100"; the following stroke gave history "Clone Stamp"; `cloneSource.list` then showed `source [100,100]`, `anchor [300,100]`, `offset [-200,0]`, and `layer` = the active layer: select the target layer first (`layer.select {"name":"Background"}`).
- **MagicWand/PaintBucket:** a click on a flat white canvas selected all of it, and the bucket filled the whole canvas with the foreground colour (history "Magic Wand", "Paint Bucket"): they behave on pixels, so check which layer is active (the type layer was above and invisible when the same colour was used).
