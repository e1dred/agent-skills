# GridCraft reference: newer and changed commands

Part of the gridcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## New in 0.12.x (verified headless)


- `pivot.options {"enableShowDetails":true}` then `pivot.showDetails {"cell":"B5"}` → `{sheet:"Sheet3",records:1}`: writes the source records behind that value
  to a new sheet *before* the current one (error if show-details is off). `pivot.list {}` shows layout, grand totals, `enableShowDetails`.
- `formulas.pasteName {"list":true,"at":"J1"}` writes each defined name and its target (`TaxRate` / `=Sheet1!$H$1`) as two columns; `{"name":"TaxRate"}` starts `=TaxRate` in the active cell.
- `data.outlineSettings {"sheet","summaryBelow":false,"summaryRight":true}`, `view.showOutlineSymbols {"on":true}`, `view.statusBar {"sum":true,"average":true}` (returns all six flags),
  `automate.stopAction {}` → `{stopped:false}` when nothing is running.
- `run --quiet` suppresses command results: omit it when you need the returned values (it hid `pivot.showDetails`' answer).

## Newer commands

Seven newer commands (`pivot.options`, `pivot.showDetails`, `data.outlineSettings`, `formulas.pasteName`, `view.statusBar`,
`view.showOutlineSymbols`, `automate.stopAction`).

Newer window commands (headless `run` has one window; the live app can have several on one workbook):
- `window.list {}` → `[{window,doc,index,title,dirty,active,hidden}]`; `window.close {"window"?,"doc"?,"force"?}` → `{closed,document}` (a workbook closes with its last window; unsaved changes need `force`).
- `view.newWindow {}` now returns `{window,doc,title}` (titles `Book1:1`, `Book1:2`; saving from either saves the one workbook).
- `window.activate` takes `{"window":id}`, `{"doc":id}` or `{"index":n}`; `file.close {"document":true}` closes the workbook and all its windows (`{closed:false,dirty:true}` while it has unsaved changes, `force` discards).
- A saved `.xlsx` now writes `<scheme val="minor"/>` for the bold font entry too (cosmetic: values, formulas, tables, charts and PDF pages are unchanged).

## 0.15 changes (verified headless 2026-11-01)
- **`range.setValues` now reports conversions** → `{cells,convertedCount,converted:[{cell,input,stored}]}` (up to 20): typed input turned `"05.04.2026"` into `5/4/2026` (**May 4**: `=MONTH()` gave 5, en-US month-first), `"2.500"` into `2.5`, `"007"` into `7`, and listed `"TRUE"`, `"#N/A"`, `"12:30"` too; text, formulas and real numbers are not listed. Check `convertedCount` after writing someone else's data and rerun with `"parse":false` if any conversion is wrong.
- With `"parse":false` a leading `'` is now **kept as part of the text** (`'007` stored, `=LEN()` 4, `ISTEXT` TRUE): leave the apostrophe off if you only want text. An empty string `""` clears the cell (it emptied a cell that held "hello").
- `formulas.recentlyUsed {}` lists the functions most recently entered in formulas, newest first (`ROUND`, `SUM` after two `cell.set` formulas), followed by a default list; a fresh workbook now returns that default list (`SUM`, `AVERAGE`, `IF`, …) instead of `[]`.

## 0.16 changes (verified headless 2026-11-02; saved `.xlsx` XML checked)
- **Python cells:** `python.set {"cell":"G1","code":"1+1","output"?:"value|object"}` stores the code (in `xl/python.xml`), but **nothing runs Python here**: the cell shows `#BLOCKED!`, and `#VALUE!` after a save and reload. `cell.get` now has `python {code,output,preview,stale,typeName}`; `python.output {"cell"}` toggles `value` ↔ `object` (or set `mode`). Code and mode survive a round trip. Do not use Python cells for numbers you need: write Excel formulas.
- **`formulas.traceError {"cell"}`** → `{error,source,arrows,truncated}`: `E1 =1/0`, `E2 =E1*2`, `E3 =E2+1` traced from E3 gave `source` E1 and two `error` arrows (E1→E2, E2→E3). A cell without an error gives `error` and `source` null and no arrows.
- **Solver additions:** `reports` takes `sensitivity` (a Simplex LP run wrote "Answer Report 1" and "Sensitivity Report 1"). `data.solverSaveModel {"to":"J1"}` wrote J1:J6 (`=MIN($C$4)`, `=COUNT($B$2:$B$3)`, one `=AND($B$2>=1)` per constraint, then the options array spilling right); `data.solverReset {}` → `{removed:25,masked:false}` (the hidden names); `data.solverLoadModel {"from":"J1:J6"}` gave the same model back. **A constraint side must be a cell reference:** `"B2+B3 >= 8"` is refused ("not a reference"); put the sum in a cell and constrain that. Saved models also get `gridcraft_solver_evals` and `gridcraft_solver_stall` names (Excel has no such options).
- **Equations:** `insert.equation {"latex":"x^2+y^2=r^2","cell":"A8","size":14}` → `{equation:1}`; `equation.edit {"id":1,"latex":"a^2+b^2=c^2"}` replaced it. Saved as Office Math in the drawing (`a14:m`, `oMath`). `info` does not list equations. The object commands (move, delete, align, order) now take `kind:"slicer"|"equation"` too.
- **Chart data table:** `chart.addElement {"element":"dataTable","on":true,"dataTableKeys":true}` (or `chart.set {"dataTable":true,…}`) → `<c:dTable>` with keys and all borders on (column/bar/line/area charts).
- **`pageLayout.pageSetup {"pageOrder":"overThenDown"|"downThenOver"}`**; the result has a new `page_order` field (the only difference in the 0.15 → 0.16 re-run besides the file path in `check`). Paste Special's shortcut is now Ctrl+Alt+V.

## 0.16.1 changes (verified headless 2026-11-04)
- **`range.move {"to":"F2","overwrite":true}`** moves the selected range (B2:C5 → F2:G5, source emptied).
- **`selection.nextCorner`** moves the active cell to the next corner of the selection, keeping it (B2 → D2 → D5 → B5 → B2).
- **`view.showHorizontalScrollBar`, `view.showVerticalScrollBar`, `view.showSheetTabs`** take `on` (or toggle without it) and return the new state.
- **`edit.find` / `edit.replace` take `within:"selection"`** (replace changed 1 cell inside, 0 outside). Find matches the **displayed** text: a currency cell is found with "1,850", not "1850".
- Regression: all cell data identical to 0.16.0; saved `.xlsx` page margins are now written exactly (`0.7` instead of `0.699999988079071`), so a byte diff flags every sheet: compare values, not bytes.

## 0.17.0 changes (verified headless 2026-11-06)
- **Catalogue:** 385 commands (377 in 0.16.1): 8 added, none removed, 12 parameter specs changed.
- **Regression:** the shared 16-case harness gives the same cell data, formulas and charts on both versions; the only real output change is the new `opacity` field on `comment_list` rows (the `*.check.txt` diffs are the output path inside the file; the sample PDF's page 2 differs in a 1x2-pixel region).
- **Form controls (the 8 new ids):** `insert.button {"at":"E4","text":"Double","command":"range.setValues","params":{"range":"E1","values":[["x",20]]}}`, `insert.slider {"at":"C2","link":"$B$1","min":0,"max":100,"step":5,"value":40}`, `insert.spinButton {"at":"C6","link":"$B$3","min":0,"max":10,"step":1,"value":3}` → `{control:id}`. A slider or spin button writes its value into the linked cell at once (B1 read 40, B3 read 3).
- **Control commands:** `control.list {}` → `[{id,kind,name,at,link,value,min,max,step,page,horizontal,action?}]`. `control.setValue {"id":1,"value":55}` moved B1 40 → 55; `control.format {"id":1,"text":"Speed","min":0,"max":200}` returned min 0 / max 200 (a slider reports no `text`); `control.press {"id":1,"approve":true}` ran the button's command (F1 10 → 20); `control.assign {"id":1,"command":"range.setValues","params":{…}}` replaced the action and the next press wrote the new value (F1 20 → 99). Buttons survive save and reopen of the `.xlsx`; `check` reports a clean round trip.
- **Objects:** `object.move`, `object.delete`, `object.setAnchorMode` and `arrange.align`/`bringForward`/`sendBackward` take `kind:"control"` now (a control moved C2 → E10 through `object.move`). `arrange.*` on a control answered without error but changed nothing a read-back shows.
- **Charts:** `chart.set` takes `holeSize` and `firstSliceAngle` for doughnut/pie. `{"chart":1,"holeSize":65,"firstSliceAngle":30}` changed the saved `chart1.xml` from holeSize 75 / firstSliceAng 0 to 65 / 30. **`chart.set` prints nothing at all on success** — read `info` or the saved chart XML instead of waiting for a line.
- **Calculation and macros:** `formulas.calculationOptions {"precisionAsDisplayed":true}` is new and `file.options` reports it under `calculation`. `macro.run`, `macro.check` and `macro.debug` accept `output` (a cell for the macro's output); with a recorded macro that has no output anchor nothing appears there, and `macro.check` only echoes the path in its result.
- Other 0.17.0 changes a CLI user may notice: Find and Replace can be limited to `within:"selection"`; sheet tabs and scroll bars can be hidden; R1C1 reference style survives open/save; GROUPBY with total depth 2 or more adds subtotals; data validation and conditional formats anchor relative formulas on the top-left cell of every area.
