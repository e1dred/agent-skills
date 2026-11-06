# Swatches, colour and export (PDF/X, PDF/A, IDML, EPUB, PPTX, HTML, images)

> **Versions:** DesignCraft 0.17.2 (Linux AppImage, `designcraft-cli`), 2026-11-05, headless unless stated.

## Swatches and tints

```
file.new {"units":"points","width":396,"height":612,"pages":1,"margins":45,"title":"Swatches and Colour"}
# process CMYK and spot colours
swatch.create {"name":"Deep Cypress","color":{"c":80,"m":30,"y":60,"k":20}}
swatch.create {"name":"Terracotta Spot","color":{"c":0,"m":65,"y":80,"k":5},"spot":true}
# frame: fill with the process colour at 40%, stroke with the spot at 50%
frame.create {"rect":[60,80,336,300],"content":"graphic"}
object.fill {"swatch":"Deep Cypress","tint":0.4,"ids":["$3.id"]}
object.stroke {"swatch":"Terracotta Spot","tint":0.5,"weight":6,"ids":["$3.id"]}
# text: spot fill at 50% for the whole paragraph, process at 35% for the first 14 bytes
frame.create {"rect":[60,330,336,470],"content":"text","text":"Colour proofs for an invented specimen page."}
text.select {"story":"$6.story","anchor":0,"focus":9999}
type.char {"attrs":{"size":22,"fill":"Terracotta Spot","fillTint":0.5}}
text.select {"story":"$6.story","anchor":0,"focus":14}
type.char {"attrs":{"fill":"Deep Cypress","fillTint":0.35}}
document.inspect {}
```

1. **You cannot create a tint swatch with the CLI.** `swatch.options {"name":"Deep Cypress 40",
   "base":"Deep Cypress","tint":0.4}` fails: *no swatch `Deep Cypress 40`* — `swatch.options` only
   **edits an existing** swatch, and a plain colour swatch refuses `base`/`tint`
   ("only tint swatches have a tint"; source `cmd/style/swatches.rs`). `swatch.create` accepts
   only a colour or a gradient. Apply a tint numerically instead: `object.fill {swatch, tint}`,
   `type.char {attrs:{fill, fillTint}}`, `table.setCell {fill, tint}`, stroke `tint`.
   (A tint swatch can still be *edited* if the document already has one, e.g. imported. To make one anyway:
   unzip the `.designcraft`, add `{"name":"Brand 50%","value":{"kind":"tint","base":"Brand","tint":0.5},
   "locked":false,"named":true}` to `document.json` `swatches`, re-zip with `mimetype` stored first, open it with
   `--in`; then `swatch.options {"name":"Brand 50%","tint":0.25}` read back `.value.tint` 0.5 → 0.25.)
2. **Spot must be declared at creation**: `spot:true` in `swatch.create`. Changing it later works
   through `swatch.options {spot:true}`, but the value must then be a plain colour swatch.
3. **Text tint is a character attribute**: `fill` + `fillTint` (0–1) inside `type.char attrs`;
   reading it back gives 0.3499999940… for 0.35 (f32), so compare with a tolerance.
4. **`object.fill`/`stroke` need an explicit target**: pass `ids:[…]` (the frame was just created
   and selected, but the reliable form is the id from `frame.create`).
5. `swatch` names are the currency everywhere (fill attributes, style definitions, PDF
   separations). `[None]`, `[Registration]`, `[Black]`, `[Paper]` are locked and can't be
   renamed or given tints.

- **Print files need CMYK swatches.** `swatch.create {color:"#1F3A5F"}` makes an RGB swatch, and a PDF/X-4 export
  then warns, and `validate-pdf` reports: *"RGB fills or strokes on page 1: under a CMYK output intent RGB needs an
  ICC profile"*. Create `{c,m,y,k}` swatches (0–100) instead, or convert in place with
  `swatch.options {name, color:{c,m,y,k}}` (every use follows). After that, the same export validates with
  `issues: []`.

