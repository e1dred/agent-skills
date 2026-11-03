# GridCraft reference: formatting and sheets

Part of the gridcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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
