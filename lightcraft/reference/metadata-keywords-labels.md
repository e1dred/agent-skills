# Metadata, keywords, labels, presets, filters

## Per-photo metadata

- `photo.inspect {id?}` returns everything: `develop`, `meta` (title, caption, alt_text, extended_description,
  copyright, creator, location, city, state, country, gps, keywords, camera, lens, iso, aperture, shutter,
  focal_mm), `rating`, `flag`, `label`, `albums`, `versions`, `history`, `file_name`, `width/height`.
- `photo.rate {rating:0..5,ids?,advance?}`, `photo.increaseRating`, `photo.decreaseRating`;
  `photo.flag {pick|reject|none,ids?}`, `photo.pick`, `photo.reject`, `photo.unflag`, `photo.cycleFlag`,
  `photo.increaseFlag`, `photo.decreaseFlag`; `photo.label {red|yellow|green|blue|purple|none,ids?}`,
  `photo.clearLabel`. All verified changing `rating`/`flag`/`label` in `photo.inspect`.
- `photo.setMeta {ids?,title,caption,altText,extendedDescription,copyright,copyrightStatus,usageTerms,
  copyrightUrl,creator,location,city,state,country,gps:"lat, lon"|[lat,lon]|null,keywords,addKeywords,
  removeKeywords}` — verified caption and keywords (setting keywords replaces the list).
- `photo.setCaptureTime {ids?,time,each?,shift?,hours?}` (verified captured 2026-03-01 → 2026-09-30).
- `photo.rename {template,start?,ids?}` — tokens `{name} {num} {seq} {seq:N} {date} {date:%Y%m%d} {folder}
  {camera} {lens} {iso} {rating} {title} {creator} {ext}` (`photo.renameTokens` lists them with meanings);
  verified `Trip-{seq:3}` → `Trip-001.JPG`. `photo.renamePreview` returns the `from/to` list without renaming.
- `photo.allMetadata {id?}` → `{exif:[],xmp:[],note}` (a demo photo: "a generated demo photo has no file");
  `photo.readMetadataFromFile {ids?}` reads XMP from the file/sidecar (`{read,failed}`),
  `photo.saveMetadataToFile {ids?}` writes it, `photo.readFocusPoints {ids?,wait?}` queues detection.
- `photo.copyMetadata` / `photo.pasteMetadata {ids?,fields?}` copy metadata between photos (verified title).
- `photo.moveToFolder {folder,ids?}`, `photo.relink {id,path}`, `photo.reload {ids?}`, `photo.delete {ids?}`
  (Recently Deleted; verified total 24 → 23), `photo.restore`, `photo.deletePermanently` (verified),
  `photo.virtualCopy {ids?,name?}` (new photo id, same file), `photo.duplicate {ids?}` (needs a real file:
  *"a generated demo photo has no file to duplicate"*), `photo.convertToDng {ids?}` (raw/real files),
  `photo.editExternal {ids?,colorSpace?,format:tiff|psd,bitDepth?,dir?}` (real files),
  `photo.analyze {ids?,rejectBelow?,pickBest?,burstGap?,similarity?}` (sharpness report),
  `photo.smartPreview {id?}`, `photo.flipHorizontal/Vertical`, `photo.rotateLeft/Right`
  (verified `develop.orientation` Normal → Rotate90/270).
- `photo.setRegion {id,index,rect}` / `photo.removeRegion {id,index}` only resize/remove **existing face or pet
  regions**; with none: *"no such region"*.
- `photo.autoTagTracklog {path|gpx,ids?,offset?,maxGap?,replace?,dryRun?}` — GPX track → GPS (verified run with a
  2-point GPX we made; the demo date is outside the track by default, use `offset`/`dryRun`).

## Keywords

- `keyword.create {name,parent?,synonyms?,includeOnExport?,exportContaining?,exportSynonyms?,person?,
  addToSelected?,ids?}` → `{keyword}`; a duplicate name is refused. `keyword.delete {keyword}` (verified removing
  it from the photo's `meta.keywords`), `keyword.rename {from,to}`, `keyword.edit {keyword,…}`,
  `keyword.merge {from:[…],into}`, `keyword.move {keyword,parent|null,merge?}`, `keyword.purgeUnused`.
- `keyword.list` → the tree (`{name,path,count,children}`); `keyword.info {keyword}`; `keyword.suggest {prefix?,
  ids?,limit?}` (empty on the synthetic test photos); `keyword.export {path?}`, `keyword.import {path|text}`
  (verified +2 keywords from text).
- `keyword.setShortcut {keywords:"a, b"}` (verified the keyword list marked), `keyword.shortcut`,
  `keyword.toggleShortcut {ids?}` (verified removing the keyword from a photo that had it), `keyword.setDefaultParent`.
- Keyword sets (nine slots): `keyword.sets` → `{current,keywords,sets:[…]}`, `keyword.saveSet {name,keywords?,
  replace?,new?}` (verified current set + 2 slots), `keyword.useSet`, `keyword.nextSet`, `keyword.previousSet`,
  `keyword.deleteSet {name}`, `keyword.toggleFromSet {index:1..9,ids?}`.
- `keyword.setShortcut` marks keywords; `person` keywords are ordinary keywords with `person:true`.

## Labels

- `label.names` → five labels with `name`/`custom`; `label.setNames {names:{red:"Urgent",…}}` (verified 2 changed);
  `label.sets` → `{current,sets:[{name,builtin,names}]}`, `label.saveSet {name}` (verified set count 2 → 3),
  `label.applySet {name}`, `label.deleteSet {name}` (verified 3 → 2).

## Metadata presets and filter presets

- `metadata.savePreset {name,fields?,only?}` (verified preset count 0 → 1), `metadata.presets`,
  `metadata.applyPreset {name,ids?}` (verified `meta.creator` "LightCraft Demo" → "Me"), `metadata.deletePreset`.
- `metadata.downloadPlaceNames` downloads the GeoNames dataset — **not run here (network rule)**;
  `metadata.placeNamesStatus` reports dataset bytes; without the dataset `metadata.reverseGeocode` refuses
  (*"the place names aren't downloaded"*). `photo.setMeta gps=…` gives a photo a position for later geocoding.
- `filter.savePreset {name}` (needs a non-empty filter: set `library.filter` first), `filter.presets`,
  `filter.applyPreset {name}`, `filter.deletePreset {name}`.

## Catalog reads

- `catalog.query {filter?,sort?,offset?,limit?}` → `{photos:[{id,fileName,captured,rating,flag,label,keywords,
  title,camera,width,height,format,edited,deleted}],total}`; `catalog.stats` → albums/byDate/months counts.
- `library.findSimilar {id,similarity?,filter?}`, `library.missing`, `library.findMissing {folder}`.
