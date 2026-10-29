---
name: gridcraft
description: Use when building, editing, checking or converting spreadsheets (.xlsx, .csv), formulas, pivots or charts, when running gridcraft-cli, or when connecting to the GridCraft app (storytold) on this machine
---

# GridCraft

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, last tested on **gridcraft-cli 0.12.1** (Linux AppImage). GridCraft is an alpha, Excel-style
spreadsheet in Rust. Every ribbon button is an *engine command* (346 of them); the CLI, the MCP server and the app's
control channel all run the same commands. If `gridcraft-cli version` is newer, re-check before relying on this.

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

## More recipes (verified headless)


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

## Everyday formatting and sheet editing (verified headless)


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

## New in 0.12.x (verified headless)


- `pivot.options {"enableShowDetails":true}` then `pivot.showDetails {"cell":"B5"}` → `{sheet:"Sheet3",records:1}`: writes the source records behind that value
  to a new sheet *before* the current one (error if show-details is off). `pivot.list {}` shows layout, grand totals, `enableShowDetails`.
- `formulas.pasteName {"list":true,"at":"J1"}` writes each defined name and its target (`TaxRate` / `=Sheet1!$H$1`) as two columns; `{"name":"TaxRate"}` starts `=TaxRate` in the active cell.
- `data.outlineSettings {"sheet","summaryBelow":false,"summaryRight":true}`, `view.showOutlineSymbols {"on":true}`, `view.statusBar {"sum":true,"average":true}` (returns all six flags),
  `automate.stopAction {}` → `{stopped:false}` when nothing is running.
- `run --quiet` suppresses command results: omit it when you need the returned values (it hid `pivot.showDetails`' answer).

## Analysis and layout tools (verified headless)


Scripts are `run --script x.jsonl --out f.xlsx` (one `{"command":…,"params":…}` per line); `cat`/`info`/`check` on the output confirm.
- **Goal seek**: `data.goalSeek {"set":"D5","to":1000,"changing":"B2"}` → `{converged:true,iterations:2,value:168}` (writes the found value into `B2`; `set` must be a formula cell, `changing` a constant).
- **Scenarios**: `data.scenarioAdd {"name":"Boom","changing":"B2:B4","values":[200,80,50]}`, `data.scenarioShow {"name"}` (writes the values), `data.scenarioManager {}`, `data.scenarioSummary {}` (adds a "Scenario Summary" sheet). Scenarios are stored in a hidden name `_sc_scenarios`.
- **Data table** (what-if): `data.dataTable {"range":"G1:H6","columnInput":"D1"}` with the input values down `G2:G6` and the formula in `H1` → writes **static values** (a snapshot, not a live `TABLE()`); `rowInput` for values across the top; two-variable with the formula in the corner.
- **Solver**: `data.solver {"objective":"E1","goal":"max|min|value","variables":"D1","constraints":["D1 <= 9","D1 >= 0","B2 int","B3 bin"],"method":"grg|simplex|evolutionary"}` → "Solver converged to a locally optimal solution"; for `price*(100-10*price)` it found price 5 (250), matching the data table. `data.solverReport` makes the report sheets.
- **Forecast sheet**: `data.forecastSheet {"timeline":"A2:A13","values":"B2:B13","periods":4}` → new sheet with a table (actual, forecast, bounds) and a line chart; dates need a date number format (`home.numberFormat {"code":"yyyy-mm"}`).
- **Analysis ToolPak**: `data.analysisToolPak {"tool":"descriptive","range":"B1:B7","labels":true,"output":"E1","summary":true}`; `regression` uses **`inputY` and `inputX`** (not `range`): `{"tool":"regression","inputY":"B1:B7","inputX":"A1:A7","labels":true,"output":"E1"}` → the usual "SUMMARY OUTPUT" block (R² 0.998 on my test line); `correlation {"range":"A1:B7","labels":true}`. Others: anovaSingle, covariance, fTest, histogram, movingAverage, rankPercentile, tTest*.
- **Subtotals / outline**: `data.subtotal {"range":"A1:C5","groupBy":"A","function":"sum","columns":["C"]}` inserts "East Total … Grand Total" rows and the outline; `data.showLevels {"rows":1}` collapses to the totals; `data.group {"rows":"2:5"}`/`ungroup`, `data.outlineSettings {"summaryBelow":false}`.
- **Consolidate** (several sheets by labels): `data.consolidate {"sources":["Q1!A1:B3","Q2!A1:B3"],"destination":"A1","function":"sum","topRow":true,"leftColumn":true}` → Widget 17, Gadget 5, Gizmo 3.
- **Advanced filter**: `data.advancedFilter {"range":"A1:B4","criteria":"E1:F2","copyTo":"H1"}` where `E1:F2` holds the field names and a condition row (`"> 6"` under Qty; blank = any) → `{matched:1,range:"H1:I2"}`; without `copyTo` it hides rows in place.
- **Charts**: `chart.addElement {"element":"trendline","type":"linear|exponential|polynomial|movingAverage","displayEquation":true,"displayRSquared":true}`, `chart.set {"legend":"bottom","xTitle","yTitle","dataLabels":false,"width":480,"height":300}`; other elements: title, legend, dataLabels, gridlines, axisTitles, smooth.
- **Print**: `pageLayout.printTitles {"rows":"1:1"}`, `pageLayout.headerFooter {"header":"&CSales report","footer":"&CPage &P of &N"}`, `pageLayout.scaleToFit {"width":1,"height":0}`, `pageLayout.orientation {"orientation":"landscape"}`, `pageLayout.printGridlines`, `pageLayout.breaks {"insert":true,"cell":"A20"}`; PDF export obeys them (landscape Letter, header/footer text present).
- **Dynamic arrays and modern functions** all calculated and `check`ed: `=LET(n,SEQUENCE(5),SUM(n*n))` → 55, `=MAP(SEQUENCE(3),LAMBDA(x,x*10))` → 10,20,30 (spills), `=TEXTSPLIT(…)`, `=FILTER(…)`, `=XMATCH(…)`, `=TEXTJOIN(", ",TRUE,UPPER(LEFT(A2:A5,1)))`, `=SORTBY(A2:A5,RIGHT(A2:A5,3),-1)`. A spill that runs into occupied cells shows `#SPILL!` (and `check` reports a mismatch against the cached value).
- **JSON import**: `data.getData {"text":"[{\"id\":1,\"name\":\"Ann\"}]"}` (or `{"path"}`) → a new sheet with a table of the keys.
- **Flash Fill** (`edit.flashFill`, `data.flashFill`) answered "didn't see a pattern" for first-name extraction in every form I tried (ranges `B2:B5`, `B4:B5`, two examples): untested/unreliable headlessly, use a formula (`=LEFT(A2,FIND(" ",A2)-1)`) instead.

## Pivot tables and chart types in depth (verified headless; renders checked)

> the others exist in both but were not compared).

