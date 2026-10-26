#!/bin/sh
# Everyday-task coverage per Craft app. Read-only. A task is covered when every id on its line exists in the installed CLI and is named in the skill.
dir=${AIMG:-"$HOME/AppImages"}; repo=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
for app in wordcraft gridcraft deckcraft photocraft cadcraft; do
    f="$repo/everyday/$app.txt"; cli="$dir/$app-cli"; [ -f "$f" ] && [ -x "$cli" ] || continue
    case $app in
      photocraft) "$cli" commands --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);d=d if isinstance(d,list) else d["commands"];print("\n".join(x["id"] for x in d))';;
      cadcraft) "$cli" commands 2>/dev/null | python3 -c 'import json,sys;print("\n".join(x["id"] for x in json.load(sys.stdin)))';;
      *) "$cli" commands 2>/dev/null | grep -oE '^[a-z][A-Za-z0-9]*\.[A-Za-z0-9.]+';;
    esac | LC_ALL=C sort -u > "$tmp/$app.all"
    grep -rIhoE --exclude-dir='__pycache__' '[A-Za-z0-9_][A-Za-z0-9_.]*' "$repo/$app" | LC_ALL=C sort -u > "$tmp/$app.tok"
    n=0; ok=0
    while IFS='|' read -r task ids; do
        [ -n "$ids" ] || continue; n=$((n+1)); miss=""
        for id in $ids; do
            grep -qxF "$id" "$tmp/$app.all" || miss="$miss $id(not in CLI)"
            grep -qxF "$id" "$tmp/$app.tok" || miss="$miss $id(not in skill)"
        done
        if [ -z "$miss" ]; then ok=$((ok+1)); else [ -n "$VERBOSE" ] && echo "  gap: $task:$miss"; fi
    done < "$f"
    printf '%-11s %2s / %-2s everyday tasks covered (%s%%)\n' "$app" "$ok" "$n" "$((100 * ok / n))"
done
