# PdfCraft command catalogue (0.19.0)

Built 2026-11-06 from the skill's own text (SKILL.md, reference/ and tools/); no command was run and nothing was re-tested. Ids come from `pdfcraft-cli` 0.19.0 (195 ids); the skill's version label: last tested on PdfCraft 0.19.0; evidence sections cite 0.18.1-0.19.0.
Status: **V** verified - the hit is under a heading naming verification or records an observed result (arrow, before/after, read-back, checked file, confirmed); **d** documented - named with parameters or usage, no recorded evidence; **n** named only - a bare list or command index; **s** skipped on purpose - the skill says skipped/not run/not tested/not exercised; **x** known no-op, broken or refused - the line says so; **V+** verified, but another line records a limit (refused or skipped in some state or version); the note quotes both. When a command has verified evidence anywhere, it counts as verified: a refusal or skip recorded elsewhere usually names a precondition or an older round.
Counts: V 166, V+ 3, d 7, n 2, s 16, x 1.
These tool names have no dot; they are grouped by the part before the first underscore (the one without an underscore is in `other`).

## accessibility (18)

| id | status | note |
|---|---|---|
| `accessibility_autotag_apply` | x | reference/text-comments-forms.md#Accessibility: `accessibility_autotag_apply` refused on a Chromium-prin… |
| `accessibility_autotag_form_fields` | V | reference/editing-signing-tools.md#Accessibility tags and …: - `accessibility_autotag_form_fields` tags … |
| `accessibility_autotag_preview` | V | reference/text-comments-forms.md#Accessibility: `accessibility_autotag_preview {"page":1}` → candidates … |
| `accessibility_check` | V | reference/editing-signing-tools.md#Accessibility tags and …: names from `accessibility_check`), `accessi… |
| `accessibility_figures` | V | reference/editing-signing-tools.md#Accessibility tags and …: …ber from `accessibility_figures`, not a 1… |
| `accessibility_find_untagged` | V | reference/text-comments-forms.md#Accessibility: …ures:[]}`; `accessibility_find_untagged` → `{failed:1, p… |
| `accessibility_fix` | d | reference/text-comments-forms.md#Accessibility: `accessibility_fix {"rule":"title","value":"…"}` |
| `accessibility_mark_tag_artifact` | V | reference/editing-signing-tools.md#Accessibility tags and …: `accessibility_mark_tag_artifact {object}` … |
| `accessibility_move_tag` | V | reference/editing-signing-tools.md#Accessibility tags and …: - `accessibility_move_tag {object, generati… |
| `accessibility_report` | V | reference/text-comments-forms.md#Accessibility: …ew value); `accessibility_report {"path":"a11y.html"}` |
| `accessibility_review_html` | V | reference/editing-signing-tools.md#Accessibility tags and …: …eck runs), `accessibility_review_html` (rep… |
| `accessibility_review_load` | V | reference/editing-signing-tools.md#Accessibility tags and …: …y_check`), `accessibility_review_load {path… |
| `accessibility_review_record` | V | reference/editing-signing-tools.md#Accessibility tags and …: - Review: `accessibility_review_record {bef… |
| `accessibility_review_save` | V | reference/editing-signing-tools.md#Accessibility tags and …: `accessibility_review_save {path, decisions… |
| `accessibility_set_alt` | V | reference/editing-signing-tools.md#Accessibility tags and …: `accessibility_set_alt {figure:14, alt}` — … |
| `accessibility_set_tag_property` | V | reference/editing-signing-tools.md#Accessibility tags and …: - `accessibility_set_tag_property {object, … |
| `accessibility_tag_content` | V | reference/editing-signing-tools.md#Accessibility tags and …: `accessibility_tag_content {object}` lists … |
| `accessibility_tags` | V | reference/text-comments-forms.md#Accessibility: …verified): `accessibility_tags` → `{count:0, tags:[]}` o… |

## action (2)

| id | status | note |
|---|---|---|
| `action_list` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: - `action_list` names the built-in actions … |
| `action_run` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `action_run {action, paths, folder}` runs o… |

## attachment (2)

| id | status | note |
|---|---|---|
| `attachment_add` | V | reference/pages-and-documents.md#Links, attachments, measu…: - `attachment_add {"doc":1,"path":"stamp.pn… |
| `attachment_delete` | V | reference/pages-and-documents.md#Links, attachments, measu…: `attachment_delete {"name":"stamp.png"}` → … |

