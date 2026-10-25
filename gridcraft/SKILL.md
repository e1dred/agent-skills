---
name: gridcraft
description: Verified working knowledge for driving the GridCraft spreadsheet app (storytold/gridcraft, an Excel-style editor that reads and writes .xlsx) from an AI agent: the headless gridcraft-cli (info, cat, eval, run, check, convert), the live control channel / MCP bridge to a running app, exact command parameter formats, traps and verification steps. Load before any GridCraft or spreadsheet task on this machine, and add what you learn at the end of it.
---

# GridCraft

Field notes from real tasks, tested on **gridcraft-cli 0.11.1** (Linux AppImage). GridCraft is an alpha, Excel-style
spreadsheet in Rust. Every ribbon button is an *engine command* (346 of them); the CLI, the MCP server and the app's
control channel all run the same commands. If `gridcraft-cli version` is newer, re-check before relying on this.

## Surfaces

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

## Verify

1. `gridcraft-cli check FILE.xlsx` — recalculates every formula against cached values and round-trips through the writer
   (exit 0 = agrees with itself; does **not** prove Excel opens it without repair).
2. `gridcraft-cli cat FILE --formulas` and `info FILE` to confirm cells, tables, charts.
3. `ui.screenshot` the live app after UI-affecting changes; for PDF use `qpdf --show-npages`.
4. Build in a scratch directory; never edit the only copy of someone's workbook — work on a copy with a new name.

## Limits to remember

No macros run; `.xls/.xlsb/.ods` import only (never written); slicers not saved to xlsx; charts shallow (no 3-D, axis
scaling); PDF export can't render Arabic/Devanagari/Thai. `app.quit` / `file.close {force:true}` discard unsaved work.

## Log

- 2026-10-25: first verified run on Linux (0.11.1): headless build/check/eval/info, live cell/table/chart/format/save/PDF,
  screenshots. Reference reading: artcraft-skills `gridcraft` (macOS, MIT) — see repo README credits.
