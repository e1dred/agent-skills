# DeckCraft command catalogue (0.16.0)

Built 2026-11-06 from the skill's own text (SKILL.md, reference/ and tools/); no command was run and nothing was re-tested. Ids come from `deckcraft-cli` 0.16.0 (331 ids); the skill's version label: last tested on deckcraft-cli 0.16.0; evidence sections cite 0.11.1-0.16.0.
Status: **V** verified - the hit is under a heading naming verification or records an observed result (arrow, before/after, read-back, checked file, confirmed); **d** documented - named with parameters or usage, no recorded evidence; **n** named only - a bare list or command index; **s** skipped on purpose - the skill says skipped/not run/not tested/not exercised; **x** known no-op, broken or refused - the line says so; **V+** verified, but another line records a limit (refused or skipped in some state or version); the note quotes both. When a command has verified evidence anywhere, it counts as verified: a refusal or skip recorded elsewhere usually names a precondition or an older round.
Counts: V 303, V+ 13, d 1, n 1, s 13, x 0.

## animation (11)

| id | status | note |
|---|---|---|
| `animation.add` | V | reference/building-decks.md#More recipes (verified headles…: …imation: `animation.add {"effect":"fade",… |
| `animation.clear` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ed shape), `animation.clear`, `animation.pa… |
| `animation.get` | V | reference/building-decks.md#More recipes (verified headles…: `animation.get` lists them |
| `animation.list` | V | reference/building-decks.md#More recipes (verified headles…: `animation.list` shows every effect. |
| `animation.move` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: `animation.move {"index","to"}`, `animation… |
| `animation.options` | V | reference/newer-commands.md#0.14 changes (verified headles…: …ids"}` and `animation.options {"index","pat… |
| `animation.painter` | s | reference/smartart-animation-masters.md#SmartArt layouts, …: …lso listed, not run: `design.ideas`/`applyI… |
| `animation.painterApply` | V | reference/shapes-text-tables.md#Text editing, character fo…: …on.clear`, `animation.painterApply` |
| `animation.remove` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …option"}`, `animation.remove {"index"}` |
| `animation.set` | V | reference/log.md#Log: …e Theme" is refused) and `animation.add` rejected `fadeIn`.- 2026-11-01: CLI refre… |
| `animation.timing` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …x","to"}`, `animation.timing {"index","star… |

## arrange (15)

