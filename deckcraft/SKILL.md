---
name: deckcraft
description: Verified working knowledge for driving the DeckCraft presentation app (storytold/deckcraft, a PowerPoint-style editor for .deckcraft and .pptx) from an AI agent: the headless deckcraft-cli (info, render, convert, run), the live control channel / MCP bridge to a running app, exact command parameter formats, traps and verification steps. Load before any DeckCraft or slide-deck task on this machine, and add what you learn at the end of it.
---

# DeckCraft

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, tested on **deckcraft-cli 0.10.0; later sections on 0.11.1** (Linux AppImage). DeckCraft is an alpha, PowerPoint-style
presentation app in Rust. Everything is a command with an id (321 of them); CLI, MCP and the live control channel run the
same commands. If `deckcraft-cli --version` is newer, re-check before relying on this.

## Surfaces

> **Versions:** written on 0.10.0 (2026-10-24/25). The headless CLI forms ran identically on 0.11.1 (see the version note). The live `app --port` / `ui.*` calls were tested on the 0.10.0 app only; the 0.11.1 app was not running when I checked, so they have **not** been re-tested.

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

> **Versions:** 0.10.0; the commands in the three build sequences below ran on both versions with identical return values.

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

> **Versions:** 0.10.0 (2026-10-25); re-run 2026-10-25 on 0.10.0 and 0.11.1 (slides, shape fill, animation, push transition, picture, notes, Harbor theme): identical return values, `info`, `.pptx` info and rendered pixels.

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

## Building a real deck (verified headless, 0.10.0)

> **Versions:** 0.10.0 (2026-10-25); re-run 2026-10-25 on 0.10.0 and 0.11.1: identical return values, `info` and `.pptx` info. **Rendered pixels differ only on the slide with the chart**: 0.11.1 draws default chart text (title, axes, legend) in a bluish theme tint where 0.10.0 drew neutral grey (about 350 pixels, at most 17 of 255 per channel); data and structure are identical. Set an explicit chart text colour if you need grey.

One `run` built title + bullets + table + chart + text box + link + background + duplicate/move/hide + section, then
`convert` to `.pptx` and `render` (checked: table, chart, formatting, background and the hidden slide all survived).

1. **Find shape ids first.** `slide.inspect {"index":0}` (`run … --print` shows the JSON) lists shapes with `id`, `kind`, `name`
   (`Title 1`, `Subtitle 2`). A fresh `file.new` slide 0 has title id 258 / subtitle 259, but always read them.
2. **Text**: `text.set {"id":258,"text":"Q3 Review"}`. For a table cell: `text.set {"text":"North","cell":[1,0]}` (row, col; acts on the
   just-inserted/selected table, or pass `id`). Bullets: `\n` separates paragraphs, a leading `\t` indents a level.
3. **Select, then format.** `format.size/bold/italic/color/alignCenter/bullets/font` act on the *selection* (inserting a shape
   selects it; otherwise `edit.select {"ids":[266]}` → `{"selected":[266]}`). Chart/alt-text commands also need a selection or `ids`:
   `chart.options` without a selection fails with "nothing selected".
4. **Chart**: `insert.chart {"type":"column","rect":[…],"categories":["Q1","Q2","Q3"],"series":[{"name":"Sales","values":[10,14,19]}]}`;
   afterwards `edit.select` it, then `chart.options {"title":"Sales by quarter","dataLabels":true,"legend":null|"b"|"r"}`,
   `chart.type {"type":"line"}`, `chart.data {"categories","series"}`. The default title is "Chart Title" — always set one or `title:null`.
5. **Link**: `insert.hyperlink {"url":"https://…","text":"Details"}` (or `{"slide":2}`); **background**: `design.background {"color":"#F4F6F8","index":2}`
   (omit `index` for the current slide, `"all":true` for every slide); **text box**: `insert.textBox {"rect":[x,y,w,h],"text":"…"}`.
6. **Slides**: `slide.duplicate {"index":1}`, `slide.move {"from":2,"to":3}`, `slide.hide {"index":3,"hidden":true}`, `slide.delete {"index"}`,
   `slide.layout {"layout":"title","index":0}`, `section.add {"name":"Body","at":1}`, `design.variant {"index":0..3}`, `design.slideSize {"preset":"widescreen"}`.
7. **Accessibility**: `review.accessibility` → `[{slide,shape,issue}]` (e.g. "Missing alternative text" for a chart); fix with
   `shape.altText {"text":"…","ids":[266]}` (or `"decorative":true`); the re-check returned `[]`.
