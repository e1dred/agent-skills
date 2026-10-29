# WordCraft agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code drive the
[WordCraft](https://github.com/storytold/wordcraft) word processor well. It holds working notes collected
from real tasks: how to connect for live editing, exact command parameter formats, traps that cost time,
how to verify results, and ready-to-run recipes.

It complements WordCraft's official docs (`docs/mcp.md`, `docs/control-protocol.md`) rather than repeating them.

Last tested with WordCraft 0.11.0 on Linux (AppImage). Unofficial: not affiliated with the WordCraft project.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill's front page: setup, live vs headless editing, CLI essentials, traps, verification, and a table of the reference files |
| `reference/` | The detailed sections (live editing, existing documents, mail merge, headers and tables, formatting, document formats, command reference, log) |
| `recipes/resume_ats.py` | Builds an ATS-friendly résumé (`.docx` + `.pdf`) with `wordcraft-cli run --script`; fictional sample data |
| `tools/wcmcp.py` | Calls WordCraft's MCP bridge tools on the running app from a shell (saves `screenshot`/`render_page` images to `IMGDIR`) |

## Install (Claude Code)

This skill is part of [agent-skills](https://gitlab.com/e1dred/agent-skills):

```sh
git clone https://gitlab.com/e1dred/agent-skills.git ~/agent-skills
~/agent-skills/install.sh wordcraft
```

That links `~/.claude/skills/wordcraft` to this folder; Claude Code picks up skills there automatically. Then connect WordCraft itself
(see **Setup** in `SKILL.md`): start the app with `--control PORT` and register the MCP server:

```sh
claude mcp add wordcraft -- wordcraft-cli mcp --connect 127.0.0.1:PORT
```

Other agents that support the Agent Skills format can use the folder the same way.

## Try the recipe

```sh
python3 -I recipes/resume_ats.py "$PWD/resume.docx" "$PWD/resume.pdf" > job.json
wordcraft-cli run --script job.json
```

Edit the `RESUME` data at the top of the script to use your own content.

## Contributing

Corrections and new verified notes are welcome. Please only add what you have confirmed on a named
WordCraft version, and keep personal data out of examples.

## License

MIT — see `LICENSE`.
