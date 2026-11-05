# Live app: control channel, MCP, screenshots

> **Versions:** DesignCraft 0.17.2 (Linux AppImage), 2026-11-05. Tested on a private hidden display and in a
> window the user had opened themselves.

## Starting and talking to the app

- Start: `designcraft.appimage --control PORT` (or env `DESIGNCRAFT_CONTROL_PORT`). Listens on **127.0.0.1 only**,
  JSON lines over TCP, **no authentication** (enable it only while in use). Log line:
  `designcraft: control server listening on 127.0.0.1:PORT`.
- Wire format: one request per line, `{"id":1,"method":"engine.execute","params":{"command":"…","params":{…}}}`;
  an invalid line gets one error reply and the connection is closed.
- From the CLI:
  - one engine command: `designcraft-cli app --port PORT file.new '{"preset":"Letter"}'`
  - one app method: `designcraft-cli app --port PORT --method ui.inspect`
  - a whole script in the open document: `designcraft-cli script FILE --connect PORT --keep-going`
  - MCP bound to the app: `designcraft-cli mcp --connect PORT` (the read/write roots cannot be combined with
    `--connect`; they confine only the in-process headless server).
- Check first what the user has open: `--method ui.inspect` → `activeDocument`, `documents:[{title, dirty}]`,
  `window`, `currentPage`, `perf`. Work in a new document (`file.new`) rather than in theirs.
- App-side document indices are **0-based** (`file.new` → `{index:0}`); headless `file.open` returned 1.

## Methods that worked

| Method | Result |
|---|---|
| `ui.inspect` | active document, documents, canvas rect, zoom, docking tree, perf |
| `ui.screenshot {"path": ABS}` | PNG of the whole window (2482×2082 on a HiDPI screen) |
| `ui.render {"path": ABS, "page": 0, "scale": 1}` | one page as PNG (page is 0-based) |
| `ui.set {"zoom": 0.8}` | view zoom (read back in `ui.inspect`) |
| `ui.docking` / `ui.click {x,y}` | panel layout + hit rects; clicking the Pages tab focused `"pages"` |
| `ui.tool.list` / `ui.menu.list` | 22 tool groups / 37 tools; 9 top-level menus with `ui:`/`cmd:` items |
| `app.save {"path": ABS}` / `app.export {"path": ABS.pdf}` | `app.export` writes the **spread**, not one page: use `file.exportPdf` for pages |

Other methods listed in the docs (not exercised): `ui.pointer`, `ui.key`, `ui.text`, `ui.ime`, `ui.paste`,
`ui.move`, `ui.drag`, `ui.resize`, `ui.focus`, `ui.tool.select`, `ui.menu.invoke`, `ui.dialog.open/set/confirm/cancel`,
`app.open`, `app.quit`.

**Never send a command that opens a dialog or file chooser without an explicit path** (open, place, import,
export, save-as without `path`): it opens on the user's screen even from a hidden display unless the app runs on
a private D-Bus (below).

## Building a page live in the user's window (worked 2026-11-05)

1. `--method ui.inspect` → no documents open.
2. `app --port PORT file.new '{…}'` → `{index:0}`; the window showed the new "Letter - Half" document.
3. `script build.script --connect PORT --keep-going` → 165/165 steps, the page appeared in the window.
4. `script save.script --connect PORT` with `file.saveAs {path}` and `file.exportPdf {path, standard:"x4", bleed,
   marks}` → files written, no dialog.
5. `--method ui.screenshot` / `ui.render` to look at the result.

The same script ran headless first (`script FILE --keep-going --save test.designcraft`, then render) to fix errors
before touching the user's window. Headless needs a `file.new` first step, which shifts every `$N` by one: generate
both variants from one program.

## Hidden window (nothing on the user's screen)

```sh
setsid -f -- sh -c 'echo $$ > W/mutter.pid; exec dbus-run-session -- mutter --headless --wayland \
  --wayland-display=wayland-dc --virtual-monitor 1600x1000 > W/mutter.log 2>&1 </dev/null'
# mutter.log: "Using public X11 display :N"; XAUTHORITY = the NEWEST /run/user/$UID/.mutter-Xwaylandauth.*
# DBUS_SESSION_BUS_ADDRESS = the private bus from /proc/<mutter pid>/environ (mutter is a child of dbus-run-session)
env -u WAYLAND_DISPLAY DISPLAY=:N XAUTHORITY=… DBUS_SESSION_BUS_ADDRESS=… \
  HOME=W/home XDG_CONFIG_HOME=… XDG_DATA_HOME=… XDG_CACHE_HOME=… DESIGNCRAFT_CONFIG_DIR=W/home/.config/designcraft \
  designcraft.appimage --control 47840 &
```

- The mutter process's own `DISPLAY`/`XAUTHORITY` variables are inherited from the parent session: use the
  display from the log and the newest auth file instead.
- `setsid -f` loses the PID: write `$$` inside the detached shell, then find mutter via
  `/proc/<pid>/task/<pid>/children`. Stop the app and mutter by those PIDs only; never `pgrep -f NAME` from a
  shell whose own command line contains NAME (it matches itself).
- One harmless warning: `org.a11y.Bus: Permission denied` on the private bus.

## MCP tools (`designcraft-cli mcp`)

`list_commands`, `execute`, `batch` (commands or script text, `$N.path` refs, stops at the first error with
`failedIndex`), `inspect_document`, `get_story`, `set_story_text`, `new_document`, `place_image`, `render_page`,
`export_png`, `screenshot` (connected only), `select_tool`, `pointer`, `key`, `type_text`, `ime`. JSON-RPC 2.0 over
stdio. `--automation-read-root DIR` / `--automation-write-root DIR` (repeatable) confine every read and write; a
kind left out grants no access of that kind.
