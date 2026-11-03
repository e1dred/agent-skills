# ONLYOFFICE reference: Word documents

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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
