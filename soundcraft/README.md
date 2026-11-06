# SoundCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code edit, mix and bounce multitrack audio and MIDI in
[SoundCraft](https://github.com/storytold/soundcraft), a Pro Tools-style DAW: import, arrange, plugins, sends, buses,
automation, markers, MIDI, stems and file conversion. It holds working notes from a real round — the CLI and its script format, exact command parameters, traps,
and how to read results back.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the SoundCraft project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, headless and live use, traps, how to verify, and a table of the reference files |
| `reference/` | The detailed sections (tested recipes, CLI/control/MCP notes from the docs, the live app and `ui.*` methods, the full command catalogue with per-id evidence, version changes, log) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh soundcraft
```

## How the agent uses SoundCraft

**Headless** — the CLI runs engine commands on a new, demo or saved session and opens no window:

```sh
SOUNDCRAFT_NO_PREFS=1 soundcraft-cli run --demo \
  --cmd 'mix.volume={"track":"Kick","db":-6}' \
  --bounce mix.wav --start 0:09.230 --end 0:18 --save song.scraft --inspect --compact
soundcraft-cli describe automation.write_range
soundcraft-cli info mix.wav
```

**Live and MCP** — start the app with `--control PORT`; `soundcraft-cli app --port PORT …` drives the open window
(engine commands plus `ui.*` methods such as screenshots, menus, clicks and keys), and `soundcraft-cli mcp` serves the
same command set over stdio.

## What the skill covers

- Sessions: new, demo, open, save (and safe overwrite), revert, templates, health check
- Import audio, MIDI and video; bounce the mix or stems with peak / true peak / LUFS read-back
- Editing: select, split, trim, move, duplicate, repeat, fades and crossfades, playlists, clip gain
- Mixing: volume, pan, mute, solo, buses, sends, built-in plugins and their parameter ids, VCAs and folders
- Automation breakpoints, write/thin/clear; markers and memory locations; tempo and meter
- MIDI tracks and notes; MIDI, MusicXML and score export; audio file conversion and normalization
- Live control of the app window and screenshots

## Limits worth knowing

- SoundCraft is alpha; 35 commands accepted parameters but had no independent read-back (listed in the catalogue).
- Many command replies are echoes: results must be read back from the session, preferences or a bounce.
- Recording, audio hardware and third-party plugins were not tested.
