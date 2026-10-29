# PhotoCraft reference: log

Part of the photocraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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
- 2026-10-26 (3): smart-object linking/export/warp/puppet/stack modes, video layers (GIF) and all remaining preference sections (read-only) verified headless on 0.16.0.
- 2026-10-26 (4): photomerge (4 layouts), HDR merge (5 methods), loadFilesIntoStack, auto-align (5 projections) and auto-blend verified on real HEIC phone photos, 0.16.0.
- 2026-10-26 (5): live UI tools on real photos: ui_set tool names, ui_pointer strokes, ui.key Enter commit, ruler straighten, Remove/Spot Healing, Perspective Crop, quick selection vs select.sky, lens correction, crop-and-straighten limits (0.16.0).
- 2026-10-26 (6): fixed the tilted-page crop (user reported cut-off and background showing): EXIF orientation trap, tools/pagecorners.py, corner-order recipe.
- 2026-10-26 (7): perspective crop corrected again (user: result looked warped): the true page quad from fitted side lines, not a rotated box; pagecorners.py rewritten.
- 2026-10-26 (8): live marquees, polygon lasso, crop, pen, type (ui.type), move, clone stamp with alt-click verified on 0.16.0.
- 2026-10-26 (9): align/distribute, shape combining, rasterize variants, channels, layer comps, destructive adjustments, warps, masks, vector masks, variable data sets, import/export odds verified headless on 0.16.0.
- 2026-10-26 (10): sweep of every remaining command id on a scratch document (355 ran, 22 refused with a reason, 33 skipped on purpose); not rendered.
- 2026-10-26 (11): painted a portrait from code (paths, selection-clipped shading, tapered strokes, oil-paint background); lessons and tools/paintlib.py.
- 2026-10-26 (12): the last 28 command ids run (26 ran or refused with a reason, 2 print commands skipped on purpose; smoke test).
- 2026-10-26 (13): phase 2: 222 smoke-tested ids verified in detail (rendered or read back); see `command-sweeps.md`.
- 2026-10-26 (13): phase 2: 29 smoke-tested ids verified in detail (rendered or read back); see `command-sweeps.md`.
- 2026-10-28 (14): CLI refreshed; 31 outputs (most rows of the everyday table, selection mask, card, shape stroke, type on a shape, style presets exported as ASL, .pcraft/.psd/.jpg/.webp/.tiff) made with the old and new CLI: identical pixels (the .asl file is byte-identical too). Newer commands and options verified headless (see `everyday-edits.md`). Live bridge re-checked (doc_new, command_run, ui_set, ui_pointer, ui_screenshot, jobs_list, doc_inspect, doc_save); AI selection and the older window-tool sections not re-run.
- 2026-10-28 (15): training exercise: non-destructive hero-product retouch (Smart Object and smart filter, hand-built mask, saved alpha channel, masked group, frequency separation with High Pass at 50%, clone-stamp retouch layer, clipped Curves and Hue/Saturation, radial Soft Light vignette); PSD round trip checked; see `workflows-and-tools.md`.
- 2026-10-28 (16): training exercise: restore a small compressed photo to match an AI-enhanced reference with classic tools (aligned pair, cleanup, smooth upscale, fitted 3D LUT, grain, eye tint); results measured and limits recorded; `tools/fitlut.py` added.
