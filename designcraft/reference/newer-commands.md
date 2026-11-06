# Changes between versions

> **Versions:** baseline DesignCraft 0.17.2 (2026-11-05): 547 command ids, all run once headless
> (see `command-catalogue.md`). When a newer CLI is installed, diff `designcraft-cli commands` ids and
> params docs against this baseline, run the new ids, and add a section here per version.

## 0.18.0 changes (verified headless 2026-11-06)
Catalogue: 547 → 555 ids, added 8, removed 0, parameters changed 6. Regression: no harness existed for this app, so a 12-step script (new document, two paragraph styles, two text frames, style applies, thread, `document.inspect`, `story.get`, `file.exportPdf`, save and render both pages) was run with the 0.17.2 and 0.18.0 CLIs: results, `document.json` and both rendered page PNGs are byte-identical.

- **`file.exportPresets {}`** → `{presets:[{name, job, builtIn}], versions:[…]}`: four built-in presets (Print + Screen, Press PDF per Layout, Images per Layout, All Layouts in One PDF) and five versions.
- **`file.saveExportPreset {"name","job"}` / `file.deleteExportPreset {"name"}`**: kept with the preferences, not the document; `file.exportPresets` went 4 → 5 names with MiniTest, then back to 4 after the delete.
- **`file.exportBatch {"job"|"preset","dir","dryRun"?,"date"?,"fileName"?}`** → `{files, warnings}`: exports every layout and version (pdf/png/jpeg), one folder per version, `{document}`, `{layout}`, `{version}`, `{date}` in the name. Run on a 6-page document: `Png/Mini-Layout 1 - 1.png` … one file per page with its bytes and page list in `files`.
- **`layout.alternate.delete {"layout"}`, `layout.alternate.duplicate {"layout","name"?}` → `{layout, firstPage, pages}`, `layout.alternate.options {"layout","name"?,"width"?,"height"?}` → `{layout}`**: page count 6 → 4 on delete, 4 → 6 on duplicate (firstPage 5), and the duplicated layout's page bounds went 800 → 820 with `width:820`.
- **`layout.parents.duplicate {"parent"} `** → `{id, prefix}`: a copy with the next free prefix (A gave `{id:20, prefix:"B"}`, and `document.inspect` listed B-Parent with 0 items).
- **`layout.createAlternate`** takes `from` (source layout name or index) and `fromName`; both created 900×700 and 800×600 page sets from "Layout 1".
- **`layout.parents.new`** takes `prefix` (1–4 characters, no `-`) and `basedOn`; `layout.parents.options` takes `prefix` and `basedOn`. `parents.new {"prefix":"C","basedOn":"A"}` gave C-Parent based on A-Parent, and `parents.options {"parent":"C","prefix":"D","name":"Renamed Parent"}` renamed it to D-Renamed Parent.
- **Hyperlinks can point at a text anchor:** `hyperlink.create {"anchor":"Target"}` and `hyperlink.edit {"id","anchor":"Other"}` wrote `dest:{kind:"anchor", value:150994945}` and then `150994946` in `hyperlink.list`. IDML import and export keep hyperlinks too.
- **`file.print`** takes `layouts` (their pages instead of `pages`) and `separateJobs`: with `dryRun` a 6-page document printed as 2 pages for `layouts:["Layout 1"]`, and two layouts gave `jobs:["Mini - Layout 1","Mini - Web"]` with `separateJobs:true`, one job without it.
- Other: an item a parent overrode and deleted is gone from the pages that use it; a text frame anchored in a copied frame keeps its text; a frame holding pasted-in content draws its own edge; IDML `TextTopInset` cell insets survive import; Esperanto added as a text language.