Test data was invented: a 24-row `Sales` table (Date, Region, Product, Units, Revenue). Scripts: `run --script x.jsonl --out f.xlsx`.
- **Pivot build:** `insert.pivotTable {"source":"Sales","destination":"new","name":"P1","rows":["Region"],"columns":["Product"],"values":[{"field":"Revenue","func":"sum"}]}` → `{anchor,id:2,name,range,sheet}`. The pivot gets the NEW sheet (inserted before the current one) and the pivot id is 2 (ids are not 1-based per pivot).
  Then, all verified with `cat --sheet`: `pivot.fields {"pivot"}` (source fields with `numeric/date/samples/areas`), `pivot.addField {"field":"Units","area":"values","func":"average","name":"Avg Units"}`,
  `pivot.calculatedField {"name":"Tax","formula":"=Revenue*0.2"}` (a "Sum of Tax" column appears; sums per cell), `pivot.valueSettings {"field":"Sum of Revenue","showAs":"percentOfGrandTotal","numberFormat":"0.0%"}` (16.7 %… 100.0 % grand total; `showAs` also percentOfColumnTotal/RowTotal, runningTotal, rank),
  `pivot.sort {"field":"Region","order":"desc"}`, `pivot.filter {"field":"Region","selected":["North","East"]}` (South dropped, totals recomputed), `pivot.layout {"layout":"tabular","style":"PivotStyleMedium9"}`, `pivot.list {}` (name, anchor, filters, calculatedFields, layout, grand-total flags).
  **Date grouping:** put it in the *layout* — `"rows":[{"field":"Date","group":"quarters"},"Region"]` gave Qtr1…Qtr4 rows; `pivot.group {"field":"Date","by":"months"}` only works if the field is already in rows or columns ("`Date` isn't in the rows or columns area").
  `pivot.collapse {"field":"Date","collapse":true}` → `{collapsed:["Qtr1",…]}` (hides the inner Region rows), `pivot.grandTotals {"mode":"off"}`, `pivot.refresh {}` → `{records:24}`, `insert.recommendedPivotTables {"source":"Sales"}` → suggestions with index/title/rows/columns/values (`apply:index` creates one).
- **Pivot reference trap:** `pivot` accepts a name, an id or a cell, but `insert.pivotChart {"pivot":"P1"}` failed with "P1 is not in a PivotTable" while `{"pivot":2}` worked (and `pivot.*` calls by name worked). Use the id for the chart. Result `{chart,pivot,series}` (the chart followed the 3-value/2-product layout: 6 series).
- **Chart types:** `insert.chart {"range":"A1:C6","type":…,"subtype":…,"title","at","width","height"}`; all of these produced a chart and rendered correctly in the PDF (one page, `pageLayout.scaleToFit` 1×1 + `file.exportPdf {"fitToPage":true}`):
  column (clustered/stacked/stacked100), bar, line (markers), area (stacked), pie, doughnut (give ONE series range `A1:B6`), scatter, radar, combo (column + line), histogram, waterfall, funnel, treemap, boxWhisker, bubble. **`stock` silently became a plain Line chart** with only two series (it needs open/high/low/close columns; not tested with four). `sunburst` not run. `insert.chartRecommendations {"range"}` → ranked `[{type,subtype,label}]`.
