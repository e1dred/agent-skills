# SoundCraft command catalogue (0.18.0) — 483 ids

Totals: **368 verified**, **78 read-ok**, **35 ran**, **2 skipped**.
`verified` = a named field in `session.inspect` / `setup.preferences`, or a bounce measurement, changed as expected (before taken after setup); `read-ok` = a query returned real data; `ran` = accepted, no independent read-back headless; `skipped` = needs hardware or plugins not installed. Paths `/scratch/…` were test files.

## session (11) — verified 8, read-ok 3

| id | status | params used | evidence |
|---|---|---|---|
| `session.new` | verified | `{"name": "Test Session", "sample_rate": 44100, "bit_depth": 16}` | name: "demo" → "Test Session" |
| `session.open` | verified | `{"path": "/scratch/demo.scraft"}` | name: "Blank" → "demo" |
| `session.close` | verified | `{}` | name: "demo" → "Untitled" |
| `session.save` | verified | `{"path": "/scratch/saves/save.scraft", "replace": true}` | file:/scratch/saves/save.scraft: missing → {"name": "save", "tracks": 9, "track0": "KickSaved"} |
| `session.save_as` | verified | `{"path": "/scratch/saves/save_as.scraft", "replace": true}` | file:/scratch/saves/save_as.scraft: missing → {"name": "save_as", "tracks": 9, "track0": "Kick"} |
| `session.save_copy` | verified | `{"path": "/scratch/saves/save_copy.scraft", "replace": true}` | file:/scratch/saves/save_copy.scraft: missing → {"name": "save_copy", "tracks": 9, "track0": "Kick"} |
| `session.save_template` | verified | `{"path": "/scratch/saves/save_template.scraft", "replace": true}` | file:/scratch/saves/save_template.scraft: missing → {"name": "demo", "tracks": 9, "track0": "Kick"} |
| `session.revert` | verified | `{}` | tracks[0].name: "TempName" → "Kick" |
| `session.inspect` | read-ok | `{}` | :  → {"bit_depth": "Int24", "busses": [{"format": "Stereo", "id": 1, "name": "Verb"}], "dirty": false, "edit_mode": "Slip", "frame_rate": "… |
| `session.format_time` | read-ok | `{"at": 96000, "format": "timecode"}` | :  → {"text": "00:00:02:00"} |
| `session.audio_health` | read-ok | `{}` | :  → {"active_audio_end_samples": 2682432, "active_audio_end_seconds": 55.884, "audio_clips": 11, "healthy": true, "issue_count": 0, "issue… |

## file (17) — verified 15, read-ok 2

| id | status | params used | evidence |
|---|---|---|---|
| `file.import_audio` | verified | `{"path": "/scratch/media/stereo_44k16.wav"}` | tracks.len: 9 → 10 |
| `file.import_midi` | verified | `{"path": "/scratch/media/four_notes.mid"}` | tracks.len: 9 → 10 |
| `file.import_video` | verified | `{"path": "/scratch/media/test_movie.mp4"}` | tracks.len: 9 → 10 |
| `file.bounce_mix` | verified | `{"path": "/scratch/out/bounce.wav"}` | file:/scratch/out/bounce.wav: missing → {"peak_dbfs": -4.78, "rms_dbfs": -21.55, "channels": 2, "rate": 48000, "frames": 2682432} |
| `file.bounce_stems` | verified | `{"dir": "/scratch/out/stems"}` | file:/scratch/out/stems: missing → demo - Bass.wav, demo - Hats.wav, demo - Keys.wav, demo - Kick.wav, demo - Lead.wav, demo - Pad.wav |
| `file.export_midi` | verified | `{"path": "/scratch/out/midi.mid"}` | file:/scratch/out/midi.mid: missing → 1606 bytes, 3 MTrk |
| `file.export_session_text` | verified | `{"path": "/scratch/out/session.txt", "replace": true}` | file:/scratch/out/session.txt: missing → 1898 bytes, head=SESSION NAME:	demo\|SAMPLE RATE:	48000\|BIT DEPTH:	Int24\|TIMEC |
| `file.export_clips` | verified | `{"dir": "/scratch/out/clips", "clips": [4]}` | file:/scratch/out/clips: missing → Kick-2.wav, Kick-3.wav, Kick.wav |
| `file.export_selected_tracks_as_session` | verified | `{"path": "/scratch/out/sel.scraft", "tracks": ["Kick"], "replace": true}` | file:/scratch/out/sel.scraft: missing → {"name": "sel", "tracks": 2, "track0": "Kick"} |
| `file.export_sibelius` | verified | `{"path": "/scratch/out/score.musicxml", "tracks": ["Keys"]}` | file:/scratch/out/score.musicxml: missing → 28799 bytes, <?xml version="1.0" encoding="UTF-8" standalone="n |
| `file.send_to_sibelius` | verified | `{"path": "/scratch/out/send.musicxml", "tracks": ["Keys"]}` | file:/scratch/out/send.musicxml: missing → 28799 bytes, <?xml version="1.0" encoding="UTF-8" standalone="n |
| `file.print_score` | verified | `{"path": "/scratch/out/score.svg", "tracks": ["Keys"]}` | file:/scratch/out/score.svg: missing → 55417 bytes, <svg xmlns="http://www.w3.org/2000/svg" width="794 |
| `file.score_setup` | read-ok | `{"title": "Test Score"}` | :  → {"bars_per_system": 4, "composer": "", "show_track_names": true, "title": "Test Score"} |
| `file.export_clip_groups` | verified | `{"path": "/scratch/out/g.scgrp", "clips": [4]}` | file:/scratch/out/g.scgrp: missing → 922 bytes |
| `file.import_clip_groups` | verified | `{"path": "/scratch/out/g.scgrp"}` | tracks[0].clips.len: 3 → 4 |
| `file.get_info` | read-ok | `{}` | :  → {"bit_depth": "Int24", "busses": [{"format": "Stereo", "id": 1, "name": "Verb"}], "dirty": false, "edit_mode": "Slip", "frame_rate": "… |
| `file.import_session_data` | verified | `{"path": "/scratch/out/data.scraft", "tracks": ["Imp2"]}` | tracks.len: 10 → 11 |

## app (1) — ran 1

| id | status | params used | evidence |
|---|---|---|---|
| `app.quit` | ran | `{}` | query \| echo/state only, no independent read-back |

## edit (94) — verified 76, read-ok 16, ran 2

| id | status | params used | evidence |
|---|---|---|---|
| `edit.undo` | verified | `{}` | tracks[0].name: "UndoMe" → "Kick" |
| `edit.redo` | verified | `{}` | tracks[0].name: "Kick" → "RedoMe" |
| `edit.restore_last_selection` | verified | `{}` | selection.end: 48000 → 96000 |
| `edit.cut` | verified | `{}` | tracks[0].clips.len: 3 → 2 |
| `edit.copy` | read-ok | `{}` | :  → {"clips": 1, "length": 886154} |
| `edit.paste` | verified | `{}` | tracks[0].clips[1].end: 2215385 → 2000000 |
| `edit.clear` | verified | `{}` | tracks[0].clips.len: 3 → 2 |
| `edit.cut_clip_gain` | verified | `{}` | tracks[0].clips[0].gain_db: -6.0 → 0.0 |
| `edit.clear_clip_gain` | verified | `{}` | tracks[0].clips[0].gain_db: -6.0 → 0.0 |
| `edit.cut_all_automation` | verified | `{"tracks": ["Kick"], "start": 0, "end": 4800000}` | tracks[0].automation.len: 1 → 0 |
| `edit.clear_all_automation` | verified | `{"tracks": ["Kick"], "start": 0, "end": 4800000}` | tracks[0].automation.len: 1 → 0 |
| `edit.clear_pan_automation` | verified | `{"tracks": ["Kick"], "start": 0, "end": 4800000}` | tracks[0].automation.len: 1 → 0 |
| `edit.clear_plugin_automation` | verified | `{"tracks": ["Kick"], "start": 0, "end": 4800000}` | tracks[0].automation.len: 1 → 0 |
| `edit.paste_repeat_to_fill` | verified | `{}` | tracks[0].clips[1].id: 18 → 33 |
| `edit.select_all` | verified | `{}` | selection.end: 443072 → 2682432 |
| `edit.select` | verified | `{"tracks": ["Bass"], "start": 0, "end": 48000}` | selection.end: 443072 → 48000 |
| `edit.select_none` | verified | `{}` | selection.end: 1329231 → 443077 |
| `edit.selection_to_timeline` | ran | `{}` | no pref change |
| `edit.timeline_to_selection` | ran | `{}` | no pref change |
| `edit.move_selection_left` | verified | `{}` | selection.end: 1329231 → 886154 |
| `edit.move_selection_right` | verified | `{}` | selection.end: 1329231 → 2215385 |
| `edit.halve_selection` | verified | `{}` | selection.end: 1329231 → 886154 |
| `edit.double_selection` | verified | `{}` | selection.end: 1329231 → 2215385 |
| `edit.extend_selection_up` | verified | `{}` | selection.tracks.len: 1 → 2 |
| `edit.extend_selection_down` | verified | `{}` | selection.tracks.len: 1 → 2 |
| `edit.remove_selection_top` | verified | `{}` | selection.tracks.len: 1 → 0 |
| `edit.remove_selection_bottom` | verified | `{}` | selection.tracks.len: 1 → 0 |
| `edit.duplicate` | verified | `{}` | tracks[0].clips[1].id: 18 → 33 |
| `edit.repeat` | verified | `{"count": 1}` | tracks[0].clips[1].id: 18 → 33 |
| `edit.shift` | verified | `{"by": 48000, "later": true}` | tracks[0].clips[0].start: 443077 → 491077 |
| `edit.insert_silence` | verified | `{}` | tracks[0].clips[0].start: 443077 → 1329231 |
| `edit.separate` | verified | `{"at": 600000}` | tracks[0].clips.len: 3 → 4 |
| `edit.separate_on_grid` | verified | `{}` | tracks[0].clips.len: 3 → 130 |
| `edit.separate_at_transients` | verified | `{"sensitivity": 0.5}` | tracks[0].clips.len: 3 → 50 |
| `edit.heal` | verified | `{}` | tracks[0].clips.len: 3 → 2 |
| `edit.trim_to_selection` | verified | `{}` | tracks[0].clips[0].start: 443077 → 500000 |
| `edit.trim_start_to_insertion` | verified | `{}` | tracks[0].clips[0].start: 443077 → 500000 |
| `edit.trim_end_to_insertion` | verified | `{}` | tracks[0].clips[0].end: 1329231 → 1000000 |
| `edit.trim_to_file_boundaries` | verified | `{"clips": [4]}` | tracks[0].clips[0].start: 443077 → 0 |
| `edit.trim_to_fill_selection` | verified | `{}` | tracks[0].clips[1].end: 2215385 → 2000000 |
| `edit.mute_clips` | verified | `{"clips": [4]}` | tracks[0].clips[0].muted: false → true |
| `edit.copy_to_new_playlist` | verified | `{}` | tracks[0].playlists: 1 → 2 |
| `edit.strip_silence` | verified | `{"threshold_db": -40}` | tracks[0].clips.len: 3 → 19 |
| `edit.fades_create` | verified | `{"clip": 4, "side": "in", "length": 4800}` | tracks[0].clips[0].fade_in: 0 → 4800 |
| `edit.fades_delete` | verified | `{}` | tracks[0].clips[0].fade_in: 4800 → 0 |
| `edit.fade_to_start` | verified | `{}` | tracks[0].clips[0].fade_in: 0 → 156923 |
| `edit.fade_to_end` | verified | `{}` | tracks[0].clips[0].fade_out: 0 → 729231 |
| `edit.nudge` | verified | `{"direction": 1, "count": 1}` | tracks[0].clips[0].start: 443077 → 491077 |
| `edit.mode` | verified | `{"mode": "grid"}` | edit_mode: "Slip" → "Grid" |
| `edit.snap_to_grid` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `edit.shuffle_lock` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `edit.tool` | verified | `{"tool": "grabber"}` | tool: "Smart" → "Grabber" |
| `edit.move_clips` | verified | `{"clips": [4], "by": 48000}` | tracks[0].clips[0].start: 443077 → 491077 |
| `edit.trim_clip` | verified | `{"clip": 4, "start": 400000}` | tracks[0].clips[0].start: 443077 → 400000 |
| `edit.consolidate` | verified | `{}` | sources.len: 5 → 6 |
| `edit.cut_pan_automation` | verified | `{"tracks": ["Kick"], "start": 0, "end": 4800000}` | tracks[0].automation.len: 1 → 0 |
| `edit.cut_plugin_automation` | verified | `{"tracks": ["Kick"], "start": 0, "end": 4800000}` | tracks[0].automation.len: 1 → 0 |
| `edit.copy_all_automation` | read-ok | `{}` | :  → {"lanes": 1, "length": 886154} |
| `edit.copy_pan_automation` | read-ok | `{}` | :  → {"lanes": 1, "length": 886154} |
| `edit.copy_plugin_automation` | read-ok | `{}` | :  → {"lanes": 1, "length": 886154} |
| `edit.copy_clip_gain` | read-ok | `{}` | :  → {"length": 886154, "points": 2} |
| `edit.paste_clip_gain` | verified | `{}` | tracks[0].clips[1].gain_db: 0.0 → -6.0 |
| `edit.copy_clip_effects` | read-ok | `{"clips": [4]}` | :  → {"clips": 1, "copied": 1, "removed": 0} |
| `edit.cut_clip_effects` | read-ok | `{"clips": [4]}` | :  → {"clips": 1, "copied": 1, "removed": 1} |
| `edit.clear_clip_effects` | read-ok | `{"clips": [4]}` | :  → {"clips": 1, "copied": 1, "removed": 1} |
| `edit.paste_clip_effects` | read-ok | `{"clips": [18]}` | :  → {"clips": 1} |
| `edit.paste_merge_midi` | verified | `{"tracks": ["Keys"], "at": 480000}` | notes.len: 180 → 360 |
| `edit.paste_merge_markers` | verified | `{"at": 96000}` | markers.len: 4 → 8 |
| `edit.paste_to_current_automation` | verified | `{}` | tracks[0].automation[0].points: 1 → 3 |
| `edit.play_timeline` | read-ok | `{}` | :  → {"end": 1329231, "start": 443077} |
| `edit.duplicate_extend` | verified | `{}` | tracks[0].clips[1].id: 18 → 33 |
| `edit.extend_up_to_members` | verified | `{}` | selection.tracks.len: 1 → 3 |
| `edit.extend_down_to_members` | verified | `{}` | selection.tracks.len: 1 → 3 |
| `edit.marker_lane_move_up` | read-ok | `{}` | :  → {"lanes": [1, 1], "markers": [1, 2, 3, 4]} |
| `edit.marker_lane_move_down` | read-ok | `{}` | :  → {"lanes": [2, 2], "markers": []} |
| `edit.marker_lane_extend_up` | read-ok | `{}` | :  → {"lanes": [1, 1], "markers": [1, 2, 3, 4]} |
| `edit.marker_lane_extend_down` | read-ok | `{}` | :  → {"lanes": [1, 2], "markers": [1, 2, 3, 4]} |
| `edit.space_clips` | verified | `{"clips": [4, 18], "gap": 4800}` | tracks[0].clips[1].start: 1329231 → 1334031 |
| `edit.snap_next` | verified | `{"clips": [4]}` | tracks[0].clips[0].start: 443077 → 453077 |
| `edit.snap_previous` | verified | `{"clips": [18]}` | tracks[0].clips[1].start: 1339231 → 1329231 |
| `edit.copy_to_target_playlist` | verified | `{}` | tracks[0] playlist 1 clips.len: 0 → 1 |
| `edit.copy_to_duplicate_playlist` | verified | `{}` | tracks[0].playlists: 1 → 2 |
| `edit.move_to_target_playlist` | verified | `{}` | tracks[0].clips.len: 3 → 2 |
| `edit.move_to_new_playlist` | verified | `{}` | tracks[0].playlists: 1 → 2 |
| `edit.move_to_duplicate_playlist` | verified | `{}` | tracks[0].playlists: 1 → 2 |
| `edit.tce_to_timeline` | verified | `{"clip": 4, "start": 443077, "end": 1000000}` | tracks[0].clips[0].length: 886154 → 556923 |
| `edit.automation_coalesce_volume_to_clip_gain` | verified | `{"tracks": ["Kick"]}` | tracks[0].clips[0].gain_db: 0.0 → -6.0 |
| `edit.automation_coalesce_clip_gain_to_volume` | verified | `{"tracks": ["Kick"]}` | tracks[0].automation.len: 0 → 1 |
| `edit.automation_trim_to_all` | verified | `{}` | tracks[0].automation[0].points: 1 → 5 |
| `edit.automation_glide_to_all` | verified | `{}` | tracks[0].automation[0].points: 1 → 5 |
| `edit.automation_glide_pan` | verified | `{}` | tracks[0].automation[0].points: 1 → 5 |
| `edit.tab` | verified | `{"back": false}` | selection.end: 480000 → 1329231 |
| `edit.copy_audio_as_midi` | read-ok | `{"track": "Kick", "start": 443077, "end": 600000}` | :  → {"length": 156923, "notes": 6} |
| `edit.strip_silence_preview` | read-ok | `{"threshold_db": -40}` | :  → {"tracks": [{"ranges": [[443077, 465550], [512062, 548589], [553600, 576318], [622830, 659357], [664368, 687086], [733598, 770125], [7… |

## view (97) — verified 96, read-ok 1

| id | status | params used | evidence |
|---|---|---|---|
| `view.zoom_in` | verified | `{}` | zoom.samples_per_px: 1967.4514285714286 → 983.7257142857143 |
| `view.zoom_out` | verified | `{}` | zoom.samples_per_px: 1967.4514285714286 → 3934.902857142857 |
| `view.zoom_by` | verified | `{"factor": 2}` | zoom.samples_per_px: 1967.4514285714286 → 983.7257142857143 |
| `view.zoom_set` | verified | `{"samples_per_px": 500}` | zoom.samples_per_px: 1967.4514285714286 → 500.0 |
| `view.zoom_preset` | verified | `{"preset": 1, "store": true}` | edit.zoom.presets[0]: 64.0 → 1967.4514285714286 |
| `view.zoom_to_selection` | verified | `{"width_px": 1200}` | zoom.samples_per_px: 1967.4514285714286 → 738.4616666666667 |
| `view.zoom_fit` | verified | `{"width_px": 1200}` | zoom.samples_per_px: 1967.4514285714286 → 2347.128 |
| `view.scroll` | verified | `{"to": 96000}` | zoom.scroll: 0 → 96000 |
| `view.waveform_zoom` | verified | `{"factor": 2}` | edit.zoom.waveform_zoom: 1.0 → 2.0 |
| `view.ruler` | verified | `{"ruler": "timecode", "visible": true}` | edit.rulers.len: 5 → 6 |
| `view.main_counter` | verified | `{"format": "timecode"}` | edit.main_counter: "BarsBeats" → "Timecode" |
| `view.sub_counter` | verified | `{"format": "timecode"}` | edit.sub_counter: "Samples" → "Timecode" |
| `view.grid` | verified | `{"format": "min_secs"}` | edit.grid.Note: {"dotted": false, "triplet": false, "value": "Sixteenth"} → "<missing>" |
| `view.grid_lines` | verified | `{"value": false}` | edit.grid_lines: true → false |
| `view.nudge` | verified | `{"format": "timecode"}` | edit.nudge.Seconds: 1.0 → "<missing>" |
| `view.edit_comments` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_mic_preamps` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_instruments` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_inserts_ae` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_inserts_fj` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_sends_ae` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_sends_fj` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_io` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_object` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_realtime_properties` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_track_color` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_marker_controls` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_pinned_tracks` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.edit_all` | verified | `{}` | edit.flags.len: 5 → 19 |
| `view.edit_minimal` | verified | `{}` | edit.flags.len: 19 → 5 |
| `view.ruler_timecode2` | verified | `{"visible": true}` | edit.rulers.len: 5 → 6 |
| `view.ruler_markers2` | verified | `{"visible": true}` | edit.rulers.len: 5 → 6 |
| `view.ruler_markers3` | verified | `{"visible": true}` | edit.rulers.len: 5 → 6 |
| `view.ruler_markers4` | verified | `{"visible": true}` | edit.rulers.len: 5 → 6 |
| `view.ruler_markers5` | verified | `{"visible": true}` | edit.rulers.len: 5 → 6 |
| `view.ruler_all_markers` | verified | `{"visible": true}` | edit.rulers.len: 5 → 9 |
| `view.ruler_all` | verified | `{}` | edit.rulers.len: 5 → 15 |
| `view.ruler_minimal` | verified | `{}` | edit.rulers.len: 5 → 2 |
| `view.ruler_tempo_editor` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.ruler_key_staff` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.marker_track_lane` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.marker_ruler_lines` | verified | `{"value": true}` | edit.flags.len: 5 → 4 |
| `view.marker_folder_lines` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.marker_ruler_lane_color` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.marker_track_lane_color` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.midi_input_display` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.midi_editor_clip_effects` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_sync_point` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_processing_state` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_name` | verified | `{"value": true}` | edit.flags.len: 5 → 4 |
| `view.clip_channel_name` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_scene_take` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_rating` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_overlap_shadows` | verified | `{"value": true}` | edit.flags.len: 5 → 4 |
| `view.clip_transparency` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_overwrite_indicator` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_copy_move_indicators` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_gain_line` | verified | `{"value": true}` | edit.flags.len: 5 → 4 |
| `view.clip_gain_info` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_effects_status` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_ara_note_overlay` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.clip_time_current` | verified | `{}` | edit.flags.len: 5 → 6 |
| `view.clip_time_original` | verified | `{}` | edit.flags.len: 5 → 6 |
| `view.clip_time_user` | verified | `{}` | edit.flags.len: 5 → 6 |
| `view.clip_time_none` | verified | `{}` | edit.flags.len: 5 → 6 |
| `view.clip_all_channels` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.waveform_peak` | verified | `{}` | edit.flags[4]: "waveform.power" → "waveform.peak" |
| `view.waveform_power` | verified | `{}` | edit.flags[4]: "waveform.peak" → "waveform.power" |
| `view.waveform_rectified` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.waveform_outlines` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.waveform_overlapped_crossfades` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.automation_trim_playlist` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.automation_composite_playlist` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_sends_all` | verified | `{}` | edit.flags.len: 5 → 15 |
| `view.expanded_sends_none` | verified | `{}` | edit.flags.len: 6 → 5 |
| `view.expanded_send_a` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_b` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_c` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_d` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_e` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_f` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_g` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_h` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_i` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.expanded_send_j` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.track_number` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.track_transcription_lane` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.dropped_video_frame_indicator` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.transport_counters` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.transport_midi_controls` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.transport_synchronization` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.transport_ableton_link` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.transport_output_meters` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.transport_expanded` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `view.flags` | read-ok | `{}` | :  → {"flags": ["view.clip.gain_line", "view.clip.name", "view.clip.overlap_shadows", "view.marker.ruler_lines", "waveform.peak"], "rulers"… |
| `view.zoom_toggle` | verified | `{"width_px": 1200, "height_px": 600}` | edit.zoom_toggle: null → {"heights": [[3, "Medium"]], "samples_per_px": 1967.4514285714286, "scroll": 0} |
| `view.zoom_toggle_cancel` | verified | `{}` | edit.zoom_toggle: {"heights": [[3, "Medium"]], "samples_per_px": 1967.4514285714286, "scroll": 0} → null |

## track (66) — verified 51, ran 8, read-ok 7

| id | status | params used | evidence |
|---|---|---|---|
| `track.new` | verified | `{"count": 2, "name": "NewT"}` | tracks.len: 9 → 11 |
| `track.group` | verified | `{"name": "Grp", "tracks": ["Kick", "Snare"]}` | groups.len: 0 → 1 |
| `track.ungroup` | verified | `{"group": "Grp"}` | groups.len: 1 → 0 |
| `track.group_toggle` | verified | `{"group": "Grp"}` | groups[0].active: true → false |
| `track.group_modify` | verified | `{"group": "Grp", "name": "Grp2"}` | groups[0].name: "Grp" → "Grp2" |
| `track.duplicate` | verified | `{"tracks": ["Kick"]}` | tracks.len: 9 → 10 |
| `track.split_into_mono` | verified | `{"tracks": ["Pad"]}` | tracks.len: 9 → 11 |
| `track.make_inactive` | verified | `{"tracks": ["Kick"], "inactive": true}` | tracks[0].inactive: false → true |
| `track.move_to_new_folder` | verified | `{"tracks": ["Kick"], "name": "Fold"}` | tracks.len: 9 → 10 |
| `track.move_to_folder` | verified | `{"tracks": ["Kick"], "folder": "Fold"}` | tracks[1].output: "Main" → {"Bus": 34} |
| `track.remove_from_folder` | verified | `{"tracks": ["Kick"]}` | tracks[1].output: {"Bus": 34} → "Main" |
| `track.change_width` | verified | `{"tracks": ["Kick"], "format": "stereo"}` | tracks[0].format: "Mono" → "Stereo" |
| `track.delete` | verified | `{"tracks": ["Snare"]}` | tracks.len: 9 → 8 |
| `track.rename` | verified | `{"track": "Kick", "name": "KickRenamed"}` | tracks[0].name: "Kick" → "KickRenamed" |
| `track.comments` | verified | `{"track": "Kick", "comments": "hello"}` | tracks[0].comments: "<missing>" → "hello" |
| `track.color` | ran | `{"tracks": ["Kick"], "color": [255, 0, 0]}` | no change in session |
| `track.height` | verified | `{"tracks": ["Kick"], "height": "large"}` | tracks[0].height: "medium" → "large" |
| `track.height_up` | verified | `{"tracks": ["Kick"]}` | tracks[0].height: "medium" → "large" |
| `track.height_down` | verified | `{"tracks": ["Kick"]}` | tracks[0].height: "medium" → "small" |
| `track.view` | verified | `{"tracks": ["Kick"], "view": "volume"}` | tracks[0].view: "waveform" → "volume" |
| `track.hide` | verified | `{"tracks": ["Kick"], "hidden": true}` | tracks[0].hidden: false → true |
| `track.pin` | ran | `{"tracks": ["Kick"]}` | no change in session |
| `track.move` | verified | `{"track": "Kick", "to": 2}` | tracks[2].name: "Hats" → "Kick" |
| `track.freeze` | ran | `{"tracks": ["Kick"]}` | no change in session |
| `track.commit` | verified | `{"tracks": ["Kick"]}` | tracks.len: 9 → 10 |
| `track.bounce` | verified | `{"tracks": ["Kick"]}` | tracks.len: 9 → 10 |
| `track.bypass_inserts` | verified | `{"tracks": ["Kick"], "bypass": true}` | tracks[0].inserts[0].bypass: false → true |
| `track.mute_sends` | verified | `{"tracks": ["Snare"], "mute": true}` | tracks[1].sends[0].mute: false → true |
| `track.set_record_to_input_only` | ran | `{}` | query \| echo/state only, no independent read-back |
| `track.scroll_to` | read-ok | `{"track": "Bass"}` | :  → {"track": 12} |
| `track.clear_clip_indicators` | read-ok | `{}` | :  → {"cleared": true} |
| `track.clear_trim_automation` | verified | `{"tracks": ["Kick"]}` | tracks[0].automation.len: 1 → 0 |
| `track.create_click` | verified | `{}` | tracks.len: 9 → 10 |
| `track.playlist_new` | verified | `{"track": "Kick", "name": "Alt1"}` | tracks[0].playlists: 1 → 2 |
| `track.playlist_duplicate` | verified | `{"track": "Kick"}` | tracks[0].playlists: 1 → 2 |
| `track.playlist_select` | verified | `{"track": "Kick", "index": 0}` | tracks[0].playlist: "Alt1" → "Kick" |
| `track.playlist_delete_unused` | verified | `{"track": "Kick"}` | tracks[0].playlists: 2 → 1 |
| `track.folder_toggle` | read-ok | `{"track": "Kick"}` | :  → {"open": false} |
| `track.vca` | read-ok | `{"tracks": ["Kick"], "vca": "VCA 1"}` | :  → {"vca": 33} |
| `track.playlist_promote` | verified | `{"track": "Kick", "playlist": 1, "start": 443077, "end": 1329231}` | tracks[0].clips.len: 2 → 3 |
| `track.input` | verified | `{"tracks": ["Kick"], "input": "Verb"}` | tracks[0].input: "None" → {"Bus": 1} |
| `track.output` | verified | `{"tracks": ["Kick"], "output": "Verb"}` | tracks[0].output: "Main" → {"Bus": 1} |
| `track.timebase` | ran | `{"tracks": ["Keys"], "ticks": true}` | no change in session |
| `track.elastic` | ran | `{"tracks": ["Kick"], "algorithm": "rhythmic"}` | no change in session |
| `track.inspect` | read-ok | `{"track": "Kick"}` | :  → {"automation": [], "automation_mode": "read", "clips": [{"end": 1329231, "fade_in": 0, "fade_out": 0, "gain_db": 0.0, "id": 4, "length… |
| `track.object` | read-ok | `{"tracks": ["Kick"], "object": true}` | :  → {"tracks": [{"object": true, "track": 3}]} |
| `track.convert_aux_to_folder` | verified | `{"tracks": ["Verb"]}` | tracks[7].kind: "aux" → "folder" |
| `track.extract_midi` | verified | `{"tracks": ["Keys"]}` | tracks.len: 9 → 10 |
| `track.save_preset` | verified | `{"path": "/scratch/out/kick.preset", "track": "Kick"}` | file:/scratch/out/kick.preset: missing → 2114 bytes |
| `track.load_preset` | verified | `{"path": "/scratch/out/kick.preset"}` | tracks[0].inserts[0].bypass: true → false |
| `track.bypass_inserts_ae` | verified | `{"tracks": ["Kick"], "bypass": true}` | tracks[0].inserts[0].bypass: false → true |
| `track.bypass_inserts_fj` | verified | `{"tracks": ["Kick"], "bypass": true}` | tracks[0].inserts[2].bypass: false → true |
| `track.bypass_eq` | verified | `{"tracks": ["Kick"], "bypass": true}` | tracks[0].inserts[0].bypass: false → true |
| `track.bypass_dynamics` | verified | `{"tracks": ["Bass"], "bypass": true}` | tracks[3].inserts[0].bypass: false → true |
| `track.bypass_reverb` | verified | `{"tracks": ["Verb"], "bypass": true}` | tracks[7].inserts[0].bypass: false → true |
| `track.bypass_delay` | verified | `{"tracks": ["Pad"], "bypass": true}` | tracks[4].inserts[1].bypass: false → true |
| `track.bypass_modulation` | verified | `{"tracks": ["Pad"], "bypass": true}` | tracks[4].inserts[0].bypass: false → true |
| `track.mute_sends_ae` | verified | `{"tracks": ["Snare"], "mute": true}` | tracks[1].sends[0].mute: false → true |
| `track.mute_sends_fj` | verified | `{"tracks": ["Snare"], "mute": true}` | tracks[1].sends[1].mute: false → true |
| `track.write_midi_rtp` | ran | `{"tracks": ["Keys"]}` | no note change |
| `track.trim_automation_write` | verified | `{"tracks": ["Kick"], "start": 48000, "end": 96000, "db": -3}` | tracks[0].automation.len: 0 → 1 |
| `track.coalesce_trim` | verified | `{"tracks": ["Kick"]}` | tracks[0].automation[0].param: "insert Z trim" → "volume" |
| `track.coalesce_vca` | verified | `{"tracks": ["VCA 1"]}` | tracks[0].volume_db: -3.0 → -9.0 |
| `track.designate_target_playlist` | read-ok | `{"tracks": ["Kick"], "index": 0}` | :  → {"tracks": [{"target": 0, "track": 3}]} |
| `track.show_target_playlist` | verified | `{"tracks": ["Kick"]}` | tracks[0].playlist: "Kick" → "Alt1" |
| `track.toggle_recent_playlist` | ran | `{"tracks": ["Kick"]}` | no change in session |

## clip (33) — verified 15, read-ok 10, ran 8

| id | status | params used | evidence |
|---|---|---|---|
| `clip.edit_lock` | verified | `{"clips": [4]}` | tracks[0].clips[0].locked: false → true |
| `clip.time_lock` | verified | `{"clips": [4]}` | tracks[0].clips[0].locked: false → true |
| `clip.send_to_back` | ran | `{"clips": [4]}` | query |
| `clip.bring_to_front` | ran | `{"clips": [4]}` | query |
| `clip.rating` | read-ok | `{"clips": [4], "rating": 5}` | :  → {"rating": 5} |
| `clip.group` | read-ok | `{"clips": [4, 7]}` | :  → {"group": 33} |
| `clip.ungroup` | ran | `{"clips": [4]}` | query |
| `clip.ungroup_all` | ran | `{}` | query |
| `clip.loop` | ran | `{"clips": [4], "count": 2}` | tried {"clips": [4], "count": 2} |
| `clip.rename` | verified | `{"clip": 4, "name": "KickClip"}` | tracks[0].clips[0].name: "Kick" → "KickClip" |
| `clip.gain` | verified | `{"clips": [4], "db": -6}` | tracks[0].clips[0].gain_db: 0.0 → -6.0 |
| `clip.gain_nudge_up` | verified | `{"clips": [4]}` | tracks[0].clips[0].gain_db: 0.0 → 1.0 |
| `clip.gain_nudge_down` | verified | `{"clips": [4]}` | tracks[0].clips[0].gain_db: 0.0 → -1.0 |
| `clip.gain_render` | verified | `{"clips": [4]}` | tracks[0].clips[0].gain_db: -6.0 → 0.0 |
| `clip.gain_bypass` | verified | `{"clips": [4]}` | bounce rms_dbfs: -20.24 → -19.96 |
| `clip.identify_sync_point` | ran | `{"clip": 4}` | query |
| `clip.remove_sync_point` | read-ok | `{"clips": [4]}` | :  → {"clips": 0} |
| `clip.quantize_to_grid` | verified | `{"clips": [4]}` | tracks[0].clips[0].start: 443214 → 443077 |
| `clip.color` | ran | `{"clips": [4], "color": [0, 255, 0]}` | query |
| `clip.elastic_properties` | verified | `{"clips": [4], "ratio": 1.5}` | tracks[0].clips[0].length: 886154 → 1329231 |
| `clip.remove_warp` | verified | `{"clips": [4]}` | tracks[0].clips[0].length: 1329231 → 886154 |
| `clip.place_source` | verified | `{"source": 2, "track": "Hats", "at": 96000}` | tracks[2].clips.len: 1 → 2 |
| `clip.capture` | read-ok | `{"name": "Cap"}` | :  → {"clips": 1} |
| `clip.inspect` | read-ok | `{"clip": 4}` | :  → {"end": 1329231, "fade_in": 0, "fade_out": 0, "gain_db": 0.0, "id": 4, "length": 886154, "locked": false, "muted": false, "name": "Kic… |
| `clip.regroup` | read-ok | `{"clips": [4, 7]}` | :  → {"clips": 2, "group": 33} |
| `clip.unloop` | verified | `{"clips": [4], "mode": "remove"}` | tracks[0].clips.len: 3 → 2 |
| `clip.effects_set` | read-ok | `{"clips": [4], "params": {"input_gain": -6}}` | :  → {"clips": 1, "params": 1} |
| `clip.effects_bypass` | read-ok | `{"clips": [4], "value": true}` | :  → {"bypass": true, "clips": 1} |
| `clip.effects_render` | read-ok | `{"clips": [4]}` | :  → {"rendered": 1} |
| `clip.conform_to_tempo` | verified | `{"clips": [4], "source_bpm": 120}` | tracks[0].clips[0].length: 886154 → 1022485 |
| `clip.remove_pitch_shift` | ran | `{"clips": [4]}` | no change in session |
| `clip.clear` | verified | `{"clips": [4]}` | tracks[0].clips.len: 3 → 2 |
| `clip.auto_rename` | read-ok | `{"clips": [4], "name": "Piece"}` | :  → {"clips": 1, "named": true} |

## event (35) — verified 23, read-ok 10, ran 2

| id | status | params used | evidence |
|---|---|---|---|
| `event.tempo` | verified | `{"bpm": 120, "at": 0}` | tempo[0].bpm: 104.0 → 120.0 |
| `event.tempo_remove` | verified | `{"at": 480000}` | tempo.len: 2 → 1 |
| `event.meter` | verified | `{"numerator": 3, "denominator": 4, "at": 0}` | meter[0].numerator: 4 → 3 |
| `event.tempo_scale` | verified | `{"factor": 1.2}` | tempo[0].bpm: 104.0 → 124.8 |
| `event.tempo_constant` | verified | `{"bpm": 120, "start": 0, "end": 480000}` | tempo.len: 1 → 2 |
| `event.insert_time` | verified | `{"start": 48000, "length": 96000}` | tracks[0].clips[0].end: 1329231 → 1425231 |
| `event.cut_time` | verified | `{"start": 48000, "end": 96000}` | tracks[0].clips[0].end: 1329231 → 1281231 |
| `event.quantize` | verified | `{"grid": "1/16", "strength": 100, "clips": [25]}` | notes[0].start: 100 → 0 |
| `event.transpose` | verified | `{"semitones": 2, "clips": [25]}` | notes[0].pitch: 60 → 62 |
| `event.change_velocity` | verified | `{"add": 10, "clips": [25]}` | notes[0].velocity: 92 → 102 |
| `event.change_duration` | verified | `{"add": 120, "clips": [25]}` | notes[0].length: 920 → 1040 |
| `event.remove_duplicate_notes` | verified | `{"clips": [25]}` | notes.len: 182 → 180 |
| `event.add_key_change` | ran | `{"key": "C major", "at": 0}` | query |
| `event.renumber_bars` | read-ok | `{}` | :  → {"note": "bars start at 1"} |
| `event.all_notes_off` | ran | `{}` | query |
| `event.midi_note` | verified | `{"clip": 25, "pitch": 67, "start_ticks": 2880, "length_ticks": 480}` | notes.len: 180 → 181 |
| `event.time_ops_window` | read-ok | `{}` | :  → {"meters": [{"denominator": 4, "numerator": 4, "tick": 0}], "sample_rate": 48000, "selection": {"end": 443072, "start": 443072}, "song… |
| `event.tempo_ops_window` | read-ok | `{}` | :  → {"meters": [{"denominator": 4, "numerator": 4, "tick": 0}], "sample_rate": 48000, "selection": {"end": 443072, "start": 443072}, "song… |
| `event.midi_ops_window` | read-ok | `{}` | :  → {"input_quantize": {"enabled": false, "grid_ticks": 240.0, "strength": 100.0, "swing": 0.0}, "performances": 0, "rtp": {}} |
| `event.move_song_start` | read-ok | `{"to": 48000}` | :  → {"moved": 2, "song_start": 48000} |
| `event.tempo_linear` | verified | `{"start": 0, "end": 480000, "start_bpm": 104, "end_bpm": 120}` | tempo.len: 1 → 36 |
| `event.tempo_parabolic` | verified | `{"start": 0, "end": 480000, "start_bpm": 104, "end_bpm": 120}` | tempo.len: 1 → 36 |
| `event.tempo_s_curve` | verified | `{"start": 0, "end": 480000, "start_bpm": 104, "end_bpm": 120}` | tempo.len: 1 → 36 |
| `event.tempo_stretch` | verified | `{"start": 0, "end": 480000, "factor": 1.5}` | tempo.len: 1 → 2 |
| `event.select_split_notes` | verified | `{"clips": [25], "action": "split"}` | tracks.len: 9 → 10 |
| `event.input_quantize` | read-ok | `{"enabled": true, "grid": "1/16"}` | :  → {"enabled": true, "grid_ticks": 240.0, "strength": 100.0, "swing": 0.0} |
| `event.step_input` | verified | `{"track": "Keys", "pitch": 60}` | selection.end: 443072 → 456923 |
| `event.restore_performance` | verified | `{"clips": [25]}` | notes[0].pitch: 62 → 60 |
| `event.flatten_performance` | read-ok | `{"clips": [25]}` | :  → {"clips": 1} |
| `event.midi_track_offsets` | read-ok | `{"track": "Keys", "offset": 480}` | :  → {"offsets": [{"name": "Keys", "offset": 480.0, "track": 23}, {"name": "Lead", "offset": 0.0, "track": 24}]} |
| `event.midi_rtp` | read-ok | `{"tracks": ["Keys"], "transpose": 2}` | :  → {"rtp": {"23.transpose": 2.0}} |
| `event.extract_chords` | verified | `{"tracks": ["Keys"], "start": 443077, "end": 1329231}` | markers.len: 4 → 12 |
| `event.beat_detective` | read-ok | `{"tracks": ["Kick"], "start": 0, "end": 480000}` | :  → {"beats": [443054, 464533], "bpm": 134.08, "count": 2, "separated": 0} |
| `event.identify_beat` | verified | `{"start": 443077, "end": 1329231, "bars": 4}` | tempo.len: 1 → 2 |
| `event.retrospective_record` | verified | `{"track": "Keys", "notes": [{"pitch": 60, "start_ticks": 0, "length_ticks": 240}]}` | tracks[5].clips.len: 1 → 2 |

## markers (6) — verified 6

| id | status | params used | evidence |
|---|---|---|---|
| `markers.add` | verified | `{"name": "Test Marker", "at": 96000}` | markers.len: 4 → 5 |
| `markers.delete` | verified | `{"number": 5}` | markers.len: 5 → 4 |
| `markers.edit` | verified | `{"number": 5, "name": "Edited"}` | markers[1].name: "Gone" → "Edited" |
| `markers.recall` | verified | `{"number": 2}` | selection.end: 443072 → 443077 |
| `markers.next` | verified | `{}` | selection.end: 0 → 443077 |
| `markers.previous` | verified | `{}` | selection.end: 2215385 → 1329231 |

## mix (29) — verified 22, ran 6, read-ok 1

| id | status | params used | evidence |
|---|---|---|---|
| `mix.volume` | verified | `{"track": "Kick", "db": -12}` | tracks[0].volume_db: -3.0 → -12.0 |
| `mix.pan` | verified | `{"track": "Kick", "pan": -0.5}` | tracks[0].pan[0]: 0.0 → -0.5 |
| `mix.mute` | verified | `{"track": "Kick", "value": true}` | tracks[0].mute: false → true |
| `mix.solo` | verified | `{"track": "Kick", "value": true}` | tracks[0].solo: false → true |
| `mix.solo_safe` | ran | `{"track": "Kick", "value": true}` | query \| echo/state only, no independent read-back |
| `mix.clear_solos` | verified | `{}` | tracks[0].solo: true → false |
| `mix.clear_mutes` | verified | `{}` | tracks[0].mute: true → false |
| `mix.record_arm` | verified | `{"track": "Kick", "value": true}` | tracks[0].record_arm: false → true |
| `mix.input_monitor` | ran | `{"track": "Kick", "value": true}` | query \| echo/state only, no independent read-back |
| `mix.phase_invert` | ran | `{"track": "Kick", "value": true}` | query \| echo/state only, no independent read-back |
| `mix.trim` | verified | `{"track": "Kick", "db": -6}` | bounce rms_dbfs: -29.17 → -32.24 |
| `mix.automation_mode` | verified | `{"track": "Kick", "mode": "touch"}` | tracks[0].automation_mode: "read" → "touch" |
| `mix.insert` | verified | `{"track": "Kick", "slot": 5, "plugin": "eq_1band"}` | tracks[0].inserts.len: 2 → 3 |
| `mix.insert_remove` | verified | `{"track": "Kick", "slot": 0}` | tracks[0].inserts.len: 2 → 1 |
| `mix.insert_bypass` | verified | `{"track": "Kick", "slot": 0, "value": true}` | tracks[0].inserts[0].bypass: false → true |
| `mix.insert_param` | verified | `{"track": "Kick", "slot": 0, "param": "input_gain", "value": -20}` | bounce rms_dbfs: -29.17 → -40.93 |
| `mix.insert_params` | verified | `{"track": "Kick", "slot": 0, "params": {"input_gain": -20}}` | bounce rms_dbfs: -29.17 → -40.93 |
| `mix.insert_move` | verified | `{"track": "Kick", "from": 0, "to": 3}` | tracks[0].inserts[0].plugin: "eq_7band" → "compressor" |
| `mix.send` | verified | `{"track": "Kick", "slot": 0, "bus": "Verb"}` | tracks[0].sends.len: 0 → 1 |
| `mix.send_remove` | verified | `{"track": "Snare", "slot": 0}` | tracks[1].sends.len: 1 → 0 |
| `mix.send_level` | verified | `{"track": "Snare", "slot": 0, "db": -20}` | tracks[1].sends[0].level_db: -10.0 → -20.0 |
| `mix.new_bus` | verified | `{"name": "Test Bus"}` | busses.len: 1 → 2 |
| `mix.surround_pan` | verified | `{"track": "Kick", "x": 0.5}` | tracks[0].surround: null → {"center": 100.0, "divergence": 0.0, "lfe_db": -144.0, "x": 0.5, "y": 1.0, "z": 0.0} |
| `mix.send_surround_pan` | verified | `{"track": "Kick", "slot": 0, "x": 0.5}` | tracks[0].sends[0].surround: null → {"center": 100.0, "divergence": 0.0, "lfe_db": -144.0, "x": 0.5, "y": 1.0, "z": 0.0} |
| `mix.insert_state` | ran | `{"track": "Kick", "slot": 0, "state": null}` | query \| echo/state only, no independent read-back |
| `mix.instrument` | ran | `{"track": "Keys", "plugin": "subtractive_synth"}` | query \| echo/state only, no independent read-back |
| `mix.instrument_param` | ran | `{"track": "Keys", "param": "cutoff", "value": 500}` | query \| echo/state only, no independent read-back |
| `mix.sampler_load` | verified | `{"track": "Keys", "path": "/scratch/media/sine440_48k24_mono.wav"}` | sources.len: 5 → 6 |
| `mix.sampler_clear` | read-ok | `{"track": "Keys"}` | :  → {"cleared": 33, "track": 23} |

## automation (10) — verified 9, read-ok 1

| id | status | params used | evidence |
|---|---|---|---|
| `automation.set_point` | verified | `{"track": "Kick", "param": "volume", "at": 96000, "value": -6}` | tracks[0].automation.len: 0 → 1 |
| `automation.write_range` | verified | `{"track": "Kick", "param": "volume", "start": 48000, "end": 96000, "value": -8}` | tracks[0].automation.len: 0 → 1 |
| `automation.clear` | verified | `{"track": "Kick", "param": "volume", "start": 0, "end": 200000}` | tracks[0].automation.len: 1 → 0 |
| `automation.thin` | verified | `{"tracks": ["Kick"], "tolerance": 0.1}` | tracks[0].automation[0].points: 6 → 2 |
| `automation.thin_all` | read-ok | `{"tolerance": 0.1}` | :  → {"removed": 2} |
| `automation.write_to_current` | verified | `{}` | tracks[0].automation[0].points: 1 → 5 |
| `automation.write_to_all` | verified | `{}` | tracks[0].automation.len: 1 → 3 |
| `automation.volume_to_clip_gain` | verified | `{"tracks": ["Kick"]}` | tracks[0].clips[0].gain_envelope: "<missing>" → [[0, -3.0], [886153, -3.0]] |
| `automation.clip_gain_to_volume` | verified | `{"tracks": ["Kick"]}` | tracks[0].automation.len: 0 → 1 |
| `automation.copy_to_send` | verified | `{"tracks": ["Kick"], "send": 0}` | tracks[0].automation.len: 1 → 2 |

## options (35) — verified 35

| id | status | params used | evidence |
|---|---|---|---|
| `options.loop_record` | verified | `{"value": true}` | edit.loop_record: false → true |
| `options.quickpunch` | verified | `{"value": true}` | edit.quickpunch: false → true |
| `options.pre_post_roll` | verified | `{"value": true}` | edit.pre_post_roll: false → true |
| `options.loop_playback` | verified | `{"value": true}` | edit.loop_playback: false → true |
| `options.link_timeline_edit` | verified | `{"value": true}` | edit.link_timeline_edit: true → false |
| `options.link_track_edit` | verified | `{"value": true}` | edit.link_track_edit: false → true |
| `options.insertion_follows_playback` | verified | `{"value": true}` | edit.insertion_follows_playback: false → true |
| `options.tab_to_transient` | verified | `{"value": true}` | edit.tab_to_transient: false → true |
| `options.mirrored_midi` | verified | `{"value": true}` | edit.mirrored_midi: false → true |
| `options.automation_follows_edit` | verified | `{"value": true}` | edit.automation_follows_edit: true → false |
| `options.markers_follow_edit` | verified | `{"value": true}` | edit.markers_follow_edit: false → true |
| `options.layered_editing` | verified | `{"value": true}` | edit.layered_editing: false → true |
| `options.click` | verified | `{"value": true}` | edit.click: false → true |
| `options.countoff` | verified | `{"value": true}` | edit.countoff: false → true |
| `options.midi_merge` | verified | `{"value": true}` | edit.midi_merge: false → true |
| `options.pre_fader_metering` | verified | `{"value": true}` | edit.pre_fader_metering: false → true |
| `options.delay_compensation` | verified | `{"value": true}` | edit.delay_compensation: true → false |
| `options.destructive_record` | verified | `{"value": true}` | edit.record_mode: "normal" → "destructive" |
| `options.trackpunch` | verified | `{"value": true}` | edit.record_mode: "normal" → "trackpunch" |
| `options.scrolling` | verified | `{"mode": "continuous"}` | edit.scrolling: "page" → "continuous" |
| `options.solo_mode` | verified | `{"mode": "afl"}` | edit.solo_mode: "sip" → "afl" |
| `options.keyboard_focus` | verified | `{"focus": "clips"}` | edit.keyboard_focus: "commands" → "clips" |
| `options.pre_roll` | verified | `{"length": 48000}` | edit.pre_roll: 96000 → 48000 |
| `options.post_roll` | verified | `{"length": 48000}` | edit.post_roll: 96000 → 48000 |
| `options.destructive_punch` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.transport_online` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.dynamic_transport` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.marker_target_follows_selection` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.midi_thru` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.auto_spot_clips` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.keyboard_lock` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.calibration_mode` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.midi_live_mode` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.low_latency_monitoring` | verified | `{"value": true}` | edit.flags.len: 5 → 6 |
| `options.prepare_dpe_tracks` | verified | `{"tracks": ["Kick"]}` | edit.flags.len: 5 → 6 |

## setup (20) — read-ok 16, verified 4

| id | status | params used | evidence |
|---|---|---|---|
| `setup.session` | verified | `{"frame_rate": "25", "bit_depth": 16, "name": "Setup Test"}` | frame_rate: "30" → "25" |
| `setup.preferences` | read-ok | `{}` | :  → {"edit": {"automation_follows_edit": true, "click": false, "countoff": false, "countoff_bars": 2, "delay_compensation": true, "edit_mo… |
| `setup.reset_edit_state` | verified | `{}` | edit.main_counter: "BarsBeats" → "MinSecs" |
| `setup.hardware` | read-ok | `{"buffer_size": 256}` | :  → {"applied": false, "bit_depth": "Int24", "buffer_size": 256, "delay_compensation": true, "device": null, "sample_rate": 48000} |
| `setup.playback_engine` | read-ok | `{"buffer_size": 512, "delay_compensation": false}` | :  → {"applied": false, "bit_depth": "Int24", "buffer_size": 512, "delay_compensation": false, "device": null, "sample_rate": 48000} |
| `setup.disk_allocation` | read-ok | `{"path": "/scratch/out"}` | :  → {"root": "/scratch/out", "tracks": [{"name": "Kick", "path": "/scratch/… |
| `setup.peripherals` | read-ok | `{"settings": {"test": 1}}` | :  → {"flags": [], "values": {"test": 1.0}} |
| `setup.io` | verified | `{"action": "create_bus", "name": "IO Bus"}` | busses.len: 1 → 2 |
| `setup.current_timecode` | read-ok | `{"timecode": "01:00:00:00"}` | :  → {"at": 443072, "timecode_start": 172356928} |
| `setup.current_feet_frames` | read-ok | `{"feet_frames": "100+00"}` | :  → {"feet_frames_start": 1324} |
| `setup.external_timecode_offset` | read-ok | `{"frames": 10}` | :  → {"frames": 10.0, "samples": 16000.0} |
| `setup.video_sync_offset` | read-ok | `{"frames": 5}` | :  → {"frames": 5.0, "samples": 8000.0} |
| `setup.click_countoff` | read-ok | `{"volume_db": -12}` | :  → {"accent_note": 84.0, "accent_velocity": 127.0, "countoff": false, "countoff_bars": 2, "normal_note": 72.0, "normal_velocity": 100.0, … |
| `setup.keyboard_shortcuts` | read-ok | `{}` | :  → {"shortcuts": [{"id": "session.new", "label": "New...", "menu": "File", "shortcut": "Cmd+N"}, {"id": "session.open", "label": "Open Se… |
| `setup.midi_studio` | read-ok | `{"devices": ["Test"]}` | :  → {"devices": ["Test"]} |
| `setup.midi_beat_clock` | read-ok | `{"enabled": true}` | :  → {"destination": null, "enabled": true, "offset": 0.0} |
| `setup.midi_input_filter` | read-ok | `{"filter": ["notes"]}` | :  → {"filtered": ["notes"]} |
| `setup.midi_input_devices` | read-ok | `{"enable": []}` | :  → {"enabled": []} |
| `setup.transcription_settings` | read-ok | `{"enabled": false}` | :  → {"enabled": false, "language": "en"} |
| `setup.main_format` | verified | `{"format": "5.1"}` | main_format: "Stereo" → "5.1" |

## transport (13) — ran 7, read-ok 5, verified 1

| id | status | params used | evidence |
|---|---|---|---|
| `transport.play` | ran | `{"from": 48000}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.stop` | ran | `{}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.toggle` | ran | `{}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.record` | ran | `{}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.pause` | ran | `{}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.half_speed` | ran | `{}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.play_selection` | ran | `{}` | headless engine has no audio device; call accepted, returns {}, transport.playing stays false |
| `transport.rtz` | read-ok | `{}` | :  → {"at": 0} |
| `transport.go_to_end` | read-ok | `{}` | :  → {"at": 2682432} |
| `transport.rewind` | read-ok | `{"seconds": 2}` | :  → {"at": 347072} |
| `transport.fast_forward` | read-ok | `{"seconds": 2}` | :  → {"at": 539072} |
| `transport.locate` | verified | `{"at": 96000}` | selection.end: 443072 → 96000 |
| `transport.status` | read-ok | `{}` | :  → {"playing": false, "position": 443072, "recording": false} |

## engine (6) — read-ok 4, skipped 2

| id | status | params used | evidence |
|---|---|---|---|
| `engine.commands` | read-ok | `{}` | :  → [{"disabled_reason": null, "enabled": true, "id": "session.new", "label": "New...", "menu": ["File"], "params": "{name?: 'Untitled', s… |
| `engine.history` | read-ok | `{}` | :  → {"can_redo": false, "undo": []} |
| `engine.plugins` | read-ok | `{}` | :  → [{"category": "Eq", "id": "eq_1band", "instrument": false, "name": "EQ 1-Band", "params": [{"choices": ["Peak", "Low Shelf", "High She… |
| `engine.parity` | read-ok | `{}` | :  → {"implemented": 397, "missing": ["File > Open > Project...", "File > Open > Sketch...", "File > Dashboard...", "File > Start Collabora… |
| `engine.clap_plugins` | skipped | `{}` | returns [] — no CLAP plug-ins installed |
| `engine.vst3_plugins` | skipped | `{}` | returns [] — no VST3 plug-ins installed in this environment |

## audiosuite (1) — verified 1

| id | status | params used | evidence |
|---|---|---|---|
| `audiosuite.process` | verified | `{"process": "normalize", "clips": [4]}` | bounce rms_dbfs: -29.17 → -28.71 |

## midi (6) — verified 5, read-ok 1

| id | status | params used | evidence |
|---|---|---|---|
| `midi.notes` | read-ok | `{"clip": 25}` | :  → {"notes": [{"channel": 0, "length": 920, "pitch": 60, "release_velocity": 64, "start": 0, "velocity": 92}, {"channel": 0, "length": 92… |
| `midi.new_clip` | verified | `{"track": "Keys", "start": 480000, "length": 96000}` | tracks[5].clips.len: 1 → 3 |
| `midi.note_add` | verified | `{"clip": 25, "pitch": 72, "start_ticks": 1920, "length_ticks": 480}` | notes.len: 180 → 181 |
| `midi.note_edit` | verified | `{"clip": 25, "index": 0, "velocity": 40}` | notes[0].velocity: 92 → 40 |
| `midi.note_delete` | verified | `{"clip": 25, "indices": [0]}` | notes.len: 180 → 179 |
| `midi.notes_move` | verified | `{"clip": 25, "indices": [0], "semitones": 2}` | notes[0].pitch: 60 → 62 |

## video (3) — ran 1, verified 1, read-ok 1

| id | status | params used | evidence |
|---|---|---|---|
| `video.online` | ran | `{"value": false}` | query \| echo/state only, no independent read-back |
| `video.offset` | verified | `{"at": 48000}` | tracks[0].clips[0].end: 48000 → 96000 |
| `video.list` | read-ok | `{}` | :  → {"online": true, "videos": [{"clips": 1, "codec": "h264", "duration": 1.0, "file_found": true, "frame_rate": 30.0, "height": 240, "id"… |

