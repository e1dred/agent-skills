# CLI, scripts and error → setup recipes

> **Versions:** DesignCraft 0.17.2 (Linux AppImage, `designcraft-cli`), 2026-11-05, headless unless stated.

## Subcommands

```
designcraft-cli run [--in FILE|--sample] [--cmd ID[=JSON]]... [--page N] [--scale S] [--pdf-options JSON] [--export OUT] [--all-pages DIR]
designcraft-cli script [FILE|-] [--in FILE|--sample] [--connect PORT] [--save OUT] [--export OUT] [--keep-going]
designcraft-cli app [--port PORT] COMMAND [JSON] | --method METHOD [JSON]
designcraft-cli mcp [--connect PORT] [--sample] [--automation-read-root DIR]... [--automation-write-root DIR]...
designcraft-cli commands [FILTER]        # JSON array: id, label, menu, params, shortcut, enabled
designcraft-cli describe COMMAND         # one entry; the params doc is the only parameter reference
designcraft-cli validate-pdf FILE.pdf [--standard x4|x1a]
designcraft-cli thumbnail FILE.designcraft OUT.png [SIZE]
designcraft-cli links | perf | bench FILE | --version
```

- `--export` picks the type from the extension: `.png/.jpg`, `.pdf`, `.designcraft`, `.idml`, `.epub`, `.pptx`,
  `.html`, `.rtf/.txt`. An unknown extension is an error and nothing runs. `--export` may repeat.
- `--page` / `--scale` bind to the exports **after** them: `run --in F --scale 2 --all-pages DIR`, not the reverse
  ("--scale has no --export or --all-pages after it"). `run --page N` is **0-based**; `file.exportPdf {pages}` is 1-based.
- `enabled` in `commands` is computed for "no document open": 517 of 547 ids say `false` there. Ignore it.

## Script files

One step per line: `command.id {"param": 1}` (also `command.id={json}`, JSON Lines or a JSON array). `#` and `//`
lines and blank lines are skipped and are **not steps**.

- `"$N.path"` = a value from the result of step N (0-based, counting every command line, including ones that
  return `null`); `$last` = the previous step; `"${N.path}"` inside a longer string; `$$` = a literal `$`.
  Miscounting gives `` `$5.story`: no `story` in null `` — then every later reference fails too. Generate long
  scripts with a small program that records each step's index instead of counting by hand.
- Text parameters: `\n` new paragraph, `\u2028` forced line break, `\t` tab, `\ue000` automatic page number.
- **Unknown parameter names are silently ignored** by most commands: check names with `describe`, verify the
  effect with a read-back.
- Output: `{"completed": n, "results": [...]}`; without `--keep-going` the first failure stops the run and
  reports `failedIndex` / `failedCommand` / `error`; with it, failures become `{"error": …}` and the exit code
  is non-zero.
- Byte offsets: `text.select {story, anchor, focus}` counts UTF-8 bytes (— is 3). `focus: 99999` past the end is
  accepted and selects to the end of the story.

## Read-backs (verify with these, never with the exit code)

- `document.inspect {}` → pages, spreads (items with bounds), parents, stories (with overset), style names,
  swatches, selection, settings.
- `type.selectionAttrs {}` → paragraph/character style and attributes of the selected text (the only way to see
  which style a paragraph has). `table.get {table}` → rows, columns, cells with spans/fills/styles/text.
  `story.get {story}` → text, lines, overset. `transform.info`, `file.info.get`, `*.list` / `*.get`.
- Render: `designcraft-cli run --in F --scale 2 --all-pages DIR` (PNG per page) and look at it.

## Isolate state in tests

Set `HOME`, `XDG_CONFIG_HOME`, `XDG_DATA_HOME`, `XDG_CACHE_HOME` (and `DESIGNCRAFT_CONFIG_DIR`) to a scratch folder;
the real `~/.config/designcraft` stayed byte-identical through a full 547-id sweep run that way. In an isolated
HOME `font.list` is empty, but the bundled families (Source Serif 4, Source Sans 3) still resolve.

## Error → setup recipes

Each line is an error (or silent no-op) and the setup that made the command work in a script.
Step references are 0-based (`$N` = result of step N).

Step references are 0-based (`$N` = result of step N): a `frame.create` on step 1 is `$1.id`, its story `$1.story`.

