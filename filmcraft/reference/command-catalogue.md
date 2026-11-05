# FilmCraft reference: command catalogue (third round)

Part of the filmcraft skill. The short front page is `../SKILL.md`. **filmcraft-cli 0.17.1**, 2026-11-04: the 589
command ids not covered by the earlier reference files, run headless on a test project (two 4 s clips with tone, a
still, a WAV) and, where a panel was needed, in the live app over `--bridge`. Levels:
**verified** = the same field read before and after (JSON path, old → new); **returned a result** = a read/list command returned real data, or an action answered without a before/after comparison; **ran** = accepted but no change could be read back (often nothing to act on in the test project);
**refused** = the command's own last message after up to six tries (it names the state or parameter still missing), tagged *needs a live panel*, *not in this build* (speech-to-text), *needs a microphone* or *file chooser* (skipped: without a path it opens the desktop's file dialog).

Setup that unlocked most commands (same script, because selection does not survive a save/reopen):
`project.select {items:[<bin item id>]}` for "select an item in the Project panel"; `timeline.select` for "no clips
selected" (select the **audio** clip for gain/volume commands); `graphics.newText` first for every `graphics.*` command
(then `graphics.list {clip}` → `layers[0]`: `position` moves with alignFrame/nudge, `localBounds` with alignText/fontSize/
leading; leading needs a two-line title); `captions.newTrack` + `captions.add` for caption commands. `file.new*`
(colour matte, bars and tone, offline file, transparent video, counting leader, adjustment layer) add a bin item only.

## audio

Returned a result (read tools, or actions whose result was not compared before/after): `audio.toggleScrubbing`, `audio.voiceover.settings`, `audio.voiceover.start`

Refused in the test project: `audio.voiceover.stop` (*needs a microphone*: command `audio.voiceover.stop` is not available right now: no voice-over is recording); `audio.voiceover.sync` (*needs a microphone*: command `audio.voiceover.sync` is not available right now: no voice-over is recording)

## captions

Verified: `captions.goTo` sequence.playhead null → 50803200000; `captions.next` sequence.playhead null → 50803200000

Returned a result (read tools, or actions whose result was not compared before/after): `captions.list`, `captions.select`, `captions.showActiveOnly`

Ran, no change read back: `captions.deleteTrack`, `captions.hideAll`, `captions.merge`, `captions.setTrack`, `captions.showAll`, `captions.trim`

Refused in the test project: `captions.previous` (no more captions)

## clip

Verified: `clip.automateToSequence` project.root.children[4].duration 1016064000000 → 2032128000000; sequence.duration 1016064000000 → 2032128000000; `clip.breakoutToMono` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1016064000000; `clip.createMulticam` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1016064000000; `clip.extractAudio` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1016064000000; `clip.insertFrameHoldSegment` project.root.children[4].duration 1016064000000 → 1270080000000; sequence.duration 1016064000000 → 1270080000000; `clip.makeSubclip` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1016064000000; `clip.nest` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1016064000000

Returned a result (read tools, or actions whose result was not compared before/after): `clip.audioPeak`, `clip.clearPosterFrame`, `clip.fieldOptions`, `clip.fillFrame`, `clip.fitToFrame`, `clip.frameHoldOptions`, `clip.generateAudioWaveform`, `clip.link`, `clip.revealInProject`, `clip.sceneEditDetection`, `clip.setPosterFrame`, `clip.sourceSettings`, `clip.timeInterpolation.frameBlending`, `clip.timeInterpolation.frameSampling`, `clip.timeInterpolation.opticalFlow`, `clip.updateMetadata`

Ran, no change read back: `clip.editOffline`, `clip.editSubclip`, `clip.enable`, `clip.group`, `clip.interpretFootage`, `clip.mergeClips`, `clip.modifyTimecode`, `clip.nudgeVolumeDown1`, `clip.nudgeVolumeDown3`, `clip.nudgeVolumeUp1`, `clip.nudgeVolumeUp3`, `clip.remix.enable`, `clip.remix.properties`, `clip.rename`, `clip.scaleToFrameSize`, `clip.speedDuration`, `clip.synchronize`, `clip.ungroup`, `clip.volumeDown`, `clip.volumeDownMany`, `clip.volumeUp`, `clip.volumeUpMany`

