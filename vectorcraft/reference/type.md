# Type

Type is split between `text.*` (content, ranges, frames, threading, tabs) and `type.*` (orientation,
case, outlines, scale/step, ruby, smart punctuation). Character and paragraph styles are
`charStyle.*` / `paraStyle.*`.

## Creating and editing text

- `text.create {x, y, text, size?, font?, style?, color?, rotation?, vertical?, area?} → {id, bounds}`
  — point type by default; with `area:{width, height, fit?}` it is area type (a frame).
  Verified: `text.create {x:100,y:600,text:"Hello",size:24}` → id, bounds width 52.8.
- `text.setText {id?|ids?, text} → {ids}` replaces the contents (keeps the first run's style).
- `text.getRange {id, start?, end?} → {text, runs:[{text, style}], length}` — read runs and styles.
- `text.editRange {id, start, end, insert?|runs?} → {id, caret}` — replace a byte range.
- `text.setRangeStyle {id, start, end, font?, style?, size?, leading?, tracking?, kerning?,
  baselineShift?, hScale?, …} → {id, runs}`.
- `text.setStyle {ids?|id?, font?, style?, size?, leading?, tracking?, justify?, fill?, …}` is the
  whole-object version. Both refuse with "nothing to change" if you pass no styling at all.
- `type.changeCase {ids?, case}`, `type.smartPunctuation`, `type.insert`, `type.fillPlaceholder`,
  `type.ruby {…}` (all verified changing the model).
- `type.orientation.vertical|horizontal`, `type.createOutlines → {ids}` (type becomes paths),
  `type.size.increase|decrease|increaseByFive|decreaseByFive`, `type.step`,
  `type.resetTracking`, `type.resetHorizontalScale`, `type.opticalMarginAlignment`,
  `type.systemLayout`, `type.fractionalWidths`.
- `type.convertToAreaType {ids}` / `type.convertToPointType {ids}` change the frame kind
  (verified; converting an already-point text is a no-op `ran`).
- Area type frames: `text.areaOptions {ids?|id?, width?, height?, rows?, columns?, gutter?, fit?,
  firstBaseline?, …}`, `text.reshapeArea {id, anchors:[[subpath, anchor]…], dx, dy}` (anchor
  references are **`[subpath, anchor]` pairs**, not `{x,y}`), `text.fitHeadline {ids?}` (verified:
  tracking set to fill the frame).
- Type on a path: `text.createInPath {path, text, …}` (needs a path object id),
  `text.reshapePath`, `type.pathOptions` — both refuse unless type on a path is selected.
- Threading: `text.thread.create {ids…}` (select at least two objects), `.add`, `.remove`,
  `.releaseSelection`, `.break`, `.info`.
- Tabs and lists: `text.tabs.set {stops:[{position, align?, leader?, alignOn?}], ids?, start?, end?}`,
  `text.tabs.get`, `text.tabs.clear`; `text.startList {id, at?}` (needs text typed with a list
  trigger), `text.convertListToText {ids}`.
- `text.discardEmpty {id?} → {removed}`, `text.touchType {id, start, dx?, dy?, …}` (one character),
  `text.insertInline` (only while editing text).

## Fonts

- `text.fonts → [{family, missing, missingGlyphs, objects, resolved…}]` lists the fonts the
  document uses (verified: Source Sans 3 on the default point text).
- `text.fontList → {families:[…]}` lists installed families (126 families / 549 faces in this
  headless environment; includes Adwaita Sans/Mono and BIZ UD fonts).
- `text.rescanFonts → {faces, families}`, `text.missingFonts → {count, fonts}`,
  `text.findFontFiles → {state, fonts}` then `text.addFontFiles {files}`,
  `text.replaceFont {from:{family, style?}, to:{family, style?}, selectionOnly?}` (a nested
  `from.family` is required).

## Styles

- `charStyle.list → {styles:[{name, attrs, uses}]}`; defaults are `[Normal Character Style]`
  (paragraph: `[Normal Paragraph Style]`).
- `charStyle.new {name?, …} → {name}` (verified "Character Style 1");
  `charStyle.setAttrs`, `charStyle.apply {name, clearOverrides?, ids?|id?, start?, end?}`,
  `charStyle.duplicate`, `charStyle.redefine`, `charStyle.rename`, `charStyle.delete`,
  `charStyle.edit` (new in 0.21.0), `charStyle.unused`.
- Same set for `paraStyle.*`.
- `charStyle.apply` and `paraStyle.apply` need **text objects selected** (error: "no text objects
  selected") — select the text first, or pass `ids`/`id`.
- Renaming or deleting the built-in `[Normal …]` style refuses (it can't be renamed/deleted).

## Practical notes

- Type ids behave like any object: `select.set {ids:[textId]}`, then `text.*` commands that
  default to the selection work.
- `text.create` returns `bounds` **before** the text is styled further; re-read `document.node
  {id}` or `text.getRange` after styling.
- A byte range (`start`/`end`) is UTF-8 bytes, not characters — for non-ASCII text read
  `text.getRange` first and use its `length`.
