# WordCraft reference: formatting and editing

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Accessibility checker (verified headless)

> Not re-checked: the full fix recipe down to `ok:true`, and the tagged-PDF check.

`file.accessibility {}` → `{"ok":bool,"issues":[{"kind":"error|warning|tip","issue","fix"?,"action"?:{command,params},"pos"}]}`.
On a deliberately flawed document it found 6: picture without alt text (error, fix `object.altText`/`picture.altText`),
table without alt text (`table.altText {title,text}`), table without a header row (`table.repeatHeader`), an empty table row
used as spacing, non-descriptive link text ("click here"), no document title (`file.properties {title}`). After fixing them:
`{"issues":[],"ok":true}`. Fix recipe: `picture.altText {"text":"…"}` right after `insert.picture`; with the caret in a table's
first cell `table.altText` + `table.repeatHeader`; real header text such as `insert.link {"url","text":"Example website"}`.
- **Not caught by the checker**: plain text used as a heading (use `para.style "Heading 1"`), three blank paragraphs in a row.
  Check these yourself with `inspect` (style names, empty `text`).
- `convert x.docx x.pdf` produced a TAGGED PDF (`pdfinfo` → `Tagged: yes`) for both the flawed and fixed file, with the document
  title as the PDF title once `file.properties` has set it.

## Paragraph formatting, lists and editing commands (verified headless; props read back with `inspect`, lists by `pdftotext`)

> Not re-checked: the pagination keeps, multilevel lists, `setNumberingValue`, `para.sort`, copy/paste format, `edit.undoTo`, `edit.goto`, the spike.

Paragraph (one call each; `text.newParagraph` carries the settings forward, see traps):
- `para.align {"value":"left|center|right|justify|distribute"}`; `para.indents {"left":36,"right":36,"firstLine":18}` (pt, negative
  `firstLine` = hanging; props `indentLeft/indentRight/indentFirst`); `para.spacing {"before":24,"after":12}`;
  `para.lineSpacing {"value":1.5}` | `{"atLeast":pt}` | `{"exactly":20}` (prop `lineSpacing {rule:multiple|exactly,value}`).
- Pagination: `para.keepNext`, `para.keepLines`, `para.pageBreakBefore`, `para.widowControl` each `{"value":true}` (all read back
  as props; `pageBreakBefore` made a 2-page document).
