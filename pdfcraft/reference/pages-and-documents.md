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

### Pages, labels and presentation (second round, verified 0.18.1, 2026-11-04)

- `page_number {"doc":1,"from":1,"to":3,"start":1,"style":"decimal"}` → page labels 1,2,3 (read them from `doc_info`).
- `page_set_box {"doc":1,"box":"crop","rect":[0,0,300,300],"pages":[1]}` → page 1 goes 595.92×842.88 pt → 300×300 pt.
- `page_reverse {"doc":1}` → page 1 becomes what was page 3; `page_duplicate {"pages":[1],"at":3}` → 3 → 4 pages;
  `page_replace {"pages":[1],"path":"other2.pdf","from_pages":[2]}` → page 1's text becomes the other file's page 2.
- `page_transition_set {"pages":[1],"style":"Dissolve","duration":1}` → `doc_info.transitions`
  `[{style:'Dissolve',duration:1.0,page:1}]`; style names are capitalised (`fade` is refused).
- `doc_watermark {"text":"DRAFT","opacity":0.2,"rotation":45,"pages":[1]}` → the watermark is **real page text**
  (page text ends 'DRAFT'); `doc_header_footer {"header_center":"Confidential","footer_center":"Page <<1>> of <<n>>",
  "pages":[1,2,3]}` → header and footer, where `<<1>>` is the page number and `<<n>>` the page count;
  `doc_background {"color":"#FFF2CC","pages":[1]}` → a page background (verify by rendering).
- `doc_initial_view {"display_title":true,"fit_window":true}` → `doc_info.initial_view` shows both set.
- `doc_close {"doc":1}` **refuses a document with unsaved changes**: save first, or pass `"discard_changes":true`.

## Documents: compare, flatten, reduce, hidden info, export (second round, verified)

- `doc_compare {"doc":1,"other":2}` compares two open PDFs → `{changes:[{kind:'inserted',new:{page:2,…}}]}`.
  `doc_compare_report {"doc":1,"other":2,"path":"compare.pdf"}` writes a report PDF (954 bytes);
  `doc_compare_mark` adds the differences as comments (`comment_list` 0 → 1).
- `doc_flatten {"doc":1,"comments":true,"fields":true}` → `info.annotations` becomes `[]` (baked into the page).
- `doc_reduce {"doc":1,"path":"reduced.pdf"}` (Acrobat Reduce File Size) → 21,499 → 18,259 bytes.
- `doc_hidden_info {"doc":1}` lists the categories Remove Hidden Information would drop (metadata 5, attachments 0,
  comments …); `doc_remove_hidden {"doc":1}` removes them and leaves the document dirty.
- `doc_export_office {"doc":1,"path":"out.docx"}` → a 2,393-byte Word file (PPTX/HTML by extension);
  `doc_export_images {"doc":1,"folder":"imgs","dpi":30}` → `test3_page_1..3.png`, and `doc_export_text` writes the
  plain text instead. The CLI `text` subcommand reads text without writing a file.

## Security, redaction and signing (second round, verified)

- `doc_protect {"doc":1,"open_password":"secret","permissions_password":"owner","printing":"none","changes":"none",
  "copy":false}` → opening without the password fails ("the document is protected by a password"); with it,
  `doc.encrypted` is true. `printing` is one of `none|low|high`.
- `doc_unprotect {"doc":1}` works only when the file has **no permissions restrictions**; the saved result opens
  with no password.
- `redact_mark {"doc":1,"page":2,"find":"total due"}` → `{marked:1, pages_marked:[2]}`; `redact_apply
  {"doc":1,"pages":[2]}` removes the text — page 2's extracted text loses the phrase.
- `doc_audit_redactions` / `audit` → `{count:0, findings:[]}` after a real redaction.
- **The redaction audit does not catch a faux redaction:** a black image over the text (`page_add_image`) leaves the
  words extractable with `pdftotext` and the scan still reports `{count:0}`. Only `redact_mark` + `redact_apply`
  removes text — check `text --page` afterwards.
- `sign_list {"doc":1}` → `{count:0, signed:0, all_valid:false}` when there are no signature fields.
- Fill & Sign: `fill_sign_add {"doc":1,"page":1,"type":"text","at":[50,100],"text":"Approved"}` → a FreeText
  annotation with contents 'Approved'; `fill_sign_date_format {"format":"dd.mm.yyyy","language":"en"}` sets the
  date pattern (default m/d/yyyy). Signatures themselves were not exercised.

## Links, attachments, measurement, JavaScript (second round, verified)

- `link_add {"doc":1,"page":1,"rect":[50,600,150,620],"url":"https://example.com"}` → `link_list` 0 → 1 link.
  Address links by the `index` from `link_list`: `link_edit {"page":1,"index":2,"url":…}` changed example.net →
  example.org; `link_delete {"page":1,"index":1}` → 2 → 1 links.
- `attachment_add {"doc":1,"path":"stamp.png","name":"stamp.png"}` → attachments `[{name,size:296}]`;
  `attachment_delete {"name":"stamp.png"}` → `[]`.
- `measure_info {"doc":1,"page":1,"points":[[50,50],[250,50]],"type":"distance"}` → `{label:'2.78 in',
  length:2.7778, angle:0}` without adding an annotation; `measure_distance {…,"label":"Wall A"}` adds one;
  `measure_scale {"at":[50,50],"distance":100,"unit":"mm","page_distance":100,"page_unit":"pt"}` sets the ratio;
  `measure_export {"out":"measures.csv"}` writes the measurements (row 'Wall A', 2.7778 in).
- `js_enabled` → `{enabled:true}`, and `js_run {"script":"app.alert('hello')"}` → `{alerts:[{message:'hello',
  icon:'error'}],…}` — this is Acrobat JavaScript, not page script.
- `doc_bates_multi {"files":[{"input":…,"output":…},…],"prefix":"ABC-","start_number":1,"digits":4}` numbers one
  continuous sequence across files (3-page file ends ABC-0001; the next starts ABC-0004). `dry_run` first returns the ranges.
- `ocr_status` → `{available:false, search_dirs:[…]}` and `ocr_recognize` refuses ("the text recognition models are
  not installed"); OCR is unusable on this machine.

## Metadata, batch and checks

- `check FILE [--json out.json]` → per file `{status, pages, failed_pages, warnings}`; verified `{"ok":1}`.
- `audit FILE` → `{count, findings}`; verifies there are no faux redactions (it fails when found).
- `batch FILE --steps convert,optimize --out-dir DIR` → `{completed, failed, files:[{path,output,bytes,steps}]}`;
  verified one file: convert 19,444 → 19,444, optimize → 17,559 bytes, `failed:0`.
- `pdfa_verify {"doc":1,"level":"PDF/A-2b"}` → `{compliant:true, …}` on a converted file.

## Other document tools (named; not run here)

`doc_combine`, `doc_split`, `page_extract`, `doc_print`, `page_add_text`, `doc_batch`, `form_reset`,
`redact_clear`, `comment_image_preview` beyond its refusal. Their parameter docs come from
`pdfcraft-cli tools`.
