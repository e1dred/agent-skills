# CadCraft reference: log

Part of the cadcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log
- 2026-10-25: first task: a 6-switch/relay/controller/strip wiring schematic on A3 (layers, symbols, legend, export to DXF/PDF/PNG), opened in the live window.
- 2026-10-26: round 2 (headless + live bridge): dimensions, hatch/gradient, blocks/attributes, layouts/viewports/PDF, editing, properties, DWG, .scr; `tools/ccrun.py`.
- 2026-10-26: round 3: tables, data extraction, overkill, regions, mline, tolerance, constraints.
- 2026-10-26: round 4: rich text, exports/plot options, xref attach, mleader/table styles, scales, dimbreak, hatchedit, splinedit, tiled viewports, autoconstrain.
- 2026-10-26: round 5: floor-plan recipe on an A3 layout; viewport scale and annotation-height traps.
- 2026-10-26: round 6: live window (screenshots, click-driven drawing, selection, what ui_click cannot do).
- 2026-10-26: round 7: block editor, refedit, attribute manager, .ctb plot styles, publish, qdim.
- 2026-10-26: round 8: annotative scaling, real-drawing edit run, basic 3D.
- 2026-10-26: round 9: real drawing in the live window; find_text contains; selecting in dense drawings.
- 2026-10-26: round 10: real AutoCAD DWG (layout, multileaders, dimensions, dynamic block read/edit), release check against GitHub.
- 2026-10-26: round 11: save versions 2000-2018, dynamic-block authoring ruled out.
- 2026-10-26: round 12: parametric imperial part (constraints not imported, metric scaling), dynamic ISO title block (visibility states).
- 2026-10-26: gap round: erase and qsave.
- 2026-10-26: round 13: the remaining draw/dimension/constraint/layer/table/view/layout/settings ids (no live window).
- 2026-10-26: the last 62 command ids run with their setups (smoke test).
- 2026-10-26: label-clearance touch-up of a finished schematic (text-box vs segment check, `move` deltas, render comparison).
- 2026-10-27: parametric ECO plate (Config_Params.txt), block files with attributes, true 1:1 A3 PDF (fit:false), radius text override.
- 2026-10-28: CLI refreshed; five drawings (shapes and text, dimensions and hatch, blocks, copy/offset/mirror/array, the relay-lamp example) built with the old and new CLI: identical DXF (handles aside), `info`, SVG and PDF pixels. Three new commands verified (below); live window re-checked on a scratch drawing (`new_drawing`, `execute`, `inspect_drawing`, `render`, `close`).
- 2026-11-03: phase 2 on 0.17.0: 60 smoke-tested ids verified by read-backs (list/getvar/DXF), 2 left; ccrun.py now passes --cmd=… so dash ids work.
- 2026-11-03: `-plottermanager` verified (same JSON as plottermanager); CadCraft smoke-tested list complete and removed.
- 2026-11-03: coverage.sh now counts a CadCraft id only where it is written as a command; that showed 10 ids named only as words (join, new, base, dim, snap, polar, status, redraw, attach, grip), now documented (7 run and read back, 3 with reasons).
