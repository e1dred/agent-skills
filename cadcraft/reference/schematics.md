# CadCraft reference: schematics

Part of the cadcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Drawing a schematic (what worked)
1. Plan on a sheet in mm (A3 landscape 420×297): a +V rail and a 0 V rail as long horizontal lines, parts hanging between them, signal flow left to right. Put coordinates in named constants.
2. One **layer per net or role** (supply +, return, trigger, switched, each signal colour, symbols, text, notes, "suggested" changes in dashed green): the legend and later edits (hide a layer) come for free.
3. Symbols from primitives: rectangle plus pads (circles r 1.2) for parts, a diagonal in a box for a relay coil, a line pair and a lifted arm for a switch, a triangle plus a bar for a diode, junction dots with `donut` ONLY where a branch leaves (not at corners).
4. Frame, title, legend and a "how it works" text box make the PDF self-explanatory.
5. Check at 150 dpi in crops (`gs … -r150`, then PIL `crop`): label overlap was the main problem (text near box edges, labels on wires). Keep labels ≥ 2 mm from lines; right-align (`"R"`) labels that sit left of a box.
6. 388 commands for a 1-sheet schematic ran in about a second headless.

## Checking a schematic's connections (verified)
Parse the saved ASCII DXF (LINE, small LWPOLYLINE donuts for junction dots, CIRCLE pads) and union the wire endpoints; a wire connects to another only at a shared endpoint or a junction dot. Compare the resulting nets with the written connection list, and report T-contacts without a dot and wire crossings. It confirmed a 6-switch/relay/controller drawing net by net (0 crossings). It proves the DRAWING matches the text, not that the real parts behave as described.

## Touching up an existing drawing: label clearance (2026-10-26; before/after PDFs looked at)
> A finished 285-entity schematic was copied, checked and edited without changing any geometry (same entity counts before and after); the original files were left alone and the result saved under new names.
- **Find tight labels by script:** `entities {"type":"Text","limit":500}` gives each text's `insert`, `height`, `halign` (left/center/right), `valign`, `rotation`; estimate its box as width = 0.52 x height x characters, expand it by 1 mm, and test it against every `Line` segment and `Polyline` segment (`geometry.vertices[].p.{x,y}`, closed polylines add the last edge) and against other texts. It flagged the six switch symbols (12 hits: "SW1" and "LED OUT +" hugging the box outline) and nothing else, which matched what the 220 dpi render showed.
- **Fix with `move {"handles":[h],"delta":[dx,dy]}`** on the copy (`run copy.dxf --cmd 'move {...}' ... --save new.dxf --export new.pdf`): +1.2/+1.0 mm for the switch name labels and -1.5/+1.4 mm for right-aligned pin labels cleared the box edges (hits 12 to 0); pin labels beside a terminal circle moved 2 mm away from it.
- **Check every nudge in the render:** moving "DC IN +" 2 mm right made it run into the next text line ("controller"), and moving it down put it against the switch's contact arm: both were reverted. The script's text-width estimate did not catch the first (0 hits) because the neighbouring text was centred: always look at the crop at 220 dpi (`gs -sDEVICE=png16m -r220`) before and after.

## Beginner wiring guide from a schematic (2026-11-01, CLI 0.16.0 headless; PDF rendered and looked at, nets checked)
> A "where every wire goes" sheet for someone who cannot read schematics: real parts as boxes with their printed terminal labels, every wire numbered (W1…) with a matching From/To/Colour/Size table, splices drawn as bars, a colour key and a "how to read this" box.
- **`layer.new {"color":"#7a3db8"}` takes a hex colour** and the PDF prints exactly that RGB (checked by pixel count): match a drawing's colours to other pictures of the same job.
- **`solid {"points":[[x,y],[x,y],[x,y]]}` (three points) is a filled triangle**: a diode arrow (plus a line for the bar) without hatch handles.
- **Show a crossing without a join as a hop:** stop the line 2 mm either side, `arc {"center","radius":2,"start":0,"end":180}`, continue. A net check that reads only LINE/LWPOLYLINE sees the hop as a break, so **include ARC endpoints** (centre ± radius at the start/end angles) when you union wire ends.
- **Net check against named terminals:** give each terminal a point and a tolerance (pad radius; a socket circle 3.6), treat closed polylines used as splice bars as one node (any wire end on the rectangle joins), union the rest by shared endpoints, and print each net's terminal names to compare with the wire table. It confirmed all 12 nets; loose ends were only the hop and the diode body (by design).
- **Layout lessons from the render:** wire tags sitting ON a wire make the line cut the number; put them 4–5 mm beside it. Three-character tags (W10) need a 3.4 mm circle and 1.65 mm text. Labels for a box's pins go outside the box when the box text is big ("LED DRIVER" ran into "N"). A note placed right of the last part ran past the frame: right-align it on the free side.
- **Revising a finished schematic in place (same day, v2 → v3 on a copy):** `run old.dxf --cmd … --save new.dxf` with `erase {"handles"}` for a removed channel, `properties.set {"handles","layer"}` to move wires to new layers (made with `layer.new` hex colours), `textedit {"handle","text"}` (centred and right-aligned texts keep their alignment point), `move` for labels that collide, then `purge` (it also deletes layers that were already unused). Re-running the net check on the result confirmed every net; the renders showed two new collisions (a longer label running into a wire and a pin label), both fixed by shortening or moving the text.
- **0.16.0** adds `-array`, `-units` and `change` (from a `commands` diff; not run). The drawing above built with no errors on 0.16.0.
