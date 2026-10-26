---
name: wordcraft
description: Verified working knowledge for driving the WordCraft word processor (storytold/wordcraft) from an AI agent — live editing through its control server / MCP bridge, headless builds with wordcraft-cli, exact command parameter formats, formatting recipes and known traps. Load before any WordCraft task, and add what you learn at the end of it.
---

# WordCraft

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, tested on **WordCraft 0.10.0; the style, review and next-tier sections on 0.11.0** (Linux AppImage). If `wordcraft-cli --version`
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

## Live mode, verified (WordCraft 0.10.0, app started with `--control 47822`, blank document open)

> **Versions:** tested 2026-10-24 on the app 0.10.0. Re-run 2026-10-25 on the app 0.11.0 (blank unsaved document, port 47826): `execute para.style`, `type_text` (real paragraphs), `select_text` + bold/italic, `get_text`, `render_page`, `inspect_document` and `ui_inspect.dirty` all behaved as described. Not re-run: `screenshot`, `batch`, `key`, `click`, `new_document`, `save_document`.

- Connect: `WORDCRAFT_PORT=47822 IMGDIR=DIR python3 -I tools/wcmcp.py '[["tool",{args}],…]'` (the helper now SAVES image
  results such as `screenshot` and `render_page` to `IMGDIR/img_N.png`; before, they were dropped as `<image>`).
  If `ui_inspect` shows `"title":"Document1"` and `"dirty":false` the user's blank document is attached.
- MCP tools (exact args): `execute {command,params}`, `batch {commands,keepGoing}`, `type_text {text,paragraphs}`,
  `select_text {text,occurrence (1-based)}`, `get_text`, `inspect_document`, `render_page {page,scale}` (the engine's
  page, 612×792 at scale 1), `screenshot` (the whole app window, ~2500 px: downscale with PIL before viewing),
  `new_document {template: blank|sample|letter|resume|report}` (built-in templates, untested), `save_document {path}`,
  `key {key,cmd,shift,alt}`, `click {x,y,count}`, `ui_inspect` (HUGE output: window state; filter it in Python for
  `title`/`dirty`), `list_commands`.
- Worked live: `para.style` Heading 1 → `type_text` → `text.newParagraph` → `type_text {"paragraphs":true}` with `\n`
  (makes real paragraphs there, unlike `text.insert`) → `select_text` + `format.bold` / `format.italic`. The user sees
  each step; the title bar shows "Edited" and `ui_inspect.dirty` turns `true`.
- **Trap: a failed `select_text` ("`italic` not found") leaves the PREVIOUS selection, and the next `format.*` hits it.**
  I asked for occurrence 2 of a word that occurs once and italicised the previous word. Check each result for
  `ERROR`, use `occurrence` correctly, and undo with `execute edit.undo`.
- A floating mini formatting toolbar appears over the text whenever something is selected, so screenshots can hide the
  paragraph being edited: `execute select.collapse` (or a `render_page` image) gives a clean look.
- `file.saveACopy` does NOT exist (`unknown command`). To keep the user's document unbound from a path, export instead:
  `execute file.exportPdf {"path":ABS}` (written, text extracted correctly). `file.save`/`file.saveAs`/`save_document`
  would bind the open document to that file and clear the Edited state: only do that when the user asks.
- Leave the user's document as found: it stays dirty with my test text; tell them to close it without saving.

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

## Mail merge (verified headless with `wordcraft-cli run --script`; letters)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (3-record CSV, one record filtered out, `start`, `recipients`, `filterRecipients`, `insertField`, `checkErrors`, `finish`): identical results and merged text. Not re-run: `addressBlock`/`greetingLine`, `rules`, envelopes/labels, `.xlsx` recipients.

