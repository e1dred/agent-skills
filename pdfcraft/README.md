# PdfCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code read and edit
[PdfCraft](https://github.com/storytold/pdfcraft) PDFs: pages, text, forms, redaction, PDF/A, checks and signing.
It holds working notes from real tasks — the headless CLI and its scripts, the live control channel, exact
tool parameters, traps, and how to verify output.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the PdfCraft
project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, headless vs live use, CLI essentials, traps, verification, and a table of the reference files |
| `reference/` | The detailed sections (pages and documents, text/comments/forms, export and PDF/A, editing and signing tools, the live app, version changes, log) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a
user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no
symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh pdfcraft
```

## How the agent uses PdfCraft

**Headless** — every ribbon action is an engine *tool*; the CLI runs them one at a time, as a script, or as
subcommands:

```sh
pdfcraft-cli info file.pdf
pdfcraft-cli text file.pdf --page 2
pdfcraft-cli edit file.pdf --out out.pdf --rotate 1:90 --delete 2
pdfcraft-cli run --script steps.json --root DIR --report
```

**Live** — start the app with a control file and drive it over loopback:

```sh
pdfcraft --control ~/.pdfcraft-control.json
pdfcraft-cli ui --control ~/.pdfcraft-control.json inspect|click|key|command|screenshot …
```

The control file holds a per-launch token; keep it in a private folder. An MCP server is available
(`pdfcraft-cli mcp --root DIR`, stdio). Keep the CLI that matches the app: extract it from the AppImage.

## What the skill covers

- Pages: insert, move, delete, rotate, extract and split, combine, labels and boxes
- Text extraction and search, comments and bookmarks, form authoring and filling, accessibility checks
- Redaction, protection, compare, flatten, hidden information; links, attachments, measurement, Bates, JavaScript
  and PDF/A conversion and verification
- Editing original text, stamps, page objects, signing, checks and audits

## Limits worth knowing

- Tools are not command ids: `pdfcraft-cli tools` lists them with input schemas; an unknown argument is refused.
- A save has no format argument and does not refuse an existing file; the MCP server cannot read temporary paths. The redaction audit can miss a faux redaction; OCR is not bundled.

## Contributing

Corrections and new verified notes are welcome. Add only what was confirmed on a named PdfCraft version.

## License

MIT — see `LICENSE`.
