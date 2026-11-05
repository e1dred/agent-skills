# PdfCraft reference: log

Part of the pdfcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-11-04: first verified run (PdfCraft 0.18.1, Linux AppImage): CLI extracted from the AppImage; 184 tools listed.
  Headless, read back each time: info/text/render, edit rotate/delete, extract/split/combine, audit/check,
  script doc_open→text_find→comment_add→bookmark_add→doc_set_info→doc_save→doc_close, page_insert_blank/page_move,
  form_add_field/form_fields/form_fill (saved AcroForm verified with qpdf), accessibility_check, doc_optimize,
  pdfa_convert/pdfa_verify (PDF/A-2b), batch convert,optimize. OCR reported unavailable (no models). Control channel
  and MCP were documented from the README, not exercised.
- 2026-11-04 (second round, PdfCraft 0.18.1): 71 tool ids run headless, each with the same field read before and
  after — 52 verified, 13 read-ok, 4 refused, 2 no-effect. Comment editing/replies/status/lock/delete, bookmark
  rename/page/style/move/delete, page labels/boxes/reverse/duplicate/replace/transitions, watermark, header/footer,
  background, Bates across files, protect/unprotect, redaction mark+apply, form properties and image
  fields, accessibility tags/autotag/fix/report, compare/report/mark, flatten, reduce, hidden info, initial view,
  Office and image export, measurements, links, attachments, Acrobat JavaScript, Fill & Sign text. The redaction
  audit was checked against a faux redaction (image over text): count 0 while the text stayed extractable.
- 2026-11-04 (third round, PdfCraft 0.18.2): CLI refreshed; the 80 tools not yet named run headless with before/after
  reads — 47 verified, 25 read-ok, 3 no-effect (view-only or other-OS tools), 2 refused for want of a sample (layers,
  XFA), 1 no GoToR link possible, 3 blocked (OCR models, 3D models). `content_copy` re-checked by hand after a weak first
  result. Recorded in `editing-signing-tools.md`.
