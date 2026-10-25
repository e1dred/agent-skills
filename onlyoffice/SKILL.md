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
  experience → rest + links). Fictional sample data; replace `RESUME`. Verified live (2 pages) and headless with
  `preview` (render matched the intended layout).

## Log

- 2026-10-24: Fillable forms (add, fill, save as form, reopen).
- 2026-10-24: PDF search/markup/split, highlight colour trap.
- 2026-10-24: Word helper tools (lists, table, page setup, comments, tracking), md/pdf export.
- 2026-10-24: Spreadsheet and presentation basics (cell_* and slide_* tools), headless build + preview; ooc.py `new:` mode.
- 2026-10-24: Initial notes: connector discovery and wrapper, live résumé rebuild, headless preview check
  (ONLYOFFICE 10.0.0 flatpak, server 2.0.0-native).
