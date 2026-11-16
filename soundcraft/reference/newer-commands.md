# Changes between versions

> **Versions:** baseline SoundCraft 0.18.0 (2026-11-06): 483 command ids, all run once headless
> (see `command-catalogue.md`). When a newer CLI is installed, diff `soundcraft-cli commands --json` ids and
> `params` against this baseline, run the new ids, and add a section here per version.

## 0.20.0 (checked 2026-11-11, from 0.18.0; 0.19.0 not tested on its own)
483 ids, none added or removed; 5 parameter docs changed in wording only (Beat Analysis, MusicXML, Punch Recording, Tempo Sync). Two recipes (demo bounce: 16,095,306 bytes, peak −4.347 dBFS, −19.371 LUFS; convert to 44.1 kHz/16-bit) are identical on both CLIs.

## 0.20.1 (checked 2026-11-15, from 0.20.0)
483 ids, none added or removed; audio formats now come from the shared craft-audio library. `info` / `convert` read **AC-3, E-AC-3 (`.ac3`, `.eac3`, `.ec3`), Opus, MOV, MKA and MPA** in addition to the old list (0.20.0 refused AC-3 with "no suitable format reader found"); `.aifc` is now listed as a write format (it already worked, but writes plain uncompressed AIFF data under the `.aifc` name).
- Compressed inputs report exact frame counts: Opus 96312 to 96000, AAC in MOV 97280 to 96000 for a 2 s tone; the "skipped bytes of junk" warning on `.mov` is gone. MP3 unchanged.
- An AC-3 file converted to WAV decodes to real audio (checked with ffprobe and peak/RMS), 24-bit stereo by default.
- A FLAC inside `.mka` now reports `"format":"Other"` instead of `"Flac"` (label only). `.wav` to `.wav` is byte-identical on both CLIs.
Not tested: 5.1 AC-3, opus or mka inside a `.scraft` session, recording.
