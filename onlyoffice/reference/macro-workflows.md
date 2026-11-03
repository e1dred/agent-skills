# ONLYOFFICE reference: macro workflows

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Conditional formats, filter, pivot, slide tools (verified via `tools/ooc.py`, 2026-10-25)

The MCP link dropped twice in a row right after the first call; `python3 -I tools/ooc.py new:xlsx calls.json` ran a whole
11-call test in one session (calls.json ends with `save_document`, which printed the saved path; the helper then detaches).

**Spreadsheet** (all succeeded; save → `info` shows the pivot sheet, chart and filter; the xlsx has pivotTable/pivotCache/chart parts):
- `cell_add_cell_value_condition {"range","operator":"xlGreater","value1":50,"fill_color":{"r":255,"g":199,"b":206},"font_color":{r,g,b}}` —
  colours are `{r,g,b}` objects, **not hex**. Also `xlBetween` with `value2`.
- `cell_add_color_scale {"range","color_scale_type":2|3}`, `cell_add_data_bars {"range","bar_color":{r,g,b},"show_value"}`,
  `cell_add_icon_set {"range","icon_set_type":"xl3TrafficLights1|xl3Arrows|…"}`, `cell_add_top10_condition {"range","rank":2,"is_bottom","is_percent"}`.
- `cell_set_auto_filter {"range":"A1:D7","field_name":"Region","criteria1_array":["East"],"operator":"xlFilterValues"}` (also `criteria1":">18"`,
  `xlTop10Items`, colour filters); `field:0` only shows the dropdowns. Read the column first with `cell_get_range_data`.
- `cell_insert_pivot_table {"value_column":"Revenue","rows":["Region"],"columns":["Product"],"aggregation":"Sum","range":"A1:D7","output_sheet_name":"Pivot"}`
  — header names must be exact (take them from `cell_read_context`); lands on a new sheet (e.g. `A3:D8`).
- `cell_add_chart {"category_column":"Region","series_columns":["Revenue"],"range":"A1:D7","chart_type":"bar|lineNormal|pie|…","title","sheet"}` — placed *below the data*.
- `cell_get_sheet_objects {}` lists charts, pivots, tables, CF rules, comments, hyperlinks per sheet — use it to confirm.
- GridCraft's `check` reports the ONLYOFFICE-written workbook as "round trip differs: package" and skips the x14 CF
  extensions (data bars / icon sets): a GridCraft limit, not a broken file.

**Presentation** (a new deck has one empty *Title Slide* with Title 1 + Subtitle 2):
- `slide_get_presentation_context {"detail":"overview|current|theme|full|audit"}` (`"all"` is invalid); `audit` lists `empty_placeholder`/`single_slide` issues with a fix.
- `slide_set_text {"text","target":"title"|"notes"|<shape name>,"slide_number"}` — `target:"notes"` sets speaker notes (survived export: DeckCraft `info` reads them).
- `slide_add_chart_to_slide {"chart_type":"bar","slide_number":1,"categories":["Q1","Q2","Q3"],"series":["Sales"],"data":[[10,14,19]]}` — `data` is a 2-D array,
  one row per series, and is **required** (or a `prompt`); without it: "give either 'data' … or 'prompt'". It is centered on the slide and
  covers any empty body area; the chart named after the series, white card background.
- `slide_change_slide_background {"background_type":"solid","color":"#F4F6F8"|"gradient","gradient_colors":["#1F3864","#2E75B6"],"gradient_angle":90,"slide_number"|"apply_to_all":true}`;
  `"generate"`/image are AI tasks. A dark gradient hides the default black title text — set a light title colour (macro) or check by rendering.
- `slide_arrange {"action":"move"|"duplicate","slide_number","position"}`, `slide_delete {"slide_number","count"}` or `{"slide_number","shape_index"}`
  for one object, `slide_set_object {"slide_number","shape_index","x_mm","y_mm","width_mm","height_mm"}` (1-based; sizes in mm).
- `slide_write_macro {"code":"…return …"}` still the fallback (e.g. `Api.GetPresentation().GetSlidesCount()` → 1).

## Next-tier workflows through macros (verified headless via `tools/ooc.py`, 2026-10-25)

