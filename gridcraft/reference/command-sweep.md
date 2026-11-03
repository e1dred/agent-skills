# GridCraft reference: command sweep

Part of the gridcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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
