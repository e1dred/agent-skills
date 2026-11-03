# DeckCraft reference: command sweep

Part of the deckcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## The last 28 command ids (2026-10-26, headless; smoke test)
> Each id ran with `deckcraft-cli run --cmd … --save` on a slide holding the objects it needs; `info` of the saved file differed from the same script without the command (`info` also reflects the current slide, so a difference proves little for the navigation commands). **Smoke test only: effects were not rendered.**
- **Ran (26):**

```
arrange.bringForward arrange.flipHorizontal arrange.flipVertical arrange.rotateLeft arrange.sendBackward edit.cut
edit.pasteText file.adopt format.justify format.outdent format.subscript review.endCompare review.replaceWord
selection.showAll shape.addPoint shape.deletePoint shape.moveHandle shape.pointType shape.setDefault slide.last
slide.next slide.previous smartArt.demote smartArt.removeNode table.insertColumnRight text.commit
```
- **Setups:** shapes for the `arrange.*` and `shape.setDefault` commands (`shape.insert {"preset":"rect","rect":[x,y,w,h],"text"}` twice; they act on the selected shapes); `insert.textBox` + `text.edit {"at":[0,0]}` + `text.selectAll` for `format.justify|outdent|subscript`, `edit.pasteText {"text"}`, `review.replaceWord {"with"}`, `text.commit {"text"}`; `shape.freeform {"points":[…],"closed":true}` + `shape.editPoints {"on":true}` for `shape.addPoint {"path":0,"segment":1,"t":0.5}`, `shape.deletePoint {"path":0,"index":1}`, `shape.pointType {"path":0,"index":1,"type":"smooth"}`; **`shape.moveHandle {"path":0,"index":1,"side":"out","x","y"}` needs the point to be smooth first** ("that side of the point has no handle"); `insert.smartArt {"kind":"list","items":["A","\tB","C"]}` for `smartArt.demote {"index":2}` and `smartArt.removeNode {"index":1}`; three slides + `slide.first` for `slide.next|previous|last`; `insert.table` for `table.insertColumnRight {"col":0}`; **`review.endCompare` needs a running compare** (`review.compare {"path":other.deckcraft}` first; "not comparing" otherwise); `edit.cut {}` (scope slides optional), `file.adopt {"path"}` opens a file like `file.open`.
- **Refused:** `file.recovery.discard` (no recovery folder is set); `file.recovery.save` (no recovery folder is set) (an app setting, not a parameter: the desktop app sets a recovery folder).
