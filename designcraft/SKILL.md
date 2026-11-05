---
name: designcraft
description: Use when laying out pages for print or screen — magazines, books, booklets, flyers, forms, planners, logs, templates with parent/master pages, threaded text, paragraph/character/table/cell styles, tables, swatches, TOC, index, data merge — when exporting PDF/X-4, PDF/X-1a, PDF/A, IDML, EPUB, PPTX or HTML, when opening IDML or InDesign .indd files, when running designcraft-cli, or when connecting to the DesignCraft app (storytold) on this machine
---

# DesignCraft

Field notes from the first full round, last tested on **DesignCraft 0.17.2** (Linux binary `designcraft-cli`).
DesignCraft is a pre-alpha, InDesign-like page layout app written in Rust; the CLI, the MCP server and the app's
control channel run the same 547 engine commands. If `designcraft-cli --version` reports a newer build, re-check
the ids and params here before relying on them (see `reference/newer-commands.md`).

## Setup

- **CLI:** `~/AppImages/designcraft-cli` (self-contained; `run`, `script`, `validate-pdf`, `thumbnail` open no
  window). Never launch the `.appimage` unless the user asks for the window or has opened it.
- **Headless batch:** `designcraft-cli script FILE [--in F | --sample] [--save OUT.designcraft] [--export OUT]
  [--keep-going]`, one `command.id {json}` per line, `"$N.field"` = result of step N (0-based, every command line
  counts). Generate long scripts from a small program that tracks step numbers.
- **Render to look at it:** `designcraft-cli run --in F --scale 2 --all-pages DIR` (options bind to the export
  *after* them; `--page` is 0-based).
- **Parameters:** `designcraft-cli describe ID` is the only reference; `commands` prints a JSON array.
- **Live app:** `designcraft --control PORT`, then `designcraft-cli app --port PORT CMD '{json}'`,
  `--method ui.inspect|ui.screenshot|ui.render`, or `script FILE --connect PORT`. No auth, localhost only.
- **Isolate state in tests:** `HOME`, `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, `XDG_CACHE_HOME` to a scratch folder.
- Paths shown as `/scratch/…` in the reference files were scratch files in the test run: use any absolute path.

## Traps (each cost a failed run)

- **Unknown parameter names are silently ignored.** Verify the effect (`document.inspect`, `type.selectionAttrs`,
  `table.get`, a render), never the exit code.
- **Most commands act on the selection.** "nothing selected" → `selection.set {ids:["$N.id"]}`; text formatting
  needs `text.select {story, anchor:0, focus:99999}` or `text.selectStory {frame}`. Full error → setup list in
  `reference/cli.md`.
- **Print colours must be CMYK.** `swatch.create {color:"#rrggbb"}` is RGB and makes PDF/X-4 fail
  `validate-pdf` ("RGB fills or strokes … needs an ICC profile"). Use `{c,m,y,k}` or convert with
  `swatch.options {name, color:{c,m,y,k}}`, re-export, re-validate.
- **Table header rows:** `table.convertFromText` makes no header row and returns `{rows, table}` without `story`
  (use the text frame's story). `table.options {headerRows:1}` alone did not draw the header cell style:
  apply it with `style.cell.apply {story, table, name, rows:[0,0], cols:[0,last]}`. Merging concatenates text.
- **Page numbers** are the special character `` in a text frame on the parent spread
  (`frame.create {spread:{kind:"parent", index:0}, …}`); there is no "Page Number" variable.
- **Tints** cannot be made as tint swatches: pass `tint` (0–1) on `object.fill`, `table.setCell`, `altRows`,
  `type.char {fillTint}`.
- **`facingPages` defaults to true**: a 4-page document is spreads 1 | 2-3 | 4. Pass `facingPages:false` when you
  address `spread:N` per page.
- **Small text-in-ellipse frames draw no text.** Use a graphic ellipse plus a separate centred text frame.
- **Dialogs and file choosers** open on the user's screen: always pass explicit paths (save/export/place/open).

## Verify before reporting

Render pages and look at them; for print PDFs run `designcraft-cli validate-pdf FILE` (`issues: []` = PDF/X pass;
it has no PDF/A check), read `file.exportPdf`'s `warnings`, and `pdfinfo -box` / `pdffonts` when available.

## Where things are

| File in `reference/` | Read it for |
|---|---|
| `cli.md` | subcommands, script syntax and `$N` refs, read-backs, test isolation, **error → setup recipes** for ~45 errors (selection, story, table, notes, xref, hyperlinks, libraries, books, layers, swatch groups, place cursor, clipboard) |
| `layout-tables.md` | new document, parent pages + page numbers (``), paragraph/character styles, baseline grid (`gridAlign`), threaded frames, text wrap, tables (`table.convertFromText`, `table.merge`, `table.setCell`, `style.cell.*`, `style.table.*`, `altRows`), a worked form layout, bundled fonts |
| `color-export.md` | swatches (CMYK, spot, tints), `file.exportPdf` (PDF/X-4, X-1a, PDF/A-2b, bleed, marks), `validate-pdf`, IDML / EPUB / fixed EPUB / PPTX / HTML / PNG / JPG export, 2-up sheets with `place.load` + `place.drop` |
| `data-toc-book.md` | data merge (`data.source.select`, `data.placeholder.add`, `data.merge`), `toc.generate`, `index.*`, books (`book.new`, `book.add`, `book.paginate`, `book.exportPdf`) |
| `live-app.md` | `--control`, `app --method`, `script --connect`, `ui.*` methods, MCP tools and roots, hidden-display recipe, building a page in a window the user opened |
| `command-catalogue.md` | all 547 ids with status (verified / read-ok / ran / refused), params doc and evidence |
| `newer-commands.md` | what changed between versions |
| `log.md` | dated learning log |

## Known gaps (0.17.2)

`layout.parentPageSize` / `layout.selectParentPage` refuse every parent id form; `font.replace` and
`color.loadProfile` need real fonts/ICC files; `file.print` needs a printer; object effects (drop shadow, bevel,
satin) and fitting options have no read-back; no PDF/X-3 or joboptions; fixed EPUB is page images; tables do not
draw anchored objects in cells. Check the repo's `docs/gaps.md` for the current list.
