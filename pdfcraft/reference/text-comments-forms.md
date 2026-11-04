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
- `comment_list`, `comment_reply`, `comment_set_status`, `comment_delete` exist; **not run here**.
- `bookmark_add {"doc":1,"title":"Results","page":2}` → `info.bookmarks` 0 → 1; `bookmark` editing/removal not run.

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
- Other form tools exist (`form_add_field_table`, `form_set_props`, `form_tab_order`, `form_merge_data`,
  `form_set_script`, `form_reset`, `form_delete_field`) — **not run here**.
- **Saving:** `doc_save` has no `format` argument and overwrites an existing target. Saving a filled form PDF keeps
  the AcroForm and its values (qpdf: hasacroform true, 1 field); `flatten_fill_sign` bakes only Fill & Sign
  annotations (its docs say form fields stay), and did not strip the field in the 1-field test.

## Accessibility

`accessibility_check {"doc":1}` → `{passed:23, failed:3, manual:5, results:[{name, rule, status, findings}]}` on the
3-page sample. `accessibility_report`, `accessibility_fix`, `accessibility_autotag_apply`,
`accessibility_find_untagged` exist — **not run here**.
