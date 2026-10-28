---
name: deckcraft
description: Use when building, editing, rendering or converting slide decks (.deckcraft, .pptx), when running deckcraft-cli, or when connecting to the DeckCraft app (storytold) on this machine
---

# DeckCraft

**Start of a session:** run `../check-versions.sh` (read-only; app vs CLI versions, ONLYOFFICE flatpak updates). A CLI older than its app has caused real failures. `../coverage.sh` shows how much of the app this skill names.

Field notes from real tasks, tested on **deckcraft-cli 0.10.0; later sections on 0.11.1** (Linux AppImage). DeckCraft is an alpha, PowerPoint-style
presentation app in Rust. Everything is a command with an id (321 of them); CLI, MCP and the live control channel run the
same commands. If `deckcraft-cli --version` is newer, re-check before relying on this.

## Surfaces

> **Versions:** written on 0.10.0 (2026-10-24/25). The headless CLI forms ran identically on 0.11.1 (see the version note). The live `app --port` / `ui.*` calls were re-tested 2026-10-25 on the 0.11.1 app (port 47824, started with plain `--control 47824`, blank unsaved Presentation1): `slide.new`, `shape.insert`, `shape.fill`, `insert.table`, `insert.chart`, `document.inspect`, `ui.screenshot` and `file.export` to PDF (2 pages) all behaved as documented, and the window showed the shape, table and pie chart.

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

## SmartArt layouts, animation and transition catalogues, master editing (verified headless, 0.11.1; renders checked)

> **Versions:** 0.11.1 only (2026-10-25); not re-run on 0.10.0.

- **All 45 SmartArt layouts render.** Build one with `insert.smartArt {"kind":"process","items":[…],"rect":[80,130,800,360]}` and switch with `smartArt.layout {"kind":…}` (`kind` of `insert.smartArt` is limited to list|process|cycle|hierarchy|pyramid|matrix; `smartArt.layout` takes the full set):
  list, blockList, hBulletList, process, chevron, verticalProcess, stepUp, cycle, blockCycle, radial, hierarchy, pyramid, invertedPyramid, matrix, titledMatrix, pictureList, pictureCaption, pictureProcess, pictureHList, timeline, venn, target, textCycle, continuousCycle, horizontalHierarchy,
  gridMatrix, gear, funnel, segmentedCycle, multidirectionalCycle, orgChart, halfCircleOrgChart, cycleMatrix, segmentedPyramid, pie, nameTitleOrgChart, verticalBoxList, trapezoidList, tableList, accentProcess, continuousBlockProcess, bendingProcess, linearVenn, stackedVenn, nestedTarget.
  A flat 4-item list in an org-chart layout draws four boxes with no connectors: give hierarchy with leading tabs (`"CEO","\tCTO","\t\tDev","\tCFO"` → levels 0/1/2/1, read back with `smartArt.nodes`). Picture layouts show empty picture slots until `smartArt.picture {"index","path"}`.
  Other verified calls: `smartArt.style {"style":"polished"}`, `smartArt.colors {"colors":"colorful"}`, `smartArt.addNode {"position":"assistant","text":"EA","index":0}`, `smartArt.toText` (→ new id), `smartArt.fromText {"kind":"cycle"}`, `smartArt.toShapes`. The ids change after each conversion.
- **Animation gallery** (`animation.list`): 24 entrance, 17 emphasis, 23 exit, 40 motion-path, 3 media effects. Entrance: appear, fade, fly, float, split, wipe, shape, wheel, randomBars, grow, zoom, swivel, bounce, blinds, box, checkerboard, circle, diamond, dissolve, peek, strips, expand, rise, spinner;
  emphasis: pulse, colorPulse, teeter, spin, growShrink, desaturate, darken, lighten, transparency, objectColor, complementaryColor, lineColor, fillColor, fontColor, underline, boldFlash, wave; exit: disappear, fadeOut, flyOut, … sinkDown, contract;
  paths: lines, arcs, turns, shapes, loops, zigzag, sineWave, heartbeat, spiralRight, spring, star5, heart, figure8Horizontal, customPath, … Direction/shape options per effect are listed in the `options` array (fly: b,lb,l,lt,t,rt,r,rb).
  `animation.add {"effect":"pulse","class":"emph|entr|exit|path","option","start":"onClick|withPrevious|afterPrevious","duration","delay","ids"}`: **pass `class` for non-entrance effects** (the default class is entrance); a path effect stores an SVG-like `path` string. `animation.get` returns every field (`class` as entrance/emphasis/exit/path, `presetId`, `delayMs`, `durationMs`, `textBuild`, `repeat`, `autoReverse`, `trigger`, `sound`).
  `animation.move {"index","to"}`, `animation.timing {"index","start","duration","delay"}` → `{changed}`, `animation.options {"index","option"}`, `animation.remove {"index"}`; all animations and the transitions survived `convert … .pptx` (info: Anim slide 3 animations).
