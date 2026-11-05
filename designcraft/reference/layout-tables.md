# Documents, parent pages, text, styles and tables

> **Versions:** DesignCraft 0.17.2 (Linux AppImage, `designcraft-cli`), 2026-11-05, headless unless stated.

## New document with a parent page and automatic page numbers

```
# Recipe 1 — new half-letter document, facing pages, parent with running footer + page number
# Half-letter = 5.5 x 8.5 in = 396 x 612 pt. Bleed 0.125 in = 9 pt.
file.new {"units":"points","width":396,"height":612,"pages":4,"startPage":1,"facingPages":true,"margins":{"top":36,"bottom":54,"inside":45,"outside":36},"bleed":9,"title":"Field Notes"}
# footer paragraph styles
style.paragraph.create {"name":"Folio","para":{"align":"left"},"chars":{"size":9,"tracking":40}}
style.paragraph.create {"name":"Folio Right","basedOn":"Folio","para":{"align":"right"}}
# --- parent page footers (parent A is the default parent of a new document) ---
frame.create {"spread":{"kind":"parent","index":0},"rect":[36,552,351,582],"content":"text","text":"Field Notes — Issue One"}
text.select {"story":"$3.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Folio"}
frame.create {"spread":{"kind":"parent","index":0},"rect":[441,552,756,582],"content":"text","text":"\ue000"}
text.select {"story":"$6.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Folio Right"}
# --- apply the parent to all four document pages ---
layout.pages.applyParent {"pages":[0,1,2,3],"parent":"A"}
document.inspect {}
```

Read-back: every page `parent:"A-Parent"`, sides 1 right / 2 left / 3 right / 4 left, margins as given.

1. **No `Page Number` text variable.** `variables.insert {"name":"Page Number"}` fails with
   `no variable 'Page Number'`. `variables.list` only has chapter number, dates, file name,
   last page number, running header. The automatic page number is a **special character**:
   U+E000 (`PAGE_NUMBER` in `crates/doc/src/story.rs`). Pass `"\ue000"` inside `text` or
   `text.insert`. Related code points: U+E001 section marker, U+E007 next page, U+E008 prev page.
2. **`$N` indices count every command line**, including ones that return `null`. The first run
   referenced `$5.story` for the second frame, but the frame was step 6 → error
   "`$5.story`: no `story` in null". Count steps carefully; comments/blank lines do not count.
3. **`--scale` / `--page` bind to the *following* export.** `run ... --all-pages DIR --scale 1`
   errors: "--scale has no --export or --all-pages after it". Put `--scale 1 --all-pages DIR`.
4. **A new document already has parent `A-Parent` (id 4).** `layout.parents.new` makes `B-Parent`.
   Use the built-in one (apply with `parent:"A"`, prefix accepted).
5. `focus: 9999` past the end is accepted and selects the whole story (no need to know byte length).
6. `frame.create` rect is **spread coordinates** on the parent spread: left page x 0–396,
   right page x 396–792 (facing parent is two pages side by side, height 612).

## Paragraph and character styles, baseline grid, threaded frames, text wrap

```
file.new {"units":"points","width":396,"height":612,"pages":2,"facingPages":false,"margins":45,"bleed":0,"title":"Styles and Threads"}
# baseline grid: 14 pt lines starting at the top margin
document.preferences {"baselineGrid":{"start":45,"increment":14,"relativeTo":"topMargin","color":[190,190,255],"viewThreshold":75}}
style.paragraph.create {"name":"Head","para":{"align":"left","spaceAfter":10},"chars":{"size":30,"leading":{"kind":"points","value":34}}}
style.paragraph.create {"name":"Body","para":{"align":"left","hyphenate":true,"firstLineIndent":12,"gridAlign":"allLines"},"chars":{"size":10.5,"leading":{"kind":"points","value":14}}}
style.character.create {"name":"Emph","chars":{"fontStyle":"Italic"}}
frame.create {"rect":[45,45,351,105],"content":"text","text":"Layout test"}
text.select {"story":"$5.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Head"}
# two threaded body frames on page 1; the story overflows both
frame.create {"rect":[45,120,351,380],"content":"text","text":"Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit.\nEsse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim.\nAd minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim.\nId est laborum lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit.\nIn voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna.\nAliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia.\nDeserunt mollit anim id est laborum lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure.\nDolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore.\nEt dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in.\nCulpa qui officia deserunt mollit anim id est laborum."}
frame.create {"rect":[45,390,351,567],"content":"text"}
text.thread {"from":"$8.id","to":"$9.id"}
text.select {"story":"$8.story","anchor":0,"focus":99999}
style.paragraph.apply {"name":"Body"}
text.select {"story":"$8.story","anchor":0,"focus":48}
style.character.apply {"name":"Emph"}
# graphic frame, then place the generated PNG into it
frame.create {"rect":[225,165,345,265],"content":"graphic"}
file.place {"path":"/scratch/…","frame":"$15.id"}
object.textWrap {"mode":"boundingBox","offset":14,"ids":["$15.id"]}
document.inspect {}
```

