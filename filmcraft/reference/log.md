# FilmCraft reference: log

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Log

- 2026-11-04: first verified run (FilmCraft 0.17.0, Linux AppImage): CLI extracted; 716 commands listed. Headless with
  a 3 s ffmpeg-generated clip: file.newProject, file.import, file.newSequenceFromClip, playhead.set, timeline.razor,
  timeline.trim (ripple; sync-lock trap), trim.selectEditPoint + trim.forward, trim.applyDefaultTransition,
  clip.audioGain, essentialSound.setType/set, graphics.newText, graphics.set (size fit), boxed text, graphics.list,
  markers.add, file.save/saveAs, project/sequence.inspect, probe, export mp4/gif, render stills. Control channel and
  MCP documented from the repo, not exercised.
