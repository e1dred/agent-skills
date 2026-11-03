---
name: onlyoffice
description: Use when editing documents, spreadsheets, slides, PDFs or forms in ONLYOFFICE Desktop Editors, live in an open window or headless, through its AI-tools MCP server (onlyoffice-document-builder), including Word macros and connecting from the Linux flatpak
---

# ONLYOFFICE Desktop Editors

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates; only present in a full clone of the repo, otherwise check `flatpak info org.onlyoffice.desktopeditors` and `flatpak remote-ls --updates` by hand). A CLI older than its app has caused real failures. In a full clone, `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, tested on **ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, Linux)** with the
AI-tools server **onlyoffice-document-builder 2.0.0-native**. Re-check anything below on other versions.

> Every section was tested on ONLYOFFICE Desktop Editors 10.0.0 (Flathub flatpak, commit 318889a1…) with `onlyoffice-document-builder 2.0.0-native`; `check-versions.sh` showed no update available through 2026-10-25, so nothing here was re-tested on a second version. Live-editing sections were tested 2026-10-24; the tool and macro sections 2026-10-25.

## Keep this file growing

At the end of every ONLYOFFICE task: add verified commands, API details, recipes and traps to the matching
file in `reference/` (see the table below); fix anything that proved wrong; mark guesses as unverified; keep it general (no personal data or
machine-specific paths — this file is meant to be shared); add a dated line to `reference/log.md`.

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

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `live-editing.md` | Editing a document the user has open, in all four editors | Live editing of all four editors |
| `word.md` | Word macros, Word helper tools, filling a template from data, editing real résumés safely | Word macro API notes; Résumés: editing real ones safely; Filling a Word template from data; Word helper tools |
| `forms-and-pdf.md` | Fillable forms (every field type), PDF tools | Forms, all field types; PDF tools; Fillable forms |
| `spreadsheets.md` | The cell_* tools: data, formulas, formats, charts, sorting | Spreadsheets; Spreadsheets, more |
| `presentations.md` | The slide_* tools and designed decks built from shapes | Designed decks from shapes; Presentations |
| `macro-workflows.md` | Next-tier tasks done through macros, conditional formats, filters, pivots and slide tools | Conditional formats, filter, pivot, slide tools; Next-tier workflows through macros |
| `tool-audit.md` | Every one of the 93 tools called, with parameters and results | Every remaining tool, verified; Tool audit: all 93 tools called on ONLYOFFICE 10.0.0 |
| `document-styles.md` | The eight document styles built in ONLYOFFICE (doc, résumé, CV, paper and more) | Document styles |
| `log.md` | Dated log of what was tested when | Log |

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

## Traps

- **An empty paragraph's `GetText()` is `"\r\n"`, not `""`.** Test emptiness with `.replace(/[\r\n]/g, "") === ""`.
- **`doc.RemoveAllElements()` leaves one empty paragraph**; after pushing new content, remove element 0 if empty.
- Applying a style doesn't override direct run formatting already on the text (vendor docs); clear direct props
  (e.g. via `word_for_all_text`) when restyling existing content.
- `doc.GetStyle(name)` returns null for an unknown name, and `SetStyle(null)` REMOVES a style — pass names to
  `SetStyle` so typos throw.
- **The MCP link can drop mid-session** (all `mcp__onlyoffice__*` tools vanish); the wrapper still works, so continue
  with `tools/ooc.py` (it now also takes `new:docx|xlsx|pptx` to start from a blank headless document).
- Never pass `discard_unsaved=true` on your own; the server refuses to drop unsaved work for a reason.

## Verify before reporting

- Live: read back with `word_get_document_text`, `ToHtml`, `GetNumbering`, `doc.GetStatistics()`.
- Visual: run the same build headless on a copy and `preview` it (see above), or ask the user to look.

## Recipes

- `recipes/resume_live.py` — ATS-friendly résumé rebuilt live in 4 visible stages (styles → header/summary →
  experience → rest + links). Fictional sample data; replace `RESUME`. Verified live (the earlier, longer sample made 2 pages; the current invented sample is 1 page) and headless with
  `preview` (render matched the intended layout).
