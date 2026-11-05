# Transform, arrange and align

All transform commands default to the selection and also take `ids`; most take `copy:true` to
leave the original in place. Coordinates are document points.

## Direct transforms (verified)

| Command | Params | Verified effect |
|---|---|---|
| `object.move` | `{ids?, dx, dy, copy?, objects?, patterns?}` | translates |
| `object.rotate` | `{ids?, angle (deg counter-clockwise), absolute?, origin?[x,y], copy?}` | rotate 30° changed the bounds 200×120 → 233.2×203.9 (origin defaults to the bbox centre) |
| `object.scale` | `{ids?, sx:%, sy?:%, origin?, copy?, strokes?}` | `sx:150` on 200×120 gave 300×180 — **sy defaults to sx** |
| `object.reflect` | `{ids?, axis:"vertical"|"horizontal"|deg, origin?, copy?}` | |
| `object.shear` | `{ids?, angle, axis?:"horizontal"|"vertical", origin?, copy?}` | |
| `object.transform` | `{matrix:[a,b,c,d,e,f], copy?, ids?, …}` | `[1,0,0,1,10,10]` moved the layer bounds by (10,10) |
| `object.setBounds` | `{x?, y?, width?, height?, reference?:0..8, proportional?, strokes?, corners?, copy?, patterns?, typeAreas?}` | `{width:300,height:50}` resized the object to 300×50 |
| `object.transformEach` | transform every selected object about its own centre | |
| `object.resetBoundingBox` | recompute the bounds after anchor edits | |
| `object.transformAgain` | repeat the previous transform | refuses "no previous transform" until one exists |
| `object.nudge` | arrow-key nudge (dx/dy) | |

`object.setProps` handles non-geometric attributes: `name`, `visible`, `locked`, `opacity` (0-100,
stored 0-1 — `opacity:80` showed 0.8), `blend`, `isolate`, `knockout`.

## Arrange (stacking order)

`object.arrange.bringToFront`, `.bringForward`, `.sendBackward`, `.sendToBack`,
`.sendToCurrentLayer`; also `object.lock`, `object.unlockAll`, `object.hide`, `object.showAll`,
`object.lock.above`, `.otherLayers`, `.unselected`, `object.hide.above`, `.otherLayers`,
`.unselected`, `object.isolate`, `object.exitIsolation`.

## Grouping

`object.group {ids?} → {id}`, `object.ungroup`, `object.compoundPath.make/release`,
`object.compoundShape.make/setMode/release/expand`, `object.maskImage`, `object.cropImage`,
`object.textWrap.make/release/options`.

## Align and distribute

- `object.align {horizontal?:"left"|"center"|"right", vertical?:"top"|"center"|"bottom",
  to?:"selection"|"artboard"|"key", ids?}` — pass at least one of horizontal/vertical:
  "give horizontal or vertical". With one object selected and `to:"selection"` nothing moves
  (verified: no change); select two or more, or use `to:"artboard"`.
- `object.distribute {horizontal?|vertical?, spacing?, to?/key?}`, `object.distributeSpacing`.
- `select.key {id?}` sets the key object so align/distribute keep it fixed.

## Pathfinder and Shape Builder

See `drawing.md`; they are transforms of path geometry: `object.pathfinder.*`,
`shapeBuilder.merge`, `object.path.splitIntoGrid`, `object.path.divideObjectsBelow`
(needs exactly one path).

## Practical rules

- Read back `document.inspect.layers[].children[].bounds` ({x,y,width,height}) and
  `selectionBounds` — both update immediately.
- Rotation/scale origins are optional but explicit origins make results deterministic:
  `origin:[x,y]` is in document coordinates.
- `copy:true` produces new objects; their ids come back in the result (`{ids:[…]}`), and the
  original ids stay valid.
- `stroke`/`corners`/`patterns` booleans decide whether stroke weights, corner radii and pattern
  tiles scale with the art (defaults follow the Transform panel preference).
