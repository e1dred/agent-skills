# WordCraft command catalogue (0.16.0)

Built 2026-11-06 from the skill's own text (SKILL.md, reference/ and tools/); no command was run and nothing was re-tested. Ids come from `wordcraft-cli` 0.16.0 (656 ids); the skill's version label: last tested on WordCraft 0.16.0; earlier evidence sections cite 0.11.0-0.15.2.
Status: **V** verified - the hit is under a heading naming verification or records an observed result (arrow, before/after, read-back, checked file, confirmed); **d** documented - named with parameters or usage, no recorded evidence; **n** named only - a bare list or command index; **s** skipped on purpose - the skill says skipped/not run/not tested/not exercised; **x** known no-op, broken or refused - the line says so; **V+** verified, but another line records a limit (refused or skipped in some state or version); the note quotes both. When a command has verified evidence anywhere, it counts as verified: a refusal or skip recorded elsewhere usually names a precondition or an older round.
Counts: V 601, V+ 39, d 2, n 0, s 13, x 1.

## arrange (15)

| id | status | note |
|---|---|---|
| `arrange.align` | s | reference/formatting-and-editing.md#Character effects, par…: Not run … - Not run or not possible headless: `arrang… |
| `arrange.bounds` | V | reference/command-reference.md#Commands (verified): …egrees"}`, `arrange.bounds`, `arrange.nudge`, `objec… |
| `arrange.bringForward` | V | reference/command-reference.md#Verified in detail, WordCra…: …e. (9): `arrange.bringForward` (state: f… |
| `arrange.copyTo` | V | reference/command-reference.md#Verified in detail, WordCra…: `arrange.copyTo` `{"x": 200, "y": 120}` (st… |
| `arrange.group` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `arrange.group` (state: rectangle and ellip… · limit: command-reference.md: Refused … `arrange.group` (not available: arrange.group: select two or… |
| `arrange.moveWithText` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `arrange.moveWithText` `{"value": true}` (s… · limit: command-reference.md: Refused … `arrange.moveWithText` (not available: arrange.moveWithText:… |
| `arrange.nudge` | V | reference/command-reference.md#Commands (verified): …e.bounds`, `arrange.nudge`, `object.altText`. |
| `arrange.position` | V | reference/command-reference.md#Commands (verified): …re"}` then `arrange.position {"preset":"topRight"}` … |
| `arrange.rotate` | V | reference/command-reference.md#Verified in detail, WordCra…: `arrange.rotate` `{"direction": "right"}` (… |
| `arrange.rotation` | V | reference/command-reference.md#Commands (verified): `arrange.rotation {"degrees"}`, `arrange.bounds`, `a… |
| `arrange.selectionPane` | V | reference/command-reference.md#Sweep of every remaining co…: …,range}]`; `arrange.selectionPane {}` → `[{… |
| `arrange.sendBackward` | V | reference/command-reference.md#Verified in detail, WordCra…: `arrange.sendBackward` (state: floating pic… |
| `arrange.ungroup` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `arrange.ungroup` (state: floating rectangl… · limit: command-reference.md: Refused … `arrange.ungroup` (not available: arrange.ungroup: select a … |
| `arrange.wrap` | V | reference/command-reference.md#Commands (verified): `arrange.wrap {"wrap":"square"}` then `arrange.posit… |
| `arrange.wrapText` | V | reference/command-reference.md#Verified in detail, WordCra…: `arrange.wrapText` `{"side": "left"}` (stat… |

## canvas (4)

| id | status | note |
|---|---|---|
| `canvas.expand` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (4): `canvas.expand` `{"by": 20}` (st… |
| `canvas.fit` | V | reference/command-reference.md#Verified in detail, WordCra…: `canvas.fit` (state: drawing canvas selecte… |
| `canvas.member` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `canvas.member` `{"index": 0, "x": 5, "y": … · limit: command-reference.md: Refused … `canvas.member` (bad parameters: no member 0 (the canvas has… |
| `canvas.scale` | V | reference/command-reference.md#Verified in detail, WordCra…: `canvas.scale` `{"factor": 1.2}` (state: ca… |

## caret (16)

| id | status | note |
|---|---|---|
| `caret.docEnd` | V | reference/command-reference.md#Commands (verified): `caret.docEnd` then lands in the paragraph after the… |
| `caret.docStart` | V | reference/command-reference.md#Commands (verified): … in row 1 (`caret.docStart`, then |
| `caret.down` | V | reference/formatting-and-editing.md#Styles management, ind…: …et.docEnd`/`caret.down` out of it first. |
| `caret.end` | V | reference/document-formats.md#Document styles (traditional…: …"Doe "}` → `caret.end` → `insert.pageField`… |
| `caret.home` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (5): `caret.home` (state: caret in bo… |
| `caret.left` | V | reference/command-reference.md#Verified in detail, WordCra…: `caret.left` (state: caret in body paragrap… |
| `caret.pageDown` | V | reference/command-reference.md#Verified in detail, WordCra…: `caret.pageDown` (state: caret in body para… |
| `caret.pageUp` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (1): `caret.pageUp` with a page break… |
| `caret.paraDown` | V | reference/command-reference.md#Commands (verified): `caret.paraDown` when one paragraph sits above the t… |
| `caret.paraUp` | V | reference/formatting-and-editing.md#Paragraph formatting, …: `caret.paraUp {"extend":true}` did NOT sele… |
| `caret.pastCitation` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …t. (1): `caret.pastCitation` with a cita… · limit: command-reference.md: Refused … `caret.pastCitation` (there's no citation after the caret) |
| `caret.right` | V | reference/command-reference.md#Commands (verified): `caret.right` at the end of a cell's text moves |
| `caret.set` | V | reference/command-reference.md#Commands (verified): with `caret.set {"pos":{"story":"body","path":[para]… |
| `caret.up` | V | reference/document-formats.md#Document styles (traditional…: …e merged), `caret.up` to the row, `table.se… |
| `caret.wordLeft` | V | reference/command-reference.md#Verified in detail, WordCra…: `caret.wordLeft` (state: caret in body para… |
| `caret.wordRight` | V | reference/command-reference.md#Verified in detail, WordCra…: `caret.wordRight` (state: caret in body par… |

## chart (5)

| id | status | note |
|---|---|---|
| `chart.dataLabels` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (5): `chart.dataLabels` `{"on": true}… |
| `chart.editData` | V | reference/command-reference.md#Verified in detail, WordCra…: `chart.editData` `{"data": {"categories": [… |
| `chart.legend` | V | reference/command-reference.md#Verified in detail, WordCra…: `chart.legend` `{"pos": "bottom"}` (state: … |
| `chart.title` | V | reference/command-reference.md#Verified in detail, WordCra…: `chart.title` `{"text": "New Title"}` (stat… |
| `chart.type` | V | reference/command-reference.md#Verified in detail, WordCra…: `chart.type` `{"type": "pie"}` (state: char… |

## design (12)

| id | status | note |
|---|---|---|
| `design.effects` | V | reference/command-reference.md#Verified in detail, WordCra…: …ge colour, `design.effects`) were not looke… |
| `design.pageBorders` | V | reference/command-reference.md#Verified in detail, WordCra…: `design.pageBorders` `{"kind":"box","width"… |
| `design.pageColor` | V | reference/command-reference.md#Verified in detail, WordCra…: `design.pageColor` `{"color": "DDEEFF"}` (s… |
| `design.paragraphSpacing` | V | reference/formatting-and-editing.md#Styles management, ind…: … `minor`), `design.paragraphSpacing {"value… |
| `design.scaleFontSizes` | V | reference/live-editing.md#Live mode, verified (WordCraft, …: …der_page`, `design.scaleFontSizes` (the car… |
| `design.setDefault` | x | reference/command-reference.md#Verified in detail, WordCra…: …he mouse), `design.setDefault` (no effect h… |
| `design.styleSet` | V | reference/formatting-and-editing.md#Styles management, ind…: …elaxed"}`, `design.styleSet {"name":…}`. |
| `design.theme` | V | reference/formatting-and-editing.md#Styles management, ind…: `design.theme {"name":"Studio"}` |
| `design.themeColors` | V | reference/formatting-and-editing.md#Styles management, ind…: `design.themeColors {"name":"Studio"}` take… |
| `design.themeFonts` | V | reference/formatting-and-editing.md#Styles management, ind…: `design.themeFonts {"heading":"Georgia","bo… |
| `design.themes` | V | reference/formatting-and-editing.md#Styles management, ind…: …ign tab: `design.themes {}` → `["Craft","… |
| `design.watermark` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …termark: `design.watermark {"text":"DRAFT… |

## developer (16)

| id | status | note |
|---|---|---|
| `developer.buildingBlock` | V | reference/command-reference.md#Verified in detail, WordCra…: …r. (2): `developer.buildingBlock` `{"tit… |
| `developer.checkBox` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: `developer.checkBox {"title","tag"}`, `deve… |
| `developer.chooseItem` | V | reference/formatting-and-editing.md#Character effects, par…: …items"}` + `developer.chooseItem {"control"… |
| `developer.comboBox` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: Also `developer.comboBox`, `picture`, `repe… |
| `developer.control` | V | reference/command-reference.md#Verified in detail, WordCra…: `developer.control` (state: docx built with… |
| `developer.datePicker` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …igner"]}`, `developer.datePicker {"title","… |
| `developer.designMode` | V | reference/formatting-and-editing.md#Character effects, par…: …gSection`, `developer.designMode {"value":t… |
| `developer.dropDown` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …er":"…"}`, `developer.dropDown {"title","ta… |
| `developer.picture` | V | reference/formatting-and-editing.md#Character effects, par…: also `developer.picture`, `buildingBlock`, … |
| `developer.plainText` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …e fields): `developer.plainText {"title":"F… |
| `developer.properties` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …gSection`, `developer.properties`, `removeC… |
| `developer.removeControl` | V | reference/formatting-and-editing.md#Character effects, par…: …ignMode}`, `developer.removeControl {"contr… |
| `developer.repeatingSection` | V | reference/formatting-and-editing.md#Character effects, par…: `developer.repeatingSection`, `developer.de… |
| `developer.richText` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …","tag"}`, `developer.richText {"title","ta… |
| `developer.setDate` | V | reference/formatting-and-editing.md#Character effects, par…: …ePicker` + `developer.setDate {"control":"w… |
| `developer.toggleCheckBox` | V | reference/formatting-and-editing.md#Character effects, par…: …,"tag"}` + `developer.toggleCheckBox {"cont… |

## document (6)

| id | status | note |
|---|---|---|
| `document.inspect` | V | reference/command-reference.md#Sweep of every remaining co…: …,format}`; `document.inspect {"text":true}`… |
| `document.layout` | V | reference/command-reference.md#Sweep of every remaining co…: … by `\t`); `document.layout {}` → caret rec… |
| `document.paragraph` | V | reference/command-reference.md#Verified in detail, WordCra…: `document.paragraph` `{"path": [2]}` (state… |
| `document.selection` | V | reference/command-reference.md#Sweep of every remaining co…: …r/footer); `document.selection {}` → `{anch… |
| `document.setText` | V | reference/command-reference.md#Verified in detail, WordCra…: `document.setText` `{"text": "Replaced whol… |
| `document.text` | V | reference/command-reference.md#Sweep of every remaining co…: …results: `document.text {}` → `{text}` (p… |

## draw (16)

| id | status | note |
|---|---|---|
| `draw.addPen` | V | reference/formatting-and-editing.md#Ink (verified headless…: …ToShape`), `draw.addPen {"kind","color","wi… |
| `draw.convertInk` | V | reference/formatting-and-editing.md#Ink (verified headless…: …o shape: `draw.convertInk {}` converts th… |
| `draw.erase` | V | reference/formatting-and-editing.md#Ink (verified headless…: `draw.erase {"page":0,"x":150,"y":380}` → `… |
| `draw.eraser` | V | reference/formatting-and-editing.md#Ink (verified headless…: …"index"}`, `draw.eraser`, `draw.select`, `d… |
| `draw.highlighter` | V | reference/command-reference.md#Verified in detail, WordCra…: …w. (2): `draw.highlighter` `{"color": "F… |
| `draw.inkToShape` | V+ | reference/formatting-and-editing.md#Ink (verified headless…: `draw.inkToShape {"value":true}` turns reco… · limit: sections-headers-tables.md: Not run … - Not run: ink (`draw.*`: `draw.stroke {"page","points","too… |
| `draw.lasso` | V+ | reference/formatting-and-editing.md#Ink (verified headless…: … delete: `draw.lasso {"page":0,"points":[… · limit: sections-headers-tables.md: Not run … - Not run: ink (`draw.*`: `draw.stroke {"page","points","too… |
| `draw.lassoColor` | V | reference/formatting-and-editing.md#Ink (verified headless…: then `draw.lassoColor {"color":"0000FF"}` →… |
| `draw.lassoDelete` | V | reference/formatting-and-editing.md#Ink (verified headless…: …moved:1}`, `draw.lassoDelete` → `{deleted:1… |
| `draw.lassoMove` | V | reference/formatting-and-editing.md#Ink (verified headless…: …lored:1}`, `draw.lassoMove {"dx":150,"dy":1… |
| `draw.pen` | V | reference/formatting-and-editing.md#Ink (verified headless…: … Pens: `draw.pen\|pencil\|highlighter {"c… |
| `draw.pencil` | V | reference/command-reference.md#Verified in detail, WordCra…: `draw.pencil` `{"color": "FF0000", "width":… |
| `draw.removePen` | V | reference/formatting-and-editing.md#Ink (verified headless…: …ex,pens}`, `draw.removePen {"index"}`, `dra… |
| `draw.replay` | V+ | reference/formatting-and-editing.md#Ink (verified headless…: …w.select`, `draw.replay {"value":true}` → t… · limit: sections-headers-tables.md: Not run … - Not run: ink (`draw.*`: `draw.stroke {"page","points","too… |
| `draw.select` | V | reference/formatting-and-editing.md#Ink (verified headless…: …w.eraser`, `draw.select`, `draw.replay {"va… |
| `draw.stroke` | V+ | reference/formatting-and-editing.md#Ink (verified headless…: - `draw.stroke {"page":0,"points":[[x,y],…]… · limit: sections-headers-tables.md: Not run … - Not run: ink (`draw.*`: `draw.stroke {"page","points","too… |

## edit (31)

| id | status | note |
|---|---|---|
| `edit.advancedFind` | s | reference/sections-headers-tables.md#Tables in depth, outl…: Not run … - Not run: ink (`draw.*`: `draw.stroke {"pa… |
| `edit.clearClipboard` | V | reference/formatting-and-editing.md#Character effects, par…: …oardItem`, `edit.clearClipboard` → `[]`. |
| `edit.clipboardItems` | V | reference/formatting-and-editing.md#Character effects, par…: …ml,text}`, `edit.clipboardItems` → `[{index… |
| `edit.clipboardPane` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (2): `edit.clipboardPane` `{"value": … |
| `edit.copy` | V | reference/formatting-and-editing.md#Paragraph formatting, …: - `edit.copy`, `edit.cut`, `edit.paste {}` … |
| `edit.copyFormat` | V | reference/formatting-and-editing.md#Paragraph formatting, …: - `edit.copyFormat` + `select.text` + `edit… |
| `edit.cut` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …dit.copy`, `edit.cut`, `edit.paste {}` (the… |
| `edit.deleteClipboardItem` | V | reference/formatting-and-editing.md#Character effects, par…: …lipboard`, `edit.deleteClipboardItem`, `edi… |
| `edit.find` | V | reference/command-reference.md#Commands (verified): `edit.find` with `"regex":true` |
| `edit.findNext` | V | reference/formatting-and-editing.md#Character effects, par…: … select: `edit.findNext {"text","matchCas… |
| `edit.findPrevious` | V | reference/formatting-and-editing.md#Character effects, par…: …t search), `edit.findPrevious`, `select.wor… |
| `edit.findReplace` | V | reference/command-reference.md#Verified in detail, WordCra…: `edit.findReplace` `{"tab": "find"}` (state… |
| `edit.formatPainter` | V | reference/formatting-and-editing.md#Character effects, par…: …t.goBack`, `edit.formatPainter`, `edit.repe… |
| `edit.goBack` | V | reference/formatting-and-editing.md#Character effects, par…: …us":Pos}`, `edit.goBack`, `edit.formatPaint… |
| `edit.goto` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …t.undoTo`, `edit.goto`, the spike. |
| `edit.insertSpike` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …the spike, `edit.insertSpike` pastes it bac… |
| `edit.paste` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …edit.cut`, `edit.paste {}` (the internal cl… |
| `edit.pasteAllClipboard` | V | reference/formatting-and-editing.md#Character effects, par…: …"index"}`, `edit.pasteAllClipboard`, `edit.… |
| `edit.pasteClipboardItem` | V | reference/formatting-and-editing.md#Character effects, par…: …review}]`, `edit.pasteClipboardItem {"index… |
| `edit.pasteFormat` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …ct.text` + `edit.pasteFormat` copied bold +… |
| `edit.pasteMerge` | s | reference/sections-headers-tables.md#Tables in depth, outl…: Not run … - Not run: ink (`draw.*`: `draw.stroke {"pa… |
| `edit.pasteSpecial` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …alic runs, `edit.pasteSpecial {"as":"text", |
| `edit.pasteText` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …er a cut), `edit.pasteText {"text"}` (plain… |
| `edit.redo` | V | reference/command-reference.md#Verified in detail, WordCra…: …dit.undo", "edit.redo"], "tabs": [{"name": … |
| `edit.repeat` | V | reference/formatting-and-editing.md#Character effects, par…: …tPainter`, `edit.repeat`. |
| `edit.replace` | s | reference/formatting-and-editing.md#Paragraph formatting, …: `edit.replace`/`findNext`/`advancedFind` ex… |
| `edit.replaceAll` | V | SKILL.md#Traps (each one cost time): - `edit.replaceAll` ignores case by default and does not keep it:… |
| `edit.spike` | V | reference/formatting-and-editing.md#Paragraph formatting, …: `edit.spike` cuts the selection into the sp… |
| `edit.undo` | V | reference/command-reference.md#Verified in detail, WordCra…: …ile.save", "edit.undo", "edit.redo"], "tabs… |
| `edit.undoHistory` | s | reference/formatting-and-editing.md#Character effects, par…: Not run … - Not run or not possible headless: `arrang… |
| `edit.undoTo` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …te format, `edit.undoTo`, `edit.goto`, the … |

## equation (21)

| id | status | note |
|---|---|---|
| `equation.backspace` | V | reference/command-reference.md#Verified in detail, WordCra…: …n. (3): `equation.backspace` (state: equ… |
| `equation.convert` | V | reference/formatting-and-editing.md#Styles management, ind…: …ominator), `equation.convert {"to":"linear\|… |
| `equation.delete` | V | reference/command-reference.md#Verified in detail, WordCra…: `equation.delete`/`backspace` act only whil… |
| `equation.deleteSurrounding` | V | reference/command-reference.md#Newer commands: - `equation.deleteSurrounding {"before":1,"after":0}`… |
| `equation.display` | V | reference/formatting-and-editing.md#Styles management, ind…: …"latex"}`, `equation.display {"value":false… |
| `equation.edit` | V | reference/command-reference.md#Verified in detail, WordCra…: … equation (`equation.edit` first) |
| `equation.enter` | V | reference/command-reference.md#Verified in detail, WordCra…: `equation.enter` (state: equation editing) … |
| `equation.exit` | V | reference/formatting-and-editing.md#Styles management, ind…: … equation; `equation.exit` returns to the b… |
| `equation.gallery` | V | reference/formatting-and-editing.md#Styles management, ind…: … come from `equation.gallery {}` → `structu… |
| `equation.get` | V | reference/command-reference.md#Verified in detail, WordCra…: … back with `equation.get`, the returned car… |
| `equation.inputFormat` | V | reference/formatting-and-editing.md#Styles management, ind…: …{"char"}`, `equation.inputFormat {"format":… |
| `equation.insertStructure` | V | reference/formatting-and-editing.md#Styles management, ind…: …e editing: `equation.insertStructure {"id":… |
| `equation.insertSymbol` | V | reference/formatting-and-editing.md#Styles management, ind…: …rs "(1)"), `equation.insertSymbol {"char"}`… |
| `equation.justify` | V | reference/formatting-and-editing.md#Styles management, ind…: …\|latex"}`, `equation.justify {"jc":"left\|ce… |
| `equation.move` | V | reference/formatting-and-editing.md#Styles management, ind…: …{"text"}`, `equation.move {"dir":"left\|righ… |
| `equation.normalText` | V | reference/command-reference.md#Verified in detail, WordCra…: `equation.normalText` `{"value":true}` then… |
| `equation.number` | V | reference/formatting-and-editing.md#Styles management, ind…: … (inline), `equation.number {"value":true}`… |
| `equation.set` | V | reference/formatting-and-editing.md#Styles management, ind…: …inear}` or `equation.set {"linear":…}`), |
| `equation.structure` | V | reference/formatting-and-editing.md#Styles management, ind…: …equation), `equation.structure {"action"}` … |
| `equation.structureActions` | V | reference/command-reference.md#Verified in detail, WordCra…: `equation.structureActions` with the math c… |
| `equation.type` | V | reference/command-reference.md#Newer commands: …t":true}`, `equation.type {"text":"cd"}` → `a+bcd`; delet… |

## fields (8)

| id | status | note |
|---|---|---|
| `fields.lock` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (8): `fields.lock` (state: caret in D… |
| `fields.next` | V | reference/command-reference.md#Verified in detail, WordCra…: `fields.next` (state: caret in DATE field) … |
| `fields.previous` | V | reference/command-reference.md#Verified in detail, WordCra…: `fields.previous` (state: caret in PAGE fie… |
| `fields.selected` | V | reference/command-reference.md#Sweep of every remaining co…: ….define`); `fields.selected {}` → `[{code,i… |
| `fields.setCode` | V | reference/command-reference.md#Verified in detail, WordCra…: `fields.setCode` `{"code": "TIME \\@ \"HH:m… |
| `fields.toggleCode` | V | reference/command-reference.md#Verified in detail, WordCra…: `fields.toggleCode` (state: caret in DATE f… |
| `fields.unlink` | V | reference/command-reference.md#Verified in detail, WordCra…: `fields.unlink` (state: caret in DATE field… |
| `fields.unlock` | V | reference/command-reference.md#Verified in detail, WordCra…: `fields.unlock` (state: DATE field locked f… |

## file (30)

| id | status | note |
|---|---|---|
| `file.accessibility` | V | reference/formatting-and-editing.md#Accessibility checker …: `file.accessibility {}` → `{"ok":bool,"issu… |
| `file.autosave` | V | reference/formatting-and-editing.md#Character effects, par…: `file.autosave {}` → `{value:false}` |
| `file.close` | V | reference/command-reference.md#Commands (verified): …"path"}` / `file.close {"force"?}` exist |
| `file.closeDocument` | V | reference/command-reference.md#Newer commands: - `file.closeDocument {"id"?,"force"?}`: a document w… |
| `file.compatibility` | V | reference/formatting-and-editing.md#Character effects, par…: `file.compatibility {}` → `{issues:[]}` |
| `file.encrypt` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: `file.encrypt {"password":"…"}` produces a … |
| `file.exportPdf` | V | reference/command-reference.md#Commands (verified): …{"path"}`, `file.exportPdf {"path"}`. |
| `file.exportPng` | V | reference/formatting-and-editing.md#Character effects, par…: `file.exportPng {"path","page":1,"scale":1}… |
| `file.info` | V | reference/formatting-and-editing.md#Character effects, par…: …ommands: `file.info {}` → pages, paragrap… |
| `file.inspect` | V | reference/formatting-and-editing.md#Character effects, par…: `file.inspect {}` → `{found:{comments,revis… |
| `file.listTemplates` | V | reference/formatting-and-editing.md#Character effects, par…: `file.listTemplates {"dir"}` needs a folder… |
| `file.new` | V | reference/command-reference.md#Verified in detail, WordCra…: …e. (2): `file.new` `{"template": "blank"… |
| `file.newFromTemplate` | V | reference/existing-documents.md#Templates (verified headle…: `file.newFromTemplate {"path":"x.dotx"}` (s… |
| `file.open` | V | reference/command-reference.md#Commands (verified): - `file.open {"path"}` / `file.close {"force"?}` exi… |
| `file.options` | V | reference/command-reference.md#Sweep of every remaining co…: …Level:N}`; `file.options {"pane":"general"}… |
| `file.print` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …e. (1): `file.print` live: opens the Pri… · limit: command-reference.md: skipped on purpose (print, user font list, theme setting, ne… |
| `file.printMarkup` | V | reference/document-formats.md#Policy manual with a TOC, ca…: …ue}' --cmd 'file.printMarkup={"value":true}… |
| `file.printPdf` | V | reference/command-reference.md#Verified in detail, WordCra…: …script use `file.printPdf {"path"}` or conv… |
| `file.privacy` | V | reference/formatting-and-editing.md#Character effects, par…: `file.privacy {}` → `{removePersonalInfo,re… |
| `file.privacyOptions` | V+ | reference/command-reference.md#Commands (verified): …us output: `file.privacyOptions {"removePersonalInfo… · limit: formatting-and-editing.md: Not run … - Not run: `styles.manage/pane/apply`, `tools.attachTemplate… |
| `file.properties` | V | reference/command-reference.md#Commands (verified): …roperties: `file.properties {"title","author","subje… |
| `file.protect` | V | reference/formatting-and-editing.md#Character effects, par…: `file.protect {"mode":"none\|readOnly\|commen… |
| `file.recover` | s | reference/formatting-and-editing.md#Character effects, par…: Not run … - Not run or not possible headless: `arrang… |
| `file.rename` | V | reference/formatting-and-editing.md#Character effects, par…: `file.rename {"name"}`. |
| `file.save` | V | reference/command-reference.md#Commands (verified): …ve/export: `file.save {"path"}`, `file.saveAs {"path… |
| `file.saveAs` | V | reference/command-reference.md#Commands (verified): …{"path"}`, `file.saveAs {"path"}`, `file.exportPdf {… |
| `file.saveTemplate` | V | reference/existing-documents.md#Templates (verified headle…: …ader, then `file.saveTemplate {"path":"x.do… |
| `file.setAuthor` | V | reference/command-reference.md#Commands (verified): - Review: `file.setAuthor {"name"}` first (sets comm… |
| `file.share` | V | reference/formatting-and-editing.md#Character effects, par…: `file.share {}` → a hint |
| `file.versions` | V | reference/formatting-and-editing.md#Character effects, par…: `file.versions {"save":"v1"}` → `[{index,la… |

## font (5)

| id | status | note |
|---|---|---|
| `font.add` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …t. (2): `font.add` headless with an isol… · limit: command-reference.md: Refused … `font.add` (/nonexistent.ttf: No such file or directory (os … |
| `font.list` | V | reference/command-reference.md#Sweep of every remaining co…: …e:1.0,…}`; `font.list {}` → `{folder:null,f… |
| `font.loadSystem` | V+ | reference/log.md#Log: …reenshots), font.loadSystem checked; 4 left (split, editor, borderPainter, researc… · limit: command-reference.md: skipped on purpose (print, user font list, theme setting, ne… |
| `font.missing` | V | reference/formatting-and-editing.md#0.15.2 changes (verifi…: - `font.missing` lists fonts the docume… |
| `font.remove` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `font.remove` `{"family":"Comic Sans MS"}` … · limit: command-reference.md: Refused … `font.remove` ("Nope" isn't a font you added) |

## format (41)

| id | status | note |
|---|---|---|
| `format.allCaps` | V | reference/command-reference.md#Commands (verified): {"command":"format.allCaps"}]}}` then `tools.macros … |
| `format.bold` | V | SKILL.md#Traps (each one cost time): line: `format.bold true` → insert → `format.resetChar` → insert the… |
| `format.border` | V | reference/formatting-and-editing.md#Character effects, par…: …5,255,0]`, `format.border {"value":true}` →… |
| `format.changeCase` | V | reference/formatting-and-editing.md#Character effects, par…: …255,0,0]`, `format.changeCase {"mode":"uppe… |
| `format.charStyle` | V | reference/formatting-and-editing.md#Character effects, par…: …he start), `format.charStyle {"style"}`, `f… |
| `format.clear` | V | reference/formatting-and-editing.md#Character effects, par…: …"style"}`, `format.clear`. |
| `format.color` | V | reference/command-reference.md#Commands (verified): … spacing), `format.color {"color":"C00000"}`. |
| `format.doubleStrikethrough` | V | reference/formatting-and-editing.md#Character effects, par…: …`outline`, `format.doubleStrikethrough` → `… |
| `format.doubleUnderline` | V | reference/formatting-and-editing.md#Character effects, par…: … `hidden`, `format.doubleUnderline`, `forma… |
| `format.emboss` | V | reference/formatting-and-editing.md#Character effects, par…: …nderline`, `format.emboss/engrave`, `format… |
| `format.emphasisMark` | V | reference/formatting-and-editing.md#0.15.2 changes (verifi…: - `format.emphasisMark {"mark":"dot"}` … |
| `format.enclose` | V | reference/formatting-and-editing.md#Character effects, par…: `format.enclose {"shape":"circle"}` needs e… |
| `format.engrave` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (6): `format.engrave` (state: 'quick'… |
| `format.font` | V | reference/formatting-and-editing.md#Character effects, par…: … (raised), `format.font {"name":"Georgia"}`… |
| `format.fontDialog` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (1): `format.fontDialog` live: opens … |
| `format.growFont` | V | reference/formatting-and-editing.md#Character effects, par…: …toggle"}`, `format.growFont/shrinkFont` (st… |
| `format.growFont1` | V | reference/command-reference.md#Verified in detail, WordCra…: `format.growFont1` (state: 'quick' selected… |
| `format.hidden` | V | reference/formatting-and-editing.md#Character effects, par…: …leStrike`, `format.hidden` → `hidden`, `for… |
| `format.highlight` | V | reference/command-reference.md#Commands (verified): …t` first): `format.highlight {"color":"yellow"}`, |
| `format.italic` | V | reference/document-formats.md#Manuscript format for publis…: …talic run (`format.italic` → text → `format… |
| `format.outline` | V | reference/formatting-and-editing.md#Character effects, par…: … `shadow`, `format.outline` → `outline`, `f… |
| `format.phonetic` | V | reference/formatting-and-editing.md#Character effects, par…: `format.phonetic {"ruby":"mii"}` → `{align,… |
| `format.position` | V | reference/formatting-and-editing.md#Character effects, par…: …→ `scale`, `format.position {"points":3}` →… |
| `format.resetChar` | V | SKILL.md#Traps (each one cost time): …→ insert → `format.resetChar` → insert the rest. |
| `format.scale` | V | reference/formatting-and-editing.md#Character effects, par…: `format.scale {"percent":150}` → `scale`, `… |
| `format.set` | V | reference/command-reference.md#Property names (verified vi…: …ter props (`format.set {"props":…}`, `style… |
| `format.shading` | V | reference/formatting-and-editing.md#Character effects, par…: …/engrave`, `format.shading {"color":"FFFF00… |
| `format.shadow` | V | reference/formatting-and-editing.md#Character effects, par…: …mallCaps`, `format.shadow` → `shadow`, `for… |
| `format.shrinkFont` | V | reference/command-reference.md#Verified in detail, WordCra…: `format.shrinkFont` (state: 'quick' selecte… |
| `format.shrinkFont1` | V | reference/command-reference.md#Verified in detail, WordCra…: `format.shrinkFont1` (state: 'quick' select… |
| `format.size` | V | reference/command-reference.md#Newer commands: …h a direct `format.size` kept its size, and Normal (no ex… |
| `format.smallCaps` | V | reference/formatting-and-editing.md#Character effects, par…: …un props): `format.smallCaps` → `smallCaps`… |
| `format.spacing` | V | reference/command-reference.md#Commands (verified): `format.spacing {"points":3}` (letter spacing), `for… |
| `format.state` | V | reference/command-reference.md#Commands (verified): …rmatting), `format.state`. |
| `format.strikethrough` | V | reference/command-reference.md#Commands (verified): …rtAlign`), `format.strikethrough {"value":true}`, |
| `format.subscript` | V | reference/command-reference.md#Commands (verified): `format.subscript` / `format.superscript` (stored as… |
| `format.superscript` | V | reference/command-reference.md#Commands (verified): …bscript` / `format.superscript` (stored as `vertAlig… |
| `format.textEffects` | V | reference/command-reference.md#Verified in detail, WordCra…: `format.textEffects` `{"style": "shadowed"}… |
| `format.underline` | V | reference/document-formats.md#Screenplay format (verified …: `format.underline {"value":true}` works for… |
| `format.underlineColor` | V | reference/formatting-and-editing.md#Character effects, par…: …":true}` + `format.underlineColor {"color":… |
| `format.wordUnderline` | V | reference/command-reference.md#Verified in detail, WordCra…: `format.wordUnderline` (state: 'quick' sele… |

## hf (3)

| id | status | note |
|---|---|---|
| `hf.next` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …f. (2): `hf.next` with a header (story p… · limit: command-reference.md: Refused … `hf.next` (not available: edit a header or footer first) |
| `hf.position` | V | reference/command-reference.md#Verified in detail, WordCra…: …f. (1): `hf.position` `{"header": 36, "f… |
| `hf.previous` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `hf.previous` from the footer back to the h… · limit: command-reference.md: Refused … `hf.previous` (not available: edit a header or footer first) |

## insert (44)

| id | status | note |
|---|---|---|
| `insert.autoText` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ent:[…]}`, `insert.autoText {"save":"Sig","… |
| `insert.blankPage` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …th":ABS}`, `insert.blankPage`, `insert.sign… |
| `insert.bookmark` | V | reference/command-reference.md#Commands (verified): …"}` (after `insert.bookmark {"name"}`) or |
| `insert.canvas` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `insert.canvas {"width":200,"height":80,"fi… |
| `insert.chart` | V | reference/command-reference.md#Commands (verified): - Charts: `insert.chart {"type":"column","data":{"ca… |
| `insert.closeHeader` | V | reference/command-reference.md#Commands (verified): … each with `insert.closeHeader` (it closes footers t… |
| `insert.coverPage` | V | reference/command-reference.md#Commands (verified): …over page: `insert.coverPage {"title","subtitle","au… |
| `insert.createFooter` | V | reference/command-reference.md#Commands (verified): `insert.createFooter {"page":1}`, `text.insert "Page… |
| `insert.createHeader` | V | reference/command-reference.md#Commands (verified): …er layout: `insert.createHeader` (caret goes in), ty… |
| `insert.crossReference` | V | reference/mail-merge-citations.md#Citations, bibliography,…: …eferences: `insert.crossReference {}` lists… |
| `insert.dateField` | V | reference/formatting-and-editing.md#Character effects, par…: `insert.dateField`/`timeField` insert the c… |
| `insert.dateTime` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …rt.shape`, `insert.dateTime`/`insert.field`… |
| `insert.deleteBookmark` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (4): `insert.deleteBookmark` `{"name"… |
| `insert.docProperty` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …the docx), `insert.docProperty {"name":"Tit… |
| `insert.dropCap` | V | reference/command-reference.md#Commands (verified): … Drop cap: `insert.dropCap {"lines":3}` on a paragra… |
| `insert.editFooter` | V | reference/formatting-and-editing.md#Character effects, par…: …age":0}` / `insert.editFooter {"page":0}` →… |
| `insert.editHeader` | V | reference/formatting-and-editing.md#Character effects, par…: …footers: `insert.editHeader {"page":0}` /… |
| `insert.equation` | V | reference/command-reference.md#Newer commands: …ng edited (`insert.equation {"linear":"a+b","edit":true}`… |
| `insert.field` | V | reference/command-reference.md#Commands (verified): Fields: `insert.field {"instr":"DATE \\@ \"yyyy\"","… |
| `insert.footer` | V | reference/command-reference.md#Commands (verified): …text":…}`, `insert.footer {"preset":"pageNumber"}` (… |
| `insert.header` | V | reference/command-reference.md#Commands (verified): …er/footer: `insert.header {"text":…}`, `insert.foote… |
| `insert.horizontalLine` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …es` title, `insert.horizontalLine`, `insert… |
| `insert.icon` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …"title"}`, `insert.icon {"query":"star"}` *… |
| `insert.link` | V | reference/command-reference.md#Commands (verified): …":…}` then `insert.link {"url":"mailto:…"}` or `{"ur… |
| `insert.object` | s | reference/sections-headers-tables.md#Tables in depth, outl…: Not run … - Not run: ink (`draw.*`: `draw.stroke {"pa… |
| `insert.pageBreak` | V | reference/command-reference.md#Commands (verified): …age break: `insert.pageBreak` adds a `\f` inside the… |
| `insert.pageField` | V | reference/command-reference.md#Commands (verified): … "Page "`, `insert.pageField`, `insert.closeHeader` … |
| `insert.pageNumber` | V | reference/command-reference.md#Commands (verified): …e numbers: `insert.pageNumber {"position":"bottom","… |
| `insert.picture` | V | reference/command-reference.md#Commands (verified): … Pictures: `insert.picture {"path":ABS,"width":pt,"a… |
| `insert.quickParts` | V | reference/sections-headers-tables.md#Tables in depth, outl…: … blocks: `insert.quickParts {"save":"Boil… |
| `insert.removeEmptyHeaders` | V | reference/formatting-and-editing.md#Character effects, par…: …veHeader`, `insert.removeEmptyHeaders`. |
| `insert.removeFooter` | V | reference/formatting-and-editing.md#Character effects, par…: …r` after), `insert.removeFooter`, `insert.r… |
| `insert.removeHeader` | V | reference/formatting-and-editing.md#Character effects, par…: …veFooter`, `insert.removeHeader`, `insert.r… |
| `insert.removeLink` | V | reference/command-reference.md#Verified in detail, WordCra…: `insert.removeLink` (state: 'lazy' hyperlin… |
| `insert.shape` | V | reference/command-reference.md#Commands (verified): …ext boxes: `insert.shape {"kind":"star","width":50,"… |
| `insert.signatureLine` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …lankPage`, `insert.signatureLine {"signer",… |
| `insert.smartArt` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …Objects: `insert.smartArt {"layout":"proc… |
| `insert.spreadsheet` | V | reference/command-reference.md#Verified in detail, WordCra…: `insert.spreadsheet` `{"csv": "a,b\n1,2"}` … |
| `insert.symbol` | V | reference/command-reference.md#Commands (verified): `insert.symbol {"char":"©"}`. |
| `insert.table` | V | reference/command-reference.md#Commands (verified): - Tables: `insert.table {"rows":3,"cols":3,"style":"… |
| `insert.textBox` | V | reference/command-reference.md#Commands (verified): `insert.textBox {"text":"…","width":120,"height":40}… |
| `insert.textFromFile` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ntalLine`, `insert.textFromFile {"path":ABS… |
| `insert.timeField` | V | reference/command-reference.md#Verified in detail, WordCra…: `insert.timeField` (state: caret in body pa… |
| `insert.wordArt` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `insert.wordArt {"text","transform":"textAr… |

## layout (18)

| id | status | note |
|---|---|---|
| `layout.break` | V | reference/command-reference.md#Commands (verified): `layout.break {"kind":"column"}` |
| `layout.columns` | V | reference/command-reference.md#Commands (verified): - Columns: `layout.columns {"count":2,"space":18,"se… |
| `layout.differentFirstPage` | V | reference/command-reference.md#Commands (verified): …irst page: `layout.differentFirstPage` (toggle). |
| `layout.differentOddEven` | V | reference/command-reference.md#Commands (verified): …henation`, `layout.differentOddEven`) — all checked |
| `layout.documentGrid` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (4): `layout.documentGrid` `{"type": … |
| `layout.hyphenation` | V | reference/command-reference.md#Commands (verified): …r"}` (also `layout.hyphenation`, `layout.differentOd… |
| `layout.lineNumbers` | V | reference/command-reference.md#Commands (verified): ….3×841.9), `layout.lineNumbers {"value":"restartPage… |
| `layout.linkToPrevious` | V | reference/document-formats.md#Screenplay format (verified …: …art":1}` → `layout.linkToPrevious` → `inser… |
| `layout.manualHyphenation` | s | reference/formatting-and-editing.md#Character effects, par…: Not run … - Not run or not possible headless: `arrang… |
| `layout.margins` | V | reference/command-reference.md#Commands (verified): - Page: `layout.margins {"top":36,"bottom":36,"left"… |
| `layout.orientation` | V | reference/command-reference.md#Commands (verified): `layout.orientation {"value":"landscape"}` → only th… |
| `layout.pageNumberFormat` | V | reference/command-reference.md#Commands (verified): …ing style: `layout.pageNumberFormat {"format":"lower… |
| `layout.pageSetup` | V | reference/command-reference.md#Sweep of every remaining co…: …ts added); `layout.pageSetup {}` → the whol… |
| `layout.section` | V | reference/sections-headers-tables.md#Sections: `layout.sec…: - `layout.section {}` is a READ: it ret… |
| `layout.sectionRtl` | V | reference/command-reference.md#Verified in detail, WordCra…: `layout.sectionRtl` `{"value":true}`: secti… |
| `layout.size` | V | reference/command-reference.md#Commands (verified): …age setup: `layout.size {"name":"A4"}` (595.3×841.9)… |
| `layout.textDirection` | V | reference/command-reference.md#Verified in detail, WordCra…: `layout.textDirection` `{"value":"down"}`: … |
| `layout.verticalAlign` | V | reference/command-reference.md#Commands (verified): `layout.verticalAlign {"value":"center"}` (also `lay… |

## link (1)

| id | status | note |
|---|---|---|
| `link.targets` | V | reference/command-reference.md#Sweep of every remaining co…: …et in it); `link.targets {}` → `{bookmarks,… |

## list (3)

| id | status | note |
|---|---|---|
| `list.define` | V | recipes/resume_ats.py#: …T_NUM = 1 # list.define on a blank template returns num 1 (verified, WordCraft 0… |
| `list.get` | V | reference/command-reference.md#Sweep of every remaining co…: …t}],top}`; `list.get {}` → the caret's list… |
| `list.multilevelPreset` | V | reference/command-reference.md#Commands (verified): …numbering: `list.multilevelPreset {"preset":"heading… |

## mailings (23)

| id | status | note |
|---|---|---|
| `mailings.addressBlock` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: mailings.addressBlock {} / mailings.greetin… |
| `mailings.checkErrors` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: mailings.checkErrors {} → {"ok":true,"recor… |
| `mailings.editRecipients` | V | reference/command-reference.md#Sweep of every remaining co…: … SmartArt; `mailings.editRecipients {}` → `… |
| `mailings.envelopes` | V | reference/formatting-and-editing.md#Character effects, par…: `mailings.envelopes {"delivery","return","s… |
| `mailings.filterRecipients` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: mailings.filterRecipients {"rules":[{"field… |
| `mailings.findRecipient` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `mailings.findRecipient` `{"text": "Bob"}` … · limit: command-reference.md: Refused … `mailings.findRecipient` (bad parameters: `text` (string) is… |
| `mailings.finish` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: mailings.finish {"path":"/abs/merged.docx",… |
| `mailings.first` | V | reference/command-reference.md#Newer commands: … commands: `mailings.first`, `mailings.last`, `mailings.g… |
| `mailings.goToRecord` | V | reference/command-reference.md#Newer commands: …ngs.last`, `mailings.goToRecord {"record":2}` (1-based; t… |
| `mailings.greetingLine` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: …sBlock {} / mailings.greetingLine {} # buil… |
| `mailings.highlightFields` | V | reference/command-reference.md#Verified in detail, WordCra…: `mailings.highlightFields` (state: letters … |
| `mailings.insertField` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: …":"Dear "}, mailings.insertField {"field":"… |
| `mailings.labels` | V+ | reference/formatting-and-editing.md#Character effects, par…: …{"csv"}` → `mailings.labels {"product":"let… · limit: log.md: … bookmark; `mailings.labels fromRecipients` continues across… |
| `mailings.last` | V | reference/command-reference.md#Newer commands: …gs.first`, `mailings.last`, `mailings.goToRecord {"record… |
| `mailings.matchFields` | V | reference/command-reference.md#Sweep of every remaining co…: …es,sort}`; `mailings.matchFields {}` → the … |
| `mailings.next` | V | reference/command-reference.md#Verified in detail, WordCra…: `mailings.next` (state: letters merge, prev… |
| `mailings.preview` | d | reference/command-reference.md#Newer commands: …Field` and `mailings.preview {"on":true}`), and `view.rea… |
| `mailings.previous` | V | reference/command-reference.md#Verified in detail, WordCra…: `mailings.previous` (state: letters merge, … |
| `mailings.printDocuments` | V | reference/command-reference.md#Newer commands: …ecord:2}`, `mailings.printDocuments` → `{records:3}` |
| `mailings.recipients` | V | reference/command-reference.md#Verified in detail, WordCra…: …works with `mailings.recipients {rows,field… |
| `mailings.rules` | V | reference/mail-merge-citations.md#Mail merge (verified hea…: mailings.rules {"rule":"IF","field":"Role",… |
| `mailings.sortRecipients` | V | reference/command-reference.md#Verified in detail, WordCra…: `mailings.sortRecipients` `{"sort": [{"fiel… |
| `mailings.start` | V | reference/formatting-and-editing.md#Character effects, par…: … merge): `mailings.start {"kind":"labels"… |

## object (1)

| id | status | note |
|---|---|---|
| `object.altText` | V | reference/command-reference.md#Commands (verified): …ge.nudge`, `object.altText`. |

## outline (26)

| id | status | note |
|---|---|---|
| `outline.close` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …e":true}`, `outline.close` → `{mode:"print"… |
| `outline.collapse` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …wn:[0,4]`, `outline.collapse/expand/toggle … |
| `outline.demote` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …e. (8): `outline.demote` (state: caret i… · limit: command-reference.md: Refused … `outline.demote` (nothing to demote) |
| `outline.demoteToBody` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.demoteToBody` (state: caret in Hea… |
| `outline.expand` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.expand` `{"block": 3}` (state: Hea… |
| `outline.firstLineOnly` | V | reference/sections-headers-tables.md#Tables in depth, outl…: … "Three"), `outline.firstLineOnly {"value":… |
| `outline.level` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.level` `{"level": 1}` (state: care… |
| `outline.moveDown` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `outline.moveDown` (state: caret in Heading… · limit: command-reference.md: Refused … `outline.moveDown` (already at the bottom) |
| `outline.moveUp` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …Heading1`, `outline.moveUp/moveDown` (moves… |
| `outline.promote` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `outline.promote/demote/level {"level":3\|"b… |
| `outline.promoteToHeading1` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.promoteToHeading1` (state: caret i… |
| `outline.selectSubtree` | V | reference/sections-headers-tables.md#Tables in depth, outl…: … subtree), `outline.selectSubtree {"block":… |
| `outline.showAll` | V | reference/command-reference.md#Verified in detail, WordCra…: …. (10): `outline.showAll` `outline.state… |
| `outline.showFormatting` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showFormatting` `{"value": true}` … |
| `outline.showLevel` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `outline.showLevel`/`showAll` only work i… |
| `outline.showLevel1` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel1` in `view.outline` on h… |
| `outline.showLevel2` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel2` in `view.outline` on h… |
| `outline.showLevel3` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel3` in `view.outline` on h… |
| `outline.showLevel4` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel4` in `view.outline` on h… |
| `outline.showLevel5` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel5` in `view.outline` on h… |
| `outline.showLevel6` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel6` in `view.outline` on h… |
| `outline.showLevel7` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel7` in `view.outline` on h… |
| `outline.showLevel8` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel8` in `view.outline` on h… |
| `outline.showLevel9` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.showLevel9` in `view.outline` on h… |
| `outline.state` | V | reference/command-reference.md#Verified in detail, WordCra…: …outline` + `outline.state` for outline leve… |
| `outline.toggle` | V | reference/command-reference.md#Verified in detail, WordCra…: `outline.toggle` `{"block": 1}` (state: Hea… |

## para (50)

| id | status | note |
|---|---|---|
| `para.addSpaceBefore` | V | reference/formatting-and-editing.md#Character effects, par…: …f\|double`, `para.addSpaceBefore` (12 pt), `… |
| `para.align` | V | reference/formatting-and-editing.md#Paragraph formatting, …: - `para.align {"value":"left\|center\|right\|j… |
| `para.alignCenter` | V | reference/formatting-and-editing.md#Character effects, par…: …rameters): `para.alignCenter\|alignLeft\|alig… |
| `para.alignLeft` | V | reference/command-reference.md#Verified in detail, WordCra…: …. (18): `para.alignLeft` (state: caret i… |
| `para.alignRight` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.alignRight` (state: caret in body par… |
| `para.asianTypography` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.asianTypography` (state: caret in bod… |
| `para.borders` | V | reference/command-reference.md#Commands (verified): …l clears), `para.borders {"kind":"left","width":3, |
| `para.bullets` | V | reference/existing-documents.md#Reformatting a real docume…: - `para.bullets {"kind":"bullet"}` TOGGLE… |
| `para.defineBullet` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.defineBullet` `{"char": "\u2022"}` (s… |
| `para.defineNumber` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.defineNumber` `{"format": "decimal", … |
| `para.demote` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `para.demote` (state: paragraph 4 made Head… · limit: command-reference.md: Refused … `para.demote` (nothing to demote) |
| `para.dialog` | V | reference/command-reference.md#Verified in detail, WordCra…: …a. (1): `para.dialog` live: opens the Pa… |
| `para.distribute` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.distribute` (state: caret in body par… |
| `para.double` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.double` (state: caret in body paragra… |
| `para.hangingIndent` | V | reference/formatting-and-editing.md#Character effects, par…: …\|outdent`, `para.hangingIndent` (indentLeft… |
| `para.heading1` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …ra.reset`, `para.heading1…3`. |
| `para.heading2` | V | reference/formatting-and-editing.md#Character effects, par…: …irst −36), `para.heading2\|heading3`, `para.… |
| `para.heading3` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.heading3` (state: caret in body parag… |
| `para.indent` | V | reference/formatting-and-editing.md#Character effects, par…: …aceAfter`, `para.indent\|outdent`, `para.han… |
| `para.indents` | V | reference/formatting-and-editing.md#Paragraph formatting, …: `para.indents {"left":36,"right":36,"firstL… |
| `para.justify` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.justify` (state: caret in body paragr… |
| `para.keepLines` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …keepNext`, `para.keepLines`, `para.pageBrea… |
| `para.keepNext` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …agination: `para.keepNext`, `para.keepLines… |
| `para.lineSpacing` | V | reference/document-formats.md#Screenplay format (verified …: …y element (`para.lineSpacing {"exactly":12}… |
| `para.listLevel` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …legal"}` + `para.listLevel {"level":1}` → "… |
| `para.ltr` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.ltr` (state: caret in body paragraph … |
| `para.moveDown` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `para.moveDown` (state: caret in Title para… · limit: command-reference.md: Refused … `para.moveDown` (a table is in the way) |
| `para.moveUp` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.moveUp` (state: caret in 'Gamma' body… |
| `para.multilevel` | V | reference/formatting-and-editing.md#Paragraph formatting, …: `para.multilevel {"kind":"legal"}` + `para.… |
| `para.normal` | V | reference/formatting-and-editing.md#Character effects, par…: `para.normal` only restores the style `No… |
| `para.numbering` | V | reference/formatting-and-editing.md#Paragraph formatting, …: … ends it), `para.numbering {"kind":"numbere… |
| `para.oneAndHalf` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.oneAndHalf` (state: caret in body par… |
| `para.outdent` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.outdent` (state: paragraph 2 given in… |
| `para.outlineLevel` | V | reference/formatting-and-editing.md#Character effects, par…: …heading3`, `para.outlineLevel`. |
| `para.pageBreakBefore` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …eepLines`, `para.pageBreakBefore`, `para.wi… |
| `para.promote` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.promote` (state: caret in body paragr… |
| `para.removeHanging` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.removeHanging` (state: paragraph 2 gi… |
| `para.removeSpaceAfter` | V | reference/formatting-and-editing.md#Character effects, par…: …` (12 pt), `para.removeSpaceAfter`, `para.i… |
| `para.reset` | V | reference/document-formats.md#Policy manual with a TOC, ca…: …tarts with `para.reset`, `para.style`, `for… |
| `para.restartNumbering` | V | reference/formatting-and-editing.md#Paragraph formatting, …: Also `para.restartNumbering`, `defineBullet… |
| `para.rtl` | V | reference/command-reference.md#Verified in detail, WordCra…: `para.rtl` (state: caret in body paragraph … |
| `para.set` | V | reference/command-reference.md#Property names (verified vi…: …aph props (`para.set {"props":…}`, `styles.… |
| `para.setNumberingValue` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …1)", "i."; `para.setNumberingValue {"value"… |
| `para.shading` | V | reference/command-reference.md#Commands (verified): …raph look: `para.shading {"color":"E7E6E6"}` (null c… |
| `para.single` | V | reference/formatting-and-editing.md#Character effects, par…: …stribute`, `para.single\|oneAndHalf\|double`,… |
| `para.sort` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …ingValue`, `para.sort`, copy/paste format, … |
| `para.spacing` | V | reference/formatting-and-editing.md#Paragraph formatting, …: `para.spacing {"before":24,"after":12}` |
| `para.style` | V | reference/command-reference.md#Commands (verified): …,"para"}`, `para.style {"style"}`, |
| `para.tabs` | V | reference/formatting-and-editing.md#Paragraph formatting, …: - Tabs: `para.tabs {"set":[{"pos":300,"alig… |
| `para.widowControl` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …akBefore`, `para.widowControl` each `{"valu… |

## picture (14)

| id | status | note |
|---|---|---|
| `picture.altText` | V | reference/formatting-and-editing.md#Accessibility checker …: …t.altText`/`picture.altText`), |
| `picture.border` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …shadow"}`, `picture.border {"color","width"… |
| `picture.change` | V | reference/sections-headers-tables.md#Tables in depth, outl…: … it), then `picture.change {"path"}` swaps … |
| `picture.color` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ractions), `picture.color {"mode":"sepia\|gr… |
| `picture.compress` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …alt text), `picture.compress`, `picture.cha… |
| `picture.corrections` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ercent"}`, `picture.corrections {"brightnes… |
| `picture.crop` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …Aspect"}`, `picture.crop {"left":0.1,"right… |
| `picture.effects` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …n\|tint"}`, `picture.effects {"effect":"blur… |
| `picture.iconColor` | V | reference/command-reference.md#Verified in detail, WordCra…: …e. (1): `picture.iconColor` `{"color": "… |
| `picture.removeBackground` | V+ | reference/sections-headers-tables.md#Tables in depth, outl…: …{"path"}`, `picture.removeBackground {"tole… · limit: sections-headers-tables.md: Not run … - Not run: ink (`draw.*`: `draw.stroke {"page","points","too… |
| `picture.reset` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …rative"}`, `picture.reset` (clears crop/eff… |
| `picture.size` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ollow with `picture.size {"width"}` and `pi… |
| `picture.style` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `picture.style {"style":"simpleFrame\|thickF… |
| `picture.transparency` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …e\|none"}`, `picture.transparency {"percent"… |

## proof (3)

| id | status | note |
|---|---|---|
| `proof.installPack` | V | reference/formatting-and-editing.md#Language packs and 0.1…: `proof.installPack {"locale":"nl"}` downloa… |
| `proof.packs` | V | reference/command-reference.md#Newer commands: …ad it from `proof.packs`, whose result now has a `languag… |
| `proof.removePack` | V | reference/formatting-and-editing.md#Language packs and 0.1…: `proof.removePack {"locale"}` removes one. |

## readAloud (7)

| id | status | note |
|---|---|---|
| `readAloud.next` | V | reference/command-reference.md#Verified in detail, WordCra…: …d. (4): `readAloud.next` after `readAlou… |
| `readAloud.playPause` | V | reference/command-reference.md#Verified in detail, WordCra…: `readAloud.playPause` starts a headless ses… |
| `readAloud.previous` | V | reference/command-reference.md#Verified in detail, WordCra…: `readAloud.previous` index 2 -> 1 ("Two sen… |
| `readAloud.skipCitations` | V | reference/command-reference.md#Verified in detail, WordCra…: `readAloud.skipCitations` `{"value":false}`… |
| `readAloud.speed` | V | reference/command-reference.md#Verified in detail, WordCra…: `readAloud.speed` `{"value": 1.5}` (state: … |
| `readAloud.status` | V | reference/command-reference.md#Sweep of every remaining co…: …(`Mod+B`); `readAloud.status {}` → `{state:… |
| `readAloud.stop` | V | reference/command-reference.md#Verified in detail, WordCra…: `readAloud.stop` state playing -> stopped, … |

## references (25)

| id | status | note |
|---|---|---|
| `references.addText` | V | reference/formatting-and-editing.md#Styles management, ind…: …emoveToc`, `references.addText` (add a head… |
| `references.bibliography` | V | reference/mail-merge-citations.md#Citations, bibliography,…: references.bibliography {"title":"Reference… |
| `references.caption` | V | reference/command-reference.md#Commands (verified): … Captions: `references.caption {"label":"Figure","te… |
| `references.citation` | V | reference/mail-merge-citations.md#Citations, bibliography,…: references.citation {"source":{"tag":"Smith… |
| `references.citationStyle` | V | reference/mail-merge-citations.md#Citations, bibliography,…: references.citationStyle {"style":"APA"} # … |
| `references.convertNotes` | s | reference/formatting-and-editing.md#Styles management, ind…: Not run … - Not run: `styles.manage/pane/apply`, `too… |
| `references.endnote` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (3): `references.endnote` `{"text": "… |
| `references.footnote` | V | reference/command-reference.md#Commands (verified): …Footnotes: `references.footnote {"text":…}` returns … |
| `references.index` | V | reference/formatting-and-editing.md#Styles management, ind…: `references.index {"columns":1,"title":"Ind… |
| `references.markCitation` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …*Method: `references.markCitation` + `ref… · limit: formatting-and-editing.md: Not run … - Not run: `styles.manage/pane/apply`, `tools.attachTemplate… |
| `references.markEntry` | V | reference/formatting-and-editing.md#Styles management, ind…: …ct.text`), `references.markEntry {"entry":"… |
| `references.nextFootnote` | V | reference/command-reference.md#Commands (verified): `references.nextFootnote` also |
| `references.noteOptions` | s | reference/formatting-and-editing.md#Styles management, ind…: Not run … - Not run: `styles.manage/pane/apply`, `too… |
| `references.notes` | V | reference/command-reference.md#Verified in detail, WordCra…: `references.notes` (state: a footnote inser… |
| `references.removeToc` | V | reference/formatting-and-editing.md#Styles management, ind…: …pdateToc`, `references.removeToc`, `referen… |
| `references.researcher` | V+ | reference/command-reference.md#Verified in detail, the las…: …w.split and references.researcher checked l… · limit: command-reference.md: …s. (1): `references.researcher` checked, unavailable by d… |
| `references.sources` | V | reference/mail-merge-citations.md#Citations, bibliography,…: …on styles, `references.sources`, cross-refe… |
| `references.tableOfAuthorities` | V | reference/command-reference.md#Verified in detail, WordCra…: `references.tableOfAuthorities` (state: car… |
| `references.tableOfFigures` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …figures: `references.tableOfFigures {"lab… |
| `references.toc` | V | reference/command-reference.md#Commands (verified): … contents: `references.toc {"levels":2,"title":"Cont… |
| `references.updateAuthorities` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (1): `references.updateAuthorities` a… |
| `references.updateFields` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (1): `references.updateFields` `{"all… |
| `references.updateFigures` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …n"}`, then `references.updateFigures` → a l… |
| `references.updateIndex` | V | reference/formatting-and-editing.md#Styles management, ind…: `references.updateIndex` after later edits. |
| `references.updateToc` | V | reference/command-reference.md#Commands (verified): … 1"`, then `references.updateToc` at the end → TOC l… |

## review (36)

| id | status | note |
|---|---|---|
| `review.accept` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …tChange` + `review.accept`/`review.reject` … |
| `review.acceptAll` | V | reference/command-reference.md#Commands (verified): `review.acceptAll` keeps the edits, `review.rejectAl… |
| `review.addToDictionary` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …ggestion`, `review.addToDictionary`, `revie… |
| `review.applySuggestion` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …gestions`, `review.applySuggestion`, `revie… |
| `review.changes` | V | reference/command-reference.md#Commands (verified): `review.changes` lists them |
| `review.combine` | V | reference/existing-documents.md#Document comparison (verif…: … variants, `review.combine`. |
| `review.comments` | V | reference/command-reference.md#Commands (verified): `review.comments` lists them (author, parent, resolv… |
| `review.compare` | V | reference/existing-documents.md#Document comparison (verif…: `review.compare {"path":ABS_revised.docx \| … |
| `review.deleteComment` | V | reference/formatting-and-editing.md#Character effects, par…: …sComment`, `review.deleteComment {"id"\|"all… |
| `review.editComment` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …ew.reply`, `review.editComment`, `review.re… |
| `review.editor` | V | reference/command-reference.md#Verified in detail, the las…: review.editor and table.borderPainter re-ru… |
| `review.hideInk` | V | reference/formatting-and-editing.md#Character effects, par…: …usChange`, `review.hideInk {"value"}`. |
| `review.ignoreAll` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …ctionary`, `review.ignoreAll`, `review.lang… |
| `review.issues` | V | reference/command-reference.md#Commands (verified): `review.issues` → list of spelling/grammar issues wi… |
| `review.language` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …gnoreAll`, `review.language`, `review.thesa… |
| `review.language.preferred` | V | reference/command-reference.md#Newer commands: …-11-03): `review.language.preferred {"lang":"de-DE"}` s… |
| `review.markup` | V | reference/formatting-and-editing.md#Styles management, ind…: `review.markup {}` toggles and returns `{sh… |
| `review.newComment` | V | reference/command-reference.md#Commands (verified): …ct.text` → `review.newComment {"text"}` returns `{"i… |
| `review.nextChange` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: `review.nextChange` + `review.accept`/`revi… |
| `review.nextComment` | V | reference/formatting-and-editing.md#Character effects, par…: …d,story}`, `review.nextComment/previousComm… |
| `review.previousChange` | V | reference/formatting-and-editing.md#Character effects, par…: …ted:[0]}`, `review.previousChange`, `review… |
| `review.previousComment` | V | reference/command-reference.md#Verified in detail, WordCra…: …w. (1): `review.previousComment` (state:… |
| `review.proofing` | V | reference/command-reference.md#Verified in detail, WordCra…: …w. (1): `review.proofing` live: toggles … |
| `review.readAloud` | s | reference/formatting-and-editing.md#Character effects, par…: Not run … - Not run or not possible headless: `arrang… |
| `review.reject` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …ew.accept`/`review.reject` act on one |
| `review.rejectAll` | V | reference/command-reference.md#Commands (verified): …the edits, `review.rejectAll` restores the original … |
| `review.reply` | V | reference/command-reference.md#Commands (verified): `review.reply {"id","text"}` |
| `review.resolveComment` | V | reference/command-reference.md#Commands (verified): `review.resolveComment {"id","value":true}` |
| `review.restrict` | V+ | reference/formatting-and-editing.md#Next-tier workflows (v…: …ryption: `review.restrict {"mode":"readOn… · limit: formatting-and-editing.md: Not run … - Not run: `styles.manage/pane/apply`, `tools.attachTemplate… |
| `review.showMarkup` | V | reference/document-formats.md#Policy manual with a TOC, ca…: …docx --cmd 'review.showMarkup={"value":true… |
| `review.spelling` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …grammar: `review.spelling` / `review.issu… |
| `review.suggestions` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: `review.suggestions`, `review.applySuggesti… |
| `review.thesaurus` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …language`, `review.thesaurus`, `review.word… |
| `review.trackChanges` | V | reference/command-reference.md#Commands (verified): `review.trackChanges {"value":true}` → later edits b… |
| `review.trackingOptions` | V | reference/formatting-and-editing.md#Styles management, ind…: `review.trackingOptions {"insertMark":"bold… |
| `review.wordCount` | V | reference/command-reference.md#Commands (verified): … Proofing: `review.wordCount` → words/characters/pag… |

## select (15)

| id | status | note |
|---|---|---|
| `select.addObject` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (9): `select.addObject` `{"index": 0}… |
| `select.all` | V | reference/formatting-and-editing.md#Paragraph formatting, …: …lection: `select.all`, or `caret.docStart… |
| `select.collapse` | V | reference/document-formats.md#Document styles (traditional…: …atHeader`, `select.collapse`) → per cell `t… |
| `select.column` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.column` (state: caret in body parag… |
| `select.dragUnit` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.dragUnit` `{"unit": "word", "pos": … |
| `select.extend` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.extend` (state: caret in body parag… |
| `select.line` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.line` (state: caret in body paragra… |
| `select.member` | V | reference/log.md#Log: …rlier; new `select.member` verified headless. |
| `select.objects` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.objects` `{"index": 0}` (state: one… |
| `select.paragraph` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.paragraph` (state: caret in body pa… |
| `select.range` | V | reference/existing-documents.md#Reformatting a real docume…: delete by `select.range` on the cell paragr… |
| `select.sentence` | V | reference/command-reference.md#Sweep of every remaining co…: …with text; `select.sentence\|paragraph\|line … |
| `select.similar` | V | reference/command-reference.md#Verified in detail, WordCra…: `select.similar` (state: 'quick' selected, … |
| `select.text` | V | recipes/resume_ats.py#: …Links last: select.text keeps the visible text and turns it into the link (verif… |
| `select.word` | V | reference/formatting-and-editing.md#Character effects, par…: …Previous`, `select.word\|sentence\|paragraph\|… |

## shape (9)

| id | status | note |
|---|---|---|
| `shape.alignText` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ert270"}`, `shape.alignText {"anchor":"t\|ct… |
| `shape.breakLink` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …arget"}` / `shape.breakLink` (flow text bet… |
| `shape.change` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …"width"}`, `shape.change {"kind":"heart"}` … |
| `shape.connect` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …xt boxes), `shape.connect`. |
| `shape.effects` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …d shadow), `shape.effects {"shadow":{"color… |
| `shape.fill` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …:60}` then `shape.fill {"color":"FFC000","t… |
| `shape.link` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …\|ctr\|b"}`, `shape.link {"target"}` / `shape… |
| `shape.outline` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …type"}}`), `shape.outline {"color","width"}… |
| `shape.textDirection` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `shape.textDirection {"dir":"horz\|vert\|vert… |

## smartArt (9)

| id | status | note |
|---|---|---|
| `smartArt.addShape` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (8): `smartArt.addShape` `{"text": "F… |
| `smartArt.colors` | V | reference/command-reference.md#Verified in detail, WordCra…: `smartArt.colors` `{"variant": "accent2"}` … |
| `smartArt.demote` | V | reference/command-reference.md#Verified in detail, WordCra…: `smartArt.demote` `{"index": 1}` (state: Sm… |
| `smartArt.itemColor` | V | reference/formatting-and-editing.md#0.15.2 changes (verifi…: …or`, and `smartArt.itemColor {"index":1,"… |
| `smartArt.items` | V | reference/command-reference.md#Sweep of every remaining co…: …s,size}]`; `smartArt.items {"items":["One",… |
| `smartArt.layout` | V | reference/command-reference.md#Verified in detail, WordCra…: `smartArt.layout` `{"layout": "cycle"}` (st… |
| `smartArt.promote` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `smartArt.promote` `{"index": 1}` (state: S… · limit: command-reference.md: Refused … `smartArt.promote` (this item is already at the top level) |
| `smartArt.reset` | V | reference/command-reference.md#Verified in detail, WordCra…: `smartArt.reset` (state: SmartArt recoloure… |
| `smartArt.textPane` | V | reference/command-reference.md#Verified in detail, WordCra…: `smartArt.textPane` `{"value": true}` (stat… |

## styles (16)

| id | status | note |
|---|---|---|
| `styles.addToGallery` | V | reference/formatting-and-editing.md#Styles management, ind…: `styles.addToGallery {"style"}` |
| `styles.apply` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (3): `styles.apply` `{"style": "Headi… |
| `styles.copyFrom` | V | reference/formatting-and-editing.md#Styles management, ind…: ….inspect`, `styles.copyFrom` (Organizer), `… |
| `styles.create` | V | reference/command-reference.md#Commands (verified): - Styles: `styles.create {"name","basedOn"}`, `style… |
| `styles.delete` | V | reference/formatting-and-editing.md#Styles management, ind…: `styles.delete {"style"}` → `{deleted:[…],r… |
| `styles.inspect` | V | reference/command-reference.md#Commands (verified): …les.list`, `styles.inspect`. |
| `styles.inspector` | V | reference/command-reference.md#Verified in detail, WordCra…: `styles.inspector` `{"value": true}` (state… |
| `styles.inspectorClear` | V | reference/command-reference.md#Verified in detail, WordCra…: `styles.inspectorClear` `{"level": "paragra… |
| `styles.list` | V | reference/command-reference.md#Commands (verified): `styles.list`, `styles.inspect`. |
| `styles.manage` | s | reference/formatting-and-editing.md#Styles management, ind…: Not run … - Not run: `styles.manage/pane/apply`, `too… |
| `styles.modify` | V | reference/command-reference.md#Property names (verified vi…: …rops":…}`, `styles.modify {"para":…}`): |
| `styles.organizer` | V | reference/formatting-and-editing.md#Styles management, ind…: …rganizer), `styles.organizer`. |
| `styles.pane` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (1): `styles.pane` live: toggles the … |
| `styles.rename` | V | reference/formatting-and-editing.md#Styles management, ind…: `styles.rename {"style","name"}` → `{id,nam… |
| `styles.setVisibility` | V | reference/formatting-and-editing.md#Styles management, ind…: …ls such as `styles.setVisibility` report `s… |
| `styles.updateToMatch` | V | reference/formatting-and-editing.md#Styles management, ind…: `styles.updateToMatch {}` (style := the car… |

## table (48)

| id | status | note |
|---|---|---|
| `table.altText` | V | reference/command-reference.md#Commands (verified): `table.altText` (all accepted; only merge, shading a… |
| `table.autofit` | V | reference/document-formats.md#Document styles (traditional…: …herwise) → `table.autofit {"mode":"fixed"}`… |
| `table.borderPainter` | V | reference/command-reference.md#Verified in detail, the las…: ….editor and table.borderPainter re-run here… |
| `table.borders` | V | reference/command-reference.md#Commands (verified): Also `table.borders {"kind":"inside","width":0.5,"co… |
| `table.cellAlign` | V | reference/command-reference.md#Commands (verified): `table.cellAlign {"value":"bottomRight"}` writes ver… |
| `table.cellMargins` | V | reference/command-reference.md#Commands (verified): `table.cellMargins`, `table.look {"headerRow","bande… |
| `table.columnWidth` | V | reference/command-reference.md#Commands (verified): - `table.columnWidth {"width":pt}` sets only the car… |
| `table.deleteCells` | V | reference/command-reference.md#Verified in detail, WordCra…: …. (16): `table.deleteCells` (state: firs… |
| `table.deleteColumn` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.deleteColumn` (state: caret in table… |
| `table.deleteRow` | V | reference/existing-documents.md#Reformatting a real docume…: `table.deleteRow` with the caret in a cell … |
| `table.deleteStyle` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ifyStyle`, `table.deleteStyle`. |
| `table.deleteTable` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.deleteTable` (state: caret in table)… |
| `table.distributeColumns` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …\|fixed"}`, `table.distributeColumns/distrib… |
| `table.distributeRows` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.distributeRows` (state: whole table … |
| `table.draw` | s | reference/formatting-and-editing.md#Character effects, par…: Not run … - Not run or not possible headless: `arrang… |
| `table.eraser` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `table.eraser` `{"page": 0, "x": 306, "y": … · limit: command-reference.md: Refused … `table.eraser` (there's no border between two cells there) |
| `table.fitColumn` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `table.fitColumn` `{"page": 0, "x": 306, "y… · limit: command-reference.md: Refused … `table.fitColumn` (there's no column border there) |
| `table.formula` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: …nd sort: `table.formula {"formula":"=SUM(… |
| `table.fromText` | V | reference/command-reference.md#Commands (verified): …e}`), then `table.fromText {"separator":"tab","autof… |
| `table.insertAt` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `table.insertAt` `{"page": 0, "x": 68, "y":… · limit: command-reference.md: Refused … `table.insertAt` (there's no table selection area or button … |
| `table.insertColumnLeft` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.insertColumnLeft` (state: caret in t… |
| `table.insertColumnRight` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.insertColumnRight` (state: caret in … |
| `table.insertRowAbove` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.insertRowAbove` (state: caret in tab… |
| `table.insertRowBelow` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ew caret): `table.insertRowBelow\|insertRowA… |
| `table.look` | V | reference/command-reference.md#Commands (verified): …lMargins`, `table.look {"headerRow","bandedRows"}`, … |
| `table.merge` | V | reference/command-reference.md#Commands (verified): …xtra cell, `table.merge` |
| `table.modifyStyle` | V | reference/sections-headers-tables.md#Tables in depth, outl…: also `table.modifyStyle`, `table.deleteStyl… |
| `table.moveDrag` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `table.moveDrag` `{"page": 0, "x": 66, "y":… · limit: command-reference.md: Refused … `table.moveDrag` (there's no table selection area or button … |
| `table.newStyle` | V | reference/sections-headers-tables.md#Tables in depth, outl…: … styles: `table.newStyle {"name":"Brand",… |
| `table.properties` | V | reference/command-reference.md#Commands (verified): … Grid"}` → `table.properties {"align":"center"}`. |
| `table.quick` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `table.quick {"kind":"calendar\|tabular\|matr… |
| `table.repeatHeader` | V | reference/command-reference.md#Commands (verified): …":true}` → `table.repeatHeader`. |
| `table.resizeDrag` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `table.resizeDrag` `{"page": 0, "x": 306, "… · limit: command-reference.md: Refused … `table.resizeDrag` (there's no table border or resize handle… |
| `table.rowHeight` | V | reference/command-reference.md#Commands (verified): …edRows"}`, `table.rowHeight {"height","rule":"atLeas… |
| `table.rtl` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.rtl` `{"value": true}` (state: whole… |
| `table.selectAt` | V+ | reference/command-reference.md#Verified in detail, WordCra…: … commands (`table.selectAt`/`insertAt`/`fit… · limit: command-reference.md: Refused … `table.selectAt` (there's no table selection area or button … |
| `table.selectCell` | V | reference/command-reference.md#Commands (verified): …e across = `table.selectCell`, `caret.right {"extend… |
| `table.selectColumn` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …litTable`, `table.selectColumn/selectTable`… |
| `table.selectRow` | V | reference/command-reference.md#Commands (verified): …ble), then `table.selectRow` → `table.shading {"colo… |
| `table.selectTable` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.selectTable` (state: caret in table)… |
| `table.shading` | V | reference/command-reference.md#Commands (verified): …lectRow` → `table.shading {"color":"D9E2F3"}` |
| `table.sort` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: `table.sort {"column":1,"order":"ascending"… |
| `table.split` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …buteRows`, `table.split {"columns":2,"rows"… |
| `table.splitTable` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …rows":1}`, `table.splitTable`, `table.selec… |
| `table.style` | V | reference/command-reference.md#Commands (verified): `table.style {"style":"Table Grid"}` → `table.proper… |
| `table.textDirection` | V | reference/sections-headers-tables.md#Tables in depth, outl…: …ectTable`, `table.textDirection {"value":"h… |
| `table.toText` | V | reference/sections-headers-tables.md#Tables in depth, outl…: `table.toText {"separator":"comma\|tab\|parag… |
| `table.viewGridlines` | V | reference/command-reference.md#Verified in detail, WordCra…: `table.viewGridlines` `{"value": true}` (st… |

## text (23)

| id | status | note |
|---|---|---|
| `text.backTab` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (5): `text.backTab` (state: tab then … |
| `text.backspace` | V | reference/formatting-and-editing.md#Character effects, par…: …33"}` (é), `text.backspace`, `text.deleteWo… |
| `text.columnBreak` | V | reference/command-reference.md#Verified in detail, WordCra…: `text.columnBreak` (state: caret mid paragr… |
| `text.copyright` | V | reference/command-reference.md#Commands (verified): …t.emDash`, `text.copyright`, |
| `text.delete` | V | reference/formatting-and-editing.md#Next-tier workflows (v…: … deletion; `text.delete`) become `&lt;w:ins&gt;`/… |
| `text.deleteWordBack` | V | reference/formatting-and-editing.md#Character effects, par…: …ackspace`, `text.deleteWordBack/Forward` |
| `text.deleteWordForward` | V | reference/command-reference.md#Verified in detail, WordCra…: `text.deleteWordForward` (state: caret at o… |
| `text.ellipsis` | V | reference/formatting-and-editing.md#Character effects, par…: …nsertTab`, `text.ellipsis`, `text.registere… |
| `text.emDash` | V | reference/command-reference.md#Commands (verified): …nbHyphen`, `text.emDash`, `text.copyright`, |
| `text.insert` | V | reference/command-reference.md#Commands (verified): - Text: `text.insert {"text"}` (a `\t` in the text i… |
| `text.insertTab` | V | reference/formatting-and-editing.md#Character effects, par…: …haracters: `text.insertTab`, `text.ellipsis… |
| `text.lineBreak` | V | reference/command-reference.md#Commands (verified): `text.lineBreak`, `text.nbsp`, `text.nbHyphen`, `tex… |
| `text.nbHyphen` | V | reference/command-reference.md#Commands (verified): …ext.nbsp`, `text.nbHyphen`, `text.emDash`, `text.cop… |
| `text.nbsp` | V | reference/command-reference.md#Commands (verified): …ineBreak`, `text.nbsp`, `text.nbHyphen`, `text.emDas… |
| `text.newParagraph` | V | SKILL.md#Traps (each one cost time): … you press `text.newParagraph` ("pear" → "Pear"; list items too),… |
| `text.optionalHyphen` | V | reference/formatting-and-editing.md#Character effects, par…: …rademark`, `text.optionalHyphen`, `text.pag… |
| `text.overtype` | V | reference/command-reference.md#Verified in detail, WordCra…: `text.overtype` (state: caret mid paragraph… |
| `text.pageBreak` | V | reference/formatting-and-editing.md#Character effects, par…: …alHyphen`, `text.pageBreak` (a `\f` inside … |
| `text.registered` | V | reference/formatting-and-editing.md#Character effects, par…: …ellipsis`, `text.registered`, `text.tradema… |
| `text.tab` | V | reference/command-reference.md#Commands (verified): `text.tab` exist (nbsp and emDash checked). |
| `text.toggleUnicode` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `text.toggleUnicode` (state: '00E9' typed a… · limit: command-reference.md: Refused … - Refused with a reason (23): `text.toggleUnicode` (sele… |
| `text.trademark` | V | reference/formatting-and-editing.md#Character effects, par…: …gistered`, `text.trademark`, `text.optional… |
| `text.typeCode` | V | reference/formatting-and-editing.md#Character effects, par…: …aragraph), `text.typeCode {"code":"0233"}` … |

## tools (11)

| id | status | note |
|---|---|---|
| `tools.attachTemplate` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …ate` after `tools.attachTemplate {"path"}` … · limit: formatting-and-editing.md: Not run … - Not run: `styles.manage/pane/apply`, `tools.attachTemplate… |
| `tools.autocorrect` | V | reference/document-formats.md#Screenplay format (verified …: …uilds with `tools.autocorrect {"enabled":fa… |
| `tools.customizeKeyboard` | V | reference/command-reference.md#Sweep of every remaining co…: …tionaries; `tools.customizeKeyboard {"comma… |
| `tools.customizeRibbon` | V | reference/command-reference.md#Verified in detail, WordCra…: `tools.customizeRibbon` (state: query the r… |
| `tools.detachTemplate` | V | reference/command-reference.md#Verified in detail, WordCra…: …s. (1): `tools.detachTemplate` after `to… |
| `tools.linkStyles` | V | reference/command-reference.md#Verified in detail, WordCra…: `tools.linkStyles` `{"value": true}` (state… |
| `tools.macros` | V | reference/command-reference.md#Commands (verified): - Macros: `tools.macros {"define":{"name":"Shout","s… |
| `tools.recordMacro` | V | reference/formatting-and-editing.md#Character effects, par…: …on label), `tools.recordMacro {"name":"M1"}… |
| `tools.search` | V | reference/formatting-and-editing.md#Character effects, par…: Tools: `tools.search {"query":"bold"}` → `{… |
| `tools.templates` | V | reference/command-reference.md#Verified in detail, WordCra…: `tools.templates` (state: no attached templ… |
| `tools.updateStyles` | V+ | reference/command-reference.md#Verified in detail, WordCra…: `tools.updateStyles` `{"path": "template.do… · limit: command-reference.md: Refused … `tools.updateStyles` (bad parameters: no template is attache… |

## view (41)

| id | status | note |
|---|---|---|
| `view.accessibilityPane` | V | reference/command-reference.md#Verified in detail, WordCra…: …. (32): `view.accessibilityPane` before:… |
| `view.altTextPane` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.altTextPane` before: altTextPane fals… |
| `view.commentsPane` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.commentsPane` before: commentsPane fa… |
| `view.darkMode` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.darkMode` before: darkMode false |
| `view.draft` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.draft` before: mode print |
| `view.fieldCodes` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.fieldCodes` `{"value": true}` before:… |
| `view.focus` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.focus` `{"value": true}` before: focu… |
| `view.formatShapePane` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.formatShapePane` before: formatShapeP… |
| `view.fullScreen` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.fullScreen` `{"value": true}` before:… |
| `view.fullScreenView` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.fullScreenView` `{"value": true}` bef… |
| `view.gridlines` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.gridlines` `{"value": true}` before: … |
| `view.hideWhiteSpace` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.hideWhiteSpace` `{"value": true}` bef… |
| `view.immersive` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.immersive` before: immersive false |
| `view.interfaceTheme` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …w. (1): `view.interfaceTheme` live: `{"v… · limit: command-reference.md: skipped on purpose (print, user font list, theme setting, ne… |
| `view.marks` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.marks` before: marks false |
| `view.multiplePages` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.multiplePages` before: fit pageWidth |
| `view.navigationPane` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.navigationPane` before: navPane false |
| `view.newWindow` | V+ | reference/command-reference.md#Verified in detail, WordCra…: …w. (1): `view.newWindow` live: opens a s… · limit: command-reference.md: skipped on purpose (print, user font list, theme setting, ne… |
| `view.numeral` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.numeral` `{"value": "context"}` befor… |
| `view.onePage` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.onePage` before: fit "", zoom 1.0 |
| `view.outline` | V | reference/command-reference.md#Verified in detail, WordCra…: … findings: `view.outline` first makes `outl… |
| `view.pageWidth` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.pageWidth` before: fit "", zoom 1.0 |
| `view.printLayout` | V | reference/sections-headers-tables.md#Tables in depth, outl…: … view ids: `view.printLayout\|webLayout\|draf… |
| `view.readColumnWidth` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.readColumnWidth` `{"value": "narrow"}… |
| `view.readLineSpacing` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.readLineSpacing` `{"value": 1.5}` bef… |
| `view.readMode` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.readMode` before: mode web, readMode … |
| `view.readPageColor` | d | reference/command-reference.md#Newer commands: …ue}`), and `view.readPageColor {"color":"none\|sepia\|inver… |
| `view.readTextSize` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.readTextSize` `{"value": 125}` before… |
| `view.ruler` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.ruler` `{"value": false}` before: rul… |
| `view.sideToSide` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.sideToSide` before: pageMovement vert… |
| `view.split` | V+ | reference/command-reference.md#Verified in detail, the las…: view.split and references.researcher checke… · limit: command-reference.md: …w. (1): `view.split` checked, does nothing in 0.15.0: it … |
| `view.state` | V | reference/command-reference.md#Verified in detail, the las…: `view.state` identical before and after, no… |
| `view.stylesPane` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.stylesPane` before: stylesPane false |
| `view.stylesPaneDock` | V | reference/command-reference.md#Newer commands: … active; `view.stylesPaneDock {"dock":"left\|right\|float… |
| `view.switchWindows` | V | reference/command-reference.md#Newer commands: - `view.switchWindows {"id"?}` lists the open documen… |
| `view.vertical` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.vertical` before: pageMovement sideTo… |
| `view.webLayout` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.webLayout` before: mode draft |
| `view.zoom` | V | reference/command-reference.md#Sweep of every remaining co…: …g mapping; `view.zoom {"value":150}` → `{fi… |
| `view.zoom100` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.zoom100` before: zoom 1.5 |
| `view.zoomIn` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.zoomIn` before: zoom 1.5 |
| `view.zoomOut` | V | reference/command-reference.md#Verified in detail, WordCra…: `view.zoomOut` before: zoom 1.6 |

## wordArt (4)

| id | status | note |
|---|---|---|
| `wordArt.style` | V | reference/command-reference.md#Verified in detail, WordCra…: …t. (4): `wordArt.style` `{"style": "outl… |
| `wordArt.textFill` | V | reference/command-reference.md#Verified in detail, WordCra…: `wordArt.textFill` `{"fill": "FF0000"}` (st… |
| `wordArt.textOutline` | V | reference/command-reference.md#Verified in detail, WordCra…: `wordArt.textOutline` `{"color": "00FF00", … |
| `wordArt.transform` | V | reference/command-reference.md#Verified in detail, WordCra…: `wordArt.transform` `{"preset": "textArchUp… |
