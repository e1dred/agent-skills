# agent-skills

[Agent Skills](https://agentskills.io) that help AI agents such as Claude Code drive desktop apps well.
Each one holds working notes collected from real tasks: how to connect for live editing, exact command and
parameter formats, traps that cost time, how to verify results, and ready-to-run recipes. Only things
confirmed on a named app version go in.

Unofficial: not affiliated with any of the app projects.

| Skill | App | Tested on | Commands documented (measured) | Everyday workflows covered (est.) |
|---|---|---|---|---|
| [`wordcraft/`](wordcraft/) | [WordCraft](https://github.com/storytold/wordcraft) word processor: live and headless editing, tables, lists, headers/footers per section, mail merge, citations, templates, comparison, accessibility | 0.10.0, 0.11.0 (headless sections re-run on both; see the skill), Linux AppImage | 411 of 643 | ~85% |
| [`gridcraft/`](gridcraft/) | [GridCraft](https://github.com/storytold/gridcraft) spreadsheet: headless CLI, live control channel, formulas, pivots, formatting, charts, .xlsx build/check/export | 0.11.1, 0.12.1 (12 scripts re-run on both; live channel re-checked on 0.12.1), Linux AppImage | 295 of 353 | ~85% |
| [`deckcraft/`](deckcraft/) | [DeckCraft](https://github.com/storytold/deckcraft) presentations: headless CLI, live control channel, SmartArt, animations, layouts, .deckcraft/.pptx/PDF export | 0.10.0, 0.11.1 (3 build sequences re-run on both; live channel re-checked on 0.11.1), Linux AppImage | 296 of 327 | ~85% |
| [`photocraft/`](photocraft/) | [PhotoCraft](https://github.com/storytold/photocraft) image editor: headless CLI, live bridge, adjustments, retouching, layers, masks, selections, batch | 0.15.1, 0.16.0 (6 pipelines re-run on both), Linux AppImage | 371 of 940 | ~85% |
| [`cadcraft/`](cadcraft/) | [CadCraft](https://github.com/storytold/cadcraft) 2D drafting (AutoCAD-style, DXF/DWG): headless CLI, layers and linetypes, dimensions, hatch, blocks and attributes, layouts and PDF plotting, editing, tables, drawing schematics from primitives, live MCP bridge, checking a drawing's connections from the DXF | 0.13.0 (CLI and live bridge), Linux AppImage; latest release (v0.13.0), nothing re-run on a second version; tested on CadCraft-made and AutoCAD-made drawings and in the live window | 191 of 441 (an upper bound: CadCraft's ids are plain words such as `line` and `text`) | ~85% |
| [`onlyoffice/`](onlyoffice/) | [ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop.aspx) through its AI-tools MCP server: Word, spreadsheets, slides (incl. designed decks), PDFs, forms, live editing | 10.0.0, Linux flatpak | 93 of 93 tools named; **91 of 93 re-run on 10.0.0 on 2026-10-25** (see the skill's audit section); the full macro API is not covered | ~95% |

Each skill marks, section by section, which version it was tested on and what was re-run on a second version (`> Versions:` lines); where it says "not re-run", treat the text as tested on the older version only. What changed and when: [CHANGELOG.md](CHANGELOG.md).

*Commands documented* is measured by `./coverage.sh` (as of 2026-10-26, after the CadCraft and WordCraft rounds): how many of the app's own command ids (MCP tools for ONLYOFFICE)
appear in the skill. It is a rough lower bound on what a skill teaches, since a workflow can be described without naming every command, and an
upper bound on what was tested, since an id can be named without being run. *Everyday workflows covered* is the author's **estimate**, rounded
to 5%, of how many of the core tasks (build, edit, format, export) have a recipe that was run and checked. It is a judgement, not a measurement.
For ONLYOFFICE the unit is MCP tools, which are convenience wrappers rather than app operations, so that figure is not comparable to the Craft rows; each document type also has a macro tool that reaches the whole Document Builder API.
Both change when an app updates; most commands in these apps are rarely needed, so a low first number does not mean a skill is thin.

More skills are added as the apps get used.

## Install (Claude Code)

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh            # or: install.sh wordcraft onlyoffice
```

`install.sh` only creates symlinks `~/.claude/skills/<skill>` → `~/agent-skills/<skill>`; it never
overwrites an existing file or folder. Claude Code picks up skills in `~/.claude/skills/` automatically.
Update later with `git -C ~/agent-skills pull`.

Each skill's own `README.md` says how to connect its app (MCP server, launch flags).

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

When an app updated, the previous CLI was kept (`<app>-cli.bak`) and the skills' own example scripts were run on both CLIs; the outputs (command results, `info`, sheet and
text contents, `.pptx` info, rendered pixels) were normalised for timestamps and paths and diffed. "Identical" in a skill's `> Versions:` line means that diff was empty. Only the
examples named in that line were re-run: anything else in the section is still tested on the older version only. Live control channels need the app running and were re-tested only where the line says so.

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
