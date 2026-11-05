# PdfCraft reference: editing, images, signing, accessibility tags, automation

Part of the pdfcraft skill. The short front page is `../SKILL.md`. Third round, headless, **pdfcraft-cli 0.18.2**
(2026-11-04): each tool run in a script with the same field read before and after. "read-ok" = a read tool that
returned real data; tools that could not be exercised are listed at the end with the reason.

## Documents and revisions (verified)

- `doc_create {from:"blank", pages:2}` makes a new document in the session (`doc_inspect` lists its pages). Its first
  `doc_save` needs a `path` ("the document has never been saved: pass a path").
- `doc_create_multiple {paths:[a.pdf, pic.png], out}` combines PDFs and images into one file (3 pages + 1 image → 4).
- `doc_list` (open documents with doc/path/pages/dirty) and `doc_inspect {doc}` (page list with size and rotation): read-ok.
- `doc_audit_space {doc}` gives a byte breakdown per content kind; `doc_backdrops {doc}` lists pages that paint their own backdrop (read-ok).
- `doc_remove_marks {kind}` removes a watermark or header/footer added earlier (text re-read after save: gone).
- `doc_export_all_images {folder}` writes every image (`img_Page_1_Image_0001.png` …); `doc_export_data {path:"x.xfdf"}`
  exports form data (XFDF or CSV), `doc_import_data {path}` fills fields from it (read back with `form_fields`).
- `doc_revisions {doc}` counts incremental-save revisions (1 → 2 after an incremental save);
  `doc_open_revision {revision:1}` opens that older state as a new unsaved document (a marker added later was absent).
- `edit_undo` / `edit_redo {doc}` step the history (`content_list` 4 → 3 → 4 items).
- `standards_remove_id {standard:"pdfa"}` drops the PDF/A claim (`info` pdfa `PDF/A-2b` → null).

## Added content, page objects, images (verified)

- **`content_*` works only on items PdfCraft added** (`page_add_text`, `page_add_image`, Edit ▸ Add content), not on the
  page's original text: on a plain PDF `content_list` is empty and `content_copy` says "page 1 has no added item 1".
  `content_list {doc}` takes no page (all pages; items carry `page` and a 1-based `index` per page).
- `content_update {page, index, text, size, font, bold, italic, color, align, char_spacing, rect}` retypes/restyles;
  `content_copy {page, index, to_page[, to_doc, at]}` pastes a copy (same rect on page 3, count 1 → 2);
  `content_delete {page, index}` (count 4 → 3).
- `object_list {page}` lists page objects with rects and a `generation`; `object_move {page, objects:[{kind,index}], offset:[0,-20], generation}`
  moves them (rect y 73 → 53); a stale `generation` is refused, and the reply's bumped generation proves the move.
- `page_images {page}` (image numbers, pixels, placement rect) and `image_hit {page, point}` (images under a point): read-ok.
- `image_edit {page, image, action:"crop", rect}` sets an editor crop (`has_editor_crop` false → true, render changes);
  `image_save {page, image, path}` writes the image out as PNG.
- `stamp_custom {page, path:"logo.png", at:[x,y]}` (or `rect`) places an image stamp (render changes).
- `page_enhance_camera {page, mode:"greyscale"[, corners, level]}` cleans up a camera shot of a page (render turns grey).

## Editing original text (verified)

- `text_lines {page}`, `text_paragraphs {page}` (with `editor_text`), `text_styles` (font/size/lines/pages per style),
  `text_fonts {page}`, `text_edit_layout {paragraph, text}` (measures a draft before committing): read-ok.
- `text_edit {page, line:2, text:"Invoice total 9999"}` rewrites a line of the original text (re-read after save).
- `text_script {page, paragraph, range:[40,44], script:"superscript"}` turns characters into super/subscript.
  Digits work (`¹²⁰⁰`); **letters fail** — the bundled fallback font has no superscript letters.
- `text_font_files {directories:["."]}` finds font files, but **only inside `--root`** ("outside the allowed directory"):
  copy the TTF into the root. `text_font_import {path:"MyFont.ttf"}` then embeds it (`text_fonts` shows `PCFull0`).

## Bookmarks, links, actions, commands (verified)

