# PhotoCraft reference: retouching, restoring and colorizing photos

Part of the photocraft skill. The short front page is `../SKILL.md`. Every recipe below was run headless on `.pcraft` copies (one `run` per step or a short chain) and judged on renders at 100%, not only on a downsized overview.

## Which recipe

| Goal | Recipe |
|---|---|
| Polish a product or still-life photo and keep every step editable | A. Non-destructive retouch |
| Enlarge and clean a small, compressed or faded photo; match a reference grade | B. Restore to match a reference |
| Colorize a black-and-white photo when a colour version of the same framing exists | C. Colorize from a colour reference |
| Colorize a black-and-white photo with no reference | D. Colorize by hand |

## Rules that hold for all four

- **Classic tools cannot invent detail** (skin texture, hair strands, stitching). They can match colour and tone and clean the picture; say so before promising a match to an AI-enhanced reference. **PhotoCraft cannot invent colour**: a colorization takes its colours from a reference or from your own choices.
- **Check alignment first** when two pictures of the same framing are involved: a correlation search over scale and shift (best at scale 1.0, shift 0 for the pairs tested). Crop a thin photographic border off a scan before upscaling.
- **`select.subject` is unreliable** (it selected a whole still life, a single shirt): build selections by hand with `select.rect {"ellipse":true,"mode":"add|subtract"}` and `select.lasso {"points":[[x,y],…],"mode":…,"feather":1.5}`, reading coordinates off a **grid overlay** of the picture.
- **Debug every mask** by filling it with `#ff00ff` at opacity 0.5 on a throw-away layer and looking at 100% crops before painting with it.
- **Layer-stack quirks:** a new adjustment layer is created *inside* an active open group and takes a still-active selection as its mask; `layer.moveTo` drops clipping, so clip (`layer.createClippingMask {"layer":id}`) after moving; `layer.layerMask.revealSelection` consumes the selection (a following `select.deselect` errors "no selection"); layers can be addressed by name; a Smart Object cannot be painted on.
- **Measure, then look.** A global error number can improve while faces get worse (a fitted 3D LUT scored better and ruined skin). A saturation map finds leftover grey; only a 100% crop judges faces and edges.

## A. Non-destructive retouch: Smart Object, masked group, frequency separation

Use for a hero object that needs sharpening, local tone work, colour tweaks and a vignette without rasterizing anything.

| Step | Command and values |
|---|---|
| Smart Object + filter | `layer.smartObjects.convertToSmartObject {}`, `layer.setProps {"name":…}`, `filter.sharpen.unsharpMask {"amount":60,"radius":1.2,"threshold":3}` (duplicates inherit smart filters) |
| Subject mask | hand-built selection, then `select.refineEdge {"smooth":2,"feather":0.5,"shiftEdge":-5,"output":"selection"}`, `select.saveSelection {"name":"Subject_Mask"}` (an alpha channel) |
| Masked group | `layer.new.group {"name":"[GRP] Core Subject"}`, then `layer.layerMask.revealSelection {"layer":<group>}` |
| Low / High layers | `layer.duplicate` the Smart Object twice (copies land above the group), `layer.moveTo {…,"target":<group>,"position":"into"}` (Low first, then High). Low: `filter.blur.gaussianBlur {"radius":4}`. High: `filter.other.highPass {"radius":4}`, blend `Linear Light`, **opacity 0.5** |
| Retouch | on a new pixel layer clipped to Low (`layer.new.layer {"clipToPrevious":true}`): `paint.cloneStamp {"size":28,"hardness":0,"opacity":35,"offset":[0,-14],"sampleLayer":"currentAndBelow"}` smooths tone, leaves texture |
| Adjustments | create, `layer.moveTo {"target":<group>,"position":"above"}`, then clip: Curves `[[0,0],[20,15],[128,135],[230,210],[255,255]]`; Hue/Saturation `{"yellows":{"hue":-2,"saturation":8}}` |
| Vignette | `layer.newFillLayer.gradient {"from":"#ffffff","to":"#000000","style":"radial"}` (`from` = centre), blend `Soft Light`, opacity 0.45 |
| Output | `--out x.psd` keeps the group and its mask, Smart Objects with live filters, alpha channel, clipping and blend modes (opacities quantise to 1/255); also a native `.pcraft` and `--out x.jpg --quality 90` |

