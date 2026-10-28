# WordCraft reference: log

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-10-24: Paragraph formatting, lists, tabs, sort, clipboard/paste, format painter, undoTo, goto, spike; two traps.
- 2026-10-24: Per-section headers/footers SOLVED; accessibility checker and tagged PDF export.
- 2026-10-24: Citations/bibliography (author string format), cross-references, document compare, templates.
- 2026-10-24: Mail merge (recipients, filter, fields, address block, IF rule, partial finish).
- 2026-10-24: Résumé round-trip fidelity check on two designs (faithful; only custom doc properties lost).
- 2026-10-24: Live mode on a blank document: typing, formatting, screenshot/render, export, failed-select trap.
- 2026-10-24: Initial notes from building and linking an ATS résumé (WordCraft 0.10.0).
- 2026-10-24: Linked the official docs (docs/mcp.md, docs/control-protocol.md); corrected path resolution.
- 2026-10-24: Generalized for sharing; résumé recipe made data-driven with fictional sample content.
- 2026-10-24: Numbered lists; confirmed that new paragraphs inherit list numbering.
- 2026-10-24: Tables (fill, header row shading/repeat, from text), headers/footers, x-of-y page numbers,
  page breaks, columns, links, TOC, footnotes, pictures, find/replace, comments, tracked changes.
- 2026-10-24: Header tab zones, page setup, regex/wildcard find, macros, proofing.
- 2026-10-24: Inline formatting, custom styles, captions, drop cap, shapes/text boxes, cover page, multilevel lists,
  roman page numbers, first-page-different footers, charts, equations, table merge, convert formats.
- 2026-10-25 (4): tracked changes, comments, compare, content controls, watermark, restrict/encrypt with password options, spelling/grammar, table of figures, table formula/sort, convert formats verified headless.
- 2026-10-25 (5): nine headless sections re-run on 0.10.0 and 0.11.0 (identical) and the live-mode steps on the 0.11.0 app; version labels added per section.
- 2026-10-25 (6): styles management, Design tab, index (mark/insert/update), TOC caret behaviour, equation editing (structures, convert, number), tracked changes by author/one at a time/options/combine verified headless on 0.11.0.
- 2026-10-25 (7): table editing/styles/nested tables, outline view, quick parts/autotext/doc properties, SmartArt/WordArt/canvas/icons, picture and shape commands verified headless on 0.11.0.
- 2026-10-25 (8): manuscript format (publisher submission) built and checked in WordCraft and ONLYOFFICE; header-skipping-page-1 order, space-before-at-page-top trap, italic carry-over fix.
- 2026-10-25 (9): screenplay format built and checked in WordCraft and ONLYOFFICE; title-page section with restarted numbering, exact line pitch, indentRight, autocorrect trap.
- 2026-10-25 (10): screenplay extras (scene numbers, bold/underline, centred, dual dialogue, acts, Fountain title page, Fountain/FDX export, (MORE)/(CONT'D) by two-pass pagination) and manuscript extras (verse, block quote, footnotes, page count, query letter, synopsis) built and checked.
- 2026-10-25 (11): stage play format (title page and characters page in their own numbering, centred cues, italic directions) built and checked in WordCraft and ONLYOFFICE; section header with a text prefix before the page field.
- 2026-10-25 (12): character effects, paragraph helpers, find next/previous, clipboard items, header/footer edit/remove, content-control actions, file info/privacy/inspect/versions/export/print, labels and envelopes verified headless on 0.11.0.
- 2026-10-25 (13): ink (strokes, lasso select/recolour/move/delete, erase, ink to shape, pens, replay) verified headless; page index is 0-based.
- 2026-10-25 (14): ink drawn by hand in the live window: 226/154-point strokes, lasso mode must be switched on with draw.lasso {}, convertInk made a rectangle from a hand-drawn box.
- 2026-10-25 (15): reformatting a real document with review comments: style-name collision, header-row shading by caret.up trap, column widths, links in cells, x-of-y footer, landscape appendix with a picture, empty-bullet-before-break fix, comment anchors.
- 2026-10-26 (16): bullets toggle trap; table-row edit in a commented document; built a 2-page explanation memo from a script.
- 2026-10-26 (17): gap round: layout.section, section breaks (nextPage/continuous), per-section orientation.
- 2026-10-26 (18): table layouts for designed pages (banner, sidebar, colour blocks, hairlines, nested bars, row-wide cellMargins, 6 pt minimum column, fixed autofit) from the 18 résumé redesigns.
- 2026-10-26 (19): continuous vertical lines: insideV table style for timelines, border bridging across spaceBefore, hanging-indent alignment (traditional-b fixed).
- 2026-10-26 (20): résumé designs now built for A4 as well as Letter (page width/height as variables, full-page row = page height - 14 pt) and without photos (initials monogram in colour blocks).
- 2026-10-26 (21): sweep of the remaining 231 command ids on a blank document with inspect/render comparison (208 ran, 23 refused with a reason); smoke test, effects not read back.
- 2026-10-27 (22): showing long text in the live window: pandoc docx + `open_document` + `render_page`.
- 2026-10-27 (23): policy manual (styles, callouts, TOC at a placeholder, 5-column matrix, tracked-change change log, markup PDF); review.trackChanges takes `value`, not `on`.
- 2026-10-27 (24): a 239-page novel manuscript built and opened in WordCraft, ONLYOFFICE and GenOffice (same pagination); GenOffice headless page count differs.
- 2026-10-27 (25): a verse play built as a stage play; builder now keeps verse lines (`| ` prefix) and handles epilogue.