1. **Baseline grid `relativeTo` has only `topOfPage` / `topMargin`** — `"margin"` errors with
   `unknown variant 'margin', expected 'topOfPage' or 'topMargin'`.
2. **Paragraph baseline alignment is `para.gridAlign`** with values `none | allLines |
   firstLineOnly` (source: `attrs/para_attrs.rs`, enum `GridAlign`). It does not appear in
   `type.para`'s truncated help text — verify in `describe style.paragraph.create` output or source.
3. **`leading` is a character attribute**, not paragraph: `chars: {leading: {kind:"points", value:14}}`
   (or `{kind:"auto"}`).
4. **A too-short heading frame silently overset.** 30 pt text in a 60 pt frame wrapped to two
   lines (68 pt) and `overset` came back true. Shorten the text or enlarge the frame; always
   check `stories[].overset`.
5. **`--page N` in `run --export` is 0-based**, unlike `file.exportPdf`'s `pages` (1-based).
   `--page 1` rendered the blank second page (0 glyphs). Use `--page 0` for the first page.
6. `text.select ... focus:9999/99999` selects past the end harmlessly — good for "whole story"
   when byte length is unknown.
7. `type.selectionAttrs` is the way to read which paragraph/character style a run has;
   `document.inspect` gives style *names* only, not per-paragraph assignment.
8. `style.paragraph.apply` at a caret/no selection applies to the current paragraph only;
   select the story range first to style everything.

## Tables (a form grid)

```
file.new {"units":"points","width":595,"height":842,"pages":1,"margins":45,"title":"Form Grid"}
style.paragraph.create {"name":"Form Cell","para":{"align":"left"},"chars":{"size":9}}
style.paragraph.create {"name":"Form Label Text","para":{"align":"left"},"chars":{"size":9,"fontStyle":"Bold","fill":"[Paper]"}}
style.cell.create {"name":"Form Label","fill":"[Black]","insets":4,"vj":"center","paragraphStyle":"Form Label Text"}
style.cell.create {"name":"Form Data","insets":4,"vj":"center","paragraphStyle":"Form Cell"}
style.table.create {"name":"Form Table","header":"Form Label","body":"Form Data","border":{"weight":0.5,"color":"[Black]"}}
frame.create {"rect":[45,60,550,700],"content":"text","text":"Field\tMeasure A\tMeasure B\tCode\tDate\tQty\tNotes\nItem 01\t\t\t\t\t\t\nItem 02\t\t\t\t\t\t\nItem 03\t\t\t\t\t\t\nItem 04\t\t\t\t\t\t\nItem 05\t\t\t\t\t\t\nItem 06\t\t\t\t\t\t\nItem 07\t\t\t\t\t\t\nItem 08\t\t\t\t\t\t\nItem 09\t\t\t\t\t\t\nItem 10\t\t\t\t\t\t\nItem 11\t\t\t\t\t\t\nItem 12\t\t\t\t\t\t"}
text.select {"story":"$6.story","anchor":0,"focus":99999}
table.convertFromText {"tableStyle":"Form Table","width":505}
table.options {"headerRows":1}
# one label cell spanning two body rows (rows 6-7 of the table, 0-based incl. header)
table.merge {"rows":[6,7],"cols":[0,0]}
# the merge concatenates the two labels — replace with one group label
table.setCell {"rows":[6,6],"cols":[0,0],"text":"Section B"}
table.setRowHeight {"height":36,"mode":"exactly","rows":[0,12]}
# dark label cells: header row and the whole label column
style.cell.apply {"name":"Form Label","rows":[0,0],"cols":[0,6]}
style.cell.apply {"name":"Form Label","rows":[1,12],"cols":[0,0]}
table.get {}
```

