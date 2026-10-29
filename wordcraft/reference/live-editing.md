# WordCraft reference: live editing

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Live mode, verified (WordCraft, app started with `--control 47822`, blank document open)

> Re-checked on the current app (port 47826, a blank unsaved document): `type_text`, `execute para.style`, `select_text` + `format.bold`, `get_text`, `inspect_document`, `ui_inspect`, `render_page`, `design.scaleFontSizes` (the caret grew with the text), `file.closeDocument`. Not re-checked: `batch`, `key`, `click`, `new_document`, `save_document`.
> Traps: `screenshot` answers "the window is minimized" when it is; `render_page` saves its PNG as `./img_N.png` in the **working folder of the client** (`wcmcp.py` left `img_1.png` in the repo): run it from a scratch folder.

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
- **Showing the user a long text (notes, a report) in their live window, 2026-10-27, 0.11.0 app on port 47826:** convert it first (`pandoc notes.md -o notes.docx`: headings, bullets and inline code come out styled), then `open_document {"path":ABS}` through `wcmcp.py` (it answered `{encrypted,paragraphs,words,path}`) and check with `render_page {"page":1,"scale":1.2}` (1-based here, unlike `draw.*`; the reply carries `pages`). Check `ui_inspect` first: the open replaced a blank, not-dirty `Document1`; never do this over a dirty document. Keep the converted file in scratch; the user saves it with Save As if they want it.
