# Data merge, table of contents, index and books

> **Versions:** DesignCraft 0.17.2 (Linux AppImage, `designcraft-cli`), 2026-11-05, headless unless stated.

## Data merge from a CSV

```
file.new {"units":"points","width":396,"height":612,"pages":1,"margins":45,"title":"Merge Template"}
style.paragraph.create {"name":"Card","para":{"align":"left","spaceAfter":6},"chars":{"size":14,"leading":{"kind":"points","value":20}}}
frame.create {"rect":[45,45,351,320],"content":"text","text":"Specimen card\n\nItem: \nCode: \nUnits: \nNote: "}
data.source.select {"path":"/scratch/…"}
data.fields {}
data.placeholder.add {"field":"Note","story":"$2.story","at":43}
data.placeholder.add {"field":"Units","story":"$2.story","at":36}
data.placeholder.add {"field":"Code","story":"$2.story","at":28}
data.placeholder.add {"field":"Item","story":"$2.story","at":21}
text.select {"story":"$2.story","anchor":0,"focus":99999}
style.paragraph.apply {"name":"Card"}
story.get {"story":"$2.story"}
document.inspect {}
```

1. **`at` defaults to 0 when `story` is given.** `data.placeholder.add {field, story}` inserts the
   `<<Field>>` marker at byte 0 — every field stacked at the start, in reverse order, and the
   merge output read `<<Note>><<Units>><<Code>><<Item>>…`. **Always pass `at`** (byte offset).
2. **Insert placeholders last-to-first** so earlier offsets remain valid (the marker is
   inserted, growing the story; the engine shifts *existing placeholders*, not your numbers).
3. **Fields are literal `<<Name>>` markers in the story** — `story.get` shows them, and typing
   `"Item: <<Item>>"` straight into `frame.create` merges too (verified: `Item: Amber tile
   literal marker test`). The *command* is still preferable: it registers the field, and
   `data.fields` then reports `uses`.
4. **Text placeholders go in a story; image/qr ones bind to a frame** (`item:` or a selected
   frame), and a text field on a frame errors with *"say which role to use on this frame"*.
5. **`records`/`range`/`perPage`** control the merge: `range "1-3"` picked the 3 rows;
   `perPage:1` put one record per page (3 pages).
6. `spread` was removed and now **errors** (it used to append to the template).
7. `data.source.select` accepts inline `bytes`/`base64` too — no file needed for a quick test.

## Table of contents

```
file.new {"units":"points","width":396,"height":612,"pages":4,"facingPages":false,"margins":45,"title":"TOC Handbook"}
style.paragraph.create {"name":"Title","para":{"align":"left","spaceAfter":18},"chars":{"size":28,"leading":{"kind":"points","value":32}}}
style.paragraph.create {"name":"Head","para":{"align":"left","spaceBefore":8,"spaceAfter":8},"chars":{"size":20,"leading":{"kind":"points","value":24}}}
style.paragraph.create {"name":"Body","para":{"align":"left","hyphenate":true},"chars":{"size":10.5,"leading":{"kind":"points","value":14}}}
frame.create {"spread":0,"rect":[45,45,351,110],"content":"text","text":"A neutral handbook"}
text.select {"story":"$4.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Title"}
frame.create {"spread":1,"rect":[45,45,351,100],"content":"text","text":"Section One"}
text.select {"story":"$7.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Head"}
frame.create {"spread":1,"rect":[45,110,351,300],"content":"text","text":"Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
text.select {"story":"$10.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Body"}
frame.create {"spread":2,"rect":[45,45,351,100],"content":"text","text":"Section Two"}
text.select {"story":"$13.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Head"}
frame.create {"spread":2,"rect":[45,110,351,300],"content":"text","text":"Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
text.select {"story":"$16.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Body"}
frame.create {"spread":3,"rect":[45,45,351,100],"content":"text","text":"Section Three"}
text.select {"story":"$19.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Head"}
frame.create {"spread":3,"rect":[45,110,351,300],"content":"text","text":"Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
text.select {"story":"$22.story","anchor":0,"focus":9999}
style.paragraph.apply {"name":"Body"}
toc.entries {"styles":["Head"]}
toc.generate {"styles":["Head"],"page":1,"rect":[45,300,351,560],"title":"Contents","pageNumbers":true,"createBookmarks":true}
toc.entries {"styles":["Head"]}
toc.update {}
document.inspect {}
```

## Book (chapters, pagination, one PDF)

```
file.open {"path":"/scratch/…"}
book.new {"path":"/scratch/…"}
book.add {"path":"/scratch/…"}
book.add {"path":"/scratch/…"}
book.list {}
file.close {"index":1}
book.paginate {}
book.list {}
book.exportPdf {"path":"/scratch/…"}
```

## Index

```
file.open {"path":"/scratch/…"}
text.select {"story":16,"anchor":0,"focus":11}
index.addReference {"topic":"Sections > One"}
text.select {"story":18,"anchor":0,"focus":11}
index.addReference {"topic":"Sections > Two"}
index.list {}
index.generate {"title":"Index","page":1,"rect":[45,400,351,560]}
index.list {}
document.inspect {}
```

1. **`frame.create` has no `page`** — the parameter is `spread` (an index into spreads), so put each
   frame with `"spread":N`. `toc.generate`/`index.generate` *do* take a 1-based `page`.
2. **`facingPages` is not added by default? No — it defaults to `true`.** Omit it and a 4-page doc
   is 3 spreads (1 | 2-3 | 4); user "spread":3 then fails *"no such spread"*, and content lands on
   the wrong pages. Pass `"facingPages":false` explicitly (verified: 2 pages → facing False, 2 spreads).
3. **`book.paginate` refuses while a chapter is open**: *"chapter … is open; close it before
   updating the book"*. `file.close {"index":1}` first (index comes from `file.open`'s return).
4. `book.add` **both links and opens** a document — after adding chapters the list is complete, but
   pagination needs them closed.
5. TOC placeholders are real text (`Section One\t2`); the tab separates entry and page number,
   and `toc.update` reflows them, so don't type into that tab.
6. Index topics are hierarchical with `" > "` (`"Sections > One"`); `index.generate` writes a
   section heading letter ("S") when `sectionHeadings:true` (default).
