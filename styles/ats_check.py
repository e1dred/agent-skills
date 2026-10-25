"""ATS lint for a .docx résumé or CV: flags the structures that commonly break applicant-tracking parsers.

    python3 -I ats_check.py resume.docx [more.docx ...]      # prints PASS / WARN / FAIL lines; exit code 1 if any FAIL

This is a checklist built from common ATS guidance, NOT a real parser and not a guarantee: it reads the .docx XML (read-only) and reports
- FAIL  tables, text boxes, more than one column, contact details only in a header/footer, no e-mail address in the body
- WARN  pictures, glyph bullets typed as text, headings an ATS may not recognise, fewer than two dates, headers/footers with text
- PASS  everything else it looked at
Use it on a copy of your own résumé, or on the styles' résumé output; nothing is modified and no text of the file is printed except heading names.
"""
import re, sys, zipfile

HEADINGS = {
    "summary": r"summary|profile|objective|about",
    "experience": r"experience|employment|work history|career",
    "education": r"education|training|qualification|academic",
    "skills": r"skill|competenc|expertise|technolog",
    "certifications": r"certif|licen[cs]e|accreditation|award|honou?r",
    "languages": r"language",
    "projects": r"project",
    "publications": r"publication|research",
    "interests": r"interest|volunteer|activities",
    "achievements": r"achievement|highlights?",
    "contact": r"contact|personal (details|information)",
    "additional": r"additional|other",
}
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
PHONE = re.compile(r"(\+?\d[\d\s().-]{7,}\d)")
DATE = re.compile(r"((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.? ?\d{4})|(\b\d{1,2}/\d{4}\b)|(\b(19|20)\d{2}\b)", re.I)


def text_of(xml):
    return re.sub(r"\s+", " ", "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", xml))).strip()


def check(path):
    z = zipfile.ZipFile(path)
    doc = z.read("word/document.xml").decode("utf8", "replace")
    styles = z.read("word/styles.xml").decode("utf8", "replace") if "word/styles.xml" in z.namelist() else ""
    res = []
    add = lambda level, msg: res.append((level, msg))

    ntbl = len(re.findall(r"<w:tbl>", doc))
    add("FAIL" if ntbl else "PASS", "tables: %d%s" % (ntbl, " (layout tables are often read cell by cell, out of order)" if ntbl else ""))
    ntx = len(re.findall(r"<w:txbxContent|<v:textbox|<wps:txbx", doc))
    add("FAIL" if ntx else "PASS", "text boxes: %d%s" % (ntx, " (many parsers skip them entirely)" if ntx else ""))
    cols = [int(n) for n in re.findall(r'<w:cols [^>]*w:num="(\d+)"', doc)]
    add("FAIL" if any(n > 1 for n in cols) else "PASS", "columns: %s" % ("max %d" % max(cols) if cols else "single"))
    npic = len(re.findall(r"<w:drawing>|<w:pict>", doc))
    add("WARN" if npic else "PASS", "pictures/drawings: %d%s" % (npic, " (ignored by ATS; text inside images is lost)" if npic else ""))

    hf = []
    for n in z.namelist():
        if re.match(r"word/(header|footer)\d*\.xml", n):
            t = text_of(z.read(n).decode("utf8", "replace"))
            hf.append((n, t))
    body = text_of(doc)
    hf_text = " ".join(t for _, t in hf)
    contact_in_hf = bool(EMAIL.search(hf_text) or PHONE.search(hf_text))
    if contact_in_hf and not (EMAIL.search(body)):
        add("FAIL", "contact details only in a header/footer (many parsers skip them)")
    elif contact_in_hf:
        add("WARN", "contact details also appear in a header/footer")
    elif hf_text.strip():
        add("WARN", "header/footer has text (%d chars); parsers may skip it, so keep nothing important there" % len(hf_text))
    else:
        add("PASS", "headers/footers: no important text")

    add("PASS" if EMAIL.search(body) else "FAIL", "e-mail address in the body: %s" % ("yes" if EMAIL.search(body) else "NO"))
    add("PASS" if PHONE.search(body) else "WARN", "phone number in the body: %s" % ("yes" if PHONE.search(body) else "not found"))

    names = {m.group(1): m.group(2) for m in re.finditer(r'<w:style [^>]*w:styleId="([^"]+)"[^>]*>\s*<w:name w:val="([^"]+)"', styles)}
    paras = re.findall(r"<w:p[ >].*?</w:p>", doc, re.S)
    heads, glyph, listed = [], 0, 0
    for p in paras:
        sm = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        t = text_of(p)
        sname = names.get(sm.group(1), sm.group(1)) if sm else ""   # ONLYOFFICE writes numeric style ids; the NAME is what parsers read
        if sm and re.match(r"(heading ?\d|title)", sname, re.I) and t:
            heads.append(t)
        if re.search(r"<w:numPr>.*?<w:numId w:val=\"[1-9]", p, re.S): listed += 1
        elif re.match(r"^\s*[•▪●•\-\*–>]\s+\S", t): glyph += 1
    # style-level numbering (a "List Bullet" style) also counts as real bullets
    if not listed and re.search(r"<w:style [^>]*w:styleId=\"[^\"]*(List|Bullet)[^\"]*\".*?<w:numPr>", styles, re.S): listed = 1
    add("WARN" if glyph else "PASS", "bullets: %d real list items, %d typed glyph bullets%s" % (listed, glyph, " (use a real list)" if glyph else ""))

    if not heads:
        add("WARN", "no Heading-styled paragraphs: parsers rely on heading styles or all-caps/bold lines to find sections")
    else:
        unknown = []
        for h in heads:
            if not any(re.search(rx, h, re.I) for rx in HEADINGS.values()):
                unknown.append(h)
        found = {k for k, rx in HEADINGS.items() if any(re.search(rx, h, re.I) for h in heads)}
        add("PASS" if {"experience", "education"} <= found else "WARN",
            "recognisable sections: %s" % (", ".join(sorted(found)) or "none"))
        if unknown:
            add("WARN", "headings an ATS may not recognise: %s (plain names like Experience, Education, Skills parse best)" % "; ".join(unknown[:5]))

    ndates = len(DATE.findall(body))
    add("PASS" if ndates >= 2 else "WARN", "dates found: %d" % ndates)
    return res


if __name__ == "__main__":
    worst = 0
    for f in sys.argv[1:]:
        print("==", f)
        for level, msg in check(f):
            print("  %-4s %s" % (level, msg))
            worst = max(worst, {"PASS": 0, "WARN": 0, "FAIL": 1}[level])
    sys.exit(worst)