- Tabs: `para.tabs {"set":[{"pos":300,"align":"right","leader":"dot"}]}` → "Item .......... $5.00" (also `clear`, `clearAll`).
- Lists: `para.bullets {"kind":"bullet"}` (or one character; `"off":true` ends it), `para.numbering {"kind":"numbered|
  numberedParen|upperLetter|lowerLetter|lowerRoman|outline"}` → "1.", "1)", "i."; `para.setNumberingValue {"value":5}` → 5., 6.;
  `para.multilevel {"kind":"legal"}` + `para.listLevel {"level":1}` → "1. / 1.1. / 1.1.1. / 2."; bullet level 1 renders "○".
  Also `para.restartNumbering`, `defineBullet {"char"}`, `defineNumber {"format","text","start"}`, `promote/demote`,
  `moveUp/moveDown` (moved the caret's paragraph up one: untested otherwise), `para.reset`, `para.heading1…3`.
- **`para.sort {"descending"?:true}` sorts only a real multi-paragraph selection**: `select.all`, or `caret.docStart` then
  `caret.docEnd {"extend":true}` worked (case-insensitive: Apple, mango, Pear). `caret.paraUp {"extend":true}` did NOT select
  paragraphs, so the sort silently did nothing.
Editing:
- `edit.copy`, `edit.cut`, `edit.paste {}` (the internal clipboard, kept after a cut), `edit.pasteText {"text"}` (plain),
  `edit.paste {"html":"<p><b>Bold</b> and <i>italic</i></p>"}` → real bold/italic runs, `edit.pasteSpecial {"as":"text",
  "text":"<b>raw</b>"}` → the tags as literal text.
- `edit.copyFormat` + `select.text` + `edit.pasteFormat` copied bold + a colour onto another word (format painter).
- `edit.undoTo {"count":2}` undoes the last 2 command steps; `edit.redo`; `edit.goto {"page":1}` (1-based) moved the caret to the
  start of page 1; `edit.spike` cuts the selection into the spike, `edit.insertSpike` pastes it back (collects text, then
  empties); `edit.replace`/`findNext`/`advancedFind` exist (not run).

## Next-tier workflows (verified headless)


**Seeing results:** `wordcraft-cli run --file F.docx --cmd id={json} --print` (or a `--script`) prints every command's result (the older notes only showed "wrote …"). `--author NAME` names who the tracked changes and comments are by (default "WordCraft User").
- **Tracked changes**: `review.trackChanges {"value":true}` (the parameter is `value`; `on` is silently ignored and the command then just TOGGLES, which only looked right from an untracked start), then ordinary edits (`select.text {"text":"quick brown"}` + `text.insert` → one insertion + one deletion; `text.delete`) become `<w:ins>`/`<w:del>`.
  `review.changes` → `[{kind:"insert|delete",author,date,start,end,text}]`; `review.nextChange` + `review.accept`/`review.reject` act on one; `review.acceptAll`/`review.rejectAll`. After `acceptAll` the text read "The slow red fox jumps over the dog."
- **Comments**: `review.newComment {"text":"…"}` (on the current selection), `review.reply`, `review.editComment`, `review.resolveComment`, `review.comments` → `[{id,anchor,author,resolved,text}]`.
- **Compare two files**: open the original and `review.compare {"path":"revised.docx"}` → `{changes:1,notHonoured:[]}`, saving it gives a document with `<w:ins>`/`<w:del>` marks for the differences (`review.combine` merges revisions).
- **Content controls** (form-style fields): `developer.plainText {"title":"Full name","tag":"fullname","placeholder":"…"}`, `developer.dropDown {"title","tag","items":["Engineer","Designer"]}`, `developer.datePicker {"title","tag","format":"yyyy-MM-dd"}`,
  `developer.checkBox {"title","tag"}`, `developer.richText {"title","tag"}`; they save as `<w:sdt>` with `<w:alias>`/`<w:tag>` (the dropdown as `dropDownList`, the date as `<w:date>`). Also `developer.comboBox`, `picture`, `repeatingSection`, `developer.properties`, `removeControl`.
- **Watermark**: `design.watermark {"text":"DRAFT"}` → a `PowerPlusWaterMarkObject` in the header part.
- **Protection and encryption**: `review.restrict {"mode":"readOnly","password":"pw"}` writes `<w:documentProtection w:edit="readOnly" w:enforcement="1">` with a SHA-512 hash and salt (a speed bump, not security);
  `file.encrypt {"password":"…"}` produces a real Office-encrypted file (`CDFV2 Encrypted`). Opening it needs a password: `--password PASS`, `--password-file PATH` or the `WORDCRAFT_PASSWORD` environment variable (prefer the last two: a command-line password is visible to other processes); without it: "this document is protected with a password".
  A file opened with a password is written back with it.
- **Spelling and grammar**: `review.spelling` / `review.issues` → items `{kind:"spelling|grammar",message,start,end,text,suggestions:["receive","relieve",…]}` ("recieve" → receive; a repeated "the the" is reported as grammar); `review.suggestions`, `review.applySuggestion`, `review.addToDictionary`, `review.ignoreAll`, `review.language`, `review.thesaurus`, `review.wordCount`.
- **Table of figures**: `references.tableOfFigures {"label":"Figure","title":"List of figures"}`, captions with `references.caption {"label":"Figure","text":"Attendance by session"}`, then `references.updateFigures` → a line "Figure 1: Attendance by session … 1" with a page number.
- **Table formulas and sort**: `table.formula {"formula":"=SUM(ABOVE)"}` in the last cell → 42; `table.sort {"column":1,"order":"ascending","header":true}` sorted the body rows and kept the header and total rows in place (the total sorted last by name, so check totals when sorting).
- **Other**: `layout.lineNumbers {"value":"restartPage","countBy":1}`, `insert.textBox {"text":"Callout box","width":150,"height":60}`, `insert.shape`, `insert.dateTime`/`insert.field`, `insert.dropCap`.
- **Converting**: `wordcraft-cli convert base.docx base.{pdf,odt,rtf,html,md,tex,txt,png}` all wrote files (png renders page 1); the `.md`/`.txt` exports keep text only.

## Styles management, index and TOC, equations, tracked changes in depth (verified headless; equation render checked)

> `wordcraft-cli commands --json` DOES give each command's parameter signature (the older note that only ids exist is about the plain listing): use it before guessing.

- **Styles:** `styles.create {"name","basedOn"}` → `{id}`; `styles.modify {"style","chr","para"}`; `styles.updateToMatch {}` (style := the caret paragraph's direct formatting); `styles.rename {"style","name"}` → `{id,name}` (**the id stays "Note" after renaming to "Aside"**, so later calls such as `styles.setVisibility` report `style:"Note"`);
  `styles.setVisibility {"style","gallery":true,"hidden":false}` (needs `gallery` and/or `hidden`, not `visible`) → `{hidden,inGallery,style}`; `styles.addToGallery {"style"}`; `styles.delete {"style"}` → `{deleted:[…],restyled:1}` (paragraphs using it fall back to Normal);
  `styles.list` → `[{id,name,kind,basedOn,quick}]`; `styles.inspect`, `styles.copyFrom` (Organizer), `styles.organizer`.
- **Design tab:** `design.themes {}` → `["Craft","Studio","Gallery","Atelier","Darkroom","Sketchbook"]`; `design.theme {"name":"Studio"}`; `design.themeColors {"name":"Studio"}` takes those theme names (`Gallery` ok; "Office", "Blue", "Orange" → "unknown colours");
  `design.themeFonts {"heading":"Georgia","body":"Calibri"}` (both keys; `body`, not `minor`), `design.paragraphSpacing {"value":"relaxed"}`, `design.styleSet {"name":…}`. **`design.styleSet` and `design.paragraphSpacing` accepted ANY string (even "zzz") without error**, so verify with `inspect`/render what changed.
- **Index:** mark first, then insert. Select the word (`select.text`), `references.markEntry {"entry":"Quokka","bold":true}` → `{entry,marked:1}`; a sub-entry is `"subentry":"Australian"` (index shows "Marsupials" / "Australian, 1"). `references.index {"columns":1,"title":"Index"}` builds A–Z letter headings (M, Q) with page numbers at the caret; `references.updateIndex` after later edits.
  `select.text {"text":"quokka","occurrence":2}` selects the second match **in the whole document**, not "the second one I haven't marked", so entry 2 was marked on the same page as entry 1. Page numbers listed per entry are real (the render and `text` agree).
- **TOC options:** `references.toc {"levels":3,"title":"Contents","tabLeader":"dot"}` inserts the TOC **at the caret and leaves the caret BEFORE it**, so text typed afterwards lands above the TOC (my "Alpha" heading ended up before "Contents"). Insert the TOC last (place the caret with `caret.docStart`) or `caret.docEnd`/`caret.down` out of it first. The inserted Index title ("Index" as Heading 1) also shows up in the TOC. `references.updateToc`, `references.removeToc`, `references.addText` (add a heading-level to a paragraph) exist.
- **Equations** (`insert.equation {"latex"|"linear"}` → `{display,editing,linear,pos}`, display math, caret stays in the equation; `equation.exit` returns to the body): render checked (E=mc², a stacked fraction `x = a/(b+c)` with an equation number "(1)", a sum with binomial and integral from LaTeX, an inline `e^(iπ)+1=0`).
  Structure editing: `equation.insertStructure {"id":"frac.stacked"}` (ids come from `equation.gallery {}` → `structures[].sections[].templates[].id`: frac.stacked, frac.skewed, frac.dydx…; `builtins[]` are *formulas* with `id` pythagoras, quadratic, euler, gaussian, fourier… and a `linear` string; **`insertStructure {"id":"quadratic"}` fails**: use `{"linear":builtin.linear}` or `equation.set {"linear":…}`),
  `equation.type {"text"}`, `equation.move {"dir":"left|right|up|down|home|end|next|prev"}` (`down` jumps to the denominator), `equation.convert {"to":"linear|professional"}`, `equation.get {}` → `{latex,linear,linearForm,at}`, `equation.set {"linear"|"latex"}`, `equation.display {"value":false}` (inline), `equation.number {"value":true}` (adds `#` to the linear form, renders "(1)"), `equation.insertSymbol {"char"}`, `equation.inputFormat {"format":"unicode|latex"}`, `equation.justify {"jc":"left|center|centerGroup|right"}` (accepted, no visible change on my display equation), `equation.structure {"action"}` (only while editing).
  `equation.*` commands other than insert fail with "not editing an equation" until the caret is inside one.
- **Tracked changes by author and one at a time:** `file.setAuthor {"name":"Ann"}` before the edits labels each author's changes; `review.changes` → `[{author,date,kind:"insert|delete|format",text,start,end,description?,props?}]` (a bold toggle is a `format` change with `props:[{prop:"bold",value:true},…]`).
  `caret.docStart` → `review.nextChange` (selects the first change) → `review.accept {"next":true}` (accept and select the following change) / `review.reject {"next":true}`; two accepts took Ann's insert and delete, a `reject` dropped Bob's bold; the remaining list was Bob's insert/delete only; `review.acceptAll {"stopTracking":true}` also switches tracking off.
  `review.trackingOptions {"insertMark":"bold","insertColor":"C00000","balloons":"inline|revisions|commentsAndFormatting","commentDisplay":"margin|selected","insertionsDeletions","formatting","comments","ink"}` returns the whole option set (deleteMark strikethrough, moveFrom/moveTo colours…); `review.markup {}` toggles and returns `{showMarkup:false}`, `review.showMarkup {"value":true}`.
  `review.combine {"text":"revised text","author":"Merge","caseChanges":true}` → `{changes,notHonoured}` (also `path`, `original`, `whiteSpace`, `formatting`): a "beta gamma." → "BETA gamma delta." case change became one delete plus one insert.
- Not run: `styles.manage/pane/apply`, `tools.attachTemplate`, TOA (`references.markCitation/tableOfAuthorities`), `references.noteOptions`, `references.convertNotes`, `review.restrict` per section, `file.privacyOptions`, equation `structureActions` listing.

## Character effects, paragraph helpers, find, content controls, files and labels (verified headless; props read back with `inspect`)


- **Character effects** (act on the selection; `inspect` shows the run props): `format.smallCaps` → `smallCaps`, `format.shadow` → `shadow`, `format.outline` → `outline`, `format.doubleStrikethrough` → `doubleStrike`, `format.hidden` → `hidden`, `format.doubleUnderline`, `format.emboss/engrave`, `format.shading {"color":"FFFF00"}` → `shading:[255,255,0]`, `format.border {"value":true}` → `border:{style,width,space}`,
  `format.scale {"percent":150}` → `scale`, `format.position {"points":3}` → `position` (raised), `format.font {"name":"Georgia"}` (sets `font` and `fontCs`), `format.size {"size":16}`, `format.underline {"value":true}` + `format.underlineColor {"color":"FF0000"}` → `underlineColor:[255,0,0]`, `format.changeCase {"mode":"upper|lower|title|sentence|toggle"}`, `format.growFont/shrinkFont` (step through the standard sizes: grow then shrink returns to the start), `format.charStyle {"style"}`, `format.clear`.
  `format.enclose {"shape":"circle"}` needs exactly one full-width character or up to two half-width ones ("select one full-width character…": select a single letter); `format.phonetic {"ruby":"mii"}` → `{align,base,ruby,size:6}` (ruby text above the selection).
- **Paragraph helpers** (no parameters): `para.alignCenter|alignLeft|alignRight|justify|distribute`, `para.single|oneAndHalf|double`, `para.addSpaceBefore` (12 pt), `para.removeSpaceAfter`, `para.indent|outdent`, `para.hangingIndent` (indentLeft 36, indentFirst −36), `para.heading2|heading3`, `para.outlineLevel`. **`para.normal` only restores the style `Normal`: justification, hanging indent and space-before set before stay** (use `para.reset` to clear direct formatting).
  Text characters: `text.insertTab`, `text.ellipsis`, `text.registered`, `text.trademark`, `text.optionalHyphen`, `text.pageBreak` (a `\f` inside the paragraph), `text.typeCode {"code":"0233"}` (é), `text.backspace`, `text.deleteWordBack/Forward`; `insert.dateField`/`timeField` insert the current date/time as text ("10/26/2026" and "1:39 AM" ran together).
- **Find and select:** `edit.findNext {"text","matchCase","wholeWord","regex"}` → `{count:3,index:0}` (selects the match; with no params repeats the last search), `edit.findPrevious`, `select.word|sentence|paragraph|line|similar`, `select.range {"anchor":Pos,"focus":Pos}`, `edit.goBack`, `edit.formatPainter`, `edit.repeat`.
  Clipboard history: `edit.copy` → `{html,text}`, `edit.clipboardItems` → `[{index,chars,preview}]`, `edit.pasteClipboardItem {"index"}`, `edit.pasteAllClipboard`, `edit.deleteClipboardItem`, `edit.clearClipboard` → `[]`.
- **Headers and footers:** `insert.editHeader {"page":0}` / `insert.editFooter {"page":0}` → `{story:1}`/`{story:2}` (creates it if missing and leaves the caret INSIDE: `insert.closeHeader` after), `insert.removeFooter`, `insert.removeHeader`, `insert.removeEmptyHeaders`.
- **Content controls:** `developer.checkBox {"title","tag"}` + `developer.toggleCheckBox {"control":"agree","value":true}` → `{checked:true}`; `developer.dropDown {…,"items"}` + `developer.chooseItem {"control":"size","index":1}` → `{display:"M",value:"M"}`; `developer.datePicker` + `developer.setDate {"control":"when","date":"2026-10-25"}` → `{date,text:"10/25/2026"}`; `developer.repeatingSection`, `developer.designMode {"value":true}` → `{designMode}`, `developer.removeControl {"control"}`; also `developer.picture`, `buildingBlock`, `control`.
- **File commands:** `file.info {}` → pages, paragraphs, dirty, properties; `file.privacy {}` → `{removePersonalInfo,removeDateTime}`; `file.inspect {}` → `{found:{comments,revisions,headers,hidden,properties…}}` (`"remove":["comments","revisions","properties","hidden","headers"]` cleans them); `file.versions {"save":"v1"}` → `[{index,label,date}]` (`"restore":index`); `file.compatibility {}` → `{issues:[]}`; `file.autosave {}` → `{value:false}`; `file.share {}` → a hint;
  `file.exportPng {"path","page":1,"scale":1}` → `{width:612,height:792,bytes}`; `file.printPdf {"path","range":"all|current|selection"}` → `{pages,chosen,copies}` (`file.printMarkup {"value":true}` prints comment balloons); `file.protect {"mode":"none|readOnly|comments|trackedChanges"}` → the protection state; `file.listTemplates {"dir"}` needs a folder (error "give `dir`"); `file.rename {"name"}`.
  Review: `review.newComment` → `{id,story}`, `review.nextComment/previousComment`, `review.deleteComment {"id"|"all":true}` → `{deleted:[0]}`, `review.previousChange`, `review.hideInk {"value"}`. Tools: `tools.search {"query":"bold"}` → `{matches:[{id,label,location,shortcut}]}` (finds the command id for a ribbon label), `tools.recordMacro {"name":"M1"}` … call again → `{saved,steps}`.
- **Labels and envelopes (mail merge):** `mailings.start {"kind":"labels"}` → `mailings.recipients {"csv"}` → `mailings.labels {"product":"letter-3x10|a4-3x7|…","fromRecipients":true}` → `{filled:2,labels:30,product}`; **with the standard column names (First Name, Last Name, Address Line 1, City, State, Postal Code) the labels read "Ada Example 1 Main St Boston, MA 02101"**; a custom `"text":"{Name}\n{Street}\n{City}"` lost its first line (only Street and City printed), so use the standard columns. `mailings.envelopes {"delivery","return","size":"Envelope #10"}` → `{width:684,height:297}` and a new document with the return address top left (the delivery address text was not found in `text` output of the new document: look at the render before relying on it).
- Not run or not possible headless: `arrange.align` (needs a selected picture or shape), table mouse commands (`table.draw/eraser/resizeDrag/selectAt/moveDrag/fitColumn`), `layout.manualHyphenation`, `file.recover`, `edit.undoHistory`, `review.readAloud`.

## Ink (verified headless and on the live window; render checked)

> **This corrects an earlier note that ink needs the live app: the `page` parameter is 0-BASED** (`"page":1` means the second page and failed with "no page 1" on a one-page document; `"page":0` works headless).

- `draw.stroke {"page":0,"points":[[x,y],…],"tool":"pen|pencil|highlighter","color":"C00000","width":2}` → `{page,pos,rect:[x,y,w,h],shape:null}` (page points, at most 5000; the stroke is anchored to the paragraph at `pos`). Render: a red polyline, a wide translucent yellow highlighter bar, a thin grey pencil line (points are joined by straight segments, no smoothing).
- **Select, edit, delete:** `draw.lasso {"page":0,"points":[loop]}` → `{count:1,selected:[pos]}` (every stroke inside the loop), `draw.lasso {"page":0,"clear":true}` → `{count:0}`; then `draw.lassoColor {"color":"0000FF"}` → `{recolored:1}`, `draw.lassoMove {"dx":150,"dy":10}` → `{moved:1}`, `draw.lassoDelete` → `{deleted:1}`. Without a lasso selection they answer "nothing is selected with the lasso".
  `draw.erase {"page":0,"x":150,"y":380}` → `{erased:pos}` removes the stroke under that point.
- **Ink to shape:** `draw.convertInk {}` converts the lasso-selected strokes that look like a shape (`{converted:[{shape:"rectangle"}]}`; a zig-zag line answers "none of the selected strokes looks like a shape"); `draw.inkToShape {"value":true}` turns recognition on so the NEXT stroke becomes a shape as it is drawn (a boxed pen stroke came back with `shape:"rectangle"`), `{"value":false}` turns it off.
- **Pens:** `draw.pen|pencil|highlighter {"color","width"}` set the tool and its look (each returns the whole draw state: `mode`, `pen`, `pencil`, `highlighter`, `inkToShape`), `draw.addPen {"kind","color","width"}` → `{index,pens}`, `draw.removePen {"index"}`, `draw.eraser`, `draw.select`, `draw.replay {"value":true}` → the strokes in drawing order `[{order,page,points,tool}]` (`false` ends it), `review.hideInk {"value":true}` hides ink on screen.
- **Hand-drawn ink in the live window (a real stroke drawn with the mouse, 2026-10-25):** a slow squiggle recorded **226 points** and a closed box **154 points** (`draw.replay` → `[{order,page:0,points,tool:"pen"}]`), so a real stroke is dense and renders smooth, unlike the 3-5 coordinates the commands usually pass. The pen's width in the ribbon runs 1.5 to 2.5 (there is no 2 pt step); `draw.pen {"width":2.5}` matches it.
  **In the live window a lasso selection only persists after the lasso tool is switched on:** call `draw.lasso {}` (no points; `view.state` shows `draw.mode:"lasso"`) and then `draw.lasso {"page":0,"points":[…]}`; in the default select mode the points call answers `selected` but the NEXT command (`draw.convertInk`, `lassoColor`, `lassoMove`) says "nothing is selected with the lasso", even inside `batch`. `draw.select {}` returns to the select tool. Headless runs keep the selection without this step.
  Verified on the user's strokes: `draw.convertInk` turned the hand-drawn box into a clean `rectangle` (render: a straight red rectangle in place of the wobbly box); `draw.lassoColor {"color":"0000FF"}` recoloured the squiggle and `draw.lassoMove {"dx":0,"dy":60}` moved it, wobble preserved. Not checked: pressure sensitivity (mouse only) and tablet tilt.
- **In the file:** each stroke is saved as a floating `wp:anchor` + `wps:wsp` freeform shape in `word/document.xml` (4 shapes for 4 strokes), so Word and ONLYOFFICE show ink as ordinary shapes; the document keeps no separate ink part.