```
mailings.start {"kind":"letters"}                       # also emails|envelopes|labels|directory
mailings.recipients {"csv":"Name,Company\nAda,Acme\n…"}   # or {"path":"/abs/people.csv"} (.csv/.tsv/.xlsx/.ods…) → {"fields":[…],"records":N}
mailings.filterRecipients {"rules":[{"field":"Status","op":"equal","value":"send"}]}   # → {"of":4,"records":3}
text.insert {"text":"Dear "}, mailings.insertField {"field":"Name"}, …      # the template text, with fields
mailings.addressBlock {} / mailings.greetingLine {}     # built from STANDARD column names: First Name, Last Name,
                                                        # Address Line 1, City, State, Postal Code → "Ada Example / 1 Main St /
                                                        # Boston, MA 02101" and "Dear Ada Example,"
mailings.rules {"rule":"IF","field":"Role","value":"","then":"…","else":"…"}   # also SKIPIF|NEXTIF|NEXT|MERGEREC
mailings.checkErrors {} → {"ok":true,"records":3,"unknownFields":[]}
mailings.finish {"path":"/abs/merged.docx","from":1,"to":2}   # one page per record; from/to merges a range
```
- The filter is applied before the merge: 4 records with one `Status=skip` gave 3 letters on 3 pages.
- An empty field simply leaves a gap ("the  position"): use an `IF` rule or filter blanks out (`op:"notBlank"`).
- **`then`/`else` text in `IF` is literal**: `else:"the Role you posted"` printed the word "Role", not the field's value, so
  you cannot embed a field inside a rule's text; put the field next to the rule instead.
- `\n` inside `text.insert` is a soft line break, so each merged letter was ONE paragraph with line breaks
  (`info` said 3 paragraphs for 3 letters); use `text.newParagraph` between paragraphs if separate paragraphs matter.
- Only letters were merged; envelopes (`mailings.envelopes`) and labels (`mailings.labels {"product":"letter-3x10",
  "fromRecipients":true}`) exist but were not run. Live mode with the app open was not tried for mailings.

## Citations, bibliography, cross-references (verified headless)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (a Book and a three-author JournalArticle in APA, IEEE and MLA, the bibliography, and the `insert.crossReference` list and heading text): identical. Not re-run: the other citation styles, `references.sources`, cross-references to bookmarks, figures, tables, equations or pages.

```
references.citationStyle {"style":"APA"}     # also IEEE, MLA, Chicago, Harvard (Anglia), ISO 690, Turabian, GOST…
references.citation {"source":{"tag":"Smith2020","type":"Book","author":"Smith, John","title":"…","year":"2020",
                     "publisher":"…","city":"…"},"pages":"12"}      # inserts "(Smith, 2020, p. 12)"; later: {"tag":"Smith2020","pages":"50"}
references.bibliography {"title":"References"}   # insert after text.newParagraph; same style as the citations
```
- **`author` is ONE string, not a list or object** (a list/map is rejected with "invalid type: sequence, expected a string").
  Several authors: `"Lee, Mina; Park, Joon; Kim, Ana"` (semicolon between "Last, First" names) → APA gives
  "(Lee & Park, 2022)" / "(Lee et al., 2022)" and "Lee, M., Park, J., & Kim, A. (2022)." `"Mina Lee and Joon Park"` parsed
  wrongly ("Park, M. L. a. J."). **Unknown source keys are silently ignored**: `authors` (plural) produced "(Title, 2020)" and
  a reference with no author. Always read the bibliography output.
- Types verified: `Book`, `JournalArticle` (`journal`, `volume`, `issue`, `pages`). Same text in IEEE: "[1]", "[2]" and a numbered
  list; MLA: "(Coaching Teachers 12)". `references.sources {"add"|"remove"|"import"}` lists/manages sources (untested).
- Cross-references: `insert.crossReference {}` lists targets (`["Methods","Results"]`); `{"to":"heading","target":"Methods",
  "show":"text"}` → "Methods"; `"show":"page"` → "1" (also bookmark, figure, table, equation, `label:<Name>`).

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

## Headers and footers per section (verified headless; render checked per page)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (the two-section script above, per-page text): identical (page 1 'Head1 … Foot1', page 2 'Head2 … Foot2'). Not re-run: the third-section inheritance and the `inspect` ids.

