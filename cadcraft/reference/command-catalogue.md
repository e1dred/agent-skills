# CadCraft command catalogue (0.18.0)

Built 2026-11-06 from the skill's own text (SKILL.md, reference/ and tools/); no command was run and nothing was re-tested. Ids come from `cadcraft-cli` 0.18.0 (457 ids); the skill's version label: last tested on cadcraft-cli 0.18.0; evidence sections cite 0.14.0-0.18.0.
Status: **V** verified - the hit is under a heading naming verification or records an observed result (arrow, before/after, read-back, checked file, confirmed); **d** documented - named with parameters or usage, no recorded evidence; **n** named only - a bare list or command index; **s** skipped on purpose - the skill says skipped/not run/not tested/not exercised; **x** known no-op, broken or refused - the line says so; **V+** verified, but another line records a limit (refused or skipped in some state or version); the note quotes both. When a command has verified evidence anywhere, it counts as verified: a refusal or skip recorded elsewhere usually names a precondition or an older round.
Counts: V 241, V+ 5, d 136, n 60, s 15, x 0.
Ids with a dot are grouped by the part before the first dot; ids without one are grouped by first letter.

## angle (1)

| id | status | note |
|---|---|---|
| `angle.measure` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …diameter), `angle.measure {vertex,p1,p2}` (… |

## annovisible (3)

| id | status | note |
|---|---|---|
| `annovisible.all` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …e. (2): `annovisible.all` ANNOALLVISIBLE… |
| `annovisible.current` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …noupdate`, `annovisible.current\|all\|toggle`… |
| `annovisible.toggle` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `annovisible.toggle` ANNOALLVISIBLE 1 -> 0 … |

## arc (10)

| id | status | note |
|---|---|---|
| `arc.continue` | s | reference/command-sweeps.md#Round 13: the remaining comman…: Not run … - Not run: `arc.continue` after an arc, `-p… |
| `arc.csa` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …c. (6): `arc.csa` `{"center":[0,0],"star… |
| `arc.cse` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …\|radius}`, `arc.cse\|csa\|csl {center,start,e… |
| `arc.csl` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `arc.csl` `{"center":[0,0],"start":[10,0],"… |
| `arc.sca` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `arc.sca` `{"start":[10,0],"center":[0,0],"… |
| `arc.sce` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …e): arcs `arc.sce\|sca\|scl {start,center,e… |
| `arc.scl` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `arc.scl` `{"start":[10,0],"center":[0,0],"… |
| `arc.sea` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …\|length}`, `arc.sea\|sed\|ser {start,end,angl… |
| `arc.sed` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `arc.sed` `{"start":[10,0],"end":[0,10],"di… |
| `arc.ser` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `arc.ser` `{"start":[10,0],"end":[0,10],"ra… |

## attdisp (3)

| id | status | note |
|---|---|---|
| `attdisp.normal` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …p. (3): `attdisp.normal` ATTMODE 0 -> 1 … |
| `attdisp.off` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `attdisp.off` ATTMODE -> 0 |
| `attdisp.on` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `attdisp.on` ATTMODE -> 2 (all attributes s… |

## blocks (7)

| id | status | note |
|---|---|---|
| `blocks.description` | V | reference/newer-commands.md#Newer commands (verified headl…: - `blocks.description {"name","description"… |
| `blocks.dynamic` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: `blocks.dynamic {"name"}` returns null for … |
| `blocks.list` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …e shows in `blocks.list` |
| `blocks.reference` | V | reference/dwg-files.md#Round 10: a real AutoCAD DWG from a…: …irst, then `blocks.reference {"handle":"23E… |
| `blocks.reference.grip` | V | reference/dwg-files.md#Round 10: a real AutoCAD DWG from a…: …` 1.2747), `blocks.reference.grips`, `block… |
| `blocks.reference.grips` | V | reference/dwg-files.md#Round 10: a real AutoCAD DWG from a…: …` 1.2747), `blocks.reference.grips`, `block… |
| `blocks.reference.set` | V | reference/dwg-files.md#Round 10: a real AutoCAD DWG from a…: …ce.grips`, `blocks.reference.set {"handle",… |

## circle (5)

| id | status | note |
|---|---|---|
| `circle.2p` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …iameter}`, `circle.2p`, `circle.3p`, `circl… |
| `circle.3p` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …ircle.2p`, `circle.3p`, `circle.ttr {h1,p1,… |
| `circle.cd` | d | reference/command-sweeps.md#Round 13: the remaining comman…: circles `circle.cd {center,diameter}`, `cir… |
| `circle.ttr` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ircle.3p`, `circle.ttr {h1,p1,h2,p2,radius}… |
| `circle.ttt` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …,radius}`, `circle.ttt {h1,p1,h2,p2,h3,p3}`… |

## compare (2)

| id | status | note |
|---|---|---|
| `compare.next` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …e. (2): `compare.next` after `compare {"… |
| `compare.previous` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `compare.previous` from area 1 it wrapped t… |

## constraintbar (2)

| id | status | note |
|---|---|---|
| `constraintbar.hideall` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `constraintbar.hideall` settings barsVisibl… |
| `constraintbar.showall` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …infer {}`, `constraintbar.showall\|hideall`,… |

## constraints (2)

| id | status | note |
|---|---|---|
| `constraints.dof` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …lue":25}`, `constraints.dof {}` ("2 degrees… |
| `constraints.inspect` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …e,h1,h2}`; `constraints.inspect` gives ids,… |

## dcdisplay (2)

| id | status | note |
|---|---|---|
| `dcdisplay.hideall` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `dcdisplay.hideall` settings dimsVisible tr… |
| `dcdisplay.showall` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …\|hideall`, `dcdisplay.showall\|hideall`. |

## dimedit (1)

| id | status | note |
|---|---|---|
| `dimedit.oblique` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …40 REF"}`, `dimedit.oblique {angle}`, `dimt… |

## dimstyle (7)

| id | status | note |
|---|---|---|
| `dimstyle.current` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …e. (3): `dimstyle.current` `{"name":"D1"… |
| `dimstyle.delete` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `dimstyle.delete` `{"name":"D3"}`: styles S… |
| `dimstyle.dimension` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `dimstyle.dimension {name,DIM*…}` = `dimsty… |
| `dimstyle.list` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …yle.list`, `dimstyle.list`, `layerstate.lis… |
| `dimstyle.override` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …XT:5}` and `dimstyle.override` (`changed:1,… |
| `dimstyle.rename` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `dimstyle.rename` `{"from":"D2","to":"D3"}`… |
| `dimstyle.update` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ored:[]`), `dimstyle.update {handles}`, `di… |

## dimtedit (5)

| id | status | note |
|---|---|---|
| `dimtedit.angle` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …t. (3): `dimtedit.angle` `{"handles","an… |
| `dimtedit.center` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `dimtedit.center` sets textJust 0 (centred)… |
| `dimtedit.home` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …angle}` (+ `dimtedit.home\|angle\|center\|righ… |
| `dimtedit.left` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: `dimtedit.left` moves it. |
| `dimtedit.right` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `dimtedit.right` adds the override textJust… |

## document (2)

| id | status | note |
|---|---|---|
| `document.bytes` | d | reference/dwg-files.md#Round 11: save versions and the las…: …}` (also `document.bytes`) writes DWG or … |
| `document.switch` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …sing file, `document.switch {index}`, `clos… |

## drawing (1)

| id | status | note |
|---|---|---|
| `drawing.inspect` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …svars {}`, `drawing.inspect {entities,limit… |

## draworder (4)

| id | status | note |
|---|---|---|
| `draworder.above` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …r. (2): `draworder.above` `{"handles":["… |
| `draworder.back` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ference}`, `draworder.back\|above\|under`, `t… |
| `draworder.front` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …p {"at"}`, `draworder.front`, `group` / `un… |
| `draworder.under` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `draworder.under` `{"handles":["102"],"refe… |

## ellipse (2)

| id | status | note |
|---|---|---|
| `ellipse.arc` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …istance}`, `ellipse.arc {center,major,ratio… |
| `ellipse.axis` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `ellipse.axis {p1,p2,distance}`, `ellipse.a… |

## erase (1)

| id | status | note |
|---|---|---|
| `erase.selection` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …lectall` + `erase.selection`, `isolateobjec… |

## grip (6)

| id | status | note |
|---|---|---|
| `grip.mirror` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …p. (6): `grip.mirror` `{"handles","base"… |
| `grip.move` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `grip.move` on a line, grip index 1 is the … |
| `grip.option` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `grip.option` `{"handle","index":1,"option"… |
| `grip.rotate` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `grip.rotate` `{"handles","base":[0,0],"ang… |
| `grip.scale` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `grip.scale` `{"handles","base":[0,0],"fact… |
| `grip.stretch` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `grip.stretch` `{"handle","index":0,"to":[-… |

## groups (1)

| id | status | note |
|---|---|---|
| `groups.list` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …ndles"}` + `groups.list`, `table {"at","row… |

## hatch (1)

| id | status | note |
|---|---|---|
| `hatch.patterns` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …e {load}`, `hatch.patterns {}` (standard na… |

## layer (4)

| id | status | note |
|---|---|---|
| `layer.current` | V | SKILL.md#Commands used (parameters verified): `layer.current {"name"}` |
| `layer.delete` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …*Layers: `layer.delete {name}` fails "lay… |
| `layer.new` | V | SKILL.md#Commands used (parameters verified): - `layer.new {"name","color":1\|"red"\|index,"lineweight":0.… |
| `layer.set` | V | SKILL.md#Commands used (parameters verified): `layer.set {"name","on","frozen","locked","color",…}`. |

## layerstate (5)

| id | status | note |
|---|---|---|
| `layerstate.delete` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …e. (2): `layerstate.delete` `{"name":"LS… |
| `layerstate.list` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …yle.list`, `layerstate.list`, `-vports list… |
| `layerstate.rename` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `layerstate.rename` `{"from":"LS1","to":"LS… |
| `layerstate.restore` | n | reference/command-sweeps.md#Round 13: the remaining comman…: … states"), `layerstate.restore\|rename {from… |
| `layerstate.save` | n | reference/command-sweeps.md#The last 62 command ids (2026-…: `layerstate.save` for `layerstate.rename\|de… |

## layout (7)

| id | status | note |
|---|---|---|
| `layout.copy` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …"Model"}`, `layout.copy {from,to}`, `layout… |
| `layout.delete` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …from,to}`, `layout.delete {name}`, `layout.… |
| `layout.list` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …e {name}`, `layout.list` (page setup and vi… |
| `layout.new` | V | reference/command-sweeps.md#Round 13: the remaining comman…: Layouts: `layout.new {name,viewport:false}`… |
| `layout.rename` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …from,to}`, `layout.rename {from,to}`, `layo… |
| `layout.saveas` | V | reference/newer-commands.md#Newer commands (verified headl…: - `layout.saveas {"name"?,"path"}` (also `l… |
| `layout.set` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …t:false}`, `layout.set {name\|"Model"}`, `la… |

## mleaderedit (2)

| id | status | note |
|---|---|---|
| `mleaderedit.add` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … others: `mleaderedit.add {handle,points}… |
| `mleaderedit.remove` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …`added:1`, `mleaderedit.remove {handle,inde… |

## mview (1)

| id | status | note |
|---|---|---|
| `mview.polygonal` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …iewports); `mview.polygonal {points}` → bou… |

## pan (4)

| id | status | note |
|---|---|---|
| `pan.down` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `pan.down` VIEWCTR y 50 -> 23.75 (a quarter… |
| `pan.left` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …previous`, `pan.left\|right\|up\|down`, `regen… |
| `pan.right` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `pan.right` VIEWCTR x 50 -> 89.375 (a quart… |
| `pan.up` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `pan.up` VIEWCTR y 50 -> 76.25. |

## point (1)

| id | status | note |
|---|---|---|
| `point.multiple` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …`wipeout`, `point.multiple`, `ray`, `donut`… |

## properties (1)

| id | status | note |
|---|---|---|
| `properties.set` | V | reference/dwg-files.md#Round 12: two more AutoCAD DWGs, 20…: …e` through `properties.set`, or delete and … |

## qselect (1)

| id | status | note |
|---|---|---|
| `qselect.info` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … 50, ccw), `qselect.info {}` (types with co… |

## quickcalc (1)

| id | status | note |
|---|---|---|
| `quickcalc.pick` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …2}` (90°), `quickcalc.pick {mode:"distance"… |

## radius (1)

| id | status | note |
|---|---|---|
| `radius.measure` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …ng mlines; `radius.measure {handle}` (R and… |

## revcloud (2)

| id | status | note |
|---|---|---|
| `revcloud.freehand` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …cLength}`, `revcloud.freehand {freehand,arc… |
| `revcloud.polygonal` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `revcloud.polygonal {points,arcLength}`, `r… |

## spline (1)

| id | status | note |
|---|---|---|
| `spline.cv` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `spline.cv {control,degree}` |

## style (4)

| id | status | note |
|---|---|---|
| `style.current` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …e. (3): `style.current` `{"name":"S1"}` … |
| `style.delete` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `style.delete` `{"name":"S2"}` (not current… |
| `style.list` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …list form (`style.list`, `dimstyle.list`, `… |
| `style.rename` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `style.rename` `{"from":"S2","to":"S3"}`: l… |

## table (11)

| id | status | note |
|---|---|---|
| `table.break` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ol,text}`, `table.break {handle,enabled,dir… |
| `table.cellstyle` | d | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …true}` and `table.cellstyle {"handle","styl… |
| `table.deletecol` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …e. (3): `table.deletecol` `{"handle","co… |
| `table.deleterow` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …*Tables: `table.deleterow\|insertcol\|delet… |
| `table.formula` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `table.formula {handle,row,col,function:"su… |
| `table.insertcol` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `table.insertcol` `{"handle","col":1}` on a… |
| `table.insertrow` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …`#CYCLE`), `table.insertrow`, `table.merge … |
| `table.merge` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …rge` after `table.merge {"row":0,"col":0,"r… |
| `table.recalc` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …sum"}` and `table.recalc` need rows that ex… |
| `table.set` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …a from 2), `table.set {"handle","row","col"… |
| `table.unmerge` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `table.unmerge` after `table.merge {"row":0… |

## tablestyle (1)

| id | status | note |
|---|---|---|
| `tablestyle.cellstyle` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …parts:3`), `tablestyle.cellstyle {name:"Dat… |

## texttofront (4)

| id | status | note |
|---|---|---|
| `texttofront.all` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …t. (4): `texttofront.all` moved text, di… |
| `texttofront.dimensions` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `texttofront.dimensions` moved only the DIM… |
| `texttofront.leaders` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `texttofront.leaders` moved only the MULTIL… |
| `texttofront.text` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `texttofront.text` a TEXT under a later LIN… |

## view (2)

| id | status | note |
|---|---|---|
| `view.get` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: … the view (`view.get` twist 0 → 15 → 30). |
| `view.set` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: …}` and `view.set {"twist":15}` rotate… |

## viewport (1)

| id | status | note |
|---|---|---|
| `viewport.set` | V | SKILL.md#CLI essentials (verified): … returned (`viewport.set {"handle":"{last}"}`). |

## volume (1)

| id | status | note |
|---|---|---|
| `volume.measure` | V | reference/drafting-features.md#Round 8 (2026-10-26; annota…: …pe Helix), `volume.measure {"handle":closed… |

## vports (6)

| id | status | note |
|---|---|---|
| `vports.1` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …s. (3): `vports.1` from 4 tiles back to … |
| `vports.2` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `vports.2` model-space tiles 1 -> 2 (`-vpor… |
| `vports.3` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … handle; `vports.3` etc. report tiles; `v… |
| `vports.4` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: `vports.4` tiles -> 4. |
| `vports.activate` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …s `mview`; `vports.activate` needs `index`. |
| `vports.named` | V | reference/newer-commands.md#Newer commands (verified headl…: - `vports.named {"name"?,"delete"?,"p1"?,"p… |

## zoom (9)

| id | status | note |
|---|---|---|
| `zoom.all` | n | reference/command-sweeps.md#Round 13: the remaining comman…: ….extents`, `zoom.all`, `zoom.in\|out` (×½, ×… |
| `zoom.dynamic` | n | reference/command-sweeps.md#Round 13: the remaining comman…: ….realtime`/`zoom.dynamic` need a `factor` (… |
| `zoom.extents` | n | reference/command-sweeps.md#Round 13: the remaining comman…: … {p1,p2}`, `zoom.extents`, `zoom.all`, `zoo… |
| `zoom.in` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …zoom.all`, `zoom.in\|out` (×½, ×2), `zoom.ob… |
| `zoom.object` | n | reference/command-sweeps.md#Round 13: the remaining comman…: … (×½, ×2), `zoom.object`, `zoom.previous`, … |
| `zoom.out` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …m. (1): `zoom.out` VIEWSIZE 105 -> 210 (… |
| `zoom.previous` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …m.object`, `zoom.previous`, `pan.left\|right… |
| `zoom.realtime` | n | reference/command-sweeps.md#Round 13: the remaining comman…: `zoom.realtime`/`zoom.dynamic` need a `fact… |
| `zoom.window` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …1200×800), `zoom.window {p1,p2}`, `zoom.ext… |

## - (10)

| id | status | note |
|---|---|---|
| `-array` | s | reference/schematics.md#Beginner wiring guide from a schem…: …6.0 adds `-array`, `-units` and `change` … |
| `-attedit` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - -attedit. (1): `-attedit` `{"tag":"I… |
| `-block` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …d as `--cmd=-block {…}` (with `=`), or the … |
| `-group` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - -group. (1): `-group` `{"option":"cr… |
| `-linetype` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - -linetype. (1): `-linetype` `{"load"… |
| `-plottermanager` | V+ | reference/command-sweeps.md#Verified in detail, CadCraft l…: …d: `--cmd=-plottermanager {…}` with an is… · limit: command-sweeps.md: Not run … - Not run: `arc.continue` after an arc, `-plottermanager`, `… |
| `-units` | s | reference/schematics.md#Beginner wiring guide from a schem…: … `-array`, `-units` and `change` (from a `c… |
| `-vports` | V+ | reference/command-sweeps.md#Verified in detail, CadCraft p…: …ate.list`, `-vports list`, `-xref ?`, `cons… · limit: drafting-features.md: …umented but not run: `xattach`, `objectscale`, `scalelistedi… |
| `-wblock` | V | reference/newer-commands.md#0.17 changes (verified headles…: … and after `-wblock`). |
| `-xref` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …rts list`, `-xref ?`, `constraints.inspect`… |

## 3 (2)

| id | status | note |
|---|---|---|
| `3dorbit` | n | reference/command-sweeps.md#Round 13: the remaining comman…: … 0.13.0: `3dorbit` ("CADCraft draws in 2D… |
| `3dpoly` | V | reference/drafting-features.md#Round 8 (2026-10-26; annota…: …(basic): `3dpoly {"points":[[x,y,z]…]}`, … |

## a (23)

| id | status | note |
|---|---|---|
| `ai_deselect` | s | reference/command-sweeps.md#Round 13: the remaining comman…: Not run … - Not run: `arc.continue` after an arc, `-p… |
| `aiobjectscaleadd` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …otative: `aiobjectscaleadd\|aiobjectscaler… |
| `aiobjectscaleremove` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ectscaleadd\|aiobjectscaleremove {handles}` … |
| `aliasedit` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …["BAR"]`), `aliasedit {set:{"zz":"circle"}}… |
| `align` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …,"pick"}`, `align`, `mirror {"handles","p1"… |
| `annoreset` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …east one), `annoreset`, `annoupdate`, `anno… |
| `annoupdate` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …nnoreset`, `annoupdate`, `annovisible.curre… |
| `appload` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …a command, `appload {name,text}` loads a .l… |
| `arc` | V | SKILL.md#Commands used (parameters verified): …radius"}`, `arc {"center","radius","start","end"}` (degree… |
| `area` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …`, `dist`, `area`, `find {"find","replace"}… |
| `array` | V | SKILL.md#Commands used (parameters verified): …`stretch`, `array`, `explode` |
| `arrayclose` | V+ | reference/command-sweeps.md#Verified in detail, CadCraft s…: - arrayclose. (1): `arrayclose` headle… · limit: command-sweeps.md: Refused … - Refused: `arrayclose` (No array is being edited.). |
| `arrayedit` | V | reference/command-sweeps.md#Verified in detail, CadCraft s…: …iting with `arrayedit {"handle":ARRAY,"sour… |
| `arraypath` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `arraypath {handles,path,count}` (returned … |
| `arraypolar` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …y handle), `arraypolar` (the centre of the … |
| `arrayrect` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …, `scale`, `arrayrect {"handles","rows","co… |
| `attach` | V | reference/command-sweeps.md#Ten ids that were only named a…: … nothing), `attach` ("not available yet: ra… |
| `attdef` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …ributes: `attdef {"tag","default","at","h… |
| `attdisp` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … counts: `attdisp {mode:"on"\|"off"\|"norma… |
| `attedit` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: `attedit {"handle","values":{"tag":"v"}}` (… |
| `attsync` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …DE 1/2/0), `attsync {name}`, `-attedit {fin… |
| `audit` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …, `purge`, `audit`, `undo {"count":1}`, `la… |
| `autoconstrain` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |

## b (14)

| id | status | note |
|---|---|---|
| `base` | V | reference/command-sweeps.md#Ten ids that were only named a…: - `base {"at":[5,7]}` sets the drawing's in… |
| `battman` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …ributes: `battman {"name":"B"}` lists the… |
| `bclose` | V | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …lock, then `bclose {}` (saves by default: b… |
| `bedit` | V | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …rified): `bedit {"name":"B"}`, draw into … |
| `blend` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `blend {h1,p1,h2,p2,continuity}` |
| `block` | V | SKILL.md#Commands used (parameters verified): blocks: `block {"name","base","handles"}` then `insert {"n… |
| `blockreplace` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: `blockreplace {"block":"C1","with":"C2"}` s… |
| `boundary` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: …ip returns `boundary:null, enabled:false`. |
| `break` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …"delta"}`, `break {"handle","p1","p2"}` → `… |
| `breakatpoint` | V | reference/newer-commands.md#0.18.0 changes (verified headl…: … (`break`, `breakatpoint`, `chprop`, `prope… |
| `breakline` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …,"text"}`; `breakline {"p1","p2"}`; constra… |
| `bsave` | V | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …ed:true`); `bsave {}` saves without closing… |
| `bsaveas` | n | reference/dwg-files.md#Round 11: save versions and the las…: …, `bsave`, `bsaveas`, `bclose`) |
| `burst` | n | reference/drafting-features.md#Round 7 (2026-10-26, headle…: `burst` explodes attribute blocks to text. |

## c (25)

| id | status | note |
|---|---|---|
| `cal` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …d {"at"}`, `cal {"expr":"2*pi*5"}` (31.4159… |
| `centerline` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …e","at"}`, `centerline {"h1","h2"}` (two li… |
| `centermark` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …\|"join"}`, `centermark` (two lines on the C… |
| `chamfer` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …leted:4`), `chamfer {"h1","p1","h2","p2","d… |
| `change` | s | reference/schematics.md#Beginner wiring guide from a schem…: …units` and `change` (from a `commands` diff… |
| `chprop` | V | reference/newer-commands.md#0.18.0 changes (verified headl…: …katpoint`, `chprop`, `properties.set`, `tri… |
| `chspace` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …/`pspace`; `chspace {handles,to:"L1"}` (`mo… |
| `circle` | V | SKILL.md#Commands used (parameters verified): …"width"}`, `circle {"center","radius"}`, `arc {"center","r… |
| `close` | V | reference/log.md#Log: … `render`, `close`). |
| `closeall` | n | reference/command-sweeps.md#Round 13: the remaining comman…: … {index}`, `closeall`. |
| `color` | V | reference/newer-commands.md#0.18.0 changes (verified headl…: …s":["100"],"color":"green"}` answered `{cha… |
| `compare` | V+ | reference/command-sweeps.md#Verified in detail, CadCraft p…: - compare. (2): `compare.next` after `… · limit: command-sweeps.md: Not run … - Not run: `arc.continue` after an arc, `-plottermanager`, `… |
| `compareclose` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - compareclose. (1): `compareclose` `{… |
| `compareexport` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - compareexport. (1): `compareexport` … |
| `constraintbar` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - constraintbar. (2): `constraintbar` … |
| `constraintinfer` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …Visible}`, `constraintinfer {}`, `constrain… |
| `constraintsettings` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … nothing), `constraintsettings {infer,barsV… |
| `copy` | V | SKILL.md#Commands used (parameters verified): …g: `move`, `copy`, `rotate`, `mirror`, `scale {"handles","… |
| `copybase` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … `cutbase`/`copybase {handles,base}`, `past… |
| `copyclip` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …, `donut`, `copyclip` + `pasteclip {"at"}`,… |
| `count` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: `count {}` counts inserts |
| `countlist` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …me, tags), `countlist {}` (per block, `nest… |
| `counttable` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …`nested`), `counttable {at}` inserts a tabl… |
| `cutbase` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …`cutclip`, `cutbase`/`copybase {handles,bas… |
| `cutclip` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …jects {}`, `cutclip`, `cutbase`/`copybase {… |

## d (43)

| id | status | note |
|---|---|---|
| `dataextraction` | d | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …terials: `dataextraction {"file":"de.csv"… |
| `datalink` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …l styles), `datalink {handle,path:CSV}` (4×… |
| `datalinkupdate` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …tle row) + `datalinkupdate {}` (`updated:1`… |
| `dcaligned` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …imensional `dcaligned\|dclinear\|dcvertical\|d… |
| `dcangular` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …\|dcvertical\|dcangular\|dcradius\|dcdiameter {… |
| `dcdiameter` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …ar\|dcradius\|dcdiameter {h1,p1,h2,p2,value\|e… |
| `dcdisplay` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - dcdisplay. (2): `dcdisplay` `{"mode"… |
| `dchorizontal` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …l {"h1"}`, `dchorizontal {"h1","p1":"start"… |
| `dclinear` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … `dcaligned\|dclinear\|dcvertical\|dcangular\|d… |
| `dcradius` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …l\|dcangular\|dcradius\|dcdiameter {h1,p1,h2,p… |
| `dcvertical` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …ed\|dclinear\|dcvertical\|dcangular\|dcradius\|d… |
| `ddptype` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …min,max}`, `ddptype {pdmode,pdsize}`, `-lin… |
| `delconstraint` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …atisfied`; `delconstraint {ids:[id]}` (ids … |
| `dim` | d | reference/command-sweeps.md#Ten ids that were only named a…: - `dim {"p1","p2","at"}` draws a linear DIM… |
| `dimaligned` | V | SKILL.md#Commands used (parameters verified): …imlinear`, `dimaligned`, … (not used). |
| `dimangular` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …ME handle (`dimangular {"lines":["{last}","… |
| `dimarc` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: … handles), `dimarc {"handle","at"}`, `cente… |
| `dimbaseline` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …s":[…]}` / `dimbaseline` continue the LAST … |
| `dimbreak` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `dimconstraint` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …roximate), `dimconstraint {type,h1,value,na… |
| `dimcontinue` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …maligned`, `dimcontinue {"points":[…]}` / `… |
| `dimdiameter` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …dimradius`/`dimdiameter {"handle","at"}` or… |
| `dimdisassociate` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …imension), `dimdisassociate` |
| `dimedit` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …{handle}`, `dimedit {handles,mode:"new",tex… |
| `diminspect` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …handles}`, `diminspect {handles,shape:"roun… |
| `dimjogged` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …,leader}`, `dimjogged {handle:circle,center… |
| `dimjogline` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …,at,jog}`, `dimjogline {handle}`, `dimedit … |
| `dimlinear` | V | SKILL.md#Commands used (parameters verified): …imensions: `dimlinear`, `dimaligned`, … (not used). |
| `dimordinate` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ensions: `dimordinate {feature,leader}`, … |
| `dimoverride` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …tJust 1`), `dimoverride {handles,DIMTXT:5}`… |
| `dimradius` | d | reference/recipes.md#Parametric ECO plate drawing on an A3…: … after the `dimradius {"center","point","at… |
| `dimreassociate` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …,rate}`, `dimreassociate` only works when… |
| `dimspace` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `dimstyle` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: Styles: `dimstyle {"name","DIMTXT":4,"DIMAS… |
| `dimtedit` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … {angle}`, `dimtedit {mode:home\|angle\|left\|… |
| `dist` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …`, `list`, `dist`, `area`, `find {"find","r… |
| `divide` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …coincide), `divide` (puts point objects: in… |
| `donut` | V | SKILL.md#Commands used (parameters verified): …1","p2"}`, `donut {"center","inside":0,"outside":2.2}` (a … |
| `drawingrecovery` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …sts xrefs, `drawingrecovery {action:"list"}… |
| `draworder` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …w order: `draworder {handles,order:"front… |
| `dsettings` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … {plane}`, `dsettings {snapunit,gridunit,po… |
| `dview` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: - `dview {"twist":30}` and `view.set … |
| `dynmode` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …grid\|otrack\|dynmode\|lwdisplay\|transparencyd… |

## e (8)

| id | status | note |
|---|---|---|
| `eattext` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ence only, `eattext {blocks,file}` wrote a … |
| `ellipse` | V | SKILL.md#Commands used (parameters verified): …on dot), `ellipse`, `spline`, `point`, `hatch`. |
| `entities` | V | reference/dwg-files.md#Round 12: two more AutoCAD DWGs, 20…: …al part: `entities {}` for all handles, `… |
| `erase` | V | reference/drafting-features.md#Erase and quick save (verif…: …t the last `erase` removed: `oops {}` (0.17… |
| `explode` | V | SKILL.md#Commands used (parameters verified): …, `array`, `explode` |
| `export` | V | SKILL.md#Commands used (parameters verified): - Output: `export {"path","format"}`, `exportpdf {"path","… |
| `exportpdf` | V | SKILL.md#Commands used (parameters verified): …format"}`, `exportpdf {"path","paper","landscape","fit","s… |
| `extend` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …es":[h]}`, `extend`, `offset {"handle","dis… |

## f (3)

| id | status | note |
|---|---|---|
| `fillet` | V | SKILL.md#Commands used (parameters verified): …`, `trim`, `fillet`, `stretch`, `array`, `explode` |
| `find` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: - `find` takes `types:["MTEXT"]` and `han… |
| `flatten` | V | reference/drafting-features.md#Round 8 (2026-10-26; annota…: …thickness, `flatten {"handles"}`. |

## g (19)

| id | status | note |
|---|---|---|
| `gccoincident` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …c\|gctangent\|gccoincident {h1,p1,h2,p2}` and… |
| `gccollinear` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …rpendicular\|gccollinear\|gcequal\|gcvertical\|… |
| `gcconcentric` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …tical\|gcfix\|gcconcentric\|gctangent\|gccoinci… |
| `gcequal` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …gccollinear\|gcequal\|gcvertical\|gcfix\|gcconc… |
| `gcfix` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …\|gcvertical\|gcfix\|gcconcentric\|gctangent\|gc… |
| `gchorizontal` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …nstraints: `gchorizontal {"h1"}`, `dchorizo… |
| `gcparallel` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … geometric `gcparallel\|gcperpendicular\|gcco… |
| `gcperpendicular` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …`gcparallel\|gcperpendicular\|gccollinear\|gce… |
| `gcsmooth` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …t a line), `gcsmooth` (two splines), each r… |
| `gcsymmetric` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …2,p2}` and `gcsymmetric {h1,h2,h3}` (symmet… |
| `gctangent` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …cconcentric\|gctangent\|gccoincident {h1,p1,h… |
| `gcvertical` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …ear\|gcequal\|gcvertical\|gcfix\|gcconcentric\|g… |
| `geomconstraint` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …`R1 = 8`), `geomconstraint {type,h1,h2}`; `… |
| `getvar` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: …handles}`, `getvar`, the command's own list… |
| `gradient` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: `gradient {"handles","name":"LINEAR","color… |
| `grid` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …gles `ortho\|grid\|otrack\|dynmode\|lwdisplay\|t… |
| `grip` | V | reference/command-sweeps.md#Ten ids that were only named a…: …own yet"), `grip` (interactive only; JSON c… |
| `group` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …, `xline`, `group {"name","handles"}` + `gr… |
| `groupedit` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `groupedit {name,add}`, `-group {option:"cr… |

## h (6)

| id | status | note |
|---|---|---|
| `hatch` | V | SKILL.md#Commands used (parameters verified): …, `point`, `hatch`. |
| `hatchedit` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `hatchpick` | n | reference/command-sweeps.md#Round 13: the remaining comman…: `hatchpick` only returns the picked points/… |
| `hatchtoback` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ers\|.all`, `hatchtoback {}` |
| `helix` | V | reference/drafting-features.md#Round 8 (2026-10-26; annota…: …,y,z]…]}`, `helix {"center","baseRadius","t… |
| `hideobjects` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …lateobjects\|hideobjects {handles}` + `uniso… |

## i (9)

| id | status | note |
|---|---|---|
| `id` | V | SKILL.md#CLI essentials (verified): …cr] [--cmd 'id {json}']... [--save OUT.dxf] [--export OUT.pdf\|svg\|pn… |
| `image` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: - Raster images: `imageattach {"path":"… |
| `imageattach` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: … images: `imageattach {"path":"/abs/pic.p… |
| `import` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …k from it, `import {"path","at","scale"}` b… |
| `insert` | V | SKILL.md#Commands used (parameters verified): …es"}` then `insert {"name","at","scale","rotation"}`, `wbl… |
| `intersect` | n | reference/drafting-features.md#Round 3 (2026-10-26, headle…: `union`/`intersect` of OVERLAPPING regions … |
| `isodraft` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … end+mid), `isodraft {on,plane}`, `isoplane… |
| `isolateobjects` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …election`, `isolateobjects\|hideobjects {han… |
| `isoplane` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …n,plane}`, `isoplane {plane}`, `dsettings {… |

## j (1)

| id | status | note |
|---|---|---|
| `join` | d | reference/command-sweeps.md#Ten ids that were only named a…: - `join {"handles":[…]}` joins touching lin… |

## l (27)

| id | status | note |
|---|---|---|
| `laycur` | n | reference/command-sweeps.md#Round 13: the remaining comman…: … checked), `laycur`, `laymch {handles,layer… |
| `laydel` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …s],"to"}`, `laydel {"names":[…]}` (deletes … |
| `layer` | d | reference/live-window.md#Round 9: a real drawing in the li…: … `height`, `layer`, `handle`) |
| `layerp` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …uniso {}`, `layerp {}` ("Restored previous … |
| `layfrz` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …`/`layoff`/`layfrz` need `{"handles":[…]}` … |
| `layiso` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: … or names: `layiso`/`layoff`/`layfrz` need … |
| `laylck` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …o a layer, `laylck\|layulk {handles}`, `layo… |
| `laymch` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … `laycur`, `laymch {handles,layer}` moved a… |
| `laymcur` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `laymcur {handles}` makes the object's laye… |
| `laymrg` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …the layer, `laymrg {"from":[names],"to"}`, … |
| `layoff` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …: `layiso`/`layoff`/`layfrz` need `{"handle… |
| `layon` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …handles}`, `layon {}`, `laythw {}`, `layuni… |
| `layout` | V | reference/dwg-files.md#Round 10: a real AutoCAD DWG from a…: …APER view (`layout {"option":"set","name":…… |
| `laythw` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …layon {}`, `laythw {}`, `layuniso {}`, `lay… |
| `layulk` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …er, `laylck\|layulk {handles}`, `layon {}`, … |
| `layuniso` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …aythw {}`, `layuniso {}`, `layerp {}` ("Res… |
| `leader` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …&T frame); `leader {"points","text"}`; `bre… |
| `lengthen` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …pt,new]}`, `lengthen {"handle","delta","pic… |
| `limits` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …eweight}`, `limits {min,max}`, `ddptype {pd… |
| `line` | V | SKILL.md#Commands used (parameters verified): … Geometry: `line {"points":[[x,y],…]}`, `pline {"vertices"… |
| `linetype` | V | SKILL.md#Commands used (parameters verified): …":0.6 (mm),"linetype":"DASHED","current":true}` (a linetyp… |
| `lisp` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …aliases: `lisp {code:"(+ 1 2)"}` → `value… |
| `list` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: … back with `list {handles}`, `getvar`, the … |
| `loops` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …er layer), `loops {}` (closed loops from lo… |
| `ltscale` | n | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …, `getvar`/`ltscale`. |
| `lwdisplay` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …ack\|dynmode\|lwdisplay\|transparencydisplay\|q… |
| `lweight` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …queries: `lweight {lineweight}`, `limits … |

## m (20)

| id | status | note |
|---|---|---|
| `massprop` | n | reference/drafting-features.md#Round 3 (2026-10-26, headle…: `massprop` needs a selection. |
| `matchprop` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …:"blue"}`, `matchprop {"source","targets","… |
| `measure` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `measure {handle,length}` (3 points on a 20… |
| `measuregeom` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …nts}` (5), `measuregeom {mode:"area",handle… |
| `minsert` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: - `minsert {block, rows:2, columns:3, row… |
| `mirror` | V | SKILL.md#Commands used (parameters verified): … `rotate`, `mirror`, `scale {"handles","base","factor"}`, … |
| `mleader` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … others: `mleaderedit.add {handle,points}… |
| `mleaderalign` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …index}`; `mleaderalign` needs `to` (the m… |
| `mleadercollect` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …igned:n`); `mleadercollect {handles,at}` ne… |
| `mleaderedit` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - mleaderedit. (1): `mleaderedit` `{"h… |
| `mleaderstyle` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `mledit` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …ected:2`); `mledit {tool:"cc",first,p1,seco… |
| `mline` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …rue}` then `mline {"points","scale"}`; `tol… |
| `mlstyle` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …erified: `mlstyle {"name","elements":[{"o… |
| `mocoro` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `mocoro {handles,base,ops:[{copy},{rotate},… |
| `move` | V | SKILL.md#Commands used (parameters verified): - Editing: `move`, `copy`, `rotate`, `mirror`, `scale {"ha… |
| `mredo` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … {count}`, `mredo {all:true}` (named the re… |
| `mspace` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …enLayers`; `mspace`/`pspace`; `chspace {han… |
| `mtext` | V | SKILL.md#Commands used (parameters verified): … on `at`), `mtext {"at","text","width",…}`. |
| `mview` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …iewports); `mview.polygonal {points}` → bou… |

## n (2)

| id | status | note |
|---|---|---|
| `ncopy` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `ncopy {handle:insert,delta}` |
| `new` | d | reference/command-sweeps.md#Ten ids that were only named a…: - `new {"metric":true}` opens another drawi… |

## o (9)

| id | status | note |
|---|---|---|
| `objectscale` | V+ | reference/drafting-features.md#Round 8 (2026-10-26; annota…: …model plus `objectscale {"handles":[text],"… · limit: drafting-features.md: …umented but not run: `xattach`, `objectscale`, `scalelistedi… |
| `offset` | V | SKILL.md#Commands used (parameters verified): …factor"}`, `offset`, `trim`, `fillet`, `stretch`, `array`,… |
| `oops` | V | reference/drafting-features.md#Erase and quick save (verif…: …` removed: `oops {}` (0.17, see `newer-comm… |
| `open` | V | reference/live-window.md#Live window: - `open {"path":"…dxf"}` → `{entities,index,warnings}` opened the … |
| `options` | n | reference/live-window.md#Round 6: live window (2026-10-26,…: …s dialogs (`options` returns the settings J… |
| `ortho` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …`, toggles `ortho\|grid\|otrack\|dynmode\|lwdis… |
| `osnap` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …tioncycling\|osnap {on,modes}` (`osmode` 3 f… |
| `otrack` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …`ortho\|grid\|otrack\|dynmode\|lwdisplay\|transp… |
| `overkill` | d | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …lean-up: `overkill {}` deleted an exact d… |

## p (22)

| id | status | note |
|---|---|---|
| `pagesetup` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …":false}`, `pagesetup {"layout","paper":"A3… |
| `pan` | V | reference/command-sweeps.md#Verified in detail, CadCraft p…: - pan. (4): `pan` `{"delta":[10,0]}` a… |
| `parameters` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `pasteblock` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …es,base}`, `pasteblock {at}` (inserts a blo… |
| `pasteclip` | d | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …opyclip` + `pasteclip {"at"}`, `draworder.f… |
| `pasteorig` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …`A$C…`), `pasteorig` only works into a DI… |
| `pdfbook` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …, S1, S2), `pdfbook` splits sheet frames in… |
| `pedit` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: … changed), `pedit {"option":"width"\|"fit"\|"… |
| `pickstyle` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …handles}`, `pickstyle {}`. |
| `pline` | V | SKILL.md#Commands used (parameters verified): …x,y],…]}`, `pline {"vertices":[…],"closed","width"}`, `cir… |
| `plot` | V | SKILL.md#Commands used (parameters verified): …"scale"}`, `plot`. |
| `plotstyle` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: `plotstyle {…}` assigns named styles to obj… |
| `plottermanager` | V | reference/command-sweeps.md#Verified in detail, CadCraft l…: - -plottermanager. (1): `-plottermanag… |
| `plotwindow` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `plotwindow {p1,p2}`, `plottermanager {acti… |
| `point` | V | SKILL.md#Commands used (parameters verified): …ry: `line {"points":[[x,y],…]}`, `pline {"vertices":[…],"c… |
| `polar` | V | reference/command-sweeps.md#Ten ids that were only named a…: - `polar {"on":false}` / `{"on":true}`: AUT… |
| `polygon` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …1","p2"}`, `polygon`, `xline`, `group {"nam… |
| `preview` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … devices), `preview {layout,paper,fit,width… |
| `properties` | V | reference/newer-commands.md#0.18.0 changes (verified headl…: - `properties.set` and `chprop` return `{… |
| `pspace` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …; `mspace`/`pspace`; `chspace {handles,to:"… |
| `publish` | V | reference/newer-commands.md#0.17 changes (verified headles…: `publish` takes `device` too but always wri… |
| `purge` | V | reference/schematics.md#Beginner wiring guide from a schem…: …lide, then `purge` (it also deletes layers … |

## q (4)

| id | status | note |
|---|---|---|
| `qdim` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …d tools: `qdim {"handles","at","mode":"ra… |
| `qpmode` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …encydisplay\|qpmode\|selectioncycling\|osnap {… |
| `qsave` | V | reference/drafting-features.md#Erase and quick save (verif…: - `qsave {"path":"q.dxf"}` writes the drawi… |
| `qselect` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …layer"]}`, `qselect {"type","property","ope… |

## r (16)

| id | status | note |
|---|---|---|
| `ray` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …multiple`, `ray`, `donut`, `copyclip` + `pa… |
| `recover` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …fs, `drawingrecovery {action:"list"}` (empt… |
| `rectang` | V | SKILL.md#CLI essentials (verified): - `--cmd 'rectang {"p1":[20,20],"p2":[60,50]}'`: the id, a space, th… |
| `redo` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … {count}`, `redo {count}`, `mredo {all:true… |
| `redraw` | V | reference/command-sweeps.md#Ten ids that were only named a…: …he reason: `redraw {}` (screen repaint only… |
| `refclose` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: … lists it, `refclose {"option":"save"}` wri… |
| `refedit` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: `refedit {"handle":insertHandle}` returns `… |
| `refset` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …rking set, `refset {}` lists it, `refclose … |
| `regen` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …\|up\|down`, `regen`, `regenall` |
| `regenall` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …, `regen`, `regenall` |
| `region` | d | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …Regions: `region {"handles"}` converts cl… |
| `reinit` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …rcle"}}` / `reinit {}`. |
| `rename` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …maining"); `rename` cannot rename layer 0 o… |
| `revcloud` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …linetype), `revcloud {"p1","p2"}`, `polygon… |
| `reverse` | d | reference/command-sweeps.md#Round 13: the remaining comman…: `reverse {handles}` |
| `rotate` | V | SKILL.md#Commands used (parameters verified): …`, `copy`, `rotate`, `mirror`, `scale {"handles","base","f… |

## s (21)

| id | status | note |
|---|---|---|
| `saveas` | V | reference/newer-commands.md#0.17 changes (verified headles…: - `saveas {"path","portableFonts":true}`*… |
| `scale` | V | SKILL.md#Commands used (parameters verified): … `mirror`, `scale {"handles","base","factor"}`, `offset`, … |
| `scalelistedit` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `script` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: … lines use `script {"text":"CIRCLE 50,50 5\… |
| `select` | V | reference/drafting-features.md#Erase and quick save (verif…: … erases the selection (`select {"handles":[… |
| `selectall` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …d, undo: `selectall` + `erase.selection`,… |
| `selectioncycling` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …play\|qpmode\|selectioncycling\|osnap {on,mode… |
| `selectsimilar` | n | reference/drafting-features.md#Round 7 (2026-10-26, headle…: …wo lines), `selectsimilar`, `id {"at"}`, `c… |
| `setvar` | d | reference/live-window.md#Round 6: live window (2026-10-26,…: … (set with `setvar`): clicks are exact worl… |
| `shapes` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …s,limit}`, `shapes {type}` (area, centroid,… |
| `share` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …only") and `share` (use `export` or `publis… |
| `snap` | V | reference/command-sweeps.md#Ten ids that were only named a…: - `snap {"on":true}`: SNAPMODE 0 -> 1, mess… |
| `solid` | V | reference/newer-commands.md#0.15 changes (2026-10-31; `sol…: - `solid {"points":[[x,y],…]}` draws a 2D s… |
| `spline` | V | SKILL.md#Commands used (parameters verified): …`ellipse`, `spline`, `point`, `hatch`. |
| `splinedit` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `status` | d | reference/command-sweeps.md#Ten ids that were only named a…: - `status {}` returns a text report: object… |
| `stretch` | V | SKILL.md#Commands used (parameters verified): … `fillet`, `stretch`, `array`, `explode` |
| `style` | V | SKILL.md#Commands used (parameters verified): …one first: `style {"name":"SCH","font":"Arial","height":0,… |
| `stylesmanager` | d | reference/drafting-features.md#Round 7 (2026-10-26, headle…: … tables: `stylesmanager {"action":"new","… |
| `subtract` | d | reference/drafting-features.md#Round 3 (2026-10-26, headle…: `subtract {"from":[h],"remove":[h]}` works |
| `sysvars` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …settings), `sysvars {}`, `drawing.inspect {… |

## t (14)

| id | status | note |
|---|---|---|
| `table` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …ups.list`, `table {"at","rows","cols","titl… |
| `tabledit` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …\|unmerge`, `tabledit {handle,row,col,text}`… |
| `tableexport` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …,"cols"}`, `tableexport {"handle","path":"t… |
| `tablestyle` | s | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …umented but not run: `xattach`, `objectscal… |
| `text` | V | SKILL.md#Commands used (parameters verified): `text {"at":[x,y],"text","height":2.6,"justify":"L\|C\|R\|M\|T… |
| `textedit` | V | reference/schematics.md#Beginner wiring guide from a schem…: … colours), `textedit {"handle","text"}` (ce… |
| `texts` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: `texts {}` lists attribute values with `tag… |
| `texttofront` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …ve\|under`, `texttofront {objects}` / `.text… |
| `thickness` | V | reference/drafting-features.md#Round 8 (2026-10-26; annota…: …rectangle, `thickness {"thickness":5}` sets… |
| `time` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …, GRASS…), `time {}`, toggles `ortho\|grid\|o… |
| `tolerance` | V | reference/drafting-features.md#Round 3 (2026-10-26, headle…: …"scale"}`; `tolerance {"at","symbol":"flatn… |
| `transparencydisplay` | n | reference/command-sweeps.md#Round 13: the remaining comman…: …e\|lwdisplay\|transparencydisplay\|qpmode\|sele… |
| `trim` | V | SKILL.md#Commands used (parameters verified): … `offset`, `trim`, `fillet`, `stretch`, `array`, `explode` |
| `txt2mtxt` | d | reference/drafting-features.md#Round 4 (2026-10-26, headle…: `txt2mtxt` needs a selection (fails "No tex… |

## u (7)

| id | status | note |
|---|---|---|
| `u` | d | reference/command-sweeps.md#Round 13: the remaining comman…: … clipboard, undo: `selectall` + `erase.se… |
| `undo` | V | reference/live-window.md#Round 9: a real drawing in the li…: …,-10), and `undo` restored them (verified b… |
| `ungroup` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: … `group` / `ungroup`. |
| `union` | n | reference/drafting-features.md#Round 3 (2026-10-26, headle…: `union`/`intersect` of OVERLAPPING regions … |
| `unisolateobjects` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …andles}` + `unisolateobjects {}`, `cutclip`… |
| `units` | V | reference/dwg-files.md#Round 12: two more AutoCAD DWGs, 20…: …r":25.4}`, `units {"lunits":2,"luprec":1,"i… |
| `usage` | d | reference/command-sweeps.md#Round 13: the remaining comman…: …erimeter), `usage {type:"layers"}` (used/un… |

## v (4)

| id | status | note |
|---|---|---|
| `view` | d | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …ave/list`, `view {"option":"save\|list"}`, `… |
| `vpclip` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …ved:1`); `vpclip` needs the viewport hand… |
| `vplayer` | V | reference/command-sweeps.md#Round 13: the remaining comman…: …t handles; `vplayer {handle,freeze:[layer]}… |
| `vports` | V | reference/command-sweeps.md#Round 13: the remaining comman…: … handle; `vports.3` etc. report tiles; `v… |

## w (2)

| id | status | note |
|---|---|---|
| `wblock` | V | SKILL.md#Commands used (parameters verified): …tation"}`, `wblock`. |
| `wipeout` | n | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …gree":3}`, `wipeout`, `point.multiple`, `ra… |

## x (7)

| id | status | note |
|---|---|---|
| `xattach` | s | reference/command-sweeps.md#Round 13: the remaining comman…: Not run … - Not run: `arc.continue` after an arc, `-p… |
| `xbind` | d | reference/drafting-features.md#Round 4 (2026-10-26, headle…: `xbind {"type":"layer","names":"REF\|LAYER"}… |
| `xclip` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: - `xclip` clips block/xref references o… |
| `xclipframe` | V | reference/newer-commands.md#0.17.1 changes (verified headl…: `xclipframe` 2 → 1 read back. |
| `xline` | V | reference/drafting-features.md#Round 2 (2026-10-26, headle…: …`polygon`, `xline`, `group {"name","handles… |
| `xopen` | d | reference/drafting-features.md#Round 4 (2026-10-26, headle…: `xopen {"name"}`, `refedit` untested. |
| `xref` | d | reference/drafting-features.md#Round 4 (2026-10-26, headle…: …handle and `xref` info), `xref {}` lists st… |

## z (1)

| id | status | note |
|---|---|---|
| `zoom` | V | SKILL.md#CLI essentials (verified): …hanged it (`zoom {"mode":"window","p1":[0,0],"p2":[420,297]}`), else… |
