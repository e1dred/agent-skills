---
name: lightcraft
description: Use when managing a photo library or developing raw/JPEG photos: importing, rating, keywords, albums, non-destructive edits (exposure, curves, masks, crop, spot removal, denoise, faces), merges (HDR, panorama), export/print/slideshow, when running lightcraft-cli, or when connecting to the LightCraft app (storytold) on this machine
---

# LightCraft

Field notes from a first full headless round, last tested on **LightCraft 0.19.0** (Linux AppImage
`lightcraft-cli`). LightCraft is a non-destructive photo library and raw developer in Rust; the CLI, the MCP
server and the app's control channel run the same engine commands. If `lightcraft-cli --version` is newer,
re-check anything here before relying on it.

## Setup

- **CLI:** `~/AppImages/lightcraft-cli` (self-contained, no window). Never run `--version` on the AppImage.
- **Headless modes:** `run --demo` (procedural 24-photo demo library, state is per process) or
  `run --library DIR` (creates/opens a library; edits, presets and templates persist). `--import PATH`
  imports before the first command.
- **One process, many commands:** `lightcraft-cli run [--demo|--library DIR] [--keep-going] COMMAND key=value … COMMAND …`
  prints one JSON line per command: `{"command","ok","result"|"error","ms"}`, exit ≠ 0 on a failure.
  Use `--script -` with JSON lines `{"command": id, "params": {…}}` for complex params.
- **Single render:** `lightcraft-cli render IN -o OUT --set control=value … --size N --quality Q --opt key=value`.
- **Merges from the shell:** `lightcraft-cli merge hdr|panorama|hdr-panorama|hdr-batch FILES…` (writes
  `<first>-HDR.dng` / `-Pano.dng` beside the first file); `synth-merge hdr|panorama -o DIR` makes test inputs.
- **MCP:** `lightcraft-cli mcp [--demo|--library DIR] [--compact]`, stdio JSON-RPC; every command stays reachable.
- **Live app:** `--connect` / `lightcraft --control` — not exercised in this round; do not open windows on the
  user's screen without being asked.

## Where things are

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `cli.md` | Subcommands, run/script forms, output shape, demo vs library, render/merge/synth-merge, what is headless | Commands worth running from a shell; Modes; Output |
| `library-and-import.md` | Import, folders, auto-import, previews, albums (incl. smart), stacks, versions, history/undo, view state (filter/sort/source/selection) | Import and folders; Albums; Stacks and versions; View, filter, selection |
| `develop.md` | Develop sliders (122 controls), crop/straighten, curves, white balance, targeted adjustments, before/after, point colour, HDR | Develop values; Controls; Crop and geometry; Curves; White balance; Before/after |
| `masks-and-repair.md` | Masks (brush, linear, radial, sky, subject, background, range), mask effects, spot removal, red eye | Masks; Mask effects; Spot removal; Red eye |
| `metadata-keywords-labels.md` | Ratings/flags/labels, titles/captions/copyright/GPS, keywords and keyword sets, metadata presets, filter presets, find similar | Per-photo metadata; Keywords; Labels; Metadata presets; Filter presets |
| `export-print-slideshow.md` | Export formats and options, export presets, contact sheets, print layouts/templates/PDF, slideshows and their export | Export; Export presets; Print; Slideshow |
| `merge-and-models.md` | HDR/panorama merges, denoise, faces, segmentation, lens database, GPU/memory, background tasks | Merge; Denoise; Faces; Segmentation; Profiles; App |
| `command-catalogue.md` | Every id (389), grouped by family, with the evidence status and the field that changed | — |
| `newer-commands.md` | What each version added or changed | 0.18.1; 0.19.0 |
| `log.md` | Dated log of what was tested when | Log |

## CLI essentials (verified)

```
lightcraft-cli --version                          # 0.19.0
lightcraft-cli commands --json                    # every id + params (389 ids)
lightcraft-cli controls --json                    # every develop control with min/max/default (122)
lightcraft-cli run --demo catalog.query limit=3   # {"command":"catalog.query","ok":true,"result":{"photos":[…]}}
lightcraft-cli run --library ~/lc-lib --import ~/Pictures --keep-going library.info
lightcraft-cli run --library ~/lc-lib library.select ids=[12] develop.set control=light.exposure value=0.7 app.export path=/tmp/x.jpg longEdge=1600
lightcraft-cli render in.cr3 -o out.jpg --set light.exposure=0.5 --size 1600 --quality 90
lightcraft-cli merge panorama a.jpg b.jpg c.jpg --projection=auto --preview /tmp/p.png
lightcraft-cli synth-merge panorama -o /tmp/panels    # view-0.png … for testing merge
```

