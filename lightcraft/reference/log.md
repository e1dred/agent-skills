# Log

## 2026-11-04 — LightCraft 0.18.1, first headless round

- Environment: `lightcraft-cli` 0.18.1 AppImage, Linux; isolated HOME under the work folder; headless only
  (`run --demo`, `run --library`, `render`, `merge`, `synth-merge`).
- Tested all 376 ids of `ids.txt` plus the 7 ids `commands` has that ids.txt lacks (beforeAfter.*, pointColor.*).
  Result: 158 verified (same field read before/after), 11 read-ok, 168 ran (accepted, no read-back field),
  35 refused, 4 skipped (model/dataset downloads forbidden). Per-id evidence in `results.jsonl`.
- All 122 develop controls set through `develop.set` and read back from `develop.controls`
  (`develop-controls.tsv`).
- Exports verified by file: jpeg/png/tiff/webp/psd/jxl/avif at 800 px; contact sheet PDF (90 KB); print PDF
  (2.6 MB); slideshow PDF (385 KB), JPEG sequence, AV1 MP4 (1.4 MB) with `wait:true`.
- Merges verified with `synth-merge` inputs: panorama → `view-4-Pano.dng` (7.8 MB), HDR →
  `bracket-0-HDR.dng` (3.0 MB); HDR batch merged one set; HDR panorama needs more bracket positions.
- Renders (480×360) used as pixel proof: exposure +1 changed 172,800 px, vignette −50 changed 103,946 px.
- Weak rows after self-review: 11 downgraded (`downgraded.txt`).
- Not tested: UI/control channel, MCP transport, raw files, AI models, Apple Photos export (macOS only).
