# ONLYOFFICE reference: document styles

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

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
