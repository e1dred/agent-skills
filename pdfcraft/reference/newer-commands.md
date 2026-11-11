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

## 0.21.0 (checked 2026-11-11, from 0.19.0; 0.20.0 not tested on its own)

`pdfcraft-cli tools` lists **208 tools** (195 in 0.19.0): 13 added, none removed, 48 descriptions or schemas changed. `--help` is unchanged, so diff `tools`, not `--help`. Two recipes (page edit, split) give the same page counts and renders on both CLIs.

### New tools (run with `run --script … --root DIR`, each read back)
- **`text_replace {"doc","find","replace", case_sensitive?, whole_words?}`** — Find and Replace inside the paragraph, keeping its fonts and rewrapping: "Beta sentence" → "Delta sentence" (`{replaced:1}`; `pdfcraft-cli text` confirms).
- `text_prepare {"doc","page"}` makes text inside Form XObjects editable (`{prepared_groups, refused_groups, repaired_fonts}`); `text_paragraphs` went from 0 to 1 paragraph.
- **Print production:** `doc_convert_colours {"doc","to":"gray"|"rgb"|"cmyk", preserve_black?}` (red → gray 76,76,76; no ICC profile, not a separation); `doc_fix_hairlines {"doc", narrower_than?, width?}` (two 0.1 pt strokes widened); `doc_printer_marks {"doc","trim","registration","color_bars","page_info","label","date"}` widens the page 36 pt a side (612×792 → 684×864); `doc_remove_marks {"kind":"printer_marks"}` removes the marks but the page stays enlarged.
- `object_copy {"doc","page","all":true}` / `object_paste {"doc","page"}` copy page objects, also into another open document (`{copied:2}`, `{pasted:2}`).
- `attachment_edit {"doc","name"|"key","description"}`; `comment_popup {"doc","page","index","open":true, rect?}`.
- Form scripts: `form_focus {"doc","field","event":"enter"|"exit"}` runs On Focus/On Blur (or XFA enter/exit) scripts; `js_event {"doc","field","event":"mouse_enter"|"mouse_exit"|"mouse_down"|"mouse_up"|"on_focus"|"on_blur"}` runs that widget action. Both returned `{changed:true}` and the field value the script set.
- `accessibility_layout_table_to_blocks {"doc","object","generation"}` turns a layout-only Table tag into Div/P tags (ids from `accessibility_tags`).
- `printer_papers {"printer":"default"}` lists a printer's paper sizes (empty with no printer driver).

### Changed tools that matter
- Colors: `page_add_text` and `content_update` take `gray` (level) or `cmyk` ([c,m,y,k]) instead of `color`; `content_list` reports them.
- `doc_optimize` gained `discard_external_refs`, `discard_form_actions`, `discard_search_index`, `target_bytes`.
- `doc_print` gained `area`, `cols`, `rows`, `creep` (booklets); `doc_batch` gained `dry_run`.
- `doc_combine` / `doc_create_multiple` accept Office files through an installed LibreOffice.
- `redact_mark` gained `regex` and `validate` (`luhn`, `mod97`, `iban`); `redact_apply` returns `save_as` (`…_Redacted`) and also removes metadata that repeats the removed text.
- `text_extract {format:"html"}`; `text_find {stop_at_limit}`.
- Forms: `form_fields` lists `on_widgets` for radio groups; `form_fill` takes `{"widget": n}`; `form_set_image {field_id}`; `form_set_props` rotation now turns the content inside the same rectangle (it used to swap the rectangle).
- Links: `link_add` / `link_edit {zoom: fit_page|fit_width|…|percentage}`; `link_list` returns `zoom` and `resolved_url`.
- `doc_info` returns `layer_order`, `portfolio`, `unreadable_objects`; `doc_open` accepts `#page=12`-style suffixes.
- `doc_export_office` now draws table borders only where the page draws them.
- `sign_document {run_form_scripts}`, `stamp_custom` text line with `{name}`, `{date}`, `{time}`, `object_move {all}`, `model_render {orbit}`, `js_run {answers, field_id}`, `image_edit {action:"ungroup"}`.
