# WordCraft reference: command reference

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Version note (0.11.0)

WordCraft 0.11.0 added 5 commands (638 → 643), none removed: `mailings.first`, `mailings.last`, `mailings.goToRecord {"record":2}` (1-based; the parameter is `record`, not `index`) → `{of:3,record:2}`, `mailings.printDocuments` → `{records:3}`
(after `mailings.start`, `mailings.recipients`, `mailings.insertField` and `mailings.preview {"on":true}`), and `view.readPageColor {"color":"none|sepia|inverse"}`. Of the older sections, nine headless ones were re-run on both versions and gave identical output (see the `> Versions` line under each); the rest of this file has not been re-run on 0.11.0.

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

> **Versions:** mostly 0.10.0 (2026-10-24). Re-verified on 0.11.0 by the style builders (2026-10-25): `layout.size/margins`, `styles.create/modify`, `list.define`, `insert.picture`, `insert.table` + `table.*`, `insert.pageNumber`, `insert.header` + `insert.pageField`, `layout.columns`, `references.footnote`, `select.text` + `insert.link`, `file.properties`. Everything else in this list has **not** been re-run on 0.11.0.

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
- Floating pictures: right after `insert.picture` the new picture is the selected object, so
  `arrange.wrap {"wrap":"square"}` then `arrange.position {"preset":"topRight"}` floats it with the text flowing
  around it (render confirmed). Wrap kinds: `inline|square|tight|through|topAndBottom|behindText|inFrontOfText`; also
  `arrange.rotation {"degrees"}`, `arrange.bounds`, `arrange.nudge`, `object.altText`.
- Text characters: `\n` inside `text.insert` is a soft line break (`<w:br/>`), NOT a new paragraph; use
  `text.newParagraph` for that. `text.lineBreak`, `text.nbsp`, `text.nbHyphen`, `text.emDash`, `text.copyright`,
  `text.tab` exist (nbsp and emDash checked).
