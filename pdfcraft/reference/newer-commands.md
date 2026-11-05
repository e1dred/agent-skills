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
