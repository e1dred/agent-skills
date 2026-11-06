# Learning log

- **2026-11-05 (0.17.2):** first round. Every id run headless in an isolated HOME with before/after read-backs
  (262 verified, 139 read-ok, 141 ran, 5 refused; three rows downgraded after review). Workflow recipes:
  half-letter facing document with parent footer and page numbers, styles + baseline grid + threads + wrap,
  table form grid, CMYK/spot swatches and tints, export matrix (PDF/X-4 valid, X-1a, PDF/A-2b, IDML round trip,
  EPUB, fixed EPUB, PPTX, HTML, PNG/JPG), CSV data merge, TOC/index/book. Live control on a hidden display and in
  a user-opened window (`script --connect`, `ui.screenshot`, `ui.render`). Worked exercise: a one-page training
  log form (half-letter) built live, PDF/X-4 validated after switching swatches from RGB to CMYK, plus a 2-up
  letter sheet made by placing the PDF twice.
- 2026-11-05 evening: live methods and dialogs tested on a private display (DeepSeek task D, screenshots reviewed): all ui.* input methods, ui.dialog.* (documentSetup, paragraphStyleOptions, insertTable), app.open/quit, selection commands; found 187 live-only commands and that live file.close/app.quit discard changes silently.
- 2026-11-05 evening: second headless round (DeepSeek task C, reviewed: 11-row sample, parent page size and unknown-key behaviour re-run here): 138 of 141 `ran` rows and all 5 refusals now verified/read-ok (402/142/3/0). Parent pages take the numeric spread id; effects/fitting read back from document.json or IDML. Corrected the old trap: unknown top-level keys are refused, only keys inside nested objects (stroke, border, margins) are ignored.
