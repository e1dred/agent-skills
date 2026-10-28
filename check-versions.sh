#!/bin/sh
# Report whether the desktop apps and their CLIs are up to date. Read-only; changes nothing.
# Usage: ./check-versions.sh            (AppImages in $AIMG, default ~/AppImages; apps in $APPS)
# For each app in $APPS: prints the app version, the installed <app>-cli version, and flags a mismatch.
# Only apps in $APPS are run with --version, because some AppImages ignore the flag and start their window
# (GenOffice, MangoDisk, Sonora and Concat do). Add an app to APPS only after checking that `<app>.appimage --version` prints and exits.
# GenOffice is checked separately below, against the vendor's update feed (GearLever once installed 0.12.115 over 0.12.117).
# A CLI older than its app has misbehaved before (live bridge timeouts), so refresh it:
#   ./<app>.appimage --appimage-extract   # then copy squashfs-root/usr/bin/<app>-cli over ~/AppImages/<app>-cli (keep a .bak)
dir=${AIMG:-"$HOME/AppImages"}
first() { sed -n '1p'; }
num() { grep -oE '[0-9]+\.[0-9]+(\.[0-9]+)?' | head -1; }
for app in ${APPS:-photocraft gridcraft deckcraft wordcraft}; do
    img="$dir/$app.appimage"
    [ -x "$img" ] || continue
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
# GenOffice: its AppImage opens the GUI on --version, so compare the file with the vendor's update feed instead (size and SHA-512 of the AppImage),
# and the `genoffice` CLI (a separate extraction) with the feed's version. Needs network; says so and moves on when the feed cannot be read.
go="$dir/genoffice.appimage"
if [ -f "$go" ]; then
    feed=${GENOFFICE_FEED:-https://cdn1.genspark.ai/user-upload-image/client/genoffice/latest-linux.yml}
    cli=$(command -v genoffice >/dev/null 2>&1 && genoffice --version 2>/dev/null | first | num)
    python3 -I - "$go" "$feed" "${cli:-?}" <<'PYEOF'
import base64, hashlib, re, sys, urllib.request
path, feed, cli = sys.argv[1:4]
try:
    y = urllib.request.urlopen(urllib.request.Request(feed, headers={"User-Agent": "curl/8"}), timeout=20).read().decode()   # the CDN refuses Python's default agent
except Exception as e:
    print("%-12s feed not readable (%s); AppImage not compared" % ("genoffice", type(e).__name__)); sys.exit(0)
ver = (re.search(r"^version:\s*(\S+)", y, re.M) or [0, "?"])[1]
m = re.search(r"url:\s*\S*\.AppImage\s*\n\s*sha512:\s*(\S+)\s*\n\s*size:\s*(\d+)", y)
if not m:
    print("%-12s feed has no AppImage entry" % "genoffice"); sys.exit(0)
sha, size = m.group(1), int(m.group(2))
import os
loc_size = os.path.getsize(path)
loc_sha = base64.b64encode(hashlib.sha512(open(path, "rb").read()).digest()).decode()
if loc_size == size and loc_sha == sha: st = "AppImage matches the feed (latest)"
else: st = "AppImage DIFFERS from the feed's latest (size %d vs %d): update, or it is an older build" % (loc_size, size)
note = "" if cli in ("?", ver) else "; CLI is %s, feed %s (re-extract the AppImage)" % (cli, ver)
print("%-12s feed %-8s cli %-8s %s%s" % ("genoffice", ver, cli, st, note))
PYEOF
fi
if command -v flatpak >/dev/null 2>&1 && flatpak info org.onlyoffice.desktopeditors >/dev/null 2>&1; then
    v=$(flatpak info org.onlyoffice.desktopeditors | sed -n 's/^ *Version: *//p')
    up=$(timeout 60 flatpak remote-ls --updates --columns=application,version 2>/dev/null | grep -i onlyoffice)
    printf '%-12s flatpak %s  %s\n' onlyoffice "$v" "${up:+UPDATE AVAILABLE: $up}"
fi
