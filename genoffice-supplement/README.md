# genoffice-supplement

Supplementary [Agent Skill](https://agentskills.io) for GenOffice (Docs, Sheets, Slides, Markdown, HTML and PDF editors, with a `genoffice` CLI and MCP server).

## What this is, and the one hard rule

GenOffice ships its own skills: a generated `genoffice` skill and a set of bundled app skills (budget planner, business report, executive deck and so on).
**This folder never contains, copies or restates any of them.** It holds only what those skills do not provide: behaviour found by running the app,
traps, units that differ between ops, exact field names that are easy to guess wrong, and recipes built and checked on a real install.
Use it **next to** GenOffice's own skills, not instead of them. If GenOffice later documents something here, delete it from here.

## Contents

| File | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill: results of a sweep of the Word (`docs apply`) ops, traps, and the document-style rebuilds compared with WordCraft and ONLYOFFICE |
| [`build_genoffice.py`](build_genoffice.py) | Builds a styled document in GenOffice from the same app-neutral plan as `../styles` (reads `../styles/plan.py`, changes nothing there) |

Everything is tested on GenOffice 0.12.117 (Linux AppImage), headless. Each result says whether it was read back from the XML or rendered.
Not covered yet: Sheets, Slides, Markdown, HTML and PDF editing, and the live editor.

## Use

```sh
../install.sh genoffice-supplement
PYTHONDONTWRITEBYTECODE=1 python3 build_genoffice.py modern doc /abs/report.docx --paper=a4 --page-numbers=bottom-center
```

Options: `--paper`, `--page-numbers`, `--header-text`, `--figure=sample`, `--footnotes`, `--merged-table`, `--columns=2`. Sample text is invented.

Unofficial: not affiliated with GenOffice.
