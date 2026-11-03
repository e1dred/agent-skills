# DeckCraft reference: log

Part of the deckcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-10-25: first verified run on Linux (0.10.0): headless run/save/convert/render/info, live new/slide/shape/table/chart/
  save/export/screenshot with the Pitch starter. Reference reading: artcraft-skills `deckcraft` (macOS, MIT).
- 2026-10-25 (2): themes, animation, transition, picture, notes, outline import, notes/handout PDF, GIF, pptx round trip verified headless.
- 2026-10-25 (3): full deck build (text, table cells, chart options, link, background, slide management, sections, accessibility) verified headless incl. pptx round trip.
- 2026-10-26: SmartArt, text builds, auto-advance timing, align/distribute/group, picture crop/adjust/style, custom master layout verified headless.
- 2026-10-25 (4): brand theme colours/fonts, header/footer, chart types, table style/merge/borders, connectors, shape effects/merge, icon/WordArt/audio, comments, spelling, compare, custom show, slide links, morph verified.
- 2026-10-25 (5): three build sequences re-run on 0.10.0 and 0.11.1 (identical except default chart text tint); version labels added per section.
- 2026-10-25 (6): live control channel re-tested on the 0.11.1 app (edits, screenshot, PDF export).
- 2026-10-25 (7): 45 SmartArt layouts rendered, animation/transition catalogues, animation edit commands + pptx round trip, transition sound/timing/applyAll, layout-level master editing verified headless on 0.11.1.
- 2026-10-25 (8): shape formatting/freeform points, text and paragraph formatting, table cell commands, photo album, action buttons/zoom/slide actions, sections, slide/notes/handout masters, artistic picture effects, file properties/templates verified headless on 0.11.1.
- 2026-10-25 (9): character formats, text movement, edit/selection helpers, arrange, table columns, audio media options, slide navigation, render/saveBytes and command discovery verified headless on 0.11.1.
- 2026-10-25 (10): ink: only `draw.inkToShape` exists; strokes need pointer input in a visible window.
- 2026-10-26: gap round: format.alignLeft/Center/Right, edit.redo, textBox rect units.
- 2026-10-26: the last 28 command ids run with their setups (smoke test).
- 2026-10-27: board deck from invented sample data (3 native charts, table, SmartArt, notes, alt text, 60-30-10 palette); chart-axis gap recorded.
- 2026-10-28: CLI refreshed; 19 decks (the six starters with title/bullets/shape/table/chart/text box/notes/transition, a blank deck with duplicate/move/hide/section/background/variant, seven chart types, five layouts) built with the old and new CLI: identical `info`, identical parts in every `.pptx`, 64 rendered slides pixel-identical. Three new commands verified; live app re-checked (file.new, slide.new, selectRange, languageAll, document.inspect, ui.render, file.close); `ui.screenshot` refused (window hidden), `ui.render` works.
- 2026-10-28 (2): `ui.screenshot` was still refused ("no frame was presented") after the user un-minimized the other apps: the window must be on screen and drawing, not just un-minimized; `ui.render` (slide only) works regardless.
- 2026-10-31: CLI refreshed (0.12.0 → 0.13.1); 14 decks (the sample, blank-deck edits, five chart types, table, shape effects and gradient fill, SmartArt, theme/background/transition/animation, numbering, date and time, comments/notes/section) built with the old and new CLI: `info`, `.pptx` XML and `.pdf` page pixels compared. Only the table alignment XML and the PDF rendering above differ; a second run of background, transition and animation (`fade`, `wipe`) gave identical `info` and `.pptx` parts; `design.theme` needs a name from `design.themes` ("Office Theme" is refused) and `animation.add` rejected `fadeIn`.- 2026-11-01: CLI refreshed (0.13.1 → 0.14.1); motion paths (points, closed, OOXML string, `animation.set`/`options`) and `slide.actions` (click, hover, text and table-cell links) run headless with a `.pptx` round trip.
- 2026-11-01 (2): full re-run, old (0.13.1) vs new (0.14.1) CLI: 23 decks (six starters with bullets, shape, table, chart, text box, notes and transition; blank-deck slide management, sections, background, variant, footer; eight chart types; five layouts; SmartArt; theme, brand colours and fonts, shape effects and animation; outline import, comment, proofing language): `.pptx`, `info`, 72 rendered slides, PDF and Markdown all identical. Renders looked at. Live channel not re-checked (the app was not running).
- 2026-11-02: CLI refreshed (0.14.1 → 0.15.0); full re-run old vs new: 23 decks, 188 outputs (pptx, info, renders, PDF, Markdown) identical; new gradient kinds run and rendered.