```
text.insert "Section one." ; insert.header {"text":"Head1"} ; insert.closeHeader ; insert.footer {"text":"Foot1"} ; insert.closeHeader
caret.docEnd ; layout.break {"kind":"nextPage"} ; text.insert "Section two."          # caret is now IN section 2
layout.linkToPrevious {}            ; insert.createHeader {} ; text.insert "Head2" ; insert.closeHeader
layout.linkToPrevious {"footer":true} ; insert.createFooter {} ; text.insert "Foot2" ; insert.closeHeader
```
Result: page 1 "Head1…Foot1", page 2 "Head2…Foot2", and a THIRD section added afterwards inherits section 2's header and footer
(`inspect` section props: `headers.default` / `footers.default` ids `[(1,2),(3,4),(3,4)]`). Rules learnt by failing first:
- Run `layout.linkToPrevious` (once; twice gave the same result, reply `{"linked":true}`) with the caret in the new section BEFORE
  `insert.createHeader`; without it the new section shares section 1's header and your text lands in it ("H1H2" on every page).
- Do NOT pass `"page"` to `insert.createHeader`/`createFooter`; the default is the caret's section.
- `insert.header {"text"}` alone in section 2 REPLACES the shared header for all sections (every page showed "H2").
- `insert.closeHeader` after each header/footer; verify with `pdftotext -f N -l N`.

## Accessibility checker (verified headless)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs (picture, table and 'click here' link, no title): identical issue lists. Not re-run: the full fix recipe down to `ok:true`, and the tagged-PDF check.

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

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs: `para.align/indents/spacing/lineSpacing/tabs`, `para.numbering` (numbered, lowerRoman), `para.bullets` and `edit.paste {html}` gave identical text and properties. Not re-run: the pagination keeps, multilevel lists, `setNumberingValue`, `para.sort`, copy/paste format, `edit.undoTo`, `edit.goto`, the spike.

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

## Choosing live vs headless

- **Live** (user watches): bridge MCP / `tools/wcmcp.py`. Check `ui_inspect` first: `title`, `dirty`.
  Never replace or close a document with unsaved changes (`file.close` without `force` refuses; keep it that way).
- **Headless** (build, then show): `wordcraft-cli run --script s.json` → `render` pages → look → fix.
  Safer for big rebuilds; open the result for the user afterwards (launch the app with the file).
- Editing a file that is open in a window: edit the file on disk, then tell the user to close the window
  WITHOUT saving and reopen — saving from the old window would overwrite the change.

## CLI essentials (verified)

> **Versions:** tested 2026-10-24 on 0.10.0. re-run 2026-10-25 on both the 0.10.0 and 0.11.0 CLIs: `run --save`, `info`, `text`, `render`, `convert … .md` identical. Not re-run: `batch` and the other converters (the style work converted to PDF on 0.11.0).

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

## Document styles (traditional, elegant, clean, professional, academic, modern, stylish, creative; document, résumé, CV, APA/MLA paper)

> **Versions:** built and rendered on 0.11.0 (2026-10-25) only.

