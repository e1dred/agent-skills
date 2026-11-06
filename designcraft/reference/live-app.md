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

| `ui.tool.select {"tool":"type"}` | `ui.inspect.tool` = type; unknown tool = error |
| `ui.pointer {"events":[{"kind":"down","x":60,"y":60},{"kind":"up",…}]}` | **canvas** points by default (`space:"screen"` to change); kinds down/drag/up/move/doubleclick; returns `{selection, tool, cursor}`. With the type tool a click placed the caret; a down/drag/up on a frame moved it exactly +50,+50 |
| `ui.text {"text":"…"}` | types at the caret (story length read back); no caret → "no valid text insertion point" |
| `ui.key {"key":"Enter"}` / `{key, text, shift, alt, ctrl, cmd}` | Enter split the paragraph (paragraphs 1→2); names: egui keys or enter/esc/delete/backspace/arrows/space/tab |
| `ui.ime {"preedit":"…","active":[0,2]}` then `{"commit":"…"}` | marked text, then commit replaces it. CJK draws as boxes unless the font has the glyphs |
| `ui.paste {"text":"…"}` | pasted into the edited text (SVG markup pastes as paths) |
| `ui.click {x,y,button?,count?}` / `ui.move {x,y}` | **screen** points, through egui widgets; `ui.move` over an icon showed its tooltip |
| `ui.drag {"x":500,"y":300,"toX":700,"toY":450,"steps":12}` | **screen** points, `x,y,toX,toY` (not from/to). With the rectangle-frame tool it drew a new frame |
| `ui.menu.invoke {"command":"view.zoomIn"}` | runs a menu command (zoom 0.92→1.37). **Without `params` it acts like choosing the menu item and may open a dialog** (`{dialog:"documentSetup"}`); with `params` it just runs |
| `ui.dialog.*` | see "Dialogs" below |
| `app.open {"path": ABS}` | opened as a second document `{index:1, warnings:[]}` |
| `app.quit` | quits **without** the unsaved-changes prompt |
| `ui.resize {width,height}`, `ui.focus` | accepted, no visible effect on a maximized window |

Input events (`ui.click`, `ui.drag`, `ui.key`, `ui.text`, `ui.ime`, `ui.paste`) are queued: read back on the next
frame (wait ~0.5–1 s). Screenshots differ by ~15 px between frames from the caret blink.

**The live app has 734 commands, the CLI 547.** `engine.commands` (app method) lists 187 more: `app.*` (73),
`window.*` (47), `view.*` (44), `help.*`, a few `color.*`/`fit.*`/`effects.*`. Unknown top-level parameter keys
are refused, live and headless alike.

## Dialogs (no file choosers)

`ui.dialog.open {id, fields?}` opens a modal (replacing any open one) and returns `{id, fields}`; `ui.inspect`
shows it under `dialog`. `ui.dialog.set {field, value}` fills one field, `ui.dialog.confirm` runs its Apply
command, `ui.dialog.cancel` closes it with no change.

- Worked: `documentSetup` (`pages` 2→4 on confirm; set `pages` 6 then cancel left 4), `paragraphStyleOptions
  {new:true}` (**the new style's name comes from the `rename` field, not `name`**), `insertTable` (needs a text
  caret first; without one, confirm is refused and the dialog **stays open**, the error only in the status bar).
- `ui.dialog.open` accepts **any** id (a typo opens an empty dialog): check `fields` is non-empty.
- Ids seen in the source: documentSetup, marginsAndColumns, createGuides, insertPages, goToPage, insertTable,
  cellOptions, textFrameOptions, paragraphStyleOptions, characterStyleOptions, swatchOptions, layerOptions,
  fittingOptions, footnoteOptions, frameSize, hyphenation, justification, paragraphRules, numberingSection,
  fileInfo, findChange, newDocument, … Never open `pdfImport`, `print`, `pdfExport`, `epubExport`, `updateLink`,
  `loadStyles`, `importOptions` (they lead to file choosers or printers).
- Document Setup's confirm wants the full field set (intent, pages, startPage, facingPages, binding, width, height,
  bleed[4], slug[4], adjustLayout, margins): open it, change one field, confirm; don't build it from scratch.

## Selection and document commands that need the window

Checked live with read-backs: `select.content` (group → child), `select.container` (child → group),
`select.nextInGroup` / `previousInGroup` (wrap around), `layer.activate {id}` (activeLayer changes; `layer.new`
activates the new layer), `edit.preview {label, command, params}` then `edit.cancelPreview` (reverted) or
`edit.commitPreview` (kept, one undo step), `file.activate {index}`, `file.close {index}`.

**`file.close` on a document with unsaved changes closes it with no prompt and discards the changes.** Save
first (`app.save {path}`, then `dirty:false` in `ui.inspect`).

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
