# GridCraft reference: log

Part of the gridcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-10-25: first verified run on Linux (0.11.1): headless build/check/eval/info, live cell/table/chart/format/save/PDF,
  screenshots. Reference reading: artcraft-skills `gridcraft` (macOS, MIT) — see repo README credits.
- 2026-10-25 (2): pivots, conditional formats, validation, names, structured refs, spill, sort, filter, charts, CSV import,
  fills verified headless; `range.fill` relative-formula trap found.
- 2026-10-25 (3): formatting, merge, borders, find/replace, hyperlink, comment, sparkline, lookups, page setup/print area, protection verified headless.
- 2026-10-25 (4): goal seek, scenarios, data table, solver, forecast, ToolPak, subtotals, consolidate, advanced filter, trendlines, print setup, dynamic-array functions, JSON import verified.
- 2026-10-25 (5): twelve scripts re-run on 0.11.1 and 0.12.1 (identical); version labels added per section.
- 2026-10-25 (6): live control channel re-tested on the 0.12.1 app (then the window stopped answering screenshots).
- 2026-10-25 (7): pivot fields/calculated fields/show-as/filter/sort/layout/grouping/collapse, pivot chart, 16 chart types and chart-editing commands verified headless on 0.12.1.
- 2026-10-25 (8): 12 conditional-format types, validation types + `data.validate`, all ToolPak tools, threaded comments/notes/protection/edit ranges, 40 functions verified headless on 0.12.1.
- 2026-10-25 (9): cell styles and themes, formatting helpers, table design, slicers (single run), remaining pivot commands, shapes/pictures/text boxes, sheet/view/page helpers and formula helpers verified headless on 0.12.1.
- 2026-10-25 (10): formula auditing, selection helpers, undo/redo, scripts and recording, ink, comments/notes, grouping, rules, objects and print helpers verified headless on 0.12.1.
- 2026-10-25 (11): ink strokes and ink-to-shape (rectangle, ellipse, triangle, line) verified headless on 0.12.1; saved as drawing shapes.
- 2026-10-26: the last 58 command ids run with their setups (smoke test, workbook compared with and without the command).
- 2026-10-27: three-sheet financial model (names, XLOOKUP, sensitivity formula grid, burn alert, cross-sheet chart) built and checked; chart-from-other-sheet traps recorded.
- 2026-10-28: CLI refreshed; nine workbook builds (table, sort, pivot, charts, conditional formats and validation, names and spill, fills/freeze/page setup, filter, financial functions) made with the old and new CLI: identical `cat --formulas`, `info`, `check`, PDF text and 10 PDF pages pixel-identical (only the font `scheme` tag in styles.xml differs). Window commands verified; live app re-checked (cell.set/range.setValues, bold, sheet.read, view.newWindow, window.list/close); `ui.screenshot` timed out (window minimized).
- 2026-10-28 (2): `ui.screenshot` re-checked with the window visible: a 2012×1464 PNG of the blank workbook (ribbon, grid, status bar). It times out ("never reported a capturable size") while the window is minimized: a minimized window cannot be drawn, so ask the user to bring it forward.
- 2026-10-31: CLI refreshed (0.13.0 → 0.14.2); 18 workbook cases (sort, charts, conditional formats, names, number formats and fills, page setup, filter, pivot, financial functions, table total row, macros, CSV, the budget and grades samples) built with the old and new CLI: `cat --formulas`, `info`, `check`, PDF and CSV outputs identical except the new `macro.*` commands (old CLI: unknown command) and `file.exportCsv values`. Two cases (`data.validation`, freeze/rename/insert-sheet/column-width) failed identically on both because my parameters were wrong, so they count as not re-run.
- 2026-11-01: CLI refreshed (0.14.2 → 0.15.0); no new ids; the two changed commands (`range.setValues` conversion report, `formulas.recentlyUsed`) run headless and `check`ed.
- 2026-11-01 (2): full re-run, old (0.14.2) vs new (0.15.0) CLI: 13 workbook scripts (table with total row, sort, pivot, three charts, conditional formats and validation, names/structured refs/spill/XLOOKUP, formatting and page setup, fills/replace/dedupe, financial and date functions, goal seek and subtotals, filter/comment/link/sparkline, macros, sheets) plus the three samples: `.xlsx`, `cat --formulas`, `info`, PDF pages and CSV identical; every `check` clean. The only difference is the new `converted`/`convertedCount` fields in `range.setValues` results. Live channel not re-checked (the app was not running).
- 2026-11-02: CLI refreshed (0.15.0 → 0.16.0); new commands run (Python cells, traceError, Solver save/load/reset and Sensitivity report, equations, chart data table, page order) and the 13 workbook scripts plus three samples re-run old vs new: `cat --formulas`, `info`, PDF and CSV identical; `check` differs only in the output path, `pageSetup` adds `page_order`.
- 2026-11-03: phase 2 on 0.16.0: 50 smoke-tested ids verified (live + headless read-backs by a second agent, reviewed), 8 left; see command-sweep.md.
- 2026-11-03: last research pass (engine source): one command found to do nothing in this version, recorded as checked.
- 2026-11-03: view.showObjects verified in the saved workbook (workbookPr showObjects).
