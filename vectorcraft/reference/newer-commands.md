# Version notes

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
