"""Check a .docx against the standard spec-script (screenplay) layout. Read-only, standard library only.

    python3 -I screenplay_check.py script.docx [more.docx]      exit code 1 if any check FAILs

Reads page margins (left 1.5 in, right/top/bottom 1 in), Courier 12 pt with a fixed 12 pt line pitch (6 lines per inch, which is what makes
"one page is about one minute" work), the indents of each element (action, scene heading, character cue, dialogue, parenthetical, transition),
that scene headings, cues and transitions are capitals, a title page that is its own section, and a page-number header that is not printed on the
first script page and restarts at 1. Rules are the common spec-script defaults; a producer's, contest's or studio's own rules win. PASS / WARN / FAIL.
"""
import html, re, sys, zipfile

WANT = {   # style name: (indent left in, indent right in, alignment)
    "SP Action": (0.0, 0.0, "left"), "SP Scene Heading": (0.0, 0.0, "left"), "SP Character": (2.2, 0.0, "left"),
    "SP Dialogue": (1.0, 1.5, "left"), "SP Parenthetical": (1.6, 2.0, "left"), "SP Transition": (0.0, 0.0, "right"),
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
        ok = abs(v.get("left", 0) - 2160) <= 40 and all(abs(v.get(k, 0) - 1440) <= 40 for k in ("right", "top", "bottom"))
        add("PASS" if ok else "FAIL", "margins L %.2f R %.2f T %.2f B %.2f in (want 1.5 / 1 / 1 / 1)" % tuple(v.get(k, 0) / 1440 for k in ("left", "right", "top", "bottom")))
    else:
        add("FAIL", "no page margins found")
    add("PASS" if len(sects) >= 2 else "WARN", "title page is its own section: %s" % ("yes (%d sections)" % len(sects) if len(sects) >= 2 else "no (script numbering will count the title page)"))
    add("PASS" if "<w:titlePg" in last else "FAIL", "script section: no page number on its first page (title-page setting): %s" % ("yes" if "<w:titlePg" in last else "NO"))
    start = re.search(r'<w:pgNumType[^>]*w:start="(\d+)"', last)
    add("PASS" if start and start.group(1) == "1" else "WARN", "script section restarts page numbering at 1: %s" % (start.group(1) if start else "not set"))
    hx = "".join(z.read(n).decode("utf8", "replace") for n in z.namelist() if re.match(r"word/header\d*\.xml", n))
    add("PASS" if "PAGE" in hx and re.search(r'<w:jc w:val="right"', hx) else "FAIL", "page number in a right-aligned header: %s" % ("yes" if "PAGE" in hx else "NO"))
    add("PASS" if re.search(r">\.<", hx) or "." in text_of(hx) else "WARN", "page number followed by a period (\"2.\"): %s" % ("yes" if "." in text_of(hx) else "no"))

    for nm in ["Normal"] + list(WANT):
        body = by_name.get(nm, "")
        if not body and nm != "Normal":
            add("WARN", "style %r not found (a script made another way?)" % nm); continue
        font = re.search(r'<w:rFonts [^>]*w:ascii="([^"]+)"', body)
        size = re.search(r'<w:sz w:val="(\d+)"', body)
        if nm == "Normal" or font:
            f = font.group(1) if font else "?"
            add("PASS" if "courier" in f.lower() else "FAIL", "%s font: %s%s" % (nm, f, "" if size is None else ", %g pt" % (int(size.group(1)) / 2)))
        if size and int(size.group(1)) != 24: add("FAIL", "%s size is not 12 pt" % nm)
        ln = re.search(r'<w:spacing [^>]*w:line="(\d+)"[^>]*w:lineRule="(\w+)"', body) or re.search(r'<w:spacing [^>]*w:lineRule="(\w+)"[^>]*w:line="(\d+)"', body)
        if ln:
            line = int(ln.group(1)) if ln.group(1).isdigit() else int(ln.group(2)); rule = ln.group(2) if ln.group(1).isdigit() else ln.group(1)
            add("PASS" if rule == "exact" and line == 240 else "FAIL", "%s line pitch: %s %s (want exact 240 = 12 pt)" % (nm, line, rule))
        elif nm == "Normal":
            add("FAIL", "Normal has no fixed line pitch")
        if nm in WANT:
            wl, wr, wj = WANT[nm]
            ind = re.search(r"<w:ind ([^>]*)/?>", body)
            l = int(re.search(r'w:(?:left|start)="(-?\d+)"', ind.group(1)).group(1)) / 1440 if ind and re.search(r'w:(?:left|start)="(-?\d+)"', ind.group(1)) else 0.0
            r = int(re.search(r'w:(?:right|end)="(-?\d+)"', ind.group(1)).group(1)) / 1440 if ind and re.search(r'w:(?:right|end)="(-?\d+)"', ind.group(1)) else 0.0
            jc = re.search(r'<w:jc w:val="(\w+)"', body); j = {"both": "justify", "start": "left", "end": "right"}.get(jc.group(1), jc.group(1)) if jc else "left"
            ok = abs(l - wl) <= 0.05 and abs(r - wr) <= 0.05 and j == wj
            add("PASS" if ok else "FAIL", "%s indents left %.2f right %.2f in, %s (want %.1f / %.1f, %s)" % (nm, l, r, j, wl, wr, wj))

    paras = re.findall(r"<w:p[ >].*?</w:p>", doc, re.S)
    bad = {"SP Scene Heading": [], "SP Character": [], "SP Transition": []}
    counts = {}
    for p in paras:
        sm = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        if not sm: continue
        nm = names.get(sm.group(1), (sm.group(1),))[0]
        counts[nm] = counts.get(nm, 0) + 1
        t = text_of(p).strip()
        if nm in bad and t and re.search(r"[a-z]", t): bad[nm].append(t[:30])
    for nm, lst in bad.items():
        add("FAIL" if lst else "PASS", "%s text is in capitals: %s" % (nm, ("%d not (e.g. %r)" % (len(lst), lst[0])) if lst else "yes"))
    heads = []
    for p in paras:
        sm = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        if sm and names.get(sm.group(1), ("",))[0] == "SP Scene Heading": heads.append(text_of(p).strip())
    badh = [h for h in heads if h and not re.match(r"(INT\.|EXT\.|EST\.|INT\./EXT\.|INT/EXT|I/E)", h)]
    add("WARN" if badh else "PASS", "scene headings start with INT./EXT.: %d of %d%s" % (len(heads) - len(badh), len(heads), (" (e.g. %r)" % badh[0]) if badh else ""))
    add("PASS" if counts.get("SP Dialogue") else "WARN", "elements: " + ", ".join("%s %d" % (k.replace("SP ", ""), v) for k, v in sorted(counts.items())))
    return res


if __name__ == "__main__":
    worst = 0
    for f in sys.argv[1:]:
        print("==", f)
        for lvl, msg in check(f):
            print("  %-4s %s" % (lvl, msg)); worst = max(worst, {"PASS": 0, "WARN": 0, "FAIL": 1}[lvl])
    sys.exit(worst)
