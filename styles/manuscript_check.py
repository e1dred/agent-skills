"""Check a .docx against standard manuscript format (publisher/agent submissions). Read-only, standard library only.

    python3 -I manuscript_check.py book.docx [more.docx]      exit code 1 if any check FAILs

It reads the file the way a submissions editor opens it: page size and margins, the body paragraph style (font, size, line spacing,
first-line indent, spacing between paragraphs, alignment), a header with the author's surname, title and page number that is NOT on page 1,
a title block with contact details and an approximate word count, real heading styles for chapters, no manual indents by tabs or spaces,
no underlining or colour in the body, and a word count that matches the "about N words" line. Rules are the common defaults
(US "standard manuscript format"); a publisher's or agent's own guidelines always win. PASS / WARN / FAIL per check.
"""
import re, sys, zipfile

MONO = ("courier",)
SERIF = ("times new roman", "times", "liberation serif", "tinos")


def text_of(x): return re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", re.sub(r"<w:tab/>", "\t", x)))


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

    def style_by_name(n):
        for sid, (nm, body) in names.items():
            if nm.lower() == n.lower(): return sid, body
        return None, ""

    # page and margins
    sect = re.findall(r"<w:sectPr.*?</w:sectPr>", doc, re.S)
    sp = sect[-1] if sect else ""
    mar = re.search(r"<w:pgMar([^>]*)/?>", sp)
    if mar:
        vals = {k: int(v) for k, v in re.findall(r'w:(top|bottom|left|right)="(-?\d+)"', mar.group(1))}
        ok = all(abs(vals.get(k, 0) - 1440) <= 30 for k in ("top", "bottom", "left", "right"))
        add("PASS" if ok else "FAIL", "margins %s (twips; 1440 = 1 inch)" % (", ".join("%s %d" % kv for kv in sorted(vals.items()))))
    else:
        add("FAIL", "no page margins found")
    pg = re.search(r'<w:pgSz[^>]*w:w="(\d+)"[^>]*w:h="(\d+)"', sp) or (lambda m: m)(None)
    if not pg:
        mw = re.search(r'<w:pgSz[^>]*w:w="(\d+)"', sp); mh = re.search(r'<w:pgSz[^>]*w:h="(\d+)"', sp)
        pg = type("M", (), {"group": lambda self, i, a=(mw, mh): a[i - 1].group(1)})() if mw and mh else None
    if pg:
        w, h = int(pg.group(1)), int(pg.group(2))
        kind = "US Letter" if (abs(w - 12240) < 40 and abs(h - 15840) < 40) else "A4" if (abs(w - 11906) < 40 and abs(h - 16838) < 40) else "other"
        add("PASS" if kind != "other" else "WARN", "page size: %s" % kind)

    # body style
    sid, body = style_by_name("Normal")
    font = re.search(r'<w:rFonts [^>]*w:ascii="([^"]+)"', body)
    dfl = re.search(r'<w:docDefaults>.*?<w:rFonts [^>]*w:ascii="([^"]+)"', styles, re.S)
    fname = (font.group(1) if font else (dfl.group(1) if dfl else "?"))
    size = re.search(r'<w:sz w:val="(\d+)"', body)
    dsz = re.search(r'<w:docDefaults>.*?<w:sz w:val="(\d+)"', styles, re.S)
    pts = int((size.group(1) if size else (dsz.group(1) if dsz else "0"))) / 2
    f = fname.lower()
    add("PASS" if (any(x in f for x in MONO) or any(x in f for x in SERIF)) else "FAIL", "body font: %s (Times New Roman or Courier New expected)" % fname)
    add("PASS" if pts == 12 else "FAIL", "body size: %g pt" % pts)
    ln = re.search(r'<w:spacing [^>]*w:line="(\d+)"[^>]*', body)
    rule = re.search(r'<w:spacing [^>]*w:lineRule="(\w+)"', body)
    line = int(ln.group(1)) if ln else 240
    double = (not rule or rule.group(1) == "auto") and abs(line - 480) <= 12 or (rule and rule.group(1) in ("exact", "atLeast") and line in (480, 576))
    add("PASS" if double else "FAIL", "body line spacing: %s (double = 480 auto)" % ("%d %s" % (line, rule.group(1) if rule else "auto")))
    ind = re.search(r'<w:ind [^>]*w:firstLine="(\d+)"', body)
    add("PASS" if ind and abs(int(ind.group(1)) - 720) <= 40 else "WARN", "first-line indent: %s (0.5 in = 720 twips)" % (ind.group(1) if ind else "none"))
    af = re.search(r'<w:spacing [^>]*w:after="(\d+)"', body); bf = re.search(r'<w:spacing [^>]*w:before="(\d+)"', body)
    add("PASS" if (not af or int(af.group(1)) == 0) and (not bf or int(bf.group(1)) == 0) else "FAIL",
        "no extra space between paragraphs: after=%s before=%s" % (af.group(1) if af else 0, bf.group(1) if bf else 0))
    add("FAIL" if re.search(r'<w:jc w:val="(both|distribute)"', body) else "PASS", "body alignment: ragged right (not justified)")

    # header / title page
    titlepg = "<w:titlePg" in sp
    add("PASS" if titlepg else "FAIL", "page 1 has its own (empty) header: %s" % ("yes" if titlepg else "NO (running header would print on the title page)"))
    hdr = ""
    for n in z.namelist():
        if re.match(r"word/header\d*\.xml", n): hdr += text_of(z.read(n).decode("utf8", "replace")) + "\n"
    hx = "".join(z.read(n).decode("utf8", "replace") for n in z.namelist() if re.match(r"word/header\d*\.xml", n))
    has_num = bool(re.search(r"PAGE", hx))
    add("PASS" if hdr.strip() and has_num else "FAIL", "running header with page number: %r" % hdr.strip()[:60])
    paras = re.findall(r"<w:p[ >].*?</w:p>", doc, re.S)
    ptexts = [text_of(p).strip("\n") for p in paras]
    first = [t for t in ptexts[:8] if t.strip()]
    wc = None
    for t in first:
        m = re.search(r"about ([\d,]+) words", t)
        if m: wc = int(m.group(1).replace(",", "")); break
    add("PASS" if wc else "WARN", "title block has \"about N words\": %s" % (wc if wc else "not found"))
    add("PASS" if any(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", t) for t in first) else "WARN", "title block has an e-mail address")
    add("PASS" if any(t.lower().startswith("by ") for t in ptexts[:20]) else "WARN", "byline (\"by Name\") under the title")

    # chapters and body
    heads = []
    for p in paras:
        sm = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        if sm and names.get(sm.group(1), ("",))[0].lower().startswith("heading"): heads.append(text_of(p).strip())
    add("PASS" if heads else "WARN", "chapter headings use a Heading style: %d%s" % (len(heads), "" if heads else " (use Heading 1 so editors can navigate)"))
    body_text = []
    for p in paras:
        sm = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        nm = names.get(sm.group(1), ("Normal",))[0] if sm else "Normal"
        if nm in ("Normal", "MS Body First"): body_text.append(text_of(p).strip())
    nwords = sum(len(t.split()) for t in body_text)
    if wc:
        diff = abs(nwords - wc) / max(wc, 1)
        add("PASS" if diff <= 0.12 else "WARN", "word count line (%d) vs body text (%d): %.0f%% apart" % (wc, nwords, diff * 100))
    manual = [t for t in body_text if t.startswith("\t") or re.match(r"^ {2,}\S", t)]
    add("FAIL" if manual else "PASS", "no indents made with tabs or spaces: %d paragraph(s) start with one" % len(manual))
    add("FAIL" if "<w:u " in doc.replace("<w:u w:val=\"none\"", "") else "PASS", "no underlining in the text (use italics for emphasis)")
    add("WARN" if re.search(r"<w:color w:val=\"(?!000000|auto)", doc) else "PASS", "text is black")
    add("WARN" if "<w:drawing" in doc else "PASS", "no pictures in the manuscript")
    run = 0; worst = 0
    for t in ptexts:
        run = run + 1 if not t.strip() else 0; worst = max(worst, run)
    add("WARN" if worst > 7 else "PASS", "longest run of empty paragraphs: %d (a chapter opening uses 6 on purpose)" % worst)
    return res


if __name__ == "__main__":
    worst = 0
    for f in sys.argv[1:]:
        print("==", f)
        for lvl, msg in check(f):
            print("  %-4s %s" % (lvl, msg)); worst = max(worst, {"PASS": 0, "WARN": 0, "FAIL": 1}[lvl])
    sys.exit(worst)
