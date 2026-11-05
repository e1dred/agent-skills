# Log — VectorCraft first full round

## 2026-11-05 — `vectorcraft-cli` 0.21.1

Old-vs-new regression (`~/.local/share/craft-regression/vectorcraft.sh`: shapes, pathfinder,
text, appearance, symbols cases + svg/pdf/ai/eps/dxf conversions) clean on both CLIs; differences
only `document.json` version 1→2, 1e-6 rounding in DXF, `.ai` with Illustrator editing data.
The 7 new ids were run individually; results in `command-catalogue.md`. Not re-run: the other
911 ids beyond the regression cases.

## 2026-11-04 — `vectorcraft-cli` 0.21.0, headless, isolated HOME

Method: one fresh process per id (new document, small object model: two overlapping rectangles,
an ellipse, a closed path, a point text, a second layer; family-specific extras such as a
clip group, a symbol, a gradient paint, a pattern, an envelope). Read-back: `document.inspect`
plus the complete `document.json` before and after, flattened and diffed with volatile fields
(revision, dirty, history, next_id, uid) excluded. Exports were checked by file size and magic
bytes; opens by `document.open` + object count. No window, no `--connect`, no `ui.*`, no
downloads.

Result: **911 ids attempted**, 0 untested. 329 of the 911 ids verified (366 including the 37 format
rows), 53 read-ok, 291 ran (accepted, effect not a readable field), 238 refused with the exact error. Plus 37
extra evidence rows for the format sweep (`document.export` × 19, `document.open` × 18).

### Per-family picture

| family | ids | verified | read-ok | ran | refused |
|---|---|---|---|---|---|
| object | 151 | 86 | 5 | 39 | 21 |
| addon | 59 | 20 | 0 | 18 | 21 |
| select | 53 | 32 | 0 | 15 | 6 |
| document | 35 | 3 | 4 | 23 | 5 |
| path | 34 | 17 | 0 | 9 | 8 |
| text | 33 | 7 | 1 | 12 | 13 |
| edit | 30 | 14 | 0 | 11 | 5 |
| file | 28 | 6 | 4 | 9 | 9 |
| layer | 26 | 14 | 0 | 7 | 5 |
| perspective | 25 | 11 | 2 | 3 | 9 |
| swatch | 23 | 7 | 3 | 7 | 6 |
| symbol | 23 | 9 | 2 | 8 | 4 |
| type | 23 | 16 | 0 | 5 | 2 |
| paint | 22 | 10 | 0 | 5 | 7 |
| view | 19 | 2 | 1 | 14 | 2 |
| brush | 18 | 6 | 4 | 4 | 4 |
| graphicStyle | 18 | 1 | 3 | 5 | 9 |
| transparency | 17 | 8 | 1 | 6 | 2 |
| appearance | 16 | 8 | 0 | 4 | 4 |
| library | 16 | 0 | 2 | 6 | 8 |
| variable | 14 | 2 | 1 | 3 | 8 |
| artboard | 13 | 9 | 0 | 3 | 1 |
| clipboard | 12 | 0 | 1 | 7 | 4 |
| dataset | 12 | 5 | 1 | 1 | 5 |
| links | 11 | 0 | 2 | 5 | 4 |
| charStyle | 10 | 2 | 1 | 2 | 5 |
| shape | 10 | 10 | 0 | 0 | 0 |
| stroke | 10 | 2 | 1 | 1 | 6 |
| paraStyle | 9 | 2 | 1 | 2 | 4 |
| print | 9 | 0 | 1 | 3 | 5 |
| effect | 8 | 3 | 1 | 2 | 2 |
| imageTrace | 8 | 2 | 0 | 2 | 4 |
| livePaint | 8 | 4 | 0 | 2 | 2 |
| plugin | 7 | 0 | 0 | 1 | 6 |
| assets | 6 | 1 | 0 | 2 | 3 |
| color | 6 | 0 | 0 | 4 | 2 |
| flattener | 6 | 0 | 1 | 2 | 3 |
| graph | 6 | 1 | 0 | 5 | 0 |
| guide | 6 | 2 | 0 | 1 | 3 |
| svgInteractivity | 6 | 2 | 1 | 1 | 2 |
| gradient | 5 | 0 | 1 | 2 | 2 |
| help | 5 | 0 | 0 | 5 | 0 |
| pdf | 5 | 0 | 1 | 2 | 2 |
| shaper | 5 | 3 | 0 | 1 | 1 |
| colorTheme | 4 | 0 | 0 | 2 | 2 |
| pattern | 4 | 0 | 0 | 3 | 1 |
| prefs | 4 | 0 | 2 | 1 | 1 |
| recolor | 4 | 0 | 1 | 1 | 2 |
| webExport | 4 | 0 | 1 | 2 | 1 |
| css | 3 | 0 | 0 | 3 | 0 |
| dimension | 3 | 0 | 0 | 0 | 3 |
| importMatches | 3 | 0 | 0 | 3 | 0 |
| attributes | 2 | 0 | 1 | 1 | 0 |
| magicWand | 2 | 0 | 1 | 1 | 0 |
| shapeBuilder | 2 | 1 | 0 | 1 | 0 |
| tool | 2 | 1 | 0 | 1 | 0 |
| action | 1 | 0 | 0 | 0 | 1 |
| command | 1 | 0 | 0 | 1 | 0 |
| eyedropper | 1 | 0 | 0 | 1 | 0 |
| image | 1 | 0 | 0 | 0 | 1 |
| node | 1 | 0 | 0 | 0 | 1 |
| script | 1 | 0 | 0 | 1 | 0 |
| shortcutSet | 1 | 0 | 0 | 0 | 1 |
| slice | 1 | 0 | 1 | 0 | 0 |
| **total** | **911** | **329** | **53** | **291** | **238** |

(Every family; the same table is in `../REPORT.md`.)

### Why the refusals

Three groups, all honest:

1. **Preconditions the harness did not build** (the bulk): clip groups, envelopes, gradient
   meshes, Live Paint groups, repeats, Intertwine groups, Objects-on-Path groups, slices,
   opacity masks, anchor selections, highlighted layer rows. The app reports these as
   "select a clip group", "no anchor points selected", "highlight two or more rows" — the
   command itself is fine and was not disproven.
2. **Environment features**: `file.recovery.*` needs Preferences folders; plugin.* needs
   installed plug-ins; variable libraries need a saved `.vcvars` file; print presets need
   saved presets.
3. **Harness limits**: `document.pdfInfo`/`document.dxfInfo` refused on our own exported
   fixtures even though `document.open` read the same files; `path.close`/`path.join` refused
   because the fixture path was closed; `symbol.update` hit the 32-level nesting guard when an
   instance was selected.

### What to retry in a later round

- Build real preconditions and retest: clip group + `object.clippingMask.editContents`,
  envelope + `object.envelope.*`, mesh + `object.mesh.*`, repeat + `object.repeat.*`,
  intertwine, Objects on Path, slices, text threading (two area texts), anchor selection with
  the Direct Selection tool, `stroke.widthPoint.*` on a variable-width stroke.
- Freeform gradients: `paint.editGradient {kind:"freeform"}` then `paint.freeform.*` — this
  round ran the first but not the follow-up points.
- `graphicStyle.apply/delete/rename` with a real style name (the pass used "Test").
- Print presets and PDF presets: save a preset first, then exercise apply/delete/export/import.

### Version note

0.17.0 → 0.21.0: +100 ids (59 of them `addon.*`), 0 removed, 142 parameter docs changed.
See `newer-commands.md`.
