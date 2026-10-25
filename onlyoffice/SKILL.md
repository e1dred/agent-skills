---
name: onlyoffice
description: Verified working knowledge for driving ONLYOFFICE Desktop Editors from an AI agent through its built-in AI-tools MCP server (onlyoffice-document-builder) — enabling it, connecting from outside the app (Linux flatpak), LIVE editing of documents open in the editor, headless editing/preview, Word macro API details that work, recipes and traps. Load before any ONLYOFFICE task, and add what you learn at the end of it.
---

# ONLYOFFICE Desktop Editors

Field notes from real tasks, tested on **ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, Linux)** with the
AI-tools server **onlyoffice-document-builder 2.0.0-native**. Re-check anything below on other versions.

## Keep this file growing

At the end of every ONLYOFFICE task: add verified commands, API details, recipes and traps to the matching
section; fix anything that proved wrong; mark guesses as unverified; keep it general (no personal data or
machine-specific paths — this file is meant to be shared); add a dated log line.

## How the connector works

- **Enable it:** Settings → *Enable AI features* (stored as `<disable-ai>0</disable-ai>` in
  `…/desktopeditors/data/settings.xml`). The app then installs an add-on at
  `…/data/addon/desktop-sdk-plugins/aitools-bridge/` containing `docbuilder-tools` (an MCP server on stdio,
  ~93 tools for word/cell/slide/pdf/forms), `libaitools-bridge.so`, and agent docs (`resources/docs/*.md`,
  `instructions.json`, `skills/`). Read `resources/docs/overview.md` — it is the vendor's own agent guide.
- **Live link:** at startup the app launches its own `docbuilder-tools`, listens on a random localhost port,
  and writes a discovery file `…/data/cache/work_temp/onlyoffice-ai-tools.json` (`{pid, port, protocol, token}`,
  mode 0600; port and token change every launch).
- **Connecting from outside:** a second `docbuilder-tools` started with `AI_TOOLS_DISCOVERY=<that file>` reaches
  the running editor. It needs the app's libraries, so on the flatpak run it inside the sandbox:
  `tools/onlyoffice-ai-mcp` does exactly that (paths for the Flathub flatpak; adjust `D=` for other installs).
  Register: `claude mcp add onlyoffice -- /path/to/onlyoffice-ai-mcp`.
  Without the app running, the same server still works headless on files.
- The flatpak needs **network permission** (`shared=network`) for the localhost link. Forks without it (e.g. the
  Euro-Office flatpak, which also never installed the add-on) don't get a working connector.
- Start the app from the desktop menu, not from an agent's shell: a child process inherits the shell's
  environment, including any session tokens. The wrapper strips the one Claude Code sets.