1. **Tab-delimited text → table** is by far the cheapest way to fill many cells:
   `table.convertFromText {tableStyle, width}` with default separators (tab / paragraph).
   `columns:` is only for when both separators are the same.
2. **`convertFromText` does not create a header row** (`headerRows:0`), and the table style's `header` cell
   style is applied nowhere. `table.options {"headerRows":1}` marks row 0 as a header, but in the training-log
   build row 0 still drew with the body cell style: apply the header cell style explicitly with
   `style.cell.apply {story, table, name, rows:[0,0], cols:[0,last]}` (this recipe does so in step 13).
3. **Merging concatenates the cells' text** — the merged label came back `"Item 06\nItem 07"`.
   Overwrite with `table.setCell {rows:[6,6], cols:[0,0], text:"Section B"}` (target the first row
   of the span; `rows:[6,7]` targets the whole span and is refused as a range in some commands).
4. **Row selector is 0-based including the header row.** `setRowHeight {rows:[0,12]}` covers all 13.
5. **Cell style is the way to colour label text white+bold.** `type.char` at the table anchor does
   not reach cell text (selection at story byte 0 is the U+E009 anchor, style `[Basic Paragraph]`).
   Put `fontStyle:"Bold"` and `fill:"[Paper]"` in the cell style's `paragraphStyle` characters.
6. **`table.select` needs a table in scope**: pass `table:<id>` (from `table.get`/`convertFromText`);
   `table.select {rows:[0,0]}` alone fails with "place the insertion point in a table".
7. Cell text lives in per-cell stories — `story.get {story:9}` shows only the anchor (length 4).
   Read content with `table.get`; read cell text formatting via `table.select` + `type.selectionAttrs`.

## Lessons from a real form (a one-page training log, half-letter)

- `table.convertFromText` returns `{rows, table}` only — **no `story`**. Address the table with the text frame's
  story plus the table id: `{"story": "$F.story", "table": "$T.table"}`.
- The table style's `header` cell style is **not applied** after `table.options {headerRows:1}` either: the
  header row kept the body cell style. Apply it explicitly:
  `style.cell.apply {story, table, name:"Head Cell", rows:[0,0], cols:[0,N]}`.
- Alternating row fills work from `table.options {altRows:{first:1, firstColor:"[None]", next:1,
  nextColor:"Pale", nextTint:0.55}}` (a tint without a tint swatch).
- Row heights: `table.setRowHeight {height, mode:"exactly", rows:[a,b]}`; column widths per column with
  `table.setColumnWidth {width, cols:[c,c], rows:[0,last]}`.
- **Text inside a small ellipse frame disappears** (an 11 pt circle with a 7 pt letter drew nothing). Draw the
  circle as a graphic frame (`frame.create {shape:"ellipse", content:"graphic"}` + `object.stroke`) and put a
  separate text frame on top, centred with `object.textFrameOptions {inset:0, verticalJustification:"center"}`
  on the selected frame (`selection.set {ids:["$F.id"]}` first; it acts on the selection).
- `frame.create` rect is `[x0,y0,x1,y1]` in points from the spread's top-left; pages of a non-facing document are
  their own spreads.
- Bundled fonts: **Source Sans 3** (Regular, Bold) and **Source Serif 4**; `type.char {attrs:{fontFamily,
  fontStyle}}` returns `{warnings}` when a family/style is missing (e.g. "Inter Bold (using Inter SemiBold)")
  and `null` when it resolves.
