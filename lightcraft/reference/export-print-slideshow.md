# Export, print and slideshow

## Export

- `app.export {path|dir, ids?, preset?, format?:jpeg|png|tiff|webp|avif|jxl|psd|dng|original, longEdge|
  shortEdge|width|height|megapixels|percent, fit?, dontEnlarge?, ppi?, quality?, jxl*, limitKb?, colorSpace?:
  srgb|displayP3|adobeRgb|proPhoto|rec2020, bitDepth?, hdr?, sharpen?, metadata?, removeLocation?, naming?,
  startNumber?, conflict?, tiffCompression?, dngCompression?, watermark?: text|{…}, addToPhotos?, photosAlbum?}`
- Verified on the demo photo at `longEdge=800`: jpeg/png/tiff/webp/psd/jxl/avif each wrote a file (psd 2.5 MB,
  jxl 37 KB, avif 35 KB; PIL reads jpeg/png/tiff/webp/psd-header only — check sizes for jxl/avif).
- `dng` and `original` need a real source file: *"LC01207.JPG is a generated demo photo: it has no original file
  to export"*. `watermark:"Test"` and `colorSpace:"displayP3"` (mean RGB shifted 156.8/142.6/140.5 →
  154.5/143.0/141.1) verified.
- `export.checkTarget {path}` returns what an export to that path would do; `export.contactSheet {path,
  ids?,paper?,landscape?,columns?,rows?,captions?}` wrote a 90 KB PDF for 3 photos.
- `export.presets` (built-ins "JPEG (Small)", … plus user ones), `export.savePreset {name,params?}` (verified
  count 4 → 5), `export.deletePreset {name}` (verified name gone), `export.photosImports` (macOS Photos import
  jobs; `{imports:[]}` here), `export.addToPhotos` — macOS only.

## Print

- `print.get` is both the state read and the layout result: `{pageWidth,pageHeight,pageCount,cellsPerPage,
  gridCells:[{x,y,w,h}],papers,settings{layout,…},photos}` (inches).
- `print.set {layout?{style:singleImage|contactSheet|picturePackage|customPackage, page{paper,customWidth,
  customHeight,orientation,margins}, grid{columns,rows,spacingX,spacingY,keepSquare}}, image?, …}` — verified:
  contactSheet 3×2 gave `cellsPerPage:6`.
- `print.cell.add {width,height,x?,y?,page?,photo?}` (inches; **width and height are required**) → `{id,cell,
  pages}`; cells live in `print.get.settings.layout.cells`. `print.cell.photo {id,photo}`, `print.cell.move
  {id,x,y,snap?}`, `print.cell.resize {id,width?,height?,x?,y?}`, `print.cell.page {id,page}`,
  `print.cell.stack {id,order:toBack|backward|forward|toFront}`, `print.cell.delete {id}` — all verified.
- `print.layout.autoLayout` works only in a picture/custom package (*"cells exist only in the Picture Package
  and Custom Package styles"*); `print.layout.clear` (verified cells 1 → 0), `print.layout.newPage` (verified
  pageCount 1 → 2), `print.reset`.
- Templates: `print.template.save {name}` (verified list 0 → 1), `print.template.list`, `print.template.apply
  {name}`, `print.template.export {name,path}` writes a `.lcprint` JSON (1.5 KB verified),
  `print.template.import {path}` (verified list 1 → 2; a taken name gets " (2)"), `print.template.delete {id}`.
- `print.exportPdf {path,ids?}` — verified 2.6 MB PDF from the contact sheet for 2 photos.

## Slideshow

- Settings, each read back from its own command: `slideshow.playback {slideDuration,fadeDuration,fadeColor,
  randomOrder,repeat,preparePreviews,manual}`, `slideshow.layout {margins|marginLeft…,linkMargins,showGuides,
  aspect:"screen"|"16:9"|"4:3",zoomToFill,backdropColor…}`, `slideshow.overlays {identityPlate,ratingStars,
  texts,audio?}` (unknown keys refused; verified `identityPlate.enabled`), `slideshow.titles {intro?,ending?}`
  (verified `intro.content: identityPlate → text`).
- `slideshow.preview {id?|title:"intro"|"ending",template?,width?,height?}` → `{cell,width,height,overlays…}`
  (verified 320×200 for id 1).
- `slideshow.export {format:pdf|jpeg|video, path, size?, quality?, fps?, container?, name?, ids?, wait?}`:
  **pass `wait:true`** — without it the call returns a `taskId` and the process can exit before the background
  task finishes, leaving `<path>.part`. With `wait:true` verified: 385 KB PDF (2 photos), a folder of
  `showjpg-001.jpg…`, a 1.4 MB AV1 `.mp4`. `slideshow.exportStatus` reports the last export.
  `activity.list`/`activity.cancel {id|all}` manage the background rows.
- Templates: `slideshow.templates.list` (5 built-ins + user ones), `slideshow.templates.save {name,replace?}`
  (verified count +1), `.apply {id|"previous"|name}` (result `{applied:"user:Name",…}`),
  `.rename {id,name}`, `.update {id}`, `.delete {id}`, `.export {id,path}` (JSON), `.import {path}` (verified
  count +1). **Template ids are `user:<Name>`** (e.g. `user:MyShow`), not `user-MyShow`.
