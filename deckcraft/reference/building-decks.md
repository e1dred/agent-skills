# DeckCraft reference: building decks

Part of the deckcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## More recipes (verified headless)


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

## Building a real deck (verified headless)

> Default chart text (title, axes, legend) is drawn in a bluish theme tint, not neutral grey. Set an explicit chart text colour if you need grey.

One `run` built title + bullets + table + chart + text box + link + background + duplicate/move/hide + section, then
`convert` to `.pptx` and `render` (checked: table, chart, formatting, background and the hidden slide all survived).

1. **Find shape ids first.** `slide.inspect {"index":0}` (`run … --print` shows the JSON) lists shapes with `id`, `kind`, `name`
   (`Title 1`, `Subtitle 2`). A fresh `file.new` slide 0 has title id 258 / subtitle 259, but always read them.
2. **Text**: `text.set {"id":258,"text":"Q3 Review"}`. For a table cell: `text.set {"text":"North","cell":[1,0]}` (row, col; acts on the
   just-inserted/selected table, or pass `id`). Bullets: `\n` separates paragraphs, a leading `\t` indents a level.
3. **Select, then format.** `format.size/bold/italic/color/alignCenter/bullets/font` act on the *selection* (inserting a shape
   selects it; otherwise `edit.select {"ids":[266]}` → `{"selected":[266]}`). Chart/alt-text commands also need a selection or `ids`:
   `chart.options` fails with "nothing selected" when no chart is selected (a chart you just inserted is selected, see the board-deck note below).
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

## Next-tier workflows (verified headless; render checked)

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

## Board deck from sample data: charts, axis, alt text (2026-10-27, 0.11.1 headless; every slide rendered and looked at)
> Task: a 7-slide board review (native charts, 60-30-10 palette, notes) from invented sample data, built by one `deckcraft-cli run` script.
- The CLI is `~/AppImages/deckcraft-cli` and is **not on PATH**: `export PATH=$HOME/AppImages:$PATH`.
- **60-30-10 palette**: `design.colors` with `lt2` = background (60%), `dk1/dk2/accent1` = navy for text, cards and chart bars (30%), `accent2` = orange used only for key-metric text boxes (10%); `design.background {"color","all":true}` last. SmartArt then colours its three boxes accent1, accent2, accent3 (the orange one looks like emphasis).
- **No axis control**: there is no command for axis minimum, number format or label format (`chart.options` has title, legend, dataLabels, gridlines, textColor only). The renderer starts the value axis above zero when the data are close together (revenue 118k to 125k drew from 116,000; CAC 396 to 450 from 390) but at 0 for churn 3.1 to 4.2. A truncated axis exaggerates changes: say so in a caption on the slide and in the notes. Data labels show raw numbers (`120000`, no `$`), so put the unit in the chart title.
- `chart.options {"textColor":"#16324F","gridlines":false,"legend":null,"dataLabels":true,"title":…}` right after `insert.chart` works without `edit.select` (the new chart is selected); `textColor` removes the bluish default tint.
- Big-number callouts: `insert.textBox {"rect"}` then `format.size`, `format.bold`, `format.color` straight after it (the new box is selected) worked for whole-box formatting.
- **Table font size**: after the `text.set` cells, `edit.select {"ids":[tableId]}` then `format.size {"size":22}` resized the whole table text. Setting it before `text.set` did nothing. For a placeholder body use `text.edit {"id","at":[0,0]}`, `text.selectAll`, `format.size {"size":32}`, `text.exit` (the render grew and the third bullet wrapped); `edit.select` + `format.size` on a placeholder showed no change.
- **`shape.altText {"text","ids"}` needs the slide that holds the shape to be current** (`slide.go {"index"}` first); otherwise "no such shape" and `run` saves nothing. Ids to use are the ones `review.accessibility` reports for the saved file. All four flags (3 charts, 1 SmartArt) cleared; `review.accessibility` → `[]`.
- Speaker notes: `slide.notes {"text","index"}` after deleting the initial blank slide; `info` of the `.pptx` shows each slide's `notes` before its `title` (alphabetical keys), so the order is not shifted. A `.pptx` round trip kept all 7 notes, charts, table and SmartArt.
