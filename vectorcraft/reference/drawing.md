# Drawing: shapes, paths, Pathfinder, Shape Builder, Shaper, Live Paint, brushes

All commands below were exercised headless on 0.21.0. "verified" means the document model changed
in the named way.

## Shapes

`shape.*` creates a live shape on the current layer and returns `{id}`.

| Command | Params | Note |
|---|---|---|
| `shape.rectangle` | `{x, y, width, height, radius?, rotation?}` | x/y is the top-left |
| `shape.ellipse` | `{x, y, width, height, rotation?}` | |
| `shape.polygon` | `{cx, cy, radius, sides=6, rotation?}` | |
| `shape.star` | `{cx, cy, radius1, radius2, points=5, rotation?}` | |
| `shape.line` | `{x1, y1, x2, y2, fill?}` | |
| `shape.arc` | `{x1,y1,x2,y2,closed?,slope?}` or `{x,y,lengthX,lengthY,reference?,baseAlong?,…}` | |
| `shape.spiral` | `{cx, cy, radius, decay=80, segments=10, clockwise?}` | |
| `shape.flare` | `{cx, cy, diameter=100, …, rays=15}` | all params have defaults |
| `shape.rectangularGrid` / `shape.polarGrid` | `{x,y,width,height, rows=5, columns=5, …}` | |

Converting a shape's live geometry to a plain path: `object.expandShape {ids?}`; the reverse,
`object.shape.convertToShape`, needs rectangles/ellipses selected and refuses otherwise
(observed: "no rectangles or ellipses selected").

## Paths

- `path.create {anchors:[{x,y,in?:[x,y],out?:[x,y]}…], closed?:bool, d?: SVG path data} → {id}`.
  `d` is an alternative to anchors. **`closed` defaults to false**; pass `closed:true` deliberately.
- Anchor editing (all verified on a 4-anchor path):
  - `path.appendAnchor`, `path.insertAnchor {id, subpath?, index/segment…} → {anchor}`
  - `path.moveAnchor {id, subpath?, anchor, x, y}`, `path.moveAnchors {…moves…}`
  - `path.setHandle {id, …, handle: in|out, x, y}`, `path.setAnchors`, `path.reshape`,
    `path.reshapeSegment`
  - `path.removeAnchor`, `path.deleteAnchors` / `path.removeAnchors` / `path.cutAtAnchors`
    (the last three need anchors selected with the Direct Selection tool; this round could not
    select anchors and they refused with "no anchor points selected")
  - `path.reverse → {changed}`, `path.average`, `path.joinScrub`
- Creation helpers: `path.freehand {points:[[x,y]…]} → {id}`, `path.curvature`, `path.blob`,
  `path.curvatureEdit` (needs `x` and `y` of the curvature point).
- Clean-up and shaping: `object.path.simplify` (verified: anchors 8→6 at level 50),
  `object.path.smooth` (verified 8→6), `object.path.addAnchorPoints` (verified 8→16),
  `object.path.cleanUp`, `object.path.outlineStroke {ids} → {ids}`,
  `object.path.offsetPath {ids} → {ids}` (verified: one path in, two out),
  `object.path.splitIntoGrid → {ids, guides}` (verified: 4 pieces), `object.path.smoothRegion`,
  `path.mirrorCut`, `path.rectCut`, `path.lineCut {from:[x,y], to:[x,y]}`, `path.split {id, segment, t}`.
- `path.close` / `path.join` **refuse on an already-closed path** ("path is already closed");
  `path.averageJoin` needs two open path ends.
- Compound paths: `object.compoundPath.make {ids?} → {id}`, `object.compoundPath.release`.
- Compound shapes: `object.compoundShape.make {ids?} → {id}`, `.setMode {mode:"add"|"subtract"|
  "intersect"|"exclude"}`, `.release`, `.expand` (new in 0.21.0).

## Pathfinder (12 ids)

All verified with two overlapping rectangles selected:

