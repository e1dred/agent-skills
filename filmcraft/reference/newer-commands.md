# FilmCraft reference: newer commands

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## 0.17.0 (first look, 2026-11-04)

First version covered by this skill. `filmcraft-cli commands --json` lists **716 commands**; there is no changelog
in the repository root, so this file starts here. Commands verified so far are named in the other reference files.

## 0.17.1 (checked 2026-11-04)

Still **716 commands**, none added or removed. Parameter docs changed for `captions.import` (new `language`),
`graphics.setCharStyle` and `timeline.move`. Twelve earlier recipes (probe, playhead, razor, ripple trim, audio gain,
marker, title, opacity, transition, still, MP4 export, captions + SRT) behaved the same as on 0.17.0; new output fields
only: `probe` adds `color_assumed {matrix, primaries, transfer}`, command results add `warnings: []`.

## 0.18.0 (checked 2026-11-06)

`filmcraft-cli commands --json` lists **717 commands** (716 in 0.17.1): 1 added, none removed, 2 with changed parameters.
A scripted round (built-in `--demo` project: inspect, render a 1 s still, export a 0.5-scale MP4, probe; then a new
project from a still: import, sequence, save, export, reopen) ran on both versions. The still PNG is byte-identical;
both MP4s have identical frame MD5s (ffmpeg `framemd5`) and identical `probe` output, with only four container bytes
differing; the inspect JSON differs only by the new `maintainPitch` field on every clip.

- **`presets.scan {}`** (new) rescans the presets folder and imports `.prfpset` files → `{changed, files, imported, removed, skipped, warnings, errors}`; on a folder with none it answered `changed:false, files:0` (ran; no `.prfpset` was available to import).
- **`clip.speedDuration`** takes `maintainPitch` (Maintain Audio Pitch: time-stretches the audio instead of resampling; unchanged when left out). `{"clips":[5],"speed":200,"maintainPitch":true}` read back speed 1.0 → 2.0, maintainPitch false → true, durationFrames 150 → 75, and `inspect sequence` now reports `maintainPitch` on every clip.
- **`file.exportMedia`** takes `h264Profile` (`baseline|main|high|high10`) and `h264IntraOnly`, and `apvProfile` gained `4444-10`, `4444-12` and `400-10`. `{"format":"h264","settings":{"h264Profile":"high10","h264IntraOnly":true}}` exported a file ffprobe calls **High 10 Intra** (bitrate 15.6 Mbps vs 0.63 Mbps for the default High export); FilmCraft's own `probe` says only "H.264 (High 10)". `h264IntraOnly` alone, with the default profile, stayed High.
- Other 0.18.0 changes that matter headless: Premiere `.prfpset` presets import; AAF/OMF audio tracks keep their names and their `bitDepth` accepts `"24"`; EDL relinked with Align Timecode lands on the file's own time; TTML export writes the track language; the Metadata panel's Out Point is the last frame kept; image-sequence export reports the stills it wrote; time interpolation applies when a clip's frame rate differs from the sequence's; a missing project stops a save before it opens.

## 0.20.0 (checked 2026-11-11, from 0.18.0; 0.19.0 not tested on its own)

718 commands (+1), 14 with changed parameter docs (5 are labels: "Lumetri" → "Color Grading"). MP4 export and a 1 s still are byte-identical on both CLIs.
- **`lumetri.exportCube {"clip":6,"path":"/abs/grade.cube","size":5}`** writes the clip's grade as a 3D LUT (`LUT_3D_SIZE 5`, 125 rows). A clip without an enabled grade is refused ("the clip has no enabled Color Grading to export").
- `file.exportMedia {"format":"mp3"}` is new (0.18.0: `unknown format`).
- `file.newColorMatte`, `newBarsAndTone`, `newBlackVideo`, `newTransparentVideo`, `newCountingLeader`, `newAdjustmentLayer`, `newSequence` take `bin` (a bin id; an unknown bin is refused). 0.18.0 ignored it.
- `sequence.settings {"videoDisplay":"frames"|"timecode"|"feet35"|"feet16"}` → `sequence.inspect .settings.display` ("Frames", "Feet + Frames 35mm").
