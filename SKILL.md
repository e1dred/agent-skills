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
- Selection + links: `select.text {"text":…}` then `insert.link {"url":"mailto:…"}` or `{"url":"https://…"}`
  keeps the selected text as the link text.
- Properties: `file.properties {"title","author","subject","keywords"}`.
- Save/export: `file.save {"path"}`, `file.saveAs {"path"}`, `file.exportPdf {"path"}`.
- `file.open {"path"}` / `file.close {"force"?}` exist; untested whether `file.open` replaces a dirty doc.

## Traps (each one cost time)

- **Unknown property keys are silently ignored** — no error (documented in docs/mcp.md). Confirm every new
  key with `inspect`. Example: `para.set {"props":{"spaceAftr":12}}` succeeds and changes nothing.
- **`styles.create` also applies the new style to the current paragraph.** Reset with `para.style` afterwards.
- **`format.bold {"value":false}` is direct formatting and overrides a style's bold.** For a bold label inside a
  line: `format.bold true` → insert → `format.resetChar` → insert the rest. Never set bold false "to be safe".
- (Unverified precaution) A new paragraph may carry over the previous paragraph's numbering — the resume
  recipe sets `numbering num 0` on every non-list paragraph. Confirm with `inspect` before calling it a trap.
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