- New in 0.18.2: `bookmark_copy {doc:2, from:1}` copies the outline from another open document (0 → 2 entries);
  `bookmark_export {doc}` returns the tree as JSON (`{bookmarks:[{title,page,open,view}]}`), and
  `bookmark_import {file:"bm.json"}` (or `bookmarks:[…]` inline; `replace`, `parent`, `position`) loads that shape back (0 → 2).
- `bookmark_from_structure` builds bookmarks from tagged **H/H1–H6** headings (autotag output is paragraphs only:
  retag a `P` to `H1` first); `bookmark_from_text_styles {levels:"Helvetica 12"}` builds them from a text style.
- `links_from_urls` turns typed URLs into links (0 → 2); `links_remove` deletes them (2 → 0).
- `action_list` names the built-in actions (Prepare for Distribution, Optimize Scanned Documents, Add Page Numbers,
  Mark as Confidential, Sanitize Documents); `action_run {action, paths, folder}` runs one over files into a folder.
- `command_list` lists the app's UI command registry (212 ids, the same ids as `ui commands` in the live app);
  `command_run {id:"page.rotate", params:{degrees:90}}` runs one headless (page 612×792 → 792×612);
  `command_batch {steps:[…]}` runs several (`completed`/`failed` counts).
- `js_set_document_script {name:"Helpers", script}` adds a document-level script; `js_document_scripts` lists them.

## Measurement, printing (verified / read-ok)

- `measure_area` / `measure_perimeter {page, points:[[x,y],…]}` add measurements (`measure_list` count 0 → 2 with values).
- `measure_snap {page, at, tolerance}` snaps to vector geometry (midpoint at distance 14 on a vector PDF); it finds
  **no segments on text or image pages**.
- `printers` lists print queues and `printer_options {printer}` their driver options — reading only; nothing was printed.
  `print_readiness {doc}` reports fonts not embedded, images, output intents, PDF/A issues.

## Signing (verified)

- `sign_id_create {name, password, path[, email, organization, unit, country, key, years]}` writes a self-signed `.p12`; the **password must be at least 8 characters**.
- `sign_document {doc, id:"id.p12", password, out[, page, rect, field, reason, location, certify, appearance]}` signs (`sign_list` 0 → 1, `/Sig` written, appearance shows
  "Digitally signed by …" with the date). `sign_trust {paths:["id.p12"]}` adds the certificate to the trusted list.
- `sign_keychain_ids` (macOS) and `sign_windows_ids` (Windows) return `count:0` on Linux without an error.

## Accessibility tags and review (verified)

- `accessibility_autotag_form_fields` tags form fields; `accessibility_tag_content {object}` lists the marked content
  (page, MCID, text) behind a tag.
- `accessibility_set_tag_property {object, generation, property:"title", value}`; `accessibility_set_alt {figure:14, alt}` — `figure`
  is the **PDF object number** from `accessibility_figures`, not a 1-based position.
- `accessibility_move_tag {object, generation, anchor, anchor_generation, placement:"after"}` reorders (8,14,15 → 8,15,14);
  `accessibility_mark_tag_artifact {object}` turns a tag into an artifact (tags 5 → 4).
- Review: `accessibility_review_record {before, after}` (JSON diff of two check runs), `accessibility_review_html` (report file),
  `accessibility_review_save {path, decisions:[{rule:"primary-language", decision:"accepted|needs_work|skipped"}]}` (rules must be
  names from `accessibility_check`), `accessibility_review_load {path}` (matched to the file by SHA-256).

## View and preview

- `render_preview {doc, page, max_side:200}` returns a small PNG payload (read-ok).
- `view_reading_colors {mode:"yellow-on-black"}` is a view setting only: the file is unchanged and a headless render
  does not show it.

## Not exercised (reason)

- `layer_set` — needs a PDF with optional-content layers ("the document has no layers").
- `xfa_to_static` — needs an XFA form. `link_open` — needs a GoToR (other-file) link; `link_add` makes only URL and GoTo links.
- `ocr_recognize_files` — OCR models not installed (`ocr_status` → `available:false`).
- `model_add` / `model_render` (new in 0.18.2, 3D annotations) — need a `.u3d` or `.prc` model.
