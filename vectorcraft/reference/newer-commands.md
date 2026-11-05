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
