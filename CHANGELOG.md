# Changelog

All notable changes to this repository. Dates are the commit dates; the repo has no version numbers, so entries are grouped by day.
Each skill also labels, section by section, which app version a section was tested on (`> Versions:` lines): this file only summarises.
Format follows [Keep a Changelog](https://keepachangelog.com/) (Added, Changed, Fixed, Known gaps).

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
