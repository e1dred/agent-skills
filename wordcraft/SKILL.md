---
name: wordcraft
description: Verified working knowledge for driving the WordCraft word processor (storytold/wordcraft) from an AI agent — live editing through its control server / MCP bridge, headless builds with wordcraft-cli, exact command parameter formats, formatting recipes and known traps. Load before any WordCraft task, and add what you learn at the end of it.
---

# WordCraft

Field notes from real tasks, tested on **WordCraft 0.10.0** (Linux AppImage). If `wordcraft-cli --version`
reports something newer, treat anything below as "probably still true" and re-check it before relying on it.

## Keep this file growing

This guide is built up as tasks happen. At the end of every WordCraft task:
- Add any command, parameter format, recipe or trap you verified to the matching section below.
- Correct anything here that turned out to be wrong (don't leave stale claims).
- Only record what you actually confirmed (by rendering, `inspect`, or reading back) — mark guesses as unverified.
- Keep it general: no personal data, names or machine-specific paths (this file is meant to be shared).
- Add a dated line to the log at the bottom.

## Official docs (read these first; this guide adds what they lack)

Repo: https://github.com/storytold/wordcraft
- `docs/mcp.md` — **the property reference**: full CharProps / ParaProps tables, Border and colour formats,
  tool arguments, file confinement. Raw: https://raw.githubusercontent.com/storytold/wordcraft/main/docs/mcp.md
- `docs/control-protocol.md` — control port, key file, methods (`engine.execute`, `ui.*`, `file.*`).
- Live command list: `engine.commands {"search":…}` / `wordcraft-cli commands --json`; MCP resources
  `wordcraft://commands` and `wordcraft://document`.
Not covered there (as of 2026-10): `styles.create` side effect, `list.define`, bold-off-overrides-style,
recipes. Those live below.

Unverified hints from the docs: CharProps has a `link` field (URL or `#bookmark`) — a possible alternative to
`select.text` + `insert.link`; colours also accept `[r,g,b]` or `"Auto"`; `num` 0 removes numbering a style gives.

## Setup

- **CLI from the AppImage:** `wordcraft.appimage --appimage-extract` → copy `squashfs-root/usr/bin/wordcraft-cli`
  somewhere stable (it is self-contained). Check with `wordcraft-cli --version`.
- **Live editing needs the control server:** start the app with `--control PORT` (or `WORDCRAFT_CONTROL_PORT`).
  Launching from the desktop menu does NOT enable it — add `--control PORT` to the launcher's `Exec=` line
  (app updates may reset the launcher). Only one window can own the port; a second instance gets none.
- **Key:** the app writes a key to `<settings>/control-key.<instance>` (e.g. `~/.config/wordcraft/control-key.local-PORT`
  on Linux); `wordcraft-cli mcp --connect 127.0.0.1:PORT` finds it by itself. Requests without it get `unauthorized`.
- **MCP:** `claude mcp add wordcraft -- wordcraft-cli mcp --connect 127.0.0.1:PORT` (live) or
  `... -- wordcraft-cli mcp --automation-read-root DIR --automation-write-root DIR` (headless, confined).
  In bridge mode the root flags are rejected: a running app's file access is not confined.
- **No MCP tools in the session?** `tools/wcmcp.py` talks to the live window directly:
  `WORDCRAFT_PORT=PORT python3 -I tools/wcmcp.py '[["get_text",{}],["ui_inspect",{}]]'` (set `LIM=` for longer output).
  Bridge tools: list_commands, execute, batch, new_document, open_document, save_document, type_text,
  select_text, get_text, inspect_document, render_page, parity, screenshot, click, key, ui_inspect.

## Choosing live vs headless

- **Live** (user watches): bridge MCP / `tools/wcmcp.py`. Check `ui_inspect` first: `title`, `dirty`.
  Never replace or close a document with unsaved changes (`file.close` without `force` refuses; keep it that way).
- **Headless** (build, then show): `wordcraft-cli run --script s.json` → `render` pages → look → fix.
  Safer for big rebuilds; open the result for the user afterwards (launch the app with the file).
- Editing a file that is open in a window: edit the file on disk, then tell the user to close the window
  WITHOUT saving and reopen — saving from the old window would overwrite the change.

## CLI essentials (verified)

```
wordcraft-cli run --template blank --script s.json            # {"template","commands":[...],"save":["a.docx","a.pdf"]}
wordcraft-cli run --file in.docx --cmd 'id={json}' ... --save out.docx [--print]   # --print shows each result
wordcraft-cli inspect f.docx      # JSON: blocks (style, text, props, runs), sections, properties
wordcraft-cli info f.docx         # pages, words, paragraphs, properties
wordcraft-cli text f.docx
wordcraft-cli render f.docx out.png --page N --scale S
wordcraft-cli convert in.docx out.pdf
wordcraft-cli commands [--json]   # ~640 commands; --json gives each command's params string
```
Script commands are `{"command": id, "params": {...}}` or a bare id string. Relative paths in the script's
`save` list resolve against the script's folder, but paths inside command params resolve against the working
folder (per docs/mcp.md) — use absolute paths. A failing script command stops the run and nothing is saved.

## Property names (verified via `inspect`)

Paragraph props (`para.set {"props":…}`, `styles.modify {"para":…}`):
`spaceBefore`, `spaceAfter` (pt), `lineSpacing {"rule":"multiple","value":1.0}`, `indentLeft`,
`indentFirst` (pt, negative = hanging), `keepNext`, `tabs [{"pos":pt,"align":"right","leader":"none"}]`,
`borders {"bottom":{"style":"single","width":1,"color":"1F3864","space":1}}`, `align` ("center", "justify"),
`numbering {"level":0,"num":N}` (num 0 = no list).

Character props (`format.set {"props":…}`, `styles.modify {"chr":…}`):
`font`, `fontCs`, `size`, `sizeCs` (pt), `bold`, `italic`, `caps`, `color` ("RRGGBB").

Section props: `marginTop/Bottom/Left/Right`, `pageW/pageH` (pt; Letter = 612×792).

## Commands (verified)

- Page: `layout.margins {"top":36,"bottom":36,"left":43.2,"right":43.2}` (pt).
- Styles: `styles.create {"name","basedOn"}`, `styles.modify {"style","chr","para"}`, `para.style {"style"}`,
  `styles.list`, `styles.inspect`. Built-in "Heading 1" can be restyled (good for ATS headings).
- Text: `text.insert {"text"}` (a `\t` in the text is a real tab), `text.newParagraph`.
- Character: `format.bold {"value":true}`, `format.resetChar` (back to the style's formatting), `format.state`.
- Lists: `list.define {"levels":[{"format":"bullet","text":"•","alignedAt":4,"indentAt":15,"follow":"tab",
  "tabAt":15,"color":"1F3864"}],"apply":true,"name":…}` returns `"num":N`; then put later paragraphs in it
  with `para.set {"props":{"numbering":{"level":0,"num":N}}}`.
- Numbered list: same command with `{"format":"decimal","text":"%1.","alignedAt":0,"indentAt":18,"follow":"tab",
  "tabAt":18}` → "1. 2. 3." (in a blank document `num` came back 1). End the list on the next paragraph with
  `para.set {"props":{"numbering":{"level":0,"num":0}}}`.
- Selection + links: `select.text {"text":…}` then `insert.link {"url":"mailto:…"}` or `{"url":"https://…"}`
  keeps the selected text as the link text.
- Tables: `insert.table {"rows":3,"cols":3,"style":"Table Grid"}` puts the caret in the first cell (`inspect`
  shows the style as `TableGrid`). Fill cells with `text.insert`; `caret.right` at the end of a cell's text moves
  to the next cell, wrapping to the next row. Header row: put the caret in row 1 (`caret.docStart`, then
  `caret.paraDown` when one paragraph sits above the table), then `table.selectRow` → `table.shading {"color":"D9E2F3"}`
  → `format.bold {"value":true}` → `table.repeatHeader`. `caret.docEnd` then lands in the paragraph after the table.
  `inspect` shows a table block as `{"type":"table","rows","cols","cells":[[…]]}`.
- **Quickest table:** type rows as tab-separated paragraphs, select them (`caret.docStart`, then
  `caret.docEnd {"extend":true}`), then `table.fromText {"separator":"tab","autofit":"contents"}` →
  `table.style {"style":"Table Grid"}` → `table.properties {"align":"center"}`. Gives a compact centred table.
- `table.columnWidth {"width":pt}` sets only the caret's column (others keep theirs);
  `table.cellAlign {"value":"bottomRight"}` writes vertical `vAlign` plus paragraph `jc` for the caret cell.
- Header/footer: `insert.header {"text":…}`, `insert.footer {"preset":"pageNumber"}` (centred page number).
  Both leave the caret IN the header/footer: follow each with `insert.closeHeader` (it closes footers too).
- Page numbers: `insert.pageNumber {"position":"bottom","align":"right","format":"x of y"}` makes a footer that
  renders "Page 2 of 2" (numbers bold); unlike `insert.footer` it leaves the caret in the body.
- Columns: `layout.columns {"count":2,"space":18,"separator":true}` with no `apply` changes the WHOLE section,
  including text above the caret. `"apply":"forward"` starts the columns at the caret: it adds a continuous
  section break, as an empty paragraph (`sectionBreak: true` in `inspect`). `layout.break {"kind":"column"}`
  jumps to the next column (a `\u000e` in the text). Kinds also include `nextPage|continuous|evenPage|oddPage`.
- Links: `insert.link {"url":…,"text":…}` inserts linked text styled `Hyperlink` (blue, underlined).
  The CharProp `format.set {"props":{"link":URL}}` on a selection also creates a working link (checked in the
  .docx rels), but the text keeps its normal look: no blue, no underline.
- Table of contents: `references.toc {"levels":2,"title":"Contents"}` at the top, headings below with
  `para.style "Heading 1"`, then `references.updateToc` at the end → TOC lines with dot leaders, page numbers,
  links to `_Toc…` bookmarks on the headings.
- Footnotes: `references.footnote {"text":…}` returns `{"id":N}` and leaves the caret IN the footnote. Get back
  with `caret.set {"pos":{"story":"body","path":[para],"off":N}}` (reliable). `references.nextFootnote` also
  happened to land after the mark in a one-note test. NOT `insert.closeHeader`: that goes to the start of the body.
- Pictures: `insert.picture {"path":ABS,"width":pt,"alt":…}` keeps the aspect ratio (returns width/height).
- Find/replace: `edit.replaceAll {"text","with","matchCase"?,"wholeWord"?}` returns `{"replaced":N}`.
  `^p` in `with` splits into new paragraphs ("One; Two" with `"; "`→`^p` gave two paragraphs); `^t` = tab.
- Review: `file.setAuthor {"name"}` first (sets comment/revision author and the file's lastModifiedBy; default
  "WordCraft User"). `select.text` → `review.newComment {"text"}` returns `{"id":N}`; `review.reply {"id","text"}`;
  `review.resolveComment {"id","value":true}`; `review.comments` lists them (author, parent, resolved).
  `review.trackChanges {"value":true}` → later edits become revisions; `review.changes` lists them
  (kind insert/delete, text, author); `review.acceptAll` keeps the edits, `review.rejectAll` restores the original (both verified).
  For anonymous output: `file.privacyOptions {"removePersonalInfo":true}` (untested).
- Landscape page in a portrait document: `layout.break {"kind":"nextPage"}` then
  `layout.orientation {"value":"landscape"}` → only the new section turns (792×612); the first stays portrait.
- Inline formatting (select with `select.text` first): `format.highlight {"color":"yellow"}`,
  `format.subscript` / `format.superscript` (stored as `vertAlign`), `format.strikethrough {"value":true}`,
  `format.spacing {"points":3}` (letter spacing), `format.color {"color":"C00000"}`. `insert.symbol {"char":"©"}`.
- Paragraph look: `para.shading {"color":"E7E6E6"}` (null clears), `para.borders {"kind":"left","width":3,
  "color":"1F3864"}` (kind `none` clears all); `line spacing` rules are `multiple|atLeast|exactly` (NOT `exact`).
- Custom style: `styles.create {"name":"Callout","basedOn":"Normal"}` → `styles.modify {"style":"Callout",
  "chr":{"italic":true,"color":"7F3F00","size":12},"para":{"indentLeft":24,"lineSpacing":{"rule":"multiple","value":1.5}}}`
  → `para.style` back to Normal afterwards (create applies it to the caret paragraph).
- Captions: `references.caption {"label":"Figure","text":"…","position":"below"}` after a picture adds a `Caption`
  paragraph "Figure 1: …" with a `SEQ Figure` field (auto-numbered). Also `Table` and `Equation` labels.
- Drop cap: `insert.dropCap {"lines":3}` on a paragraph (prop `dropCap` in `inspect`; renders as a large initial).
- Shapes/text boxes: `insert.shape {"kind":"star","width":50,"height":50}` (also rectangle, ellipse, arrow, line…),
  `insert.textBox {"text":"…","width":120,"height":40}`. **A text box leaves the caret inside it** (like headers):
  get out with `caret.set {"pos":{"story":"body","path":[0],"off":0}}`.
- Cover page: `insert.coverPage {"title","subtitle","author"}` inserts ~25 paragraphs at the top (spacer blanks, Title
  with rule, Subtitle, author, auto-date ending in a page break). Following text lands after it.
- Multilevel numbering: `list.multilevelPreset {"preset":"headings"}` returns `num`; the first paragraph becomes
  Heading 1 numbered "1"; further paragraphs get `para.set {"props":{"numbering":{"level":1,"num":N}}}` → "1.1", "1.2";
  level 0 again → "2". Presets: `headings|article|outlineHeadings|chapter`.
- Page numbering style: `layout.pageNumberFormat {"format":"lowerRoman","start":1}` (also upperRoman, letters).
- Different first page: `layout.differentFirstPage` (toggle). Footer/header created AFTER it (caret on page 1) goes to
  the FIRST-page slot, so pages 2+ show nothing. To number pages 2+ only: `layout.differentFirstPage`, then
  `insert.createFooter {"page":1}`, `text.insert "Page "`, `insert.pageField`, `insert.closeHeader` → page 1 blank,
  page 2 "Page 2" (verified with pdftotext per page).
- Charts: `insert.chart {"type":"column","data":{"categories":[…],"series":[{"name","values":[…]}]},"title"?,"legend"?}`
  renders a native chart (checked). Equations: `insert.equation {"latex":"x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}"}`
  renders as display math, and the caret stays in the math: `caret.docEnd` before more text.
  Fields: `insert.field {"instr":"DATE \\@ \"yyyy\"","result":"2026"}`.
- Table cells: merge across = `table.selectCell`, `caret.right {"extend":true}` per extra cell, `table.merge`
  (`inspect` then shows a one-cell row). Also `table.borders {"kind":"inside","width":0.5,"color":…}`,
  `table.cellMargins`, `table.look {"headerRow","bandedRows"}`, `table.rowHeight {"height","rule":"atLeast"}`,
  `table.altText` (all accepted; only merge, shading and borders were checked visually).
- Convert: `wordcraft-cli convert in.docx out.{pdf,odt,html,md}` all work; `.md` keeps only text and the equation's
  linear form (charts, images and tables are not carried in the test document).
- Header/footer layout: `insert.createHeader` (caret goes in), type `Left\tCenter\tRight`, then
  `para.set {"props":{"tabs":[{"pos":234,"align":"center","leader":"none"},{"pos":468,"align":"right","leader":"none"}]}}`
  (pos = text width / 2 and text width; 1" margins on Letter = 468) → three zones, verified by render. Without tab
  stops the text just sits at the default stops. `insert.header {"preset":"blankThree"}` fills in literal
  "[Type here]" placeholders and leaves the caret at the start, so your text is inserted before them: avoid it.
- Page setup: `layout.size {"name":"A4"}` (595.3×841.9), `layout.lineNumbers {"value":"restartPage","countBy":1}`,
  `layout.verticalAlign {"value":"center"}` (also `layout.hyphenation`, `layout.differentOddEven`) — all checked
  in `inspect` section props and by render.
- Selecting: `select.text {"text","occurrence":N}` (1-based) picks the Nth match. `edit.find` with `"regex":true`
  works (`b[a-z]+` found "bird"); with `"wildcards":true` it is Word-style (`<b*>`, `(c)at`), NOT regex: my `b[a-z]+`
  wildcard found nothing. `edit.find` returns `{"count","matches":[{start,end}]}` and does not change the
  selection when there are no matches (a later `format.*` then hits the OLD selection: always check `count`).
  Capture groups in `edit.replaceAll`: use `"wildcards":true` with `(c)at` → `\\1AT` ; with `"regex":true`
  `\\1` and `$0` were left as literal text.
- Macros: `tools.macros {"define":{"name":"Shout","steps":[{"command":"format.bold","params":{"value":true}},
  {"command":"format.allCaps"}]}}` then `tools.macros {"run":"Shout"}` runs the steps on the selection.
- Proofing: `review.wordCount` → words/characters/pages; `review.issues` → list of spelling/grammar issues with
  offsets and suggestions (found "jumpd" and a capitalisation).
- Page break: `insert.pageBreak` adds a `\f` inside the current paragraph (not a new paragraph); text continues
  on the next page in the same paragraph.
- Properties: `file.properties {"title","author","subject","keywords"}`.
- Save/export: `file.save {"path"}`, `file.saveAs {"path"}`, `file.exportPdf {"path"}`.
- `file.open {"path"}` / `file.close {"force"?}` exist; untested whether `file.open` replaces a dirty doc.

## Traps (each one cost time)

- **Unknown property keys are silently ignored** — no error (documented in docs/mcp.md). Confirm every new
  key with `inspect`. Example: `para.set {"props":{"spaceAftr":12}}` succeeds and changes nothing.
- **`styles.create` also applies the new style to the current paragraph.** Reset with `para.style` afterwards.
- **`format.bold {"value":false}` is direct formatting and overrides a style's bold.** For a bold label inside a
  line: `format.bold true` → insert → `format.resetChar` → insert the rest. Never set bold false "to be safe".
- **`text.newParagraph` carries the list over:** the new paragraph keeps the previous one's numbering
  (verified with `inspect`). Set `numbering num 0` on the first paragraph after a list.
- **`insert.header` / `insert.footer` leave the caret in that header/footer** — without `insert.closeHeader`
  the rest of the script's text ends up in the footer, and `inspect` shows an empty body.
- **`references.footnote` leaves the caret in the footnote**, same as headers. And `insert.closeHeader` always
  puts the caret at the START of the body, so after a header/footer added mid-script, move with `caret.docEnd`.
- A table inserted inside a column layout keeps full-page-width columns and runs past the column; set widths.
- **`edit.replaceAll` ignores case by default and does not keep it:** "colour"→"color" also turned "Colour" into
  "color". Use `"matchCase":true` and one call per capitalisation.
- With tracked changes on, `inspect`/`text` show deleted text too ("graygrey"): runs carry `ins`/`del` ids.
- Script failure message names the command index and the bad variant ("unknown variant `exact`, expected one of …"):
  read it, the allowed values are listed. Nothing is saved when a script command fails.
- `inspect` shows a page-number field's cached text ("Page 1 of 1" in a 2-page document); `render` shows the
  real numbers. Check page numbers by rendering, not with `inspect`.
- `--print` output from `run` shows each command's result; without it failures are easy to miss.
- Right tab must sit at the text width: page width − left − right margin (612 − 2×43.2 = 525.6 → use 525).

## Verify before reporting

- `info` for page count; `render` each page and look at it (`--scale 1.3`; crop to zoom).
- `pdftotext -layout` on the PDF to check ATS reading order; `pdffonts` for embedded fonts.
- Links: unzip the .docx and check `word/_rels/document.xml.rels` for the targets.

## Recipes

- `recipes/resume_ats.py` — ATS-friendly résumé: Calibri 10.5, 0.6"/0.5" margins, navy Heading 1 with bottom
  rule, job title with right-tab dates, italic employer line, navy bullets, linked email/profile, ~2 pages.
  Sample content is fictional; replace the `RESUME` data at the top.
  Usage: `python3 -I recipes/resume_ats.py /abs/out.docx /abs/out.pdf > s.json && wordcraft-cli run --script s.json`.

## Log

- 2026-10-24: Initial notes from building and linking an ATS résumé (WordCraft 0.10.0).
- 2026-10-24: Linked the official docs (docs/mcp.md, docs/control-protocol.md); corrected path resolution.
- 2026-10-24: Generalized for sharing; résumé recipe made data-driven with fictional sample content.
- 2026-10-24: Numbered lists; confirmed that new paragraphs inherit list numbering.
- 2026-10-24: Tables (fill, header row shading/repeat, from text), headers/footers, x-of-y page numbers,
  page breaks, columns, links, TOC, footnotes, pictures, find/replace, comments, tracked changes.
- 2026-10-24: Header tab zones, page setup, regex/wildcard find, macros, proofing.
- 2026-10-24: Inline formatting, custom styles, captions, drop cap, shapes/text boxes, cover page, multilevel lists,
  roman page numbers, first-page-different footers, charts, equations, table merge, convert formats.
