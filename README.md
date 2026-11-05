# agent-skills

[Agent Skills](https://agentskills.io) that help AI agents such as Claude Code drive desktop apps well.
Each one holds working notes collected from real tasks: how to connect for live editing, exact command and
parameter formats, traps that cost time, how to verify results, and ready-to-run recipes. Only things
confirmed on the latest tested app version go in; each skill names that one version, not a history.

> **Note for AI assistants:** to install a skill from this repo, read [`INSTALL.md`](INSTALL.md) first.

Unofficial: not affiliated with any of the app projects.

**Craft apps** (the [storytold](https://github.com/storytold) editors):

| Skill | App | Last tested on | Commands documented (measured) | Everyday tasks covered (checklist) |
|---|---|---|---|---|
| [`wordcraft/`](wordcraft/) | [WordCraft](https://github.com/storytold/wordcraft) word processor: live and headless editing, tables, lists, headers/footers per section, mail merge, citations, templates, comparison, accessibility | 0.15.2, Linux AppImage | 655 of 655 | 25 of 25 (100%) |
| [`gridcraft/`](gridcraft/) | [GridCraft](https://github.com/storytold/gridcraft) spreadsheet: headless CLI, live control channel, formulas, pivots, formatting, charts, .xlsx build/check/export | 0.16.1, Linux AppImage | 377 of 377 | 26 of 26 (100%) |
| [`deckcraft/`](deckcraft/) | [DeckCraft](https://github.com/storytold/deckcraft) presentations: headless CLI, live control channel, SmartArt, animations, layouts, .deckcraft/.pptx/PDF export | 0.15.1, Linux AppImage | 331 of 331 | 30 of 30 (100%) |
| [`photocraft/`](photocraft/) | [PhotoCraft](https://github.com/storytold/photocraft) image editor: headless CLI, live bridge, adjustments, retouching, layers, masks, selections, batch | 0.20.2, Linux AppImage | 965 of 965 | 34 of 34 (100%) |
| [`cadcraft/`](cadcraft/) | [CadCraft](https://github.com/storytold/cadcraft) 2D drafting (AutoCAD-style, DXF/DWG): headless CLI, layers and linetypes, dimensions, hatch, blocks and attributes, layouts and PDF plotting, editing, tables, drawing schematics from primitives, live MCP bridge, checking a drawing's connections from the DXF | 0.17.1, Linux AppImage; also tested on AutoCAD-made drawings and in the live window | 457 of 457 | 33 of 33 (100%) |
| [`pdfcraft/`](pdfcraft/) | [PdfCraft](https://github.com/storytold/pdfcraft) PDF editor: headless CLI and scripted tools, pages (insert, rotate, delete, extract, split, combine, labels, boxes, transitions), text, comments and bookmarks, forms, protection, redaction, compare, links, measurement, Bates, metadata, PDF/A, checks, digital signing, accessibility tags, content and text editing; live control (213 UI commands) on a hidden display | 0.18.2, Linux AppImage; headless and live | 189 of 189 (tools, not command ids) | 30 of 30 (100%) |
| [`filmcraft/`](filmcraft/) | [FilmCraft](https://github.com/storytold/filmcraft) video editor: projects, importing media, sequences, cutting and trimming, titles and graphics, transitions, effects and keyframes, the audio mixer, captions and SRT, markers, MP4/GIF export, the export queue, interchange exports, frame stills, probing, multicam, source monitor, preferences and shortcuts; live control over the MCP bridge on a hidden display | 0.17.1, Linux AppImage; headless and live | 716 of 716 | 30 of 30 (100%) |

**ONLYOFFICE and GenOffice** (not Craft apps):

| Skill | App | Last tested on | Commands documented (measured) | Everyday tasks covered (checklist) |
|---|---|---|---|---|
| [`onlyoffice/`](onlyoffice/) | [ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop.aspx) through its AI-tools MCP server: Word, spreadsheets, slides (incl. designed decks), PDFs, forms, live editing | 10.0.0, Linux flatpak | 93 of 93 | 34 of 34 (100%) |
| [`genoffice-supplement/`](genoffice-supplement/) | [GenOffice](https://github.com/genspark-ai/genoffice) (`genoffice` CLI and MCP). **Supplementary only:** what GenOffice's own skills do not cover (none of them are copied here): the Word, Excel and PowerPoint ops, their traps and units, and the document styles rebuilt in GenOffice | 0.12.852, Linux AppImage; headless, plus the live editor | 153 of 153 ops from `genoffice guide` (all run and checked except `moveSection`) | 50 of 50 (100%) across Docs, Sheets and Slides plus convert, merge and render |

Where part of a section was not re-run on the version a skill names, a `> Not re-checked:` line says what, so treat those parts as tested on an earlier version only. What changed and when: [CHANGELOG.md](CHANGELOG.md).

*Commands documented* (`./coverage.sh`) is how many of the app's command ids the skill names (ONLYOFFICE: MCP tools; GenOffice: documented ops; CadCraft ids count only where written as commands, since many are plain words). For the Craft apps the ids were also run and their effect checked, apart from a few skipped on purpose and named in the skill; commands found to do nothing in the tested version are recorded as such in the skill ([`smoke-tested/`](smoke-tested/) explains how). *Everyday tasks covered* (`./everyday.sh`) counts the ordinary tasks in [`everyday/`](everyday/) whose commands all exist and are named in the skill; the lists cover the basics only. For ONLYOFFICE the unit is its MCP tools; each document type also has a macro tool that reaches the whole Document Builder API (in 10.0: about 1,370 methods for Word, 1,430 for spreadsheets, 490 for presentations and 600 for PDF), of which the skill documents only a small part (about 5% of the method names).

More skills are added as the apps get used.

## Install with your AI assistant

You don't need to keep a clone. Ask your assistant (Claude Code, OpenCode, Codex or similar) something like:

> Install the `wordcraft` skill from https://gitlab.com/e1dred/agent-skills into your skills directory.

It knows where it keeps skills; [`INSTALL.md`](INSTALL.md) covers what is specific to this repo (which folders are skills, setup beyond the files, how to fetch). Skills are instructions your assistant will follow, so skim a skill before trusting it, as with any code you install.

## History

`wordcraft/` and `onlyoffice/` were first published as separate repos (`e1dred/wordcraft-skill`,
`e1dred/onlyoffice-skill`) and were merged here with their history.

## Credits

The PhotoCraft, GridCraft and DeckCraft skills used [artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills) (MIT, written against macOS)
as background reading about what the app can do; nothing was copied, and everything in this repo was run and checked on
Linux. Thanks to its author.

## Document styles

[`styles/`](styles/) has eight looks (traditional, elegant, clean, professional, academic, modern, stylish, creative), each as a document, an ATS-friendly résumé, a European-style CV and (academic) an APA/MLA paper, on US Letter or A4, with tables, headers/footers, columns and optional photo,
built identically in WordCraft and ONLYOFFICE from one spec, with font fallbacks that match what is installed. See the [gallery](styles/README.md).

### How versions were compared

When an app updated, the previous CLI was kept (`<app>-cli.<version>`) and the skills' own example scripts were run on both CLIs; the outputs (command results, `info`, sheet and
text contents, `.pptx` info, rendered pixels) were normalised for timestamps and paths and diffed. A skill's version label moves to the new version only after this re-run;
whatever could not be re-run is listed in a `> Not re-checked:` line. Live control channels need the app running and were re-tested only where the skill says so.

## Keeping up with app updates

The apps (AppImages) update themselves, but a separately installed `<app>-cli` does not, and a CLI older than its app has caused
real failures (live-bridge timeouts). Run `./check-versions.sh` at the start of a session: it lists app vs CLI versions, flags
mismatches and reports a pending ONLYOFFICE flatpak update. It only reads; refresh a CLI by re-extracting it from the AppImage.
After updating a CLI, run `./coverage.sh` and refresh the *Commands documented* column.

## Contributing

Corrections and new verified notes are welcome. Please only add what you have confirmed on a named app
version, and keep personal data out of examples.

## License

MIT — see `LICENSE`.
