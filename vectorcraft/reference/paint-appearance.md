# Paint, appearance, effects, transparency; swatches, gradients, patterns, stamps, graphic styles

## Fills and strokes

- `paint.setFill` / `paint.setStroke` take **one** of: `color:"#rrggbb"` (or [r,g,b],
  {c,m,y,k}, {gray}, {l,a,b}), `none:true`, `swatch:"Name"` (keeps the link to a global/spot
  swatch), `gradient:{…}`, `pattern:{…}`. Passing none of them refuses:
  "give color, none, swatch or gradient". Both verified changing the selected objects.
- `paint.swap`, `paint.default`, `paint.toggleActive {fill|stroke}`, `paint.none`,
  `paint.invert` (verified: changed 2 objects), `paint.sampleColor`, `paint.lastColor`,
  `paint.lastGradient`, `paint.recent`, `paint.proxies`.
- Stroke geometry: `stroke.set {width?, cap?, join?, dashes?, align?, arrowheads?, scale?}`,
  `stroke.setAdvanced`, `stroke.widthProfile.list → {current, profiles}`, `stroke.widthPoint.set`,
  `.copy`, `.remove`, `stroke.widthProfile.set` — the width-point commands need a width profile
  and a variable-width stroke, which this round did not build.

## Appearance stack

Every object has an appearance: an ordered list of `fill` / `stroke` items plus `effects`.
Read it in `document.json` as `objects[].appearance.items[]` / `.effects[]`; `document.inspect`
shows the effective `fill`, `stroke`, `opacity` on each node.

- `appearance.addFill`, `appearance.addStroke`, `appearance.clear`, `appearance.reduceToBasic`,
  `appearance.duplicateItem`, `appearance.setActiveItem {index}`, `appearance.targetContents`
  (all verified changing the model).
- `appearance.setItem`, `appearance.removeItem`, `appearance.moveItem`, `appearance.copyFrom
  {source}`, `appearance.transfer {source}`, `appearance.newArt {…}` (default appearance for new
  art), `appearance.setNewArtBasic {on}`, `appearance.showAllHidden`.
- Effects: `effect.apply {effect:"stylize.dropShadow", params?:{…}, item?} → {ids, index}`.
  Verified: applying `stylize.dropShadow` adds `appearance.effects[{id:"stylize.dropShadow"}]`.
  `effect.list → {catalog, applied}` (read-ok); `effect.setParams`, `effect.remove {index}`,
  `effect.duplicate`, `effect.move {from, to}`, `effect.expandAppearance {ids} → {ids}`
  (verified: materialises the look and removes the live effect; it refuses with "select (or
  target) objects whose appearance isn't basic" when there is no live effect to bake).
- `effect.lightingPreset {preset:"standard"|"diffuse"|"topLeft"|"right"}`.

## Transparency and blending

- `transparency.set {ids?, opacity? 0-100, blend?:"Multiply"…, isolate?, knockout?,
  knockoutShape?, item?, target?}` verified: opacity 50 → `opacity 0.5` on the object.
- `transparency.info {ids?} → {blend, isolate, knockout, opacity…}` (read-ok).
- Opacity masks: `transparency.makeOpacityMask {ids?} → {id, editing}` (verified);
  `transparency.setOpacityMask {clip?, invert?, disabled?, linked?}`,
  `transparency.releaseOpacityMask`, `.disableOpacityMask`, `.enableOpacityMask`,
  `.linkOpacityMask`, `.unlinkOpacityMask`, `.editOpacityMask → {layer}`, `.viewOpacityMask`,
  `.stopEditingOpacityMask`, `.opacityMaskInfo`. Most require an object that already has a mask —
  "no target object has an opacity mask: select one or give `id`".
- Page-level: `transparency.togglePageIsolatedBlending`, `.togglePageKnockoutGroup`,
  `.toggleNewMasksClipping`, `.toggleNewMasksInverted` (verified toggles returning `{value}`).

## Swatches

