---
name: soundcraft
description: Use when editing, mixing or bouncing multitrack audio or MIDI sessions (.scraft), importing WAV/AIFF/FLAC/MP3/MIDI, adding plugins, sends, buses or automation, converting or normalizing audio files, exporting stems, MIDI or MusicXML, when running soundcraft-cli, or when connecting to the SoundCraft app (storytold, a Pro Tools-style DAW) on this machine
---

# SoundCraft

Field notes from the first full round, last tested on **SoundCraft 0.18.0** (Linux AppImage, CLI `soundcraft-cli`).
SoundCraft is an alpha, Pro Tools-style DAW in Rust. The CLI, the MCP server and the app's control channel run the
same 483 engine commands. If `soundcraft-cli --version` reports a newer build, diff `commands --json` against
`reference/command-catalogue.md` before relying on parameters here.

## Setup

- **CLI:** `~/AppImages/soundcraft-cli` (no window). `run` (commands on a new / `--demo` / `--in` session, then
  `--bounce OUT`, `--save OUT`, `--inspect`), `script FILE` (one `ID JSON` per line), `describe ID` (the only
  parameter reference), `info FILE` (audio or `.scraft`), `convert` (resample, bit depth, normalize; WAV/AIFF/FLAC),
  `plugins`, `parity`, `mcp`, `app`.
- **Keep the user's settings out of tests:** prefix every test run with `SOUNDCRAFT_NO_PREFS=1` (no preferences
  read or written, no log file). Changing `HOME` alone is not enough, and `~` then points at the new HOME:
  use absolute paths.
- **Demo session** (`run --demo`): 9 tracks Kick, Snare, Hats, Bass, Pad, Keys (MIDI), Lead (MIDI), Verb (aux bus),
  Master 1; Kick has inserts EQ7 + Comp. Good for any test that needs material.
- **Live app:** `soundcraft.appimage --control PORT [--no-audio]`, then `soundcraft-cli app --port PORT ID '{json}'`
  (dotted ids = engine commands; `ui.*`, `session.inspect`, `app.quit` are methods). No token, loopback only.
  Details and the `ui.*` methods: `reference/live-app.md`.

## Traps (each cost a failed run)

- **Command replies are often echoes.** `mix.mute`, `mix.phase_invert`, `view.*` toggles return `{"value":true}`
  whatever happened. Read state back: session state from `session.inspect` (or `run --inspect`), option/view
  state from `setup.preferences` → `edit.flags` (the flag name appears, e.g. `edit.snap_to_grid`), `edit.rulers`.
- **Plugin (insert) parameters are not in `session.inspect`** (`params: null`). Verify by bouncing with the target
  track soloed and comparing **LUFS**, not peak: Kick EQ `input_gain` 0 → -6 changed LUFS -26.8 → -29.8 while the
  compressor after it held the peak (-8.6 → -9.0). Parameter ids are not the friendly names (`eq_7band` has
  `input_gain`, `hpf_on`, `low_shelf_gain`…; no `freq`/`gain`): list ids, ranges and units with
  `run --cmd engine.plugins` (the `plugins` subcommand prints names only).
- **`--start/--end` take seconds or time strings** (`9.23`, `0:09.230`, `samples:443077`), not bare sample numbers:
  `--start 443077` means 443077 s ("bounces are limited to 4 hours"). Inside commands, positions are samples
  unless written `{"seconds":x}` or as a time string.
- **Saving over a file:** `run --in S.scraft --save S.scraft` is refused without `--in-place`; `session.save` /
  `save_as` need `"replace":true`. Bounces overwrite silently. A `.scraft` copied without its `Audio Files/`
  folder opens with "missing media" warnings: copy the whole session folder.
- **Selection first:** `automation.write_to_current` / `write_to_all` refuse ("make an edit selection first");
  many `edit.*` commands act on the selection (`edit.select {tracks:[name],start,end}`). `clip.group` needs 2+ clips.
- **`track.color {tracks?, color}` takes `[r,g,b]` or a palette index**, not `"#rrggbb"`; colour is visible only
  in the UI (checked by screenshot).
- **Toggles without `value` flip state**, so a second run undoes the first: pass `{"value":true|false}`.
- **Headless transport does nothing** (`transport.play` → `{}`, no audio device). In the live app it plays even
  with `--no-audio` (`ui.inspect` → `playing:true`, position moves; `transport.stop` returns to the start).
- `info` cannot read `.mid` (use `file.import_midi`); `convert` cannot write MP3/AAC.
- **Live dialogs:** `ui.menu.invoke {path:"Track > New..."}` opens a dialog (`ui.inspect` → `dialog:"new_tracks"`);
  `ui.key {key:"Escape"}` closes it. Programmatic engine commands never open dialogs.

## Verify before reporting

Bounce and measure: `file.bounce_mix` / `run --bounce` print `peak_db`, `true_peak`, `lufs`, `seconds`; `info OUT.wav`
gives format and length. For structure, compare a named field of `session.inspect` before (after setup) and after.
For anything visual, `ui.screenshot {path}` in a live app and look at it.

## Where things are

| File in `reference/` | Read it for |
|---|---|
| `recipes.md` | 8 tested end-to-end recipes: import + bounce, arrange (split/trim/move/crossfade), mix with send + plugin measured, volume automation, markers, MIDI notes, convert/normalize, save/reopen |
| `docs-notes.md` | CLI subcommands and flags, exit codes, env vars, control protocol framing and methods, MCP tools and automation roots, file formats read/written, known gaps |
| `live-app.md` | live control, `ui.*` methods with parameters, what was checked on screen, hidden-display recipe |
| `command-catalogue.md` | all 483 ids with status (verified / read-ok / ran / skipped), params used and evidence |
| `newer-commands.md` | what changed between versions |
| `log.md` | dated learning log |

## Known gaps (0.18.0)

No `.ptx`/AAF/OMF; no MP3/AAC export; MIDI export drops imported controllers; recording, audio hardware and
third-party plugin UIs untested (no device or CLAP/VST3 plugins installed); 35 ids `ran` without an independent
read-back (UI-only state such as track pin/freeze/timebase, clip stacking order, solo safe, input monitor).
Repo `docs/gaps.md` has the current list.
