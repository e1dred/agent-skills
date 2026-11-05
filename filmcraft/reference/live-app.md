# FilmCraft reference: the live app (bridge)

Part of the filmcraft skill. The short front page is `../SKILL.md`. Verified 2026-11-04 on **FilmCraft 0.17.1**, with
the app on a private headless display (the same mutter + Xwayland setup as in the pdfcraft skill's `live-app.md`,
"Running the app where the user cannot see it"; give the test instance its own `HOME`/XDG folders).

## Connecting

- Start: `FILMCRAFT_CONTROL_TOKEN=<64 hex> filmcraft --control PORT` (log: "control server listening on 127.0.0.1:PORT";
  without the token the listener stays closed). With no project it opens the built-in demo project.
- CLI over the bridge: `FILMCRAFT_CONTROL_TOKEN=… filmcraft-cli --bridge 127.0.0.1:PORT exec <id> …` / `inspect project`.
  There are no `ui.*` command ids: the UI tools exist only in the MCP server.
- MCP: `filmcraft-cli mcp --bridge 127.0.0.1:PORT` lists 18 tools: `command_run`, `command_batch`, `command_list`,
  `doc_inspect`, `project_inspect`, `sequence_inspect`, `media_import`, `render_frame`, `render_preview`, and the live-only
  `ui_inspect`, `ui_elements`, `ui_click`, `ui_drag`, `ui_key`, `ui_type`, `ui_screenshot`, `ui_control`.
  From a shell: `python3 -I tools/fcmcp.py '[["ui_inspect",{}],["ui_screenshot",{}]]' --port PORT --img-dir DIR`.

## What the live app adds (verified)

- `ui_screenshot` returns the whole window (or one panel); `ui_elements` lists about 300 elements with ids such as
  `panel.tab.Project`, `timeline.clip.<id>`, `timeline.tab.*`, `project.search`.
- `ui_click {id:"panel.tab.Project"}` switched the panel; clicking `timeline.clip.<id>` selects that clip (what
  title commands need). `ui_key {key:"Space"}` toggles playback (`ui_inspect` → `playback.playing`); `ui_type` writes
  into the focused field (`project.search`). `ui_control {method:"ui.playback", params:{action:"toggle"}}` also plays.
- **Keyframes at any time work live:** `effects.addKeyframe {clip, effect:"opacity", param:"opacity", seconds:1.5,
  value:40}` → `added:true`, keyframes 5 → 6, time snapped to a frame (headless with a raw `mediaTime` it did nothing).
- `prefs.get` / `prefs.schema` / `prefs.reset`, `shortcuts.list` / `audit` / `conflicts` / `presets`, `mediaBrowser.list`
  / `roots` / `settings` / `favorite`, `mediaCache.info`, `multicam.inspect` + `audioFollowsVideo` / `recordStart` /
  `recordStop`: read back or changed as expected. `transcript.models` reports `available:false` until a Whisper model
  is downloaded; `tts.voices` lists the built-in voices.
- **Diff `ui_inspect` with care:** `fps`, `playback.shown`, the element count and a moving `playhead` change on every
  call; leave them out of before/after comparisons or everything looks changed.
