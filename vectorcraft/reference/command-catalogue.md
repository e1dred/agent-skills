# VectorCraft command catalogue (0.21.0) — 911 ids

Generated from `vectorcraft-cli commands` and this round's evidence. Status per id:
**verified** = the same field read before/after (inspect + document model); **read-ok** = a read/list returned real data;
**ran** = accepted, effect not a readable field; **refused** = the exact error is quoted in `results.jsonl`.
The params column is the first part of the command's own parameter doc; run `vectorcraft-cli commands` for the full text.

## object (151)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `object.transform` | verified | {matrix: [a,b,c,d,e,f], copy?: bool, ids?, strokes?: bool, corners?: bool, typeAreas?: bool, anchors?: bool, objects?: bool (Transform Objec… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 497.82399999999996 |
| `object.move` | verified | {ids?: [id…] (selected first; default: the selection), dx, dy, copy?, objects?: bool (Transform Objects, default true; false: the art stays … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 497.82399999999996 |
| `object.rotate` | verified | {ids?: [id…] (selected first; default: the selection), angle: deg (counter-clockwise), absolute?: bool (angle is the bounding box's new angl… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 546.7230746181009 |
| `object.scale` | verified | {ids?: [id…] (selected first; default: the selection), sx: %, sy?: %, origin?: [x,y], copy?, strokes?: bool (Scale Strokes & Effects: stroke… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 477.82399999999996 |
| `object.reflect` | verified | {ids?: [id…] (selected first; default: the selection), axis: "vertical"\|"horizontal"\|deg, origin?, copy?, objects?: bool (Transform Object… | `inspect.layers{id=1}.children{id=3}.bounds.x`: 400.0 → 100.0 |
| `object.shear` | verified | {ids?: [id…] (selected first; default: the selection), angle: deg, axis?: "horizontal"\|"vertical", origin?, copy?, objects?: bool (Transfor… | `inspect.layers{id=1}.bounds.width`: 400.0 → 422.5823661818338 |
| `object.transformAgain` | refused | {copy?, strokes?, corners?, patterns?, typeAreas?: bool (as object.transform's; default: the value the transform it repeats used, else objec… | vectorcraft-cli: step 9 (object.transformAgain): no previous transform |
| `object.nudge` | verified | {dx: -1\|0\|1, dy: -1\|0\|1, big?: bool (×10), copy?: bool, patterns?: bool (Transform Patterns: pattern fills and strokes transform with th… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 497.82399999999996 |
| `object.arrange.bringToFront` | ran | {ids?: [id…] (selected first; default: the selection)} | no change in inspect/json; result=null |
| `object.arrange.bringForward` | ran | {ids?: [id…] (selected first; default: the selection)} | no change in inspect/json; result=null |
| `object.arrange.sendBackward` | ran | {ids?: [id…] (selected first; default: the selection)} | no change in inspect/json; result=null |
| `object.arrange.sendToBack` | ran | {ids?: [id…] (selected first; default: the selection)} | no change in inspect/json; result=null |
| `object.arrange.sendToCurrentLayer` | ran | {ids?: [id…] (selected first; default: the selection)} | no change in inspect/json; result=null |
| `object.group` | verified | {ids?: [id…] (selected first; default: the selection)} → {id} | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.ungroup` | ran | {ids?: [id…] (selected first; default: the selection)} | no change in inspect/json; result=null |
| `object.lock` | verified | {ids?: [id…] (selected first; default: the selection; in isolation mode, only those inside the isolated object)} | `inspect.layers{id=1}.children{id=3}.locked`: False → True |
| `object.unlockAll` | ran | {scope?: "document"\|"group" (default document, which in isolation mode is the isolated object; group: only the objects inside the groups th… | no change in inspect/json; result={"count": 0} |
| `object.hide` | verified | {ids?: [id…] (selected first; default: the selection; in isolation mode, only those inside the isolated object)} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 207.82399999999996 |
| `object.showAll` | ran | {scope?: "document"\|"group" (default document, which in isolation mode is the isolated object; group: only the objects inside the groups th… | no change in inspect/json; result={"count": 0} |
| `object.compoundPath.make` | verified | {ids?: [id…] (selected first; default: the selection)} | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.compoundPath.release` | ran | {ids?: [id…] (selected first; default: the selection)} release the selected compound paths into their paths, each with the compound path's p… | no change in inspect/json; result=null |
| `object.clippingMask.make` | verified | {ids?: [id…] (selected first; default: the selection)} the topmost selected object (a path, compound path or text, which loses its paint) cl… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.clippingMask.release` | ran | {ids?: [id…] (selected first; default: the selection)} the selected clip groups become plain groups; their clipping path (path, compound pat… | no change in inspect/json; result=null |
| `object.clippingMask.editContents` | verified | {} select the clipped art of the selected clip groups → {count} | `inspect.selection[0]`: 7 → 2 |
| `object.clippingMask.editMask` | verified | {} select the clipping paths of the selected clip groups → {count} | `inspect.selection[0]`: 7 → 3 |
| `object.isolate` | verified | {id?} isolate a group, a layer or a single object (default: the first selected object); type, a hidden or locked object, an object in a hidd… | `inspect.isolation`: None → 2 |
| `object.exitIsolation` | ran | {} | no change in inspect/json; result=null |
| `object.setProps` | ran | {ids?\|id?, name?, visible?, locked? (visible: false or locked: true deselects every selected object hidden or locked after the call, the ke… | no change in inspect/json; result=null |
| `object.align` | verified | {horizontal?: "left"\|"center"\|"right", vertical?: "top"\|"center"\|"bottom", to?: "selection"\|"artboard"\|"key" (default: the key object … | `inspect.layers{id=1}.bounds.width`: 400.0 → 300.0 |
| `object.distribute` | ran | {horizontal?: "left"\|"center"\|"right", vertical?: "top"\|"center"\|"bottom", spacing?: pt (used with a key, select.key: the key object, or… | no change in inspect/json; result=null |
| `object.distributeSpacing` | ran | {axis?: "horizontal"\|"vertical" (default: "horizontal"), spacing?: pt (the key object, select.key, or the key guide, select.key {guide}, st… | no change in inspect/json; result=null |
| `object.setBounds` | ran | {x?, y?, width?, height?, reference?: 0..8 (9-point grid; a number past 8 is read as 8), proportional?, strokes?, corners?, copy?: bool, pat… | no change in inspect/json; result={"ids": [2, 3]} |
| `object.expandShape` | verified | {} convert live shapes to plain paths | `inspect.layers{id=1}.children{id=3}.kind`: Ellipse → Path |
| `object.setLiveShape` | ran | {id?, ids?, radius?: pt (or % of each corner's maximum when `relativeRadii` is true), kind?: "round"\|"invertedRound"\|"chamfer", relativeRa… | no change in inspect/json; result=null |
| `object.distort` | verified | {corners: [[x,y]×4] (TL, TR, BR, BL), from?: [x0,y0,x1,y1] (default: selection bounds), ids?} projective warp of anchors and handles | `inspect.layers{id=1}.bounds.width`: 400.0 → 200.0 |
| `object.pathfinder.unite` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.minusFront` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.bounds.width`: 400.0 → 200.0 |
| `object.pathfinder.intersect` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=6}.anchors`: 4 → <removed> |
| `object.pathfinder.exclude` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.divide` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.trim` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.merge` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.crop` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=6}.anchors`: 4 → <removed> |
| `object.pathfinder.outline` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.minusBack` | verified | {ids?: [id…] (selected first; default: the selection), precision?: pt 0.001..10, removeRedundantPoints?: bool, removeUnpainted?: bool (defau… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.pathfinder.trap` | refused | {ids?: [id…] (selected first; default: the selection), thickness?: pt 0.01..5000 (0.25; how far the lighter colour reaches into the darker o… | vectorcraft-cli: step 9 (object.pathfinder.trap): Trap: no edges of different colours meet among the |
| `object.pathfinder.options` | read-ok | {precision?: pt 0.001..10 (0.01; how closely the Pathfinder operations follow the paths: results are refit to within it and pieces thinner t… | no change in inspect/json; result={"precision": 0.01, "removeRedundantPoints": false, "removeUnpaint |
| `object.path.outlineStroke` | verified | {} replace stroked paths with filled outlines → {ids} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 508.32399999999996 |
| `object.path.offsetPath` | verified | {offset: pt (negative insets), joins?: "miter"\|"round"\|"bevel", miterLimit?: 4} → {ids} (new objects above the originals) | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 607.824 |
| `object.path.simplify` | verified | {tolerance?: pt (1), level?: 0..100 (the Simplify slider, in place of tolerance: 0 fewest anchor points, 50 is 1 pt, every 10 levels halves … | `inspect.layers{id=1}.bounds.width`: 400.0 → 400.00000000000006 |
| `object.path.smooth` | verified | {level?: 0..100 (50; the Smooth slider: 0 minimum smoothing, the path staying within 0.1% of its longer side, 100 maximum: smoothed along it… | `inspect.layers{id=1}.bounds.width`: 400.0 → 399.90617114326335 |
| `object.path.addAnchorPoints` | verified | {} → {ids} | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → 8 |
| `object.path.divideObjectsBelow` | refused | {} cut the objects below with the selected path (which is removed) → {ids} | vectorcraft-cli: step 9 (object.path.divideObjectsBelow): Divide Objects Below: select exactly one p |
| `object.path.splitIntoGrid` | verified | {rows?: 2, columns?: 2, gutter?: pt (12; rowGutter?, columnGutter?: one of the two), totalHeight?, totalWidth?: pt (the grid's size; the sel… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.path.cleanUp` | ran | {strayPoints?: true, unpaintedObjects?: true, emptyTextPaths?: true} → {removed} | no change in inspect/json; result={"removed": 0} |
| `object.compoundShape.make` | verified | {ids?: [id…] (selected first; default: the selection), mode?: "add"\|"subtract"\|"intersect"\|"exclude" (default add; Alt-clicking a Shape M… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.compoundShape.setMode` | refused | {mode: "add"\|"subtract"\|"intersect"\|"exclude", ids?: [id…] (selected first; default: the selection)} the members of compound shapes that … | vectorcraft-cli: step 9 (object.compoundShape.setMode): command `object.compoundShape.setMode` is no |
| `object.compoundShape.release` | verified | {ids?: [id…] (selected first; default: the selection)} the selected compound shapes (and those holding the selected objects) become their me… | `inspect.layers{id=1}.children{id=7}.bounds.height`: 120.0 → <removed> |
| `object.compoundShape.expand` | verified | {ids?: [id…] (selected first; default: the selection)} the selected compound shapes (and those holding the selected objects) become the path… | `inspect.layers{id=1}.children{id=7}.bounds.height`: 120.0 → <removed> |
| `object.lock.above` | ran | {} lock objects in the same layer that are above and overlap the selection, deselecting every selected object left locked or hidden (the key… | no change in inspect/json; result={"count": 0} |
| `object.lock.otherLayers` | verified | {} lock every layer that holds no selected object; in isolation mode, change nothing and return a count of 0 → {count} | `inspect.layers{id=6}.locked`: False → True |
| `object.lock.unselected` | verified | {} lock unselected artwork in one undo step, including unselected members of partly selected groups, clipping groups and compound paths, and… | `inspect.layers{id=1}.children{id=5}.locked`: False → True |
| `object.hide.above` | ran | {} hide objects in the same layer that are above and overlap the selection, deselecting every selected object left hidden or locked (the key… | no change in inspect/json; result={"count": 0} |
| `object.hide.otherLayers` | verified | {} hide every layer that holds no selected object; in isolation mode, change nothing and return a count of 0 → {count} | `inspect.layers{id=6}.visible`: True → False |
| `object.hide.unselected` | verified | {} hide, in one undo step, every object select.all takes that is not selected and holds no selected object; in a group that holds one it hid… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 120.0 |
| `object.transformEach` | ran | {scaleH?: % (100), scaleV?: % (100), moveH?: pt, moveV?: pt (down = +), rotate?: deg (counter-clockwise), reflectX?: bool (flip left-right, … | no change in inspect/json; result={"ids": [2, 3]} |
| `object.resetBoundingBox` | ran | {} square the bounding box of the selected objects to the page again after a rotation (their geometry stays; one undo step, none when no box… | no change in inspect/json; result={"changed": 0} |
| `object.rasterize` | verified | {ppi?, background?: transparent\|white\|black\|"#rrggbb", antiAlias?: none\|art\|type (text snapped to pixels)\|bool, padding?\|addAround?: … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 508.32399999999996 |
| `object.createObjectMosaic` | verified | {columns=10, rows=10 (whole numbers, kept within 1..1000), width?, height? (new size in pt; default the image's), spacingX=0, spacingY=0 (pt… | `inspect.objects`: 7 → 58 |
| `object.cropImage` | refused | {rect?: [x, y, width, height] \| trim?: true (to the pixels that aren't fully transparent, pixel for pixel; an image with none to cut is lef… | vectorcraft-cli: step 11 (object.cropImage): invalid parameters for `object.cropImage`: nothing to c |
| `object.maskImage` | verified | {} clip the selected image with a rectangle around it (its own outline, rotated with it) and select that clipping path, whose handles then c… | `inspect.layers{id=1}.children{id=7}.bounds.height`: 200.0 → <removed> |
| `object.createTrimMarks` | verified | {style?: "roman"\|"japanese" (default: the japaneseCropMarks preference; japanese: double lines at the trim and bleed edges plus centre mark… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 535.324 |
| `object.shape.convertToShape` | refused | {} turn paths that are rectangles (any rotation) or axis-aligned ellipses into live shapes → {converted} | vectorcraft-cli: step 9 (object.shape.convertToShape): Convert to Shape: no rectangles or ellipses s |
| `object.blend.make` | verified | {ids?, steps?: n \| distance?: pt \| smooth?: bool, orientation?: page\|path (default: the Blend Options set with nothing selected, else smo… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.blend.release` | verified | {} release the selected blends: the key objects come back and the spine stays as a path with no fill or stroke, below them; a blend with a n… | `inspect.layers{id=1}.children{id=7}.bounds.height`: 120.0 → <removed> |
| `object.blend.options` | ran | {spacing?: smooth\|steps\|distance, value?: n, steps?: n, distance?: pt, orientation?: page\|path, smooth?: bool, easingType?: easeIn\|easeO… | no change in inspect/json; result={"defaults": true} |
| `object.blend.expand` | verified | {} replace the selected blends by groups of their keys and steps, each keeping the blend's id, name, transparency (knockout and isolation in… | `inspect.layers{id=1}.bounds.y`: 100.0 → 99.99999999999999 |
| `object.blend.replaceSpine` | refused | {} use the selected path as the spine of the selected blend (the path is consumed) | vectorcraft-cli: step 11 (object.blend.replaceSpine): Replace Spine: select a blend and a path |
| `object.blend.reverseSpine` | verified | {} reverse the order of the key objects along the spine | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 527.824 |
| `object.blend.info` | read-ok | {} the options of the first selected blend, else those new blends start with → {target: blend\|defaults, id?, spacing: smooth\|steps\|distan… | no change in inspect/json; result={"distance": 10.0, "orientation": "page", "spacing": "smooth", "st |
| `object.blend.spine.moveAnchor` | verified | {id? (default: the selected blend), anchor: index, x, y, handle?: in\|out, independent?: bool} move a point of the blend's spine (its handle… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 567.824 |
| `object.blend.spine.convertAnchor` | verified | {id? (default: the selected blend), anchor: index, to: smooth\|corner, x?, y?} convert a blend spine point: dragging a corner creates symmet… | `doc.layers{id=1}.kind.children{id=7}.kind.spec.keyAnchors[0]`: <absent> → 0 |
| `object.blend.spine.reshapeSegment` | verified | {id? (default: the selected blend), segment: index, t: 0..1, dx, dy, perpendicular?: bool} bend a segment of the blend's spine so its point … | `doc.layers{id=1}.kind.children{id=7}.kind.spec.keyAnchors[0]`: <absent> → 0 |
| `object.blend.spine.addAnchor` | verified | {id? (default: the selected blend), x, y} add a point to the blend's spine where it passes nearest (x, y) → {anchor} | `doc.layers{id=1}.kind.children{id=7}.kind.spec.keyAnchors[0]`: <absent> → 0 |
| `object.blend.spine.removeAnchor` | refused | {id? (default: the selected blend), anchor: index} delete a point of the blend's spine that no key object sits on | vectorcraft-cli: step 11 (object.blend.spine.removeAnchor): invalid parameters for `object.blend.spi |
| `object.blend.reverseFrontToBack` | ran | {} reverse the stacking order of the selected blends | no change in inspect/json; result=null |
| `object.envelope.makeWithWarp` | verified | {ids?, style?: arc\|arcLower\|arcUpper\|arch\|bulge\|shellLower\|shellUpper\|flag\|wave\|fish\|rise\|fisheye\|inflate\|squeeze\|twist (arc),… | `inspect.layers{id=1}.bounds.width`: 400.0 → 444.979340205228 |
| `object.envelope.makeWithMesh` | verified | {ids?, rows?: 1..50 (4), cols?: 1..50 (4), columns?: as cols} envelope the selected objects with a mesh of rows × cols patches → {id} | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.envelope.makeWithTopObject` | verified | {ids?} the topmost selected path becomes the envelope of the others → {id} | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.envelope.resetWithWarp` | ran | {style?, bend?, h?, v?, horizontal? \| orientation? (as makeWithWarp; unset: the envelope's current warp, else arc 50 %), horizontalDistorti… | no change in inspect/json; result=null |
| `object.envelope.resetWithMesh` | verified | {rows?: 1..50, cols?: 1..50 (unset: a mesh envelope's own, else 4), maintainShape?: bool (true: the mesh follows the current envelope shape;… | `doc.layers{id=1}.kind.children{id=7}.kind.kind.type`: warp → mesh |
| `object.envelope.info` | read-ok | {} the selected envelope's settings, or with none selected the defaults new envelopes get → {id: n\|null, type: warp\|mesh\|topObject, style… | no change in inspect/json; result={"antiAlias": true, "distortAppearance": true, "distortLinearGradi |
| `object.envelope.release` | verified | {} release the selected envelopes into their content and their shape (a grey gradient mesh for warp and mesh envelopes, the path for a top-o… | `inspect.layers{id=1}.children{id=7}.bounds.height`: 177.01105258680417 → <removed> |
| `object.envelope.options` | ran | {fidelity?: 0..100, antiAlias?: bool, preserveShape?: clippingMask\|transparency, distortAppearance?: bool, distortLinearGradients?: bool, d… | no change in inspect/json; result=null |
| `object.envelope.expand` | verified | {} replace the selected envelopes by groups of their distorted content (type outlined), keeping name, opacity, blend mode, isolation, knocko… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 508.32339250308786 |
| `object.envelope.editContents` | verified | {editing?: bool} toggle Edit Contents / Edit Envelope → {editing} | `inspect.selection[0]`: 7 → 2 |
| `object.envelope.setMeshPoint` | refused | {id, index, x, y, handle?: 0 right\|1 left\|2 down\|3 up} move a point of a mesh envelope (its handles follow), or with `handle` place that … | vectorcraft-cli: step 11 (object.envelope.setMeshPoint): invalid parameters for `object.envelope.set |
| `object.mesh.create` | verified | {ids?, rows?: n (4), cols?: n (4), appearance?: flat\|center\|edge, highlight?: % (100), at?: [x,y], tolerance?: pt (0), columns?: as cols} … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 507.82400000000007 |
| `object.mesh.setPointColor` | verified | {id, index \| points: [index…] \| items: [{id, index \| points}…], color?, keepModel?: bool (as paint.setFill), opacity?: 0..1} colour and/o… | `doc.layers{id=1}.kind.children{id=2}.kind.points[1].color.b`: 1.0 → 0.0 |
| `object.mesh.movePoint` | ran | {id, index, x, y, handle?: 0 right\|1 left\|2 down\|3 up} move a point of a gradient mesh or mesh envelope (its handles follow), or with `ha… | no change in inspect/json; result=null |
| `object.mesh.movePoints` | verified | {id, points: [index…] \| items: [{id, index \| points}…], dx, dy} move points of gradient meshes or mesh envelopes by (dx, dy), their handle… | `doc.layers{id=1}.kind.children{id=2}.kind.points[2].p.x`: 200.0 → 210.0 |
| `object.mesh.addLine` | ran | {id, x, y, color?, keepModel?: bool (as paint.setFill), tolerance?: pt (0)} add a row and a column through (x, y) to a gradient mesh (new po… | no change in inspect/json; result={"index": 0} |
| `object.mesh.deletePoint` | refused | {id, index} delete the mesh lines through a point of a gradient mesh or mesh envelope | vectorcraft-cli: step 11 (object.mesh.deletePoint): invalid parameters for `object.mesh.deletePoint` |
| `object.mesh.expand` | verified | {} replace the selected meshes by groups of flat-coloured pieces → {ids} | `inspect.layers{id=1}.bounds.height`: 507.82400000000007 → 507.824 |
| `object.convertDocumentColorMode` | refused | {…as file.documentColorMode} same as file.documentColorMode: {mode: "cmyk"\|"rgb", convert?: true, intent?, grays?} → {changed} (an alias ke… | vectorcraft-cli: step 9 (object.convertDocumentColorMode): invalid parameters for `file.documentColo |
| `object.textWrap.make` | verified | {offset?: pt (6), invert?: bool, ids?} area type below the selected objects (same layer) wraps around them → {ids} | `doc.layers{id=1}.kind.children{id=2}.wrap.invert`: <absent> → False |
| `object.textWrap.release` | verified | {ids?} → {ids} | `doc.layers{id=1}.kind.children{id=2}.wrap.invert`: False → <removed> |
| `object.textWrap.options` | ran | {offset?: pt, invert?: bool, ids?} set the options of the selected wrap objects; no options → the current {offset, invert} | no change in inspect/json; result={"invert": false, "offset": 6.0} |
| `object.makePixelPerfect` | verified | {ids?\|id?} snap each object's edges to the pixel grid (odd stroke weights on half pixels) and round stroke weights | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 507.32399999999996 |
| `object.expandBrush` | refused | {ids?\|id?} replace brushed paths (in the selection) with groups of the brush art → {ids} | vectorcraft-cli: step 9 (object.expandBrush): Expand: no brush strokes selected |
| `object.pattern.make` | verified | {ids?, name? (trimmed; blank: New Pattern N), tileType?: grid\|brickByRow\|brickByColumn\|hexByColumn\|hexByRow, brickOffset?: 0..1 (0.5), w… | `inspect.currentLayer`: 1 → 9 |
| `object.pattern.edit` | refused | {name?} edit a pattern (default: the selected object's fill pattern) in pattern editing mode; refused while an opacity mask is edited | vectorcraft-cli: step 10 (object.pattern.edit): command `object.pattern.edit` is not available right |
| `object.pattern.done` | refused | {} leave pattern editing mode, saving the tile art into the pattern | vectorcraft-cli: step 9 (object.pattern.done): command `object.pattern.done` is not available right  |
| `object.pattern.cancel` | refused | {} leave pattern editing mode, discarding changes | vectorcraft-cli: step 9 (object.pattern.cancel): command `object.pattern.cancel` is not available ri |
| `object.pattern.saveCopy` | refused | {name? (trimmed; blank: <pattern> copy)} while editing, save the current tile as a new pattern swatch → {name} | vectorcraft-cli: step 9 (object.pattern.saveCopy): command `object.pattern.saveCopy` is not availabl |
| `object.repeat.radial` | verified | {ids?, instances?: n (8), radius?: pt} radial repeat of the selection (or switch the selected repeat to radial) → {id} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 1080.0 |
| `object.repeat.grid` | verified | {ids?, hSpacing?: pt, vSpacing?: pt (¼ of the art size), rows?: n (3), cols?: n (3)} grid repeat of the selection → {id} | `inspect.layers{id=1}.bounds.width`: 400.0 → 1400.0 |
| `object.repeat.mirror` | verified | {ids?, angle?: deg (90 = vertical axis), offset?: pt (10)} mirror repeat of the selection → {id} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 507.824 |
| `object.repeat.release` | verified | {} release the selected repeats back to their source art → {ids} | `inspect.layers{id=1}.bounds.width`: 1400.0 → 400.0 |
| `object.repeat.options` | ran | {instances?, radius?, reverseOverlap?, startAngle?, endAngle?, center?: [x,y] \| hSpacing?, vSpacing?, rows?, cols?, gridType?, flipRows?, f… | no change in inspect/json; result=null |
| `object.repeat.expand` | verified | {} replace the selected repeats by groups of their instances → {ids} | `inspect.layers{id=1}.children{id=7}.children{id=3}.anchors`: 4 → <removed> |
| `object.intertwine.make` | verified | {ids?: two or more objects (default: the selection)} put the objects in an Intertwine group and choose the Intertwine tool, which arranges i… | `inspect.layers{id=1}.children{id=3}.anchors`: 4 → <removed> |
| `object.intertwine.edit` | ran | {} choose the Intertwine tool for the selected Intertwine group (Esc or Enter goes back to the tool before) | no change in inspect/json; result={"id": 7} |
| `object.intertwine.release` | verified | {} give the objects of the selected Intertwine groups back as they were made, dropping the arranged areas → {ids} | `inspect.layers{id=1}.children{id=7}.bounds.height`: 120.0 → <removed> |
| `object.intertwine.arrange` | refused | {id?: Intertwine group (default: the selected one), at?: [x,y] (the overlap area under this point, as a click picks it) \| area?: [[x,y]…] (… | vectorcraft-cli: step 11 (object.intertwine.arrange): invalid parameters for `object.intertwine.arra |
| `object.objectsOnPath.attach` | verified | {path?: id of the path to attach to (without it: choose the Objects on Path tool, whose click on a path attaches the selection to it), ids?:… | `inspect.tool`: selection → objectsOnPath |
| `object.objectsOnPath.options` | refused | {ids?: Objects on Path groups or objects in them (default: the selection), pivot?: 0-8 (the reference point of each object that attaches to … | vectorcraft-cli: step 10 (object.objectsOnPath.options): command `object.objectsOnPath.options` is n |
| `object.objectsOnPath.expand` | refused | {ids?: Objects on Path groups or objects in them (default: the selection)} make the groups plain groups of the path and the objects where th… | vectorcraft-cli: step 10 (object.objectsOnPath.expand): command `object.objectsOnPath.expand` is not |
| `object.liquify` | verified | {tool: warp\|twirl\|pucker\|bloat\|scallop\|crystallize\|wrinkle, points: [[x,y,pressure?]…] (the brush stroke; pen pressure 0..1, default 1… | `inspect.layers{id=1}.children{id=2}.anchors`: 4 → 17 |
| `object.puppetWarp` | verified | {id?\|ids? (default: selection), pins: [[x,y]…] (current pin positions), moved: [[x,y]…] (targets, same length), angles?: [deg\|null…] (same… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 507.82399967162263 |
| `object.puppetWarp.pins` | ran | {id?\|ids? (default: selection), expand?: pt} → {ids, pins, moved, angles, expand, rest: true, auto} the Puppet Warp pins on the art: pins =… | no change in inspect/json; result={"angles": [null, null, null], "auto": true, "expand": 3.0, "ids": |
| `object.setOverprint` | verified | {fill?: bool, stroke?: bool, item?: appearance item index\|null, ids?\|id?, target?: "object"\|"contents"} make fills and/or strokes overpri… | `doc.layers{id=1}.kind.children{id=2}.appearance.items[0].overprint`: <absent> → True |
| `object.flattenTransparency` | ran | {preset?: "high"\|"medium"\|"low" or a saved preset's name (see flattener.presets.list; default medium), balance?: 0..100 (raster/vector bal… | no change in inspect/json; result={"ids": [2, 3], "options": {"antiAlias": true, "balance": 75.0, "c |
| `object.expand` | verified | {object?: true (type → outlines, live shapes → paths, effects baked, blends → groups of their steps, repeats → groups of their instances, In… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 508.32399999999996 |
| `object.expand.info` | read-ok | {} what each Expand option would change in the selection → {object, fill, stroke, gradient, appearance} (true: something to expand; gradient… | no change in inspect/json; result={"appearance": false, "fill": false, "gradient": false, "object":  |
| `object.slice.make` | ran | {ids?} make each selected object (or ids) an object slice: its slice follows the object's bounds → {ids: the new object slices} | no change in inspect/json; result={"ids": [2, 3]} |
| `object.slice.release` | ran | {} release the selected slices: an object slice leaves its object as it was, a user slice becomes an unpainted rectangle; the objects end up… | no change in inspect/json; result={"ids": [2]} |
| `object.slice.fromGuides` | verified | {} replace the user slices with the grid the ruler guides cut the artboards into (two vertical and two horizontal guides give 9) → {ids} | `doc.slices{id=7}.id`: <absent> → 7 |
| `object.slice.fromSelection` | verified | {ids?\|id?} a user slice over the visual bounds of the selected objects (or ids), selected → {id} | `inspect.selection[0]`: 2 → <removed> |
| `object.slice.duplicate` | verified | {dx?: pt (default 10), dy?: pt (default 10)} copy the selected slices as user slices with their options, offset by dx, dy; the copies are se… | `inspect.selection[0]`: 2 → <removed> |
| `object.slice.combine` | refused | {} replace the two or more selected slices with one user slice over their bounds (the first one's options; object slices are released) → {id… | vectorcraft-cli: step 11 (object.slice.combine): invalid parameters for `object.slice.combine`: sele |
| `object.slice.divide` | verified | {rows?: slices down, rowHeight?: pt per slice, columns?: slices across, columnWidth?: pt per slice} cut each selected slice into a grid of u… | `inspect.selection[0]`: 2 → <removed> |
| `object.slice.deleteAll` | ran | {} delete every user slice and release every object slice → {count} | no change in inspect/json; result={"count": 2} |
| `object.slice.options` | read-ok | {kind?: "image"\|"noImage"\|"htmlText" (object slices of type only), name?, url?, target?, message?, alt?: (image), text?: cell text; HTML a… | no change in inspect/json; result={"alt": "", "background": "", "hAlign": "default", "htmlText": fal |
| `object.slice.clipToArtboard` | verified | {on?: bool} toggle (or set) Clip to Artboard: on, slices are clipped to the artboards and auto slices fill them; off, auto slices cover the … | `doc.slices_clip_to_artboard`: <absent> → False |
| `object.slice.create` | verified | {x, y, width, height} a user slice over that rectangle, selected (the Slice tool's drag) → {id} | `inspect.selection[0]`: 2 → <removed> |
| `object.slice.setRect` | refused | {id: user slice, x, y, width, height} move or resize a user slice (an object slice follows its object) → {id} | vectorcraft-cli: step 9 (object.slice.setRect): invalid parameters for `object.slice.setRect`: #2 is |
| `object.slice.move` | ran | {slices?: [id…] (default: the selected slices), dx, dy} move the slices: user slices move, object slices move their objects → {ids} | no change in inspect/json; result={"ids": []} |
| `object.slice.delete` | ran | {slices?: [id…] (default: the selected slices)} delete the user slices and release the object slices (their objects stay) → {count} | no change in inspect/json; result={"count": 0} |
| `object.slice.select` | verified | {slices?: [id…] (user slice ids or ids of objects with an object slice; none: deselect the slices), toggle?: bool (Shift: add the unselected… | `inspect.selection[0]`: 2 → <removed> |
| `object.vectorHalftone` | verified | {shape?: "circle"\|"ellipse"\|"square"\|"diamond"\|"line" (circle), frequency?: lines per inch 1–300 (20), angle?: deg (45; CMYK: the black … | `inspect.layers{id=1}.bounds.width`: 400.0 → 399.82185051202197 |

## addon (59)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `addon.arrange.grid` | verified | {layout?: "grid" (rows and columns) \| "row" (one row) \| "column" (one column), columns?: 1..10000 (grid; default ⌈√count⌉; never more than… | `inspect.layers{id=1}.bounds.width`: 400.0 → 311.0 |
| `addon.arrange.swap` | verified | {size?: false (true: each also takes the other's width and height), scaleStrokes?: the Scale Strokes & Effects preference} swap the places (… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 527.824 |
| `addon.arrange.replace` | verified | {fit?: "keep" (the copy keeps its size) \| "bounds" (scaled to the replaced object's width and height) \| "proportional" (scaled to fit insi… | `inspect.layers{id=1}.children{id=2}.anchors`: 4 → <removed> |
| `addon.arrange.size` | verified | {width?: pt, height?: pt (at least one; each 0.001..1000000), proportional?: false (with only one of them given, the other follows in propor… | `inspect.layers{id=1}.children{id=2}.bounds.width`: 200.0 → 100.0 |
| `addon.arrange.groupOverlapping` | ran | {} group the selected objects (the top-level ones, at most 20000) wherever their visual bounds overlap or touch, chains included (when A ove… | no change in inspect/json; result={"grouped": 0, "groups": []} |
| `addon.arrange.randomizeOpacity` | verified | {min?: % 0..100 (30), max?: % 0..100 (100; not less than min), seed?: whole number (0; the same seed, objects and range give the same opacit… | `inspect.layers{id=1}.children{id=3}.opacity`: <absent> → 0.7697960138320923 |
| `addon.arrange.sort` | ran | {by?: "width" \| "height" \| "area" (width × height) \| "x" (left edge) \| "y" (top edge) \| "opacity" (%) \| "stacking" (stacking order, fr… | no change in inspect/json; result={"count": 2} |
| `addon.cleanup.simplify` | ran | {tolerance?: 1..100 (20; higher removes more anchors and lets the outline move further from where it was, up to tolerance × 0.02 pt), protec… | no change in inspect/json; result={"after": 8, "before": 8, "ids": [2, 3]} |
| `addon.cleanup.check` | ran | {scope?: "selection"\|"document" (default: the selection, or the document while nothing is selected), kinds?: [kind…] (default: all: emptyTe… | no change in inspect/json; result={"findings": [], "scope": "selection", "total": 0} |
| `addon.cleanup.show` | refused | {kind: kind (see addon.cleanup.check), scope?: "selection"\|"document"} select the objects with that issue → {kind, count, ids, artboards} | vectorcraft-cli: step 9 (addon.cleanup.show): invalid parameters for `addon.cleanup.show`: unknown i |
| `addon.cleanup.fix` | ran | {scope?: "selection"\|"document", kinds?: [kind…] (default: all; see addon.cleanup.check)} fix the issues addon.cleanup.check finds, in up t… | no change in inspect/json; result={"fixed": {}, "scope": "selection", "total": 0} |
| `addon.cleanup.deepUngroup` | ran | {includeClipGroups?: bool (false: clipping groups, and the art inside them, stay as they are; true: they are ungrouped too and their clippin… | no change in inspect/json; result={"ids": [2, 3], "ungrouped": 0} |
| `addon.cleanup.rejoin` | ran | {gap?: pt 0..6 (0.1), ids?: [id…] (default: the selection)} weld the open paths under the objects whose ends lie within the gap of each othe… | no change in inspect/json; result={"ids": [], "joined": 0, "removed": 0} |
| `addon.cleanup.breakText` | refused | {by?: "lines"\|"paragraphs"\|"words"\|"glyphs" (lines), ids?: [id…] (default: the selection)} each horizontal point or area type object beco… | vectorcraft-cli: step 9 (addon.cleanup.breakText): Select horizontal point or area type whose text f |
| `addon.cleanup.combineText` | refused | {ids?: [id…] (default: the selection)} merge one-line horizontal point type into as few objects as it can, every glyph staying where it was:… | vectorcraft-cli: step 9 (addon.cleanup.combineText): Select two or more one-line point type objects  |
| `addon.cleanup.joinText` | refused | {ids?: [id…] (default: the selection)} join one-line horizontal point type into one point type object, as one undo step: pieces turned and s… | vectorcraft-cli: step 9 (addon.cleanup.joinText): Select two or more one-line point type objects to  |
| `addon.cleanup.removeBreaks` | refused | {kind: "line"\|"paragraph", ids?: [id…]} remove the forced line breaks (line) or paragraph returns (paragraph) in the characters selected wi… | vectorcraft-cli: step 9 (addon.cleanup.removeBreaks): No line breaks to remove |
| `addon.cleanup.splitText` | refused | {} while a Type tool edits horizontal point or area type: the text before the selected characters, they and the text after become point type… | vectorcraft-cli: step 9 (addon.cleanup.splitText): command `addon.cleanup.splitText` is not availabl |
| `addon.cleanup.alignInPlace` | refused | {align: "left"\|"center"\|"right", ids?: [id…] (default: the selection)} align every paragraph of each horizontal point type object so, movi… | vectorcraft-cli: step 9 (addon.cleanup.alignInPlace): Select point type |
| `addon.cleanup.resetTextTransform` | refused | {scale?: bool (false: the horizontal scale stays; true: it goes too, the object's and every character's), ids?: [id…] (default: the selectio… | vectorcraft-cli: step 9 (addon.cleanup.resetTextTransform): Select point type |
| `addon.cleanup.replaceFonts` | refused | {font?: family (default: the default type font, Source Sans 3; any of its names)} set every character of the document's type (the type in th… | vectorcraft-cli: step 9 (addon.cleanup.replaceFonts): No fonts are missing |
| `addon.color.select` | verified | {kind: "spotColors" (objects painted with a spot colour swatch, solid or in a gradient's stops) \| "colorEffects" (objects carrying a visibl… | `inspect.selection[0]`: 2 → <removed> |
| `addon.color.filter` | refused | {effect: a colour adjustment's effect id (adjust.brightnessContrast, adjust.curves, adjust.hueSaturation, adjust.levels, adjust.shiftToColor… | vectorcraft-cli: step 9 (addon.color.filter): invalid parameters for `addon.color.filter`: `test` is |
| `addon.color.printFixes` | refused | {scope?: "selection" (the selection, or `ids`; by default, the document while nothing is selected) \| "document" (every layer), inkLimit?: t… | vectorcraft-cli: step 9 (addon.color.printFixes): invalid parameters for `addon.color.printFixes`: P |
| `addon.color.nearestSwatch` | ran | {library?: a swatch library's id or name (swatch.library.list: the built-in ones, and the colour books and libraries the user saved or loade… | no change in inspect/json; result={"colors": [{"hex": "#ffffff", "matches": [{"deltaE": 0.0, "hex":  |
| `addon.color.applyNearestSwatch` | ran | {library?: as addon.color.nearestSwatch (default: "document"), fill?: true, stroke?: true, ids?: [id…] (default: the selection)} give each s… | no change in inspect/json; result={"added": [], "changed": 0, "swatches": ["White", "Black"]} |
| `addon.color.swatchLegend` | verified | {names?: [swatch name…] (default: every colour swatch of the document, in panel order), columns?: 1..50 (4), size?: chip side in pt 8..1000 … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 996.0 |
| `addon.document.saveTimestampedCopy` | ran | {folder? (default: the document's own folder; needed for a document never saved), format?: vectorcraft\|pdf\|svg\|svgz\|ai\|eps (default: th… | no change in inspect/json; result={"bytes": 31825, "format": "vectorcraft", "path": "<scratch> |
| `addon.document.exportAllOpen` | ran | {folder, format?: vectorcraft\|pdf\|svg\|svgz\|ai\|eps (default: pdf)} write a copy of every open document, in tab order, to `folder` as Fil… | no change in inspect/json; result={"failed": [], "files": [{"path": "<scratch> |
| `addon.document.symbolsFromLayers` | verified | {layers?: [layer id…] (top-level layers; default: those highlighted in the Layers panel when two or more are, else every one), replace?: boo… | `doc.symbols[0].art.id`: <absent> → 7 |
| `addon.pathtools.erase` | ran | {points: [[x, y] \| [x, y, pressure 0..1]…] (the brush's path, at most 100000 points), diameter?: pt 0.1..2500 (20; a point's pressure scale… | no change in inspect/json; result={"ids": [2, 3], "removed": 0} |
| `addon.pathtools.extend` | refused | {id, subpath?: index (0), end: "start"\|"end", length?: pt (negative shortens; never all of it), to?: [x, y] (instead of length: the length … | vectorcraft-cli: step 9 (addon.pathtools.extend): invalid parameters for `addon.pathtools.extend`: t |
| `addon.pathtools.inspect` | ran | {id, x, y, tolerance?: pt (3; how near an anchor counts as over it)} what the path reads at the point nearest (x, y): {subpath, closed, anch… | no change in inspect/json; result={"anchor": {"angle": 90.0, "in": null, "index": 0, "out": null, "s |
| `addon.pathtools.setAnchor` | verified | {x?, y?: pt (on the page), inLength?, outLength?: pt (0 retracts), inAngle?, outAngle?: degrees counter-clockwise} move the selected anchors… | `inspect.layers{id=1}.bounds.width`: 400.0 → 212.2729944406843 |
| `addon.pathtools.smooth` | verified | {ratio?: 0.1..0.5 (0.3905: a square's corners make a circle)} make the selected anchors smooth: a lone handle is mirrored; without handles, … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 532.6752678248012 |
| `addon.pathtools.corner` | verified | {retract?: bool (true: the handles go; false: they stay where they are and move apart)} make the selected anchors corners, as one undo step … | `inspect.layers{id=1}.children{id=3}.kind`: Ellipse → Path |
| `addon.pathtools.equalize` | verified | {} give each selected anchor's two handles their average length (a missing one is made opposite the other), as one undo step → {anchors (cha… | `inspect.layers{id=1}.children{id=3}.kind`: Ellipse → Path |
| `addon.pathtools.removeKeepShape` | refused | {} remove the direct-selected anchors, refitting the handles beside each so the outline keeps its shape as best it can, as one undo step; op… | vectorcraft-cli: step 9 (addon.pathtools.removeKeepShape): invalid parameters for `addon.pathtools.r |
| `addon.pathtools.addPoints` | verified | {count?: 1..100 (1)} add count anchors to each selected segment (a segment between two selected anchors, or every segment of a path selected… | `inspect.layers{id=1}.bounds.y`: 100.0 → 99.99999999999999 |
| `addon.pathtools.close` | refused | {mode?: "handles" (keep the ends' handles)\|"straight" (a straight closing segment)\|"smooth" (the ends made smooth), ratio?: 0.1..0.5 (0.39… | vectorcraft-cli: step 9 (addon.pathtools.close): invalid parameters for `addon.pathtools.close`: sel |
| `addon.pathtools.crossings` | ran | {cut?: bool (false: add anchors where the paths cross; true: also cut them there), selfCrossings?: bool (false: where a path crosses itself … | no change in inspect/json; result={"crossings": 0, "ids": []} |
| `addon.pathtools.slideAnchor` | verified | {id, subpath?: index (0), anchor: index, t: -0.98..0.98 (where to: positive, a curve parameter on the segment after the anchor; negative, ba… | `inspect.layers{id=1}.children{id=2}.kind`: Rectangle → Path |
| `addon.pathtools.divideDashes` | verified | {dash?: pt 0.01..1000000 (10), gap?: pt 0..1000000 (0: the pieces touch), fit?: bool (false: exact lengths, the last piece of each run what … | `inspect.layers{id=1}.bounds.x`: 100.0 → 99.99999999999999 |
| `addon.pathtools.expandDashes` | refused | {ids?: [id…] (default: the selection)} turn the dashed stroke of each path and compound path under the objects into separate open paths, one… | vectorcraft-cli: step 9 (addon.pathtools.expandDashes): invalid parameters for `addon.pathtools.expa |
| `addon.pathtools.shape.create` | verified | {center: [x, y], kind?: "rectangle"\|"ellipse"\|"polygon" (default)\|"star"\|"ring"\|"arrow"\|"cross"\|"heart"\|"gear"\|"bubble" (a speech b… | `inspect.objects`: 6 → 7 |
| `addon.pathtools.shape.set` | refused | {id, kind?, center?, width?, height?, rotation?, count?, a?, b?, radius?} change a parametric shape's numbers (as addon.pathtools.shape.crea… | vectorcraft-cli: step 9 (addon.pathtools.shape.set): invalid parameters for `addon.pathtools.shape.s |
| `addon.pathtools.shape.convert` | verified | {ids?: [id…] (default: the selection)} make each plain closed path that is a rectangle, an ellipse or a polygon with equal sides and corners… | `inspect.layers{id=1}.children{id=3}.kind`: Ellipse → Path |
| `addon.pathtools.cornerSet` | refused | {ids?: [id…] (the selection), anchors?: [index…] (of each path's outline with no corners cut; else its direct-selected anchors, or all of th… | vectorcraft-cli: step 9 (addon.pathtools.cornerSet): invalid parameters for `addon.pathtools.cornerS |
| `addon.pathtools.cornerRemove` | ran | {ids?: [id…] (the selection), anchors?: [index…] (of each path's outline with no corners cut; else its direct-selected anchors, or all of th… | no change in inspect/json; result={"corners": 4, "ids": [2]} |
| `addon.pathtools.mergeEdge` | refused | {a, b: two path ids (they needn't be selected), at: [x, y] (where), diameter?: pt 0.25..200 (20; how near `at` the edge is looked for), tole… | vectorcraft-cli: step 9 (addon.pathtools.mergeEdge): invalid parameters for `addon.pathtools.mergeEd |
| `addon.pathtools.movePointsTogether` | ran | {enabled?: bool (default: the opposite of now)} Keep Shared Points Together: whether anchors coincident (within the Shared Edge Merge Tool's… | no change in inspect/json; result={"enabled": true} |
| `addon.pen.append` | refused | {id, subpath?: index (default: the last open subpath), x, y, in?: [x, y], out?: [x, y], segment?: "straight" (the segment into the new ancho… | vectorcraft-cli: step 9 (addon.pen.append): invalid parameters for `addon.pen.append`: the path has  |
| `addon.pen.close` | refused | {id, subpath?: index (default: the last open subpath), segment?: "straight"\|"curved" (default: the closing segment takes the handles its en… | vectorcraft-cli: step 9 (addon.pen.close): invalid parameters for `addon.pen.close`: the path has no |
| `addon.pen.segment` | ran | {id, subpath?: index (0), segment: index, curved: bool} make a segment straight (its handles retracted) or curved (each end without a handle… | no change in inspect/json; result={"changed": false} |
| `addon.pen.removePoint` | verified | {id, subpath?: index (0), anchor: index, plain?: bool (false: the handles beside it are refitted so the outline keeps its shape, and an open… | `inspect.layers{id=1}.children{id=2}.anchors`: 4 → 3 |
| `addon.pen.togglePoint` | verified | {id, subpath?: index (0), anchor: index, ratio?: 0.1..0.5 (0.3905)} a smooth anchor becomes a corner with its handles where they are; any ot… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 522.5506772295117 |
| `addon.pen.reshape` | verified | {id, subpath?: index (0), segment: index, t?: 0..1 (where it was grabbed, 0.5; held to 0.05..0.95), dx, dy: pt, mode?: "free" (both handles … | `inspect.layers{id=1}.children{id=2}.bounds.width`: 200.0 → 200.63777722999333 |
| `addon.pen.nextSegment` | ran | {curved: bool} whether a click with the Smart Pen Tool adds a curved segment or a straight one (the tool's `next` option, kept with the pref… | no change in inspect/json; result={"next": "straight"} |
| `addon.pen.closeJoin` | refused | {} with exactly two open path ends direct-selected, join them as path.join does; else close the selected open paths keeping their ends' hand… | vectorcraft-cli: step 9 (addon.pen.closeJoin): invalid parameters for `addon.pathtools.close`: selec |

## select (53)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `select.all` | verified | {} → {count}; while the Type tool edits text, all of that text instead → {editing, start, end} (byte offsets) | `inspect.selectionBounds.height`: 120.0 → 507.82399999999996 |
| `select.allOnArtboard` | verified | {artboard?: index (0-based; the app passes the active one; default: the first)} | `inspect.selectionBounds.height`: 120.0 → 507.82399999999996 |
| `select.none` | verified | {} | `inspect.selection[0]`: 2 → <removed> |
| `select.reselect` | ran | {} | no change in inspect/json; result=null |
| `select.inverse` | verified | {} | `inspect.selection[0]`: 2 → 4 |
| `select.nextAbove` | verified | {} | `inspect.selection[0]`: 2 → 3 |
| `select.nextBelow` | ran | {} | no change in inspect/json; result=null |
| `select.set` | ran | {ids: [id…]} all ids must be non-negative integers naming existing objects → {count, ids} (resulting selection) | no change in inspect/json; result={"count": 2, "ids": [2, 3]} |
| `select.add` | ran | {ids: [id…]} all ids must be non-negative integers naming existing objects → {count, ids} (resulting selection) | no change in inspect/json; result={"count": 2, "ids": [2, 3]} |
| `select.toggle` | verified | {id} or {ids: [id…]}: each selected one leaves the selection, the others join it; all ids must be non-negative integers naming existing obje… | `inspect.selection[0]`: 2 → 3 |
| `select.key` | ran | {id?: a selected top-level object (not a layer, a compound-path member or an object inside another selected object); one of two or more or t… | no change in inspect/json; result={"key": null} |
| `select.anchors` | verified | {id, anchors: [[subpath, anchor]…], mode: "set"\|"add"\|"toggle"} | `inspect.selection[1]`: 3 → <removed> |
| `select.segments` | verified | {id, segments: [[subpath, segment]…], mode?: "set"\|"add"\|"toggle"} select path segments; their endpoints move with them, Delete removes on… | `inspect.selection[0]`: 2 → <removed> |
| `select.anchorsMany` | verified | {items: [{id, anchors}], mode?: "set"\|"add"\|"toggle"\|"subtract" (set by default; add: true is mode add), add?: bool (an older way to ask … | `inspect.selection[0]`: 2 → <removed> |
| `select.color` | refused | {fill?: colour, stroke?: colour (as paint.setFill's color; at least one)} select the objects whose fill (and stroke) reads as that colour in… | vectorcraft-cli: step 9 (select.color): invalid parameters for `select.color`: `fill`: not a colour: |
| `select.same.fillColor` | verified | {} the objects filled with the first selected object's fill colour (any tint of its global or spot swatch, the same tint with prefs selectSa… | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.same.strokeColor` | verified | {} the objects stroked with the first selected object's stroke colour (tints and compound paths as select.same.fillColor) | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.same.strokeWeight` | verified | {} | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.same.fillAndStroke` | verified | {} the objects with the first selected object's fill and stroke colours (tints, compound paths and Live Paint faces as select.same.fillColor… | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.same.opacity` | verified | {} | `inspect.selectionBounds.height`: 120.0 → 507.82399999999996 |
| `select.same.blendingMode` | verified | {} | `inspect.selectionBounds.height`: 120.0 → 507.82399999999996 |
| `select.same.appearance` | verified | {} | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.same.shapeType` | verified | {} | `inspect.selection[1]`: 3 → <removed> |
| `select.object.allOnSameLayers` | verified | {} | `inspect.selectionBounds.height`: 120.0 → 507.82399999999996 |
| `select.object.clippingMasks` | verified | {} | `inspect.selection[0]`: 2 → <removed> |
| `select.object.textObjects` | verified | {} | `inspect.selection[0]`: 2 → 5 |
| `select.object.strayPoints` | verified | {} | `inspect.selection[0]`: 2 → <removed> |
| `select.object.openPaths` | verified | {} | `inspect.selection[0]`: 2 → <removed> |
| `select.same.graphicStyle` | refused | {} the objects linked to the graphic style the first selected object is linked to (compound paths as select.same.fillColor) | vectorcraft-cli: step 9 (select.same.graphicStyle): invalid parameters for `select.same.graphicStyle |
| `select.same.appearanceAttribute` | verified | {item?: appearance item index} the objects sharing an appearance attribute of the first selected object: its fill or stroke `item` (default:… | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.globalEdit` | refused | {appearance?: bool, size?: bool, artboards?: "all" \| range such as "1, 3-5", includeCanvas?: bool} (each defaults to the Global Edit Option… | vectorcraft-cli: step 9 (select.globalEdit): command `select.globalEdit` is not available right now: |
| `select.globalEditOptions` | ran | {appearance?: bool, size?: bool, artboards?: "all" \| range such as "1, 3-5", includeCanvas?: bool} set the options Start Global Edit matche… | no change in inspect/json; result={"appearance": false, "artboards": "all", "count": 0, "includeCanv |
| `select.magicWand` | verified | {id, mode?: set\|add\|subtract} select objects similar to `id` by the Magic Wand settings → {count} | `inspect.selectionBounds.height`: 120.0 → 450.0 |
| `select.font` | verified | {family, style?} select the text objects using the font, and the instances of the symbols whose art uses it, that are not hidden or locked, … | `inspect.selection[0]`: 2 → <removed> |
| `select.same.symbolInstance` | verified | {} → {count} | `inspect.selection[0]`: 2 → <removed> |
| `select.same.linkBlockSeries` | ran | {} select every frame of the threads of the selected type objects (and of the type inside selected groups); type in no thread selects itself… | no change in inspect/json; result={"count": 1} |
| `select.same.fontFamily` | ran | {} → {count} | no change in inspect/json; result={"count": 1} |
| `select.same.fontFamilyStyle` | ran | {} → {count} | no change in inspect/json; result={"count": 1} |
| `select.same.fontFamilyStyleSize` | ran | {} → {count} | no change in inspect/json; result={"count": 1} |
| `select.same.fontSize` | ran | {} → {count} | no change in inspect/json; result={"count": 1} |
| `select.same.textFillColor` | ran | {} → {count} | no change in inspect/json; result={"count": 1} |
| `select.same.textStrokeColor` | ran | {} → {count} | no change in inspect/json; result={"count": 1} |
| `select.object.directionHandles` | ran | {} direct-select every anchor (showing all handles) of the selected paths and the paths inside the selected objects, leaving out paths that … | no change in inspect/json; result={"anchors": 8} |
| `select.object.pointText` | verified | {} → {count} | `inspect.selection[0]`: 2 → 5 |
| `select.object.areaText` | verified | {} → {count} | `inspect.selection[0]`: 2 → <removed> |
| `select.object.brushStrokes` | verified | {} → {count} | `inspect.selection[0]`: 2 → <removed> |
| `select.object.bristleBrushStrokes` | verified | {} objects whose topmost stroke has a bristle brush (type bristle in brush.list), whatever the brush is named → {count} | `inspect.selection[0]`: 2 → <removed> |
| `select.save` | verified | {name?} save the current selection under a name, in the document (default "Selection N"; an existing name is replaced; at most 25, names up … | `doc.saved_selections[0].name`: <absent> → Selection 1 |
| `select.update` | refused | {} make the saved selection last recalled (`select.recall`) hold the selected objects instead of its own, in one undo step → {name} | vectorcraft-cli: step 9 (select.update): command `select.update` is not available right now: no save |
| `select.recall` | refused | {name} select the objects of a saved selection, leaving out those deleted since and those that are hidden or locked, inside a hidden or lock… | vectorcraft-cli: step 9 (select.recall): command `select.recall` is not available right now: no save |
| `select.editSaved` | refused | {name, newName?: rename, delete?: bool} \| {edits: [{name, newName?, delete?}…]} rename or delete saved selections, all in one undo step; na… | vectorcraft-cli: step 9 (select.editSaved): command `select.editSaved` is not available right now: n |
| `select.savedList` | ran | {} → [name…] for the active document | no change in inspect/json; result=[] |
| `select.object.slices` | verified | {} select every user and object slice → {count} | `inspect.selection[0]`: 2 → <removed> |

## document (35)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `document.activate` | ran | {index} | no change in inspect/json; result=null |
| `document.inspect` | ran | {depth?, childLimit?, ids?: [id…] (list just these nodes, of any level, in this order, under `nodes` in place of `layers`; an unknown id is … | no change in inspect/json; result={"artboards": [{"height": 792.0, "name": "Artboard 1", "width": 61 |
| `document.node` | ran | {id, summary?: compact summary, depth?: child levels in the summary (default all), childLimit?: children shown per node (default all; a leve… | no change in inspect/json; result={"appearance": {"items": [{"kind": "fill", "paint": {"color": {"b" |
| `document.find` | ran | {name?: substring of the Layers panel name, kind?: panel label such as Group; Path; Type or Image (exact), text?: substring of type content,… | no change in inspect/json; result={"matches": [], "total": 0} |
| `document.json` | read-ok | {} → complete document model | no change in inspect/json; result={"artboards": [{"id": 1, "name": "Artboard 1", "rect": {"x0": 0.0, |
| `document.setUnits` | ran | {units: "Points"\|"Picas"\|"Inches"\|"Millimeters"\|"Centimeters"\|"Pixels"\|"Feet & Inches"\|"Meters"\|"Yards"\|"Feet"} the document's unit… | no change in inspect/json; result=null |
| `document.switchUnits` | verified | {} the document's units become the next of Points, Picas, Inches, Millimeters, Centimeters, Pixels, Feet & Inches, Meters, Yards and Feet (t… | `inspect.units`: Points → Picas |
| `document.rulerOrigin` | ran | {artboard?: index=0 (the active artboard, which artboard rulers measure from)} → {x, y} the rulers' zero point, in absolute document points | no change in inspect/json; result={"x": 0.0, "y": 0.0} |
| `document.setRulerOrigin` | verified | {x, y, artboard?: index=0} set the rulers' zero point in absolute document points: the document's with global rulers, that artboard's with a… | `doc.artboard_ruler_origins.1.x`: <absent> → 100.0 |
| `document.resetRulerOrigin` | ran | {artboard?: index=0} reset the rulers' zero point to that artboard's top-left corner (with artboard rulers, that artboard's own zero point) | no change in inspect/json; result={"x": 0.0, "y": 0.0} |
| `document.open` | verified | {path \| name \| dataBase64 (a file's path, or its name with its bytes), pages?: "2-3, 5" (PDF/.ai: 1-based, default all; one artboard each)… | `inspect.artboards[0].height`: 792.0 → 200.0 |
| `document.serialize` | ran | {format?: vectorcraft (default)\|template\|svg\|svgz\|pdf\|ai\|png\|jpg\|webp\|gif\|png8\|txt\|dxf\|eps\|emf\|wmf\|tiff\|bmp\|tga\|psd (ait,… | no change in inspect/json; result={"dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZnQiLAogICJ2ZXJzaW |
| `document.export` | ran | {path?, format?: svg\|svgz\|pdf\|ai\|png\|jpg\|webp\|gif\|png8\|txt\|dxf\|eps\|emf\|wmf\|tiff\|bmp\|tga\|psd\|vectorcraft\|template (default… | no change in inspect/json; result={"bytes": 5975, "dataBase64": "iVBORw0KGgoAAAANSUhEUgAAAmQAAAMYCAY |
| `document.exportSelection` | ran | {path?, format?: png\|jpg\|webp\|svg\|svgz\|pdf\|ai\|gif\|png8\|tiff\|bmp\|tga\|psd\|txt\|dxf\|eps\|emf\|wmf\|vectorcraft\|template (default… | no change in inspect/json; result={"bounds": [99.5, 99.5, 401.0, 121.0], "bytes": 2482, "dataBase64" |
| `document.exportForScreens` | ran | {folder?, zip?: false (one .zip of every file, each deflated or stored, whichever is smaller: no folder → {name, dataBase64, bytes, files: [… | no change in inspect/json; result={"files": [{"dataBase64": "iVBORw0KGgoAAAANSUhEUgAAAmQAAAMYCAYAAAB |
| `document.exportPresets.list` | read-ok | {} → {presets: [{name, builtIn, settings}]} the built-in batch export presets (Logo Package, Print-Ready PDF), then the saved ones; any name… | no change in inspect/json; result={"presets": [{"builtIn": true, "name": "Logo Package", "settings": |
| `document.exportPresets.save` | ran | {name, settings: {formats, settings, preset, name, prefix, counterStart, counterPer, folders, subfolders, includeBleed, includeArtboardFill,… | no change in inspect/json; result={"created": true, "name": "Test", "settings": {}} |
| `document.exportPresets.delete` | refused | {name} delete a saved batch export preset (built-in ones stay) → {deleted} | vectorcraft-cli: step 9 (document.exportPresets.delete): invalid parameters for `document.exportPres |
| `document.exportPresets.import` | refused | {path? \| data?: file text \| dataBase64?, replace?: false (replace saved presets of the same names; else the imported ones get a number)} a… | vectorcraft-cli: step 9 (document.exportPresets.import): invalid parameters for `document.exportPres |
| `document.exportPresets.export` | refused | {names?: [preset names, built-in ones too] (default: every saved preset), path?} write the presets as a .vcexportpresets file (JSON); more t… | vectorcraft-cli: step 9 (document.exportPresets.export): invalid parameters for `document.exportPres |
| `document.formats` | read-ok | {} → {formats: [{id, label, extensions, mime, read, write, raster, options: {name: {type, default, description}}, plugin?: the id of the exp… | no change in inspect/json; result={"formats": [{"extensions": ["vectorcraft", "drawcraft"], "id": "v |
| `document.pdfInfo` | refused | {path \| name? \| dataBase64 (a file's path, or its bytes), password?, thumbnail?: page (1-based), thumbnailSize?: 160 (px, longest side), c… | vectorcraft-cli: step 9 (document.pdfInfo): cannot read PDF: PDF parser rejected the document: Inval |
| `document.exportForOffice` | ran | {path?, ppi?: 150 (72, 150, 300… pixels per inch), transparent?: false (else on white), artboard?: 0, acknowledgeLoss?: bool (write over the… | no change in inspect/json; result={"bytes": 17696, "dataBase64": "iVBORw0KGgoAAAANSUhEUgAABPsAAAZyCA |
| `document.exportSettings` | ran | {} → {settings}: the document.exportForScreens params the document last exported with ({} when never; saved with the document, the dialog re… | no change in inspect/json; result={"settings": {}} |
| `document.save` | ran | {path?, format?: vectorcraft\|template\|pdf\|svg\|svgz\|ai\|eps (default: the path's extension, else the document's own format), options?: {… | no change in inspect/json; result={"bytes": 31825, "dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZn |
| `document.rasterEffectsSettings` | ran | {resolution?: ppi (1–2400) \| "screen" (72) \| "medium" (150) \| "high" (300), colorModel?: "rgb"\|"cmyk" (the document's mode)\|"grayscale"… | no change in inspect/json; result={"addAround": 0.0, "antiAlias": true, "background": "transparent", |
| `document.info` | read-ok | {selectionOnly?, category?: document\|objects\|graphicStyles\|brushes\|spotColors\|patterns\|gradients\|symbols\|fonts\|fontDetails\|linkedI… | no change in inspect/json; result={"brushNames": ["3 pt. Round", "6 pt. Flat", "10 pt. Oval", "Charc |
| `document.exportPdf` | ran | {path?, preset?: "VectorCraft Default" (built-in or saved: pdf.preset.list), artboard? \| artboards?: [i…] \| range?: "1-3, 5" (1-based; def… | no change in inspect/json; result={"bytes": 9858, "dataBase64": "JVBERi0xLjcKJYCAgIAKCjEgMCBvYmoKPDw |
| `document.pdfSettings` | ran | {preset?, includeDocument?: false, …options of document.exportPdf} → {settings (the preset with the options applied), presets: [name…], chan… | no change in inspect/json; result={"changed": [], "presets": ["VectorCraft Default", "High Quality P |
| `document.setup` | ran | {units?: "Points"\|"Inches"\|"Millimeters"\|…, bleed?: pt (all sides)\|[top, bottom, left, right]\|{top?, bottom?, left?, right?} (0–72 pt),… | no change in inspect/json; result={"backgroundContents": "transparent", "bleed": [0.0, 0.0, 0.0, 0.0 |
| `document.exportDxf` | ran | {path?, version?: R12\|R13\|R14\|2000\|2004\|2007\|2010\|2013\|2018 (default), unit?: mm (default; any unit name: pt, in, cm…), scale?: 1 (d… | no change in inspect/json; result={"bytes": 23273, "dataBase64": "ICAwClNFQ1RJT04KICAyCkhFQURFUgogID |
| `document.exportEps` | ran | {path?, level?: 2\|3 (default; PostScript language level: 3 writes smooth gradients and masks transparent image pixels out, 2 steps gradient… | no change in inspect/json; result={"bytes": 38881, "dataBase64": "xdDTxh4AAACBKgAAAAAAAAAAAACfKgAAQm |
| `document.dxfInfo` | refused | {path} or {name?, dataBase64} what a DXF drawing holds → {version (2018, R12…), units (its drawing unit: Millimeters, Inches, Unitless…), la… | vectorcraft-cli: step 9 (document.dxfInfo): not a DXF drawing |
| `document.exportForWeb` | ran | {path?, preset?: a webExport.presets name (its settings, then these keys), format?: gif (default)\|jpg\|png8\|png24, reduction?: perceptual\… | no change in inspect/json; result={"bytes": 3721, "files": [{"dataBase64": "R0lGODlhZAIYA8QAAP////// |
| `document.exportForWeb.preview` | ran | {…the settings of document.exportForWeb (preset?, format?…), slice?: n (1-based, from slice.list; default the whole image), kbps?: 56.6 (con… | no change in inspect/json; result={"bytes": 3721, "colors": [{"color": "#ffffff", "locked": false, " |

## path (34)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `path.create` | verified | {anchors: [{x, y, in?: [x,y], out?: [x,y]}], closed?: bool, d?: SVG path data} → {id} | `inspect.objects`: 6 → 7 |
| `path.appendAnchor` | verified | {id, x, y, in?: [x,y], out?: [x,y], subpath?: usize (the open subpath to extend, 0 included; an invalid or closed one is an error; default: … | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 4 |
| `path.close` | refused | {id, subpath?: usize (the open subpath to close, 0 included; default: the last open one), in?: [x,y] (handle into the first anchor), indepen… | vectorcraft-cli: step 9 (path.close): path is already closed |
| `path.moveAnchors` | verified | {dx, dy, patterns?: bool (Transform Patterns: pattern fills and strokes transform with the objects that move whole; default: prefs transform… | `inspect.layers{id=1}.children{id=4}.bounds.x`: 100.0 → 110.0 |
| `path.setHandle` | verified | {id, subpath?, anchor, which: "in"\|"out", x, y, independent?: bool} | `inspect.layers{id=1}.children{id=4}.bounds.height`: 150.0 → 253.125 |
| `path.moveAnchor` | verified | {id, subpath?, anchor, x, y} move one anchor to (x, y), its handles with it | `inspect.layers{id=1}.children{id=4}.bounds.height`: 150.0 → 450.0 |
| `path.setAnchors` | verified | {id, subpaths: [{anchors: [{x,y,in?,out?}], closed}]} replace a path's geometry | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 0 |
| `path.reverse` | verified | {ids?\|id?, subpath?: usize (reverse only this subpath of each path, 0 included; default: every subpath), reversed?: bool (true: every subpa… | `doc.layers{id=1}.kind.children{id=4}.kind.path.subpaths[0].anchors[0].p[0]`: 100.0 → 200.0 |
| `path.join` | refused | {ids?: [path, ...] (default: the selected paths; a compound path ID expands to its open member paths), subpaths?: [usize, usize] (which subp… | vectorcraft-cli: step 9 (path.join): path is already closed |
| `path.average` | verified | {axis?: "horizontal"\|"vertical"\|"both"} | `inspect.layers{id=1}.children{id=4}.bounds.height`: 150.0 → 0.0 |
| `path.averageJoin` | refused | {to: "corner"\|"smooth" (the joined anchor: corner retracts both handles, smooth pulls handles in line with the neighbours), ids?: [path, ..… | vectorcraft-cli: step 9 (path.averageJoin): invalid parameters for `path.averageJoin`: select two op |
| `path.convertAnchors` | ran | {to: "corner"\|"smooth"} convert the direct-selected anchors (all anchors of fully selected paths, every point of a selected blend's spine) … | no change in inspect/json; result=null |
| `path.deleteAnchors` | refused | {} delete the direct-selected anchors and their segments, opening closed paths there, and delete objects selected whole alongside them; what… | vectorcraft-cli: step 9 (path.deleteAnchors): command `path.deleteAnchors` is not available right no |
| `path.reshape` | verified | {id, x, y, dx, dy, tol=3, radius?} Reshape tool: grab the path at (x, y) (adding an anchor there unless one is within tol) and drag it by (d… | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 4 |
| `path.insertAnchor` | verified | {id, subpath?, segment, t: 0..1} | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 4 |
| `path.cutAtAnchors` | refused | {} cut the paths at their direct-selected anchors (one undo step): a closed path opens there, an open one becomes one path per piece; one of… | vectorcraft-cli: step 9 (path.cutAtAnchors): command `path.cutAtAnchors` is not available right now: |
| `path.freehand` | verified | {points: [[x,y]…] or [[x,y,pressure]…] or [[x,y,pressure,tiltX,tiltY,rotation]…] (pen pressure 0..1: the stroke keeps it, for Calligraphic a… | `inspect.objects`: 6 → 7 |
| `path.curvature` | verified | {points: [{x, y, corner?}], closed?, id?} create (or with id: replace) a path curving through the points → {id} | `inspect.objects`: 6 → 7 |
| `path.curvatureEdit` | refused | {id, subpath?, op: "move"\|"insert"\|"extend"\|"close", anchor?, segment?, t?, end?: "start"\|"end", from?: "keep"\|"smooth"\|"corner", corn… | vectorcraft-cli: step 9 (path.curvatureEdit): invalid parameters for `path.curvatureEdit`: x and y m |
| `path.removeAnchor` | verified | {id, subpath?, anchor, curvature?} remove one anchor, re-fitting the curve (with curvature: true, the curve where it was follows the remaini… | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 2 |
| `path.removeAnchors` | refused | {} remove the direct-selected anchors without opening their paths, refitting the curve round each; the anchor after each removed one is sele… | vectorcraft-cli: step 9 (path.removeAnchors): command `path.removeAnchors` is not available right no |
| `path.convertAnchor` | ran | {id, subpath?, anchor, to: "corner"\|"smooth", x?, y?} (smooth with x/y: out handle there, in handle mirrored; without: as the Curvature too… | no change in inspect/json; result=null |
| `path.reshapeSegment` | verified | {id, subpath?, segment, t, dx, dy, perpendicular?: bool} bend a segment so the point at t moves by (dx, dy); with perpendicular (Shift), bot… | `inspect.layers{id=1}.children{id=4}.bounds.width`: 200.0 → 214.7046445495384 |
| `path.split` | verified | {id, subpath?, segment, t} or {id, subpath?, anchor}: closed paths open there, open paths become two → {ids} | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 5 |
| `path.knife` | ran | {points: [[x,y]…]} cut closed shapes (selected, or all when nothing is selected) along the polyline → {ids} | no change in inspect/json; result={"ids": []} |
| `path.eraseRegion` | ran | {points: [[x,y]…] or [[x,y,pressure]…] (pen pressure 0..1), size?: pt (10), sizeMode?: "fixed" (default) \| "pressure" (Eraser Tool Options'… | no change in inspect/json; result={"ids": []} |
| `path.eraseSegments` | ran | {points: [[x,y]…], width?: pt (8)} erase the parts of selected paths under the drag → {ids} | no change in inspect/json; result={"ids": []} |
| `path.smoothRegion` | ran | {points: [[x,y]…], radius?: pt (12), fidelity?: pt (2.5)} smooth selected paths near the drag → {ids, before, after} | no change in inspect/json; result={"after": 0, "before": 0, "ids": []} |
| `path.joinScrub` | ran | {points: [[x,y]…], tolerance?: pt (12)} join the open-path endpoints scrubbed over → {id} | no change in inspect/json; result={"id": null} |
| `path.blob` | verified | {points: [[x,y]…] or [[x,y,pressure]…] (pen pressure 0..1), size?: pt (10), sizeMode?: "fixed" (default) \| "pressure" (Blob Brush Tool Opti… | `inspect.objects`: 6 → 7 |
| `path.setFillRule` | ran | {rule: "nonZero"\|"evenOdd", ids?\|id?} the fill rule of the paths and compound paths in ids or the selection (groups: those inside), as one… | no change in inspect/json; result={"changed": 0} |
| `path.mirrorCut` | verified | {axis?: "vertical"\|"horizontal"\|"free" (vertical), from?: [x,y], to?: [x,y] (free: the axis through both; vertical/horizontal: the axis th… | `inspect.layers{id=1}.children{id=4}.anchors`: 3 → 4 |
| `path.lineCut` | refused | {from: [x,y], to: [x,y]} split the selected paths and compound paths along the line through both points, extended across the art: filled sha… | vectorcraft-cli: step 9 (path.lineCut): invalid parameters for `path.lineCut`: missing point `from`  |
| `path.rectCut` | ran | {rect: [x, y, width, height]} or {from: [x,y], to: [x,y]} (opposite corners) crop the selected paths and compound paths to the rectangle as … | no change in inspect/json; result={"ids": [], "removed": 0} |

## text (33)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `text.create` | verified | {x, y, text, rotation?: deg (about x, y), vertical?: bool = false, size?: pt, font?: family, style? (default Regular, or the family's closes… | `inspect.layers{id=6}.bounds`: None → <removed> |
| `text.setText` | verified | {id?\|ids?, text} replace the contents of text objects (keeps the first run's style) → {ids, overflow?: [id…] (area type and type on a path … | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 189.96000000000004 |
| `text.areaOptions` | ran | {ids?\|id?, width?: pt, height?: pt, rows?, columns?, gutter?: pt (between rows and columns), rowGutter?: pt\|null (between rows when it dif… | no change in inspect/json; result={"columns": 1, "firstBaseline": "ascent", "firstBaselineMin": 0.0, |
| `text.reshapeArea` | verified | {id, anchors: [[subpath, anchor]…], dx, dy} or {items: [{id, anchors}…], dx, dy} move anchors of area type's frame (the type area) by dx, dy… | `doc.layers{id=6}.kind.children{id=7}.kind.kind.frame.subpaths[0].anchors[0].p[0]`: 0.0 → 10.0 |
| `text.reshapePath` | refused | {id, anchors: [[subpath, anchor]…], dx, dy} move anchors of type on a path's path by dx, dy points, with their handles; the start and end br… | vectorcraft-cli: step 9 (text.reshapePath): invalid parameters for `text.reshapePath`: not type on a |
| `text.fitHeadline` | verified | {ids?\|id?} track the first line of area type so it fills the frame width → {tracking} | `doc.layers{id=6}.kind.children{id=7}.kind.runs[0].style.tracking`: 0.0 → 706.6 |
| `text.setStyle` | verified | {ids?\|id?, font?, style? (font alone: the style is kept when the new family has it, else its closest), size?: pt, leading?: pt\|"auto", tra… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 509.78 |
| `text.editRange` | verified | {id, start: byte, end: byte, insert?: string, runs?: [{text, style}]} replace bytes start..end of the plain text (inserted text takes the re… | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 19.128 |
| `text.startList` | ran | {id, at?: byte (default: the end of the text)} start a list from typed characters, what the Type tool runs when a space is typed on its own:… | no change in inspect/json; result={"caret": 5, "id": 5, "started": false} |
| `text.setRangeStyle` | verified | {id? (default: the one selected type object), start?: byte, end?: byte (default: all text), font?, style?, size?: pt, leading?: pt\|"auto", … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 509.78 |
| `text.touchType` | refused | {id, start: byte (a character of it), dx?: pt, dy?: pt, hScale?: %, vScale?: %, rotation?: deg} change one character (a ligature, one glyph … | vectorcraft-cli: step 9 (text.touchType): invalid parameters for `text.touchType`: the first charact |
| `text.getRange` | ran | {id, start?, end?, effective?: bool = false} → {text, runs: [{text, style}], length}; effective uses document-point size/leading/baseline sh… | no change in inspect/json; result={"length": 5, "runs": [{"style": {"all_caps": false, "baseline_shi |
| `text.createInPath` | refused | {path: id, mode: "area"\|"onPath", text?: "", vertical?: bool = false, at?: [x, y] (on-path start: nearest point), size?, font?, style?, col… | vectorcraft-cli: step 10 (text.createInPath): invalid parameters for `text.createInPath`: missing `p |
| `text.discardEmpty` | ran | {id} remove text object `id` if it has no characters (what the Type tool does with point type it placed when editing ends). When nothing but… | no change in inspect/json; result={"removed": false} |
| `text.insertInline` | refused | {id?: text id (default: the text the Type tool edits), at?: byte offset (default: the Type tool's selection, which it replaces; clamped to t… | vectorcraft-cli: step 9 (text.insertInline): invalid parameters for `text.insertInline`: node 2 is n |
| `text.fonts` | read-ok | {selectionOnly?} (the type in the art of the symbols in scope included: all of the document's, or those the selected instances show) → [{fam… | no change in inspect/json; result=[{"family": "Source Sans 3", "missing": false, "missingGlyphs": 0, |
| `text.replaceFont` | refused | {from: {family, style?}, to: {family (any of its names; stored as the font's own family name), style?}, selectionOnly?} (style omitted: ever… | vectorcraft-cli: step 9 (text.replaceFont): invalid parameters for `text.replaceFont`: `from.family` |
| `text.fontList` | ran | {family?, style?} → {families: [names]} sorted: the bundled fonts, fonts added and the fonts installed on the system (none on the web), each… | no change in inspect/json; result={"families": ["Adwaita Mono", "Adwaita Sans", "BIZ UDMincho", "BIZ |
| `text.rescanFonts` | ran | {} scan the system font folders again, for fonts installed or removed since the app started; text in a font that became available redraws in… | no change in inspect/json; result={"faces": 549, "families": 126} |
| `text.missingFonts` | ran | {} → {fonts: [{family, style, status: missing\|substitute, resolved: {family, style}}] (sorted by name; at most 1000), count, fontsNextToDoc… | no change in inspect/json; result={"count": 0, "fonts": []} |
| `text.findFontFiles` | ran | {folder?: an absolute path, fonts?: [{family, style?}] (1 to 1000; default: the active document's missing fonts, as text.missingFonts lists … | no change in inspect/json; result={"fonts": [], "state": "idle"} |
| `text.addFontFiles` | refused | {files: [paths the last text.findFontFiles search found] (1 to 1000)} copy the font files into VectorCraft's own Fonts folder (next to the p… | vectorcraft-cli: step 9 (text.addFontFiles): invalid parameters for `text.addFontFiles`: `/tmp/claud |
| `text.thread.create` | refused | {} thread the selected area type and type on a path (and closed paths, which become area frames) in stacking order → {ids} | vectorcraft-cli: step 10 (text.thread.create): command `text.thread.create` is not available right n |
| `text.thread.add` | refused | {from, to?, rect?: [x, y, width, height], at?: [x, y], before?} thread area type or type on a path `from` (a click on its out port) into one… | vectorcraft-cli: step 10 (text.thread.add): invalid parameters for `text.thread.add`: invalid object |
| `text.thread.releaseSelection` | refused | {} take the selected frames out of their threads (the story re-flows through the rest) | vectorcraft-cli: step 10 (text.thread.releaseSelection): command `text.thread.releaseSelection` is n |
| `text.thread.remove` | refused | {} break the selected frames' threads; each frame keeps the text it shows | vectorcraft-cli: step 10 (text.thread.remove): command `text.thread.remove` is not available right n |
| `text.thread.break` | refused | {id, port: "in"\|"out"} break the thread of area type or type on a path `id` before it (its in port) or after it (its out port), as a double… | vectorcraft-cli: step 10 (text.thread.break): invalid parameters for `text.thread.break`: no such ob |
| `text.thread.info` | ran | {} → [[id…]] every thread in order | no change in inspect/json; result=[] |
| `text.tabs.set` | refused | {stops: [{position: pt, align?: left\|center\|right\|decimal, leader?: ". ", alignOn?: "."}], ids?\|id?, start?: byte, end?: byte} replace t… | vectorcraft-cli: step 9 (text.tabs.set): invalid parameters for `text.tabs.set`: missing stops |
| `text.tabs.get` | ran | {ids?\|id?, start?: byte} → {stops} of the first selected text object (its paragraph at `start`; default the first) | no change in inspect/json; result={"stops": []} |
| `text.tabs.clear` | ran | {ids?\|id?, start?: byte, end?: byte} | no change in inspect/json; result={"stops": 0} |
| `text.setFormat` | refused | {ids?\|id?, kerning?: 1/1000 em\|"auto"\|"optical", baselineShift?: pt, hScale?: %, vScale?: %, rotation?: deg, underline?, strikethrough?, … | vectorcraft-cli: step 9 (text.setFormat): invalid parameters for `text.setFormat`: nothing to change |
| `text.convertListToText` | ran | {ids?\|id?, start?: byte, end?: byte} (Type › Bullets and Numbering › Convert to Text: the paragraphs of the selected type, or of `ids`, or … | no change in inspect/json; result={"converted": 0, "ids": [], "inserted": []} |

## edit (30)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `edit.dropSelection` | refused | {sourceDocument: uid, ids: [id…], grab: [x,y], at: [x,y]} copy 1–10000 editable source objects from an open document to the active document,… | vectorcraft-cli: step 9 (edit.dropSelection): invalid parameters for `edit.dropSelection`: grab must |
| `edit.undo` | verified | {} | `inspect.layers{id=6}.bounds`: None → <removed> |
| `edit.redo` | refused | {} | vectorcraft-cli: step 9 (edit.redo): command `edit.redo` is not available right now: nothing to redo |
| `edit.clearHistory` | ran | {} remove every undo and redo step of the active document (the History panel menu's Clear History): the document stays as it is, and clearin… | no change in inspect/json; result={"cleared": 5} |
| `edit.undoGroup.begin` | ran | {label?: string} until edit.undoGroup.end, the edits made in the document active at the begin, and in each document opened or created before… | no change in inspect/json; result=null |
| `edit.undoGroup.end` | ran | {cancel?: bool} close the undo group: its edits stay one undo step or, with `cancel`, are undone | no change in inspect/json; result=null |
| `edit.cut` | verified | {} (the Artboard tool chosen: artboard.cut) | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 207.82399999999996 |
| `edit.copy` | ran | {} (the Artboard tool chosen: artboard.copy) | no change in inspect/json; result={"copied": 2} |
| `edit.paste` | verified | {center?: [x, y], dx?, dy?, swatchConflict?} paste centred on `center` (the app passes the view centre), else offset by dx/dy (default: the … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 517.824 |
| `edit.pasteInFront` | verified | {swatchConflict?, artboard?: index (the active artboard: the objects go where they were on the artboard they were copied from, on this one)}… | `inspect.objects`: 6 → 7 |
| `edit.pasteInBack` | verified | {swatchConflict?, artboard?: index (as edit.pasteInFront)} paste in place just below the bottom selected object, or at the bottom of the cur… | `inspect.objects`: 6 → 7 |
| `edit.pasteInPlace` | verified | {swatchConflict?, artboard?: index (as edit.pasteInFront)} paste where the objects were copied (resources, layers and drawing modes as edit.… | `inspect.objects`: 6 → 7 |
| `edit.pasteOnAllArtboards` | verified | {swatchConflict?} paste a copy on every artboard at the offset the objects had to the artboard they were copied from (resources, layers and … | `inspect.objects`: 6 → 7 |
| `edit.clear` | verified | {ids?} delete the objects `ids`, else the selection (fully selected objects and direct-selected anchors together, else ruler guides) | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 207.82399999999996 |
| `edit.duplicate` | verified | {ids?: [id…] (selected first; default: the selection), dx?, dy?} duplicate the selection in place (offset optional) | `inspect.objects`: 6 → 8 |
| `edit.colors.invert` | verified | {fill?: true, stroke?: true, includeImages?: true, includePatterns?: true, ids?} replace each colour by its RGB inverse (keeps the colour mo… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → #000000 |
| `edit.colors.toCMYK` | verified | {fill?, stroke?, includeImages?, includePatterns?, ids?} (as edit.colors.invert) → {changed} | `inspect.layers{id=1}.children{id=3}.stroke`: #000000 → #2a2b2c |
| `edit.colors.toGrayscale` | verified | {fill?, stroke?, includeImages?, includePatterns?, ids?} (as edit.colors.invert) → {changed} | `doc.layers{id=1}.kind.children{id=2}.appearance.items[0].paint.color.model`: rgb → gray |
| `edit.colors.toRGB` | ran | {fill?, stroke?, includeImages?, includePatterns?, ids?} (as edit.colors.invert) → {changed} | no change in inspect/json; result={"changed": 0} |
| `edit.colors.saturate` | ran | {intensity: -100..100 (%; a number outside the range counts as its nearest end), fill?, stroke?, includeImages?, includePatterns?, ids?} sca… | no change in inspect/json; result={"changed": 0} |
| `edit.colors.adjustBalance` | verified | {mode?: "rgb"\|"cmyk"\|"gray"\|"global" (default: from the channels given), r?, g?, b? \| c?, m?, y?, k? \| gray? \| tint?: -100..100 (% add… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → #fcfcfc |
| `edit.colors.blendFrontToBack` | refused | {} ≥3 filled objects (solid fills or gradient meshes, which keep their shading): intermediate fills graded between the frontmost and backmos… | vectorcraft-cli: step 9 (edit.colors.blendFrontToBack): Blend colors: select at least three objects  |
| `edit.colors.blendHorizontally` | refused | {} ≥3 filled objects or meshes: fills graded between the leftmost and rightmost → {changed} | vectorcraft-cli: step 9 (edit.colors.blendHorizontally): Blend colors: select at least three objects |
| `edit.colors.blendVertically` | refused | {} ≥3 filled objects or meshes: fills graded between the topmost and bottommost → {changed} | vectorcraft-cli: step 9 (edit.colors.blendVertically): Blend colors: select at least three objects w |
| `edit.colorSettings` | ran | {rgb?: profile, cmyk?: profile, intent?: "perceptual"\|"relative"\|"saturation"\|"absolute", bpc?: bool} set the working spaces → {rgb, cmyk… | no change in inspect/json; result={"bpc": true, "cmyk": "VectorCraft Generic CMYK (SWOP-like)", "int |
| `edit.assignProfile` | ran | {rgb?: profile\|null, cmyk?: profile\|null} tag the document with profiles (colour numbers are kept) → {rgb, cmyk} | no change in inspect/json; result={"cmyk": null, "rgb": null} |
| `edit.colors.overprintBlack` | ran | {remove?: false, percentage?: 100, fill?: true, stroke?: true, includeCmyBlacks?: false, includeSpotBlacks?: false, ids?} make the black fil… | no change in inspect/json; result={"changed": 0} |
| `edit.findReplace` | ran | {find, replace?: "", matchCase?: false, wholeWord?: false, ids?} replace in every text object (or ids) → {count}. Matches never span style r… | no change in inspect/json; result={"count": 0} |
| `edit.findNext` | ran | {find, matchCase?, wholeWord?} select the next text object (after the selected one, wrapping) containing `find` → {id\|null} | no change in inspect/json; result={"id": null} |
| `edit.pasteWithoutFormatting` | verified | {center?, dx?, dy?, swatchConflict?} paste as edit.paste; pasted text takes the default character style (one run) and leaves its character a… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 513.912 |

## file (28)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `file.new` | verified | {preset?: a name from file.newPresets (start from it; the other params change it), name?\|title?: document name (default Untitled-N), width?… | `inspect.layers{id=6}.bounds`: None → <removed> |
| `file.close` | refused | {index?} | vectorcraft-cli: step 10 (document.inspect): command `document.inspect` is not available right now:  |
| `file.list` | read-ok | {path} the files and folders in folder `path`, by name: what an agent may open there (held to the automation read root when one is in force)… | no change in inspect/json; result={"entries": [{"kind": "file", "name": "Untitled-1-2.pdf", "size":  |
| `file.saveAs` | ran | {…as document.save} {path?, format?: vectorcraft\|template\|pdf\|svg\|svgz\|ai\|eps (default: the path's extension, else the document's own;… | no change in inspect/json; result={"bytes": 31825, "dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZn |
| `file.saveCopy` | ran | {…as document.save} {path?, format?, options?} write a copy; the document keeps its path, title and modified state → {path, format, bytes, w… | no change in inspect/json; result={"bytes": 31825, "dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZn |
| `file.saveAsTemplate` | ran | {…as document.save} {path? (saved with the format's extension: one naming another format is replaced, and one is added to a name without it)… | no change in inspect/json; result={"bytes": 31847, "dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZn |
| `file.newFromTemplate` | verified | {path} or {name, dataBase64}: open a template (or any readable file) as a new untitled document → {index, title, format, warnings} | `inspect.artboards[0].height`: 792.0 → 200.0 |
| `file.revert` | refused | {confirmed?: bool (the app's own: it asks first, then runs the command with it)} discard the changes: reload the saved file into the same ta… | vectorcraft-cli: step 10 (file.revert): command `file.revert` is not available right now: no changes |
| `file.formatOptions` | ran | {format?: a writable format id or ait (default: the document's own)} → {id, label, extensions, mime, read, write, raster, options: {name: {t… | no change in inspect/json; result={"extensions": ["vectorcraft", "drawcraft"], "id": "vectorcraft",  |
| `file.closeAll` | refused | {} → {closed} | vectorcraft-cli: step 10 (document.inspect): command `document.inspect` is not available right now:  |
| `file.documentColorMode` | verified | {mode: "cmyk"\|"rgb", convert?: true (convert every color of the art (opacity masks included), symbols, graph designs, pattern tiles, graphi… | `inspect.colorMode`: Rgb → Cmyk |
| `file.info` | read-ok | {title?, author?, authorTitle?, description?, keywords?: [string…]\|"a, b" (each once), rating?: 0–5, copyrightStatus?: "unknown"\|"copyrigh… | no change in inspect/json; result={"artboards": 1, "author": "", "authorTitle": "", "colorMode": "rg |
| `file.newPresets` | read-ok | {category?: "Recent"\|"Saved"\|"Mobile"\|"Web"\|"Print"\|"Film & Video"\|"Art & Illustration"\|"Branding"\|"Social"} the New Document preset… | no change in inspect/json; result={"categories": [{"name": "Recent", "presets": [{"artboardLayout":  |
| `file.newPresets.save` | ran | {name, preset?: start from this preset, …settings as file.new (default: Letter in prefs unitsGeneral)} save New Document settings as a user … | no change in inspect/json; result={"count": 1, "name": "Test"} |
| `file.newPresets.delete` | refused | {name} delete a saved New Document preset → {deleted} | vectorcraft-cli: step 9 (file.newPresets.delete): command `file.newPresets.delete` is not available  |
| `file.place` | verified | {path \| name \| dataBase64 (a file's path, or its name with its bytes), link?: true (a raster image keeps its file's path; a VectorCraft do… | `inspect.objects`: 6 → 10 |
| `file.place.info` | read-ok | {path \| name \| dataBase64 (a file's path, or its name with its bytes), page?, crop?, password?, thumbnail?: px, link?: bool, dxf?: {…} (bo… | no change in inspect/json; result={"format": "svg", "height": 149.0, "name": "base.svg", "warnings": |
| `file.place.queue` | refused | {paths?: [path…], files?: [{name, dataBase64}…], link?, template?, page?, crop?, text?, dxf?, thumbnail?: px} load the place cursor (the `pl… | vectorcraft-cli: step 9 (file.place.queue): invalid parameters for `file.place.queue`: give paths or |
| `file.package` | ran | {folder?, name?: (default: "<document> Folder"), copyLinks?: true, linksFolder?: true (the linked files go in Links/, else next to the docum… | no change in inspect/json; result={"bytes": 210410, "dataBase64": "UEsDBBQAAAgIAIokZV1qn0rC5AoAADN8A |
| `file.print` | ran | {preset?: name (as print.setup's: its settings instead of the document's; the saved settings stay), settings?: {…settings of print.setup} (o… | no change in inspect/json; result={"bytes": 7230, "dataBase64": "JVBERi0xLjcKJYCAgIAKCjEgMCBvYmoKPDw |
| `file.recovery.save` | refused | {} write a recovery copy of every modified document changed since its last copy, in this app's own area of the store (the app does this ever… | vectorcraft-cli: step 9 (file.recovery.save): command `file.recovery.save` is not available right no |
| `file.recovery.list` | refused | {} the recovery copies in the store → {copies: [{file ("<area>/<name>"), title, path (the document's file, if it had one), format, saved (Un… | vectorcraft-cli: step 9 (file.recovery.list): command `file.recovery.list` is not available right no |
| `file.recovery.restore` | refused | {file?} open a copy left behind by a crash (default: every one; a running VectorCraft's copies are never taken) as a new document titled "<n… | vectorcraft-cli: step 9 (file.recovery.restore): command `file.recovery.restore` is not available ri |
| `file.recovery.discard` | refused | {file?} delete a copy left behind by a crash (default: every one; copies of open documents and of running VectorCraft apps stay) → {discarde… | vectorcraft-cli: step 9 (file.recovery.discard): command `file.recovery.discard` is not available ri |
| `file.open` | verified | {path} open any readable file (see document.formats) as a new document; templates open untitled | `inspect.artboards[0].height`: 792.0 → 200.0 |
| `file.save` | verified | {…as document.save} = document.save {path?, format?, options?, svg?: {…SVG options}}: .vectorcraft, .ai (a PDF that reopens editable), .pdf,… | `inspect.path`: None → <scratch> |
| `file.export` | ran | {…as document.export} = document.export {path?, format?, artboard?, range?, scale?, …} (no path → dataBase64) | no change in inspect/json; result={"bytes": 5975, "dataBase64": "iVBORw0KGgoAAAANSUhEUgAAAmQAAAMYCAY |
| `file.exportForScreens` | ran | {folder?, zip?, artboards? \| range? \| fullDocument? \| assets?, includeBleed?, includeArtboardFill?, subfolders?, preset?, formats?, setti… | no change in inspect/json; result={"files": [{"dataBase64": "iVBORw0KGgoAAAANSUhEUgAAAmQAAAMYCAYAAAB |

## layer (26)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `layer.new` | verified | {name?, top?: bool, below?: bool, color?, template?, locked?, visible?, printable?, preview?, dimImages?} a layer directly above the current… | `inspect.currentLayer`: 6 → 7 |
| `layer.newSublayer` | verified | {parent?: layer id (default: the highlighted row's layer, else the current layer), bottom?: bool, name?, …options as layer.new} a sublayer o… | `inspect.currentLayer`: 6 → 7 |
| `layer.delete` | verified | {ids?\|id?} delete rows: layers, sublayers, groups or objects with what they hold (default: the highlighted rows, else the current layer). T… | `inspect.currentLayer`: 6 → 1 |
| `layer.duplicate` | verified | {ids?\|id?} copy rows (default: the highlighted rows, else the current layer), each just above its original; a layer's copy is named `<name>… | `inspect.layerRows[0]`: 6 → 7 |
| `layer.setCurrent` | ran | {id} click a row: it alone is highlighted, and the layer it is (or the layer it is in) becomes the current layer, where new art goes. Not an… | no change in inspect/json; result={"id": 6, "layer": 6} |
| `layer.highlight` | ran | {ids, mode?: "set"\|"add"\|"toggle"} highlight Layers panel rows (Shift-click: a range, Ctrl-click: toggle one); the last one's layer become… | no change in inspect/json; result={"rows": [6]} |
| `layer.setProps` | ran | {ids?\|id? (default: the highlighted rows, else the current layer), name? (with prefs.identifyObjectsBy xmlId: a valid XML ID, stored as the… | no change in inspect/json; result=null |
| `layer.collectInNew` | verified | {ids?} move rows (default: the highlighted rows, else the selected objects) into a new layer where the topmost of them was (a sublayer when … | `inspect.currentLayer`: 6 → 7 |
| `layer.selectAll` | verified | {id, add?: bool} the Layers panel's selection column: select the visible, unlocked art of a layer (its sublayers' too), or the object itself… | `inspect.selection[0]`: 6 → <removed> |
| `layer.move` | verified | {ids\|id, target, place?: "above"\|"below"\|"inside" (default inside), copy?: bool} drag rows in the Layers panel: above or below the target… | `inspect.layers{id=6}.bounds`: None → <removed> |
| `layer.clippingMask.toggle` | refused | {id?: layer or group (default: the one highlighted layer or group row, else the one selected group, else the current layer)} make: its top o… | vectorcraft-cli: step 9 (layer.clippingMask.toggle): the layer has no objects to clip by |
| `layer.target` | verified | {id, add?: bool (Shift-click: the item joins the selection, or leaves it when all selected; nothing is targeted)} target a layer, group or o… | `inspect.selection[0]`: 6 → <removed> |
| `layer.pasteRemembersLayers` | verified | {on?} (default: toggle) the document option: on, the Paste commands put objects back into the layers they were copied from (by name; a missi… | `inspect.pasteRemembersLayers`: False → True |
| `layer.merge` | refused | {ids?\|id?} (default: the highlighted rows) merge two or more rows into the layer listed (highlighted) last: the other layers' contents and … | vectorcraft-cli: step 9 (layer.merge): invalid parameters for `layer.merge`: highlight two or more r |
| `layer.flatten` | verified | {id?} (default: the highlighted row's top-level layer, else the current one's) move the art of every other visible top-level layer into this… | `inspect.layers{id=6}.bounds`: None → <removed> |
| `layer.releaseToLayers` | refused | {id?: layer or group (default: the highlighted row, else the current layer), build?: bool} each object in it goes into a new sublayer of its… | vectorcraft-cli: step 9 (layer.releaseToLayers): there are no objects to release |
| `layer.releaseToLayersBuild` | refused | {id?} layer.releaseToLayers with build: true → {ids} | vectorcraft-cli: step 9 (layer.releaseToLayersBuild): there are no objects to release |
| `layer.reverse` | refused | {ids?\|id?} (default: the highlighted rows) reverse the stacking order of two or more rows that share a layer or group; each keeps the place… | vectorcraft-cli: step 9 (layer.reverse): invalid parameters for `layer.reverse`: highlight two or mo |
| `layer.template` | verified | {ids?\|id?, on?: bool (default: toggle the first)} make layers templates (locked, dimmed, left out of print and export) or ordinary layers a… | `inspect.layers{id=6}.dimImages`: None → 50 |
| `layer.hideOthers` | verified | {ids?\|id?} hide every top-level layer but those holding the highlighted rows (else the current layer), which show. One undo step → {count} | `inspect.layers{id=1}.visible`: True → False |
| `layer.showAll` | ran | {} show every layer and sublayer → {count} | no change in inspect/json; result={"count": 0} |
| `layer.outlineOthers` | verified | {ids?\|id?} turn Preview off (outline view) for every top-level layer but those holding the highlighted rows (else the current layer), which… | `inspect.layers{id=1}.preview`: True → False |
| `layer.previewAll` | ran | {} turn Preview on for every layer and sublayer → {count} | no change in inspect/json; result={"count": 0} |
| `layer.lockOthers` | verified | {ids?\|id?} lock every top-level layer but those holding the highlighted rows (else the current layer), which unlock → {count} | `inspect.layers{id=1}.locked`: False → True |
| `layer.unlockAll` | ran | {} unlock every layer and sublayer → {count} | no change in inspect/json; result={"count": 0} |
| `layer.locate` | ran | {id?} (default: the last selected object) highlight the object's row; the Layers panel opens the layers around it and scrolls to it → {id, a… | no change in inspect/json; result={"ancestry": [6], "id": 6} |

## perspective (25)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `perspective.grid.set` | verified | {kind?: 1\|2\|3, origin?: [x,y], horizon?, vpLeft?, vpRight?, vpVertical?: [x,y], distance?, cell?, extent?, height?, visible?, plane?, left… | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.grid.preset` | refused | {kind: 1\|2\|3 (its normal view) \| name: a preset (see perspective.presets.list)} reset the grid to the preset fitted to the first artboard… | vectorcraft-cli: step 9 (perspective.grid.preset): invalid parameters for `perspective.grid.preset`: |
| `perspective.grid.show` | verified | {visible?: bool} (no param toggles). View state: not an undo step | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.plane.set` | verified | {plane: left\|right\|ground\|none} Plane Switching widget. View state: not an undo step | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.attach` | verified | {ids?\|id?, plane?: left\|right\|ground (default: the active plane)} project the objects onto the plane | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 1037.997199635369 |
| `perspective.release` | verified | {ids?\|id?} detach from the grid (geometry unchanged) | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.move` | refused | {ids?\|id?, from: [x,y], to: [x,y], plane?, copy?: bool (move copies, as Alt-dragging does), perpendicular?: bool (move along the plane's no… | vectorcraft-cli: step 9 (perspective.move): invalid parameters for `perspective.move`: missing from |
| `perspective.draw` | refused | {command: shape.* id, params, plane?, snap?: bool (default: Snap to Grid), at?: [x, y] (a point of the plane the shape lies on, as the tool … | vectorcraft-cli: step 9 (perspective.draw): invalid parameters for `perspective.draw`: command must  |
| `perspective.transform` | verified | {ids?\|id?, matrix: [a,b,c,d,e,f] (affine map in plane coordinates, points: u along the plane, v up or away), depth?: pt to move along the p… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 1029.9950674551296 |
| `perspective.nudge` | refused | {dx, dy: arrow direction (-1, 0 or 1), big?: bool (×10), copy?: bool} move the selection in perspective by the keyboard increment, as the ar… | vectorcraft-cli: step 9 (perspective.nudge): the selection isn't in perspective |
| `perspective.plane.move` | verified | {plane?: left\|right\|ground (default: the active plane), offset?: pt (where along its normal; 0 is its place in the grid's definition) \| b… | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.plane.matchObject` | refused | {id? (default: the first selected object)} move the plane the object is attached to onto the object and make it the active plane → {plane, o… | vectorcraft-cli: step 9 (perspective.plane.matchObject): the object isn't in perspective |
| `perspective.editText` | refused | {id? (default: the selected type)} Object › Perspective › Edit Text: show type in perspective flat where it is drawn, in isolation mode, to … | vectorcraft-cli: step 10 (perspective.editText): select type in perspective |
| `perspective.grid.get` | read-ok | {} → {grid: the model (as perspective.grid.set takes it), define: the Define Grid fields (as perspective.grid.define takes them), station: {… | no change in inspect/json; result={"define": {"angle": 45.0, "distance": 293.76, "gridline": 20.0, " |
| `perspective.grid.define` | ran | {name?: preset name ("" = custom), kind?: 1\|2\|3, units?: unit name (points, pixels, inches, centimeters, millimeters…), scale?: [artboard,… | no change in inspect/json; result={"angle": 45.0, "distance": 293.76, "gridline": 20.0, "groundColor |
| `perspective.presets.list` | read-ok | {} → {presets: [{builtIn, name, kind, …the perspective.grid.define fields}]} the built-in views (fitted to the first artboard, protected) fi… | no change in inspect/json; result={"presets": [{"angle": 45.0, "builtIn": true, "distance": 306.0, " |
| `perspective.presets.save` | ran | {name?: (default: a new "Perspective Preset N"), newName?: rename it, preset?: the preset to start from (default: the saved preset `name`, e… | no change in inspect/json; result={"created": true, "definition": {"angle": 45.0, "distance": 293.76 |
| `perspective.presets.delete` | refused | {name} delete a saved preset (built-in ones stay) → {deleted: name} | vectorcraft-cli: step 9 (perspective.presets.delete): invalid parameters for `perspective.presets.de |
| `perspective.presets.export` | refused | {names?: [preset names, built-in ones too] (default: every saved preset), path?} write the presets as a .vcperspective file (JSON) → {path, … | vectorcraft-cli: step 9 (perspective.presets.export): invalid parameters for `perspective.presets.ex |
| `perspective.presets.import` | refused | {path? \| data?: file text \| dataBase64?, replace?: false (replace saved presets of the same names; else imported ones whose name is taken … | vectorcraft-cli: step 9 (perspective.presets.import): invalid parameters for `perspective.presets.im |
| `perspective.widget.options` | ran | {show?: bool, position?: topLeft\|topRight\|bottomLeft\|bottomRight} the Plane Switching Widget: shown or not, and the corner of the documen… | no change in inspect/json; result={"position": "topLeft", "show": true} |
| `perspective.grid.lock` | verified | {on?: bool} (no param toggles) View › Perspective Grid › Lock Grid: the grid's widgets can't be dragged (the Plane Switching Widget still wo… | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.grid.lockStation` | verified | {on?: bool} (no param toggles) dragging one vanishing point moves the other around the station point (the viewing angle turns, the viewer st… | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.grid.snap` | verified | {on?: bool} (no param toggles) art drawn or moved in perspective lands on gridlines within a quarter cell (on by default). View state: not a… | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |
| `perspective.grid.rulers` | verified | {on?: bool} (no param toggles) a ruler up the line where the planes meet, in the grid's units at its scale. View state: not an undo step → {… | `doc.unknown.perspectiveGrid.angle`: <absent> → 45.0 |

## swatch (23)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `swatch.new` | verified | {name?, color? \| colors?: [colour] (one swatch each, in one undo step) \| swatch? \| gradient? \| pattern?: name (default: the current fill… | `doc.swatches[37].global`: <absent> → False |
| `swatch.delete` | verified | {name? \| names?: [swatch or colour group names] (a group goes with its swatches), unlink?: true (art using a deleted global swatch keeps it… | `doc.swatches[3].name`: Red → Orange Red |
| `swatch.newGroup` | verified | {name?, swatches?: [names] (solid colours move into the group; gradients, patterns and None stay), colors?: [colour] (added as new swatches)… | `doc.swatch_groups[2].name`: <absent> → Color Group |
| `swatch.duplicate` | verified | {name} | `doc.swatches[4].name`: Orange Red → Red copy |
| `swatch.sortByName` | verified | {} | `doc.swatch_groups[0].swatches[0].name`: K=90 → K=10 |
| `swatch.edit` | ran | {name, newName?, color? (e.g. {l, a, b} for a Lab colour), keepModel?: bool (as paint.setFill; the swatch's own color and a color given with… | no change in inspect/json; result={"name": "Red", "relinked": 0} |
| `swatch.list` | read-ok | {group?: name (only that colour group's swatches)} → {swatches: [{name, kind: "none"\|"color"\|"gradient"\|"pattern", group, global, spot, c… | no change in inspect/json; result={"groups": [{"name": "Grays", "swatches": ["K=90", "K=80", "K=70", |
| `swatch.move` | verified | {name? \| names?: [swatch names, in order; or colour group names to reorder the groups], to?: index in the destination (they go before the s… | `doc.swatches[3].name`: Red → Orange Red |
| `swatch.addUsedColors` | ran | {selection?: false (only the selected art's colours; default: all the art's), global?: false (the new swatches are global and the matching u… | no change in inspect/json; result={"added": [], "linked": 0} |
| `swatch.unused` | read-ok | {} → {names: [the swatches nothing uses, in panel order]}: a colour is used when a paint links to it or an unlinked paint, gradient stop or … | no change in inspect/json; result={"names": ["Red", "Orange", "Yellow", "Yellow Green", "Lime", "Gre |
| `swatch.merge` | refused | {names: [two or more solid-colour swatches], name?: the merged swatch's name (one swatch kept)} keep the first (its name and colour) and del… | vectorcraft-cli: step 9 (swatch.merge): invalid parameters for `swatch.merge`: give two or more swat |
| `swatch.ungroup` | refused | {name: colour group} move its swatches to the end of the ungrouped swatches and remove the group, as one undo step → {swatches: [names]} | vectorcraft-cli: step 9 (swatch.ungroup): invalid parameters for `swatch.ungroup`: no colour group ` |
| `swatch.sortByKind` | ran | {} order the swatches of each list by kind (None first, then process colours, spot colours, gradients, patterns; colour groups stay after th… | no change in inspect/json; result=null |
| `swatch.spotOptions` | ran | {useLab?: bool (omitted: unchanged)} the document's Spot Colors options: spot colours defined in Lab show, print and export from their Lab v… | no change in inspect/json; result={"relinked": 0, "useLab": true} |
| `swatch.editGroup` | refused | {group: colour group, colors: [colour] (hex, key, {c,m,y,k} or {l,a,b}; the group's swatches take them in order, extra colours become new sw… | vectorcraft-cli: step 9 (swatch.editGroup): invalid parameters for `swatch.editGroup`: no colour gro |
| `swatch.setSpot` | verified | {name, spot?: true} make a swatch a spot colour (prints on its own plate; spot swatches are global) → {name, spot} | `doc.swatches[3].global`: False → True |
| `swatch.library.list` | read-ok | {} → {libraries: [{id, name, category: "builtIn"\|"gradients"\|"patterns"\|"user" (User Defined: the library files in the user library folde… | no change in inspect/json; result={"libraries": [{"category": "builtIn", "count": 216, "id": "web-sa |
| `swatch.library.get` | refused | {library: id or name} → {id, name, category, swatches: [{name, kind, group, global, spot, color?, hex?, gradient?, pattern?}] (as swatch.lis… | vectorcraft-cli: step 9 (swatch.library.get): invalid parameters for `swatch.library.get`: no swatch |
| `swatch.library.add` | refused | {library: id or name, names?: [swatch or colour group names in the library] (default: all of it; a group comes as a colour group, a single s… | vectorcraft-cli: step 9 (swatch.library.add): invalid parameters for `swatch.library.add`: no swatch |
| `swatch.resetDefaults` | ran | {replace?: false} bring back the default swatches and colour groups of the document's colour mode that are missing (by name), as one undo st… | no change in inspect/json; result={"added": []} |
| `swatch.library.save` | ran | {path?, format?: "vcswatches" (lossless JSON: colour models, global, spot, gradients, groups) \| "gpl" (8-bit RGB palette; groups as `# Grou… | no change in inspect/json; result={"count": 50, "data": "{\n \"format\": \"vcswatches\",\n \"version |
| `swatch.library.load` | ran | {path? \| data?: file text \| dataBase64?, name?: file name (default: the path's)} load a .vcswatches, .gpl, .ase (swatch exchange) or .acb … | no change in inspect/json; result={"count": 50, "library": "loaded/<scratch> |
| `swatch.library.copyToUser` | refused | {library: id or name of a loaded library (category "loaded", swatch.library.load)} copy it into the user library folder of the desktop app, … | vectorcraft-cli: step 9 (swatch.library.copyToUser): command `swatch.library.copyToUser` is not avai |

## type (23)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `type.orientation.vertical` | verified | {ids?\|id?} set vertical writing | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 552.8 |
| `type.orientation.horizontal` | ran | {ids?\|id?} set horizontal writing | no change in inspect/json; result={"ids": [5], "vertical": false} |
| `type.createOutlines` | verified | {} convert the selected text to groups of compound paths (one per glyph); a frame of threaded text leaves its thread with the text it shows … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 500.288 |
| `type.scaleTextAttributes` | refused | {ids?\|id?} bake each selected type object's transform scale into its character sizes (leading, baseline shift and horizontal scale included… | vectorcraft-cli: step 9 (type.scaleTextAttributes): command `type.scaleTextAttributes` is not availa |
| `type.opticalMarginAlignment` | verified | {ids?\|id?, on?: bool} turn Optical Margin Alignment on or off for the selected type and every frame of its threads (on omitted: the opposit… | `doc.layers{id=1}.kind.children{id=5}.kind.opticalMarginAlignment`: <absent> → True |
| `type.systemLayout` | verified | {on?: bool} turn System Layout on or off for the document (on omitted: the opposite of the document's setting) and every text object in it. … | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 53.0 |
| `type.fractionalWidths` | verified | {ids?\|id?, on?: bool} turn Fractional Widths on or off for the selected type and every frame of its threads (on omitted: the opposite of th… | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 53.0 |
| `type.ruby` | verified | {ids?\|id?, start?: byte, end?: byte, text?: reading, position?: above\|below (vertical type: right\|left), align?: start\|center\|end, size… | `inspect.layers{id=1}.bounds.width`: 400.0 → 419.992 |
| `type.changeCase` | verified | {case: "upper"\|"lower"\|"title"\|"sentence", ids?\|id?} → {ids} | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 66.936 |
| `type.smartPunctuation` | ran | {quotes?: true (straight quotes become the Document Setup quotes), dashes?: true (-- → en dash, --- → em dash), ellipsis?: true (... → …), s… | no change in inspect/json; result={"changed": 0} |
| `type.convertToAreaType` | verified | {ids?\|id?} point type → area type framed by its current layout bounds → {ids} | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 64.80000000000001 |
| `type.convertToPointType` | ran | {ids?\|id?} area type → point type; soft line wraps become line breaks, and a frame of threaded text leaves its thread with the text it hold… | no change in inspect/json; result={"ids": [5]} |
| `type.pathOptions` | refused | {ids?\|id?, start?: 0..1, end?: 0..1\|null, flip?: bool, effect?: rainbow\|skew\|3dRibbon\|stairStep\|gravity, alignToPath?: ascender\|desce… | vectorcraft-cli: step 10 (type.pathOptions): invalid parameters for `type.pathOptions`: select type  |
| `type.fillPlaceholder` | verified | {ids?\|id?} replace selected text with placeholder text (area type is filled to its frame) → {ids} | `inspect.layers{id=1}.bounds.width`: 400.0 → 531.072 |
| `type.insert` | verified | {char: "bullet"\|"copyright"\|"ellipsis"\|"paragraph"\|"registered"\|"section"\|"trademark"\|"emDash"\|"enDash"\|"discretionaryHyphen"\|"non… | `inspect.layers{id=1}.children{id=5}.bounds.width`: 52.80000000000001 → 60.096000000000004 |
| `type.fitHeadline` | verified | {ids?\|id?} track the first line of area type so it fills the frame width → {ids, tracking} | `doc.layers{id=6}.kind.children{id=7}.kind.runs[0].style.tracking`: 0.0 → 706.6166666666666 |
| `type.step` | verified | {attribute: "size"\|"leading"\|"tracking"\|"kerning"\|"baselineShift", by?: steps (1; negative steps down), id?, start?: byte, end?: byte, i… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 508.476 |
| `type.size.increase` | verified | {by?: steps (1)} type.step {attribute: size} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 508.476 |
| `type.size.decrease` | verified | {by?: steps (1)} type.step {attribute: size, by: -by} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 507.172 |
| `type.size.increaseByFive` | verified | {} type.step {attribute: size, by: 5}: five times the Size/Leading increment (typeSizeIncrement) | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 511.08399999999995 |
| `type.size.decreaseByFive` | verified | {} type.step {attribute: size, by: -5}: five times the Size/Leading increment (typeSizeIncrement) | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 504.56399999999996 |
| `type.resetTracking` | ran | {ids?: [id…]} set tracking to 0 and clear manual kerning without changing the automatic method in all the text of the type objects in `ids`,… | no change in inspect/json; result={"ids": [5]} |
| `type.resetHorizontalScale` | ran | {ids?: [id…]} set the horizontal scale to 100% (as the Character panel shows it, the object's own transform included) in all the text of the… | no change in inspect/json; result={"ids": [5]} |

## symbol (23)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `symbol.list` | read-ok | {} → {symbols: [{name, instances, size: [w,h], registration: 0..8, exportType: movieClip\|graphic, nineSlice, type: static\|dynamic}], curre… | no change in inspect/json; result={"current": "Sym1", "symbols": [{"exportType": "movieClip", "insta |
| `symbol.new` | verified | {name?, ids?\|id?, registration?: 0..8 (9-point grid, 4 = centre; Symbol Options › Registration), exportType?: movieClip (default)\|graphic,… | `inspect.layers{id=1}.children{id=9}.bounds.height`: 120.0 → <removed> |
| `symbol.options` | verified | {name?, newName?, registration?: 0..8, exportType?: movieClip\|graphic, nineSlice?: bool, nineSliceGuides?: array, type?: static\|dynamic} r… | `doc.layers{id=1}.kind.children{id=8}.kind.symbol`: Sym1 → Test |
| `symbol.place` | verified | {name?, x?, y?} place an instance so its registration point is at (x, y) (default: artboard centre; name default: current) → {id} | `inspect.objects`: 7 → 8 |
| `symbol.breakLink` | verified | {ids?\|id?} expand selected instances into plain art (with their appearance changes to a dynamic symbol), placed through the symbol's 9-slic… | `inspect.layers{id=1}.children{id=9}.bounds.height`: 120.0 → <removed> |
| `symbol.edit` | verified | {id?, ids?: [id…] (instead of id), name?, x?, y?, artboard?: index=0 (the active artboard; the app passes it), viewCenter?: [x, y] (the app … | `inspect.currentLayer`: 1 → 10 |
| `symbol.exitEditing` | ran | {} leave symbol editing mode; after an edit, select the instance it was entered from; leaving without having changed the art adds no undo st… | no change in inspect/json; result=null |
| `symbol.update` | refused | {name, ids?\|id?} replace the symbol's art with the selection (instances update, keeping their appearance changes to the objects at paths th… | vectorcraft-cli: step 12 (symbol.update): objects can't be nested more than 32 deep |
| `symbol.delete` | verified | {name \| names: [name…], expandInstances?: true} delete a symbol (or several, in one undo step); its instances are expanded (or deleted with… | `inspect.layers{id=1}.children{id=9}.bounds.height`: 120.0 → <removed> |
| `symbol.duplicate` | verified | {name, newName?} → {name} | `doc.symbols[1].art.appearance.items[0].kind`: <absent> → fill |
| `symbol.replace` | ran | {name, ids?\|id?} swap the symbol of the selected instances (an instance given a different symbol drops its appearance changes; one given it… | no change in inspect/json; result={"ids": [9]} |
| `symbol.instance.setAppearance` | refused | {id?\|ids?: [one id] (default: the one selected object), path: [i…] (the object in the symbol's art: child indices in paint order from the a… | vectorcraft-cli: step 12 (symbol.instance.setAppearance): invalid parameters for `symbol.instance.se |
| `symbol.instance.reset` | ran | {ids?\|id?} drop the selected dynamic symbol instances' own appearance changes, so they show the symbol's appearance again → {ids: the insta… | no change in inspect/json; result={"ids": []} |
| `symbol.setCurrent` | ran | {name} the symbol the symbolism tools spray (not an undo step) | no change in inspect/json; result=null |
| `symbol.unused` | ran | {} → {names: [the symbols nothing places, in panel order]} (the Symbols panel selects them): instances in the art (opacity masks included), … | no change in inspect/json; result={"names": []} |
| `symbol.selectInstances` | verified | {name} select every instance of a symbol → {count} | `inspect.selection[0]`: 9 → 8 |
| `symbol.spray` | verified | {points: [[x,y]…], name?, radius?: 40, density?: 1..10 (5), scale?: 1, alt?: bool (remove instances)} spray instances into a symbol set → {i… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 513.8787188525215 |
| `symbol.adjust` | ran | {tool: shift\|scrunch\|size\|spin\|stain\|screen\|style, points: [[x,y]…], radius?: 40, intensity?: 1..10 (5), alt?: bool, color?, keepModel… | no change in inspect/json; result={"count": 0} |
| `symbol.libraries` | read-ok | {} → {libraries: [{id, name, category: "builtIn"\|"user" (User Defined: the .vectorcraft files in the user library folder, rescanned now)\|"… | no change in inspect/json; result={"libraries": [{"category": "builtIn", "count": 9, "id": "basic-sh |
| `symbol.library` | refused | {library: id or name} → {id, name, category, symbols: [{name, size: [w, h], registration: 0..8, exportType}] (as symbol.list)} | vectorcraft-cli: step 12 (symbol.library): invalid parameters for `symbol.library`: no symbol librar |
| `symbol.addFromLibrary` | refused | {library: id or name, name? \| names?: [symbol names in the library] (default: all of it), place?: false (also place an instance of the firs… | vectorcraft-cli: step 12 (symbol.addFromLibrary): invalid parameters for `symbol.addFromLibrary`: no |
| `symbol.saveLibrary` | ran | {path?, names?: [symbol names] (default: all), name?: library name (default: the document's), user?: false (save into the user library folde… | no change in inspect/json; result={"count": 1, "dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZnQiLA |
| `symbol.loadLibrary` | ran | {path? \| data?: file text \| dataBase64?, name?: file name (default: the path's)} load the symbols of any document VectorCraft opens (see d… | no change in inspect/json; result={"count": 0, "library": "loaded/<scratch> |

## paint (22)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `paint.setFill` | verified | {color?: "#rrggbb"\|[r,g,b]\|{c,m,y,k}\|{gray}\|{l,a,b} (CIE Lab), none?: true, swatch?: name (a global or spot colour stays linked, so swat… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → #ff0000 |
| `paint.setStroke` | verified | {…as paint.setFill, item?: the stroke item to set} same as paint.setFill, for the stroke | `inspect.layers{id=1}.children{id=3}.stroke`: #000000 → #ff0000 |
| `paint.swap` | verified | {ids?\|id?} swap the fill and stroke of the selection (type too) and of the defaults | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → #000000 |
| `paint.default` | ran | {ids?\|id?} white fill and 1 pt black stroke for the selection and the defaults; type gets black fill and no stroke | no change in inspect/json; result=null |
| `paint.toggleActive` | verified | {fill?: bool (true: bring the Fill proxy forward, false: the Stroke proxy; omitted: swap which is in front)} → {fillActive} | `inspect.paint.fillActive`: True → False |
| `paint.none` | verified | {} set the active proxy (fill or stroke) to None → {objects} | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → None |
| `paint.editGradient` | verified | {stroke?: bool (default: the targeted item's kind, else the active proxy), kind?: linear\|radial\|freeform (freeform places points on each o… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → Linear gradient |
| `paint.setGradientGeom` | verified | {start?: [x,y], end?: [x,y] (document coordinates; both or neither: omitted, the vector stays), aspect?: % (radial: the extent ellipse's hei… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → Linear gradient |
| `paint.sampleColor` | verified | {color, stroke?: bool (default: whichever proxy is active), ids?, stop?: index, clearStroke?: bool} sample a color into the active fill/stro… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → #ff0000 |
| `paint.invert` | verified | {stroke?: bool (default: the active proxy), ids?\|id?, item?: appearance item index\|null, target?: "object"\|"contents"} invert the active … | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → #000000 |
| `paint.complement` | ran | {stroke?: bool (default: the active proxy), ids?\|id?, item?: appearance item index\|null, target?: "object"\|"contents"} replace the active… | no change in inspect/json; result={"changed": 0} |
| `paint.lastColor` | ran | {stroke?: bool (default: the active proxy), ids?\|id?, item?: appearance item index\|null, target?: "object"\|"contents"} apply the last sol… | no change in inspect/json; result={"objects": 2} |
| `paint.lastGradient` | verified | {stroke?: bool (default: the active proxy), ids?\|id?, item?: appearance item index\|null, target?: "object"\|"contents"} apply the last gra… | `inspect.layers{id=1}.children{id=3}.fill`: #ffffff → Linear gradient |
| `paint.recent` | ran | {} → {colors: [{hex, color}] newest first (fed by every paint command and the eyedropper), lastColor: {hex, color}, lastGradient: gradient p… | no change in inspect/json; result={"colors": [], "lastColor": {"color": {"b": 1.0, "g": 1.0, "model" |
| `paint.proxies` | ran | {} → {fill, stroke: the paints the Fill/Stroke proxies show (the Appearance panel's active item for the proxy of its kind, else the first se… | no change in inspect/json; result={"fill": {"color": {"b": 1.0, "g": 1.0, "model": "rgb", "r": 1.0}, |
| `paint.freeform.addPoint` | refused | {at: [x,y] (document coordinates), color? (default: the gradient's colour there), keepModel?: bool (as paint.setFill), opacity?: 0..1 (or 0.… | vectorcraft-cli: step 11 (paint.freeform.addPoint): invalid parameters for `paint.freeform.addPoint` |
| `paint.freeform.setPoint` | refused | {index? (default: the selected point), at?: [x,y] (document coordinates), color?, keepModel?: bool (as paint.setFill), opacity?: 0..1 (or 0.… | vectorcraft-cli: step 11 (paint.freeform.setPoint): invalid parameters for `paint.freeform.setPoint` |
| `paint.freeform.deletePoint` | refused | {index? (default: the selected point), ids?\|id?, stroke?: bool (default: the targeted item's kind, else the active proxy), item?: fill/stro… | vectorcraft-cli: step 11 (paint.freeform.deletePoint): invalid parameters for `paint.freeform.delete |
| `paint.freeform.addLine` | refused | {points: [index, …] (at least two), ids?\|id?, stroke?: bool (default: the targeted item's kind, else the active proxy), item?: fill/stroke … | vectorcraft-cli: step 11 (paint.freeform.addLine): invalid parameters for `paint.freeform.addLine`:  |
| `paint.freeform.splitLine` | refused | {line: line index, segment: the segment from the line's point `segment` to the next, t?: 0..1 along it (default 0.5), ids?\|id?, stroke?: bo… | vectorcraft-cli: step 11 (paint.freeform.splitLine): invalid parameters for `paint.freeform.splitLin |
| `paint.freeform.selectPoint` | refused | {index: point index \| null to clear} select a point of the freeform gradient behind the active proxy (the first selected object's): the poi… | vectorcraft-cli: step 11 (paint.freeform.selectPoint): invalid parameters for `paint.freeform.select |
| `paint.freeform.get` | refused | {stroke?: bool (default: the active proxy)} the freeform gradient behind the proxy of the first selected object → {mode: points\|lines, poin… | vectorcraft-cli: step 11 (paint.freeform.get): invalid parameters for `paint.freeform.get`: the pain |

## view (19)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `view.globalRulers` | verified | {global?: bool (default: toggle)} global rulers measure the whole document from one zero point; artboard rulers (a new document's) from the … | `doc.rulers`: artboard → global |
| `view.drawMode` | ran | {mode?: normal\|behind\|inside} (inside needs one selected path, compound path or type; no param cycles normal → behind → inside → normal, g… | no change in inspect/json; result={"mode": "behind"} |
| `view.proofSetup` | ran | {target?: "workingCmyk"\|"cmyk:<profile>"\|"legacyMacRgb"\|"srgb"\|"monitorRgb"\|"protanopia"\|"deuteranopia"\|"tritanopia", intent?, simula… | no change in inspect/json; result={"intent": "relative", "overprintPreview": false, "proofColors": f |
| `view.proofColors` | ran | {on?: bool (default: toggle)} → proof state | no change in inspect/json; result={"intent": "relative", "overprintPreview": false, "proofColors": t |
| `view.overprintPreview` | ran | {on?: bool (default: toggle)} → proof state | no change in inspect/json; result={"intent": "relative", "overprintPreview": true, "proofColors": fa |
| `view.separationsPreview` | ran | {on?: bool, plates?: [names], toggle?: plate, only?: plate} Separations Preview: show the chosen plates (one plate = greyscale ink coverage)… | no change in inspect/json; result={"on": false, "plates": [{"name": "Cyan", "rgb": [0.0, 0.640795946 |
| `view.capsLock` | ran | {on?: bool} set or read the Caps Lock state the desktop app reports; while it is on, the drawing tools show the precise crosshair, and Use P… | no change in inspect/json; result={"on": false} |
| `view.saved.new` | verified | {name?, center: [x, y], zoom: (1 = 100%), rotation?: deg} save a view in the document (the app fills in the current one; default "View N"; a… | `doc.views[0].center.x`: <absent> → 300.0 |
| `view.saved.edit` | refused | {name, newName?: rename, delete?: bool} \| {edits: [{name, newName?, delete?}…]} rename or delete saved views, all in one undo step; names a… | vectorcraft-cli: step 9 (view.saved.edit): command `view.saved.edit` is not available right now: no  |
| `view.saved.list` | ran | {} → {views: [{name, center, zoom, rotation}]} | no change in inspect/json; result={"views": []} |
| `view.transparencyGrid` | ran | {on?: bool (default: toggle)} show the transparency grid behind the active document's artboards (each document has its own setting) → {on} | no change in inspect/json; result={"on": true} |
| `view.snapToGlyph.options` | read-ok | {baseline?: bool, xHeight?: bool, bounds?: bool, proximity?: bool, angular?: bool, anchors?: bool} the Character panel's Snap to Glyph optio… | no change in inspect/json; result={"anchors": true, "angular": true, "baseline": true, "bounds": tru |
| `view.guides.make` | verified | {} turn the selected paths into guides → {count} | `inspect.selection[0]`: 2 → <removed> |
| `view.guides.release` | refused | {index?: a ruler guide's index, ids?: [guide path id…]} turn guides into paths: index releases that ruler guide and ids release those guide … | vectorcraft-cli: step 9 (view.guides.release): Release Guides: no guides |
| `view.guides.lock` | ran | {locked?: bool} toggle (or set) the session's guide lock; locking deselects the ruler guides and guide paths in every open document → {locke… | no change in inspect/json; result={"locked": true} |
| `view.guides.clear` | ran | {} delete all ruler guides and guide paths → {count} | no change in inspect/json; result={"count": 0} |
| `view.slices.hide` | ran | {hidden?: bool} toggle (or set) whether the canvas hides the slices (session view state); hiding deselects the slices in every open document… | no change in inspect/json; result={"hidden": true} |
| `view.slices.lock` | ran | {locked?: bool} toggle (or set) the slice lock: locked slices can't be selected or edited with the Slice Selection tool; locking deselects t… | no change in inspect/json; result={"locked": true} |
| `view.printTiling` | ran | {on?: bool (default: toggle)} show the pages of the document's print settings on the canvas (each document has its own setting; the Print Ti… | no change in inspect/json; result={"on": true} |

## graphicStyle (18)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `graphicStyle.apply` | refused | {name, add?: bool, ids?\|id? (layers too), target?: "object"\|"contents"} give the objects (default: the selection; a group or layer itself,… | vectorcraft-cli: step 10 (graphicStyle.apply): no graphic style `Test` |
| `graphicStyle.new` | verified | {name?, id?} a style from object `id` or the first selected object: its appearance, opacity, blend mode, isolate and knockout (a group witho… | `doc.graphic_styles{id=5}.appearance.items[0].kind`: <absent> → fill |
| `graphicStyle.delete` | refused | {name} \| {names: [name…]} delete styles; their objects keep their look but are unlinked | vectorcraft-cli: step 10 (graphicStyle.delete): no graphic style `Test` |
| `graphicStyle.duplicate` | refused | {name} → {name} | vectorcraft-cli: step 10 (graphicStyle.duplicate): no graphic style `Test` |
| `graphicStyle.list` | read-ok | {} → {styles: [{id, name, fill, stroke, strokeWidth, fills, strokes, effects: [effect id…], opacity: 0..100, blend, isolate, knockout: "on"\… | no change in inspect/json; result={"overrideCharColor": true, "selected": null, "styles": [{"blend": |
| `graphicStyle.redefine` | refused | {name?, id?} replace the style (default: the one the object was last linked to) with the look of object `id` or the first selected object; t… | vectorcraft-cli: step 10 (graphicStyle.redefine): no graphic style `Test` |
| `graphicStyle.breakLink` | ran | {ids?\|id?, target?: "object"\|"contents"} unlink the objects (default: the selection) from their graphic style; they keep their look | no change in inspect/json; result=null |
| `graphicStyle.rename` | refused | {name, to} (Graphic Style Options; names are unique and linked objects stay linked) → {name} | vectorcraft-cli: step 10 (graphicStyle.rename): no graphic style `Test` |
| `graphicStyle.unused` | read-ok | {} → {names: [the styles no object is linked to]} (the panel selects them) | no change in inspect/json; result={"names": ["Default Graphic Style", "Black Outline", "Heavy Ink",  |
| `graphicStyle.sortByName` | ran | {} sort the styles by name (the Default Graphic Style stays first) | no change in inspect/json; result=null |
| `graphicStyle.merge` | refused | {names: [name…] (two or more), name?} add a style combining the styles' fills, strokes and effects (each style's on top of the ones before i… | vectorcraft-cli: step 10 (graphicStyle.merge): invalid parameters for `graphicStyle.merge`: give two |
| `graphicStyle.move` | refused | {name, to: index} move the style to position `to` of the list (0 = first, clamped), as dragging it in the Graphic Styles panel does | vectorcraft-cli: step 10 (graphicStyle.move): invalid parameters for `graphicStyle.move`: missing `t |
| `graphicStyle.setOptions` | ran | {overrideCharColor?: bool} Override Character Color (the preference `overrideCharColor`, on by default): applying a style to type replaces i… | no change in inspect/json; result={"overrideCharColor": true} |
| `graphicStyle.libraries` | read-ok | {} → {libraries: [{id, name, category: "builtIn"\|"user" (User Defined: the .vcstyles files in the user library folder, rescanned now)\|"loa… | no change in inspect/json; result={"libraries": [{"category": "builtIn", "count": 9, "id": "shadows- |
| `graphicStyle.library` | refused | {library: id or name} → {id, name, category, styles: [{name, fill, stroke, strokeWidth, fills, strokes, effects: [effect id…], opacity, blen… | vectorcraft-cli: step 10 (graphicStyle.library): invalid parameters for `graphicStyle.library`: no g |
| `graphicStyle.addFromLibrary` | refused | {library: id or name, name? \| names?: [style names in the library] (default: all of it), apply?: false (also apply the first one to `ids` o… | vectorcraft-cli: step 10 (graphicStyle.addFromLibrary): invalid parameters for `graphicStyle.addFrom |
| `graphicStyle.saveLibrary` | ran | {path?, names?: [style names] (default: all), name?: library name (default: the document's), user?: false (save into the user library folder… | no change in inspect/json; result={"count": 4, "data": "{\n \"format\": \"vcstyles\",\n \"version\": |
| `graphicStyle.loadLibrary` | ran | {path? \| data?: file text \| dataBase64?, name?: file name (default: the path's)} load a .vcstyles library, or the graphic styles of any do… | no change in inspect/json; result={"count": 4, "library": "loaded/<scratch> |

## brush (18)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `brush.list` | read-ok | {} → {brushes: [{name, type}], current} | no change in inspect/json; result={"brushes": [{"name": "3 pt. Round", "type": "calligraphic"}, {"na |
| `brush.get` | read-ok | {name} → the brush definition (JSON) | no change in inspect/json; result={"angle": 0.0, "name": "3 pt. Round", "roundness": 100.0, "size":  |
| `brush.selectionArt` | ran | {ids?\|id?} → {art: the object brush.new takes as a new scatter or art brush's art and as a new pattern brush's side tile (several objects b… | no change in inspect/json; result={"art": null} |
| `brush.apply` | verified | {name, ids?\|id?} apply a brush to the strokes of the selected paths (adds a stroke if missing) and make it current → {ids} | `doc.unknown.currentBrush`: <absent> → 3 pt. Round |
| `brush.remove` | ran | {ids?\|id?} remove brushes from the selected strokes → {ids} | no change in inspect/json; result={"ids": []} |
| `brush.setCurrent` | refused | {name: string\|null} the brush the Paintbrush tool paints with (not an undo step) | vectorcraft-cli: step 9 (brush.setCurrent): invalid parameters for `brush.setCurrent`: no brush name |
| `brush.new` | verified | {type: calligraphic\|scatter\|art\|pattern\|bristle, name? (trimmed; blank: New <Type> Brush; a bristle brush name, with the number a taken … | `doc.unknown.brushes[0].angle`: <absent> → 0.0 |
| `brush.delete` | verified | {name} \| {names: [name…]} delete brushes; strokes using them become plain strokes | `doc.unknown.brushes[0].angle`: <absent> → 45.0 |
| `brush.move` | verified | {name? \| names?: [brush names of one type, in order], to?: index among the brushes of that type in brush.list order (they go before the bru… | `doc.unknown.brushes[0].angle`: <absent> → 45.0 |
| `brush.duplicate` | verified | {name, newName? (trimmed; blank: <name> copy)} \| {names: [name…]} → {name} \| {names} | `doc.unknown.brushes[0].angle`: <absent> → 0.0 |
| `brush.unused` | read-ok | {} → {names: [the brushes no stroke paints with, in library order]} (the Brushes panel selects them): strokes in the art (opacity masks incl… | no change in inspect/json; result={"names": ["3 pt. Round", "6 pt. Flat", "10 pt. Oval", "Charcoal", |
| `brush.options` | verified | {name, params?: {…fields to change (brush.get shows them; values outside their ranges are clamped). calligraphic: angle −180..180°, roundnes… | `doc.unknown.brushes[0].angle`: <absent> → 0.0 |
| `brush.freehand` | refused | {…params as path.freehand, brush} paint a freehand stroke with a brush → {id} | vectorcraft-cli: step 9 (brush.freehand): invalid parameters for `path.freehand`: missing array `poi |
| `brush.libraries` | read-ok | {} → {libraries: [{id, name, category: "builtIn"\|"user" (User Defined: the .vectorcraft files in the user library folder, rescanned now)\|"… | no change in inspect/json; result={"libraries": [{"category": "builtIn", "count": 5, "id": "art-ribb |
| `brush.library` | refused | {library: id or name} → {id, name, category, brushes: [{name, type}] (as brush.list)} | vectorcraft-cli: step 9 (brush.library): invalid parameters for `brush.library`: no brush library `t |
| `brush.addFromLibrary` | refused | {library: id or name, name? \| names?: [brush names in the library] (default: all of it), apply?: false (also apply the first one to paths, … | vectorcraft-cli: step 9 (brush.addFromLibrary): invalid parameters for `brush.addFromLibrary`: no br |
| `brush.saveLibrary` | ran | {path?, names?: [brush names] (default: all), name?: library name (default: the document's), user?: false (save into the user library folder… | no change in inspect/json; result={"count": 14, "dataBase64": "ewogICJmb3JtYXQiOiAidmVjdG9yY3JhZnQiL |
| `brush.loadLibrary` | ran | {path? \| data?: file text \| dataBase64?, name?: file name (default: the path's)} load the brushes of any document VectorCraft opens (see d… | no change in inspect/json; result={"count": 14, "library": "loaded/<scratch> |

## transparency (17)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `transparency.set` | ran | {ids?\|id?, opacity?: 0..100, blend?: name, isolate?, knockout?: "on"\|"off"\|"neutral"\|bool (true = on, false = neutral), knockoutShape?: … | no change in inspect/json; result=null |
| `transparency.makeOpacityMask` | refused | {ids?, clip?, invert?} the topmost of the selected objects (or of `ids`) becomes the mask of the others (grouped if several; a layer among s… | vectorcraft-cli: step 11 (transparency.makeOpacityMask): the object already has an opacity mask |
| `transparency.releaseOpacityMask` | verified | {id?\|ids?} put the mask art back above each masked object (default: the selection, or the object whose mask is being edited, which leaves m… | `inspect.layers{id=1}.bounds.width`: 200.0 → 400.0 |
| `transparency.disableOpacityMask` | verified | {id?\|ids?} keep the mask but stop applying it | `doc.layers{id=1}.kind.children{id=2}.mask.disabled`: False → True |
| `transparency.enableOpacityMask` | ran | {id?\|ids?} | no change in inspect/json; result=null |
| `transparency.unlinkOpacityMask` | verified | {id?\|ids?} the object moves without its mask | `doc.layers{id=1}.kind.children{id=2}.mask.linked`: True → False |
| `transparency.linkOpacityMask` | ran | {id?\|ids?} | no change in inspect/json; result=null |
| `transparency.setOpacityMask` | verified | {id?\|ids?, clip?, invert?, disabled?, linked?} change the opacity masks of `ids`, the selection, or the object whose mask is being edited | `doc.layers{id=1}.kind.children{id=2}.mask.invert`: False → True |
| `transparency.toggleNewMasksClipping` | ran | {value?} → {value} | no change in inspect/json; result={"value": false} |
| `transparency.toggleNewMasksInverted` | ran | {value?} → {value} | no change in inspect/json; result={"value": true} |
| `transparency.opacityMaskInfo` | ran | {id?\|ids?} → [{id, clip, invert, disabled, linked, art}] the opacity masks of `ids`, the selection, or the object whose mask is being edite… | no change in inspect/json; result=[{"art": 3, "clip": true, "disabled": false, "id": 2, "invert": fa |
| `transparency.info` | read-ok | {id?\|ids?} → {ids, opacity: 0..100, blend, isolate, knockout: "on"\|"off"\|"neutral", knockoutShape, editingMask, pageIsolatedBlending, pag… | no change in inspect/json; result={"blend": "Normal", "editingMask": null, "ids": [2], "isolate": fa |
| `transparency.togglePageIsolatedBlending` | verified | {value?} make the page an isolated group (default: toggle): blend modes of top-level objects don't blend with what lies under the page; save… | `doc.page_isolate`: <absent> → True |
| `transparency.togglePageKnockoutGroup` | verified | {value?} make the page a knockout group (default: toggle): its layers (the contents of neutral layers) hide what they cover instead of showi… | `doc.page_knockout`: <absent> → True |
| `transparency.editOpacityMask` | verified | {id?} edit the mask art of `id` (default: the first selected object with a mask) in place, as clicking the mask thumbnail in the Transparenc… | `inspect.currentLayer`: 1 → 7 |
| `transparency.stopEditingOpacityMask` | refused | {} leave mask editing (the object thumbnail) → {id} | vectorcraft-cli: step 11 (transparency.stopEditingOpacityMask): invalid parameters for `transparency |
| `transparency.viewOpacityMask` | verified | {on?: bool (default: toggle), id?} show only the opacity mask of `id` (default: the object whose mask is edited, else the first selected obj… | `inspect.currentLayer`: 1 → 7 |

## appearance (16)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `appearance.addFill` | verified | {ids?\|id?, target?: "object"\|"contents"} add a fill on top of each selected object's own stack, on an image right below its Contents row (… | `inspect.layers{id=1}.children{id=5}.objectFill`: <absent> → #000000 |
| `appearance.addStroke` | verified | {ids?\|id?, target?} add a stroke on top of each selected object's own stack, on an image right below its Contents row (a copy of its top st… | `inspect.layers{id=1}.children{id=5}.objectFill`: <absent> → None |
| `appearance.clear` | verified | {ids?\|id?, target?} leave each object one empty fill and stroke (None; a group none of its own) and reset its opacity and blend mode | `inspect.layers{id=1}.children{id=5}.objectFill`: <absent> → None |
| `appearance.reduceToBasic` | verified | {ids?\|id?, target?} keep only one visible fill and stroke (without ids: the Appearance panel's active row in place of the topmost one of it… | `inspect.layers{id=1}.children{id=5}.objectFill`: <absent> → None |
| `appearance.setItem` | ran | {index: paint-order item index, ids?\|id? (default: the selection), target?: "object"\|"contents", opacity?: 0..100, blend?: name, visible?:… | no change in inspect/json; result=null |
| `appearance.removeItem` | ran | {index \| indices: [..] (paint-order item indices), ids?\|id?, target?, aligned?: bool (index and item are rows of the first target's stack:… | no change in inspect/json; result=null |
| `appearance.addEffect` | refused | {…as effect.apply} same as effect.apply (an alias): {effect: id, params?: {…}, item?: appearance item index\|null, ids?, target?} → {ids, in… | vectorcraft-cli: step 10 (appearance.addEffect): invalid parameters for `effect.apply`: unknown effe |
| `appearance.duplicateItem` | verified | {index \| indices: [..] (paint-order item indices), to?: paint-order index of the copy (with several, of the lowest copy: they land together… | `doc.layers{id=1}.kind.children{id=6}.appearance.items[1].kind`: stroke → fill |
| `appearance.moveItem` | ran | {from: paint-order item index \| "contents", indices?: [..] (several items instead of from: they move as one block in their order, the lowes… | no change in inspect/json; result={"contents": 0} |
| `appearance.copyFrom` | refused | {source: id, ids?, pickUp?, apply? (trees as eyedropper.setOptions, merged over the Eyedropper Options for this call), reverse?: bool, appen… | vectorcraft-cli: step 10 (appearance.copyFrom): invalid parameters for `appearance.copyFrom`: missin |
| `appearance.setActiveItem` | verified | {index: paint-order item index in the first selected object's stack \| null} make that fill/stroke row the target of the paint.setFill/setSt… | `inspect.paint.appearanceItem`: None → 0 |
| `appearance.showAllHidden` | refused | {ids?\|id?, target?} make every hidden fill, stroke and effect (the object's and each item's) of each selected object visible again; errors … | vectorcraft-cli: step 10 (appearance.showAllHidden): Show All Hidden Attributes: nothing is hidden |
| `appearance.targetContents` | verified | {ids?\|id?, target?: "object"\|"contents"} select the members of the selected groups and layers (or `ids`), as double-clicking the Appearanc… | `inspect.selection[0]`: 7 → 2 |
| `appearance.transfer` | refused | {source: id, target: id, copy?: bool} give `target` (a layer, group or object) the appearance (fills, strokes, effects) and transparency (op… | vectorcraft-cli: step 10 (appearance.transfer): invalid parameters for `appearance.transfer`: missin |
| `appearance.setNewArtBasic` | verified | {on?: bool (omitted: toggle)} the Appearance panel option (the preference newArtBasic, on by default): on, new art takes one fill and stroke… | `inspect.paint.fill`: #ffffff → #000000 |
| `appearance.newArt` | ran | {} what the next object drawn gets → {basic: New Art Has Basic Appearance, appearance: {items, effects} (the model's JSON; placed gradients … | no change in inspect/json; result={"appearance": {"items": [{"kind": "fill", "paint": {"color": {"b" |

## library (16)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `library.list` | read-ok | {} → {libraries: [{id, name, graphics, colors, gradients, patterns, charStyles, paraStyles, groups} (counts)], current: the current library'… | no change in inspect/json; result={"current": "MyLib", "folder": null, "libraries": [{"charStyles":  |
| `library.get` | read-ok | {library?: id or name (default: the current library)} → {id, name, graphics: [{id, name, width, height, thumbnail: PNG base64}], colors: [{n… | no change in inspect/json; result={"charStyles": [], "colors": [], "gradients": [], "graphics": [{"h |
| `library.setCurrent` | refused | {library: id or name} the library the Libraries panel shows, which library commands without a `library` act on → {id} | vectorcraft-cli: step 12 (library.setCurrent): invalid parameters for `library.setCurrent`: no libra |
| `library.create` | ran | {name?: "My Library"} a new empty library (its file in the library folder), made the current one → {id, name} | no change in inspect/json; result={"id": "My Library", "name": "My Library"} |
| `library.rename` | ran | {library?, name} rename a library (default: the current one) → {id, name} | no change in inspect/json; result={"id": "MyLib", "name": "MyLib"} |
| `library.delete` | ran | {library?} delete a library (default: the current one) and its file; not undoable → null | no change in inspect/json; result=null |
| `library.add` | ran | {library?: id or name (default: the current library, made when there is none), kind: graphic\|fillColor\|strokeColor\|fillGradient\|strokeGr… | no change in inspect/json; result={"existing": true, "id": "graphic", "kind": "graphic", "library":  |
| `library.use` | refused | {library?, kind, item: name (graphic: id or name), center?: [x, y] (graphic; default: the first artboard's centre), to?: fill\|stroke (color… | vectorcraft-cli: step 12 (library.use): invalid parameters for `library.use`: kind must be graphic,  |
| `library.removeItem` | refused | {library?, kind, item: name (graphic: id or name)} delete an item (out of its group too) → null | vectorcraft-cli: step 12 (library.removeItem): invalid parameters for `library.removeItem`: kind mus |
| `library.createGroup` | ran | {library?, name?: "Group" (a name the library's groups have, ignoring case, gets a number), items?: [{kind, item}] (moved into it out of the… | no change in inspect/json; result={"group": "Group", "library": "MyLib"} |
| `library.renameGroup` | refused | {library?, group: name, name} rename a group (another group's name, ignoring case, is an error) → {library, group: the new name} | vectorcraft-cli: step 12 (library.renameGroup): invalid parameters for `library.renameGroup`: the li |
| `library.deleteGroup` | refused | {library?, group: name} delete a group: its items stay in the library, ungrouped → {library, ungrouped: how many} | vectorcraft-cli: step 12 (library.deleteGroup): invalid parameters for `library.deleteGroup`: the li |
| `library.moveItem` | refused | {library?, kind, item: name (graphic: id or name), group?: name (null or none: out of its group), before?: item \| after?: item (an item of … | vectorcraft-cli: step 12 (library.moveItem): invalid parameters for `library.moveItem`: kind must be |
| `library.moveGroup` | refused | {library?, group: name, to: index} move a group to position `to` of the library's groups (0 = first; past the end: last), as dragging its he… | vectorcraft-cli: step 12 (library.moveGroup): invalid parameters for `library.moveGroup`: missing `t |
| `library.export` | ran | {library?: id or name (default: the current library), path?} write a library (its colours, gradients, patterns, styles, graphics with their … | no change in inspect/json; result={"data": "{\"name\":\"MyLib\",\"colors\":[],\"charStyles\":[],\"pa |
| `library.import` | refused | {path? \| data?: file text \| dataBase64?, name?: the library's name (default: the file's)} add the library of a .vclibrary file (as library… | vectorcraft-cli: step 12 (library.import): invalid parameters for `library.import`: not a library fi |

## variable (14)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `variable.define` | verified | {name, kind: text\|visibility\|image\|graph} define a variable (graph: CSV data on a graph root); refused while the variables are locked | `doc.variables.variables[1].kind`: <absent> → text |
| `variable.delete` | refused | {names?} delete variables with their bindings and values (default: the highlighted one); refused while the variables are locked | vectorcraft-cli: step 10 (variable.delete): invalid parameters for `variable.delete`: no variable hi |
| `variable.rename` | refused | {name, newName} rename a variable, with its bindings and its values in every dataset; refused while the variables are locked | vectorcraft-cli: step 10 (variable.rename): invalid parameters for `variable.rename`: no variable na |
| `variable.list` | read-ok | {} → variables with kinds and binding counts, and whether they are locked → {variables, locked} | no change in inspect/json; result={"locked": false, "variables": [{"bindings": 0, "kind": "text", "n |
| `variable.makeTextDynamic` | refused | {} define a text variable over the selection, named after it and bound to it; refused while the variables are locked | vectorcraft-cli: step 10 (variable.makeTextDynamic): invalid parameters for `variable.makeTextDynami |
| `variable.makeVisibilityDynamic` | refused | {} define a visibility variable over the selection, named after it and bound to it; refused while the variables are locked | vectorcraft-cli: step 10 (variable.makeVisibilityDynamic): invalid parameters for `variable.makeVisi |
| `variable.makeImageDynamic` | refused | {} define an image variable over the selection, named after it and bound to it; refused while the variables are locked | vectorcraft-cli: step 10 (variable.makeImageDynamic): invalid parameters for `variable.makeImageDyna |
| `variable.makeGraphDynamic` | refused | {} define a graph variable over the selected graph root(s), named after it and bound to it; each dataset row supplies CSV as graph.setData; … | vectorcraft-cli: step 10 (variable.makeGraphDynamic): invalid parameters for `variable.makeGraphDyna |
| `variable.bind` | refused | {variable, ids?} bind objects (default: the selection) to a variable; text needs type, image needs an image object, graph needs a graph root… | vectorcraft-cli: step 10 (variable.bind): invalid parameters for `variable.bind`: nothing to bind |
| `variable.unbind` | ran | {ids?, variable?} drop bindings (default: the selection): `variable` drops that one, else every variable the object has | no change in inspect/json; result={"unbound": 0} |
| `variable.lock` | verified | {locked?: bool} lock or unlock the variables (default: toggle); saved with the document; a change is one undo step. While locked, variable.d… | `doc.variables.locked`: <absent> → True |
| `variable.highlight` | ran | {variable?} highlight one Variables panel row (a click); what the panel's Delete, Options… and Select Bound Object act on. An empty or missi… | no change in inspect/json; result={"variable": null} |
| `variable.loadLibrary` | refused | {path? \| xml? \| dataBase64?} replace the document's variables and data sets with a variable library's (XML: `variableSets` › `variableSet`… | vectorcraft-cli: step 10 (variable.loadLibrary): invalid parameters for `variable.loadLibrary`: the  |
| `variable.saveLibrary` | ran | {path?} write the document's text variables and every data set as a variable library, the XML that variable.loadLibrary reads: a `variable` … | no change in inspect/json; result={"datasets": 0, "skipped": [], "variables": ["v1"], "xml": "<?xml  |

## artboard (13)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `artboard.new` | verified | {x?, y?, width?, height?, name?, color?: color (its background color, as artboard.setProps takes it; default: none), showCenterMark?: bool, … | `inspect.artboards[2].height`: <absent> → 792.0 |
| `artboard.delete` | verified | {index \| indices: [index…]} delete artboards (with their guides) in one step; one is always left, and a locked one is an error | `inspect.artboards[0].name`: Artboard 1 → Artboard 2 |
| `artboard.deleteEmpty` | verified | {} delete every artboard with no artwork on it (no object, hidden, locked and template art included, whose visual bounds meet or touch it, c… | `inspect.artboards[1].height`: 792.0 → <removed> |
| `artboard.setProps` | ran | {index \| artboards: [{index, name?, color?, locked?, showCenterMark?, showCrossHairs?, showVideoSafeAreas?, videoRulerPixelAspectRatio?, x?… | no change in inspect/json; result=null |
| `artboard.fitToArt` | verified | {index?: n \| indices?: [n…] (0-based; the app passes the selected artboards: the Artboard tool's, else the active one; default: the first)}… | `inspect.artboards[0].height`: 792.0 → 508.32399999999996 |
| `artboard.fitToSelection` | verified | {index?: n (0-based; the app passes the active artboard; default: the first)} the artboard fits the selected art (with its strokes); a locke… | `inspect.artboards[0].height`: 792.0 → 121.0 |
| `artboard.move` | verified | {index \| indices: [index…], dx, dy, moveArt?: bool, copy?: bool, patterns?: bool (Transform Patterns: pattern fills and strokes transform w… | `inspect.artboards[0].x`: 0.0 → 10.0 |
| `artboard.convertToArtboards` | verified | {} turn each selected object's bounds into a new artboard (the objects are removed) → {artboards} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 207.82399999999996 |
| `artboard.rearrange` | ran | {layout?: gridByRow\|gridByColumn\|row\|column (gridByRow; byColumn?: true is gridByColumn), order?: leftToRight\|rightToLeft (leftToRight: … | no change in inspect/json; result={"artboards": 2, "columns": 2, "rows": 1} |
| `artboard.reorder` | refused | {index, to} change an artboard's number | vectorcraft-cli: step 10 (artboard.reorder): invalid parameters for `artboard.reorder`: missing to |
| `artboard.duplicate` | verified | {index?: n \| indices?: [n…] (default: the artboards the Artboard tool has selected), art?: bool (default: the Artboard tool's moveArt optio… | `inspect.layers{id=1}.bounds.width`: 400.0 → 1664.0 |
| `artboard.copy` | ran | {index? \| indices?, art?} (defaults as artboard.duplicate) put the artboards, and the art fully inside each when `art`, on the clipboard: e… | no change in inspect/json; result={"copied": 4} |
| `artboard.cut` | verified | {index? \| indices?, art?} artboard.copy, then delete the artboards and that art in one undo step (one artboard is always left: the cut fail… | `inspect.artboards[0].name`: Artboard 1 → Artboard 2 |

## clipboard (12)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `clipboard.exportSvg` | ran | {} → {svg} the copied objects as standalone SVG (null when the clipboard is empty) | no change in inspect/json; result={"svg": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<svg xmlns=\" |
| `clipboard.importSvg` | ran | {svg \| dataBase64 (SVG or SVGZ bytes), center?: [x, y]} replace the clipboard with the SVG's objects (and the images, patterns and symbols … | no change in inspect/json; result={"count": 1} |
| `clipboard.conflicts` | ran | {} → {swatches: [{name, document, clipboard, spot}]} the global or spot swatches the copied objects use whose name the active document gives… | no change in inspect/json; result={"swatches": []} |
| `clipboard.exportPng` | ran | {scale?: 1 (pixels per point, up to 64)} → {dataBase64, width, height (px), warnings} the copied objects cropped to their visual bounds, tra… | no change in inspect/json; result={"dataBase64": "iVBORw0KGgoAAAANSUhEUgAAADUAAAAgCAYAAACy/TBYAAAAAX |
| `clipboard.exportPdf` | ran | {} → {dataBase64, warnings} a one-page PDF of the copied objects, the page their visual bounds (dataBase64 null when the clipboard is empty)… | no change in inspect/json; result={"dataBase64": "JVBERi0xLjcKJYCAgIAKCjEgMCBvYmoKPDwvVHlwZS9QYWdlcy |
| `clipboard.exportText` | ran | {} → {text} the copied type objects' text, one object per line (null unless every copied object is type, or a group of type) | no change in inspect/json; result={"text": "Hello"} |
| `clipboard.flavours` | read-ok | {} → {flavours: [mime…]} what Copy offers other apps for the current clipboard, best first, by the Clipboard Handling preferences: text/plai… | no change in inspect/json; result={"flavours": ["text/plain", "image/svg+xml", "image/png"]} |
| `clipboard.importImage` | refused | {dataBase64 (PNG, JPEG, GIF, WebP, TIFF or BMP bytes), mime?: the type the system clipboard gave (an image/… type; the format is read from t… | vectorcraft-cli: step 10 (clipboard.importImage): invalid parameters for `clipboard.importImage`: no |
| `clipboard.importText` | ran | {text, center?: [x, y]} replace the clipboard with point text of `text` (one paragraph per line; trailing line breaks dropped) in the defaul… | no change in inspect/json; result={"count": 1} |
| `clipboard.importPdf` | refused | {dataBase64, page?: 1, password? (an encrypted PDF), editingData?: false (true: the data is a .ai or .ait file, read as document.open reads … | vectorcraft-cli: step 10 (clipboard.importPdf): invalid parameters for `clipboard.importPdf`: cannot |
| `clipboard.importEmf` | refused | {dataBase64 (EMF or WMF bytes), center?: [x, y]} replace the clipboard with the picture's objects (paths, clipping groups, images, point typ… | vectorcraft-cli: step 10 (clipboard.importEmf): invalid parameters for `clipboard.importEmf`: the da |
| `clipboard.importEps` | refused | {dataBase64 (EPS or other PostScript bytes), center?: [x, y]} replace the clipboard with the picture's objects as document.open reads an EPS… | vectorcraft-cli: step 10 (clipboard.importEps): invalid parameters for `clipboard.importEps`: the da |

## dataset (12)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `dataset.new` | refused | {name, values?: {variable: value}} add a dataset | vectorcraft-cli: step 12 (dataset.new): invalid parameters for `dataset.new`: dataset `DS1` already  |
| `dataset.set` | verified | {name, newName?, values?: {variable: value}} replace a dataset's values; a variable left out loses its value in this row. `newName` also ren… | `doc.variables.datasets[0].values.v1.text`: a → <removed> |
| `dataset.rename` | refused | {name, newName} rename a dataset | vectorcraft-cli: step 12 (dataset.rename): invalid parameters for `dataset.rename`: dataset `DS1` al |
| `dataset.capture` | refused | {name?} record what the bound objects hold right now as a new dataset (Data Set 1…), and make it the active one; a frame of threaded text ho… | vectorcraft-cli: step 12 (dataset.capture): invalid parameters for `dataset.capture`: bind something |
| `dataset.update` | refused | {all?: bool} write what the bound objects hold now into the active dataset, for each variable the dataset holds; a variable whose objects re… | vectorcraft-cli: step 12 (dataset.update): invalid parameters for `dataset.update`: no active data s |
| `dataset.delete` | refused | {names?} delete datasets (default: the active one) | vectorcraft-cli: step 12 (dataset.delete): invalid parameters for `dataset.delete`: no active data s |
| `dataset.list` | read-ok | {} → datasets with their values, the active one, and which rows the art still matches | no change in inspect/json; result={"active": null, "datasets": [{"matches": true, "name": "DS1", "va |
| `dataset.select` | verified | {name} apply a dataset in one undo step (none when it leaves the document as it was), deselecting every selected object left hidden or locke… | `doc.variables.active_dataset`: <absent> → DS1 |
| `dataset.next` | verified | {} apply the next dataset, wrapping | `doc.variables.active_dataset`: <absent> → DS1 |
| `dataset.prev` | verified | {} apply the previous dataset, wrapping | `doc.variables.active_dataset`: <absent> → DS1 |
| `dataset.import` | verified | {path? \| data? \| dataBase64? \| csv?} load datasets from CSV, comma- or tab-separated, in UTF-16 with a byte-order mark, UTF-8 or else Win… | `doc.variables.datasets[1].name`: <absent> → Data Set 1 |
| `dataset.export` | ran | {path?} write every dataset as CSV (header: name, then one column per variable: `#Name` for a visibility variable, `@Name` for an image vari… | no change in inspect/json; result={"csv": "name,v1\nDS1,a\n", "datasets": 1} |

## links (11)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `links.check` | ran | {ids?: [image or placed document ids] (default: every linked image and placed document)} where each linked file is and whether it changed si… | no change in inspect/json; result={"links": [], "missing": 0, "modified": 0} |
| `links.update` | ran | {ids?: [image or placed document ids] (default: the linked images whose file was modified or is showing its preview, and placed documents wh… | no change in inspect/json; result={"missing": [], "updated": []} |
| `links.updateChanged` | ran | {} read again the active document's linked files that changed on disk since they were last seen (size or modification time), whatever Prefer… | no change in inspect/json; result={"ask": [], "modified": [], "updated": []} |
| `links.relink` | refused | {ids?: [image or placed document ids] (default: the selected ones; with folder and nothing selected, every missing link), path \| folder, co… | vectorcraft-cli: step 9 (links.relink): invalid parameters for `links.relink`: object 2 is not an im |
| `links.list` | read-ok | {show?: all (default)\|missing\|modified\|embedded, sort?: name\|kind (file format)\|status (missing, modified, ok, embedded); default: stac… | no change in inspect/json; result={"embedded": 0, "links": [], "missing": 0, "modified": 0} |
| `links.goTo` | ran | {id?} select image or placed document `id` (default: the first selected one); the Links panel scrolls it into view → {id, bounds: [x0, y0, x… | no change in inspect/json; result={"bounds": [156.0, 296.0, 456.0, 496.0], "id": 7} |
| `links.embed` | refused | {ids?: [image or placed document ids] (default: the selected linked ones)} break the links (the Links panel's Break Link): images keep the l… | vectorcraft-cli: step 9 (links.embed): invalid parameters for `links.embed`: object 2 is not an imag |
| `links.unembed` | refused | {id?: an embedded image (default: the one selected), path?} write the image's pixels to the file at path (PNG, JPEG, GIF or WebP as stored, … | vectorcraft-cli: step 11 (links.unembed): invalid parameters for `links.unembed`: image 8 is linked  |
| `links.info` | read-ok | {id?} an image's or placed document's Link Info (default: the one selected) → image.info's fields (id, name, linked, link, colorMode, pixelW… | no change in inspect/json; result={"colorMode": "RGB", "created": 1793852841689, "effectivePpi": [72 |
| `links.placementOptions` | refused | {ids?: [image or placed document ids] (default: the selected ones), preserve?: transforms\|bounds (default)\|fileDimensions\|fit\|fill, alig… | vectorcraft-cli: step 9 (links.placementOptions): invalid parameters for `links.placementOptions`: o |
| `links.findFiles` | ran | {folder?: an absolute path, ids?: [image or placed document ids] (default: the active document's missing links), maxSeconds?: 60 (1 to 600),… | no change in inspect/json; result={"links": [], "state": "idle"} |

## shape (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `shape.rectangle` | verified | {x, y, width, height, radius?: pt, rotation?: deg (about centre)} → {id} | `inspect.objects`: 6 → 7 |
| `shape.ellipse` | verified | {x, y, width, height, rotation?: deg (about centre)} → {id} | `inspect.objects`: 6 → 7 |
| `shape.polygon` | verified | {cx, cy, radius, sides=6, rotation?: deg} → {id} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 607.824 |
| `shape.star` | verified | {cx, cy, radius1, radius2, points=5, rotation?: deg} → {id} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 607.824 |
| `shape.flare` | verified | {cx, cy, diameter=100, opacity=50 (%), brightness=30 (%), growth=20 (%), fuzziness=50 (%), rays=15, longest=300 (%), rayFuzziness=100 (%), r… | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 720.2702567675973 |
| `shape.line` | verified | {x1, y1, x2, y2, fill?: bool (Fill Line: the current fill, else none)} → {id} | `inspect.objects`: 6 → 7 |
| `shape.spiral` | verified | {cx, cy, radius, decay=80 (%), segments=10, clockwise?} → {id} | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 559.5480447996378 |
| `shape.arc` | verified | {x1, y1, x2, y2, closed?, slope?} or {x, y, lengthX, lengthY, reference?, baseAlong?: x\|y, slope?, closed?, fillArc?} → {id} | `inspect.objects`: 6 → 7 |
| `shape.rectangularGrid` | verified | {x, y, width, height, rows=5, columns=5, rowSkew=0, columnSkew=0 (−500…500 %: + crowds the horizontal dividers toward the top, the vertical … | `inspect.objects`: 6 → 18 |
| `shape.polarGrid` | verified | {x, y, width, height, concentric=5, radial=5, concentricSkew=0, radialSkew=0 (−500…500 %: + crowds the ellipses toward the outside, the radi… | `inspect.objects`: 6 → 18 |

## stroke (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `stroke.set` | ran | {weight?: pt, cap?: butt\|round\|square, join?: miter\|round\|bevel, miterLimit?, align?: center\|inside\|outside, dash?: [d,g,…]\|null (a 0… | no change in inspect/json; result={"objects": 2} |
| `stroke.setAdvanced` | refused | {arrowScale?: [start %, end %], swapArrows?: bool, flipProfile?: "along"\|"across", brush?: name\|null, item?: stroke item index\|null, ids?… | vectorcraft-cli: step 9 (stroke.setAdvanced): invalid parameters for `stroke.setAdvanced`: nothing t |
| `stroke.widthProfile.add` | refused | {name?} save the selected stroke's variable width to the Profile list (kept with the preferences) under `name` (default "Width Profile N"; u… | vectorcraft-cli: step 9 (stroke.widthProfile.add): command `stroke.widthProfile.add` is not availabl |
| `stroke.widthProfile.delete` | refused | {name?} remove a saved profile from the Profile list (default: the selected stroke's); built-in profiles can't be deleted, and strokes keep … | vectorcraft-cli: step 9 (stroke.widthProfile.delete): command `stroke.widthProfile.delete` is not av |
| `stroke.widthProfile.reset` | refused | {} remove every saved profile, leaving the built-ins → {removed: count} | vectorcraft-cli: step 9 (stroke.widthProfile.reset): command `stroke.widthProfile.reset` is not avai |
| `stroke.widthProfile.list` | read-ok | {} → {profiles: [{id (stroke.set `profile`), label, builtIn, points: [[t, left, right]…]}], current: the selected stroke's profile id or nam… | no change in inspect/json; result={"current": "uniform", "profiles": [{"builtIn": true, "id": "unifo |
| `stroke.widthPoint.set` | verified | {id, t: 0..1 (fraction of the path length), left, right: side widths in pt, index?: width point to edit or move, adjustAdjoining?: bool (the… | `inspect.layers{id=1}.children{id=2}.strokeOptions.profile`: uniform → custom |
| `stroke.widthPoint.remove` | refused | {id, index \| indices: [..]} remove width points (removing the last one leaves a uniform stroke) | vectorcraft-cli: step 9 (stroke.widthPoint.remove): invalid parameters for `stroke.widthPoint.remove |
| `stroke.widthPoint.copy` | verified | {id, index: the width point to copy, t: 0..1 where the copy goes} → {index} (Alt-drag with the Width tool). Landing on another point makes a… | `inspect.layers{id=1}.children{id=2}.strokeOptions.profile`: uniform → custom |
| `stroke.widthProfile.set` | refused | {ids?\|id?, points: [[t, left, right]…] (width factors, 1 = the stroke weight) \| null = uniform} | vectorcraft-cli: step 9 (stroke.widthProfile.set): invalid parameters for `stroke.widthProfile.set`: |

## charStyle (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `charStyle.list` | read-ok | {} → {styles: [{name, attrs, uses}]} | no change in inspect/json; result={"styles": [{"attrs": {}, "name": "[Normal Character Style]", "use |
| `charStyle.new` | verified | {name? (trimmed, as rename trims `to`), attrs?: {…} (default: selected text), id?, start?: byte, end?: byte} → {name}; a nonempty character … | `doc.char_styles[0].name`: <absent> → Character Style 1 |
| `charStyle.apply` | refused | {name, clearOverrides?, ids?\|id?, start?, end? (id with start and end: a Type tool range; character styles style it, paragraph styles apply… | vectorcraft-cli: step 9 (charStyle.apply): invalid parameters for `charStyle.apply`: no text objects |
| `charStyle.redefine` | refused | {name, id?, start?: byte, end?: byte} from selected text; nonempty character ranges sample their first selected character, start alone keeps… | vectorcraft-cli: step 9 (charStyle.redefine): invalid parameters for `charStyle.redefine`: select te |
| `charStyle.setAttrs` | ran | {name, attrs: {…}} replace the style's attributes; users keep their overrides | no change in inspect/json; result=null |
| `charStyle.duplicate` | verified | {name} → {name} | `doc.char_styles[0].name`: <absent> → [Normal Character Style] copy |
| `charStyle.rename` | refused | {name, to} | vectorcraft-cli: step 9 (charStyle.rename): invalid parameters for `charStyle.rename`: `[Normal Char |
| `charStyle.delete` | refused | {name} \| {names: [name…]} delete styles in one undo step (text keeps its look; never the Normal style) | vectorcraft-cli: step 9 (charStyle.delete): invalid parameters for `charStyle.delete`: `[Normal Char |
| `charStyle.unused` | ran | {} → {names: [the styles no text uses, in panel order; never the Normal style]} (the panel highlights them) | no change in inspect/json; result={"names": []} |
| `charStyle.edit` | refused | {name, to, attrs: {…}} replace name and sparse attributes in one undo step; users keep local overrides | vectorcraft-cli: step 9 (charStyle.edit): invalid parameters for `charStyle.edit`: `[Normal Characte |

## paraStyle (9)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `paraStyle.list` | read-ok | {} → {styles: [{name, attrs, uses}]} | no change in inspect/json; result={"styles": [{"attrs": {}, "name": "[Normal Paragraph Style]", "use |
| `paraStyle.new` | verified | {name? (trimmed, as rename trims `to`), attrs?: {…} (default: selected text), id?, start?: byte, end?: byte} → {name}; a nonempty character … | `doc.para_styles[0].name`: <absent> → Paragraph Style 1 |
| `paraStyle.apply` | refused | {name, clearOverrides?, ids?\|id?, start?, end? (id with start and end: a Type tool range; character styles style it, paragraph styles apply… | vectorcraft-cli: step 9 (paraStyle.apply): invalid parameters for `paraStyle.apply`: no text objects |
| `paraStyle.redefine` | refused | {name, id?, start?: byte, end?: byte} from selected text; nonempty character ranges sample their first selected character, start alone keeps… | vectorcraft-cli: step 9 (paraStyle.redefine): invalid parameters for `paraStyle.redefine`: select te |
| `paraStyle.setAttrs` | ran | {name, attrs: {…}} replace the style's attributes; users keep their overrides | no change in inspect/json; result=null |
| `paraStyle.duplicate` | verified | {name} → {name} | `doc.para_styles[0].name`: <absent> → [Normal Paragraph Style] copy |
| `paraStyle.rename` | refused | {name, to} | vectorcraft-cli: step 9 (paraStyle.rename): invalid parameters for `paraStyle.rename`: `[Normal Para |
| `paraStyle.delete` | refused | {name} \| {names: [name…]} delete styles in one undo step (text keeps its look; never the Normal style) | vectorcraft-cli: step 9 (paraStyle.delete): invalid parameters for `paraStyle.delete`: `[Normal Para |
| `paraStyle.unused` | ran | {} → {names: [the styles no text uses, in panel order; never the Normal style]} (the panel highlights them) | no change in inspect/json; result={"names": []} |

## print (9)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `print.setup` | refused | {preset?: name ([Default] or a saved print preset, any case: print.presets.list; its settings replace the document's, as choosing it in the … | vectorcraft-cli: step 9 (print.setup): invalid parameters for `print.setup`: unknown parameter `inks |
| `print.preview` | ran | {preset?: name (as print.setup's: its settings instead of the document's), settings?: {…settings of print.setup} (over the document's or the… | no change in inspect/json; result={"inks": [], "pages": 1, "settings": {"advanced": {"flattenerPrese |
| `print.presets.list` | read-ok | {} → {presets: [{name, builtIn, settings (as print.setup's), changed: [{option, value}] (how it differs from [Default])}]} [Default] (the de… | no change in inspect/json; result={"presets": [{"builtIn": true, "changed": [], "name": "[Default]", |
| `print.presets.save` | ran | {name?: (default: a new "Print Preset N"), newName?: rename it, preset?: the preset to start from (default: the saved preset `name`, else [D… | no change in inspect/json; result={"created": true, "name": "Print Preset 1", "settings": {"advanced |
| `print.presets.delete` | refused | {name} delete a saved preset ([Default] stays) → {deleted: name} | vectorcraft-cli: step 9 (print.presets.delete): invalid parameters for `print.presets.delete`: no sa |
| `print.presets.export` | refused | {names?: [preset names, [Default] too] (default: every saved preset), path?} write the presets as a .vcprintpresets file (JSON) → {path, cou… | vectorcraft-cli: step 9 (print.presets.export): invalid parameters for `print.presets.export`: no sa |
| `print.presets.import` | refused | {path? \| data?: file text \| dataBase64?, replace?: false (replace saved presets of the same names; else imported ones whose name is taken … | vectorcraft-cli: step 9 (print.presets.import): invalid parameters for `print.presets.import`: not a |
| `print.tiling.set` | refused | {origin: [x, y] (document point: the top-left corner of the first page's imageable area), artboard? (0-based: the artboard it is measured fr… | vectorcraft-cli: step 9 (print.tiling.set): invalid parameters for `print.tiling.set`: give origin:  |
| `print.tiling` | ran | {settings?: {…settings of print.setup} (over the document's)} the pages as View → Show Print Tiling draws them, from print.preview's layout … | no change in inspect/json; result={"pages": [{"artboard": 0, "imageable": [0.0, 0.0, 612.0, 792.0],  |

## effect (8)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `effect.apply` | ran | {effect: id (see effect.list, e.g. "stylize.dropShadow", "distort.roughen", "warp.arc", or "plugin.<id>" for an installed effect plug-in), p… | no change in inspect/json; result={"ids": [5], "index": 1, "item": null} |
| `effect.list` | read-ok | {ids?\|id?: object ids (default: the selection), target?: "object"\|"contents"} → {catalog: [{id, label, menu, params, defaults, raster, len… | no change in inspect/json; result={"activeItem": null, "applied": [{"effects": [{"id": "stylize.drop |
| `effect.remove` | verified | {index: int (position in the effect list), indices?: [int] (several positions in the same list instead of index, removed in one undo step; e… | `doc.layers{id=1}.kind.children{id=5}.appearance.effects{id=stylize.dropShadow}.id`: stylize.dropShadow → <removed> |
| `effect.setParams` | ran | {index: int, params?: {…} (merged into the current parameters), warpStyle?: string (an existing Warp style suffix, e.g. arc or flag; changes… | no change in inspect/json; result={"ids": [5]} |
| `effect.lightingPreset` | refused | {index: int, preset: standard\|diffuse\|topLeft\|right, item?: appearance item index\|null (omitted: the active item, else the object's), id… | vectorcraft-cli: step 10 (effect.lightingPreset): invalid parameters for `effect.lightingPreset`: ob |
| `effect.expandAppearance` | verified | {ids?\|id?: [..], target?} turn each object's appearance into objects: every fill and stroke becomes an object of its own (a stroke stays a … | `inspect.layers{id=1}.bounds.height`: 507.82399999999996 → 524.5 |
| `effect.duplicate` | ran | {index: int, indices?: [int] (several positions in the same list instead of index; every one must exist), item?: appearance item index\|null… | no change in inspect/json; result={"ids": [5]} |
| `effect.move` | refused | {from: int\|[int] (position in the source list; a list moves several effects of that list, which keep their order and land together), to: in… | vectorcraft-cli: step 10 (effect.move): effect.move: no effect at index 1 |

## livePaint (8)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `livePaint.make` | verified | {ids?\|id?} build a Live Paint group from the selected paths (paths, compound paths and groups of them; type, images and other objects are r… | `inspect.layers{id=1}.children{id=12}.children{id=11}.anchors`: 4 → <removed> |
| `livePaint.merge` | verified | {ids?\|id?} add the other selected paths (compound paths, groups of paths and Live Paint groups too; type, images and other objects are refu… | `inspect.layers{id=1}.children{id=12}.children{id=11}.anchors`: 4 → <removed> |
| `livePaint.release` | verified | {id?, ids?: [id…] (instead of id)} replace Live Paint groups with their original paths → {ids} | `inspect.layers{id=1}.children{id=12}.bounds.height`: 120.0 → <removed> |
| `livePaint.expand` | verified | {id?, ids?: [id…] (instead of id)} turn Live Paint groups into plain groups of their painted faces and edges → {ids} | `inspect.layers{id=1}.children{id=12}.children{id=7}.bounds.height`: 120.0 → <removed> |
| `livePaint.gapOptions` | ran | {id?, ids?: [id…] (instead of id; default: the selected Live Paint groups), detect?: bool (Gap Detection: paint stops at gaps up to size wid… | no change in inspect/json; result={"closed": 0, "faces": 2, "gaps": [], "ids": [12]} |
| `livePaint.fill` | ran | {group?: id \| ids?\|id?: [id…] (paths to make live first, as livePaint.make does), point: [x,y], color?\|swatch?\|gradient?\|none? (default… | no change in inspect/json; result={"face": 8, "group": 12} |
| `livePaint.strokeEdge` | refused | {group: id, point: [x,y], color?\|swatch?\|none? (default: current stroke), width?: pt (default: current weight), tolerance?: pt (4), tint?:… | vectorcraft-cli: step 11 (livePaint.strokeEdge): invalid parameters for `livePaint.strokeEdge`: miss |
| `livePaint.info` | refused | {group, id?: object id (default: the selection)} → {faces: [{id, fill, bounds}], edges: [{id, stroke, width}], sources, gapOptions: {detect,… | vectorcraft-cli: step 11 (livePaint.info): invalid parameters for `livePaint.info`: missing group |

## imageTrace (8)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `imageTrace.make` | verified | {id?: image or Image Trace group (default: selection), preset?: name (imageTrace.presets), savedPreset?: {settings} (a saved preset's settin… | `inspect.layers{id=1}.children{id=7}.bounds.height`: 200.0 → <removed> |
| `imageTrace.makeAndExpand` | verified | {…as imageTrace.make} same as imageTrace.make, then expand → {id, paths, anchors, colors} | `inspect.layers{id=1}.children{id=7}.bounds.height`: 200.0 → <removed> |
| `imageTrace.release` | refused | {id?, ids?: [id…] (instead of id)} put the source image back in place of Image Trace groups → {ids} | vectorcraft-cli: step 11 (imageTrace.release): select an Image Trace object |
| `imageTrace.expand` | refused | {id?, ids?: [id…] (instead of id)} keep only the traced paths (drop the source image) → {ids} | vectorcraft-cli: step 11 (imageTrace.expand): select an Image Trace object |
| `imageTrace.setView` | refused | {id?\|ids?: Image Trace objects (default: selection), view: "tracingResult"\|"tracingResultWithOutlines"\|"outlines"\|"outlinesWithSourceIma… | vectorcraft-cli: step 11 (imageTrace.setView): select an Image Trace object |
| `imageTrace.presets` | ran | {} → {presets: [{name, builtIn, params, enhanced: the params of the preset's enhanced version, null if it has none}], revision: grows each t… | no change in inspect/json; result={"presets": [{"builtIn": true, "enhanced": {"autoGrouping": true,  |
| `imageTrace.presets.save` | ran | {name?: (default: a new "Tracing Preset N"), newName?: rename the saved preset `name`, preset?: the preset to start from (default: the saved… | no change in inspect/json; result={"created": true, "name": "Tracing Preset 1", "params": {"autoGrou |
| `imageTrace.presets.delete` | refused | {name} delete a saved tracing preset (built-in ones stay) → {deleted: name} | vectorcraft-cli: step 9 (imageTrace.presets.delete): invalid parameters for `imageTrace.presets.dele |

## plugin (7)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `plugin.list` | ran | {} → {plugins: [{id, name, version, kind: "filter"\|"effect"\|"exporter", author, description, params (doc), paramsSchema, effect? (the effe… | no change in inspect/json; result={"folder": null, "plugins": []} |
| `plugin.info` | refused | {id} → plugin.list's entry plus {manifest, defaults, lastError (a live effect's last failure, null)} | vectorcraft-cli: step 9 (plugin.info): invalid parameters for `plugin.info`: missing `id` (see plugi |
| `plugin.run` | refused | {id, params?: {…} (the plug-in's parameters; or give them as top-level keys; missing ones take their defaults, see plugin.info), ids?: [..] … | vectorcraft-cli: step 9 (plugin.run): invalid parameters for `plugin.run`: missing `id` (see plugin. |
| `plugin.install` | refused | {path: a .wasm file (desktop) \| dataBase64: the module (+ name?: shown as its source), replace?: bool (true: a plug-in with the same id is … | vectorcraft-cli: step 9 (plugin.install): not a valid plug-in module: not a WebAssembly binary (miss |
| `plugin.inspect` | refused | {path: a .wasm file (desktop) \| dataBase64: the module, name?: the file name shown as its source (with dataBase64)} validate a WebAssembly … | vectorcraft-cli: step 9 (plugin.inspect): not a valid plug-in module: not a WebAssembly binary (miss |
| `plugin.remove` | refused | {id} uninstall a plug-in (its live effects then leave the geometry as it is) → {removed} | vectorcraft-cli: step 9 (plugin.remove): invalid parameters for `plugin.remove`: missing `id` |
| `plugin.reload` | refused | {path?: a folder (default: the Additional Plug-ins Folder preference)} install every *.wasm in it (desktop; a bad module is reported and ski… | vectorcraft-cli: step 9 (plugin.reload): <scratch> |

## color (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `color.harmony` | ran | {color, rule: complementary\|complementary2\|splitComplementary\|leftComplement\|rightComplement\|analogous\|analogous2\|monochromatic\|shad… | no change in inspect/json; result={"colors": ["#ff0000", "#00ffff"], "grid": [["#800000", "#9f0000", |
| `color.loadProfile` | refused | {path: .icc/.icm file of at most 32 MB} register an ICC profile (native only). The desktop app and vectorcraft-cli keep a copy of the file i… | vectorcraft-cli: step 9 (color.loadProfile): invalid parameters for `color.loadProfile`: invalid ICC |
| `color.removeProfile` | refused | {name} forget a profile color.loadProfile loaded, and the copy kept of it (built-in profiles and the working spaces stay) → {removed: name} | vectorcraft-cli: step 9 (color.removeProfile): invalid parameters for `color.removeProfile`: no prof |
| `color.convert` | ran | {color, to: "rgb"\|"cmyk"\|"gray"\|"lab", intent?} → {model, values, hex, lab: [L,a,b], outOfGamut, deltaE} | no change in inspect/json; result={"deltaE": 5.523568153381348, "hex": "#ff0000", "lab": [54.2917327 |
| `color.gamutCheck` | ran | {ids?\|id?, colors?: [color]} colours that can't be printed in the working CMYK (selection, or the whole document when nothing is selected) … | no change in inspect/json; result={"checked": 4, "outOfGamut": []} |
| `color.plates` | ran | {} → {on, plates: [{name, spot, visible, rgb}]} | no change in inspect/json; result={"on": false, "plates": [{"name": "Cyan", "rgb": [0.0, 0.640795946 |

## graph (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `graph.create` | verified | {type: column\|stackedColumn\|bar\|stackedBar\|line\|area\|scatter\|pie\|radar, x, y, width, height, series?: [..], categories?: [..], rows?… | `inspect.objects`: 26 → 59 |
| `graph.setData` | ran | {id?, series?, categories?, rows?, csv?: first row = series labels (first cell empty); then one row per category: label; values…; an empty c… | no change in inspect/json; result={"categories": [], "csv": ",,\n1,2\n3,4\n", "rows": [[1.0, 2.0], [ |
| `graph.setType` | ran | {id?, type?, seriesIndexes?: [index], columnWidth?: % (1–1000; past 100 columns overlap), clusterWidth?: % (1–1000), legend?: bool, markPoin… | no change in inspect/json; result={"axisMax": null, "axisMin": null, "categoryTickLength": "none", " |
| `graph.design` | ran | {new?: name\|true (New Design: the selected art becomes a graph design, named "New Design" when true; put a rectangle at the back to set the… | no change in inspect/json; result={"designs": [], "unused": []} |
| `graph.column` | ran | {id?, seriesIndexes?: [index], design?: name\|null, columnType?: vertical\|uniform\|repeating\|sliding, each?: value (more than 0), fraction… | no change in inspect/json; result={"columnType": "vertical", "design": null, "designs": [], "each":  |
| `graph.marker` | ran | {id?, seriesIndexes?: [index], design?: name\|null} draw the data points and legend swatch of the series selected with Group Selection (or l… | no change in inspect/json; result={"design": null, "designs": []} |

## guide (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `guide.add` | verified | {vertical: bool, pos: pt (x for vertical, y for horizontal), artboard?: index (an artboard guide: it runs across that artboard only and move… | `doc.guides[0].layer`: <absent> → 1 |
| `guide.list` | ran | {} → [{index, vertical, pos, selected, artboard?: index (an artboard guide's), layer?: id (the layer it is on), shown, editable (its layer s… | no change in inspect/json; result=[] |
| `guide.select` | verified | {indexes: [index…], toggle?: bool} select ruler guides on their own (deselecting the art); toggle adds or removes them instead, keeping the … | `inspect.selection[0]`: 2 → <removed> |
| `guide.remove` | refused | {index?} delete ruler guide `index`, else the selected ones (as Delete / edit.clear does) → {count} | vectorcraft-cli: step 9 (guide.remove): invalid parameters for `guide.remove`: no guide selected |
| `guide.move` | refused | {index, pos: pt} \| {dx?, dy?: pt, copy?: bool} put ruler guide `index` at `pos`, or move the selected guides (vertical ones by dx, horizont… | vectorcraft-cli: step 9 (guide.move): invalid parameters for `guide.move`: no guide 0 |
| `guide.setLayer` | refused | {index?, indexes?: [index…], layer: id} put ruler guide `index` (or guides `indexes`), else the selected guides, on layer `layer` (a layer o… | vectorcraft-cli: step 9 (guide.setLayer): invalid parameters for `guide.setLayer`: no guide selected |

## flattener (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `flattener.presets.list` | read-ok | {} → {presets: [{name, builtIn, options}]} the built-in presets (High, Medium and Low Resolution), then the saved ones; any of these names w… | no change in inspect/json; result={"presets": [{"builtIn": true, "name": "High Resolution", "options |
| `flattener.presets.save` | ran | {name?: (default: a new "Flattener Preset N"), newName?: rename it, preset?: the preset to start from (default: the saved preset `name`, els… | no change in inspect/json; result={"created": true, "name": "Flattener Preset 1", "options": {"antiA |
| `flattener.presets.delete` | refused | {name} delete a saved preset (built-in ones stay) → {deleted: name} | vectorcraft-cli: step 9 (flattener.presets.delete): invalid parameters for `flattener.presets.delete |
| `flattener.presets.import` | refused | {path? \| data?: file text \| dataBase64?, replace?: false (replace saved presets of the same names; else the imported ones get a number)} a… | vectorcraft-cli: step 9 (flattener.presets.import): invalid parameters for `flattener.presets.import |
| `flattener.presets.export` | refused | {names?: [preset names, built-in ones too] (default: every saved preset), path?} write the presets as a .vcflattener file (JSON) → {path, co… | vectorcraft-cli: step 9 (flattener.presets.export): invalid parameters for `flattener.presets.export |
| `flattener.preview` | ran | {highlight?: "none"\|"rasterizedRegions" (areas the raster/vector balance rasterizes whole)\|"transparentObjects"\|"allAffected"\|"expandedP… | no change in inspect/json; result={"counts": {"allAffected": 0, "allRasterized": 0, "expandedPattern |

## svgInteractivity (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `svgInteractivity.info` | read-ok | {ids?\|id?} → {ids, events: [{event, script}…] in the panel's order \| null (the objects' events differ), files: [the linked JavaScript file… | no change in inspect/json; result={"eventNames": ["onfocusin", "onfocusout", "onactivate", "onmoused |
| `svgInteractivity.setEvent` | verified | {event: "onclick"\|"onmouseover"\|… (svgInteractivity.info's eventNames), script: string (the JavaScript; "" removes the event), ids?\|id?} … | `doc.layers{id=1}.kind.children{id=2}.attrs.events[0][0]`: <absent> → onclick |
| `svgInteractivity.removeEvent` | refused | {event, ids?\|id?} remove an event and its JavaScript from ids or the selection, as one undo step → {changed: objects} | vectorcraft-cli: step 9 (svgInteractivity.removeEvent): invalid parameters for `svgInteractivity.rem |
| `svgInteractivity.clearEvents` | ran | {ids?\|id?} remove every event from ids or the selection, as one undo step → {changed: objects} | no change in inspect/json; result={"changed": 0} |
| `svgInteractivity.addFile` | verified | {file: path or URL (written as given, without surrounding spaces)} link a JavaScript file to the document, after the others: SVG export writ… | `doc.svg_scripts[0]`: <absent> → <scratch> |
| `svgInteractivity.removeFile` | refused | {file} unlink a JavaScript file from the document → {files} | vectorcraft-cli: step 9 (svgInteractivity.removeFile): invalid parameters for `svgInteractivity.remo |

## assets (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `assets.add` | verified | {ids?: [id…] (default: the selected objects; a layer id collects the art under it, including in its sublayers), multiple?: true (an asset pe… | `doc.assets{id=7}.id`: <absent> → 7 |
| `assets.remove` | refused | {assets: [asset id…]} take assets out of the Asset Export panel (their art stays) → {removed: n} | vectorcraft-cli: step 9 (assets.remove): invalid parameters for `assets.remove`: no such assets (see |
| `assets.rename` | refused | {asset: id, name} rename an asset (its files' names) | vectorcraft-cli: step 9 (assets.rename): invalid parameters for `assets.rename`: `asset` is the asse |
| `assets.list` | ran | {} → {assets: [{id, name, nodes: [id…], bounds: [x, y, width, height] \| null (the crop: the bounds the renderer measures for what its art d… | no change in inspect/json; result={"assets": []} |
| `assets.export` | refused | {assets?: [asset id…] (default all), folder?, zip?, openLocation?, formats?, preset?, settings?, prefix?, subfolders?, antiAlias?} each asse… | vectorcraft-cli: step 9 (assets.export): invalid parameters for `assets.export`: no assets yet: coll |
| `assets.settings.set` | ran | {exportPreset?: (a preset of document.exportPresets.list: its formats or preset, its format settings over the saved ones, its prefix (none w… | no change in inspect/json; result={"settings": {}} |

## gradient (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `gradient.selectStop` | ran | {index: stop index (0 = the start) \| null to clear} select a stop of the gradient behind the active proxy (the first selected object's, els… | no change in inspect/json; result={"index": 0} |
| `gradient.presets.list` | read-ok | {} → {presets: [{name, library: the built-in library (theme) it comes from, null for a saved one, builtIn, gradient: {kind, stops, method?, … | no change in inspect/json; result={"presets": [{"builtIn": true, "gradient": {"angle": 0.0, "kind":  |
| `gradient.presets.apply` | refused | {name: a preset's name (gradient.presets.list), stroke?, item?, ids?\|id?, target? (as paint.editGradient)} give the gradient behind the act… | vectorcraft-cli: step 10 (gradient.presets.apply): invalid parameters for `gradient.presets.apply`:  |
| `gradient.presets.save` | ran | {name?: (default: a new "Gradient Preset N"; unique, any case, and not a built-in preset's)} save the gradient behind the active proxy (pain… | no change in inspect/json; result={"name": "Gradient Preset 1"} |
| `gradient.presets.delete` | refused | {name?: a saved preset (default: the saved preset the active proxy's gradient is)} remove a saved preset; built-in presets can't be deleted,… | vectorcraft-cli: step 10 (gradient.presets.delete): command `gradient.presets.delete` is not availab |

## help (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `help.discord` | ran | {} → {url} the ArtCraft community Discord | no change in inspect/json; result={"url": "https://discord.gg/artcraft"} |
| `help.website` | ran | {} → {url} | no change in inspect/json; result={"url": "https://getartcraft.com"} |
| `help.appPage` | ran | {} → {url} this app's page | no change in inspect/json; result={"url": "https://getartcraft.com/apps/vectorcraft"} |
| `help.github` | ran | {} → {url} source code, issues and releases | no change in inspect/json; result={"url": "https://github.com/storytold/vectorcraft"} |
| `help.links` | ran | {} → {discord, website, appPage, github} | no change in inspect/json; result={"appPage": "https://getartcraft.com/apps/vectorcraft", "discord": |

## shaper (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `shaper.scribble` | verified | {points: [[x,y]…], ids?: [id…] (default: nearby art), tolerance?: pt (4)} interior scribbles remove fills; scribbles through several regions… | `inspect.layers{id=1}.children{id=2}.anchors`: 4 → <removed> |
| `shaper.select` | ran | {point: [x,y], source?: bool} click selects a group, then a face; source enters construction isolation and selects an original (while an opa… | no change in inspect/json; result={"id": null} |
| `shaper.release` | verified | {id? (default: selection)} restore the original paths → {ids} | `inspect.layers{id=1}.children{id=8}.bounds`: None → <removed> |
| `shaper.expand` | verified | {id? (default: selection)} keep the visible result as ordinary paths → {id} | `inspect.layers{id=1}.children{id=8}.children{id=7}.bounds.height`: 120.0 → <removed> |
| `shaper.releaseSource` | refused | {source: id, group?: id (default: the Shaper Group that holds `source`)} take one original shape out of its Shaper Group: it becomes a path … | vectorcraft-cli: step 9 (shaper.releaseSource): invalid parameters for `shaper.releaseSource`: sourc |

## pdf (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `pdf.preset.list` | read-ok | {} → {presets: [{name, builtIn, supported (the writer produces its standard), description, settings (as document.pdfSettings)}]} the built-i… | no change in inspect/json; result={"presets": [{"builtIn": true, "description": "Keeps the document  |
| `pdf.preset.save` | ran | {name?: (default: a new "PDF Preset N"), newName?: rename it, description?, preset?: the preset to start from (default: the saved preset `na… | no change in inspect/json; result={"created": true, "name": "PDF Preset 5", "settings": {"advanced": |
| `pdf.preset.delete` | refused | {name} delete a saved preset (built-in ones stay) → {deleted: name} | vectorcraft-cli: step 9 (pdf.preset.delete): invalid parameters for `pdf.preset.delete`: no saved PD |
| `pdf.preset.export` | ran | {names?: [preset names, built-in ones too] (default: every saved preset), path?} write the presets as a .vcpdfpresets file (JSON) → {path, c… | no change in inspect/json; result={"count": 5, "data": "{\n \"format\": \"vcpdfpresets\",\n \"preset |
| `pdf.preset.import` | refused | {path? \| data?: file text \| dataBase64?, replace?: false (replace saved presets of the same names; else imported ones whose name is taken … | vectorcraft-cli: step 9 (pdf.preset.import): invalid parameters for `pdf.preset.import`: not a PDF p |

## recolor (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `recolor.colors` | read-ok | {ids?: object ids (default: the selection, or with nothing selected the objects select.all takes, without the hidden and locked objects insi… | no change in inspect/json; result={"colors": [{"count": 2, "hex": "#000000", "key": "rgb 0 0 0"}, {" |
| `recolor.apply` | refused | {map: rows [{from: [colour keys (recolor.colors) or "#rrggbb" (every colour shown as that hex)], to: colour (hex, key, {c,m,y,k} or {l,a,b})… | vectorcraft-cli: step 9 (recolor.apply): invalid parameters for `recolor.apply`: missing `map` (rows |
| `recolor.reduce` | ran | {colors?: n (rows; default: one per colour, with the tints of a global swatch in its row), method?: as recolor.apply; default scaleTints (pi… | no change in inspect/json; result={"map": [], "method": "scaleTints", "preserved": ["rgb 0 0 0", "rg |
| `recolor.randomize` | refused | {map: rows as recolor.apply, order?: true (shuffle the new colours among the rows that aren't excluded), saturationBrightness?: false (rando… | vectorcraft-cli: step 9 (recolor.randomize): invalid parameters for `recolor.randomize`: missing `ma |

## pattern (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `pattern.options` | ran | {name? (default: the pattern being edited), newName? (trimmed; blank: the name is kept), tileType?, brickOffset?, width?, height?, hSpacing?… | no change in inspect/json; result={"name": "Pat1"} |
| `pattern.delete` | refused | {name} delete a pattern swatch (objects painted with it lose that paint) | vectorcraft-cli: step 10 (pattern.delete): invalid parameters for `pattern.delete`: no pattern `Test |
| `pattern.list` | ran | {} → {patterns: [{name, tileType, width, height, ...}], editing?} | no change in inspect/json; result={"editing": null, "patterns": []} |
| `pattern.transform` | ran | {ids?\|id?, matrix: [a,b,c,d,e,f]} transform only the pattern placement of the objects' pattern paints (Transform Patterns) | no change in inspect/json; result={"count": 0} |

## prefs (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `prefs.get` | read-ok | {key?} → the value of one preference (or preference group: eyedropper), or {prefs: {…all…}} | no change in inspect/json; result={"prefs": {"aicbMode": "preserveAppearance", "alignGlyphBoundsArea |
| `prefs.set` | refused | {key, value} or {values: {key: value, …}} set preferences (validated; see prefs.list; lengths in pt or strings with a unit; unitsGeneral als… | vectorcraft-cli: step 9 (prefs.set): invalid parameters for `prefs.set`: unknown preference `test` |
| `prefs.reset` | ran | {category?} reset one category (or everything) to defaults | no change in inspect/json; result={"prefs": {"aicbMode": "preserveAppearance", "alignGlyphBoundsArea |
| `prefs.list` | read-ok | {} → [{key, category, section, label, kind, value, …}] every preference | no change in inspect/json; result=[{"category": "General", "key": "keyboardIncrement", "kind": "numb |

## colorTheme (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `colorTheme.list` | ran | {} the saved colour themes, in order → {themes: [{name, colors: ["#rrggbb"], keys: [colour keys, exact in each colour's model], rule?}]} | no change in inspect/json; result={"themes": []} |
| `colorTheme.save` | ran | {colors: [1–5 colours] \| color + rule (a harmony rule id or label, see color.harmony: its 5-colour theme from that base colour, base first)… | no change in inspect/json; result={"count": 1, "name": "Theme 1"} |
| `colorTheme.delete` | refused | {name} delete a saved colour theme → {deleted} | vectorcraft-cli: step 9 (colorTheme.delete): command `colorTheme.delete` is not available right now: |
| `colorTheme.addToSwatches` | refused | {name} add a saved theme's colours to the Swatches panel as a colour group named after it (as swatch.newGroup), as one undo step → {name: th… | vectorcraft-cli: step 9 (colorTheme.addToSwatches): invalid parameters for `colorTheme.addToSwatches |

## webExport (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `webExport.settings` | ran | {reset?: false, preset?, …the settings of document.exportForWeb} remember settings for the Save for Web dialog (it opens on them): the keys … | no change in inspect/json; result={"settings": {"antiAlias": "art", "artboard": null, "clipToArtboar |
| `webExport.presets.list` | read-ok | {} → {presets: [{name, builtIn, settings}]} the built-in presets, then the saved ones; any name works as `preset` in document.exportForWeb | no change in inspect/json; result={"presets": [{"builtIn": true, "name": "GIF, 128 colours", "settin |
| `webExport.presets.save` | ran | {name, newName?: rename it, preset?: start from this preset (default: the saved preset `name`, else the defaults), settings?: {…}, …the sett… | no change in inspect/json; result={"created": true, "name": "Test", "settings": {"antiAlias": "art", |
| `webExport.presets.delete` | refused | {name} delete a saved preset (built-in ones stay) → {deleted: name} | vectorcraft-cli: step 9 (webExport.presets.delete): invalid parameters for `webExport.presets.delete |

## dimension (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `dimension.create` | refused | {mode?: linear\|angular\|radius\|diameter, a?: [x,y], b?: [x,y], vertex?: [x,y], source?: {kind: segment, edge: {node,subpath,segment}}\|{ki… | vectorcraft-cli: step 9 (dimension.create): a must be [x,y] |
| `dimension.update` | refused | {ids?: [dimension ids] (default selection), options?: dimension options, offset?: pt} restyle or move existing dimensions → {ids} | vectorcraft-cli: step 9 (dimension.update): Select only dimensions |
| `dimension.applyToAll` | refused | {id?: dimension id (default the first selected dimension)} gives every dimension in the document that dimension's style (its scale too), as … | vectorcraft-cli: step 9 (dimension.applyToAll): Select a dimension first |

## css (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `css.selection` | ran | {ids?\|id?: [id…] (default: the selection), units?: px\|pt\|mm\|cm\|in (default px; 1 px = 1 pt, as in SVG export), position?: false (positi… | no change in inspect/json; result={"css": ".rectangle {\n width: 200px;\n height: 120px;\n backgroun |
| `css.generate` | ran | {…options as css.selection} css.selection of every object in the document | no change in inspect/json; result={"css": ".rectangle {\n width: 200px;\n height: 120px;\n backgroun |
| `css.export` | ran | {path?, scope?: selection\|all (default selection; ids? picks the objects), …options as css.selection, id?: object id (default: the selectio… | no change in inspect/json; result={"data": ".rectangle {\n width: 200px;\n height: 120px;\n backgrou |

## importMatches (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `importMatches.list` | ran | {kind?: name\|key\|modifiers, query?: text (in the name, target or label; any case)} the matches the user confirmed when importing other app… | no change in inspect/json; result=[] |
| `importMatches.set` | ran | {matches: [{kind: name\|key\|modifiers, name: as the file writes it (codes in decimal), target: a command id, tool:<id> or panel:<id> (name)… | no change in inspect/json; result={"count": 0} |
| `importMatches.reset` | ran | {kind?: name\|key\|modifiers} forget the import matches, all of them or those of one kind → {removed} | no change in inspect/json; result={"removed": 0} |

## magicWand (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `magicWand.set` | ran | {fillColor?, fillTolerance?: 0-255, strokeColor?, strokeTolerance?: 0-255, strokeWeight?, weightTolerance?: pt, opacity?, opacityTolerance?:… | no change in inspect/json; result={"blendingMode": false, "fillColor": true, "fillTolerance": 32.0,  |
| `magicWand.options` | read-ok | {} → the Magic Wand settings | no change in inspect/json; result={"blendingMode": false, "fillColor": true, "fillTolerance": 32.0,  |

## shapeBuilder (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `shapeBuilder.merge` | verified | {ids?\|id?: [id…] (default: selection), points: [[x,y]…] (drag path; one point = click; may be left out with rect), rect?: [x, y, width, hei… | `inspect.layers{id=1}.children{id=2}.anchors`: 4 → <removed> |
| `shapeBuilder.regions` | ran | {ids?\|id?, gap?: pt (0–72; 0: Gap Detection off), openFilledAsClosed?: true (as shapeBuilder.merge)} → {regions: [{bounds: [x0,y0,x1,y1], a… | no change in inspect/json; result={"edges": [{"bounds": [100.0, 100.0, 300.0, 220.0], "source": 2},  |

## attributes (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `attributes.info` | read-ok | {ids?\|id?, item?, target?: "object"\|"contents"} → {ids, overprintFill, overprintStroke, showCenter, imageMap: "none"\|"rectangle"\|"polygo… | no change in inspect/json; result={"fillRule": "nonZero", "ids": [2, 3], "imageMap": "none", "note": |
| `attributes.set` | ran | {overprintFill?: bool, overprintStroke?: bool (aimed as object.setOverprint's fill and stroke, item? too), showCenter?: bool (the canvas sho… | no change in inspect/json; result={"changed": 0} |

## tool (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `tool.select` | verified | {tool} e.g. selection, directSelection, pen, rectangle, ellipse, polygon, star, lineSegment | `inspect.tool`: selection → rotate |
| `tool.setOption` | ran | {key?, value? \| values?: {key: value…}, tool?: id (default: the active tool)} → the tool's options (`{}` reads them); kept options last acr… | no change in inspect/json; result=null |

## command (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `command.batch` | ran | {label?, commands: [{command, params}], artboard?: index (the active artboard; the app passes it: each edit.pasteInPlace, edit.pasteInFront,… | no change in inspect/json; result={"results": []} |

## action (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `action.batch` | refused | {commands: [{command, params}] (the action's steps), source?: folder (default) \| datasets, folder? (required for folder: the source folder)… | vectorcraft-cli: step 9 (action.batch): invalid parameters for `action.batch`: commands[0]: missing  |

## node (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `node.move` | refused | {id, parent?: id (null = top level), index} put a row at `index` (0 = bottom) of `parent` (layers only at the top level or in layers), desel… | vectorcraft-cli: step 9 (node.move): invalid parameters for `node.move`: layers go only at the top l |

## eyedropper (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `eyedropper.setOptions` | ran | {sampleSize?: 1\|3\|5 (pixels square averaged when sampling an image: point, 3×3, 5×5), pickUp?, apply?: {appearance?: {transparency?, fill?… | no change in inspect/json; result={"apply": {"appearance": {"fill": {"color": true, "overprint": tru |

## image (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `image.info` | refused | {id?} an image object (default: the one selected) → {id, name, linked, link, colorMode: RGB\|Grayscale\|CMYK, pixelWidth, pixelHeight, ppi: … | vectorcraft-cli: step 9 (image.info): invalid parameters for `image.info`: object 2 is not an image |

## slice (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `slice.list` | read-ok | {} the slices as laid out, numbered left to right and top to bottom → {slices: [{number, id (null for auto slices), source: "user"\|"object"… | no change in inspect/json; result={"clipToArtboard": true, "hidden": false, "locked": false, "slices |

## script (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `script.check` | ran | {path? \| data?: the script's text \| dataBase64?, name?: the file's name (default: the path's; with a path, only the reply's name), include… | no change in inspect/json; result={"directives": [], "dom": {"members": [], "types": []}, "features" |

## shortcutSet (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `shortcutSet.read` | refused | {path? \| data?: the file's text \| dataBase64?, name?: the file's name (default: the path's)} read a shortcut set another app saved as text… | vectorcraft-cli: step 9 (shortcutSet.read): This shortcut file is in a form VectorCraft can't read. |
