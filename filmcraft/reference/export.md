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

## Presets and the export queue (second round, verified 0.17.0, 2026-11-04)

- `export.presets.get {"name":"Match Source – Adaptive High Bitrate"}` → `{builtin:true, category:'Match Source',
  format:'h264', extension:'mp4'}`; `export.presets.favorite {"name":"…","favorite":true}` → favorite false → true.
- `export.formats {}` → 21 formats.
- `export.resolve {"path":"resolved.mp4","format":"h264","width":320,"height":180,"fps":25}` → `{frames:125,
  output:{fps:'25', height:180, channels:2, …}}` — resolves the settings without writing a file.
- `export.queue.add {"path":"queued.mp4","format":"h264","width":320,"height":180,"fps":25}` → `{added:[1]}`;
  `export.queue.list {}` → items with `id, path, format, sequence, progress`; `export.queue.start {"wait":true}` →
  progress 1.0 and a 419,604-byte file.
- `export.queue.cancel {"id":1}` returns the item list and nothing in it records the cancellation — do not rely on
  the readback; check whether the output file appears.
- Interchange, all written headless: `file.exportInterchange {"format":"fcpxml","path":"i.fcpxml"}` (1,914 bytes —
  its report said a graphic clip was **not supported**), `file.exportOtio {"path":"i.otio"}` (39,751),
  `file.exportFcp7Xml {"path":"i.xml"}` (27,052), `file.exportAle {"path":"i.ale"}` (295, `{clips:2}`),
  `file.exportOmf {"path":"i.omf"}` (270,015). Read the command's report: a format can drop items silently.

## Stills

`filmcraft-cli --project p.fcproj render --seconds 2 --out frame.png [--scale 0.5]` renders one Program frame.
Verified: 320×180 PNGs at 0.5, 1.5, 2 and 2.5 s (five to fifteen ms each). Use `render` to check a title, grade or
transition before exporting.

## Probing

`filmcraft-cli probe clip.mp4` → `{kind:"Movie", container:"MPEG-4", duration:762048000000, file_size,
video:{codec:"H.264 (High)", width:320, height:180, frame_rate:{num:25,den:1}, pixel_format, bitrate, color},
audio_streams:[{codec:"AAC", channels:1, sample_rate:44100}]}`.
Duration is in ticks (254,016,000,000/s). `probe --image-sequence` is for numbered stills only.
