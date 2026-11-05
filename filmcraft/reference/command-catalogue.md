# FilmCraft reference: command catalogue (third round)

Part of the filmcraft skill. The short front page is `../SKILL.md`. **filmcraft-cli 0.17.1**, 2026-11-04: the 589
command ids not covered by the earlier reference files, run headless on a test project (two 4 s clips with tone, a
still, a WAV) and, where a panel was needed, in the live app over `--bridge`. Levels:
**verified** = the same field read before and after (JSON path, old → new); **returned a result** = a read/list command returned real data, or an action answered without a before/after comparison; **ran** = accepted but no change could be read back (often nothing to act on in the test project);
**refused/blocked** = the command's own message, which names the state or parameter it needs.

Setup that unlocked most commands (same script, because selection does not survive a save/reopen):
`project.select {items:[<bin item id>]}` for "select an item in the Project panel"; `timeline.select` for "no clips
selected" (select the **audio** clip for gain/volume commands); `graphics.newText` first for every `graphics.*` command
(then `graphics.list {clip}` → `layers[0]`: `position` moves with alignFrame/nudge, `localBounds` with alignText/fontSize/
leading; leading needs a two-line title); `captions.newTrack` + `captions.add` for caption commands. `file.new*`
(colour matte, bars and tone, offline file, transparent video, counting leader, adjustment layer) add a bin item only.


## audio

Returned a result (read tools, or actions whose result was not compared before/after): `audio.toggleScrubbing`, `audio.voiceover.settings`, `audio.voiceover.start`

Refused or blocked in the test project: `audio.voiceover.stop` (not available right now: no voice-over is recording command `audio.voiceover.stop` is not ); `audio.voiceover.sync` (not available right now: no voice-over is recording command `audio.voiceover.sync` is not )

## captions

Verified: `captions.goTo` sequence.playhead null → 50803200000; `captions.next` sequence.playhead null → 50803200000

Returned a result (read tools, or actions whose result was not compared before/after): `captions.list`, `captions.select`, `captions.showActiveOnly`

Ran, no change read back: `captions.deleteTrack`, `captions.hideAll`, `captions.setTrack`, `captions.showAll`

Refused or blocked in the test project: `captions.merge`; `captions.previous`; `captions.trim` (invalid parameters for `captions.trim`: no caption (pass `caption` or select one) invalid )

## clip

Verified: `clip.automateToSequence` project.root.children[4].duration 1016064000000 → 2032128000000; sequence.duration 1016064000000 → 2032128000000; `clip.breakoutToMono` new bin item (root.children[5], duration 1016064000000 ticks); `clip.createMulticam` new bin item (root.children[5], duration 1016064000000 ticks); `clip.extractAudio` new bin item (root.children[5], duration 1016064000000 ticks); `clip.insertFrameHoldSegment` project.root.children[4].duration 1016064000000 → 1270080000000; sequence.duration 1016064000000 → 1270080000000; `clip.makeSubclip` new bin item (root.children[5], duration 1016064000000 ticks); `clip.nest` new bin item (root.children[5], duration 1016064000000 ticks)

Returned a result (read tools, or actions whose result was not compared before/after): `clip.audioPeak`, `clip.clearPosterFrame`, `clip.fieldOptions`, `clip.fillFrame`, `clip.fitToFrame`, `clip.frameHoldOptions`, `clip.generateAudioWaveform`, `clip.link`, `clip.revealInProject`, `clip.sceneEditDetection`, `clip.setPosterFrame`, `clip.sourceSettings`, `clip.timeInterpolation.frameBlending`, `clip.timeInterpolation.frameSampling`, `clip.timeInterpolation.opticalFlow`, `clip.updateMetadata`

Ran, no change read back: `clip.enable`, `clip.nudgeVolumeDown1`, `clip.nudgeVolumeDown3`, `clip.nudgeVolumeUp1`, `clip.nudgeVolumeUp3`, `clip.rename`, `clip.volumeDown`, `clip.volumeDownMany`, `clip.volumeUp`, `clip.volumeUpMany`