**Find the right call yourself:** `get_api_reference {"topic":"…"}` has short, accurate pages (topics seen: `defined_names`, `protection`, `charts`, `hyperlinks`, `transitions`, `animations`, `masters`, `themes`, `tables`, `gotchas`, `validation`, `comments`, `pivots`, `cond_format`, plus the older `patterns, units, colors, headers-footers, images, forms, document, macro`),
or `get_api_reference {"class_name":"ApiParagraph"}` for a class's real methods. A macro error says so and warns that **the engine has no undo**: everything before the error is still in the document, so retries must be idempotent. Introspecting an object's methods inside a macro works for Word/cell objects, but slide objects return obfuscated names, so use the reference.

**Word**
- Track changes: `doc.SetTrackRevisions(true)` then edit through the API; `range.Delete()` made a tracked `<w:del>`; **`range.AddText('x')` appends AFTER the found range instead of replacing it** (`quick brown` + `slow red` → "quick brownslow red"). `doc.AcceptAllRevisionChanges()`/`RejectAllRevisionChanges()`, `doc.IsTrackRevisions()`.
- Comments: `range.AddComment('text','Author')` (a `commentRangeStart` appears; `doc.GetAllComments()`); the `word_comment_text` tool does the same by search. Watermark: `doc.InsertWatermark('DRAFT')` (also Get/Set/RemoveWatermarkSettings).
- Content controls and forms: `doc.GetAllContentControls()`, `GetFormsData/SetFormsData`, `AddCheckBoxContentControl`/`AddComboBoxContentControl` exist; the `form_*` tools are the easier route.
- **Password-protected files**: `save_document {"path","format":"docx","password":"…"}` writes a real Office-encrypted file (`CDFV2 Encrypted`; the reply says "it asks for that password when it is opened"); reopen with `open_document {"path","password":"…"}`. Keep an unprotected copy while you still have work to do. To remove a password, open with it and save again without `password`.

**Spreadsheet** (macro tool `cell_write_macro {"code","images":{}}`)
- Defined names: `Api.AddDefName('SalesData','Sheet1!$B$2:$B$5')` returns a boolean (read back with `Api.GetDefName`, which throws if missing; `Api.GetDefNames()` is the safe existence check).
- Protected ranges (this is the sheet-protection API): `var pr = ws.AddProtectedRange('Locked','Sheet1!$A$1:$C$5'); pr.SetAnyoneType('CanEdit|CanView|NotView'); pr.AddUser(id,name,'CanEdit')`; there is no `Delete()` on a protected range.
- Hyperlinks: `ws.SetHyperlink('E1','https://example.com','','tip','Docs')` (worksheet method; there is no `range.SetHyperlink`; internal link: address `''`, subAddress `'Sheet2!A1'`) → `<hyperlink ref="E1">`.
- Charts: after `cell_add_chart`, `ws.GetAllCharts()[0]` offers `SetTitle`, `SetHorAxisTitle/SetVerAxisTitle(title,sizeHps,bold)`, `SetLegendPos('bottom')`, `SetShowDataLabels(ser,cat,val,pct)`, `SetMajorHorizontalGridlines(stroke|null)`, tick marks and label font sizes. Font sizes are half-points.

**Presentation** (macro tool `slide_write_macro`)
- **Transitions**: `var t = slide.GetSlideShowTransition(); t.SetEntryEffect('effectPushLeft'); t.SetDuration(700); t.SetAdvanceOnClick(false); t.SetAdvanceOnTime(true); t.SetAdvanceTime(4000)` → `<p:transition advClick="0" advTm="4000"><p:push dir="l">` (effect names: effectFade, effectPush*/effectWipe*… ; `effectNone` removes it).
- **Animations**: `var seq = slide.GetTimeLine().GetMainSequence(); var e = seq.AddEffect(shape, 'fade', 'onclick')` (second effect `'spin','afterprevious'`); triggers are lowercase `onclick|withprevious|afterprevious`; effect names are kebab or camel (`fade`, `fly-in`, `spin`, `entranceFade`, `emphasisSpin`, `path-circle`…). `AddEffect` returns **null without an error** for an unknown name (my first try with `'entrFade'`/`'clickEffect'` returned null and count 0). `e.SetDuration(800)`, `GetEffectType()`, `seq.GetCount()`. DeckCraft reads the saved file back with `animations:2` (entrance fade, emphasis spin).
- Theme: `slide.GetTheme().GetColorScheme().ChangeColor(0, Api.Color(228,87,46))` (positions 0–5 accent1–6, 6 dk1, 7 dk2, 8 folHlink, 9 hlink, 10 lt1, 11 lt2); `pres.GetMaster(0).GetLayoutsCount()` → 11; `slide.ApplyLayout(layout)`, `pres.ApplyTheme`.
