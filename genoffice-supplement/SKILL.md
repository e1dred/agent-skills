---
name: genoffice-supplement
description: Use when editing .docx or other Office files with GenOffice (Docs editor, genoffice CLI/MCP) and its own bundled skill leaves a Word op, unit, page-count difference or document-style rebuild unclear; load next to GenOffice's own skill
---

# GenOffice supplement

> **Updates:** if this folder has a `.installed-from` file (written when it was copied from the repo), run `git ls-remote https://gitlab.com/e1dred/agent-skills.git HEAD` once per session. Take the hash on the output line that ends in exactly `HEAD`; if it differs from the file's, tell the user a newer version exists and offer to update it (see "Updating" in https://gitlab.com/e1dred/agent-skills/-/blob/main/INSTALL.md, which can merge local edits); never update without asking. Compare the hashes after trimming whitespace. No file, a clone or symlink, or no network (empty output or an error from `git ls-remote`): skip silently.

**Scope rule (strict):** this skill holds only things GenOffice's own bundled skills do not provide. It never copies or restates
a GenOffice-provided skill (its generated `genoffice` skill, the ~45 recommended app skills). Read those first; this adds
what running the app showed. Tested on GenOffice 0.12.852 (Linux AppImage), CLI and MCP, headless; the sweeps in `reference/` were re-run on 0.12.446, 0.12.600 and 0.12.852 with the same results as on 0.12.117, the live-editor checks were not.

GenOffice has six editors: Docs, Sheets, Slides, Markdown, HTML and PDF. The Docs (.docx), Sheets (.xlsx) and Slides (.pptx ops and the page-spec build) are covered, plus the conversions that reach the Markdown, HTML and PDF editors. The live editor (`open`, `selection`, writes to an open file) is covered too.

## Where things are

Read the file that matches the task; each lists the sections it holds. Use `grep -n` on `reference/` to find a command id.

| File in `reference/` | Read it for | Sections |
|---|---|---|
| `docs-ops.md` | Word ops (`docs apply`): the sweep results, gaps closed, and the index of every op | Word-op sweep, 2026-10-27, GenOffice 0.12.117; Docs gaps closed; Op index; New in 0.12.600: `remove_parts` (strip customXml / webExtensions metadata before filing) |
| `sheets.md` | Spreadsheet ops (`sheet apply`) | Sheets sweep |
| `slides.md` | Presentation ops (`slides apply`) | Slides sweep |
| `markdown-html-pdf.md` | Converting and creating Markdown, HTML and PDF with the CLI | Markdown, HTML and PDF through the CLI |
| `live-editor.md` | `open`, `selection` and writing to a file that is open in the GenOffice editor | Live editor: `open`, `selection`, writing to a file that is open |
| `document-styles.md` | Rebuilding the eight document styles in GenOffice, compared with WordCraft and ONLYOFFICE; headless vs app page counts | All eight styles x doc, report, resume and cv against WordCraft; Style rebuild: `modern` doc via GenOffice vs WordCraft vs ONLYOFFICE; All eight styles, doc kind, GenOffice vs WordCraft; Page count: headless `render` vs the app window |

## Traps (each one tripped the sweep)
- Op field names differ from what you guess: `moveBlocks` takes `blockIndexes` (no `target`); `setList` takes `kind: "bullet"|"number"` (not `type`). Rejections name the allowed fields and the whole batch is atomic: nothing applied.
- Things defined or created earlier in a batch are NOT visible to later ops of the same batch for: `define_style` type table then `setTableStyle`; `wrap_content_control` then `unwrap_content_control`. Split into two `apply` calls. (define_style paragraph then applyStyle in one batch works.)
- `define_style` for a new style needs paragraph or run formatting (or basedOn); basedOn must exist in the document. A new docx has no table styles (`tableStyles: []`), so create one with a run property and apply it in a second call.
- `setTableCellFormat` fill does not change text colour: a dark header fill keeps black text. Set white text separately (setFont on that block does not reach table cells in my sweep; not yet tested how).
- `insert_text_box` default anchor is the paragraph, so x/y count from the margin, not the page edge: x 15cm + 4cm wide ran off the right side. Use `anchor:"page"` for page coordinates. insert_picture needs `float.anchor:"page"` the same way.
- Comment ids are small positional strings ("1", "2"); revision ids ("r1"...) are positional and change after every edit, so re-read before accept/reject.
- Reject-all restored the original text; accept with type filter leaves the other revisions pending.
- Table merge concatenates cell text as separate paragraphs; split keeps text in the top-left cell.
- Watermark is heavy at opacity 0.3 with a large size; use about 0.15 for body-text legibility.

## Not yet tested
setFont null (clear), partial-selection edits, setImageProperties on a floating picture, insert_content formula render, insertField IF/PAGEREF, `--dry-run` and `--best-effort`. (Writing to a file open in the app, live `open`/`selection` and the style comparison with WordCraft and ONLYOFFICE are now tested: see `reference/live-editor.md` and `reference/document-styles.md`.)

## Keep this file growing
Add what you learn to the matching file in `reference/` (see the table above), labelled with the GenOffice version and what was checked (XML, read-back or render). Do not paste text from GenOffice's own skills.