`../styles/` holds the specs (`styles.json`), a font resolver (installed fonts first, Office-portable by default) and a neutral build plan (`plan.py`);
`python3 -I styles/build_wordcraft.py STYLE doc|resume|cv|paper /abs/out.docx [--paper=a4] [--page-numbers=…] [--columns=2] [--photo=…]
[--layout=functional|combined] [--format=apa|mla] [--overwrite] > job.json` then `wordcraft-cli run --script job.json`. See `../styles/README.md` for the table, gallery,
ATS notes and options. Verified: every style in 3 kinds plus the feature samples, rendered with `wordcraft-cli convert x.docx x.pdf`. Facts that mattered:
- **`para.set {"props":{"numbering":{"level":0,"num":0}}}` also wipes the style's indents** (first-line and hanging indents vanished on every paragraph). Only set numbering on bullet paragraphs and on the first paragraph after a list.
- **A new paragraph inherits the previous paragraph's DIRECT properties** (a one-off `spaceBefore` 96 leaked onto every later paragraph). Set `spaceBefore`/`pageBreakBefore` explicitly on each paragraph.
- Page break before a paragraph: `para.set {"props":{"pageBreakBefore":true}}`. `insert.pageBreak` stays inside the same paragraph, so the next heading text lands in it.
- Header with text plus page number: `insert.header {"text":"Morgan "}` → `caret.end` → `insert.pageField` → `para.set {"props":{"align":"right"}}` → `insert.closeHeader` (without `caret.end` the number comes first). Page number only: `insert.pageNumber {"position":"top","align":"right"}` or `"bottom"`. Style them with `styles.modify {"style":"Header"|"Footer",…}`.
- Two columns after the title: `text.newParagraph` → `layout.columns {"count":2,"space":24,"separator":true,"apply":"forward"}`; the rest of the document continues in columns.
- Tables: `insert.table {"rows","cols","style":"Table Grid"}`, per cell `para.style` + `text.insert` + `caret.right`; then `caret.up` to the header row, `table.selectRow`, `table.shading {"color"}`, `format.set {"props":{"bold":true,"color"}}`, `table.repeatHeader`, `table.borders {"color","width":0.5}`.
  `table.borders` applies to the **whole table** and ignores `preset`/`style:none` (unknown parameter names are silently ignored); a borderless start is table style `"Normal Table"`. Then `caret.docEnd` leaves the table.
- Photo: `insert.picture {"path","width":85,"alt"}` in its own paragraph above the name.
- Merged cells: fill every cell (skip text in the cells to be merged), `caret.up` to the row, `table.selectRow`, `table.merge` (→ `gridSpan`), then `table.selectRow` AGAIN before `table.shading`/`format.set` (the merge drops the selection).
- Footnote after a phrase: `select.text {"text":"seed log."}` → `caret.right` → `references.footnote {"text":…}`; do all footnotes LAST (the caret stays inside the footnote).
- Right-to-left: `para.set {"props":{"bidi":true,"align":"left"}}` — in a bidi paragraph "left" is the START edge, so it renders on the right of the page ("right" renders left). Set the font with `format.set {"props":{"font":"Arial","fontCs":"Arial"}}`; for CJK add `"fontEa":"Noto Sans CJK JP"`. Reset the next paragraph with `bidi:false` and `format.resetChar`.
- Figure: `insert.picture {"path","width":300,"alt":"…"}` in a `Doc Figure` paragraph, then `text.newParagraph` and the caption paragraph; the alt text lands as `descr` on the drawing.
- `wordcraft-cli commands` lists ids only (no parameter docs, no `describe`): learn parameters from this file or by trial, and remember unknown parameter names are silently ignored.

## Next-tier workflows (verified headless, 0.11.0)

> **Versions:** 0.11.0 only (2026-10-25); not run on 0.10.0.

**Seeing results:** `wordcraft-cli run --file F.docx --cmd id={json} --print` (or a `--script`) prints every command's result (the older notes only showed "wrote …"). `--author NAME` names who the tracked changes and comments are by (default "WordCraft User").
- **Tracked changes**: `review.trackChanges {"on":true}`, then ordinary edits (`select.text {"text":"quick brown"}` + `text.insert` → one insertion + one deletion; `text.delete`) become `<w:ins>`/`<w:del>`.
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

## Styles management, index and TOC, equations, tracked changes in depth (verified headless, 0.11.0; equation render checked)

> **Versions:** 0.11.0 only (2026-10-25); not run on 0.10.0. `wordcraft-cli commands --json` DOES give each command's parameter signature (the older note that only ids exist is about the plain listing): use it before guessing.

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

## Manuscript format for publishers (verified headless, 0.11.0; both apps render the same pages)

> **Versions:** 0.11.0 (2026-10-25). Built by `styles/build_wordcraft.py x manuscript …`, checked with `styles/manuscript_check.py`; see `styles/README.md` for the options.

