# Learning log

- **2026-11-05 (0.17.2):** first round. Every id run headless in an isolated HOME with before/after read-backs
  (262 verified, 139 read-ok, 141 ran, 5 refused; three rows downgraded after review). Workflow recipes:
  half-letter facing document with parent footer and page numbers, styles + baseline grid + threads + wrap,
  table form grid, CMYK/spot swatches and tints, export matrix (PDF/X-4 valid, X-1a, PDF/A-2b, IDML round trip,
  EPUB, fixed EPUB, PPTX, HTML, PNG/JPG), CSV data merge, TOC/index/book. Live control on a hidden display and in
  a user-opened window (`script --connect`, `ui.screenshot`, `ui.render`). Worked exercise: a one-page training
  log form (half-letter) built live, PDF/X-4 validated after switching swatches from RGB to CMYK, plus a 2-up
  letter sheet made by placing the PDF twice.
