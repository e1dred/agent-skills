# VectorCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code draw and edit
[VectorCraft](https://github.com/storytold/vectorcraft) illustrations: shapes and paths, Pathfinder,
type, fills and effects, layers, artboards, symbols, and import/export across the vector and raster
formats. It holds working notes from a real headless round — the CLI and its batch format, exact
command parameters, traps, and how to read results back.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the VectorCraft project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, headless use, CLI essentials, the document model, traps, and a table of the reference files |
| `reference/` | The detailed sections (drawing and paths, type, paint and appearance, layers/artboards/symbols, transform and align, import and export, the full command catalogue with per-id evidence, version changes, log) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh vectorcraft
```

## How the agent uses VectorCraft

**Headless** — the CLI runs engine commands in batch and opens no window:

```sh
vectorcraft-cli commands
vectorcraft-cli info drawing.svg
vectorcraft-cli convert in.svg out.pdf --artboard 0
vectorcraft-cli run --commands steps.jsonl
```

Each step is `{"command": "<id>", "params": {…}}`; the run prints one JSON result per step, and a failing step ends the run.

**Live and MCP** — `vectorcraft-cli mcp` serves the same command set over stdio (with optional automation read/write roots). The skill's setup
section documents the flags; the round that produced it was headless only.

## What the skill covers

- Shapes, paths and anchor editing, Pathfinder, Shape Builder, Shaper, Live Paint, brushes
- Point, area and path type, ranges and styles, character and paragraph styles, fonts
- Fills, strokes, swatches, gradients, patterns, the appearance stack, live effects, transparency
  and opacity masks, graphic styles
- Layers and sublayers, artboards, symbols and instances, guides, variables and datasets
- Transforms, arrange, align and distribute
- Opening, placing, saving, exporting and converting in every readable and writable format the app
  reports, including SVG, PDF, AI, EPS, DXF, EMF/WMF and PSD, plus templates, print and package

## Limits worth knowing

- There is no `--keep-going` on a batch run: one bad step aborts the rest.
- Most commands act on the selection or need a specific object selected; precondition errors name
  what to select, and no parameter change fixes them.
- Some families need state that a first attempt may not have built (clip groups, envelopes, meshes,
  Live Paint groups, threaded text); the reference notes which ones and what they need.
- Not every feature was reachable headless: the skill's log lists what was refused and why rather
  than guessing.

## Contributing

Corrections and new verified notes are welcome; add only what was confirmed on a named version.

## License

MIT — see `LICENSE`.