- **No MCP tools in the session** (or the session's MCP link dropped — seen once mid-task): `tools/ooc.py`
  runs calls through the wrapper directly: `python3 -I tools/ooc.py "/abs/Doc.docx" calls.json`.

## Live vs headless (verified)

- `list_editor_documents` → paths open in the editor plus `modified` flags, and a count of
  `unsaved_new_documents`. A never-saved document has no path and **cannot be attached** — ask the user to
  Save As first.
- `open_document(path)` with a path that is open in the editor **attaches live**: every edit appears in the
  user's window at once; `get_document_info` says `mode: "live"`.
  - `save_document` is refused (only the user saves); `close_document` only detaches.
  - `preview` is refused live, and `get_api_reference(class_name=…)` introspection fails
    ("Could not create an instance") — use the topic guides instead.
  - The attached file on disk keeps the old version until the user saves: tell them about Save As vs Save.
- `open_document(path)` on a file NOT open in the editor works **headless**: `save_document(path, overwrite=true)`
  and `preview(pages=…, format="png", path=…)` both work. Use this to check a layout visually — e.g. run the
  same macros on a copy and render it.
- Each `ooc.py` run re-attaches; in headless mode, save before the run ends or the edits are lost.

## Word macro API notes (`word_write_macro`, verified)

Read `get_api_reference(topic=…)` first: topics `styles`, `lists`, `paragraphs`, `search`, `sections`,
`patterns`, `units`, `tables`, `runs`, `colors`, `headers-footers`, `images`, `forms`, `document`, `macro`.
- **Units:** font size in half-points (`SetFontSize(21)` = 10.5 pt); spacing, indents, tabs, page size and
  margins in twips (20/pt, 1440/in; Letter = 12240×15840); border width in 1/8 pt.
- Live macros run in strict mode: declare every variable; return only JSON-simple values.
- Styles: `doc.GetStyle("Normal")`, `doc.CreateStyle(name, "paragraph")` + `SetBasedOn(doc.GetStyle("Normal"))`;
  edit via `style.GetTextPr()` (`SetFontFamily`, `SetFontSize`, `SetBold`, `SetCaps`, `SetColor(Api.Color("#1F3864"))`,
  `SetItalic`, `SetSpacing`) and `style.GetParaPr()` (`SetSpacingBefore/After`, `SetSpacingLine(240,"auto")`,
  `SetKeepNext`, `SetJc`, `SetIndLeft`, `SetIndFirstLine`, `SetTabs([twips],["right"])`, `SetBottomBorder`).
  Restyling built-in "Heading 1" keeps real headings for ATS/outline.
- `SetBottomBorder("single", 6, 1, color)`: the recipe tries an `ApiColor` first and falls back to r,g,b
  arguments; the border rendered, but which form this version accepted is unverified.
- Page: `doc.GetSections()[0].SetPageSize(w,h)` / `.SetPageMargins(left, top, right, bottom)`.
- Paragraphs: `Api.CreateParagraph()`, `p.SetStyle(name)`, runs via `Api.CreateRun()` + `r.AddText()`,
  `r.SetBold(true)`, `r.AddTabStop()` for a tab character, `p.AddElement(r)`, `doc.Push(p)`.
- Bullets: `doc.CreateNumbering("bullet").GetLevel(0)`; `SetTemplateType("bullet","•")`, `GetTextPr().SetColor(…)`,
  `GetParaPr().SetIndLeft/SetIndFirstLine`, `SetSuff("tab")`; `p.SetNumbering(level)`. Objects don't persist
  between macro calls — in a later call, reuse the level from an existing list paragraph (`p.GetNumbering()`).
- Links: `doc.Search(text, true)[0].AddHyperlink(url, tip)` keeps the visible text (mailto: and https: verified).
- Read back: `p.ToHtml({RenderHTMLTags: true})` (shows `<strong>`, `<a href>`), `p.GetNumbering()`,
  `doc.GetStatistics()` → `{PageCount, WordsCount, ParagraphCount, …}` (works live).

## Live editing of all four editors (verified on open documents)

`list_editor_documents` first (it also names which folder each PDF/doc really lives in), then attach with the exact path.
The same tools as headless work live, and the user sees the edits at once:
- **Word:** `word_insert_paragraphs`, `word_add_table`, `word_page_setup` (footer + page numbers), `word_write_macro`
  (`GetStatistics()` → words/pages) all applied live; the new-document empty first paragraph is not there on an
  existing blank file's content, expect it anyway when counting elements.
- **Spreadsheet:** `cell_set_cell_data` with a `copyTo` formula and `numberFormat`, `cell_add_chart`, `cell_get_range_data`
  all worked live; `formulaChecks` still returns the computed values (10 and 8 for `=B2*C2`).
- **Presentation:** the slide macro that adds a slide, `slide_set_text` (title/subtitle/notes) and
  `slide_add_chart_to_slide` worked live; a blank saved deck starts with one title slide and `currentSlideIndex` follows
  the last edit.
- **PDF:** `pdf_get_page_info`, `pdf_get_all_pages_info`, `pdf_search_document` (reports `total` and `truncated` when
  `max_results` cuts it off) and `pdf_get_text_quads` worked live. **`pdf_get_document_info` failed live** with
  "returned a malformed reply: null": use `pdf_get_page_info` instead. Markup on a live PDF was not tried (it
  would change the user's file in the editor).
- **Filling an existing PDF form live (81-field government form, fake values):** `pdf_get_page_info
  {"page_number":1,"include_forms":true}` returns `forms[]` with `name`, `type` (`textField|checkboxField|…`), `value`
  (`''` or `Off` when empty), `tooltip`, `isRequired`, `isReadOnly`, `charLimit`, `options` and a long `nearbyText`.
  That listing is huge (every field repeats ~300 characters of surrounding text): save the output to a file and
  filter it in Python instead of printing it. Then `pdf_fill_form_fields {"fields":[{"name":"Patient Name",
  "value":"Test Patient"},{"name":"Check Box3","value":"Yes"}]}` → `successCount`/`failed`; re-read with
  `include_forms` to confirm (`Check Box3 = 'Yes'`, untouched boxes stay `Off`). Field `name`s can be unhelpful
  (`Text37`, `Check Box12`): use `tooltip` and `nearbyText` to pick the right one, and ask the user for real values.
  Unlike `form_fill` (documents you build, a LIST of `{key,value}`), this tool takes `{name,value}`; a checkbox's
  on-value is its `options[].export` (here `Yes`); an empty string unchecks.
- **Adding content to a live PDF (`pdf_write_macro`; confirmed on a screenshot of the editor window):** existing page
  text cannot be edited, only read, marked up, redacted or covered; new content is added with `page.AddObject(…)`
  (page index 0-based; read `get_api_reference(editor="pdf", topic=…)`: `macro`, `shapes_text`, `stamps`, `markup`,
  `redact`, `drawings`). Verified:
  - Text box: `Api.CreateShape('rect', Api.PointsToEmus(w), Api.PointsToEmus(h), fill, stroke)`, `s.SetPosition(
    Api.PointsToEmus(x), Api.PointsToEmus(y))`, text via `s.GetContent().GetElement(0).AddElement(run)`. Rendered with
    the fill and border. **`run.SetFontSize(14)` gave 7 pt text** (half-points: use 28 for 14 pt).
  - Stamp: `Api.CreateStampAnnot([x1,y1,x2,y2],'SB_Draft')` → an orange "DRAFT" stamp (rect in points, top-left origin).
  - Highlight: `page.Search({text})` returns matches in document order, NOT reading order: the first match for a
    form title was its footer copy at the bottom of the page, so check which match you mark. `Api.CreateHighlightAnnot(
    quads)` drew a red-filled box; set the colour (`SetFillColor`/`SetColor` per `annotations`) if you want yellow.
  - Live PDFs cannot be previewed from the agent: ask the user for a screenshot (the Read tool can view it).
- `save_document` and `preview` are refused live ("NOTHING WAS SAVED … only the user can save it"): tell the user to
  Ctrl+S, and remind them that test edits sit unsaved in their window (close without saving to discard).
- Test files: ask the user to Save As blank files (docx/xlsx/pptx/pdf) first; a never-saved document cannot be attached.

## Résumés: editing real ones safely (verified on copies; originals untouched)

- **Never edit the user's file:** `cp` it into the scratchpad, work headless on the copy, `save_document` under a NEW
  name. Résumé folders may hold other people's files: leave those alone.
- **Two designs exist; check which first** with a macro that returns counts only (no text): `d.GetElementsCount()`,
  per-element `GetClassType()` (`'table'|'paragraph'`), style names via `p.GetStyle().GetName()`, page/word counts from
  `d.GetStatistics()`. A *style-based* résumé (styles like Heading 1, Job Title, Bullet; no tables) is easy to restyle.
  A *table-based* one (a 1-row, 2-cell table per job: employer/title left, dates right; bullets as List Paragraph)
  needs table-aware edits and its date cell is narrow, so a longer date wraps onto a second line.
- **Add a bullet that matches the others:** `var cp=d.GetElement(i).Copy(); … d.AddElement(i+1, cp);` where `i` is the last
  bullet paragraph (verified: numbering, font and indent are kept). In a clone, bullets can hold the leading tab in a
  SEPARATE run: replace only the text run (`r.ClearContent(); r.AddText(newText)` on the first run whose text has
  letters, clear the later runs) and do NOT put `\t` in the new text (that gave a double indent).
- **Tracked changes:** `d.SetTrackRevisions(true)` then `word_search_replace` (e.g. a date) is tracked (red strike +
  underlined new text in the PDF render). **`d.AddElement` of a whole paragraph is NOT tracked**: flag it for review with
  `para.AddComment('New bullet proposed for review','Claude')` (comment count read back as 1) or highlight it.
  Turn tracking off again before saving if the user wants clean text.
- ATS check: `pdftotext -layout` on the exported PDF keeps one line per job ("Employer … dates") even for the
  table-based layout, so reading order was fine.
- Page count after edits: `d.GetStatistics().PageCount` (3 pages stayed 3 after one extra bullet).

## Forms, all field types (verified headless: build, fill, save as form, reopen)

- `form_add_field` types: `text` (also `multiline:true`, `max_chars:200` → `charLimit`), `dropdown` (`items`, reported
  back as `comboBoxForm` with an extra "Choose an item" first entry), `combobox` (`items`), `checkbox`, `radio`
  (one `key` for the group, a different `choice_name` per option: add one call per option), `date` (`date_format`).
- `form_fill {"fields":[{"key","value"},…]}`: text/multiline/date as strings ("10/24/2026"), dropdown by item text,
  checkbox "yes"/"true", **radio by the choice name** on the group key (`{"key":"contact","value":"by_email"}` → `◉`).
  **A combo box refused a value that was not in its list** (`failed … "set failed"`), although the UI allows typing:
  pick a listed item.
- `save_document {"format":"form"}` → reopen with `open_document`: it comes back as an editable Word document with all
  fields and values (checked with `form_get_fields`). The `preview` shows labels and values inline without field boxes.

## Filling a Word template from data (verified)

Put `{{placeholders}}` in the text, then one `word_search_replace` per key: ALL occurrences are replaced, run
formatting (bold/colour) of the placeholder is kept (`<strong>` survived in `ToHtml`), and a check for leftover `{{`
returned none. Always search the result for `{{` before saving.

## Word helper tools (verified headless; cheaper than macros)

- A new docx starts with ONE empty paragraph (element 1); content tools append after it.
- `word_insert_paragraphs {"paragraphs":[…],"style":"Heading 1"}` (style applies to the batch) and
  `{"paragraphs":[…],"list_type":"numbered"}` (one batch = one list, "1. 2. 3."; call again to restart at 1).
- `word_add_table {"rows":[["Task","Owner"],…],"header":true}` (bold first row, plain grid); `word_search_replace
  {"search","replace","match_case"}`.
- `word_page_setup {"page_size":"A4","margins_mm":20,"header_text":"…","footer_text":"Confidential",
  "page_numbers":true,"align":"center"}` → PDF footer reads "Confidential 1"; `page_numbers_of_total`,
  `start_page_number`, `first_page_different`, `orientation` also exist (untested).
- `word_comment_text {"search":"timeline","prompt":"…","comment_text":"…","type":"comment"|"footnote"}`: the schema
  demands `prompt` even when `comment_text` is given (without it: "missing required argument prompt"). Author is
  "AI Assistant". Footnote text appears at the page bottom in the PDF.
- Comments by macro: `d.GetAllComments()[0]` → `AddReply('text','Author')`, `SetSolved(true)`, `GetQuoteText()`,
  `GetRepliesCount()` all work.
- Track changes by macro: `d.SetTrackRevisions(true)`, then tools such as `word_search_replace` are recorded;
  `d.AcceptAllRevisionChanges()` (or `Reject…`) works. `d.GetReviewReport()` is an object keyed by user but its
  values are not arrays and it is circular (`JSON.stringify` fails): inspect its keys before relying on it.
- `save_document {"path":…,"format":"pdf"|"md"|"docx"}`: PDF carries header/footer/footnotes; the `md` export
  keeps headings, numbered lists and tables (`**bold**` header cells) and drops headers/footers.

## PDF tools (verified headless; open a .pdf to get the `pdf_*` tools)

- `pdf_get_document_info` → page count + AcroForm field summary; `pdf_search_document {"query":"a|b","is_regex":true,
  "context_chars":20}` → matches with page, snippet, occurrence; `pdf_get_page_info {"page_number","include_forms"}`.
- Markup is a two-step pipeline: `pdf_get_text_quads {"page_number":1,"items":["requirements"]}` (items may be
  strings or `{"text"}`) → per-occurrence quads; then `pdf_markup_text {"page_number":1,"type":"highlight"|
  "strikeout"|"underline"|redact,"markup_targets":[{"text","quads":[the quad(s) of ONE occurrence],"comment"?}]}`.
  Passing only `{"text"}` fails with "empty quads". Apply `save_document` afterwards.
- **Colour trap:** `color` as a list (`[255,235,0]`, `[1,.92,0]`), `"#FFEB00"` or `"FFEB00"` all produced a solid BLACK
  box over the text in the render. Omit `color` (default yellow) or pass an object `{"r":255,"g":235,"b":0}`.
  Always render a page after marking up: the black box also looked like a redaction.
- `pdf_split {"parts":[{"pages":"1","path":ABS}],"overwrite":true}`; `pdf_merge {"sources":[{path,pages?}],
  "output_path"}` (untested).

## Fillable forms (verified headless)

- Flow: `create_document("docx")` → `form_add_field {"type":"text"|"dropdown"|"combobox"|"checkbox"…,"key","label",
  "placeholder","required","items":[…]}` per field → `save_document {"format":"form"}` (a fillable PDF that reopens
  EDITABLE as a Word document with its fields; `format:"pdf"` flattens it and says so in the reply).
- `form_get_fields` lists keys, `type` (`textForm|comboBoxForm|checkBoxForm|…`), `value`, `filled`, `required`.
  A dropdown reports as `comboBoxForm` and has an extra first list entry "Choose an item".
- **`form_fill {"fields":[{"key":"full_name","value":"Ada"},{"key":"plan","value":"Pro"},{"key":"agree","value":"true"}]}`**:
  `fields` must be a LIST of `{key,value}`; a `{key: value}` object fails with `field not found`. Checkbox values:
  "true"/"1"/"yes"/"on"/"checked"/"x". Read `form_get_fields` back (`filled:true`, checkbox `☑`).
- `word_generate_form {"description"}` is a two-call AI task that returns `{FIELD:…}` template syntax (untested).

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

## Designed decks from shapes (verified headless; render checked)

For anything presented, skip placeholders (`get_api_reference(editor="slide", topic="designed")` has the library; a tested copy
is `recipes/designed_deck_helpers.js`). Recipe, all inside ONE `slide_write_macro`: paste the helpers, `master.SetBackground(
SF("#EEF2F7"))`, `s1=pres.GetSlideByIndex(0); s1.ApplyLayout(blank)` and delete its leftover placeholders
(`s1.GetAllDrawings()` → `Delete()`), then per slide `Api.CreateSlide(); ApplyLayout(blank); AddSlide`, and compose with
`header(sl,"KICKER","Title")`, `card`, `chip`+`arrR` (process flow), `takeaway`, `footer`. A 4-slide deck (title with two
overlapping circles, three cards, a 4-step flow, chart slide) rendered cleanly on the first try.
- Add the chart AFTER the macro with `slide_add_chart_to_slide` on a blank-layout slide: it lands centred and small (~40% width)
  in the default blue/orange, not the deck palette; resize/recolour it by macro if it matters.
- Size cards to their content: at 3.5 M EMU high with two lines of text they looked half empty.
- Fonts: Linux has no Segoe UI; the library's `FONT` variable was set to Arial and rendered as Arial.
- `slide_get_presentation_context {"detail":"audit"}` still flags `layout_mismatch` on a designed title slide: ignore it.
- `preview` with `pages:"all"` writes `<path>_pages/imageN.png` beside your `path`; its reply text wrongly says the pages are
  in the default output folder, which was empty. Combine the pages into one contact sheet with PIL to read a whole deck in
  one image.

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

## Presentations (verified headless; `slide_*` tools)

Read `learn_about(topic="presentations")` (designed vs placeholder route). Placeholder route, as tested:
- A new deck has one title slide. Add slides by macro (no add-slide tool):
  `var p=Api.GetPresentation(),m=p.GetMaster(0),s=Api.CreateSlide();s.ApplyLayout(m.GetLayoutByType('obj'));p.AddSlide(s);`
  (types `title|obj|twoObj|secHead|picTx|titleOnly|blank`).
- Theme colours: `m.GetTheme().SetColorScheme(Api.CreateThemeColorScheme([12 × Api.Color('#…')],'Name'))`, order
  accent1..accent6, dk1, dk2, folHlink, hlink, lt1, lt2. Charts then use accents 1–3 (navy/blue/orange in the test).
- `slide_set_text {"slide_number":N,"target":"title|subtitle|body|notes","text":"line1\nline2"}` (newline = new paragraph;
  `target:"notes"` writes speaker notes).
- `slide_add_chart_to_slide {"slide_number":3,"chart_type":"bar","categories":[…],"series":["Q1","Q2"],"data":[[…],[…]]}`:
  **each inner list of `data` is ONE series' values** (length = number of categories). Giving only categories+series
  names without `data` is an error ("give either 'data' … or 'prompt'"). Mismatched shapes are padded: 3 rows with
  2 names made a third "Series 3" and cut the categories to the row length. The chart fills the content placeholder.
- `slide_get_presentation_context {"detail":"audit"}` lists problems per slide (e.g. `no_speaker_notes`); `preview`
  with `pages:"all"` renders every slide.

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

## Traps

- **An empty paragraph's `GetText()` is `"\r\n"`, not `""`.** Test emptiness with `.replace(/[\r\n]/g, "") === ""`.
- **`doc.RemoveAllElements()` leaves one empty paragraph**; after pushing new content, remove element 0 if empty.
- Applying a style doesn't override direct run formatting already on the text (vendor docs); clear direct props
  (e.g. via `word_for_all_text`) when restyling existing content.
- `doc.GetStyle(name)` returns null for an unknown name, and `SetStyle(null)` REMOVES a style — pass names to
  `SetStyle` so typos throw.
- **The MCP link can drop mid-session** (all `mcp__onlyoffice__*` tools vanish); the wrapper still works, so continue
  with `tools/ooc.py` (it now also takes `new:docx|xlsx|pptx` to start from a blank headless document).
- Never pass `discard_unsaved=true` on your own; the server refuses to drop unsaved work for a reason.

## Verify before reporting

- Live: read back with `word_get_document_text`, `ToHtml`, `GetNumbering`, `doc.GetStatistics()`.
- Visual: run the same build headless on a copy and `preview` it (see above), or ask the user to look.

## Recipes

- `recipes/resume_live.py` — ATS-friendly résumé rebuilt live in 4 visible stages (styles → header/summary →
  experience → rest + links). Fictional sample data; replace `RESUME`. Verified live (the earlier, longer sample made 2 pages; the current invented sample is 1 page) and headless with
  `preview` (render matched the intended layout).

## Log

- 2026-10-24: Designed decks from shapes, conditional formatting, pivot, validation, named range, print setup.
- 2026-10-24: Résumé copies (bullet clone, tracked date change, comment on a new paragraph), all form field types, template fill.
- 2026-10-24: Live edits in all four editors (word, cell, slide, pdf).
- 2026-10-24: Fillable forms (add, fill, save as form, reopen).
- 2026-10-24: PDF search/markup/split, highlight colour trap.
- 2026-10-24: Word helper tools (lists, table, page setup, comments, tracking), md/pdf export.
- 2026-10-24: Spreadsheet and presentation basics (cell_* and slide_* tools), headless build + preview; ooc.py `new:` mode.
- 2026-10-24: Initial notes: connector discovery and wrapper, live résumé rebuild, headless preview check
  (ONLYOFFICE 10.0.0 flatpak, server 2.0.0-native).
- 2026-10-25: conditional formats, autofilter, pivot, chart, sheet-object listing, slide set_text/notes/chart/background/arrange/delete/set_object verified via ooc.py.