Refused or blocked in the test project: `clip.editOffline` (not available right now: select an offline clip command `clip.editOffline` is not availabl); `clip.editSubclip` (not available right now: select a subclip in the Project panel command `clip.editSubclip` ); `clip.group` (not available right now: no clips selected command `clip.group` is not available right now); `clip.interpretFootage` (not available right now: select footage in the Project panel or clips in the timeline comm); `clip.mergeClips` (not available right now: select a video clip and audio clips in the Project panel or the T); `clip.modifyTimecode` (not available right now: select a clip in the Project panel command `clip.modifyTimecode` ); `clip.multicamEnable` (not available right now: no clips selected command `clip.multicamEnable` is not available ); `clip.multicamFlatten` (not available right now: no clips selected command `clip.multicamFlatten` is not available); `clip.remix` (invalid parameters for `clip.remix`: select an audio clip or pass `clip` invalid parameter); `clip.remix.enable` (not available right now: select an audio clip command `clip.remix.enable` is not available); `clip.remix.properties` (not available right now: select an audio clip command `clip.remix.properties` is not avail); `clip.remix.revert` (not available right now: select an audio clip command `clip.remix.revert` is not available); `clip.replaceFromBin` (not available right now: no clips selected command `clip.replaceFromBin` is not available ); `clip.replaceFromSource` (not available right now: no clips selected command `clip.replaceFromSource` is not availab); `clip.replaceFromSourceMatchFrame` (not available right now: no clips selected command `clip.replaceFromSourceMatchFrame` is n); `clip.restoreCaptionsFromSource` (not available right now: the clip); `clip.scaleToFrameSize` (not available right now: no clips selected command `clip.scaleToFrameSize` is not availabl); `clip.setTimeInterpolation` (not available right now: no clips selected command `clip.setTimeInterpolation` is not avai); `clip.speedDuration` (not available right now: no clips selected command `clip.speedDuration` is not available r); `clip.synchronize` (not available right now: select at least two clips to synchronize command `clip.synchroniz); `clip.ungroup` (not available right now: no clips selected command `clip.ungroup` is not available right n)

## clipMixer

Refused or blocked in the test project: `clipMixer.release` (invalid parameters for `clipMixer.release`: need `strip` (); `clipMixer.set` (invalid parameters for `clipMixer.set`: need `clip` invalid parameters for `clipMixer.set`); `clipMixer.setMode` (invalid parameters for `clipMixer.setMode`: need `strip` (); `clipMixer.touch` (invalid parameters for `clipMixer.touch`: need `strip` ()

## color

Returned a result (read tools, or actions whose result was not compared before/after): `color.spaces`

## colors

Verified: `colors.addCustom` {name:"Round3", color:"#336699"} → colour listed; per session: add and use in the SAME script; `colors.removeCustom` {color:"#336699"} (the hex, not the name) → colour gone

Refused or blocked in the test project: `colors.updateCustom` ("no such saved color": old→new params not in describe)

## command

Returned a result (read tools, or actions whose result was not compared before/after): `command.list`

## edit

Verified: `edit.clear` project.root.children[4].duration 1016064000000 → 0; sequence.duration 1016064000000 → 0; `edit.duplicate` new bin item (root.children[5], duration 1016064000000 ticks); `edit.find` sequence.playhead 254016000000 → 0; `edit.removeUnused` project.root.children[1].item 2 → 7; project.root.children[1].label "Iris" → "Forest"; `edit.rippleDelete` project.root.children[4].duration 1016064000000 → 0; sequence.duration 1016064000000 → 0; `edit.rippleDeleteHead` project.root.children[4].duration 1016064000000 → 762048000000; sequence.duration 1016064000000 → 762048000000

Returned a result (read tools, or actions whose result was not compared before/after): `edit.consolidateDuplicates`, `edit.editOriginal`, `edit.label.iris`, `edit.removeAttributes`, `edit.selectAll`, `edit.selectAllMatching`, `edit.selectLabelGroup`

Ran, no change read back: `edit.deselectAll`, `edit.label`, `edit.label.blue`, `edit.label.brown`, `edit.label.caribbean`, `edit.label.cerulean`, `edit.label.forest`, `edit.label.green`, `edit.label.lavender`, `edit.label.magenta`, `edit.label.mango`, `edit.label.purple`, `edit.label.rose`, `edit.label.tan`, `edit.label.teal`, `edit.label.violet`, `edit.label.yellow`

Refused or blocked in the test project: `edit.findNext` (not available right now: use Find… first command `edit.findNext` is not available right no); `edit.pasteAttributes` (not available right now: copy a clip first command `edit.pasteAttributes` is not available); `edit.pasteInsert` (not available right now: clipboard is empty command `edit.pasteInsert` is not available ri); `edit.pasteMedia` (invalid parameters for `edit.pasteMedia`: need `paths` invalid parameters for `edit.pasteM)

## effects

Refused or blocked in the test project: `effects.deleteKeyframe` (invalid parameters for `keyframe`: need `clip` invalid parameters for `keyframe`: need `cl); `effects.moveKeyframe` (invalid parameters for `keyframe`: need `clip` invalid parameters for `keyframe`: need `cl); `effects.moveKeyframes` (invalid parameters for `effects.moveKeyframes`: need keyframes invalid parameters for `eff); `effects.setInterpolation` (invalid parameters for `keyframe`: need `clip` invalid parameters for `keyframe`: need `cl); `effects.setKeyframe` (invalid parameters for `keyframe`: need `clip` invalid parameters for `keyframe`: need `cl); `effects.toggleEnabled` (invalid parameters for `effects.toggleEnabled`: need `clip` invalid parameters for `effect)

## essentialSound

Returned a result (read tools, or actions whose result was not compared before/after): `essentialSound.clearType`

Refused or blocked in the test project: `essentialSound.applyPreset` (invalid parameters for `essentialSound.applyPreset`: need `preset` invalid parameters for ); `essentialSound.autoMatch` (invalid parameters for `essentialSound.autoMatch`: no clips with an audio type and audible); `essentialSound.deletePreset` (invalid parameters for `essentialSound.deletePreset`: need `name` invalid parameters for `); `essentialSound.generateDucking` (invalid parameters for `essentialSound.generateDucking`: select Music or Ambience clips (d); `essentialSound.savePreset` (invalid parameters for `essentialSound.savePreset`: need `name` invalid parameters for `es)

## events

Returned a result (read tools, or actions whose result was not compared before/after): `events.clear`, `events.list`

## export

Ran, no change read back: `export.queue.clear`, `export.queue.stop`, `export.quick`

Refused or blocked in the test project: `export.presets.delete` (invalid parameters for `export.presets.delete`: need `name` invalid parameters for `export); `export.presets.export` (invalid parameters for `export.presets.export`: need `path` invalid parameters for `export); `export.presets.import` (invalid parameters for `export.presets.import`: need `path` invalid parameters for `export); `export.presets.save` (invalid parameters for `export.presets.save`: need a `name` invalid parameters for `export); `export.queue.move` (invalid parameters for `export.queue.move`: need `id` (see export.queue.list) invalid para); `export.queue.remove` (invalid parameters for `export.queue.remove`: need `id` (see export.queue.list) invalid pa); `export.queue.retry` (invalid parameters for `export.queue.retry`: need `id` (see export.queue.list) invalid par)