- `swatch.new {name?, color?|colors?|swatch?|gradient?|pattern?, tint?, mode?} → {name, names}` —
  with no colour it uses the current fill (verified: named "R=255 G=255 B=255" when white).
- `swatch.list → {groups, swatches}` (read-ok; includes the RGB/Grays groups and spot swatches);
  `swatch.unused → {names}`, `swatch.addUsedColors`, `swatch.duplicate {name} → {name}` (verified
  "Red copy"), `swatch.delete {name|names} → {deleted, unlinked}` (verified deleting "Red"),
  `swatch.move`, `swatch.merge {names}`, `swatch.sortByName`, `swatch.sortByKind`,
  `swatch.edit {name, newName?, color?, mode?}`, `swatch.editGroup`, `swatch.newGroup {name} →
  {name, swatches}`, `swatch.ungroup`, `swatch.setSpot {name} → {name, spot}`, `swatch.spotOptions`.
- Libraries: `swatch.library.list → {libraries:[{id,name,count}]}` (built-in `web-safe-216` has
  216), `swatch.library.get {library}`, `swatch.library.add`, `swatch.library.save → {count,
  dataBase64}`, `swatch.library.load {path|data|dataBase64}`, `swatch.library.copyToUser`,
  `swatch.resetDefaults`.

## Gradients

- `gradient.presets.list → {presets:[{name, builtIn, gradient}]}` (read-ok; 0.21.0's new preset
  system), `gradient.presets.apply {name}`, `gradient.presets.save {name} → {name}` (verified),
  `gradient.presets.delete`.
- `paint.editGradient {kind:"linear"|"radial"|"freeform", stroke?, mode?, method?, …}` — verified
  with the selected objects and kind linear/radial; it switches the paint to a gradient.
  `paint.setGradientGeom`, `gradient.selectStop {index} → {index}`.
- Verified way to make a gradient from scratch:
  `paint.setFill {gradient:{type:"linear", stops:[{offset:0,color:"#ff0000"},
  {offset:1,color:"#0000ff"}]}}`; the inspect paint becomes `"fill": "Linear gradient"`.
  A stop **needs `offset`** (0-1) — `position` is rejected with "stop 0 needs `offset`".
- Freeform gradients (`paint.freeform.*`) refuse unless the targeted paint already is one:
  "the paint is not a freeform gradient (apply one with paint.editGradient …)".

## Patterns

- `object.pattern.make {ids?, name?, tileType?, width?, height?, edit?:true} → {name}` makes a
  pattern swatch from the selection and **enters pattern-editing mode** (verified: "Pat1").
- While editing: `pattern.options {name?, newName?, tileType?, brickOffset?, width?, height?,
  copies?, dimCopies?, showTileEdge?…}`, `pattern.transform`, `pattern.list`.
  Finish with `object.pattern.done`, `object.pattern.saveCopy`, or `object.pattern.cancel`.
- Outside editing mode these refuse ("not in pattern editing mode", "the document has no patterns").

## Graphic styles

- `graphicStyle.list → {styles:[…], selected, overrideCharColor}` (read-ok; built-ins include
  "Default Graphic Style", "Black Outline", "Heavy Ink", "Sunshine").
- `graphicStyle.new {name?, id?} → {name}`, `.apply {name}`, `.redefine`, `.rename`, `.delete`,
  `.duplicate`, `.breakLink`, `.merge {names}`, `.move`, `.unused`, `.setOptions`,
  `.libraries`, `.library {library}`, `.addFromLibrary`, `.saveLibrary`, `.loadLibrary`.
- `graphicStyle.new`/`.redefine` need an object selected (or `id`); `.apply` refuses "no graphic
  style `X`" for an unknown name.

## Brushes, stamps

- Brushes are covered in `drawing.md`.
- Stamps/patterns used as stamps: `object.pattern.make` + `pattern.options`; symbol spraying is
  `symbol.spray` (see `layers-artboards-symbols.md`).
