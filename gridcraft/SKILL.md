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

## More recipes (verified headless, 0.11.1)

Build with `run --script steps.jsonl --out f.xlsx` (one `{"command":…,"params":…}` per line), then `check` + `cat`.

- **Formula fill**: set the first cell with `cell.set`, then `edit.fillDown {"range":"E2:E7"}`. Do **not** use
  `range.fill {"range","input":"=C2*D2"}` for this: the relative formula is interpreted from the *active cell* (A1), so
  `E2` became `=G3*H3`. `range.setValues` with `=` strings is fine (references are literal).
- **Sort** with formulas in the data works and adjusts relative refs: `data.sort {"range":"A1:E7","header":true,"keys":[{"column":"E","order":"desc"}]}`.
- **Pivot**: `insert.pivotTable {"source":"Sales"|"Sheet1!$A$1:$E$7","destination":"new"|"Sheet1!H3","rows":["Region"],
  "columns":["Product"],"values":[{"field":"Revenue","func":"sum"}]}`; the new sheet is inserted *before* the current one and
  becomes active, so `cat`/`--print` then shows the pivot — pass `--sheet NAME`. Grand totals verified against SUMIFS.
- **Structured refs, names, spill** all calculate: `=SUMIFS(Sales[Revenue],Sales[Region],"North")*(1+TaxRate)`,
  `=SORT(UNIQUE(Sales[Region]))` (spills down), `formulas.defineName {"name":"TaxRate","refersTo":"=Sheet1!$H$1"}`.
- **Conditional format**: `home.conditionalFormat {"range","rule":{"type":"cellIs","operator":"greater","value":"50","preset":"lightRedFill"}}`
  or `{"type":"dataBar"}`; **validation**: `data.validation {"range","type":"list","formula1":"Widget,Gadget"}`.
- **Fill colour**: `home.formatCells {"range","style":{"fill":{"pattern":"Solid","fg":{"Rgb":14544887}}}}` — `Rgb` is an
  integer `0xRRGGBB` (alpha byte ignored), not a hex string. `Theme`/`Auto` are the other colour variants. Writes
  `fgColor rgb=…` to styles.xml.
- **Filter**: `data.filter {"range"}` turns AutoFilter on, then `data.filterBy {"column":"A","values":["East"]}`; `--print` still
  lists every row, so verify hiding via the live screenshot (not checked).
- **Charts**: `insert.chart` types incl. `pie`, `column` + `"subtype":"stacked"`, `"at":"J2"`; `home.insertSheet {"name":"Notes"}`;
  `freeze`: `view.freezeTopRow {}`. `info` lists each chart's kind and series count.
- **CSV**: `convert in.csv out.xlsx` and `data.fromTextCsv` both turn `007` into `7`. Keep text with
  `file.open {"path":"in.csv","csvAsText":true}` (verified: `007` kept). CSV/HTML export per sheet: `convert f.xlsx out.csv --sheet Sheet1`.
- `check` after a pivot/CF/validation/name workbook: all formulas matched, round trip equal.

## Everyday formatting and sheet editing (verified headless, 0.11.1)

Typical report build (checked: `check` clean, PDF 2 pages): header row styled, % and thousands formats, borders, merge, link,
sparkline, lookups, chart, protect.

| Goal | Command + params |
|---|---|
| fill / font colour | `home.fillColor {"range","color":"#DDEBF7"}`, `home.fontColor {"range","color":"#1F3864"}` (simpler than `home.formatCells`) |
| bold / size / wrap | `home.bold {"range","on":true}`, `home.fontSize {"range","size":12}`, `home.wrapText {"range","on":true}` |
| borders | `home.borders {"range":"A1:D5","preset":"all|outside|bottom|thickOutside|doubleBottom|…","style"?}` |
| merge | `home.mergeCenter {"range":"A7:D7"}` (`home.mergeAcross`); set the text after merging |
| number format | `home.numberFormat {"range","format":"Percentage|Currency|…"}` or `{"code":"#,##0"}` |
| widths / rows | `home.columnWidth {"cols":"A:D","chars":14}`, `home.insertRows {"rows":"3:5"}`, `home.deleteRows {"rows":"3:5"}` |
| find & replace | `edit.replace {"what":"Jan","with":"January","all":true,"within":"sheet|workbook"}` |
| copy / paste | `edit.copy {"range"}`, `edit.paste {"at":"C3"}`, `edit.pasteSpecial {"what":"values|formats|formulas…","operation"?,"transpose"?}` |
| series | `edit.fillSeries {"range","type":"linear|growth|date","step":1,"dateUnit":"month"}`; `edit.fillRight {"range"}` |
| dedupe / split | `data.removeDuplicates {"range","columns":["A"],"header":true}`, `data.textToColumns {"range","delimiters":[","]}` |
| hyperlink | `insert.link {"cell":"A9","target":"https://…|Sheet2!A1|mailto:…","text":"Site"}` |
| comment | `review.newComment {"cell":"B2","text":"…","author"?}` (writes threaded-comment parts; round-trips) |
| sparkline | `insert.sparkline {"range":"B2:B5","location":"F2","type":"line|column|winLoss"}` |
| page setup | `pageLayout.pageSetup {"orientation":"landscape","paper":"A4","margins"?}`, `pageLayout.printArea {"range":"A1:D5"}` — PDF export obeys them (print area gave 1 page) |
| protect | `review.protectSheet {}` (`password?`, permission flags) → `<sheetProtection sheet="1">`; `review.protectWorkbook` |
| lookups verified | `=XLOOKUP("Apr",A2:A5,B2:B5)`, `=IFERROR(VLOOKUP("Mar",A2:D5,2,FALSE),"n/a")`, `=TEXT(TODAY(),"yyyy-mm-dd")` (TODAY is flagged *volatile* in `check`, as expected) |

Notes: `cat` prints values as formatted (`1,200`, `33.33%`); add `--formulas` for formulas. Sparkline cells don't extend `info`'s used range.
New sheets and charts keep working after protection; protect last in the script.

## Version note (2026-10-25)

App 0.12.1 / CLI 0.12.1 added 7 commands (`pivot.options`, `pivot.showDetails`, `data.outlineSettings`, `formulas.pasteName`, `view.statusBar`,
`view.showOutlineSymbols`, `automate.stopAction`); none removed. The recipes in this file produced byte-identical cell output on 0.11.1 and 0.12.1.

## Log

- 2026-10-25: first verified run on Linux (0.11.1): headless build/check/eval/info, live cell/table/chart/format/save/PDF,
  screenshots. Reference reading: artcraft-skills `gridcraft` (macOS, MIT) — see repo README credits.
- 2026-10-25 (2): pivots, conditional formats, validation, names, structured refs, spill, sort, filter, charts, CSV import,
  fills verified headless; `range.fill` relative-formula trap found.
- 2026-10-25 (3): formatting, merge, borders, find/replace, hyperlink, comment, sparkline, lookups, page setup/print area, protection verified headless.
