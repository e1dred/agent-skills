---
name: onlyoffice
description: Verified working knowledge for driving ONLYOFFICE Desktop Editors from an AI agent through its built-in AI-tools MCP server (onlyoffice-document-builder) — enabling it, connecting from outside the app (Linux flatpak), LIVE editing of documents open in the editor, headless editing/preview, Word macro API details that work, recipes and traps. Load before any ONLYOFFICE task, and add what you learn at the end of it.
---

# ONLYOFFICE Desktop Editors

Field notes from real tasks, tested on **ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, Linux)** with the
AI-tools server **onlyoffice-document-builder 2.0.0-native**. Re-check anything below on other versions.

## Keep this file growing

At the end of every ONLYOFFICE task: add verified commands, API details, recipes and traps to the matching
section; fix anything that proved wrong; mark guesses as unverified; keep it general (no personal data or
machine-specific paths — this file is meant to be shared); add a dated log line.

## How the connector works

- **Enable it:** Settings → *Enable AI features* (stored as `<disable-ai>0</disable-ai>` in
  `…/desktopeditors/data/settings.xml`). The app then installs an add-on at
  `…/data/addon/desktop-sdk-plugins/aitools-bridge/` containing `docbuilder-tools` (an MCP server on stdio,
  ~93 tools for word/cell/slide/pdf/forms), `libaitools-bridge.so`, and agent docs (`resources/docs/*.md`,
  `instructions.json`, `skills/`). Read `resources/docs/overview.md` — it is the vendor's own agent guide.
- **Live link:** at startup the app launches its own `docbuilder-tools`, listens on a random localhost port,
  and writes a discovery file `…/data/cache/work_temp/onlyoffice-ai-tools.json` (`{pid, port, protocol, token}`,
  mode 0600; port and token change every launch).
- **Connecting from outside:** a second `docbuilder-tools` started with `AI_TOOLS_DISCOVERY=<that file>` reaches
  the running editor. It needs the app's libraries, so on the flatpak run it inside the sandbox:
  `tools/onlyoffice-ai-mcp` does exactly that (paths for the Flathub flatpak; adjust `D=` for other installs).
  Register: `claude mcp add onlyoffice -- /path/to/onlyoffice-ai-mcp`.
  Without the app running, the same server still works headless on files.
- The flatpak needs **network permission** (`shared=network`) for the localhost link. Forks without it (e.g. the
  Euro-Office flatpak, which also never installed the add-on) don't get a working connector.
- Start the app from the desktop menu, not from an agent's shell: a child process inherits the shell's
  environment, including any session tokens. The wrapper strips the one Claude Code sets.
