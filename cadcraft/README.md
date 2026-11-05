# CadCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code draw and check
[CadCraft](https://github.com/storytold/cadcraft) drawings: AutoCAD-style 2D drafting with DXF/DWG in and out,
wiring schematics, floor plans and engineering drawings. It holds working notes from real tasks — exact command
parameter formats, traps that cost time, how to verify a drawing by rendering it, and end-to-end recipes.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the CadCraft
project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, live vs headless use, CLI essentials, traps, verification, and a table of the reference files |
| `reference/` | The detailed sections (schematics, drafting features, recipes, the live window, DWG files, command sweeps, version changes, log) |
| `tools/schem.py` | A `Sheet` that collects commands and builds a DXF, a white PDF and a PNG; example in `examples/relay_lamp.py` |
| `tools/ccmcp.py` | Calls CadCraft's MCP bridge on the running app from a shell |
| `tools/ccrun.py` | Runs command lines, including ids that start with `-` |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a
user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no
symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh cadcraft
```

## How the agent uses CadCraft

**Headless** — the CLI runs whole command stacks and prints one JSON result per command:

```sh
cadcraft-cli run drawing.dxf --metric --cmd 'rectang {"p1":[20,20],"p2":[60,50]}' --save out.dxf --export out.pdf
cadcraft-cli convert in.dxf out.pdf
```

**Live** — with the app running under `--control PORT`, the agent drives the same commands through the MCP bridge
(`cadcraft-cli mcp --connect HOST:PORT`; see **Setup** in `SKILL.md`). Keep the CLI that matches the app: extract
it from the AppImage with `--appimage-extract` rather than running the AppImage with `--version`, which opens the
GUI.

## What the skill covers

- Drawing a wiring schematic and checking its connections from the DXF
- Dimensions, hatch, blocks and attributes, text and styles, layouts and viewports
- Plotting to PDF with real colours and lineweights, PNG/SVG output, plot styles
- End-to-end recipes: a metre-unit floor plan on A3, a parametric plate at true 1:1
- Driving the live CadCraft window: clicks, screenshots, a real drawing open
- Opening, editing and saving real AutoCAD DWGs, including save versions
- Probes of every remaining command id, so command coverage is visible

## Limits worth knowing

- PNG export is dark and thin — a CAD screen look, not a document; use PDF for anything a person will read.
- Unknown or unloaded linetypes fail the whole run; load the linetype first.
- Handles are strings, and commands that need entities (block, trim, hatch) take handles from earlier results.
- Authoring dynamic blocks has no commands (UI only).

## Contributing

Corrections and new verified notes are welcome. Add only what was confirmed on a named CadCraft version, and keep
personal data and other people's documents out of examples.

## License

MIT — see `LICENSE`.
