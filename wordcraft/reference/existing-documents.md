# WordCraft reference: existing documents

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Opening real résumés (.docx) in WordCraft: fidelity check (verified on copies, 2 designs)

> **Versions:** tested 2026-10-24 on 0.10.0 with two older résumé files (the figures below come from those). re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs on two current résumé files (one style-based, one table-based, copies in scratch): `info`, the open+save round trip, style/table/link/numbering/margin counts and the PDF word-sequence ratio came out **identical** on both versions. Not re-compared against ONLYOFFICE's renderer.

`wordcraft-cli info f.docx` → pages/paragraphs; `convert f.docx f.pdf`; `run --file f.docx --save out.docx` is the open+save round trip.
- A style-based résumé (custom styles, no tables, 2 hyperlinks) round-tripped IDENTICALLY: same style counts, 2 pages,
  998 words, links, margins, numbering, document title; text diff of the two PDFs 1.0000.
- A table-based résumé (9 layout tables, list bullets, direct formatting, 6 numbering definitions, 195 styles) kept all of
  it: tables, styles, margins, bullet definitions, 20 border blocks, 3 pages. Differences: text runs are merged (42 → 37 font
  runs, harmless), one line wrapped differently (ONLYOFFICE hyphenated "class-rooms", WordCraft kept "classrooms"), a
  bullet character extracted as `•` instead of `·`, and `docProps/custom.xml` (custom document properties) was dropped.
- Compare renderers by exporting both PDFs, then `pdftotext` word sequences with `difflib.SequenceMatcher` and a
  4-up page image (original-renderer vs WordCraft for each file). Verdict: WordCraft is safe for these résumés when saving
  to a NEW file; keep the original untouched.

## Document comparison (verified headless)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (word and character level on a one-line edit): identical changes. Not re-run: the two-résumé comparison, `showIn` variants, `review.combine`.

`review.compare {"path":ABS_revised.docx | "text":"revised text","level":"word|character","author":"Cmp","showIn":"original|revised|new"}`
→ `{"changes":N,"notHonoured":[]}` and the differences become tracked changes; read them with `review.changes` (kind
insert/delete/format, text). Word level on a one-line edit gave exactly `delete "jumps " / insert "leaps " / delete "16.5 " /
insert "18 "`; character level gave `jum→lea`, `6.5→8`. Two résumé versions with different layouts gave 48 change blocks (238
records incl. 52 `format` records): filter `kind` to `insert|delete` for the text story. CLI form:
`wordcraft-cli run --file old.docx --cmd 'review.compare={"path":"/abs/new.docx","level":"word","showIn":"new"}' --cmd 'review.changes={}' --save cmp.docx --print`
(commands are `id={json}`; there is no `--params` option). `review.combine` takes the same parameters.

## Templates (verified headless)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (all five built-in templates by pages/paragraphs/text; `file.saveTemplate` + `file.newFromTemplate` with a custom style, margins and header): identical. Not re-run: `tools.attachTemplate`.

- Built-ins: `wordcraft-cli run --template resume|letter|report|sample|blank --save x.docx` (resume: 1 page of fictional "Alex
  Rivera" text; letter; report; sample: a 2-page handbook).
- Make one: build styles, margins and a header, then `file.saveTemplate {"path":"x.dotx"}`; start from it with
  `file.newFromTemplate {"path":"x.dotx"}` (script without `"template"`): styles, header text and margins (64 pt) all
  carried over and `Heading 1`/custom `Callout` styles applied correctly.
- Refresh an old document's styles: `tools.attachTemplate {"path":"x.dotx","linkStyles":true,"update":true}` replaced ALL styles
  (reply lists `replaced:[Normal, Heading 1…]`), turning a stale custom style (green bold) into the template's (italic brown,
  indented). It changes styles only, not margins or headers.

## Reformatting a real document with review comments (verified on a real 3-page .docx, 0.11.0)

> **Versions:** 0.11.0 (2026-10-25). From rebuilding a friend's plain Word document as a styled, 4-page document and a second copy carrying review comments. Original left untouched; both outputs are new files.

