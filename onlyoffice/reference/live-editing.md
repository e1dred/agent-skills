# ONLYOFFICE reference: live editing

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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
