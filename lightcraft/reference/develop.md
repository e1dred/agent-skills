# Develop: sliders, crop, curves, white balance, before/after

All of this is non-destructive and undoable; read `photo.inspect` (`develop.*`, `meta`, `edited`) or
`develop.get` (settings only) before and after.

## Develop values

- `develop.set {control, value, ids?}` or `{values:{control:value,…}}` — sets one or many sliders on the
  selection. Every one of the 122 controls was set once and read back from `develop.controls` (see
  `develop-controls.tsv`: id, section, min, max, default, value).
- `develop.adjust {control,delta}`, `develop.quickAdjust {control,delta,ids?}` — relative change (verified:
  exposure 0 → 0.5; contrast 0 → 10).
- `develop.get {id?}` returns the settings tree; `develop.controls {section?}` returns every slider with
  `range`, `default`, `value`.
- `develop.reset {ids?}`, `develop.resetControl {control}`, `develop.resetSection {section}`,
  `develop.sectionEnabled {section,enabled}` (verified: disabled_sections gains one entry).
- `develop.auto`, `develop.autoBwMix`, `develop.autoSync {on?}`, `develop.sync {groups?}`,
  `develop.copy` (returns copied `groups`), `develop.paste {ids?,groups?}`, `develop.pastePrevious {ids?}`,
  `develop.merge {settings,label?}` (merges a partial settings JSON; verified exposure 0 → 0.8),
  `develop.matchExposure {ids?}`, `develop.treatment` (toggles colour/B&W: `color` → `bw`).
- `develop.beginInteraction {label}` / `develop.endInteraction` / `develop.cancelInteraction` bracket a drag so
  it makes one undo step.
- `develop.targeted {target:curve|hue|sat|lum, x, y, delta, channel?}` — targeted adjustment at a normalized
  point (verified: mixer orange hue +10, red sat 2.84 under the point).
- `develop.updateProcess {ids?}` — migrates photos to the current processing version; refused
  (*"already on the current process (version 2)"*) when there is nothing to do.
- `develop.profile {id,amount?}` — ids from `profiles.list` (`lc.color`, `lc.neutral`, …, verified amount
  100 → 50); `profiles.menu` gives the grouped menu; `profile.favorite`, `profile.import {paths: .cube|zip}`,
  `profile.deleteImported {id: "lut:…"}` (verified with a 2³ LUT we wrote ourselves).
- `develop.hdr {enabled?,maxEv?}` — result `{enabled,maxEv}`; `photo.inspect.develop.hdr` exists but the toggle
  only showed as `edited`/`history` in the demo. `hdr.*` SDR controls exist in `light` and `detail`.

## Controls (122, by section)

| Section | n | ids |
|---|---|---|
| profile | 1 | `profile.amount` |
| color | 4 | `wb.temp` `wb.tint` `color.vibrance` `color.saturation` |
| light | 13 | `light.exposure` `light.contrast` `light.highlights` `light.shadows` `light.whites` `light.blacks` `hdr.maxEv` `hdr.sdrBrightness` `hdr.sdrContrast` `hdr.sdrHighlights` `hdr.sdrShadows` `hdr.sdrWhites` `hdr.sdrClarity` |
| curve | 8 | `curve.highlights` `curve.lights` `curve.darks` `curve.shadows` `curve.splitShadows` `curve.splitMid` `curve.splitHighlights` `curve.refineSaturation` |
| mixer | 24 | `mixer.{red,orange,yellow,green,aqua,blue,purple,magenta}.{hue,sat,lum}` |
| bwMix | 8 | `bw.{red,orange,yellow,green,aqua,blue,purple,magenta}` |
| grading | 14 | `grading.{shadows,midtones,highlights,global}.{hue,sat,lum}` `grading.blending` `grading.balance` |
| effects | 3 | `effects.texture` `effects.clarity` `effects.dehaze` |
| vignette | 5 | `vignette.amount` `vignette.midpoint` `vignette.roundness` `vignette.feather` `vignette.highlights` |
| grain | 3 | `grain.amount` `grain.size` `grain.roughness` |
| detail | 11 | `enhance.denoise` `detail.sharpen{Amount,Radius,Detail,Masking}` `detail.nr{Luminance,Detail,Contrast,Color,ColorDetail,ColorSmoothness}` |
| optics | 13 | `optics.{distortion,vignetting,vignettingMidpoint,profileDistortion,profileVignetting}` `optics.defringe{Purple,Green}*` `optics.caRed` `optics.caBlue` |
| geometry | 8 | `geometry.{vertical,horizontal,rotate,aspect,scale,offsetX,offsetY}` `crop.angle` |
| calibration | 7 | `calibration.{shadowsTint,redHue,redSat,greenHue,greenSat,blueHue,blueSat}` |

