# Newer commands / versions

## 0.18.1 (2026-11-04)

First commanded round for this skill; no earlier version was available to diff. What exists in 0.18.1:

- 383 command ids (`lightcraft-cli commands`), 122 develop controls (`lightcraft-cli controls`).
- Subcommands: `run`, `mcp`, `render`, `snapshot`, `merge`, `synth-merge`, `denoise-serve`, `commands`,
  `controls`, `calibrate`.
- Families: activity, album(s), app, beforeAfter, catalog, crop, curve, denoise, develop, edit, export, faces,
  filter, focus, folder, geometry, history, journal, keyword, label, lens, library, mask, merge, metadata,
  photo, pointColor, preset(s), print, profile(s), redeye, segment, slideshow, spot, stack, version.
- Evidence for every id: `results.jsonl`; status per id: `skill/reference/command-catalogue.md`; refusals and
  why: `REPORT.md`.
- Not tested: `snapshot` (drives the UI), the control channel (`--connect`, `ui.*`), MCP transport, raw decoding,
  any model download or AI model (none installed).