- **Transition gallery** (`transition.list`, 49): Subtle (none, morph [objects|words|characters], fade [smoothly|throughBlack], push, wipe, split, reveal, cut, randomBar, shape, uncover, cover, flash) and Exciting (fallOver, drape, curtains, wind, prestige, fracture, crush, peelOff, pageCurlDouble, airplane, origami, dissolve, checker, blinds, clock [clockwise|counterClockwise|wedge], ripple, …) with default durations (morph 2000 ms, fade 700, push 1000).
  `transition.set {"kind":"push","option":"u","duration":1200}`, `transition.options {"option":"d"}`, `transition.timing {"onClick":true,"after":4000}`, `transition.sound {"builtin":"chime"}` → `{sound:"Chime.wav",media,playable}` (builtins: chime, click, camera, whoosh, drumRoll, laser, or `path`), `transition.applyAll {}` copies the current slide's transition to every slide **that exists then** (a slide added after keeps its own).
- **Slide master / layouts:** `view.slideMaster {}` opens the master view on the *current slide's layout* (`{kind:"layout",layout:1,master:0}`); a shape inserted then lives on that layout and appears on every slide using it (verified: a navy footer bar + "ACME CONFIDENTIAL" on "Title and Content" slides, not on others).
  `master.insertLayout {"name"}` → `{id}`, `master.insertPlaceholder {"kind":"text|picture|content|chart|table|media","rect"}` → `{id}`, `master.renameLayout {"name"}`, `master.preserve {"preserve":true}`, `master.placeholders {"title":true,"footers":true}`, `view.closeMaster`; the new layout appears in `document.inspect.layouts` and `slide.new {"layout":"Banner 2"}` uses it.
  A new layout does NOT inherit shapes added to another layout. To brand every slide, edit the master itself (use `view.slideMaster {"master":0}` without a layout — not tested).
