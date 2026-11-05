#!/bin/sh
# Print the "commands documented" figure for each skill, measured against the installed CLIs. Read-only.
# Usage: ./coverage.sh            (CLIs in $AIMG, default ~/AppImages)
# A command counts as documented when its id (a leading "-" counts, as in cadcraft `-block`) appears anywhere in the skill's text
# (CadCraft: only where it is written as a command, see cadtokens below). That is a lower bound on
# what the skill teaches (a workflow can be described without naming every command) and an upper bound on
# what was tested (an id can be named without being run). Unit: engine commands for the Craft apps,
# MCP tools for ONLYOFFICE (names listed in onlyoffice/tool-names.txt).
dir=${AIMG:-"$HOME/AppImages"}
repo=$(cd "$(dirname "$0")" && pwd)
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT

tokens() { grep -rIhoE --exclude='tool-names.txt' --exclude-dir='__pycache__' -e '-?[A-Za-z0-9_][A-Za-z0-9_.]*' "$1" | LC_ALL=C sort -u; }

# CadCraft ids are often plain words (line, copy, join), so for CadCraft an id counts only where it is written as a
# command: any word in a fenced code block, the leading id (or `a|b|c` group of ids) of an inline code span, or a
# quoted string in a tools/*.py file. "join the working set" in prose no longer counts as documenting `join`.
cadtokens() {
    python3 -I - "$1" <<'EOF' | LC_ALL=C sort -u
import pathlib, re, sys
ID = r"-?[A-Za-z0-9_][A-Za-z0-9_.]*"
out = set()
for f in pathlib.Path(sys.argv[1]).rglob("*"):
    if not f.is_file() or "__pycache__" in f.parts: continue
    t = f.read_text(errors="ignore")
    if f.suffix == ".py":
        out |= set(re.findall(r"""["'](%s)["']""" % ID, t))
    elif f.suffix == ".md":
        for block in re.findall(r"```.*?\n(.*?)```", t, re.S): out |= set(re.findall(ID, block))
        for span in re.findall(r"`([^`\n]+)`", re.sub(r"```.*?```", "", t, flags=re.S)):
            m = re.match(r"\s*(?:--cmd[= ]'?)?(%s(?:\|%s)*)" % (ID, ID), span)
            if m: out |= set(m.group(1).split("|"))
print("\n".join(out))
EOF
}

for app in wordcraft gridcraft deckcraft photocraft cadcraft pdfcraft filmcraft lightcraft vectorcraft designcraft; do
    cli="$dir/$app-cli"; [ -x "$cli" ] || { echo "$app: no CLI at $cli" >&2; continue; }
    ver=$("$cli" --version 2>/dev/null | sed -n '1s/.*\([0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\).*/\1/p')
    if [ "$app" = pdfcraft ]; then
        "$cli" tools 2>/dev/null | python3 -c 'import json,sys;print("\n".join(x["name"] for x in json.load(sys.stdin)))'   # PdfCraft: tools, not commands
    elif [ "$app" = filmcraft ]; then
        "$cli" commands --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);d=d if isinstance(d,list) else d["commands"];print("\n".join(x["id"] for x in d))'
    elif [ "$app" = photocraft ] || [ "$app" = cadcraft ] || [ "$app" = vectorcraft ] || [ "$app" = designcraft ]; then
        if [ "$app" = cadcraft ] || [ "$app" = vectorcraft ] || [ "$app" = designcraft ]; then cargs=commands; else cargs="commands --json"; fi   # cadcraft-cli prints JSON from plain `commands`
        "$cli" $cargs 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);d=d if isinstance(d,list) else d["commands"];print("\n".join(x["id"] for x in d))'
    else
        "$cli" commands 2>/dev/null | grep -oE '^[a-z][A-Za-z0-9]*\.[A-Za-z0-9.]+'
    fi | LC_ALL=C sort -u > "$tmp/$app.all"
    if [ "$app" = cadcraft ]; then cadtokens "$repo/$app"; else tokens "$repo/$app"; fi > "$tmp/$app.tok"
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

# GenOffice: the unit is the ops documented by `genoffice guide docs|sheets|slides` (listed by genoffice-supplement/op_names.py;
# editor-only sheet ops and not-AI-callable slide ops are excluded). The supplement is supplementary: this counts how many of those ops it names.
if command -v genoffice >/dev/null 2>&1 && [ -f "$repo/genoffice-supplement/op_names.py" ]; then
    python3 -I "$repo/genoffice-supplement/op_names.py" | LC_ALL=C sort -u > "$tmp/go.pairs"
    awk '{print $2}' "$tmp/go.pairs" | LC_ALL=C sort -u > "$tmp/go.all"
    tokens "$repo/genoffice-supplement" > "$tmp/go.tok"
    total=$(wc -l < "$tmp/go.all"); have=$(LC_ALL=C comm -12 "$tmp/go.all" "$tmp/go.tok" | wc -l)
    printf '%-11s %-7s %4s / %-4s ops documented (%s%%)\n' genoffice "$(genoffice --version | sed 's/[^0-9.]//g')" "$have" "$total" "$((100 * have / total))"
fi