## bookmark (12)

| id | status | note |
|---|---|---|
| `bookmark_add` | V | reference/pages-and-documents.md#Scripted documents (first…: {"tool":"bookmark_add","args":{"doc":1,"tit… |
| `bookmark_copy` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: …in 0.18.2: `bookmark_copy {doc:2, from:1}` … |
| `bookmark_delete` | V | reference/text-comments-forms.md#Bookmark tools (second ro…: - `bookmark_delete {"path":[2]}` → 2 entrie… |
| `bookmark_export` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `bookmark_export {doc}` returns the tree as… |
| `bookmark_from_structure` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: - `bookmark_from_structure` builds bookmark… |
| `bookmark_from_text_styles` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `bookmark_from_text_styles {levels:"Helveti… |
| `bookmark_import` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `bookmark_import {file:"bm.json"}` (or `boo… |
| `bookmark_list` | V | reference/text-comments-forms.md#Bookmark tools (second ro…: `bookmark_list {"doc":1}` lists them with t… |
| `bookmark_move` | V | reference/text-comments-forms.md#Bookmark tools (second ro…: - `bookmark_move {"path":[2],"position":0}`… |
| `bookmark_rename` | V | reference/text-comments-forms.md#Bookmark tools (second ro…: - `bookmark_rename {"path":[1],"title":"Fin… |
| `bookmark_set_page` | V | reference/text-comments-forms.md#Bookmark tools (second ro…: - `bookmark_set_page {"path":[1],"page":3}`… |
| `bookmark_set_style` | V | reference/text-comments-forms.md#Bookmark tools (second ro…: - `bookmark_set_style {"path":[1],"bold":tr… |

## command (3)

