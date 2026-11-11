# Version notes

## 0.24.0 (tested 2026-11-11, from 0.22.0; 0.23.0 was not tested on its own)

Catalogue: **1421 ids** (+488, 0 removed, 134 changed). Regression (5 scripted cases + 5
conversions, 0.22.0 vs 0.24.0): identical apart from the items under "Behaviour".

**443 of the new ids are desktop UI commands** (`"ui": true` in `commands`): `window.*`, `view.*`,
`ui.*`, `file.openRecent1…30`, `align.*` buttons, `select.recall*`, `type.recentFont*`,
`shortcuts.*`, toolbar items. Headless they refuse with
`` `<id>` is a desktop UI command (`ui: true`); start `vectorcraft --control 7979` and use `vectorcraft-cli mcp --connect` ``.
Run them only against a live app (see `cli.md`, "Live app"). Live round on a hidden display:
98 verified, 67 returned data, 113 ran, 156 refused, 9 skipped. Refusals are mostly empty slots
in a fresh profile (`no such user library`, `no such recent file`, `no such recent font`).

### Desktop UI ids that work live (state read back with `inspect_ui`)
- **View:** `view.grid`, `view.rulers`, `view.outline`, `view.artboards`, `view.boundingBox`,
  `view.snapToPoint`, `view.trimView`, `view.presentation`; `view.setZoom {zoom:200}` → zoom 2.0;
  `view.zoomIn/zoomOut`, `view.goToArtboard`, `view.firstArtboard`; `view.goto1…25` jump to views
  saved with `view.saved.new {name, center:[x,y], zoom}`.
- **Align buttons:** `align.horizontalLeft/Center/Right`, `align.verticalTop/Center/Bottom`,
  `align.horizontalVerticalCenter` move the selection (history "Align"). The 8
  `align.distribute*` buttons refused even with two objects selected: use `object.distribute`.
- **Selections:** `select.save {name}` then `select.recall1…25` → `{count}`.
- **Panels and toolbars:** `window.panel.activate|close|dock|float {panel:"layers"}`,
  `window.panel.collapse`, `window.toolbar.new {name}` / `.rename {name, to}` / `.duplicate`,
  `window.taskBar`, `window.helpBar`, `window.toolbarAdvanced`, workspaces.
- **Type buttons** (type selected): `type.bold`, `type.alignCenter/Right`, `type.justifyLeft`,
  `type.applyBullets {bullet:"dot"}`, `type.applyNumbers {numbers:"arabicPeriod"}`, hyphenate.
  `type.italic` after `type.bold` is refused when the family has no Bold Italic.
- **Shortcuts:** `shortcuts.set {id:"view.zoomIn", shortcut:"Cmd+Shift+9"}` switches the set to
  "Custom"; `shortcuts.reset`; `shortcuts.preset {name:"Classic Defaults"}`.
- `addon.pathtools.cornerTool` / `sharedEdgeTool` select those tools with their options.

### New ids that work headless (each read back)
- **SVG filters:** `svgFilter.define {xml:"<filter id=\"f1\">…</filter>"}` → `{name}`;
  `svgFilter.apply {name}` on the selection wraps it in `<g filter="url(#filter-1)">` with the
  filter in `<defs>`; `svgFilter.list`, `svgFilter.delete {name}`, `svgFilter.import`.
