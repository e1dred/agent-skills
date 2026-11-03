# GridCraft reference: recipes

Part of the gridcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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

## Macros and CSV values (0.14, verified headless 2026-10-31)
- **Macros live inside the workbook**: `macro.save` in one `run` and `macro.list` after reopening the saved `.xlsx` shows it; a fresh sample has none.
- `macro.save {"macro":{"name","description"?,"steps":[{"type":"command","id":"home.bold","params":{"range":"B4:G4"}}]}}` → `{name,steps}`; other step types in the help (`repeat`, `if`, `stop`) were not run. `macro.list`, `macro.get {"name"}` (the macro with `v`, `inputs`, `output`, `permissions`), `macro.rename {"name","to"}`, `macro.delete {"name"}`.
- `macro.check {"name"}` is a dry run that puts everything back → `{ok, conflicts, footprint:{sheets:[{sheet,bounds,changed,…}]}}`; `macro.run {"name","inputs"?:{Input:"B2:D9"}|"B2:D9"}` runs as one undo step (`{macro,ran,inputs}`).
- `macro.record {"name"?}` starts, `macro.record {"stop":true}` saves (`{saved,steps,dropped,skipped,inputs}`): the selection when recording started becomes the macro's `Input` (`A1` in headless), and running it applied the recorded `home.italic` relative to that input.
- `macro.debug {"action":"start|step|continue|runTo|stop|state","name"}`: `start` pauses before step 1 (`state:"paused"`, `current`), one `step` on a one-step macro ran it (`state:"finished"`, `changed:["Sales!B4:G4"]`) and a later `stop` then answered "No macro is being debugged". While paused, `macro.run` is refused ("Finish or stop the macro first").
- `file.exportCsv {"path","values":true}` writes raw values (full-precision numbers) instead of the displayed text; the same command without `values` is unchanged from 0.13.0.
