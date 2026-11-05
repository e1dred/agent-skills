# Layers, artboards, symbols, guides, variables and datasets

## Layers

A new document has one layer ("Layer 1", id 1). Layers and sublayers are rows in
`document.json` under `layers[]`, each with `kind.children[]` (objects) and `type:"layer"`.
`document.inspect` lists the same rows with their children's bounds.

- `layer.new {name?, top?, below?, color?, template?, locked?, visible?, printable?, preview?} → {id}`
  (verified id); `layer.newSublayer {parent?, bottom?, …} → {id}`.
- `layer.setCurrent {id/layer}`, `layer.highlight {ids}`, `layer.target {id} → {id, selected}`,
  `layer.setProps {ids?|id?, name?, visible?, locked?, template?, printable?, preview?, dimImages?}`.
- `layer.delete → {deleted}`, `layer.duplicate → {ids}`, `layer.move {ids, target}` (verified;
  a row cannot be moved into itself — "a row can't go into itself"),
  `layer.collectInNew → {id}`, `layer.selectAll → {selected}`, `layer.locate {id} → {ancestry}`.
- Show/hide/lock: `layer.hideOthers`, `layer.showAll`, `layer.lockOthers`, `layer.unlockAll`,
  `layer.previewAll`, `layer.outlineOthers`, `layer.template {on}` (all verified toggles).
- `layer.flatten {id} → {id, discarded}`, `layer.merge` (needs two or more highlighted rows),
  `layer.releaseToLayers` / `layer.releaseToLayersBuild` (need art to release),
  `layer.reverse` (two or more rows in one layer), `layer.clippingMask.toggle` (needs objects to
  clip by; "the layer has no objects to clip by"), `layer.pasteRemembersLayers {on}`.
- Clipping masks on objects are separate: `object.clippingMask.make {ids?} → {id}`,
  `.release`, `.editContents`, `.editMask` (the last two need a clip group selected).

## Artboards

- `artboard.new {x?, y?, width?, height?, name?, color?, showCenterMark?, …} → {index}`
  (0-based index; verified name "A2" at x=700).
- `artboard.setProps {index | artboards:[{index, name?, color?, x?, y?, width?, height?, …}…]}`
  — one artboard, or several in one undo step.
- `artboard.move {index|indices, dx, dy, moveArt?, copy?, patterns?} → {indices, moved}`,
  `artboard.reorder {index, to}`, `artboard.rearrange {columns?, rows?, spacing?} → {artboards, rows, columns}`
  (verified), `artboard.fitToArt`, `artboard.fitToSelection` (both verified).
- `artboard.delete {index}`, `artboard.deleteEmpty → {deleted}`, `artboard.duplicate → {ids, index}`,
  `artboard.cut`/`copy`, `artboard.convertToArtboards {ids} → {artboards}` (verified: one object
  group became 2 artboards).
- `document.inspect` reports `artboards[]` with name, x, y, width, height.

## Symbols

- `symbol.new {name?, ids?|id?, registration?: 0..8, exportType?: movieClip|graphic, nineSlice?,
  type?: static|dynamic} → {id, name, registration, exportType, type}` — makes a symbol from the
  selection and replaces it with an instance. **Select the art first** (a bare call refuses
  "nothing selected").
- `symbol.place {name?, x?, y?} → {id}` places an instance at the registration point (default
  artboard centre). `symbol.spray {points:[[x,y]…]} → {id, count}` sprays instances;
  `symbol.adjust` is the tool version.
- `symbol.list → {current, symbols:[{name, instances, …}]}`, `symbol.options {name?, newName?,
  registration?, exportType?, nineSlice?, type?} → {name, type, registration, exportType}`,
  `symbol.setCurrent`, `symbol.selectInstances {name} → {count}`, `symbol.unused`,
  `symbol.duplicate → {name}`, `symbol.replace {name}`, `symbol.delete {name}`,
  `symbol.breakLink → {ids}`.
- Editing: `symbol.edit {name} → {id, layer}` enters editing of the symbol's art;
  `symbol.exitEditing` leaves. `symbol.update` re-defines from the current art — this round hit
  "objects can't be nested more than 32 deep" when an instance was selected, so edit the symbol's
  art directly instead of re-symbolising the instance.
- Instance appearances: `symbol.instance.setAppearance {id?|ids?, path:[i…], fill?, stroke?,
  opacity?, blend?}` works only on **dynamic** symbols: a static symbol refuses with
  "`Sym1` is a static symbol: set its Symbol Type to Dynamic" — call
  `symbol.options {name, type:"dynamic"}` first. `symbol.instance.reset` restores.
- Libraries: `symbol.libraries → {libraries:[{id,name,count,category}]}` (built-in `basic-shapes`
  has 9), `symbol.library {library}`, `symbol.addFromLibrary {library, name?}`,
  `symbol.saveLibrary → {count, dataBase64}`, `symbol.loadLibrary {path|data|dataBase64}`.

## Guides

- `guide.add {x?, y?, angle?, artboard?} → {index}` (verified), `guide.list` (read-ok),
  `guide.select → {selected}`, `guide.remove {index}`, `guide.move`, `guide.setLayer`.
- Removing/moving needs a selected guide ("no guide selected", "no guide 0"); add one first in the
  same script.

## Variables and datasets (data-driven art)

- `variable.define {name, kind:"text"|"visibility"|"image"|"graph"} → {name, kind}` (verified).
  `kind` has **no default** — pass it.
- `variable.list → {locked, variables:[{name, kind, bindings}]}` (read-ok),
  `variable.bind {variable, ids/…}` (needs objects bound to variables first),
  `variable.makeTextDynamic`/`makeVisibilityDynamic`/`makeImageDynamic`/`makeGraphDynamic`,
  `variable.unbind`, `variable.lock`, `variable.highlight`, `variable.rename`, `variable.delete`,
  `variable.loadLibrary`, `variable.saveLibrary`.
- `dataset.new {name, values?"}, `dataset.set {name, values?} → {name, values, removed}` (verified),
  `dataset.list → {active, datasets}`, `dataset.select {name} → {applied, skipped, warning}`,
  `dataset.next`, `dataset.prev`, `dataset.rename`, `dataset.delete`, `dataset.capture`,
  `dataset.update`, `dataset.import {path|data|dataBase64|csv}`, `dataset.export → {csv}`.
- A dataset that binds variables nothing uses applies 0 changes and warns
  "nothing in data set DS1 was applied" — define variables and bind art first.
