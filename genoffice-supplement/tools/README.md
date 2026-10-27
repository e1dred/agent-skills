# tools: re-run the GenOffice sweeps

These are the scripts behind the results in `../SKILL.md`, kept so the checks can be repeated when GenOffice updates. Sample data is invented and tiny (`data/`).

| File | What it does |
|---|---|
| `run_sweeps.sh` | Sets up a scratch folder (sample .docx, .xlsx, .pptx, a small picture) and runs the three sweeps |
| `sweep_docs.py`, `check_docs_xml.py` | About 45 Word ops, one fresh copy per case; the second script prints what the saved XML says (fonts, borders, fields, headers, sections, comments, notes) |
| `sweep_sheets.py`, `sweep_sheets_staged.py` | About 40 Excel ops, then the ones that need two `apply` calls (convert to values, table, pivots, chart edit, sheet copy and move, protection) |
| `sweep_slides.py` | About 30 PowerPoint cases (text, shapes, tables, charts, SmartArt, slides, animations, deck ops) |
| `build_pair.sh`, `compare_styles.py` | Build a style x kind with WordCraft and with GenOffice (`REPO` is the agent-skills folder; `WORDCRAFT_CLI` the CLI path) and compare the renders page by page (needs Pillow) |
| `../op_names.py` | Lists the ops `genoffice guide` documents (used by `../../coverage.sh`) |

"ok" only means an op was accepted: read the values back, check the XML, and render. The scripts print the first two; render with `genoffice render`.
Run for the style comparison: `REPO=~/agent-skills ./build_pair.sh professional doc` inside a scratch folder, once per style and kind, then `python3 compare_styles.py`.