| id | status | note |
|---|---|---|
| `arrange.align` | V | reference/building-decks.md#More recipes (verified headles…: `arrange.align {"edge":"center"}`. |
| `arrange.bringForward` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …e. (5): `arrange.bringForward` `{"ids": … |
| `arrange.bringToFront` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: Arrange: `arrange.bringToFront\|sendToBack\|b… |
| `arrange.distribute` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …→ `{ids}`, `arrange.distribute {"dir":"hori… |
| `arrange.flipHorizontal` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `arrange.flipHorizontal` `{"ids": [260]}` (… |
| `arrange.flipVertical` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `arrange.flipVertical` `{"ids": [260]}` (he… |
| `arrange.group` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ranging: `arrange.group` → `{id}`, `arran… |
| `arrange.nudge` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …\|regroup`, `arrange.nudge {"dx":6,"dy":0}` … |
| `arrange.regroup` | V | reference/shapes-text-tables.md#Text editing, character fo…: …→ `{ids}`, `arrange.regroup` → `{id}` (a NE… |
| `arrange.reorder` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …y = 6 pt), `arrange.reorder {"id","index"}`… |
| `arrange.rotateLeft` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `arrange.rotateLeft` `{"ids": [277]}` (live… |
| `arrange.rotateRight` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ach time), `arrange.rotateRight\|rotateLeft\|… |
| `arrange.sendBackward` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `arrange.sendBackward` `{"ids": [277]}` (li… |
| `arrange.sendToBack` | V | reference/shapes-text-tables.md#Text editing, character fo…: …roup too), `arrange.sendToBack\|bringForward… |
| `arrange.ungroup` | V | reference/shapes-text-tables.md#Text editing, character fo…: … → `{id}`, `arrange.ungroup` → `{ids}`, `ar… |

## chart (3)

| id | status | note |
|---|---|---|
| `chart.data` | V | reference/building-decks.md#Building a real deck (verified…: …:"line"}`, `chart.data {"categories","serie… |
| `chart.options` | V+ | reference/building-decks.md#Building a real deck (verified…: …` it, then `chart.options {"title":"Sales b… · limit: building-decks.md: `chart.options` fails with "nothing selected" when no chart … |
| `chart.type` | V | reference/building-decks.md#Building a real deck (verified…: `chart.type {"type":"line"}`, `chart.data {… |

## commands (1)

| id | status | note |
|---|---|---|
| `commands.list` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ex…]}]}`), `commands.list {"filter":"media.… |

## comment (7)

| id | status | note |
|---|---|---|
| `comment.add` | V | reference/building-decks.md#Next-tier workflows (verified …: … review: `comment.add {"text","x","y"}` →… |
| `comment.delete` | V | reference/building-decks.md#Next-tier workflows (verified …: …ent.list`, `comment.delete {"index"\|"all":t… |
| `comment.list` | V | reference/building-decks.md#Next-tier workflows (verified …: …d":true}`, `comment.list`, `comment.delete … |
| `comment.next` | V | reference/shapes-text-tables.md#Text editing, character fo…: …index}`, `comment.next` returned the firs… |
| `comment.prev` | V | reference/shapes-text-tables.md#Text editing, character fo…: … twice and `comment.prev` said "no more com… |
| `comment.reply` | V | reference/building-decks.md#Next-tier workflows (verified …: …`{index}`, `comment.reply {"index","text"}`… |
| `comment.resolve` | V | reference/building-decks.md#Next-tier workflows (verified …: …,"text"}`, `comment.resolve {"index","resol… |

## design (14)

| id | status | note |
|---|---|---|
| `design.applyIdea` | V+ | reference/shapes-text-tables.md#Shapes, text formatting, t…: `design.applyIdea {"id"}` untested. · limit: shapes-text-tables.md: Not run … - Not run: media playback commands (`media.play/pause/seek/i… |
| `design.background` | V | reference/building-decks.md#Building a real deck (verified…: …kground: `design.background {"color":"#F4… |
| `design.browseTheme` | V+ | reference/shapes-text-tables.md#Shapes, text formatting, t…: …,saved}]`, `design.browseTheme {"path"}` (a… · limit: smartart-animation-masters.md: …lso listed, not run: `design.ideas`/`applyIdea`, `view.hando… |
| `design.colors` | V | reference/building-decks.md#Next-tier workflows (verified …: …d theme: `design.colors {"name":"Brand","… |
| `design.effects` | s | reference/smartart-animation-masters.md#SmartArt layouts, …: …lso listed, not run: `design.ideas`/`applyI… |
| `design.fonts` | V | reference/building-decks.md#Next-tier workflows (verified …: `design.fonts {"name":"Brand fonts","major"… |
| `design.headerFooter` | V | reference/building-decks.md#Next-tier workflows (verified …: … number: `design.headerFooter {"slideNumb… |
| `design.hideBackgroundGraphics` | s | reference/smartart-animation-masters.md#SmartArt layouts, …: …lso listed, not run: `design.ideas`/`applyI… |
| `design.ideas` | V+ | reference/shapes-text-tables.md#Shapes, text formatting, t…: `design.ideas {"slide"}` returned `[]` head… · limit: smartart-animation-masters.md: …lso listed, not run: `design.ideas`/`applyIdea`, `view.hando… |
| `design.slideSize` | V | reference/building-decks.md#Building a real deck (verified…: …x":0..3}`, `design.slideSize {"preset":"wid… |
| `design.theme` | V+ | reference/building-decks.md#More recipes (verified headles…: …Theme: `design.theme {"name":"Harbor"}`… · limit: log.md: `design.theme` needs a name from `design.themes` ("Office Th… |
| `design.themes` | V+ | reference/building-decks.md#More recipes (verified headles…: …(list with `design.themes`) · limit: log.md: … name from `design.themes` ("Office Theme" is refused) and `… |
| `design.variant` | V | reference/building-decks.md#Building a real deck (verified…: …,"at":1}`, `design.variant {"index":0..3}`,… |
| `design.variants` | V | reference/shapes-text-tables.md#Text editing, character fo…: …,"data"}`, `design.variants {}` → the curre… |

## document (1)

| id | status | note |
|---|---|---|
| `document.inspect` | V | SKILL.md#Command formats (verified): …s, boxes), `document.inspect` (needs an open deck) \| |

## draw (1)

| id | status | note |
|---|---|---|
| `draw.inkToShape` | V | reference/shapes-text-tables.md#Ink in DeckCraft (what is …: …k command: `draw.inkToShape {}` → `{shapes:… |

## edit (12)

| id | status | note |
|---|---|---|
| `edit.copy` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ids:[…]}`, `edit.copy` → `{html,text}` (emp… |
| `edit.cut` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …t. (2): `edit.cut` `{"scope": "slides"}`… |
| `edit.delete` | V | reference/shapes-text-tables.md#Text editing, character fo…: …→ `{ids}`, `edit.delete` → `{deleted:1}`, `… |
| `edit.deselect` | V | reference/shapes-text-tables.md#Text editing, character fo…: …"Paste"}`, `edit.deselect` |
| `edit.duplicate` | V | reference/shapes-text-tables.md#Text editing, character fo…: …lection: `edit.duplicate {"ids"}` → `{ids… |
| `edit.paste` | V | reference/shapes-text-tables.md#Text editing, character fo…: … a shape), `edit.paste {"text"\|"html"}` → `… |
| `edit.pasteSpecial` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ed shape), `edit.pasteSpecial {"as":"keepSo… |
| `edit.pasteText` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `edit.pasteText` `{"text": "Pasted "}` (hea… |
| `edit.redo` | V | reference/shapes-text-tables.md#Alignment and redo (verifi…: …undo` then `edit.redo` in one `run` both su… |
| `edit.select` | V | reference/building-decks.md#Building a real deck (verified…: otherwise `edit.select {"ids":[266]}` → `{"… |
| `edit.selectAll` | V | reference/shapes-text-tables.md#Text editing, character fo…: …s:[263]}`, `edit.selectAll` → `{ids:[…]}`, … |
| `edit.undo` | V | reference/shapes-text-tables.md#Text editing, character fo…: …leted:1}`, `edit.undo/redo` → `{label:"Past… |

## file (19)

