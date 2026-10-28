---
name: onlyoffice
description: Use when editing documents, spreadsheets, slides, PDFs or forms in ONLYOFFICE Desktop Editors, live in an open window or headless, through its AI-tools MCP server (onlyoffice-document-builder), including Word macros and connecting from the Linux flatpak
---

# ONLYOFFICE Desktop Editors

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, tested on **ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, Linux)** with the
AI-tools server **onlyoffice-document-builder 2.0.0-native**. Re-check anything below on other versions.

> **Versions:** every section was tested on ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, commit 318889a1…) with `onlyoffice-document-builder 2.0.0-native`; `check-versions.sh` showed no update available through 2026-10-25, so nothing here was re-tested on a second version. Live-editing sections were tested 2026-10-24; the tool and macro sections 2026-10-25.

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
  "output_path","overwrite"}` (verified 2026-10-25: "Merged 4 page(s) from 2 file(s)").

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

## Every remaining tool, verified (2026-10-25, via `tools/ooc.py`; 93 of 93 tools now covered)

A new docx has one empty paragraph at index 1, so `word_insert_paragraphs` text starts at index/`par_number` 2. Indexes are 1-based and count top-level elements (a table is one);
a TOC or table shifts later numbers — re-read `word_get_document_structure` (`{"start_index","end_index"}` for a slice) before addressing by number, or use `internal_id`.

**Word**
- Read: `word_get_paragraph_text {"par_number":2}` or `{"internal_id"}` → text, html, internalId; `word_search_document {"query","is_regex","flags","context_chars"}` → matches with `paragraphIndex`.
- Write: `word_set_paragraph_text {"text","index"|"internal_id"}`; `word_set_paragraph_props {"index","jc":"center","spacing_before":12,"spacing_after":6,"style":"Heading 1","list_type":"bullet","list_level":0}`
  (`end_index` for a range); `word_change_paragraph_style {"style","par_number"|"internal_id"}`; `word_delete {"index","count"}` or `{"internal_id"}` → `{deleted,removed,remaining}`.
- Text style: `word_change_text_style {"search":"Revenue","bold":true,"font_size":14,"color":{"r":192,"g":57,"b":43}}` — **colour must be `{r,g,b}` or `"r,g,b"`, not hex**; also `italic`, `underline`, `highlight`, `match_case`.
- Insert: `word_insert {"kind":"toc"|"page_break"|"hyperlink"|"bookmark","index","text","url","name"}` (TOC builds from Heading styles; page numbers fill on open; bookmark `index` is a paragraph number),
  `word_insert_page {"location":"end"}`, `word_add_image {"src":"/abs/pic.png","width":40,"height":27,"index":0}` (mm; 0 = end; no `src` = an AI task asking you for a picture).
- Tables: `word_table_edit {"action":"add_row|remove_row|add_column|remove_column","table_index":1,"position":0,"count":1}` → `{rows,columns}`; needs an existing table (`word_add_table` first). Cell text: `word_set_paragraph_text` with the cell's internalId.
- Code on text: `word_for_all_paragraphs {"code":"result.push(par.GetText().length); par.SetSpacingAfter(120);"}` (variables `par`, `result`); `word_for_range {"code":"range.SetItalic(true); …","start_index","end_index"}` (variable `range`).
- **AI-task tools** (return `[AI TASK]`; you produce the answer, then call again with the parameter): `word_check_spelling {"par_number":2}` → send again with `"corrected_text":"…"`;
  `word_rewrite_text {"prompt","par_number","result":"new text","show_difference":true}` (recorded as a tracked insertion); `word_describe_image {"prompt","image_index":1}` returns the picture for you to look at;
  `word_generate_docx {"description","markdown":"# Title\n\n- item"}` builds a document from your markdown into an empty doc.

**Spreadsheet**
- `cell_set_values {"range":"A1","values":[[…]],"number_format"?}` (null = empty), `cell_set_formula {"cell":"D2","formula":"=B2*C2"}`, `cell_get_cell_details {"ranges":"A1:D3","include_styles":false}` (value + formula pairs),
  `cell_search_data {"search_term","match_formulas":true,"regex","wildcards","range","sheet_name"}` (finds formulas too), `cell_insert {"range":"3:3","mode":"rows|columns","count","shift":"down|right"}` and
  `cell_delete {"range":"A3:D3","mode":"contents|rows|columns|cells"}` (→ `{rowsDeleted,…}`).
- `cell_write_macro {"code":"…return …","images":{}}` — `images` is required and must be an object `{name: path}` (an empty `{}` is fine); returns the macro's return value.
- `cell_add_image {"src","cell":"H2","width":40,"height":27}` (mm).
- **AI-task tools**: `cell_explain_formula {"range":"D2"}` (just returns an instruction; your explanation is the answer, nothing is written); `cell_fix_formula {"range":"D2:D3"}` → AI task listing `Sheet!D2: =B2/0 → #DIV/0! [FIX THIS]`,
  call again with `"fixes":[{"sheet":"Sheet1","address":"D2","formula":"=IF(…)"}]` ("No formula errors found" when the range is clean); `cell_fill_missing_data {"range":"B2:B3","fills":[{"row":2,"column":1,"new_value":5}]}` (row/column 1-based *relative to the range*; key is `new_value`, not `value`).

