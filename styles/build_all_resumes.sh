#!/bin/sh
# Build every redesigned résumé for Letter and A4 (docx + pdf + a PNG of page 1), the photo-free variants of the
# designs that show a photo placeholder, and contact sheets.
#   ./build_all_resumes.sh /abs/out_dir
# -> out_dir/letter/ and out_dir/a4/, each with <style>-<a|b>.docx/.pdf/.png, <style>-<a|b>-nophoto.*, sheet.png, sheet-nophoto.png
# Needs wordcraft-cli (in $AIMG, default ~/AppImages) and python3 with Pillow (avatars and sheets).
out=${1:?usage: build_all_resumes.sh /abs/out_dir}
cli=${AIMG:-$HOME/AppImages}/wordcraft-cli
here=$(cd "$(dirname "$0")" && pwd)
photo=$(python3 -I "$here/resume_designs.py" --list-photo | tr '\n' ' ')
build() {   # name outbase flags...
  name=$1; base=$2; shift 2
  python3 -I "$here/resume_designs.py" "$name" "$base.docx" --overwrite "$@" > "$base.job.json" || return
  "$cli" run --script "$base.job.json" >/dev/null 2>&1 && "$cli" render "$base.docx" "$base.png" --page 1 --scale 1.0 >/dev/null 2>&1
  rm -f "$base.job.json"
}
for paper in letter a4; do
  d="$out/$paper"; mkdir -p "$d"; flag=""; [ "$paper" = a4 ] && flag="--a4"
  for name in $(python3 -I "$here/resume_designs.py" --list); do
    build "$name" "$d/$name" $flag; echo "$paper $name"
    case " $photo " in *" $name "*) build "$name" "$d/$name-nophoto" $flag --no-photo; echo "$paper $name-nophoto";; esac
  done
  python3 -I "$here/resume_sheet.py" "$d"
done
