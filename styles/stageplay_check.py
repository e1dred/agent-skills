"""Check a .docx against the stage-play layout this repo builds (common US playwright submission format). Read-only, standard library only.

    python3 -I stageplay_check.py play.docx [more.docx]      exit code 1 if any check FAILs

Reads page margins (1 in), Times New Roman or Courier New 12 pt single-spaced, centred capital character cues, italic indented stage
directions and parentheticals, centred bold act and scene headings, a title page that is its own section, a characters page, and a page-number
header (title and number) that restarts at 1 and is not printed on the first page after the title page. Theatres, publishers (Samuel French,
Dramatists Play Service) and contests set their own rules: those always win. PASS / WARN / FAIL.
"""
import html, re, sys, zipfile

WANT = {   # style: (indent left in, indent right in, alignment, italic)
    "ST Cue": (0.0, 0.0, "center", False), "ST Speech": (0.0, 0.0, "left", False), "ST Direction": (1.0, 0.5, "left", True),
    "ST Parenthetical": (1.0, 1.0, "left", True), "ST Act": (0.0, 0.0, "center", False), "ST Scene": (0.0, 0.0, "center", False),
}


def text_of(x): return html.unescape(re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", re.sub(r"<w:tab/>", "\t", x))))


def check(path):
    res = []
    add = lambda lvl, msg: res.append((lvl, msg))
    z = zipfile.ZipFile(path)
    doc = z.read("word/document.xml").decode("utf8", "replace")
    styles = z.read("word/styles.xml").decode("utf8", "replace")
    names = {}
    for m in re.finditer(r'<w:style [^>]*?w:styleId="([^"]+)"[^>]*>(.*?)</w:style>', styles, re.S):
        nm = re.search(r'<w:name w:val="([^"]+)"', m.group(2))
        names[m.group(1)] = (nm.group(1) if nm else m.group(1), m.group(2))
    by_name = {nm: body for nm, body in names.values()}
    sects = re.findall(r"<w:sectPr.*?</w:sectPr>", doc, re.S)
    last = sects[-1] if sects else ""
    mar = re.search(r"<w:pgMar([^>]*)/?>", last)
    if mar:
        v = {k: int(x) for k, x in re.findall(r'w:(top|bottom|left|right)="(-?\d+)"', mar.group(1))}
        add("PASS" if all(abs(v.get(k, 0) - 1440) <= 40 for k in ("top", "bottom", "left", "right")) else "FAIL",
            "margins L %.2f R %.2f T %.2f B %.2f in (want 1 each)" % tuple(v.get(k, 0) / 1440 for k in ("left", "right", "top", "bottom")))
    else:
        add("FAIL", "no page margins found")
    add("PASS" if len(sects) >= 2 else "WARN", "title page is its own section: %s" % ("yes" if len(sects) >= 2 else "no (page numbers will count it)"))
    add("PASS" if "<w:titlePg" in last else "FAIL", "no page number on the first page after the title page: %s" % ("yes" if "<w:titlePg" in last else "NO"))
    start = re.search(r'<w:pgNumType[^>]*w:start="(\d+)"', last)
    add("PASS" if start and start.group(1) == "1" else "WARN", "numbering restarts at 1 after the title page: %s" % (start.group(1) if start else "not set"))
    hx = "".join(z.read(n).decode("utf8", "replace") for n in z.namelist() if re.match(r"word/header\d*\.xml", n))
    add("PASS" if "PAGE" in hx and text_of(hx).strip() else "FAIL", "header with the title and a page number: %r" % text_of(hx).strip()[:50])
    body = by_name.get("Normal", "")
    font = re.search(r'<w:rFonts [^>]*w:ascii="([^"]+)"', body); f = (font.group(1) if font else "?")
    add("PASS" if any(x in f.lower() for x in ("times", "courier", "liberation serif")) else "FAIL", "body font: %s" % f)
    size = re.search(r'<w:sz w:val="(\d+)"', body)
    add("PASS" if size and int(size.group(1)) == 24 else "FAIL", "body size: %s pt" % (int(size.group(1)) / 2 if size else "?"))
    ln = re.search(r'<w:spacing [^>]*w:line="(\d+)"', body)
    add("PASS" if (not ln or int(ln.group(1)) <= 280) else "WARN", "line spacing: %s (single = 240)" % (ln.group(1) if ln else "default single"))
    for nm, (wl, wr, wj, wi) in WANT.items():
        sb = by_name.get(nm)
        if not sb:
            add("WARN", "style %r not found (a play made another way?)" % nm); continue
        ind = re.search(r"<w:ind ([^>]*)/?>", sb)
        l = int(re.search(r'w:(?:left|start)="(-?\d+)"', ind.group(1)).group(1)) / 1440 if ind and re.search(r'w:(?:left|start)="(-?\d+)"', ind.group(1)) else 0.0
        r = int(re.search(r'w:(?:right|end)="(-?\d+)"', ind.group(1)).group(1)) / 1440 if ind and re.search(r'w:(?:right|end)="(-?\d+)"', ind.group(1)) else 0.0
        jc = re.search(r'<w:jc w:val="(\w+)"', sb); j = {"both": "justify", "start": "left", "end": "right"}.get(jc.group(1), jc.group(1)) if jc else "left"
        it = bool(re.search(r"<w:i/>|<w:i w:val=\"(1|true|on)\"", sb))
        ok = abs(l - wl) <= 0.05 and abs(r - wr) <= 0.05 and j == wj and it == wi
        add("PASS" if ok else "FAIL", "%s: indents %.2f/%.2f in, %s%s (want %.1f/%.1f, %s%s)" % (nm, l, r, j, ", italic" if it else "", wl, wr, wj, ", italic" if wi else ""))
    paras = re.findall(r"<w:p[ >].*?</w:p>", doc, re.S)
    by = {}
    for p in paras:
        sm = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        if sm: by.setdefault(names.get(sm.group(1), (sm.group(1),))[0], []).append(text_of(p).strip())
    cues = by.get("ST Cue", [])
    low = [c for c in cues if re.search(r"[a-z]", c)]
    add("FAIL" if low else "PASS", "character cues in capitals: %d of %d%s" % (len(cues) - len(low), len(cues), (" (e.g. %r)" % low[0]) if low else ""))
    for nm, rx in (("ST Act", r"^ACT\b"), ("ST Scene", r"^SCENE\b")):
        bad = [t for t in by.get(nm, []) if not re.match(rx, t, re.I)]
        add("WARN" if bad else "PASS", "%s headings read ACT/SCENE: %d of %d" % (nm[3:], len(by.get(nm, [])) - len(bad), len(by.get(nm, []))))
    add("PASS" if by.get("ST Cast Heading") else "WARN", "a CHARACTERS page: %s" % ("yes (%d characters)" % len(by.get("ST Cast", [])) if by.get("ST Cast Heading") else "not found"))
    add("PASS" if cues else "WARN", "elements: %s" % ", ".join("%s %d" % (k[3:], len(v)) for k, v in sorted(by.items())))
    try:
        import json, os, shutil, subprocess
        cli = os.environ.get("WORDCRAFT_CLI") or shutil.which("wordcraft-cli") or os.path.expanduser("~/AppImages/wordcraft-cli")
        pages = int(json.loads(subprocess.run([cli, "info", path], capture_output=True, text=True, timeout=60).stdout)["pages"])
        add("PASS", "pages: %d including the title page" % pages)
    except Exception:
        pass
    return res


if __name__ == "__main__":
    worst = 0
    for f in sys.argv[1:]:
        print("==", f)
        for lvl, msg in check(f):
            print("  %-4s %s" % (lvl, msg)); worst = max(worst, {"PASS": 0, "WARN": 0, "FAIL": 1}[lvl])
    sys.exit(worst)
