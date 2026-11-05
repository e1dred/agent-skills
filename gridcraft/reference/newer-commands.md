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
