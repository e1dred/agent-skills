# PhotoCraft agent skill

An [Agent Skill](https://agentskills.io) for driving the [PhotoCraft](https://github.com/storytold/photocraft) image
editor from an AI agent: the headless `photocraft-cli`, the live bridge to a running app, exact command parameter formats,
traps and recipes, collected from real tasks. Part of [agent-skills](../README.md); install with `./install.sh photocraft` if you keep a clone, or ask your AI assistant (it follows [INSTALL.md](https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md)).

The version it was last tested on is at the top of `SKILL.md`. Unofficial. Background reading for what PhotoCraft can do:
[artcraft-skills](https://github.com/midasmatterhorn/artcraft-skills) (MIT, macOS) — referred to, not copied.

## Live editing

Start the app with a control port and a token file (create the file once; it holds a 64-character hex token):

```sh
photocraft.appimage --control 47825 --control-token-file ~/.config/photocraft/control.token \
  --automation-read-root ~/Pictures --automation-write-root ~/Pictures
claude mcp add photocraft -- photocraft-cli mcp --bridge 127.0.0.1:47825 --control-token-file ~/.config/photocraft/control.token
```

Use the `photocraft-cli` that matches the app version (extract it from the AppImage with `--appimage-extract`; it is at `squashfs-root/usr/bin/photocraft-cli`).
From 0.16.0 the bridge refuses `--automation-*-root` flags: set the roots on the app. A bridge call that times out after 55 s means the window is not drawing frames
(minimised, covered, or a dialog is open). Without MCP tools, `tools/pcmcp.py` makes the same calls from the shell.
