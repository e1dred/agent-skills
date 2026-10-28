# WordCraft reference: sections headers tables

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Headers and footers per section (verified headless; render checked per page)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (the two-section script above, per-page text): identical (page 1 'Head1 … Foot1', page 2 'Head2 … Foot2'). Not re-run: the third-section inheritance and the `inspect` ids.

```
text.insert "Section one." ; insert.header {"text":"Head1"} ; insert.closeHeader ; insert.footer {"text":"Foot1"} ; insert.closeHeader
caret.docEnd ; layout.break {"kind":"nextPage"} ; text.insert "Section two."          # caret is now IN section 2
layout.linkToPrevious {}            ; insert.createHeader {} ; text.insert "Head2" ; insert.closeHeader
layout.linkToPrevious {"footer":true} ; insert.createFooter {} ; text.insert "Foot2" ; insert.closeHeader
```
The same recipe as a script for `wordcraft-cli run --script hdr.json` (re-run 2026-10-27: page 1 "Head1 … Foot1", page 2 "Head2 … Foot2"; commands without parameters need no `params`):
```
{"template":"blank","commands":[
 {"command":"text.insert","params":{"text":"Section one."}},
 {"command":"insert.header","params":{"text":"Head1"}},{"command":"insert.closeHeader"},
 {"command":"insert.footer","params":{"text":"Foot1"}},{"command":"insert.closeHeader"},
 {"command":"caret.docEnd"},{"command":"layout.break","params":{"kind":"nextPage"}},
 {"command":"text.insert","params":{"text":"Section two."}},
 {"command":"layout.linkToPrevious","params":{}},{"command":"insert.createHeader","params":{}},
 {"command":"text.insert","params":{"text":"Head2"}},{"command":"insert.closeHeader"},
 {"command":"layout.linkToPrevious","params":{"footer":true}},{"command":"insert.createFooter","params":{}},
 {"command":"text.insert","params":{"text":"Foot2"}},{"command":"insert.closeHeader"}],
 "save":["hdr.pdf","hdr.docx"]}
```
Result: page 1 "Head1…Foot1", page 2 "Head2…Foot2", and a THIRD section added afterwards inherits section 2's header and footer
(`inspect` section props: `headers.default` / `footers.default` ids `[(1,2),(3,4),(3,4)]`). Rules learnt by failing first:
- Run `layout.linkToPrevious` (once; twice gave the same result, reply `{"linked":true}`) with the caret in the new section BEFORE
  `insert.createHeader`; without it the new section shares section 1's header and your text lands in it ("H1H2" on every page).
- Do NOT pass `"page"` to `insert.createHeader`/`createFooter`; the default is the caret's section.
- `insert.header {"text"}` alone in section 2 REPLACES the shared header for all sections (every page showed "H2").
- `insert.closeHeader` after each header/footer; verify with `pdftotext -f N -l N`.

## Tables in depth, outline view, building blocks, pictures and shapes (verified headless, 0.11.0; renders checked)

> **Versions:** 0.11.0 only (2026-10-25); not run on 0.10.0.

- **Table editing** (caret in a cell; each returns the new caret): `table.insertRowBelow|insertRowAbove|insertColumnRight|insertColumnLeft`, `table.deleteRow|deleteColumn|deleteTable`, `table.autofit {"mode":"contents|window|fixed"}`, `table.distributeColumns/distributeRows`, `table.split {"columns":2,"rows":1}`, `table.splitTable`, `table.selectColumn/selectTable`, `table.textDirection {"value":"horizontal|down|up"}`,
  `table.toText {"separator":"comma|tab|paragraph|other"}` (rows become "A1,B1,C1," paragraphs; empty cells leave bare commas), `table.look {"headerRow":true,"bandedRows":true}`. **Table styles:** `table.newStyle {"name":"Brand","basedOn":"Table Grid","headerRow":{"fill":"1F3864","bold":true,"color":"FFFFFF"},"wholeTable":{"borderColor":"1F3864"}}` → `{id}`, then `table.style {"style":"Brand"}`; also `table.modifyStyle`, `table.deleteStyle`.
  `table.quick {"kind":"calendar|tabular|matrix"}` inserts a ready table (the calendar is a Monday-first month grid with the weekend columns; the first row bold). **Nested tables work:** `insert.table` with the caret inside a cell → the new table's path is `[9,0,1,0]` (table block, row, cell, paragraph) and text typed in it has path `[9,0,1,0,0,0,0]`; the render showed the inner table inside the outer cell (the outer cell's text wraps narrowly).