| id | status | note |
|---|---|---|
| `file.adopt` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …e. (1): `file.adopt` `{"path": "base.dec… |
| `file.close` | V | reference/log.md#Log: … ui.render, file.close); `ui.screenshot` refused (window hidden), `ui.render` work… |
| `file.export` | V | SKILL.md#Command formats (verified): \| export \| `file.export {"path":…,"format"?,"all"?:true,"slide"?,"s… |
| `file.info` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ompany"}`, `file.info {}` → `{title,path,fo… |
| `file.new` | V | SKILL.md#Command formats (verified): …new deck \| `file.new` (blank) or `file.new {"template":"Pitch"}` (s… |
| `file.open` | n | SKILL.md#Traps: …`file.new`/`file.open`. |
| `file.openBytes` | V | reference/shapes-text-tables.md#Text editing, character fo…: …>,bytes}`, `file.openBytes {"name","data"}`… |
| `file.properties` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …Files: `file.properties {"title","subje… |
| `file.recovery.discard` | V+ | reference/command-sweep.md#Verified in detail, DeckCraft s…: …y. (2): `file.recovery.discard` live: `{… · limit: command-sweep.md: Refused … - Refused: `file.recovery.discard` (no recovery folder i… |
| `file.recovery.list` | V | reference/command-sweep.md#Verified in detail, DeckCraft s…: …hat entry (`file.recovery.list` back to []) |
| `file.recovery.open` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |
| `file.recovery.save` | V+ | reference/command-sweep.md#Verified in detail, DeckCraft s…: `file.recovery.save` live (the CLI has no r… · limit: command-sweep.md: Refused … `file.recovery.save` (no recovery folder is set) (an app set… |
| `file.render` | V | reference/shapes-text-tables.md#Text editing, character fo…: …scovery: `file.render {"slide":0,"scale":… |
| `file.revert` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |
| `file.save` | V+ | SKILL.md#Command formats (verified): \| save \| `file.save {"path":…}` (format by extension: `.deckcraft`,… · limit: SKILL.md: - Never `file.save` to `.png/.jpg`: it is refused ("saving a… |
| `file.saveAs` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …`{bytes}`, `file.saveAs {"path"}`, `file.re… |
| `file.saveBytes` | V | reference/shapes-text-tables.md#Text editing, character fo…: …,height}`, `file.saveBytes {"format":"pptx\|… |
| `file.saveTemplate` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …fing 5 …), `file.saveTemplate {"path":"t.po… |
| `file.templates` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …perties}`, `file.templates {}` → the six st… |

## font (4)

| id | status | note |
|---|---|---|
| `font.add` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |
| `font.replace` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: … families, `font.replace {"from":"Inter","t… |
| `font.rescan` | V | reference/shapes-text-tables.md#Text editing, character fo…: … command is unavailable), `shape.presets {}… |
| `font.used` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `font.used {}` → families, `font.replace {"… |

## format (47)

| id | status | note |
|---|---|---|
| `format.align` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …tart":3}`, `format.align*`, `format.indent/… |
| `format.alignCenter` | V | reference/shapes-text-tables.md#Alignment and redo (verifi…: …lignLeft`, `format.alignCenter`, `format.al… |
| `format.alignLeft` | V | reference/shapes-text-tables.md#Text editing, character fo…: …paragraph: `format.alignLeft\|alignCenter\|al… |
| `format.alignRight` | V | reference/shapes-text-tables.md#Alignment and redo (verifi…: …gnCenter`, `format.alignRight` (no paramete… |
| `format.anchor` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …bottom"}`, `format.anchor {"anchor":"top\|mi… |
| `format.autofit` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …bottom"}`, `format.autofit {"mode":"none\|sh… |
| `format.bold` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: then `format.bold\|italic\|underline\|striketh… |
| `format.bullets` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: … `{"pt"}`, `format.bullets {"on":true,"char… |
| `format.caps` | V | reference/shapes-text-tables.md#Text editing, character fo…: …t {"on"}`, `format.caps {"caps":"none\|small… |
| `format.case` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …"color"}`, `format.case {"mode":"upper\|lowe… |
| `format.clear` | V | reference/shapes-text-tables.md#Text editing, character fo…: …t.shrink`, `format.clear`, `format.fontDial… |
| `format.color` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …cript {}`, `format.color {"color"}`, `forma… |
| `format.columns` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …resize"}`, `format.columns {"count":2,"spac… |
| `format.direction` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …mat.wrap`, `format.direction`. |
| `format.font` | V | reference/shapes-text-tables.md#Text editing, character fo…: …nvisible), `format.font {"family":"Georgia"… |
| `format.fontDialog` | V | reference/shapes-text-tables.md#Text editing, character fo…: …at.clear`, `format.fontDialog {"family","si… |
| `format.grow` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …{"pt":3}`, `format.grow/shrink`, `format.te… |
| `format.highlight` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …"color"}`, `format.highlight {"color"}`, `f… |
| `format.indent` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …fore: after format.indent: &lt;a:pPr lvl="1"/&gt; |
| `format.italic` | V | reference/shapes-text-tables.md#Text editing, character fo…: …n `null`): `format.italic {"on":true}`, `fo… |
| `format.justify` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …t. (3): `format.justify` (headless) befo… |
| `format.language` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …preset"}`, `format.language`, |
| `format.languageAll` | d | reference/newer-commands.md#Newer commands: - `format.languageAll {"lang":"fr-FR","noProof"?}` sets the … |
| `format.lineSpacing` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …pacing"}`, `format.lineSpacing {"lines":1.5… |
| `format.margins` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: Box: `format.margins {"left","top","right",… |
| `format.numbering` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …,"size"}`, `format.numbering {"on":true,"sc… |
| `format.outdent` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `format.outdent` (headless) before: after f… |
| `format.painter` | V | reference/shapes-text-tables.md#Text editing, character fo…: …g\|none"}`, `format.painter {"sticky"}` + `f… |
| `format.painterApply` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ticky"}` + `format.painterApply {"ids"}`. |
| `format.paragraph` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: paragraph: `format.paragraph {"align":"just… |
| `format.paragraphDialog` | V | reference/shapes-text-tables.md#Text editing, character fo…: …\|outdent`, `format.paragraphDialog {"align"… |
| `format.rtl` | V | reference/shapes-text-tables.md#Text editing, character fo…: …strike"}`, `format.rtl {"on"}` |
| `format.ruler` | V | reference/shapes-text-tables.md#Text editing, character fo…: …cing,…}`), `format.ruler {}` → `{x,y,width,… |
| `format.shrink` | V | reference/shapes-text-tables.md#Text editing, character fo…: …eorgia"}`, `format.shrink`, `format.clear`,… |
| `format.size` | V | reference/building-decks.md#More recipes (verified headles…: `format.size/bold/font/color` act on the se… |
| `format.spacing` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …\|cycle"}`, `format.spacing {"pt":3}`, `form… |
| `format.state` | V | reference/shapes-text-tables.md#Text editing, character fo…: `format.state {}` → the effective formattin… |
| `format.strikethrough` | V | reference/shapes-text-tables.md#Text editing, character fo…: …h\|wavy"}`, `format.strikethrough {"on":true… |
| `format.subscript` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `format.subscript` (headless) before: run p… |
| `format.superscript` | V | reference/shapes-text-tables.md#Text editing, character fo…: …e":true}`, `format.superscript\|subscript {"… |
| `format.tabs` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …/outdent`, `format.tabs`. |
| `format.textOutline` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …w {"on"}`, `format.textOutline {"color","wi… |
| `format.textShadow` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …w/shrink`, `format.textShadow {"on"}`, `for… |
| `format.textTransparency` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ll\|all"}`, `format.textTransparency {"value… |
| `format.textWarp` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …"width"}`, `format.textWarp {"preset"}`, `f… |
| `format.underline` | V | reference/shapes-text-tables.md#Text editing, character fo…: …n":true}`, `format.underline {"on":true,"st… |
| `format.wrap` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ing":18}`, `format.wrap`, `format.direction… |

## guide (4)

| id | status | note |
|---|---|---|
| `guide.add` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: Guides: `guide.add {"vertical":true,"pos":4… |
| `guide.delete` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …","pos"}`, `guide.delete {"index"}`. |
| `guide.list` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …`{index}`, `guide.list` → `[{pos,vertical}]… |
| `guide.move` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …rtical}]`, `guide.move {"index","pos"}`, `g… |

## handout (1)

| id | status | note |
|---|---|---|
| `handout.placeholders` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ers {…}` / `handout.placeholders {…}` (flag… |

## insert (18)

| id | status | note |
|---|---|---|
| `insert.actionButton` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `insert.actionButton {"kind":"home\|back\|for… |
| `insert.audio` | V | reference/building-decks.md#Next-tier workflows (verified …: …Audio: `insert.audio {"path":"tone.wav"… |
| `insert.chart` | V | SKILL.md#Command formats (verified): \| chart \| `insert.chart {"type":"column\|bar\|line\|pie\|…","rect":[…],… |
| `insert.dateTime` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …deNumber`, `insert.dateTime {"format":"date… |
| `insert.hyperlink` | V | reference/building-decks.md#Building a real deck (verified…: Link: `insert.hyperlink {"url":"https:/… |
| `insert.icon` | V | reference/building-decks.md#Next-tier workflows (verified …: `insert.icon {"name":"star","rect":[…]}` (`… |
| `insert.icons` | V | reference/building-decks.md#Next-tier workflows (verified …: …ct":[…]}` (`insert.icons` lists them), `ins… |
| `insert.photoAlbum` | V+ | reference/shapes-text-tables.md#Shapes, text formatting, t…: … extras: `insert.photoAlbum {"pictures":[… · limit: smartart-animation-masters.md: …lso listed, not run: `design.ideas`/`applyIdea`, `view.hando… |
| `insert.photoAlbumEdit` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ne slide), `insert.photoAlbumEdit` |
| `insert.picture` | V | reference/building-decks.md#More recipes (verified headles…: …Picture: `insert.picture {"path":"pic.png… |
| `insert.slideNumber` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …nToZoom}`, `insert.slideNumber`, `insert.da… |
| `insert.smartArt` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …martArt: `insert.smartArt {"kind":"proces… |
| `insert.symbol` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |
| `insert.table` | V | SKILL.md#Command formats (verified): \| table \| `insert.table {"rows":3,"cols":2,"rect":[…]}` \| |
| `insert.textBox` | V | reference/building-decks.md#Building a real deck (verified…: …ext box: `insert.textBox {"rect":[x,y,w,h… |
| `insert.video` | V | reference/building-decks.md#Next-tier workflows (verified …: …the slide (`insert.video` is the same shape… |
| `insert.wordArt` | V | reference/building-decks.md#Next-tier workflows (verified …: …sts them), `insert.wordArt {"text","style":… |
| `insert.zoom` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …rendered), `insert.zoom {"kind":"summary\|sl… |

## master (6)

| id | status | note |
|---|---|---|
| `master.deleteLayout` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …mx theme), `master.deleteLayout`. |
| `master.insertLayout` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …,master}`, `master.insertLayout {"name":"My… |
| `master.insertPlaceholder` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: … → `{id}`, `master.insertPlaceholder {"kind… |
| `master.placeholders` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …e":true}`, `master.placeholders {"title":tr… |
| `master.preserve` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …{"name"}`, `master.preserve {"preserve":tru… |
| `master.renameLayout` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: `master.renameLayout/deleteLayout` also exi… |

## media (9)

| id | status | note |
|---|---|---|
| `media.gifPlay` | V | reference/shapes-text-tables.md#Text editing, character fo…: …rames"), `media.gifPlay {"play"}` is for … |
| `media.info` | V | reference/shapes-text-tables.md#Text editing, character fo…: `media.info {}` → `{bytes,name,durationMs,o… |
| `media.options` | V | reference/shapes-text-tables.md#Text editing, character fo…: `media.options {"autoplay":true,"loop":true… |
| `media.pause` | V | reference/shapes-text-tables.md#Text editing, character fo…: …a.toggle`, `media.pause`, `media.stop` (eac… |
| `media.play` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |
| `media.posterFrame` | V+ | reference/shapes-text-tables.md#Text editing, character fo…: `media.posterFrame` refuses audio ("only … · limit: shapes-text-tables.md: Not run … - Not run: video files, `media.posterFrame` on a video, `fil… |
| `media.seek` | V | reference/shapes-text-tables.md#Text editing, character fo…: `media.seek {"ms"}`, `media.toggle`, `media… |
| `media.stop` | V | reference/shapes-text-tables.md#Text editing, character fo…: …ia.pause`, `media.stop` (each returns `{id}… |
| `media.toggle` | V | reference/shapes-text-tables.md#Text editing, character fo…: …k {"ms"}`, `media.toggle`, `media.pause`, `… |

## notes (1)

| id | status | note |
|---|---|---|
| `notes.placeholders` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …irst use), `notes.placeholders {…}` / `hand… |

## picture (12)

| id | status | note |
|---|---|---|
| `picture.adjust` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …ractions), `picture.adjust {"brightness":0.… |
| `picture.artisticEffect` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ictures: `picture.artisticEffect {"effect… |
| `picture.change` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …nce":20}`, `picture.change`, `picture.reset… |
| `picture.compress` | V | reference/shapes-text-tables.md#Text editing, character fo…: … command is unavailable), `shape.presets {}… |
| `picture.crop` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: ….picture`, `picture.crop {"left":0.1,"right… |
| `picture.recolor` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …sts them), `picture.recolor {"preset":"sepi… |
| `picture.recolors` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …y\|none"}`, `picture.recolors {}` → list of … |
| `picture.removeBackground` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …cale\|…"}`, `picture.removeBackground {"tole… |
| `picture.reset` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …e.change`, `picture.reset`. |
| `picture.style` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: `picture.style {"style":"softEdgeOval"}` (`… |
| `picture.styles` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …geOval"}` (`picture.styles` lists them), `p… |
| `picture.transparentColor` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …, bw50…`), `picture.transparentColor {"colo… |

## review (12)

| id | status | note |
|---|---|---|
| `review.accept` | s | reference/shapes-text-tables.md#Text editing, character fo…: Not run … - Not run: video files, `media.posterFrame`… |
| `review.accessibility` | V | reference/building-decks.md#Building a real deck (verified…: …ibility: `review.accessibility` → `[{slid… |
| `review.addToDictionary` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …to know: `review.addToDictionary {"word"}… |
| `review.compare` | V | reference/building-decks.md#Next-tier workflows (verified …: `review.compare {"path":"revised.deckcraft"… |
| `review.dictionary` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `review.dictionary {}` → `{available,folder… |
| `review.endCompare` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `review.endCompare` is proven by `review.re… |
| `review.reject` | V | reference/building-decks.md#Next-tier workflows (verified …: …eads them; `review.reject` only while a com… |
| `review.replaceWord` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `review.replaceWord` `{"with": "us"}` (head… |
| `review.revisions` | V | reference/building-decks.md#Next-tier workflows (verified …: …ide"]}]}` (`review.revisions` re-reads them… |
| `review.spelling` | V | reference/building-decks.md#Next-tier workflows (verified …: `review.spelling` → misspellings with `sugg… |
| `review.spellingChange` | V | reference/building-decks.md#Next-tier workflows (verified …: …eh → the), `review.spellingChange {"shape",… |
| `review.thesaurus` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |

## section (5)

| id | status | note |
|---|---|---|
| `section.add` | V | reference/building-decks.md#Building a real deck (verified…: …ndex":0}`, `section.add {"name":"Body","at"… |
| `section.move` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …,"name"}`, `section.move {"index","to"}`, `… |
| `section.remove` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …x","to"}`, `section.remove`, `section.remov… |
| `section.removeAll` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …n.remove`, `section.removeAll`. |
| `section.rename` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …tions:N}`, `section.rename {"index","name"}… |

## selection (3)

| id | status | note |
|---|---|---|
| `selection.hideAll` | V | reference/command-sweep.md#Verified in detail, DeckCraft s…: …ess: after `selection.hideAll` every shape … |
| `selection.select` | V | reference/shapes-text-tables.md#Text editing, character fo…: …sibility), `selection.select {"ids"\|"id","t… |
| `selection.showAll` | V | reference/command-sweep.md#Verified in detail, DeckCraft s…: …n. (1): `selection.showAll` headless: af… |

## shape (37)

| id | status | note |
|---|---|---|
| `shape.action` | V | reference/newer-commands.md#0.14 changes (verified headles…: …tions from `shape.action`) or `textLink` (a… |
| `shape.addPoint` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `shape.addPoint\|deletePoint\|pointType\|moveH… |
| `shape.adjust` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …{"name"}`, `shape.adjust {"index":0,"value"… |
| `shape.altText` | V | reference/building-decks.md#Building a real deck (verified…: `shape.altText {"text":"…","ids":[266]}` (o… |
| `shape.change` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ion pane), `shape.change {"preset":"hexagon… |
| `shape.closePath` | V | reference/newer-commands.md#New in 0.11.x (verified headle…: … outline), `shape.closePath {"index":0}`, `… |
| `shape.connect` | V | reference/building-decks.md#Next-tier workflows (verified …: …*Shapes: `shape.connect {"from":271,"to":… |
| `shape.deletePoint` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `shape.deletePoint` `{"id": 260, "path": 0,… |
| `shape.deleteSegment` | V | reference/newer-commands.md#New in 0.11.x (verified headle…: …ndex":0}`, `shape.deleteSegment {"index":0,… |
| `shape.editPoints` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …e: enter `shape.editPoints {"on":true}` f… |
| `shape.effects` | V | reference/building-decks.md#Next-tier workflows (verified …: `shape.effects {"ids":[271],"shadow":"outer… |
| `shape.fill` | V | reference/building-decks.md#More recipes (verified headles…: … / text: `shape.fill {"color":"#E07B39"}`… |
| `shape.flip` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: … `{"by"}`, `shape.flip {"axis":"horizontal\|… |
| `shape.freeform` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: ….change`), `shape.freeform {"points":[[x,y]… |
| `shape.insert` | V | SKILL.md#Command formats (verified): \| shape \| `shape.insert {"preset":"roundRect\|star5\|…","rect":[x,y,w… |
| `shape.inspect` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: … → `{id}`, `shape.inspect {}` (box incl. ro… |
| `shape.line` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ius etc.), `shape.line {"color","width","da… |
| `shape.lock` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …rtical"}`, `shape.lock {"locked"}`, `shape.… |
| `shape.merge` | V | reference/building-decks.md#Next-tier workflows (verified …: `shape.merge {"op":"union\|combine\|fragment\|… |
| `shape.move` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …Aspect"}`, `shape.move {"dx","dy"}` or `{"x… |
| `shape.moveHandle` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `shape.moveHandle` `{"id": 260, "path": 0, … |
| `shape.movePoint` | s | reference/shapes-text-tables.md#Text editing, character fo…: Not run … - Not run: video files, `media.posterFrame`… |
| `shape.openPath` | V | reference/newer-commands.md#New in 0.11.x (verified headle…: …n a shape: `shape.openPath {"index":0}` (br… |
| `shape.pointType` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `shape.pointType` `{"id": 260, "path": 0, "… |
| `shape.points` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …rned empty `shape.points` (`{paths:[],…}`) … |
| `shape.presets` | V | reference/shapes-text-tables.md#Text editing, character fo…: … command is unavailable), `shape.presets {}… |
| `shape.quickStyle` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …,"none"}`, `shape.quickStyle {"index":9}` (… |
| `shape.rename` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …turn `1`): `shape.rename {"name"}`, `shape.… |
| `shape.resize` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …"x","y"}`, `shape.resize {"w","h"}`, |
| `shape.rotate` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `shape.rotate {"deg"}` (absolute) or `{"by"… |
| `shape.segmentType` | V | reference/newer-commands.md#New in 0.11.x (verified headle…: …deleted"), `shape.segmentType {"index":0,"s… |
| `shape.setBounds` | V | reference/building-decks.md#More recipes (verified headles…: `shape.setBounds {x,y,w,h,ids?}` |
| `shape.setDefault` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `shape.setDefault` shows on the NEXT insert… |
| `shape.sites` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `shape.sites {"id"}` needs an id. |
| `shape.sizePosition` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …× accent), `shape.sizePosition {"x","y","w"… |
| `shape.smoothCorners` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …exagon"}`, `shape.smoothCorners {"smoothing… |
| `shape.visible` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …locked"}`, `shape.visible {"visible":false}… |

## show (4)

| id | status | note |
|---|---|---|
| `show.customShow` | V | reference/building-decks.md#Next-tier workflows (verified …: …w setup: `show.customShow {"name":"Short"… |
| `show.fromCurrent` | s | reference/shapes-text-tables.md#Shapes, text formatting, t…: Not run … - Not run: media playback commands (`media.… |
| `show.fromStart` | V | reference/building-decks.md#Next-tier workflows (verified …: `show.fromStart` plays (live app). |
| `show.setup` | V | reference/building-decks.md#Next-tier workflows (verified …: …,2]}` then `show.setup {"type":"speaker\|bro… |

## slide (22)

| id | status | note |
|---|---|---|
| `slide.actions` | V | reference/log.md#Log: …e Theme" is refused) and `animation.add` rejected `fadeIn`.- 2026-11-01: CLI refre… |
| `slide.colorAt` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …de.reset`, `slide.colorAt {"x","y"}` → `{co… |
| `slide.delete` | V | reference/building-decks.md#Building a real deck (verified…: …n":true}`, `slide.delete {"index"}`, |
| `slide.duplicate` | V | reference/building-decks.md#Building a real deck (verified…: …*Slides: `slide.duplicate {"index":1}`, `… |
| `slide.first` | V | reference/shapes-text-tables.md#Text editing, character fo…: …imation: `slide.first\|next\|previous\|last`… |
| `slide.fromOutline` | V | reference/building-decks.md#More recipes (verified headles…: … import: `slide.fromOutline {"text":"# Ti… |
| `slide.go` | V | SKILL.md#Command formats (verified): …navigate \| `slide.go {"index":1}` (0-based) \| |
| `slide.hide` | V | reference/building-decks.md#Building a real deck (verified…: …,"to":3}`, `slide.hide {"index":3,"hidden":… |
| `slide.inspect` | V | SKILL.md#Command formats (verified): … inspect \| `slide.inspect {"index"?}` (shapes, ids, boxes), `docume… |
| `slide.last` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …e. (3): `slide.last` (live) before: docu… |
| `slide.layout` | V | reference/building-decks.md#Building a real deck (verified…: `slide.layout {"layout":"title","index":0}`… |
| `slide.move` | V | reference/building-decks.md#Building a real deck (verified…: …ndex":1}`, `slide.move {"from":2,"to":3}`, … |
| `slide.new` | V | SKILL.md#Command formats (verified): \| slide \| `slide.new {"layout":"title\|titleAndContent\|titleOnly\|bla… |
| `slide.next` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `slide.next` (live) before: selection.slide… |
| `slide.notes` | V | SKILL.md#Command formats (verified): \| notes \| `slide.notes {"text":"…","index":2}` \| |
| `slide.previous` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `slide.previous` (live) before: selection.s… |
| `slide.rename` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …ed shape), `slide.rename {"name","index"}`,… |
| `slide.reset` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …"index"}`, `slide.reset`, `slide.colorAt {"… |
| `slide.reuse` | V | reference/newer-commands.md#New in 0.11.x (verified headle…: - `slide.reuseList {"path":"deck.deckcraft"… |
| `slide.reuseList` | V | reference/newer-commands.md#New in 0.11.x (verified headle…: - `slide.reuseList {"path":"deck.deckcraft"… |
| `slide.selectRange` | V | reference/newer-commands.md#Newer commands: - `slide.selectRange {"from"?,"to","add"?}` → `{selected:[sl… |
| `slide.selectSlides` | V | reference/shapes-text-tables.md#Text editing, character fo…: …`{index}`, `slide.selectSlides {"indices":[… |

## smartArt (13)

| id | status | note |
|---|---|---|
| `smartArt.addNode` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: `smartArt.addNode {"text":"Review"}` → `{in… |
| `smartArt.colors` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …lished"}`, `smartArt.colors {"colors":"colo… |
| `smartArt.demote` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …t. (2): `smartArt.demote` `{"id": 283, "… |
| `smartArt.fromText` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …→ new id), `smartArt.fromText {"kind":"cycl… |
| `smartArt.layout` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: `smartArt.layout {"kind":"chevron\|blockList… |
| `smartArt.nodes` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …`{index}`, `smartArt.nodes {}` (read back `… |
| `smartArt.picture` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …lots until `smartArt.picture {"index","path… |
| `smartArt.promote` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …es":[…]}`, `smartArt.promote/demote/removeN… |
| `smartArt.removeNode` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: `smartArt.removeNode` `{"id": 283, "index":… |
| `smartArt.setNodes` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …,text}]`), `smartArt.setNodes {"lines":[…]}… |
| `smartArt.style` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …ied calls: `smartArt.style {"style":"polish… |
| `smartArt.toShapes` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …"cycle"}`, `smartArt.toShapes`. |
| `smartArt.toText` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …ndex":0}`, `smartArt.toText` (→ new id), `s… |

## table (21)

| id | status | note |
|---|---|---|
| `table.borders` | V | reference/building-decks.md#Next-tier workflows (verified …: …ader row), `table.borders {"which":"inside\|… |
| `table.cellAlign` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …normal"}`, `table.cellAlign {"anchor"}`, `t… |
| `table.cellFill` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …olumns"}`, `table.cellFill {"color","cells"… |
| `table.cellMargins` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …[[r,c]]}`, `table.cellMargins {"preset":"wi… |
| `table.columnWidth` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …anchor"}`, `table.columnWidth {"col","width… |
| `table.deleteColumn` | V | reference/shapes-text-tables.md#Text editing, character fo…: … {"col"}`, `table.deleteColumn {"col"}`, `t… |
| `table.deleteRow` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …lumnLeft`, `table.deleteRow\|deleteColumn`, … |
| `table.distributeColumns` | V | reference/shapes-text-tables.md#Text editing, character fo…: … {"col"}`, `table.distributeColumns`, `tabl… |
| `table.distributeRows` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …teColumn`, `table.distributeRows/Columns`, … |
| `table.drawLine` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …/Columns`, `table.drawLine/eraseLine` |
| `table.eraseLine` | V | reference/shapes-text-tables.md#Text editing, character fo…: …":[1,1]}`, `table.eraseLine {"at":[x,y]}`. |
| `table.insertColumnLeft` | V | reference/shapes-text-tables.md#Text editing, character fo…: …*Tables: `table.insertColumnLeft\|insertCo… |
| `table.insertColumnRight` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …e. (1): `table.insertColumnRight` `{"id"… |
| `table.insertRowAbove` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …height"}`, `table.insertRowAbove\|insertColu… |
| `table.insertRowBelow` | V | reference/building-decks.md#Building a real deck (verified…: …hanges via `table.insertRowBelow {"row","id… |
| `table.merge` | V | reference/building-decks.md#Next-tier workflows (verified …: …d\|none"}`, `table.merge {"from":[0,0],"to":… |
| `table.options` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …*Tables: `table.options {"headerRow","tot… |
| `table.rowHeight` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …"width"}`, `table.rowHeight {"row","height"… |
| `table.selectCells` | V | reference/shapes-text-tables.md#Text editing, character fo…: …eColumns`, `table.selectCells {"from":[0,0]… |
| `table.split` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `table.split {"cell":[r,c]}` only on a me… |
| `table.style` | V | reference/building-decks.md#Next-tier workflows (verified …: …*Tables: `table.style {"style":"medium2-a… |

## text (17)

| id | status | note |
|---|---|---|
| `text.autocorrect` | V | reference/shapes-text-tables.md#Text editing, character fo…: …orward"}`, `text.autocorrect {"on":true}` →… |
| `text.commit` | V | reference/command-sweep.md#Verified in detail, DeckCraft p…: …t. (1): `text.commit` `{"text": "Committ… |
| `text.compose` | V | reference/shapes-text-tables.md#Text editing, character fo…: …tends it), `text.compose/commit` (input-met… |
| `text.delete` | V | reference/shapes-text-tables.md#Text editing, character fo…: …nd:true}`, `text.delete {"dir":"backward\|fo… |
| `text.deleteSurrounding` | V | reference/newer-commands.md#Newer commands: - `text.deleteSurrounding {"before":2,"after":0,"bytes"?}` a… |
| `text.edit` | V | reference/newer-commands.md#Newer commands: …ng edited: `text.edit {"id":261}` (caret at the end), `text.… |
| `text.exit` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …agraphs}`, `text.exit` |
| `text.find` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `text.find {"text","matchCase","wholeWords"… |
| `text.get` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …aragraph), `text.get {"id"}` → `{text,parag… |
| `text.insert` | V | reference/newer-commands.md#Newer commands: …fore":2}`, `text.insert {"text":"!"}` turned "Hello" into "H… |
| `text.move` | V | reference/shapes-text-tables.md#Text editing, character fo…: …h {"at"}`, `text.move {"to":"left\|right\|up\|… |
| `text.replace` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …rt,end}]`, `text.replace {"text","with"}` →… |
| `text.select` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …,`notes`), `text.select {"anchor":[p,c],"ca… |
| `text.selectAll` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …":[p,c]}`, `text.selectAll`, `text.insert {… |
| `text.selectParagraph` | V | reference/shapes-text-tables.md#Text editing, character fo…: …d {"at"}`, `text.selectParagraph {"at"}`, `… |
| `text.selectWord` | V | reference/shapes-text-tables.md#Text editing, character fo…: …":[p,c]}`, `text.selectWord {"at"}`, `text.… |
| `text.set` | V | reference/building-decks.md#More recipes (verified headles…: `text.set {"id","text"}`, |

## transition (6)

| id | status | note |
|---|---|---|
| `transition.applyAll` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …r `path`), `transition.applyAll {}` copies … |
| `transition.list` | V | reference/building-decks.md#Next-tier workflows (verified …: …0}` works (`transition.list` shows the kind… |
| `transition.options` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …n":1200}`, `transition.options {"option":"d… |
| `transition.set` | V | SKILL.md#Command formats (verified): …ansition \| `transition.set {"kind":"fade","duration"?:ms,"index"?}`… |
| `transition.sound` | V | reference/smartart-animation-masters.md#SmartArt layouts, …: …r":4000}`, `transition.sound {"builtin":"ch… |
| `transition.timing` | V | reference/smartart-animation-masters.md#SmartArt, grouping…: …700}` then `transition.timing {"onClick":fa… |

## view (4)

| id | status | note |
|---|---|---|
| `view.closeMaster` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: …geNumber), `view.closeMaster`. |
| `view.handoutMaster` | V+ | reference/shapes-text-tables.md#Shapes, text formatting, t…: …sMaster` / `view.handoutMaster` → `{created… · limit: smartart-animation-masters.md: …lso listed, not run: `design.ideas`/`applyIdea`, `view.hando… |
| `view.notesMaster` | V | reference/shapes-text-tables.md#Shapes, text formatting, t…: `view.notesMaster` / `view.handoutMaster` →… |
| `view.slideMaster` | V+ | reference/newer-commands.md#0.16.0 changes (verified headl…: `view.slideMaster` refuses an invalid maste… · limit: smartart-animation-masters.md: …tself (use `view.slideMaster {"master":0}` without a layout … |

## window (1)

| id | status | note |
|---|---|---|
| `window.next` | s | reference/shapes-text-tables.md#Text editing, character fo…: Not run … - Not run: video files, `media.posterFrame`… |
