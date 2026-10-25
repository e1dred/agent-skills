#!/bin/sh
# Print the "commands documented" figure for each skill, measured against the installed CLIs. Read-only.
# Usage: ./coverage.sh            (CLIs in $AIMG, default ~/AppImages)
# A command counts as documented when its id appears anywhere in the skill's text. That is a lower bound on
# what the skill teaches (a workflow can be described without naming every command) and an upper bound on
# what was tested (an id can be named without being run). Unit: engine commands for the Craft apps,
# MCP tools for ONLYOFFICE (names listed in onlyoffice/tool-names.txt).
dir=${AIMG:-"$HOME/AppImages"}
repo=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT

tokens() { grep -rIhoE --exclude='tool-names.txt' --exclude-dir='__pycache__' '[A-Za-z0-9_][A-Za-z0-9_.]*' "$1" | LC_ALL=C sort -u; }

for app in wordcraft gridcraft deckcraft photocraft; do
    cli="$dir/$app-cli"; [ -x "$cli" ] || { echo "$app: no CLI at $cli" >&2; continue; }
    ver=$("$cli" --version 2>/dev/null | sed -n '1s/.*\([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\).*/\1/p')
    if [ "$app" = photocraft ]; then
        "$cli" commands --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);d=d if isinstance(d,list) else d["commands"];print("\n".join(x["id"] for x in d))'
    else
        "$cli" commands 2>/dev/null | grep -oE '^[a-z][A-Za-z0-9]*\.[A-Za-z0-9.]+'
    fi | LC_ALL=C sort -u > "$tmp/$app.all"
    tokens "$repo/$app" > "$tmp/$app.tok"
    total=$(wc -l < "$tmp/$app.all"); have=$(LC_ALL=C comm -12 "$tmp/$app.all" "$tmp/$app.tok" | wc -l)
    printf '%-11s %-7s %4s / %-4s commands documented (%s%%)\n' "$app" "$ver" "$have" "$total" "$((100 * have / total))"
done

names="$repo/onlyoffice/tool-names.txt"
if [ -f "$names" ]; then
    tokens "$repo/onlyoffice" > "$tmp/oo.tok"
    LC_ALL=C sort -u "$names" > "$tmp/oo.all"
    total=$(wc -l < "$tmp/oo.all"); have=$(LC_ALL=C comm -12 "$tmp/oo.all" "$tmp/oo.tok" | wc -l)
    printf '%-11s %-7s %4s / %-4s tools documented (%s%%)\n' onlyoffice "$(flatpak info org.onlyoffice.desktopeditors 2>/dev/null | sed -n 's/^ *Version: *//p')" "$have" "$total" "$((100 * have / total))"
fi
