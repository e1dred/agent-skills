---
name: filmcraft
description: Use when cutting or trimming video, adding titles and graphics, grading colour, mixing audio, exporting MP4/GIF or stills, when running filmcraft-cli, or when connecting to the FilmCraft app (storytold) on this machine
---

# FilmCraft

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

Field notes from first headless tasks, last tested on **FilmCraft 0.17.0** (Linux AppImage). FilmCraft is an
early-alpha, Premiere-style video editor in Rust. Every menu item and button is an engine *command*; the CLI, the
MCP server and the app's control channel run the same commands. If `filmcraft-cli --version` is newer, re-check
anything here before relying on it.

## Setup

- **CLI:** extract it from the AppImage (`filmcraft.appimage --appimage-extract`, copy `usr/bin/filmcraft-cli`
  somewhere stable); self-contained, no window. Never run `--version` on the AppImage itself.
- **Headless:** `filmcraft-cli --project p.fcproj exec <id> key=value …`; scripts are JSON lines and keep one session:
  `filmcraft-cli --project p.fcproj run script.jsonl [--save]` with lines `{"id":"…","params":{…}}`,
  or standalone `filmcraft-cli run` after `file.newProject`. Subcommands: `commands`, `describe`, `inspect`,
  `import`, `export`, `render`, `probe`.
- **Live app:** `filmcraft --control 9876` (or `FILMCRAFT_CONTROL_PORT`); the listener needs
  `FILMCRAFT_CONTROL_TOKEN` (64 hex characters) in the environment — without it it stays closed. Bridge with
  `filmcraft-cli mcp --bridge 127.0.0.1:9876`.
- **MCP:** `filmcraft-cli mcp` (headless) or `--bridge` (live).

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `projects-and-timeline.md` | Projects, importing media, sequences, playhead, razor and trim, markers, saving | Projects and media; Sequences; Cutting and trimming; Markers and saving; Other editing tools |
| `titles-and-graphics.md` | Text and shape layers, size/fit on small frames, reading layers back | Titles; Sizing and fitting; Layer properties |
| `export.md` | Export presets, MP4/GIF export, frame stills, probing media | Presets; Exporting; Stills; Probing |
| `newer-commands.md` | What each version added or changed | 0.17.0 |
| `log.md` | Dated log of what was tested when | Log |

## CLI essentials (verified)

```
filmcraft-cli commands --json                    # 716 commands: id, label, menu, params, enabled
filmcraft-cli describe file.import               # parameter docs for one command
filmcraft-cli --project p.fcproj inspect         # {project:{…}, sequence:{…}} as JSON
filmcraft-cli import clip.mp4 --project p.fcproj
filmcraft-cli --project p.fcproj export out.mp4 --scale 0.5 --quality 70
filmcraft-cli --project p.fcproj render --seconds 2 --out frame.png
filmcraft-cli probe clip.mp4                     # kind, duration (ticks), video/audio stream details
```

- A JSONL script keeps state: `file.newProject` → `file.import {"paths":["clip.mp4"]}` → `{"items":[1]}` →
  `file.newSequenceFromClip {"items":[1]}` → `{"clips":[6,7],"sequence":4}` → … → `file.saveAs {"path":"p.fcproj"}`.
- Pass `--project` on every later CLI call: without it each invocation is a fresh session.

## Traps

- **Times are ticks**, not frames: the sequence reports 762,048,000,000 for 3 s (254,016,000,000 ticks/s);
  `playhead.set` accepts `seconds`, `frame`, `time` or `timecode` and **snaps to the nearest frame** (1.5 s → frame 37).
- **A text layer at the default size overflows a small frame.** `graphics.newText` defaults to 100 px: on a 320×180
  sequence, "Hello FilmCraft" at `size:48` drew 334.7 px wide from x=40 and was cut at the right edge. Fit it by
  setting `size` (~32 → 223 px wide; checked in a render). Paragraph text with `box:[w,h]` wraps, but the box
  CLIPS lines that do not fit its height: `box:[240,60]` at size 40 showed only "Hello" (the second line was cut off),
  so make the box tall enough for every line (about 1.3 × size per line).
- **Ripple edits fail across a sync-locked track:** `timeline.trim` with `mode:"ripple"` answered "this edit would
  break sync: V2 is sync-locked and has a clip in the way" when a title sat on V2. Lock/unlock the other track first
  or trim without ripple.
- `probe --image-sequence` only accepts numbered stills; on a movie it errors.
- `--demo` opens the built-in demo project: it inspects and renders (a 1920×1080 frame at 1 s), exported fine only
  as far as tested; missing media exports as placeholder frames unless `--allow-offline` accepts them.
- `file.exportMedia` waits for its file unless `"wait":false`; the CLI `export` always waits.

## Verify before reporting

`inspect sequence` (clip starts/ends in frames, tracks, transitions, effects), `probe` for the exported file's
duration and codecs, and `render` a frame at the interesting times to look at. Frame counts: 3 s at 25 fps = 75
frames; a ripple trim of `-10` frames gave 65.
