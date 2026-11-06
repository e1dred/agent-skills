# SoundCraft 0.18.0 — 8 tested recipes

All run with `HOME=$OUT/home SOUNDCRAFT_NO_PREFS=1`, CLI `~/AppImages/soundcraft-cli`,
`$OUT=/scratch`.
Each was run for real; the read-back on the last line is from that run.

## (a) New session → import audio onto a track → bounce
```sh
scl run --cmd 'session.new={"name":"Recipe A","sample_rate":48000,"bit_depth":24}' \
  --cmd 'file.import_audio={"path":"'$OUT'/media/sine440_48k24_mono.wav","new_tracks":true}' \
  --bounce $OUT/recipes/a.wav --inspect --compact
```
Read-back: `file.import_audio: {"imported":[{"channels":1,"clip":3,"frames":96000,"source":1,"track":2}]}`;
bounce `{"peak_db":-15.0,"seconds":2.0}`; inspect `"name":"Recipe A","length_samples":96000`.
(Import defaults to new tracks; mono rides the stereo main bus, hence -15 dBFS for a -12 dBFS file.)

## (b) Arrange: split, trim, move, crossfade, bounce
```sh
scl run --demo --cmd 'edit.separate={"at":600000}' \
  --cmd 'edit.trim_clip={"clip":4,"end":1000000}' \
  --cmd 'edit.move_clips={"clips":[18],"by":10000}' \
  --cmd 'edit.fades_create={"clip":4,"side":"out","length":4800}' \
  --cmd 'edit.fades_create={"clip":18,"side":"in","length":4800}' \
  --bounce $OUT/recipes/b.wav --inspect --compact
```
Read-back: `edit.separate: {"separated":1}`; `edit.trim_clip: {"end":600000,"start":443077}`;
`edit.move_clips: {"by":10000,"moved":1}`; each fade `{"fades":1}`; bounce `peak -4.78 dBFS`.
(Trim after separate shortened the second half; the two fades form a crossfade at the cut.)

## (c) Mix: volume/pan/mute, bus send, plugin parameter change — measured
```sh
scl run --demo --bounce $OUT/recipes/c_before.wav --start 0:09.230 --end 0:27.692
scl run --demo --cmd 'mix.volume={"track":"Kick","db":-12}' \
  --cmd 'mix.pan={"track":"Snare","pan":-0.4}' --cmd 'mix.mute={"track":"Hats","value":true}' \
  --cmd 'mix.send={"track":"Kick","slot":0,"bus":"Verb"}' \
  --cmd 'mix.send_level={"track":"Kick","slot":0,"db":-12}' \
  --cmd 'mix.insert_param={"track":"Kick","slot":0,"param":"input_gain","value":-6}' \
  --bounce $OUT/recipes/c_after.wav --start 0:09.230 --end 0:27.692
```
Read-back: `mix.send: {"bus":1,"slot":0}`; `mix.insert_param: {"value":-6.0}`;
bounce before peak -4.70 / RMS -19.96 dBFS, after peak -5.12 / RMS -20.51 dBFS.
(`--start/--end` take seconds/time strings, not sample numbers.)

## (d) Volume automation breakpoints
```sh
scl run --demo --cmd 'automation.set_point={"track":"Kick","param":"volume","at":443077,"value":0}' \
  --cmd 'automation.set_point={"track":"Kick","param":"volume","at":600000,"value":-12}' \
  --cmd 'automation.set_point={"track":"Kick","param":"volume","at":800000,"value":-3}' \
  --bounce $OUT/recipes/d.wav --start 0:09.230 --end 0:20.000 --inspect --compact
```
Read-back: inspect has `"automation":[{"param":"volume","points":3}]`; bounce `peak -4.83 dBFS`.
(`automation.clear` needs explicit track/param/start/end; a bare call is a no-op.)

## (e) Markers / memory locations
```sh
scl run --demo --cmd 'markers.add={"name":"Chorus 2","at":2400000}' \
  --cmd 'markers.edit={"number":5,"name":"Final Chorus"}' \
  --cmd 'markers.recall={"number":5}' --inspect --compact
```
Read-back: `markers.add: {"id":33,"number":5}`; `markers.recall: {"at":2400000}`; inspect marker 5 is
`{"name":"Final Chorus","number":5,"start":2400000}`.

## (f) MIDI track with notes
```sh
scl run --demo --cmd 'track.new={"kind":"midi","name":"Recipe MIDI"}' \
  --cmd 'midi.new_clip={"track":"Recipe MIDI","start":0,"length":96000}' --inspect --compact
# take "clip":34 from that output, then:
scl run --demo --cmd 'track.new={"kind":"midi","name":"Recipe MIDI"}' \
  --cmd 'midi.new_clip={"track":"Recipe MIDI","start":0,"length":96000}' \
  --cmd 'midi.note_add={"clip":34,"pitch":60,"start_ticks":0,"length_ticks":480,"velocity":100}' \
  --cmd 'midi.note_add={"clip":34,"pitch":64,"start_ticks":480,"length_ticks":480,"velocity":90}' \
  --cmd 'midi.notes={"clip":34}'
```
Read-back: `midi.notes: {"notes":[{"length":480,"pitch":60,"start":0,"velocity":100},{"length":480,"pitch":64,"start":480,"velocity":90}]}`.
(Clip ids are engine-assigned: 34 here after one `track.new` on the demo.)

## (g) Convert / normalize a file
```sh
scl convert $OUT/media/sine440_48k24_mono.wav $OUT/recipes/g.wav --rate 44100 --bit-depth 16 --normalize
scl info $OUT/recipes/g.wav --compact
```
Read-back: `{"channels":1,"format":"Wav","frames":88200,"sample_format":"Int16","sample_rate":44100,"seconds":2.0}`;
measured peak -0.1 dBFS (was -12). Dithers automatically because 24→16 loses resolution.

## (h) Save, reopen and `info` a .scraft session
```sh
scl run --demo --save $OUT/recipes/h.scraft
scl info $OUT/recipes/h.scraft
```
Read-back: save `{"audio_files_written":5,"path":".../h.scraft"}`; `info` summary:
`SESSION NAME: h`, `SAMPLE RATE: 48000`, `BIT DEPTH: Int24`, `# OF AUDIO TRACKS: 5`,
`# OF AUDIO CLIPS: 11`, `# OF AUDIO FILES: 5`, and the five `Audio Files/*.wav` names.

## Notes
- `session.save` refuses an existing path without `replace:true`; use a new path or replace.
- `file.bounce_mix` returns peak/LUFS/seconds, so it doubles as the verification tool.
- Everything above also works through MCP `execute`/`inspect_session`; see command-catalogue.md.
