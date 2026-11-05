# Masks, mask effects, spot removal, red eye

## Masks

- `mask.add {kind, …shape, name?}` → `{activeMask:id}`; masks are numbered from 1 per photo and appear in
  `photo.inspect.develop.masks` (each has `adjust`, `components`, `invert`, `visible`, `refine`, `name`).
- Kinds that work headless (each verified adding a mask to the demo photo): `radial` (`center{x,y},rx,ry`),
  `linear` (`start,end`), `brush` (then `mask.brushStroke`), `sky`, `subject`, `background`,
  `luminanceRange` (`lo,hi`), `colorRange` (`x,y` sample point).
- **`object` and `prompt` need the SAM 3 model (~3.4 GB, Meta SAM licence) and are refused without it:**
  *"The SAM 3 model is not installed…"*. `segment.prepare` and `segment.model.status` use the same model
  (`status` reports `{available:false,…}`); `segment.model.download` was not run (no downloads).
- `mask.brushStroke {id,points,size,feather?,flow?,density?,erase?,autoMask?,pressure?,connect?}` — verified
  adding a stroke (`components[0].shape.strokes` 0 → 1).
- `mask.addComponent {id,op:add|subtract|intersect,kind,…shape}`, `mask.component {id,component,action:
  invert|duplicate|delete|rename|op,name?,op?}`, `mask.invert`, `mask.delete`, `mask.deleteAll`,
  `mask.duplicate {invert?}`.
- `mask.rename {id,name}`, `mask.visible {id,visible}`, `mask.select {id|null}`, `mask.move {id,to|delta}`,
  `mask.refine {id,value}` (0…100; changed only `edited`/history in the demo, no read-back field),
  `mask.refineDetail {id,component?}` (Object/Describe masks only — refused on a radial mask).
- `mask.update {id,component?,shape}` needs the **complete** shape, e.g.
  `{"kind":"radial","center":{"x":0.4,"y":0.4},"rx":0.2,"ry":0.2,"angle":0,"feather":50,"invert":false}`;
  a partial shape is refused with `missing field \`angle\``.
- `mask.objectPoint {id,x,y,exclude?}` needs an Object mask first (*"the mask has no Object selection"*).
- `mask.sampleColor {x,y,add?,id?,component?}` — verified adding a colour sample to a colourRange mask.
- `mask.adjust {id,values:{exposure,contrast,highlights,shadows,whites,blacks,temp,tint,texture,clarity,dehaze,
  hue,saturation,sharpness,noise,moire,defringe,color_hue,color_sat,amount}}` — verified contrast 30.

## Mask effects

- `mask.saveEffect {name,id?,group?,fields?,amount?,brush?}` saves the mask's adjust as a named effect;
  `mask.effects` → `{current,effects:[…],groups,toolEffects}`; `mask.applyEffect {name,id?|ids?|all?|photos:"selected",remember?}`
  applies it (verified: a second mask's contrast 0 → 30 from effect E1).
- `mask.deleteEffect {name|names}`, `mask.duplicateEffect {name,to?}`, `mask.renameEffect {name,to}`,
  `mask.renameEffectGroup {group,to}` (param is `group`, not `from`), `mask.setEffectGroup {name|names,group}`,
  `mask.favoriteEffect {name|names,favorite?}`, `mask.toolEffect {tool,name?}`.
- `mask.exportEffects {path,names?,group?}` writes a JSON file (`{count,path}`), `mask.importEffects
  {path|paths,group?,dryRun?}` (our round-trip import reported the file in `failed`; the export format is its own).
- `mask.updateEffect {name,id?,fields?,amount?,brush?}`.

## Spot removal

- `spot.add {mode:remove|heal|clone|fill, points:[[x,y]…], size (fraction of long edge), feather?,opacity?,
  source?:[dx,dy]}` → `{index}`; verified both `remove` and `heal`, and `develop.spots.length` 0 → 1.
- `spot.delete {index?}`, `spot.select {index|null}` (`library.state.activeSpot`), `spot.update {index?,
  move?,source?,moveSource?,size?,feather?,opacity?,mode?}` (verified moving the point 0.5 → 0.52),
  `spot.refreshSource {index?}` (verified source offset flipped sign).
- `spot.findDust {sensitivity?,add?}` — verified: found 8 spots (`develop.spots.length` 0 → 8).
- `spot.findBlemishes {sensitivity?,add?,maxPerFace?}` — needs the YuNet face detector (232 KB, MIT); refused
  without it. Same model is needed by `faces.detect`.

## Red eye

- `redeye.add {center,rx,ry,pet?,pupilSize?,darken?}` → `{index}` (verified `develop.red_eye.length` 0 → 1).
- `redeye.catchlight {index,on?,offset?}` — **only for pet eyes** (*"catchlights are for pet eyes"*); add with
  `pet:true` first.
- `redeye.delete {index}` (verified).