- **Outline view:** `view.outline` → `{mode:"outline"}`; **`outline.showLevel`/`showAll` only work in outline view** ("only in Outline view" otherwise). `outline.state {}` → `{levels:[1,10,2,10,1,10],showLevel,shown:[…],collapsed:[…],firstLineOnly}` (level 10 = body text; `shown` lists visible blocks), `outline.showLevel {"level":1}` → `shown:[0,4]`, `outline.collapse/expand/toggle {"block"?}` (collapsed:[2] hid the subtree), `outline.selectSubtree {"block":0}` selects a heading with everything under it,
  `outline.promote/demote/level {"level":3|"body"}/demoteToBody/promoteToHeading1`, `outline.moveUp/moveDown` (moves the **whole selected subtree**: "One" with its body moved below "Three"), `outline.firstLineOnly {"value":true}`, `outline.close` → `{mode:"print"}`. **Trap:** `promote/demote/level` act on EVERY paragraph of the selection, so after `selectSubtree` all its paragraphs (body text included) became Heading 1: collapse the selection first (`caret.docStart`).
  `view.state {}` returns every view flag (panes, dark mode, draw pen settings…); other view ids: `view.printLayout|webLayout|draft|readMode|zoom {"value":percent|"pageWidth"}|ruler|navigationPane|fieldCodes {"value"}|focus|darkMode|interfaceTheme {"value":"light|dark|system"}` (live-window features, not rendered headless).
- **Building blocks:** `insert.quickParts {"save":"Boiler"}` (from the selection; global gallery) → `{parts:[…],document:[…]}`, `insert.autoText {"save":"Sig","in":"document","insert":"Sig","delete":name}` (`in:"document"` keeps it in the docx), `insert.docProperty {"name":"Title"}` puts a field with the `file.properties` title, `insert.horizontalLine`, `insert.textFromFile {"path":ABS}`, `insert.blankPage`, `insert.signatureLine {"signer","title"}`, `insert.icon {"query":"star"}` **lists** matching icons (`{icons:[{id,name,category,keywords}]}`; insert with `{"id":"star","color","size"}`).
- **Objects:** `insert.smartArt {"layout":"process|basicList|cycle|hierarchy|pyramid|radial|matrix|venn","items":["Plan",{"text":"x","level":1}]}` → `{smartArt:{layout,items,colors},width:432,height:252}`; `insert.wordArt {"text","transform":"textArchUp|textArchDown|textCircle…","style"}` → `{story:1}` and **the caret ends INSIDE the WordArt box** (leave with `caret.set {"pos":{"story":"body","path":[0],"off":0}}`; the box then floats and may overlap the next object);
  `insert.canvas {"width":200,"height":80,"fill":"FFF2CC","outline":"7F3F00"}` ("a drawing canvas can't go inside a text box": get out of the WordArt first).
