#!/bin/sh
# Report whether the desktop apps and their CLIs are up to date. Read-only; changes nothing.
# Usage: ./check-versions.sh            (AppImages in $AIMG, default ~/AppImages)
# For each <app>.appimage: prints the app version, the installed <app>-cli version, and flags a mismatch.
# A CLI older than its app has misbehaved before (live bridge timeouts), so refresh it:
#   ./<app>.appimage --appimage-extract   # then copy squashfs-root/usr/bin/<app>-cli over ~/AppImages/<app>-cli (keep a .bak)
dir=${AIMG:-"$HOME/AppImages"}
first() { sed -n '1p'; }
num() { grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?' | head -1; }
for img in "$dir"/*.appimage; do
    [ -e "$img" ] || continue
    app=$(basename "$img" .appimage)
    av=$(timeout 25 "$img" --version 2>/dev/null | first | num)
    if [ -x "$dir/$app-cli" ]; then
        cv=$("$dir/$app-cli" --version 2>/dev/null | first | num)
        [ -n "$cv" ] || cv=$("$dir/$app-cli" version 2>/dev/null | first | num)
        if [ "$av" = "$cv" ]; then st=ok; else st="CLI differs: re-extract"; fi
        printf '%-12s app %-8s cli %-8s %s\n' "$app" "${av:-?}" "${cv:-?}" "$st"
    else
        printf '%-12s app %-8s (no CLI installed)\n' "$app" "${av:-?}"
    fi
done
if command -v flatpak >/dev/null 2>&1 && flatpak info org.onlyoffice.desktopeditors >/dev/null 2>&1; then
    v=$(flatpak info org.onlyoffice.desktopeditors | sed -n 's/^ *Version: *//p')
    up=$(timeout 60 flatpak remote-ls --updates --columns=application,version 2>/dev/null | grep -i onlyoffice)
    printf '%-12s flatpak %s  %s\n' onlyoffice "$v" "${up:+UPDATE AVAILABLE: $up}"
fi