- **Chart editing** (target `"chart":id`, ids per workbook, the chart must be on the ACTIVE sheet): `chart.set {"legend":"top","xTitle","yTitle","dataLabels":true,"gridlines":false,"style":3,"width","height","dx"}`, `chart.addElement {"element":"trendline","series":0,"type":"linear","displayEquation":true}`,
  `chart.changeColors {"palette":"monochrome|colorful|accent1..6"}` (or `colors:[hex…]`), `chart.formatSelection {"series":1,"color":"#C00000"}`, `chart.quickLayout {"layout":3}`, `chart.changeType {"type":"line","subtype":"markers"}`, `chart.switchRowColumn`,
  `chart.selectData {"range":"Sheet1!A1:C6","categories":"Sheet1!A2:A6"}` (series count dropped 3 → 2), `chart.move {"sheet":"Dash","at":"B2"}` → the chart appears on that sheet; afterwards the *target sheet must be activated* (`sheet.activate {"sheet":1}`; param is `sheet`, index or name) before another `chart.*` call.
  Several of these return `null`/`{chart}` only: confirm with `info` (`chart LineMarkers "T" at B2, 2 series`).
- Not run: pivot slicers/timelines, `pivot.moveField/removeField/changeSource/style/subtotals/reportLayout` individually, `pivot.delete`, `chart.shapeFill/shapeOutline`, secondary axis, axis scaling (the Limits section says it is unsupported), live-window rendering of pivots.

## Conditional formats, validation, ToolPak, review and functions (verified headless; render checked)

> Data is invented.

