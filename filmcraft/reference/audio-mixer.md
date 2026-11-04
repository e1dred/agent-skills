# FilmCraft reference: audio and the mixer

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Mixer (verified 0.17.0, 2026-11-04)

- `mixer.inspect {}` → strips (`Audio 1`, `Mix`, any submixes) with `volumeDb`, `pan`, inserts and sends.
- `mixer.setValue {"strip":"A1","lane":"volume","value":-6}` → Audio 1 `volumeDb` 0.0 → -6.0.
- `mixer.setStrip {"strip":"A1","volumeDb":-3,"pan":0.2,"muted":false}` → volumeDb -3.0, pan 0.2.
- `mixer.addSubmix {"name":"Sub","channels":"Stereo"}` → `{id:16, ref:'S1'}`; use that `ref` in later calls.
  `mixer.deleteSubmix {"strip":"S1"}` removes it (strips go back to `Audio 1`, `Mix`).
- `mixer.addInsert {"strip":"A1","effect":"hard_limiter"}` → Audio 1 inserts 0 → 1. The value must be a real
  **audio effect id** from `effects.list {"kind":"Audio"}`, not a label such as `volume`.
- `mixer.setInsert {"strip":"A1","slot":0,"enabled":false}` → insert enabled true → false.
- `mixer.addSend {"strip":"A1","target":"S1"}` → `{send:0}`, sends 0 → 1. The target must be a submix that exists in
  the same run; `mixer.setSend {"strip":"A1","send":0,"levelDb":-10}` sets its level (send 0 at -10 dB).
- `mixer.removeSend {"strip":"A1","send":0}` returns ok; its effect was not captured in a readback.
- `clip.audioChannels {"format":"mono"}` refused ("select a clip with audio") in headless runs.

## Clip audio (first round)

- `clip.audioGain {"clips":[7],"mode":"set","db":-6}` → `{clips:1, gainDb:[{clip:7,gainDb:-6.0}]}`; the value
  survives save and reopen.
- `essentialSound.set {"clips":[7],"key":"volume.levelDb","value":-3}` needs an audio type first:
  `essentialSound.setType {"clips":[7],"type":"dialogue"}`, otherwise it answers "has no audio type; set one first".
