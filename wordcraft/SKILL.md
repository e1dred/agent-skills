---
name: wordcraft
description: Use when writing, formatting or converting Word documents (.docx), manuscripts, letters, reports or résumés, when running wordcraft-cli, or when connecting to the WordCraft app (storytold) live on this machine
---

# WordCraft

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, last tested on **WordCraft 0.12.0** (Linux AppImage). If `wordcraft-cli --version`
reports something newer, treat anything in this skill as "probably still true" and re-check it before relying on it.

## Keep this file growing

This guide is built up as tasks happen. At the end of every WordCraft task:
- Add any command, parameter format, recipe or trap you verified to the matching file in `reference/` (see the table below).
- Correct anything here that turned out to be wrong (don't leave stale claims).
- Only record what you actually confirmed (by rendering, `inspect`, or reading back) — mark guesses as unverified.
- Keep it general: no personal data, names or machine-specific paths (this file is meant to be shared).
- Add a dated line to `reference/log.md`.

## Official docs (read these first; this guide adds what they lack)

Repo: https://github.com/storytold/wordcraft
- `docs/mcp.md` — **the property reference**: full CharProps / ParaProps tables, Border and colour formats,
  tool arguments, file confinement. Raw: https://raw.githubusercontent.com/storytold/wordcraft/main/docs/mcp.md
- `docs/control-protocol.md` — control port, key file, methods (`engine.execute`, `ui.*`, `file.*`).
- Live command list: `engine.commands {"search":…}` / `wordcraft-cli commands --json`; MCP resources
  `wordcraft://commands` and `wordcraft://document`.
Not covered there (as of 2026-10): `styles.create` side effect, `list.define`, bold-off-overrides-style,
recipes. Those live in `reference/`.

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

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `live-editing.md` | Live editing through the control server or MCP bridge: connecting, typing, selecting, screenshots, what not to do to the user's open document | Live mode, verified |
| `existing-documents.md` | Opening, comparing, templating and reformatting documents that already exist (résumés, review comments, template files) | Opening real résumés; Document comparison; Templates; Reformatting a real document with review comments |
| `mail-merge-citations.md` | Mail merge, citations, bibliography and cross-references | Mail merge; Citations, bibliography, cross-references |
| `sections-headers-tables.md` | Headers and footers per section, section breaks and orientation, designed table layouts, tables in depth, outline view, pictures and shapes | Headers and footers per section; Tables in depth, outline view, building blocks, pictures and shapes; Sections; Table layouts for designed pages |
| `formatting-and-editing.md` | Paragraph, character and style formatting, lists, TOC and index, tracked changes, accessibility checker, ink, content controls | Accessibility checker; Paragraph formatting, lists and editing commands; Next-tier workflows; Styles management, index and TOC, equations, tracked changes in depth; Character effects, paragraph helpers, find, content controls, files and labels; Ink |
| `document-formats.md` | Ready-made document styles and formats built with the builders in ../styles: eight styles, manuscript, screenplay, stage play, policy manual, whole novel | Document styles; Manuscript format for publishers; Screenplay format; Policy manual with a TOC, callouts, matrix and tracked-change log; A whole public-domain novel as a manuscript; A verse play from an ebook HTML |
| `command-reference.md` | Property names and the verified command list, plus the sweep of every remaining command id; look up exact parameters here | Version note; Property names; Commands; Sweep of every remaining command id on a blank document |
| `log.md` | Dated log of what was tested when | Log |

## Choosing live vs headless

- **Live** (user watches): bridge MCP / `tools/wcmcp.py`. Check `ui_inspect` first: `title`, `dirty`.
  Never replace or close a document with unsaved changes (`file.close` without `force` refuses; keep it that way).
- **Headless** (build, then show): `wordcraft-cli run --script s.json` → `render` pages → look → fix.
  Safer for big rebuilds; open the result for the user afterwards (launch the app with the file).
- Editing a file that is open in a window: edit the file on disk, then tell the user to close the window
  WITHOUT saving and reopen — saving from the old window would overwrite the change.

## CLI essentials (verified)

> Not re-checked: `batch` and the other converters.

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
- Different headers per section: SOLVED, see "Headers and footers per section" in `reference/sections-headers-tables.md`. The earlier failures came from passing `page` to `insert.createHeader` and from the call order.
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
