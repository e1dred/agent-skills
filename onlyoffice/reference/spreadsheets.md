# ONLYOFFICE reference: spreadsheets

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Spreadsheets (verified headless; `cell_*` tools)

Create with `create_document(format="xlsx")` (or `ooc.py new:xlsx calls.json`). Read `learn_about(topic="spreadsheets")`.
- `cell_set_cell_data {"cells":[{address,value|formula,style,numberFormat,copyTo}]}`: `style` is CSS-like
  (`font-weight:bold;background-color:#1F3864;color:#ffffff`); a `formula` seed + `copyTo:"D2:D4"` fills down with
  shifted references; the reply's `formulaChecks` shows the computed values (e.g. `=SUM(B2:C2)` → 270): read them.
- `cell_read_context` → table `regionAddress`, `headerRow`, `dataRowCount`, `nextCol`, per-column `type`
  (`formula` columns are flagged); use its header names for the tools below.
- `cell_set_sort {"range":"A1:D4","key1":"Total","sort_order1":"xlDescending"}` sorts by header name and keeps rows
  together (formulas followed their rows); a total row outside the range stayed put.
- `cell_add_data_bars {"range":"D2:D4"}`, `cell_layout {"action":"freeze"}` (header row → `frozenAt:"1:1"`),
  `cell_add_chart {"category_column":"Region","series_columns":["Q1","Q2"],"range":"A1:C4","chart_type":"bar","title":…}`
  (placed below the data; renders in `preview`; theme-less default colours).
- `cell_get_range_data {"range"}` returns `headers[]` + `rows[][]` (a blank cell is `null`).
- `preview` of a sheet prints the first page with chart and data bars (checked).

## Spreadsheets, more (verified headless)

- Conditional formatting tools (all applied, `cell_add_*`): `color_scale {"range","color_scale_type":3}`,
  `cell_value_condition {"range","operator":"xlGreater","value1":8,"fill_color":{"r","g","b"},"font_color":{…}}`,
  `top10_condition {"range","rank":3,"fill_color":{…}}`, `icon_set {"range","icon_set_type":"xl3Arrows"}`.
- `cell_set_multi_sort {"range":"A1:F25","key1":"Region","key2":"Revenue","sort_order2":"xlDescending"}` (header names).
- **`cell_insert_pivot_table {"range":"A1:F25","rows":["Region"],"columns":["Month"],"value_column":"Units","aggregation":"Sum",
  "output_sheet_name":"Pivot"}` creates the pivot on a NEW sheet inserted FIRST (index 0)**: the active sheet and the first
  `preview` page then show the pivot, so `cell_sheet {"action":"activate","name":…}` back to the data sheet if you go on.
  The pivot rendered with Sum of Units, row/column labels and grand totals.
- Data validation by macro (`ws.GetRange(…).GetValidation()`): `v.Delete(); v.Add('xlValidateList','xlValidAlertStop',
  'xlBetween','Bolts,Nuts,Gears'); v.SetInCellDropdown(true); v.SetShowError(true); v.SetErrorTitle(…); v.SetErrorMessage(…)`;
  whole-number limits `v.Add('xlValidateWholeNumber','xlValidAlertStop','xlBetween','0','100')`. Read back with
  `GetType()`/`GetFormula1()`. Cascading `INDIRECT` lists are NOT supported.
- Named range: `Api.AddDefName('Units','Sheet1!$D$2:$D$25',false)` then `=SUM(Units)` evaluated (735).
- Print setup per sheet: `ps=ws.GetPageSetup(); ps.SetOrientation('xlLandscape'); ps.SetPaperSize('xlPaperLetter');
  ps.SetFitToPagesWide(1); ps.SetFitToPagesTall(0); ps.SetPrintTitleRows('$1:$1'); ps.SetCenterFooter('Page &P of &N')`:
  the exported PDF's page for that sheet was Letter landscape with the footer, while the other sheet kept A4 portrait.
- `cell_layout {"action":"freeze","range":"A2"}` → `frozenAt:"1:1"`; `column_width {"range":"A:F","size":14}`.