- **Spelling:** `text.spelling.check` → `{words, more}`; `text.spelling.suggest {word}` →
  `{suggestions}`; `addWord`, `removeWord`, `changeWord`, `editDictionary`, `ignoreAll`,
  `dictionary` (the user dictionary lives in the app's config folder: use an isolated HOME for tests).
- **Composite fonts:** `type.compositeFonts.set {fonts:[{name, parts:{roman:{font}, kanji:{font}, …}}]}`,
  `.list`, `.export {path}` (`.vccomposite`), `.import {path}`.
- **Style libraries:** `charStyle.load`, `paraStyle.load`, `textStyle.loadAll` copy styles from
  another document → `{added, existing, skipped}`.
- **Scripts:** `script.run {source}` → `{changed, console, log, fuelUsed, hostCalls, dialogs…}`;
  `script.console`, `script.console.clear`, `script.listInstalled` (Scripts folder), `script.stop`.
- **Preferences:** `prefs.export {}` → `{count, data}` (JSON text); `prefs.import {path}` →
  `{imported}`. Trap: `prefs.export {path}` failed with "No such file or directory" for an existing
  folder; export without `path` and write `data` yourself.
- `engine.apiReference` → Markdown reference of every command that has a parameter schema.
- `object.setPixelAligned {ids}` snaps to the pixel grid: a 1 pt-stroked rect at 100,100 exports
  at `x="100.5" y="100.5"`.
- `document.compare {path: png}` compares the artboard render with a PNG → `{rmse, over, total,
  threshold}` (visual regression check).
- **3D assets:** after `effect.apply {effect:"threeD.revolve"}`, `assets.add3D {ids}` →
  `{assets:[id]}`, `assets.set3DFormat {assets, format:"obj"}`, `assets.export3D` writes
  `.obj` + `.mtl`.
- `actionSet.read {path | data}` parses an `.aia` action set without running it → `{set,
  version, actions:[{name, steps}], unread}` (unread lines are listed, so a broken file is diagnosable).
- `symbol.instance.resetTransform {ids}` undoes scaling of an instance (250×120 → 100×80);
  `symbol.instance.selectPart` needs `symbol.options {type:"dynamic"}` first, and a one-shape
  symbol's art is the root path `[]` (`[0]` is refused).
- `text.setPathHandle {id, anchor, which:"in"|"out", x, y}` reshapes the path under type on a path.
- `artboard.rename {index, name}`, `artboard.switchOrientation` (612×792 → 792×612).
- `edit.newDocumentFromState` makes a new document from a history state.
- `plugin.safeMode`, `plugin.setEnabled {id, enabled}`, `plugin.clearCache`, `effect.deferredStatus`.

### Behaviour and parameter changes
- **CMYK display color changed:** CMYK `{c:0,m:60,y:90,k:0}` renders `#f88538` (0.22.0:
  `#f17921`). Exports of CMYK art to SVG/PNG differ by up to 23 per channel.
- **`.ai` save keeps live type** in the editing data: 0.22.0 warned "type is written as its
  outlines"; 0.24.0 has no warning (file 17.9 → 16.3 KB in the test).
- **Artboards:** `artboard.new {side:"right"|"left"|…, beside: index}`,
  `artboard.duplicate {selectedArtboards, side}`; `edit.copy/cut {selectedArtboards}` and
  `edit.paste {artboardsAt}` move artboards with their art (0.22.0 refused these params).
- `select.font {family, style?, scope:{artboards:[…]}}`.
- `text.setFormat` gained `antiAlias`, `listLevel`, `listAlign`, `numbers`, `bullets`, `kinsokuType`.
- `type.insert` gained `code` / `unicode` (insert a character by code point).
- `effect.setParams {index, threeDType: plane|extrude|revolve|inflate}`.
- `print.setup` settings keep `copiesPerSheet`, `gutter`, `tiling` (0.22.0 dropped them silently).
- `prefs.set {documentUnits}`; `document.exportDxf {dxfPreset: "cnc"}` writes AC1015 (default AC1032).
- New result fields: `document.info.patternObjects`, `assets.list[].format3D`, `plugin.list`
  (`safeMode`, `disabled`, `settings`, `permissions`, `commands`), `clipboard.importText`
  (`columns`, `rows`), and `notChanged:{hidden, locked}` on `edit.colors.*`, `paint.invert`,
  `paint.complement`, `recolor.apply`.
- `document.open` documents `importer`, `params`, `legacyNameEncoding` (Shift-JIS/GBK/Big5 names);
  not exercised.
- Trap: 12 appearance/paint/transparency ids mention `exceptions` in their parameter text, but
  `exceptions` is refused as a parameter on both builds. It describes skipped objects only.
- `text.createInPath` returns the path's bounds, not the new type's.

## 0.21.1 (tested 2026-11-05)

Catalogue: **918 ids** (+7, 0 removed, 67 `params` doc strings changed). Regression (5 scripted
cases + 5 conversions, old vs new CLI): identical output apart from the items under "Behaviour".

### New ids (all run headless; see `command-catalogue.md`)
- `addon.document.batchTraceFolder {folder, destinationFolder, preset?, expand?, format?}` — trace
  every image in a folder; never overwrites (`name-2.svg`); non-images are skipped silently; the
  Default preset traces black-and-white.
- `addon.select.byArtboards {artboards:[i…], relation?: overlap|inside|outside}` → `{count}`.
- `addon.type.textTweaker {id, attribute, from, to, shape?}` — ramps one character attribute
  letter by letter (spaces skipped by default); text stays live.
- `select.globalEditExclude {id}` — drop one object from an active Global Edit; it ends when
  fewer than two remain.
- `select.same.textFillAndStrokeColor {}`.
- `text.glyphAlternates {id, start}` / `text.setGlyphAlternate {id, start, gid|null}` — OpenType
  alternates per character (Glyphs panel). Verified by render: Source Sans 3 g→769 and a→710 give
  single-storey forms. A gid not in the list is refused.

### Behaviour and documented-parameter changes
- **8-digit and 4-digit hex colours are refused** everywhere a colour is taken (`#ff000080` →
  `invalid parameters for \`paint\`: bad color`). Use `#rrggbb` plus an opacity parameter.
- `.ai` export now embeds Illustrator editing data (PieceInfo / AIPrivateData; file grew 5.2 →
  9.0 KB in the regression case).
- `document.json` reports `version: 2` (was 1); object structure unchanged.
- Ruler guides: `edit.cut`/`edit.copy` take selected guides along; `edit.clear {guides:true}`.
- Threaded stories: `text.getRange` and `text.setRangeStyle` take `story: true`; `select.all`
  in threaded text selects the whole story; `text.editRange` takes `clear: [ids]`.
- `object.transformEach {relative}`, `file.saveCopy {precision}`.

## 0.21.0 (tested 2026-11-04)

Catalogue: **911 ids** (0.17.0 had 811; 100 added, 0 removed, 142 `params` doc strings changed).
Full diff in `../version-diff.md` and the raw dumps beside it; added ids listed below.

### New: `addon.*` family (59 ids)
Packaged multi-step commands, first seen in 0.21.0:
- `addon.arrange.*` — grid, groupOverlapping, randomizeOpacity, replace, size, sort, swap
- `addon.cleanup.*` — alignInPlace, breakText, check, combineText, deepUngroup, fix, joinText,
  rejoin, removeBreaks, replaceFonts, resetTextTransform, show, simplify, splitText
- `addon.color.*` — applyNearestSwatch, filter, nearestSwatch, printFixes, select, swatchLegend
- `addon.document.*` — exportAllOpen, saveTimestampedCopy, symbolsFromLayers
- `addon.pathtools.*` — addPoints, close, corner, cornerRemove, cornerSet, crossings,
  divideDashes, equalize, erase, expandDashes, extend, inspect, mergeEdge, movePointsTogether,
  removeKeepShape, setAnchor, shape.convert, shape.create, shape.set, slideAnchor, smooth
- `addon.pen.*` — append, close, closeJoin, nextSegment, removePoint, reshape, segment, togglePoint

### New: core commands (41 ids)
- compound shapes: `object.compoundShape.make | .setMode | .release | .expand`
- gradient presets: `gradient.presets.apply | .delete | .list | .save`
- brush libraries: `brush.addFromLibrary | .libraries | .library | .loadLibrary | .saveLibrary`
- symbols: `symbol.exitEditing`, `symbol.instance.reset`, `symbol.instance.setAppearance`,
  `symbol.unused`
- type: `text.convertListToText`, `text.reshapePath`, `text.startList`, `text.thread.break`
- document: `document.exportPresets.export|import`, `document.switchUnits`
- styles: `charStyle.edit`, `charStyle.unused`, `paraStyle.unused`
- image trace: `imageTrace.presets.delete|save`
- view: `view.capsLock`, `view.snapToGlyph.options`
- misc: `artboard.deleteEmpty`, `path.averageJoin`, `select.same.linkBlockSeries`,
  `shaper.releaseSource`, `variable.saveLibrary`

### Documented-parameter changes (142)
Largest: object 31, path 9, text 9, document 8, symbol 8, appearance 7. These are additions to
existing parameters rather than renames; re-read the `params` string of a command before passing
new options. Full list: `../out/ids-changed.txt`.

## 0.22.0 (tested 2026-11-06)

Catalogue: **933 ids** (+15, 0 removed, 16 `params` doc strings changed). Regression (9 scripted
cases, 36 outputs, old vs new CLI): 29 identical. The 7 differences are the document model's
`"version"` 2 → 3 (appearance, shapes, symbols, text, pathfinder), a creation timestamp that moved
by 1 s, PDF sizes +1 byte, `.ai` +280 bytes (Illustrator PieceInfo) and `.eps` +6 bytes; no geometry,
text or paint change.

### New ids (all run headless; see `command-catalogue.md`)
- `addon.shapes.rectangle|ellipse|polygon|star|spiral|box3d` — the scriptable shape tools: `{x,y,width,height,radius,radii,startAngle,endAngle,arcMode,rotation}` for the box shapes, `{cx,cy,radius,sides|points,radius1,radius2,turns,divergence,innerRadius}` for the round ones → `{id}`. Rectangle, ellipse and polygon stay live shapes (`kind.live.shape`, editable with `addon.shapes.configure`); star, spiral and box3d arrive as paths (10, 13 and 12 anchors for the default settings), with the requested extents (a 200×120 rectangle at 100,100 spans x 100-300, y 100-220).
- `addon.shapes.configure {ids, radius|radii, sides, isStar, spokeRatio, turns, divergence, innerRadius, angleX/Y/Z, parallelX/Y/Z, arcMode, reset}` → `{updated}`: `radius:40` gave `radii:[40,40,40,40]`, `sides:8` took a hexagon to 8 anchors, `reset:true` returned the radii to 0.
- `addon.color.fillToStroke` / `addon.color.strokeToFill {ids?|id?, skipNone?}` (Swap Fill and Stroke): each takes the other's paint, leaving width, stroke and other objects alone.
- `addon.contour.set {offset, corners, miterLimit}`: adds a copy above the selection carrying a **live** `path.offsetPath` effect (`{offset:8.0, joins:"round", miterLimit:4.0}`, nothing baked). It takes **no id parameters** - select the paths first.
- `addon.select.byLinkStatus {status, ids?, add?, zoom?}` → `{count, selected, skipped}`: `"linked"` found the placed PNG (id 2), `"embedded"` nothing.
- `addon.type.releasePath {mode?: both|path|text, keepOriginal?, ids?}` → `{ids, paths, texts}`: type on a path became point type (id kept) plus the path (new id).
- `document.move {from?, to}` → `{index}`: moves a document tab; with documents DocA, DocB, moving index 1 to 0 made index 0 read back as DocB.
- `stroke.weightUp` / `stroke.weightDown {ids?|id?}`: step one stroke weight per call (1 → 2 → 3 pt, then back to 2), a quarter unit below 1 pt.

### Changed ids (run headless)
- `addon.pathtools.cornerSet` gained `every: all|odd|even` (and per-item `items`): `every:"odd"` on a hexagon rounded 3 of its 6 corners (`{corners:3}`, 6 → 9 anchors).
- `document.export` and `document.exportSelection` document `ppi` as raster pixels per inch, winning over `scale` (exportSelection gains it): a 612×792 document exported at 1224×1584 at `ppi:144`; a 201×101 selection at 402×202.
- `library.add` adds a plain solid colour with `color`, and keeps a spot swatch with `color` + `swatch` + `tint`: the entry came back as `{name:"SpotTint", hex:"#00aa00", spot:"SpotGreen", tint:0.5}`. `library.get` colours now carry `spot` and `tint`; `library.use {kind:"fillColor", item:"LibGreen", ids}` painted the selection.
- `object.blend.spine.moveAnchor` gained `with: [index…]`: moving anchor 0 of a blend with `with:[1]` created the spine (`subpaths[0].anchors [[100,60],[400,60]]`, `keyAnchors:[0,1]`).
- `text.tabs.set` requires string `align`/`leader`/`alignOn` and refuses an empty `alignOn` ("`alignOn` cannot be empty"); two stops (decimal/"." at 100, centered leader at 200) read back from `text.tabs.get`.
- `path.joinScrub` joins two open paths near each other, or trims two crossing ones and joins at the crossing. **Select the paths first**: without a selection it answers `{id:null}` and changes nothing; with them it returned `{id:2}` and one 3-anchor path.
- `addon.cleanup.removeBreaks` removes the real U+2028: "Line one<U+2028>line two" became "Line one line two" (`{removed:1}`).
- `variable.loadLibrary {path|xml|dataBase64}` replaced an empty document's variables with the saved library's (`variables:["Title"]`).
- `addon.document.batchTraceFolder` traced a folder of one PNG into `.vectorcraft`, `failed: []`.
- `links.findFiles {folder}` answers at once with the search state (`state:"searching"` on a first call); a headless run ends before the thread finishes, so found files were not observed headless.
- `text.convertListToText` answered `{converted:0}` on plain paragraphs; no headless command makes a list paragraph yet, so its effect on a real list was not observed.
- `attributes.set` wrote `url` and `imageMap`, read back by `attributes.info` (URL also joins `recentUrls`); `path.freehand` accepts pressure/tilt points and smooths them (three points → a 2-anchor path).

### Behaviour notes for CLI/MCP
- The saved document model is `"version":3`; 0.21.1 reads 2.
