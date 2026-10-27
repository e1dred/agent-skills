#!/bin/sh
# usage: run.sh style kind
REPO=${REPO:?set REPO to the agent-skills folder}
s=$1; k=$2; W=$(pwd)
PYTHONDONTWRITEBYTECODE=1 python3 -I "$REPO/styles/build_wordcraft.py" $s $k $W/wc-$s-$k.docx --paper=a4 --overwrite > $W/wc-$s-$k.json 2>/dev/null && "${WORDCRAFT_CLI:-$HOME/AppImages/wordcraft-cli}" run --script $W/wc-$s-$k.json >/dev/null 2>&1
PYTHONDONTWRITEBYTECODE=1 python3 "$REPO/genoffice-supplement/build_genoffice.py" $s $k $W/go-$s-$k.docx --paper=a4 >/dev/null 2>$W/err-$s-$k.txt
for p in wc go; do rm -rf r-$p-$s-$k; genoffice render $W/$p-$s-$k.docx --out $W/r-$p-$s-$k --json >/dev/null 2>&1; done
