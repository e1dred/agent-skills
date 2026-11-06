---
name: cadcraft
description: Use when drawing or editing 2D CAD, DXF/DWG files, wiring schematics, floor plans or engineering drawings, exporting drawings to PDF, SVG or PNG, when running cadcraft-cli, or when connecting to the CadCraft app (storytold) on this machine
---

# CadCraft

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

Field notes from one real task (a wiring schematic), last tested on **cadcraft-cli 0.18.0** (Linux AppImage). CadCraft is an AutoCAD-style 2D drafting app (457 commands, DXF/DWG in and out). The CLI, the live control channel and the MCP bridge run the same commands. VectorCraft (illustration, not CAD) was extracted too but not tested; for precise, labelled, orthogonal drawings CadCraft is the better fit.

## Keep this file growing
At the end of every CadCraft task add what you verified (render and look) to the matching file in `reference/` (see the table below), fix what proved wrong, keep it general (no personal data or other people's documents), and add a dated line to `reference/log.md`.

## Setup
- **CLI:** `~/AppImages/cadcraft.appimage --appimage-extract` (in a scratch folder), copy `squashfs-root/usr/bin/cadcraft-cli` to `~/AppImages/`. Never run `--version` on the AppImage itself (it opens the GUI); the CLI answers `--version`. The paths are this author's; the tools in `tools/` take `CADCRAFT_CLI` (the CLI) and `ccmcp.py` takes `CADCRAFT_HOST` (`127.0.0.1:PORT`, default port 47827).
- **Live app:** `cadcraft.appimage --control PORT` (the user starts it). `cadcraft-cli mcp --connect HOST:PORT` is the MCP bridge; without MCP tools in the session use `tools/ccmcp.py` (stdio JSON-RPC client). Tools: `command_line, script, execute, list_commands, inspect_drawing, query_entities, render, find_text, new_drawing, open, save, cancel, screenshot, ui_inspect, ui_click`.
- Helper for drawing: `tools/schem.py` (a `Sheet` that collects commands, then `build()` writes DXF, a white PDF and a PNG). Example: `examples/relay_lamp.py`.

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `schematics.md` | Drawing wiring schematics, checking their connections from the DXF, beginner wiring guides, touching up label clearance | Drawing a schematic; Checking a schematic's connections; Touching up an existing drawing: label clearance; Beginner wiring guide from a schematic |
| `drafting-features.md` | Dimensions, hatch, blocks and attributes, layouts and viewports, plotting to PDF and plot styles (PNG or SVG output: `device` in `newer-commands.md`), text and styles, xref, annotative scales, editing, erase and quick save (undoing an erase: `oops` in `newer-commands.md`) | Round 2; Round 3; Round 4; Round 7; Round 8; Erase and quick save |
| `recipes.md` | End-to-end drawings: a metre-unit floor plan on A3, a parametric plate at true 1:1 | Round 5: end-to-end recipe, a metre-unit floor plan on an A3 sheet; Parametric ECO plate drawing on an A3 sheet at true 1:1 |
| `live-window.md` | Driving the running CadCraft window through its bridge: connecting, clicks, screenshots, a real drawing open live | Live window; Round 6: live window; Round 9: a real drawing in the live window |
| `dwg-files.md` | Opening, editing and saving real AutoCAD DWGs: dynamic blocks, layouts, save versions, constraints | Round 10: a real AutoCAD DWG from another program; Round 11: save versions and the last open items; Round 12: two more AutoCAD DWGs, 2010 format |
| `command-sweeps.md` | Probes of every remaining command id and the last 62 smoke-tested ids | Round 13: the remaining command ids; The last 62 command ids; Verified in detail, CadCraft phase 2; Verified in detail, CadCraft second pass; Verified in detail, CadCraft last id; Ten ids that were only named as ordinary words |
| `newer-commands.md` | What each version added or changed, with exact parameters: oops, -wblock, plot devices, portable fonts, layout save-as, named viewports | 0.15 changes; 0.17 changes; Newer commands |
| `log.md` | Dated log of what was tested when | Log |

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

## Traps
- Unknown or unloaded linetype in `layer.new` fails the whole run.
- Ids that start with `-` (`-block`, `-group`, `-plottermanager`) must be passed as `--cmd=-block {…}` (with `=`); `--cmd -block` is read as a CLI flag ("unexpected argument '-b'"). `tools/ccrun.py` does this.
- PNG export is dark and thin: not for documents.
- Handles are strings; commands that need entities (`block`, `trim`, `hatch`) need the handles from earlier results (use `{last}` or collect them).
- Not possible or not available: authoring dynamic blocks (no commands, UI only). For vector illustration (not CAD) use the vectorcraft skill.
