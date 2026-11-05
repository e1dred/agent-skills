# Version notes

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