**Slides**
- `slide_search_document {"query","slide_number","include_notes","include_masters"}`, `slide_search_replace {"search","replace","match_case","include_notes"}`.
- `slide_add_image_by_description {"src":"/abs/pic.png","slide_number":1,"width_mm":60,"height_mm":40}` (with `src` it inserts at once, centered), `slide_replace_image {"src","slide_number"}` (→ "Image 'Picture 4' replaced"; `target` names a specific one).
- **AI-task tools**: `slide_rewrite_slide_text {"prompt","slide_number":1,"rewritten":[{"id":"1758","text":"<p>Review</p>"}]}` (the first call shows the paragraph ids as HTML; return only changed ones);
  `slide_generate_notes {"slide_numbers":[1],"style":"talking-points","notes":[{"slideNum":1,"notes":"…"}],"overwrite"?}` → saved as speaker notes (`slide_get_presentation_context` shows them).

**Forms and images**
- `form_set_data {"values":{"name":"Ann Example","email":"ann@example.com","agree":true}}` fills by key (checkbox shows ☑); `form_delete_field {"key":"email"}` (or `"all":true`); check with `form_get_fields {}`.
- `view_image {"path":"/abs/pic.png"}` → size and format plus the picture itself, for you to look at.

## Document styles (traditional, elegant, clean, professional, academic, modern, stylish, creative; document, résumé, CV, APA/MLA paper)

