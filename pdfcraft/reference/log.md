# PdfCraft reference: log

Part of the pdfcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-11-04: first verified run (PdfCraft 0.18.1, Linux AppImage): CLI extracted from the AppImage; 184 tools listed.
  Headless, read back each time: info/text/render, edit rotate/delete, extract/split/combine, audit/check,
  script doc_open→text_find→comment_add→bookmark_add→doc_set_info→doc_save→doc_close, page_insert_blank/page_move,
  form_add_field/form_fields/form_fill (saved AcroForm verified with qpdf), accessibility_check, doc_optimize,
  pdfa_convert/pdfa_verify (PDF/A-2b), batch convert,optimize. OCR reported unavailable (no models). Control channel
  and MCP were documented from the README, not exercised.
