#!/bin/sh
# Build every redesigned résumé (docx + pdf) and a PNG of page 1 into a folder, plus a contact sheet.
#   ./build_all_resumes.sh /abs/out_dir [--data=/abs/content.json]
# Needs wordcraft-cli (in $AIMG, default ~/AppImages) and python3 with Pillow for the avatars and the sheet.
out=${1:?usage: build_all_resumes.sh /abs/out_dir [--data=...]}; shift
cli=${AIMG:-$HOME/AppImages}/wordcraft-cli
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$out"
for d in $(python3 -I "$here/resume_designs.py" --list); do
  python3 -I "$here/resume_designs.py" "$d" "$out/$d.docx" --overwrite "$@" > "$out/.$d.json" || continue
  "$cli" run --script "$out/.$d.json" >/dev/null 2>&1 && "$cli" render "$out/$d.docx" "$out/$d.png" --page 1 --scale 1.0 >/dev/null 2>&1
  rm -f "$out/.$d.json"; echo "$d"
done
python3 -I "$here/resume_sheet.py" "$out"
