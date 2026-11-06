# FilmCraft reference: log

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-11-04: first verified run (FilmCraft 0.17.0, Linux AppImage): CLI extracted; 716 commands listed. Headless with
  a 3 s ffmpeg-generated clip: file.newProject, file.import, file.newSequenceFromClip, playhead.set, timeline.razor,
  timeline.trim (ripple; sync-lock trap), trim.selectEditPoint + trim.forward, trim.applyDefaultTransition,
  clip.audioGain, essentialSound.setType/set, graphics.newText, graphics.set (size fit), boxed text, graphics.list,
  markers.add, file.save/saveAs, project/sequence.inspect, probe, export mp4/gif, render stills. Control channel and
  MCP documented from the repo, not exercised.
- 2026-11-04 (second round, FilmCraft 0.17.0): 60 command ids run headless, each with the same field read before and
  after — 37 verified, 7 read-ok, 9 no-effect, 4 refused, 3 blocked. Video and audio transitions, default transition,
  effect parameters and animation toggles, frame hold, timeline selection, project notes, the full mixer (values,
  strips, submixes, inserts, sends), captions (add/edit/times/move/duplicate/delete, SRT in and out), export presets,
  resolve, the export queue, and FCPXML/OTIO/FCP7 XML/ALE/OMF interchange. Keyframes at an arbitrary mediaTime and
  graphic-layer alignment did not work headless.
- 2026-11-04 (third round, FilmCraft 0.17.1): CLI refreshed; the 589 remaining ids run headless and, where a panel
  was needed, live over the bridge on a hidden display. After review (top-level "something changed" evidence was
  re-run for exact JSON paths; setup-contaminated title rows re-run with the baseline after setup): 81 verified,
  129 returned a result, 106 ran without a change to read back, 273 refused or blocked in the test project (reason kept).
  Later the same night: six retry passes on the 273 (real multicam angles, captions, presets, accumulated parameters,
  error-driven) → final for the 589: **90 verified**, 141 returned a result, 192 ran without a read-back, 166 refused,
  each with its last error and a category (needs a live panel, speech-to-text not in this build, microphone, file
  chooser). Rows whose only change was the saved copy's name were downgraded. Live retries stopped after file
  choosers reached the user's screen.
  Recorded in `command-catalogue.md` and `live-app.md`.
- 2026-11-06 (fourth round, 0.17.1 -> 0.18.0): 717 ids (+`presets.scan`); demo-project round identical apart from the new `maintainPitch` field; `clip.speedDuration` maintainPitch and `file.exportMedia` H.264 High 10 / Intra verified.