**Common mistakes:** High Pass at 100% opacity in Linear Light doubles the detail (measured 1.7×); at 0.5 the composite matches the original within 2-5 levels. `image.applyImage` needs a pixel layer, so it means rasterizing; High Pass keeps both layers live. Adjustments created while the group is active end up inside it.

## B. Restore a small compressed photo to match a reference

Use to enlarge and clean a small JPEG or faded scan. Measured outcome against an AI-enhanced reference: colour/tone distance 44 → 23, fine detail 11 → 103 against 614 in the reference.

| Step | Command and values |
|---|---|
| Crop border | `image.crop {"x":5,"y":5,"width":…,"height":…}` |
| Clean at native size | `filter.noise.reduceNoise {"strength":6,"preserveDetails":50,"reduceColorNoise":60,"sharpenDetails":0,"removeJpegArtifact":true}` |
| Upscale | `image.imageSize {"width":…,"resample":"bicubicSmoother"}` |
| Round off block steps, sharpen lightly | `filter.blur.surfaceBlur {"radius":5,"threshold":14}`, `filter.sharpen.smartSharpen {"amount":100,"radius":1.6,"reduceNoise":40}` |
| Colour match | 3D LUT from the pair: `uv run --no-project --with numpy --with pillow python3 tools/fitlut.py SOURCE TARGET out.cube` (system Python has no numpy), then `layer.newAdjustmentLayer.colorLookup {"file":"/abs/out.cube"}`. A faded scan's grade is mostly a black-point lift and a darker, more contrasty curve |
| Texture on a print | `layer.duplicate` the base, `filter.other.highPass {"radius":3}`, Overlay ~0.25, feathered ellipse as layer mask: a thread-like speckle, not real embroidery |
| Subtle eye colour | feathered ellipses on the irises, `layer.new.layer {"mode":"Color","opacity":0.22}`, `edit.fill {"contents":"color","color":"#8a9aa6"}` |
| Film grain | `layer.new.layer`, `edit.fill` `#808080`, `filter.noise.addNoise {"amount":14,"distribution":"gaussian","monochromatic":true,"seed":7}`, Overlay 0.4 (editable, not graded by the LUT below) |

**Common mistakes:** `preserveDetails` and `lanczos` upscales keep JPEG 8×8 blocks as stair-steps that sharpening emphasises. Smart Sharpen at 150-200 / radius 2 gives white halos on high-contrast edges and an oil-painted look. Eye tint at opacity 0.35 with a saturated blue looks painted. The downsized overview hides both the stair-steps and the halos.

## C. Colorize from a colour reference: frequency split

Use when a colour version of the same framing exists. Tone and colour come from a blurred copy of the reference, detail from the original. Result against the reference: colour distance 23.4 → 5.8, fine detail 105 → 251 (reference 253).

| Step | Command and values |
|---|---|
| Base | `image.imageSize {…,"resample":"bicubicSharper"}` to the reference's size (a downscale), `filter.sharpen.unsharpMask {"amount":40,"radius":0.9,"threshold":2}` |
| Low frequency | `file.placeEmbedded {"path":"/abs/reference.png","scale":100,"center":[w/2,h/2]}` lands exactly on a same-size canvas; `filter.blur.gaussianBlur {"radius":10}` |
| High frequency | `layer.duplicate {"layer":"Background","name":"Detail"}`, `layer.moveTo {"layer":"Detail","target":<placed layer>,"position":"above"}`, `layer.select {"name":"Detail"}`, `filter.other.highPass {"radius":10}`, `Linear Light`, opacity 0.55 |
| Fine colour | a second copy of the reference above: `Color` blend, opacity 0.6, `gaussianBlur {"radius":2}` (restores small coloured details) |

**Common mistakes:** one Colour-blend layer over the grey photo cannot follow the reference's re-lighting (lighter skin, darker shirt): distance only fell 23 → 20. A fitted 3D LUT scored 12 but left pale patches and brown blotches on faces. Blur and high-pass radius 18 left a ghost halo beside an ear (a few pixels of misalignment, enlarged); 7-10 was clean. The high-pass radius should equal the blur radius; opacity above 0.6 makes film grain crunchy.

