# FilmCraft reference: export and stills

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Presets (verified 0.17.0, 2026-11-04)

`filmcraft-cli export --list-presets` prints JSON: built-in and user presets with `name, category, format,
formatLabel, extension, frameSize, builtin`. Verified entries include "Match Source – Adaptive High Bitrate"
(H.264, mp4, bitrate adapts to frame size) in category "Match Source". Use `--preset "<name>"` or `--format h264|hevc|…`.

## Exporting

```sh
filmcraft-cli --project p.fcproj export out.mp4 --scale 0.5 --quality 70
filmcraft-cli --project p.fcproj export out.gif
```

- MP4: a 3 s 320×180 25 fps sequence exported at `--scale 0.5 --quality 70` → out.mp4, 3.018 s, 392,540 bytes
  (ffprobe: duration 3.018005).
- GIF: the same sequence after the razor/title edit → out.gif, 1,022,458 bytes.
- `--range entire|inOut|workArea` or `--start/--end` seconds; `--no-audio`; `--allow-offline` accepts placeholder
  frames for missing media. The CLI waits for the export; `file.exportMedia` waits too unless `"wait":false`.
- `file.exportMedia` parameters (from `describe`): `path`, `preset`, `settings`, `format`, `width/height/fps`,
  `bitrateKbps`, `bitrateMode`, `crf`, `scale`, `audio`, `quality`, `range`, `startSeconds`, `endSeconds`, `wait`.
- Interchange exports exist as separate commands (`file.exportFcpxml`, `file.exportEdl`, `file.exportAaf`, …) —
  not run here.

## Stills

`filmcraft-cli --project p.fcproj render --seconds 2 --out frame.png [--scale 0.5]` renders one Program frame.
Verified: 320×180 PNGs at 0.5, 1.5, 2 and 2.5 s (five to fifteen ms each). Use `render` to check a title, grade or
transition before exporting.

## Probing

`filmcraft-cli probe clip.mp4` → `{kind:"Movie", container:"MPEG-4", duration:762048000000, file_size,
video:{codec:"H.264 (High)", width:320, height:180, frame_rate:{num:25,den:1}, pixel_format, bitrate, color},
audio_streams:[{codec:"AAC", channels:1, sample_rate:44100}]}`.
Duration is in ticks (254,016,000,000/s). `probe --image-sequence` is for numbered stills only.