- **Header that skips page 1:** create the header text in the default slot first (`insert.header {"text":"Tilby / TITLE / "}` → `caret.end` → `insert.pageField` → `para.set {"props":{"align":"right"}}` → `insert.closeHeader`), THEN `layout.differentFirstPage`. Page 1 then shows nothing and pages 2+ show "Tilby / TITLE / 2" (render and `pdftotext` checked). The opposite order puts the text into the first-page slot only (see the per-section header notes).
- **"Space before" is ignored at the top of a page** in WordCraft's layout, even with `pageBreakBefore`: a chapter heading with `spaceBefore:144` after a page break printed at the very top. Use six empty double-spaced paragraphs (a style with no indent) to drop a third of the page, or put the spacing before a paragraph that is not first on the page (the title block's `spaceBefore` worked on page 1).
- **Italic leaks into the next paragraph:** a paragraph ending in an italic run (`format.italic` → text → `format.resetChar`) still made every following paragraph italic, including a chapter heading. Call `format.resetChar` right after `para.set` at the start of each new paragraph.
- A right tab inside a one-line style (`tabs: [{pos:468, align:right}]`) puts "about 350 words" at the right margin on the same line as the author's name; `text.insert` with `\t` is a real tab.
- Real `Heading 1` for chapters (restyled: 12 pt, bold, centred, black, double-spaced), `Normal` body with `indentFirst:36`, `lineSpacing multiple 2.0`, `spaceAfter:0`; the checker reads these back from `styles.xml`.

## Screenplay format (verified headless, 0.11.0; both apps give the same pages)

> **Versions:** 0.11.0 (2026-10-25). Built by `styles/build_wordcraft.py x screenplay …`, checked with `styles/screenplay_check.py`.

