# DeckCraft reference: newer and changed commands

Part of the deckcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## New in 0.11.x (verified headless)


- Path editing on a shape: `shape.openPath {"index":0}` (break a closed outline), `shape.closePath {"index":0}`, `shape.deleteSegment {"index":0,"segment":2}`
  (**only on a closed outline**, otherwise "only a segment of a closed outline can be deleted"), `shape.segmentType {"index":0,"segment":1,"type":"straight|curved"}`.
  The first parameter is `index` (the subpath), not `path`; `segment` is the vertex ending the segment. Act on the selected shape or pass `id`.
- `slide.reuseList {"path":"deck.deckcraft"}` → `{name,slides:[{index,title,hidden}]}`: preview which slides `slide.reuse {"path","slides":[…],"at"?}` can bring in.
- `review.reject {"index"|"all":true}` only works while a Compare is in progress ("not comparing" otherwise).

## Newer commands

Six newer commands (`shape.openPath/closePath/deleteSegment/segmentType`, `slide.reuseList`, `review.reject`). The full-deck recipe
(select chart → `chart.options`, accessibility check, `.pptx` round trip with a hidden slide) is covered in "Building a real deck".

Three newer commands (headless, checked in the saved file):
- `slide.selectRange {"from"?,"to","add"?}` → `{selected:[slideIds]}`; commands that act on the selected slides then apply to all of them: `slide.hide {"hidden":true}` after `selectRange {"from":1,"to":2}` hid both.
- `format.languageAll {"lang":"fr-FR","noProof"?}` sets the proofing language of every text (slides, tables, notes, masters, layouts, default for new text; one undo step): the `.pptx` slide XML then carries `lang="fr-FR"`.
- `text.deleteSurrounding {"before":2,"after":0,"bytes"?}` acts on text being edited: `text.edit {"id":261}` (caret at the end), `text.deleteSurrounding {"before":2}`, `text.insert {"text":"!"}` turned "Hello" into "Hel!" → `{deleted}`.

## 0.13 changes (2026-10-31; only the first and last bullets were run, the rest are read from `commands`)
- **Run:** `table.cellAlign {"anchor","align"}`: `align` (left|center|right|justify) now sets the horizontal alignment of every paragraph in the cells; the saved `.pptx` gets `<a:pPr algn="ctr"/>` in each cell.
- **Help text only:** `slide.move {"ids":[slide id…],"to"}` takes slide ids as well as `from`; `to` counts without the moved slides. `format.numbering {"start":n}` starts a new run of numbers at `n`.
- **Help text only:** `shape.fill {"background":true}` lets the slide background show through a shape or text box; `shape.effects {"shadowProps":{"size":…}}` takes a shadow size.
- **Help text only:** `review.compare` now answers with `number` (the editor's slide number) and `onlyIn: "deck"|"file"`; `review.accept` takes the file's side. `insert.dateTime` fills the date placeholder of a Handout or Notes Master.
- **Run:** rendering changed slightly: the same sample deck's PDF pages differ from 0.12.0 in anti-aliasing and in lighter chart gridlines (maximum channel difference 63 of 255, layout identical). `presentation.json` differs only in the `generator` string.

## 0.14 changes (verified headless 2026-11-01; `.pptx` XML checked)
- **Motion paths from points:** `animation.add {"effect":"customPath","class":"path","path":[[0,0],[200,0],[200,-100]],"closed"?:true,"start","duration"}` → `{count,path:"M 0 0 L 0.208333 0 L 0.208333 -0.185185 E"}`. Points are slide points as **offsets from where the shape sits** (negative y = up); they are stored as fractions of the 960×540 slide, and `closed:true` adds `Z`. The OOXML string form works too (`"path":"M 0 0 L 0.1 0.1 L 0.2 0 E"`, fractions, as `animation.get` shows it). `animation.set {…,"path","ids"}` and `animation.options {"index","path"}` take the same `path`/`closed` to replace or re-shape a path. Saved to `.pptx` as `<p:animMotion path="…" pathEditMode="relative">` and read back unchanged after reopening the `.pptx`. The motion itself only plays in a show (not visible in `render`).
- **`slide.actions {"index"?}`** → `{index,slideId,actions:[{event,type,target,owner,hyperlink}]}` lists links without following them: `event` is `click` or `hover` (shape actions from `shape.action`) or `textLink` (a text-run link, with `owner.paragraphIndex`, also inside table cells); `type` is `slide` (target = the slide's **id**, not its index) or `url`. `insert.hyperlink {"url","text"}` right after `insert.textBox` came back as a shape `click` on the text box. All four kinds survived a `.pptx` round trip. A slide without links → `actions: []`.

## 0.15 changes (verified headless 2026-11-02; `.pptx` XML checked, slide rendered and looked at)
- **More gradient kinds:** `shape.fill {"gradient":{"stops":[[0,"#1F3864"],[1,"#FFFFFF"]],"kind":"radial|rectangular|path","focus":[l,t,r,b],"rotateWithShape":true}}`. `focus` (fractions) is where the first stop sits: `[0.5,0.5,0.5,0.5]` is the centre, `[0,0,1,1]` the top-left corner. Saved as `<a:path path="circle|rect|shape">` with `<a:fillToRect>` (×100000) and `rotWithShape="1"`. Rendered: radial is a centred glow, rectangular from `[0,0,1,1]` fades out of the top-left corner, `path` on an ellipse follows its outline. Linear keeps `angle`.
- No ids added or removed; the 23-deck re-run (188 outputs) was identical between 0.14.1 and 0.15.0.
