# ONLYOFFICE reference: tool audit

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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

## Tool audit: all 93 tools called on ONLYOFFICE 10.0.0 (2026-10-25, headless via `tools/ooc.py`)

> 10.0.0 (flatpak, server 2.0.0-native). Documents were invented; every tool was CALLED, results read back. **91 of 93 passed**; the two that did not are listed first. "Documented" (`coverage.sh`) only means the name appears in this folder; this audit is the measure of what was run.

- **Not verified today:** `list_editor_documents` ("ONLYOFFICE Desktop is not reachable": it needs the desktop app that started the server; verified live in earlier sessions, see the live-editing section) and `pdf_fill_form_fields` (works on a real AcroForm PDF; a form saved from Word reopens as a Word document, so the tool answered "works on an opened PDF, but the active document is … Word"; verified earlier on a government form, not repeated).
- **Passed as designed but return a task instead of a change (AI-task tools):** `word_check_spelling`, `word_rewrite_text`, `word_comment_text` (argument is `prompt`, not `comment`), `word_describe_image`, `word_generate_form`, `cell_explain_formula`, `cell_fill_missing_data`, `slide_rewrite_slide_text`; `cell_fix_formula` answered "No formula errors found" on a clean range. They need you to do the task and call again.
- **Argument names I guessed wrong first (the tool lists the right ones in its error; unknown arguments are rejected here, unlike the Craft apps):** `word_add_table {"rows":[["a","b"],["c","d"]],"header":true,"index"}` (rows is a list of lists), `cell_set_cell_data {"cells":[{address,formula,numberFormat,copyTo}]}`, `cell_add_cell_value_condition {"operator":"xlGreater","value1"}` (xl-names), `cell_set_sort {"key1","sort_order1":"xlDescending","header":"xlYes"}` (`header` is `xlYes|xlNo`, not a boolean), `cell_set_multi_sort {"key1","key2","sort_order2"}`,
  `pdf_markup_text {"page_number","type","markup_targets":[{"text","quads"}]}` (quads from `pdf_get_text_quads`, which returned `items:[]` for a word that is not on that page), `pdf_merge {"sources","output_path"}`. `word_for_range` refuses a range that touches a table cell ("not one stretch of the body").
- **Behaviour worth knowing:** `pdf_get_document_info` works on an opened PDF headless (the earlier failure was live only). `cell_insert_pivot_table` failed with "An error occurred while creating the pivot table!" when the source range included a column without a header (a formula column in E); with a clean `A1:D6` it worked. `word_add_image` and `cell_add_image` take mm; `word_page_setup {"orientation":"landscape"}` → `{pageWidthTw:15840,…}`.
- Still not covered by tools or tested: the unbounded Document Builder macro API (the roadmap areas: Word styles/TOC/sections via macros, spreadsheet pivot options/slicers/sparklines, slide masters, PDF annotations beyond highlight, protection), a second ONLYOFFICE version, and complex live editing.
