# PdfCraft reference: export, rendering and PDF/A

Part of the pdfcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Rendering (verified 0.18.1, 2026-11-04)

- `pdfcraft-cli render f.pdf --page N [--dpi 96] --out x.png` — PNG/JPG/TIF/PAM by extension.
  A4 at 50 dpi renders 414×586 px; after `edit --rotate 1:90` the same page renders 586×414 (the way to prove
  a rotation, since `info` has no rotation field).
- In a script, `page_render {"doc":1,"page":1,"dpi":50}` renders in-session: the result is
  `{bytes:9939, width:414, height:586, image:"png", hint:"pass --out file.png to save it"}` (no `path` argument).
  For a file, use the `render` subcommand (or `run page_render doc=1 page=2 --out x.png` while a document is open).
- `render` is the way to export a page picture; the CLI has no office-format converter.

## Optimize

`doc_optimize {"doc":1,"path":"opt.pdf"}` (Acrobat-style PDF Optimizer; `preset: "standard"|"mobile"` and options).
Verified on the 3-page sample: 18,701 → 18,205 bytes, same 3 pages, `info` otherwise unchanged.
`pdfcraft-cli batch f.pdf --steps convert,optimize --out-dir DIR` ran the same two steps on one file
(convert 19,444 → 19,444 bytes, optimize → 17,559) and reported `failed:0`.

## PDF/A

- `pdfa_convert {"doc":1}` → `{level:"PDF/A-2b", compliant:true, declared:{output_intents:["sRGB IEC61966-2.1"],
  pdfa:"PDF/A-2b", pdfua:null}, issues:[]}`; `doc_save` then writes the converted file, and
  `pdfcraft-cli info` reports `"pdfa": "PDF/A-2b"`.
- `pdfa_verify {"doc":1,"level":"PDF/A-2b"}` on the saved file → `{compliant:true, …}`.
- `pdfa_verify`/`pdfa_convert` cover what the engine can fix (XMP, output intent, forbidden actions/JS, encryption);
  fonts that are not embedded are reported as remaining issues — check `issues` rather than assuming compliance.

## Checks before handing a file over

- `check FILE` — engine round-trip and page sanity (`{"ok":1}` on the sample).
- `audit FILE` — faux-redaction scan; `{count:0, findings:[]}` means none found (exit status fails when found).
- `info` — pages, fields, annotations, bookmarks, `pdfa`, `tagged`, `encrypted`, `warnings`.
