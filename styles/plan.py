"""Turn a style spec + a document kind into an app-neutral build plan, so WordCraft and ONLYOFFICE build the same thing.

    plan = make("modern", "cv", {"paper": "a4"})        # a dict; see the keys at the bottom of make()

Kinds: doc (report), resume (ATS-safe, one column), cv (European CV), paper (student paper, `fmt` apa or mla).
Options (all optional): paper "letter"|"a4"; page_numbers "bottom-center"|"bottom-right"|"top-right"; header_text str;
columns 2..3 (doc body in columns after the subtitle); photo /abs/path.png (resume/cv); layout chronological|functional|combined
(resume); fmt apa|mla (paper); local_fonts bool. All sizes are points, all colours RRGGBB.
Style property keys: font size color bold italic caps spacing align before after line indent_left indent_first keep_next
border_bottom=(color,width,space) border_left=(color,width,space) tab_right=pt.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content
from resolve import resolve

PAGES = {"letter": (612.0, 792.0), "a4": (595.3, 841.9)}


def _rule(h, color, kind):
    if h["rule"] == "bottom": return {"border_bottom": (color, 1.0, 1)}
    if h["rule"] == "left": return {"border_left": (color, 3.0, 6)}
    return {}


def make(style_name, kind, o=None):
    o = dict(o or {})
    if kind == "paper":
        style_name = "academic"
    S = resolve(style_name, portable=not o.get("local_fonts"))
    paper = o.get("paper") or ("a4" if kind == "cv" else "letter")
    PW, PH = PAGES[paper]
    HF, BF = S["font"]["heading"], S["font"]["body"]
    C, SZ, B, H, T, RS, TB = S["color"], S["size"], S["body"], S["heading"], S["title"], S["resume"], S["table"]
    notes, links, blocks, styles = [], [], [], []
    plan = {"style": style_name, "kind": kind, "paper": paper, "font": S["font"], "summary": S["summary"],
            "notes": notes, "links": links, "blocks": blocks, "styles": styles, "header": None, "footer": None,
            "bullet": {"color": C["accent"]}, "columns": None}
    m = RS["margins_in"] if kind in ("resume", "cv") else S["margins_in"]
    top, bottom, left, right = [v * 72 for v in m]
    if kind == "paper":
        top = bottom = left = right = 72.0
    plan["page"] = {"w": PW, "h": PH, "margins": [top, bottom, left, right]}
    width = PW - left - right
    plan["width"] = width

    def add(name, **p): styles.append((name, p))

    def para(style, *runs, bullet=False):
        blocks.append({"t": "p", "style": style, "bullet": bullet,
                       "runs": [(True, r[1]) if isinstance(r, tuple) else (False, r) for r in runs]})

    # ---------------------------------------------------------------- page furniture
    pn = o.get("page_numbers")
    if pn == "top-right": plan["header"] = {"text": o.get("header_text", ""), "number": True, "align": "right"}
    elif o.get("header_text"): plan["header"] = {"text": o["header_text"], "number": False, "align": "right"}
    if pn in ("bottom-center", "bottom-right"):
        plan["footer"] = {"number": True, "align": "center" if pn == "bottom-center" else "right"}

    # ---------------------------------------------------------------- doc
    if kind == "doc":
        bs = SZ["body"]
        add("Normal", font=BF, size=bs, color=C["text"], before=0, after=B["after"], align=B["align"], indent_first=B["first_indent"], line=B["line"])
        hp = dict(font=HF, size=SZ["h1"], color=C["heading"], bold=H["bold"], italic=H["italic"], caps=H["caps"], spacing=H["spacing"],
                  before=H["before"], after=H["after"], keep_next=True, align=H["align"], indent_first=0, line=1.0)
        hp.update(_rule(H, C["accent"], kind)); add("Heading 1", **hp)
        add("Heading 2", font=HF, size=SZ["h2"], color=C["heading"], bold=True, italic=H["italic"], before=max(H["before"] * 0.6, 0), after=3,
            keep_next=True, align="left", indent_first=0, line=1.0)
        tp = dict(font=HF, size=SZ["title"], color=C["heading"], bold=T["bold"], caps=T["caps"], align=T["align"], after=4, indent_first=0, line=1.0)
        if T["rule"] == "bottom": tp["border_bottom"] = (C["accent"], 1.5, 4)
        add("Doc Title", **tp)
        add("Doc Subtitle", font=BF, size=bs, color=C["muted"], align=T["align"], after=14, indent_first=0, line=1.0)
        add("Doc Quote", font=BF, size=bs, color=C["muted"], italic=True, indent_left=24, indent_first=0, before=4, after=10, align="left",
            border_left=(C["accent"], 2.5, 8))
        add("Doc Bullet", indent_first=0, after=3, align="left")
        add("Doc Table", font=BF, size=max(bs - 1, 8), color=C["text"], before=2, after=2, align="left", indent_first=0, line=1.0)
        for k, v in content.DOC:
            if k == "title": para("Doc Title", v)
            elif k == "subtitle":
                para("Doc Subtitle", v)
                if o.get("columns"): blocks.append({"t": "columns", "n": int(o["columns"])})
            elif k == "h1": para("Heading 1", v)
            elif k == "h2": para("Heading 2", v)
            elif k == "p": para("Normal", v)
            elif k == "quote": para("Doc Quote", v)
            elif k == "bullets":
                for b in v: para("Doc Bullet", b, bullet=True)
            elif k == "table":
                blocks.append({"t": "table", "rows": v, "fill": TB["header_fill"], "text": TB["header_text"], "border": TB["border"], "style": "Doc Table"})
        plan["props"] = {"title": "Style sample: " + style_name, "author": "Sample Author", "subject": S["summary"]}
        if o.get("columns"): notes.append("columns: fine for newsletters and handouts; never use them in a résumé (see styles/README.md on ATS).")

    # ---------------------------------------------------------------- resume / cv
    elif kind in ("resume", "cv"):
        R = content.CV if kind == "cv" else content.RESUME
        bs = RS["body_size"]
        add("Normal", font=BF, size=bs, color=C["text"], before=0, after=0, align="left", indent_first=0, line=1.0)
        hp = dict(font=HF, size=min(SZ["h1"], bs + 2.5), color=C["heading"], bold=H["bold"], italic=H["italic"], caps=H["caps"], spacing=H["spacing"],
                  before=8, after=3, keep_next=True, align="left", indent_first=0, line=1.0)
        hp.update(_rule(H, C["accent"], kind)); add("Heading 1", **hp)
        add("Resume Name", font=HF, size=RS["name_size"], color=C["heading"], bold=True, align=RS["name_align"], after=1, indent_first=0)
        add("Resume Headline", font=BF, size=bs + 1, color=C["muted"], bold=True, align=RS["name_align"], after=1, indent_first=0)
        add("Resume Contact", font=BF, size=bs, color=C["text"], align=RS["name_align"], after=3, indent_first=0)
        add("Resume Body", after=2, align="left", indent_first=0)
        add("Job Title", font=BF, size=bs + 0.5, color=C["text"], bold=True, before=4, keep_next=True, indent_first=0, tab_right=width)
        add("Job Org", font=BF, size=bs, color=C["muted"], italic=True, after=1.5, keep_next=True, indent_first=0)
        add("Resume Bullet", after=1, indent_first=0, align="left")
        add("Resume Line", after=1.5, indent_first=0, tab_right=width)
        add("Resume Photo", after=4, indent_first=0, align=RS["name_align"], line=1.0)
        if o.get("photo"):
            blocks.append({"t": "photo", "path": o["photo"], "w": 85.0, "h": 113.0, "style": "Resume Photo"})
            notes.append("photo: pictures are ignored by ATS and some employers (US, UK) prefer none; use only where the local norm expects one.")
        if o.get("header_text") or pn == "top-right":
            notes.append("header text: many ATS parsers skip headers and footers, so keep contact details in the body.")
        bullet = lambda b: para("Resume Bullet", b, bullet=True)
        if kind == "cv":
            para("Resume Name", R["name"]); para("Resume Headline", R["headline"]); para("Resume Contact", R["address"])
            para("Resume Contact", "  •  ".join([R["phone"], R["email"]]))
            para("Heading 1", "Profile"); para("Resume Body", R["profile"])
            para("Heading 1", "Work experience")
            for j in R["jobs"]:
                para("Job Title", f"{j['title']}\t{j['dates']}"); para("Job Org", j["org"])
                for b in j["bullets"]: bullet(b)
            para("Heading 1", "Education and training")
            for d, s, y in R["education"]:
                para("Job Title", f"{d}\t{y}"); para("Job Org", s)
            para("Heading 1", "Languages"); para("Resume Line", (True, "Mother tongue: "), R["languages"]["mother"])
            for lang, li, rd, sp, wr in R["languages"]["other"]:
                para("Resume Line", (True, lang + ": "), f"listening {li}, reading {rd}, speaking {sp}, writing {wr} (CEFR)")
            para("Heading 1", "Digital skills")
            for label, txt in R["digital"]: para("Resume Line", (True, label + ": "), txt)
            para("Heading 1", "Certificates")
            for n, i, y in R["certificates"]: para("Resume Line", (True, n), f" — {i}\t{y}")
            para("Heading 1", "Interests"); para("Resume Body", R["interests"])
            links.append([R["email"], "mailto:" + R["email"]])
            plan["props"] = {"title": R["name"] + " - Curriculum Vitae", "author": R["name"], "subject": R["headline"]}
        else:
            layout = o.get("layout", "chronological")
            X = content.RESUME_EXTRA
            para("Resume Name", R["name"]); para("Resume Headline", R["headline"])
            para("Resume Contact", "  •  ".join([R["location"], R["email"], R["profile"]]))
            para("Heading 1", "Professional Summary"); para("Resume Body", R["summary"])

            def competencies():
                para("Heading 1", "Core Competencies")
                for label, items in R["competencies"]: para("Resume Line", (True, label + ": "), " • ".join(items))

            def experience():
                para("Heading 1", "Professional Experience")
                for j in R["jobs"]:
                    para("Job Title", f"{j['title']}\t{j['dates']}"); para("Job Org", j["org"])
                    for b in j["bullets"]: bullet(b)

            if layout == "functional":
                notes.append("functional layout: skills first, short work history. Some recruiters distrust it and ATS cannot tie skills to dates; use it only to downplay gaps or a change of field.")
                para("Heading 1", "Skills and Achievements")
                for g, items in X["skill_groups"]:
                    para("Job Title", g)
                    for b in items: bullet(b)
                para("Heading 1", "Work History")
                for j in R["jobs"]: para("Resume Line", (True, j["title"]), f", {j['org'].split('  ')[0]}\t{j['dates']}")
            elif layout == "combined":
                competencies()
                para("Heading 1", "Selected Achievements")
                for b in X["highlights"]: bullet(b)
                experience()
            else:
                competencies(); experience()
            para("Heading 1", "Education")
            for d, s, y in R["education"]: para("Resume Line", (True, d), f" — {s}\t{y}")
            para("Heading 1", "Certifications")
            for n, i, y in R["certifications"]: para("Resume Line", (True, n), f" — {i}\t{y}")
            links += [[R["email"], "mailto:" + R["email"]], [R["profile"], "https://www." + R["profile"]]]
            plan["props"] = {"title": R["name"] + " - Resume", "author": R["name"], "subject": R["headline"]}

    # ---------------------------------------------------------------- paper (APA 7 / MLA 9)
    elif kind == "paper":
        fmt = o.get("fmt", "apa")
        P = content.PAPER
        cites = P["cites"][fmt]
        fill = lambda t: t.format(**cites)
        add("Normal", font=BF, size=12, color="000000", before=0, after=0, align="left", indent_first=36, line=2.0)
        add("Heading 1", font=BF, size=12, color="000000", bold=True, align="center", indent_first=0, before=0, after=0, keep_next=True, line=2.0)
        add("Heading 2", font=BF, size=12, color="000000", bold=True, align="left", indent_first=0, before=0, after=0, keep_next=True, line=2.0)
        add("Paper Title", font=BF, size=12, color="000000", bold=(fmt == "apa"), align="center", indent_first=0, before=0, after=0, line=2.0)
        add("Paper Meta", font=BF, size=12, color="000000", align="center" if fmt == "apa" else "left", indent_first=0, before=0, after=0, line=2.0)
        add("Reference", font=BF, size=12, color="000000", indent_left=36, indent_first=-36, align="left", before=0, after=0, line=2.0)
        plan["header"] = {"text": (P["surname"] + " ") if fmt == "mla" else "", "number": True, "align": "right"}
        if fmt == "apa":
            blocks.append({"t": "spacer", "pt": 96})
            para("Paper Title", P["title"])
            for k in ("author", "affiliation", "course", "instructor", "date"): para("Paper Meta", P[k])
            blocks.append({"t": "pagebreak"})
            para("Paper Title", P["title"])
            for k, v in P["body"]:
                para({"p": "Normal", "h1": "Heading 1", "h2": "Heading 2"}[k], fill(v))
            blocks.append({"t": "pagebreak"})
            para("Heading 1", "References")
            for r in P["refs"]: para("Reference", r)
        else:
            for v in (P["author"], P["instructor"], P["course"], P["date"]): para("Paper Meta", v)
            para("Paper Title", P["title"])
            for k, v in P["body"]:
                if k == "p": para("Normal", fill(v))
            blocks.append({"t": "pagebreak"})
            para("Paper Title", "Works Cited")
            for r in P["mla_refs"]: para("Reference", r)
        plan["props"] = {"title": P["title"], "author": P["author"], "subject": fmt.upper() + " student paper (sample)"}
        notes.append("paper: layout only. Check your instructor's or journal's current style guide for rules this sample does not show.")

    return plan


def parse_argv(argv):
    """-> (style, kind, out, options, flags) from a builder's sys.argv."""
    pos = [a for a in argv[1:] if not a.startswith("--")]
    opt = {}
    for a in argv[1:]:
        if a.startswith("--") and "=" in a:
            k, v = a[2:].split("=", 1); opt[k.replace("-", "_")] = v
    flags = {a[2:] for a in argv[1:] if a.startswith("--") and "=" not in a}
    o = {"paper": opt.get("paper", "").lower() or None, "page_numbers": opt.get("page_numbers"), "header_text": opt.get("header_text"),
         "columns": opt.get("columns"), "photo": opt.get("photo"), "layout": opt.get("layout", "chronological"),
         "fmt": opt.get("format", "apa"), "local_fonts": "local-fonts" in flags}
    return pos[0], pos[1], pos[2], {k: v for k, v in o.items() if v not in (None, "")}, flags