- **No MCP tools in the session** (or the session's MCP link dropped — seen once mid-task): `tools/ooc.py`
  runs calls through the wrapper directly: `python3 -I tools/ooc.py "/abs/Doc.docx" calls.json`.

## Live vs headless (verified)

- `list_editor_documents` → paths open in the editor plus `modified` flags, and a count of
  `unsaved_new_documents`. A never-saved document has no path and **cannot be attached** — ask the user to
  Save As first.
- `open_document(path)` with a path that is open in the editor **attaches live**: every edit appears in the
  user's window at once; `get_document_info` says `mode: "live"`.
  - `save_document` is refused (only the user saves); `close_document` only detaches.
  - `preview` is refused live, and `get_api_reference(class_name=…)` introspection fails
    ("Could not create an instance") — use the topic guides instead.
  - The attached file on disk keeps the old version until the user saves: tell them about Save As vs Save.
- `open_document(path)` on a file NOT open in the editor works **headless**: `save_document(path, overwrite=true)`
  and `preview(pages=…, format="png", path=…)` both work. Use this to check a layout visually — e.g. run the
  same macros on a copy and render it.
- Each `ooc.py` run re-attaches; in headless mode, save before the run ends or the edits are lost.

## Word macro API notes (`word_write_macro`, verified)

Read `get_api_reference(topic=…)` first: topics `styles`, `lists`, `paragraphs`, `search`, `sections`,
`patterns`, `units`, `tables`, `runs`, `colors`, `headers-footers`, `images`, `forms`, `document`, `macro`.
- **Units:** font size in half-points (`SetFontSize(21)` = 10.5 pt); spacing, indents, tabs, page size and
  margins in twips (20/pt, 1440/in; Letter = 12240×15840); border width in 1/8 pt.
- Live macros run in strict mode: declare every variable; return only JSON-simple values.
- Styles: `doc.GetStyle("Normal")`, `doc.CreateStyle(name, "paragraph")` + `SetBasedOn(doc.GetStyle("Normal"))`;
  edit via `style.GetTextPr()` (`SetFontFamily`, `SetFontSize`, `SetBold`, `SetCaps`, `SetColor(Api.Color("#1F3864"))`,
  `SetItalic`, `SetSpacing`) and `style.GetParaPr()` (`SetSpacingBefore/After`, `SetSpacingLine(240,"auto")`,
  `SetKeepNext`, `SetJc`, `SetIndLeft`, `SetIndFirstLine`, `SetTabs([twips],["right"])`, `SetBottomBorder`).
  Restyling built-in "Heading 1" keeps real headings for ATS/outline.
- `SetBottomBorder("single", 6, 1, color)`: the recipe tries an `ApiColor` first and falls back to r,g,b
  arguments; the border rendered, but which form this version accepted is unverified.
- Page: `doc.GetSections()[0].SetPageSize(w,h)` / `.SetPageMargins(left, top, right, bottom)`.
- Paragraphs: `Api.CreateParagraph()`, `p.SetStyle(name)`, runs via `Api.CreateRun()` + `r.AddText()`,
  `r.SetBold(true)`, `r.AddTabStop()` for a tab character, `p.AddElement(r)`, `doc.Push(p)`.
- Bullets: `doc.CreateNumbering("bullet").GetLevel(0)`; `SetTemplateType("bullet","•")`, `GetTextPr().SetColor(…)`,
  `GetParaPr().SetIndLeft/SetIndFirstLine`, `SetSuff("tab")`; `p.SetNumbering(level)`. Objects don't persist
  between macro calls — in a later call, reuse the level from an existing list paragraph (`p.GetNumbering()`).
- Links: `doc.Search(text, true)[0].AddHyperlink(url, tip)` keeps the visible text (mailto: and https: verified).
- Read back: `p.ToHtml({RenderHTMLTags: true})` (shows `<strong>`, `<a href>`), `p.GetNumbering()`,
  `doc.GetStatistics()` → `{PageCount, WordsCount, ParagraphCount, …}` (works live).

## Traps

- **An empty paragraph's `GetText()` is `"\r\n"`, not `""`.** Test emptiness with `.replace(/[\r\n]/g, "") === ""`.
- **`doc.RemoveAllElements()` leaves one empty paragraph**; after pushing new content, remove element 0 if empty.
- Applying a style doesn't override direct run formatting already on the text (vendor docs); clear direct props
  (e.g. via `word_for_all_text`) when restyling existing content.
- `doc.GetStyle(name)` returns null for an unknown name, and `SetStyle(null)` REMOVES a style — pass names to
  `SetStyle` so typos throw.
- Never pass `discard_unsaved=true` on your own; the server refuses to drop unsaved work for a reason.

## Verify before reporting

- Live: read back with `word_get_document_text`, `ToHtml`, `GetNumbering`, `doc.GetStatistics()`.
- Visual: run the same build headless on a copy and `preview` it (see above), or ask the user to look.

## Recipes

- `recipes/resume_live.py` — ATS-friendly résumé rebuilt live in 4 visible stages (styles → header/summary →
  experience → rest + links). Fictional sample data; replace `RESUME`. Verified live (2 pages) and headless with
  `preview` (render matched the intended layout).

## Log

- 2026-10-24: Initial notes: connector discovery and wrapper, live résumé rebuild, headless preview check
  (ONLYOFFICE 10.0.0 flatpak, server 2.0.0-native).
