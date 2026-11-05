# DesignCraft command catalogue (0.17.2) — 547 ids

Generated from `designcraft-cli commands` and this round's headless run (0.17.2, 2026-11-05). Status per id: **verified** = the same field read before/after (document.inspect, type.selectionAttrs, transform.info or the family read-back named in the evidence); **read-ok** = a list/get/export returned real data; **ran** = accepted, no readable field changed (UI-only, view, effects not exposed by inspect); **refused** = the exact error is quoted. The params column is the first part of the command's own parameter doc (run `designcraft-cli commands` for the full text).

Totals: 262 verified, 139 read-ok, 141 ran, 5 refused (three rows downgraded from verified after review: `edit.undo`, `file.openIdml`, `file.openBytes`).

## file (37)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `file.new` | verified | {preset?: "Letter"\|"A4"\|… or a saved preset (file.savePreset), intent?: print\|web\|mobile, units?: points\|picas\|millimeters\|…, width?, hei… | inspect.settings.pageHeight: 792.0 -> 841.8897637795277 |
| `file.newSample` | verified | {} — a multi-page magazine sample | inspect.characterStyles[1]: "<absent>" -> "Emphasis" |
| `file.presets` | read-ok | {} → the built-in presets [{name, intent, width, height, units}], then the saved ones (with `saved: true`) | [{"height": 792.0, "intent": "print", "name": "Letter", "units": "picas", "width": 612.0}, {"height": 1008.0, "intent": "print", "name": "Legal", "units": "picas", "width": 612.0}, {"height": 1224.0,  |
| `file.savePreset` | ran | {name, …the settings as file.new} — kept with the preferences; `file.new {preset: name}` uses it. A saved preset of that name is replaced… | accepted; no readable field changed |
| `file.deletePreset` | ran | {name} — a saved document preset | accepted; no readable field changed |
| `file.open` | read-ok | {path} — a DesignCraft or IDML file (recognised by its content, so the extension may be missing), or an InDesign .indd/.indt (recognised … | {"documentFonts": 0, "index": 2, "warnings": []} |
| `file.openBytes` | ran | {name, base64} — DesignCraft JSON, an IDML package or an InDesign .indd/.indt → {index, warnings} | opened; only the title differs (a re-opened copy, not a change) |
| `file.openRecent` | read-ok | {index} — reopen entry `index` of File › Open Recent (as file.open); a file that is gone is an error and stays listed | {"documentFonts": 0, "index": 2, "warnings": []} |
| `file.recentFiles` | read-ok | {} → [{path, name, exists}] File › Open Recent, most recent first | [{"exists": true, "name": "base.designcraft", "path": "/scratch/out/base.designcraft"}] |
| `file.clearRecent` | ran | {} — empty File › Open Recent | accepted; no readable field changed |
| `file.save` | read-ok | {path?} — a `path` without the .designcraft extension gets it → {path: the file written, bytes} | out/exp/sample.designcraft 889463B written; document path set |
| `file.saveAs` | read-ok | {path} — a path without the .designcraft extension gets it → {path: the file written, bytes} | writes a copy and changes the document path (path field changes) |
| `file.saveACopy` | read-ok | {path} — writes the document without changing which file it is or its unsaved state; a path without the .designcraft extension gets it → … | writes a copy without changing the document's path/unsaved state |
| `file.revert` | verified | {} — back to the last saved version (not undoable) | inspect.spreads[0].items[0].bounds[0]: 60.0 -> "<absent>" |
| `file.recovery.list` | ran | {dir?} → [{uid, path, title, saved}] unsaved documents left by a crash (default: the session's recovery folder) | accepted; no readable field changed |
| `file.recovery.save` | read-ok | {dir?} — write every unsaved document to the recovery folder (the app does this on a timer) | {"saved": 0} |
| `file.recovery.open` | ran | {dir?} — reopen documents left in the recovery folder (unsaved) | accepted; no readable field changed |
| `file.serialize` | read-ok | {} → {base64, bytes} the .designcraft file | {"base64": "UEsDBAoAAAAAAAAAIQAnYSB5HwAAAB8AAAAIAAAAbWltZXR5cGVhcHBsaWNhdGlvbi92bmQuZGVzaWduY3JhZnQremlwUEsDBBQAAAAIAAAAIQDg/YjOQQAAAEUAAAAJAAAAbWV0YS5qc29uq1ZKyy/KTSxRslJKSS3OTM9LLkpMK1HSUUpPzUstSizJ |
| `file.close` | ran | {index?} | closed the document; the next blank document becomes active (pageCount 3->1) |
| `file.activate` | ran | {index} | switched to document 0; read-back shows the other document |
| `file.place` | ran | {path?\|base64?, name?, frame?: id (place into), spread?, x?, y?, width?: finite number > 0 (null: absent), height? (video/audio), pdfPage… | accepted; no readable field changed |
| `file.info` | ran | {documentTitle?, author?, description?, keywords?: ["a", "b"] \| "a; b", copyrightNotice?, copyrightInfoUrl?}: each field given replaces t… | file.info stores metadata; read it with file.info.get (that row verifies the fields) |
| `file.info.get` | ran | {} → the file info, without changing the document | accepted; no readable field changed |
| `file.exportIdml` | read-ok | {path?, embedImages?: true} — writes an IDML package to `path`, or returns {base64} without a path | sample.idml 557808B; reopened via --in: 4 pages, 18 stories, 15 paragraph styles |
| `file.openIdml` | ran | {path \| base64, name?} — opens an IDML package, or an InDesign document or template (.indd, .indt: converted to IDML first; its conversio… | opened an exported IDML; only ids/title differ (a re-opened copy, not a change) |
| `file.exportPdf` | read-ok | {path?, pages?: "1-3,5" \| [1,3] (1-based positions: "1" is the first page, which ui.render and app.export take as page 0; default all), f… | plain 552943B/4pp; PDF/X-4 1008119B validate=valid; PDF/X-1a 634491B validate=valid; PDF/A-2b 556502B (validate-pdf only checks PDF/X) |
| `file.exportEpub` | read-ok | {path?, title?, author?, language?: "en", identifier?: str (dc:identifier; a stable urn:uuid by default), coverImage?: path (a PNG or JPE… | sample.epub 826536B; zip with mimetype application/epub+zip, 8 entries |
| `file.exportFixedEpub` | read-ok | {path?, title?, author?, language?} — pre-paginated EPUB → {path, bytes} (no path: {base64, bytes}) | fixed.epub 2372447B, 4 pages; 12 zip entries (page1.xhtml...) |
| `file.printBooklet` | read-ok | {path?, type?: saddleStitch\|twoUpConsecutive, spaceBetween? (pt)} — printer spreads as PDF (pages imposed in booklet order) → {path, byte… | booklet.pdf exported (printer spreads) |
| `file.exportHtml` | read-ok | {path?, title?, language?} — one self-contained page (styles inline, images embedded), stories and graphics in reading order → {path, byt… | sample.html 1108370B; starts '<!DOCTYPE html> <html lang="en">' |
| `file.exportPptx` | read-ok | {path?, pages?: "1-3,5" \| [1,3] (1-based positions; default all), lineBreaks?: keep\|reflow (keep: DesignCraft's lines, spacing and leadin… | sample.pptx 1698553B; 4 slide parts in the zip |
| `file.exportText` | read-ok | {path?, format?: "txt"\|"rtf"\|"tagged" (Tagged Text; default from the path, else txt), story?, frame?} — the story being edited or of the … | sample.txt 29B 'Export me. Second paragraph.'; rtf 199B; tagged 113B (needs a text frame selected) |
| `file.exportXml` | read-ok | {path?} — the tagged content in reading order → {path, bytes} (no path: {text}) | tagged.xml 116B '<ProbeStory>Tagged paragraph.</ProbeStory>' after xml.tag on the frame; xml.tagText alone left <Root/> empty |
| `file.importXml` | read-ok | {path \| text} — each element's content goes into the next text frame with that tag (child elements of mapped tags become paragraphs in th… | {"placed": 0, "unmatched": 1} |
| `file.package` | read-ok | {dir: folder to create, idml?: true, pdf?: false\|true\|{…options of file.exportPdf}, instructions?: text} — the document (its placed files… | package folder written with document + links |
| `file.printers` | read-ok | {} → {printers: [names], default} | {"default": null, "printers": ["Virtual_PDF"]} |
| `file.print` | refused | {printer?, copies?: 1, pages?: "1-3,5", dryRun?: bool (export and preview submission without printing), …the PDF settings of file.exportP… | invalid parameters for `file.print`: lp: Error - No default destination. |

## snippet (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `snippet.export` | read-ok | {path?} — the selected items (with their stories, styles and images) as a .designcraft snippet; no path: {base64} | {"base64": "UEsDBAoAAAAAAAAAIQAnYSB5HwAAAB8AAAAIAAAAbWltZXR5cGVhcHBsaWNhdGlvbi92bmQuZGVzaWduY3JhZnQremlwUEsDBBQAAAAIAAAAIQDg/YjOQQAAAEUAAAAJAAAAbWV0YS5qc29uq1ZKyy/KTSxRslJKSS3OTM9LLkpMK1HSUUpPzUstSizJ |
| `snippet.place` | verified | {path \| base64, spread?, x?, y?} — items keep their positions unless x/y given (top-left) | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 100.0 |

## place (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `place.styles` | ran | {path \| base64, name} → {paragraph: [name], character: [name], conflicts: [name]} — the styles a Word/RTF file brings (for styleMap / sty… | accepted; no readable field changed |
| `place.load` | ran | {path \| base64, name?} — load a graphic into the place cursor (then click/drag with the placeGun tool) | only loads the place cursor (canUndo flips); nothing placed until a click |
| `place.drop` | verified | {spread?, x, y, rect?: [x0,y0,x1,y1], frame?: id} | inspect.spreads[0].items[0].asset: "<absent>" -> 11 |

## document (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `document.epubSplit` | read-ok | {split?: "off"\|"exportTags"\|{style: name}} — EPUB Export Options › Split Document, stored with the document: one content file (off, the d… | {"split": "off"} |
| `document.preferences` | read-ok | {horizontalUnits?, verticalUnits?: points\|picas\|inches\|millimeters\|…, keyboardIncrement? (pt), kerningIncrement? (1/1000 em: Alt+Left/Rig… | {"advancedType": {"subscriptPosition": 33.3, "subscriptSize": 58.3, "superscriptPosition": 33.3, "superscriptSize": 58.3}, "baselineGrid": {"color": [140, 205, 230], "increment": 12.0, "relativeTo": " |
| `document.inspect` | read-ok | {} → pages, spreads, items, stories (with overset), styles, swatches, selection | {"activeLayer": 1, "canUndo": false, "characterStyles": ["[None]"], "dirty": false, "layers": [{"color": [43, 155, 255], "id": 1, "locked": false, "name": "Layer 1", "printable": true, "showGuides": t |
| `document.list` | read-ok | {} | [{"active": false, "dirty": false, "index": 0, "title": "Untitled-1"}, {"active": true, "dirty": false, "index": 1, "title": "Probe"}] |
| `document.history` | ran | {} | accepted; no readable field changed |

## edit (18)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `edit.undo` | ran | {} | undo after a selection: only the selection read-back changed (not proof of an undone edit) |
| `edit.redo` | verified | {} | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 80.0 |
| `edit.selectAll` | ran | {} — all items on the active spreads, or all text in the story | accepted; no readable field changed |
| `edit.deselectAll` | verified | {} | attrs.characterStyle: "[None]" -> "<absent>" |
| `edit.clear` | verified | {ids?} — delete selected items (or the selected text, points or ruler guides) | inspect.stories[0].length: 76 -> 0 |
| `edit.copy` | read-ok | {} → {text} when text is selected (with formatting, footnotes, markers) | {"text": "Alpha beta gamma. Delta epsilon zeta.\nEta theta iota kappa. Lambda mu nu xi."} |
| `edit.cut` | verified | {} | inspect.stories[0].length: 76 -> 0 |
| `edit.pasteWithoutFormatting` | verified | {text?} — plain text at the insertion point, in the format there | inspect.stories[0].length: 76 -> 152 |
| `edit.paste` | verified | {inPlace?: bool, spread?: index (0), text?: the system clipboard's text (pastes it unless it is what was copied here; with no insertion p… | inspect.stories[0].length: 76 -> 152 |
| `edit.pasteInto` | verified | {id?} — the copied objects become the content of the selected frame (or `id`), clipped by it | inspect.spreads[0].items[0].children[0].bounds[0]: "<absent>" -> 60.0 |
| `edit.pasteInPlace` | verified | {spread?: index (0)} | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 60.0 |
| `edit.duplicate` | verified | {} | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 72.0 |
| `edit.preview` | ran | {label, command, params?} — run `command` on the document as it was before the preview began, replacing the last preview; the first call … | accepted; no readable field changed |
| `edit.commitPreview` | ran | {} — the open preview becomes one undo step | accepted; no readable field changed |
| `edit.cancelPreview` | ran | {} — the document goes back to how it was before the preview | accepted; no readable field changed |
| `edit.pasteSvg` | verified | {svg: markup (what Illustrator, VectorCraft or Figma put on the clipboard), spread?, at?: [x, y] (spread coords of the art's centre; defa… | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 268.5 |
| `edit.stepAndRepeat` | verified | {count?: 1..1000, dx?, dy?, rows?, columns?, ids?} — copies of the selection (or ids) offset by (dx, dy); with rows/columns, a grid of at… | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 72.0 |
| `edit.transparencyBlendSpace` | ran | {space: cmyk\|rgb} — the colour space transparency is composited in for output | accepted; no readable field changed |

## selection (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `selection.set` | verified | {ids: [id], add?: bool, content?: bool, anchors?: [[id, subpath, index]] (Direct Selection: the selected anchor points; their paths are s… | inspect.selection.items[1]: 12 -> "<absent>" |
| `selection.toggle` | verified | {id} | inspect.selection.items[1]: 12 -> "<absent>" |
| `selection.key` | verified | {id} — make a selected item the key object for Align; the current key object drops the key | inspect.selection.key: "<absent>" -> 11 |

## endnote (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `endnote.insert` | verified | {text?} — a reference at the insertion point; the first one makes the endnote frame on a new last page → {story, id, frame} | readback[0].id: "<absent>" -> 1 |
| `endnote.edit` | verified | {story, id, text} | readback[0].text: "An endnote." -> "Changed endnote." |
| `endnote.delete` | verified | {story, id} — removes the reference and its text | readback[0].id: 1 -> "<absent>" |
| `endnote.list` | ran | {} → [{story, id, number, text}] in numbering order | accepted; no readable field changed |
| `endnote.options` | read-ok | {style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|kanji, startAt?, prefix?, suffix?, heading?, headingStyle?, paraStyle?, s… | {"heading": "Endnotes", "headingStyle": "[Basic Paragraph]", "paraStyle": "[Basic Paragraph]", "prefix": "", "separator": "\t", "startAt": 1, "style": "arabic", "suffix": ""} |

## note (9)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `note.new` | verified | {text, author?} — at the insertion point → {story, id} | readback[0].at: "<absent>" -> 76 |
| `note.convertFromText` | verified | {author?} → {story, id}. The selected text moves into a new note anchored where it was. | readback[0].at: "<absent>" -> 0 |
| `note.edit` | verified | {story, id, text?, author?} | readback[0].text: "A note." -> "Changed note." |
| `note.delete` | verified | {story, id} | readback[0].at: 76 -> "<absent>" |
| `note.convertToText` | verified | {story, id} — the note's text replaces its anchor | readback[0].at: 76 -> "<absent>" |
| `note.split` | verified | {story, id, at} → {story, id}. The note's text from byte `at` on moves into a new note anchored right after it. | readback[0].text: "A note." -> "A not" |
| `note.list` | ran | {} → [{story, id, at, author, text}] in story order | accepted; no readable field changed |
| `note.previous` | verified | {} → {story, id, pos}. The caret moves after the anchor of the story's previous note. | inspect.selection.text.anchor: 71 -> 63 |
| `note.next` | verified | {} → {story, id, pos}. The caret moves after the anchor of the story's next note. | inspect.selection.text.anchor: 0 -> 79 |

## frame (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `frame.create` | verified | {spread?: index \| {kind: doc\|parent, index} (a parent spread: index into `parents` of document.inspect), rect: [x0,y0,x1,y1] (spread coor… | inspect.spreads[0].items[0].bounds[0]: "<absent>" -> 100.0 |
| `frame.grid` | verified | {rect, cols, rows, gutter? (pt, 12), shape?, content?, spread?} — a grid of frames filling `rect` (frame tools: arrow keys while dragging) | inspect.spreads[0].items[0].bounds[0]: "<absent>" -> 40.0 |

## line (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `line.create` | verified | {spread?, a: [x,y], b: [x,y]} | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 100.0 |

## transform (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `transform.move` | verified | {dx, dy, copy?: bool, ids?, toSpread?, content?: bool (move the placed graphic or pasted-in items inside each frame; the frame stays. Def… | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 85.0 |
| `transform.resize` | verified | {from: rect, to: rect, content?: bool (scale content), distribute?: bool (Live Distribute: objects keep their size, their centres spread … | inspect.spreads[0].items[0].bounds[2]: 220.0 -> 260.0 |
| `transform.rotate` | verified | {angle (degrees, CCW), ref?: 0..8 (reference point of the selection bounds, default 4: centre), ids?} | transform.rotation: -0.0 -> 15.0 |
| `transform.scale` | verified | {sx, sy, ids?} (about the selection centre) | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 52.0 |
| `transform.again` | verified | {individually?: bool, sequence?: bool, ids?} — repeat the last transform (or the whole sequence applied to this selection), on the select… | inspect.spreads[0].items[0].bounds[0]: 80.0 -> 100.0 |
| `transform.clear` | ran | {ids?} — remove rotation, shear and scaling (the object keeps its centre) | accepted; no readable field changed |
| `transform.shear` | verified | {angle (degrees), ref?: 0..8 (reference point of the selection bounds, default 4: centre), ids?} | transform.shear: 0.0 -> 10.0 |
| `transform.flip` | verified | {axis: horizontal\|vertical, ref?: 0..8 (reference point of the selection bounds, default 4: centre), ids?} | transform.rotation: -0.0 -> 180.0 |
| `transform.set` | verified | {x?, y? (measured from the rulers' zero point, view.zeroPoint), width?, height?, scaleX? (%), scaleY? (%), rotation? (°), shear? (°), ref… | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 100.0 |
| `transform.info` | read-ok | {ids?} → {scaleX, scaleY (%), rotation, shear (°), content?: the same for a placed graphic} of the first target | {"rotation": -0.0, "scaleX": 100.0, "scaleY": 100.0, "shear": 0.0} |

## object (60)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `object.matchAttributes` | ran | {from: id, ids?} — copy fill, stroke, corners, opacity, effects, wrap | accepted; no readable field changed |
| `object.arrange` | verified | {to: front\|forward\|backward\|back, ids?} | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 260.0 |
| `object.bringToFront` | verified | {} | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 260.0 |
| `object.bringForward` | verified | {} | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 260.0 |
| `object.sendBackward` | verified | {} | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 260.0 |
| `object.sendToBack` | verified | {} | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 260.0 |
| `object.group` | verified | {ids?} | inspect.spreads[0].items[0].bounds[2]: 220.0 -> 420.0 |
| `object.ungroup` | verified | {ids?} | inspect.spreads[0].items[0].bounds[2]: 420.0 -> 220.0 |
| `object.lock` | verified | {ids?} | inspect.spreads[0].items[0].locked: false -> true |
| `object.unlockAll` | ran | {} | accepted; no readable field changed |
| `object.hide` | verified | {ids?} | inspect.spreads[0].items[0].hidden: false -> true |
| `object.showAll` | ran | {} | accepted; no readable field changed |
| `object.setFlags` | ran | {ids: [id], hidden?: bool, locked?: bool} — Layers panel eye/lock per object | accepted; no readable field changed |
| `object.fill` | verified | {swatch? (a swatch's name, e.g. [Paper]), tint?: 0..1, ids?} — at least one; a tint alone keeps each object's own swatch (the Swatches pa… | inspect.spreads[0].items[0].fill: "[None]" -> "[Paper]" |
| `object.swapFillStroke` | ran | {ids?} — each object's fill and stroke colours (and tints) trade places; locked objects stay as they are. With nothing selected: those of… | accepted; no readable field changed |
| `object.defaultFillStroke` | verified | {ids?} — no fill and a black stroke; locked objects stay as they are. With nothing selected: for new shapes | inspect.spreads[0].items[0].stroke.swatch: "[None]" -> "[Black]" |
| `object.stroke` | verified | {swatch?, tint?, weight?, align?: center\|inside\|outside, type?: {kind: solid\|dashed\|dotted\|thickThin\|thinThick\|thinThin\|thickThick\|thinTh… | inspect.spreads[0].items[0].stroke.swatch: "[None]" -> "[Black]" |
| `object.opacity` | ran | {opacity: 0..1, blend?: normal\|multiply\|…, ids?} | accepted; no readable field changed |
| `object.dropShadow` | ran | {on?: bool, distance?, angle?, globalLight?: bool, opacity?, size?, spread? (%), color? (swatch), mode?: blend mode (multiply…), ids?} | accepted; no readable field changed |
| `object.innerShadow` | ran | {on?: bool, distance?, angle?, globalLight?: bool, opacity?, size?, choke? (%), color?, mode?: blend mode, ids?} | accepted; no readable field changed |
| `object.outerGlow` | ran | {on?: bool, opacity?, size?, spread? (%), color?, mode?: blend mode (screen…), ids?} | accepted; no readable field changed |
| `object.exportOptions` | read-ok | {ids?, artifact?: bool (tagged PDF decoration), rasterize?: bool (EPUB/HTML image), align?: left\|center\|right\|"", pageBreakBefore?: bool,… | {"objects": 1} |
| `object.innerGlow` | ran | {on?: bool, opacity?, size?, choke? (%), center?: bool (glow from the centre), color?, ids?} | accepted; no readable field changed |
| `object.bevel` | ran | {on?: bool, size?, depth? (%), angle?, globalLight?: bool, highlight?, highlightOpacity?, shadow?, shadowOpacity?, ids?} | accepted; no readable field changed |
| `object.satin` | ran | {on?: bool, opacity?, angle?, distance?, size?, invert?: bool, color?, ids?} | accepted; no readable field changed |
| `object.directionalFeather` | ran | {on?: bool, widths?: [top, left, bottom, right] \| number, ids?} | accepted; no readable field changed |
| `object.effects` | ran | {effects?: {dropShadow?: {on?, color?, opacity?, angle?, globalLight?, distance?, size?, spread?}, innerShadow?, outerGlow?, innerGlow? {… | accepted; no readable field changed |
| `object.feather` | ran | {width (0 = off), ids?} | accepted; no readable field changed |
| `object.content` | verified | {type: graphic\|text\|unassigned, ids?} | attrs.characterStyle: "<absent>" -> "[None]" |
| `object.textFrameOptions` | ran | {columns?, gutter?, inset?: number\|[t,l,b,r] (null keeps that side), verticalJustification?: top\|center\|bottom\|justify, paragraphSpacingL… | accepted; no readable field changed |
| `object.cornerOptions` | ran | {shape: none\|rounded\|inverseRounded\|inset\|bevel\|fancy, size, corners?: [{shape, size} \| null] (4 entries in path order: top-left, top-rig… | accepted; no readable field changed |
| `object.textWrap` | ran | {mode?: none\|boundingBox\|contour\|jumpObject\|jumpToNextColumn (boundingBox when absent, unless side or contour is given; null or those: ea… | accepted; no readable field changed |
| `object.fit` | ran | {mode: fillProportionally (preserves aspect ratio, covers frame, clips overflow)\|fitProportionally (preserves aspect ratio, shows whole i… | accepted; no readable field changed |
| `object.fittingOptions` | ran | {autoFit?: bool, fitting?: none\|fillProportionally\|fitProportionally\|fitContentToFrame\|centerContent, align?: 0..8 (reference point, 4 = … | accepted; no readable field changed |
| `object.clearFittingOptions` | ran | {ids?} — the frames' fitting options back to the defaults: no auto-fit, no crop amounts, the centre reference point; the content stays wh… | accepted; no readable field changed |
| `object.rename` | verified | {id \| ids?, name} | inspect.spreads[0].items[0].name: "" -> "ProbeObject" |
| `object.align` | verified | {edge: left\|hcenter\|right\|top\|vcenter\|bottom, to?: selection\|keyObject\|margins\|page\|spread (default: keyObject while a key object is set)… | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 0.0 |
| `object.distribute` | ran | {axis: horizontal\|vertical, by?: centers\|spacing, spacing?: points, ids?} | accepted; no readable field changed |
| `object.clippingPath` | verified | {type?: alpha\|edges (default alpha), threshold?: 0–255 (alpha: opaque above; edges: darker than 255 − threshold counts; default 25), tole… | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 35.0 |
| `object.clippingPathOptions` | read-ok | {type?: none, invert?: bool, includeInsideEdges?: bool, ids?} — without type, invert or includeInsideEdges, reports each selected graphic… | {"items": [{"id": 11, "type": "none"}]} |
| `object.primaryTextFrame` | read-ok | {on?: bool (default: toggle), ids?} — the selected text frame's story becomes the primary story (Smart Text Reflow adds and removes pages… | {"primary": true, "story": 12} |
| `object.attributes` | ran | {overprintFill?, overprintStroke?, overprintGap?, nonprinting?: bool, ids?} — Attributes panel | accepted; no readable field changed |
| `object.globalLight` | ran | {angle} — the light angle shared by shadows that use Global Light | accepted; no readable field changed |
| `object.label` | ran | {label, ids?} — free text scripts and agents can find objects by | accepted; no readable field changed |
| `object.altText` | ran | {text, ids?} — alternative text for tagged PDF and EPUB | accepted; no readable field changed |
| `object.transparencyGroup` | ran | {isolate?: bool, knockout?: bool, ids?} — Effects panel: Isolate Blending, Knockout Group | accepted; no readable field changed |
| `object.findByLabel` | read-ok | {label} → ids of objects whose label is `label` | {"ids": [11]} |
| `object.setLayer` | ran | {layer, ids?} — a group member moves its whole top-level group | accepted; no readable field changed |
| `object.reorder` | verified | {ids?, above?: id \| below?: id \| index?: n (0 = top of the layer), layer?} — moves the objects (siblings on one spread) in the stacking o… | inspect.spreads[0].items[0].bounds[0]: 60.0 -> 260.0 |
| `object.makeCompoundPath` | verified | {ids?} — one path from the selected paths (the backmost object's look); paths inside others become holes → {id} | inspect.spreads[0].items[0].bounds[2]: 180.0 -> 340.0 |
| `object.releaseCompoundPath` | read-ok | {ids?} — each subpath becomes its own object → {ids} | {"ids": [11]} |
| `object.pathfinder` | verified | {op: add\|subtract\|intersect\|exclude\|minusBack, ids?} — combine the selected shapes into one, which keeps the frontmost object's look and … | inspect.spreads[0].items[0].bounds[2]: 220.0 -> 420.0 |
| `object.gradientFeather` | ran | {on?: true, radial?, angle?, start?: opacity 0–100 (100), end?: (0), from?: [x,y], to?: [x,y] (spread coords: the Gradient Feather tool's… | accepted; no readable field changed |
| `object.caption` | verified | {text?: template (default "{name}"; variables {name} {path} {altText} {label} {ppi} {dimensions} {format}), position?: below\|above\|left\|r… | attrs.characterStyle: "<absent>" -> "[None]" |
| `object.pdfLayers` | ran | {id?} → [{name, visible, default}] — the layers of the selected placed PDF | accepted; no readable field changed |
| `object.layerOptions` | ran | {ids?, hidden: [layer name], useDefaults?: bool} — hide layers; useDefaults:false makes [] explicitly all on; legacy [] restores file def… | accepted; no readable field changed |
| `object.qrCode` | verified | {type?: url\|text\|sms\|email\|vcard (default url), content (url/text), number?, message?, to?, subject?, body?, name?, phone?, email?, org?,… | inspect.spreads[0].items[0].children[0].bounds[0]: "<absent>" -> 88.27586206896552 |
| `object.convertShape` | verified | {to: rectangle\|roundedRectangle\|beveledRectangle\|inverseRoundedRectangle\|ellipse\|triangle\|polygon\|line\|orthogonalLine\|openPath\|closedPath… | inspect.spreads[0].items[0].kind: "<rectangle>" -> "<ellipse>" |
| `object.gradient` | verified | {kind?: linear\|radial, stops?: [{location: 0–100, color: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b](0..255)\|{model: rgb\|cmyk\|gray, …}(0..1) \| sw… | inspect.spreads[0].items[0].fill: "[None]" -> "Gradient" |
| `object.color` | verified | {color: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b](0..255)\|{model: rgb\|cmyk\|gray, r,g,b\|c,m,y,k\|k}(0..1), target?: fill\|stroke, text?: bool, ids… | inspect.spreads[0].items[0].fill: "[None]" -> "R=51 G=102 B=153" |

## path (15)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `path.create` | verified | {spread?, anchors: [{p:[x,y], in?:[x,y], out?:[x,y]}], closed?: bool} | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 100.0 |
| `path.appendAnchor` | verified | {id, anchor: {p, in?, out?} (spread coords), subpath?: index (default the last), at?: end\|start (default end)} — after the subpath's last… | inspect.spreads[0].items[0].bounds[2]: 200.0 -> 300.0 |
| `path.setAnchor` | verified | {id, subpath?: index (default the last), anchor: index\|"first"\|"last", p?, in?, out? (spread coords)} — moves an anchor or its direction … | inspect.spreads[0].items[0].bounds[0]: 100.0 -> 110.0 |
| `path.reverse` | read-ok | {ids?, subpath?: index (only that subpath of the first target)} — the anchors run the other way (the end point becomes the start) | {"reversed": 1} |
| `path.close` | ran | {id, subpath?: index (default every subpath)} | accepted; no readable field changed |
| `path.moveAnchors` | ran | {id, anchors: [[subpath, index]], dx, dy, handle?: in\|out} \| {points: [[id, subpath, index, dx?, dy?]], dx?, dy?} (anchors of several pat… | accepted; no readable field changed |
| `path.addAnchor` | read-ok | {id, at: [x,y] (spread coords; the nearest point on the path), tolerance?: pt (default 4)} → {subpath, anchor} | {"anchor": 1, "subpath": 0} |
| `path.deleteAnchor` | verified | {id, subpath, anchor} — removes the point (and the object when no path is left) | inspect.spreads[0].items[0].bounds[2]: 200.0 -> 150.0 |
| `path.convertAnchor` | read-ok | {id, subpath, anchor, to?: [x,y] (spread coords: drag out symmetric handles to there), corner?: bool} — without `to`, a smooth point beco… | {"kind": "smooth"} |
| `path.erase` | read-ok | {id, points: [[x,y], …] (spread coords: the Erase tool's drag), tolerance?: pt (default 4)} — removes the stretch of path the drag ran along | {"subpaths": 2} |
| `path.smooth` | read-ok | {id, points: [[x,y], …] (spread coords), tolerance?: pt (default 4)} — re-fits the stretch the drag ran along with fewer, smoother anchors | {"subpaths": 1} |
| `path.join` | verified | {ids?} — one open path: closes it; two open paths: joins them where their ends are nearest (coincident ends become one point) into the fi… | inspect.spreads[0].items[0].bounds[2]: 180.0 -> 340.0 |
| `path.deletePoints` | verified | {points?: [[id, subpath, index]]} — the Direct Selection tool's selected points by default, in one undo step (Properties › Quick Actions … | inspect.spreads[0].items[0].bounds[2]: 200.0 -> 150.0 |
| `path.convertPoints` | read-ok | {kind: plain\|corner\|smooth\|symmetrical, ids?} — the Direct Selection tool's selected points, or every point of the selected paths: plain … | {"converted": 4} |
| `path.split` | verified | {id, at: [x,y] (spread coords; the nearest point on the path)} — Scissors: an open path becomes two, a closed one opens there → {ids} | inspect.spreads[0].items[0].bounds[2]: 250.0 -> 200.0 |

## tool (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `tool.polygonSettings` | read-ok | {sides?: 3–100, starInset?: 0–100 (%)} → the settings new polygons use | {"sides": 6, "starInset": 0.0} |
| `tool.select` | read-ok | {tool: selection\|directSelection\|type\|rectangleFrame\|…} | {"tool": "selection"} |
| `tool.list` | read-ok | {} | [[{"icon": "tool-selection", "id": "selection", "label": "Selection Tool", "shortcut": "V"}], [{"icon": "tool-direct", "id": "directSelection", "label": "Direct Selection Tool", "shortcut": "A"}], [{" |

## gap (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `gap.move` | verified | {at: [x, y] (spread), delta?: pt \| dx? \| dy?: a drag (the part along the gap's axis counts), spread?} — Gap tool: the gap at `at` between… | inspect.spreads[0].items[0].bounds[2]: 220.0 -> 230.0 |

## article (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `article.list` | read-ok | {} → [{name, items, export}] | [{"export": true, "items": [], "name": "ProbeArticle"}] |
| `article.new` | verified | {name?, ids? (default: the selection)} → {name} | readback[0].export: "<absent>" -> true |
| `article.add` | verified | {name, ids? (default: the selection)} — appended in order | readback[0].items[0]: "<absent>" -> 11 |
| `article.remove` | verified | {name, ids} | readback[0].items[0]: 11 -> "<absent>" |
| `article.options` | ran | {name, to?: new name, export?: bool, order?: [ids] (reorder)} | accepted; no readable field changed |
| `article.delete` | verified | {name} | readback[0].export: true -> "<absent>" |

## type (43)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `type.createOutlines` | verified | {ids?} — text frames become compound paths of their glyphs (one per line and text colour, grouped when several, so Ungroup separates the … | attrs.characterStyle: "[None]" -> "<absent>" |
| `type.onPath` | verified | {id: path, text?, start?: distance along the path, flip?, align?: baseline\|ascender\|descender\|center} → {story} — the text cursor goes in… | attrs.characterStyle: "<absent>" -> "[None]" |
| `type.pathOptions` | read-ok | {id?, start?, end?: distance along the path or null (the path's end), flip?, align?: baseline\|ascender\|descender\|center, delete?: true (D… | {"align": "baseline", "end": null, "flip": false, "start": 10.0} |
| `type.pickUpFormat` | read-ok | {frame, point} — the Eyedropper with text selected: the character and paragraph formatting (styles and overrides) of the text under the p… | {"paragraphStyle": "[Basic Paragraph]", "style": "[None]"} |
| `type.fillWithPlaceholder` | verified | {frame?, story?} | inspect.stories[0].length: 76 -> 565 |
| `type.char` | verified | {attrs: {fontFamily?, fontStyle?, size?, leading?: {kind:auto}\|{kind:points,value}, tracking?, kerning?, hScale?, vScale?, baselineShift?… | attrs.chars.size: 12.0 -> 18.0 |
| `type.kernPair` | verified | {kerning: {kind: metrics\|optical\|none}\|{kind: manual, value: 1/1000 em}\|null} — at a caret in text, the pair at the caret (the character … | attrs.chars.kerning.kind: "metrics" -> "manual" |
| `type.para` | verified | {attrs: {align?, leftIndent?, firstLineIndent?, spaceBefore?, spaceAfter?, dropCapLines?, dropCapChars?, dropCapStyle?, dropCapAlignLeft?… | attrs.para.spaceBefore: 0.0 -> 6.0 |
| `type.align` | verified | {align: left\|center\|right\|leftJustified\|…} | attrs.para.align: "left" -> "center" |
| `type.alignLeft` | ran | {} | accepted; no readable field changed |
| `type.alignCenter` | verified | {} | attrs.para.align: "left" -> "center" |
| `type.alignRight` | verified | {} | attrs.para.align: "left" -> "right" |
| `type.justify` | verified | {} | attrs.para.align: "left" -> "leftJustified" |
| `type.bold` | verified | {on?: bool} — the family's bold style, keeping italic (style linking); toggles when `on` is left out | attrs.chars.fontStyle: "Regular" -> "Bold" |
| `type.italic` | verified | {on?: bool} — the family's italic style, keeping the weight (style linking); toggles when `on` is left out | attrs.chars.fontStyle: "Regular" -> "Italic" |
| `type.swapFillStroke` | verified | {} — swap each selected character's resolved fill/stroke and tints; at a caret, swap the next typing's colors | attrs.chars.fill: "[Black]" -> "[None]" |
| `type.underline` | verified | {} | attrs.chars.underline: false -> true |
| `type.allCaps` | verified | {} | attrs.chars.capitalization: "normal" -> "allCaps" |
| `type.tateChuYoko` | verified | {on?: bool} — set the selected text horizontally within one em of a vertical line (toggles by default) | attrs.chars.tateChuYoko: false -> true |
| `type.ruby` | verified | {text?, type?: group\|perCharacter, alignment?: left\|center\|right\|fullJustify\|jis\|equalAki\|oneAki, position?: aboveRight\|belowLeft, xOffse… | attrs.chars.ruby: "" -> "ruby" |
| `type.kenten` | verified | {on?: bool, kind?: sesameDot\|whiteSesameDot\|fisheye\|blackCircle\|smallBlackCircle\|bullseye\|blackTriangle\|whiteTriangle\|whiteCircle\|smallWh… | attrs.chars.kenten: false -> true |
| `type.shatai` | verified | {magnification?: % (0 = off), angle?: degrees, adjustRotation?: bool, adjustTsume?: bool} — slant the selected characters by compressing … | attrs.chars.shataiMagnification: 0.0 -> 50.0 |
| `type.autoTateChuYoko` | verified | {digits?: 0..10 (0 = off), includeRoman?: bool} — in vertical text, set runs of up to `digits` half-width digits (and roman letters) acro… | attrs.para.autoTcy: 0 -> 2 |
| `type.gridSettings` | verified | {alignment?: none\|romanBaseline\|emTop\|emCenter\|emBottom\|icfTop\|icfBottom, firstLineOnly?: bool, gyoudori?: 0..100 (0 = auto), paragraphGy… | attrs.para.gridAlign: "none" -> "allLines" |
| `type.rotateRoman` | verified | {on?: bool} — half-width characters stand upright in vertical text, for the selected paragraphs (toggles by default) | attrs.para.rotateRoman: false -> true |
| `type.romanWordBreak` | verified | {on?: bool} — roman words in the selected paragraphs may break between any two letters, without a hyphen (toggles by default) | attrs.para.romanWordBreak: false -> true |
| `type.warichu` | verified | {on?: bool, lines?: int, size?: number, lineSpacing?: number, align?: auto\|left\|center\|right\|justify, charsBeforeBreak?: int, charsAfterB… | attrs.chars.warichu: false -> true |
| `type.storyDirection` | verified | {vertical: bool} — the stories of the text selection or the selected frames: vertical lines run top to bottom and follow each other right… | inspect.stories[0].lines: 2 -> 4 |
| `type.kernStep` | verified | {steps?: n (default 1; negative tightens), amount?: 1/1000 em (in place of steps × the document's kerningIncrement)} — with a caret, the … | attrs.chars.tracking: 0.0 -> 20.0 |
| `type.sizeUp` | verified | {} | attrs.chars.size: 12.0 -> 14.0 |
| `type.sizeDown` | verified | {} | attrs.chars.size: 12.0 -> 10.0 |
| `type.changeCase` | verified | {case: upper\|lower\|title\|sentence} — the selected text, or the stories of selected frames (formatting kept) | inspect.stories[0].preview: "Alpha beta gamma. Delta epsilon zeta.\nEta theta iota kappa. Lambda mu nu xi." -> "ALPHA BETA GAMMA. DELTA EPSILON ZETA.\nETA THETA IOTA KAPPA. LAMBDA MU NU XI." |
| `type.openType` | read-ok | {feature?: dlig\|frac\|ordn\|swsh\|titl\|calt\|zero\|ssNN\|any tag, on?: bool (default: toggle), figures?: tabularLining\|proportionalOldstyle\|pro… | {"features": [], "figures": "default"} |
| `type.selectionAttrs` | read-ok | {mixed?: bool} → resolved character/paragraph attributes at the text selection; `ownChars`: what the text has of its own over its paragra… | {"charOverrides": 0, "characterStyle": "[None]", "characterStyleOverrides": 0, "chars": {"allowKashidas": true, "baselineShift": 0.0, "capitalization": "normal", "change": "none", "characterAlignment" |
| `type.openTypeFeatures` | read-ok | {} → the OpenType features and stylistic sets the selected text's fonts offer, each with its applied and available state (none, some or a… | {"features": [{"applied": "none", "available": "all", "tag": "aalt"}, {"applied": "none", "available": "all", "tag": "c2sc"}, {"applied": "none", "available": "all", "tag": "case"}, {"applied": "none" |
| `type.feature` | ran | {features: {tag: true\|false, …}} — turns OpenType features on or off across the selected text, keeping each run's other features | accepted; no readable field changed |
| `type.tabs.get` | read-ok | {style?} → {tabs, leftIndent, firstLineIndent, rightIndent, width, frame?, column?: [x0,y0,x1,y1] (frame inner space)} — the first select… | {"column": [36.0, 36.0, 320.0, 240.0], "firstLineIndent": 0.0, "frame": 11, "leftIndent": 0.0, "rightIndent": 0.0, "tabs": [], "width": 284.0} |
| `type.tabs.add` | verified | {position (pt from the column's left edge), align?: left\|center\|right\|char, leader? (≤ 8 characters), alignOn? (one character), style?} →… | attrs.para.tabs[0].align: "<absent>" -> "left" |
| `type.tabs.move` | verified | {index, position, style?} → {index, tabs} | attrs.para.tabs[0].position: 120.0 -> 150.0 |
| `type.tabs.change` | verified | {index, align?: left\|center\|right\|char, leader?, alignOn?, style?} → {index, tabs} | attrs.para.tabs[0].align: "left" -> "center" |
| `type.tabs.remove` | verified | {index, style?} → {tabs} | attrs.para.tabs[0].align: "left" -> "<absent>" |
| `type.tabs.clear` | ran | {style?} → {tabs} | accepted; no readable field changed |
| `type.tabs.repeat` | verified | {index, width?, style?} → {index, tabs} — repeats the distance from the previous stop (or the left indent) to this one up to the column w… | attrs.para.tabs[1].align: "<absent>" -> "left" |

## flex (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `flex.add` | verified | {ids?} — the selected objects (top level, one spread) in a new Flex Layout container where they are; aligned objects get that direction, … | inspect.spreads[0].items[0].children[0].bounds[0]: "<absent>" -> 60.0 |
| `flex.convert` | read-ok | {ids?} — a group (its objects) or a rectangle frame (with what is pasted into it) becomes a Flex Layout container → {id} | {"id": 11} |
| `flex.remove` | read-ok | {ids?} — the container goes; its objects stay where they are, grouped when there are several (a container with its own fill or stroke sta… | {"ids": [11]} |
| `flex.set` | ran | {ids?, direction?: row\|rowReverse\|column\|columnReverse, wrap?: bool, justify?: flexStart\|center\|flexEnd\|spaceBetween\|spaceAround\|spaceEve… | accepted; no readable field changed |
| `flex.reorder` | read-ok | {id (an object in a container), to?: index \| by?: ±n} — its place in the container's order → {index} | {"index": 1} |

## book (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `book.new` | verified | {path} — an empty book file (.dcbook) | readback.path: "/scratch/ou -> "/scratch/ou |
| `book.open` | read-ok | {path} → {documents} | {"documents": 0} |
| `book.close` | verified | {} | readback.command: "<absent>" -> "book.list" |
| `book.add` | verified | {path, at?: index} | readback.documents[1].firstPage: "<absent>" -> 4 |
| `book.remove` | verified | {index} | readback.documents[0].firstPage: 1 -> "<absent>" |
| `book.styleSource` | ran | {index} | accepted; no readable field changed |
| `book.list` | read-ok | {} → {path, styleSource, documents: [{path, pages, firstPage}]} | {"documents": [{"firstPage": 1, "pages": 3, "path": "/scratch/out/base.designcraft"}], "path": "/scratch/… |
| `book.paginate` | read-ok | {} — each document starts numbering where the previous one ended, and takes its chapter number (automatic: one more than the previous doc… | {"chapters": [], "pages": 0} |
| `book.syncStyles` | read-ok | {} — paragraph and character styles and swatches of the style source go into every document (by name) | {"synced": 0} |
| `book.exportPdf` | read-ok | {path?} — every document in order as one PDF → {path, bytes, pages} (no path: {base64, …}) | {"bytes": 3102, "pages": 3, "path": "/scratch/out/book.pdf"} |

## button (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `button.set` | read-ok | {ids?, action: page\|firstPage\|lastPage\|nextPage\|previousPage\|url\|none, page?, url?} — the selected objects act on release in interactive PDF | {"buttons": 1} |
| `button.clear` | read-ok | {ids?} | {"buttons": 1} |
| `button.list` | ran | {} → [{id, name, action}] | accepted; no readable field changed |

## form (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `form.set` | read-ok | {ids?, kind: textField\|checkBox\|comboBox\|listBox\|signature, name?, value?, options?: [string], multiline?, required?, fontSize?} — intera… | {"fields": 1} |
| `form.clear` | ran | {ids?} — no longer a form field | accepted; no readable field changed |
| `form.list` | ran | {} → [{id, kind, name, value, options}] | accepted; no readable field changed |

## color (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `color.settings` | read-ok | {rgb?: working RGB profile, cmyk?: working CMYK profile, intent?: perceptual\|relative\|saturation\|absolute, bpc?: bool} → {rgb, cmyk, inte… | {"bpc": true, "cmyk": "Coated FOGRA39 (fitted, craft-cms)", "intent": "relative", "profiles": [{"builtin": true, "kind": "rgb", "name": "sRGB IEC61966-2.1"}, {"builtin": true, "kind": "rgb", "name": " |
| `color.loadProfile` | refused | {path} — an ICC profile (.icc/.icm) to use as a working space or proof target | invalid parameters for `color.loadProfile`: invalid ICC profile: not an ICC profile (missing 'acsp' signature) |
| `color.convert` | read-ok | {color: {model: rgb, r, g, b} \| {model: cmyk, c, m, y, k} \| {model: gray, k}, to: rgb\|cmyk\|gray\|lab} — through the working spaces | {"c": 0.8424807786941528, "k": 0.012222002260386944, "m": 0.5661570429801941, "model": "cmyk", "y": 0.2000114470720291} |
| `color.extractTheme` | read-ok | {id?: selected image frame} → {from, colors: [up to five RGB hex colours]} — samples the source raster, ignoring transparent pixels; at m… | {"colors": ["#3e3e80", "#3ebd80", "#9e3e80", "#bebd80", "#de3e80"], "from": 11} |
| `color.sample` | verified | {at: [x,y] (spread coords), spread?, target?: fill\|stroke, ids?, matchFrom?: id} → {color: "#rrggbb", swatch, from: image id} — the Eyedr… | inspect.spreads[0].items[0].fill: "[None]" -> "R=69 G=63 B=128" |

## swatch (13)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `swatch.addColorTheme` | verified | {colors: [one to five RGB hex colours], name?: group name} → {name, swatches} — adds the previewed palette as one undoable swatch group | inspect.swatches[10]: "<absent>" -> "Color Theme 1" |
| `swatch.create` | verified | {name?, color: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b](0..255)\|{model: rgb\|cmyk\|gray, …}(0..1), spot?: bool} \| {name? ("New Gradient Swatch")… | inspect.swatches[10]: "<absent>" -> "ProbeSwatch" |
| `swatch.new` | verified | {swatch?: name, target?: fill\|stroke} → {name} — the Swatches panel's New Swatch: `swatch` (default: the selection's fill or stroke) as a… | inspect.swatches[10]: "<absent>" -> "[Paper] copy" |
| `swatch.load` | read-ok | {path?\|base64?, replace?: bool} — colour swatches from a swatch exchange (.ase) file; a name the file repeats gets a number ("Red 2") and… | {"added": 0, "replaced": 0} |
| `swatch.save` | read-ok | {path?, names?: [swatch names] (default: all colour swatches)} → {base64} or writes `path` (.ase) | {"base64": "QVNFRgABAAAAAAAGAAEAAAA8ABIAQwA9ADEAMAAwACAATQA9ADAAIABZAD0AMAAgAEsAPQAwAABDTVlLP4AAAAAAAAAAAAAAAAAAAAACAAEAAAA8ABIAQwA9ADAAIABNAD0AMQAwADAAIABZAD0AMAAgAEsAPQAwAABDTVlLAAAAAD+AAAAAAAAAAAAA |
| `swatch.addToSwatches` | read-ok | {swatch?: name (default: the selection's fill), target?: fill\|stroke, name?: new name} — makes an unnamed colour a swatch | {"name": "R=51 G=102 B=153"} |
| `swatch.options` | ran | {name, to?: new name, nameWithValue?: bool, color?: "#rrggbb"\|{c,m,y,k}(0..100)\|[r,g,b]\|{gray}(0..100), spot?: bool, tint?: 0–1 (tint swa… | accepted; no readable field changed |
| `swatch.addUnnamed` | read-ok | {} — every unnamed colour used becomes a swatch | {"added": 0} |
| `swatch.delete` | verified | {name} | inspect.swatches[10]: "ProbeSwatch" -> "<absent>" |
| `swatch.newColorGroup` | ran | {name?, swatches?: [names]} — a Swatches panel folder (the swatches move into it) → {name} | accepted; no readable field changed |
| `swatch.moveToGroup` | ran | {swatches: [names], group: name \| null (top level)} | accepted; no readable field changed |
| `swatch.ungroupColorGroup` | ran | {name} — its swatches go back to the top level | accepted; no readable field changed |
| `swatch.renameColorGroup` | ran | {name, to} | accepted; no readable field changed |

## changes (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `changes.track` | ran | {on?: bool (default: toggle)} | accepted; no readable field changed |
| `changes.list` | read-ok | {} → [{story, start, end, kind: inserted\|deleted, text}] | [{"end": 5, "kind": "deleted", "start": 0, "story": 12, "text": "Alpha"}, {"end": 13, "kind": "inserted", "start": 5, "story": 12, "text": "Changed "}] |
| `changes.accept` | verified | {story, start} — the change at that position | readback[0].end: 5 -> 8 |
| `changes.reject` | verified | {story, start} — the change at that position | readback[0].end: 5 -> 13 |
| `changes.acceptAll` | verified | {story?} — deleted text goes, added text stays | readback[0].end: 5 -> "<absent>" |
| `changes.rejectAll` | verified | {story?} — added text goes, deleted text comes back | readback[0].end: 5 -> "<absent>" |

## condition (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `condition.list` | ran | {} → [{name, color, visible}] | accepted; no readable field changed |
| `condition.new` | verified | {name, color?: [r, g, b], visible?} → {name} | readback[0].color[0]: "<absent>" -> 79 |
| `condition.options` | verified | {name, to?: new name, color?: [r, g, b], visible?: bool} | readback[0].visible: true -> false |
| `condition.delete` | verified | {name} — the text it was applied to stays (shown) | readback[0].color[0]: 79 -> "<absent>" |
| `condition.apply` | verified | {name, on?: bool (default true), only?: bool (remove the others)} — to the selected text; `name: null` with `only` removes all | attrs.charOverrides: 0 -> 1 |

## library (8)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `library.new` | ran | {path?} — an empty Object Library (saved to `path` when given) | accepted; no readable field changed |
| `library.open` | read-ok | {path \| json} → {items} | {"items": 0} |
| `library.list` | read-ok | {} → [{index, name, description}] | [{"description": "", "index": 0, "name": "rectangle"}] |
| `library.json` | read-ok | {} → the library as JSON text (to save where there's no file system) | {"json": "{\"items\":[{\"name\":\"rectangle\",\"description\":\"\",\"snippet\":\"UEsDBAoAAAAAAAAAIQAnYSB5HwAAAB8AAAAIAAAAbWltZXR5cGVhcHBsaWNhdGlvbi92bmQuZGVzaWduY3JhZnQremlwUEsDBBQAAAAIAAAAIQDg/YjOQQA |
| `library.add` | ran | {name?, description?} — the selection → {index} | accepted; no readable field changed |
| `library.place` | verified | {index, spread?, x?, y?} — at its original position unless x/y (top-left) are given | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 60.0 |
| `library.remove` | ran | {index} | accepted; no readable field changed |
| `library.close` | ran | {} | accepted; no readable field changed |

## conveyor (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `conveyor.collect` | read-ok | {ids? (default: the selection)} — each object onto the Content Collector conveyor → {count} | {"count": 2} |
| `conveyor.place` | verified | {index? (0), spread?, x?, y?, keep?: bool (stay on the conveyor)} — the Content Placer: the collected object at x/y (top-left) | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 60.0 |
| `conveyor.list` | ran | {} → [name] | accepted; no readable field changed |
| `conveyor.clear` | ran | {} | accepted; no readable field changed |

## list (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `list.bullets` | verified | {on?: bool (default: off when every selected paragraph has bullets, else on)} — the Bulleted List button: paragraphs with no indents get … | attrs.para.firstLineIndent: 0.0 -> -18.0 |
| `list.numbers` | verified | {on?: bool (default: off when every selected paragraph is numbered, else on)} — the Numbered List button, as list.bullets | attrs.para.firstLineIndent: 0.0 -> -18.0 |
| `list.define` | read-ok | {name, continueAcrossStories?: true, rename?} — paragraphs join it with type.para {listType: numbers, listName} | {"lists": [{"continueAcrossStories": true, "name": "ProbeList2"}]} |
| `list.delete` | ran | {name} | accepted; no readable field changed |

## story (9)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `story.placeAndLink` | verified | {story (parent), rect, spread?} — a new frame whose story copies the parent and stays linked → {id, story} | inspect.spreads[0].items[1].bounds[0]: "<absent>" -> 400.0 |
| `story.links` | ran | {} → [{story, parent, outOfDate}] | accepted; no readable field changed |
| `story.updateLink` | read-ok | {story? (default: every out-of-date linked story)} — the child takes the parent's current content (its own edits are replaced) | {"updated": 0} |
| `story.unlink` | ran | {story} | accepted; no readable field changed |
| `story.setDirection` | ran | {story?, frame?: a text frame of the story, direction: leftToRight\|rightToLeft} — column progression, independent of paragraph direction | accepted; no readable field changed |
| `story.options` | verified | {story?, frame?: a text frame of the story (default: the stories of the text selection or the selected frames), opticalMargin?: bool — Op… | attrs.storyOptions.opticalMargin: false -> true |
| `story.setText` | verified | {story, text} — replace a story's whole text | inspect.stories[0].length: 76 -> 20 |
| `story.replaceRange` | verified | {story, start, end, text} — replace a byte range keeping surrounding formatting | inspect.stories[0].length: 76 -> 78 |
| `story.get` | read-ok | {story? \| frame?} → text, frames, paragraphs, vertical, lines, overset (the UTF-8 byte offset into `text` where it stops fitting its fram… | {"direction": "leftToRight", "frames": [11], "id": 12, "length": 76, "lines": 2, "overset": null, "oversetChars": null, "paragraphs": 2, "text": "Alpha beta gamma. Delta epsilon zeta.\nEta theta iota  |

## math (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `math.insert` | verified | {latex, size?: points (12), x?, y?, spread?} or {id, latex, size?} — at the text insertion point (inline), else as a frame; with `id`: ed… | inspect.stories[0].length: 76 -> 79 |
| `math.svg` | read-ok | {latex, size?} → {svg, width, height} — typeset without placing | {"height": 25.896, "svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"10.12pt\" height=\"25.90pt\" viewBox=\"0 0 10.124 25.896\"><rect x=\"1.200\" y=\"12.588\" width=\"7.724\" height=\"0.720\"/ |

## media (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `media.options` | ran | {ids?, playOnPageLoad?, loop?, controls?, poster?: {path \| base64+name} \| null (placeholder)} — for placed video and sound | accepted; no readable field changed |
| `media.get` | read-ok | {id?} → {kind, name, playOnPageLoad, loop, controls, poster} | {"controls": true, "kind": "audio", "loop": false, "name": "test.wav", "playOnPageLoad": false, "poster": null} |

## liquid (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `liquid.pageRule` | read-ok | {rule: off\|scale\|reCenter\|guideBased\|objectBased\|controlledByParent (the parent page's rule), pages?: [1-based] (default: all)} | {"pages": 3} |
| `liquid.object` | read-ok | {ids?, resizeWidth?, resizeHeight?, pinTop?, pinBottom?, pinLeft?, pinRight?} — for object-based pages | {"objects": 2} |

## guide (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `guide.liquid` | ran | {spread?, page, index, on?: bool (default true)} | accepted; no readable field changed |
| `guide.add` | verified | {orientation: horizontal\|vertical, position (spread coordinate, at most 1000000 pt either way), spread?, page? (index in the spread; defa… | inspect.selection.guides[0].index: 0 -> 1 |
| `guide.move` | verified | {spread?, page, index, position (at most 1000000 pt either way)} | readback[0].position: 300.0 -> 120.0 |
| `guide.moveBy` | read-ok | {dx?, dy?, guides?: [{spread?, page, index}] (default: the selected guides)} — vertical guides move by dx, horizontal ones by dy, as one … | {"moved": 1} |
| `guide.delete` | verified | {spread?, page, index}, or {} for the selected guides; an address without page or index is an error | inspect.selection.guides[0].index: 0 -> "<absent>" |
| `guide.deleteAll` | verified | {spread?} | inspect.selection.guides[0].index: 0 -> "<absent>" |
| `guide.list` | read-ok | {spread?} → [{page, index, orientation, position, spread, selected}] | [{"index": 0, "orientation": "horizontal", "page": 0, "position": 300.0, "selected": true, "spread": false}] |
| `guide.select` | read-ok | {spread?, page, index, guides?: [{spread?, page, index}] (several, in place of page and index), add?: bool (keep the guides already selec… | {"selected": 1} |
| `guide.selectAll` | read-ok | {spread?} — every guide on the spread that is not locked or on a locked or hidden layer → {selected: n} | {"selected": 1} |
| `guide.deselect` | verified | {} | inspect.selection.guides[0].index: 0 -> "<absent>" |

## layout (28)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `layout.createAlternate` | verified | {name, width, height, rule?: page rule for the copies (default: keep each page's)} — every page copied after the last at the new size (a … | inspect.spreads[2].index: "<absent>" -> 2 |
| `layout.pages.insert` | verified | {count?: 1 (1 to 9999), after?: 0-based page index (default: the last page; past it: at the end), before?: 0-based page index (instead of… | inspect.spreads[2].index: "<absent>" -> 2 |
| `layout.rotateSpreadView` | read-ok | {spread?: index (0), angle: 90 (clockwise) \| -90 \| 180 \| 0 (clear)} — turn one spread on screen (output is unaffected) | {"rotation": 90} |
| `layout.pages.delete` | verified | {pages: [index]} | inspect.spreads[1].pages[1].bounds[0]: 612.0 -> "<absent>" |
| `layout.pages.move` | ran | {from, to} | accepted; no readable field changed |
| `layout.pages.duplicateSpread` | verified | {spread, atEnd?: bool (Duplicate Spread at End of Document; the Pages panel's New Page button takes a dropped page there), to?: page inde… | inspect.spreads[2].index: "<absent>" -> 2 |
| `layout.pages.applyParent` | ran | {pages: [index], parent: id\|"A-Parent"\|"A"\|null (null or "[None]" clears)} | accepted; no readable field changed |
| `layout.parents.new` | verified | {prefix?, name?: "Parent"} | inspect.parents[1].basedOn: "<absent>" -> null |
| `layout.parents.delete` | verified | {id: parent spread id} — unapply the parent and keep local overrides as ordinary items | inspect.parents[1].basedOn: null -> "<absent>" |
| `layout.parents.edit` | ran | {on?: bool, parent?: id\|"A-Parent"\|"A"} — show parent spreads on the canvas; `parent` shows that parent (and implies on). Turning on with… | accepted; no readable field changed |
| `layout.parents.options` | ran | {parent: id\|"B-Parent"\|"B", basedOn: id\|"A-Parent"\|"A"\|null (= [None])} — the parent shows its base's items under its own, and so do the … | accepted; no readable field changed |
| `layout.marginsAndColumns` | verified | {pages?: [index] (default all), margins?: number\|{top,bottom,inside,outside}, columns?, gutter?, adjustLayout?: bool (objects follow the … | inspect.spreads[1].pages[0].columnRects[0][0]: 36.0 -> 40.0 |
| `layout.moveColumnGuide` | verified | {spread?, parent? (a parent's prefix, label or index: its spread instead of `spread`), page (index in the spread), gutter (0 = between th… | inspect.spreads[0].pages[0].columnRects[0][2]: 300.0 -> 100.0 |
| `layout.documentSetup` | verified | {width?, height?, pages?: count, startPage?: n, facingPages?, binding?: leftToRight\|rightToLeft, intent?: print\|web\|mobile, margins?: n \|… | inspect.settings.facingPages: true -> false |
| `layout.pages.toSpread` | verified | {page (1-based), spread (0-based)} — the page joins that spread (up to 10 pages; the spread stops shuffling) | inspect.spreads[0].pages[0].bounds[0]: 0.0 -> 612.0 |
| `layout.spreadShuffle` | ran | {spread (0-based), allow: bool} — off keeps the spread's pages together when pages are added or removed | accepted; no readable field changed |
| `layout.pageSize` | verified | {pages: [1-based page numbers], width?, height?, preset?: "A4"\|"Letter"\|…, anchor?: 0–8 (reference point that stays put, row-major from t… | inspect.spreads[0].pages[0].bounds[2]: 612.0 -> 500.0 |
| `layout.parentPageSize` | refused | {parent: spread id, page: 0-based parent page index, width?, height?, anchor?: 0–8} — resize only this parent page, keeping document page… | invalid parameters for `layout.parentPageSize`: no such parent page |
| `layout.selectParentPage` | refused | {parent: spread id\|null, page?: 0-based parent page index} — select a parent page with the Page tool; null clears the selection | invalid parameters for `layout.selectParentPage`: no such parent page |
| `layout.pageOptions` | ran | {pages: [1-based], showParentOverlay?: bool} — Page tool options (Show Parent Page Overlay: the parent page's size drawn over the page) | accepted; no readable field changed |
| `layout.selectPage` | verified | {page: 1-based \| null, ids?: [item ids] (objects selected with it: the Page tool on an object-based page)} — the page the Page tool selec… | inspect.selection.page: "<absent>" -> 0 |
| `layout.section` | verified | {page (1-based; starts a section there), startNumber?: n (1–99999)\|null (continue), style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|low… | inspect.spreads[0].pages[0].name: "1" -> "i" |
| `layout.chapterNumbering` | read-ok | {style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|arabicLeadingZero\|arabicThreeDigits\|arabicFourDigits, start?: n (Start Ch… | {"book": null, "chapterNumber": 1, "label": "1", "source": "userDefined", "style": "arabic"} |
| `layout.numberingOptions` | verified | {page, …the settings as layout.section, chapter?: {…the settings as layout.chapterNumbering}} — the section and the document's chapter nu… | inspect.spreads[0].pages[0].name: "1" -> "i" |
| `layout.overrideParentItems` | ran | {page (0-based), ids?: parent items (default: all on the page's parent page)} → {ids} the page's editable copies | accepted; no readable field changed |
| `layout.removeOverrides` | read-ok | {page (0-based)} — deletes the page's overridden copies; the parent items show again | {"removed": 0} |
| `layout.detachAll` | read-ok | {page (0-based)} — the page's overridden copies become ordinary items | {"detached": 0} |
| `layout.createGuides` | read-ok | {rows?: 0..1000, columns?: 0..1000, rowGutter?: 12, columnGutter?: 12, fitTo?: margins\|page, removeExisting?: false, spread?, page? (inde… | {"guides": 4} |

## xml (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `xml.tags` | read-ok | {} → {root, tags: [{name, color}], styleMap: [[style, tag]], dtd: bool} | {"dtd": false, "root": "Root", "styleMap": [], "tags": [{"color": [230, 120, 40], "name": "ProbeTag"}]} |
| `xml.newTag` | verified | {name, color?: [r, g, b]} | readback.tags[1].color[0]: "<absent>" -> 60 |
| `xml.deleteTag` | verified | {name} — tagged objects are untagged | readback.tags[0].color[0]: 230 -> "<absent>" |
| `xml.tagText` | verified | {tag \| null (untag)} — the selected text becomes an inline element | readback.tags[0].color[0]: "<absent>" -> 230 |
| `xml.tag` | verified | {tag (made if new), ids? (default: the selection)} — `tag: null` untags | readback.tags[0].color[0]: "<absent>" -> 230 |
| `xml.mapStyle` | verified | {style: paragraph style, tag \| null} — that style's paragraphs export as `<tag>` elements and import back with it | readback.styleMap[0][0]: "<absent>" -> "ProbePara" |
| `xml.structure` | read-ok | {} → {root, elements: [{tag, id, kind, text?}]} in reading order | {"elements": [], "root": "Root"} |
| `xml.loadDtd` | verified | {path \| text} — keep the DTD for validation and add a tag for each declared element; the root takes the first element's name unless alrea… | readback.dtd: false -> true |
| `xml.deleteDtd` | verified | {} | readback.dtd: true -> false |
| `xml.validate` | read-ok | {} — check the structure (as exported) against the loaded DTD → {valid, problems: [{path, message}]} | {"problems": [], "valid": true} |

## strokeStyle (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `strokeStyle.list` | ran | {} → [{name, kind}] | accepted; no readable field changed |
| `strokeStyle.new` | verified | {name, type: stripes\|dash\|dot, bands?: [[start, width] (fractions of the weight)], pattern?: [dash, gap, …] (pt)} — apply with object.str… | readback[0].kind.kind: "<absent>" -> "dashed" |
| `strokeStyle.delete` | verified | {name} — strokes using it become solid | readback[0].kind.kind: "dashed" -> "<absent>" |

## script (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `script.run` | read-ok | {text} — command script lines (`command.id {json}`, JSON lines or a JSON array; `$N.path` refers to earlier results) → {results, steps} | {"results": [{"activeLayer": 1, "canUndo": false, "characterStyles": ["[None]"], "dirty": false, "layers": [{"color": [43, 155, 255], "id": 1, "locked": false, "name": "Layer 1", "printable": true, "s |

## states (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `states.create` | read-ok | {ids? (default: the selection; one group's objects or several objects become states)} → {id, states} | {"id": 13, "states": ["State 1", "State 2"]} |
| `states.list` | read-ok | {id?} → {states, active} | {"active": 0, "states": ["State 1", "State 2"]} |
| `states.show` | verified | {id?, index? \| name?} | readback.active: 0 -> 1 |
| `states.rename` | verified | {id?, index, name} | readback.states[0]: "State 1" -> "State Two" |
| `states.release` | verified | {id?} — back to a plain group (every state shows) | readback.states[0]: "State 1" -> "<absent>" |

## page (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `page.transition` | read-ok | {pages?: [1-based] \| spread? \| all?: bool, kind: blinds\|box\|comb\|cover\|dissolve\|fade\|push\|split\|uncover\|wipe\|zoomIn\|zoomOut\|none, duratio… | {"spreads": 2} |
| `page.transitions` | ran | {} → [{spread, kind, duration, horizontal}] | accepted; no readable field changed |

## select (8)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `select.firstAbove` | verified | {} — the frontmost object on the spread (layers included) | inspect.selection.items[0]: 11 -> 12 |
| `select.nextAbove` | verified | {} | inspect.selection.items[0]: 11 -> 12 |
| `select.nextBelow` | verified | {} | inspect.selection.items[1]: 12 -> "<absent>" |
| `select.lastBelow` | verified | {} — the backmost object on the spread | inspect.selection.items[1]: 12 -> "<absent>" |
| `select.container` | ran | {} — the group or frame holding the selection | accepted; no readable field changed |
| `select.content` | ran | {} — the graphic in a frame, or the first object in a group | accepted; no readable field changed |
| `select.nextInGroup` | ran | {} | accepted; no readable field changed |
| `select.previousInGroup` | ran | {} | accepted; no readable field changed |

## links (7)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `links.copyTo` | verified | {dir, assets?: [asset ids] (default: all)} — write the placed files to `dir` and relink to the copies → {copied} | readback[0].path: "/scratch/te -> "/scratch/ |
| `links.list` | read-ok | {} → [{asset, name, path, status: ok\|modified\|missing\|embedded, refused?: why a missing link isn't followed (a path on another computer, … | [{"asset": 12, "name": "test.png", "path": "/scratch/test.png", "pdfCrop": null, "pixels": [240, 160], "refused": null, "s |
| `links.relink` | read-ok | {asset \| story, path} — use another file for every placement of the graphic (keeps the selected PDF page; error if missing), or import an… | {"name": "test.png"} |
| `links.relinkFolder` | read-ok | {dir?: folder to look in (default: each link's own folder), extension?: e.g. "tif" (Relink File Extension), assets?: [ids], missingOnly?:… | {"notFound": [], "relinked": 0} |
| `links.update` | read-ok | {asset? \| story?} — reload modified links from their files (all when neither); a linked text file is imported again into its story with t… | {"updated": 0} |
| `links.embed` | verified | {asset \| story} — keep only the copy in the document (a text file: unlink the story) | readback[0].path: "/scratch/te -> null |
| `links.goTo` | read-ok | {asset \| story} — selects the frames showing the graphic or the linked text | {"ids": [11]} |

## text (17)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `text.placeCaret` | verified | {frame, point: [x,y] (spread coords)} — converts empty frames to text frames | inspect.selection.text.anchor: 76 -> 6 |
| `text.release` | ran | {frame, point, moved: bool, copy?: bool} — ends a press in text: a drag that started in the selected text moves (copy: duplicates) it to … | accepted; no readable field changed |
| `text.extendTo` | verified | {frame, point, unit?: word\|line\|paragraph\|story} — moves the selection's focus to the point; with `unit`, after a text.selectAt, the sele… | inspect.selection.text.focus: 76 -> 19 |
| `text.selectWord` | verified | {frame, point} — the word (or run of spaces) under the point | inspect.selection.text.anchor: 76 -> 5 |
| `text.selectAt` | verified | {frame, point, unit: word\|line\|paragraph\|story} — what a double, triple, quadruple or quintuple click selects: the word (or run of spaces… | inspect.selection.text.anchor: 76 -> 5 |
| `text.selectSentence` | verified | {frame, point} — the sentence under the point | inspect.selection.text.anchor: 76 -> 0 |
| `text.selectParagraph` | verified | {frame, point} — the paragraph under the point, without its paragraph return | inspect.selection.text.anchor: 76 -> 0 |
| `text.selectStory` | verified | {frame, point} — all the text of the story under the point, threaded frames included | inspect.selection.text.anchor: 76 -> 0 |
| `text.select` | verified | {story, anchor, focus} (UTF-8 byte offsets into the story text, as find.find reports them: á or — counts 2 or 3) | inspect.selection.text.anchor: 76 -> 0 |
| `text.insert` | verified | {text, raw?: bool (no typographer's quotes)} — replaces the selected text | inspect.stories[0].length: 76 -> 89 |
| `text.deleteSurrounding` | verified | {before?: int, after?: int, bytes?: bool, commit?: string} — removes the text around the selection (an input method's delete-surrounding)… | inspect.stories[0].length: 76 -> 75 |
| `text.delete` | verified | {forward?: bool, word?: bool} | inspect.stories[0].length: 76 -> 75 |
| `text.move` | read-ok | {dir: left\|right\|up\|down\|lineStart\|lineEnd\|storyStart\|storyEnd, extend?, word?} | {"pos": 76} |
| `text.exitToFrame` | verified | {} | inspect.selection.items[0]: "<absent>" -> 11 |
| `text.thread` | verified | {from?, to?, rect?: [x0,y0,x1,y1] (spread coords), spread?, autoflow?: bool} — threads frame `to` right after frame `from` (between `from… | inspect.spreads[0].items[1].story: 14 -> 16 |
| `text.unthread` | verified | {frame?, side?: after\|before} — breaks the thread after (or before) `frame` (default: the selected text frame). The frames from the break… | inspect.spreads[0].items[1].story: 12 -> 15 |
| `text.removeFromThread` | verified | {frame?} — takes `frame` (default: the selected text frame) out of its thread: the frames before and after it join up and keep the text, … | inspect.spreads[0].items[0].story: 12 -> 15 |

## style (28)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `style.breakLink` | verified | {kind: paragraph\|character} — the selected text keeps its look as local formatting, with [No Paragraph Style] / [None] | attrs.paragraphStyle: "[Basic Paragraph]" -> "[No Paragraph Style]" |
| `style.compositeFont.list` | ran | {} → composite font definitions | accepted; no readable field changed |
| `style.compositeFont.set` | ran | {name, entries: [{name?, characters?, family, style?, relativeSize?, horizontalScale?, verticalScale?, baselineShift?, scaleOption?}]} — … | accepted; no readable field changed |
| `style.exportTag` | read-ok | {style, character?: bool, tag?: p\|h1…h6\|blockquote\|pre\|li\|… (span\|em\|strong\|code\|sup\|sub… for characters; "" = automatic), class?, split?… | {"class": "", "tag": "p"} |
| `style.paragraph.apply` | verified | {name, clearOverrides?: bool} | attrs.paragraphStyle: "[Basic Paragraph]" -> "ProbePara" |
| `style.character.apply` | verified | {name} | attrs.characterStyle: "[None]" -> "ProbeChar" |
| `style.paragraph.redefine` | ran | {name?} — incorporate the first selected paragraph/character's local formatting into its paragraph style; retain character styles; one un… | accepted; no readable field changed |
| `style.character.redefine` | ran | {name?} — incorporate the first selected character's local formatting into its character style without capturing paragraph attributes; on… | accepted; no readable field changed |
| `style.paragraph.create` | verified | {name, basedOn?, nextStyle?, para?: {paragraph attributes, as type.para names them: align, leftIndent, firstLineIndent, spaceBefore, spac… | inspect.paragraphStyles[3]: "<absent>" -> "ProbeParaNew" |
| `style.paragraph.edit` | verified | {name, rename?, basedOn?, nextStyle?: style \| null ([Same style]), resetToBase?: bool (Reset To Base: the style sets nothing of its own; … | inspect.paragraphStyles[2]: "ProbePara" -> "ProbePara2" |
| `style.paragraph.delete` | verified | {name, replaceWith?} | inspect.paragraphStyles[2]: "ProbePara" -> "<absent>" |
| `style.character.create` | verified | {name, basedOn?: style \| "[None]", chars?: {character attributes, as type.char names them: fontFamily, fontStyle, size, leading, tracking… | inspect.characterStyles[2]: "<absent>" -> "ProbeCharNew" |
| `style.character.edit` | verified | {name, rename?, basedOn?: style \| "[None]" \| null, chars?: {character attribute (as type.char names them: fontFamily, fontStyle, size, …)… | inspect.characterStyles[1]: "ProbeChar" -> "ProbeChar2" |
| `style.character.delete` | verified | {name, replaceWith?} | inspect.characterStyles[1]: "ProbeChar" -> "<absent>" |
| `style.list` | read-ok | {} → paragraph and character style names | {"cell": ["[None]"], "character": ["[None]", "ProbeChar"], "object": ["[None]", "[Basic Graphics Frame]", "[Basic Text Frame]", "ProbeObj"], "paragraph": ["[No Paragraph Style]", "[Basic Paragraph]",  |
| `style.object.apply` | ran | {name, ids?} — sets the style's fill, stroke, effects and text frame options on the items | accepted; no readable field changed |
| `style.object.create` | verified | {name, fromSelection?: true (fill, stroke, effects and text frame options of the first selected item), fill?, paragraphStyle?, effects?: … | readback.object[4]: "<absent>" -> "ProbeObjNew" |
| `style.object.edit` | read-ok | {name, effects?: {…} \| null (the style no longer sets effects), dropShadow?, feather?, innerShadow?, outerGlow?, innerGlow?, bevel?, sati… | {"name": "ProbeObj", "updated": 0} |
| `style.object.clearOverrides` | verified | {ids?} — each item takes its object style's fill, stroke, effects and text frame options again → {changed} | inspect.spreads[0].items[0].stroke.swatch: "[None]" -> "[Black]" |
| `style.group` | ran | {kind: paragraph\|character, names: [style names], group: "Heads" \| "Heads/Display" \| "" (out of any group)} — styles are named Group/Name… | accepted; no readable field changed |
| `style.load` | read-ok | {path \| base64, name?: the file's name (`.idml` reads IDML), paragraph?: [name], character?: [name], conflicts?: redefine\|useExisting\|aut… | {"character": {"added": [], "renamed": {}, "replaced": []}, "paragraph": {"added": [], "renamed": {}, "replaced": ["[Basic Paragraph]"]}, "swatches": []} |
| `style.load.list` | read-ok | {path \| base64, name?} → {paragraph: [{name, conflict}], character: [{name, conflict}]} — the styles `style.load` would bring; `conflict`… | {"character": [], "paragraph": [{"conflict": true, "name": "[Basic Paragraph]"}]} |
| `style.cell.create` | verified | {name, fromSelection?: bool (the target cell's look), fill?, tint?, insets?: n\|[t,l,b,r], vj?: top\|center\|bottom\|justify, firstBaseline?:… | readback.cell[1]: "<absent>" -> "ProbeCellNew" |
| `style.cell.apply` | read-ok | {name, story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} — the target cells (the whole table when the cursor is in it) | {"cells": 1} |
| `style.cell.edit` | ran | {name, …same as style.cell.create} — cells using the style follow | accepted; no readable field changed |
| `style.table.create` | verified | {name, basedOn?: table style name, header?, body?, footer?, leftColumn?, rightColumn?: cell style names, border?: {weight?, color?, tint?… | readback.table[1]: "<absent>" -> "ProbeTableNew" |
| `style.table.apply` | ran | {name, story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} | accepted; no readable field changed |
| `style.table.edit` | ran | {name, …same as style.table.create} — tables using the style follow | accepted; no readable field changed |

## ink (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `ink.list` | read-ok | {} → {allToProcess, inks: [{name, process: bool (printed as process), alias?}]} — the spot inks | {"allToProcess": false, "inks": []} |
| `ink.options` | ran | {allToProcess?: bool, ink?: spot swatch, toProcess?: bool, alias?: spot swatch \| null} — output: spots to process, ink aliases | accepted; no readable field changed |
| `ink.separations` | read-ok | {page?: 1-based page position (default 1; its spread is separated), dpi?: 9–300 (default 72), inkLimit?: percent, standard?: none\|x4\|a2b,… | {"conversion": "Coated FOGRA39 (fitted, craft-cms)", "dpi": 72.0, "height": 792, "inks": [{"area": 0.0, "max": 0.0, "mean": 0.0, "name": "Cyan", "spot": false}, {"area": 0.0, "max": 0.0, "mean": 0.0,  |

## table (41)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `table.insert` | verified | {rows?: body rows (4, at most 500), cols? \| columns? (4, at most 200), headerRows? (0), footerRows? (0, each at most 100), tableStyle?: n… | readback.anchor: "<absent>" -> 77 |
| `table.convertFromText` | verified | {columnSeparator?: tab\|comma\|paragraph\|text (tab), rowSeparator?: paragraph\|tab\|comma\|text (paragraph), columns?: number of columns when … | readback.anchor: "<absent>" -> 38 |
| `table.convertToText` | verified | {columnSeparator?: tab\|comma\|paragraph\|text (tab), rowSeparator?: paragraph\|tab\|comma\|text (paragraph), story?, table?, rows?: [a, b] \| r… | readback.anchor: 77 -> "<absent>" |
| `table.insertRow` | verified | {where?: above\|below, count? (1), story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.cells[12].col: "<absent>" -> 0 |
| `table.insertRowAbove` | verified | {count?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.cells[12].col: "<absent>" -> 0 |
| `table.insertRowBelow` | verified | {count?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.cells[12].col: "<absent>" -> 0 |
| `table.insertColumn` | verified | {where?: left\|right, count? (1), width?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selec… | readback.cells[10].col: 1 -> 2 |
| `table.insertColumnLeft` | verified | {count?, width?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.cells[10].col: 1 -> 2 |
| `table.insertColumnRight` | verified | {count?, width?, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.cells[10].col: 1 -> 2 |
| `table.deleteRow` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the rows of the target cells | readback.cells[10].col: 1 -> "<absent>" |
| `table.deleteColumn` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the columns of the target cells | readback.cells[10].col: 1 -> "<absent>" |
| `table.delete` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.anchor: 77 -> "<absent>" |
| `table.merge` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — merge the target cell range | readback.cells[0].colSpan: 1 -> 2 |
| `table.dropCells` | verified | {frame, from: [x, y], to: [x, y]} — selected whole rows (or columns) dragged from `from` move to the row (column) at `to`; otherwise a te… | readback.anchor: 77 -> "<absent>" |
| `table.placeGraphic` | read-ok | {path? \| base64?, name?: with base64, fit?: proportional\|fill (default proportional), story?, table?, rows?: [a, b] \| row?, cols?: [a, b]… | {"asset": 14, "col": 0, "row": 0} |
| `table.textCell` | ran | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — drop the target cells' graphics | accepted; no readable field changed |
| `table.moveRow` | ran | {from?, to, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} (0-based; from default… | accepted; no readable field changed |
| `table.moveColumn` | ran | {from?, to, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} (0-based; from default… | accepted; no readable field changed |
| `table.sortRows` | read-ok | {column?: 0-based (default: the target cell's), descending?: bool, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target… | {"sorted": 4} |
| `table.unmerge` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.cells[0].colSpan: 2 -> 1 |
| `table.splitHorizontally` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — each target cell becomes two, o… | readback.cells[10].col: 1 -> 2 |
| `table.splitVertically` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — each target cell becomes two, s… | readback.cells[0].colSpan: 1 -> 2 |
| `table.setCell` | verified | {fill?: swatch, tint?: 0..1, insets?: n \| [t,l,b,r], vj? \| verticalJustification?: top\|center\|bottom\|justify, firstBaseline?: ascent\|capH… | readback.cells[0].fill: "[None]" -> "[Paper]" |
| `table.getCellStroke` | read-ok | {story?, table?, rows?, cols?, edges?} → {weight, color, tint, type, gapColor, gapTint, fill, fillTint, edges: count} of the chosen edges… | {"color": "[Black]", "edges": 4, "fill": "[None]", "fillTint": 1.0, "gapColor": "[None]", "gapTint": 1.0, "tint": 1.0, "type": {"kind": "solid"}, "weight": 1.0} |
| `table.setRowHeight` | verified | {height, mode?: atLeast\|exactly, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.rows[0].height: 3.0 -> 24.0 |
| `table.setColumnWidth` | verified | {width, story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | readback.columns[0].width: 94.66666666666667 -> 70.0 |
| `table.resizeBorder` | verified | {story?, table?, frame?, axis: column\|row, index, delta? \| size?, keepTableSize?: bool} — moves the border after column/row `index` by `d… | readback.columns[0].width: 94.66666666666667 -> 104.66666666666667 |
| `table.distributeColumns` | ran | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | accepted; no readable field changed |
| `table.distributeRows` | verified | {story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} — equal fixed heights preserving the selected rows' composed total height; may… | readback.rows[0].height: 3.0 -> 20.451999999999998 |
| `table.options` | verified | {direction?: leftToRight\|rightToLeft, border?: {weight?, color?, tint?, type?, gapColor?, gapTint?}, spaceBefore?, spaceAfter?, headerRow… | readback.options.direction: "leftToRight" -> "rightToLeft" |
| `table.convertRowsToHeader` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the target rows, at the top of … | readback.headerRows: 0 -> 1 |
| `table.convertRowsToBody` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the target header rows next to … | readback.footerRows: 1 -> 0 |
| `table.convertRowsToFooter` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} — the target rows, at the bottom … | readback.footerRows: 0 -> 1 |
| `table.select` | verified | {story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?, what?: cell\|row\|column\|table} | inspect.selection.cells.range.c0: "<absent>" -> 0 |
| `table.selectTable` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | inspect.selection.cells.range.c0: "<absent>" -> 0 |
| `table.selectRow` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | inspect.selection.cells.range.c0: "<absent>" -> 0 |
| `table.selectColumn` | verified | {story?, table?, rows?: [a, b] \| row?, cols?: [a, b] \| col? (the target cells; default: the selection)} | inspect.selection.cells.range.c0: "<absent>" -> 0 |
| `table.nextCell` | verified | {} | readback.range.c0: 0 -> 1 |
| `table.prevCell` | ran | {} | accepted; no readable field changed |
| `table.toggleSelection` | read-ok | {} — Esc in a table, as InDesign: the insertion point or text in a cell selects that cell; selected cells select the text of the first one | {"cells": true} |
| `table.get` | read-ok | {story?, table?, rows?: [a,b] \| row?, cols?: [a,b] \| col?} → rows, columns, cells (text, spans, fill), options | {"anchor": 77, "cells": [{"col": 0, "colSpan": 1, "fill": "[None]", "firstBaseline": "ascent", "firstBaselineMin": 0.0, "insets": [4.0, 4.0, 4.0, 4.0], "rotation": 0.0, "row": 0, "rowSpan": 1, "style" |

## layer (9)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `layer.move` | ran | {id, to: index (0 = top/frontmost)} | accepted; no readable field changed |
| `layer.selectItems` | verified | {id} | inspect.selection.items[0]: 12 -> 11 |
| `layer.new` | verified | {name?} | inspect.activeLayer: 1 -> 13 |
| `layer.set` | verified | {id, name?, color?: [r,g,b] \| layer colour name ("Light Blue", "Red", …), visible?, locked?, printable?, showGuides?, suppressWrapWhenHid… | inspect.layers[0].name: "Layer 1" -> "Layer One" |
| `layer.delete` | verified | {id} | inspect.activeLayer: 12 -> 1 |
| `layer.merge` | verified | {ids: [layer ids], into?: layer id (default: the first)} — their objects move to `into`, the other layers are deleted | inspect.activeLayer: 12 -> 1 |
| `layer.deleteUnused` | read-ok | {} — layers without objects (one layer always stays) | {"deleted": 0} |
| `layer.others` | ran | {id, hide?: bool, lock?: bool, show?: true (Show All Layers), unlock?: true (Unlock All Layers)} — Hide Others / Lock Others act on every… | accepted; no readable field changed |
| `layer.activate` | ran | {id} | accepted; no readable field changed |

## prefs (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `prefs.set` | read-ok | {showHiddenCharacters?, typographersQuotes?, polygonSides?, starInset?, scaleStrokes?, dimensionsIncludeStroke?, transformationsAreTotals… | {"absolutePageNumbers": false, "autocorrect": false, "autocorrectList": [["teh", "the"], ["adn", "and"], ["taht", "that"], ["recieve", "receive"], ["seperate", "separate"], ["occured", "occurred"], [" |

## app (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `app.links` | read-ok | {} → {discord, website, appPage, github, issues} (ArtCraft Discord, website, DesignCraft page and repository) | {"appPage": "https://getartcraft.com/apps/designcraft", "discord": "https://discord.gg/artcraft", "github": "https://github.com/storytold/designcraft", "issues": "https://github.com/storytold/designcr |

## find (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `find.objects` | ran | {fill?, stroke?: swatch, strokeWeight?, opacity? (0–1), kind?: text\|graphic\|shape\|line\|group, layer?, label?, select?: bool (default true… | accepted; no readable field changed |
| `find.changeObjects` | ran | {…the criteria of find.objects, change: {fill?, stroke?, strokeWeight?, opacity?}} → {changed} | accepted; no readable field changed |
| `find.find` | read-ok | {find, grep?: bool, caseSensitive?: bool, wholeWord?: bool, scope?: document\|story\|selection, story?, findFormat?: {charStyle?, paraStyle… | [{"end": 5, "start": 0, "story": 12, "text": "Alpha"}] |
| `find.change` | verified | {find, change, grep?, caseSensitive?, wholeWord?, scope?, story?, findFormat?: {charStyle?, paraStyle?, chars?: resolved character attrib… | inspect.stories[0].preview: "Alpha beta gamma. Delta epsilon zeta.\nEta theta iota kappa. Lambda mu nu xi." -> "Omega beta gamma. Delta epsilon zeta.\nEta theta iota kappa. Lambda mu nu xi." |
| `find.next` | ran | {find, grep?, caseSensitive?, wholeWord?, scope?: document\|story\|selection, story?, findFormat?: {charStyle?, paraStyle?, chars?: resolve… | accepted; no readable field changed |

## variables (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `variables.list` | read-ok | {} → [{index, name, type, …, value (page 1)}] | [{"index": 0, "name": "Chapter Number", "type": "chapterNumber", "value": "1"}, {"format": "MM/dd/yy", "index": 1, "name": "Creation Date", "type": "creationDate", "value": "11/05/26"}, {"extension":  |
| `variables.define` | verified | {name, type: custom\|lastPageNumber\|chapterNumber\|fileName\|creationDate\|modificationDate\|outputDate\|runningHeader, text? (a string; a numb… | readback[7].index: "<absent>" -> 7 |
| `variables.delete` | verified | {name} — instances become plain text of their current value | readback[7].index: 7 -> "<absent>" |
| `variables.insert` | verified | {name} — at the text insertion point | inspect.stories[0].length: 76 -> 3 |
| `variables.convertToText` | verified | {} — the variable instances in the selected text become plain text of the value each shows on its page; the variables stay defined | inspect.stories[0].length: 20 -> 22 |
| `variables.convertAllToText` | ran | {name} — every instance of the variable in the document becomes plain text of the value it shows on its page (Text Variables › Convert to… | accepted; no readable field changed |

## toc (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `toc.generate` | read-ok | {entries: [{style, level?: 1 (1-9), entryStyle?: paragraph style of its entries (default "TOC Level n"), pageNumber?: "after"\|"before"\|"n… | {"entries": 2, "story": 14} |
| `toc.update` | read-ok | {} — regenerate the existing table of contents | {"entries": 2, "story": 14} |
| `toc.entries` | read-ok | {entries \| styles} → [{level, text, page}] without changing the document | [{"level": 1, "page": "1", "text": "Head One"}, {"level": 1, "page": "1", "text": "Body text here."}] |

## footnote (6)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `footnote.insert` | verified | {text?} — a footnote reference at the insertion point; the caret moves into the new footnote's text | readback[0].anchor: "<absent>" -> 76 |
| `footnote.options` | read-ok | {style?: arabic\|upperRoman\|lowerRoman\|upperLetters\|lowerLetters\|symbols\|kanji, startAt?, restart?: never\|page\|spread\|section, prefix?, su… | {"affixIn": "none", "firstBaseline": "leading", "firstBaselineMin": 0.0, "paraStyle": "[Basic Paragraph]", "prefix": "", "refCharStyle": "[None]", "refPosition": "superscript", "restart": "never", "ru |
| `footnote.list` | read-ok | {story?} → [{story, id, index, anchor, text}] in story order | [{"anchor": 76, "id": 1, "index": 0, "story": 12, "text": "Footnote text."}] |
| `footnote.setText` | verified | {story, id, text} — replaces the footnote's text | readback[0].text: "A footnote." -> "Changed footnote." |
| `footnote.delete` | verified | {story, id} — deletes the reference (and so the footnote) | readback[0].anchor: 76 -> "<absent>" |
| `footnote.goToReference` | read-ok | {} — from footnote text, puts the caret after the footnote's reference | {"pos": 79, "story": 12} |

## xref (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `xref.insert` | verified | {anchor? \| paragraph?: text to find (first paragraph containing it) \| story?: with para? \| para?: 0-based paragraph of `story`, format?: … | inspect.stories[0].length: 82 -> 85 |
| `xref.list` | ran | {} → [{story, pos, target, format, text}] | accepted; no readable field changed |
| `xref.formats` | read-ok | {} → [{name, definition}] | [{"definition": "\"<fullPara />\" on page <pageNum />", "name": "Full Paragraph & Page Number"}, {"definition": "\"<fullPara />\"", "name": "Full Paragraph"}, {"definition": "\"<paraText />\" on page  |
| `xref.defineFormat` | ran | {name, definition} — building blocks: <fullPara />, <paraText />, <paraNum />, <pageNum />, <txtAnchrName />, <chapNum />, <fileName />, … | accepted; no readable field changed |
| `xref.setFormat` | verified | {story, index, format} | inspect.stories[0].lines: 3 -> 2 |

## anchor (2)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `anchor.create` | verified | {name} — a text anchor at the insertion point; the name is the document's, so it must not be one another anchor already has | inspect.stories[0].length: 76 -> 79 |
| `anchor.list` | ran | {} → [{id, name, story, pos, page}] | accepted; no readable field changed |

## index (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `index.addReference` | verified | {topics?: [level 1..4] \| topic?: "Level 1 > Level 2" (default: the selected text), sort?: [keys], range?: currentPage\|toEndOfStory\|suppre… | readback[0].page: "<absent>" -> "1" |
| `index.list` | read-ok | {} → [{story, pos, topics, range, page}] | [{"page": "1", "pos": 0, "range": {"type": "currentPage"}, "story": 12, "topics": ["alpha"]}] |
| `index.generate` | verified | {title?: "Index", sectionHeadings?: true, runIn?: false, page?: 1-based page for a new frame, rect?: [x0,y0,x1,y1]} — replaces the existi… | inspect.paragraphStyles[2]: "<absent>" -> "Index Title" |
| `index.update` | read-ok | {} — regenerate the existing index | {"entries": 1, "story": 14} |

## anchored (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `anchored.insert` | verified | {ids, story?, pos? (default: the text insertion point), position?: inline\|aboveLine\|custom, yOffset?, align?: left\|center\|right, spaceBef… | readback[0].index: "<absent>" -> 0 |
| `anchored.options` | ran | {story?, index? (default: the object at the insertion point), position?: inline\|aboveLine\|custom, yOffset?, align?: left\|center\|right, sp… | accepted; no readable field changed |
| `anchored.release` | verified | {story?, index? (default: the object at the insertion point)} — puts the object back on the page where it is now and removes it from the … | readback[0].index: 0 -> "<absent>" |
| `anchored.list` | read-ok | {story?} → [{story, index, pos, position, size}] | [{"index": 0, "pos": 0, "position": {"kind": "inline", "y_offset": 0.0}, "size": [190.0, 160.0], "story": 12}] |

## view (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `view.lockColumnGuides` | read-ok | {on?: bool (default: toggle)} → {locked} — locked column guides can't be dragged; saved with the document (IDML ColumnGuideLocked), on in… | {"locked": false} |
| `view.zeroPoint` | read-ok | {at?: [x, y] (points right of and below the ruler origin — document.preferences rulerOrigin: spread\|page\|spine; kept on the pasteboard), … | {"locked": false, "zeroPoint": [0.0, 0.0]} |
| `view.lockZeroPoint` | read-ok | {on?: bool (default: toggle)} → {locked} — a locked zero point can't be dragged, moved or reset | {"locked": true} |

## font (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `font.list` | read-ok | {} → [{family, style, characters, missing, styleMissing, source: bundled\|installed\|document\|added (null when missing), matchStatus: exact… | [{"bitmapOnly": false, "characters": 75, "editable": false, "family": "Source Serif 4", "fsType": 0, "matchStatus": "exact", "missing": false, "noSubsetting": false, "previewPrint": false, "replacemen |
| `font.replace` | refused | {family, style?, toFamily, toStyle?, redefineStyles?: true} — replaces the font in text and (by default) in paragraph and character styles | invalid parameters for `font.replace`: Choose an available replacement font family |
| `font.reload` | read-ok | {} — scans the font folders again and reads again the installed font files changed or removed since they were read, then recomposes the o… | {"cataloged": 315, "changed": []} |

## spelling (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `spelling.check` | ran | {story?, suggestions?: true} → [{story, start, end, word, suggestions}] | accepted; no readable field changed |
| `spelling.setWords` | ran | {words: [word]} — replace the document's user dictionary | accepted; no readable field changed |
| `spelling.words` | ran | {} → [word] | accepted; no readable field changed |
| `spelling.addWord` | ran | {word} | accepted; no readable field changed |
| `spelling.change` | verified | {story, start, end, to} | inspect.stories[0].length: 76 -> 75 |

## hyphenation (3)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `hyphenation.addException` | ran | {word: "ex~am~ple" (breaks only at ~) or a word with no ~ (never hyphenated)} | accepted; no readable field changed |
| `hyphenation.removeException` | ran | {word} (with or without ~) | accepted; no readable field changed |
| `hyphenation.list` | ran | {} → [word] | accepted; no readable field changed |

## data (10)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `data.source.select` | verified | {path \| bytes\|base64, name, delimiter?: comma\|tab\|semicolon, sheet?} → {fields, records, warnings} | readback[0].kind: "<absent>" -> "text" |
| `data.source.update` | read-ok | {} → re-read the linked file | {"fields": [{"kind": "text", "name": "name"}, {"kind": "text", "name": "city"}], "records": 2, "warnings": []} |
| `data.source.remove` | ran | {} → drop the source; placeholders stay | accepted; no readable field changed |
| `data.fields` | ran | {csv? \| rows? \| path? \| bytes? \| base64?, name?, delimiter?, sheet?} → [{name, kind, uses}]; no params reads the linked source and does n… | accepted; no readable field changed |
| `data.placeholder.add` | verified | {field, role?: text\|image\|qr\|hyperlink, story?, at?, end?, item?} → {id} | readback[0].uses: 0 -> 1 |
| `data.placeholder.remove` | verified | {id} | readback[0].uses: 1 -> 0 |
| `data.options` | read-ok | {records?, one?, range?, perPage?, arrange?, insets?, columnSpacing?, rowSpacing?, fitting?, center?, linkImages?, limit?} | {"arrange": "rows", "center": false, "columnSpacing": 0.0, "fitting": "fitProportionally", "insets": [36.0, 36.0, 36.0, 36.0], "linkImages": true, "one": 1, "perPage": "single", "range": "", "records" |
| `data.preview` | read-ok | {record?: n} → fill the template with that record (session only) | {"record": 1} |
| `data.preview.stop` | ran | {} → restore the unfilled template | accepted; no readable field changed |
| `data.merge` | verified | {csv? \| rows? \| path? \| bytes? \| base64?, name?, delimiter?, sheet?, records?, one?, range?, perPage?, arrange?, insets?, columnSpacing?,… | attrs.characterStyle: "[None]" -> "<absent>" |

## hyperlink (5)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `hyperlink.create` | verified | {url? \| email? \| page? (1-based), name?, ids?} — from the selected text, or the selected frames | readback[0].dest.kind: "<absent>" -> "url" |
| `hyperlink.delete` | verified | {id} | readback[0].dest.kind: "url" -> "<absent>" |
| `hyperlink.list` | ran | {} | accepted; no readable field changed |
| `hyperlink.edit` | verified | {id, name?, url? \| email? \| page? (1-based)} | readback[0].dest.value: "https://example.com" -> "https://example.org" |
| `hyperlink.goToSource` | ran | {id} — selects the hyperlink's text or frame | accepted; no readable field changed |

## bookmark (4)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `bookmark.rename` | ran | {index, name} | accepted; no readable field changed |
| `bookmark.add` | ran | {name?, page? (1-based; default: current selection's page or 1)} | accepted; no readable field changed |
| `bookmark.delete` | ran | {index} | accepted; no readable field changed |
| `bookmark.list` | ran | {} | accepted; no readable field changed |

## preflight (1)

| id | status | params doc (short) | evidence |
|---|---|---|---|
| `preflight.run` | read-ok | {minPpi?: 150} → issues [{severity, kind, message, item?, page?}] | {"errors": 0, "issues": [], "warnings": 0} |

