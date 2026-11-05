# CadCraft reference: newer and changed commands

Part of the cadcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## 0.15 changes (2026-10-31; `solid`, `chprop` and the DXF change were run, the rest is read from `commands`)
- `solid {"points":[[x,y],…]}` draws a 2D solid: three or four points for the first, two more for each next one chained on its last two corners → `{"handles":[…]}` (a SOLID entity in the DXF).
- `chprop {"handles":[…],"layer"?,"color"?,"linetype"?,…}` is `properties.set` that leaves out objects on locked layers → `{changed,locked}`; moving one circle to layer L2 with colour 3 was read back from the DXF (`8 L2`, `62 3`).
- **Help text only:** `ellipse.axis` accepts a point instead of a distance for the other half-axis; `bedit` gained `save` and `check` for switching blocks in the Block Editor.
- **DXF change:** an MTEXT written for a dimension now has group 72 = 5 ("by style") where 0.14.0 wrote 1; nothing else in the dimension drawings changed.

## 0.17.1 changes (verified headless 2026-11-04; DXF read back)
- **Raster images:** `imageattach {"path":"/abs/pic.png","width":100}` (alias `image`, and `attach {path}`, which was "not available yet" before) attaches a PNG; the image list shows pixels, size and status `Loaded`. A **bare relative name is refused** ("file not found"): pass an absolute path or a `data:` URI.
- **`minsert {block, rows:2, columns:3, rowSpacing:20, columnSpacing:20}`** writes a real MINSERT (DXF 70=3, 71=2, 44/45=20).
- **`xclip`** clips block/xref references only (an image answers "select block or xref references"); a query before any clip returns `boundary:null, enabled:false`. `{"option":"new","rectangle":…}` set a 4-point boundary. **`xclipframe`** 2 → 1 read back.
- **`dview {"twist":30}`** and **`view.set {"twist":15}`** rotate the view (`view.get` twist 0 → 15 → 30).
- **`find` takes `types:["MTEXT"]` and `handles:["100"]`** and returns `matches`.
- Regression: PDFs and DXF entities identical to 0.17.0; saved DXF gains DIMSTYLE group 51 = 0.0 (+10 bytes).

## 0.17 changes (verified headless 2026-11-02; DXF and outputs read back)
- **`oops {}`** brings back what the last ERASE, BLOCK or -WBLOCK removed → `{restored:1}` (tested after `erase` and after `-wblock`).
- **`-wblock {"path","handles"|"name","base"?}`** writes the objects to a new drawing and **erases them** from this one (→ `{path,bytes,entities}`); follow it with `oops {}` to keep them. Write it `--cmd=-wblock {…}` (leading dash).
- **`plot {"device":"CADCraft PNG"|"CADCraft SVG"|"CADCraft PDF"|<a PLOTTERMANAGER plotter>|"None"}`** picks the output format: PNG gave a 3508×2480 A4-landscape page at 300 dpi, SVG a vector file. The PNG call that ran: `plot {"path":"/abs/p.png","layout":"Model","device":"CADCraft PNG","fit":true}`. `publish` takes `device` too but always writes PDF.
- **`saveas {"path","portableFonts":true}`** (and DXF `export`) swaps Linux fonts for their Windows equivalents in that file: a text style on "Liberation Sans" was saved as `arial.ttf`, with the original name kept in the style's extended data (group 1000 `FONT`); "DejaVu Sans" (no Windows equivalent) stayed as it was. Use it for DXFs going to AutoCAD on Windows.
- `info` has a new `readNotes` list (empty for drawings CadCraft wrote).

## Newer commands (verified headless and live)
- `blocks.description {"name","description"}` → `{block,description}`; `description` is required (an empty string clears it; there is no read form). `block {…,"description":"…"}` sets it at creation (it is stored in the DXF). Up to 255 characters, one line.
- `layout.saveas {"name"?,"path"}` (also `layout {"option":"saveas","name","path"}`) → `{name,path,bytes}`; a path with no extension gets `.dwt`; `.dwg` and `.dxf` are accepted. It writes wherever the path says: use a scratch folder.
- `vports.named {"name"?,"delete"?,"p1"?,"p2"?,"layout"?}`: no name lists `{current,configurations:[{name,viewports}]}`; a name restores a saved configuration (an unknown name is an error); on a layout it puts one viewport per tile over p1–p2 or the printable area. Save one first: `-vports {"option":"2","arrangement":"vertical"}` then `-vports {"option":"save","name":"TwoUp"}`.
- Traps: a `--cmd` value starting with `-` must be written `--cmd=-vports {…}` (the CLI reads a separate `-vports` as a flag); `"{last}"` works in headless `run` but a live `execute` needs the real handle (`"100"`).
- 2026-10-28 (2): live `screenshot` re-checked with the window visible: a 2204×1380 PNG written to a temp folder (the tool prints the path).
- 2026-10-31: CLI refreshed (0.14.0 → 0.15.1); the relay-lamp example plus eight drawings (shapes and text, dimensions, hatch, blocks, properties, copy/move/offset/mirror) built with the old and new CLI: DXF, PNG and PDF identical except the dimension MTEXT group 72 above; `solid` and `chprop` verified (they do not exist in 0.14.0).
- 2026-11-01: CLI refreshed to 0.16.0; beginner wiring guide (hex layer colours, solid triangles, hop crossings, net check with arcs).
- 2026-11-01 (2): full re-run, old (0.15.1) vs new (0.16.0) CLI: six drawings (shapes, text styles and justification, layers and linetypes, dimensions and hatch, blocks and inserts, copy/rotate/mirror/scale/offset) plus `examples/relay_lamp.py`: DXF entity, table and block sections, `info` and PDF pages identical. Live bridge not re-checked (the app was not running).
- 2026-11-02: CLI refreshed (0.16.0 → 0.17.0); full re-run old vs new (six drawings plus relay-lamp): entities, tables and PDF identical; `info` adds `readNotes`, the text drawing's DXF grew 34 bytes outside the entity, table and block sections (not examined). New commands run: oops, -wblock, plot devices, portableFonts.
