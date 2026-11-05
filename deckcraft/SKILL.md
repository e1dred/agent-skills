---
name: deckcraft
description: Use when building, editing, rendering or converting slide decks (.deckcraft, .pptx), when running deckcraft-cli, or when connecting to the DeckCraft app (storytold) on this machine
---

# DeckCraft

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates; only present in a full clone of the repo, otherwise compare `deckcraft-cli --version` with the app's version in its About box or on its releases page by hand; `--version` on an AppImage can open the app). A CLI older than its app has caused real failures. In a full clone, `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, last tested on **deckcraft-cli 0.15.1** (Linux AppImage). DeckCraft is an alpha, PowerPoint-style
presentation app in Rust. Everything is a command with an id (331 of them); CLI, MCP and the live control channel run the
same commands. If `deckcraft-cli --version` is newer, re-check before relying on this.

## Keep this file growing

This guide is built up as tasks happen. At the end of every DeckCraft task:
- Add any command, parameter format, recipe or trap you verified to the matching file in `reference/` (see the table below).
- Correct anything here that turned out to be wrong (don't leave stale claims).
- Only record what you actually confirmed (by rendering, `info` or reading back); mark guesses as unverified.
- Keep it general: no personal data, names or machine-specific paths (this file is meant to be shared).
- Add a dated line to `reference/log.md`.

## Surfaces


- **Headless CLI**: `info FILE`, `render FILE --all --scale 1 OUTDIR/` (PNG per slide, 0-based `--slide N`),
  `convert IN OUT` (`.deckcraft .pptx .pdf .txt/.md .png .jpg .gif`; PNG/JPG = first slide only),
  `run [--in FILE|--sample] --cmd 'id={json}'... --save OUT [--export OUT] [--print]`,
  `commands [FILTER]`, `describe COMMAND` (parameter docs — use this before guessing).
- **Live app**: start with `--control PORT`; then `deckcraft-cli app --port PORT COMMAND '{json}'` runs a command, and
  `deckcraft-cli app --port PORT --method ui.inspect|ui.screenshot|document.inspect '{json}'` calls a control method.
  (Note: the CLI `--port` goes *before* the command.)
- **MCP**: `deckcraft-cli mcp --connect PORT`. If the MCP server failed to connect at session start the app wasn't running
  yet; the `app` subcommand works anyway.

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `building-decks.md` | Building whole decks: recipes, exports (PDF, notes pages, handouts, GIF), a real deck end to end, a board deck with charts, next-tier workflows | More recipes; Building a real deck; Next-tier workflows; Board deck from sample data: charts, axis, alt text |
| `smartart-animation-masters.md` | SmartArt layouts, grouping, pictures, slide layouts, animation and transition catalogues, master editing | SmartArt, grouping, pictures, layouts; SmartArt layouts, animation and transition catalogues, master editing |
| `shapes-text-tables.md` | Shapes, text and character formatting, tables, photo album, shape actions and action buttons (listing a slide's links: `slide.actions` in `newer-commands.md`), sections, media, navigation, alignment, ink | Shapes, text formatting, tables, photo album, actions, sections, masters and files; Text editing, character formats, arranging, media, navigation and data commands; Ink in DeckCraft; Alignment and redo |
| `newer-commands.md` | What each version added or changed (0.11 onward), with exact parameters: motion paths, slide actions, gradient kinds | New in 0.11.x; Newer commands; 0.13 changes; 0.14 changes; 0.15 changes |
| `command-sweep.md` | The last 28 command ids, smoke-tested | The last 28 command ids; Verified in detail, DeckCraft phase 2; Verified in detail, DeckCraft second pass |
| `log.md` | Dated log of what was tested when | Log |

## Command formats (verified)

| Goal | Command |
|---|---|
| new deck | `file.new` (blank) or `file.new {"template":"Pitch"}` (starters: Briefing, Lesson, Pitch, Field Notes, Quarterly, Evening Talk) |
| slide | `slide.new {"layout":"title|titleAndContent|titleOnly|blank|twoContent|…","title":"…","body":"a\nb\n\tnested","at"?}` → `{id,index}`; inserted after the current slide and becomes current |
| navigate | `slide.go {"index":1}` (0-based) |
| shape | `shape.insert {"preset":"roundRect|star5|…","rect":[x,y,w,h],"text"?}` points on a 960×540 slide → `{id}` |
| table | `insert.table {"rows":3,"cols":2,"rect":[…]}` |
| chart | `insert.chart {"type":"column|bar|line|pie|…","rect":[…],"categories"?,"series"?:[{name,values}]}` |
| notes | `slide.notes {"text":"…","index":2}` |
| transition | `transition.set {"kind":"fade","duration"?:ms,"index"?}` — parameter is `kind`, not `type` |
| inspect | `slide.inspect {"index"?}` (shapes, ids, boxes), `document.inspect` (needs an open deck) |
| save | `file.save {"path":…}` (format by extension: `.deckcraft`, `.pptx`) |
| export | `file.export {"path":…,"format"?,"all"?:true,"slide"?,"scale"?}`; PDF options `layout, perPage, paper, orientation, slides` |

## Traps

- Headless `file.new` already contains **one empty title slide**; `slide.new` inserts after it, so the deck starts with a
  blank slide 0. Delete it (`slide.delete {"index":0}`) or reuse it.
- Live app with no deck open is on the Home screen: `document.inspect` errors "no presentation open" until `file.new`/`file.open`.
- `file.export` of a PNG with `"all":true` names files `stem1.png … stemN.png` (from 1) while `render --all` writes `slide-01.png`.
- Never `file.save` to `.png/.jpg` (writes native bytes under an image name); use `file.export` / `convert`.
- `file.save` to `.pptx` makes the live document point at the pptx. Keep a `.deckcraft` master and treat `.pptx` as an exchange copy.
- `file.close` and `app.quit` discard unsaved work without asking. Save with explicit paths first.
- `run` stops at the first failing command and saves nothing.
- `ui.screenshot` PNGs are ~2366 px wide (HiDPI); they're large, view rarely.
- Default theme fonts are Inter (blank) / Montserrat+Lato (Pitch); substituted fonts change line breaks, so verify by rendering.

## Verify

1. `deckcraft-cli info OUT.pptx` — slide count, titles, layouts after a round trip.
2. `deckcraft-cli render FILE --all --scale 1 dir/` and look at the PNGs (text overflow and charts are only visible there).
3. PDF: `qpdf --show-npages`; the text layer is selectable, the artwork is raster.
4. `.pptx` repair-free opening in PowerPoint is unverified; say so rather than claiming parity.
5. Work in a scratch directory; copy sources first, never edit someone's only deck.

## Limits

No `.ppt/.odp/.pptm`, no SVG/HEIC pictures, no MP4 export (GIF only), no recording, PDF artwork rasterised, SmartArt/animations
partial, English UI only.
