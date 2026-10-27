"""Turn a style spec + a document kind into an app-neutral build plan, so WordCraft and ONLYOFFICE build the same thing.

    plan = make("modern", "cv", {"paper": "a4"})        # a dict; see the keys at the bottom of make()

Kinds: doc (generic styled document), report (quarterly program review: fact sheet, KPI row, status tables), resume (ATS-safe, one column), cv (European CV), paper (student paper, `fmt` apa or mla),
manuscript (standard manuscript format for publishers/agents; options title author pen surname address phone email wordcount ms_font=times|courier
ms_layout=novel|short text=/abs/file.txt),
stageplay (common US playwright layout; options as screenplay plus font=times|courier),
screenplay (spec-script layout; options title author address phone email draft text=/abs/file.txt).
Options (all optional): paper "letter"|"a4"; page_numbers "bottom-center"|"bottom-right"|"top-right"; header_text str;
columns 2..3 (doc body in columns after the subtitle); photo /abs/path.png (resume/cv); layout chronological|functional|combined
(resume); fmt apa|mla (paper); local_fonts bool. All sizes are points, all colours RRGGBB.
Style property keys: font size color bold italic caps spacing align before after line indent_left indent_first keep_next
border_bottom=(color,width,space) border_left=(color,width,space) tab_right=pt.
"""
import os, re, sys
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
    if kind in ("paper", "manuscript", "screenplay", "query", "synopsis", "stageplay"):
        style_name = "academic"
    S = resolve(style_name, portable=not o.get("local_fonts"))
    if o.get("figure") == "sample": o["figure"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sample-figure.png")
    paper = o.get("paper") or ("a4" if kind == "cv" else "letter")
    PW, PH = PAGES[paper]
    HF, BF = S["font"]["heading"], S["font"]["body"]
    C, SZ, B, H, T, RS, TB = S["color"], S["size"], S["body"], S["heading"], S["title"], S["resume"], S["table"]
    notes, links, blocks, styles = [], [], [], []
    SCRIPT_FONTS = {"arabic": "Arial", "hebrew": "Arial", "japanese": "Noto Sans CJK JP", "chinese": "Noto Sans CJK SC", "korean": "Noto Sans CJK KR"}
    SCRIPT_LANG = {"arabic": "ar-SA", "hebrew": "he-IL", "japanese": "ja-JP", "chinese": "zh-CN", "korean": "ko-KR"}
    plan = {"style": style_name, "kind": kind, "paper": paper, "font": S["font"], "summary": S["summary"],
            "notes": notes, "links": links, "blocks": blocks, "styles": styles, "header": None, "footer": None,
            "bullet": {"color": C["accent"]}, "columns": None, "footnotes": []}
    m = RS["margins_in"] if kind in ("resume", "cv") else S["margins_in"]
    top, bottom, left, right = [v * 72 for v in m]
    if kind in ("paper", "manuscript", "screenplay", "query", "synopsis", "stageplay"):
        top = bottom = left = right = 72.0
    plan["page"] = {"w": PW, "h": PH, "margins": [top, bottom, left, right]}
    width = PW - left - right
    plan["width"] = width

    def add(name, **p): styles.append((name, p))

    def para(style, *runs, bullet=False):
        blocks.append({"t": "p", "style": style, "bullet": bullet,
                       "runs": [r if isinstance(r, tuple) else (False, r) for r in runs]})   # flag: True = bold, "i" = italic

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
        add("Doc Figure", align="left", before=4, after=2, indent_first=0, line=1.0, keep_next=True)
        add("Doc Caption", font=BF, size=max(bs - 1.5, 8), color=C["muted"], italic=True, align="left", after=12, indent_first=0, line=1.0)
        add("Doc Script", indent_first=0, after=B["after"])
        fn_texts = {"seed log.": "Sign-in sheets were kept by the volunteer on duty at each session."}
        figure_w = min(300.0, width)
        for k, v in content.DOC:
            if k == "title": para("Doc Title", v)
            elif k == "subtitle":
                para("Doc Subtitle", v)
                if o.get("columns"): blocks.append({"t": "columns", "n": int(o["columns"])})
            elif k == "h1": para("Heading 1", v)
            elif k == "h2": para("Heading 2", v)
            elif k == "p":
                para("Normal", v)
                if o.get("script") and not any(b.get("script") for b in blocks):
                    name, text, rtl = content.SCRIPTS[o["script"]]
                    blocks.append({"t": "p", "style": "Doc Script", "bullet": False, "runs": [(False, text)], "script": o["script"], "rtl": rtl, "font": SCRIPT_FONTS[o["script"]], "lang": SCRIPT_LANG[o["script"]]})
                    notes.append("script: %s sample sentence (check the wording with a native reader before reusing it); other machines may substitute the font." % name)
                if o.get("footnotes") and v.rstrip().endswith("seed log."):
                    plan["footnotes"].append({"anchor": "seed log.", "text": fn_texts["seed log."]})
            elif k == "quote": para("Doc Quote", v)
            elif k == "bullets":
                for b in v: para("Doc Bullet", b, bullet=True)
            elif k == "table":
                rows = [list(r) for r in v]; merge = []
                if o.get("merged_table"):
                    rows = [["Workshop attendance, autumn 2026"] + [""] * (len(rows[0]) - 1)] + rows
                    merge = [[0, 0, 0, len(rows[0]) - 1]]
                blocks.append({"t": "table", "rows": rows, "merge": merge, "sub_fill": TB["border"], "fill": TB["header_fill"], "text": TB["header_text"], "border": TB["border"], "style": "Doc Table"})
                if o.get("figure"):
                    blocks.append({"t": "figure", "path": o["figure"], "w": figure_w, "h": figure_w * 520 / 900, "caption": "Figure 1. Workshop attendance by session (invented data).",
                                   "style": "Doc Figure", "caption_style": "Doc Caption", "alt": "Bar chart of workshop attendance by session"})
        plan["props"] = {"title": "Style sample: " + style_name, "author": "Sample Author", "subject": S["summary"]}
        if o.get("columns"): notes.append("columns: fine for newsletters and handouts; never use them in a résumé (see styles/README.md on ATS).")

    # ---------------------------------------------------------------- report (quarterly review)
    elif kind == "report":
        R = content.REPORT
        bs = SZ["body"]
        tint = lambda hx, k: "".join("%02X" % round(int(hx[i:i + 2], 16) * (1 - k) + 255 * k) for i in (0, 2, 4))
        add("Normal", font=BF, size=bs, color=C["text"], before=0, after=max(B["after"], 6), align="left", indent_first=0, line=min(B["line"], 1.2))   # a report is single-spaced even in the double-spaced academic style
        hp = dict(font=HF, size=SZ["h1"], color=C["heading"], bold=H["bold"], italic=H["italic"], caps=H["caps"], spacing=H["spacing"],
                  before=max(H["before"], 16), after=max(H["after"], 6), keep_next=True, align="left", indent_first=0, line=1.0)
        hp.update(_rule(H, C["accent"], kind)); add("Heading 1", **hp)
        add("Heading 2", font=HF, size=SZ["h2"], color=C["heading"], bold=True, italic=H["italic"], before=8, after=3, keep_next=True, align="left", indent_first=0, line=1.0)
        tp = dict(font=HF, size=SZ["title"], color=C["heading"], bold=T["bold"], caps=T["caps"], align="left", after=2, indent_first=0, line=1.0)
        if T["rule"] == "bottom": tp["border_bottom"] = (C["accent"], 1.5, 4)
        add("Doc Title", **tp)
        add("Doc Subtitle", font=HF, size=SZ["h1"], color=C["accent"], bold=False, align="left", after=12, indent_first=0, line=1.0)
        add("Doc Bullet", indent_first=0, after=3, align="left")
        add("Doc Table", font=BF, size=max(bs - 1, 8), color=C["text"], before=2, after=2, align="left", indent_first=0, line=1.0)
        add("Rpt Label", font=BF, size=max(bs - 1.5, 8), color=C["muted"], bold=True, before=2, after=2, align="left", indent_first=0, line=1.0)
        add("Rpt KPI Value", font=HF, size=22, color=C["accent"] if C["accent"] != C["muted"] else C["heading"], bold=True, before=6, after=0, align="center", indent_first=0, line=1.0)
        add("Rpt KPI Label", font=BF, size=max(bs - 1.5, 8), color=C["muted"], before=0, after=6, align="center", indent_first=0, line=1.0)
        add("Rpt Note", font=BF, size=max(bs - 2, 8), color=C["muted"], italic=True, before=10, after=0, align="left", indent_first=0, line=1.0)
        soft = tint(C["accent"], 0.88)
        TBL = dict(t="table", rich=True, text=TB["header_text"], border=TB["border"], style="Doc Table")
        RAG = {"Complete": ("C8E6C9", "1B5E20"), "On track": ("C8E6C9", "1B5E20"), "At risk": ("FFE9A8", "6B4A00"), "Delayed": ("F8C9C4", "8E1B10"),
               "High": ("F8C9C4", "8E1B10"), "Medium": ("FFE9A8", "6B4A00"), "Low": ("C8E6C9", "1B5E20")}

        def rag_cells(rows, col):
            return {"%d,%d" % (r, col): RAG[row[col]] for r, row in enumerate(rows) if r and row[col] in RAG}

        para("Doc Title", R["title"]); para("Doc Subtitle", R["subtitle"])
        # label / value pairs in two rows of two, so the table reads as a quick fact sheet
        meta = [[R["meta"][0][0], R["meta"][0][1], R["meta"][1][0], R["meta"][1][1]], [R["meta"][2][0], R["meta"][2][1], R["meta"][3][0], R["meta"][3][1]]]
        fills = {"%d,%d" % (r, c): (soft, None) for r in range(2) for c in range(4)}
        fills.update({"1,3": RAG[R["meta"][3][1]]})
        blocks.append(dict(TBL, rows=meta, header=False, grid=False, fills=fills, widths=[0.17, 0.33, 0.17, 0.33],
                           cell_styles=[["Rpt Label", "Doc Table", "Rpt Label", "Doc Table"]] * 2))
        para("Heading 1", "1. Executive summary"); para("Normal", R["summary"])
        k = R["kpis"]
        blocks.append(dict(TBL, rows=[[v for v, _ in k], [l for _, l in k]], header=False, grid=False,
                           fills={"%d,%d" % (r, c): (soft, None) for r in range(2) for c in range(len(k))},
                           cell_styles=[["Rpt KPI Value"] * len(k), ["Rpt KPI Label"] * len(k)]))
        para("Heading 1", "2. Highlights")
        for b in R["highlights"]: para("Doc Bullet", b, bullet=True)
        para("Heading 1", "3. Milestones")
        rows = R["milestones"]
        blocks.append(dict(TBL, rows=rows, header=True, grid=True, fill=TB["header_fill"], fills=rag_cells(rows, 3), widths=[0.40, 0.22, 0.14, 0.24],
                           cell_styles=[["Doc Table"] * 4] * len(rows)))
        para("Heading 1", "4. Budget")
        rows = R["budget"]
        blocks.append(dict(TBL, rows=rows, header=True, grid=True, fill=TB["header_fill"], fills={}, widths=[0.40, 0.20, 0.20, 0.20],
                           cell_styles=[["Doc Table"] * 4] * len(rows)))
        para("Heading 1", "5. Risks and issues")
        rows = R["risks"]
        blocks.append(dict(TBL, rows=rows, header=True, grid=True, fill=TB["header_fill"], fills=rag_cells(rows, 1), widths=[0.34, 0.14, 0.52],
                           cell_styles=[["Doc Table"] * 3] * len(rows)))
        para("Heading 1", "6. Next quarter")
        for b in R["next"]: para("Doc Bullet", b, bullet=True)
        para("Rpt Note", R["note"])
        if not o.get("page_numbers"): plan["footer"] = {"number": True, "align": "right"}
        if not o.get("header_text"): plan["header"] = {"text": R["title"] + "  |  " + R["subtitle"], "number": False, "align": "left"}
        plan["props"] = {"title": R["title"] + ": " + R["subtitle"], "author": "Sample Author", "subject": S["summary"]}
        notes.append("report: status cells carry the word (Complete, At risk, High...) as well as the colour, so the table still reads in greyscale or to a screen reader.")

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
            para("Resume Contact", "  •  ".join([R["location"], R["phone"], R["email"], R["profile"]]))
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
        X = content.PAPER_EXTRAS
        cites = P["cites"][fmt]
        fill = lambda t: t.format(**cites)
        add("Normal", font=BF, size=12, color="000000", before=0, after=0, align="left", indent_first=36, line=2.0)
        add("Heading 1", font=BF, size=12, color="000000", bold=True, align="center", indent_first=0, before=0, after=0, keep_next=True, line=2.0)
        add("Heading 2", font=BF, size=12, color="000000", bold=True, align="left", indent_first=0, before=0, after=0, keep_next=True, line=2.0)
        add("Paper Title", font=BF, size=12, color="000000", bold=(fmt == "apa"), align="center", indent_first=0, before=0, after=0, line=2.0)
        add("Paper Meta", font=BF, size=12, color="000000", align="center" if fmt == "apa" else "left", indent_first=0, before=0, after=0, line=2.0)
        add("Reference", font=BF, size=12, color="000000", indent_left=36, indent_first=-36, align="left", before=0, after=0, line=2.0)
        add("Paper Abstract", font=BF, size=12, color="000000", indent_first=0, align="left", before=0, after=0, line=2.0)
        add("Block Quote", font=BF, size=12, color="000000", indent_left=36, indent_first=0, align="left", before=0, after=0, line=2.0)
        add("Table Caption", font=BF, size=12, color="000000", indent_first=0, align="left", before=0, after=0, line=2.0, keep_next=True)
        add("Paper Table", font=BF, size=11, color="000000", indent_first=0, align="left", before=1, after=1, line=1.0)
        plan["header"] = {"text": (P["surname"] + " ") if fmt == "mla" else "", "number": True, "align": "right"}

        def extras_table():
            label, title = X["table_caption"]
            if fmt == "apa":
                para("Table Caption", (True, label)); para("Table Caption", ("i", title))
            else:
                para("Table Caption", f"{label}. {title}")
            blocks.append({"t": "table", "rows": X["table_rows"], "merge": [], "fill": "FFFFFF", "text": "000000", "border": "000000", "style": "Paper Table"})
        body = P["body"]
        if fmt == "apa":
            blocks.append({"t": "spacer", "pt": 96})
            para("Paper Title", P["title"])
            for k in ("author", "affiliation", "course", "instructor", "date"): para("Paper Meta", P[k])
            blocks.append({"t": "pagebreak"})
            if o.get("extras"):
                para("Heading 1", "Abstract"); para("Paper Abstract", X["abstract"]); para("Normal", ("i", "Keywords: "), X["keywords"])
                blocks.append({"t": "pagebreak"})
            para("Paper Title", P["title"])
        else:
            for v in (P["author"], P["instructor"], P["course"], P["date"]): para("Paper Meta", v)
            para("Paper Title", P["title"])
        np_ = 0
        for k, v in body:
            if fmt == "mla" and k != "p": continue
            style = {"p": "Normal", "h1": "Heading 1", "h2": "Heading 2"}[k]
            para(style, fill(v))
            if k == "p":
                np_ += 1
                if np_ == 1 and o.get("footnotes"):
                    plan["footnotes"].append({"anchor": fill(v)[-26:], "text": "Okafor surveyed 214 gardeners across six sites."})
                if np_ == 2 and o.get("extras"):
                    para("Block Quote", X["quote"])
        if o.get("extras"): extras_table()
        blocks.append({"t": "pagebreak"})
        if fmt == "apa":
            para("Heading 1", "References")
            for r in P["refs"]: para("Reference", r)
        else:
            para("Paper Title", "Works Cited")
            for r in P["mla_refs"]: para("Reference", r)
        plan["props"] = {"title": P["title"], "author": P["author"], "subject": fmt.upper() + " student paper (sample)"}
        notes.append("paper: layout only. Check your instructor's or journal's current style guide for rules this sample does not show.")
        if o.get("extras"): notes.append("extras: abstract (APA), block quote and a captioned table. The table uses a plain grid; APA tables normally use horizontal rules only, which neither app's border tools can set per side.")

    # ---------------------------------------------------------------- manuscript (standard manuscript format)
    elif kind == "manuscript":
        M = content.MANUSCRIPT
        mf = {"courier": "Courier New"}.get((o.get("ms_font") or "").lower(), "Times New Roman")
        layout = o.get("ms_layout") if o.get("ms_layout") in ("novel", "short") else "novel"
        title = o.get("title") or M["title"]
        author = o.get("author") or M["author"]
        pen = o.get("pen") or (author if o.get("author") else M["pen"])
        surname = o.get("surname") or (author.split()[-1] if o.get("author") else M["surname"])
        addr = [x.strip() for x in o["address"].split("|")] if o.get("address") else ([] if o.get("author") else M["address"])
        phone = o.get("phone") or ("" if o.get("author") else M["phone"])
        email = o.get("email") or ("" if o.get("author") else M["email"])
        txt = M["text"]
        if o.get("text"):
            txt = open(o["text"], encoding="utf-8").read()
        # parse the simple markup into (kind, runs) items
        def runs_of(line):
            out, bits = [], re.split(r"(\*[^*\n]+\*)", line)
            for b in bits:
                if len(b) > 2 and b[0] == b[-1] == "*": out.append(("i", b[1:-1]))
                elif b: out.append((False, b))
            return out
        items = []
        for chunk in re.split(r"\n\s*\n", txt.strip()):
            raw = [l.strip() for l in chunk.strip().split("\n") if l.strip()]
            if raw and all(l.startswith("| ") or l == "|" for l in raw):          # verse: one line per paragraph, line breaks kept
                items.append(("verse", [runs_of(l[2:]) for l in raw if l != "|"])); continue
            chunk = " ".join(raw)
            if not chunk: continue
            if chunk.startswith("# ") : items.append(("chapter", chunk[2:].strip()))
            elif chunk in ("#", "* * *", "***"): items.append(("scene", None))
            elif chunk.upper() in ("THE END", "END"): items.append(("end", None))
            elif chunk.startswith("> "): items.append(("quote", runs_of(chunk[2:])))      # block quotation
            else: items.append(("p", runs_of(chunk)))
        # footnotes: [^text] inside a paragraph becomes a real footnote anchored on the words just before it
        for ix, (k, v) in enumerate(items):
            if k not in ("p", "quote"): continue
            full, newruns = "", []
            for fl, t in v:
                pieces = re.split(r"(\[\^[^\]]+\])", t)
                for pc in pieces:
                    if pc.startswith("[^") and pc.endswith("]"):
                        anchor = full.rstrip()[-26:]
                        if anchor: plan["footnotes"].append({"anchor": anchor, "text": pc[2:-1]})
                    elif pc:
                        newruns.append((fl, pc)); full += pc
            items[ix] = (k, newruns)
        words = sum(len(t.split()) for k, v in items if k in ("p", "quote") for _, t in v) + sum(len(t.split()) for k, v in items if k == "verse" for ln in v for _, t in ln)
        wc = int(o["wordcount"]) if o.get("wordcount") else None
        if wc is None:
            wc = int(round(words, -3)) if words >= 10000 else int(round(words / 100.0) * 100) if words >= 1000 else int(round(words / 50.0) * 50) if words >= 100 else words
        wc_text = "about {:,} words".format(wc)
        bs = 12
        add("Normal", font=mf, size=bs, color="000000", before=0, after=0, align="left", indent_first=36, line=2.0)
        add("Heading 1", font=mf, size=bs, color="000000", bold=True, align="center", indent_first=0, before=0, after=0, keep_next=True, line=2.0)
        add("MS Body First", font=mf, size=bs, color="000000", before=0, after=0, align="left", indent_first=0, line=2.0)
        add("MS Drop", font=mf, size=bs, color="000000", before=0, after=0, align="left", indent_first=0, line=2.0)
        add("MS Block Quote", font=mf, size=bs, color="000000", before=0, after=0, align="left", indent_left=36, indent_first=0, line=2.0)
        add("MS Verse", font=mf, size=bs, color="000000", before=0, after=0, align="left", indent_left=36, indent_first=0, line=1.0)
        add("MS Scene Break", font=mf, size=bs, color="000000", before=0, after=0, align="center", indent_first=0, line=2.0)
        add("MS Contact", font=mf, size=bs, color="000000", before=0, after=0, align="left", indent_first=0, line=1.0, tab_right=468)
        add("MS Title", font=mf, size=bs, color="000000", before=0, after=0, align="center", indent_first=0, line=2.0, caps=True)
        add("MS Byline", font=mf, size=bs, color="000000", before=0, after=0, align="center", indent_first=0, line=2.0)
        add("MS End", font=mf, size=bs, color="000000", before=0, after=0, align="center", indent_first=0, line=2.0)
        short_title = " ".join(title.split()[:4]).upper()
        plan["header"] = {"text": "%s / %s / " % (surname, short_title), "number": True, "align": "right"}
        plan["different_first"] = True
        # title block
        lines = [author] + addr + ([phone] if phone else []) + ([email] if email else [])
        for i, l in enumerate(lines):
            runs = [l + ("\t" + wc_text if i == 0 else "")]
            para("MS Contact", *runs)
        blocks.append({"t": "spacer", "pt": 150 if layout == "novel" else 96})
        para("MS Title", title)
        para("MS Byline", "by " + pen)
        if layout == "novel":
            blocks.append({"t": "pagebreak"})
        first_after_break = True
        started = False

        def drop():   # about a third of the page down: six empty double-spaced lines (space-before is ignored at the top of a page by WordCraft's layout)
            for _ in range(6): para("MS Drop")
        for k, v in items:
            if k == "chapter":
                if started:
                    blocks.append({"t": "pagebreak"}); drop()
                elif layout == "novel":
                    drop()                                        # the title page already ended with a page break
                else:
                    blocks.append({"t": "spacer", "pt": 24})
                para("Heading 1", v); started = True; first_after_break = True
            elif k == "scene":
                para("MS Scene Break", "#"); first_after_break = True
            elif k == "end":
                para("MS End", "THE END")
            elif k == "quote":
                para("MS Block Quote", *v); first_after_break = True
            elif k == "verse":
                for li, ln in enumerate(v):
                    if li == 0: blocks.append({"t": "spacer", "pt": 12})
                    para("MS Verse", *ln)
                first_after_break = True; blocks.append({"t": "spacer", "pt": 12})
            else:
                if layout == "short" and not started:
                    blocks.append({"t": "spacer", "pt": 24}); started = True
                para("MS Body First" if first_after_break else "Normal", *v); first_after_break = False
        plan["props"] = {"title": title, "author": author, "subject": "Manuscript (sample)" if not o.get("text") else "Manuscript"}
        notes.append("manuscript: standard layout for submissions (%s, 12 pt, double-spaced, 1-inch margins); always follow the publisher's or agent's own guidelines first." % mf)
        notes.append("manuscript: %s counted from the body text (%d words); header and title page carry no word-count field, so update it after editing." % (wc_text, words))

    # ---------------------------------------------------------------- screenplay (standard spec-script layout)
    elif kind == "screenplay":
        SP = content.SCREENPLAY
        mf = "Courier New"
        txt = open(o["text"], encoding="utf-8").read() if o.get("text") else SP["text"]
        custom = bool(o.get("text"))
        # Fountain-style title-page keys at the top of the file (Title: Credit: Author: Draft date: Contact: ...)
        meta = {}
        KEYS = r"(Title|Credit|Authors?|Source|Draft date|Date|Revision|Contact|Copyright|Notes)"
        mt = re.match(r"((?:" + KEYS + r":[^\n]*\n(?:[ \t]+[^\n]*\n)*)+)\s*\n", txt.lstrip("\ufeff") + "\n", re.I)
        if mt:
            cur = None
            for ln in mt.group(1).split("\n"):
                km = re.match(r"^" + KEYS + r":\s*(.*)$", ln, re.I)
                if km: cur = km.group(1).lower(); meta[cur] = [km.group(2).strip()] if km.group(2).strip() else []
                elif ln.strip() and cur: meta[cur].append(ln.strip())
            txt = txt.lstrip("\ufeff")[mt.end() - 1:] if False else re.sub(r"^" + re.escape(mt.group(1)), "", txt.lstrip("\ufeff"), count=1)
        first = lambda k: (meta.get(k) or [""])[0]
        title = o.get("title") or first("title") or ("" if custom else SP["title"]) or "Untitled"
        author = o.get("author") or first("author") or first("authors") or ("" if custom else SP["author"])
        credit = first("credit") or "written by"
        contact = [x.strip() for x in o["address"].split("|")] if o.get("address") else (meta.get("contact") or ([] if custom else list(SP["contact"])))
        if o.get("phone"): contact.append(o["phone"])
        if o.get("email"): contact.append(o["email"])
        draft = o.get("draft") if o.get("draft") is not None else (first("draft date") or first("revision") or first("date") or ("" if custom else SP["draft"]))

        def runs_of(line):
            out = []
            for b in re.split(r"(\*\*[^*\n]+\*\*|\*[^*\n]+\*|_[^_\n]+_)", line):
                if b.startswith("**") and b.endswith("**") and len(b) > 4: out.append((True, b[2:-2]))
                elif len(b) > 2 and b[0] == b[-1] == "*": out.append(("i", b[1:-1]))
                elif len(b) > 2 and b[0] == b[-1] == "_": out.append(("u", b[1:-1]))
                elif b: out.append((False, b))
            return out
        SCENE = re.compile(r"^(\.[A-Za-z0-9]|INT\.|EXT\.|EST\.|INT\./EXT\.|INT/EXT|I/E)", re.I)
        TRANS = re.compile(r"^[A-Z0-9 .'()\-]+TO:$")
        ACT = re.compile(r"^(TEASER|COLD OPEN|ACT (ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN)|END OF (TEASER|COLD OPEN|ACT [A-Z]+))$")
        caps = lambda t: not re.search(r"[a-z]", t) and re.search(r"[A-Z]", t)
        items, last_speaker, action_since = [], None, False
        for chunk in re.split(r"\n\s*\n", txt.strip()):
            lines = [l.strip() for l in chunk.strip().split("\n") if l.strip()]
            if not lines: continue
            head = lines[0]
            if SCENE.match(head):
                items.append(("scene", head.lstrip(".").upper())); last_speaker = None
                if lines[1:]: items.append(("action", " ".join(lines[1:]))); action_since = True
            elif len(lines) == 1 and ACT.match(head):
                items.append(("act", head)); last_speaker = None
            elif len(lines) == 1 and head.startswith(">") and head.endswith("<"):
                items.append(("center", head.strip("><").strip())); action_since = True
            elif len(lines) == 1 and (head.startswith(">") or (caps(head) and TRANS.match(head)) or head.upper() in ("FADE OUT.", "FADE TO BLACK.", "SMASH CUT TO BLACK.")):
                items.append(("trans", head.lstrip(">").strip().upper())); last_speaker = None
            elif len(lines) > 1 and (head.startswith("@") or (caps(re.sub(r"\(.*?\)|\^", "", head)) and not head.endswith(":") and len(head) < 40)):
                dual = head.endswith("^")
                name = head.rstrip("^").lstrip("@").strip().upper()
                base = re.sub(r"\s*\(.*?\)", "", name).strip()
                if base == last_speaker and action_since and "CONT" not in name:
                    name = name + " (CONT'D)"
                sub = [("char", name)]; last_speaker = base; action_since = False
                para_buf = []
                for l in lines[1:]:
                    if l.startswith("(") and l.endswith(")"):
                        if para_buf: sub.append(("dial", " ".join(para_buf))); para_buf = []
                        sub.append(("more", l) if l.upper() == "(MORE)" else ("paren", l))
                    else: para_buf.append(l)
                if para_buf: sub.append(("dial", " ".join(para_buf)))
                if dual and items and items[-1][0] == "cue":
                    items[-1] = ("dual", [items[-1][1], sub])
                else:
                    items.append(("cue", sub))
            else:
                items.append(("action", " ".join(lines))); action_since = True
        flat = []
        for k, v in items:
            if k == "cue": flat.extend(v)
            elif k == "dual": flat.append(("dual", v))
            else: flat.append((k, v))
        items = flat
        nsc = sum(1 for k, _ in items if k == "scene")
        words = sum(len(str(v).split()) for k, v in items if k in ("action", "dial"))
        sn, bs_, us_ = bool(o.get("scene_numbers")), bool(o.get("bold_scenes")), bool(o.get("underline_scenes"))
        add("Normal", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_first=0, line_exact=12)
        sh = dict(font=mf, size=12, color="000000", before=24, after=0, align="left", indent_first=0, line_exact=12, keep_next=True)
        if bs_: sh["bold"] = True
        if us_: sh["underline"] = True
        if sn: sh.update(indent_first=-54, tab_right=432)
        add("SP Scene Heading", **sh)
        add("SP Action", font=mf, size=12, color="000000", before=12, after=0, align="left", indent_first=0, line_exact=12)
        add("SP Character", font=mf, size=12, color="000000", before=12, after=0, align="left", indent_left=158.4, indent_first=0, line_exact=12, keep_next=True)
        add("SP More", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=158.4, indent_first=0, line_exact=12)
        add("SP Parenthetical", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=115.2, indent_right=144, indent_first=0, line_exact=12, keep_next=True)
        add("SP Dialogue", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=72, indent_right=108, indent_first=0, line_exact=12)
        add("SP Transition", font=mf, size=12, color="000000", before=12, after=0, align="right", indent_first=0, line_exact=12)
        add("SP Centered", font=mf, size=12, color="000000", before=12, after=0, align="center", indent_first=0, line_exact=12)
        add("SP Act", font=mf, size=12, color="000000", before=0, after=12, align="center", indent_first=0, line_exact=12, bold=True, underline=True, caps=True, keep_next=True)
        add("SP Dual Character", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=36, indent_first=0, line_exact=12, keep_next=True)
        add("SP Dual Parenthetical", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=18, indent_right=18, indent_first=0, line_exact=12, keep_next=True)
        add("SP Dual Dialogue", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=0, indent_right=0, indent_first=0, line_exact=12)
        add("SP Title", font=mf, size=12, color="000000", before=0, after=0, align="center", indent_first=0, line_exact=12, caps=True)
        add("SP Title Page", font=mf, size=12, color="000000", before=0, after=0, align="center", indent_first=0, line_exact=12)
        add("SP Contact", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_first=0, line_exact=12)
        # title page (its own section: not counted; the script starts again at page 1, which prints no number)
        blocks.append({"t": "spacer", "pt": 216})
        para("SP Title", title)
        if author:
            blocks.append({"t": "spacer", "pt": 24}); para("SP Title Page", credit)
            blocks.append({"t": "spacer", "pt": 12}); para("SP Title Page", author)
        if draft:
            blocks.append({"t": "spacer", "pt": 24}); para("SP Title Page", draft)
        for i, l in enumerate(contact):
            if i == 0: blocks.append({"t": "spacer", "pt": 168 if draft else 200})
            para("SP Contact", l)
        blocks.append({"t": "sectionbreak"})
        STYLE = {"scene": "SP Scene Heading", "action": "SP Action", "char": "SP Character", "paren": "SP Parenthetical", "dial": "SP Dialogue",
                 "trans": "SP Transition", "center": "SP Centered", "act": "SP Act", "more": "SP More"}
        DSTYLE = {"char": "SP Dual Character", "paren": "SP Dual Parenthetical", "dial": "SP Dual Dialogue", "more": "SP Dual Parenthetical"}
        scene_no, first_item = 0, True
        for k, v in items:
            if k == "dual":
                cols = [[(DSTYLE[kk], runs_of(vv) if kk == "dial" else [(False, vv)]) for kk, vv in col] for col in v]
                blocks.append({"t": "dual", "cols": cols, "spacer": 12}); first_item = False; continue
            if k == "act" and not first_item and not v.startswith("END OF"):
                blocks.append({"t": "pagebreak"})
            if k == "scene":
                scene_no += 1
                text = "%d\t%s\t%d" % (scene_no, v, scene_no) if sn else v
                para(STYLE[k], (False, text))
            else:
                runs = runs_of(v) if k in ("action", "dial", "center") else [(False, v)]
                para(STYLE[k], *runs)
            first_item = False
        plan["header"] = {"text": "", "number": True, "align": "right", "suffix": "."}
        plan["script_header"] = True
        plan["sp"] = {"items": items, "title": title, "author": author, "credit": credit, "draft": draft, "contact": contact}
        plan["props"] = {"title": title, "author": author, "subject": "Screenplay" if custom else "Screenplay (sample)"}
        plan["page"]["margins"] = [72.0, 72.0, 108.0, 72.0]
        notes.append("screenplay: standard spec-script layout (Courier New 12 pt, 12 pt line pitch, left margin 1.5 in); about one page per minute of screen time. Follow a producer's or contest's own rules first.")
        notes.append("screenplay: %d scene(s), %d words of action and dialogue; (CONT'D) is added when a speaker resumes after action." % (nsc, words))

    # ---------------------------------------------------------------- query letter and synopsis (companions of a manuscript submission)
    elif kind in ("query", "synopsis"):
        M = content.MANUSCRIPT
        mf = {"courier": "Courier New"}.get((o.get("ms_font") or "").lower(), "Times New Roman")
        custom = bool(o.get("author"))
        title = o.get("title") or M["title"]
        author = o.get("author") or M["author"]
        surname = o.get("surname") or (author.split()[-1] if custom else M["surname"])
        addr = [x.strip() for x in o["address"].split("|")] if o.get("address") else ([] if custom else M["address"])
        phone = o.get("phone") or ("" if custom else M["phone"]); email = o.get("email") or ("" if custom else M["email"])
        agent = [x.strip() for x in o["agent"].split("|")] if o.get("agent") else ([] if custom else content.QUERY["agent"])
        date = o.get("date") or ("" if custom else content.QUERY["date"])
        Q = content.QUERY if kind == "query" else content.SYNOPSIS
        txt = open(o["text"], encoding="utf-8").read() if o.get("text") else Q["text"]

        def runs_of(line):
            out = []
            for b in re.split(r"(\*[^*\n]+\*)", line):
                if len(b) > 2 and b[0] == b[-1] == "*": out.append(("i", b[1:-1]))
                elif b: out.append((False, b))
            return out
        add("Normal", font=mf, size=12, color="000000", before=0, after=12, align="left", indent_first=0, line=1.0)
        add("MS Contact", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_first=0, line=1.0)
        add("MS Heading", font=mf, size=12, color="000000", before=0, after=12, align="center", indent_first=0, line=1.0, bold=True, caps=True)
        contact = [author] + addr + ([phone] if phone else []) + ([email] if email else [])
        for l in contact: para("MS Contact", l)
        if kind == "query":
            if date: blocks.append({"t": "spacer", "pt": 14}); para("MS Contact", date)
            if agent:
                blocks.append({"t": "spacer", "pt": 14})
                for l in agent: para("MS Contact", l)
            blocks.append({"t": "spacer", "pt": 14})
            for chunk in re.split(r"\n\s*\n", txt.strip()):
                chunk = " ".join(l.strip() for l in chunk.strip().split("\n"))
                if chunk: para("Normal", *runs_of(chunk))
            para("Normal", "Sincerely,")
            para("MS Contact", author)
            plan["props"] = {"title": "Query letter: " + title, "author": author, "subject": "Query letter (sample)" if not o.get("text") else "Query letter"}
            notes.append("query: one-page business letter (single-spaced, 12 pt). Keep it to about 300-350 words; every agent states their own query rules, follow those.")
        else:
            blocks.append({"t": "spacer", "pt": 24}); para("MS Heading", title + ": Synopsis")
            for chunk in re.split(r"\n\s*\n", txt.strip()):
                chunk = " ".join(l.strip() for l in chunk.strip().split("\n"))
                if chunk: para("Normal", *runs_of(chunk))
            short_title = " ".join(title.split()[:4]).upper()
            plan["header"] = {"text": "%s / %s / Synopsis / " % (surname, short_title), "number": True, "align": "right"}
            plan["different_first"] = True
            plan["props"] = {"title": title + ": Synopsis", "author": author, "subject": "Synopsis (sample)" if not o.get("text") else "Synopsis"}
            notes.append("synopsis: single-spaced, present tense, third person; one to two pages is the usual ask. Follow the agent's or publisher's stated length.")

    # ---------------------------------------------------------------- stage play (common US playwright submission layout)
    elif kind == "stageplay":
        ST = content.STAGEPLAY
        mf = {"courier": "Courier New"}.get((o.get("ms_font") or "").lower(), "Times New Roman")
        txt = open(o["text"], encoding="utf-8").read() if o.get("text") else ST["text"]
        custom = bool(o.get("text"))
        meta = {}
        KEYS = r"(Title|Credit|Authors?|Source|Draft date|Date|Revision|Contact|Copyright|Notes)"
        mt = re.match(r"((?:" + KEYS + r":[^\n]*\n(?:[ \t]+[^\n]*\n)*)+)\s*\n", txt.lstrip("﻿") + "\n", re.I)
        if mt:
            cur = None
            for ln in mt.group(1).split("\n"):
                km = re.match(r"^" + KEYS + r":\s*(.*)$", ln, re.I)
                if km: cur = km.group(1).lower(); meta[cur] = [km.group(2).strip()] if km.group(2).strip() else []
                elif ln.strip() and cur: meta[cur].append(ln.strip())
            txt = re.sub(r"^" + re.escape(mt.group(1)), "", txt.lstrip("﻿"), count=1)
        first = lambda k: (meta.get(k) or [""])[0]
        title = o.get("title") or first("title") or ("" if custom else ST["title"]) or "Untitled"
        author = o.get("author") or first("author") or first("authors") or ("" if custom else ST["author"])
        credit = first("credit") or ("" if custom else ST["credit"])
        contact = [x.strip() for x in o["address"].split("|")] if o.get("address") else (meta.get("contact") or ([] if custom else list(ST["contact"])))
        if o.get("phone"): contact.append(o["phone"])
        if o.get("email"): contact.append(o["email"])
        draft = o.get("draft") if o.get("draft") is not None else (first("draft date") or first("revision") or first("date") or ("" if custom else ST["draft"]))

        def runs_of(line):
            out = []
            for b in re.split(r"(\*\*[^*\n]+\*\*|\*[^*\n]+\*)", line):
                if b.startswith("**") and b.endswith("**") and len(b) > 4: out.append((True, b[2:-2]))
                elif len(b) > 2 and b[0] == b[-1] == "*": out.append(("i", b[1:-1]))
                elif b: out.append((False, b))
            return out
        caps = lambda t: not re.search(r"[a-z]", t) and re.search(r"[A-Z]", t)
        CASTH = re.compile(r"^(CAST OF CHARACTERS|CHARACTERS|DRAMATIS PERSONAE|THE CAST)$", re.I)
        items, n_acts, n_scenes = [], 0, 0
        for chunk in re.split(r"\n\s*\n", txt.strip()):
            lines = [l.strip() for l in chunk.strip().split("\n") if l.strip()]
            if not lines: continue
            head = lines[0]
            if CASTH.match(head):
                items.append(("casthead", head.upper()))
                for l in lines[1:]: items.append(("cast", l))
            elif re.match(r"^(SETTING|TIME|PLACE|AT RISE)\s*:", head, re.I):
                for l in lines: items.append(("setting", l))
            elif len(lines) == 1 and re.match(r"^ACT\b", head, re.I):
                items.append(("act", head.upper())); n_acts += 1
            elif len(lines) == 1 and re.match(r"^SCENE\b", head, re.I):
                items.append(("scene", head.upper())); n_scenes += 1
            elif len(lines) == 1 and head.upper().rstrip(".") in ("BLACKOUT", "CURTAIN", "END OF PLAY", "END OF ACT ONE", "END OF ACT TWO", "LIGHTS DOWN", "END"):
                items.append(("end", head.upper()))
            elif head.startswith("(") and lines[-1].endswith(")"):
                items.append(("dir", " ".join(lines)))
            elif len(lines) > 1 and caps(re.sub(r"\(.*?\)", "", head)) and not head.endswith(":") and len(head) < 40:
                items.append(("cue", head.lstrip("@").upper()))
                buf = []
                for l in lines[1:]:
                    if l.startswith("(") and l.endswith(")"):
                        if buf: items.append(("speech", " ".join(buf))); buf = []
                        items.append(("paren", l))
                    else: buf.append(l)
                if buf: items.append(("speech", " ".join(buf)))
            else:
                items.append(("dir", " ".join(lines)))
        words = sum(len(v.split()) for k, v in items if k in ("speech", "dir"))
        nspeech = sum(1 for k, _ in items if k == "cue")
        add("Normal", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_first=0, line=1.0)
        add("ST Act", font=mf, size=12, color="000000", before=0, after=12, align="center", indent_first=0, line=1.0, bold=True, caps=True, keep_next=True)
        add("ST Scene", font=mf, size=12, color="000000", before=12, after=12, align="center", indent_first=0, line=1.0, bold=True, caps=True, keep_next=True)
        add("ST Direction", font=mf, size=12, color="000000", before=12, after=0, align="left", indent_left=72, indent_right=36, indent_first=0, line=1.0, italic=True)
        add("ST Cue", font=mf, size=12, color="000000", before=12, after=0, align="center", indent_first=0, line=1.0, caps=True, keep_next=True)
        add("ST Speech", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=0, indent_right=0, indent_first=0, line=1.0)
        add("ST Parenthetical", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_left=72, indent_right=72, indent_first=0, line=1.0, italic=True, keep_next=True)
        add("ST Cast Heading", font=mf, size=12, color="000000", before=0, after=12, align="center", indent_first=0, line=1.0, bold=True, caps=True)
        add("ST Cast", font=mf, size=12, color="000000", before=0, after=6, align="left", indent_left=36, indent_first=-36, line=1.0)
        add("ST Setting", font=mf, size=12, color="000000", before=12, after=0, align="left", indent_left=0, indent_first=0, line=1.0)
        add("ST End", font=mf, size=12, color="000000", before=12, after=0, align="center", indent_first=0, line=1.0, bold=True, caps=True)
        add("ST Title", font=mf, size=12, color="000000", before=0, after=0, align="center", indent_first=0, line=1.0, bold=True, caps=True)
        add("ST Title Page", font=mf, size=12, color="000000", before=0, after=0, align="center", indent_first=0, line=1.0)
        add("ST Contact", font=mf, size=12, color="000000", before=0, after=0, align="left", indent_first=0, line=1.0)
        blocks.append({"t": "spacer", "pt": 200})
        para("ST Title", title)
        if credit: blocks.append({"t": "spacer", "pt": 14}); para("ST Title Page", credit)
        if author:
            blocks.append({"t": "spacer", "pt": 14}); para("ST Title Page", "by")
            blocks.append({"t": "spacer", "pt": 14}); para("ST Title Page", author)
        if draft: blocks.append({"t": "spacer", "pt": 28}); para("ST Title Page", draft)
        for i, l in enumerate(contact):
            if i == 0: blocks.append({"t": "spacer", "pt": 150 if draft else 190})
            para("ST Contact", l)
        blocks.append({"t": "sectionbreak"})     # title page = its own section; the rest is numbered from 1 (first page unnumbered)
        STYLE = {"casthead": "ST Cast Heading", "setting": "ST Setting", "act": "ST Act", "scene": "ST Scene", "dir": "ST Direction", "cue": "ST Cue",
                 "speech": "ST Speech", "paren": "ST Parenthetical", "end": "ST End"}
        prev = None
        for k, v in items:
            if k == "act" and prev is not None:
                blocks.append({"t": "pagebreak"})      # every act starts a new page (the cast page, if any, comes first)
            if k == "cast":
                bits = v.split(",", 1)
                runs = [(True, bits[0].strip())] + ([(False, "," + bits[1])] if len(bits) > 1 else [])
                para("ST Cast", *runs)
            elif k == "setting":
                m = re.match(r"^([A-Za-z ]+:)\s*(.*)$", v)
                para("ST Setting", *( [(True, m.group(1)), (False, " " + m.group(2))] if m else [(False, v)] ))
            elif k in ("dir", "speech"):
                para(STYLE[k], *runs_of(v))
            else:
                para(STYLE[k], (False, v))
            prev = k
        plan["header"] = {"text": "%s / " % " ".join(title.upper().split()[:4]), "number": True, "align": "right", "suffix": ""}
        plan["script_header"] = True
        plan["props"] = {"title": title, "author": author, "subject": "Stage play" if custom else "Stage play (sample)"}
        notes.append("stage play: common US playwright submission layout (%s 12 pt, 1-inch margins, single-spaced, centred cues, italic stage directions); theatres and publishers (Samuel French, Dramatists Play Service, contests) set their own rules, follow theirs first." % mf)
        notes.append("stage play: %d act(s), %d scene(s), %d speech(es), %d words of speech and direction." % (n_acts, n_scenes, nspeech, words))

    return plan


def parse_argv(argv):
    """-> (style, kind, out, options, flags) from a builder's sys.argv."""
    pos = [a for a in argv[1:] if not a.startswith("--")]
    opt = {}
    for a in argv[1:]:
        if a.startswith("--") and "=" in a:
            k, v = a[2:].split("=", 1); opt[k.replace("-", "_")] = v
    flags = {a[2:] for a in argv[1:] if a.startswith("--") and "=" not in a}
    o = {"figure": opt.get("figure"), "script": opt.get("script"), "footnotes": "footnotes" in flags, "merged_table": "merged-table" in flags, "extras": "extras" in flags,
         "paper": opt.get("paper", "").lower() or None, "page_numbers": opt.get("page_numbers"), "header_text": opt.get("header_text"),
         "columns": opt.get("columns"), "photo": opt.get("photo"), "layout": opt.get("layout", "chronological"),
         "fmt": opt.get("format", "apa"), "local_fonts": "local-fonts" in flags,
         "title": opt.get("title"), "author": opt.get("author"), "pen": opt.get("pen"), "surname": opt.get("surname"), "address": opt.get("address"),
         "phone": opt.get("phone"), "email": opt.get("email"), "wordcount": opt.get("wordcount"), "ms_font": opt.get("font"),
         "ms_layout": opt.get("layout") if opt.get("layout") in ("novel", "short") else None, "text": opt.get("text"), "draft": opt.get("draft"),
         "agent": opt.get("agent"), "date": opt.get("date"), "scene_numbers": "scene-numbers" in flags, "bold_scenes": "bold-scenes" in flags, "underline_scenes": "underline-scenes" in flags}
    return pos[0], pos[1], pos[2], {k: v for k, v in o.items() if v not in (None, "", False)}, flags
