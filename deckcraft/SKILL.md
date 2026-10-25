---
name: deckcraft
description: Verified working knowledge for driving the DeckCraft presentation app (storytold/deckcraft, a PowerPoint-style editor for .deckcraft and .pptx) from an AI agent: the headless deckcraft-cli (info, render, convert, run), the live control channel / MCP bridge to a running app, exact command parameter formats, traps and verification steps. Load before any DeckCraft or slide-deck task on this machine, and add what you learn at the end of it.
---

# DeckCraft

Field notes from real tasks, tested on **deckcraft-cli 0.10.0** (Linux AppImage). DeckCraft is an alpha, PowerPoint-style
presentation app in Rust. Everything is a command with an id (321 of them); CLI, MCP and the live control channel run the
same commands. If `deckcraft-cli --version` is newer, re-check before relying on this.

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

## More recipes (verified headless, 0.10.0)

- **Theme**: `design.theme {"name":"Harbor"}` (list with `design.themes`); starters via `file.new {"template":"Quarterly"}` give 5 slides.
- **Fill / text**: `shape.fill {"color":"#E07B39"}` acts on the just-inserted (selected) shape; also `ids`. `text.set {"id","text"}`,
  `format.size/bold/font/color` act on the selection; `shape.setBounds {x,y,w,h,ids?}`; `arrange.align {"edge":"center"}`.
- **Animation**: `animation.add {"effect":"fade","start":"onClick","duration":600}` → `{"count":1}`; `animation.get` lists them
  (class, effect, durationMs, shape id). `animation.list` shows every effect. Animations, the `push` transition (with
  `durationMs`) and notes all survived a `.deckcraft` → `.pptx` → reopen round trip.
- **Picture**: `insert.picture {"path":"pic.png","rect":[500,200,200,120]}` (PNG renders; SVG/HEIC don't). Relative paths resolve from the CLI's cwd.
- **Outline import**: `slide.fromOutline {"text":"# Title\n- bullet\n  - nested","markdown":true}` → `{"slides":N}` (headings = slides). Adds after the
  current slide; the blank first slide of a fresh `file.new` stays.
- **Exports** via `run --in F --export OUT --export-params JSON`: notes pages `{"layout":"notes"}` (one page per slide: 6),
  handouts `{"layout":"handouts","perPage":6}` (1 page for 6 slides); `convert F x.gif` makes an animated GIF
  (GIF89a, 960×540); `convert F x.md` writes the outline (tab-indented bullets).
- Render check: `deckcraft-cli render F --slide 1 --scale 1 out.png` (slide index 0-based; output path is the *last* argument).

## Log

- 2026-10-25: first verified run on Linux (0.10.0): headless run/save/convert/render/info, live new/slide/shape/table/chart/
  save/export/screenshot with the Pitch starter. Reference reading: artcraft-skills `deckcraft` (macOS, MIT).
- 2026-10-25 (2): themes, animation, transition, picture, notes, outline import, notes/handout PDF, GIF, pptx round trip verified headless.