## file

Verified: `file.closeAllProjects` project.activeSequence 7 → "<absent>"; project.root.children[0].customLabelColor null → "<absent>"; `file.closeProject` project.activeSequence 7 → "<absent>"; project.root.children[0].customLabelColor null → "<absent>"; `file.importDemoFootage` new bin item (root.children[10], duration 2540160000000 ticks); `file.newAdjustmentLayer` new bin item (root.children[5], duration 508032000000 ticks); `file.newBarsAndTone` new bin item (root.children[5], duration 762048000000 ticks); `file.newBin` project.root.children[5].id "<absent>" → 11; project.root.children[5].name "<absent>" → "B"; `file.newBinFromSelection` project.root.children[0].item 1 → 2; project.root.children[0].name "clip1.mp4" → "clip2.mp4"; `file.newBlackVideo` new bin item (root.children[5], duration 1270080000000 ticks); `file.newColorMatte` new bin item (root.children[5], duration 508032000000 ticks); `file.newCountingLeader` new bin item (root.children[5], duration 1270080000000 ticks); `file.newOfflineFile` new bin item (root.children[5], duration 2540160000000 ticks); `file.newTransparentVideo` new bin item (root.children[5], duration 1270080000000 ticks)

Returned a result (read tools, or actions whose result was not compared before/after): `file.mediaProperties`, `file.reveal`

Ran, no change read back: `file.autoSaveStatus`, `file.close`, `file.listAutoSaves`, `file.mediaPropertiesFile`, `file.projectSettings.general`, `file.projectSettings.scratchDisks`, `file.recoveryList`, `file.revert`, `file.saveAll`, `file.saveCopy`, `file.templates`