- `run` words without `=` start the next command; a value is JSON when it parses (`1`, `true`, `[1,2]`, `{}`),
  else a string — so `aspect="1x1"` (quoted in a shell) stays a string.
- Without `--keep-going` the run stops at the first failed command.
- Read state back with a real field, e.g. `photo.inspect id=N` returns the whole develop tree and `meta`;
  `develop.get id=N` returns settings only; `library.state` returns view/filter/sort/selection.
- Commands addressed to "the selection" or "the active photo" need `library.select ids=[…]` first in the same script.

## Traps

- **Demo photos have no file.** `--demo` photos are generated: export to `dng`/`original`, `photo.duplicate`,
  `photo.editExternal`, `photo.saveMetadataToFile` and every merge refuse with *"a generated demo photo has no
  file"*. Use a `--library` with real images for anything that touches bytes.
- **Background work dies with the process.** `slideshow.export` returns a task and runs in the background;
  in a one-shot `run` the process exits first and leaves `out.pdf.part`. Pass `wait: true` (verified: pdf, jpeg,
  video). `library.buildPreviews wait:true` likewise.
- **Demo state is per process; library state persists.** A preset created with `--demo` is gone in the next
  process; with `--library` it is on disk (`preset.create` → id like `user.43.libp1`).
- **`folder.rename` / `folder.move` rename the real folder on disk** (verified: in2 → in2-renamed). Never point
  them at a user's photo folder without asking.
- **Folder commands only accept folders the library imported from**, by the exact path `library.folders` shows.
  A folder imported only by `--import` at startup was reported as *"no photo in the library was imported from
  it"*; a folder added later with `library.import` worked.
- **Two different rating enums.** `album.createSmart`/`album.setRules` rules take `atLeast|exactly|atMost`;
  `library.selectBy` takes `gte|eq|lte`. Mixing them is an "unknown variant" refusal.
- **Control ids are not inspect paths.** `develop.set control=light.exposure` is right; the inspect tree shows
  `develop.light.exposure`, and camel-case controls (`detail.sharpenAmount`, `curve.splitShadows`) appear as
  snake_case. An unknown control (e.g. `light.vibrance`; the real one is `color.vibrance`) fails the call.
- **`render --set` takes only controls, never commands.** `--set treatment=bw` is refused ("not a finite number").
- **Masks `object` and `prompt` need the SAM 3 model (~3.4 GB)** and are refused without it; `subject`, `sky`,
  `background`, `brush`, `linear`, `radial`, `luminanceRange`, `colorRange` all work headless.
- **`mask.update` wants the complete shape** (kind, center{x,y}, rx, ry, angle, feather, invert), not a diff.
- **Faces, blemish finding and face boxes need models**: YuNet (232 KB) for detection, a recognition model for
  indexing; `spot.findBlemishes` refused for the same YuNet reason. Model downloads were never run here.
- **`redeye.catchlight` only exists on pet eyes** (`redeye.add … pet=true` first).
- **`photo.setRegion`/`photo.removeRegion` edit existing face/pet regions**; with none, "no such region".
- **`develop.updateProcess` is refused when the photo is already on the current process** — that is success,
  not failure.
- **`export.addToPhotos` is macOS-only** ("Apple Photos is only available on macOS").
- **`denoise.toggle` applies to raw photos only**; JPEGs are refused.
- **Attach the background task id**: `slideshow.export`/`activity.cancel` use task ids from `activity.list`.

## Verify before reporting

- Read the same field before and after in one run: `photo.inspect` (develop, meta, rating, flag, label,
  versions, spots, red_eye, masks), `library.state` (source, filter, sort, selection, visibleCount, undo),
  `albums.list`, `keyword.list`, `presets.list`, `print.get`, `slideshow.<section>`.
- For bytes, check the file: PIL size/mean for images, file size for PDFs/MP4s; `render` at a small size is
  the cheapest visual proof (exposure +1 changed 172,800 px of a 480×360 render; vignette −50 changed 103,946).
- A history-length or `edited` change alone is not proof of a specific effect — downgrade it.