## D. Colorize by hand, without a reference

Use for a black-and-white photo with no colour version. **One solid-colour Fill layer per region:** with a selection active, `layer.newFillLayer.solidColor {"color":"#rrggbb"}` makes it the layer's mask; then `layer.setProps {"name":…,"blend":"Color","opacity":…}`. The photo's brightness stays; only hue and saturation are added. Start every region with a `replace` lasso.

| Region | Colour | Opacity | Mask |
|---|---|---|---|
| Spruce / dark foliage | `#3a6b54` | 0.75 | polygon ∩ `select.colorRange {"select":"shadows","tonalRange":75,"mode":"intersect","fuzziness":20}`, minus hair |
| Lawn | `#7f9a45` | 0.68 | polygons, minus both shirts |
| Shadowed lawn pockets | `#566f38` | 0.75 | polygons following the real gaps |
| Sky | `#8fb4e0` | 0.75 | polygon ∩ highlights (170) |
| Skin | `#d4a38f` / `#c99a80` | 0.7 / 0.68 | face + neck polygons along the real outline |
| Lips | `#b8605c` / `#a96a5e` | 0.6 / 0.55 | small polygons |
| Asphalt | `#7b6f66` | 0.5 | polygon |
| Bronze (lamp cap and frame) | `#8c6038` | 0.7 | polygon minus the glass panes |
| Glass showing foliage | `#3d6b52` Color 0.6 + `#7ea88c` Multiply 0.5 | | pane polygons |
| Shirt (a guess) | `#5f7fa8` | 0.55 | outline expanded ~3 px, also coloured inside the collar |
| White shirt folds | `#9fb0cc` | 0.35 | polygon ∩ midtones [90,230] |

**Grey or greying hair needs five tonal bands**, each its own Color layer from the same hair mask (polygons minus the face polygons, created before the skin layers) intersected with `select.colorRange` (`tonalRange`, `fuzziness` 20-25):

| Band | Colour | Opacity |
|---|---|---|
| Shadows ≤100 | brown `#5c4a3b` | 0.8 |
| Mids [95,145] | ash brown `#8a7b6a` | 0.8 |
| Upper mids [140,190] | soft ash `#b8ab98` | 0.8 |
| Lights [185,225] | warm white `#e2dcd0` | 0.7 |
| Brightest ≥215 | cool silver `#dfe6ef` | 0.6 |

**Review checklist (run it before showing the result):**
1. **Saturation map:** keep pixels with HSV saturation < 0.09 and value 0.10-0.90, paint them magenta on a labelled grid. It finds grey that a glance misses (hair, shadowed pockets, wedges beside a neck, a lamp post, a driveway). White shirts and sky should stay near neutral.
2. **Shared edges:** give two neighbouring masks exactly the same edge points (a shirt and the lawn behind it); expand the neighbour's outline by ~3 px so its bright rim belongs to it, and `subtract` that one polygon from every background mask. A few pixels of gap leave a grey sliver; overlap stacks tints into a lime band; 7 px of expansion leaves a dark band.
3. **Necks and collars:** neck skin runs down to the real neckline; the inside back of a collar is shirt, not skin.
4. **Transparent things show what is behind them** (lamp glass, spectacle lenses).
5. **Seams:** two polygons sharing an edge (tree line over lawn) show a hard line: feather both by ~8.

**Common mistakes:** one faint tint on hair still reads as greyscale (`#b5ada3` at 0.42), one strong warm tint reads as blond (`#bba88f` at 0.55). Dark hair strands inside a foliage polygon turn green unless the hair outline is subtracted. Skin at opacity 0.8 with a saturated tan looks burnt; 0.68-0.7 with a calmer tone looks natural. A hand colorization's global distance to someone else's colorization means little (22.6 vs 23.0 for the plain grey print): judge it by looking. Colours the grey tones can determine (foliage, lawn, sky, skin, metal) are plausible; colours they cannot (a T-shirt, flowers, frames) are guesses: say so.
