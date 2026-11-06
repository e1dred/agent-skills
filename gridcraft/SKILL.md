---
name: gridcraft
description: Use when building, editing, checking or converting spreadsheets (.xlsx, .csv), formulas, pivots or charts, when running gridcraft-cli, or when connecting to the GridCraft app (storytold) on this machine
---

# GridCraft

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates; only present in a full clone of the repo, otherwise compare `gridcraft-cli --version` with the app's version in its About box or on its releases page by hand; `--version` on an AppImage can open the app). A CLI older than its app has caused real failures. In a full clone, `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, last tested on **gridcraft-cli 0.17.0** (Linux AppImage). GridCraft is an alpha, Excel-style
spreadsheet in Rust. Every ribbon button is an *engine command* (385 of them); the CLI, the MCP server and the app's
control channel all run the same commands. If `gridcraft-cli version` is newer, re-check before relying on this.

## Keep this file growing

This guide is built up as tasks happen. At the end of every GridCraft task:
- Add any command, parameter format, recipe or trap you verified to the matching file in `reference/` (see the table below).
- Correct anything here that turned out to be wrong (don't leave stale claims).
- Only record what you actually confirmed (by rendering, `check` or reading back); mark guesses as unverified.
- Keep it general: no personal data, names or machine-specific paths (this file is meant to be shared).
- Add a dated line to `reference/log.md`.

## Surfaces

> One `send` failed once with "not reachable: Resource temporarily unavailable", and after the first batch `ui.screenshot` and `ui.inspect` hung until killed (the app still answered earlier commands; same symptom as PhotoCraft's stalled window, cause not determined, so bring the window to the front and retry).

- **Headless CLI** (no window, deterministic; best for building/reading/verifying files):
  `info FILE`, `cat FILE [--range A1:D9] [--formulas|--csv]`, `eval '=FORMULA' [--in FILE]`,
  `run [--in FILE|--sample budget|sales|grades] --cmd 'id={json}'... --out FILE [--print RANGE]`,
  `check FILE|DIR [--json]`, `convert IN OUT` (xlsx/csv/tsv/json/html/pdf by extension),
  `commands --search X` (ids + parameter docs), `functions --search X`.
- **Live app**: start it with `--control PORT`; then `gridcraft-cli send PORT METHOD '{json}'` (prints the JSON reply).
  Methods used and confirmed: `engine.execute {"command":ID,"params":{…}}`, `ui.inspect`, `document.inspect`,
  `sheet.read {"range":"A1:D5"}`, `cell.get {"cell":"A1"}`, `engine.journal {"limit":N}`, `ui.screenshot {"path":…}`,
  `ui.click {"x":…,"y":…}` (screen points), `ui.key {"key":"Escape"}`.
- **MCP**: `gridcraft-cli mcp --connect PORT` (live) or `gridcraft-cli mcp` (headless). If the MCP server shows
  "failed to connect" at session start, the app was not running yet — `send` over the CLI works regardless.

`gridcraft-cli send` also accepts a command id as the method (`cell.get`, `sheet.read` are methods; `ui.backstage` is
**not** a method — run it through `engine.execute`).

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `recipes.md` | Worked builds to copy: budget/sales/grade recipes, a three-sheet financial model, macros and CSV export | More recipes; Three-sheet financial model: names, lookups, sensitivity grid, cross-sheet chart; Macros and CSV values |
| `formatting-and-sheets.md` | Number formats, fills, borders, cell styles, tables, slicers, objects, sheet management, view | Everyday formatting and sheet editing; Cell styles, table design, slicers, objects, sheets, view and helper commands |
| `analysis-pivots-charts.md` | What-if, Solver (saving, loading or resetting a Solver model in cells and the Sensitivity report: `newer-commands.md`), forecast, pivot tables, every chart type, conditional formats, validation, ToolPak, review and functions | Analysis and layout tools; Pivot tables and chart types in depth; Conditional formats, validation, ToolPak, review and functions |
| `auditing-and-helpers.md` | Formula auditing, selection, scripts, comments, grouping, print helpers, ink | Formula auditing, selection, scripts, ink, comments, grouping and print helpers; Ink in GridCraft |
| `newer-commands.md` | What each version added or changed (0.12 onward), with exact parameters: Python cells, Trace Error, Solver models, equations, chart data tables | New in 0.12.x; Newer commands; 0.15 changes; 0.16 changes; 0.17.0 changes |
| `command-sweep.md` | The last 58 command ids, smoke-tested on a blank workbook | The last 58 command ids; Verified in detail, GridCraft phase 2; Verified in detail, GridCraft second pass; Checked, no effect in this version; Verified in detail, GridCraft show objects; Verified in detail, GridCraft formula bar and ruler; Checked, no effect on Wayland |
| `log.md` | Dated log of what was tested when | Log |

## Command formats (verified)


| Goal | Command |
|---|---|
| one cell | `cell.set {"cell":"A1","input":"=B2*C2"}` (input is a string; `=` starts a formula; returns the computed value) |
| many cells | `range.setValues {"range":"A2","values":[["a",3,4.5,"=B2*C2"],…]}` → `{"cells":N}` |
| read | `sheet.read {"range":"A1:D5","formulas"?:true,"formatted"?:true}` |
| bold | `home.bold {"range":"A1:D1","on":true}` — **a toggle if `on` is omitted** |
| number format | `home.numberFormat {"range":"C2:D5","format":"Currency"}` (or `"code":"0.00"`) |
| col width | `home.autofitColumnWidth {"cols":"A:D"}`, `home.columnWidth {"cols":"B:D","width":64}` |
| table | `insert.table {"range":"A1:D5","header":true,"style"?,"name"?}` |
| chart | `insert.chart {"range":"A1:A5,D1:D5","type":"column","title":"Totals","at"?:"H2"}` (comma-separated ranges work) |
| sort | `data.sort {"range","header":true,"keys":[{"column":"B","order":"desc"}]}` |
| save | `file.saveAs {"path":…}` (.xlsx default; `.csv .tsv .json .html .pdf` by extension) |
| PDF | `file.exportPdf {"path":…,"sheets":"active|all","range"?,"fitToPage"?}` → `{pages,bytes,path}` |

## Traps

- `home.formatCells` takes a *struct* for fills (`"fill":"#DDEBF7"` is rejected: "expected struct Fill"); check
  `gridcraft-cli commands --search formatCells`/`describe` or use `home.*` helpers. Font bold via `{"font":{"bold":true}}` works.
- `home.bold` without `on` toggles — a second call undoes the first. Always pass `on`.
- A blank new window can be sitting on a **Backstage** page (`ui.inspect` → `"backstage":"home"`/`"saveAs"`), which hides
  the grid in screenshots. Click Back (≈ x70,y90 in the 1504-px screenshot's coordinates) or just `ui.click` it; `Escape` did not close it.
  Do not run `ui.backstage {"page":"close"}` — that closes the document.
- The live window takes keyboard focus: text typed/pasted at the desktop lands in the active cell (seen: a chat message
  arrived as `edit.paste` into A1). Read `engine.journal` to see where an unexpected edit came from, and re-read cells
  after a long gap.
- `file.saveAs` makes the live document point at that path and clears dirty; PDF export does not rename it. A table + chart
  sheet exported to 2 PDF pages (chart spills).
- `run --sample` layouts differ from a blank sheet (sample "sales" has a table at B4); `--print A1:H6` shows what you actually wrote.
- Writes to a file path need real paths; programmatic `file.open`/`file.save` without `path` fail ("never opens dialogs").
- `chart.set` prints nothing on success (no JSON line at all); check the chart with `info` or the saved chart XML rather than treating the silence as a failure.

## Verify

1. `gridcraft-cli check FILE.xlsx` — recalculates every formula against cached values and round-trips through the writer
   (exit 0 = agrees with itself; does **not** prove Excel opens it without repair).
2. `gridcraft-cli cat FILE --formulas` and `info FILE` to confirm cells, tables, charts.
3. `ui.screenshot` the live app after UI-affecting changes; for PDF use `qpdf --show-npages`.
4. Build in a scratch directory; never edit the only copy of someone's workbook — work on a copy with a new name.

## Limits to remember

No macros run; `.xls/.xlsb/.ods` import only (never written); slicers not saved to xlsx; charts shallow (no 3-D, axis
scaling); PDF export can't render Arabic/Devanagari/Thai. `app.quit` / `file.close {force:true}` discard unsaved work.