- **Pictures** (right after `insert.picture`, the picture is the selected object; each call returns `{object:{alt,crop,float,…}}`): `picture.size {"scale":80}|{"width","height","lockAspect"}`, `picture.crop {"left":0.1,"right":0.1}` (fractions), `picture.color {"mode":"sepia|grayscale|washout|blackAndWhite|saturation|tint"}`, `picture.effects {"effect":"blur|sharpen|invert|posterize|pixelate|none"}`, `picture.transparency {"percent"}`, `picture.corrections {"brightness","contrast","sharpen"}`,
  `picture.style {"style":"simpleFrame|thickFrame|rounded|softEdge|shadow"}`, `picture.border {"color","width"}`, `picture.altText {"text","title","decorative"}`, `picture.reset` (clears crop/effects but KEEPS the alt text), `picture.compress`, `picture.change {"path"}`, `picture.removeBackground {"tolerance"}`. Render: sepia + crop + rounded frame + border looked right.
- **Shapes:** `insert.shape {"kind":"star","width":60,"height":60}` then `shape.fill {"color":"FFC000","transparency"}` (or `{"gradient":{"stops":[…],"type"}}`), `shape.outline {"color","width"}`, `shape.change {"kind":"heart"}` (render: a gold heart with outline and shadow), `shape.effects {"shadow":{"color":"000000","transparency":50,"blur":6,"distance":4,"angle":45},"glow":…}` (a preset name such as `outerBottomRight` is rejected: "unknown shadow preset"; use the object form),
  `shape.textDirection {"dir":"horz|vert|vert270"}`, `shape.alignText {"anchor":"t|ctr|b"}`, `shape.link {"target"}` / `shape.breakLink` (flow text between text boxes), `shape.connect`.
- Not run: ink (`draw.*`: `draw.stroke {"page","points","tool","color","width"}`, `draw.lasso`, `draw.inkToShape`, `draw.replay`), `insert.object/spreadsheet`, `edit.pasteMerge`/clipboard pane, `edit.advancedFind/findReplace`, `file.*` extras, `picture.removeBackground`, `shape.fill` gradients.

## Sections: `layout.section`, section breaks and per-section orientation (verified headless, 0.11.0, 2026-10-26)
> **Versions:** 0.11.0. Built with `wordcraft-cli run --template blank --cmd … --save sec.docx`; read back from `word/document.xml`.
- **`layout.break {"kind":"nextPage"|"continuous"|"evenPage"|"oddPage"|"page"|"column"|"textWrapping"}`** starts a new section for the section kinds (3 `w:sectPr` after a next-page and a continuous break); `info` reported 2 pages. `insert.pageBreak {}` is the plain page break.
- **`layout.section {}` is a READ**: it returns the current section's properties (columns, header and footer distances, header/footer slots, gutter, margins, page size), not a break. Use it to check a section before changing it.
- **`layout.orientation {"orientation":"landscape"}` applies to the CURRENT section only:** the first section stayed `12240×15840` portrait, the second became `15840×12240 orient="landscape"`, and a following continuous section kept landscape. Insert the break first, then change the orientation.

