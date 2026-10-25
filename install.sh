#!/bin/sh
# Link skills from this repo into ~/.claude/skills (or $SKILLS_DIR).
# Usage: ./install.sh            link every skill
#        ./install.sh wordcraft  link only the named skills
# Never overwrites anything: an existing file or folder of the same name is left alone.
set -eu

repo=$(cd "$(dirname "$0")" && pwd)
dest=${SKILLS_DIR:-"$HOME/.claude/skills"}
mkdir -p "$dest"

if [ $# -eq 0 ]; then
    set --
    for d in "$repo"/*/; do
        [ -f "$d/SKILL.md" ] && set -- "$@" "$(basename "$d")"
    done
fi

status=0
for name in "$@"; do
    src="$repo/$name"
    link="$dest/$name"
    if [ ! -f "$src/SKILL.md" ]; then
        echo "skip $name: no such skill in $repo" >&2; status=1
    elif [ -L "$link" ] && [ "$(readlink "$link")" = "$src" ]; then
        echo "ok   $name (already linked)"
    elif [ -e "$link" ] || [ -L "$link" ]; then
        echo "skip $name: $link already exists; move it away and run again" >&2; status=1
    else
        ln -s "$src" "$link"
        echo "link $link -> $src"
    fi
done
exit $status
