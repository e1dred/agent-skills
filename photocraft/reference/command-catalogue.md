# PhotoCraft command catalogue (0.21.0)

Built 2026-11-06 from the skill's own text (SKILL.md, reference/ and tools/); no command was run and nothing was re-tested. Ids come from `photocraft-cli` 0.21.0 (993 ids); the skill's version label: last tested on photocraft-cli 0.21.0; evidence sections cite 0.13-0.21.0.
Status: **V** verified - the hit is under a heading naming verification or records an observed result (arrow, before/after, read-back, checked file, confirmed); **d** documented - named with parameters or usage, no recorded evidence; **n** named only - a bare list or command index; **s** skipped on purpose - the skill says skipped/not run/not tested/not exercised; **x** known no-op, broken or refused - the line says so; **V+** verified, but another line records a limit (refused or skipped in some state or version); the note quotes both. When a command has verified evidence anywhere, it counts as verified: a refusal or skip recorded elsewhere usually names a precondition or an older round.
Counts: V 910, V+ 49, d 1, n 0, s 31, x 2.

## actions (21)

| id | status | note |
|---|---|---|
| `actions.assignSet` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …eps:3}`) → `actions.assignSet {"action":"We… |
| `actions.conditional` | V | reference/everyday-edits.md#Image commands, selections, to…: …ed:true}`, `actions.conditional {"if":"hasS… |
| `actions.delete` | V | reference/everyday-edits.md#Image commands, selections, to…: …,played}`, `actions.delete {"action","step"… |
| `actions.dialog` | V | reference/everyday-edits.md#Image commands, selections, to…: …led:[0]}`, `actions.dialog {"action","step"… |
| `actions.get` | V | reference/everyday-edits.md#Image commands, selections, to…: …cording}`, `actions.get {"action"}` → `{ste… |
| `actions.insert` | V | reference/everyday-edits.md#Image commands, selections, to…: …:"blue"}`, `actions.insert {"action","id":"… |
| `actions.list` | V | reference/everyday-edits.md#Image commands, selections, to…: `actions.list` → `{actions:[{name,set,steps… |
| `actions.load` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: … document: `actions.load {"path"}` then `ac… |
| `actions.move` | V | reference/everyday-edits.md#Image commands, selections, to…: …p,steps}`, `actions.move {"action","step":1… |
| `actions.newSet` | V | reference/log.md#Log: …one added (`actions.newSet`), none removed, 41 parameter specs changed, all additi… |
| `actions.photoshopStep` | s | reference/everyday-edits.md#Image commands, selections, to…: Not run … - Not run: `actions.photoshopStep` (needs a… |
| `actions.play` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …th"}` then `actions.play {"action"}` → `{ra… |
| `actions.record` | V | reference/everyday-edits.md#Image commands, selections, to…: …Actions: `actions.record {"name":"Glow"}`… |
| `actions.rename` | V | reference/everyday-edits.md#Image commands, selections, to…: …s,color}`, `actions.rename {"action","name"… |
| `actions.save` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `actions.save {"path":"web.atn","set":"My A… |
| `actions.setColor` | V | reference/everyday-edits.md#Image commands, selections, to…: …,"name"}`, `actions.setColor {"action","col… |
| `actions.setHistory` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: - `actions.setHistory {"singleState":true… |
| `actions.setPlayback` | V | SKILL.md#Traps: …are not: `actions.setPlayback` and `history.options` read back correctly inside one |
| `actions.stop` | V | reference/everyday-edits.md#Image commands, selections, to…: …ommands… → `actions.stop` → `{action,steps:… |
| `actions.stopMessage` | V | reference/everyday-edits.md#Image commands, selections, to…: …ogs:[1]}`, `actions.stopMessage {"message",… |
| `actions.toggle` | V | reference/everyday-edits.md#Image commands, selections, to…: …,"to":0}`, `actions.toggle {"action","step"… |

## brush (18)

| id | status | note |
|---|---|---|
| `brush.defineFromSelection` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …{"path"}`, `brush.defineFromSelection {"nam… |
| `brush.get` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …g `*.list`/`brush.get`/`session.inspect`/`l… |
| `brush.mixer.clean` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …"}` first, `brush.mixer.clean {}` after (→ … |
| `brush.mixer.load` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …ark smear: `brush.mixer.load {"color":"#e63… |
| `brush.mixer.sample` | V | reference/everyday-edits.md#Newer commands and options (ve…: - `brush.mixer.sample {"points":[[x,y]]}`… |
| `brush.presets.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (8): `brush.presets.delete` removed t… |
| `brush.presets.deleteGroup` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `brush.presets.deleteGroup` deletes the gro… · limit: command-sweeps.md: Refused … - Refused with a reason on the default state (22; the reas… |
| `brush.presets.importAbr` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: … commands, `brush.presets.importAbr {"path"… |
| `brush.presets.importImage` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `brush.presets.importImage` `{"path":"tip.p… |
| `brush.presets.list` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …Presets: `brush.presets.list {}` → 36 bui… |
| `brush.presets.move` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `brush.presets.move` `{"name","group"}` put… |
| `brush.presets.moveGroup` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `brush.presets.moveGroup` `{"group":"G2","i… |
| `brush.presets.rename` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …ommands: `brush.presets.rename {"name","n… |
| `brush.presets.renameGroup` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `brush.presets.renameGroup` `{"group":"G1",… · limit: command-sweeps.md: Refused … `brush.presets.renameGroup` (invalid parameters for brush.pr… |
| `brush.presets.save` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: `brush.presets.save {"name":"My Marker","br… |
| `brush.presets.setCurrent` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `brush.presets.setCurrent` marks which pres… |
| `brush.presets.update` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ich preset `brush.presets.update {}` writes… |
| `brush.texturePattern` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …{"name"}`, `brush.texturePattern`. |

## channel (22)

| id | status | note |
|---|---|---|
| `channel.delete` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …o":0}` and `channel.delete {"channel":"A"}`… |
| `channel.duplicate` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `channel.duplicate {"channel":"red","name":… |
| `channel.list` | V | reference/workflows-and-tools.md#Paths and channels (verif…: … the whole `channel.list` (`alpha[]` with i… |
| `channel.merge` | s | reference/everyday-edits.md#Layer arrangement, shape combi…: `channel.merge {"mode":"rgb","documents":[…… |
| `channel.mergeSpot` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …or"}` then `channel.mergeSpot {}` → null, `… |
| `channel.move` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …e:false`), `channel.move {"channel":"B","to… |
| `channel.new` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: … made with `channel.new`) |
| `channel.newSpot` | V+ | reference/everyday-edits.md#Layer arrangement, shape combi…: … channel), `channel.newSpot {"name","color"… · limit: workflows-and-tools.md: Not run … Not run: `channel.newSpot/mergeSpot/split/merge/move/delete`… |
| `channel.options` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `channel.options {"channel":…,"color":"#00f… |
| `channel.rename` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `channel.rename {"channel":"Mask B","name":… |
| `channel.setVisible` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …hannels: `channel.setVisible {"channel":"… |
| `channel.split` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …`) → null, `channel.split {"closeOriginal":… |
| `channel.target` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `channel.target {"channel":"composite"}` or… |
| `channel.target.composite` | V | reference/workflows-and-tools.md#Paths and channels (verif…: …site"}` or `channel.target.composite {}` re… |
| `channel.target.layerMask` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …umbering), `channel.target.layerMask {}` ne… |
| `channel.target.slot3` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …}` → null, `channel.target.slot3 {}` target… |
| `channel.target.slot4` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (6): `channel.target.slot4` Cmd+4: ta… |
| `channel.target.slot5` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `channel.target.slot5` Cmd+5: targets the B… |
| `channel.target.slot6` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `channel.target.slot6` Cmd+6: targets alpha… |
| `channel.target.slot7` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `channel.target.slot7` Cmd+7: targets alpha… |
| `channel.target.slot8` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `channel.target.slot8` Cmd+8: targets alpha… |
| `channel.target.slot9` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `channel.target.slot9` Cmd+9: targets alpha… |

## cloneSource (5)

| id | status | note |
|---|---|---|
| `cloneSource.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ve source (`cloneSource.list` active 2, wit… |
| `cloneSource.overlay` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …overlay}`, `cloneSource.overlay {"show":tru… |
| `cloneSource.resetTransform` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …ity":40}`, `cloneSource.resetTransform {"in… |
| `cloneSource.select` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `cloneSource.select` `{"index":2… |
| `cloneSource.set` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: … slots): `cloneSource.set {"index":1,"sou… |

## color (1)

| id | status | note |
|---|---|---|
| `color.profileMismatch` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (1): `color.profileMismatch` acts on … |

## command (1)

| id | status | note |
|---|---|---|
| `command.list` | s | reference/command-sweeps.md#Round: every remaining command…: Not run on purpose … - Not run on purpose (33): `file.print*… |

## count (7)

| id | status | note |
|---|---|---|
| `count.add` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …"color"}`, `count.add {"x","y"}` → `{number… |
| `count.clear` | s | reference/workflows-and-tools.md#Slices, preset libraries,…: (`count.clear`/`deleteGroup` not run.) |
| `count.deleteGroup` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (1): `count.deleteGroup` `{}` deletes… |
| `count.move` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …Size":4}`, `count.move {"index":0,"to":[60,… |
| `count.newGroup` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …nt tool: `count.newGroup {"name","color"}… |
| `count.remove` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …[60,60]}`, `count.remove {"index":1}` |
| `count.setGroup` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …,groups}`, `count.setGroup {"name":"Seeds",… |

## document (11)

| id | status | note |
|---|---|---|
| `document.activate` | s | reference/command-sweeps.md#Round: every remaining command…: Not run on purpose … - Not run on purpose (33): `file.print*… |
| `document.inspect` | V | reference/live-mode.md#Live UI tools: pointer, tools, stra…: ….list` and `document.inspect` are NOT contr… |
| `document.move` | V | reference/command-sweeps.md#The last 28 command ids (2026-…: - `document.move {"document":0,"to":1}` reo… |
| `document.pixel` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `document.pixel {"x","y"}` and `document.sa… |
| `document.presets.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (3): `document.presets.delete` {delet… |
| `document.presets.get` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `document.presets.get` returns the preset p… |
| `document.presets.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `document.presets.list` lists the saved pre… |
| `document.presets.save` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …cuments: `document.presets.save {"name","… |
| `document.recent.add` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (1): `document.recent.add` `{"setting… · limit: command-sweeps.md: Refused … `document.recent.add` (invalid parameters for document.recen… |
| `document.recent.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ent entry (`document.recent.list` shows it … |
| `document.sampleColor` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …,"y"}` and `document.sampleColor {"x","y","… |

## edit (79)

| id | status | note |
|---|---|---|
| `edit.assignProfile` | V | reference/everyday-edits.md#Layer management, edit and fil…: …icc etc.), `edit.assignProfile {"profile":"… |
| `edit.autoAlignLayers` | V+ | reference/workflows-and-tools.md#Photomerge, HDR merge, au…: …yers {}` → `edit.autoAlignLayers {"projecti… · limit: everyday-edits.md: Not run: `edit.autoAlignLayers/autoBlendLayers` (need overla… |
| `edit.autoBlendLayers` | V | reference/workflows-and-tools.md#Photomerge, HDR merge, au…: …o-blend: `edit.autoBlendLayers {"method":… |
| `edit.checkSpelling` | V | reference/everyday-edits.md#Layer management, edit and fil…: …placeText`/`edit.checkSpelling` "the docume… |
| `edit.clear` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …ommands: `edit.clear {}` (selection clear… |
| `edit.colorSettings` | V | reference/everyday-edits.md#Layer management, edit and fil…: …profile}`, `edit.colorSettings {}`. |
| `edit.contentAwareFill` | V | reference/everyday-edits.md#Retouching, compositing and se…: `edit.contentAwareFill {"output":"new","col… |
| `edit.contentAwareScale` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …nd type: `edit.contentAwareScale {"width"… |
| `edit.convertToProfile` | V | reference/everyday-edits.md#Layer management, edit and fil…: …lay-p3"}`, `edit.convertToProfile {"profile… |
| `edit.copy` | V | reference/everyday-edits.md#Layer management, edit and fil…: … Edit: `edit.copy`/`copyMerged` → `{bou… |
| `edit.copyMerged` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …{bounds}`, `edit.copyMerged {}` → `{bounds}… |
| `edit.cut` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: … cleared), `edit.cut {}` → `{bounds}`, `edi… |
| `edit.defineBrushPreset` | V | reference/everyday-edits.md#Layer management, edit and fil…: … process), `edit.defineBrushPreset {"name"}… |
| `edit.defineCustomShape` | V | reference/everyday-edits.md#Layer management, edit and fil…: …,height}`, `edit.defineCustomShape {"name",… |
| `edit.definePattern` | V | reference/everyday-edits.md#Layer management, edit and fil…: `edit.definePattern {"name":"Tile1"}` (from… |
| `edit.deleteAndFillSelection` | V | reference/everyday-edits.md#Layer management, edit and fil…: …Preserve`, `edit.deleteAndFillSelection` → … |
| `edit.fade` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …{bounds}`, `edit.fade {"opacity":50,"mode":… |
| `edit.fill` | V | reference/everyday-edits.md#Newer commands and options (ve…: `edit.fill {"target":"filterMask"}` likewis… |
| `edit.fillBackground` | V | reference/everyday-edits.md#Layer management, edit and fil…: …ape layer, `edit.fillBackground`, `edit.fil… |
| `edit.fillBackgroundPreserve` | V | reference/everyday-edits.md#Layer management, edit and fil…: …Preserve`, `edit.fillBackgroundPreserve`, `… |
| `edit.fillForeground` | V | reference/live-mode.md#Live mode and removing a background…: `edit.fillForeground` with `target:"mask"… |
| `edit.fillForegroundPreserve` | V | reference/everyday-edits.md#Layer management, edit and fil…: …ckground`, `edit.fillForegroundPreserve`, `… |
| `edit.fillHistory` | V | reference/everyday-edits.md#Layer management, edit and fil…: …,window}`, `edit.fillHistory`. |
| `edit.findAndReplaceText` | V | reference/everyday-edits.md#Layer management, edit and fil…: `edit.findAndReplaceText`/`edit.checkSpelli… |
| `edit.installedProfiles` | V | reference/everyday-edits.md#Layer management, edit and fil…: …c2020…]}`, `edit.installedProfiles {}` (sca… |
| `edit.keyboardShortcuts` | s | reference/everyday-edits.md#Layer management, edit and fil…: Not run: `edit.autoAlignLayers/autoBlendLay… |
| `edit.menus` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (2): `edit.menus` `{"hide":["filter.b… |
| `edit.paste` | V+ | reference/everyday-edits.md#Everyday layer and edit comman…: …copy {}` → `edit.paste {"center":[300,230]}… · limit: workflows-and-tools.md: …(spec only, not run): `file.close {"save":"discard\|ask"}`, `… |
| `edit.pasteSpecial.pasteInPlace` | V | reference/everyday-edits.md#Layer management, edit and fil…: …{bounds}`, `edit.pasteSpecial.pasteInPlace`… |
| `edit.pasteSpecial.pasteInto` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …l. (2): `edit.pasteSpecial.pasteInto` co… |
| `edit.pasteSpecial.pasteOutside` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.pasteSpecial.pasteOutside` same setup… |
| `edit.perspectiveWarp` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …mal"}` and `edit.perspectiveWarp {"planes":… |
| `edit.preferences.cursors` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (16): `edit.preferences.cursors` READ-… |
| `edit.preferences.enhancedControls` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.enhancedControls` READ-ON… |
| `edit.preferences.export` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …ng:true`), `edit.preferences.export {}` → `… |
| `edit.preferences.fileHandling` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.fileHandling` READ-ONLY p… |
| `edit.preferences.general` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …e as JSON: `edit.preferences.general {}` → … |
| `edit.preferences.guidesGridAndSlices` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.guidesGridAndSlices` READ… |
| `edit.preferences.historyLog` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.historyLog` READ-ONLY pag… |
| `edit.preferences.integrations` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.integrations` READ-ONLY p… |
| `edit.preferences.interface` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.interface` READ-ONLY page… |
| `edit.preferences.performance` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.performance` READ-ONLY pa… |
| `edit.preferences.plugIns` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.plugIns` READ-ONLY page: … |
| `edit.preferences.rawDefaults` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.rawDefaults` READ-ONLY pa… |
| `edit.preferences.scratchDisks` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.scratchDisks` READ-ONLY p… |
| `edit.preferences.tools` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.tools` READ-ONLY page: `{… |
| `edit.preferences.transparencyAndGamut` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.transparencyAndGamut` REA… |
| `edit.preferences.type` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.type` READ-ONLY page: `{s… |
| `edit.preferences.unitsAndRulers` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.unitsAndRulers` READ-ONLY… |
| `edit.preferences.workspace` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.preferences.workspace` READ-ONLY page… |
| `edit.presets.exportImportPresets` | s | reference/everyday-edits.md#Layer management, edit and fil…: Not run: `edit.autoAlignLayers/autoBlendLay… |
| `edit.presets.migratePresets` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (1): `edit.presets.migratePresets` re… · limit: command-sweeps.md: Refused … `edit.presets.migratePresets` (invalid parameters for edit.p… |
| `edit.presets.presetManager` | V | reference/everyday-edits.md#Layer management, edit and fil…: `edit.presets.presetManager {"action":"list… |
| `edit.profileInfo` | V | reference/everyday-edits.md#Layer management, edit and fil…: Colour: `edit.profileInfo {}` → `{builtins:… |
| `edit.puppetWarp` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …el layers: `edit.puppetWarp {"pins":[{"src"… |
| `edit.purge.all` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `edit.purge.all`, `edit.purge.histories`, `… |
| `edit.purge.clipboard` | V | reference/everyday-edits.md#Layer management, edit and fil…: `edit.purge.clipboard\|histories\|undo\|videoC… |
| `edit.purge.histories` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …urge.all`, `edit.purge.histories`, `edit.pu… |
| `edit.purge.undo` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …istories`, `edit.purge.undo` say "nothing t… |
| `edit.purge.videoCache` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `edit.purge.videoCache` → `{bytes:0,message… |
| `edit.redo` | V | reference/everyday-edits.md#Layer management, edit and fil…: …astState`, `edit.redo` ("nothing to redo"). |
| `edit.stroke` | V | reference/everyday-edits.md#Everyday layer and edit comman…: - `edit.stroke {"width":6,"color":"#00000… |
| `edit.toggleLastState` | V | reference/everyday-edits.md#Layer management, edit and fil…: `edit.toggleLastState`, `edit.redo` ("nothi… |
| `edit.toolbar` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.toolbar` `{"hidden":["eraser"]}` -> `… |
| `edit.transform` | V+ | reference/log.md#Log: …ffers, and `edit.transform` and `edit.transform.rotate90Cw` now also print `layers… · limit: workflows-and-tools.md: …(spec only, not run): `file.close {"save":"discard\|ask"}`, `… |
| `edit.transform.again` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `edit.transform.again` / `againCopy` fail… |
| `edit.transform.againCopy` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `edit.transform.againCopy` "there is no tra… |
| `edit.transform.flipHorizontal` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `edit.transform.flipHorizontal/Vertical`, `… |
| `edit.transform.flipVertical` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …d warps: `edit.transform.flipVertical`, `… |
| `edit.transform.removeWarpSplit` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …m. (7): `edit.transform.removeWarpSplit`… |
| `edit.transform.rotate180` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.transform.rotate180` same bar stays 1… |
| `edit.transform.rotate90Ccw` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.transform.rotate90Ccw` same bar: 40x1… |
| `edit.transform.rotate90Cw` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.transform.rotate90Cw` turns the activ… |
| `edit.transform.splitWarpCrosswise` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.transform.splitWarpCrosswise` same wa… |
| `edit.transform.splitWarpHorizontally` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.transform.splitWarpHorizontally` with… |
| `edit.transform.splitWarpVertically` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `edit.transform.splitWarpVertically` same w… |
| `edit.transform.warp` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `edit.transform.warp {"style":"arc","value"… |
| `edit.transform.warpGrid` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …rt object: `edit.transform.warpGrid {"size"… |
| `edit.undo` | V | reference/everyday-edits.md#Everyday layer and edit comman…: …` (same as `edit.undo` / `edit.redo`) retur… |

## file (59)

| id | status | note |
|---|---|---|
| `file.approveMemory` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: `file.approveMemory {id}` answers a prompt … |
| `file.automate.batch` | V+ | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: - `file.automate.batch` (and `createDroplet… · limit: workflows-and-tools.md: Not run … - Not run: `file.automate.cropAndStraightenPhotos` (needs a … |
| `file.automate.conditionalModeChange` | s | reference/workflows-and-tools.md#Photomerge, HDR merge, au…: Not run … - Not run: `file.automate.cropAndStraighten… |
| `file.automate.contactSheetII` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: … 500×333), `file.automate.contactSheetII {"… |
| `file.automate.createDroplet` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: Droplets: `file.automate.createDroplet {"pa… |
| `file.automate.cropAndStraightenPhotos` | V+ | reference/live-mode.md#Live UI tools: pointer, tools, stra…: - `file.automate.cropAndStraightenPhotos … · limit: workflows-and-tools.md: Not run … - Not run: `file.automate.cropAndStraightenPhotos` (needs a … |
| `file.automate.fitImage` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …utomation: `file.automate.fitImage {"width"… |
| `file.automate.lensCorrection` | s | reference/workflows-and-tools.md#Photomerge, HDR merge, au…: Not run … - Not run: `file.automate.cropAndStraighten… |
| `file.automate.mergeToHdrPro` | V | reference/workflows-and-tools.md#Photomerge, HDR merge, au…: …R merge: `file.automate.mergeToHdrPro {"p… |
| `file.automate.photomerge` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `file.automate.photomerge {"paths":"DIR","l… |
| `file.automate.runDroplet` | s | reference/workflows-and-tools.md#Photomerge, HDR merge, au…: Not run … - Not run: `file.automate.cropAndStraighten… |
| `file.close` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.close` returned to it · limit: command-sweeps.md: Not run on purpose … - Not run on purpose (33): `file.print*`, `file.open`, `… |
| `file.closeAll` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (7): `file.closeAll` `{closed:2}`, `s… · limit: command-sweeps.md: Refused … - Refused: `file.closeAll` (error: no document open) |
| `file.closeOthers` | V | reference/command-sweeps.md#The last 28 command ids (2026-…: …e` first); `file.closeOthers {"document":0}… |
| `file.export.artboardsToFiles` | V | reference/everyday-edits.md#Layer management, edit and fil…: … family: `file.export.artboardsToFiles {"… |
| `file.export.artboardsToPdf` | s | reference/everyday-edits.md#Layer arrangement, shape combi…: Not run … - Not run: `layer.new.artboardFromLayers`, … |
| `file.export.colorLookupTables` | V | reference/everyday-edits.md#Layer management, edit and fil…: …,height}`, `file.export.colorLookupTables {… |
| `file.export.dataSetsAsFiles` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …d,index}`, `file.export.dataSetsAsFiles {"d… |
| `file.export.exportPreferences` | V | reference/everyday-edits.md#Layer management, edit and fil…: …undingBox, `file.export.exportPreferences {… |
| `file.export.layerCompsToFiles` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (2): `file.export.layerCompsToFiles` … |
| `file.export.layersToFiles` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …, alpha of `file.export.layersToFiles` outp… |
| `file.export.pathsToIllustrator` | V | reference/everyday-edits.md#Layer management, edit and fil…: `file.export.pathsToIllustrator {"path":"p.… |
| `file.export.presets.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (2): `file.export.presets.delete` `{d… |
| `file.export.presets.get` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.export.presets.get` `{"name":"E1"}` r… |
| `file.export.presets.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.export.presets.list` then empty |
| `file.export.presets.save` | V | reference/everyday-edits.md#Layer management, edit and fil…: `file.export.presets.save {"name":"Web","se… |
| `file.export.quickExport` | V | reference/everyday-edits.md#Retouching, compositing and se…: … export: `file.export.quickExport {"path"… |
| `file.export.renderVideo` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …ayer` then `file.export.renderVideo {"dir":… |
| `file.export.saveForWebLegacy` | V | reference/everyday-edits.md#Layer management, edit and fil…: …etadata…), `file.export.saveForWebLegacy {"… |
| `file.exrParts` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.exrParts` on a 64x64 32-bit EXR writt… · limit: command-sweeps.md: Refused … `file.exrParts` (invalid parameters for file.exrParts: missi… |
| `file.fileInfo` | V | reference/everyday-edits.md#Layer management, edit and fil…: Scripts: `file.fileInfo {"title","author","… |
| `file.generate.imageAssets` | s | reference/everyday-edits.md#Layer management, edit and fil…: Not run … - Not run: `file.openAs/placeLinked/closeAl… |
| `file.import.notes` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (1): `file.import.notes` `{"path":ABS… · limit: command-sweeps.md: Refused … `file.import.notes` (swap.png has no notes) |
| `file.import.variableDataSets` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `file.import.variableDataSets {"path":"ds.c… |
| `file.import.videoFramesToLayers` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …ew odds: `file.import.videoFramesToLayers… |
| `file.import.wiaSupport` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `file.import.wiaSupport {}` → `{available:f… |
| `file.new` | V | SKILL.md#CLI essentials (verified): `file.new` params: `width`, `height`, `mode`, `depth`, `background` … |
| `file.newFromClipboard` | s | reference/command-sweeps.md#Round: every remaining command…: Not run on purpose … - Not run on purpose (33): `file.print*… |
| `file.openAs` | V+ | reference/workflows-and-tools.md#New in 0.20.2: action his…: `file.openAs` gains `approveHighMemory`. · limit: everyday-edits.md: Not run … - Not run: `file.openAs/placeLinked/closeAll`, printing, EXR… |
| `file.openExrParts` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.openExrParts` needs at least one `"pa… · limit: command-sweeps.md: Refused … `file.openExrParts` (error: `file.openExrParts`: /nonexisten… |
| `file.package` | V | reference/everyday-edits.md#Layer management, edit and fil…: …own file), `file.package {"dir"}` → `&lt;dir&gt;/… |
| `file.placeEmbedded` | V | reference/everyday-edits.md#Everyday photo edits (verified…: … / logo: `file.placeEmbedded {"path":"/ab… |
| `file.placeLinked` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.placeLinked` `{"path":ABSOLUTE,"cente… |
| `file.print` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: Then `file.print {"printer":"Virtual_PDF","… · limit: command-sweeps.md: Not run on purpose … - Not run on purpose (33): `file.print*`, `file.open`, `… |
| `file.print.page` | s | reference/command-sweeps.md#The last 28 command ids (2026-…: Skipped on purpose … - Skipped on purpose (they print): `fil… |
| `file.print.printers` | V | reference/command-sweeps.md#The last 28 command ids (2026-…: …nters` and `file.print.printers` → `{printe… |
| `file.printOneCopy` | s | reference/command-sweeps.md#The last 28 command ids (2026-…: Skipped on purpose … - Skipped on purpose (they print): `fil… |
| `file.printers` | V | reference/command-sweeps.md#The last 28 command ids (2026-…: …d earlier; `file.printers` and `file.print.… |
| `file.revealInFinder` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.revealInFinder` `{"dryRun":true}` ret… · limit: command-sweeps.md: Refused … `file.revealInFinder` (invalid parameters for file.revealInF… |
| `file.revert` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `file.revert` reloaded the saved .pcraft (`… · limit: command-sweeps.md: Refused … `file.revert` (command file.revert is not available right no… |
| `file.saveACopy` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: … document (`file.saveACopy … overwrite`, re… |
| `file.scripts.browse` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `file.scripts.browse {}` needs `path`, `scr… |
| `file.scripts.deleteAllEmptyLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: …`camera`), `file.scripts.deleteAllEmptyLaye… |
| `file.scripts.flattenAllLayerEffects` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `file.scripts.flattenAllLayerEffects {}` → … |
| `file.scripts.flattenAllMasks` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …tened:0}`, `file.scripts.flattenAllMasks {}… |
| `file.scripts.imageProcessor` | V | reference/everyday-edits.md#Layer management, edit and fil…: `file.scripts.imageProcessor {"input":[file… |
| `file.scripts.loadFilesIntoStack` | V | reference/everyday-edits.md#Layer management, edit and fil…: …`{flattened,skipped}`, `file.scripts.loadFi… |
| `file.scripts.scriptEventsManager` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `file.scripts.scriptEventsManager {}` → `{b… |
| `file.scripts.statistics` | s | reference/everyday-edits.md#Layer management, edit and fil…: …,errors}`, `file.scripts.statistics` needs … |

## filter (124)

| id | status | note |
|---|---|---|
| `filter.adaptiveWideAngle` | s | reference/workflows-and-tools.md#Filter families, layer co…: Not run … - Not run: the 47 `filter.gallery.*` artist… |
| `filter.blur.average` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (10): `filter.blur.average` one flat c… |
| `filter.blur.blur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.blur` very slight at defaults |
| `filter.blur.blurMore` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.blurMore` slight at defaults |
| `filter.blur.boxBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.boxBlur` slight at defaults |
| `filter.blur.gaussianBlur` | V | SKILL.md#CLI essentials (verified): ["filter.blur.gaussianBlur",{"radius":2}]]`); output name = input na… |
| `filter.blur.lensBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.lensBlur` strong out-of-focus … |
| `filter.blur.motionBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.motionBlur` slight horizontal … |
| `filter.blur.radialBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.radialBlur` spin blur around t… |
| `filter.blur.shapeBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.shapeBlur` strong soft blur |
| `filter.blur.smartBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.smartBlur` slight, edge-preser… |
| `filter.blur.surfaceBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blur.surfaceBlur` slight smoothing. |
| `filter.blurGallery.fieldBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …y. (4): `filter.blurGallery.fieldBlur` s… |
| `filter.blurGallery.irisBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blurGallery.irisBlur` blur with a s… |
| `filter.blurGallery.pathBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blurGallery.pathBlur` strong horizo… |
| `filter.blurGallery.spinBlur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.blurGallery.spinBlur` slight rotati… |
| `filter.blurGallery.tiltShift` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …rtion"…}`, `filter.blurGallery.tiltShift {"… |
| `filter.cameraRaw` | V | reference/everyday-edits.md#Newer commands and options (ve…: - `filter.cameraRaw` now acts on `shado… |
| `filter.convertForSmartFilters` | x | reference/workflows-and-tools.md#Filter families, layer co…: `filter.convertForSmartFilters` is refused … |
| `filter.distort.displace` | V | reference/workflows-and-tools.md#Filter families, layer co…: - `filter.distort.displace` needs `mapPath`… |
| `filter.distort.pinch` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (7): `filter.distort.pinch` slight pi… |
| `filter.distort.polarCoordinates` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.distort.polarCoordinates` circular … |
| `filter.distort.ripple` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.distort.ripple` wavy ripple |
| `filter.distort.shear` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.distort.shear` barely visible at de… |
| `filter.distort.spherize` | V | reference/live-mode.md#Live session and wider toolbox (ver…: …ng true) → `filter.distort.spherize {"amoun… |
| `filter.distort.twirl` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.distort.twirl` swirl around the cen… |
| `filter.distort.wave` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.distort.wave` strong wavy distortio… |
| `filter.distort.zigZag` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.distort.zigZag` barely visible at d… |
| `filter.filterGallery` | s | reference/workflows-and-tools.md#Filter families, layer co…: Not run … - Not run: the 47 `filter.gallery.*` artist… |
| `filter.gallery.accentedEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (47): `filter.gallery.accentedEdges` e… |
| `filter.gallery.angledStrokes` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.angledStrokes` posterized d… |
| `filter.gallery.basRelief` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.basRelief` grey embossed re… |
| `filter.gallery.chalkCharcoal` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.chalkCharcoal` grey chalk/c… |
| `filter.gallery.charcoal` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.charcoal` black with white … |
| `filter.gallery.chrome` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.chrome` liquid-metal black/… |
| `filter.gallery.coloredPencil` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.coloredPencil` light crossh… |
| `filter.gallery.conteCrayon` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.conteCrayon` dark crayon st… |
| `filter.gallery.craquelure` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.craquelure` crack network o… |
| `filter.gallery.crosshatch` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.crosshatch` subtle crosshat… |
| `filter.gallery.cutout` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.cutout` flat posterized col… |
| `filter.gallery.darkStrokes` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.darkStrokes` darker, higher… |
| `filter.gallery.diffuseGlow` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.diffuseGlow` soft bloom plu… |
| `filter.gallery.dryBrush` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.dryBrush` posterized dry-br… |
| `filter.gallery.filmGrain` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.filmGrain` fine film grain |
| `filter.gallery.fresco` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.fresco` dark, contrasty pai… |
| `filter.gallery.glass` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.glass` refracted, wobbly gl… |
| `filter.gallery.glowingEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.glowingEdges` neon edges on… |
| `filter.gallery.grain` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.grain` coarse coloured grai… |
| `filter.gallery.graphicPen` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.graphicPen` black and white… |
| `filter.gallery.halftonePattern` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.halftonePattern` grey dot s… |
| `filter.gallery.inkOutlines` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.inkOutlines` slightly darke… |
| `filter.gallery.mosaicTiles` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.mosaicTiles` tile grid with… |
| `filter.gallery.neonGlow` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.neonGlow` blue-tinted glow |
| `filter.gallery.notePaper` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.notePaper` black/white embo… |
| `filter.gallery.oceanRipple` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.oceanRipple` wavy ripple di… |
| `filter.gallery.paintDaubs` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.paintDaubs` blocky daubed s… |
| `filter.gallery.paletteKnife` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.paletteKnife` flat knife-li… |
| `filter.gallery.patchwork` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.patchwork` square tile mosa… |
| `filter.gallery.photocopy` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.photocopy` black ink lines … |
| `filter.gallery.plaster` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.plaster` grey plaster relie… |
| `filter.gallery.plasticWrap` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.plasticWrap` glossy plastic… |
| `filter.gallery.posterEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.posterEdges` posterized col… |
| `filter.gallery.reticulation` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.reticulation` black/white s… |
| `filter.gallery.roughPastels` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.roughPastels` pastel stroke… |
| `filter.gallery.smudgeStick` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.smudgeStick` soft smeared l… |
| `filter.gallery.spatter` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.spatter` spray speckle edge |
| `filter.gallery.sponge` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.sponge` dabbed blocky textu… |
| `filter.gallery.sprayedStrokes` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.sprayedStrokes` directional… |
| `filter.gallery.stainedGlass` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.stainedGlass` cell mosaic w… |
| `filter.gallery.stamp` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.stamp` two-tone black/white… |
| `filter.gallery.sumiE` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.sumiE` very dark ink-wash b… |
| `filter.gallery.texturizer` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.texturizer` canvas texture |
| `filter.gallery.tornEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.tornEdges` two-tone with to… |
| `filter.gallery.underpainting` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.underpainting` soft blur wi… |
| `filter.gallery.waterPaper` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.waterPaper` fibre paper tex… |
| `filter.gallery.watercolor` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.gallery.watercolor` soft painted wa… |
| `filter.lastFilter` | s | reference/workflows-and-tools.md#Filter families, layer co…: Not run … - Not run: the 47 `filter.gallery.*` artist… |
| `filter.lensCorrection` | V | reference/live-mode.md#Live UI tools: pointer, tools, stra…: - `filter.lensCorrection {"profile":"gene… |
| `filter.liquify` | V | reference/everyday-edits.md#Retouching, compositing and se…: …Liquify: `filter.liquify {"strokes":[{"to… |
| `filter.noise.addNoise` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …ngth":4}`, `filter.noise.addNoise {"amount"… |
| `filter.noise.despeckle` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (3): `filter.noise.despeckle` no visi… |
| `filter.noise.dustAndScratches` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.noise.dustAndScratches` slight smoo… |
| `filter.noise.median` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.noise.median` slight smoothing. |
| `filter.noise.reduceNoise` | V | reference/everyday-edits.md#Everyday photo edits (verified…: … / noise \| `filter.noise.reduceNoise {"stre… |
| `filter.other.colorToAlpha` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (6): `filter.other.colorToAlpha` whit… |
| `filter.other.custom` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.other.custom` no visible change wit… |
| `filter.other.highPass` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.other.highPass` grey with only edge… |
| `filter.other.hsbHsl` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.other.hsbHsl` channels reinterprete… |
| `filter.other.maximum` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.other.maximum` slightly lighter, th… |
| `filter.other.minimum` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.other.minimum` slightly darker, thi… |
| `filter.other.offset` | V | reference/workflows-and-tools.md#Filter families, layer co…: …"angle"}`, `filter.other.offset {"horizonta… |
| `filter.pixelate.colorHalftone` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (7): `filter.pixelate.colorHalftone` … |
| `filter.pixelate.crystallize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.pixelate.crystallize` irregular cry… |
| `filter.pixelate.facet` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.pixelate.facet` slight faceting |
| `filter.pixelate.fragment` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.pixelate.fragment` offset ghost cop… |
| `filter.pixelate.mezzotint` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.pixelate.mezzotint` coloured noise,… |
| `filter.pixelate.mosaic` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.pixelate.mosaic` large square pixel… |
| `filter.pixelate.pointillize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.pixelate.pointillize` white-ish dot… |
| `filter.render.clouds` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (6): `filter.render.clouds` replaces … |
| `filter.render.differenceClouds` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.render.differenceClouds` cloud nois… |
| `filter.render.fibers` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.render.fibers` black/white vertical… |
| `filter.render.flame` | V | reference/workflows-and-tools.md#Filter families, layer co…: …pe 1..34), `filter.render.flame {}` (a flam… |
| `filter.render.lensFlare` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.render.lensFlare` flare with rays, … |
| `filter.render.lightingEffects` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.render.lightingEffects` spotlight: … |
| `filter.render.pictureFrame` | V | reference/workflows-and-tools.md#Filter families, layer co…: `filter.render.pictureFrame {"frame":"waves… |
| `filter.render.relight` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.render.relight` orange-yellow relit… |
| `filter.render.tree` | V | reference/workflows-and-tools.md#Filter families, layer co…: …imitives), `filter.render.tree {"baseTreeTy… |
| `filter.sharpen.sharpen` | d | SKILL.md#Commands that worked (exact parameter formats): …dius":2}`, `filter.sharpen.sharpen {}`. |
| `filter.sharpen.sharpenEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …n. (2): `filter.sharpen.sharpenEdges` sl… |
| `filter.sharpen.sharpenMore` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.sharpen.sharpenMore` slight sharpen… |
| `filter.sharpen.smartSharpen` | V | reference/everyday-edits.md#Everyday layer and edit comman…: …as`) and `filter.sharpen.smartSharpen {"a… |
| `filter.sharpen.unsharpMask` | V | reference/everyday-edits.md#Everyday photo edits (verified…: … sharpen \| `filter.sharpen.unsharpMask {"am… |
| `filter.stylize.diffuse` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (8): `filter.stylize.diffuse` slight … |
| `filter.stylize.emboss` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.emboss` grey embossed relie… |
| `filter.stylize.extrude` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.extrude` 3D block/pyramid o… |
| `filter.stylize.findEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.findEdges` white with colou… |
| `filter.stylize.oilPaint` | V | reference/live-mode.md#Live session and wider toolbox (ver…: `filter.stylize.oilPaint {}` (stylization 4… |
| `filter.stylize.solarize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.solarize` false colours in … |
| `filter.stylize.tiles` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.tiles` tile offsets with wh… |
| `filter.stylize.traceContour` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.traceContour` white with co… |
| `filter.stylize.wind` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.stylize.wind` slight horizontal str… |
| `filter.vanishingPoint` | s | reference/workflows-and-tools.md#Filter families, layer co…: Not run … - Not run: the 47 `filter.gallery.*` artist… |
| `filter.video.deInterlace` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …o. (2): `filter.video.deInterlace` no vi… |
| `filter.video.ntscColors` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `filter.video.ntscColors` no visible change… |

## gradient (12)

| id | status | note |
|---|---|---|
| `gradient.fill.create` | V | reference/everyday-edits.md#Everyday layer and edit comman…: - `gradient.fill.create {"from":[200,0],"… |
| `gradient.fill.get` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …earlier) → `gradient.fill.get {}` → `{style… |
| `gradient.fill.set` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …dpoints}`, `gradient.fill.set {"angle":45,"… |
| `gradient.fill.stop` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …om angle), `gradient.fill.stop {"action":"c… |
| `gradient.presets.apply` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …up,name}`, `gradient.presets.apply {"preset… |
| `gradient.presets.edit` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …ll layer), `gradient.presets.edit {"action"… |
| `gradient.presets.importGrd` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (1): `gradient.presets.importGrd` a r… · limit: command-sweeps.md: Refused … `gradient.presets.importGrd` (invalid parameters for gradien… |
| `gradient.presets.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ex strings `gradient.presets.list` prints |
| `gradient.presets.new` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: … Basics…), `gradient.presets.new {"name","s… |
| `gradient.presets.reset` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (1): `gradient.presets.reset` after `… |
| `gradient.presets.select` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: use `gradient.presets.select {"preset"}` fi… |
| `gradient.presets.stop` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `gradient.presets.stop {"action":"add","l… |

## help (1)

| id | status | note |
|---|---|---|
| `help.checkForUpdates` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: …xportAsl`, `help.checkForUpdates`, `updates… |

## history (14)

| id | status | note |
|---|---|---|
| `history.clear` | V | reference/workflows-and-tools.md#Filter families, layer co…: `history.clear` drops the old states (Edit … |
| `history.deleteSnapshot` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …y. (3): `history.deleteSnapshot` `{"snap… |
| `history.deleteState` | s | reference/workflows-and-tools.md#Filter families, layer co…: Not run … - Not run: the 47 `filter.gallery.*` artist… |
| `history.newDocument` | V | reference/workflows-and-tools.md#Filter families, layer co…: Trap: `history.newDocument {"name"}` ma… |
| `history.newSnapshot` | V | reference/everyday-edits.md#Newer commands and options (ve…: Checked by `history.newSnapshot`, then `ima… |
| `history.options` | V | SKILL.md#Traps: …yback` and `history.options` read back correctly inside one |
| `history.redo` | V | reference/everyday-edits.md#Everyday layer and edit comman…: …undo {}` / `history.redo {}` (same as `edit… |
| `history.renameSnapshot` | x | reference/workflows-and-tools.md#Filter families, layer co…: … following `history.renameSnapshot` on the … |
| `history.selectSnapshot` | V | reference/workflows-and-tools.md#Filter families, layer co…: `history.selectSnapshot {"snapshot":1}` ret… |
| `history.selectState` | V | reference/workflows-and-tools.md#Filter families, layer co…: `history.selectState {"state":1}` (0 = olde… |
| `history.setSource` | V | reference/workflows-and-tools.md#Filter families, layer co…: `history.setSource {"state":2}` then `paint… |
| `history.stepBackward` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …undo step (`history.stepBackward` brought i… |
| `history.stepForward` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `history.stepForward` back to state 1: Rect… |
| `history.undo` | V | reference/everyday-edits.md#Everyday layer and edit comman…: … change: `history.undo {}` / `history.red… |

## image (66)

| id | status | note |
|---|---|---|
| `image.adjustments.blackWhite` | V | reference/everyday-edits.md#Everyday photo edits (verified…: \| B&W \| `image.adjustments.blackWhite {}` (… |
| `image.adjustments.brightnessContrast` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …contrast \| `image.adjustments.brightnessCon… |
| `image.adjustments.channelMixer` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: … photo): `image.adjustments.channelMixer … |
| `image.adjustments.colorBalance` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (9): `image.adjustments.colorBalance`… |
| `image.adjustments.colorLookup` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.colorLookup` lut tealOra… |
| `image.adjustments.colorLookup.list` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …lour looks `image.adjustments.colorLookup.l… |
| `image.adjustments.curves` | V | reference/everyday-edits.md#Everyday photo edits (verified…: \| curves \| `image.adjustments.curves {"poin… |
| `image.adjustments.desaturate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.desaturate` greyscale |
| `image.adjustments.equalize` | V | reference/everyday-edits.md#Image commands, selections, to…: …Color {}`, `image.adjustments.equalize\|inve… |
| `image.adjustments.exposure` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …exposure \| `image.adjustments.exposure {"ex… |
| `image.adjustments.gradientMap` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.gradientMap` duotone: da… |
| `image.adjustments.hdrToning` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.hdrToning` stronger loca… |
| `image.adjustments.hueSaturation` | V | reference/everyday-edits.md#Everyday layer and edit comman…: - `image.adjustments.hueSaturation {"hue"… |
| `image.adjustments.invert` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.invert` colour negative |
| `image.adjustments.levels` | V | reference/everyday-edits.md#Everyday photo edits (verified…: \| levels \| `image.adjustments.levels {"inBl… |
| `image.adjustments.matchColor` | s | reference/everyday-edits.md#Image commands, selections, to…: Not run: `image.adjustments.matchColor`. |
| `image.adjustments.photoFilter` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …arm/cool \| `image.adjustments.photoFilter {… |
| `image.adjustments.posterize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.posterize` 4 levels: fla… |
| `image.adjustments.replaceColor` | V | reference/everyday-edits.md#Retouching, compositing and se…: …estructive `image.adjustments.replaceColor … |
| `image.adjustments.selectiveColor` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.selectiveColor` reds wit… |
| `image.adjustments.shadowsHighlights` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …ghlights \| `image.adjustments.shadowsHighli… |
| `image.adjustments.threshold` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.adjustments.threshold` pure black/wh… |
| `image.adjustments.vibrance` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …turation \| `image.adjustments.vibrance {"vi… |
| `image.analysis.countTool` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `image.analysis.countTool {}` lists the gro… |
| `image.analysis.info` | V | reference/everyday-edits.md#Image commands, selections, to…: …s layers), `image.analysis.info {}` |
| `image.analysis.placeScaleMarker` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (2): `image.analysis.placeScaleMarker… |
| `image.analysis.recordMeasurements` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …orded with `image.analysis.recordMeasuremen… |
| `image.analysis.rulerTool` | V | reference/everyday-edits.md#Image commands, selections, to…: …000 cm"}`, `image.analysis.rulerTool {"star… |
| `image.analysis.selectDataPoints` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `image.analysis.selectDataPoints` `{}` read… |
| `image.analysis.setMeasurementScale` | V | reference/everyday-edits.md#Image commands, selections, to…: …d notes: `image.analysis.setMeasurementSc… |
| `image.analysis.straightenLayer` | V | reference/live-mode.md#Live UI tools: pointer, tools, stra…: …h}`), then `image.analysis.straightenLayer … |
| `image.applyDataSet` | V | reference/everyday-edits.md#Image commands, selections, to…: …fs":[]}` / `image.applyDataSet {"name"}` fo… |
| `image.applyImage` | V | reference/everyday-edits.md#Image commands, selections, to…: `image.applyImage` needs a pixel layer ("ac… |
| `image.autoColor` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `image.autoColor {}`, `image.autoContrast {… |
| `image.autoContrast` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …Color {}`, `image.autoContrast {}`, `image.… |
| `image.autoTone` | V | reference/everyday-edits.md#Image commands, selections, to…: …uctive): `image.autoTone\|autoContrast\|aut… |
| `image.calculations` | V | reference/everyday-edits.md#Image commands, selections, to…: `image.calculations {"source1":{"layer":"me… |
| `image.canvasSize` | V+ | SKILL.md#Commands that worked (exact parameter formats): … 400×250), `image.canvasSize`, · limit: workflows-and-tools.md: …(spec only, not run): `file.close {"save":"discard\|ask"}`, `… |
| `image.crop` | V | SKILL.md#CLI essentials (verified): …n.jpg --cmd image.crop --params '{"x":100,"y":50,"width":800,"height… |
| `image.detectFaces` | V | reference/everyday-edits.md#Image commands, selections, to…: …document), `image.detectFaces {}` → `{faces… |
| `image.duplicate` | V | reference/command-sweeps.md#The last 28 command ids (2026-…: …documents: `image.duplicate` first); `file.… |
| `image.imageRotation.180` | V | reference/everyday-edits.md#Image commands, selections, to…: …as grows), `image.imageRotation.180\|90ccw\|f… |
| `image.imageRotation.90ccw` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …bits8 {}`, `image.imageRotation.90ccw`, `im… |
| `image.imageRotation.90cw` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …e / flip \| `image.imageRotation.90cw\|90ccw\|… |
| `image.imageRotation.flipCanvasHorizontal` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …on.90ccw`, `image.imageRotation.flipCanvasH… |
| `image.imageRotation.flipCanvasVertical` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …n. (1): `image.imageRotation.flipCanvasV… |
| `image.imageSize` | V | SKILL.md#CLI essentials (verified): … steps (`[["image.imageSize",{"width":300}], |
| `image.mode.bitmap` | s | reference/everyday-edits.md#Image commands, selections, to…: Not run … - Not run: `actions.photoshopStep` (needs a… |
| `image.mode.bits16` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `image.mode.bits16` → depth 16 (TIFF) |
| `image.mode.bits32` | V | reference/everyday-edits.md#Image commands, selections, to…: Modes: `image.mode.bits32\|bits8` (null), `i… |
| `image.mode.bits8` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …trast {}`, `image.mode.bits8 {}`, `image.im… |
| `image.mode.cmyk` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `image.mode.cmyk` → saved TIFF reports CMYK… |
| `image.mode.colorTable` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `image.mode.colorTable` `{}` rea… |
| `image.mode.duotone` | V | reference/everyday-edits.md#Image commands, selections, to…: `image.mode.duotone` "needs a Grayscale i… |
| `image.mode.grayscale` | V | reference/everyday-edits.md#Image commands, selections, to…: … image": `image.mode.grayscale` first. |
| `image.mode.indexedColor` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `image.mode.indexedColor {"colors":32,"pale… |
| `image.mode.lab` | V | reference/everyday-edits.md#Image commands, selections, to…: …8` (null), `image.mode.lab` → `{profile:"La… |
| `image.mode.multichannel` | V | reference/everyday-edits.md#Image commands, selections, to…: …ent,bpc}`, `image.mode.multichannel` → `{ch… |
| `image.mode.rgb` | V | reference/everyday-edits.md#Image commands, selections, to…: … back with `image.mode.rgb` → `{converted:"… |
| `image.perspectiveCrop` | V | reference/everyday-edits.md#Retouching, compositing and se…: `image.perspectiveCrop` rasterizes smart ob… |
| `image.revealAll` | V | reference/everyday-edits.md#Image commands, selections, to…: …,height}`, `image.revealAll` → `{changed}`,… |
| `image.rotation.arbitrary` | V | reference/everyday-edits.md#Image commands, selections, to…: …n `null`), `image.rotation.arbitrary {"angl… |
| `image.trap` | s | reference/everyday-edits.md#Image commands, selections, to…: Not run: `bitmap`, `colorTable`, `image.tra… |
| `image.trim` | V | reference/everyday-edits.md#Image commands, selections, to…: …Vertical`, `image.trim {"basedOn":"transpar… |
| `image.variables.dataSets` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …errors), `image.variables.dataSets {"data… |
| `image.variables.define` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …"}]` after `image.variables.define {"defs":… |

## jobs (2)

| id | status | note |
|---|---|---|
| `jobs.cancel` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (2): `jobs.cancel` `{}` while the Len… |
| `jobs.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `jobs.list` then showed job 2 `state:"cance… |

## layer (230)

| id | status | note |
|---|---|---|
| `layer.addAboveToSelection` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …":3}` then `layer.addAboveToSelection {}` (… |
| `layer.addBelowToSelection` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - layer.addBelowToSelection. (1): `lay… |
| `layer.align.bottomEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …n. (4): `layer.align.bottomEdges` layer.… |
| `layer.align.horizontalCenters` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.align.horizontalCenters` layer.list … |
| `layer.align.leftEdges` | V | reference/everyday-edits.md#Layer management, edit and fil…: …selection: `layer.align.leftEdges {"to":"la… |
| `layer.align.rightEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.align.rightEdges` layer.list bounds:… |
| `layer.align.topEdges` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …tribute: `layer.align.topEdges`, `bottomE… |
| `layer.align.verticalCenters` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.align.verticalCenters` layer.list bo… |
| `layer.arrange.bringForward` | V | reference/everyday-edits.md#Everyday layer and edit comman…: …rd {}` and `layer.arrange.bringForward {}` … |
| `layer.arrange.bringToFront` | V | reference/everyday-edits.md#Layer management, edit and fil…: …,layers}`, `layer.arrange.bringToFront\|send… |
| `layer.arrange.reverse` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (2): `layer.arrange.reverse` selectio… |
| `layer.arrange.sendBackward` | V | reference/everyday-edits.md#Everyday layer and edit comman…: …ibility: `layer.arrange.sendBackward {}` … |
| `layer.arrange.sendToBack` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.arrange.sendToBack` moved the Star j… |
| `layer.artboard.addBeside` | V | reference/everyday-edits.md#Layer management, edit and fil…: …board 1"), `layer.artboard.addBeside {"side… |
| `layer.artboard.set` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …d. (1): `layer.artboard.set` `{"rect":[2… |
| `layer.combineShapes.excludeOverlappingShapes` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (3): `layer.combineShapes.excludeOver… |
| `layer.combineShapes.intersectShapeAreas` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.combineShapes.intersectShapeAreas` p… |
| `layer.combineShapes.mergeShapeComponents` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.combineShapes.mergeShapeComponents` … |
| `layer.combineShapes.subtractFrontShape` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …3 then 4): `layer.combineShapes.subtractFro… |
| `layer.combineShapes.unite` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.combineShapes.unite\|subtractFrontSha… |
| `layer.copyToDocument` | s | reference/everyday-edits.md#Layer management, edit and fil…: Not run … - Not run: `file.openAs/placeLinked/closeAl… |
| `layer.createClippingMask` | V | reference/everyday-edits.md#Retouching, compositing and se…: …lipping: `layer.createClippingMask {"laye… |
| `layer.delete` | V | reference/live-mode.md#Live mode and removing a background…: …s (revert: `layer.delete` the new layer). D… |
| `layer.delete.hiddenLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: …romLayer`, `layer.delete.hiddenLayers` → `{… |
| `layer.distribute.bottomEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (7): `layer.distribute.bottomEdges` m… |
| `layer.distribute.horizontalCenters` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.distribute.horizontalCenters` middle… |
| `layer.distribute.horizontally` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.distribute.horizontally` layer.list:… |
| `layer.distribute.leftEdges` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.distribute.leftEdges`, `rightEdges`,… |
| `layer.distribute.rightEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.distribute.rightEdges` middle layer'… |
| `layer.distribute.topEdges` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.distribute.topEdges` middle layer's … |
| `layer.distribute.verticalCenters` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.distribute.verticalCenters` middle l… |
| `layer.distribute.vertically` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.distribute.vertically` middle layer … |
| `layer.duplicate` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: `layer.duplicate` → `select.subject` → `lay… |
| `layer.exportAs` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.exportAs {"layer":4,"path":"exp.png"… |
| `layer.fill.pattern.set` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …l. (2): `layer.fill.pattern.set` switche… |
| `layer.fill.solidColor.set` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.fill.solidColor.set` changed an exis… |
| `layer.flattenImage` | V | reference/everyday-edits.md#Everyday layer and edit comman…: … ran after `layer.flattenImage {}` (one Bac… |
| `layer.frame.convert` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …d-back): `layer.frame.convert {"layer":3,… |
| `layer.frame.fit` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: `layer.frame.fit {"layer":7,"mode":"content… |
| `layer.frame.info` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: `layer.frame.info {"layer":3}` → `{content,… |
| `layer.frame.set` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: `layer.frame.set {"layer":7,"name":"Framed"… |
| `layer.frame.setContent` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: `layer.frame.setContent {"layer":7,"content… |
| `layer.groupLayers` | V | reference/everyday-edits.md#Newer commands and options (ve…: …ew.group`, `layer.groupLayers`, `layer.new.… |
| `layer.hideLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: …sparency`, `layer.hideLayers/showLayers`, `… |
| `layer.layerContentOptions` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.layerContentOptions {}` → `{editor:"… |
| `layer.layerMask.apply` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.layerMask.apply/fromTransparency` an… |
| `layer.layerMask.delete` | V | reference/live-mode.md#Live mode and removing a background…: `layer.layerMask.delete {"layer":3}` → `lay… |
| `layer.layerMask.edit` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …k. (3): `layer.layerMask.edit` density 5… |
| `layer.layerMask.enabled` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerMask.enabled` enabled:false on … |
| `layer.layerMask.fromTransparency` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …ct.rect`), `layer.layerMask.fromTransparenc… |
| `layer.layerMask.hideAll` | V | reference/everyday-edits.md#Layer management, edit and fil…: … shapes: `layer.layerMask.hideAll\|revealA… |
| `layer.layerMask.hideSelection` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …,layer}`), `layer.layerMask.hideSelection` … |
| `layer.layerMask.linked` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerMask.linked` {linked:false} acc… |
| `layer.layerMask.revealAll` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …Masks: `layer.layerMask.revealAll`, `en… |
| `layer.layerMask.revealSelection` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …ct …` then `layer.layerMask.revealSelection… |
| `layer.layerStyle.bevelEmboss` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (20): `layer.layerStyle.bevelEmboss` i… |
| `layer.layerStyle.blendingOptions` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.blendingOptions` opacity … |
| `layer.layerStyle.clear` | V | reference/everyday-edits.md#Image commands, selections, to…: …fects:1}`, `layer.layerStyle.clear {"layer"… |
| `layer.layerStyle.colorOverlay` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.colorOverlay` solid red o… |
| `layer.layerStyle.contours.delete` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.contours.delete` removed … · limit: command-sweeps.md: Refused … `layer.layerStyle.contours.delete` (invalid parameters for l… |
| `layer.layerStyle.contours.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.contours.list` lists user… |
| `layer.layerStyle.contours.load` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.contours.load` loaded C1 … · limit: command-sweeps.md: Refused … `layer.layerStyle.contours.load` (not a contour file: invali… |
| `layer.layerStyle.contours.new` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.contours.new` `{name,cont… |
| `layer.layerStyle.contours.save` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.contours.save` wrote c.sh… · limit: command-sweeps.md: Refused … `layer.layerStyle.contours.save` (invalid parameters for lay… |
| `layer.layerStyle.copyLayerStyle` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.copyLayerStyle` the style… |
| `layer.layerStyle.createLayer` | V | reference/workflows-and-tools.md#Filter Gallery, every lay…: `layer.layerStyle.createLayer {}` turns t… |
| `layer.layerStyle.defaultFor` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ault uses: `layer.layerStyle.defaultFor {"k… |
| `layer.layerStyle.dropShadow` | V | SKILL.md#Recipes: …ded rect → `layer.layerStyle.dropShadow` |
| `layer.layerStyle.globalLight` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.globalLight` changes the … |
| `layer.layerStyle.gradientOverlay` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.gradientOverlay` angle 90… |
| `layer.layerStyle.hideAllEffects` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.hideAllEffects` the drop … |
| `layer.layerStyle.innerGlow` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.innerGlow` white glow ins… |
| `layer.layerStyle.innerShadow` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.innerShadow` dark shadow … |
| `layer.layerStyle.makeDefault` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `layer.layerStyle.makeDefault` s… |
| `layer.layerStyle.outerGlow` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.outerGlow` yellow glow ou… |
| `layer.layerStyle.pasteLayerStyle` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.pasteLayerStyle` pasting … |
| `layer.layerStyle.patternOverlay` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.patternOverlay` default p… |
| `layer.layerStyle.replace` | V | reference/everyday-edits.md#Image commands, selections, to…: `layer.layerStyle.replace {"layer":3,"effec… |
| `layer.layerStyle.satin` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.satin` dark satin shading… |
| `layer.layerStyle.scaleEffects` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.scaleEffects` scale 300 m… |
| `layer.layerStyle.showAllEffects` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.layerStyle.showAllEffects` the hidde… |
| `layer.layerStyle.stroke` | V | reference/everyday-edits.md#Everyday photo edits (verified…: … {…}` then `layer.layerStyle.stroke {"color… |
| `layer.layerStyle.transferEffects` | V | reference/everyday-edits.md#Image commands, selections, to…: `layer.layerStyle.transferEffects` needs … |
| `layer.linkLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.linkLayers` "select two or more" |
| `layer.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …and `info`/`layer.list`/`type.info`/`*.list… |
| `layer.lockLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: …l":true}`, `layer.lockLayers {"layer","posi… |
| `layer.maskAllObjects` | V | reference/everyday-edits.md#Layer management, edit and fil…: …verlay"}`, `layer.maskAllObjects {}` → `{bo… |
| `layer.matting.colorDecontaminate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …g. (3): `layer.matting.colorDecontaminat… |
| `layer.matting.defringe` | V | reference/everyday-edits.md#Layer management, edit and fil…: …rency` and `layer.matting.defringe\|removeBl… |
| `layer.matting.removeBlackMatte` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.matting.removeBlackMatte` on a feath… |
| `layer.matting.removeWhiteMatte` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.matting.removeWhiteMatte` same edge … |
| `layer.mergeDown` | V | reference/everyday-edits.md#Retouching, compositing and se…: …first with `layer.mergeDown {}`) did not ch… |
| `layer.mergeGroup` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …yers` then `layer.mergeGroup {}` → `{layer}… |
| `layer.mergeLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: …ctInRect`, `layer.mergeLayers` (one layer =… |
| `layer.mergeVisible` | V | reference/everyday-edits.md#Layer management, edit and fil…: …rge down), `layer.mergeVisible`, `layer.sta… |
| `layer.moveTo` | V | reference/live-mode.md#Live mode and removing a background…: `layer.moveTo {"layer":4,"target":2,"positi… |
| `layer.new.artboard` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …rd made by `layer.new.artboard` (`info` art… |
| `layer.new.artboardFromGroup` | V+ | reference/workflows-and-tools.md#New in 0.20.2: action his…: - `layer.new.artboardFromGroup` takes `pres… · limit: everyday-edits.md: Not run … - Not run: `file.openAs/placeLinked/closeAll`, printing, EXR… |
| `layer.new.artboardFromLayers` | V+ | reference/everyday-edits.md#Newer commands and options (ve…: - `layer.new.artboardFromLayers {"name","… · limit: everyday-edits.md: Not run … - Not run: `layer.new.artboardFromLayers`, `layer.new.frameF… |
| `layer.new.backgroundFromLayer` | V | reference/everyday-edits.md#Layer management, edit and fil…: …t":true}`, `layer.new.backgroundFromLayer`,… |
| `layer.new.frame` | V | reference/everyday-edits.md#Layer management, edit and fil…: …00,200]}`, `layer.new.frame {"x","y","width… |
| `layer.new.frameFromLayers` | V+ | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: `layer.new.frameFromLayers` needs a selecti… · limit: everyday-edits.md: Not run … - Not run: `layer.new.artboardFromLayers`, `layer.new.frameF… |
| `layer.new.group` | V | reference/everyday-edits.md#Newer commands and options (ve…: …*Groups: `layer.new.group`, `layer.groupL… |
| `layer.new.groupFromLayers` | V | reference/everyday-edits.md#Newer commands and options (ve…: …upLayers`, `layer.new.groupFromLayers` take… |
| `layer.new.layer` | V | reference/everyday-edits.md#Everyday layer and edit comman…: …yer first (`layer.new.layer`). |
| `layer.new.layerFromBackground` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.new.layerFromBackground {"ifPresent"… |
| `layer.new.layerViaCopy` | V | reference/everyday-edits.md#Layer management, edit and fil…: …y on top), `layer.new.layerViaCopy` → `{lay… |
| `layer.new.layerViaCut` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.new.layerViaCut {}` needs a selectio… |
| `layer.newAdjustmentLayer.blackWhite` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (12): `layer.newAdjustmentLayer.blackW… |
| `layer.newAdjustmentLayer.brightnessContrast` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.brightnessContras… |
| `layer.newAdjustmentLayer.channelMixer` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.channelMixer` red… |
| `layer.newAdjustmentLayer.colorBalance` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.colorBalance` war… |
| `layer.newAdjustmentLayer.colorLookup` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …ilm…) with `layer.newAdjustmentLayer.colorL… |
| `layer.newAdjustmentLayer.curves` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.curves` points [[… |
| `layer.newAdjustmentLayer.exposure` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.exposure` exposur… |
| `layer.newAdjustmentLayer.gradientMap` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.gradientMap` navy… |
| `layer.newAdjustmentLayer.hueSaturation` | V | reference/everyday-edits.md#Everyday photo edits (verified…: `layer.newAdjustmentLayer.hueSaturation {"s… |
| `layer.newAdjustmentLayer.invert` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.invert` colour ne… |
| `layer.newAdjustmentLayer.levels` | V | reference/everyday-edits.md#Everyday layer and edit comman…: `layer.newAdjustmentLayer.levels {"inBlack"… |
| `layer.newAdjustmentLayer.photoFilter` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.photoFilter` cool… |
| `layer.newAdjustmentLayer.posterize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.posterize` 3 leve… |
| `layer.newAdjustmentLayer.selectiveColor` | V | reference/everyday-edits.md#Retouching, compositing and se…: …*Colour: `layer.newAdjustmentLayer.select… |
| `layer.newAdjustmentLayer.threshold` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.threshold` black/… |
| `layer.newAdjustmentLayer.vibrance` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.newAdjustmentLayer.vibrance` more sa… |
| `layer.newFillLayer.gradient` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: …mand_run` (`layer.newFillLayer.gradient`, `… |
| `layer.newFillLayer.pattern` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (1): `layer.newFillLayer.pattern` pat… |
| `layer.newFillLayer.solidColor` | V | reference/live-mode.md#Live mode and removing a background…: …ng colour: `layer.newFillLayer.solidColor {… |
| `layer.newLayerBasedSlice` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.newLayerBasedSlice` on an empty laye… |
| `layer.pickAt` | V | reference/everyday-edits.md#Layer management, edit and fil…: …ted:[…]}`, `layer.pickAt {"x","y"}`, `layer… |
| `layer.quickExportAsPng` | V | reference/everyday-edits.md#Retouching, compositing and se…: `layer.quickExportAsPng {"layer","path"}` f… |
| `layer.rasterize.allLayers` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …(a shape), `layer.rasterize.allLayers {}` →… |
| `layer.rasterize.fillContent` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.rasterize.fillContent` on a shape: "… |
| `layer.rasterize.layer` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …ayer":6}`, `layer.rasterize.layer {"layer":… |
| `layer.rasterize.layerStyle` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …adow` then `layer.rasterize.layerStyle {"la… |
| `layer.rasterize.shape` | V | reference/everyday-edits.md#Layer management, edit and fil…: …deleted}`, `layer.rasterize.shape\|allLayers… |
| `layer.rasterize.smartObject` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `layer.rasterize.smartObject` th… |
| `layer.rasterize.type` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …sterize: `layer.rasterize.type {"layer":6… |
| `layer.rasterize.vectorMask` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (2): `layer.rasterize.vectorMask` inf… |
| `layer.rasterize.video` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.rasterize.video` {rasterized:true}. |
| `layer.releaseClippingMask` | V | reference/everyday-edits.md#Retouching, compositing and se…: `layer.releaseClippingMask`. |
| `layer.removeBackground` | V | reference/everyday-edits.md#Layer management, edit and fil…: …taminate`, `layer.removeBackground` only … |
| `layer.renameLayer` | V | reference/everyday-edits.md#Layer management, edit and fil…: …*Layers: `layer.renameLayer {"layer","nam… |
| `layer.select` | V | reference/everyday-edits.md#Retouching, compositing and se…: …ackground (`layer.select {"name":"Backgroun… |
| `layer.selectAbove` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - layer.selectAbove. (1): `layer.selec… |
| `layer.selectBelow` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - layer.selectBelow. (1): `layer.selec… |
| `layer.selectBottom` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - layer.selectBottom. (1): `layer.sele… |
| `layer.selectInRect` | V | reference/everyday-edits.md#Layer management, edit and fil…: …"x","y"}`, `layer.selectInRect`, `layer.mer… |
| `layer.selectLinkedLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: `layer.selectLinkedLayers` only when linked… |
| `layer.selectTop` | V | reference/everyday-edits.md#Layer management, edit and fil…: …on helpers `layer.selectTop\|selectBottom\|se… |
| `layer.setAdjustment` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.setAdjustment {"layer":id,…params}` … |
| `layer.setEffectsExpanded` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (1): `layer.setEffectsExpanded` panel… |
| `layer.setEffectsVisible` | s | reference/everyday-edits.md#Layer arrangement, shape combi…: Not run … - Not run: `layer.new.artboardFromLayers`, … |
| `layer.setExpanded` | V | reference/everyday-edits.md#Layer management, edit and fil…: …upLayers`, `layer.setExpanded {"expanded":t… |
| `layer.setLabelColor` | V | reference/everyday-edits.md#Layer management, edit and fil…: …,"name"}`, `layer.setLabelColor {"color":"r… |
| `layer.setProps` | V | reference/everyday-edits.md#Everyday photo edits (verified…: `layer.setProps {"blend":"Overlay","opacity… |
| `layer.showLayers` | V | reference/everyday-edits.md#Everyday layer and edit comman…: … hides it, `layer.showLayers {}` shows it a… |
| `layer.showOnly` | V | reference/everyday-edits.md#Layer management, edit and fil…: …owLayers`, `layer.showOnly {}` (⌥-click eye… |
| `layer.smartFilter.blendingOptions` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (6): `layer.smartFilter.blendingOptio… |
| `layer.smartFilter.clearSmartFilters` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.clearSmartFilters` info:… |
| `layer.smartFilter.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.delete` info: second fil… |
| `layer.smartFilter.deleteFilterMask` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …r. (3): `layer.smartFilter.deleteFilterM… |
| `layer.smartFilter.disableFilterMask` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.disableFilterMask` a blu… · limit: command-sweeps.md: Refused … `layer.smartFilter.disableFilterMask` (command layer.smartFi… |
| `layer.smartFilter.disableSmartFilters` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.disableSmartFilters` inf… |
| `layer.smartFilter.move` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.move` info.smartFilters … |
| `layer.smartFilter.setParams` | V | reference/everyday-edits.md#Retouching, compositing and se…: `layer.smartFilter.setParams {"index":0,"pa… |
| `layer.smartFilter.setVisible` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.setVisible` info: second… |
| `layer.smartFilter.transfer` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartFilter.transfer` `{"from":6,"to… · limit: command-sweeps.md: Refused … `layer.smartFilter.transfer` (invalid parameters for layer.s… |
| `layer.smartObjects.convertToEmbedded` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (23): `layer.smartObjects.convertToEmb… |
| `layer.smartObjects.convertToLayers` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.convertToLayers` unpack… |
| `layer.smartObjects.convertToLinked` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.convertToLinked` writes… · limit: command-sweeps.md: Refused … `layer.smartObjects.convertToLinked` (the smart object's con… |
| `layer.smartObjects.convertToSmartObject` | V | reference/everyday-edits.md#Retouching, compositing and se…: …filters: `layer.smartObjects.convertToSma… |
| `layer.smartObjects.editContents` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.editContents` opens the… |
| `layer.smartObjects.embedAllLinked` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: - `layer.smartObjects.embedAllLinked {}`*… |
| `layer.smartObjects.exportContents` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.exportContents` wrote t… |
| `layer.smartObjects.exportSvg` | V | reference/log.md#Log: … checked), `layer.smartObjects.exportSvg` and `updateSvg` (render checked, stale f… |
| `layer.smartObjects.newSmartObjectViaCopy` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.newSmartObjectViaCopy` … |
| `layer.smartObjects.perspectiveWarp` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …r arched), `layer.smartObjects.perspectiveW… |
| `layer.smartObjects.puppetWarp` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (3): `layer.smartObjects.puppetWarp` … |
| `layer.smartObjects.rasterize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.rasterize` layer.list s… |
| `layer.smartObjects.relinkToFile` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.relinkToFile` points th… |
| `layer.smartObjects.replaceContents` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.replaceContents` {insta… |
| `layer.smartObjects.revealInFinder` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.revealInFinder` dryRun:… · limit: command-sweeps.md: Refused … `layer.smartObjects.revealInFinder` (command layer.smartObje… |
| `layer.smartObjects.saveContents` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.saveContents` after `ed… · limit: command-sweeps.md: Refused … `layer.smartObjects.saveContents` (command layer.smartObject… |
| `layer.smartObjects.stackMode.entropy` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.entropy` sett… |
| `layer.smartObjects.stackMode.kurtosis` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.kurtosis` set… |
| `layer.smartObjects.stackMode.maximum` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.maximum` sett… |
| `layer.smartObjects.stackMode.mean` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.mean` setting… |
| `layer.smartObjects.stackMode.median` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.median` setti… |
| `layer.smartObjects.stackMode.minimum` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.minimum` sett… |
| `layer.smartObjects.stackMode.none` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.none` setting… |
| `layer.smartObjects.stackMode.range` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.range` settin… |
| `layer.smartObjects.stackMode.skewness` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.skewness` set… |
| `layer.smartObjects.stackMode.standardDeviation` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.standardDevia… |
| `layer.smartObjects.stackMode.summation` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.summation` se… |
| `layer.smartObjects.stackMode.variance` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.stackMode.variance` set… |
| `layer.smartObjects.updateAllModifiedContent` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.updateAllModifiedConten… |
| `layer.smartObjects.updateChanged` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (1): `layer.smartObjects.updateChange… |
| `layer.smartObjects.updateModifiedContent` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.smartObjects.updateModifiedContent` … |
| `layer.smartObjects.updateSvg` | V | reference/workflows-and-tools.md#New in 0.19.0: path to se…: `layer.smartObjects.updateSvg {"document","… |
| `layer.smartObjects.updateVectorSource` | V | reference/workflows-and-tools.md#New in 0.19.0: path to se…: - `layer.smartObjects.updateVectorSource`… |
| `layer.smartObjects.warp` | V | reference/workflows-and-tools.md#Smart-object leftovers, v…: …hecked): `layer.smartObjects.warp {"style… |
| `layer.stampDown` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.stampDown {}` needs a PIXEL layer be… |
| `layer.stampVisible` | V | reference/everyday-edits.md#Layer management, edit and fil…: …eVisible`, `layer.stampVisible` → `{layer}`… |
| `layer.toggleLockTransparency` | V | reference/everyday-edits.md#Layer management, edit and fil…: …ayers:1}`, `layer.toggleLockTransparency`, … |
| `layer.toggleMaskOverlay` | V | reference/everyday-edits.md#Layer management, edit and fil…: …ther":5}`, `layer.toggleMaskOverlay {"layer… |
| `layer.translate` | V | reference/everyday-edits.md#Layer management, edit and fil…: …further"), `layer.translate {"layer","dx","… |
| `layer.ungroupLayers` | V | reference/everyday-edits.md#Layer management, edit and fil…: …omLayers`, `layer.ungroupLayers`, `layer.se… |
| `layer.vectorMask.add` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …ath.set`), `layer.vectorMask.add {"name":"w… |
| `layer.vectorMask.currentPath` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …k. (4): `layer.vectorMask.currentPath` r… |
| `layer.vectorMask.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.vectorMask.delete` info.hasVectorMas… |
| `layer.vectorMask.edit` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …k. (3): `layer.vectorMask.edit` `{"inver… |
| `layer.vectorMask.enabled` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.vectorMask.enabled` {enabled:false} … |
| `layer.vectorMask.fromPath` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …el layer → `layer.vectorMask.fromPath {"nam… |
| `layer.vectorMask.hideAll` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.vectorMask.hideAll` replaces the mas… |
| `layer.vectorMask.info` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …th}`, then `layer.vectorMask.info`, `edit {… |
| `layer.vectorMask.linked` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.vectorMask.linked` {linked:false} re… |
| `layer.vectorMask.revealAll` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.vectorMask.revealAll` empty non-inve… |
| `layer.videoLayers.deleteFrame` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …. (11): `layer.videoLayers.deleteFrame` … |
| `layer.videoLayers.duplicateFrame` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.duplicateFrame` frames 2… |
| `layer.videoLayers.insertBlankFrame` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.insertBlankFrame` frames… |
| `layer.videoLayers.interpretFootage` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.interpretFootage` {frame… |
| `layer.videoLayers.newBlankVideoLayer` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `layer.videoLayers.newBlankVideoLayer` then… |
| `layer.videoLayers.newVideoLayerFromFile` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.newVideoLayerFromFile` 3… |
| `layer.videoLayers.rasterize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.rasterize` {rasterized:t… |
| `layer.videoLayers.reloadFrame` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.reloadFrame` {frames:3} … · limit: command-sweeps.md: Refused … `layer.videoLayers.reloadFrame` (invalid parameters for laye… |
| `layer.videoLayers.replaceFootage` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.replaceFootage` {frames:… |
| `layer.videoLayers.restoreAllFrames` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.restoreAllFrames` after … |
| `layer.videoLayers.restoreFrame` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.restoreFrame` after a de… |
| `layer.videoLayers.showAlteredVideo` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layer.videoLayers.showAlteredVideo` {frame… |
| `layer.xmpMetadata` | V | reference/everyday-edits.md#Layer management, edit and fil…: …"shape"}`, `layer.xmpMetadata {"layer"}` → … |

## layerComp (14)

| id | status | note |
|---|---|---|
| `layerComp.apply` | V | reference/everyday-edits.md#Retouching, compositing and se…: … `{comp}`, `layerComp.apply {"comp":"Soft"}… |
| `layerComp.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …p. (7): `layerComp.delete` `{"comp":"C"}… |
| `layerComp.duplicate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layerComp.duplicate` `{"comp":"A"}` made c… |
| `layerComp.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layerComp.list` `{comps:[{id,name,comment,… |
| `layerComp.new` | V | reference/everyday-edits.md#Retouching, compositing and se…: …r comps: `layerComp.new {"name":"Soft"}` … |
| `layerComp.next` | s | reference/everyday-edits.md#Layer arrangement, shape combi…: Not run … - Not run: `layer.new.artboardFromLayers`, … |
| `layerComp.previous` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layerComp.previous` from comp B (Backgroun… |
| `layerComp.rename` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layerComp.rename` `{"comp":"A copy","name"… |
| `layerComp.reorder` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layerComp.reorder` `{"comp":"C","index":0}… |
| `layerComp.restoreLastDocumentState` | s | reference/workflows-and-tools.md#Filter families, layer co…: Not run … - Not run: the 47 `filter.gallery.*` artist… |
| `layerComp.setComment` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …bility"}`, `layerComp.setComment {"comp","c… |
| `layerComp.setOptions` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `layerComp.setOptions` `{"comp":"B","positi… |
| `layerComp.update` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …p.new` ×2, `layerComp.update {"comp":"Two",… |
| `layerComp.updateWarnings` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …omment"}`, `layerComp.updateWarnings {"clea… |

## measurementLog (3)

| id | status | note |
|---|---|---|
| `measurementLog.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …g. (3): `measurementLog.delete` `{"rows"… |
| `measurementLog.export` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `measurementLog.export` `{}` returns `{csv,… |
| `measurementLog.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `measurementLog.list` `{columns:[label,date… |

## notes (4)

| id | status | note |
|---|---|---|
| `notes.add` | V | reference/everyday-edits.md#Image commands, selections, to…: `notes.add {"x","y","text","author"}` → `{i… |
| `notes.delete` | V | reference/everyday-edits.md#Image commands, selections, to…: …,"text"}`, `notes.delete {"index"\|"all":tru… |
| `notes.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …orted:1}`; `notes.list` went from 1 note to… |
| `notes.set` | V | reference/everyday-edits.md#Image commands, selections, to…: …tes.list`, `notes.set {"index","text"}`, `n… |

## paint (28)

| id | status | note |
|---|---|---|
| `paint.artHistoryBrush` | V | reference/everyday-edits.md#Newer commands and options (ve…: - `paint.artHistoryBrush {"points","size"… |
| `paint.backgroundEraser` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: `paint.backgroundEraser {"points","size"}` … |
| `paint.blur` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …t. (3): `paint.blur` a stroke along a ha… |
| `paint.bucket` | V | reference/everyday-edits.md#Newer commands and options (ve…: - `paint.bucket {"mode":"multiply"}` bl… |
| `paint.burn` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `paint.burn` a 30 px stroke across mid-grey… |
| `paint.cloneStamp` | V | reference/everyday-edits.md#Retouching, compositing and se…: `paint.cloneStamp {"points","size":60,"sour… |
| `paint.colorReplacement` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …,"size"}`, `paint.colorReplacement {"points… |
| `paint.contentAwareMove` | s | reference/workflows-and-tools.md#Brushes and paint tools (…: Not run … - Not run: `paint.patch`, `paint.contentAwa… |
| `paint.dodge` | V | reference/everyday-edits.md#Newer commands and options (ve…: …ing tools (`paint.dodge/burn/blur/…`) accep… |
| `paint.gradient` | V | reference/live-mode.md#Live session and wider toolbox (ver…: …"color"}`, `paint.gradient {"from":[x,y],"t… |
| `paint.healingBrush` | V | reference/everyday-edits.md#Retouching, compositing and se…: `paint.healingBrush` takes the same `source… |
| `paint.historyBrush` | V+ | reference/workflows-and-tools.md#Filter families, layer co…: …":2}` then `paint.historyBrush {"points","s… · limit: workflows-and-tools.md: Not run … - Not run: `paint.patch`, `paint.contentAwareMove`, `paint.r… |
| `paint.magicEraser` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …omposite), `paint.magicEraser {"x","y","tol… |
| `paint.mixerBrush` | V | reference/everyday-edits.md#Newer commands and options (ve…: `paint.mixerBrush` takes `mixerState`. |
| `paint.mixerLoad` | V | reference/log.md#Log: …o 0.1 px), `paint.mixerLoad {"x","y","size"}` (→ `{loaded,color}`), `layer.layerSt… |
| `paint.patch` | s | reference/workflows-and-tools.md#Brushes and paint tools (…: Not run … - Not run: `paint.patch`, `paint.contentAwa… |
| `paint.patternStamp` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: `paint.patternStamp {"points","size","patte… |
| `paint.pencil` | V | reference/live-mode.md#Live session and wider toolbox (ver…: `paint.pencil`, `paint.bucket {"x","y","tol… |
| `paint.redEye` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: `paint.redEye {"x","y"}` errors "no red-eye… |
| `paint.remove` | V+ | reference/everyday-edits.md#Retouching, compositing and se…: …ait: one `paint.remove` stroke drawn *aro… · limit: workflows-and-tools.md: Not run … - Not run: `paint.patch`, `paint.contentAwareMove`, `paint.r… |
| `paint.setSymmetry` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …ymmetry: `paint.setSymmetry {"mode":"vert… |
| `paint.sharpen` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `paint.sharpen` `{"strength":100}` on an op… |
| `paint.smudge` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: `paint.smudge`, `paint.sponge {"points","si… |
| `paint.sponge` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …t.smudge`, `paint.sponge {"points","size"}`… |
| `paint.spotHealing` | V+ | reference/everyday-edits.md#Retouching, compositing and se…: …[x,y],…]`: `paint.spotHealing {"points","si… · limit: live-mode.md: …next stroke fails with "command `paint.spotHealing` is not a… |
| `paint.stroke` | V+ | reference/everyday-edits.md#Newer commands and options (ve…: - `paint.stroke {"fill":true}` with a c… · limit: live-mode.md: `paint.stroke` is refused when the active layer is a Type la… |
| `paint.symmetryDisable` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: `paint.symmetryDisable {}` turns it off (`s… |
| `paint.symmetryFromPath` | V | reference/workflows-and-tools.md#Brushes and paint tools (…: …line, then `paint.symmetryFromPath {"name":… |

## path (25)

| id | status | note |
|---|---|---|
| `path.addAnchor` | V | reference/everyday-edits.md#Newer commands and options (ve…: … commands (`path.addAnchor`, `path.moveAnch… |
| `path.addToSelection` | V | reference/log.md#Log: … headless: `path.addToSelection`, `path.subtractFromSelection` (render checked), `… |
| `path.bendSegment` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …330,90]}`, `path.bendSegment {"subpath":0,"… |
| `path.clippingPath.clear` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …h. (1): `path.clippingPath.clear` after … |
| `path.clippingPath.set` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ear` after `path.clippingPath.set {"name":"… · limit: workflows-and-tools.md: …lso listed, not run: `path.moveAnchors/moveHandle/bendSegmen… |
| `path.convertPoint` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …[0,-40]}`, `path.convertPoint {"subpath":0,… |
| `path.delete` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …:[0,40]}`, `path.deleteAnchor {"subpath":0,… |
| `path.deleteAnchor` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …:[0,40]}`, `path.deleteAnchor {"subpath":0,… |
| `path.fill` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `path.fill {"name":"Arch","color":"#2E75B6"… |
| `path.info` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …knot":4}`, `path.info {}`, `path.clippingPa… |
| `path.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …:"Clip"}` (`path.list` clippingPath {name:"… |
| `path.mergeShapeComponents` | V | reference/log.md#Log: …exclude`), `path.mergeShapeComponents` (two overlapping squares became one combine… |
| `path.moveAnchors` | V+ | reference/everyday-edits.md#Newer commands and options (ve…: …ddAnchor`, `path.moveAnchors`, …) take `"ty… · limit: workflows-and-tools.md: …lso listed, not run: `path.moveAnchors/moveHandle/bendSegmen… |
| `path.moveHandle` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …00,120]}`, `path.moveHandle {"subpath","kno… |
| `path.rename` | V+ | reference/workflows-and-tools.md#Paths and channels (verif…: `path.rename {"to":"Arch"}` saves it (`path… · limit: painting-a-portrait.md: `path.rename {"to":name}` fails with "a path named X already… |
| `path.set` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …om a path: `path.set` → `layer.select` the … |
| `path.setOperation` | V | reference/log.md#Log: …0 and run: `path.setOperation {"subpaths":[1],"op":"subtract"}` (the second square… |
| `path.stroke` | V | reference/workflows-and-tools.md#Paths and channels (verif…: …":80}` and `path.stroke {"name":"Arch","siz… |
| `path.style.copyFill` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …:4}` after `path.style.copyFill`: the ellip… |
| `path.style.copyStroke` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (3): `path.style.copyStroke` copies t… · limit: command-sweeps.md: Refused … `path.style.copyStroke` (command path.style.copyStroke is no… |
| `path.style.pasteFill` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `path.style.pasteFill` `{"layer":4}` after … |
| `path.style.pasteStroke` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `path.style.pasteStroke` `{"layer":4}` gave… · limit: command-sweeps.md: Refused … `path.style.pasteStroke` (command path.style.copyStroke is n… |
| `path.subtractFromSelection` | V | reference/log.md#Log: …election`, `path.subtractFromSelection` (render checked), `layer.smartObjects.expo… |
| `path.toSelection` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `path.toSelection {"name":"Arch","feather":… |
| `path.transform` | V | reference/workflows-and-tools.md#Paths and channels (verif…: `path.transform {"name":…,"matrix":[a,b,c,d… |

## pattern (10)

| id | status | note |
|---|---|---|
| `pattern.delete` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `pattern.delete {"pattern"}` |
| `pattern.export` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `pattern.export {"path":"x.pat","patterns":… |
| `pattern.import` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `pattern.import {"path":"x.pat"}` → `{impor… |
| `pattern.list` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: patterns: `pattern.list`, `edit.fill {"cont… |
| `pattern.presets.apply` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …with ids), `pattern.presets.apply {"pattern… |
| `pattern.presets.edit` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (2): `pattern.presets.edit` `rename` … · limit: command-sweeps.md: Refused … `pattern.presets.edit` (invalid parameters for pattern.prese… |
| `pattern.presets.list` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …presets: `pattern.presets.list` (group Ge… |
| `pattern.presets.new` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `pattern.presets.new {"name":"TmpPat","rect… |
| `pattern.presets.select` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `pattern.presets.select` `{"pattern":"Brick… |
| `pattern.rename` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `pattern.rename {"pattern","name"}` |

## plugin (5)

| id | status | note |
|---|---|---|
| `plugin.install` | s | reference/workflows-and-tools.md#Slices, preset libraries,…: Not run … - Not run: `.grd`/`.abr` imports, `count.cl… |
| `plugin.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …iled:[]}`, `plugin.list` then shows it and … |
| `plugin.reload` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …n. (3): `plugin.reload` `{"path":FOLDER}… · limit: command-sweeps.md: Refused … `plugin.reload` (error: `plugin.reload`: invalid parameters … |
| `plugin.remove` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `plugin.remove` `{"id":"org.test.invert"}` … · limit: command-sweeps.md: Refused … `plugin.remove` (error: `plugin.remove`: no plug-in "nope" i… |
| `plugin.run` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `plugin.run` `{"id":"org.test.invert"}` on … · limit: command-sweeps.md: Refused … `plugin.run` (error: `plugin.run`: command `plugin.run` is n… |

## prefs (3)

| id | status | note |
|---|---|---|
| `prefs.get` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (3): `prefs.get` `{"path":"performanc… |
| `prefs.reset` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `prefs.reset` `{"path":"unitsAndRulers"}` r… |
| `prefs.set` | V+ | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `prefs.set` `{"path","value"}` or `{"values… · limit: command-sweeps.md: Refused … `prefs.set` (invalid parameters for prefs.set: give path and… |

## select (35)

| id | status | note |
|---|---|---|
| `select.all` | V | reference/everyday-edits.md#Image commands, selections, to…: …ections: `select.all\|deselect\|inverse`, `… |
| `select.allLayers` | V | reference/everyday-edits.md#Image commands, selections, to…: layers: `select.allLayers` → `{selected:2}`… |
| `select.colorRange` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …ction ids: `select.colorRange`, `select.gro… |
| `select.convertToShape` | V | reference/everyday-edits.md#Image commands, selections, to…: …orkPath`), `select.convertToShape {"toleran… |
| `select.deselect` | V+ | reference/everyday-edits.md#Everyday photo edits (verified…: ….inverse`, `select.deselect`. · limit: live-mode.md: … consumed (`select.deselect` then fails with "no selection")… |
| `select.deselectLayers` | V | reference/everyday-edits.md#Image commands, selections, to…: …ted:[3]}`, `select.deselectLayers`, `select… |
| `select.drop` | V | reference/everyday-edits.md#Image commands, selections, to…: … pixels) + `select.drop` → `{dropped}`, |
| `select.editInQuickMaskMode` | V | reference/everyday-edits.md#Image commands, selections, to…: …ed:true}`, `select.editInQuickMaskMode {"on… |
| `select.findLayers` | V | reference/everyday-edits.md#Image commands, selections, to…: …ected:2}`, `select.findLayers {"name":"Elli… |
| `select.float` | V | reference/everyday-edits.md#Image commands, selections, to…: …y picture, `select.float {"dx","dy","copy"}… |
| `select.focusArea` | V | reference/live-mode.md#Live mode and removing a background…: `select.focusArea` gave patchy strips |
| `select.grow` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …lorRange`, `select.grow`, `select.modify.fe… |
| `select.inverse` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …radius"}`, `select.inverse`, `select.desele… |
| `select.isolateLayers` | V | reference/everyday-edits.md#Image commands, selections, to…: …ctLayers`, `select.isolateLayers {"on":true… |
| `select.lasso` | V | reference/everyday-edits.md#Retouching, compositing and se…: …ternative: `select.lasso {"points":[…12 poi… |
| `select.loadLuminosity` | V | reference/everyday-edits.md#Image commands, selections, to…: …ind path), `select.loadLuminosity` → `{sele… |
| `select.loadSelection` | V | reference/everyday-edits.md#Retouching, compositing and se…: `select.loadSelection {"channel":"Face","in… |
| `select.magicWand` | V | reference/everyday-edits.md#Image commands, selections, to…: … dropped), `select.magicWand {"x","y","tole… |
| `select.magneticLasso` | V+ | reference/everyday-edits.md#Image commands, selections, to…: …elected}`, `select.magneticLasso {"points":… · limit: everyday-edits.md: Not run … - Not run: `actions.photoshopStep` (needs a `.atn` step), `i… |
| `select.modify.border` | V | reference/everyday-edits.md#Image commands, selections, to…: …erance"}`, `select.modify.border {"radius":… |
| `select.modify.contract` | V | reference/live-mode.md#Live mode and removing a background…: …yer":3}` → `select.modify.contract {"radius… |
| `select.modify.expand` | V | reference/everyday-edits.md#Retouching, compositing and se…: …roup…]}` → `select.modify.expand {"radius":… |
| `select.modify.feather` | V | reference/everyday-edits.md#Everyday photo edits (verified…: …ect.grow`, `select.modify.feather {"radius"… |
| `select.modify.smooth` | V | reference/live-mode.md#Live mode and removing a background…: …rves, then `select.modify.smooth` or refine… |
| `select.object` | V | reference/live-mode.md#Live mode and removing a background…: `select.object {"rect":[x,y,w,h]}` cut thro… |
| `select.quick` | V | reference/live-mode.md#Live mode and removing a background…: `select.quick` with positive then `mode:"su… |
| `select.rect` | V | reference/everyday-edits.md#Everyday photo edits (verified…: `select.rect {"x":300,"y":200,"width":600,"… |
| `select.refineEdge` | V | reference/live-mode.md#Live mode and removing a background…: `select.refineEdge {"radius":6,"smartRadius… |
| `select.reselect` | V | reference/everyday-edits.md#Image commands, selections, to…: …\|inverse`, `select.reselect` ("no selection… |
| `select.saveSelection` | V | reference/everyday-edits.md#Retouching, compositing and se…: …er":20}` → `select.saveSelection {"name":"F… |
| `select.similar` | V | reference/everyday-edits.md#Image commands, selections, to…: …nce":32}`, `select.similar {"tolerance"}`, … |
| `select.sky` | V | reference/everyday-edits.md#Image commands, selections, to…: …ickMask}`, `select.sky {}` → `{changed:fals… |
| `select.subject` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: …ckground): `select.subject {}` → `{bounds:[… |
| `select.toWorkPath` | V | reference/everyday-edits.md#Image commands, selections, to…: `select.toWorkPath {"tolerance":2}` → `{sub… |
| `select.transformSelection` | V | reference/everyday-edits.md#Image commands, selections, to…: …ed:true}`, `select.transformSelection {"rec… |

## session (1)

| id | status | note |
|---|---|---|
| `session.inspect` | V | reference/command-sweeps.md#The last 28 command ids (2026-…: …ows-only); `session.inspect {}` → documents… |

## shape (10)

| id | status | note |
|---|---|---|
| `shape.create` | V | SKILL.md#Recipes: …ent fill → `shape.create` rounded rect → `layer.layerStyle.dropShadow` |
| `shape.edit` | V | SKILL.md#Commands that worked (exact parameter formats): …ounds,…}`; `shape.edit`, `shape.info`, `shape.r… |
| `shape.info` | V | SKILL.md#Commands that worked (exact parameter formats): …ape.edit`, `shape.info`, `shape.rasterize`. |
| `shape.presets.edit` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (3): `shape.presets.edit` `{"action":… |
| `shape.presets.importCsh` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: - `shape.presets.importCsh {"path":"x.csh… |
| `shape.presets.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `shape.presets.list` `{groups:[{name,shapes… |
| `shape.presets.new` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …presets: `shape.presets.new {"name":"Tri"… |
| `shape.presets.place` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `shape.presets.place {"preset":"Tri","rect"… |
| `shape.presets.reset` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `shape.presets.reset` restores the built-in… |
| `shape.rasterize` | V | SKILL.md#Commands that worked (exact parameter formats): …ape.info`, `shape.rasterize`. |

## slice (7)

| id | status | note |
|---|---|---|
| `slice.delete` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `slice.delete {"number":3}` → `{deleted:1}` |
| `slice.divide` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `slice.divide {"number":1,"horizontal":1,"v… |
| `slice.fromGuides` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `slice.fromGuides {}` replaces every slice … |
| `slice.list` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: … slices in `slice.list`) |
| `slice.new` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …*Slices: `slice.new {"rect":[0,0,200,150]… |
| `slice.promote` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `slice.promote {"number":3}` |
| `slice.set` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `slice.set {"number":2,"name","alt",…}` (an… |

## style (7)

| id | status | note |
|---|---|---|
| `style.presets.apply` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …up}`, then `style.presets.apply {"preset":"… |
| `style.presets.edit` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `style.presets.edit {"action":"rename",…}`. |
| `style.presets.exportAsl` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: `style.presets.exportAsl {"path":"x.asl","g… |
| `style.presets.importAsl` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: `style.presets.importAsl {"path":"x.asl","g… |
| `style.presets.list` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: …verified): `style.presets.list {}` → groups… |
| `style.presets.new` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …+ stroke), `style.presets.new {"name":"Card… |
| `style.presets.reset` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (1): `style.presets.reset` after `edi… |

## swatches (12)

| id | status | note |
|---|---|---|
| `swatches.add` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `swatches.add {"color":"#0E7C86","name":"Br… |
| `swatches.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (6): `swatches.delete` `{"swatch":"G"… |
| `swatches.deleteGroup` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `swatches.deleteGroup` removed group "Ours"… |
| `swatches.export` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `swatches.export {"format":"ase","path":"br… |
| `swatches.import` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …swatches), `swatches.import {"path":"brand.… |
| `swatches.list` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …watches: `swatches.list {}` → groups (Gra… |
| `swatches.move` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `swatches.move` `{"swatch":"B","to":"Mine",… |
| `swatches.newGroup` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `swatches.newGroup {"name":"Brand","swatche… |
| `swatches.rename` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `swatches.rename/delete {"swatch":name}` |
| `swatches.renameGroup` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `swatches.renameGroup` `{"group":"Mine","na… |
| `swatches.reset` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `swatches.reset` replaces the library with … |
| `swatches.use` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `swatches.use` `{"swatch":"R","target":"bac… |

## timeline (7)

| id | status | note |
|---|---|---|
| `timeline.create` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ame` after `timeline.create {duration:30,fp… |
| `timeline.delete` | V | reference/everyday-edits.md#Image commands, selections, to…: …ousFrame`, `timeline.delete` → `{timeline:n… |
| `timeline.info` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: …fps":5}` + `timeline.info` work and a `.gif… |
| `timeline.nextFrame` | V | reference/everyday-edits.md#Image commands, selections, to…: …reported), `timeline.nextFrame\|previousFram… |
| `timeline.previousFrame` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `timeline.previousFrame` after `… |
| `timeline.setFrame` | V | reference/everyday-edits.md#Image commands, selections, to…: …fps":10}`, `timeline.setFrame {"frame":3}` … |
| `timeline.setProps` | V | reference/everyday-edits.md#Image commands, selections, to…: …"fps":5}`, `timeline.setProps {"fps":10}`, … |

## tool (5)

| id | status | note |
|---|---|---|
| `tool.presets.edit` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (2): `tool.presets.edit` `{"action":"… |
| `tool.presets.list` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …nt brush), `tool.presets.list` (5 built-ins… |
| `tool.presets.new` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …presets: `tool.presets.new {"name":"Soft … |
| `tool.presets.reset` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `tool.presets.reset` removes user presets a… |
| `tool.presets.select` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …ft 40 px), `tool.presets.select {"preset"}`… |

## tools (13)

| id | status | note |
|---|---|---|
| `tools.decreaseBrushHardness` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (5): `tools.decreaseBrushHardness` ha… |
| `tools.decreaseBrushSize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `tools.decreaseBrushSize` brush size 20 -> … |
| `tools.defaultColors` | V | reference/everyday-edits.md#Image commands, selections, to…: …apColors`, `tools.defaultColors`, `tools.se… |
| `tools.firstBrush` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `tools.firstBrush/lastBrush` → Hard Round /… |
| `tools.increaseBrushHardness` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `tools.increaseBrushHardness` hardness 0.75… |
| `tools.increaseBrushSize` | V | reference/everyday-edits.md#Image commands, selections, to…: …ll brush), `tools.increaseBrushSize\|decreas… |
| `tools.lastBrush` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `tools.lastBrush` selects the last preset i… |
| `tools.nextBrush` | V | reference/everyday-edits.md#Image commands, selections, to…: …Hardness`, `tools.nextBrush\|previousBrush\|f… |
| `tools.previousBrush` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `tools.previousBrush` steps back one preset… |
| `tools.rotateBrush` | V | reference/everyday-edits.md#Image commands, selections, to…: …l Grain"), `tools.rotateBrush {"degrees":30… |
| `tools.setBrush` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …nged): use `tools.setBrush {"preset":name}`… |
| `tools.setColors` | V | reference/everyday-edits.md#Image commands, selections, to…: …colours: `tools.setColors {"foreground":"… |
| `tools.swapColors` | V | reference/everyday-edits.md#Image commands, selections, to…: …undCmyk`), `tools.swapColors`, `tools.defau… |

## type (98)

| id | status | note |
|---|---|---|
| `type.antiAlias.crisp` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (6): `type.antiAlias.crisp` {antialia… |
| `type.antiAlias.none` | V | reference/everyday-edits.md#Image commands, selections, to…: …mes back), `type.antiAlias.none\|sharp\|crisp… |
| `type.antiAlias.sharp` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.antiAlias.sharp` {antialias:"sharp"} … |
| `type.antiAlias.smooth` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.antiAlias.smooth` {antialias:"smooth"… |
| `type.antiAlias.strong` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.antiAlias.strong` {antialias:"strong"… |
| `type.antiAlias.windows` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.antiAlias.windows` {antialias:"window… |
| `type.antiAlias.windowsLcd` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.antiAlias.windowsLcd` {antialias:"win… |
| `type.attachToPath` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ath` after `type.attachToPath {"layer":4,"s… |
| `type.caret` | V | reference/everyday-edits.md#Image commands, selections, to…: `type.caret {"index":3}` → `{line,segment:[… |
| `type.characterStyle.apply` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (7): `type.characterStyle.apply` appl… |
| `type.characterStyle.clearOverride` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.characterStyle.clearOverride` charact… |
| `type.characterStyle.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.characterStyle.delete` list is back t… |
| `type.characterStyle.duplicate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.characterStyle.duplicate` list adds i… |
| `type.characterStyle.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `type.characterStyle.list` `{cur… |
| `type.characterStyle.new` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …S1 made by `type.characterStyle.new` with t… |
| `type.characterStyle.redefine` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.characterStyle.redefine` redefine fro… |
| `type.characterStyle.rename` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.characterStyle.rename` list shows the… |
| `type.characterStyle.set` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.characterStyle.set` list shows the at… |
| `type.convertToParagraphText` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …families), `type.convertToParagraphText/Poi… |
| `type.convertToPointText` | V | reference/everyday-edits.md#Image commands, selections, to…: `type.convertToPointText` on point text: "t… |
| `type.convertToShape` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …aths:12}`, `type.convertToShape {}` (type →… |
| `type.create` | V | SKILL.md#Recipes: → `type.create` → `hueSaturation` adjustment → `--out card.png` (rendered correctly). |
| `type.createSelection` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …end":40}`, `type.createSelection`, `type.an… |
| `type.createWorkPath` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …n/effects: `type.createWorkPath {}` → `{sub… |
| `type.decreaseSize` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - type.decreaseSize. (1): `type.decrea… |
| `type.decreaseSizeMore` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - type.decreaseSizeMore. (1): `type.de… |
| `type.detachFromPath` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `type.detachFromPath` after `typ… |
| `type.edit` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …`bounds`). `type.edit {"replace":{"start":0… |
| `type.fillPath` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: - `type.fillPath {"layer"?:id,"shape"?:la… |
| `type.font.favorite` | V | reference/everyday-edits.md#Newer commands and options (ve…: - `type.font.favorite {"family":"Arial","… |
| `type.font.library` | V | reference/everyday-edits.md#Newer commands and options (ve…: `type.font.library {}` → `{favorites}`. |
| `type.fonts` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …,inside}`, `type.fonts {}` (installed famil… |
| `type.hitTest` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: ….info {}`, `type.hitTest {"x","y"}` → `{ind… |
| `type.increaseSize` | V | reference/everyday-edits.md#Image commands, selections, to…: … layout: `type.increaseSize\|decreaseSize\|… |
| `type.increaseSizeMore` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - type.increaseSizeMore. (1): `type.in… |
| `type.info` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …ayer.list`/`type.info`/`*.list` read-backs … |
| `type.insertText` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …les kept), `type.insertText {"text":" [adde… |
| `type.loadDefaultTypeStyles` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - type.loadDefaultTypeStyles. (1): `ty… |
| `type.navigate` | V | reference/everyday-edits.md#Image commands, selections, to…: …,[x,y]]}`, `type.navigate {"index":3,"move"… |
| `type.openType.contextualAlternates` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (7): `type.openType.contextualAlterna… |
| `type.openType.discretionaryLigatures` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.discretionaryLigatures` retu… |
| `type.openType.fractions` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.fractions` returns {feature:… |
| `type.openType.numerals.default` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: - `type.openType.numerals.default`, `type… |
| `type.openType.numerals.lining` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: ….default`, `type.openType.numerals.lining`,… |
| `type.openType.numerals.oldstyle` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: …s.lining`, `type.openType.numerals.oldstyle… |
| `type.openType.numerals.proportional` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: …oldstyle`, `type.openType.numerals.proporti… |
| `type.openType.numerals.proportionalLining` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: …ortional`, `type.openType.numerals.proporti… |
| `type.openType.numerals.proportionalOldstyle` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: …alLining`, `type.openType.numerals.proporti… |
| `type.openType.numerals.tabular` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: …Oldstyle`, `type.openType.numerals.tabular`… |
| `type.openType.numerals.tabularLining` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: ….tabular`, `type.openType.numerals.tabularL… |
| `type.openType.numerals.tabularOldstyle` | V | reference/workflows-and-tools.md#New in 0.20.2: action his…: …arLining`, `type.openType.numerals.tabularO… |
| `type.openType.oldstyle` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.oldstyle` returns {feature:"… |
| `type.openType.ordinals` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.ordinals` returns {feature:"… |
| `type.openType.ornaments` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (2): `type.openType.ornaments` `{"on"… |
| `type.openType.standardLigatures` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: OpenType: `type.openType.standardLigatures\|… |
| `type.openType.stylisticAlternates` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.stylisticAlternates` returns… |
| `type.openType.stylisticSets.set1` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …ic sets: `type.openType.stylisticSets.set… |
| `type.openType.stylisticSets.set10` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set11` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set12` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set13` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set14` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set15` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set16` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set17` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set18` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set19` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set2` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set20` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set3` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set4` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set5` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set6` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set7` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set8` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.stylisticSets.set9` | V | reference/workflows-and-tools.md#0.21.0 changes: frames, O…: …y ids (ran, no visible effect checked: the … |
| `type.openType.swash` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.swash` returns {feature:"sws… |
| `type.openType.titlingAlternates` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.openType.titlingAlternates` same for … |
| `type.orientation.horizontal` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …n. (1): `type.orientation.horizontal` af… |
| `type.orientation.vertical` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …tal` after `type.orientation.vertical` (bou… |
| `type.paragraphStyle.apply` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (7): `type.paragraphStyle.apply` appl… |
| `type.paragraphStyle.clearOverride` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.paragraphStyle.clearOverride` charact… |
| `type.paragraphStyle.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.paragraphStyle.delete` list is back t… |
| `type.paragraphStyle.duplicate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.paragraphStyle.duplicate` list adds i… |
| `type.paragraphStyle.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …e. (1): `type.paragraphStyle.list` `{cur… |
| `type.paragraphStyle.new` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `type.paragraphStyle.new/apply/list` manage… |
| `type.paragraphStyle.redefine` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.paragraphStyle.redefine` redefine fro… |
| `type.paragraphStyle.rename` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.paragraphStyle.rename` list shows the… |
| `type.paragraphStyle.set` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `type.paragraphStyle.set` list shows the at… |
| `type.pasteLoremIpsum` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …`{caret}`, `type.pasteLoremIpsum {}`, `type… |
| `type.rasterize` | V | reference/everyday-edits.md#Image commands, selections, to…: …updated}`, `type.rasterize` → `{layer}` |
| `type.rasterizeTypeLayer` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - type.rasterizeTypeLayer. (1): `type.… |
| `type.replaceAllMissingFonts` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: - type.replaceAllMissingFonts. (1): `t… |
| `type.resolveMissingFonts` | V | reference/everyday-edits.md#Image commands, selections, to…: …index:5}`, `type.resolveMissingFonts {}` → … |
| `type.saveDefaultTypeStyles` | V | reference/everyday-edits.md#Image commands, selections, to…: …sing:[]}`, `type.saveDefaultTypeStyles` / `… |
| `type.setStyle` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …e command: `type.setStyle {"range":[0,6],"c… |
| `type.updateAllTextLayers` | V | reference/everyday-edits.md#Image commands, selections, to…: …nt,size}`, `type.updateAllTextLayers` → `{u… |
| `type.warpText` | V | reference/workflows-and-tools.md#Next-tier workflows (veri…: `type.warpText {"style":"arc\|flag\|wave\|fish… |

## updates (1)

| id | status | note |
|---|---|---|
| `updates.status` | V | reference/everyday-edits.md#Version 0.16.0 notes (2026-10-…: …rUpdates`, `updates.status` (935 → 940). |

## variables (1)

| id | status | note |
|---|---|---|
| `variables.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (1): `variables.list` `{active,dataSe… |

## view (31)

| id | status | note |
|---|---|---|
| `view.clearCanvasGuides` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …arGuides`, `view.clearCanvasGuides` ran |
| `view.clearGuides` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …oveGuide`, `view.clearGuides`, `view.clearC… |
| `view.clearSelectedArtboardGuides` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …w. (1): `view.clearSelectedArtboardGuide… |
| `view.clearSlices` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …ckSlices`, `view.clearSlices`. |
| `view.colorSamplers.add` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …erOrigin`, `view.colorSamplers.add {"x","y"… |
| `view.colorSamplers.clear` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …s. (3): `view.colorSamplers.clear` `{del… |
| `view.colorSamplers.delete` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.colorSamplers.delete` `{"index":0}` -… |
| `view.colorSamplers.list` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.colorSamplers.list` `{samplers:[{inde… |
| `view.colorSamplers.move` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …{bounds}`, `view.colorSamplers.move/list/de… |
| `view.deleteGuide` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …"color"}`, `view.deleteGuide {"orientation"… |
| `view.editGuide` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: `view.editGuide {"orientation","index","pos… |
| `view.gamutWarning` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …":false}`, `view.gamutWarning {"on":true,"t… |
| `view.layerMask` | V | reference/everyday-edits.md#Newer commands and options (ve…: - `view.layerMask {"mask":"layer\|filter"}… |
| `view.lockSlices` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …verlay"}`, `view.lockSlices`, `view.clearSl… |
| `view.moveGuide` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …erOrigin`, `view.moveGuide`, `view.clearGui… |
| `view.newGuide` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: … View: `view.newGuide {"orientation":"v… |
| `view.newGuideLayout` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: …arGuides`, `view.newGuideLayout {"columns":… |
| `view.newGuidesFromShape` | V | reference/workflows-and-tools.md#Slices, preset libraries,…: …entation), `view.newGuidesFromShape {}` → `… |
| `view.proofColors` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …still off (`view.proofColors` then turned i… |
| `view.proofSetup` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …w. (1): `view.proofSetup` `{"profile":"w… |
| `view.proofSetup.colorBlindnessDeuteranopia` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: …p. (7): `view.proofSetup.colorBlindnessD… |
| `view.proofSetup.colorBlindnessProtanopia` | V | reference/workflows-and-tools.md#Type, transforms, swatche…: `view.proofSetup.colorBlindnessProtanopia {… |
| `view.proofSetup.legacyMacintoshRgb` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.proofSetup.legacyMacintoshRgb` sets p… |
| `view.proofSetup.workingBlackPlate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.proofSetup.workingBlackPlate` sets pr… |
| `view.proofSetup.workingCmyPlate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.proofSetup.workingCmyPlate` sets proo… |
| `view.proofSetup.workingCyanPlate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.proofSetup.workingCyanPlate` sets pro… |
| `view.proofSetup.workingMagentaPlate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.proofSetup.workingMagentaPlate` sets … |
| `view.proofSetup.workingYellowPlate` | V | reference/command-sweeps.md#Verified in detail, PhotoCraft…: `view.proofSetup.workingYellowPlate` sets p… |
| `view.resetRulerOrigin` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: …,"y":50}`, `view.resetRulerOrigin`, `view.m… |
| `view.setRulerOrigin` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `view.setRulerOrigin {"x":100,"y":50}`, `vi… |
| `view.thirtyTwoBitPreviewOptions` | V | reference/everyday-edits.md#Layer arrangement, shape combi…: `view.thirtyTwoBitPreviewOptions` only on a… |
