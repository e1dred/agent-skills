---
name: vectorcraft
description: Use when drawing, editing, tracing or converting vector artwork — shapes, paths, Pathfinder, type, fills/gradients/patterns, appearance and effects, layers, artboards, symbols, transform and align, SVG/PDF/AI/EPS/DXF/PSD import and export — when running vectorcraft-cli, or when connecting to the VectorCraft app (storytold) on this machine
---

# VectorCraft

Field notes from the first full headless round, last tested on **VectorCraft 0.21.0**
(Linux binary `vectorcraft-cli`). VectorCraft is a vector illustration app written in Rust; the
CLI, the MCP server and the app's control channel run the same engine commands. If
`vectorcraft-cli --version` reports a newer build, re-check the ids and params here before relying
on them — the catalogue grows fast (0.17.0 had 811 ids, 0.21.0 has 911; see
`reference/newer-commands.md`).

## Setup

- **CLI:** `~/AppImages/vectorcraft-cli` (self-contained; opens no window in `run`, `convert`,
  `info`, `bench`, `perf`). Never launch the `.appimage` unless the user asks for the window.
- **Headless batch:** `vectorcraft-cli run --commands FILE` (or `-` for stdin) with a JSON array
  or JSON Lines of `{"command": id, "params": {...}}` steps; also `--cmd ID --params JSON`
  repeated, and `--in FILE` / `--export OUT` steps. Prints one JSON object per step:
  `{"command","result","step"}`. **An unknown or failing command aborts the whole run with exit 1**
  — there is no `--keep-going` here, so put risky commands last or run them alone.
- **Convert one file:** `vectorcraft-cli convert IN OUT [--scale N] [--artboard I|--range R]
  [--outline-text] [--decimals 1-7] [--hidden-objects layer|omit|visible]`.
- **Inspect a file:** `vectorcraft-cli info FILE` → warnings, title, colour mode, units, artboards,
  object counts, fonts. `bench FILE` and `perf` time the renderer.
- **MCP:** `vectorcraft-cli mcp [--connect ADDR | --headless] [--automation-read-root DIR]
  [--automation-write-root DIR]`. The roots confine what open/place/link saves can touch and imply
  `--headless`.
- **Live app:** `vectorcraft --control PORT`, then `--connect` on the CLI. Not exercised in this
  round; do not open a window on the user's screen without being asked. There is no
  `--keep-going` on `run`, so live scripting should go through MCP.
- **Isolate state:** the CLI writes preferences/libraries under `$HOME`. For tests set
  `HOME`, `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, `XDG_CACHE_HOME` to a scratch folder (this round
  did exactly that).

## Where things are

| File in `reference/` | Read it for |
|---|---|
| `cli.md` | Subcommands, run/commands forms, output shape, exit codes, automation roots, headless vs live |
| `drawing.md` | Shapes, `path.create`, Pathfinder, Shape Builder, Shaper, Live Paint, brushes, envelope/mesh distort |
| `type.md` | Point/area/path type, ranges, styles, threading, tabs, lists, fonts |
| `paint-appearance.md` | Fills/strokes, swatches, gradients (incl. freeform), patterns, appearance stack, effects, transparency, graphic styles |
| `layers-artboards-symbols.md` | Layers/sublayers, artboards, symbols and instances, datasets/variables, guides |
| `transform-align.md` | move/rotate/scale/reflect/shear/transform, setBounds, align, distribute, pathfinder-style stacking |
| `import-export.md` | open, save, export and convert in every readable/writable format, place, PDF, print, package |
| `command-catalogue.md` | Every id (911), grouped by family, with this round's status and the field that changed |
| `newer-commands.md` | What 0.17.0 → 0.21.0 added and changed |
| `log.md` | Dated log of what was tested when, and what is still unverified |

## The document model (verified)

- A new document is 612×792 pt, one artboard ("Artboard 1"), one layer ("Layer 1"). Object ids
  start at 2 (1 is the layer); `shape.rectangle {x,y,width,height} → {"id":2}`.
- `document.inspect` is the cheap read: artboards, layers with children (bounds, fill, stroke),
  `selection`, `objects`, `paint` (current fill/stroke), `revision`, `dirty`, `history`.
- `document.json` is the complete document model — layers (objects nested in `kind.children`),
  artboards, swatches, symbols, graphic styles, guides, units. Diff this before/after for exact
  evidence. Floating-point noise is common; compare with tolerance when writing tests.
- `select.set {ids:[…]}`, `select.all`, `select.none` drive every command that defaults to
  "the selection". Most commands also take `ids` / `id` explicitly — prefer that when scripting.
- Read one object: `document.node {id}`, or `document.inspect {ids:[…]}`; find by name/kind/text:
  `document.find {name|kind|text}`.

## CLI essentials (verified)

```
vectorcraft-cli commands                     # the whole catalogue as JSON (911 entries)
vectorcraft-cli info drawing.svg             # warnings, artboards, object counts, fonts
vectorcraft-cli convert in.svg out.pdf --artboard 0
# a script of steps, one JSON object per line:
{"command":"shape.rectangle","params":{"x":100,"y":100,"width":200,"height":120}}
{"command":"text.create","params":{"x":100,"y":400,"text":"Hello","size":24}}
{"command":"document.export","params":{"path":"out.svg","format":"svg"}}
```

- A failing step ends the run: `vectorcraft-cli: step 2 (text.point): unknown command …; exit 1`.
  Parameters are checked before the command runs: `invalid parameters for \`shape.rectangle\`:
  missing number \`x\``, `missing \`name\` (see …)`.
