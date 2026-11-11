# CLI and headless modes

Tested on `vectorcraft-cli` 0.21.0 (Linux), re-checked on 0.21.1. `vectorcraft-cli` with no arguments prints usage;
every subcommand below was exercised headless on 2026-11-04.

## Subcommands

| Command | What it does | Verified |
|---|---|---|
| `vectorcraft-cli commands` | prints the command catalogue as JSON: `{id,label,menu,params,shortcut,enabled,disabled_reason}` | yes (918 entries in 0.21.1) |
| `vectorcraft-cli run [--in FILE] [--cmd ID [--params JSON]]… [--commands FILE\|-] [--export FILE]… [--scale N]` | batch: open or create a document, run steps in order, export at the end | yes |
| `vectorcraft-cli convert IN OUT …` | open IN, export OUT in the format the extension picks | yes (18 formats) |
| `vectorcraft-cli info FILE` | JSON summary: warnings, title, colour mode, units, artboards, object counts, fonts | yes |
| `vectorcraft-cli bench FILE [--size WxH] [--iters N]` | ms per frame (warm, multithreaded/single) | not run |
| `vectorcraft-cli perf [--paths N] [--deep]` | performance budgets on a synthetic document | not run |
| `vectorcraft-cli mcp [--connect ADDR \| --headless] [--automation-read-root DIR]… [--automation-write-root DIR]…` | MCP server on stdio | not run (needs a client) |

`--automation-read-root` / `--automation-write-root` confine the files commands may open, place,
relink or write (save, export, package, library saves). Either one implies `--headless`. A live app
enforces the same roots when started as `vectorcraft --control PORT --automation-read-root …`.

## `run` step formats

`--commands FILE` accepts:

- a JSON array of `{"command": "id", "params": {…}}` (alias `"id"` for `"command"`), or
- JSON Lines, one object per line (what this round used).

`--cmd ID` with `--params JSON` may be repeated; `--export FILE` steps are interleaved where they
appear. A `.ait` export target is written as `file.saveAsTemplate` would.

Output: one JSON object per step: `{"command": "...", "result": <any>, "step": "cmd"}`.
On failure the process exits 1 and stderr names the step:

```
vectorcraft-cli: step 2 (text.point): unknown command `text.point`; did you mean `text.fonts`?
vectorcraft-cli: step 3 (shape.rectangle): invalid parameters for `shape.rectangle`: missing number `x`
```

There is **no** `--keep-going`: the failing step ends the run, and later steps never execute. To
test a list of commands independently, run one process per command (this round's harness did).

Parameter checking happens before execution and is precise: `missing number \`x\``,
`missing \`name\` (see gradient.presets.list)`, `` `index` must be a whole number ``,
`kind must be graphic, fillColor, …`. Preconditions are runtime errors instead:
`command \`object.align\` is not available right now: nothing selected`.

## Document lifecycle in a run

- With no `--in`, the run starts from a new untitled document: 612×792 pt, one artboard, one
  layer; ids start at 1 for the layer, objects from 2.
- `document.open {path}` swaps the active document; ids restart. `file.new` does the same for a
  blank one. `file.close {index?}` closes the active document, after which `document.inspect`
  refuses with `no document open` (observed).
- `document.save {path}` / `file.saveAs {path}` write and change the document's path;
  `file.saveCopy` writes without changing the document; `document.serialize` returns bytes.
- Isolated state: set `HOME` and the XDG vars to a scratch folder. The CLI reads/writes
  preferences, swatch/brush/gradient libraries and presets there.

## Open/read vs export/write in one process

`run` can open a file, edit it, and export the result (`--in F --cmd … --export out.svg`). All
paths must be under an automation root if the MCP server was started with roots; the CLI itself
has no sandbox unless roots are given.

## Live app

Tested 2026-11-11 (0.24.0) on a hidden display: `vectorcraft --control PORT` (add
`--automation-read-root DIR --automation-write-root DIR` to confine files), then
`vectorcraft-cli mcp --connect 127.0.0.1:PORT` and its MCP tools `run_command`, `inspect_ui`,
`doc_inspect`, `answer_dialog`, `press_key`, `screenshot`. The 443 `ui: true` ids run only here
(headless they refuse: "is a desktop UI command"). Ask before putting a window on the user's
screen; for tests use a private headless compositor with its own D-Bus so dialogs stay hidden.

- **Errors:** a refused `run_command` comes back as a tool result with `isError: true`, not as a
  JSON-RPC error. Check `isError`, or every refusal looks like success.
- **Read-backs:** `inspect_ui` holds the window state (`view.zoom`, `view.center`, `ui.view.grid`,
  `ui.dock_tab`, `ui.shortcut_set` …); use it before/after view, window and shortcut commands.
- **Native file dialogs wedge the channel.** `css.exportFile`, `file.export.png`,
  `shortcuts.export/import`, `ui.actionSet.load`, `ui.checkScript`, `ui.importSvgFilter`,
  `ui.loadAllStyles`, `ui.loadParaStyles`, `ui.runScript`, `ui.shortcutImportDialog`,
  `window.{brush,graphicStyle,swatch,symbol}Library.other` and `edit.autoSpellCheck` open one;
  `answer_dialog {action:"cancel"}`, Escape, `file.cancelExport` and `file.cancelOpen` do not close
  it (`{cancelled: 0}`), and every later command reports the dialog. Use the headless command with
  a `path` instead (`document.export`, `shortcuts`/`prefs` export with data), or restart the app.
- App dialogs (`ui.newLayer`, `ui.newSwatch`, `window.workspace.new` …) return
  `{kind, fields}`; fill or cancel them with `answer_dialog`.
- `ui.preferences` does not exist; the preferences dialog is `edit.preferences`.
- `window.panel.layout {action: {Float: {panel: "layers", rect: …}}}` — the action is a tagged
  enum and `Float` needs `rect`.
