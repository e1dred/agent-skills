# SoundCraft 0.18.0 — docs notes (facts from docs + --help)

Sources: docs/cli.md, docs/control-protocol.md, docs/mcp.md, docs/gaps.md,
docs/file-format-parity.md, README.md (repo root), and `soundcraft-cli <cmd> --help`.
CLI: `~/AppImages/soundcraft-cli` (0.18.0).

## CLI subcommands (one example each)
- `info FILE [--compact]` — audio format as JSON, or a `.scraft` summary (text).
  `soundcraft-cli info mix.wav` → `{"channels":2,"format":"Wav",...,"sample_rate":48000}`.
- `convert IN OUT [--bit-depth 16|24|32f] [--rate HZ] [--normalize] [--dither|--no-dither] [--in-place]`
  `soundcraft-cli convert in.wav out.flac --bit-depth 16 --rate 44100`
  (dithers only when resolution is lost, unless told otherwise; normalize targets -0.1 dBFS).
- `run [--cmd ID[=JSON]]... [--in S.scraft] [--demo] [--bounce OUT] [--start T] [--end T]
  [--save S.scraft] [--inspect] [--compact] [--in-place]`
  `soundcraft-cli run --demo --cmd 'mix.volume={"track":"Kick","db":-6}' --bounce mix.wav`
  Prints each command result (one line), then bounce, save, inspect, in that order.
- `script FILE [--keep-going] [--in FILE|--demo] [--bounce/--save/--inspect...]`
  `soundcraft-cli script steps.txt --demo --keep-going --save out.scraft`
  One `ID JSON` per line; blank/# lines skipped; a failing line stops unless --keep-going.
- `commands [FILTER] [--json] [--compact]` — list ids (483 total), filter by id/label.
- `describe ID [--compact]` — one command's details as JSON (params, menu, shortcut, enabled).
- `app [--port P] METHOD [JSON] [--compact]` — control method or engine id shorthand for
  engine.execute; port from `SOUNDCRAFT_CONTROL_PORT`, default 7979.
- `mcp [--demo] [--connect PORT] [--automation-read-root DIR]... [--automation-write-root DIR]...`
  — MCP on stdio (tools in docs/mcp.md). Roots confine reads/writes; --connect conflicts with roots/--demo.
- `parity [--write PATH]` — markdown parity report.
- `plugins` — built-in plugin ids/labels (31: eq_1band, eq_7band, compressor, ..., sampler).
- `-V/--version`, `help <cmd>`; no `version` subcommand.

## Exit codes / output
0 success; 1 command failed (missing file, unknown id, app not running); 2 usage error
(bad/twice-given flag, wrong type, conflicting flags, missing value). Errors go to stderr as
`error: <message>`. Results are JSON on stdout; `run`/`script` result lines `ID: JSON` are one line each.
An output that is also an input is a usage error unless `--in-place` (and never for bounce==save).

## Environment
- `SOUNDCRAFT_CONTROL_PORT` — port / host:port for `app --port` and desktop `--control`.
- Desktop app: `SOUNDCRAFT_CONFIG_DIR` (empty = no settings folder), `SOUNDCRAFT_NO_PREFS`,
  `SOUNDCRAFT_NO_SYSTEM_FONTS`, `SOUNDCRAFT_WAYLAND`, `RUST_LOG` (env_logger directives).
- Automation roots are flags only; no env variable grants file access.

## Control protocol (docs/control-protocol.md)
TCP on 127.0.0.1, newline-delimited JSON, one request per line, one reply per line.
Desktop: `soundcraft --control <port>` (`0` = free port, prints `SOUNDCRAFT_CONTROL_PORT=…`).
`--no-audio` for UI acceptance (does not stop recording input on arm/monitor).
Request: `{"id":1,"method":"engine.execute","params":{"command":"track.new","params":{...}}}`
Reply: `{"id":1,"ok":true,"result":{...}}`; error: `{"id":1,"ok":false,"error":"..."}`.
No token/auth in the docs; loopback only.
Methods: engine.execute (alias command), engine.commands, engine.parity, session.inspect
({detail:"summary"|"full"}), ui.inspect, ui.set, ui.menu.list, ui.menu.invoke, ui.click, ui.drag,
ui.scroll, ui.zoom, ui.move, ui.key, ui.text, ui.screenshot, app.quit; docking via engine.execute
ui.dock/ui.dock.reset. Positions: samples, {"seconds":x}, or strings like "bars_beats:5|1|000",
"min_secs:0:12.500", "timecode:00:00:10:00", "samples:48000". Tracks by id or name, clips by id;
ranges start+end or start+length, omitted = edit selection.

## MCP (docs/mcp.md)
Tools: list_commands, execute, batch (≤1000), inspect_session, new_session, open_session,
save_session, import_audio, bounce_mix, parity, and app-only screenshot/ui_inspect/ui_set/
menu_invoke/click/drag/key (with --connect). Resources soundcraft://session, soundcraft://commands.
Automation roots confine file reads (open_session, import_audio/midi/video, session data, presets,
sampler_load) and writes (save/bounce/export/presets, Audio Files/, Backups/). Refusals are ordinary
tool errors (`automation path rejected: outside the write root ...`). Missing roots stop the server.

## File formats (docs/file-format-parity.md)
- Sessions: `.scraft` JSON + `Audio Files/` (read/write; plugin state embedded). Import Session Data
  from `.scraft` only. Clip groups `.scgrp` (own). Session-as-text export (`file.export_session_text`).
- No `.ptx/.ptf`, `.ptxt`, AAF, OMF, ADM BWF, MXF audio/video, iXML, Pro Tools track/fade/I-O presets.
- Audio read: WAV/BWF/RF64, AIFF/AIFF-C, FLAC, MP3, AAC/M4A/MP4, ALAC, OGG, CAF; also 8-bit and
  float64 read. Write: WAV/BWF/RF64, AIFF/AIFF-C, FLAC. No MP3/AAC export (G-21).
- MIDI: SMF type 0/1 read; export is partial (imported controllers omitted; tracks filter ignored).
  MusicXML export (`file.export_sibelius`), printable score SVG, `file.print_score`.
- Video: H.264/MP4, ProRes, Motion JPEG read (own decoder); no HEVC/AV1/DNx; no video bounce.
- Plugins: VST3/CLAP/AU hosted; no AAX. Built-in JSON presets, no `.tfx`.
- Overall file-format readiness ~40% (session interchange the big gap).

## Known gaps (docs/gaps.md highlights)
G-01 audio interface: device/output selection done; no multichannel I/O routing, no duplex clock.
G-02 no MIDI hardware I/O at all. G-03 no Pro Tools/AAF/OMF interchange. G-06 media decoded whole
in memory; no disk streaming/recording-to-disk. G-07 no fidelity harness vs Pro Tools. G-08 built-in
plugins are presets of a few algorithms, not a broad suite. G-12 no Atmos. G-17 video/post limits.
G-20 MIDI/instrument depth. G-21 no compressed export. G-22 no cloud services.