`develop.set` ids are exactly these strings. `photo.inspect` shows the same values under snake_case paths
(`detail.sharpenAmount` → `develop.detail.sharpen_amount`); a name that is not a control (`light.vibrance`)
is refused.

## Crop and geometry

- `crop.set {rect:[x0,y0,x1,y1] (normalized), angle?}` (verified rect 0,0,1,1 → 0.2,0.2,0.8,0.8).
- `crop.aspect {aspect:"original"|"free"|"current"|"toggle"|"1x1"|"4x5"|"8.5x11"|"5x7"|"2x3"|"4x3"|"16x9"|"16x10"|[w,h], orientation?:crop|given}`
  (verified `1x1` shrank the crop to a square; `2x3` set `crop.aspect` 300×200).
- `crop.rotateAspect` swaps the locked ratio (verified 2:3 → 3:2), `crop.straighten {angle}` (−45…45; verified
  5°), `crop.drag {handle,from,to,start?,keepRatio?}` (verified topLeft 0,0 → 0.2,0.2), `crop.reset`,
  `crop.autoStraighten` (refused on the synthetic gradient: *"no dominant horizontal or vertical lines"*).
- `geometry.upright {mode:off|auto|guided|level|vertical|full}` (verified `level`), `geometry.guides
  {guides:[[x0,y0,x1,y1]…], add?}` (verified one guide; adding a guide switched upright to `guided`).

## Curves

- `develop.curve {channel:master|red|green|blue, points:[[x,y]…] 0..1}` — verified with
  `[[0,0],[0.5,0.6],[1,1]]` (curve.master length 0 → 3).
- `curve.presets` → `{current, presets:[{name,master,red,green,blue,builtin?}]}`; `curve.applyPreset {name}`
  (verified "Medium Contrast").
- `curve.savePreset {name}`, `curve.deletePreset {name}` (built-ins cannot be deleted),
  `curve.exportPresets {path,names?}` writes `.lccurve` (`{path,count}`), `curve.importPresets {path|paths}` →
  `{imported,failed}` (verified round trip: save TestS2 → export → delete → import → TestS2 back),
  `curve.reset {channel:all|point|parametric|master|red|green|blue}`.

## White balance

- `develop.wb {mode:asShot|auto|daylight|cloudy|shade|tungsten|fluorescent|flash|custom, temp?, tint?}` —
  verified `cloudy` (temp 6500 → 5500, tint 0 → 10, mode asShot → cloudy).
- `develop.wbPick {x,y}` — normalised point of a neutral; refused without `x`/`y`.
- `develop.hdr {enabled,maxEv}`, `develop.treatment` (B&W toggle).

## Before/after and point colour

- `beforeAfter.setBefore {source:import|current|history|version, index?, name?}`, `beforeAfter.swap`,
  `beforeAfter.copyBeforeToAfter` (verified: exposure 1.0 → 0.0), `beforeAfter.copyAfterToBefore`,
  `beforeAfter.resetBefore`.
- `pointColor.pick {x,y}` samples a colour (max 8) and returns `{index,lum,chroma,hue}` (verified adding
  `develop.point_colors[0]`); `pointColor.delete {index}`.
