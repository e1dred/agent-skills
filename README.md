# ONLYOFFICE agent skill

An [Agent Skill](https://agentskills.io) that helps AI agents such as Claude Code work with
[ONLYOFFICE Desktop Editors](https://www.onlyoffice.com/desktop.aspx) through the app's own AI-tools MCP
server, including **live editing**: the agent edits the document you have open, and you watch the changes
happen in the editor.

It holds working notes collected from real tasks: how to enable and connect the server from outside the
app, live vs headless behaviour, Word macro API details that work, traps, verification, and recipes.

Tested with ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, Linux) and its AI-tools server
2.0.0-native. Unofficial: not affiliated with Ascensio System SIA / ONLYOFFICE.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The skill: how the connector works, live vs headless, macro API notes, traps, recipes |
| `tools/onlyoffice-ai-mcp` | Runs the app's AI-tools MCP server inside the flatpak, linked to the running editor |
| `tools/ooc.py` | Runs tool calls against a document from a shell (attach → calls → detach) |
| `recipes/resume_live.py` | Rebuilds a document into an ATS-friendly résumé live, in 4 visible stages; fictional sample data |

## Install (Claude Code, Linux flatpak)

1. In ONLYOFFICE, turn on **Settings → Enable AI features**, then restart it.
2. Clone the skill and register the connector:

   ```sh
   git clone <this repository URL> ~/.claude/skills/onlyoffice
   chmod +x ~/.claude/skills/onlyoffice/tools/onlyoffice-ai-mcp
   claude mcp add onlyoffice -- ~/.claude/skills/onlyoffice/tools/onlyoffice-ai-mcp
   ```

3. Open a saved document in ONLYOFFICE and ask your agent to edit it.

The wrapper's paths are for the Flathub flatpak (`org.onlyoffice.desktopeditors`). For other installs, adjust
the paths at the top of `tools/onlyoffice-ai-mcp` (not yet tested).

## Safety notes

- While attached to an open document, the agent cannot save it: you decide whether to Save, Save As, or
  close without saving.
- The connector only listens on your own machine and uses a per-launch token the app writes to a private file.

## Contributing

Corrections and new verified notes are welcome. Please only add what you have confirmed on a named
ONLYOFFICE version, and keep personal data out of examples.

## License

MIT — see `LICENSE`.