- **Fixed line pitch:** `lineSpacing {"rule":"exactly","value":12}` on every element (`para.lineSpacing {"exactly":12}`); with Courier 12 this gives 6 lines per inch. Right indents are a paragraph property too: `indentRight` (pt), next to `indentLeft`.
- **Title page not counted, script numbered from 1, page 1 without a number:** type the title page, `layout.break {"kind":"nextPage"}`, then in the NEW section `layout.pageNumberFormat {"format":"decimal","start":1}` → `layout.linkToPrevious` → `insert.createHeader` → `insert.pageField` → `text.insert "."` → `para.set {"props":{"align":"right"}}` → `insert.closeHeader` → `caret.docEnd` → **`layout.differentFirstPage` last**. Result per page (`pdftotext`): title page no header, script page 1 no number, then "2." "3.". Doing `differentFirstPage` BEFORE `createHeader` put the number on script page 1 only (the header went into the first-page slot).
- **Autocorrect rewrites typed text:** `...` became `…` and some lines were capitalised; start screenplay and manuscript builds with `tools.autocorrect {"enabled":false}`.
- Keep-with-next on scene headings, cues and parentheticals stops a cue from being stranded at the bottom of a page; a transition can still start a page.
- `pdftotext -layout` drops some blank lines between elements even when the page has them: judge spacing on a render, not on the text dump.
- **Underline is a style name, not a boolean:** `styles.modify … chr {"underline":true}` fails ("expected string or map"); use `"single"`. `format.underline {"value":true}` works for typed runs.
- **Dual dialogue** = `insert.table {"rows":1,"cols":2,"style":"Normal Table"}` (borderless), type a cue and its speech in the first cell (`para.style` + `para.set {"props":{"spaceBefore":12}}` on its first paragraph, `text.newParagraph` between paragraphs), `caret.right` to the second cell, then `caret.docEnd` leaves the table. Render checked: two columns side by side.
- **Scene numbers** in the margin: a hanging first-line indent (`indentFirst:-54`) plus a right tab at the text width, text `N<tab>INT. …<tab>N`.
- **(MORE)/(CONT'D)** cannot be set in advance (page breaks depend on the layout): the repo's `screenplay_paginate.py` builds, reads the per-page words from the PDF, splits the speech at the break (one line earlier, because the `(MORE)` line needs room) and rebuilds until stable. Identical repeated speeches fool its word matching: test with varied text.

## Character effects, paragraph helpers, find, content controls, files and labels (verified headless, 0.11.0; props read back with `inspect`)

> **Versions:** 0.11.0 (2026-10-25); not run on 0.10.0.

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

## Ink (verified headless and on the live window, 0.11.0; render checked)

> **Versions:** 0.11.0 (2026-10-25). **This corrects an earlier note that ink needs the live app: the `page` parameter is 0-BASED** (`"page":1` means the second page and failed with "no page 1" on a one-page document; `"page":0` works headless).

- `draw.stroke {"page":0,"points":[[x,y],…],"tool":"pen|pencil|highlighter","color":"C00000","width":2}` → `{page,pos,rect:[x,y,w,h],shape:null}` (page points, at most 5000; the stroke is anchored to the paragraph at `pos`). Render: a red polyline, a wide translucent yellow highlighter bar, a thin grey pencil line (points are joined by straight segments, no smoothing).
- **Select, edit, delete:** `draw.lasso {"page":0,"points":[loop]}` → `{count:1,selected:[pos]}` (every stroke inside the loop), `draw.lasso {"page":0,"clear":true}` → `{count:0}`; then `draw.lassoColor {"color":"0000FF"}` → `{recolored:1}`, `draw.lassoMove {"dx":150,"dy":10}` → `{moved:1}`, `draw.lassoDelete` → `{deleted:1}`. Without a lasso selection they answer "nothing is selected with the lasso".
  `draw.erase {"page":0,"x":150,"y":380}` → `{erased:pos}` removes the stroke under that point.
- **Ink to shape:** `draw.convertInk {}` converts the lasso-selected strokes that look like a shape (`{converted:[{shape:"rectangle"}]}`; a zig-zag line answers "none of the selected strokes looks like a shape"); `draw.inkToShape {"value":true}` turns recognition on so the NEXT stroke becomes a shape as it is drawn (a boxed pen stroke came back with `shape:"rectangle"`), `{"value":false}` turns it off.
- **Pens:** `draw.pen|pencil|highlighter {"color","width"}` set the tool and its look (each returns the whole draw state: `mode`, `pen`, `pencil`, `highlighter`, `inkToShape`), `draw.addPen {"kind","color","width"}` → `{index,pens}`, `draw.removePen {"index"}`, `draw.eraser`, `draw.select`, `draw.replay {"value":true}` → the strokes in drawing order `[{order,page,points,tool}]` (`false` ends it), `review.hideInk {"value":true}` hides ink on screen.
- **In the file:** each stroke is saved as a floating `wp:anchor` + `wps:wsp` freeform shape in `word/document.xml` (4 shapes for 4 strokes), so Word and ONLYOFFICE show ink as ordinary shapes; the document keeps no separate ink part.

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

## Traps (each one cost time)

> **Versions:** found on 0.10.0 unless the item says otherwise; the three traps from the style builders (numbering `num 0` wiping indents, inherited direct properties, `insert.pageBreak`) were found on 0.11.0.

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
- Different headers per section: SOLVED, see "Headers and footers per section" below. The earlier failures came from passing `page` to `insert.createHeader` and from the call order.
- **A new paragraph inherits the previous paragraph's formatting** (indents, spacing, alignment, line spacing came along: a
  "Spaced" paragraph typed after a hanging-indent one still had the hanging indent). Set every property you care about on each
  paragraph, or call `para.reset` first.
- **AutoCorrect capitalises a one-word paragraph when you press `text.newParagraph`** ("pear" → "Pear"; list items too), while
  multi-word lines were left alone. `tools.autocorrect {"enabled":false}` as the first command keeps your text as typed.
- **`\n` in `text.insert` does not start a paragraph** — "Line A\nLine B" stays one paragraph with a line break.
- `--print` output from `run` shows each command's result; without it failures are easy to miss.
- Right tab must sit at the text width: page width − left − right margin (612 − 2×43.2 = 525.6 → use 525).

## Verify before reporting

- `info` for page count; `render` each page and look at it (`--scale 1.3`; crop to zoom).
- `pdftotext -layout` on the PDF to check ATS reading order; `pdffonts` for embedded fonts.
- Links: unzip the .docx and check `word/_rels/document.xml.rels` for the targets.

## Recipes