8. Tables: new tables are 3-row styled with the theme colour; empty cells stay empty; row/col changes via `table.insertRowBelow {"row","id"}` etc.

## SmartArt, grouping, pictures, layouts (verified headless, 0.11.1)

> **Versions:** 0.11.1 only (2026-10-25); not re-run on 0.10.0.

- **SmartArt**: `insert.smartArt {"kind":"process|list|cycle|hierarchy|pyramid|matrix","items":["Plan","Build","Ship"]}` (leading tabs = sub-points) → `{id}`; then
  `smartArt.addNode {"text":"Review"}` → `{index}`, `smartArt.nodes {}` (read back `[{level,text}]`), `smartArt.setNodes {"lines":[…]}`, `smartArt.promote/demote/removeNode {"index"}`,
  `smartArt.layout {"kind":"chevron|blockList|verticalProcess|radial|timeline…"}`. Rendered result checked: 4 coloured chevrons with the text. Accessibility flags SmartArt as "Missing alternative text" — use `shape.altText`.
- **Text builds**: select the placeholder (`edit.select {"ids":[281]}`), `animation.add {"effect":"fade","start":"onClick"}`, then `animation.options {"textBuild":"byParagraph"}` → `{"changed":1}`.
- **Auto-advance**: `transition.set {"kind":"fade","duration":700}` then `transition.timing {"onClick":false,"after":3000}` (ms).
- **Align / distribute / group**: `edit.selectAll` → `{ids}`, `arrange.distribute {"dir":"horizontal","to":"selection"}`, `arrange.align {"edge":"middle","to":"selection"}`, `arrange.group` → `{id}` (render showed three shapes evenly spaced on one line).
- **Pictures**: after `insert.picture`, `picture.crop {"left":0.1,"right":0.1}` (fractions), `picture.adjust {"brightness":0.1,"saturation":1.5}` (brightness −1..1, saturation 0..4),
  `picture.style {"style":"softEdgeOval"}` (`picture.styles` lists them), `picture.recolor {"preset":"sepia|grayscale|…"}`, `picture.removeBackground {"tolerance":20}`, `picture.change`, `picture.reset`.
- **Custom layout**: `view.slideMaster` → `{kind:"layout",layout,master}`, `master.insertLayout {"name":"My Layout"}` → `{id}`, `master.insertPlaceholder {"kind":"picture|content|text|chart|table|media","rect":[x,y,w,h]}`,
  `view.closeMaster`, then `slide.layout {"layout":"My Layout"}` (name or the returned id). `master.renameLayout/deleteLayout` also exist.
- `review.accessibility` also reports "Missing slide title" for blank/layout-only slides; give them titles or accept.

## Next-tier workflows (verified headless, 0.11.1; render checked)

> **Versions:** 0.11.1 (2026-10-25). The theme-colour/fonts, header/footer, pie and stacked-column charts, table style/merge, connector, shape-effects and icon steps were also run on 0.10.0 with identical return values (same chart-text tint difference in the render). Comments, spelling, compare, custom shows, audio, WordArt, slide links and morph were run on 0.11.1 only.

- **Brand theme**: `design.colors {"name":"Brand","colors":{"dk1":"#1B1B1B","lt1":"#FFFFFF","dk2":"#16324F","lt2":"#F2F5F8","accent1":"#0E7C86","accent2":"#E4572E","accent3":"#C8963E","accent4":"#6B2E5F","accent5":"#17A398","accent6":"#7A8B99","hlink":"#0E7C86","folHlink":"#6B2E5F"}}` and
  `design.fonts {"name":"Brand fonts","major":"Georgia","minor":"Calibri"}` restyle the whole deck (titles became Georgia, charts and shapes took accent1/accent2 in order). `design.variant {"index":0..3}` picks a built-in colour variant.
