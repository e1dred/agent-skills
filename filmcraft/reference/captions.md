# FilmCraft reference: captions and subtitles

Part of the filmcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Caption tracks and SRT (verified 0.17.0, 2026-11-04)

- `captions.newTrack {"format":"Subtitle","name":"English"}` → `{track:16}`, shown in the sequence as `C1`.
- `captions.add {"track":"C1","text":"First caption","seconds":0.2,"durationSeconds":1}` → `{caption:17}`; the
  exported SRT line is `00:00:00,200 --> 00:00:01,200`.
- `captions.setText {"caption":17,"text":"First edited"}` changes the text (read it back in the SRT);
  `captions.setTimes {"caption":17,"startSeconds":0.4,"endSeconds":1.2}` → SRT start `00:00:00,400`.
- `captions.move {"captions":[17],"deltaFrames":5}` → start `00:00:00,600` (5 frames = 50,803,200,000 ticks at
  25 fps); `captions.duplicate {"captions":[17],"deltaFrames":10}` → `{captions:[19]}`;
  `captions.delete {"captions":[18]}` → `{deleted:1}`.
- `captions.export {"path":"caps.srt","format":"srt","track":"C1"}` writes the file (95 bytes for two captions);
  `captions.import {"path":"caps.srt","name":"Imported"}` → `{captions:2, format:'SubRip (SRT)', track:19}`.
- `captions.setStyle {"track":"C1","size":24,"color":"#ffff00"}` returns ok, but the style lives in the project only
  and does not appear in an exported SRT — verify it in the Program monitor, not the file.
- Export the SRT (or read `sequence.inspect`) to prove any caption edit; the command replies alone are thin.
