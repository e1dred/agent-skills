# FilmCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code edit video in
[FilmCraft](https://github.com/storytold/filmcraft): media import, sequences, cutting, titles, audio, captions and
export. It holds working notes from real tasks — exact parameters, traps, verification, and recipes.

The version it was last tested on is at the top of `SKILL.md`. Unofficial: not affiliated with the FilmCraft
project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, headless vs live use, CLI essentials, traps, verification, and a table of the reference files |
| `reference/` | The detailed sections (projects and timeline, titles and graphics, the audio mixer, captions, export, the command catalogue, the live app, version changes, log) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills). AI assistants installing it for a
user should follow [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md) (copy the folder, no
symlink). For people who keep a clone:

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh filmcraft
```

## How the agent uses FilmCraft

**Headless** — the CLI runs engine commands against a project; a script keeps one session:

```sh
filmcraft-cli commands --json
filmcraft-cli --project p.fcproj inspect
filmcraft-cli --project p.fcproj export out.mp4 --scale 0.5 --quality 70
filmcraft-cli --project p.fcproj render --seconds 2 --out frame.png
```

**Live** — start the app with a control port and a token in the environment, then bridge to it:

```sh
FILMCRAFT_CONTROL_TOKEN=<64 hex characters> filmcraft --control 9876
filmcraft-cli mcp --bridge 127.0.0.1:9876
```

Without the token the listener stays closed. Extract the CLI from the AppImage rather than running the AppImage.

## What the skill covers

- Projects, importing media, sequences and the playhead; razor, trim and ripple edits, markers, transitions
- Video effects and keyframes, frame holds; text and shape layers sized for small frames
- The audio mixer and clip gain; caption tracks and SRT import/export
- Export presets and queue, MP4/GIF, stills, interchange, probing
- A catalogue of the remaining command ids with the evidence behind each; driving the running app on a hidden display

## Limits worth knowing

- Times are ticks, not frames, and the playhead snaps to the nearest frame. A text layer at the default size
  overflows a small frame, and a text box clips lines that do not fit.
- Ripple edits fail across a sync-locked track with a clip in the way; some behaviour (raw-time keyframes) only
  works live — the skill says which.
- Selection does not survive a save/reopen; an interchange export can drop a title — read its report.

## Contributing

Corrections and new verified notes are welcome. Add only what was confirmed on a named FilmCraft version.

## License

MIT — see `LICENSE`.