- **Plan:** read the source with `wordcraft-cli text`, rebuild it from a script (`styles.create`/`modify`, content, tables, links), render to PDF and LOOK at every page, then build a second copy that adds comments. One builder with a `--comments` flag produced both from the same content.
- **Built-in style names already exist:** `styles.create {"name":"Caption"}` fails ("a style named `Caption` already exists"). Use `styles.modify` for built-ins (Normal, Heading 1-3, Caption, Header, Footer) and `styles.create` only for your own (Doc Title, Callout, Table Text…).
- **Callout paragraph** = a custom style with a left border and an indent: `styles.modify {"style":"Callout","chr":{"color":"1F3864"},"para":{"indentLeft":14,"borders":{"left":{"style":"single","width":3,"color":"2E75B6","space":8}}}}` (render: a blue bar beside navy text). Bold lead-ins ("The solution: …") are runs: `format.bold` → `text.insert` → `format.resetChar`.
- **Tables, three traps/recipes:**
  1. **`caret.up` moves by visual LINE, not by row.** Going "up N rows" from the last cell to shade the header row hit the wrong row whenever cells wrapped (the second row was shaded). Shade the header FIRST: right after `insert.table`, `table.selectRow` → `table.shading {"color"}` → `table.repeatHeader` → `select.collapse`, then fill the cells.
  2. **Column widths:** with the caret in row 0, `table.columnWidth {"width":pt}` sets that column; call it for each cell of row 0 as you type it (`caret.right` between). The render showed exactly those widths.
  3. **Header text colour:** `format.set {"props":{"bold":true,"color":"FFFFFF"}}` before typing a header cell, `format.resetChar` before every other cell; `table.borders {"color":"BFBFBF","width":0.5}` after the last cell, then `caret.docEnd` leaves the table. `table.repeatHeader` repeated the header on the next page (render).
- **Hyperlinks in table cells:** `select.text {"text":"Product page","occurrence":2}` then `insert.link {"url"}` worked inside cells (underlined link in the render). The same link text repeats, so link in document order with `occurrence` counted over the text as it stands (an already linked run still counts).
- **Page number "x of y":** `insert.pageNumber {"position":"bottom","align":"center","format":"x of y"}` → "Page 1 of 4" in the footer (styled with `styles.modify {"style":"Footer"}`).
- **Landscape appendix with a picture:** `layout.break {"kind":"nextPage"}` then `layout.orientation {"value":"landscape"}` turned only the new section (4th page landscape, header and footer carried on); `insert.picture {"path","width":640,"alt"}` in a centred keep-with-next paragraph, then a `Caption` paragraph (italic grey). A 2339×1654 px PNG at width 640 pt looked sharp.
- **Stray bullet before a section break:** `text.newParagraph` after a bullet list carries the list, so the page break left an EMPTY bullet at the end of the page. Set `para.set {"props":{"numbering":{"level":0,"num":0}}}` on that paragraph BEFORE `layout.break`.
- **Comments:** `file.setAuthor {"name":"Reviewer (Claude)"}` once, then for each note `select.text {"text":anchor,"occurrence":n}` + `review.newComment {"text"}`. 11 comments anchored on phrases inside paragraphs, a table cell and list items; `review.comments {}` listed all 11 with the author, `info` showed `comments:11`. **A failed `select.text` stops the whole script** ("`…` not found"): anchors must appear exactly that many times (a header text is not searchable; the same words in the title and a table are two occurrences). Anchor on a phrase that occurs once and use `occurrence:1`.
- **Faithful reformatting:** keep the author's wording in the clean copy, put judgement into the comment copy, restate (not reinterpret) facts in added summary tables, fix only mechanical things (restarted numbering, tracking parameters in links) and say so.
- Not run: tracked changes for suggested wording edits (comments only), `review.combine` against the friend's later version.

- **`para.bullets {"kind":"bullet"}` TOGGLES, and `text.newParagraph` keeps the list:** calling it on every item turned bullets OFF on every second item (render: alternate bullets and plain paragraphs). Call it on the first item only, then `para.bullets {"off":true}` after the last one. (0.11.0, 2026-10-26)
- **Editing a table cell by text in a reviewed document:** `edit.replaceAll` and `select.text` miss text that a comment anchor splits (replaced:0 / "not found"); delete by `select.range` on the cell paragraph path with offsets instead, and check the result with `inspect` (an offset was 3 characters short once). `table.deleteRow` with the caret in a cell (via `select.text` + `select.collapse`) works, but check the row did not hold the only mention of another part. (0.11.0, 2026-10-26)
