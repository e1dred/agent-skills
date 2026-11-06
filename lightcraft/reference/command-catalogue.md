# LightCraft command catalogue (0.19.0)

Every id from `lightcraft-cli commands` (389 in 0.19.0; the 0.18.1 sweep covered 376 here and left out the 5 beforeAfter.* and 2 pointColor.* ids; the 6 ids new in 0.19.0 are added below with their 0.19.0 evidence). Status is the evidence in results.jsonl: **V** verified (same field read before/after), **R** read-ok, **r** ran (accepted, no read-back field), **x** refused (error in REPORT.md), **s** skipped. Parameters live in `commands` / commands.json.

## activity (2)

| id | status | note |
|---|---|---|
| `activity.cancel` | r | no change in activity.list; result={"cancelled": 0} |
| `activity.list` | r | no change in activity.list; result={"tasks": []} |

## album (15)

| id | status | note |
|---|---|---|
| `album.addPhotos` | r | no change in albums.list; result={"added": 1, "skipped": 0} |
| `album.clearQuick` | r | no change in albums.list; result=null |
| `album.create` | r | {"id": 8, "skipped": 0} |
| `album.createSmart` | V | .length 4 → 5 |
| `album.delete` | r | .length 5 → 4 |
| `album.move` | r | no change in albums.list; result=null |
| `album.removePhotos` | r | no change in albums.list; result={"album": "Test Album", "removed": 1} |
| `album.rename` | r | no change in albums.list; result=null |
| `album.reorder` | r | no change in albums.list; result={"changed": 5} |
| `album.ruleFields` | r | no change in album.ruleFields; result=[{"field": "rating", "group": null, "kind": "number" |
| `album.setCover` | r | no change in albums.list; result=null |
| `album.setRules` | r | no change in albums.list; result={"count": 18} |
| `album.setTarget` | r | no change in albums.list; result={"target": 8} |
| `album.sort` | r | no change in albums.list; result={"changed": 0} |
| `album.toggleTarget` | V | albums.length 2 → 3 |

## albums (1)

| id | status | note |
|---|---|---|
| `albums.list` | r | no change in albums.list; result=[{"children": [{"children": [], "count": 5, "cover": 1, " |

## app (4)

| id | status | note |
|---|---|---|
| `app.export` | V | file:<scratch> None → {'bytes': 71886, 'mean': [156.8, 142.6, 140.5], 'size': [800, 533]} |
| `app.gpu` | V | available True → False |
| `app.hotPixelLimit` | V | percent 0.2 (default 0.2) → 0.5, a no-param call read 0.5 back (0.19.0) |
| `app.memoryBudget` | V | budget 1610612736 → 536870912 |

## catalog (2)

| id | status | note |
|---|---|---|
| `catalog.query` | r | no change in catalog.query; result={"photos": [{"camera": "Synthetic X2", "captured": "202 |
| `catalog.stats` | r | no change in catalog.stats; result={"albums": 6, "byDate": [{"count": 24, "days": [["2026- |

## crop (7)

| id | status | note |
|---|---|---|
| `crop.aspect` | V | develop.crop.geometry.rect.x0 0.0 → 0.16666666666666666 |
| `crop.autoStraighten` | r | no change in photo.inspect; result={"changed": false, "reason": "no dominant horizontal or |
| `crop.drag` | V | develop.crop.geometry.rect.x0 0.0 → 0.19999999999999998 |
| `crop.reset` | V | develop.crop.geometry.rect.x0 0.1 → 0.0 |
| `crop.rotateAspect` | V | develop.crop.aspect[0] 300 → 200 |
| `crop.set` | V | develop.crop.geometry.rect.x0 0.0 → 0.2 |
| `crop.straighten` | V | develop.crop.geometry.angle 0.0 → 5.0 |

## curve (7)

| id | status | note |
|---|---|---|
| `curve.applyPreset` | V | develop.curve.master.length 0 → 5 |
| `curve.deletePreset` | V | curve.presets.names TestS2 present → TestS2 absent |
| `curve.exportPresets` | V | curve.presets.names ['Linear', 'Medium Contrast', 'Strong Contrast', 'TestS2'] → ['Linear', 'Medium Contrast', 'Strong Contrast'] |
| `curve.importPresets` | r | {"failed": [], "imported": ["TestS2"]} |
| `curve.presets` | r | no change in curve.presets; result={"current": "Linear", "presets": [{"blue": [], "builtin |
| `curve.reset` | V | develop.curve.master.length 3 → 0 |
| `curve.savePreset` | r | {"current": "TestS", "presets": [{"blue": [], "builtin": true, "green": [], "master": [],  |

## denoise (16)

| id | status | note |
|---|---|---|
| `denoise.cancel` | r | no change in denoise.queue; result={"cancelled": 0} |
| `denoise.clear` | r | no change in denoise.queue; result={"bytes": 0, "deleted": 0} |
| `denoise.models.download` | s | model download is forbidden by the task rules (no downloads of models or binaries) |
| `denoise.models.downloadCancel` | r | no change in denoise.models.downloads; result={"discarded": false} |
| `denoise.models.downloads` | r | no change in denoise.models.downloads; result={"downloads": [], "running": false} |
| `denoise.models.inspect` | x | invalid parameters for `denoise.models.inspect`: No denoise-model.json beside this .onnx f |
| `denoise.models.install` | x | invalid parameters for `denoise.models.install`: cannot read `<scratch> |
| `denoise.models.list` | r | no change in denoise.models.list; result={"auto": true, "cacheGb": 2, "dir": "<scratch> |
| `denoise.models.remove` | x | invalid parameters for `denoise.models.remove`: that model is not installed |
| `denoise.models.select` | r | no change in denoise.models.list; result={"model": null} |
| `denoise.models.test` | x | invalid parameters for `denoise.models.test`: that model is not installed |
| `denoise.pump` | r | no change in denoise.queue; result={"active": false, "downloading": false, "generation": 0 |
| `denoise.queue` | x | invalid parameters for `denoise.queue`: no denoise model is chosen: install one first (`de |
| `denoise.settings` | V | cacheGb 20 → 2 |
| `denoise.status` | r | no change in denoise.status; result={"auto": true, "cache": {"bytes": 0, "files": 0, "limi |
| `denoise.toggle` | x | invalid parameters for `denoise.toggle`: AI Denoise applies to raw photos developed from t |

## develop (29)

| id | status | note |
|---|---|---|
| `develop.adjust` | V | develop.light.exposure 0.0 → 0.5 |
| `develop.auto` | V | develop.color.vibrance 0.0 → 30.0 |
| `develop.autoBwMix` | V | develop.bw_mix.aqua 0.0 → -60.0 |
| `develop.autoSync` | r | no change in photo.inspect; result={"on": true} |
| `develop.beginInteraction` | r | no change in photo.inspect; result=null |
| `develop.cancelInteraction` | r | no change in photo.inspect; result=null |
| `develop.controls` | R | [{"decimals": 0, "default": 100.0, "id": "profile.amount", "label": "Amount", "max": 200.0 |
| `develop.copy` | r | no change in photo.inspect; result={"groups": ["profile", "treatment", "whiteBalance", "li |
| `develop.curve` | V | develop.curve.master.length 0 → 3 |
| `develop.endInteraction` | r | no change in photo.inspect; result=null |
| `develop.get` | r | no change in develop.get; result={"bw_mix": {"aqua": 0.0, "blue": 0.0, "green": 0.0, "mage |
| `develop.hdr` | r | edited None → 2026-11-05T04:07:58 |
| `develop.matchExposure` | r | no change in photo.inspect; result={"changed": 1, "skipped": []} |
| `develop.merge` | V | develop.light.exposure 0.0 → 0.8 |
| `develop.paste` | V | develop.light.exposure 0.0 → 1.2 |
| `develop.pastePrevious` | r | edited None → 2026-11-05T03:59:13 |
| `develop.profile` | V | develop.profile.amount 100.0 → 50.0 |
| `develop.quickAdjust` | V | develop.light.contrast 0.0 → 10.0 |
| `develop.reset` | V | develop.light.exposure 1.0 → 0.0 |
| `develop.resetControl` | V | develop.light.exposure 1.0 → 0.0 |
| `develop.resetSection` | V | develop.light.exposure 1.0 → 0.0 |
| `develop.sectionEnabled` | V | develop.disabled_sections.length 0 → 1 |
| `develop.set` | V | develop.light.contrast 0.0 → 25.0 |
| `develop.sync` | r | no change in photo.inspect; result={"changed": 1} |
| `develop.targeted` | V | develop.mixer.orange.hue 0.0 → 10.0 |
| `develop.treatment` | V | develop.treatment color → bw |
| `develop.updateProcess` | x | command `develop.updateProcess` is not available right now: already on the current process |
| `develop.wb` | V | develop.wb.mode asShot → cloudy |
| `develop.wbPick` | V | develop.wb.mode asShot → custom |

## edit (2)

| id | status | note |
|---|---|---|
| `edit.redo` | V | develop.light.exposure 0.0 → 1.0 |
| `edit.undo` | V | develop.light.exposure 1.0 → 0.0 |

## export (7)

| id | status | note |
|---|---|---|
| `export.addToPhotos` | x | command `export.addToPhotos` is not available right now: Apple Photos is only available on |
| `export.checkTarget` | r | {"path": "<scratch> |
| `export.contactSheet` | r | file None → {'error': "cannot identify image file '<scratch>"} |
| `export.deletePreset` | V | export.presets.names EP1 present → EP1 absent |
| `export.photosImports` | R | {"imports": []} |
| `export.presets` | R | [{"builtin": true, "name": "JPEG (Small)", "params": {"colorSpace": "srgb", "format": "jpe |
| `export.savePreset` | V | export.presets.length 4 → 5 |

## faces (21)

| id | status | note |
|---|---|---|
| `faces.detect` | x | invalid parameters for `faces.detect`: finding faces needs the YuNet face detector (232 KB |
| `faces.enable` | x | invalid parameters for `faces.enable`: choose a recognition model first (Settings ▸ Faces  |
| `faces.evaluate` | x | invalid parameters for `faces.evaluate`: no recognition model is chosen: add one in Settin |
| `faces.gpu` | V | cpuOnly False → True |
| `faces.index` | x | invalid parameters for `faces.index`: no recognition model is chosen: add one in Settings  |
| `faces.models.download` | s | model download is forbidden by the task rules (no downloads of models or binaries) |
| `faces.models.downloadCancel` | r | no change in faces.models.downloads; result={"discarded": false} |
| `faces.models.downloads` | r | no change in faces.models.downloads; result={"downloads": [], "running": false} |
| `faces.models.inspect` | x | invalid parameters for `faces.models.inspect`: cannot read `<scratch> |
| `faces.models.install` | x | invalid parameters for `faces.models.install`: cannot read `<scratch> |
| `faces.models.list` | r | no change in faces.models.list; result={"catalog": {"errors": [], "models": 0, "path": "/t |
| `faces.models.remove` | x | invalid parameters for `faces.models.remove`: that model is not installed |
| `faces.models.select` | r | no change in faces.models.list; result={"embedder": null} |
| `faces.models.test` | x | invalid parameters for `faces.models.test`: that model is not installed |
| `faces.nameFaces` | x | invalid parameters for `faces.nameFaces`: none of those faces exist |
| `faces.person` | r | no change in faces.person; result={"confirmed": [], "more": [], "name": "Nobody", "pending |
| `faces.pump` | r | no change in faces.unnamed; result={"active": false} |
| `faces.renamePerson` | x | invalid parameters for `faces.renamePerson`: no person named A |
| `faces.setName` | x | invalid parameters for `faces.setName`: no such region |
| `faces.suggest` | x | invalid parameters for `faces.suggest`: no recognition model is chosen: add one in Setting |
| `faces.unnamed` | r | no change in faces.unnamed; result={"faces": [], "ordered": false, "ready": false, "total" |

## filter (4)

| id | status | note |
|---|---|---|
| `filter.applyPreset` | r | no change in library.state; result={"photos": 15} |
| `filter.deletePreset` | V | .length 1 → 0 |
| `filter.presets` | r | no change in filter.presets; result=[] |
| `filter.savePreset` | V | .length 0 → 1 |

## focus (1)

| id | status | note |
|---|---|---|
| `focus.pump` | r | no change in focus.pump; result={"active": false, "last": null, "lookedAt": 0, "running":  |

## folder (6)

| id | status | note |
|---|---|---|
| `folder.create` | r | no change in library.folders; result={"path": "<scratch> |
| `folder.label` | r | no change in library.folders; result={"label": "red", "path": "<scratch> |
| `folder.move` | r | no change in library.folders; result={"path": "<scratch> |
| `folder.rename` | V | [0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].path <scratch> → <scratch> |
| `folder.scanChanges` | r | no change in photo.inspect; result={"duplicates": 0, "metadata": [], "missing": [], "moved |
| `folder.synchronize` | V | logBytes 0 → 3560 |

## geometry (2)

| id | status | note |
|---|---|---|
| `geometry.guides` | V | develop.geometry.guides.length 0 → 1 |
| `geometry.upright` | V | develop.geometry.upright off → level |

## history (5)

| id | status | note |
|---|---|---|
| `history.clear` | V | history[0] Exposure → Cleared History |
| `history.list` | r | no change in history.list; result={"cursor": null, "history": [], "versions": []} |
| `history.next` | V | develop.light.contrast 0.0 → 30.0 |
| `history.previous` | V | develop.light.contrast 30.0 → 0.0 |
| `history.restore` | V | develop.light.contrast 30.0 → 0.0 |

## journal (1)

| id | status | note |
|---|---|---|
| `journal.list` | r | no change in journal.list; result=[{"command": "library.select", "params": {"ids": [1]}}] |

## keyword (23)

| id | status | note |
|---|---|---|
| `keyword.create` | r | {"keyword": "KWTest"} |
| `keyword.delete` | V | meta.keywords.length 4 → 3 |
| `keyword.deleteSet` | V | current SetX → Recent Keywords |
| `keyword.edit` | r | no change in photo.inspect; result={"changed": 0, "listed": 1} |
| `keyword.export` | r | no change in keyword.list; result={"captureOneRefuses": [], "keywords": 25, "path": "/tmp/ |
| `keyword.import` | r | .length 25 → 27 |
| `keyword.info` | r | no change in keyword.info; result={"count": 1, "exportContaining": true, "exportSynonyms": |
| `keyword.list` | r | no change in keyword.list; result=[{"children": [], "count": 2, "name": "aurora", "path":  |
| `keyword.merge` | r | no change in photo.inspect; result={"changed": 0, "listed": 1} |
| `keyword.move` | r | no change in photo.inspect; result={"changed": 0, "listed": 0} |
| `keyword.nextSet` | r | no change in keyword.sets; result={"current": "Recent Keywords", "keywords": [], "sets": [ |
| `keyword.previousSet` | r | no change in keyword.sets; result={"current": "Recent Keywords", "keywords": [], "sets": [ |
| `keyword.purgeUnused` | r | no change in photo.inspect; result={"purged": 0} |
| `keyword.rename` | r | no change in keyword.list; result={"changed": 0, "listed": 2} |
| `keyword.saveSet` | V | current Recent Keywords → KSet |
| `keyword.setDefaultParent` | r | no change in keyword.list; result={"keyword": "KWParent"} |
| `keyword.setShortcut` | V | keywords.length 0 → 2 |
| `keyword.sets` | r | no change in keyword.sets; result={"current": "Recent Keywords", "keywords": ["KWParent"], |
| `keyword.shortcut` | r | no change in keyword.shortcut; result={"keywords": []} |
| `keyword.suggest` | r | no change in keyword.suggest; result=[] |
| `keyword.toggleFromSet` | r | no change in photo.inspect; result={"changed": 0} |
| `keyword.toggleShortcut` | V | meta.keywords.length 4 → 3 |
| `keyword.useSet` | r | no change in keyword.sets; result={"current": "Recent Keywords", "keywords": ["KWParent"], |

## label (6)

| id | status | note |
|---|---|---|
| `label.applySet` | r | no change in photo.inspect; result={"changed": 0} |
| `label.deleteSet` | V | sets.length 3 → 2 |
| `label.names` | R | [{"custom": null, "label": "red", "name": "Red"}, {"custom": null, "label": "yellow", "nam |
| `label.saveSet` | V | sets.length 2 → 3 |
| `label.setNames` | r | no change in label.names; result={"changed": 2} |
| `label.sets` | r | no change in label.sets; result={"current": "Colors", "sets": [{"builtin": true, "name": " |

## lens (2)

| id | status | note |
|---|---|---|
| `lens.databaseStatus` | r | no change in lens.databaseStatus; result={"dir": null, "download": {"state": "idle"}, "len |
| `lens.downloadDatabase` | V | dir None → <scratch> |

## library (48)

| id | status | note |
|---|---|---|
| `library.autoImport` | V | copy False → True |
| `library.autoImportScan` | r | no change in library.info; result={"folder": "<scratch> |
| `library.browse` | V | new 2 → 0 |
| `library.buildPreviews` | r |  None → <removed> |
| `library.cancelPreviews` | r | no change in library.previewProgress; result=null |
| `library.clearFilter` | V | filter.rating 3 → 0 |
| `library.clearPreviews` | V | cache.disk.bytes 36773 → 0 |
| `library.compact` | V | persistence.lastSnapshot.blockingMs 0.0 → 0.13692500000000002 |
| `library.devices` | r | no change in library.devices; result=[] |
| `library.down` | r | no change in library.state; result={"active": 1} |
| `library.emptyRecentlyDeleted` | r | no change in catalog.query; result={"deleted": 0} |
| `library.filter` | V | filter.rating 0 → 3 |
| `library.findMissing` | V | .length 4 → 0 |
| `library.findSimilar` | V | photos.length 2 → 0 |
| `library.folders` | r | no change in library.folders; result=[{"children": [{"children": [{"children": [{"children |
| `library.forgetLocal` | r | no change in library.info; result={"days": 30, "dryRun": true, "foldersStamped": 0, "forgo |
| `library.groups` | r | no change in library.state; result=[{"count": 3, "key": "2026-09", "label": "September 202 |
| `library.holdView` | r | no change in library.state; result={"hold": true} |
| `library.import` | V | logBytes 0 → 9733 |
| `library.importLightroom` | x | invalid parameters for `library.importLightroom`: missing path |
| `library.importPreview` | r | no change in library.importPreview; result={"candidates": [{"captured": "2026-11-05T03:58: |
| `library.info` | r | no change in library.info; result={"albums": 0, "cache": {"disk": {"bytes": 0, "hits": 0,  |
| `library.inspectLightroom` | x | invalid parameters for `library.inspectLightroom`: No such file or directory (os error 2) |
| `library.memory` | r | no change in library.memory; result={"budget": 1610612736, "cacheBudget": 805306368, "engi |
| `library.missing` | r | no change in library.missing; result=[{"id": 1, "path": "<scratch> |
| `library.next` | r | no change in library.state; result={"active": 1} |
| `library.preferences` | r | no change in library.state; result={"cacheMb": 2048, "forgetLocalDays": 30, "import": {"au |
| `library.previewProgress` | r | no change in library.previewProgress; result=null |
| `library.previous` | V | selection.active 1 → 8 |
| `library.recheckPreviewOnly` | r | no change in library.info; result={"checked": 0, "cleared": [], "updated": []} |
| `library.refresh` | r | no change in library.state; result=null |
| `library.refreshLensProfiles` | r | no change in photo.inspect; result={"checked": 0, "database": false, "found": []} |
| `library.removeFolder` | x | invalid parameters for `library.removeFolder`: <scratch> |
| `library.retrySidecars` | r | no change in library.info; result={"waiting": 0, "written": 0} |
| `library.select` | V | selection.active 21 → 2 |
| `library.selectAll` | V | selection.ids.length 1 → 24 |
| `library.selectBy` | V | selection.active 21 → 7 |
| `library.selectNone` | r | no change in library.state; result=null |
| `library.shuffle` | V | sort.key captureDate → random |
| `library.smartPreviews` | r | no change in library.info; result={"built": 0, "failed": [[1, "<scratch> |
| `library.smartPreviewsLocation` | r | no change in library.info; result={"available": true, "bytes": 0, "count": 0, "custom": tr |
| `library.sort` | V | sort.ascending False → True |
| `library.source` | V | selection.active 21 → 7 |
| `library.state` | r | no change in library.state; result={"activeMask": null, "activeSpot": null, "clipboard": f |
| `library.toggleAutoWriteXmp` | r | no change in library.state; result={"autoWrite": true, "naming": "stem"} |
| `library.toggleFilters` | V | filter.rating 3 → 0 |
| `library.up` | V | selection.active 1 → 8 |
| `library.xmpPreferences` | r | no change in library.state; result={"autoWrite": true, "naming": "full"} |

## mask (31)

| id | status | note |
|---|---|---|
| `mask.add` | V | develop.masks.length 0 → 1 |
| `mask.addComponent` | V | develop.masks[0].components.length 1 → 2 |
| `mask.adjust` | V | develop.masks[0].adjust.contrast 0.0 → 20.0 |
| `mask.applyEffect` | V | develop.masks[1].adjust.contrast 0.0 → 30.0 |
| `mask.brushStroke` | V | develop.masks[0].components[0].shape.strokes.length 0 → 1 |
| `mask.component` | V | develop.masks[0].components[0].invert False → True |
| `mask.delete` | V | develop.masks.length 1 → 0 |
| `mask.deleteAll` | V | develop.masks.length 2 → 0 |
| `mask.deleteEffect` | r | no change in photo.inspect; result={"current": null, "effects": [], "groups": [], "toolEff |
| `mask.duplicate` | V | develop.masks.length 1 → 2 |
| `mask.duplicateEffect` | r | no change in photo.inspect; result={"current": "E1", "effects": [{"adjust": {"amount": 100 |
| `mask.effects` | r | no change in mask.effects; result={"current": "E1", "effects": [{"adjust": {"amount": 100. |
| `mask.exportEffects` | r | no change in mask.effects; result={"count": 1, "path": "<scratch> |
| `mask.favoriteEffect` | r | no change in mask.effects; result={"current": "E1", "effects": [{"adjust": {"amount": 100. |
| `mask.importEffects` | r | no change in mask.effects; result={"dividers": [], "failed": [["<scratch> |
| `mask.invert` | V | develop.masks[0].invert False → True |
| `mask.move` | r | no change in photo.inspect; result={"activeMask": 1} |
| `mask.objectPoint` | x | invalid parameters for `mask.objectPoint`: the mask has no Object selection (add one first |
| `mask.refine` | r | history.length 1 → 2 |
| `mask.refineDetail` | x | invalid parameters for `mask.refineDetail`: the mask has no Object or Describe selection |
| `mask.rename` | V | develop.masks[0].name Mask 1 → MyMask |
| `mask.renameEffect` | r | no change in photo.inspect; result={"current": "E2", "effects": [{"adjust": {"amount": 100 |
| `mask.renameEffectGroup` | V | effects[0].group G1 → G2 |
| `mask.sampleColor` | V | develop.masks[0].components[0].shape.samples.length 0 → 1 |
| `mask.saveEffect` | r | no change in photo.inspect; result={"current": "E1", "effects": [{"adjust": {"amount": 100 |
| `mask.select` | r | no change in photo.inspect; result=null |
| `mask.setEffectGroup` | V | groups[0].name  → G1 |
| `mask.toolEffect` | r | no change in mask.effects; result={"toolEffects": {"brush": "E1"}} |
| `mask.update` | V | develop.masks[0].components[0].shape.center.x 0.5 → 0.4 |
| `mask.updateEffect` | r | no change in photo.inspect; result={"current": "E1", "effects": [{"adjust": {"amount": 100 |
| `mask.visible` | V | develop.masks[0].visible True → False |

## merge (4)

| id | status | note |
|---|---|---|
| `merge.hdr` | V | photos.length 9 → 10 |
| `merge.hdrBatch` | r | no change in catalog.query; result={"failed": [{"error": "the merged file <scratch> |
| `merge.hdrPanorama` | x | 8 photos don't form brackets of 3 for at least two positions |
| `merge.panorama` | V | photos.length 8 → 9 |

## metadata (7)

| id | status | note |
|---|---|---|
| `metadata.applyPreset` | V | meta.creator LightCraft Demo → Me |
| `metadata.deletePreset` | V | .length 1 → 0 |
| `metadata.downloadPlaceNames` | s | downloads the GeoNames place-name dataset (network); forbidden by task rules. Invoked once |
| `metadata.placeNamesStatus` | r | no change in metadata.placeNamesStatus; result={"attribution": "Place names: GeoNames (geo |
| `metadata.presets` | r | no change in metadata.presets; result=[] |
| `metadata.reverseGeocode` | x | invalid parameters for `metadata.reverseGeocode`: the place names aren't downloaded (No su |
| `metadata.savePreset` | V | .length 0 → 1 |

## photo (44)

| id | status | note |
|---|---|---|
| `photo.addToLibrary` | r | no change in catalog.query; result={"added": 0} |
| `photo.allMetadata` | R | {"exif": [], "note": "a generated demo photo has no file", "xmp": []} |
| `photo.analyze` | r | no change in photo.inspect; result={"failed": [], "groups": 0, "photos": [{"best": false,  |
| `photo.autoTagTracklog` | V | meta.gps None → <removed> |
| `photo.clearLabel` | r | no change in photo.inspect; result={"changed": 1} |
| `photo.convertToDng` | r | no change in photo.inspect; result={"converted": [], "skipped": [[1, "not a file"]]} |
| `photo.copyMetadata` | r | no change in photo.allMetadata; result={"altText": "", "caption": "", "city": "", "copyrig |
| `photo.cycleFlag` | V | flag pick → reject |
| `photo.decreaseFlag` | V | flag pick → none |
| `photo.decreaseRating` | V | rating 3 → 2 |
| `photo.delete` | V | photos.length 24 → 23 |
| `photo.deletePermanently` | V | photos.length 24 → 23 |
| `photo.duplicate` | r | no change in catalog.query; result={"ids": [9]} |
| `photo.editExternal` | r | no change in catalog.query; result={"copies": [{"id": 10, "original": 1, "path": "/tmp/cla |
| `photo.flag` | V | flag pick → reject |
| `photo.flipHorizontal` | V | develop.crop.flip_h False → True |
| `photo.flipVertical` | V | develop.crop.flip_v False → True |
| `photo.increaseFlag` | r | no change in photo.inspect; result={"changed": 0} |
| `photo.increaseRating` | V | rating 3 → 4 |
| `photo.inspect` | R | {"albums": [2, 7], "as_shot_wb": null, "captured": "2026-03-01T05:00:00", "deleted": false |
| `photo.label` | V | label None → blue |
| `photo.moveToFolder` | x | invalid parameters for `photo.moveToFolder`: <scratch> |
| `photo.pasteMetadata` | r | no change in photo.inspect; result={"changed": 1} |
| `photo.pick` | r | no change in photo.inspect; result={"changed": 1} |
| `photo.rate` | V | rating 3 → 5 |
| `photo.readFocusPoints` | R | {"queued": 0, "running": false} |
| `photo.readMetadataFromFile` | R | {"failed": [{"error": "no XMP sidecar or embedded XMP", "id": 1}], "read": []} |
| `photo.reject` | V | flag pick → reject |
| `photo.relink` | V | content_hash 7bbb39d5c822ffbccce091e916b99a96 → d0ef19c9419261d44a56e9e22cc6820e |
| `photo.reload` | r | no change in photo.inspect; result={"reloaded": []} |
| `photo.removeRegion` | x | invalid parameters for `photo.removeRegion`: no such region |
| `photo.rename` | V | file_name LC01207.JPG → Trip-001.JPG |
| `photo.renamePreview` | r | no change in photo.inspect; result=[{"from": "LC01207.JPG", "id": 1, "to": "Shot-01.JPG"}] |
| `photo.renameTokens` | R | {"dateDirectives": [{"directive": "%Y", "meaning": "year, 4 digits"}, {"directive": "%y",  |
| `photo.restore` | V | photos.length 23 → 24 |
| `photo.rotateLeft` | V | develop.orientation Normal → Rotate270 |
| `photo.rotateRight` | V | develop.orientation Normal → Rotate90 |
| `photo.saveMetadataToFile` | V | xmp.length 16 → 5 |
| `photo.setCaptureTime` | V | captured 2026-03-01T05:00:00 → 2026-09-30T14:05:00 |
| `photo.setMeta` | V | meta.caption  → A caption |
| `photo.setRegion` | x | invalid parameters for `photo.setRegion`: no such region |
| `photo.smartPreview` | r | no change in photo.inspect; result={"originalOnline": true, "smartPreview": false} |
| `photo.unflag` | V | flag pick → none |
| `photo.virtualCopy` | r | no change in photo.inspect; result={"ids": [25]} |

## preset (10)

| id | status | note |
|---|---|---|
| `preset.apply` | V | develop.color.vibrance 0.0 → 18.0 |
| `preset.create` | r | {"id": "user.41.px1793851517"} |
| `preset.delete` | r | .length 44 → 43 |
| `preset.export` | r | no change in presets.list; result={"count": 1, "path": "<scratch> |
| `preset.favorite` | r | no change in presets.list; result=null |
| `preset.import` | r | .length 43 → 44 |
| `preset.move` | x | invalid parameters for `preset.move`: unknown preset `user.41.libp1` |
| `preset.rename` | x | invalid parameters for `preset.rename`: unknown preset `user.41.libp1` |
| `preset.update` | x | invalid parameters for `preset.update`: unknown preset `user.41.libp1` |
| `preset.saveRecipe` | V | {"name":"Mini Recipe","recipe":[{"id":"light.exposure","value":0.3},{"id":"light.contrast","value":12}]} → {id: "user.import-recipes-mini-recipe", name: "Mini Recipe"} (0.19.0) |

## presets (1)

| id | status | note |
|---|---|---|
| `presets.list` | r | no change in presets.list; result=[{"builtin": true, "favorite": false, "group": "Color",  |

## prefs (2)

| id | status | note |
|---|---|---|
| `prefs.backgroundPrep` | R | app {culling {ahead 5, eyeAhead 8, previews true, scope all}, develop {ahead 2, scope all}, library {…}}; with a library open `own` true and `library.culling.scope` "marked" (0.19.0) |
| `prefs.setBackgroundPrep` | V | library culling scope all → marked, own false → true; refuses "no library is open" in `--demo` mode (0.19.0) |

## print (20)

| id | status | note |
|---|---|---|
| `print.cell.add` | V | settings.layout.cells.length 0 → 1 |
| `print.cell.delete` | V | settings.layout.cells.length 1 → 0 |
| `print.cell.move` | V | settings.layout.cells[0].rect.x 1.0 → 2.0 |
| `print.cell.page` | r | no change in print.get; result={"id": 1, "page": 0} |
| `print.cell.photo` | V | settings.layout.cells[0].photo 1 → 2 |
| `print.cell.resize` | V | settings.layout.cells[0].rect.h 2.0 → 3.0 |
| `print.cell.stack` | V | settings.layout.cells[0].id 1 → 2 |
| `print.exportPdf` | r | file 0 → 2585181 |
| `print.get` | r | no change in print.get; result={"cellsPerPage": 1, "gridCells": [{"h": 10.5, "w": 8.0, "x" |
| `print.layout.autoLayout` | r | no change in print.get; result={"cells": [], "pages": 1} |
| `print.layout.clear` | V | settings.layout.cells.length 1 → 0 |
| `print.layout.newPage` | V | pageCount 1 → 2 |
| `print.reset` | V | cellsPerPage 12 → 1 |
| `print.set` | V | cellsPerPage 1 → 6 |
| `print.template.apply` | r | no change in print.get; result={"cellsPerPage": 1, "gridCells": [{"h": 10.5, "w": 8.0, "x" |
| `print.template.delete` | V | templates.length 1 → 0 |
| `print.template.export` | r | no change in print.template.list; result={"name": "T1", "path": "<scratch> |
| `print.template.import` | V | templates.length 1 → 2 |
| `print.template.list` | r | no change in print.template.list; result={"templates": []} |
| `print.template.save` | V | templates.length 0 → 1 |

## profile (4)

| id | status | note |
|---|---|---|
| `profile.deleteImported` | r | .length 23 → 22 |
| `profile.favorite` | r | no change in profiles.list; result={"favorite": true} |
| `profile.import` | r | .length 22 → 23 |
| `profile.deleteCamera` | x | invalid parameters for `profile.deleteCamera`: no imported camera profile `dcp:none` — no .dcp on the test machine (0.19.0) |

## profiles (3)

| id | status | note |
|---|---|---|
| `profiles.list` | R | [{"favorite": false, "group": "Basic", "id": "lc.color", "name": "Color"}, {"favorite": fa |
| `profiles.camera` | R | {"profiles": []} (no .dcp imported) (0.19.0) |
| `profiles.menu` | R | {"favorites": [], "groups": [{"name": "Basic", "profiles": [{"favorite": false, "group": " |

## redeye (3)

| id | status | note |
|---|---|---|
| `redeye.add` | V | develop.red_eye.length 0 → 1 |
| `redeye.catchlight` | V | history.length 1 → 2 |
| `redeye.delete` | V | develop.red_eye.length 1 → 0 |

## segment (4)

| id | status | note |
|---|---|---|
| `segment.model.cancel` | r | no change in segment.model.status; result={"cancelled": false} |
| `segment.model.download` | s | model download is forbidden by the task rules (no downloads of models or binaries) |
| `segment.model.status` | r | no change in segment.model.status; result={"analyzing": false, "available": true, "busy":  |
| `segment.prepare` | x | The SAM 3 model is not installed. Download it (about 3.4 GB, SAM License (Meta)) when Ligh |

## slideshow (15)

| id | status | note |
|---|---|---|
| `slideshow.export` | V | file 0 → [1386955] |
| `slideshow.exportStatus` | r | no change in slideshow.exportStatus; result={"running": false} |
| `slideshow.layout` | V | aspect screen → 4:3 |
| `slideshow.overlays` | V | identityPlate.enabled False → True |
| `slideshow.playback` | V | fadeColor None → #ff0000 |
| `slideshow.preview` | r | no change in slideshow.preview; result={"cell": [0.0, 0.0, 320.0, 200.0], "height": 200, " |
| `slideshow.templates.apply` | r | no change in slideshow.playback; result={"applied": "user:Show1793851479", "name": "Show17 |
| `slideshow.templates.delete` | V | templates.length 8 → 7 |
| `slideshow.templates.export` | r | no change in slideshow.templates.list; result={"id": "user:Show1793851479", "name": "Show1 |
| `slideshow.templates.import` | V | templates.length 8 → 9 |
| `slideshow.templates.list` | r | no change in slideshow.templates.list; result={"folder": "<scratch> |
| `slideshow.templates.rename` | r | no change in slideshow.templates.list; result={"builtin": false, "group": "user", "id": "u |
| `slideshow.templates.save` | V | templates.length 5 → 7 |
| `slideshow.templates.update` | r | no change in slideshow.templates.list; result={"builtin": false, "group": "user", "id": "u |
| `slideshow.titles` | V | intro.content identityPlate → text |

## spot (7)

| id | status | note |
|---|---|---|
| `spot.add` | V | develop.spots.length 0 → 1 |
| `spot.delete` | V | develop.spots.length 1 → 0 |
| `spot.findBlemishes` | x | invalid parameters for `spot.findBlemishes`: finding faces needs the YuNet face detector ( |
| `spot.findDust` | V | develop.spots.length 0 → 8 |
| `spot.refreshSource` | V | develop.spots[0].source_offset.x 0.06400000303983688 → -0.06400000303983688 |
| `spot.select` | r | no change in library.state; result={"activeSpot": 0} |
| `spot.update` | V | develop.spots[0].points[0].x 0.5 → 0.52 |

## stack (11)

| id | status | note |
|---|---|---|
| `stack.auto` | r | no change in library.state; result={"photos": 0, "stacks": 0} |
| `stack.collapseAll` | r | no change in library.state; result={"changed": 0} |
| `stack.expandAll` | V | undo Group into Stack → Expand All Stacks |
| `stack.group` | V | selection.ids.length 2 → 1 |
| `stack.moveDown` | r | undo Group into Stack → Move in Stack |
| `stack.moveUp` | r | no change in library.state; result={"changed": 0} |
| `stack.remove` | V | undo Group into Stack → Remove from Stack |
| `stack.setTop` | r | no change in library.state; result={"changed": 0} |
| `stack.split` | V | undo Group into Stack → Split Stack |
| `stack.toggle` | V | undo Group into Stack → Expand Stack |
| `stack.ungroup` | V | undo Group into Stack → Ungroup Stack |

## version (5)

| id | status | note |
|---|---|---|
| `version.create` | V | versions.length 1 → 2 |
| `version.delete` | V | versions.length 1 → 0 |
| `version.rename` | V | versions[0].name v1 → renamed |
| `version.restore` | V | develop.light.exposure -1.0 → 1.0 |
| `version.update` | V | versions[0].settings.light.contrast 0.0 → 40.0 |