Refused in the test project: `clip.multicamEnable` (command `clip.multicamEnable` is not available right now: no clips selected); `clip.multicamFlatten` (command `clip.multicamFlatten` is not available right now: no clips selected); `clip.remix` (invalid parameters for `clip.remix`: select an audio clip or pass `clip`); `clip.remix.revert` (command `clip.remix.revert` is not available right now: select an audio clip); `clip.replaceFromBin` (*file chooser*: may open a native file chooser: not run); `clip.replaceFromSource` (*file chooser*: may open a native file chooser: not run); `clip.replaceFromSourceMatchFrame` (*file chooser*: may open a native file chooser: not run); `clip.restoreCaptionsFromSource` (command `clip.restoreCaptionsFromSource` is not available right now: the clip's media has); `clip.setTimeInterpolation` (command `clip.setTimeInterpolation` is not available right now: no clips selected)

## clipMixer

Refused in the test project: `clipMixer.release` (*needs a live panel*: invalid parameters for `clipMixer.release`: no strip "Test"); `clipMixer.set` (invalid parameters for `clipMixer.set`: need `clip`); `clipMixer.setMode` (*needs a live panel*: invalid parameters for `clipMixer.setMode`: no strip "Test"); `clipMixer.touch` (*needs a live panel*: invalid parameters for `clipMixer.touch`: no strip "Test")

## color

Returned a result (read tools, or actions whose result was not compared before/after): `color.spaces`

## colors

Verified: `colors.addCustom` {name:"Round3", color:"#336699"} → colour listed; per session: add and use in the SAME script; `colors.removeCustom` {color:"#336699"} (the hex, not the name) → colour gone

Returned a result (read tools, or actions whose result was not compared before/after): `colors.updateCustom`

## command

Returned a result (read tools, or actions whose result was not compared before/after): `command.list`

## edit

Verified: `edit.clear` project.root.children[4].duration 1016064000000 → 0; sequence.duration 1016064000000 → 0; `edit.duplicate` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1016064000000; `edit.find` sequence.playhead 254016000000 → 0; `edit.removeUnused` project.root.children[1].item 2 → 7; project.root.children[1].label "Iris" → "Forest"; `edit.rippleDelete` project.root.children[4].duration 1016064000000 → 0; sequence.duration 1016064000000 → 0; `edit.rippleDeleteHead` project.root.children[4].duration 1016064000000 → 762048000000; sequence.duration 1016064000000 → 762048000000

Returned a result (read tools, or actions whose result was not compared before/after): `edit.consolidateDuplicates`, `edit.editOriginal`, `edit.label.iris`, `edit.removeAttributes`, `edit.selectAll`, `edit.selectAllMatching`, `edit.selectLabelGroup`

Ran, no change read back: `edit.deselectAll`, `edit.label`, `edit.label.blue`, `edit.label.brown`, `edit.label.caribbean`, `edit.label.cerulean`, `edit.label.forest`, `edit.label.green`, `edit.label.lavender`, `edit.label.magenta`, `edit.label.mango`, `edit.label.purple`, `edit.label.rose`, `edit.label.tan`, `edit.label.teal`, `edit.label.violet`, `edit.label.yellow`, `edit.pasteAttributes`

Refused in the test project: `edit.findNext` (command `edit.findNext` is not available right now: use Find… first); `edit.pasteInsert` (command `edit.pasteInsert` is not available right now: clipboard is empty); `edit.pasteMedia` (invalid parameters for `edit.pasteMedia`: need `paths`)

## effects

Ran, no change read back: `effects.toggleEnabled`

Refused in the test project: `effects.deleteKeyframe` (invalid parameters for `keyframe`: need `clip`); `effects.moveKeyframe` (invalid parameters for `keyframe`: need `clip`); `effects.moveKeyframes` (invalid parameters for `effects.moveKeyframes`: need keyframes); `effects.setInterpolation` (invalid parameters for `keyframe`: need `clip`); `effects.setKeyframe` (invalid parameters for `keyframe`: need `clip`)

## essentialSound

Returned a result (read tools, or actions whose result was not compared before/after): `essentialSound.clearType`

Refused in the test project: `essentialSound.applyPreset` (invalid parameters for `essentialSound.applyPreset`: need `preset`); `essentialSound.autoMatch` (invalid parameters for `essentialSound.autoMatch`: no clips with an audio type and audible); `essentialSound.deletePreset` (invalid parameters for `essentialSound.deletePreset`: need `name`); `essentialSound.generateDucking` (invalid parameters for `essentialSound.generateDucking`: select Music or Ambience clips (d); `essentialSound.savePreset` (*file chooser*: may open a native file chooser: not run)

## events

Returned a result (read tools, or actions whose result was not compared before/after): `events.clear`, `events.list`

## export

Ran, no change read back: `export.queue.clear`, `export.queue.stop`, `export.quick`

Refused in the test project: `export.presets.delete` (*file chooser*: may open a native file chooser: not run); `export.presets.export` (*file chooser*: may open a native file chooser: not run); `export.presets.import` (*file chooser*: may open a native file chooser: not run); `export.presets.save` (*file chooser*: may open a native file chooser: not run); `export.queue.move` (*file chooser*: may open a native file chooser: not run); `export.queue.remove` (*file chooser*: may open a native file chooser: not run); `export.queue.retry` (*file chooser*: may open a native file chooser: not run)

## file

Verified: `file.closeAllProjects` project.activeSequence 7 → "<absent>"; project.root.children[0].customLabelColor null → "<absent>"; `file.closeProject` project.activeSequence 7 → "<absent>"; project.root.children[0].customLabelColor null → "<absent>"; `file.importDemoFootage` project.root.children[10].customLabelColor "<absent>" → null; project.root.children[10].duration "<absent>" → 2540160000000; `file.newAdjustmentLayer` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 508032000000; `file.newBarsAndTone` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 762048000000; `file.newBin` project.root.children[5].id "<absent>" → 11; project.root.children[5].name "<absent>" → "B"; `file.newBinFromSelection` project.root.children[0].item 1 → 2; project.root.children[0].name "clip1.mp4" → "clip2.mp4"; `file.newBlackVideo` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1270080000000; `file.newColorMatte` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 508032000000; `file.newCountingLeader` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1270080000000; `file.newOfflineFile` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 2540160000000; `file.newTransparentVideo` project.root.children[5].customLabelColor "<absent>" → null; project.root.children[5].duration "<absent>" → 1270080000000

Returned a result (read tools, or actions whose result was not compared before/after): `file.mediaProperties`, `file.reveal`

Ran, no change read back: `file.autoSaveStatus`, `file.close`, `file.discardRecovery`, `file.listAutoSaves`, `file.mediaPropertiesFile`, `file.newSearchBin`, `file.projectManager`, `file.projectSettings.general`, `file.projectSettings.scratchDisks`, `file.recover`, `file.recoveryList`, `file.revert`, `file.saveAll`, `file.saveCopy`, `file.templates`

Refused in the test project: `file.autoSaveNow` (*file chooser*: may open a native file chooser: not run); `file.closeAllOtherProjects` (command `file.closeAllOtherProjects` is not available right now: only one project is open); `file.exportGraphicsTemplate` (*file chooser*: may open a native file chooser: not run); `file.exportSelectionProject` (*file chooser*: may open a native file chooser: not run); `file.importAaf` (*file chooser*: may open a native file chooser: not run); `file.importFromMediaBrowser` (*file chooser*: may open a native file chooser: not run); `file.replaceFonts` (*file chooser*: may open a native file chooser: not run); `file.saveAsTemplate` (*file chooser*: may open a native file chooser: not run)

## fonts

Returned a result (read tools, or actions whose result was not compared before/after): `fonts.list`

## graphics

Verified: `graphics.alignFrame.bottom` layers[0].position[1] 60.0 → 136.46484375; layers[0].quad[0][1] 30.9375 → 107.40234375; `graphics.alignFrame.left` layers[0].position[0] 20.0 → 0.0; layers[0].quad[0][0] 20.0 → 0.0; `graphics.alignFrame.right` layers[0].position[0] 20.0 → 275.3515625; layers[0].quad[0][0] 20.0 → 275.3515625; `graphics.alignFrame.top` layers[0].position[1] 60.0 → 29.0625; layers[0].quad[0][1] 30.9375 → 0.0; `graphics.alignFrame.vcenter` layers[0].position[1] 60.0 → 82.763671875; layers[0].quad[0][1] 30.9375 → 53.701171875; `graphics.alignTextCenter` layers[0].localBounds[0] 0.0 → -22.32421875; layers[0].localBounds[2] 44.6484375 → 22.32421875; `graphics.alignTextRight` layers[0].localBounds[0] 0.0 → -44.6484375; layers[0].localBounds[2] 44.6484375 → 0.0; `graphics.fontSizeDown` layers[0].localBounds[1] -29.0625 → -28.09375; layers[0].localBounds[2] 44.6484375 → 43.16015625; `graphics.fontSizeDown5` layers[0].localBounds[1] -29.0625 → -24.21875; layers[0].localBounds[2] 44.6484375 → 37.20703125; `graphics.fontSizeUp` layers[0].localBounds[1] -29.0625 → -30.03125; layers[0].localBounds[2] 44.6484375 → 46.13671875; `graphics.fontSizeUp5` layers[0].localBounds[1] -29.0625 → -33.90625; layers[0].localBounds[2] 44.6484375 → 52.08984375; `graphics.leadingDown` layers[0].localBounds[3] 43.53515625 → 42.53515625; layers[0].quad[2][1] 103.53515625 → 102.53515625; `graphics.leadingDown5` layers[0].localBounds[3] 43.53515625 → 38.53515625; layers[0].quad[2][1] 103.53515625 → 98.53515625; `graphics.leadingUp` layers[0].localBounds[3] 43.53515625 → 44.53515625; layers[0].quad[2][1] 103.53515625 → 104.53515625; `graphics.leadingUp5` layers[0].localBounds[3] 43.53515625 → 48.53515625; layers[0].quad[2][1] 103.53515625 → 108.53515625; `graphics.nudgeDown` layers[0].position[1] 60.0 → 61.0; layers[0].quad[0][1] 30.9375 → 31.9375; `graphics.nudgeDown5` layers[0].position[1] 60.0 → 65.0; layers[0].quad[0][1] 30.9375 → 35.9375; `graphics.nudgeLeft` layers[0].position[0] 20.0 → 19.0; layers[0].quad[0][0] 20.0 → 19.0; `graphics.nudgeLeft5` layers[0].position[0] 20.0 → 15.0; layers[0].quad[0][0] 20.0 → 15.0; `graphics.nudgeRight` layers[0].position[0] 20.0 → 21.0; layers[0].quad[0][0] 20.0 → 21.0; `graphics.nudgeRight5` layers[0].position[0] 20.0 → 25.0; layers[0].quad[0][0] 20.0 → 25.0; `graphics.nudgeUp` layers[0].position[1] 60.0 → 59.0; layers[0].quad[0][1] 30.9375 → 29.9375; `graphics.nudgeUp5` layers[0].position[1] 60.0 → 55.0; layers[0].quad[0][1] 30.9375 → 25.9375; `graphics.resetAllParameters` layers[0].position[0] 20.0 → 160.0; layers[0].position[1] 60.0 → 90.0; `graphics.resetDuration` project.root.children[4].duration 1016064000000 → 1524096000000; sequence.duration 1016064000000 → 1524096000000; `graphics.upgradeToSourceGraphic` project.root.children[6].customLabelColor "<absent>" → null; project.root.children[6].duration "<absent>" → 914457600000000

Returned a result (read tools, or actions whose result was not compared before/after): `graphics.alignTextLeft`, `graphics.bringForward`, `graphics.bringToFront`, `graphics.fonts.used`, `graphics.pin`, `graphics.selectNextGraphic`, `graphics.selectNextLayer`, `graphics.selectPreviousGraphic`, `graphics.selectPreviousLayer`, `graphics.sendBackward`, `graphics.sendToBack`, `graphics.setRoll`, `graphics.template.controls`, `graphics.template.list`

Refused in the test project: `graphics.alignGroup.bottom` (command `graphics.alignGroup.bottom` is not available right now: select two or more graphi); `graphics.alignGroup.hcenter` (command `graphics.alignGroup.hcenter` is not available right now: select two or more graph); `graphics.alignGroup.left` (command `graphics.alignGroup.left` is not available right now: select two or more graphic); `graphics.alignGroup.right` (command `graphics.alignGroup.right` is not available right now: select two or more graphic); `graphics.alignGroup.top` (command `graphics.alignGroup.top` is not available right now: select two or more graphic l); `graphics.alignGroup.vcenter` (command `graphics.alignGroup.vcenter` is not available right now: select two or more graph); `graphics.alignSelection.bottom` (command `graphics.alignSelection.bottom` is not available right now: select two or more gr); `graphics.alignSelection.hcenter` (command `graphics.alignSelection.hcenter` is not available right now: select two or more g); `graphics.alignSelection.left` (command `graphics.alignSelection.left` is not available right now: select two or more grap); `graphics.alignSelection.right` (command `graphics.alignSelection.right` is not available right now: select two or more gra); `graphics.alignSelection.top` (command `graphics.alignSelection.top` is not available right now: select two or more graph); `graphics.alignSelection.vcenter` (command `graphics.alignSelection.vcenter` is not available right now: select two or more g); `graphics.distribute` (invalid parameters for `graphics.distribute`: select three or more layers); `graphics.distributeHorizontally` (command `graphics.distributeHorizontally` is not available right now: select three or more); `graphics.distributeSpaceHorizontally` (command `graphics.distributeSpaceHorizontally` is not available right now: select three or); `graphics.distributeSpaceVertically` (command `graphics.distributeSpaceVertically` is not available right now: select three or m); `graphics.distributeVertically` (command `graphics.distributeVertically` is not available right now: select three or more g); `graphics.setCharStyle` (invalid parameters for `graphics.setCharStyle`: need `style` (or `clear`)); `graphics.setResponsiveTime` (invalid parameters for `graphics.setResponsiveTime`: need `introFrames` / `outroFrames` (o); `graphics.template.apply` (*file chooser*: may open a native file chooser: not run); `graphics.template.export` (*file chooser*: may open a native file chooser: not run); `graphics.template.install` (*file chooser*: may open a native file chooser: not run); `graphics.template.remove` (*file chooser*: may open a native file chooser: not run); `graphics.template.set` (*file chooser*: may open a native file chooser: not run); `graphics.template.thumbnail` (*file chooser*: may open a native file chooser: not run); `graphics.upgradeCaption` (invalid parameters for `graphics.upgradeCaption`: select captions to upgrade)

## help

Returned a result (read tools, or actions whose result was not compared before/after): `help.systemReport`

## history

Returned a result (read tools, or actions whose result was not compared before/after): `history.clear`, `history.list`

Ran, no change read back: `history.deleteRedoable`

## jobs

Returned a result (read tools, or actions whose result was not compared before/after): `jobs.list`

Refused in the test project: `jobs.cancel` (invalid parameters for `jobs.cancel`: need `job`)

## labels

Returned a result (read tools, or actions whose result was not compared before/after): `labels.presets`

Refused in the test project: `labels.deletePreset` (invalid parameters for `labels.deletePreset`: need `name`); `labels.exportPreset` (*file chooser*: may open a native file chooser: not run); `labels.importPreset` (*file chooser*: may open a native file chooser: not run)

## lumetri

Returned a result (read tools, or actions whose result was not compared before/after): `lumetri.presetThumbnails`, `lumetri.presets`

Ran, no change read back: `lumetri.setInputLut`, `lumetri.setLook`

Refused in the test project: `lumetri.applyMatch` (invalid parameters for `lumetri.applyMatch`: select a video clip); `lumetri.applyPreset` (invalid parameters for `lumetri.applyPreset`: need `name`); `lumetri.setSection` (invalid parameters for `lumetri.setSection`: need `section`)

## lut

Returned a result (read tools, or actions whose result was not compared before/after): `lut.list`

Refused in the test project: `lut.export` (*file chooser*: may open a native file chooser: not run); `lut.import` (*file chooser*: may open a native file chooser: not run); `lut.remove` (invalid parameters for `lut.remove`: need `id`)

## markers

Verified: `markers.addFlashCue` sequence.markers[0].author "<absent>" → ""; sequence.markers[0].color "<absent>" → "Green"; `markers.goToOut` sequence.playhead 254016000000 → 1016064000000; `markers.goToSplitAudioIn` not available right now: there are no split points command `markers.goToSplitAudioIn` is not available right now:; `markers.markSelection` sequence.in null → 0; sequence.out null → 1005903360000

Returned a result (read tools, or actions whose result was not compared before/after): `markers.copyPasteIncludesSequenceMarkers`, `markers.exportCsv`, `markers.filterColors`, `markers.markSplitAudioIn`, `markers.markSplitAudioOut`, `markers.markSplitVideoIn`, `markers.markSplitVideoOut`, `markers.rippleSequenceMarkers`

Ran, no change read back: `markers.addRangeInOut`, `markers.clearAll`, `markers.clearCurrent`, `markers.clearIn`, `markers.clearOut`, `markers.goNext`, `markers.goPrev`

Refused in the test project: `markers.delete` (invalid parameters for `markers.delete`: need marker id); `markers.goToSplitAudioOut` (there is no Audio Out point); `markers.goToSplitVideoIn` (there is no Video In point); `markers.goToSplitVideoOut` (there is no Video Out point); `markers.showAllMarkerColors` (command `markers.showAllMarkerColors` is not available right now: all marker colours are s)

## masks

Returned a result (read tools, or actions whose result was not compared before/after): `masks.list`

Ran, no change read back: `masks.add`, `masks.select`

Refused in the test project: `masks.addVertex` (invalid parameters for `masks.addVertex`: need `after`); `masks.moveVertex` (invalid parameters for `masks.moveVertex`: need `vertex`); `masks.remove` (invalid parameters for `masks`: select a video clip (or pass `clip`)); `masks.removeVertex` (invalid parameters for `masks.removeVertex`: need `vertex`); `masks.roundCorners` (invalid parameters for `masks.roundCorners`: need `radius` (pixels, > 0)); `masks.set` (invalid parameters for `masks`: select a video clip (or pass `clip`)); `masks.toggleVertexSmooth` (invalid parameters for `masks.toggleVertexSmooth`: need `vertex`); `masks.track` (invalid parameters for `masks`: select a video clip (or pass `clip`)); `masks.translate` (invalid parameters for `masks.translate`: need `delta`)

## media

Returned a result (read tools, or actions whose result was not compared before/after): `media.makeOffline`

Ran, no change read back: `media.colorInfo`, `media.createProxies`, `media.detachProxies`, `media.findMissing`, `media.linkMedia`, `media.offlineAll`, `media.proxyPresets`, `media.reconnectFullRes`, `media.refreshChanged`, `media.search`, `media.status`, `media.toggleProxies`

Refused in the test project: `media.attachProxies` (*file chooser*: may open a native file chooser: not run); `media.autoRelink` (*file chooser*: may open a native file chooser: not run); `media.relink` (*file chooser*: may open a native file chooser: not run); `media.replaceFootage` (*file chooser*: may open a native file chooser: not run)

## mediaBrowser

Verified: `mediaBrowser.favorite` same-field before/after via mediaBrowser.list

Returned a result (read tools, or actions whose result was not compared before/after): `mediaBrowser.list`, `mediaBrowser.roots`, `mediaBrowser.settings`

Ran, no change read back: `mediaBrowser.clearRecent`, `mediaBrowser.select`

Refused in the test project: `mediaBrowser.import` (*file chooser*: may open a native file chooser: not run); `mediaBrowser.navigate` (*file chooser*: may open a native file chooser: not run); `mediaBrowser.openInSource` (*file chooser*: may open a native file chooser: not run); `mediaBrowser.probe` (*file chooser*: may open a native file chooser: not run)

## mediaCache

Returned a result (read tools, or actions whose result was not compared before/after): `mediaCache.info`

Ran, no change read back: `mediaCache.clean`

## metadata

Returned a result (read tools, or actions whose result was not compared before/after): `metadata.get`

Ran, no change read back: `metadata.set`

## mixer

Returned a result (read tools, or actions whose result was not compared before/after): `mixer.recordStart`, `mixer.recordStop`

Refused in the test project: `mixer.clearLane` (*needs a live panel*: invalid parameters for `mixer.clearLane`: no strip "Test"); `mixer.deleteKeyframe` (*needs a live panel*: invalid parameters for `mixer.deleteKeyframe`: no strip "Test"); `mixer.moveKeyframe` (*needs a live panel*: invalid parameters for `mixer.moveKeyframe`: no strip "Test"); `mixer.release` (*needs a live panel*: invalid parameters for `mixer.release`: no strip "Test"); `mixer.removeInsert` (*needs a live panel*: invalid parameters for `mixer.removeInsert`: no strip "Test"); `mixer.setKeyframe` (*needs a live panel*: invalid parameters for `mixer.setKeyframe`: no strip "Test"); `mixer.touch` (*needs a live panel*: invalid parameters for `mixer.touch`: no strip "Test"); `mixer.writeAutomation` (*needs a live panel*: invalid parameters for `mixer.writeAutomation`: no strip "Test")

## multicam

Verified: `multicam.audioFollowsVideo` same-field before/after via multicam.inspect; `multicam.recordStart` same-field before/after via multicam.inspect; `multicam.recordStop` same-field before/after via multicam.inspect

Returned a result (read tools, or actions whose result was not compared before/after): `multicam.inspect`

Ran, no change read back: `multicam.autoAdjustQuality`, `multicam.cut`, `multicam.cutToCamera`, `multicam.cutToCamera1`, `multicam.cutToCamera2`, `multicam.cutToCamera3`, `multicam.cutToCamera4`, `multicam.cutToCamera5`, `multicam.cutToCamera6`, `multicam.cutToCamera7`, `multicam.cutToCamera8`, `multicam.cutToCamera9`, `multicam.editCameras`, `multicam.grid`, `multicam.gridLayout`, `multicam.nextPage`, `multicam.page`, `multicam.prevPage`, `multicam.selectCamera1`, `multicam.selectCamera2`, `multicam.selectCamera3`, `multicam.selectCamera4`, `multicam.selectCamera5`, `multicam.selectCamera6`, `multicam.selectCamera7`, `multicam.selectCamera8`, `multicam.selectCamera9`, `multicam.selectionTopDown`, `multicam.showPreviewMonitor`, `multicam.switchAngle`, `multicam.transmitView`

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

Refused in the test project: `presets.apply` (invalid parameters for `presets.apply`: need `preset`); `presets.delete` (invalid parameters for `presets.delete`: need `name`); `presets.export` (*file chooser*: may open a native file chooser: not run); `presets.import` (*file chooser*: may open a native file chooser: not run); `presets.rename` (invalid parameters for `presets.rename`: need `name`); `presets.save` (*file chooser*: may open a native file chooser: not run)

## project

Verified: `project.moveToBin` invalid parameters for `project.moveToBin`: need `items` (or a Project panel selection)

Returned a result (read tools, or actions whose result was not compared before/after): `project.delete`, `project.freeform.unstack`

Ran, no change read back: `project.columns.list`, `project.deselectAll`, `project.freeform.alignToGrid`, `project.freeform.arrangements`, `project.freeform.deleteArrangement`, `project.freeform.layout`, `project.freeform.options`, `project.freeform.reset`, `project.ingestSettings`, `project.items`, `project.matteColor`, `project.select`, `project.selectAll`, `project.setMarks`, `project.view.set`, `project.viewPreset.list`, `project.viewPreset.saveAs`

Refused in the test project: `project.columns.resize` (invalid parameters for `project.columns.resize`: need `column`); `project.columns.set` (invalid parameters for `project.columns.set`: need `columns`: [name / {name, width}]); `project.deleteSearchBin` (invalid parameters for `project.deleteSearchBin`: need `bin`); `project.editSearchBin` (invalid parameters for `project.editSearchBin`: need `bin`); `project.freeform.move` (*needs a live panel*: invalid parameters for `project.freeform.move`: need `items` (or a Project panel selection); `project.freeform.resize` (*needs a live panel*: invalid parameters for `project.freeform.resize`: need `items` (or a Project panel selecti); `project.freeform.restoreArrangement` (invalid parameters for `project.freeform.restoreArrangement`: need `name`); `project.freeform.saveArrangement` (*file chooser*: may open a native file chooser: not run); `project.freeform.stack` (invalid parameters for `project.freeform.stack`: select two or more items to stack); `project.renameBin` (invalid parameters for `project.renameBin`: need `bin`); `project.searchBinItems` (invalid parameters for `project.searchBinItems`: need `bin`); `project.sort` (invalid parameters for `project.sort`: need `column`); `project.viewPreset.delete` (None); `project.viewPreset.rename` (None); `project.viewPreset.restore` (None); `project.viewPreset.save` (*file chooser*: may open a native file chooser: not run)

## scopes

Returned a result (read tools, or actions whose result was not compared before/after): `scopes.read`

## sequence

Verified: `sequence.addTracks` tracks (video,audio) (1, 1) → (2, 1); `sequence.deleteTrack` invalid parameters for `sequence.deleteTrack`: need `track`; `sequence.extract` command `sequence.extract` is not available right now: mark an In or Out point first; `sequence.revealNested` command `sequence.revealNested` is not available right now: select a nested sequence clip; `sequence.simplify` project.activeSequence 7 → 11; project.root.children[5].customLabelColor "<absent>" → null

Returned a result (read tools, or actions whose result was not compared before/after): `sequence.closeOthers`, `sequence.colorSettings`, `sequence.deleteRenderFilesInToOut`, `sequence.goToNextGap`, `sequence.goToNextGapInTrack`, `sequence.goToPrevGap`, `sequence.goToPrevGapInTrack`, `sequence.lift`, `sequence.linkedSelection`, `sequence.matchFrame`, `sequence.nestSequences`, `sequence.normalizeMixTrack`, `sequence.renderAudio`, `sequence.renderBar`, `sequence.renderEffectsInToOut`, `sequence.renderInToOut`, `sequence.revealInProject`, `sequence.selectionFollowsPlayhead`, `sequence.setWorkAreaIn`, `sequence.setWorkAreaOut`, `sequence.showDuplicateFrameMarkers`, `sequence.showThroughEdits`, `sequence.snap`, `sequence.workAreaBar`

Ran, no change read back: `sequence.addEdit`, `sequence.addEditAllTracks`, `sequence.deleteTracks`, `sequence.duplicateFrames`, `sequence.makeSubsequence`, `sequence.moveTab`, `sequence.renderSelection`, `sequence.reverseMatchFrame`, `sequence.throughEdits`

Refused in the test project: `sequence.closeGap` (invalid parameters for `sequence.closeGap`: no gaps to close); `sequence.deleteRenderFiles` (command `sequence.deleteRenderFiles` is not available right now: there are no render files); `sequence.joinThroughEdits` (command `sequence.joinThroughEdits` is not available right now: there are no through edits); `sequence.removeTransition` (invalid parameters for `sequence.removeTransition`: no transition given or selected); `sequence.setTransition` (invalid parameters for `sequence.setTransition`: need `transition`); `sequence.setWorkArea` (invalid parameters for `sequence.setWorkArea`: need `start` (ticks)); `sequence.transcribe` (command `sequence.transcribe` is not available right now: speech-to-text is not available)

## shortcuts

Returned a result (read tools, or actions whose result was not compared before/after): `shortcuts.audit`, `shortcuts.conflicts`, `shortcuts.list`, `shortcuts.presets`

Ran, no change read back: `shortcuts.clear`, `shortcuts.forKey`, `shortcuts.redo`, `shortcuts.undo`

Refused in the test project: `shortcuts.deletePreset` (invalid parameters for `shortcuts.deletePreset`: need `name`); `shortcuts.export` (*file chooser*: may open a native file chooser: not run); `shortcuts.get` (invalid parameters for `shortcuts.get`: need `command`); `shortcuts.import` (*file chooser*: may open a native file chooser: not run); `shortcuts.loadPreset` (invalid parameters for `shortcuts.loadPreset`: need `name`); `shortcuts.resolve` (invalid parameters for `shortcuts.resolve`: need `keys`); `shortcuts.savePreset` (*file chooser*: may open a native file chooser: not run); `shortcuts.set` (invalid parameters for `shortcuts.set`: need `command`)

## source

Verified: `source.overwrite` {seconds:1} → clips [12,13] on the timeline

Returned a result (read tools, or actions whose result was not compared before/after): `source.close`, `source.closeAll`, `source.inspect`

Ran, no change read back: `source.setPlayhead`

## state

Returned a result (read tools, or actions whose result was not compared before/after): `state.inspect`

## timeline

Verified: `timeline.nudgeRight` command `timeline.nudgeRight` is not available right now: no clips selected; `timeline.nudgeRight5` command `timeline.nudgeRight5` is not available right now: no clips selected; `timeline.slideRight` command `timeline.slideRight` is not available right now: no clips selected; `timeline.slideRight5` command `timeline.slideRight5` is not available right now: no clips selected

Returned a result (read tools, or actions whose result was not compared before/after): `timeline.nudgeLeft`, `timeline.nudgeLeft5`, `timeline.selectClipAtPlayhead`, `timeline.selectNextClip`, `timeline.selectPrevClip`, `timeline.toggleAllAudioTargets`, `timeline.toggleAllSourceAudio`, `timeline.toggleAllSourceVideo`, `timeline.toggleAllVideoTargets`, `timeline.toggleTargetA1`, `timeline.toggleTargetV1`

Ran, no change read back: `timeline.moveAudioTargetsDown`, `timeline.moveAudioTargetsUp`, `timeline.moveVideoTargetsDown`, `timeline.moveVideoTargetsUp`, `timeline.nudgeDown`, `timeline.nudgeUp`, `timeline.setTargeting`, `timeline.setTrack`, `timeline.slideLeft`, `timeline.slideLeft5`, `timeline.slipLeft`, `timeline.slipLeft5`, `timeline.slipRight`, `timeline.slipRight5`, `timeline.toggleMuteTargetedAudio`, `timeline.toggleOutputTargetedVideo`, `timeline.toggleSoloTargetedAudio`, `timeline.toggleTargetA2`, `timeline.toggleTargetA3`, `timeline.toggleTargetA4`, `timeline.toggleTargetA5`, `timeline.toggleTargetA6`, `timeline.toggleTargetA7`, `timeline.toggleTargetA8`, `timeline.toggleTargetV2`, `timeline.toggleTargetV3`, `timeline.toggleTargetV4`, `timeline.toggleTargetV5`, `timeline.toggleTargetV6`, `timeline.toggleTargetV7`, `timeline.toggleTargetV8`

Refused in the test project: `timeline.selectGap` (invalid parameters for `timeline.selectGap`: need `track`)

## transcript

Returned a result (read tools, or actions whose result was not compared before/after): `transcript.inspect`, `transcript.models`

Refused in the test project: `transcript.createCaptions` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.delete` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.downloadModel` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.extract` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.generate` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.lift` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.removeFillers` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.removePauses` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.renameSpeaker` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.search` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.select` (*not in this build*: genuine limit: not-in-build/hardware); `transcript.set` (*not in this build*: genuine limit: not-in-build/hardware)

## trim

Verified: `trim.extendNextEdit` project.root.children[4].duration 1016064000000 → 254016000000; sequence.duration 1016064000000 → 254016000000; `trim.next` project.root.children[4].duration 1016064000000 → 254016000000; sequence.duration 1016064000000 → 254016000000; `trim.playAround` sequence.playhead 254016000000 → 0; `trim.rippleNext` project.root.children[4].duration 1016064000000 → 254016000000; sequence.duration 1016064000000 → 254016000000; `trim.ripplePrevious` project.root.children[4].duration 1016064000000 → 762048000000; sequence.duration 1016064000000 → 762048000000

Returned a result (read tools, or actions whose result was not compared before/after): `trim.backwardMany`, `trim.edit`, `trim.extendToPlayhead`, `trim.forwardMany`, `trim.monitor`, `trim.nudge`, `trim.selectNearest`, `trim.shuttle`, `trim.shuttleStop`, `trim.tick`, `trim.toggleType`

Ran, no change read back: `trim.cancelDynamic`, `trim.clear`, `trim.extendPreviousEdit`, `trim.previous`

## tts

Returned a result (read tools, or actions whose result was not compared before/after): `tts.voices`

Refused in the test project: `tts.create` (invalid parameters for `tts.create`: `text` is required); `tts.downloadVoices` (invalid parameters for `tts.downloadVoices`: natural voices are not available in this buil); `tts.edit` (command `tts.edit` is not available right now: select a narration clip); `tts.inspect` (invalid parameters for `tts.inspect`: pass `item` or `clip`, or select a narration clip); `tts.preview` (invalid parameters for `tts.preview`: `text` is required); `tts.render` (invalid parameters for `tts.render`: `text` is required)
