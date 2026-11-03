# ONLYOFFICE reference: presentations

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Designed decks from shapes (verified headless; render checked)

For anything presented, skip placeholders (`get_api_reference(editor="slide", topic="designed")` has the library; a tested copy
is `recipes/designed_deck_helpers.js`). Recipe, all inside ONE `slide_write_macro`: paste the helpers, `master.SetBackground(
SF("#EEF2F7"))`, `s1=pres.GetSlideByIndex(0); s1.ApplyLayout(blank)` and delete its leftover placeholders
(`s1.GetAllDrawings()` → `Delete()`), then per slide `Api.CreateSlide(); ApplyLayout(blank); AddSlide`, and compose with
`header(sl,"KICKER","Title")`, `card`, `chip`+`arrR` (process flow), `takeaway`, `footer`. A 4-slide deck (title with two
overlapping circles, three cards, a 4-step flow, chart slide) rendered cleanly on the first try.
- Add the chart AFTER the macro with `slide_add_chart_to_slide` on a blank-layout slide: it lands centred and small (~40% width)
  in the default blue/orange, not the deck palette; resize/recolour it by macro if it matters.
- Size cards to their content: at 3.5 M EMU high with two lines of text they looked half empty.
- Fonts: Linux has no Segoe UI; the library's `FONT` variable was set to Arial and rendered as Arial.
- `slide_get_presentation_context {"detail":"audit"}` still flags `layout_mismatch` on a designed title slide: ignore it.
- `preview` with `pages:"all"` writes `<path>_pages/imageN.png` beside your `path`; its reply text wrongly says the pages are
  in the default output folder, which was empty. Combine the pages into one contact sheet with PIL to read a whole deck in
  one image.

## Presentations (verified headless; `slide_*` tools)

Read `learn_about(topic="presentations")` (designed vs placeholder route). Placeholder route, as tested:
- A new deck has one title slide. Add slides by macro (no add-slide tool):
  `var p=Api.GetPresentation(),m=p.GetMaster(0),s=Api.CreateSlide();s.ApplyLayout(m.GetLayoutByType('obj'));p.AddSlide(s);`
  (types `title|obj|twoObj|secHead|picTx|titleOnly|blank`).
- Theme colours: `m.GetTheme().SetColorScheme(Api.CreateThemeColorScheme([12 × Api.Color('#…')],'Name'))`, order
  accent1..accent6, dk1, dk2, folHlink, hlink, lt1, lt2. Charts then use accents 1–3 (navy/blue/orange in the test).
- `slide_set_text {"slide_number":N,"target":"title|subtitle|body|notes","text":"line1\nline2"}` (newline = new paragraph;
  `target:"notes"` writes speaker notes).
- `slide_add_chart_to_slide {"slide_number":3,"chart_type":"bar","categories":[…],"series":["Q1","Q2"],"data":[[…],[…]]}`:
  **each inner list of `data` is ONE series' values** (length = number of categories). Giving only categories+series
  names without `data` is an error ("give either 'data' … or 'prompt'"). Mismatched shapes are padded: 3 rows with
  2 names made a third "Series 3" and cut the categories to the row length. The chart fills the content placeholder.
- `slide_get_presentation_context {"detail":"audit"}` lists problems per slide (e.g. `no_speaker_notes`); `preview`
  with `pages:"all"` renders every slide.
