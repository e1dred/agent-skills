# DeckCraft reference: SmartArt, animation and masters

Part of the deckcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## SmartArt, grouping, pictures, layouts (verified headless)


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

## SmartArt layouts, animation and transition catalogues, master editing (verified headless; renders checked)


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
