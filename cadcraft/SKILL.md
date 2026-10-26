---
name: cadcraft
description: Verified working knowledge for the CadCraft 2D drafting app (storytold, an AutoCAD-style editor for DXF/DWG) driven from an AI agent: the headless cadcraft-cli (run --cmd, export PDF/SVG/PNG), layers, linetypes, text styles, drawing wiring schematics from primitives, the live MCP bridge and its limits. Load before any CadCraft or 2D-drawing/schematic task on this machine, and add what you learn at the end of it.
---

# CadCraft

Field notes from one real task (a wiring schematic), tested on **cadcraft-cli 0.13.0** (Linux AppImage). CadCraft is an AutoCAD-style 2D drafting app (441 commands, DXF/DWG in and out). The CLI, the live control channel and the MCP bridge run the same commands. VectorCraft (illustration, not CAD) was extracted too but not tested; for precise, labelled, orthogonal drawings CadCraft is the better fit.

## Keep this file growing
At the end of every CadCraft task add what you verified (render and look), fix what proved wrong, keep it general (no personal data or other people's documents), add a log line.

## Setup
- **CLI:** `~/AppImages/cadcraft.appimage --appimage-extract` (in a scratch folder), copy `squashfs-root/usr/bin/cadcraft-cli` to `~/AppImages/`. Never run `--version` on the AppImage itself (it opens the GUI); the CLI answers `--version`.
- **Live app:** `cadcraft.appimage --control PORT` (the user starts it). `cadcraft-cli mcp --connect HOST:PORT` is the MCP bridge; without MCP tools in the session use `tools/ccmcp.py` (stdio JSON-RPC client). Tools: `command_line, script, execute, list_commands, inspect_drawing, query_entities, render, find_text, new_drawing, open, save, cancel, screenshot, ui_inspect, ui_click`.
- Helper for drawing: `tools/schem.py` (a `Sheet` that collects commands, then `build()` writes DXF, a white PDF and a PNG). Example: `examples/relay_lamp.py`.

## CLI essentials (verified)
```
cadcraft-cli run [FILE | --sample | --metric] [--script TEXT] [--script-file F.scr] [--cmd 'id {json}']... [--save OUT.dxf] [--export OUT.pdf|svg|png]
cadcraft-cli info FILE.dxf                      # counts per entity type, layers, extents
cadcraft-cli convert IN.dxf OUT.(dxf|dwg|svg|png|pdf) [--window x0,y0,x1,y1 | --view extents]
cadcraft-cli commands [FILTER]                  # JSON: id, label, params string, menu (the parameter docs live here)
```
- `--cmd 'rectang {"p1":[20,20],"p2":[60,50]}'`: the id, a space, then JSON. Results print as `{"handle":"101"}`; `"{last}"` in any parameter means the last handle returned (`viewport.set {"handle":"{last}"}`).
- Use `--metric` for a new millimetre drawing. A failing command stops the run and nothing is saved.
- **Export format matters:** `--export x.png` gives a DARK CAD-themed 2400×1600 picture with hair-thin lines (fine for a quick look); **`--export x.pdf` gives a white page with real colours and lineweights**: use it for deliverables, then `gs -sDEVICE=png16m -r150 -o x.png x.pdf` for a picture. The export view is the current view if you changed it (`zoom {"mode":"window","p1":[0,0],"p2":[420,297]}`), else the drawing extents. `.svg` of a text-heavy drawing is large (9.7 MB for 112 texts).

## Commands used (parameters verified)
- `layer.new {"name","color":1|"red"|index,"lineweight":0.6 (mm),"linetype":"DASHED","current":true}` (a linetype must be loaded first: `linetype {"load":"DASHED"}` or "invalid parameters … is not loaded"); `layer.current {"name"}`; `layer.set {"name","on","frozen","locked","color",…}`. New objects take the current layer.
- Text: the default style "Standard" is a **stick font**; make a readable one first: `style {"name":"SCH","font":"Arial","height":0,"current":true}`. `text {"at":[x,y],"text","height":2.6,"justify":"L|C|R|M|TL…","rotation":90}` (justify with `C`/`R` aligns on `at`), `mtext {"at","text","width",…}`.
- Geometry: `line {"points":[[x,y],…]}`, `pline {"vertices":[…],"closed","width"}`, `circle {"center","radius"}`, `arc {"center","radius","start","end"}` (degrees), `rectang {"p1","p2"}`, `donut {"center","inside":0,"outside":2.2}` (a filled **junction dot**), `ellipse`, `spline`, `point`, `hatch`.
- Editing: `move`, `copy`, `rotate`, `mirror`, `scale {"handles","base","factor"}`, `offset`, `trim`, `fillet`, `stretch`, `array`, `explode`; blocks: `block {"name","base","handles"}` then `insert {"name","at","scale","rotation"}`, `wblock`. Dimensions: `dimlinear`, `dimaligned`, … (not used).
- Output: `export {"path","format"}`, `exportpdf {"path","paper","landscape","fit","scale"}`, `plot`.

## Drawing a schematic (what worked)
1. Plan on a sheet in mm (A3 landscape 420×297): a +V rail and a 0 V rail as long horizontal lines, parts hanging between them, signal flow left to right. Put coordinates in named constants.
2. One **layer per net or role** (supply +, return, trigger, switched, each signal colour, symbols, text, notes, "suggested" changes in dashed green): the legend and later edits (hide a layer) come for free.
3. Symbols from primitives: rectangle plus pads (circles r 1.2) for parts, a diagonal in a box for a relay coil, a line pair and a lifted arm for a switch, a triangle plus a bar for a diode, junction dots with `donut` ONLY where a branch leaves (not at corners).
4. Frame, title, legend and a "how it works" text box make the PDF self-explanatory.
5. Check at 150 dpi in crops (`gs … -r150`, then PIL `crop`): label overlap was the main problem (text near box edges, labels on wires). Keep labels ≥ 2 mm from lines; right-align (`"R"`) labels that sit left of a box.
6. 388 commands for a 1-sheet schematic ran in about a second headless.

## Live window
- `open {"path":"…dxf"}` → `{entities,index,warnings}` opened the drawing as a new document next to the user's empty `Drawing1` (nothing replaced). `execute {"command":"zoom","params":{"mode":"extents"}}` → null.
- **`screenshot` answers "no frame was presented (screen locked or window hidden)" when the window is not visible**; the offscreen `ui.render` renders only the drawing, not the UI. Ask the user to unlock the screen and bring the window forward before any UI test.

## Traps
- Unknown or unloaded linetype in `layer.new` fails the whole run.
- PNG export is dark and thin: not for documents.
- Handles are strings; commands that need entities (`block`, `trim`, `hatch`) need the handles from earlier results (use `{last}` or collect them).
- Not tested: blocks/attributes, dimensions, hatch, paper-space layouts and viewports, DWG output, the `.scr` script form, VectorCraft.

## Log
- 2026-10-25: first task: a 6-switch/relay/controller/strip wiring schematic on A3 (layers, symbols, legend, export to DXF/PDF/PNG), opened in the live window.