- `place the insertion point in a table` → create a text frame with `caret: true`, then `table.insert {"rows":4,"columns":3}` in the same script; 30 table.* ids need nothing more.
- `nothing selected` → `frame.create {"rect":[...]}` then `selection.set {"ids":["$1.id"]}`; most object.*, style.object.*, form.*, button.* ids work after this.
- `nothing selected` for align/distribute → `object.distribute` needs 3 objects: create three frames and select all three.
- text formatting has no effect → select the story first: `text.selectStory {"frame":"$1.id"}` (or `text.select {"story":...,"anchor":0,"focus":5}`).
- `missing frame` on text.select*/type.pickUpFormat → pass `{"frame":"$1.id","point":[70,50]}`; a selection is not enough.
- `missing story` on story.*/footnote.setText → pass `{"story":"$1.story"}`; footnote/endnote/note edits also need `"id"` from the insert result.
- `no footnote 1` / `missing id` → use the id returned by `footnote.insert`/`note.new` (`$2.id`), quoted inside JSON.
- `notes go in story text` on note.previous/note.next → leave the caret in the main story after the notes (`text.placeCaret` at the story end), not inside a note story.
- `no earlier note in this story` → insert the second note later in the story (`text.placeCaret` at a point, then `note.new`).
- `no paragraph style X` → create it first: `style.paragraph.create {"name":"ProbePara"}`; same for `style.character.create` / `style.cell.create` / `style.table.create`.
- `select text using the named style` (style.character.redefine) → apply the style to the selection in setup (`style.character.apply`), then redefine.
- `no hyperlink 0` → create one first (`text.selectStory`, `hyperlink.create {"url":...}`) and pass the id from `hyperlink.list` (`$3.ids.0`).
- `give anchor, paragraph or story+para` on xref.insert → define the format first, then `xref.insert {"paragraph":"Alpha"}` (works); an anchor name alone failed in setup order define→insert, but anchor works when inserted before any format define.
- `no cross-reference` on xref.setFormat → pass `{"story":...,"index":0,"format":"ProbeFormat"}` after a successful insert.
- `nothing loaded in the place cursor` → run `place.load {"path":...}` earlier in the same script, then `place.drop {"spread":0,"x":100,"y":100}`.
- `no library open` → `library.new {"path":...}` then `library.add {}` with an object selected; `library.place`/`remove` need `{"index":0}`.
- `no book open` → `book.new {"path":...}` then `book.add {"path": saved.designcraft}` in the same session; book.remove needs `{"index":0}`.
- `give a parent spread id` / `no such parent page` (layout.parentPageSize, layout.selectParentPage) → no id form works (parent spread id from inspect or from layout.parents.new, name or index all refused).
- `invalid ICC profile ... missing 'acsp'` → color.loadProfile needs a real ICC profile file; none can be generated here.
- `Choose an available replacement font family` → `font.list` returns [] in an isolated HOME; font.replace cannot be exercised.
- `no changes since the last save` (file.revert) → save first, then modify in setup; revert then restores (object removed, dirty false).
- `no recovery folder` → file.recovery.* need `{"dir":".../recovery"}`; without a crash folder list is [] and open returns {"opened":[]}.
- `no recent files` → open a saved file in the same session before file.recentFiles / file.openRecent / file.clearRecent.
- `edit text or select a text frame` (file.exportText) → select a text frame object: text docs in the sample document are not enough.
- `clipboard is empty` → `edit.copy` in the same script before edit.paste/pasteInto/pasteInPlace.
- `no tab stop 0` → `type.tabs.add {"position":120}` first in setup, then move/change/remove/repeat.
- `column guides are locked` → `view.lockColumnGuides {"on":false}` in setup; a page with `columns:2` also needed for layout.moveColumnGuide ("0 gutters").
- `a document needs at least one layer` / `no such layer` → `layer.new {"name":"Layer 2"}` first; layer commands act on `id` (not ids).
- `no color group X` → `swatch.newColorGroup {"name":"ProbeGroup"}` then move swatches in; ungroup/rename take `name`.
- `isn't a spot ink` (ink.options) → create the swatch with `spot:true`.
- `special swatches are already listed` (swatch.addToSwatches) → set an object's colour with `object.color` first, then `swatch.addToSwatches {}`.
- `unknown parameter index` on path.* → path.setAnchor/deleteAnchor/convertAnchor take `anchor` (index), path.split takes `at:[x,y]`, path.erase/smooth take `points:[[x,y],...]`.
- `select two or more paths/shapes` → create two `path.create` objects (or two frames for pathfinder), select both.
- `the object isn't in a Flex Layout` → group two frames (`object.group`), then `flex.convert {"ids":["$3.id"]}`; reorder a member by its own id.
- `no gap there` (gap.move) → `at` must sit in the gap between two objects on the same spread (`[240,120]` for frames at 60–220 and 260–420).
- `text frames can't be anchored yet` / `no item N` → anchor a graphic frame with a placed image: create the image frame, `file.place {"frame":"$2.id"}`, then `anchored.insert {"ids":["$2.id"],"story":"$1.story","pos":0}`.
- `select one placed raster image` (color.extractTheme) → place test.png into a frame and select the frame, not a text frame.
- `select a data source` (data.placeholder.add) → `data.source.select {"path":"...csv","name":"data"}` first; placeholders then report from `data.fields`? add returns an id used by data.placeholder.remove.
- XML export stays empty → `xml.tag {"tag":..., "ids":[frame id]}`; `xml.tagText` alone never reaches `file.exportXml`.
- `table.merge does nothing` on a whole-table selection → pass `{"rows":[0,1],"cols":[0,1]}`; unmerge needs a merged table first.
- `no such parent page` → see layout parent line above; treat as a gap.
