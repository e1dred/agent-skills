# LightCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code manage a
[LightCraft](https://github.com/storytold/lightcraft) photo library and develop raw or JPEG photos:
import and organise, rate and keyword, non-destructive edits and masks, merges, and export, print
and slideshows. It holds working notes from a real headless round — the CLI and its script format,
exact command parameters, traps, and how to verify a result.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the LightCraft project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, headless modes, CLI essentials, traps, verification, and a table of the reference files |
| `reference/` | The detailed sections (CLI, library and import, develop, masks and repair, metadata and keywords, export/print/slideshow, merges and models, the full command catalogue with per-id evidence, version changes, log) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh lightcraft
```

## How the agent uses LightCraft

**Headless** — the CLI runs engine commands against a demo or a real library:

```sh
lightcraft-cli commands --json
lightcraft-cli controls --json
lightcraft-cli run --demo catalog.query limit=3
lightcraft-cli run --library DIR --import DIR --keep-going library.info
lightcraft-cli render in.cr3 -o out.jpg --set light.exposure=0.5 --size 1600
lightcraft-cli merge panorama a.jpg b.jpg c.jpg
```

Commands can also be written as a JSON-lines script (`--script -`), and `--keep-going` keeps a batch running past a failed step.

**MCP** — `lightcraft-cli mcp` serves the same commands over stdio; the round that produced the skill did not drive the live app.

## What the skill covers

- Import, folders, auto-import, previews, albums and smart albums, stacks, versions, history, view
  state (filter, sort, source, selection)
- Develop sliders, crop and straighten, curves, white balance, targeted adjustments, before/after,
  point colour, HDR
- Masks (brush, linear, radial, sky, subject, background, range), mask effects, spot removal, red eye
- Ratings, flags, labels, titles and metadata, keywords and keyword sets, presets
- Export formats and presets, contact sheets, print layouts to PDF, slideshows and their export
- HDR and panorama merges, denoise, faces, segmentation, lens profiles, background tasks

## Limits worth knowing

- Demo-mode photos are generated and have no file; anything that touches bytes needs a real library.
- Model-backed features (object/prompt masks, faces, blemish finding, denoise) refuse without their
  models installed, and the round never downloaded any.
- Background tasks die with a one-shot run unless the command is told to wait.
- Folder rename/move commands act on the real directory, so they need care around user folders.

## Contributing

Corrections and new verified notes are welcome; add only what was confirmed on a named version.

## License

MIT — see `LICENSE`.