`../styles/` holds the specs (`styles.json`), a font resolver (installed fonts first, Office-portable by default) and a neutral build plan (`plan.py`);
`python3 -I styles/build_onlyoffice.py STYLE doc|resume|cv|paper /abs/out.docx [--paper=a4] [--page-numbers=…] [--columns=2] [--photo=…]
[--layout=functional|combined] [--format=apa|mla] [--pdf] [--overwrite] > calls.json` then `python3 -I tools/ooc.py new:docx calls.json`. See `../styles/README.md`
for the table, gallery, ATS notes and options. Verified: every style in 3 kinds plus the feature samples, rendered by ONLYOFFICE's own PDF export. Macro facts that mattered:
- **`save_document` never overwrites** an existing file: it writes `name (1).pdf` and the old `name.pdf` stays. I once judged a stale file for an hour; delete the old file or pass `overwrite:true`.
- **A failing macro does not stop `ooc.py`**: the later `save_document` still runs and saves a half-built document. Always grep the output for `Error` (the style builders' test loops do).
- `Api.CreateTable(rows, cols)` in this build (first argument = **rows**); reach cells with `tbl.GetRow(r).GetCell(c)`. Colour a header cell's text on the *run* (`run.SetColor`), not the paragraph.
  Borders: `tbl.SetTableBorderTop/Bottom/Left/Right/InsideH/InsideV("single", 4, 0, color)`; shading `cell.SetShd("clear", color)`.
- Header/footer: `sec.GetHeader("default", true).GetElement(0)` then `AddText` and `AddPageNumber()`; `sec.GetFooter("default", true)`. Style them via `doc.GetStyle("Header")`/`"Footer"`.
- Columns after a title: `doc.CreateSection(lastParagraph)` closes section 1 there; then on `doc.GetFinalSection()`: `SetType("continuous")` and `SetEqualColumns(2, 360)` (`SetNumberOfColumns` does not exist).
- Page break before a paragraph: `p.SetPageBreakBefore(true)` (cleaner than a break run, which leaves an empty line).
- Photo: run the macro, then `word_add_image {"src","width":30,"height":40,"index":1}` (mm), then a second macro `doc.GetElement(0).SetStyle(doc.GetStyle("Resume Photo"))`.
- `Api.CreateTable(rows, cols)` is confirmed by `get_api_reference` ("first arg ROWS"). `tbl.MergeCells([cell objects])` merges (cells of the same row → the row then has FEWER cells: fill text after merging, using `row.GetCellsCount()`).
- No paragraph-direction call exists in this macro API (no `SetBidi` anywhere; `SetLanguage` exists on runs/paragraphs/text properties). Right-to-left and CJK text render correctly with the right font plus `SetJc("right")` for RTL, but the paragraph stays left-to-right underneath.
- `word_comment_text {"search","prompt":"Add a footnote","comment_text":"…","type":"footnote"}` adds a real footnote but anchors it at the END of the paragraph containing the phrase.
- Picture alt text: the image tools have no parameter; use `doc.GetAllDrawingObjects()[n].SetDescription("…")` (also `SetTitle`, `SetName`) in a macro afterwards (document order).
- `word_add_image {"src","width","height","index"}` inserts BEFORE the element at `index` (1-based, top-level elements); when adding several pictures in ascending order, add 1 for each already inserted.
- Introspect objects when the reference is silent: `for (var k in obj) if (typeof obj[k] === "function" && /pattern/i.test(k)) …` inside `word_write_macro`.
- **`report` kind (quarterly review), 2026-10-26:** in a `word_write_macro`, `cell.SetWidth("twips", n)` per cell gives column widths, `cell.SetShd("clear", color)` the status fills, and `SetTableBorder*("none", 0, 0, color)` a borderless fact-sheet/KPI table; all matched WordCraft in the PDF render. See `styles/build_onlyoffice.py` (`addRichTable`).

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

## Tool audit: all 93 tools called on ONLYOFFICE 10.0.0 (2026-10-25, headless via `tools/ooc.py`)

> **Versions:** 10.0.0 (flatpak, server 2.0.0-native). Documents were invented; every tool was CALLED, results read back. **91 of 93 passed**; the two that did not are listed first. "Documented" (`coverage.sh`) only means the name appears in this folder; this audit is the measure of what was run.

- **Not verified today:** `list_editor_documents` ("ONLYOFFICE Desktop is not reachable": it needs the desktop app that started the server; verified live in earlier sessions, see the live-editing section) and `pdf_fill_form_fields` (works on a real AcroForm PDF; a form saved from Word reopens as a Word document, so the tool answered "works on an opened PDF, but the active document is … Word"; verified earlier on a government form, not repeated).
- **Passed as designed but return a task instead of a change (AI-task tools):** `word_check_spelling`, `word_rewrite_text`, `word_comment_text` (argument is `prompt`, not `comment`), `word_describe_image`, `word_generate_form`, `cell_explain_formula`, `cell_fill_missing_data`, `slide_rewrite_slide_text`; `cell_fix_formula` answered "No formula errors found" on a clean range. They need you to do the task and call again.
- **Argument names I guessed wrong first (the tool lists the right ones in its error; unknown arguments are rejected here, unlike the Craft apps):** `word_add_table {"rows":[["a","b"],["c","d"]],"header":true,"index"}` (rows is a list of lists), `cell_set_cell_data {"cells":[{address,formula,numberFormat,copyTo}]}`, `cell_add_cell_value_condition {"operator":"xlGreater","value1"}` (xl-names), `cell_set_sort {"key1","sort_order1":"xlDescending","header":"xlYes"}` (`header` is `xlYes|xlNo`, not a boolean), `cell_set_multi_sort {"key1","key2","sort_order2"}`,
  `pdf_markup_text {"page_number","type","markup_targets":[{"text","quads"}]}` (quads from `pdf_get_text_quads`, which returned `items:[]` for a word that is not on that page), `pdf_merge {"sources","output_path"}`. `word_for_range` refuses a range that touches a table cell ("not one stretch of the body").
- **Behaviour worth knowing:** `pdf_get_document_info` works on an opened PDF headless (the earlier failure was live only). `cell_insert_pivot_table` failed with "An error occurred while creating the pivot table!" when the source range included a column without a header (a formula column in E); with a clean `A1:D6` it worked. `word_add_image` and `cell_add_image` take mm; `word_page_setup {"orientation":"landscape"}` → `{pageWidthTw:15840,…}`.
- Still not covered by tools or tested: the unbounded Document Builder macro API (the roadmap areas: Word styles/TOC/sections via macros, spreadsheet pivot options/slicers/sparklines, slide masters, PDF annotations beyond highlight, protection), a second ONLYOFFICE version, and complex live editing.

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
- 2026-10-25 (2): the remaining 38 tools (Word text/structure/AI tools, spreadsheet cell tools, slide search/image/AI tools, form_set_data/delete, view_image) verified; all 93 documented.
- 2026-10-25 (3): tracked revisions, comments, watermark, password-encrypted save, defined names, protected ranges, hyperlinks, chart formatting, slide transitions/animations/theme colours verified via macros.
- 2026-10-25 (4): version labels added; nothing re-tested on a second version (no update available).
- 2026-10-25 (6): audit: all 93 tools called on 10.0.0 headless; 91 passed, 2 not verified today (live-only / real PDF form); pdf_merge verified; argument corrections recorded.