- `recipes/resume_ats.py` — ATS-friendly résumé: Calibri 10.5, 0.6"/0.5" margins, navy Heading 1 with bottom
  rule, job title with right-tab dates, italic employer line, navy bullets, linked email/profile; the invented sample fits 1 page (about 2 with a real career).
  Sample content is fictional; replace the `RESUME` data at the top.
  Usage: `python3 -I recipes/resume_ats.py /abs/out.docx /abs/out.pdf > s.json && wordcraft-cli run --script s.json`.

## Log

- 2026-10-24: Paragraph formatting, lists, tabs, sort, clipboard/paste, format painter, undoTo, goto, spike; two traps.
- 2026-10-24: Per-section headers/footers SOLVED; accessibility checker and tagged PDF export.
- 2026-10-24: Citations/bibliography (author string format), cross-references, document compare, templates.
- 2026-10-24: Mail merge (recipients, filter, fields, address block, IF rule, partial finish).
- 2026-10-24: Résumé round-trip fidelity check on two designs (faithful; only custom doc properties lost).
- 2026-10-24: Live mode on a blank document: typing, formatting, screenshot/render, export, failed-select trap.
- 2026-10-24: Initial notes from building and linking an ATS résumé (WordCraft 0.10.0).
- 2026-10-24: Linked the official docs (docs/mcp.md, docs/control-protocol.md); corrected path resolution.
- 2026-10-24: Generalized for sharing; résumé recipe made data-driven with fictional sample content.
- 2026-10-24: Numbered lists; confirmed that new paragraphs inherit list numbering.
- 2026-10-24: Tables (fill, header row shading/repeat, from text), headers/footers, x-of-y page numbers,
  page breaks, columns, links, TOC, footnotes, pictures, find/replace, comments, tracked changes.
- 2026-10-24: Header tab zones, page setup, regex/wildcard find, macros, proofing.
- 2026-10-24: Inline formatting, custom styles, captions, drop cap, shapes/text boxes, cover page, multilevel lists,
  roman page numbers, first-page-different footers, charts, equations, table merge, convert formats.
- 2026-10-25 (4): tracked changes, comments, compare, content controls, watermark, restrict/encrypt with password options, spelling/grammar, table of figures, table formula/sort, convert formats verified headless.
- 2026-10-25 (5): nine headless sections re-run on 0.10.0 and 0.11.0 (identical) and the live-mode steps on the 0.11.0 app; version labels added per section.
- 2026-10-25 (6): styles management, Design tab, index (mark/insert/update), TOC caret behaviour, equation editing (structures, convert, number), tracked changes by author/one at a time/options/combine verified headless on 0.11.0.
- 2026-10-25 (7): table editing/styles/nested tables, outline view, quick parts/autotext/doc properties, SmartArt/WordArt/canvas/icons, picture and shape commands verified headless on 0.11.0.
- 2026-10-25 (8): manuscript format (publisher submission) built and checked in WordCraft and ONLYOFFICE; header-skipping-page-1 order, space-before-at-page-top trap, italic carry-over fix.
- 2026-10-25 (9): screenplay format built and checked in WordCraft and ONLYOFFICE; title-page section with restarted numbering, exact line pitch, indentRight, autocorrect trap.
- 2026-10-25 (10): screenplay extras (scene numbers, bold/underline, centred, dual dialogue, acts, Fountain title page, Fountain/FDX export, (MORE)/(CONT'D) by two-pass pagination) and manuscript extras (verse, block quote, footnotes, page count, query letter, synopsis) built and checked.
- 2026-10-25 (11): stage play format (title page and characters page in their own numbering, centred cues, italic directions) built and checked in WordCraft and ONLYOFFICE; section header with a text prefix before the page field.
- 2026-10-25 (12): character effects, paragraph helpers, find next/previous, clipboard items, header/footer edit/remove, content-control actions, file info/privacy/inspect/versions/export/print, labels and envelopes verified headless on 0.11.0.
- 2026-10-25 (13): ink (strokes, lasso select/recolour/move/delete, erase, ink to shape, pens, replay) verified headless; page index is 0-based.