- `document.export` picks the format from the extension unless `format` is given; it returns
  `{path, format, bytes, warnings}`. The `--export` steps of `run` do the same thing.

## Traps

- **No `--keep-going`.** One bad command kills the batch; errors name the step index. Put a
  possibly-failing command in its own run, or use MCP (where each command is a call).
- **Commands act on the selection.** "nothing selected", "select a clip group", "select a text
  object", "no anchor points selected" are preconditions, not parameter errors — select the right
  object first (`select.set`, or pass `ids`).
- **Positioning is in points for the document, not screen pixels.** `shape.rectangle` x/y is the
  top-left; rotate/scale origins default to the bounding-box centre.
- **A closed path refuses `path.close`/`path.join`** ("path is already closed"). `path.create`
  defaults to `closed: false` only if you leave it out — pass `closed: true` deliberately.
- **`object.scale` scales both axes when `sy` is omitted** (`sx:150` doubled a 200×120 rectangle
  to 300×180): pass `sy` when you mean one axis.
- **`document.open` replaces the active document but the run continues**; a script that opens a
  file and then edits must account for the new document's ids.
- **Static symbols can't take instance appearances.** `symbol.instance.setAppearance` refuses
  (`… is a static symbol: set its Symbol Type to Dynamic`) until `symbol.options {type:"dynamic"}`.
- **`object.pattern.make` enters pattern-editing mode**; finish with `object.pattern.done`
  (`saveCopy` while still editing). `object.pattern.edit` needs the document to have a pattern.
- **Effects are live.** `effect.apply {effect:"stylize.dropShadow"}` records an appearance effect;
  `effect.expandAppearance` bakes it, and refuses when the appearance is basic.
- **Exporting `.txt` writes the type only** (one line per type object), not a dump of the art.
- **Hidden layers**: exports keep hidden layers, as SVG `data-*` attributes; `convert` has
  `--hidden-objects layer|omit|visible` for `.ai` output.

## Evidence status of this skill

Tested on 2026-11-04 against `vectorcraft-cli` 0.21.0, headless, isolated `HOME`, no downloads:
911 ids attempted, results in `results.jsonl` (one line per id). Verified (same field read
before/after): 366; read-ok: 53; ran (accepted, not a readable field): 291; refused: 238, each with
its exact error. Refusals cluster in features that need preconditions this harness did not build
(clip groups, envelopes, Live Paint groups, datasets/variables, model-less presets) and in two
headless-absent features: Data Recovery (needs Preferences folders) and PDF/DXF inspection of
synthetic fixtures. See `reference/log.md` for the per-family picture.