| Command | Verified result |
|---|---|
| `object.pathfinder.unite` | `{ids:[7]}` one merged path |
| `object.pathfinder.minusFront` / `minusBack` | `{ids:[7]}` |
| `object.pathfinder.intersect` | `{ids:[8]}`; refuses "Intersect produced an empty result" when shapes don't overlap |
| `object.pathfinder.exclude` | `{ids:[7]}` |
| `object.pathfinder.divide` | `{ids:[9]}` (several pieces) |
| `object.pathfinder.trim` / `merge` / `outline` | `{ids:[9]}` |
| `object.pathfinder.crop` | `{ids:[9]}` |
| `object.pathfinder.trap` | refused: "no edges of different colours meet among the selected objects" |
| `object.pathfinder.options` | reads/sets precision, removeRedundantPoints, removeUnpainted |

Commands default to the selection and also take `ids`. Results replace the inputs, so ids shift:
re-read them from the result rather than reusing the old ids.

## Shape Builder and Shaper

- `shapeBuilder.regions {} → {edges, lines, regions}` — analysis only; the regions carry `bounds`
  and `source` ids (verified: two rectangles → two edges, one region).
- `shapeBuilder.merge {points:[[x,y]…] | rect:[x,y,w,h]} → {ids, regions, edges, lines, merged}` —
  a drag path through the regions to merge (verified: merged 7 into the result).
- `shaper.scribble {points:[[x,y]…], ids?, tolerance?} → {id, regions, strokes}` — built-in
  Shaper tool; scribbling inside a region removes the fill (verified).
- `shaper.select {point:[x,y]}`, `shaper.release → {ids}`, `shaper.expand → {id}` (verified),
  `shaper.releaseSource` (needs a Shaper Group's original shape).

## Live Paint

- `livePaint.make {ids?} → {id, faces, edges}` on the selected paths (verified: 2 faces).
  Refuses type/images.
- `livePaint.fill {group?, face, color?}`, `livePaint.strokeEdge`, `livePaint.gapOptions`,
  `livePaint.info {group}`.
- `livePaint.merge` (add paths to a group), `livePaint.release → {ids}`,
  `livePaint.expand → {ids}` (verified: expands back to plain paths).

## Brushes

- `brush.list → {brushes:[{name,type}]}`; built-ins are `3 pt. Round`, `6 pt. Flat`, `10 pt. Oval`,
  `Charcoal`, `Tapered Stroke`, and more (14 in the default set).
- Create: `brush.new {name?, type?}` (verified → "New Calligraphic Brush"); defaults are
  calligraphic; `brush.options {name, …}` edits size/angle/roundness/…
- Apply/remove: `brush.apply {ids?, name}`, `brush.remove`, `brush.setCurrent`, `brush.move`.
- Libraries: `brush.libraries`, `brush.library {library}`, `brush.addFromLibrary`,
  `brush.saveLibrary → {count, dataBase64}`, `brush.loadLibrary {path|data|dataBase64}`.
- `brush.duplicate`, `brush.delete`, `brush.unused`; `brush.freehand` is really `path.freehand`
  ("missing array `points`" if you call it without points).

## Distortion families (precondition-heavy)

- Envelopes: `object.envelope.makeWithWarp {ids?, style, bend…}`, `.makeWithMesh {rows, cols}`,
  `.makeWithTopObject`, then `.resetWithWarp`, `.release`, `.expand`, `.editContents`,
  `.setMeshPoint`, `.options` — all need an envelope selected; without one the error is
  "select an envelope".
- Gradient meshes: `object.mesh.create {rows, cols, appearance}` then `object.mesh.setPointColor`,
  `.movePoint`, `.movePoints`, `.addLine`, `.deletePoint`, `.expand` — without a mesh:
  "not a gradient mesh or mesh envelope".
- Warps: `object.liquify {tool, …}`, `object.puppetWarp {pins, moved}`, `object.distort
  {corners:[[x,y]×4]}`, `object.transform {matrix:[a,b,c,d,e,f]}`.
