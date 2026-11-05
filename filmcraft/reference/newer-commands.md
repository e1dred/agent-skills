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
