# Changelog

All notable changes to this repository. Dates are the commit dates; the repo has no version numbers, so entries are grouped by day.
Each skill also labels, section by section, which app version a section was tested on (`> Versions:` lines): this file only summarises.
Format follows [Keep a Changelog](https://keepachangelog.com/) (Added, Changed, Fixed, Known gaps).

## Unreleased

### Added
- WordCraft: recipe and traps from reformatting a real document with review comments (table header shading and column widths, links in cells, landscape appendix, comment anchors).
- README table: CadCraft row (55 of 441 command ids named, an upper bound because its ids are plain words; everyday estimate ~20% from one task), refreshed counts for the other apps; `coverage.sh` now measures CadCraft too.
- Gap round (2026-10-26): PhotoCraft layer order/visibility/merge down, stroke, gradient fill, copy/paste, undo scope, hue/saturation, smart sharpen; DeckCraft alignment, redo and textBox rect units; CadCraft erase/qsave; WordCraft `layout.section` and per-section orientation. `everyday.sh` + `everyday/*.txt`: measured everyday-task checklists (replace the flat 85% estimate); all five now 100%.
- WordCraft: bullet-toggle trap (`para.bullets` toggles; call it on the first item only), editing a table cell in a reviewed document, and a memo built from a script.
- CadCraft round 12: two more AutoCAD DWGs: a parametric imperial part (constraints are not imported; imperial-to-metric scaling updates measurements but not dimension text) and a dynamic ISO title block (visibility-state switching verified in renders).
- CadCraft round 11: `saveas` in every DWG/DXF version (R2000/R2004 turn multileaders into leaders plus text), binary DXF, dynamic-block authoring ruled out (no commands), procedure for a future CadCraft release.
- CadCraft round 10: a real AutoCAD DWG (1380 entities, layout with 4 viewports, 36 multileaders, 28 dimensions, dynamic block) opened, queried, edited and rendered; dynamic-block reference commands verified; how to check for a newer CadCraft release.
- CadCraft round 9: a real drawing opened in the live window (copy for edits), `find_text` uses `contains`, selecting in dense drawings via `select {window}`, never save inspected files.
- CadCraft round 8: annotative text across viewport scales (checked in the PDF), editing a real drawing copy, basic 3D commands.
- CadCraft round 7: block editor and in-place reference editing, attribute manager, block replace, plot-style tables (.ctb, effect checked in the PDF), publish, more dimension tools.
- CadCraft round 6 (live window): screenshots, drawing by command_line + ui_click, click and window selection, repeat-last-command trap, snap/ortho not applied to clicks, panels and dialogs not drivable.
- CadCraft rounds 4 and 5: rich text, plot/export options, xref attach, mleader/table styles, scale list, dimbreak, hatchedit, splinedit, tiled viewports, autoconstrain, and an end-to-end floor-plan recipe with viewport-scale and annotation-height traps.
- CadCraft rounds 2 and 3 (0.13.0, headless plus live bridge): dimensions, hatch/gradient, blocks and attributes, layouts/viewports/PDF plot, trim/extend/fillet/stretch/arrays, properties and queries, DWG round trip, `.scr`, tables, data extraction, overkill, regions, mline, tolerance, constraints; `tools/ccrun.py` helper (many commands per run, JSON results); traps (handles renumber, `{last}` twice, `command_line` vs `script` take `text`).
- **CadCraft skill** (first version, from a real wiring-schematic task): headless `cadcraft-cli` (run, export PDF/DXF), layers and linetypes, readable text style, drawing schematics from primitives, the live MCP bridge and its limits; `tools/schem.py` helper, `tools/ccmcp.py` bridge client, and an invented example.
- **Craft apps, further rounds (2026-10-25):** WordCraft (character effects, paragraph helpers, find, content-control actions, file/privacy/versions/export/print commands, labels and envelopes), GridCraft (formula auditing, selection helpers, undo/redo, scripts and recording, ink, objects, comments, grouping, print helpers), DeckCraft (character formats, text movement, edit/arrange helpers, audio options, slide navigation, render and save-to-data commands), PhotoCraft (image auto adjustments and modes, measurement and notes, selection tools, brush state, actions editing, timeline, type styles, layer-style defaults).
- **Stage play format** (kind `stageplay`): common US playwright submission layout in WordCraft and ONLYOFFICE (title page, characters page, centred cues, italic directions, acts and scenes, title-and-number header), plain-text input, Times or Courier, and `stageplay_check.py`.
- **Manuscript format** (`styles/`, kind `manuscript`): standard manuscript layout for publisher and agent submissions in WordCraft and ONLYOFFICE (title page, running header from page 2, double-spaced 12 pt, chapter drops, scene breaks), your own text through `--text=`, Times or Courier, novel or short-story layout, A4 or Letter, and `manuscript_check.py` to verify a file. Gallery image and a WordCraft skill section.
- **Manuscript extras:** verse, block quotations and footnotes in the plain-text input, page count and words per page in `manuscript_check.py`, a **query letter** kind (`query`) and a **synopsis** kind (`synopsis`).
- **Screenplay extras:** scene numbers, bold/underlined scene headings, bold/underline/centred text, dual dialogue, TV act markers (TEASER, ACT ONE, END OF ACT), Fountain title-page keys, `screenplay_paginate.py` (adds `(MORE)` and `(CONT'D)` at page breaks), and `screenplay_export.py` (Fountain and Final Draft `.fdx` output).
- **Screenplay format** (kind `screenplay`): standard spec-script layout in WordCraft and ONLYOFFICE (Courier 12 pt on a 12 pt pitch, element indents, title page as its own section, numbering from 1 with `2.` `3.` at the top right), Fountain-like plain-text input with automatic `(CONT'D)`, and `screenplay_check.py`.

## 2026-10-25

Tested on: PhotoCraft 0.15.1 and 0.16.0, GridCraft 0.11.1 and 0.12.1, DeckCraft 0.10.0 and 0.11.1, WordCraft 0.10.0 and 0.11.0, ONLYOFFICE Desktop Editors 10.0.0 (flatpak).

### Added
- **GridCraft and DeckCraft skills**, first versions: headless CLI, live control channel, formulas, pivots, charts, themes, animations, exports.
- **Document styles** (`styles/`): eight looks (traditional, elegant, clean, professional, academic, modern, stylish, creative) as document, résumé, CV and APA/MLA paper for WordCraft and ONLYOFFICE; font resolver, A4/Letter, ATS lint (`ats_check.py`), gallery.
- **Tools:** `check-versions.sh` (app vs CLI versions), `coverage.sh` (commands documented per skill), PhotoCraft bridge helper (`pcmcp.py`), ONLYOFFICE schema helper (`ooschema.py`).
- **PhotoCraft 0.16.0:** paths and channels; brushes, presets, mixer brush, symmetry; all 65 filters of the main families plus the 47 Filter Gallery filters; layer comps, history and snapshots, smart filters; every layer style and all 16 adjustment layers; type (character and paragraph styles, OpenType, warp, convert), transforms and warps, swatches (ASE/ACO), smart-object commands, vector masks, video layers, guides, colour samplers, proofing, preferences; layer management, clipboard and paste variants, colour profiles, and the export family (artboards, comps, layers, presets, LUT, Illustrator, file scripts).
- **GridCraft 0.12.1:** pivots in depth (fields, calculated fields, show-as, filters, grouping, collapse, pivot charts), all chart types and chart editing, 12 conditional-format types, validation types and `data.validate`, every remaining Analysis ToolPak tool, threaded comments, protection and edit ranges, 40 functions, cell styles and themes, table design, slicers, shapes and pictures, sheet/view/formula helpers.
- **DeckCraft 0.11.1:** all 45 SmartArt layouts, the animation and transition catalogues, master and layout editing, shapes and freeform points, text and paragraph formatting, table cell commands, photo album, action buttons, slide zoom, sections, notes and handout masters, picture effects, file properties and templates.
- **WordCraft 0.11.0:** style management and the Design tab, index and TOC behaviour, equations, tracked changes by author and one at a time, tables in depth (styles, nested tables), outline view, building blocks, pictures and shapes.
- **ONLYOFFICE 10.0.0:** conditional formats, autofilter, pivot, chart and slide tools; the remaining tools documented (93 of 93 named); macro workflows (revisions, comments, watermark, protected ranges, chart formatting, transitions); **audit: all 93 tools called, 91 passing** (section "Tool audit" in the skill).
- README: measured ("commands documented") and estimated ("everyday workflows") coverage columns, with their definitions.

### Changed
- Every skill section now carries a `> Versions:` line (tested on / re-run on / not re-run). Headless sections were re-run on both the old and the new CLI where one existed (identical results, except the default chart text tint in DeckCraft 0.11.1).
- PhotoCraft live bridge: needs the matching CLI; `--automation-*-root` flags are refused with `--bridge` in 0.16.0.
- README coverage counts refreshed (WordCraft 312/643, GridCraft 216/353, DeckCraft 228/327, PhotoCraft 290/940, ONLYOFFICE 93/93 named, 91/93 re-run).

### Fixed
- `pdf_merge` (ONLYOFFICE) was marked untested: verified (merged 4 pages from 2 files). `pdf_get_document_info` works headless (the earlier failure was live only).
- WordCraft: `wordcraft-cli commands --json` does give parameter signatures (an older note said ids only).
- `check-versions.sh` no longer runs `--version` on apps that open a GUI.
- Résumé recipe sample data replaced with an invented, unrelated career.
- Corrections found while testing are listed per section as "Trap" notes (examples: GridCraft `view.zoom` takes `percent`; DeckCraft `table.split` only on merged cells; DeckCraft `review.addToDictionary` writes the user's real dictionary file; ONLYOFFICE rejects unknown arguments).

### Known gaps
- PhotoCraft: AI selection (`select.subject`) still fails on the dark-suit test portrait (re-tested on 0.16.0); photomerge/HDR and auto-align need real overlapping photos; `edit.transform.again` fails headless; `layer.smartObjects.convertToLinked` failed on a fresh smart object.
- GridCraft: Flash Fill finds no pattern headlessly; `.xls/.xlsb/.ods` import untested; slicers do not survive between runs or in xlsx.
- DeckCraft: media playback, presenter view and `design.applyIdea` untested.
- WordCraft: ink (`draw.*`), embedded objects, the clipboard pane, `tools.attachTemplate`, table of authorities.
- ONLYOFFICE: the Document Builder macro API is mostly uncovered; no second app version tested; `list_editor_documents` and `pdf_fill_form_fields` not re-verified in the audit.

## 2026-10-24

### Added
- **Repository start:** WordCraft, ONLYOFFICE and PhotoCraft skills, top-level README and `install.sh`.
- **WordCraft 0.10.0:** tables, headers and footers (per section), page numbers, columns, links, TOC, footnotes, pictures, find and replace, comments, tracked changes, styles, captions, shapes, cover page, lists, charts, equations, macros, proofing, mail merge, citations and bibliography, cross-references, document comparison, templates, accessibility checker, résumé fidelity check, live-mode notes.
- **ONLYOFFICE:** spreadsheet and presentation notes, Word helper tools, PDF tools, fillable forms, live editing in all four editors, filling an existing PDF form, real résumé editing on copies, designed decks.
- **PhotoCraft 0.15.1:** CLI run/info/convert/batch, layers, shapes, type, styles, live mode, and background removal (lasso plus refine edge to a layer mask), with a measured better method (grid-read trace, smooth, contract).

### Known gaps
- PhotoCraft hair-aware refine failed on a blurred dark background; AI selection not yet available in 0.15.1.
