# GenOffice supplement reference: document styles

Part of the genoffice-supplement skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## All eight styles x doc, report, resume and cv against WordCraft (2026-10-27, A4, same renderer)
`build_genoffice.py` and `styles/build_wordcraft.py` were run for every style and kind (32 pairs) and every page was rendered with `genoffice render` and compared: page count (all 32 pairs equal) and the mean absolute pixel difference of a 300x424 greyscale page (0 = identical; text anti-aliasing alone gives about 2 to 3).
Mean page difference (higher = less alike): doc 2.4 (clean) to 8.3 (professional, one page of tighter text); resume 2.8 (modern) to 5.9; cv 4.0 (modern) to 8.0 (academic, creative); report 6.1 (clean) to 13.7 (stylish). Overall 6.1. Clean, modern and the résumés match closely; the report kind differs most because of table details.
What still differs, seen on side-by-side images:
- **Report tables:** the fact-sheet and KPI cells are left-aligned in GenOffice's version (WordCraft centres the KPI row): there is no op to align one cell's paragraph, only the whole table (`setParagraphFormat` on the table block). Cell text sizes are a little larger, columns wrap earlier ("Community Garden Program" wrapped in the academic style) and rows are slightly taller, so a table can slip across a page break (the risks table lost its last row to page 2 in two styles).
- **Bullets:** the bullet indent is wider than WordCraft's in every style.
- **Header text** is centred (no alignment op), where the plan wants it right-aligned.
Bug found while comparing: **`define_style` drops a zero first-line indent**, so in the academic style (Normal has a 0.5 in first-line indent) every style based on Normal (headings, bullets, table text, captions) inherited it and looked indented. `post_process` now writes `<w:ind w:firstLine="0"/>` into those styles.
Other builder additions: report tables (per-cell fills, status colours, column widths from the plan, header row, optional grid, cell paragraph spacing set on the whole table) through `setTableCellFormat`/`setMatchedFont`; cell paragraphs otherwise take Normal's spacing, which made every table row far too tall.

## Style rebuild: `modern` doc via GenOffice vs WordCraft vs ONLYOFFICE (2026-10-27)
Builder: `build_genoffice.py` in this folder (imports `../styles/plan.py` read-only, so the same plan feeds all three apps). Run: `PYTHONDONTWRITEBYTECODE=1 python3 build_genoffice.py modern doc /abs/out.docx --paper=a4 --page-numbers=bottom-center`. Handles block types p/heading/bullets/table/figure caption text of kind doc; figure picture, footnote, merged title row, columns, header text are not done yet.
All three docx files were rendered with the same renderer (`genoffice render`) and compared side by side (WordCraft: `wordcraft-cli run --script job.json`).
Result: title, headings, body, subtitle, margins, header-row fill, page number and table borders match. Differences left in GenOffice's version:
- Quote left bar and heading rules: `define_style` has no borders. `setParagraphFormat borders` takes only "tblr" letters and writes a thin auto-coloured line (sz 4, colour auto), so no teal bar and no coloured heading rule.
- Bullet colour: stays black (WordCraft and ONLYOFFICE give teal bullets); bullet indent is larger.
- Text looks slightly larger than in the other two at the same point sizes (not investigated).
Traps from this build:
- `define_style` lengths (spaceBefore/After, indents) are POINTS; twips (pt*20) made 20x gaps and an 8-page document. `setParagraphFormat` lengths are twips. Different units in two ops of the same guide.
- `insert_content` HTML lists/tables get block indexes: a `<ul>` makes one block per `<li>`, a table is one block.
- A table header row needs white text set per cell: `setMatchedFont {text: "<cell text>", color, bold, target: table block}` works inside table cells.
- Create the docx from HTML (`genoffice create --type docx --from in.html`), then define_style in one apply and applyStyle in a second apply.

## All eight styles, doc kind, GenOffice vs WordCraft (2026-10-27, A4, rendered with the same renderer)
build_genoffice.py now also does: figure (insert_picture after the caption's predecessor, done last, in reverse order), footnote (insert_footnote with afterText), merged title row (mergeTableCells + sub-header fill), columns (insert_section_break continuous, then set_page_setup section 1 columns), header text and page number (header text comes out centred, the plan wants right-aligned: no header alignment op).
Match (no visible difference except bullets): clean, academic, modern.
Gaps at first, worst first (CLOSED later the same day by the styles.xml/numbering.xml patch, see "Docs gaps closed" in `docs-ops.md`):
1. professional: no navy title rule and no heading rules, no letter-spacing on the caps headings.
2. elegant: no burgundy hairline under the headings, no letter-spacing on the caps headings.
3. creative: no teal heading rules.  4. stylish: no gold bar left of the headings.  5. traditional: no title rule.
Everywhere: bullets stay black and indent further than in WordCraft.
More traps: with columns=2 the table keeps its full width and is clipped in a narrow column (the last columns vanish); there is no op to resize the table to the column. Header/footer text has no alignment option (centred only).
Untried workaround for the rules: `setParagraphFormat borders:"b"` on each heading block gives a thin auto-coloured line (black), so right position, wrong colour.

## Page count: headless `render` vs the app window (2026-10-27, GenOffice 0.12.117)
A 239-page manuscript .docx (Times New Roman 12 pt, double-spaced, 1-inch margins) showed 239 pages in the GenOffice app window, in WordCraft and in ONLYOFFICE, with the same first word on the last page. **`genoffice render` (headless export + pdfium) said "page out of range (1-235)" for the same file.** Chapter I still started on page 21 there, so the two paths drift later in the book. Judge pagination in the app window or a PDF made by the app, not from the headless page range. Cause not determined.