| id | status | note |
|---|---|---|
| `command_batch` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `command_batch {steps:[…]}` runs several (`… |
| `command_list` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: - `command_list` lists the app's UI command… |
| `command_run` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `command_run {id:"page.rotate", params:{deg… |

## comment (9)

| id | status | note |
|---|---|---|
| `comment_add` | V | reference/pages-and-documents.md#Scripted documents (first…: {"tool":"comment_add","args":{"doc":1,"page… |
| `comment_delete` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comment_delete {}` → `comment_list` coun… |
| `comment_edit` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comment_edit {"contents":"edited note"}`… |
| `comment_image_preview` | V+ | reference/text-comments-forms.md#Comment tools (second rou…: - `comment_image_preview` refuses ("choose … · limit: pages-and-documents.md: …ct_clear`, `comment_image_preview` beyond its refusal. |
| `comment_list` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): …on page 2 (`comment_list` went from 1 comment t… |
| `comment_lock` | V | reference/text-comments-forms.md#Comment tools (second rou…: `comment_lock {"locked":true}` → locked fal… |
| `comment_mark` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comment_mark {"marked":true}` → marked f… |
| `comment_reply` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comment_reply {"text":"thanks, fixed"}` … |
| `comment_set_status` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comment_set_status {"status":"completed"… |

## comments (4)

| id | status | note |
|---|---|---|
| `comments_copy` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): - `comments_copy {"doc":1,"comments":[[1,1]]}` … |
| `comments_hide` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comments_hide {"hidden":true}` returns `… |
| `comments_paste` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): …42\" …"}`; `comments_paste {"doc":1,"page":2,"x… |
| `comments_summarize` | V | reference/text-comments-forms.md#Comment tools (second rou…: - `comments_summarize {"doc":1,"out":"comme… |

## content (4)

| id | status | note |
|---|---|---|
| `content_copy` | V | reference/editing-signing-tools.md#Added content, page obj…: … empty and `content_copy` says "page 1 has … |
| `content_delete` | V | reference/editing-signing-tools.md#Added content, page obj…: `content_delete {page, index}` (count 4 → 3… |
| `content_list` | V | reference/editing-signing-tools.md#Documents and revisions…: …e history (`content_list` 4 → 3 → 4 items). |
| `content_update` | V | reference/editing-signing-tools.md#Added content, page obj…: - `content_update {page, index, text, size,… |

## doc (40)

| id | status | note |
|---|---|---|
| `doc_audit_redactions` | V | reference/pages-and-documents.md#Security, redaction and s…: - `doc_audit_redactions` / `audit` → `{coun… |
| `doc_audit_space` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_audit_space {doc}` gives a byte brea… |
| `doc_backdrops` | V | reference/editing-signing-tools.md#Documents and revisions…: `doc_backdrops {doc}` lists pages that pain… |
| `doc_background` | V | reference/pages-and-documents.md#Pages, labels and present…: `doc_background {"color":"#FFF2CC","pages":… |
| `doc_batch` | s | reference/pages-and-documents.md#Other document tools (nam…: …add_text`, `doc_batch`, `form_reset`, |
| `doc_bates_multi` | V | reference/pages-and-documents.md#Links, attachments, measu…: - `doc_bates_multi {"files":[{"input":…,"ou… |
| `doc_close` | V | SKILL.md#CLI essentials (verified): …oc_save` → `doc_close`. |
| `doc_combine` | s | reference/pages-and-documents.md#Other document tools (nam…: `doc_combine`, `doc_split`, `page_extract`,… |
| `doc_compare` | V | reference/pages-and-documents.md#Documents: compare, flatt…: - `doc_compare {"doc":1,"other":2}` compare… |
| `doc_compare_mark` | V | reference/pages-and-documents.md#Documents: compare, flatt…: `doc_compare_mark` adds the differences as … |
| `doc_compare_report` | V | reference/pages-and-documents.md#Documents: compare, flatt…: `doc_compare_report {"doc":1,"other":2,"pat… |
| `doc_create` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_create {from:"blank", pages:2}` make… |
| `doc_create_multiple` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_create_multiple {paths:[a.pdf, pic.p… |
| `doc_export_all_images` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_export_all_images {folder}` writes e… |
| `doc_export_data` | V | reference/editing-signing-tools.md#Documents and revisions…: `doc_export_data {path:"x.xfdf"}` |
| `doc_export_images` | V | reference/pages-and-documents.md#Documents: compare, flatt…: `doc_export_images {"doc":1,"folder":"imgs"… |
| `doc_export_office` | V | reference/pages-and-documents.md#Documents: compare, flatt…: - `doc_export_office {"doc":1,"path":"out.d… |
| `doc_export_text` | V | reference/pages-and-documents.md#Documents: compare, flatt…: ….png`, and `doc_export_text` writes the |
| `doc_flatten` | V | reference/pages-and-documents.md#Documents: compare, flatt…: - `doc_flatten {"doc":1,"comments":true,"fi… |
| `doc_header_footer` | V | reference/pages-and-documents.md#Pages, labels and present…: `doc_header_footer {"header_center":"Confid… |
| `doc_hidden_info` | V | reference/pages-and-documents.md#Documents: compare, flatt…: - `doc_hidden_info {"doc":1}` lists the cat… |
| `doc_import_data` | V | reference/editing-signing-tools.md#Documents and revisions…: …F or CSV), `doc_import_data {path}` fills f… |
| `doc_info` | V | reference/pages-and-documents.md#Scripted documents (first…: `doc_info {"doc":1}` adds fields, fonts, |
| `doc_initial_view` | V | reference/pages-and-documents.md#Pages, labels and present…: - `doc_initial_view {"display_title":true,"… |
| `doc_inspect` | V | reference/editing-signing-tools.md#Documents and revisions…: …e session (`doc_inspect` lists its pages). |
| `doc_list` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_list` (open documents with doc/path/… |
| `doc_open` | V | SKILL.md#CLI essentials (verified): …e session: `doc_open` → tools with `doc` = its id → `doc_save` → `do… |
| `doc_open_revision` | V | reference/editing-signing-tools.md#Documents and revisions…: `doc_open_revision {revision:1}` opens that… |
| `doc_optimize` | V | reference/log.md#Log: …lity_check, doc_optimize, |
| `doc_print` | s | reference/pages-and-documents.md#Other document tools (nam…: …_extract`, `doc_print`, `page_add_text`, `d… |
| `doc_protect` | V | reference/pages-and-documents.md#Security, redaction and s…: - `doc_protect {"doc":1,"open_password":"se… |
| `doc_reduce` | V | reference/pages-and-documents.md#Documents: compare, flatt…: - `doc_reduce {"doc":1,"path":"reduced.pdf"… |
| `doc_remove_hidden` | V | reference/pages-and-documents.md#Documents: compare, flatt…: `doc_remove_hidden {"doc":1}` removes them … |
| `doc_remove_marks` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_remove_marks {kind}` removes a water… |
| `doc_revisions` | V | reference/editing-signing-tools.md#Documents and revisions…: - `doc_revisions {doc}` counts incremental-… |
| `doc_save` | V | SKILL.md#CLI essentials (verified): …= its id → `doc_save` → `doc_close`. |
| `doc_set_info` | V | reference/pages-and-documents.md#Scripted documents (first…: {"tool":"doc_set_info","args":{"doc":1,"key… |
| `doc_split` | s | reference/pages-and-documents.md#Other document tools (nam…: …_combine`, `doc_split`, `page_extract`, `do… |
| `doc_unprotect` | V | reference/pages-and-documents.md#Security, redaction and s…: - `doc_unprotect {"doc":1}` works only when… |
| `doc_watermark` | V | reference/pages-and-documents.md#Pages, labels and present…: - `doc_watermark {"text":"DRAFT","opacity":… |

## edit (2)

| id | status | note |
|---|---|---|
| `edit_redo` | V | reference/editing-signing-tools.md#Documents and revisions…: …it_undo` / `edit_redo {doc}` step the histo… |
| `edit_undo` | V | reference/editing-signing-tools.md#Documents and revisions…: - `edit_undo` / `edit_redo {doc}` step the … |

## fill (2)

| id | status | note |
|---|---|---|
| `fill_sign_add` | V | reference/pages-and-documents.md#Security, redaction and s…: …ll & Sign: `fill_sign_add {"doc":1,"page":1… |
| `fill_sign_date_format` | V | reference/pages-and-documents.md#Security, redaction and s…: `fill_sign_date_format {"format":"dd.mm.yyy… |

## form (15)

| id | status | note |
|---|---|---|
| `form_actions` | V | reference/text-comments-forms.md#Form authoring in depth (…: - `form_actions {"field":"full_name"}` → `{… |
| `form_add_field` | V | reference/log.md#Log: form_add_field/form_fields/form_fill (saved AcroForm verified with qpdf), accessib… |
| `form_add_field_table` | d | reference/text-comments-forms.md#Forms: …ols exist (`form_add_field_table`, `form_tab_order`, `form_merge… |
| `form_calculation_order` | V | reference/text-comments-forms.md#Form authoring in depth (…: …thing, and `form_calculation_order` refuses… |
| `form_delete_field` | s | reference/text-comments-forms.md#Forms: …rm_reset`, `form_delete_field`) — not run here. |
| `form_detect_fields` | V | reference/text-comments-forms.md#Form authoring in depth (…: - `form_detect_fields {"doc":1}` returned `… |
| `form_fields` | V | reference/editing-signing-tools.md#Documents and revisions…: … back with `form_fields`). |
| `form_fill` | V | reference/log.md#Log: …form_fields/form_fill (saved AcroForm verified with qpdf), accessibility_check, do… |
| `form_merge_data` | n | reference/text-comments-forms.md#Forms: …ab_order`, `form_merge_data`, |
| `form_reset` | s | reference/pages-and-documents.md#Other document tools (nam…: …oc_batch`, `form_reset`, |
| `form_set_actions` | V | reference/text-comments-forms.md#Form authoring in depth (…: `form_set_actions` with an empty list |
| `form_set_image` | V | reference/text-comments-forms.md#Form authoring in depth (…: `form_set_image {"field":"photo","path":"st… |
| `form_set_props` | V | reference/text-comments-forms.md#Form authoring in depth (…: - `form_set_props {"doc":1,"field":"full_na… |
| `form_set_script` | s | reference/text-comments-forms.md#Forms: `form_set_script`, `form_reset`, `form_delete_field`) — not ru… |
| `form_tab_order` | n | reference/text-comments-forms.md#Forms: …ld_table`, `form_tab_order`, `form_merge_data`, |

## image (3)

| id | status | note |
|---|---|---|
| `image_edit` | V | reference/editing-signing-tools.md#Added content, page obj…: - `image_edit {page, image, action:"crop", … |
| `image_hit` | V | reference/editing-signing-tools.md#Added content, page obj…: … rect) and `image_hit {page, point}` (image… |
| `image_save` | V | reference/editing-signing-tools.md#Added content, page obj…: `image_save {page, image, path}` writes the… |

## js (4)

| id | status | note |
|---|---|---|
| `js_document_scripts` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `js_document_scripts` lists them. |
| `js_enabled` | V | reference/pages-and-documents.md#Links, attachments, measu…: - `js_enabled` → `{enabled:true}`, and `js_… |
| `js_run` | V | reference/pages-and-documents.md#Links, attachments, measu…: …rue}`, and `js_run {"script":"app.alert('he… |
| `js_set_document_script` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: - `js_set_document_script {name:"Helpers", … |

## layer (1)

| id | status | note |
|---|---|---|
| `layer_set` | s | reference/editing-signing-tools.md#Not exercised (reason): - `layer_set` — needs a PDF with optional-con… |

## link (5)

| id | status | note |
|---|---|---|
| `link_add` | V+ | reference/pages-and-documents.md#Links, attachments, measu…: - `link_add {"doc":1,"page":1,"rect":[50,60… · limit: editing-signing-tools.md: `link_add` makes only URL and GoTo links. |
| `link_delete` | V | reference/pages-and-documents.md#Links, attachments, measu…: `link_delete {"page":1,"index":1}` → 2 → 1 … |
| `link_edit` | V | reference/pages-and-documents.md#Links, attachments, measu…: …ink_list`: `link_edit {"page":1,"index":2,"… |
| `link_list` | V | reference/pages-and-documents.md#Links, attachments, measu…: …e.com"}` → `link_list` 0 → 1 link. |
| `link_open` | s | reference/editing-signing-tools.md#Not exercised (reason): `link_open` — needs a GoToR (other-file) link |

## links (2)

| id | status | note |
|---|---|---|
| `links_from_urls` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: - `links_from_urls` turns typed URLs into l… |
| `links_remove` | V | reference/editing-signing-tools.md#Bookmarks, links, actio…: `links_remove` deletes them (2 → 0). |

## measure (8)

| id | status | note |
|---|---|---|
| `measure_area` | V | reference/editing-signing-tools.md#Measurement, printing (…: - `measure_area` / `measure_perimeter {page… |
| `measure_distance` | V | reference/pages-and-documents.md#Links, attachments, measu…: …nnotation; `measure_distance {…,"label":"Wa… |
| `measure_export` | V | reference/pages-and-documents.md#Links, attachments, measu…: `measure_export {"out":"measures.csv"}` wri… |
| `measure_info` | V | reference/pages-and-documents.md#Links, attachments, measu…: - `measure_info {"doc":1,"page":1,"points":… |
| `measure_list` | V | reference/editing-signing-tools.md#Measurement, printing (…: …surements (`measure_list` count 0 → 2 with … |
| `measure_perimeter` | V | reference/editing-signing-tools.md#Measurement, printing (…: …re_area` / `measure_perimeter {page, points… |
| `measure_scale` | V | reference/pages-and-documents.md#Links, attachments, measu…: `measure_scale {"at":[50,50],"distance":100… |
| `measure_snap` | V | reference/editing-signing-tools.md#Measurement, printing (…: - `measure_snap {page, at, tolerance}` snap… |

## model (2)

| id | status | note |
|---|---|---|
| `model_add` | s | reference/editing-signing-tools.md#Not exercised (reason): - `model_add` / `model_render` (new in 0.18.2… |
| `model_render` | s | reference/editing-signing-tools.md#Not exercised (reason): …del_add` / `model_render` (new in 0.18.2, 3D … |

## object (2)

| id | status | note |
|---|---|---|
| `object_list` | V | reference/editing-signing-tools.md#Added content, page obj…: - `object_list {page}` lists page objects w… |
| `object_move` | V | reference/editing-signing-tools.md#Added content, page obj…: `object_move {page, objects:[{kind,index}],… |

## ocr (6)

| id | status | note |
|---|---|---|
| `ocr_dictionary` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): - `ocr_dictionary {"path":"ocr-dictionary-en.tx… |
| `ocr_recognize` | V | reference/pages-and-documents.md#Links, attachments, measu…: …:[…]}` and `ocr_recognize` refuses ("the te… |
| `ocr_recognize_files` | s | reference/editing-signing-tools.md#Not exercised (reason): - `ocr_recognize_files` — OCR models not inst… |
| `ocr_review_apply` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): - `ocr_review_apply {"doc":1,"review":1,"correc… |
| `ocr_status` | V | reference/editing-signing-tools.md#Not exercised (reason): …installed (`ocr_status` → `available:false`). |
| `ocr_words` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): - `ocr_words {"doc":1,"engine":"tesseract","ret… |

## other (1)

| id | status | note |
|---|---|---|
| `printers` | V | reference/editing-signing-tools.md#Measurement, printing (…: - `printers` lists print queues and `printe… |

## page (18)

| id | status | note |
|---|---|---|
| `page_add_image` | V | reference/editing-signing-tools.md#Added content, page obj…: …add_text`, `page_add_image`, Edit ▸ Add con… |
| `page_add_text` | V+ | reference/editing-signing-tools.md#Added content, page obj…: …t added (`page_add_text`, `page_add_image… · limit: pages-and-documents.md: …oc_print`, `page_add_text`, `doc_batch`, `form_reset`, |
| `page_delete` | d | reference/pages-and-documents.md#Pages: - `page_delete {"doc":1,"pages":[4]}`, `page_rotate {"doc":1,"de… |
| `page_duplicate` | V | reference/pages-and-documents.md#Pages, labels and present…: `page_duplicate {"pages":[1],"at":3}` → 3 →… |
| `page_enhance_camera` | V | reference/editing-signing-tools.md#Added content, page obj…: - `page_enhance_camera {page, mode:"greysca… |
| `page_enhance_scan` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): - `page_enhance_scan {"doc":1}` (ran) → `{image… |
| `page_extract` | s | reference/pages-and-documents.md#Other document tools (nam…: …oc_split`, `page_extract`, `doc_print`, `pa… |
| `page_images` | V | reference/editing-signing-tools.md#Added content, page obj…: - `page_images {page}` (image numbers, pixe… |
| `page_insert_blank` | V | reference/pages-and-documents.md#Pages: - `page_insert_blank {"doc":1,"at":1,"width":595,"height":842}` … |
| `page_insert_file` | s | reference/pages-and-documents.md#Pages: `page_insert_file {"doc":1,"at":2,"path":"other.pdf"}` (add anot… |
| `page_move` | d | reference/pages-and-documents.md#Pages: - `page_move {"doc":1,"pages":[2],"to":4}` — after it, `text` sh… |
| `page_number` | V | reference/pages-and-documents.md#Pages, labels and present…: - `page_number {"doc":1,"from":1,"to":3,"st… |
| `page_render` | V | SKILL.md#CLI essentials (verified): `page_render` has |
| `page_replace` | V | reference/pages-and-documents.md#Pages, labels and present…: `page_replace {"pages":[1],"path":"other2.p… |
| `page_reverse` | V | reference/pages-and-documents.md#Pages, labels and present…: - `page_reverse {"doc":1}` → page 1 becomes… |
| `page_rotate` | d | reference/pages-and-documents.md#Pages: …es":[4]}`, `page_rotate {"doc":1,"degrees":90,"pages":[1]}`, |
| `page_set_box` | V | reference/pages-and-documents.md#Pages, labels and present…: - `page_set_box {"doc":1,"box":"crop","rect… |
| `page_transition_set` | V | reference/pages-and-documents.md#Pages, labels and present…: - `page_transition_set {"pages":[1],"style"… |

## pdfa (2)

| id | status | note |
|---|---|---|
| `pdfa_convert` | V | reference/export-and-pdfa.md#PDF/A: - `pdfa_convert {"doc":1}` → `{level:"PDF/A-2b", compliant:true, dec… |
| `pdfa_verify` | V | reference/export-and-pdfa.md#PDF/A: - `pdfa_verify {"doc":1,"level":"PDF/A-2b"}` on the saved file → `{c… |

## print (1)

| id | status | note |
|---|---|---|
| `print_readiness` | V | reference/editing-signing-tools.md#Measurement, printing (…: `print_readiness {doc}` reports fonts not e… |

## printer (1)

| id | status | note |
|---|---|---|
| `printer_options` | V | reference/editing-signing-tools.md#Measurement, printing (…: …queues and `printer_options {printer}` thei… |

## redact (3)

| id | status | note |
|---|---|---|
| `redact_apply` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): …nd 0 after `redact_apply`. |
| `redact_clear` | s | reference/pages-and-documents.md#Other document tools (nam…: `redact_clear`, `comment_image_preview` bey… |
| `redact_mark` | V | reference/pages-and-documents.md#Security, redaction and s…: - `redact_mark {"doc":1,"page":2,"find":"to… |

## render (1)

| id | status | note |
|---|---|---|
| `render_preview` | d | reference/editing-signing-tools.md#View and preview: - `render_preview {doc, page, max_side:200}` return… |

## sign (6)

| id | status | note |
|---|---|---|
| `sign_document` | V | reference/editing-signing-tools.md#Signing (verified): - `sign_document {doc, id:"id.p12", password, out… |
| `sign_id_create` | V | reference/editing-signing-tools.md#Signing (verified): - `sign_id_create {name, password, path[, email, … |
| `sign_keychain_ids` | V | reference/editing-signing-tools.md#Signing (verified): - `sign_keychain_ids` (macOS) and `sign_windows_i… |
| `sign_list` | V | reference/editing-signing-tools.md#Signing (verified): …]}` signs (`sign_list` 0 → 1, `/Sig` written, app… |
| `sign_trust` | V | reference/editing-signing-tools.md#Signing (verified): `sign_trust {paths:["id.p12"]}` adds the certific… |
| `sign_windows_ids` | V | reference/editing-signing-tools.md#Signing (verified): …macOS) and `sign_windows_ids` (Windows) return `c… |

## stamp (1)

| id | status | note |
|---|---|---|
| `stamp_custom` | V | reference/editing-signing-tools.md#Added content, page obj…: - `stamp_custom {page, path:"logo.png", at:… |

## standards (1)

| id | status | note |
|---|---|---|
| `standards_remove_id` | V | reference/editing-signing-tools.md#Documents and revisions…: - `standards_remove_id {standard:"pdfa"}` d… |

## text (12)

| id | status | note |
|---|---|---|
| `text_edit` | V | reference/editing-signing-tools.md#Editing original text (…: - `text_edit {page, line:2, text:"Invoice t… |
| `text_edit_layout` | V | reference/editing-signing-tools.md#Editing original text (…: …s {page}`, `text_edit_layout {paragraph, te… |
| `text_extract` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): …eview:1}`; `text_extract` then returned `Betta`… |
| `text_find` | V | reference/newer-commands.md#0.19.0 (checked 2026-11-06): …32013000`, `text_find "DE89"` found 1 match bef… |
| `text_font_files` | V | reference/editing-signing-tools.md#Editing original text (…: - `text_font_files {directories:["."]}` fin… |
| `text_font_import` | V | reference/editing-signing-tools.md#Editing original text (…: `text_font_import {path:"MyFont.ttf"}` then… |
| `text_fonts` | V | reference/editing-signing-tools.md#Editing original text (…: `text_fonts {page}`, `text_edit_layout {par… |
| `text_lines` | V | reference/editing-signing-tools.md#Editing original text (…: - `text_lines {page}`, `text_paragraphs {pa… |
| `text_paragraphs` | V | reference/editing-signing-tools.md#Editing original text (…: …s {page}`, `text_paragraphs {page}` (with `… |
| `text_script` | V | reference/editing-signing-tools.md#Editing original text (…: - `text_script {page, paragraph, range:[40,… |
| `text_styles` | V | reference/editing-signing-tools.md#Editing original text (…: …or_text`), `text_styles` (font/size/lines/p… |
| `text_word_count` | V | reference/text-comments-forms.md#Text and search (verified…: - `text_word_count {"doc":1}` → per page `{… |

## view (1)

| id | status | note |
|---|---|---|
| `view_reading_colors` | d | reference/editing-signing-tools.md#View and preview: - `view_reading_colors {mode:"yellow-on-black"}` is… |

## xfa (1)

| id | status | note |
|---|---|---|
| `xfa_to_static` | s | reference/editing-signing-tools.md#Not exercised (reason): - `xfa_to_static` — needs an XFA form. |
