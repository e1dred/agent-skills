# FilmCraft reference: projects and timeline

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Projects and media (verified 0.17.0, 2026-11-04)

A JSONL script keeps one session; `--project` on later CLI calls reopens the saved project.

```jsonl
{"id":"file.newProject","params":{}}
{"id":"file.import","params":{"paths":["clip.mp4"]}}
{"id":"file.newSequenceFromClip","params":{"items":[1]}}
{"id":"file.saveAs","params":{"path":"p.fcproj"}}
```

- `file.newProject` → `{"name":"Untitled","revision":2}`.
- `file.import {"paths":[…]}` → `{"items":[1],"errors":[]}`; `project.inspect` lists the item
  (`{item:1, name:"clip.mp4", type:"Movie", duration:762048000000}` for a 3 s clip).
- `file.newSequenceFromClip {"items":[1]}` → `{"clips":[6,7],"sequence":4}` — a video clip and its linked audio.
  The sequence inherits the clip's 320×180/25 fps settings (75 frames for 3 s).
- `file.saveAs {"path":"p.fcproj"}` / `file.save {}`; sizes were ~4–9 KB for these test projects.
- `file.openDemoProject {}` (and the CLI's `--demo`) opens the built-in demo project; `inspect` lists its bins, and
  `render --seconds 1` produced a 1920×1080 frame. Export from the demo was not run.
- `inspect project` and `inspect sequence` are read-only JSON dumps (CLI subcommand); the same data comes from
  `project.inspect` and `sequence.inspect` commands in a script. Sequence keys worth reading: `video[].items[]`
  (`clip, startFrame, endFrame, sourceIn, sourceOut, speed, effects`), `audio[]`, `markers[]`, `transitions[]`,
  `settings.frame_rate/width/height`.

## Sequences

- `file.newSequence {"name","width","height","fps","sampleRate","fromItem"?,"fromItems"?}` creates an empty sequence
  or one containing items (params from `describe`; not run separately here).
- `sequence.inspect` (CLI `inspect sequence`) for the active sequence; `sequence.settings`, `sequence.open`,
  `sequence.close` exist (not run).
- Frame math used throughout: `durationFrames` and clip `startFrame`/`endFrame` are frame counts; `duration` is ticks
  (3 s = 762,048,000,000 ticks at 25 fps — 254,016,000,000 ticks/s).

## Cutting and trimming

- `playhead.set {"seconds":1.5}` → `{time:375943680000}` (frame 37); it snaps to the nearest frame.
- `timeline.razor {"time":381024000000,"track":2,"clip":6}` → `{"cuts":2}`; the V1 clip split into
  `(6, 0–37)` and `(8, 37–75)` (the linked audio was cut too).
- `timeline.trim {"clip":6,"edge":"out","mode":"ripple","deltaFrames":-10}` → `{delta:-101606400000}`; the clip
  went 75 → 65 frames. It needs `clip` + `edge`; `mode:"regular|ripple"`, `delta`/`deltaFrames`.
  **With a clip on a sync-locked track in the way it fails:** "this edit would break sync: V2 is sync-locked and has
  a clip in the way" — unlock that track or use regular trim.
- Selection-based trimming keeps state only inside one run: `trim.selectEditPoint {"clip":6,"edge":"out","kind":"ripple"}`
  → `{editPoints:[{clip:6,kind:"ripple",out:true},{clip:7,…}]}`, then `trim.forward {}` → `{applied:[10160640000]}`
  (one frame; 65 → 66). In a later CLI invocation it says "no edit points selected".
- `trim.applyDefaultTransition {"clips":[6]}` → `{transitions:[15,16]}` (two transition ids);
  `trim.backward|forward|backwardMany|forwardMany|toggleType` nudge/change the selected trim.
- `clip.audioGain {"clips":[7],"mode":"set","db":-6}` → `{clips:1, gainDb:[{clip:7,gainDb:-6.0}]}`; after
  `file.save` and a reopen, `sequence.inspect` shows the audio clip's `gainDb` -6.0.
- `essentialSound.set` needs an audio type first: without `essentialSound.setType {"clips":[7],"type":"dialogue"}`
  it answers "clip `testclip.mp4` has no audio type; set one first". With the type set,
  `essentialSound.set {"clips":[7],"key":"volume.levelDb","value":-3}` → `{clips:1}`; `essentialSound.inspect`
  then lists the clip's settings block (clarity, volume…).

## Markers and saving

- `markers.add {"target":"program","name":"Review here","comment":"checked"}` → `{marker:14}`; one marker then
  appears in `sequence.inspect.markers`. `markers.addRange`, `markers.addChapter`, `markers.edit` exist (not run).
- `file.save {}` after edits keeps the project at its current path; `file.saveAs` picks a new one.

## Other editing tools (named; not run here)

`timeline.place` / `timeline.delete` / `timeline.select` / `timeline.move` / `timeline.roll` / `timeline.slip` /
`timeline.slide` / `timeline.rateStretch`, `playhead.step` / `playhead.start` / `playhead.end`, `markers.markIn` /
`markers.markOut`, `effects.apply` / `effects.remove` / `effects.setParam` / `effects.addKeyframe`,
`captions.newTrack` / `captions.add` / `captions.split` / `captions.setText`, `source.open` / `source.insert`,
`edit.undo` / `edit.redo` / `edit.cut` / `edit.copy` / `edit.paste`, `file.open`,
`file.newProjectFromTemplate`, `file.importImageSequence`, `file.exportFrame`, `file.exportFcpxml`,
`export.presets.list`, `sequence.settings`. Parameter docs come from `filmcraft-cli describe`; none was exercised
in the first round.