## Table layouts for designed pages: banners, sidebars, colour blocks (verified headless, 0.11.0, 2026-10-26; rendered and compared with ONLYOFFICE)
> **Versions:** 0.11.0 only. Built by `styles/resume_designs.py` (18 résumé layouts); every page rendered with `wordcraft-cli render` and with ONLYOFFICE's preview: the same on both.
- **Full-bleed page:** `layout.margins {"top":0,"bottom":0,"left":0,"right":0}`, one `insert.table {"rows","cols","style":"Normal Table"}`, a shaded cell (`table.selectCell` → `table.shading {"color"}` → `select.collapse`), `table.rowHeight {"height":778,"rule":"atLeast"}` made a dark sidebar that runs to the page edges. **The rule value is `"exact"` (not "exactly") for rowHeight**; the table plus the empty paragraph after it must fit: a 788 pt row spilled to page 2, 778 fit (set the empty paragraph tiny: `styles.modify {"style":"Normal","chr":{"size":1},"para":{"lineSpacing":{"rule":"exactly","value":1}}}`, then give picture paragraphs their own style, or the picture is clipped to 1 pt).
- **`table.autofit {"mode":"fixed"}` right after `insert.table`** or narrow columns are widened and squeeze their neighbours. **A column is never narrower than 6 pt (120 twips)**, so a 1–2 pt divider column is impossible: draw hairlines as a paragraph LEFT BORDER on every paragraph of one column (`styles.modify … para {"borders":{"left":{"style":"single","width":0.75,"color":"BFBFBF","space":14}}}` plus `indentLeft`); consecutive bordered paragraphs form one continuous line, dots go in as a "●" run.
- **`table.cellMargins` is ROW-WIDE** (the last call wins for every cell of the row; per-cell margins are not possible): call it once per row and inset columns with paragraph indents instead (`para.set {"props":{"indentLeft","indentRight","spaceBefore"}}` per paragraph; a nested table takes `table.properties {"indent":pt}`).
- **`table.borders {"kind":"right"|"bottom"…}` always lands on the TABLE edge, never on the selected cell or column.** Per-cell borders are not available; use shaded cells or paragraph borders.
- **Merged banner:** after `insert.table` set `table.columnWidth` for each column (caret.right between), return with `caret.docStart` (+ one `caret.paraDown` per paragraph before the table), then `table.selectCell` + `caret.right {"extend":true}` per extra cell + `table.merge` + `select.collapse`; format and fill afterwards. Without merges, set the widths while filling row 0 (works anywhere in the flow, no homing).
- **A continuous vertical line between columns/rows: use a table STYLE with only the inside-vertical border.** `table.newStyle {"name":"Timeline","basedOn":"Normal Table","wholeTable":{"borders":{"edges":"insideV","style":"single","width":0.75,"color":"A9A9A9"}}}` then `insert.table {…,"style":"Timeline"}` (2 columns: dates | details): one hairline through every row, no horizontal lines, identical in ONLYOFFICE. Part edges can be `insideV|insideH|top|bottom|left|right|outside|inside|all`. This replaces paragraph left borders for timelines (a paragraph border is broken at every row and shifts by a hanging indent: bullets with `left=26, first=-10` drew their line 2 pt right of the title's).
- **A paragraph left border is drawn across `spaceAfter` but NOT across `spaceBefore`:** heading-style paragraphs with `spaceBefore` left a gap in the line at every section. Move the heading's space-before onto the previous paragraph's `spaceAfter` (`para.set {"props":{"spaceAfter":…}}` on the previous paragraph, `spaceBefore:0` on the next) and the line bridges. Bordered paragraphs must also share the same effective left edge (`indentLeft + indentFirst`).
- **Vertical centring:** `table.cellAlign {"value":"center"}` (also topLeft/topCenter/…/bottomRight; `middleCenter` and `centerCenter` are rejected).
- **Skill bar = nested table** inside a cell: `text.newParagraph` → `insert.table {"rows":1,"cols":2}` → `table.rowHeight {"height":4,"rule":"exact"}` → shade each cell (`table.selectCell`, `table.shading`, `select.collapse`) → `table.columnWidth` for the filled and the empty part (min 6 pt each) → `caret.right` after the second cell leaves the nested table in a fresh paragraph. Render: a gold bar over a grey track.
- **After a table the caret sits in an empty paragraph with the previous paragraph's style** (a heading's border and spacing came with it): reuse it for the next text (do not add `text.newParagraph`), and at the end of the document `para.reset` + `para.style Normal`.
- **A new paragraph inherits direct paragraph AND character formatting** (a centred picture paragraph centred the next paragraphs; a bold run bolded the next paragraph): start each paragraph with `para.reset`, `para.style`, `format.resetChar`.
- Paragraph shading for a highlighted heading bar: `para.shading {"color":"DCE6F2"}` after `para.style`; with left/right indents it makes a highlight bar behind a centred name.
- Avatar/photo: `insert.picture {"path","width":118,"alt"}` in a centred paragraph; a generated PNG circle (PIL) worked. Fonts: Century Gothic, Georgia, Calibri, Corbel, Times New Roman, Arial are installed and portable; Poppins and Montserrat exist locally only.
