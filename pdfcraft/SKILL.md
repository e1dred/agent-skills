---
name: pdfcraft
description: Use when reading, editing, combining, splitting, annotating or securing PDFs, filling forms, rendering pages, exporting PDF/A, when running pdfcraft-cli, or when connecting to the PdfCraft app (storytold) on this machine
---

# PdfCraft

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

Field notes from first headless tasks, last tested on **PdfCraft 0.18.1** (Linux AppImage). PdfCraft is an
early-alpha PDF editor in Rust: viewing, page organizing, comments, forms, redaction, PDF/A. Every ribbon action
is an engine *tool*; the CLI, the MCP server and the app's control channel run the same tools. If
`pdfcraft-cli --version` is newer, re-check anything here before relying on it.

## Setup

- **CLI:** extract it from the AppImage (`pdfcraft.appimage --appimage-extract`, copy `usr/bin/pdfcraft-cli`
  somewhere stable); self-contained, no window. Never run `--version` on the AppImage itself.
- **Headless tools:** `pdfcraft-cli run <tool> key=value … --root DIR [--out x.png]`, or a script:
  `pdfcraft-cli run --script steps.json --root DIR --report` (JSON lines `{"tool":"doc_open","args":{…}}`).
- **Subcommands:** `info`, `text`, `render`, `edit`, `combine`, `extract`, `split`, `check`, `audit`, `batch`, `tools`.
- **Live app:** `pdfcraft --control ~/.pdfcraft-control.json` writes a random token to that file and listens on
  loopback only; drive it with `pdfcraft-cli ui --control FILE inspect|click|key|command|drag|screenshot|quit …`.
  Keep the control file in a private folder (never /tmp).
- **MCP:** opt-in, stdio only: `pdfcraft-cli mcp --root DIR` (`--compact` for a short list), with optional
  `--automation-read-root` / `--automation-write-root`.

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a tool id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `pages-and-documents.md` | Opening/saving in scripts, info fields, page insert/move/delete/rotate, extract, split, combine, metadata, batch, check, audit; page labels/boxes/transitions, watermark/header/footer, compare, flatten, reduce, protection, redaction, links, attachments, measurement, Bates, JavaScript, export | Scripted documents; Pages; Pages, labels and presentation; Documents: compare, flatten, reduce, hidden info, export; Security, redaction and signing; Links, attachments, measurement, JavaScript; Metadata, batch and checks; Other document tools |
| `text-comments-forms.md` | Extracting and searching text, word counts, comments and bookmarks, form authoring and filling, accessibility | Text and search; Comments and bookmarks; Form authoring in depth; Accessibility |
| `export-and-pdfa.md` | Page rendering, optimize, PDF/A convert and verify, output choices | Rendering; Optimize; PDF/A; Checks before handing a file over |
| `newer-commands.md` | What each version added or changed | 0.18.1 |
| `log.md` | Dated log of what was tested when | Log |

## CLI essentials (verified)

```
pdfcraft-cli info f.pdf                       # pages, fields, annotations, title, pdfa, pdf_version, warnings
pdfcraft-cli text f.pdf --page 2              # extracted text (pages split by form feeds)
pdfcraft-cli render f.pdf --page 1 --dpi 50 --out p1.png
pdfcraft-cli edit f.pdf --out e.pdf --rotate 1:90 --delete 2 --insert-blank 1   # options run in order
pdfcraft-cli combine a.pdf b.pdf --out c.pdf
pdfcraft-cli extract f.pdf --pages 1,3 --out x.pdf
pdfcraft-cli split f.pdf --every 1 --out-dir out/        # f-p1.pdf, f-p2.pdf, …
pdfcraft-cli check f.pdf [--json out.json]; pdfcraft-cli audit f.pdf
pdfcraft-cli batch f.pdf --steps convert,optimize --out-dir out/
pdfcraft-cli run --script steps.json --root DIR --report
```

- Scripts are one session: `doc_open` → tools with `doc` = its id → `doc_save` → `doc_close`. `page_render` has
  no path; use the `render` subcommand for files (or `run page_render doc=1 page=2 --out x.png` with a doc open).
- `doc_save` takes `{doc, path, full, flatten_fill_sign}` — there is **no `format`** argument. It writes to a new path
  or over the document's own file (incremental, atomic) and does not refuse an existing file. A PDF with form fields
  keeps its AcroForm on save; `flatten_fill_sign` bakes Fill & Sign annotations and removes them, form fields stay.

## Traps

- **Tools are not command ids:** `pdfcraft-cli tools` prints JSON (184 tools with `input_schema`); `run` takes
  `name=value` pairs. An unknown argument is refused by name.
- **`doc_set_info` keys are case-sensitive:** `{"key":"Title"}` sets the title; `"title"` is silently ignored.
- **`doc_save` has no `format` argument and overwrites without asking** (verified: it rewrote an existing
  `annotated.pdf`). Form fields survive a save (qpdf: hasacroform true); `flatten_fill_sign` only bakes Fill & Sign
  annotations — it did not strip form fields in the 1-field test.
- **The MCP server cannot read /tmp paths** (`OpenFile failed (code 80)`); the CLI can. Keep test files under a
  readable root or use the CLI.
- **OCR is not bundled here:** `ocr_status` → `available:false` (no model files in its search dirs).
- `info` has no page-rotation field; prove a rotation by the rendered size (A4 at 50 dpi: 414×586 → 586×414).
- **The redaction audit misses a faux redaction:** a black image over text (`page_add_image`) left it extractable
  while `audit` still returned `{count:0}`. Only `redact_mark` + `redact_apply` removes text — check `text --page` after.
- **Bookmarks are addressed by an integer `path`** (`[1]` = first top-level entry) and comment tools by `page` plus
  the 1-based `index` from `comment_list`. Bookmark colour is `[r,g,b]` 0..1; `page_transition_set` style names are
  capitalised ("Dissolve", not "fade").
- **`doc_close` refuses a document with unsaved changes** — save, or pass `"discard_changes":true`.
- **`form_detect_fields` finds blanks on printed forms, not AcroForm fields** — use `form_fields` for those.
  `doc_protect`'s `printing` is `none|low|high`, and a permissions password blocks `doc_unprotect`.

## Verify before reporting

`info` for page count/fields/pdfa, `text --page` for content, and `render` a page to look at. `check` round-trips
through the engine; `audit` scans for faux redactions but did not catch an image laid over text, so check the page
text after redacting. For form work, read the field values back with `form_fields`
(or qpdf's AcroForm JSON), never only the fill result.
