# PdfCraft reference: newer commands

Part of the pdfcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## 0.18.1 (first look, 2026-11-04)

First version covered by this skill. `pdfcraft-cli tools` lists **184 tools**; there is no changelog in the
repository root, so this file starts here. Commands verified so far are named in the other reference files;
anything there marked "not run here" has not been checked in this round.

## 0.18.2 (checked 2026-11-04)

`pdfcraft-cli tools` lists **189 tools** (184 before). New: `bookmark_copy`, `bookmark_export`, `bookmark_import`
(verified, see `editing-signing-tools.md`), `model_add`, `model_render` (3D annotations; not run, no .u3d/.prc model).
`doc_optimize`: mono JBIG2 now packs up to 16 images into one shared symbol dictionary (description change only).
Twelve earlier recipes (rotate, extract, combine, split, find, comment, bookmark, form fill, metadata, watermark,
page numbers, reduce) gave identical output on 0.18.1 and 0.18.2 (info, text, render checksums).

## 0.19.0 (checked 2026-11-06)

`pdfcraft-cli tools` lists **195 tools** (189 in 0.18.2): 6 added, none removed, 7 with changed schemas or descriptions.
A scripted round (create a 3-page PDF, add text, save, reopen, rotate, comment, extract, combine, split, optimise,
save, then `info`, `text`, `render`, `check`) gave identical renders, text and qpdf-normalised structure on both
versions; only the random annotation `/NM` and trailer `/ID` differ, and `comment_list` rows now carry
`opacity`, `fill_opacity`, `text_opacity` and `border_shape`.

New tools:
- `ocr_words {"doc":1,"engine":"tesseract","retain_review":true}` → per page `{words:[{text,box,confidence,band,engine,suspect}], mean_confidence, already_on_page}`, plus `review` (a number). On an image-only page bearing one word: `Beta`, confidence 96.8, band `high`, box `[145.4,149.8,46.8,17.3]`.
- `ocr_review_apply {"doc":1,"review":1,"corrections":[{"page":1,"word":1,"text":"Betta"}]}` → `{applied:1,review:1}`; `text_extract` then returned `Betta` (it said `Beta` before). The `review` number comes from `ocr_words retain_review`; without it the tool refuses with "missing argument review".
- `ocr_dictionary {"path":"ocr-dictionary-en.txt","add":["Beta","Gamma"]}` → `{count:2, path, words:["beta","gamma"]}`; read back with the same path and no `add`/`remove`. The file name must match `ocr-dictionary-<language>.txt` or it is refused.
- `comments_copy {"doc":1,"comments":[[1,1]]}` → `{comments:1, xfdf:"<?xml …<annots><text page=\"0\" rect=\"50,722,70,742\" …"}`; `comments_paste {"doc":1,"page":2,"xfdf":…}` put the copy on page 2 (`comment_list` went from 1 comment to 2, one per page).
- `page_enhance_scan {"doc":1}` (ran) → `{images:1, pages_cleaned:[1], not_scanned:[], skipped:[], undo:"Enhance scanned file"}`; the pages are rewritten in place, no render comparison was made.

Changed tools:
- `ocr_recognize` / `ocr_recognize_files` take `engine` (auto|ocrs|tesseract), `strategy`, `force_ocr`, `auto_rotate`, `binarize`, `denoise`, `deskew`, `region`, `output_mode`, `out` and `skip_text_files`. With `engine:"tesseract"` an image-only page gets its text as invisible text (`pages[0].text` "Beta", `words:1`), and `ocr_recognize_files` wrote a searchable copy into the folder (`recognized:1`, `text` then returned "Beta").
- `comment_add` and `comment_edit` take `fill_opacity`, `text_opacity`, `border_shape` (`oval`/`circle` for text boxes) and (add only) `ortho`; `comment_edit` addresses a comment by `page` + `index`, not a `comment` pair. A text box created at fill 0.3 / text 0.5 / oval read back 0.8 / 0.2 / circle after the edit.
- `redact_mark` accepts `pattern:"iban"` (new value beside phone, email, credit-card, ssn, date). On a page with `IBAN DE89370400440532013000`, `text_find "DE89"` found 1 match before and 0 after `redact_apply`.
- `fill_sign_add` takes `border`, `border_color` and `border_shape` for typed text (accepted; `comment_list` does not report the border back, only the FreeText rect).

Worth knowing when driving OCR from a shell:
- The default `engine` is `auto`, which picks **ocrs**, whose model files are absent from a hand-extracted CLI: it reports `skipped` with 0 words rather than an error. Pass `engine:"tesseract"` (a system tesseract on PATH) and set `PDFCRAFT_MODELS` only if you really have the ocrs models.
- `ocr_status` now reports one entry per engine with `available` and the reason, plus its search dirs — read it before trusting a recognition result.
