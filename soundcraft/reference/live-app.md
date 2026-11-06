# SoundCraft live app

Part of the soundcraft skill (front page `../SKILL.md`). Checked on SoundCraft 0.18.0, 2026-11-06, on a private
headless display (the user's own window was not touched).

## Starting and calling it
- `soundcraft.appimage [--demo] [--no-audio] --control PORT` (`0` picks a free port and prints `SOUNDCRAFT_CONTROL_PORT=…`).
  `--no-audio` skips the audio device; playback still runs (see below).
- `soundcraft-cli app --port PORT METHOD_OR_ID '{json}'` prints the reply. Dotted engine ids (`track.color`) are
  shorthand for `engine.execute`; `session.inspect`, `ui.*`, `app.quit` are methods.
- Wire format: TCP 127.0.0.1, one JSON object per line: `{"id":1,"method":"engine.execute","params":{"command":"track.new","params":{…}}}`
  → `{"id":1,"ok":true,"result":…}` or `{"ok":false,"error":"…"}`. No token.
- If the user has the app open, ask which port, work in a new blank session, and never `file.close` / `app.quit`
  their window.

## ui.* methods (0.18.0)
| method | params | checked |
|---|---|---|
| `ui.screenshot` | `{path}` | → `{path,width,height}`; 1920×1043 PNG of the edit window |
| `ui.inspect` | `{}` | `window`, `dialog`, `playing`, `position`, `edit_layout.rows` = `[track id, [x0,y0,x1,y1]]` per row and the timeline rect (use them to aim clicks) |
| `ui.set` | any UI state field | `{"window":"Mix"}` switched to the Mix window (screenshot) |
| `ui.menu.list` | `{}` | 512 entries `{command, path}` (e.g. `File > New...`) |
| `ui.menu.invoke` | `{path}` or `{id}` | `"Track > New..."` → `{dialog:"new_tracks", invoked:"track.new"}` (opens the dialog) |
| `ui.key` | `{key, cmd?, shift?, alt?, ctrl?}` | `Escape` closed the New Tracks dialog (`dialog` → null) |
| `ui.click` | `{x, y, button?, count?, cmd?, shift?, alt?, ctrl?}` | a click on the Hats row of the track list selected track 9 (`session.inspect` selection.tracks) |
| `ui.drag` `ui.move` `ui.text` | `{x,y,to_x,to_y,steps?}`, `{x,y}`, `{text}` | accepted (`{}`), no read-back |
| `ui.scroll` `ui.zoom` | — | in the repo docs but **unknown in 0.18.0** ("unknown command") |
An empty `{}` gives a clear error for `ui.menu.invoke` ("menu item `` is not implemented yet") and `ui.key` ("unknown key").

## What needed the window
- `transport.play` in the live app: `ui.inspect` → `playing:true`, `position` 443072 → 515555 after 1.5 s even with
  `--no-audio`; `transport.stop` → `playing:false` and back at 443072 (the start point).
- `track.color {tracks:["Kick"], color:[0,255,0]}`: Kick turned green in the track list and on its Mix strip.
  `"#00ff00"` is refused ("`color` must be [r,g,b] or a palette index").
- `mix.phase_invert` and `mix.solo_safe` reply `{value:true}` but show nothing on the Mix strips and nothing in
  `session.inspect {detail:"full"}` (track keys: automation, automation_mode, clips, format, height, hidden, id,
  inactive, input, inserts, kind, mute, name, output, pan, playlist, playlists, record_arm, sends, solo, surround,
  view, volume_db). Still unverified.

## Hidden display (keeps windows and file choosers off the user's screen)
Run a private `mutter --headless --wayland --virtual-monitor 1920x1080` inside `dbus-run-session`, start the app on
its Xwayland display with that session's `DBUS_SESSION_BUS_ADDRESS`, an isolated `HOME`/`XDG_*` and
`SOUNDCRAFT_NO_PREFS=1`. Quit with `app.quit` (live app: it exits), then stop mutter by PID.