- **Conditional formats** (`home.conditionalFormat {"range","rule":{…}}` → `{rules:N}` = running count on the sheet). Verified types and the PDF render (rules stack; later ones layer over earlier fills, a colour scale painted over a `cellIs` fill):
  `cellIs` (`operator` greater/between + `value`/`value2`), `beginsWith`/`containsText` (`text`), `blanks`, `duplicate`, `top10 {"rank":2}`, `aboveAverage`, `expression {"formula":"=$C2=\"B\""}` (formula relative to the range's top-left), `colorScale {"colors":[3 hex]}`, `dataBar {"color"}`, `iconSet {"set":"3TrafficLights1"}`.
  Looks: `preset` (`greenFill`, `yellowFill`, `lightRedFill`, `redText`, `redBorder`, …) or `style {"font":{"bold":true},"fill":"#FFE699"}` (a plain hex string works here, unlike `home.formatCells`). Icons did not show in the PDF export (unverified in the live window). `check`: clean round trip.
- **Validation:** `data.validation {"range","type":"whole|decimal|list|date|time|textLength|custom|any","operator","formula1","formula2","errorStyle":"stop|warning|information","errorTitle","errorMessage","inputTitle","inputMessage","dropdown","clear"}` (list: `"formula1":"Yes,No,Maybe"`; custom: `"=ISNUMBER(I2)"`).
  **Test it without a window:** `data.validate {"cell":"F2","input":"11"}` → `{ok:false,message,style:"Stop",title}` or `{ok:true}`; a `warning` style came back as `style:"Warning"`. `data.circleInvalid {}` → `{invalid:["F2"]}` lists cells that already break their rule (a value outside the validated range is of course not listed).
- **Analysis ToolPak, all remaining tools** (each ran; numbers sane): `anovaSingle {"range":"A1:C7","labels":true,"alpha":0.05}` (F 18.58, P 8.7e-5 on my data), `covariance`, `fTest {"range1","range2"}`, `histogram {"range","bins":"D2:D4"}` (→ Bin/Frequency/"More"), `movingAverage {"range","interval":3}` (first rows `#N/A`),
  `exponentialSmoothing {"damping":0.3}`, `rankPercentile` (Point/value/Rank/Percent), `tTestPaired|tTestEqual|tTestUnequal {"range1","range2","alpha","hypothesizedDifference"}` (full SUMMARY blocks incl. Pooled Variance, df, t Stat, one/two-tail P and critical values).
  **Trap:** with no `output` the report goes to a NEW sheet that becomes ACTIVE, so a following tool's `range` points at the empty new sheet ("Input range contains non-numeric data"). Give each an `output` cell on the data sheet (`"output":"A28"`; `overwrite:true` for non-empty cells) or `sheet.activate {"sheet":0}` between calls. Results are static values.
- **Comments and notes:** `review.newComment {"cell","text","author"}`, `review.replyComment {"cell","text","author"}`, `review.resolveComment {"cell"}`, `review.newNote {…}` (legacy note), `review.convertToComments {}` → `{converted:1}`. The saved xlsx has `comments1.xml`, `threadedComments/threadedComment1.xml` (a reply carries `parentId`, resolved = `done="1"`) and `persons/person.xml` (one person per author).
- **Protection:** `review.protectSheet {"password":"pw","insertRows":false,"sort":true,…}` then `cell.set` → "The cell or chart you're trying to change is on a protected sheet." (aborts a `run` script); `review.unprotectSheet {"password":"bad"}` → "The password you supplied is not correct."; the right password unprotects.
  `review.allowEditRanges {"action":"add","title":"Qty edit","range":"B2:B3"}` → `<protectedRange name sqref>` in the sheet xml; `{}` lists them. `review.workbookStatistics {}` → per-sheet and workbook counts; `review.checkAccessibility {}` → `[{issue:"Default sheet name",sheet}]`.
- **Functions** (513 exist; `functions --search X` shows signature and category; `eval '=…'` checks one): all of these returned the expected value: PMT 377.42, XNPV, IRR 0.1679, NPER, CUMIPMT, DB, PRICE (financial); STDEV.S, NORM.DIST, PERCENTILE.INC, CORREL, T.TEST, FORECAST.LINEAR (statistical);
  EDATE, NETWORKDAYS 23, WORKDAY, DATEDIF "m" 13, YEARFRAC (date); TEXT, SUBSTITUTE, TEXTBEFORE (2nd instance), REGEXEXTRACT, VALUETOTEXT (text); XLOOKUP, INDEX, MATCH, CHOOSECOLS, TAKE, VSTACK (lookup/array, arrays print tab-separated);
  BITAND, BASE, DEC2HEX, COMPLEX, IMABS, CONVERT mi→km 1.609344, MMULT, MDETERM, ROMAN, GCD, SUMPRODUCT, AGGREGATE (engineering/math). Array constants use `{1,2;3,4}` (comma = column, semicolon = row).
- Not run: shapes/images in cells, cell styles/themes, `.xls/.xlsb/.ods` imports on a real corpus, solver reports/methods in depth, Flash Fill.

## Cell styles, table design, slicers, objects, sheets, view and helper commands (verified headless; PDF render checked)

> Data invented. Step-by-step form used: `run --in f.xlsx --cmd 'id={json}' --out f.xlsx` (one command per run, so one failure does not lose the file; **selection, slicers and the clipboard do NOT survive between runs**: commands that need a selected table/slicer must share one `run`).

- **Cell styles** (render checked): `home.cellStyle {"range","name":"Heading 1|Good|Bad|Neutral|Title|Total|Accent1…|Normal"}` (Heading 1 = bold with a coloured bottom rule; Good green, Bad red; **Accent colours follow the theme**: after `pageLayout.theme {"name":"Ocean"}` + `pageLayout.themeColors {"name":"Ember"}` "Accent2" rendered orange), `home.newCellStyle {"name":"MyStyle","fromCell":"A1"}` → `{name}`.
  Themes: `pageLayout.theme {"name":"Craft|Slate|Meadow|Ember|Ocean|Orchid|Graphite","colors":[12 hex],"majorFont","minorFont"}`, `pageLayout.themeColors {"name"|"colors"}`, `themeFonts`, `themeEffects`.
- **Formatting helpers** (all ran; `on` omitted = toggle): `home.italic|underline|doubleUnderline|strikethrough|superscript|subscript|shrinkToFit {"range","on"}`, `home.fontName {"range","name":"Georgia"}`, `home.increaseFontSize|decreaseFontSize` (→ `{size}`), `home.alignLeft|alignCenter|alignRight|justify|alignTop|alignMiddle|alignBottom`, `home.orientation {"range","angle":45}`, `home.increaseIndent`,
  `home.accounting`/`percent`/`comma`/`increaseDecimal` (a value of 5 under `home.percent` showed 500%: the format multiplies), `home.mergeCells/unmergeCells`, `home.rowHeight {"rows":"1:1","height":30}`, `home.autofitRowHeight`, `home.hideRows|unhideRows {"rows"}`, `home.hideColumns|unhideColumns {"cols"}`, `home.lockCell {"range","on"}`, `home.insertColumns/deleteColumns {"cols"}`, `home.insertCells {"range","shift":"down"}`.
  Editing: `edit.clearFormats|clearContents|clearAll|clearComments|clearHyperlinks {"range"}`, `edit.fillUp|fillLeft {"range"}` (**`fillLeft` over A1:C1 overwrote B1/C1 with A1's text**), `edit.autoFill {"range","target":"A2:A10"}` (needs `target`), `edit.find {"what"}` (error "We couldn't find what you were looking for" when absent), `edit.goToSpecial {"what":"formulas"}` ("No cells were found"), `selection.currentRegion` → `{selection:"A1:C5"}`, `selection.stats` → `{count,sum,average,min,max}`.
  `insert.checkbox {"range":"E5:E6"}` + `cell.toggleCheckbox {"cell"}` (PDF shows TRUE/FALSE, no box), `insert.symbol {"char":"©"}` **appends to the active cell's text** (A1 became "Region©").
- **Table design** (needs a table; the name must not look like a cell reference: `"T1"` → "The name that you entered is not valid", `"SalesTbl"` fine): `table.totalRow {"on":true}`, `table.totalFunction {"column":"Sales","function":"average|sum|count|countNums|max|min|stdDev|var|none"}`, `table.bandedRows|bandedColumns|firstColumn|lastColumn|headerRow {"on"}`, `table.style {"style":"TableStyleMedium9"}`, `table.rename {"name"}`, `table.resize {"range":"A1:C5"}`, `table.convertToRange`, `table.removeDuplicates {"columns":[…]}` (needs column names present in the table; failed on a first try), `table.summarizePivot`.
- **Slicers:** `insert.slicer {"table"|"pivot","column":"Region","at":"F2"}` → `{slicer:2}` (also `table.insertSlicer {"column","at"}`); in the SAME run `slicer.toggle {"value":"N"}` (needs `value`; `multi:true` for several), `slicer.clear`/`selectAll` (both "Clear Slicer Filter"), `slicer.delete`. Across runs: "no slicer on this sheet" (slicers are not saved to xlsx).
- **Pivot remainder:** `pivot.moveField {"pivot","field":"Product","from":"columns","to":"rows"}`, `pivot.removeField {"field","area"}`, `pivot.subtotals {"mode":"none|top|bottom"}`, `pivot.reportLayout {"layout":"outline"}`, `pivot.style {"style":"PivotStyleMedium9"}`, `pivot.changeSource {"source":"Sheet1!$A$1:$C$5"}` → `{dropped:[],range}`, `data.refreshAll` → `{refreshed:1}`, `pivot.delete {}`.
- **Objects:** `insert.shape {"kind":"roundedRectangle","at":"H2","width":120,"height":50,"text","fill":"#FFD966","line":"#7F6000"}` → `{shape:1}` (renders as a filled rounded box with centred text), `insert.textBox {"at","text","width","height"}` → `{shape:id}`, `insert.picture {"path","at","width","alt"}` → `{image:1}`, `insert.icons {}` → `{shape}`;
  `shape.setText {"id","text"}` (**`id` must be a TEXT BOX id**), `arrange.bringForward|sendBackward {"id"}`, `object.move {"id","at"}` ("no such object" for a wrong id), `arrange.group`, `arrange.rotate {"degrees"}`, `object.delete {"id"}`.
- **Sheets, view, page:** `sheet.rename {"sheet":0,"name":"Data"}`, `sheet.tabColor {"sheet","color"}`, `sheet.move {"sheet":1,"to":0}`, `sheet.hide/unhide`, `sheet.next/previous`, `home.deleteSheet`; `view.freezePanes {"cell":"B2"}` → `{freeze:[1,1]}`, `view.zoom {"percent":120}` (**`percent`, not `value`**), `view.showZeros|gridlines|headings|formulaBar|ruler {"on"}`, `view.pageBreakPreview`/`view.normal` → `{view}`, `view.split`; `pageLayout.size {"name":"A4"}`, `pageLayout.margins {"preset":"narrow"}`, `pageLayout.printHeadings {"on":true}`, `pageLayout.background {"color"}`.
- **Formula helpers:** `formulas.evaluate {"formula":"=SUM(C2:C5)*2"}` → 780.0, `formulas.errorChecking {}` → `{circular:[],errors:[]}`, `formulas.showFormulas {"on"}`, `formulas.calculationOptions {"mode":"manual|automatic"}` → `{mode,iterative,maxIterations}`, `formulas.calculateNow` → `{cells}`, `formulas.createFromSelection {"range":"A1:C5","top":true}` → `{created:3}` (names from the header row; `formulas.nameManager` lists them with values),
  `formulas.autoSum {"range"}`, `formulas.tracePrecedents {"cell"}` → `[]`, `formulas.convertToNumber`, `formulas.functions {}` (the whole library with category and signature). Files: `file.properties {"title","author"}` (→ full block), `file.exportHtml {"path"}`, `file.exportCsv {"path"}` wrote **0 bytes** from a freshly started sheet in a step-run (use `convert f.xlsx out.csv --sheet Sheet1`), `history.list {"limit"}` → `{undo,redo}`.
- Not run: `.xls/.xlsb/.ods` import (no sample file; none of the tools here writes one), ink (`draw.*`), `automate.*` scripts, `data.queriesConnections`, printing, `review.spelling/thesaurus`, `view.customViews/newWindow`.

## Formula auditing, selection, scripts, ink, comments, grouping and print helpers (verified headless)

> Data invented. These ran in ONE `run` per script (selection, recording and object ids live only within a run).

- **Formula auditing:** `formulas.tracePrecedents {"cell":"D6"}` → `[{range:"D2:D5",sheet}]`, `formulas.traceDependents {"cell":"B2"}` → `[{cell:"D2"}]`, `formulas.selectPrecedents {"cell","all":true}` → `{active,selection:"D2:D5"}`, `selectDependents`, `formulas.removeArrows`,
  `formulas.evaluateFormula {"cell":"D2"}` → `{formula,result:7.5,steps:[{expression,value}…]}` (the Evaluate Formula steps), `formulas.watchWindow {"add":"Sheet1!D6"}` → `[{cell,formula,value}]`, `formulas.calculateSheet` → `{cells}`, `formulas.errorChecking` (earlier section), `formulas.recentlyUsed` → `[]` in a fresh workbook,
  `formulas.moreFunctions {"category":"Statistical|Engineering|Information|Database|Compatibility|Web|Cube"}` → `[{name,signature,description,category}]`, `formulas.insertFunction {"name":"VLOOKUP"}` (starts the formula in the active cell), `formulas.financial|logical|text|dateTime|lookupReference|mathTrig` (open a gallery in the UI), `formulas.deleteName {"name"}`, `formulas.useInFormula {"name"}`.
- **Selection and navigation:** `selection.set {"range":"A1:B2,D4"}` → `{active:"D4",selection}`, `selection.move {"dr":1,"dc":0,"extend","jump":true}` (Ctrl+arrow), `selection.next`, `selection.row` → `5:5`, `selection.column` → `A1:XFD1048576` (the column letters of the ACTIVE cell were not honoured: it selected from A), `edit.selectAll` (current region first: `A1:D6`), `edit.goTo {"reference":"C3"|"Sheet2!A1:C3"|name}`,
  `edit.cut {"range"}` → `{range,text}`, `edit.undo {"steps":2}` → `{undone:"Set Values"}` (**undo also undoes the data seeding**: only undo what you made), `edit.redo`, `edit.formatPainter` (first call picks up, `{"apply":"C3:D4"}` pastes), `edit.clearAll|clearContents|clearComments|clearHyperlinks|clearFormats|fillUp|fillLeft`, `selection.stats`.
- **Sorting and filters:** `data.sortAscending|sortDescending {"range","column":"B"}` → `{sorted}`, `data.clearFilter`, `data.reapply`; `data.group {"rows":"2:4"}`, `data.hideDetail|showDetail {"rows","level"}`, `data.ungroup {"rows"}`.
- **Automation scripts:** `automate.recordActions {}` … do things … `automate.recordActions {"stop":true,"name":"Bold header"}` → `{recording:false,saved,steps:1}`; `automate.newScript {"name","commands":[{"command","params"}]}`, `automate.allScripts` → `[{name,steps,trusted}]`, `automate.trustScripts {}` → `{trusted:true}`, `automate.runScript {"name"}` → `{ran:1}` (a script stored in an untrusted workbook is refused until trusted), `automate.deleteScript {"name"}`. Scripts are saved in the workbook.
- **Ink:** `draw.stroke {"points":[[10,10],[80,40],[120,10]],"color":"#C00000","width":2}` → `{shape:1}`, `draw.inkToShape {}` → `{kind:"Line"}` (a three-point stroke became a line), `draw.pen {"on":true,"color"}`, `draw.eraser {"on":true}`, `draw.lasso`.
- **Objects:** shapes, text boxes, pictures and charts **share one id counter** per workbook (a second chart got id 3 after two shapes; always use the id the insert returned): `arrange.align {"kind":"shape","ids":[1,2],"align":"left"}`, `arrange.sendBackward {"kind","id","toBack":true}`, `arrange.selectionPane {}` → `[{id,kind,name,at,anchorMode}]`, `object.setAnchorMode {"kind","id","mode":"moveOnly|moveAndSize|absolute"}`, `chart.delete {"chart":id}`, `chart.shapeOutline`.
- **Review and links:** `review.newNote` / `review.showNote {"cell"}` / `review.showAllNotes`, `review.nextComment|previousComment` → `{sheet,cell}`, `review.showComments {"on":true}`, `review.deleteComment {"cell"}`, `review.thesaurus {"word":"big"}` (only words that share the stem: "biga, bigam, bigamy…", not synonyms), `review.changeSpelling {"cell","word","to"}`, `review.addToDictionary {"word"}` (**writes the user's dictionary file: do not run as a test**); `link.open {"cell"}` → `{opened:"https://example.com"}` (http, https, mailto and in-workbook links only).
- **Rules and tables:** `home.manageRules {}` → `{rules:[{ranges,rule}]}` (`moveUp|moveDown|delete` take an index), `home.clearRules {"range"|"sheet":true}`, `home.formatAsTable {"range","style":"TableStyleMedium2","header":true}` → `{table:"Table1"}`, `data.fromTableRange {}` → copies the table to a new sheet "Sheet1 (2)" as a table (`{rows,cols,sheet}`), `table.headerRow|bandedColumns|firstColumn|lastColumn {"on"}`.
- **Formatting helpers:** `home.underline {"range","style":"double"}`, `home.superscript|subscript|strikethrough|shrinkToFit {"range","on"}`, `home.alignCenter|alignRight|justify|alignTop|alignMiddle|alignBottom`, `home.decreaseIndent`, `home.comma`, `home.increaseDecimal|decreaseDecimal`, `home.drawBorder {"range","edge":"bottom|top|left|right|grid","style":"thick","color"}`, `home.defaultWidth {"width":80}`, `home.deleteCells {"range","shift":"up|left|row|column"}`, `home.deleteColumns {"cols"}`, `sheet.moveColumns {"cols":"B:B","before":3}` (zero-based) → `{cols:"C:C"}`, `home.unhideRows|unhideColumns`.
- **Output:** `file.saveBytes {"format":"csv|xlsx|tsv|json|html"}` → `{base64,bytes,name}`, `file.printPreview {"page":1}` → `{pages,page:{paper,orientation,range,scale…}}`, `file.print {"fitToPage":true}` → `{pages,bytes,base64}` (the PDF as base64), `app.commands {"search":"sparkline"}` → ids, labels and parameter docs (a quick parameter lookup).
- Not run: `.xls/.xlsb/.ods` import, `window.activate`, `view.*` (live window), `pageLayout.themeFonts/themeEffects`, `slicer.selectAll` outside one run.

## Ink in GridCraft (verified headless; saved file read back)

> Compared with WordCraft ink (see that skill): there is no page index and no lasso/erase-by-point; each stroke is a drawing object on the sheet.

- `draw.stroke {"points":[[x,y],…],"color":"#C00000","width":2}` (sheet points) → `{shape:id}`: the stroke becomes a freeform shape immediately (saved as `a:custGeom` in `xl/drawings/drawing1.xml`). `draw.inkToShape {}` converts **the last stroke** (or `{"id"}`) to a clean shape and names its kind: a closed four-corner stroke → `{kind:"Rectangle"}`, a 24-point loop → `Ellipse`, a closed three-corner stroke → `Triangle`, a zig-zag open stroke → `Line` (it never refuses; WordCraft's `draw.convertInk` refuses non-shapes). Saved as `a:prstGeom prst="rect|ellipse|triangle|line"`.
- Converted shapes appear in `arrange.selectionPane` as ordinary shapes (`"Rectangle 1"`, `"Ellipse 2"`, anchored at the cell they start in, `anchorMode:"absolute"`), so `arrange.*`, `object.*` and `chart.shapeOutline` work on them. A highlighter-style wide yellow stroke (`width:10`) is just a thick stroke (no translucency flag).
- `draw.pen {"on","color","width"}`, `draw.eraser {"on"}` set the tool state for pointer drawing in the live window; `draw.lasso {}` takes no points (selects by dragging).

## Newer commands

Seven newer commands (`pivot.options`, `pivot.showDetails`, `data.outlineSettings`, `formulas.pasteName`, `view.statusBar`,
`view.showOutlineSymbols`, `automate.stopAction`).

## The last 58 command ids (2026-10-26, headless; smoke test)
> Each id ran with `gridcraft-cli run --sample sales --cmd 'id={json}'` (plus the setup it needs) and returned without an error; the saved workbook's `cat --formulas` and `info --json` were compared with the same script without the command. **Smoke test only: effects were not looked at.** Sample "sales" has its table at B4 (Region, Q1..Q4, Total).
- **Changed the workbook (58):**

```
data.scenarioDelete data.showDetail data.sortDescending edit.beginEdit edit.clearClipboard edit.clearComments
edit.clearContents edit.clearHyperlinks edit.fillLeft file.new file.options formulas.dateTime formulas.logical
formulas.lookupReference formulas.mathTrig formulas.selectDependents formulas.text home.addIns home.alignBottom
home.alignMiddle home.alignRight home.alignTop home.decreaseDecimal home.decreaseFontSize home.doubleUnderline
home.insertCopiedCells home.justify home.shrinkToFit home.strikethrough home.subscript home.unhideColumns
home.unmergeCells insert.recommendedCharts pageLayout.themeEffects pivot.fieldList review.previousComment
sheet.previous sheet.unhide table.bandedColumns table.firstColumn table.lastColumn view.arrangeAll view.formulaBar
view.freezeFirstColumn view.gridlines view.headings view.hideWindow view.macros view.newWindow view.pageLayout
view.rightToLeft view.ruler view.showObjects view.switchWindows view.unfreezePanes view.unhideWindow view.zoom100
view.zoomToSelection
```
- **Ran, workbook unchanged (0):** window, view and ribbon-state commands that return a value or only change the app (`view.*`, `formulas.dateTime|logical|lookupReference|mathTrig|text` (open the function library), `home.addIns`, `file.options`, `edit.beginEdit|clearClipboard`, `pivot.fieldList`, `review.previousComment`, `sheet.previous` ...), or commands whose effect is not stored in the file:

```

```
- **Setups that mattered:** `selection.set {"range":"C5"}` first for anything that needs "a cell in a table" (`table.firstColumn|lastColumn|bandedColumns {"on":true}` answered "select a cell in a table" without it); `home.insertSheet {"name":"Extra"}` then `sheet.hide {"sheet":"Extra"}` before `sheet.unhide {"sheet":"Extra"}`; `sheet.activate {"sheet":"Extra"}` before `sheet.previous`; `cell.set {"cell":"H1","input":"=C5"}` before `formulas.selectDependents {"cell":"C5","all":true}`; `data.scenarioAdd {"name":"S1","changing":"C5:C6"}` before `data.scenarioDelete {"name":"S1"}`; `insert.pivotTable {"rows":["Region"],"values":[{"field":"Q1","func":"sum"}]}` (with a cell of the table selected) before `data.showDetail {"rows":true}`; `edit.copy {"range":"A1:A2"}` + `selection.set {"range":"J3"}` before `home.insertCopiedCells {"at":"J3","shift":"down"}` (**it refused to shift cells that sit in a table: "it would shift cells in a table on your worksheet"**); `home.hideColumns {"cols":"B:C"}` before `home.unhideColumns {"cols":"B:C"}`; `home.mergeCells` before `home.unmergeCells`.
- Parameter shapes: `data.sortDescending {"range":"B5:G8","column":"C"}`, `home.strikethrough|subscript|shrinkToFit {"range","on":true}`, `home.decreaseDecimal|decreaseFontSize|doubleUnderline|justify|alignTop|alignMiddle|alignBottom|alignRight {"range"}`, `edit.fillLeft|clearContents|clearComments|clearHyperlinks {"range"}`, `view.formulaBar|gridlines|headings|rightToLeft|ruler|showObjects {"on":false}`, `view.zoomToSelection {"viewWidth","viewHeight"}`, `pageLayout.themeEffects {"name":"Subtle"}`, `insert.recommendedCharts {"range":"A1:C6"}`, `file.new {"sample":"budget"}`.

## Three-sheet financial model: names, lookups, sensitivity grid, cross-sheet chart (2026-10-27, 0.12.1 headless; PDF render looked at)
> Task: a three-sheet financial model from invented sample data, written as a JSON-lines script (`gridcraft-cli run --script build.jsonl --out model.xlsx`).
- **`run --script` with no `--in` starts a blank workbook** (`Sheet1`): `sheet.rename {"sheet":0,"name":"Summary"}`, `home.insertSheet {"name"}` for the others. One failing step saves NOTHING (it took four rebuilds to find the chart steps that failed), so run the whole script after every change and read the last line.
- Write cells on a sheet only after `sheet.activate {"sheet":"Name"}`. A forward reference to a sheet filled later gives `#N/A` in the step output; the saved workbook recalculates correctly (`check`: 177 formulas, 177 matched, round trip equal).
- **Defined names** (`formulas.defineName {"name":"Base_Rev","refersTo":"=Assumptions!$B$11"}`) work in formulas on other sheets, inside `SUMPRODUCT`, and **inside a conditional-format expression** (`"formula":"=AND(ISNUMBER($J4),$J4>Alert_Threshold)"`, rendered: the September burn cell turned red). `XLOOKUP(Base_Month,range,range)` and `INDEX/MATCH` on a date column both returned the right base values.
- **Two-variable sensitivity without a data table:** `=SUMPRODUCT(Base_Rev*(1+Rev_Growth+B$18)^SEQUENCE(12))-SUMPRODUCT(Base_Opex*(1+$A19)^(SEQUENCE(12)/12)*(1+HC_Growth)^SEQUENCE(12))` is live (changing an assumption moved the grid) and `check`ed. A reconciliation cell (grid formula at the current inputs minus the forecast total, rounded) read 0.00 before and after changing two inputs. `data.dataTable` only writes static values, so prefer this.
- **Charts from another sheet:** `insert.chart {"range":"Detailed_Forecast!A1:A16,…"}` fails ("no sheet named `Detailed_Forecast!A1:A16,Detailed_Forecast`"). Build the chart on the data sheet, then `chart.move {"chart":1,"sheet":"Summary","at":"H4"}`. A multi-area range needs a TEXT category column first: a date column or a formula-date column fails with "multi-area charts require a text category column followed by equal-height series columns". Workaround that worked: chart only the series (`D1:E16`), then `chart.selectData {"range":"Detailed_Forecast!D1:E16","categories":"Detailed_Forecast!L2:L16"}` with `L` = `=TEXT(A2,"mmm yy")`.
- Number format codes with signs and colour work: `$#,##0;[Red]-$#,##0`, `+0.0%;-0.0%;0.0%`, `mmm yyyy`. `data.validation` `decimal between -1 and 1` on the input cells wrote cleanly (`data.validate` was not checked on that sheet).
- `gridcraft-cli convert x.xlsx x.pdf` prints only the ACTIVE sheet (3 pages for a wide Summary). For every sheet: `run --in x.xlsx --cmd 'pageLayout.orientation={"orientation":"landscape"}' --cmd 'pageLayout.scaleToFit={"width":1,"height":0}' --cmd 'file.exportPdf={"path":"all.pdf","sheets":"all","fitToPage":true}'` (the run then complains `--out` is missing; the PDF is already written).
- Modelling note for the spec: with OpEx above revenue every Q3 month, the base-case 12-month profit is -$12,278 and the grid straddles zero; only the September burn (18.6 % over the 3-month average) trips the 15 % alert. Burn is negative (a surplus) from May 2027, so the variance column is left blank when burn <= 0.

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