- **Footer, date, slide number**: `design.headerFooter {"slideNumber":true,"footer":true,"footerText":"Sample deck","hideOnTitle":true}` (applies to all slides unless `"all":false`).
- **Chart types** (`insert.chart {"type":…,"rect","categories","series":[{name,values}]}`): `pie` (one series), `line` (several series), `stackedColumn` rendered correctly; also bar, doughnut, area, scatter, combo, waterfall… Change later with `chart.type {"type"}` / `chart.data {"categories","series"}` after `edit.select`. The default title is "Chart Title": set `chart.options {"title":…}`.
- **Tables**: `table.style {"style":"medium2-accent1|light1-accent2|dark1-tx1|grid|none"}`, `table.merge {"from":[0,0],"to":[0,2]}` (a merged header row), `table.borders {"which":"inside|outside|all|top|bottom|insideH…","color":"#BBBBBB","width":0.75}`; table styles follow the theme's accent colours.
- **Shapes**: `shape.connect {"from":271,"to":272,"preset":"bentConnector3|straightConnector1|curvedConnector3"}` → glued connector `{id,fromSite,toSite}` (it follows the shapes when they move);
  `shape.effects {"ids":[271],"shadow":"outer","glow":{"color":"#0E7C86","radius":8}}` (also softEdges, reflection, bevel, threeD); `shape.merge {"op":"union|combine|fragment|intersect|subtract","ids":[273,274]}` → one freeform `{ids:[280]}`; `insert.icon {"name":"star","rect":[…]}` (`insert.icons` lists them), `insert.wordArt {"text","style":3}`.
- **Audio**: `insert.audio {"path":"tone.wav","rect":[60,400,40,40]}` → `{contentType:"audio/wav",durationMs:1000,playable:true}` and a speaker icon on the slide (`insert.video` is the same shape).
- **Comments and review**: `comment.add {"text","x","y"}` → `{index}`, `comment.reply {"index","text"}`, `comment.resolve {"index","resolved":true}`, `comment.list`, `comment.delete {"index"|"all":true}`; `review.spelling` → misspellings with `suggestions` (Recieve → Receive, teh → the), `review.spellingChange {"shape","word","to"}`;
  `review.compare {"path":"revised.deckcraft"}` → `{changes:[{kind:"inserted",slide:2,details:["New slide"]}]}` (`review.revisions` re-reads them; `review.reject` only while a compare is open).
- **Show setup**: `show.customShow {"name":"Short","slides":[0,2]}` then `show.setup {"type":"speaker|browsed|kiosk","loop":true,"custom":"Short"}`; `show.fromStart` plays (live app).
- **Links between slides**: `edit.select {"ids":[265]}` (a shape must be selected) then `insert.hyperlink {"slide":2,"tooltip":"…"}`; without a selection: "select text or a shape". `transition.set {"kind":"morph","duration":900}` works (`transition.list` shows the kinds).
- The live-app-only and video items remain untested: playing a show, presenter view, `insert.video`, narration.

## New in 0.11.x (verified headless)

> **Versions:** 0.11.1 only (the commands do not exist in 0.10.0).

- Path editing on a shape: `shape.openPath {"index":0}` (break a closed outline), `shape.closePath {"index":0}`, `shape.deleteSegment {"index":0,"segment":2}`
  (**only on a closed outline**, otherwise "only a segment of a closed outline can be deleted"), `shape.segmentType {"index":0,"segment":1,"type":"straight|curved"}`.
  The first parameter is `index` (the subpath), not `path`; `segment` is the vertex ending the segment. Act on the selected shape or pass `id`.
- `slide.reuseList {"path":"deck.deckcraft"}` → `{name,slides:[{index,title,hidden}]}`: preview which slides `slide.reuse {"path","slides":[…],"at"?}` can bring in.
- `review.reject {"index"|"all":true}` only works while a Compare is in progress ("not comparing" otherwise).

## Version note (2026-10-25)

App/CLI 0.11.1 added 6 commands (`shape.openPath/closePath/deleteSegment/segmentType`, `slide.reuseList`, `review.reject`); none removed. The full-deck recipe
(select chart → `chart.options`, accessibility check, `.pptx` round trip with a hidden slide) behaved identically on 0.10.0 and 0.11.1.

## Log

- 2026-10-25: first verified run on Linux (0.10.0): headless run/save/convert/render/info, live new/slide/shape/table/chart/
  save/export/screenshot with the Pitch starter. Reference reading: artcraft-skills `deckcraft` (macOS, MIT).
- 2026-10-25 (2): themes, animation, transition, picture, notes, outline import, notes/handout PDF, GIF, pptx round trip verified headless.
- 2026-10-25 (3): full deck build (text, table cells, chart options, link, background, slide management, sections, accessibility) verified headless incl. pptx round trip.
- 2026-10-26: SmartArt, text builds, auto-advance timing, align/distribute/group, picture crop/adjust/style, custom master layout verified headless.
- 2026-10-25 (4): brand theme colours/fonts, header/footer, chart types, table style/merge/borders, connectors, shape effects/merge, icon/WordArt/audio, comments, spelling, compare, custom show, slide links, morph verified.
- 2026-10-25 (5): three build sequences re-run on 0.10.0 and 0.11.1 (identical except default chart text tint); version labels added per section.
