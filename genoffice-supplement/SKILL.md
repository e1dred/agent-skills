---
name: genoffice-supplement
description: Supplementary, verified notes on GenOffice (Docs editor and the genoffice CLI/MCP) that its own bundled skills do not cover: what each Word op really does, traps, units, document-style rebuilds compared with WordCraft and ONLYOFFICE. Load next to GenOffice's own skill before editing .docx with GenOffice; add what you learn.
---

# GenOffice supplement

**Scope rule (strict):** this skill holds only things GenOffice's own bundled skills do not provide. It never copies or restates
a GenOffice-provided skill (its generated `genoffice` skill, the ~45 recommended app skills). Read those first; this adds
what running the app showed. Tested on GenOffice 0.12.117 (Linux AppImage), CLI and MCP, headless.

GenOffice has six editors: Docs, Sheets, Slides, Markdown, HTML and PDF. Only the Docs (.docx) ops are covered so far.

## Word-op sweep, 2026-10-27, GenOffice 0.12.117 (headless CLI `genoffice docs apply`)
Method: fresh copy of a 9-block docx per op, apply, then read back with `docs read` flags, unzip the XML, and render (`genoffice render x.docx --out dir`, one PNG per page) and look.

Status "ok" only means the op was accepted. Check the XML or the render.

Verified (XML and/or render): setFont (bold, colour, size, family; link), setMatchedFont (text -> run-level bold+highlight), setParagraphFormat (jc, line, firstLine, spacing, shading, borders "tb", tabs with leader), setHeadingLevel, findReplace, deleteBlocks, moveBlocks, setList/clearList, insertToc (TOC field, entries listed, NO page numbers in render; Word computes them on open), insertField SEQ/DATE/MERGEFIELD/REF, insertBookmark, updateFields, table row/column insert/delete, mergeTableCells/splitTableCell, setTableCellFormat (fill, vAlign, borders), applyStyle, insert_content (h2, p, pre, blockquote, formula), replace_blocks, insert_image, insert_picture (floating, wrapSquare, alt text), setImageProperties, insert_text_box, insert_chart/edit_chart (native chart part + embedded workbook), set_header_footer ({PAGE}/{NUMPAGES} work; first/even views set titlePg/evenAndOddHeaders), set_page_setup (paper, landscape, margins, 2 columns, pageNumberStart), insert_section_break, set_watermark (rendered diagonal), define_style, add/reply/resolve/delete comment (threads, done flag), insert_footnote/endnote, set_properties (core+custom), wrap/unwrap_content_control, --track (author, ins/del revisions), accept_changes/reject_changes (selector by author/type/all), `docs compare` (redline with revisions).

## Traps (each one tripped the sweep)
- Op field names differ from what you guess: `moveBlocks` takes `blockIndexes` (no `target`); `setList` takes `kind: "bullet"|"number"` (not `type`). Rejections name the allowed fields and the whole batch is atomic: nothing applied.
- Things defined or created earlier in a batch are NOT visible to later ops of the same batch for: `define_style` type table then `setTableStyle`; `wrap_content_control` then `unwrap_content_control`. Split into two `apply` calls. (define_style paragraph then applyStyle in one batch works.)
- `define_style` for a new style needs paragraph or run formatting (or basedOn); basedOn must exist in the document. A new docx has no table styles (`tableStyles: []`), so create one with a run property and apply it in a second call.
- `setTableCellFormat` fill does not change text colour: a dark header fill keeps black text. Set white text separately (setFont on that block does not reach table cells in my sweep; not yet tested how).
- `insert_text_box` default anchor is the paragraph, so x/y count from the margin, not the page edge: x 15cm + 4cm wide ran off the right side. Use `anchor:"page"` for page coordinates. insert_picture needs `float.anchor:"page"` the same way.
- Comment ids are small positional strings ("1", "2"); revision ids ("r1"...) are positional and change after every edit, so re-read before accept/reject.
- Reject-all restored the original text; accept with type filter leaves the other revisions pending.
- Table merge concatenates cell text as separate paragraphs; split keeps text in the top-left cell.
- Watermark is heavy at opacity 0.3 with a large size; use about 0.15 for body-text legibility.

## Not yet tested
setFont null (clear), partial-selection edits, setImageProperties on a floating picture, insert_content formula render, insertField IF/PAGEREF, docs apply on a file open in the app (needs --force), `--dry-run`, `--best-effort`, live `open`/`selection`, and comparison with WordCraft/ONLYOFFICE styles.


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
Gaps, worst first (all from the border/spacing limits above):
1. professional: no navy title rule and no heading rules, no letter-spacing on the caps headings.
2. elegant: no burgundy hairline under the headings, no letter-spacing on the caps headings.
3. creative: no teal heading rules.  4. stylish: no gold bar left of the headings.  5. traditional: no title rule.
Everywhere: bullets stay black and indent further than in WordCraft.
More traps: with columns=2 the table keeps its full width and is clipped in a narrow column (the last columns vanish); there is no op to resize the table to the column. Header/footer text has no alignment option (centred only).
Untried workaround for the rules: `setParagraphFormat borders:"b"` on each heading block gives a thin auto-coloured line (black), so right position, wrong colour.

## Keep this file growing
Add what you learn, labelled with the GenOffice version and what was checked (XML, read-back or render). Do not paste text from GenOffice's own skills.
