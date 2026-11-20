# GenOffice supplement reference: Docs ops

Part of the genoffice-supplement skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Docs-op sweep, 2026-10-27, GenOffice 0.12.117 (headless CLI `genoffice docs apply`)
Method (scripts in `tools/`, re-run with `bash tools/run_sweeps.sh`): fresh copy of a 9-block docx per op, apply, then read back with `docs read` flags, unzip the XML, and render (`genoffice render x.docx --out dir`, one PNG per page) and look.

Status "ok" only means the op was accepted: unzip the .docx and read the XML.

Verified (XML and/or render): setFont (bold, colour, size, family; link), setMatchedFont (text -> run-level bold+highlight), setParagraphFormat (jc, line, firstLine, spacing, shading, borders "tb", tabs with leader), setHeadingLevel, findReplace, deleteBlocks, moveBlocks, setList/clearList, insertToc (TOC field, entries listed), insertField SEQ/DATE/MERGEFIELD/REF, insertBookmark, updateFields, table row/column insert/delete, mergeTableCells/splitTableCell, setTableCellFormat (fill, vAlign, borders), applyStyle, insert_content (h2, p, pre, blockquote, formula), replace_blocks, insert_image, insert_picture (floating, wrapSquare, alt text), setImageProperties, insert_text_box, insert_chart/edit_chart (native chart part + embedded workbook), set_header_footer ({PAGE}/{NUMPAGES} work; first/even views set titlePg/evenAndOddHeaders), set_page_setup (paper, landscape, margins, 2 columns, pageNumberStart), insert_section_break, set_watermark (rendered diagonal), define_style, add/reply/resolve/delete comment (threads, done flag), insert_footnote/endnote, set_properties (core+custom), wrap/unwrap_content_control, --track (author, ins/del revisions), accept_changes/reject_changes (selector by author/type/all), `docs compare` (redline with revisions).

## Docs gaps closed (2026-10-27, GenOffice 0.12.117, headless)
- **Coloured borders, letter-spacing and bullet colour cannot be set with ops** (an unknown field such as `borderColor` is rejected). **Workaround that works:** after the last `apply`, rewrite the .docx zip and patch `word/styles.xml` (insert `<w:pBdr>` with colour, size and space into the style's `w:pPr` before `w:shd/tabs/spacing/ind/jc`, and `<w:spacing w:val="N"/>` before `w:sz` in its `w:rPr` for letter-spacing) and `word/numbering.xml` (a `<w:color>` in the bullet level's `w:rPr`). `build_genoffice.py` does this in `post_process`. Result, rendered against WordCraft: the professional (navy title and heading rules, spaced caps), elegant (burgundy hairlines), creative (teal rules), stylish (gold bar) and traditional (title rule) styles now match, and bullets take the accent colour. Order matters in OOXML, which is why the insert points are fixed.
- **Résumé and CV kinds** now build too (`build_genoffice.py STYLE resume|cv /abs/out.docx`): both consist only of paragraphs, so the same path works. Right-aligned dates come from a style tab stop (`define_style paragraph.tabs: [{"pos":"506pt","align":"right"}]`) plus a tab in the text. Compared page 1 with WordCraft's version for the professional style: the same layout, headings, rules, bullets and right-aligned dates (education dates are not bold in the GenOffice version).
- **Not done:** partial-selection edits (they need a selection made in the app).

## Coverage of the op lists (2026-10-27, GenOffice 0.12.117, headless)
All ops the three guides list were run at least once and checked, except the ones their guide marks not-ai-callable (binary payloads), in the sweeps above or in a last round for the stragglers (note edit/delete, defined-name delete, section add/rename/remove, animation reorder/remove, connector endpoints, group/ungroup, slide layout, comment and slide delete, picture opacity, crop and redaction on a picture made with `create --spec`). Exception: `moveSection` was rejected when there was only one section ("the section change was rejected") and is untested with two.

## New in 0.13.18 (tested headless 2026-11-15, from 0.12.852)
- `create --type docx ... --no-generator-fields` drops Application / AppVersion from `docProps/app.xml` (the Word-default Template stays). 0.12.852: `unknown_option`.
- `convert` from a legacy `.ppt`: only the reject path was tested (a non-OLE file gives `conversion_failed`, reason `not_cfb`).
- `set_header_footer` `section`: **0.12.852 silently ignored it**: both ops hit the trailing section and the later one won, so an earlier section's header was lost. In 0.13.18 it is honoured; `docs read --header-footer` lists every section and an out-of-range value is refused.
- `sheet apply` `add_chart` `columns`: **column letters, at least 2**. 0.12.852 silently ignored the key and charted the default columns; the letters and the minimum show up in the error.
- `.docx` files no longer contain zip directory entries (`word/`, `_rels/`); Office does not care, but `namelist()` counts are lower than before.
- Unchanged: the three sweeps (docs, sheets, slides), `info`, `render` (byte-identical PNG), `merge`.
