#!/bin/sh
# Everyday-task coverage per Craft app. Read-only. A task is covered when every id on its line exists in the installed CLI and is named in the skill.
dir=${AIMG:-"$HOME/AppImages"}; repo=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
for app in wordcraft gridcraft deckcraft photocraft cadcraft pdfcraft filmcraft lightcraft vectorcraft designcraft; do
    f="$repo/everyday/$app.txt"; cli="$dir/$app-cli"; [ -f "$f" ] && [ -x "$cli" ] || continue
    case $app in
      photocraft) "$cli" commands --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);d=d if isinstance(d,list) else d["commands"];print("\n".join(x["id"] for x in d))';;
      pdfcraft) "$cli" tools 2>/dev/null | python3 -c 'import json,sys;print("\n".join(x["name"] for x in json.load(sys.stdin)))';;
      filmcraft) "$cli" commands --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);d=d if isinstance(d,list) else d["commands"];print("\n".join(x["id"] for x in d))';;
      cadcraft|vectorcraft|designcraft) "$cli" commands 2>/dev/null | python3 -c 'import json,sys;print("\n".join(x["id"] for x in json.load(sys.stdin)))';;
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
# GenOffice: ids are ops from `genoffice guide` (genoffice-supplement/op_names.py) or CLI commands; covered when every id exists and the supplement names it.
f="$repo/everyday/genoffice.txt"
if command -v genoffice >/dev/null 2>&1 && [ -f "$f" ]; then
    { python3 -I "$repo/genoffice-supplement/op_names.py" | awk '{print $2}'; genoffice --help 2>&1 | awk '/^  [a-z-]+ /{print $1}'; } | LC_ALL=C sort -u > "$tmp/go.all"
    grep -rIhoE --exclude-dir='__pycache__' '[A-Za-z0-9_][A-Za-z0-9_.]*' "$repo/genoffice-supplement" | LC_ALL=C sort -u > "$tmp/go.tok"
    n=0; ok=0
    while IFS='|' read -r task ids; do
        [ -n "$ids" ] || continue; n=$((n+1)); miss=""
        for id in $ids; do
            grep -qxF "$id" "$tmp/go.all" || miss="$miss $id(not in genoffice)"
            grep -qxF "$id" "$tmp/go.tok" || miss="$miss $id(not in skill)"
        done
        if [ -z "$miss" ]; then ok=$((ok+1)); else [ -n "$VERBOSE" ] && echo "  gap: $task:$miss"; fi
    done < "$f"
    printf '%-11s %2s / %-2s everyday tasks covered (%s%%)\n' genoffice "$ok" "$n" "$((100 * ok / n))"
fi

# ONLYOFFICE everyday tasks: the tool set is the skill's tool-names.txt (the MCP server's tools),
# and a tool counts as named when it appears somewhere in the onlyoffice/ skill folder.
f="$repo/everyday/onlyoffice.txt"
if [ -f "$f" ]; then
    LC_ALL=C sort -u "$repo/onlyoffice/tool-names.txt" > "$tmp/oo.all"
    grep -rIhoE --exclude='tool-names.txt' --exclude-dir='__pycache__' '[A-Za-z0-9_][A-Za-z0-9_.]*' "$repo/onlyoffice" | LC_ALL=C sort -u > "$tmp/oo.tok"
    n=0; ok=0
    while IFS='|' read -r task ids; do
        [ -n "$ids" ] || continue; n=$((n+1)); miss=""
        for id in $ids; do
            grep -qxF "$id" "$tmp/oo.all" || miss="$miss $id(not in tool-names)"
            grep -qxF "$id" "$tmp/oo.tok" || miss="$miss $id(not in skill)"
        done
        if [ -z "$miss" ]; then ok=$((ok+1)); else [ -n "$VERBOSE" ] && echo "  gap: $task:$miss"; fi
    done < "$f"
    printf '%-11s %2s / %-2s everyday tasks covered (%s%%)\n' onlyoffice "$ok" "$n" "$((100 * ok / n))"
fi
