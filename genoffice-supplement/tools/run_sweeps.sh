#!/bin/sh
# Re-run the GenOffice op sweeps (Docs, Sheets, Slides) in a scratch directory and print a one-line status per case.
# Usage: ./run_sweeps.sh [WORKDIR]      (default ./work next to this script; created, safe to delete)
# Needs: genoffice on PATH, python3. Results are JSON lines in WORKDIR/results_*.txt; the XML checks print with check_docs_xml.py.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
work=${1:-"$here/work"}
mkdir -p "$work"; cp "$here"/*.py "$here"/*.sh "$here"/data/* "$work"/
cd "$work"
python3 -I make_pic.py
genoffice create --type docx --from base.html --out base.docx --force --json >/dev/null
genoffice create --type xlsx --from base.csv --header --out base.xlsx --force --json >/dev/null
genoffice create --type pptx --ops base_ops.json --out base.pptx --force --json >/dev/null
echo "== Docs";   python3 -I sweep_docs.py   > results_docs.txt;   python3 -c "import json;[print(d['status'],d['case'],d['summary'][:70]) for d in map(json.loads,open('results_docs.txt'))]"
python3 -I check_docs_xml.py
echo "== Sheets"; python3 -I sweep_sheets.py > results_sheets.txt; python3 -c "import json;[print(d['status'],d['case'],d['summary'][:70]) for d in map(json.loads,open('results_sheets.txt'))]"
python3 -I sweep_sheets_staged.py
echo "== Slides"; python3 -I sweep_slides.py | head -80
echo "Done. Expected failures are the ones the notes describe (SKILL.md, Traps); compare with the previous run when GenOffice updates."
