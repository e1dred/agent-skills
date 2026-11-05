# DesignCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code lay out pages in
[DesignCraft](https://github.com/storytold/designcraft): documents with parent pages, threaded text and styles,
tables and forms, swatches, data merge, TOC, index and books, and export to PDF/X, PDF/A, IDML, EPUB, PPTX and
HTML. It holds working notes from a real round — the CLI and its script format, exact command parameters, traps,
and how to read results back.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the DesignCraft project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, headless and live use, traps, how to verify, and a table of the reference files |
| `reference/` | The detailed sections (CLI and error → setup recipes, layout/text/tables, colour and export, data merge/TOC/books, the live app, the full command catalogue with per-id evidence, version changes, log) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh designcraft
```

## How the agent uses DesignCraft

**Headless** — the CLI runs command scripts and opens no window:

```sh
designcraft-cli commands
designcraft-cli script steps.txt --keep-going --save out.designcraft --export out.pdf
designcraft-cli run --in out.designcraft --scale 2 --all-pages pages/
designcraft-cli validate-pdf out.pdf
```

Each script line is `command.id {json}`; `"$N.field"` passes a value from an earlier step's result.

**Live and MCP** — start the app with `--control PORT`; `designcraft-cli app --port PORT …` and
`script FILE --connect PORT` drive the open window, and `designcraft-cli mcp` serves the same command set over stdio.

## What the skill covers

- Documents, pages, parent pages, automatic page numbers, margins, bleed, facing pages
- Text frames, threading, paragraph and character styles, baseline grid, text wrap, notes, cross-references
- Tables: from text, merging, cell and table styles, alternating fills, row heights and column widths
- Swatches (CMYK, spot), tints, colour themes
- Export: PDF/X-4, PDF/X-1a, PDF/A-2b, plain PDF with bleed and marks, IDML (round trip), EPUB, fixed EPUB, PPTX,
  HTML, PNG, JPG; PDF/X validation
- Data merge from CSV, table of contents, index, books
- Live control of the app window and screenshots

## Limits worth knowing

- DesignCraft is pre-alpha; some commands refuse or have no read-back (listed in `SKILL.md`).
- Most commands act on the selection; the reference lists the setup each error asks for.
- Unknown parameter names are ignored silently, so results must be read back, not assumed.