- Internal links: `select.text` then `insert.link {"bookmark":"name"}` (after `insert.bookmark {"name"}`) or
  `insert.link {"heading":N}` (N = the heading's block index in `inspect`; a `_Toc…` bookmark is created for it).
  Both give `Hyperlink`-styled runs with `link:"#…"`.
- Restyling a built-in heading: `styles.modify {"style":"Heading 1","chr":{"font":"Georgia","size":20,"color":"7F3F00",
  "bold":true},"para":{"spaceBefore":18,"spaceAfter":6,"borders":{"bottom":{"style":"single","width":1,"color":"7F3F00",
  "space":1}}}}` (rendered correctly). Nested bullets: `list.define` with two `levels` (second `alignedAt":18,
  "indentAt":36`, text "–") `apply`:true puts paragraphs in `ListParagraph` style; level 1 via `numbering {"level":1,"num":N}`.
- Document properties are read back from `inspect` → `properties` (`creator` = the `author` you set).
- Page break: `insert.pageBreak` adds a `\f` inside the current paragraph (not a new paragraph); text continues
  on the next page in the same paragraph.
- Properties: `file.properties {"title","author","subject","keywords"}`.
- Save/export: `file.save {"path"}`, `file.saveAs {"path"}`, `file.exportPdf {"path"}`.
- `file.open {"path"}` / `file.close {"force"?}` exist; untested whether `file.open` replaces a dirty doc.

## Sweep of every remaining command id on a blank document (2026-10-26, 0.11.0, headless; effect checked by `inspect`, partly by render)
> **Versions:** 0.11.0 only, CLI only. **What this proves and what it does not:** each id was run with `wordcraft-cli run --script` on a blank document holding a heading, two paragraphs, a 2x2 table and a sentence ("quick brown" selected), plus the object or state its family needs (a SmartArt, chart, WordArt, canvas, equation, field, mail-merge list, picture, bookmark/link/comment, outline view, header). Parameters came from `wordcraft-cli commands --json`. Two checks per id: the command returned without an error, and the saved document's `inspect` JSON was compared with the same script WITHOUT the command (changed or not). The seven commands marked R below were also compared by rendering page 1. Effects were NOT otherwise read back or looked at, so "ran" means the command exists and takes those parameters. Scratch files only.
- **Ran and changed the document (77 ids):**

```
arrange.bringForward arrange.copyTo arrange.rotate arrange.sendBackward canvas.expand canvas.scale chart.dataLabels
chart.editData chart.title chart.type design.pageBorders developer.buildingBlock document.setText equation.backspace
equation.enter equation.normalText equation.structureActions fields.lock fields.unlink file.new format.engrave
format.growFont1 format.shrinkFont format.shrinkFont1 format.wordUnderline hf.position insert.deleteBookmark
insert.removeLink insert.spreadsheet insert.timeField layout.documentGrid layout.pageSetup layout.sectionRtl
layout.textDirection outline.demoteToBody outline.level outline.promoteToHeading1 para.alignLeft para.alignRight
para.asianTypography para.defineBullet para.defineNumber para.distribute para.double para.heading3 para.justify
para.ltr para.moveUp para.oneAndHalf para.outdent para.promote para.removeHanging para.rtl picture.iconColor
references.endnote references.tableOfAuthorities smartArt.addShape smartArt.colors smartArt.demote smartArt.items
smartArt.layout smartArt.reset styles.apply table.deleteCells table.deleteColumn table.deleteTable
table.insertColumnLeft table.insertColumnRight table.insertRowAbove text.backTab text.columnBreak
text.deleteWordForward view.draft view.marks view.readMode view.webLayout wordArt.transform
```
- **Ran, changed the rendered page but not `inspect` (R, 7 ids):** `table.distributeRows`, `table.rtl`, `design.pageColor`, `format.textEffects`, `wordArt.style`, `wordArt.textFill`, `wordArt.textOutline`
- **Ran, document unchanged (124 ids).** Most are reads or window/view state (zoom, panes, read mode, caret/selection moves, `document.*`, `readAloud.*`, `tools.customize*`). A few are mutating commands that need a different state to show an effect: `fields.toggleCode|setCode|unlock` (select the field first: `fields.selected` listed the DATE field), `mailings.next|previous` (merge preview on), `chart.legend`, `canvas.fit`, `arrange.wrapText` (a floating picture), `equation.delete`, `references.updateFields|updateAuthorities`, `styles.inspectorClear`, `table.borderPainter`, `design.effects`, `tools.detachTemplate|linkStyles` (no template attached):

```
arrange.selectionPane arrange.wrapText canvas.fit caret.home caret.left caret.pageDown caret.pageUp caret.wordLeft
caret.wordRight chart.legend design.effects design.setDefault developer.control document.inspect document.layout
document.paragraph document.selection document.text draw.highlighter draw.pencil edit.clipboardPane edit.findReplace
equation.delete equation.edit fields.next fields.previous fields.selected fields.setCode fields.toggleCode
fields.unlock file.options file.print font.list font.loadSystem format.fontDialog link.targets list.get
mailings.editRecipients mailings.highlightFields mailings.matchFields mailings.next mailings.previous
mailings.sortRecipients outline.expand outline.showAll outline.showFormatting outline.showLevel1 outline.showLevel2
outline.showLevel3 outline.showLevel4 outline.showLevel5 outline.showLevel6 outline.showLevel7 outline.showLevel8
outline.showLevel9 outline.toggle para.dialog readAloud.next readAloud.playPause readAloud.previous
readAloud.skipCitations readAloud.speed readAloud.status readAloud.stop references.notes references.researcher
references.updateAuthorities references.updateFields review.editor review.previousComment review.proofing
select.addObject select.column select.dragUnit select.extend select.line select.objects select.paragraph
select.sentence select.similar smartArt.textPane styles.inspector styles.inspectorClear styles.pane
table.borderPainter table.selectTable table.viewGridlines text.overtype tools.customizeKeyboard tools.customizeRibbon
tools.detachTemplate tools.linkStyles tools.templates view.accessibilityPane view.altTextPane view.commentsPane
view.darkMode view.fieldCodes view.focus view.formatShapePane view.fullScreen view.fullScreenView view.gridlines
view.hideWhiteSpace view.immersive view.interfaceTheme view.multiplePages view.navigationPane view.newWindow
view.numeral view.onePage view.pageWidth view.readColumnWidth view.readLineSpacing view.readTextSize view.ruler
view.sideToSide view.split view.stylesPane view.vertical view.zoom view.zoom100 view.zoomIn view.zoomOut
```
- **Refused with a reason (23):** `text.toggleUnicode` (select a character code (like 00E9) or one character); `font.add` (/nonexistent.ttf: No such file or directory (os error 2)); `font.remove` ("Nope" isn't a font you added); `para.moveDown` (a table is in the way); `para.demote` (nothing to demote); `outline.demote` (nothing to demote); `outline.moveDown` (already at the bottom); `table.eraser` (there's no border between two cells there); `table.resizeDrag` (there's no table border or resize handle there); `table.selectAt` (there's no table selection area or button there); `table.insertAt` (there's no table selection area or button there); `table.moveDrag` (there's no table selection area or button there); `table.fitColumn` (there's no column border there); `mailings.findRecipient` (bad parameters: `text` (string) is required); `arrange.moveWithText` (not available: arrange.moveWithText: select a floating picture or shape first); `arrange.group` (not available: arrange.group: select two or more pictures or shapes first (Shift+click)); `arrange.ungroup` (not available: arrange.ungroup: select a group first); `smartArt.promote` (this item is already at the top level); `canvas.member` (bad parameters: no member 0 (the canvas has 0)); `hf.next` (not available: edit a header or footer first); `hf.previous` (not available: edit a header or footer first); `tools.updateStyles` (bad parameters: no template is attached; give `path`); `caret.pastCitation` (there's no citation after the caret)
- **Useful read results:** `document.text {}` → `{text}` (paragraphs joined by `\n`, table cells by `\t`); `document.layout {}` → caret rectangle and per-page info (`pages[].firstBlock`, header/footer); `document.selection {}` → `{anchor,focus,format}`; `document.inspect {"text":true}` = `inspect` with text; `select.sentence|paragraph|line {}` → `{anchor,focus}` (a sentence of 45 characters was selected from a caret in it); `link.targets {}` → `{bookmarks,headings:[{block,level,text}],top}`; `list.get {}` → the caret's list levels (as `list.define`); `fields.selected {}` → `[{code,instr,locked,pos,range}]`; `arrange.selectionPane {}` → `[{hidden,index,kind,name,pos,size}]`; `smartArt.items {"items":["One","Two",{"text":"Sub","level":1}]}` returns the whole SmartArt; `mailings.editRecipients {}` → `{headers,records,rows,rules,sort}`; `mailings.matchFields {}` → the address/greeting mapping; `view.zoom {"value":150}` → `{fit:"",zoom:1.5}`; `outline.showLevelN {}` → `{showLevel:N}`; `file.options {"pane":"general"}` → author, checkSpelling, dictionaries; `tools.customizeKeyboard {"command":"format.bold"}` → its keys (`Mod+B`); `readAloud.status {}` → `{state:"stopped",rate:1.0,…}`; `font.list {}` → `{folder:null,fonts:[]}` (no fonts added); `layout.pageSetup {}` → the whole section (columns, header/footer distances, docGrid).
- **Traps and facts:** `text.toggleUnicode` needs a selected character or code (like `00E9`); `para.moveDown`/`outline.moveDown` refuse when a table is in the way or the paragraph is last; `para.demote`/`outline.demote` say "nothing to demote" on a level-1 paragraph; the table mouse commands (`table.eraser|resizeDrag|selectAt|insertAt|moveDrag|fitColumn`) take `{page,x,y,…}` in page points and answer "there's no table border or resize handle there" unless the point sits on one (headless page geometry was not worked out); `arrange.group|ungroup|moveWithText` need a selected floating object ("select two or more pictures or shapes first"); `hf.next|previous` need a header or footer being edited; `mailings.findRecipient` needs `text`; `canvas.member {"index"}` needs a canvas with members; `tools.updateStyles` needs a `path` when no template is attached; `font.add {"path"|"data","name"}` fails on a missing file and `font.remove {"family"}` only removes fonts that were added; `caret.pastCitation` needs a citation after the caret. `view.*` commands that toggle a window pane return a value but nothing renders headless.
