# agent-skills

[Agent Skills](https://agentskills.io) that help AI agents such as Claude Code drive desktop apps well.
Each one holds working notes collected from real tasks: how to connect for live editing, exact command and
parameter formats, traps that cost time, how to verify results, and ready-to-run recipes. Only things
confirmed on a named app version go in.

Unofficial: not affiliated with any of the app projects.

| Skill | App | Tested on |
|---|---|---|
| [`wordcraft/`](wordcraft/) | [WordCraft](https://github.com/storytold/wordcraft) word processor: live and headless editing, tables, lists, headers/footers per section, mail merge, citations, templates, comparison, accessibility | 0.10.0, Linux AppImage |
| [`photocraft/`](photocraft/) | [PhotoCraft](https://github.com/storytold/photocraft) image editor: headless CLI, live mode, layers, masks, batch, background removal | 0.15.1, Linux AppImage |
| [`onlyoffice/`](onlyoffice/) | [ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop.aspx) through its AI-tools MCP server: Word, spreadsheets, slides (incl. designed decks), PDFs, forms, live editing | 10.0.0, Linux flatpak |
| [`gridcraft/`](gridcraft/) | [GridCraft](https://github.com/storytold/gridcraft) spreadsheet: headless CLI, live control channel, .xlsx build/check/export | 0.11.1, Linux AppImage |
| [`deckcraft/`](deckcraft/) | [DeckCraft](https://github.com/storytold/deckcraft) presentations: headless CLI, live control channel, .deckcraft/.pptx/PDF export | 0.10.0, Linux AppImage |

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

## Keeping up with app updates

The apps (AppImages) update themselves, but a separately installed `<app>-cli` does not, and a CLI older than its app has caused
real failures (live-bridge timeouts). Run `./check-versions.sh` at the start of a session: it lists app vs CLI versions, flags
mismatches and reports a pending ONLYOFFICE flatpak update. It only reads; refresh a CLI by re-extracting it from the AppImage.

## Contributing

Corrections and new verified notes are welcome. Please only add what you have confirmed on a named app
version, and keep personal data out of examples.

## License

MIT — see `LICENSE`.
