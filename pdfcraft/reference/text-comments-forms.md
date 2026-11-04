# PdfCraft reference: text, comments, forms, accessibility

Part of the pdfcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Text and search (verified 0.18.1, 2026-11-04)

- `pdfcraft-cli text f.pdf [--page N]` — the extracted text; pages are separated by form feeds.
- `text_extract {"doc":1,"pages":[2,3]}` — per-page text in-session; `rect` narrows to a rectangle.
- `text_find {"doc":1,"query":"total due"}` → `{count:1, matches:[{page:2, rects:[[x0,y0,x1,y1]], text:"total due"}]}`
  (page is 1-based; rects feed comments/redaction).
- `text_word_count {"doc":1}` → per page `{characters, characters_without_spaces, words}`; verified pages 1–3:
  0 / 12 / 5 words on a 3-page sample (the first page held only a heading).

## Comments and bookmarks

- `comment_add {"doc":1,"page":2,"type":"highlight","find":"total due","contents":"review","color":"#ffd400"}`
  → `{comment:{id,index,lines,page}}`; the saved file's `info.annotations` went 0 → 1.
  Anchors can be `find` (a text search), `rect`, `quads`, `points`/`path` (ink), or `at`. `type:"highlight"` was
  verified; the other annotation kinds (underline, sticky note, ink, stamps…) were not run.
- `bookmark_add {"doc":1,"title":"Results","page":2}` → `info.bookmarks` 0 → 1.

### Comment tools (second round, verified 0.18.1, 2026-11-04)

Every comment tool takes `doc`, `page` and the **1-based `index` from `comment_list {"doc":1,"page":2}`**:

- `comment_edit {"contents":"edited note"}` → contents 'note one' → 'edited note'.
- `comment_reply {"text":"thanks, fixed"}` → replies `[]` → `[{contents:'thanks, fixed', type:'Text'}]`.
- `comment_set_status {"status":"completed"}` → status null → 'Completed' (stored capitalised).
- `comment_mark {"marked":true}` → marked false → true; `comment_lock {"locked":true}` → locked false → true.
- `comment_delete {}` → `comment_list` count 1 → 0 (removes the thread).
- `comments_summarize {"doc":1,"out":"comments.md"}` → a one-page summary of the comments (915 bytes).
- `comment_image_preview` refuses ("choose an image signature or initials") unless the comment is an image signature.
- `comments_hide {"hidden":true}` returns `{hidden:true}`, but `comment_list` has no hidden field — the change cannot be read back.

### Bookmark tools (second round, verified)

A bookmark is addressed by `path`, an **integer array** (`[1]` = the first top-level entry), not by title;
`bookmark_list {"doc":1}` lists them with their titles and target pages:

- `bookmark_rename {"path":[1],"title":"Findings"}` → title 'Results' → 'Findings'.
- `bookmark_set_page {"path":[1],"page":3}` → page 2 → 3.
- `bookmark_set_style {"path":[1],"bold":true,"color":[1,0,0]}` → the saved outline object gains `/C [1 0 0]` and
  `/F 2`; colour is `[r,g,b]` with values 0..1.
- `bookmark_move {"path":[2],"position":0}` → order Results, Appendix → Appendix, Results.
- `bookmark_delete {"path":[2]}` → 2 entries → 1.

## Forms

Authoring an AcroForm in a PDF (verified):

```json
{"tool":"form_add_field","args":{"doc":1,"page":1,"name":"full_name","type":"text","rect":[50,600,200,20],"caption":"Full name"}}
```

- `form_add_field` → `{field:"full_name"}`; `form_fields {"doc":1}` → `{count:1, fields:[{name, type:"text",
  page:1, rect:[50.0,20.0,200.0,600.0], value:null, read_only:false}]}`.
  **The rect is reported as PDF corners (bottom-left origin)**, not as the `[x,y,w,h]` passed in: the same field came
  back as `[50,20,200,600]`. Read `form_fields` back instead of assuming the stored rect.
- `form_fill {"doc":1,"values":{"full_name":"Ada Example"}}` → `{filled:1}`; `form_fields` then shows
  `value:"Ada Example"`; saved `gaps_filled.pdf` has `info.acroform_fields` 1.
- Other form tools exist (`form_add_field_table`, `form_tab_order`, `form_merge_data`,
  `form_set_script`, `form_reset`, `form_delete_field`) — **not run here**.
- **Saving:** `doc_save` has no `format` argument and overwrites an existing target. Saving a filled form PDF keeps
  the AcroForm and its values (qpdf: hasacroform true, 1 field); `flatten_fill_sign` bakes only Fill & Sign
  annotations (its docs say form fields stay), and did not strip the field in the 1-field test.

### Form authoring in depth (second round, verified)

- `form_set_props {"doc":1,"field":"full_name","read_only":true,"required":true,"tooltip":"Your full name"}` →
  `form_fields` shows `read_only:true, required:true, tooltip:'Your full name'` (all three were false/empty).
- `form_add_field {"page":1,"name":"photo","type":"image","rect":[50,700,150,780]}` → an image field is stored as
  a **button widget**; `form_set_image {"field":"photo","path":"stamp.png"}` then puts the picture in it — the saved
  widget carries `/MK {/I: <image XObject>}`.
- `form_actions {"field":"full_name"}` → `{actions:[], field:'full_name'}`; `form_set_actions` with an empty list
  changes nothing, and `form_calculation_order` refuses ("full_name has no calculation") until a field is calculated.
- `form_detect_fields {"doc":1}` returned `{fields: []}` even on a PDF that already had a form field: it finds the
  blanks in a **printed, non-interactive** form, not AcroForm fields. Use `form_fields` for those.

## Accessibility

`accessibility_check {"doc":1}` → `{passed:23, failed:3, manual:5, results:[{name, rule, status, findings}]}` on the
3-page sample.

Second round (verified): `accessibility_tags` → `{count:0, tags:[]}` on an untagged PDF; `accessibility_figures` →
`{count:0, figures:[]}`; `accessibility_find_untagged` → `{failed:1, passed:2, results:[…]}`;
`accessibility_autotag_preview {"page":1}` → candidates with bbox, bold and font size, while
`accessibility_autotag_apply` refused on a Chromium-printed PDF ("page 1: unsupported or painted operator") —
expect it to refuse on some producers, so check the tags afterwards. `accessibility_fix {"rule":"title","value":"…"}`
sets the document title (doc_info title 'print.html' → the new value); `accessibility_report {"path":"a11y.html"}`
writes the HTML report (5,272 bytes, 23 passed / 3 failed / 5 manual).
