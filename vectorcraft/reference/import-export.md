# Opening, saving, exporting and converting

## Commands

- `document.open {path|name|dataBase64, pages?|page?, cropTo?, …} → {fileInfoTitle, format, index,
  missingLinks, modified, warnings}` — replaces the active document. Verified with SVG, PDF, AI,
  EPS, PSD, DXF, EMF, WMF, templates and the native format.
- `file.open` is the same and verified; `file.new {preset?, width?, height?, units?, orientation?,
  artboards?, …} → {index}` starts a blank document; `file.newFromTemplate {path|name,dataBase64}`
  opens a template as untitled.
- Save: `document.save {path?, format?, options?, svg?, modified?} → {path, bytes, format, warnings}`,
  `file.saveAs` (same, takes the new path as the document's own), `file.saveCopy` (copies without
  changing the document), `file.saveAsTemplate {path?, format?:"template"|"ait"}`.
- Export: `document.export {path?, format?, scale?, …options} → {path, bytes, format, warnings}`,
  `document.exportSelection` (crops to the selection), `document.serialize {format?}` (returns
  `dataBase64` instead of writing), `document.exportForScreens {folder?, zip?, artboards?, …}`,
  `document.exportForOffice`, `document.exportForWeb`, `document.exportPdf`, `document.exportEps`,
  `document.exportDxf`, `file.export`, `file.exportForScreens`, `file.print`, `file.package`.
- Read info: `file.info`, `document.info`, `document.formats → {formats:[…], readable, writable}`,
  `file.formatOptions {format?}`, `document.exportSettings`, `document.pdfInfo {path…}`,
  `document.dxfInfo`, `links.*` for placed images.
- Place images: `file.place {path|name|dataBase64, link?} → {ids, format, width, height, linked,
  warnings}` (verified: a 300×200 SVG placed at 148 pt high, unlinked);
  `file.place.info`, `file.place.queue`, `links.place/relink/embed/unembed/update/info/list`.
- Clipboard: `clipboard.importSvg/importText/importImage/importPdf/importEmf/importEps`,
  `clipboard.exportSvg/Png/Pdf/Text`, `clipboard.flavours → {flavours}` (verified:
  text/plain, image/svg+xml, image/png), `clipboard.conflicts`.

## Formats actually verified (2026-11-04, 0.21.0)

**Export — every writable format produced a file of the right type** (`document.export`,
`format` explicit, magic bytes checked):

| Format | Bytes (test doc) | Format | Bytes |
|---|---|---|---|
| `.vectorcraft` | 31 532 | `.svg` | 767 |
| `.svgz` | 425 | `.pdf` | 9 845 |
| `.ai` | 10 389 | `.png` | 5 975 |
| `.jpg` | 21 262 | `.gif` | 3 721 |
| `.webp` | 3 122 | `.tif` | 49 218 |
| `.bmp` | 1 454 166 | `.tga` | 1 454 156 |
| `.psd` | 82 317 | `.vctemplate` | 31 554 |
| `.txt` | 6 (type text only) | `.dxf` | 23 139 |
| `.eps` | 38 863 | `.emf` | 3 700 |
| `.wmf` | 2 692 | | |

The same 19 formats were also produced by `vectorcraft-cli convert in.svg out.<ext>`.

**Open — every readable fixture opened with art intact:**

| Read | Objects after open | Read | Objects |
|---|---|---|---|
| `.vectorcraft` | 4 | `.svg` / `.svgz` | 4 / 4 |
| `.pdf` / `.ai` | 4 / 4 | `.eps` | 4 |
| `.png` / `.jpg` / `.gif` / `.webp` | 2 each (one image) | `.tif` / `.bmp` / `.tga` | 2 each |
| `.psd` | 2 | `.vctemplate` | 4 |
| `.dxf` | 25 (one per stroke/shape piece) | `.emf` / `.wmf` | 5 / 5 |

## Format rules worth knowing

- Format comes from the path's extension; `format` overrides it. Unknown extension → PNG.
- Raster exports are sized by `scale` (pixels per point, default 1): a 612×792 pt artboard is
  612×792 px at scale 1.
- A PDF export omits the embedded native document unless the caller asks for it
  (`convert`'s `--preserve-editing`; the app's Save As PDF keeps it by default).
- `convert IN OUT` is the one-file path. Its flags: `--artboard I` (0-based), `--range "1-3,5"`
  (1-based), `--scale`, `--outline-text`, `--decimals 1-7` (SVG coordinates), `--hidden-objects
  layer|omit|visible`, `--transparent-images flatten|omit`, `--ai-version 7|pdf`,
  `--replace-lossy`, `--editing-data`. A PDF gets every artboard; EPS gets the art bounds; other
  formats the first artboard.
- `.txt` export writes the type only — the test document's one text object became a 6-byte file.
- PSD/PSB import is the merged image (README); PSD export writes layers.
- `--automation-read-root`/`--automation-write-root` (MCP) limit which paths may be opened,
  placed or written.
- Templates: `file.saveAsTemplate` writes `.vctemplate` (or legacy `.ait` when `format:"ait"`);
  `file.newFromTemplate` opens one as a new untitled document.

## Print and package

`print.preview`, `print.tiling`, `print.setup`, `print.presets.list/save/delete/export/import`,
`file.print` (verified: produced a 7 230-byte PDF). `file.package {path?}` bundles a **saved**
document and its links as a ZIP (verified after saving: 210 410 bytes; without a save it refuses
"save the document first").

## Known headless gaps found

- `document.pdfInfo` refused on the synthetic PDF our own exporter wrote ("PDF parser rejected the
  document") even though `document.open` read the same file; use `document.open` + inspect for
  PDF facts.
- `document.dxfInfo` refused on our own DXF ("not a DXF drawing"); `document.open` read it fine.
- `file.recovery.*` refuses without Data Recovery folders configured in Preferences.
- `file.close`/`file.closeAll` leave no document open, so the follow-up inspect errors
  ("no document open") — run them last in a script.