## Export matrix

```
file.new {"units":"points","width":396,"height":612,"pages":2,"facingPages":false,"margins":45,"bleed":9,"title":"Export Matrix"}
style.paragraph.create {"name":"Ex Head","para":{"align":"left","spaceAfter":12},"chars":{"size":26,"leading":{"kind":"points","value":30}}}
style.paragraph.create {"name":"Ex Body","para":{"align":"left","hyphenate":true},"chars":{"size":10,"leading":{"kind":"points","value":13}}}
frame.create {"rect":[45,45,351,150],"content":"text","text":"Export matrix\nA specimen sheet for output tests"}
text.select {"story":"$3.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Ex Head"}
frame.create {"rect":[45,170,351,560],"content":"text","text":"Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum. "}
text.select {"story":"$6.story","anchor":0,"focus":99999}
style.paragraph.apply {"name":"Ex Body"}
frame.create {"rect":[60,380,336,520],"content":"graphic"}
file.place {"path":"/scratch/…","frame":"$9.id"}
document.inspect {}
```

- `file.exportPdf {path, standard:"x4"|"x1a"|"a2b"|"none", bleed:true, marks:{crop:true, bleed:false,
  pageInfo:false}, title}` → `{path, bytes, pages, warnings}`. **Read `warnings`**: a PDF/X problem is
  reported there and the file is still written.
- PDF/X-4 adds a FOGRA39 output intent, embeds fonts and sets the boxes: a 396×612 page with 9 pt bleed and marks
  came out with MediaBox 462×678, BleedBox 24–438 × 24–654, TrimBox 33–429 × 33–645 (`pdfinfo -box`).
- Bleed (and slug) belong to the document, not the export: set them in `file.new {bleed}` or later with
  `layout.documentSetup {bleed: 9}` (points; `slug` likewise), then export with `bleed:true`. For a home-printing
  PDF use `standard:"none"` with no `bleed`/`marks`.
- `designcraft-cli validate-pdf FILE.pdf [--standard x4|x1a]` → JSON `{issues, path, standard}`; `issues: []` is a
  pass. It has no PDF/A check.

1. **`validate-pdf` always labels its check "PDF/X-4"** unless told otherwise; it cannot validate
   PDF/A-2b. A PDF/A export legitimately fails it. Only X-4 (and X-1a with `--standard x1a`)
   are meaningful; read the `standard` field in the JSON.
2. **Export sizes differ by purpose**: X-4 is 481 KB because marks/bleed and embedded fonts are
   added; A-2b/plain are ~20 KB. Don't compare them as if one were "the same file".
3. **`file.exportPdf` takes 1-based `pages`** (`"1-3"`), while `run --page` is 0-based.
4. **IDML export needs a path** (no path returns `{base64}`), and `embedImages:true` matters —
   without it the package links to the image by absolute path.
5. **Fixed EPUB is images** (page PNGs). Choose reflowable when the text must be live/searchable.
6. **The cover is page 1** (`cover:true`), which for this 2-page sheet duplicates page 1.
7. File extension decides `run --export` type; `.jpg` works, other unknown extensions abort.
8. `--export` may repeat, and `--page/--scale` apply only to the exports after them.

## Several copies of a page on one sheet (2-up for home printing)

Place the exported PDF twice on a letter-landscape page; the placed PDF stays vector (fonts embedded):

```
file.new {"units":"points","width":792,"height":612,"pages":1,"facingPages":false,"margins":0}
place.load {"path":"/abs/path/single.pdf"}
place.drop {"spread":0,"x":0,"y":0}
place.load {"path":"/abs/path/single.pdf"}
place.drop {"spread":0,"x":396,"y":0}
```

`place.load` returns `{asset, width, height, loaded}`; `place.drop` returns `{id}`; the item reads back as
`<image>` with bounds `[0,0,396,612]` / `[396,0,792,612]`. Export with `--export out.pdf` or `file.exportPdf`.