Refused or blocked in the test project: `file.autoSaveNow`; `file.closeAllOtherProjects` (not available right now: only one project is open command `file.closeAllOtherProjects` is ); `file.discardRecovery` (not available right now: there are no unsaved changes to recover command `file.discardReco); `file.exportGraphicsTemplate` (not available right now: select a graphic clip command `file.exportGraphicsTemplate` is no); `file.exportSelectionProject` (not available right now: select an item in the Project panel command `file.exportSelection); `file.importAaf` (invalid parameters for `file.importAaf`: need `path` invalid parameters for `file.importAa); `file.importFromMediaBrowser` (invalid parameters for `file.importFromMediaBrowser`: select files in the Media Browser in); `file.newSearchBin` (invalid parameters for `file.newSearchBin`: enter text to search for invalid parameters fo); `file.projectManager` (invalid parameters for `file.projectManager`: need `destination` invalid parameters for `f); `file.recover` (not available right now: there are no unsaved changes to recover command `file.recover` is); `file.replaceFonts` (invalid parameters for `file.replaceFonts`: need `from` (a family, or {family, style}) inv); `file.saveAsTemplate` (invalid parameters for `file.saveAsTemplate`: need `path` (no data directory for templates)

## fonts

Returned a result (read tools, or actions whose result was not compared before/after): `fonts.list`

## graphics

Verified: `graphics.alignFrame.bottom` layers[0].position[1] 60.0 → 136.46484375; layers[0].quad[0][1] 30.9375 → 107.40234375; `graphics.alignFrame.left` layers[0].position[0] 20.0 → 0.0; layers[0].quad[0][0] 20.0 → 0.0; `graphics.alignFrame.right` layers[0].position[0] 20.0 → 275.3515625; layers[0].quad[0][0] 20.0 → 275.3515625; `graphics.alignFrame.top` layers[0].position[1] 60.0 → 29.0625; layers[0].quad[0][1] 30.9375 → 0.0; `graphics.alignFrame.vcenter` layers[0].position[1] 60.0 → 82.763671875; layers[0].quad[0][1] 30.9375 → 53.701171875; `graphics.alignTextCenter` layers[0].localBounds[0] 0.0 → -22.32421875; layers[0].localBounds[2] 44.6484375 → 22.32421875; `graphics.alignTextRight` layers[0].localBounds[0] 0.0 → -44.6484375; layers[0].localBounds[2] 44.6484375 → 0.0; `graphics.fontSizeDown` layers[0].localBounds[1] -29.0625 → -28.09375; layers[0].localBounds[2] 44.6484375 → 43.16015625; `graphics.fontSizeDown5` layers[0].localBounds[1] -29.0625 → -24.21875; layers[0].localBounds[2] 44.6484375 → 37.20703125; `graphics.fontSizeUp` layers[0].localBounds[1] -29.0625 → -30.03125; layers[0].localBounds[2] 44.6484375 → 46.13671875; `graphics.fontSizeUp5` layers[0].localBounds[1] -29.0625 → -33.90625; layers[0].localBounds[2] 44.6484375 → 52.08984375; `graphics.leadingDown` layers[0].localBounds[3] 43.53515625 → 42.53515625; layers[0].quad[2][1] 103.53515625 → 102.53515625; `graphics.leadingDown5` layers[0].localBounds[3] 43.53515625 → 38.53515625; layers[0].quad[2][1] 103.53515625 → 98.53515625; `graphics.leadingUp` layers[0].localBounds[3] 43.53515625 → 44.53515625; layers[0].quad[2][1] 103.53515625 → 104.53515625; `graphics.leadingUp5` layers[0].localBounds[3] 43.53515625 → 48.53515625; layers[0].quad[2][1] 103.53515625 → 108.53515625; `graphics.nudgeDown` layers[0].position[1] 60.0 → 61.0; layers[0].quad[0][1] 30.9375 → 31.9375; `graphics.nudgeDown5` layers[0].position[1] 60.0 → 65.0; layers[0].quad[0][1] 30.9375 → 35.9375; `graphics.nudgeLeft` layers[0].position[0] 20.0 → 19.0; layers[0].quad[0][0] 20.0 → 19.0; `graphics.nudgeLeft5` layers[0].position[0] 20.0 → 15.0; layers[0].quad[0][0] 20.0 → 15.0; `graphics.nudgeRight` layers[0].position[0] 20.0 → 21.0; layers[0].quad[0][0] 20.0 → 21.0; `graphics.nudgeRight5` layers[0].position[0] 20.0 → 25.0; layers[0].quad[0][0] 20.0 → 25.0; `graphics.nudgeUp` layers[0].position[1] 60.0 → 59.0; layers[0].quad[0][1] 30.9375 → 29.9375; `graphics.nudgeUp5` layers[0].position[1] 60.0 → 55.0; layers[0].quad[0][1] 30.9375 → 25.9375; `graphics.resetAllParameters` layers[0].position[0] 20.0 → 160.0; layers[0].position[1] 60.0 → 90.0; `graphics.resetDuration` project.root.children[4].duration 1016064000000 → 1524096000000; sequence.duration 1016064000000 → 1524096000000; `graphics.upgradeToSourceGraphic` new bin item (root.children[6], duration 914457600000000 ticks)

Returned a result (read tools, or actions whose result was not compared before/after): `graphics.alignTextLeft`, `graphics.bringForward`, `graphics.bringToFront`, `graphics.fonts.used`, `graphics.pin`, `graphics.selectNextGraphic`, `graphics.selectNextLayer`, `graphics.selectPreviousGraphic`, `graphics.selectPreviousLayer`, `graphics.sendBackward`, `graphics.sendToBack`, `graphics.setRoll`, `graphics.template.controls`, `graphics.template.list`

Refused or blocked in the test project: `graphics.alignGroup.bottom` (not available right now: select two or more graphic layers command `graphics.alignGroup.bo); `graphics.alignGroup.hcenter` (not available right now: select two or more graphic layers command `graphics.alignGroup.hc); `graphics.alignGroup.left` (not available right now: select two or more graphic layers command `graphics.alignGroup.le); `graphics.alignGroup.right` (not available right now: select two or more graphic layers command `graphics.alignGroup.ri); `graphics.alignGroup.top` (not available right now: select two or more graphic layers command `graphics.alignGroup.to); `graphics.alignGroup.vcenter` (not available right now: select two or more graphic layers command `graphics.alignGroup.vc); `graphics.alignSelection.bottom` (not available right now: select two or more graphic layers command `graphics.alignSelectio); `graphics.alignSelection.hcenter` (not available right now: select two or more graphic layers command `graphics.alignSelectio); `graphics.alignSelection.left` (not available right now: select two or more graphic layers command `graphics.alignSelectio); `graphics.alignSelection.right` (not available right now: select two or more graphic layers command `graphics.alignSelectio); `graphics.alignSelection.top` (not available right now: select two or more graphic layers command `graphics.alignSelectio); `graphics.alignSelection.vcenter` (not available right now: select two or more graphic layers command `graphics.alignSelectio); `graphics.distribute` (invalid parameters for `graphics.distribute`: select three or more layers invalid paramete); `graphics.distributeHorizontally` (not available right now: select three or more graphic layers command `graphics.distributeH); `graphics.distributeSpaceHorizontally` (not available right now: select three or more graphic layers command `graphics.distributeS); `graphics.distributeSpaceVertically` (not available right now: select three or more graphic layers command `graphics.distributeS); `graphics.distributeVertically` (not available right now: select three or more graphic layers command `graphics.distributeV); `graphics.setCharStyle` (invalid parameters for `graphics.setCharStyle`: need `style` (or `clear`) invalid paramete); `graphics.setResponsiveTime` (invalid parameters for `graphics.setResponsiveTime`: need `introFrames` / `outroFrames` (o); `graphics.template.apply` (invalid parameters for `graphics.template.apply`: need `template` invalid parameters for `); `graphics.template.export` (invalid parameters for `graphics.template.export`: need `path` (no data directory for temp); `graphics.template.install` (invalid parameters for `graphics.template.install`: need `path` invalid parameters for `gr); `graphics.template.remove` (invalid parameters for `graphics.template.remove`: need `template` invalid parameters for ); `graphics.template.set` (invalid parameters for `graphics.template.set`: need `control` and `value`, or `values` in); `graphics.template.thumbnail` (invalid parameters for `graphics.template.thumbnail`: need `template` invalid parameters f); `graphics.upgradeCaption` (not available right now: there are no captions command `graphics.upgradeCaption` is not av)

## help

Returned a result (read tools, or actions whose result was not compared before/after): `help.systemReport`

## history

Returned a result (read tools, or actions whose result was not compared before/after): `history.clear`, `history.list`

Refused or blocked in the test project: `history.deleteRedoable` (not available right now: nothing to redo command `history.deleteRedoable` is not available)

## jobs

Returned a result (read tools, or actions whose result was not compared before/after): `jobs.list`

Refused or blocked in the test project: `jobs.cancel` ("no such job" without a queued export ({job}))

## labels

Returned a result (read tools, or actions whose result was not compared before/after): `labels.presets`

Refused or blocked in the test project: `labels.deletePreset` (invalid parameters for `labels.deletePreset`: need `name` invalid parameters for `labels.d); `labels.exportPreset` (invalid parameters for `labels.exportPreset`: need `path` invalid parameters for `labels.e); `labels.importPreset` (invalid parameters for `labels.importPreset`: need `path` invalid parameters for `labels.i)

## lumetri

Returned a result (read tools, or actions whose result was not compared before/after): `lumetri.presetThumbnails`, `lumetri.presets`

Ran, no change read back: `lumetri.setInputLut`, `lumetri.setLook`

Refused or blocked in the test project: `lumetri.applyMatch` (invalid parameters for `lumetri.applyMatch`: select a video clip invalid parameters for `l); `lumetri.applyPreset` (invalid parameters for `lumetri.applyPreset`: need `name` invalid parameters for `lumetri.); `lumetri.setSection` (invalid parameters for `lumetri.setSection`: need `section` invalid parameters for `lumetr)

## lut

Returned a result (read tools, or actions whose result was not compared before/after): `lut.list`

Refused or blocked in the test project: `lut.export` (invalid parameters for `lut.export`: need `lut` invalid parameters for `lut.export`: need ); `lut.import` (invalid parameters for `lut.import`: look.cube: No such file or directory (os error 2) inv); `lut.remove` (invalid parameters for `lut.remove`: need `id` invalid parameters for `lut.remove`: need `)

## markers

Verified: `markers.addFlashCue` sequence.markers[0].author "<absent>" → ""; sequence.markers[0].color "<absent>" → "Green"; `markers.goToOut` sequence.playhead 254016000000 → 1016064000000; `markers.markSelection` sequence.in null → 0; sequence.out null → 1005903360000

Returned a result (read tools, or actions whose result was not compared before/after): `markers.copyPasteIncludesSequenceMarkers`, `markers.exportCsv`, `markers.filterColors`, `markers.markSplitAudioIn`, `markers.markSplitAudioOut`, `markers.markSplitVideoIn`, `markers.markSplitVideoOut`, `markers.rippleSequenceMarkers`

Ran, no change read back: `markers.addRangeInOut`, `markers.clearAll`, `markers.clearCurrent`, `markers.clearIn`, `markers.clearOut`, `markers.goNext`, `markers.goPrev`

Refused or blocked in the test project: `markers.delete` (invalid parameters for `markers.delete`: no such marker in this owner invalid parameters f); `markers.goToSplitAudioIn` (not available right now: there are no split points command `markers.goToSplitAudioIn` is n); `markers.goToSplitAudioOut` (not available right now: there are no split points command `markers.goToSplitAudioOut` is ); `markers.goToSplitVideoIn` (not available right now: there are no split points command `markers.goToSplitVideoIn` is n); `markers.goToSplitVideoOut` (not available right now: there are no split points command `markers.goToSplitVideoOut` is ); `markers.showAllMarkerColors` (not available right now: all marker colours are shown command `markers.showAllMarkerColors)

## masks

Returned a result (read tools, or actions whose result was not compared before/after): `masks.list`

Ran, no change read back: `masks.add`, `masks.select`

Refused or blocked in the test project: `masks.addVertex` (invalid parameters for `masks.addVertex`: need `after` invalid parameters for `masks.addVe); `masks.moveVertex` (invalid parameters for `masks.moveVertex`: need `vertex` invalid parameters for `masks.mov); `masks.remove` (invalid parameters for `masks`: select a video clip (or pass `clip`) invalid parameters fo); `masks.removeVertex` (invalid parameters for `masks.removeVertex`: need `vertex` invalid parameters for `masks.r); `masks.roundCorners` (invalid parameters for `masks.roundCorners`: need `radius` (pixels, > 0) invalid parameter); `masks.set` (invalid parameters for `masks`: select a video clip (or pass `clip`) invalid parameters fo); `masks.toggleVertexSmooth` (invalid parameters for `masks.toggleVertexSmooth`: need `vertex` invalid parameters for `m); `masks.track` (invalid parameters for `masks`: select a video clip (or pass `clip`) invalid parameters fo); `masks.translate` (invalid parameters for `masks.translate`: need `delta` invalid parameters for `masks.trans)

## media

Returned a result (read tools, or actions whose result was not compared before/after): `media.makeOffline`

Ran, no change read back: `media.detachProxies`, `media.findMissing`, `media.linkMedia`, `media.offlineAll`, `media.proxyPresets`, `media.refreshChanged`, `media.status`, `media.toggleProxies`

Refused or blocked in the test project: `media.attachProxies` (invalid parameters for `media.attachProxies`: need `item` invalid parameters for `media.at); `media.autoRelink` (invalid parameters for `media.autoRelink`: need `from` and `to`, or `folder` invalid param); `media.colorInfo` (invalid parameters for `media.colorInfo`: need `item` invalid parameters for `media.colorI); `media.createProxies`; `media.reconnectFullRes` (invalid parameters for `media.reconnectFullRes`: need `item` invalid parameters for `media); `media.relink` (invalid parameters for `media.relink`: need `item` invalid parameters for `media.relink`: ); `media.replaceFootage` (invalid parameters for `media.relink`: need `item` invalid parameters for `media.relink`: ); `media.search` (invalid parameters for `media.search`: need `folder` invalid parameters for `media.search`)

## mediaBrowser

Verified: `mediaBrowser.favorite` same-field before/after via mediaBrowser.list

Returned a result (read tools, or actions whose result was not compared before/after): `mediaBrowser.list`, `mediaBrowser.roots`, `mediaBrowser.settings`

Ran, no change read back: `mediaBrowser.clearRecent`, `mediaBrowser.select`

Refused or blocked in the test project: `mediaBrowser.import` (live run); `mediaBrowser.navigate` (live run); `mediaBrowser.openInSource` (live run); `mediaBrowser.probe` (live run)

## mediaCache

Returned a result (read tools, or actions whose result was not compared before/after): `mediaCache.info`

Ran, no change read back: `mediaCache.clean`

## metadata

Returned a result (read tools, or actions whose result was not compared before/after): `metadata.get`

Ran, no change read back: `metadata.set`

## mixer

Returned a result (read tools, or actions whose result was not compared before/after): `mixer.recordStart`, `mixer.recordStop`

Refused or blocked in the test project: `mixer.clearLane` (invalid parameters for `mixer.clearLane`: need `strip` (); `mixer.deleteKeyframe` (invalid parameters for `mixer.deleteKeyframe`: need `strip` (); `mixer.moveKeyframe` (invalid parameters for `mixer.moveKeyframe`: need `strip` (); `mixer.release` (invalid parameters for `mixer.release`: need `strip` (); `mixer.removeInsert` (invalid parameters for `mixer.removeInsert`: need `strip` (); `mixer.setKeyframe` (invalid parameters for `mixer.setKeyframe`: need `strip` (); `mixer.touch` (invalid parameters for `mixer.touch`: need `strip` (); `mixer.writeAutomation` (invalid parameters for `mixer.writeAutomation`: need `strip` ()

## multicam

Verified: `multicam.audioFollowsVideo` same-field before/after via multicam.inspect; `multicam.recordStart` same-field before/after via multicam.inspect; `multicam.recordStop` same-field before/after via multicam.inspect

Returned a result (read tools, or actions whose result was not compared before/after): `multicam.inspect`

Ran, no change read back: `multicam.autoAdjustQuality`, `multicam.grid`, `multicam.nextPage`, `multicam.prevPage`, `multicam.selectionTopDown`, `multicam.showPreviewMonitor`, `multicam.transmitView`

Refused or blocked in the test project: `multicam.cut` (live run); `multicam.cutToCamera` (live run); `multicam.cutToCamera1` (live run); `multicam.cutToCamera2` (live run); `multicam.cutToCamera3` (live run); `multicam.cutToCamera4` (live run); `multicam.cutToCamera5` (live run); `multicam.cutToCamera6` (live run); `multicam.cutToCamera7` (live run); `multicam.cutToCamera8` (live run); `multicam.cutToCamera9` (live run); `multicam.editCameras` (live run); `multicam.gridLayout` (live run); `multicam.page` (live run); `multicam.selectCamera1` (live run); `multicam.selectCamera2` (live run); `multicam.selectCamera3` (live run); `multicam.selectCamera4` (live run); `multicam.selectCamera5` (live run); `multicam.selectCamera6` (live run); `multicam.selectCamera7` (live run); `multicam.selectCamera8` (live run); `multicam.selectCamera9` (live run); `multicam.switchAngle` (live run)

## perf

Returned a result (read tools, or actions whose result was not compared before/after): `perf.stats`

## playhead

Verified: `playhead.nextEdit` sequence.playhead 254016000000 → 1016064000000; `playhead.nextEditAnyTrack` sequence.playhead 254016000000 → 1016064000000; `playhead.prevEdit` sequence.playhead 254016000000 → 0; `playhead.prevEditAnyTrack` sequence.playhead 254016000000 → 0; `playhead.selectedClipEnd` sequence.playhead null → 1005903360000; `playhead.selectedClipStart` sequence.playhead null → 0; `playhead.stepBack` sequence.playhead 254016000000 → 243855360000; `playhead.stepBack5` sequence.playhead 254016000000 → 203212800000; `playhead.stepForward` sequence.playhead 254016000000 → 264176640000; `playhead.stepForward5` sequence.playhead 254016000000 → 304819200000

## prefs

Verified: `prefs.reset` same-field before/after via prefs.get

Returned a result (read tools, or actions whose result was not compared before/after): `prefs.get`, `prefs.schema`

Ran, no change read back: `prefs.set`

## presets

Ran, no change read back: `presets.list`

Refused or blocked in the test project: `presets.apply` (invalid parameters for `presets.apply`: need `preset` invalid parameters for `presets.appl); `presets.delete` (invalid parameters for `presets.delete`: need `name` invalid parameters for `presets.delet); `presets.export` (invalid parameters for `presets.export`: need `path` invalid parameters for `presets.expor); `presets.import` (invalid parameters for `presets.import`: need `path` invalid parameters for `presets.impor); `presets.rename` (invalid parameters for `presets.rename`: need `name` invalid parameters for `presets.renam); `presets.save` (invalid parameters for `presets.save`: need a `name` invalid parameters for `presets.save`)

## project

Returned a result (read tools, or actions whose result was not compared before/after): `project.delete`

Ran, no change read back: `project.columns.list`, `project.deselectAll`, `project.freeform.alignToGrid`, `project.freeform.arrangements`, `project.freeform.layout`, `project.freeform.options`, `project.freeform.reset`, `project.ingestSettings`, `project.items`, `project.select`, `project.selectAll`, `project.view.set`, `project.viewPreset.list`, `project.viewPreset.saveAs`

Refused or blocked in the test project: `project.columns.resize` (invalid parameters for `project.columns.resize`: need `column` invalid parameters for `pro); `project.columns.set` (invalid parameters for `project.columns.set`: need `columns`: [name / {name, width}); `project.deleteSearchBin` (invalid parameters for `project.deleteSearchBin`: need `bin`); `project.editSearchBin` (invalid parameters for `project.editSearchBin`: need `bin`); `project.freeform.deleteArrangement` (invalid parameters for `project.freeform.deleteArrangement`: need `name`); `project.freeform.move` (invalid parameters for `project.freeform.move`: need `items` (or a Project panel selection); `project.freeform.resize` (invalid parameters for `project.freeform.resize`: need `items` (or a Project panel selecti); `project.freeform.restoreArrangement` (invalid parameters for `project.freeform.restoreArrangement`: need `name`); `project.freeform.saveArrangement` (invalid parameters for `project.freeform.saveArrangement`: need `name`); `project.freeform.stack` (invalid parameters for `project.freeform.stack`: select two or more items to stack); `project.freeform.unstack` (invalid parameters for `project.freeform.unstack`: need `items` (or a Project panel select); `project.matteColor` (invalid parameters for `project.matteColor`: `color` must be #rrggbb); `project.moveToBin` (invalid parameters for `project.moveToBin`: need `items` (or a Project panel selection)); `project.renameBin` (invalid parameters for `project.renameBin`: need `bin`); `project.searchBinItems` (invalid parameters for `project.searchBinItems`: need `bin`); `project.setMarks` (invalid parameters for `project.setMarks`: need `item`); `project.sort` (invalid parameters for `project.sort`: need `column`); `project.viewPreset.delete` (command `project.viewPreset.delete` is not available right now: no view presets are saved); `project.viewPreset.rename` (command `project.viewPreset.rename` is not available right now: no view presets are saved); `project.viewPreset.restore` (command `project.viewPreset.restore` is not available right now: no view presets are saved); `project.viewPreset.save` (command `project.viewPreset.save` is not available right now: no view preset is current)

## scopes

Returned a result (read tools, or actions whose result was not compared before/after): `scopes.read`

## sequence

Verified: `sequence.addTracks` tracks (video,audio) (1, 1) → (2, 1); `sequence.simplify` project.activeSequence 7 → 11; project.root.children[5].customLabelColor "<absent>" → null

Returned a result (read tools, or actions whose result was not compared before/after): `sequence.closeOthers`, `sequence.colorSettings`, `sequence.goToNextGap`, `sequence.goToNextGapInTrack`, `sequence.goToPrevGap`, `sequence.goToPrevGapInTrack`, `sequence.linkedSelection`, `sequence.matchFrame`, `sequence.nestSequences`, `sequence.normalizeMixTrack`, `sequence.renderAudio`, `sequence.renderBar`, `sequence.renderEffectsInToOut`, `sequence.renderInToOut`, `sequence.revealInProject`, `sequence.selectionFollowsPlayhead`, `sequence.setWorkAreaIn`, `sequence.setWorkAreaOut`, `sequence.showDuplicateFrameMarkers`, `sequence.showThroughEdits`, `sequence.snap`, `sequence.workAreaBar`

Ran, no change read back: `sequence.addEdit`, `sequence.addEditAllTracks`, `sequence.duplicateFrames`, `sequence.throughEdits`

Refused or blocked in the test project: `sequence.closeGap` (invalid parameters for `sequence.closeGap`: no gaps to close); `sequence.deleteRenderFiles` (command `sequence.deleteRenderFiles` is not available right now: there are no render files); `sequence.deleteRenderFilesInToOut` (command `sequence.deleteRenderFilesInToOut` is not available right now: mark an In or Out ); `sequence.deleteTrack` (invalid parameters for `sequence.deleteTrack`: need `track`); `sequence.deleteTracks` (no tracks to delete); `sequence.extract` (command `sequence.extract` is not available right now: mark an In or Out point first); `sequence.joinThroughEdits` (command `sequence.joinThroughEdits` is not available right now: there are no through edits); `sequence.lift` (command `sequence.lift` is not available right now: mark an In or Out point first); `sequence.makeSubsequence` (select clips or mark In and Out first); `sequence.moveTab` (invalid parameters for `sequence.moveTab`: need `index`); `sequence.removeTransition` (invalid parameters for `sequence.removeTransition`: no transition given or selected); `sequence.renderSelection` (command `sequence.renderSelection` is not available right now: no clips selected); `sequence.revealNested` (command `sequence.revealNested` is not available right now: select a nested sequence clip); `sequence.reverseMatchFrame` (command `sequence.reverseMatchFrame` is not available right now: no clip in the Source mon); `sequence.setTransition` (invalid parameters for `sequence.setTransition`: need `transition`); `sequence.setWorkArea` (invalid parameters for `sequence.setWorkArea`: need `start` (ticks)); `sequence.transcribe` (command `sequence.transcribe` is not available right now: speech-to-text is not available )

## shortcuts

Returned a result (read tools, or actions whose result was not compared before/after): `shortcuts.audit`, `shortcuts.conflicts`, `shortcuts.list`, `shortcuts.presets`

Ran, no change read back: `shortcuts.redo`, `shortcuts.undo`

Refused or blocked in the test project: `shortcuts.clear` (live run); `shortcuts.deletePreset` (live run); `shortcuts.export` (live run); `shortcuts.forKey` (live run); `shortcuts.get` (live run); `shortcuts.import` (live run); `shortcuts.loadPreset` (live run); `shortcuts.resolve` (live run); `shortcuts.savePreset` (live run); `shortcuts.set` (live run)

## source

Verified: `source.overwrite` {seconds:1} → clips [12,13] on the timeline

Returned a result (read tools, or actions whose result was not compared before/after): `source.close`, `source.closeAll`, `source.inspect`

Ran, no change read back: `source.setPlayhead`

## state

Returned a result (read tools, or actions whose result was not compared before/after): `state.inspect`

## timeline

Returned a result (read tools, or actions whose result was not compared before/after): `timeline.selectClipAtPlayhead`, `timeline.selectNextClip`, `timeline.selectPrevClip`, `timeline.toggleAllAudioTargets`, `timeline.toggleAllSourceAudio`, `timeline.toggleAllSourceVideo`, `timeline.toggleAllVideoTargets`, `timeline.toggleTargetA1`, `timeline.toggleTargetV1`

Ran, no change read back: `timeline.setTargeting`, `timeline.setTrack`, `timeline.toggleMuteTargetedAudio`, `timeline.toggleOutputTargetedVideo`, `timeline.toggleSoloTargetedAudio`

Refused or blocked in the test project: `timeline.moveAudioTargetsDown` (the targets are already at the edge); `timeline.moveAudioTargetsUp` (the targets are already at the edge); `timeline.moveVideoTargetsDown` (the targets are already at the edge); `timeline.moveVideoTargetsUp` (the targets are already at the edge); `timeline.nudgeDown` (command `timeline.nudgeDown` is not available right now: no clips selected); `timeline.nudgeLeft` (command `timeline.nudgeLeft` is not available right now: no clips selected); `timeline.nudgeLeft5` (command `timeline.nudgeLeft5` is not available right now: no clips selected); `timeline.nudgeRight` (command `timeline.nudgeRight` is not available right now: no clips selected); `timeline.nudgeRight5` (command `timeline.nudgeRight5` is not available right now: no clips selected); `timeline.nudgeUp` (command `timeline.nudgeUp` is not available right now: no clips selected); `timeline.selectGap` (invalid parameters for `timeline.selectGap`: there is no gap there); `timeline.slideLeft` (command `timeline.slideLeft` is not available right now: no clips selected); `timeline.slideLeft5` (command `timeline.slideLeft5` is not available right now: no clips selected); `timeline.slideRight` (command `timeline.slideRight` is not available right now: no clips selected); `timeline.slideRight5` (command `timeline.slideRight5` is not available right now: no clips selected); `timeline.slipLeft` (command `timeline.slipLeft` is not available right now: no clips selected); `timeline.slipLeft5` (command `timeline.slipLeft5` is not available right now: no clips selected); `timeline.slipRight` (command `timeline.slipRight` is not available right now: no clips selected); `timeline.slipRight5` (command `timeline.slipRight5` is not available right now: no clips selected); `timeline.toggleTargetA2` (there is no track A2); `timeline.toggleTargetA3` (there is no track A3); `timeline.toggleTargetA4` (there is no track A4); `timeline.toggleTargetA5` (there is no track A5); `timeline.toggleTargetA6` (there is no track A6); `timeline.toggleTargetA7` (there is no track A7); `timeline.toggleTargetA8` (there is no track A8); `timeline.toggleTargetV2` (there is no track V2); `timeline.toggleTargetV3` (there is no track V3); `timeline.toggleTargetV4` (there is no track V4); `timeline.toggleTargetV5` (there is no track V5); `timeline.toggleTargetV6` (there is no track V6); `timeline.toggleTargetV7` (there is no track V7); `timeline.toggleTargetV8` (there is no track V8)

## transcript

Returned a result (read tools, or actions whose result was not compared before/after): `transcript.inspect`, `transcript.models`

Refused or blocked in the test project: `transcript.createCaptions` (live run); `transcript.delete` (live run); `transcript.downloadModel` (live run); `transcript.extract` (live run); `transcript.generate` (live run); `transcript.lift` (live run); `transcript.removeFillers` (live run); `transcript.removePauses` (live run); `transcript.renameSpeaker` (live run); `transcript.search` (live run); `transcript.select` (live run); `transcript.set` (live run)

## trim

Verified: `trim.extendNextEdit` project.root.children[4].duration 1016064000000 → 254016000000; sequence.duration 1016064000000 → 254016000000; `trim.next` project.root.children[4].duration 1016064000000 → 254016000000; sequence.duration 1016064000000 → 254016000000; `trim.playAround` sequence.playhead 254016000000 → 0; `trim.rippleNext` project.root.children[4].duration 1016064000000 → 254016000000; sequence.duration 1016064000000 → 254016000000; `trim.ripplePrevious` project.root.children[4].duration 1016064000000 → 762048000000; sequence.duration 1016064000000 → 762048000000

Returned a result (read tools, or actions whose result was not compared before/after): `trim.edit`, `trim.monitor`, `trim.selectNearest`, `trim.shuttleStop`, `trim.tick`

Ran, no change read back: `trim.cancelDynamic`, `trim.extendPreviousEdit`, `trim.previous`

Refused or blocked in the test project: `trim.backwardMany` (command `trim.backwardMany` is not available right now: no edit points selected); `trim.clear` (command `trim.clear` is not available right now: no edit points selected); `trim.extendToPlayhead` (command `trim.extendToPlayhead` is not available right now: no edit points selected); `trim.forwardMany` (command `trim.forwardMany` is not available right now: no edit points selected); `trim.nudge` (command `trim.nudge` is not available right now: no edit points selected); `trim.shuttle` (command `trim.shuttle` is not available right now: no edit points selected); `trim.toggleType` (command `trim.toggleType` is not available right now: no edit points selected)

## tts

Returned a result (read tools, or actions whose result was not compared before/after): `tts.voices`

Refused or blocked in the test project: `tts.create` (live run); `tts.downloadVoices` (live run); `tts.edit` (live run); `tts.inspect` (live run); `tts.preview` (live run); `tts.render` (live run)