- Also listed, not run: `design.ideas`/`applyIdea`, `view.handoutMaster/notesMaster`, `design.browseTheme` (apply a .pptx/.potx's master), `design.effects`, `design.hideBackgroundGraphics`, `insert.photoAlbum`, `animation.painter`, equations (no `equation.*` ids in DeckCraft).

## Shapes, text formatting, tables, photo album, actions, sections, masters and files (verified headless, 0.11.1; renders checked)

> **Versions:** 0.11.1 only (2026-10-25); not run on 0.10.0. **`deckcraft-cli describe CMD` prints every parameter with types and notes: read it before guessing** (most of the failures below were wrong parameter names that `describe` would have shown).

- **Shape formatting** (act on the just-inserted/selected shape, `ids` optional; return `1`): `shape.rename {"name"}`, `shape.adjust {"index":0,"value":0.4}` (corner radius etc.), `shape.line {"color","width","dash":"solid|dot|dash|lgDash|dashDot|sysDot|sysDash","cap","join","compound":"single|double|thickThin…","none"}`, `shape.quickStyle {"index":9}` (0..41 = theme row × accent), `shape.sizePosition {"x","y","w","h","rot","scaleW","scaleH","lockAspect"}`, `shape.move {"dx","dy"}` or `{"x","y"}`, `shape.resize {"w","h"}`,
  `shape.rotate {"deg"}` (absolute) or `{"by"}`, `shape.flip {"axis":"horizontal|vertical"}`, `shape.lock {"locked"}`, `shape.visible {"visible":false}` (selection pane), `shape.change {"preset":"hexagon"}`, `shape.smoothCorners {"smoothing":50,"radius":10}` (**only on rectangles/rounded rectangles**, so smooth BEFORE `shape.change`), `shape.freeform {"points":[[x,y]…],"closed":true,"smooth":true}` → `{id}`, `shape.inspect {}` (box incl. rot/flip, geom, fill, effects).
  Arrange: `arrange.bringToFront|sendToBack|bringForward|sendBackward|rotateRight|rotateLeft|flipHorizontal|flipVertical|ungroup|regroup`, `arrange.nudge {"dx":6,"dy":0}` (arrow key = 6 pt), `arrange.reorder {"id","index"}`. Guides: `guide.add {"vertical":true,"pos":480}` → `{index}`, `guide.list` → `[{pos,vertical}]`, `guide.move {"index","pos"}`, `guide.delete {"index"}`.
  Edit points: a preset star returned empty `shape.points` (`{paths:[],…}`) and `addPoint/movePoint/pointType/deletePoint` did nothing visible: **enter `shape.editPoints {"on":true}` first (turns a preset into a freeform)**, then `shape.points` → `{paths,types,segments}`. `shape.sites {"id"}` needs an id.
- **Text editing and formatting** (render checked: bold red upper-case "FIRST", check-mark bullets in teal, text in the left column): `text.edit {"at":[para,char]}` (or `id`,`cell`,`notes`), `text.select {"anchor":[p,c],"caret":[p,c]}`, `text.selectAll`, `text.insert {"text"}` (`\n` = new paragraph), `text.get {"id"}` → `{text,paragraphs}`, `text.exit`; then `format.bold|italic|underline|strikethrough|superscript|subscript {}`, `format.color {"color"}`, `format.highlight {"color"}`, `format.case {"mode":"upper|lower|title|sentence|toggle|cycle"}`, `format.spacing {"pt":3}`, `format.grow/shrink`, `format.textShadow {"on"}`, `format.textOutline {"color","width"}`, `format.textWarp {"preset"}`, `format.language`,
  paragraph: `format.paragraph {"align":"justify","indentLeft","indentFirst":18,"spaceBefore","spaceAfter":6,"lineSpacing"}`, `format.lineSpacing {"lines":1.5}` or `{"pt"}`, `format.bullets {"on":true,"char":"✓|•|○|■|□|◆|➢|–","color","size"}`, `format.numbering {"on":true,"scheme":"romanLcPeriod|arabicPeriod|arabicParenR|alphaUcPeriod…","start":3}`, `format.align*`, `format.indent/outdent`, `format.tabs`.
  Box: `format.margins {"left","top","right","bottom"}`, `format.anchor {"anchor":"top|middle|bottom"}`, `format.autofit {"mode":"none|shrink|resize"}`, `format.columns {"count":2,"spacing":18}`, `format.wrap`, `format.direction`. `text.find {"text","matchCase","wholeWords"}` → `[{slide,shape,cell,para,start,end}]`, `text.replace {"text","with"}` → `{replaced:2}`. `font.used {}` → families, `font.replace {"from":"Inter","to":"Georgia"}` → `{replaced}`.
- **Tables:** `table.options {"headerRow","totalRow","bandedRows","firstColumn","lastColumn","bandedColumns"}`, `table.cellFill {"color","cells":[[r,c]]}`, `table.cellMargins {"preset":"wide|narrow|none|normal"}`, `table.cellAlign {"anchor"}`, `table.columnWidth {"col","width"}`, `table.rowHeight {"row","height"}`, `table.insertRowAbove|insertColumnRight|insertColumnLeft`, `table.deleteRow|deleteColumn`, `table.distributeRows/Columns`, `table.drawLine/eraseLine`;
  **`table.split {"cell":[r,c]}` only on a merged cell** ("that cell isn't merged"): `table.merge {"from":[0,0],"to":[0,1]}` first.
- **Photo album, slide extras:** `insert.photoAlbum {"pictures":[{"path","name","rot","brightness","contrast"}|{"text"}],"layout":"fit|1|2|4|1title|2title|4title","frame":"none|rect|rounded|simple","captions":true,"grayscale","theme","name"}` → `{album,first,pictures:4,slides:1}` (render: four framed pictures with file-name captions, 2×2 on one slide), `insert.photoAlbumEdit`;
  `insert.actionButton {"kind":"home|back|forward|beginning|end|information|return|movie|document|sound|help|custom","rect"}` (a blue home button rendered), `insert.zoom {"kind":"summary|slide|section","slides":[0,1]}` → `{ids:[…],returnToZoom}`, `insert.slideNumber`, `insert.dateTime {"format":"datetime1"}` → `{text:"10/25/2026",update:true,where:"footer"}`,
  `shape.action {"on":"click|hover","action":"none|next|previous|first|last|lastViewed|endShow|playMedia|slide|url|customShow|program","slide","url","tooltip"}` (on the selected shape), `slide.rename {"name","index"}`, `slide.reset`, `slide.colorAt {"x","y"}` → `{color:"16324F",alpha}` (eyedropper: a quick way to verify a master element without rendering).
  Sections: `section.add {"name","at"}` → `{sections:N}`, `section.rename {"index","name"}`, `section.move {"index","to"}`, `section.remove`, `section.removeAll`. `design.ideas {"slide"}` returned `[]` headless; `design.applyIdea {"id"}` untested.
- **Masters:** **`view.slideMaster {"master":0}` opens the master itself** (`{kind:"master"}`; without it the current layout opens). A rect inserted there and filled (`#16324F` bar at the bottom) was read back from the rendered slide with `slide.colorAt {"x":10,"y":520}` → `16324F`, i.e. it shows on every slide whose layout shows master graphics. `view.notesMaster` / `view.handoutMaster` → `{created:true}` (create the master on first use), `notes.placeholders {…}` / `handout.placeholders {…}` (flags for header, date, slideImage, body, footer, pageNumber), `view.closeMaster`.
- **Pictures:** `picture.artisticEffect {"effect":"artisticPencilGrayscale|artisticBlur|artisticLineDrawing|artisticFilmGrain|artisticCutout|artisticGlowEdges|artisticPhotocopy|none"}`, `picture.recolors {}` → list of presets (`none, grayscale, sepia, washout, bw25, bw50…`), `picture.transparentColor {"color":"#FFFFFF"}` or `{"at":[x,y]}`.
- **Files:** `file.properties {"title","subject","author","keywords","comments","category","company"}`, `file.info {}` → `{title,path,format,dirty,slides,hiddenSlides,sections,properties}`, `file.templates {}` → the six starter decks with slide counts (Briefing 5 …), `file.saveTemplate {"path":"t.potx"}` → `{bytes}`, `file.saveAs {"path"}`, `file.recovery.list` → `[{uid,path,title,saved}]`, `design.browseTheme {"path"}` (apply a .pptx/.potx master or .thmx theme), `master.deleteLayout`.
- **Side effect to know:** `review.addToDictionary {"word"}` writes `~/.local/share/deckcraft/dictionaries/user.dic` (the user's real dictionary, not undoable): do not run it as a test (I removed the file my test created). `review.dictionary {}` → `{available,folders}` lists hunspell search folders.
- Not run: media playback commands (`media.play/pause/seek/info/posterFrame/gifPlay`: need a video/audio file open in a live window), `show.fromCurrent`, `design.applyIdea`, `file.recovery.open/discard`, `file.revert`, `font.add/rescan`, `insert.symbol`, `review.thesaurus/accept/endCompare`.

## Text editing, character formats, arranging, media, navigation and data commands (verified headless, 0.11.1)

> **Versions:** 0.11.1 only (2026-10-25); not run on 0.10.0. Test audio was a generated 1-second tone.

- **Character formats** (inside `text.edit`, on a selection; return `null`): `format.italic {"on":true}`, `format.underline {"on":true,"style":"sng|dbl|heavy|dotted|dash|wavy"}`, `format.strikethrough {"on":true,"double":true}`, `format.superscript|subscript {"on"}`, `format.caps {"caps":"none|small|all"}`, `format.textTransparency {"value":0.3}` (0 opaque, 1 invisible), `format.font {"family":"Georgia"}`, `format.shrink`, `format.clear`, `format.fontDialog {"family","size","bold","italic","underline","color","strike"}`, `format.rtl {"on"}`;
  `format.state {}` → the effective formatting at the selection (`{align,bold,italic,font,fontRef,lang,lineSpacing,…}`), `format.ruler {}` → `{x,y,width,marginLeft,indent,tabs:[{pos,align}],defaultTab:72}`, paragraph: `format.alignLeft|alignCenter|alignRight|justify|outdent`, `format.paragraphDialog {"align":"justify|justLow|distributed","indentLeft","indentRight","special":"firstLine|hanging|none"}`, `format.painter {"sticky"}` + `format.painterApply {"ids"}`.
- **Moving through text:** `text.edit {"at":[p,c]}`, `text.selectWord {"at"}`, `text.selectParagraph {"at"}`, `text.move {"to":"left|right|up|down|wordLeft|wordRight|lineStart|lineEnd|paraStart|paraEnd|…"}` → `{caret:[0,41],lineEnd:true}`, `text.delete {"dir":"backward|forward|wordBackward|wordForward"}`, `text.autocorrect {"on":true}` → the whole AutoCorrect table (`teh`→`the`, `recieve`→`receive`, …; `add:[[from,to]]` extends it), `text.compose/commit` (input-method composition).
- **Edit and selection:** `edit.duplicate {"ids"}` → `{ids:[263]}`, `edit.selectAll` → `{ids:[…]}`, `edit.copy` → `{html,text}` (empty for a shape), `edit.paste {"text"|"html"}` → `{id}` (a pasted copy of the selected shape), `edit.pasteSpecial {"as":"keepSource|destinationTheme|picture|text"}` → `{ids}`, `edit.delete` → `{deleted:1}`, `edit.undo/redo` → `{label:"Paste"}`, `edit.deselect`; `selection.hideAll/showAll` (selection pane visibility), `selection.select {"ids"|"id","toggle","add"}`.
- **Arranging:** `arrange.group` → `{id}`, `arrange.ungroup` → `{ids}`, `arrange.regroup` → `{id}` (a NEW group id each time), `arrange.rotateRight|rotateLeft|flipHorizontal|flipVertical` (on a group too), `arrange.sendToBack|bringForward|sendBackward`.
- **Tables:** `table.insertColumnLeft|insertColumnRight {"col"}`, `table.deleteColumn {"col"}`, `table.distributeColumns`, `table.selectCells {"from":[0,0],"to":[1,1]}`, `table.eraseLine {"at":[x,y]}`.
- **Media** (verified with a WAV): `insert.audio {"path","rect"}` → `{id,contentType,durationMs:1000,probe:{audio:{channels,codec}}}`; `media.info {}` → `{bytes,name,durationMs,options,probe}`; `media.options {"autoplay":true,"loop":true,"volume":0.5,"trimStart":100,"trimEnd","rewind","acrossSlides","hide","fullScreen"}`; `media.seek {"ms"}`, `media.toggle`, `media.pause`, `media.stop` (each returns `{id}`); **`media.posterFrame` refuses audio ("only videos have poster frames")**, `media.gifPlay {"play"}` is for GIF pictures. Playback itself is only audible/visible in the live window.
- **Slides and animation:** `slide.first|next|previous|last` → `{index}`, `slide.selectSlides {"indices":[0,1]}` → `{selected:[ids]}`, `animation.set {"effect":"fade","class":"entrance"}` → `{count:1}` (on the selected shape), `animation.clear`, `animation.painterApply`; `comment.add {"text","x","y"}` → `{index}`, **`comment.next` returned the first comment twice and `comment.prev` said "no more comments"** (the walk state is not kept between calls in a headless run): read `comment.list` instead.
- **Data and discovery:** `file.render {"slide":0,"scale":0.3}` → `{png:<base64>,width,height}`, `file.saveBytes {"format":"pptx|deckcraft"}` → `{data:<base64>,bytes}`, `file.openBytes {"name","data"}`, `design.variants {}` → the current theme's four colour variants (`{current,theme,variants:[{colors:[hex…]}]}`), `commands.list {"filter":"media."}` → `[{id,label,params,enabled,disabled_reason:"nothing selected"}]` (tells you why a command is unavailable), `shape.presets {}` → `[{name,label,category}]` (the shape gallery), `font.rescan {}` → `{faces:601,families:236}`, `picture.compress {"ppi":96,"all":true}` → `{pictures,before,after}`.
- Not run: video files, `media.posterFrame` on a video, `file.recovery.*`, `window.next`, input-method composition, `review.accept/endCompare` outside a compare, the point-editing commands on a real freeform (`shape.movePoint/moveHandle/pointType/deletePoint`).

## Ink in DeckCraft (what is and is not possible headless, 0.11.1)

> **Versions:** 0.11.1 (2026-10-25).

- DeckCraft has ONE ink command: `draw.inkToShape {}` → `{shapes:[ids],kept:n}` ("turns recognisable ink strokes on the slide into lines, rectangles, ellipses and triangles"; `{"shapes":[],"kept":0}` on a slide without ink). There is **no `draw.stroke`, `draw.pen` or lasso command** (`unknown command`): ink strokes come only from pointer input in the live window (the control channel offers `ui.drag {x,y,…}` and `ui.pointer {events}`) or from a file that already contains ink.
- `ui.screenshot` answers "no frame was presented (screen locked or window hidden); use ui.render" when the window is not visible; `ui.render {"path"}` then renders only the SLIDE (960×540), not the ribbon, so pen selection and drawing through the UI need the window visible and the screen unlocked.

## Version note (2026-10-25)

App/CLI 0.11.1 added 6 commands (`shape.openPath/closePath/deleteSegment/segmentType`, `slide.reuseList`, `review.reject`); none removed. The full-deck recipe
(select chart → `chart.options`, accessibility check, `.pptx` round trip with a hidden slide) behaved identically on 0.10.0 and 0.11.1.

## Alignment and redo (verified headless, 0.11.1, 2026-10-26; render looked at)
> **Versions:** 0.11.1.
- `format.alignLeft`, `format.alignCenter`, `format.alignRight` (no parameters) act on the selected text or shapes: after `insert.textBox` the new box is selected, so `--cmd 'insert.textBox={"text":"Right aligned","rect":[100,100,800,100]}' --cmd format.alignRight` right-aligned the text inside its 800-point-wide box (render: it sat at the right end), `alignCenter` centred and `alignLeft` left-aligned it.
- **`insert.textBox` takes `rect: [x,y,w,h]` in points of a 960×540 slide** (the PNG export is 1920×1080). `x`, `y`, `width`, `height` are ignored: two boxes without `rect` were stacked at the default position and overlapped, and `rect:[1,1,6,1]` made a 6-point-wide box that wrapped one letter per line.
- `edit.undo` then `edit.redo` in one `run` both succeed (a text box added and removed again, then restored).

## The last 28 command ids (2026-10-26, 0.11.1, headless; smoke test)
> **Versions:** 0.11.1 only, CLI only. Each id ran with `deckcraft-cli run --cmd … --save` on a slide holding the objects it needs; `info` of the saved file differed from the same script without the command (`info` also reflects the current slide, so a difference proves little for the navigation commands). **Smoke test only: effects were not rendered.**
- **Ran (26):**

```
arrange.bringForward arrange.flipHorizontal arrange.flipVertical arrange.rotateLeft arrange.sendBackward edit.cut
edit.pasteText file.adopt format.justify format.outdent format.subscript review.endCompare review.replaceWord
selection.showAll shape.addPoint shape.deletePoint shape.moveHandle shape.pointType shape.setDefault slide.last
slide.next slide.previous smartArt.demote smartArt.removeNode table.insertColumnRight text.commit
```
- **Setups:** shapes for the `arrange.*` and `shape.setDefault` commands (`shape.insert {"preset":"rect","rect":[x,y,w,h],"text"}` twice; they act on the selected shapes); `insert.textBox` + `text.edit {"at":[0,0]}` + `text.selectAll` for `format.justify|outdent|subscript`, `edit.pasteText {"text"}`, `review.replaceWord {"with"}`, `text.commit {"text"}`; `shape.freeform {"points":[…],"closed":true}` + `shape.editPoints {"on":true}` for `shape.addPoint {"path":0,"segment":1,"t":0.5}`, `shape.deletePoint {"path":0,"index":1}`, `shape.pointType {"path":0,"index":1,"type":"smooth"}`; **`shape.moveHandle {"path":0,"index":1,"side":"out","x","y"}` needs the point to be smooth first** ("that side of the point has no handle"); `insert.smartArt {"kind":"list","items":["A","\tB","C"]}` for `smartArt.demote {"index":2}` and `smartArt.removeNode {"index":1}`; three slides + `slide.first` for `slide.next|previous|last`; `insert.table` for `table.insertColumnRight {"col":0}`; **`review.endCompare` needs a running compare** (`review.compare {"path":other.deckcraft}` first; "not comparing" otherwise); `edit.cut {}` (scope slides optional), `file.adopt {"path"}` opens a file like `file.open`.
- **Refused:** `file.recovery.discard` (no recovery folder is set); `file.recovery.save` (no recovery folder is set) (an app setting, not a parameter: the desktop app sets a recovery folder).

## Board deck from sample data: charts, axis, alt text (2026-10-27, 0.11.1 headless; every slide rendered and looked at)
> **Versions:** 0.11.1 only. Task: a 7-slide board review (native charts, 60-30-10 palette, notes) from invented sample data, built by one `deckcraft-cli run` script.
- The CLI is `~/AppImages/deckcraft-cli` and is **not on PATH**: `export PATH=$HOME/AppImages:$PATH`.
- **60-30-10 palette**: `design.colors` with `lt2` = background (60%), `dk1/dk2/accent1` = navy for text, cards and chart bars (30%), `accent2` = orange used only for key-metric text boxes (10%); `design.background {"color","all":true}` last. SmartArt then colours its three boxes accent1, accent2, accent3 (the orange one looks like emphasis).
- **No axis control**: there is no command for axis minimum, number format or label format (`chart.options` has title, legend, dataLabels, gridlines, textColor only). The renderer starts the value axis above zero when the data are close together (revenue 118k to 125k drew from 116,000; CAC 396 to 450 from 390) but at 0 for churn 3.1 to 4.2. A truncated axis exaggerates changes: say so in a caption on the slide and in the notes. Data labels show raw numbers (`120000`, no `$`), so put the unit in the chart title.
- `chart.options {"textColor":"#16324F","gridlines":false,"legend":null,"dataLabels":true,"title":…}` right after `insert.chart` works without `edit.select` (the new chart is selected); `textColor` removes the bluish default tint.
- Big-number callouts: `insert.textBox {"rect"}` then `format.size`, `format.bold`, `format.color` straight after it (the new box is selected) worked for whole-box formatting.
- **Table font size**: after the `text.set` cells, `edit.select {"ids":[tableId]}` then `format.size {"size":22}` resized the whole table text. Setting it before `text.set` did nothing. For a placeholder body use `text.edit {"id","at":[0,0]}`, `text.selectAll`, `format.size {"size":32}`, `text.exit` (the render grew and the third bullet wrapped); `edit.select` + `format.size` on a placeholder showed no change.
- **`shape.altText {"text","ids"}` needs the slide that holds the shape to be current** (`slide.go {"index"}` first); otherwise "no such shape" and `run` saves nothing. Ids to use are the ones `review.accessibility` reports for the saved file. All four flags (3 charts, 1 SmartArt) cleared; `review.accessibility` → `[]`.
- Speaker notes: `slide.notes {"text","index"}` after deleting the initial blank slide; `info` of the `.pptx` shows each slide's `notes` before its `title` (alphabetical keys), so the order is not shifted. A `.pptx` round trip kept all 7 notes, charts, table and SmartArt.

## Log

- 2026-10-25: first verified run on Linux (0.10.0): headless run/save/convert/render/info, live new/slide/shape/table/chart/
  save/export/screenshot with the Pitch starter. Reference reading: artcraft-skills `deckcraft` (macOS, MIT).
- 2026-10-25 (2): themes, animation, transition, picture, notes, outline import, notes/handout PDF, GIF, pptx round trip verified headless.
- 2026-10-25 (3): full deck build (text, table cells, chart options, link, background, slide management, sections, accessibility) verified headless incl. pptx round trip.
- 2026-10-26: SmartArt, text builds, auto-advance timing, align/distribute/group, picture crop/adjust/style, custom master layout verified headless.
- 2026-10-25 (4): brand theme colours/fonts, header/footer, chart types, table style/merge/borders, connectors, shape effects/merge, icon/WordArt/audio, comments, spelling, compare, custom show, slide links, morph verified.
- 2026-10-25 (5): three build sequences re-run on 0.10.0 and 0.11.1 (identical except default chart text tint); version labels added per section.
- 2026-10-25 (6): live control channel re-tested on the 0.11.1 app (edits, screenshot, PDF export).
- 2026-10-25 (7): 45 SmartArt layouts rendered, animation/transition catalogues, animation edit commands + pptx round trip, transition sound/timing/applyAll, layout-level master editing verified headless on 0.11.1.
- 2026-10-25 (8): shape formatting/freeform points, text and paragraph formatting, table cell commands, photo album, action buttons/zoom/slide actions, sections, slide/notes/handout masters, artistic picture effects, file properties/templates verified headless on 0.11.1.
- 2026-10-25 (9): character formats, text movement, edit/selection helpers, arrange, table columns, audio media options, slide navigation, render/saveBytes and command discovery verified headless on 0.11.1.
- 2026-10-25 (10): ink: only `draw.inkToShape` exists; strokes need pointer input in a visible window.
- 2026-10-26: gap round: format.alignLeft/Center/Right, edit.redo, textBox rect units.
- 2026-10-26: the last 28 command ids run with their setups (smoke test).
- 2026-10-27: board deck from invented sample data (3 native charts, table, SmartArt, notes, alt text, 60-30-10 palette); chart-axis gap recorded.
