# PdfCraft reference: pages and documents

Part of the pdfcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Scripted documents (first verified tasks, pdfcraft-cli 0.18.1, 2026-11-04)

A script is JSON lines (`{"tool":"doc_open","args":{…}}`); `run --script steps.json --root DIR --report` returns one
JSON document (`{ok, steps:[{step,tool,status,result}]}`). The session holds one document; open, work, save, close.

```json
[{"tool":"doc_open","args":{"path":"test3.pdf"}},
 {"tool":"text_find","args":{"doc":1,"query":"total due"}},
 {"tool":"comment_add","args":{"doc":1,"page":2,"type":"highlight","find":"total due","contents":"review","color":"#ffd400"}},
 {"tool":"bookmark_add","args":{"doc":1,"title":"Results","page":2}},
 {"tool":"doc_set_info","args":{"doc":1,"key":"Title","value":"Quarterly Report"}},
 {"tool":"doc_save","args":{"doc":1,"path":"annotated.pdf"}},
 {"tool":"doc_close","args":{"doc":1}}]
```

Verified results: `text_find` count 1 on page 2; `comment_add` made 1 annotation; `bookmark_add` 1 bookmark;
`doc_set_info {"key":"Title"}` set the saved file's title (`"title"` is ignored — keys are case-sensitive);
`doc_save` wrote 18,213 bytes; `info` of the result: annotations 1, bookmarks 1.

- `doc_open {"path"}` returns `{doc, pages, editable, encrypted, path,…}`; `doc_info {"doc":1}` adds fields, fonts,
  links, layers, open destinations; `doc_close {"doc":1}` → `{closed:1}`.
- `doc_save {"doc":1,"path":"x.pdf"}` (arguments: `doc, path, full, flatten_fill_sign`; there is no `format`).
  It writes to a new path (full rewrite) or over the document's own file (incremental update) and **does not refuse
  an existing file** — verified by rewriting an existing `annotated.pdf` (17,559 bytes). `flatten_fill_sign` bakes
  Fill & Sign text/marks/signatures and removes those annotations; form fields and comments stay editable.
- `doc_optimize {"doc":1,"path":"opt.pdf"}`: verified 18,701 → 18,205 bytes.
- `doc_set_info` also writes custom properties (any name without spaces/`/`/`#`); `doc_info` lists them under `custom`.

## Pages

`info` keys that matter: `pages`, `first_page_pt`, `fields`, `annotations`, `acroform_fields`, `bookmarks`, `title`,
`pdf_version`, `pdfa`, `pdfua`, `tagged`, `encrypted`, `warnings`.

CLI (each option runs in order, page numbers refer to the document after earlier options):

- `edit in.pdf --out out.pdf --rotate 1,3:90 --delete 2,4 --move 5:1 --insert-blank 1 [--title T --author A]`
- `extract in.pdf --pages 1,3,5-8 --out out.pdf` (order as given; verified 1,3 → 2 pages)
- `split in.pdf --every N | --before 3,7 [--out-dir DIR]` (verified `--every 1` → `test3-p1.pdf`, `-p2`, `-p3`)
- `combine a.pdf b.pdf … --out c.pdf` (verified 2+2 → 4 pages)

Script tools on an open document:

- `page_insert_blank {"doc":1,"at":1,"width":595,"height":842}` → pages 3→4 (blank page inserted at 1)
- `page_move {"doc":1,"pages":[2],"to":4}` — after it, `text` shows the blank page last: Two, Three, One
- `page_delete {"doc":1,"pages":[4]}`, `page_rotate {"doc":1,"degrees":90,"pages":[1]}`,
  `page_insert_file {"doc":1,"at":2,"path":"other.pdf"}` (add another PDF's pages; not run)
- `page_render {"doc":1,"page":2,"dpi":50}` renders in-session (no path); for a file use `render`.

Rotation has no field in `info`: verify by rendering — A4 at 50 dpi is 414×586, and 90° gives 586×414.

## Metadata, batch and checks

- `check FILE [--json out.json]` → per file `{status, pages, failed_pages, warnings}`; verified `{"ok":1}`.
- `audit FILE` → `{count, findings}`; verifies there are no faux redactions (it fails when found).
- `batch FILE --steps convert,optimize --out-dir DIR` → `{completed, failed, files:[{path,output,bytes,steps}]}`;
  verified one file: convert 19,444 → 19,444, optimize → 17,559 bytes, `failed:0`.
- `pdfa_verify {"doc":1,"level":"PDF/A-2b"}` → `{compliant:true, …}` on a converted file.

## Other document tools (named; not run here)

`doc_combine`, `doc_split`, `page_extract`, `doc_print`, `doc_protect` / `doc_unprotect`, `doc_audit_redactions`,
`redact_mark` / `redact_apply` / `redact_clear`, `link_add` / `link_list`, `attachment_add`, `measure_distance` /
`measure_export`, `ocr_recognize` / `ocr_status`, `doc_export_text`, `doc_export_images`, `page_add_text` /
`page_add_image`, `doc_batch`, `comment_list`, `bookmark_list`, `form_reset`. Their parameter docs come from
`pdfcraft-cli tools`; none of these was exercised in the first round.
