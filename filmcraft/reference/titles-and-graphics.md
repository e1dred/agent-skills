# FilmCraft reference: titles and graphics

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Titles (verified 0.17.0, 2026-11-04)

- `graphics.newText {"text":"Hello FilmCraft","seconds":2,"size":48,"position":[40,140]}` → `{clip:12, layer:0}`.
  It creates a **new graphic clip** on a new video track at the playhead; `newClip:false`/`clip:id` add to an
  existing one. Defaults: text "New Text", size 100 px, 5 s.
- `graphics.set {"clip":12,"layer":0,"props":{"size":32}}` changes properties of an existing layer (font,
  font_style, size, align, tracking, leading, fill_color, stroke/stroke_width, background, shadow, position,
  scale, rotation, opacity); `"keyframe":true` puts a keyframe on every property at `time`.
- `graphics.setText {"clip":12,"layer":0,"text":"New words"}` edits the text; `graphics.setTextType
  {"clip":12,"layer":0,"type":"point|paragraph"}` switches between point text and a wrapping box.
- Shapes: `graphics.newShape {"shape":"rectangle|ellipse|polygon|path","position":[…],"size":[w,h]}`,
  `graphics.newRectangle`, `graphics.newEllipse`, `graphics.newPolygon`; arrange/align/distribute commands exist
  (`graphics.alignFrame.hcenter`, `graphics.align {"align":"left|hcenter|right|top|vcenter|bottom"}`).

## Sizing and fitting (the small-frame trap)

On a **320×180** sequence, the example above ran off the right edge: `graphics.list` reported
`localBounds [0.0, -46.5, 334.734375, 11.578125]` at position [40,140] — the right edge reached 374.7 px and the
render showed "Hello FilmCra" cut at the frame edge. Two verified fixes:

- **Set a smaller size** — `graphics.set {"clip":12,"layer":0,"props":{"size":32}}` → localBounds
  `[0.0, -31.0, 223.15625, 7.71875]`, right edge 40 + 223.2 = 263.2 px, inside the 320 px frame.
- **Use paragraph text in a box**: create with `"box":[240,60]` at `"position":[40,60]`: localBounds `[0,0,240,60]` and the text wraps at the box width, but lines that do not fit the box HEIGHT are clipped: with "Hello FilmCraft" at size 40 the render showed only "Hello". Give the box about 1.3 × size per line (two lines at 40 → height ≥ 104).

Rule of thumb: check `localBounds` width + position x against the sequence width before rendering; point text does
not wrap, boxed paragraph text does.

## Layer properties (read back)

`graphics.list {"clip":12}` → `{canvas:[w,h], clip, duration, layers:[{kind, layer, name, position, localBounds,
box, quad, anchor, effectIndex, enabled}]}`; `graphics.selectLayer`, `graphics.moveLayers {"layers":[0],"delta":[dx,dy]}`,
`graphics.arrangeLayer {"to":"front|back|forward|backward"}` reorder them. `graphics.set` changes what a later
`graphics.list` shows — use that, and `render --seconds S`, to verify a title instead of trusting the create result.
