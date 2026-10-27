"""Redesigned, human-first résumés built from tables, shaded cells, tracked headings, skill bars and timelines (WordCraft).

    python3 -I resume_designs.py DESIGN /abs/out.docx [--a4] [--no-photo] [--local-fonts] [--overwrite] > job.json
    wordcraft-cli run --script job.json            # writes out.docx and out.pdf next to it

    python3 -I resume_designs.py --list            # the designs

DESIGN is  <style>-<a|b>  (e.g. elegant-a, stylish-b): nine styles (traditional, elegant, clean, professional, academic, modern,
stylish, creative, minimal) x two layouts, modelled on the *vibe* of reference résumés (colour, type, structure), never their text or branding.
These layouts are for humans first: columns, sidebars, shaded blocks, icons and photo placeholders do NOT read well in an ATS. Use the
single-column `resume` kind in build_wordcraft.py when a parser reads the file. Sample content is invented (resume_data.py).
"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolve import installed
from resume_data import DATA, for_design

LETTER = (612.0, 792.0)
A4 = (595.3, 841.9)


class Doc:
    """A recorder of WordCraft commands with a small layout vocabulary (styles, paragraphs, tables)."""

    def __init__(self, local_fonts=False, page=LETTER, photo=True):
        self.cmds, self.have, self.local = [], installed(), local_fonts
        self.PW, self.PH, self.photo = page[0], page[1], photo
        if page == A4: self.c("layout.size", name="A4")
        self.fresh, self.page, self.made = True, page, set()
        self.padl = self.padr = self.top = 0.0      # per-column padding: table.cellMargins is ROW-wide in WordCraft, so columns are inset with paragraph indents
        self.sty = {}
        self.prev = None                           # style name of the paragraph the caret is in (for bridging a left border across spaceBefore)
        self.c("tools.autocorrect", enabled=False)
        self.c("styles.modify", style="Normal", chr={"size": 1, "sizeCs": 1}, para={"spaceBefore": 0, "spaceAfter": 0, "lineSpacing": {"rule": "exactly", "value": 1}})
        self.npara, self.in_cell = 0, 0

    # ---- plumbing
    def c(self, cmd, **p): self.cmds.append({"command": cmd, "params": p} if p else {"command": cmd})

    def font(self, *stack):
        portable = {"Calibri", "Cambria", "Candara", "Century Gothic", "Consolas", "Constantia", "Corbel", "Georgia", "Arial", "Times New Roman", "Trebuchet MS", "Verdana", "Tahoma"}
        for f in stack:
            if f in self.have and (self.local or f in portable): return f
        for f in stack:
            if f in self.have: return f
        return stack[-1]

    def style(self, name, font="Calibri", size=10, color="000000", bold=False, italic=False, caps=False, spacing=0, before=0, after=0,
              align=None, line=None, left=0, first=0, right=0, tab=None, bottom=None, top=None, leftb=None, keep=False, smallcaps=False):
        chr_ = {"font": font, "fontCs": font, "size": size, "sizeCs": size, "color": color.lstrip("#")}
        if bold: chr_["bold"] = True
        if italic: chr_["italic"] = True
        if caps: chr_["caps"] = True
        if smallcaps: chr_["smallCaps"] = True
        if spacing: chr_["spacing"] = spacing
        par = {"spaceBefore": before, "spaceAfter": after, "indentLeft": left, "indentFirst": first, "indentRight": right}
        if align: par["align"] = align
        par["lineSpacing"] = {"rule": "multiple", "value": line} if isinstance(line, float) or line is None else {"rule": "exactly", "value": line}
        if line is None: par["lineSpacing"] = {"rule": "multiple", "value": 1.0}
        if tab: par["tabs"] = [{"pos": tab, "align": "right", "leader": "none"}]
        if keep: par["keepNext"] = True
        b = {}
        for k, v in (("bottom", bottom), ("top", top), ("left", leftb)):
            if v: col, w, sp = v; b[k] = {"style": "single", "width": w, "color": col.lstrip("#"), "space": sp}
        if b: par["borders"] = b
        self.sty[name] = (left, first, right, before, after, bool(leftb))
        if name not in self.made:
            self.c("styles.create", name=name, basedOn="Normal"); self.made.add(name)
        self.c("styles.modify", style=name, chr=chr_, para=par)
        return name

    def vline_style(self, name, color="A9A9A9", width=0.75):
        """A table style whose only border is the vertical line BETWEEN columns: one continuous hairline through every row (paragraph borders break at row gaps)."""
        if name not in self.made:
            self.c("table.newStyle", name=name, basedOn="Normal Table", wholeTable={"borders": {"edges": "insideV", "style": "single", "width": width, "color": color.lstrip("#")}})
            self.made.add(name)
        return name

    def page_setup(self, top, bottom, left, right):
        self.c("layout.margins", top=top, bottom=bottom, left=left, right=right)

    # ---- text
    def P(self, style, *runs, shade=None):
        """One paragraph. runs: str, or (str, {props}) with props bold/italic/color/size/font/caps/spacing/underline."""
        bridge = False
        if not self.fresh:
            pv, nw = self.sty.get(self.prev), self.sty.get(style)
            if pv and nw and pv[5] and nw[5] and nw[3] > 0:      # a left border is not drawn across spaceBefore (it is across spaceAfter): move it
                self.c("para.set", props={"spaceAfter": pv[4] + nw[3]}); bridge = True
            self.c("text.newParagraph")
        self.fresh = False
        self.prev = style
        if not self.in_cell: self.npara += 1
        self.c("para.reset")                      # a new paragraph inherits the last one's direct formatting (align, indents, spacing)
        self.c("para.style", style=style)
        self.c("format.resetChar")                # ...and its character formatting (a bold run leaked into the next paragraph)
        if self.padl or self.padr or self.top or bridge:
            l, f, r = self.sty.get(style, (0, 0, 0))[:3]
            props = {"indentLeft": l + self.padl, "indentFirst": f, "indentRight": r + self.padr}
            if self.top: props["spaceBefore"] = self.top; self.top = 0.0
            elif bridge: props["spaceBefore"] = 0
            self.c("para.set", props=props)
        if shade: self.c("para.shading", color=shade)
        for r in runs:
            text, props = (r, None) if isinstance(r, str) else r
            if props:
                pr = {k: (v.lstrip("#") if k == "color" else v) for k, v in props.items()}
                if "font" in pr: pr["fontCs"] = pr["font"]
                if "size" in pr: pr["sizeCs"] = pr["size"]
                self.c("format.set", props=pr)
            self.c("text.insert", text=text)
            if props: self.c("format.resetChar")

    def picture(self, path, width, align="left", before=0, after=0, style="Photo"):
        if not self.photo: return                                   # photo-free variant
        self.style("Photo", "Calibri", 10, "000000", line=1.0)     # Normal is 1 pt high (see __init__): a picture paragraph needs real line height
        if not self.fresh: self.c("text.newParagraph")
        self.fresh = False
        if not self.in_cell: self.npara += 1
        self.c("para.style", style=style)
        self.c("para.set", props={"align": align, "spaceBefore": before + self.top, "spaceAfter": after, "indentLeft": self.padl, "indentRight": self.padr})
        self.top = 0.0
        self.c("insert.picture", path=path, width=width, alt="Photo placeholder")
        self.prev = None

    # ---- tables
    def table(self, widths, rows, fills=None, heights=None, margins=None, valign=None):
        """rows: list of rows; each row a list of callables (called with the caret in that cell). fills/margins/valign: same shape or None.
        heights: per row (pt, exact) or None. widths: column widths (pt)."""
        nr, nc = len(rows), len(widths)
        self.c("insert.table", rows=nr, cols=nc, style="Normal Table")
        for r, row in enumerate(rows):
            if heights and heights[r]: self.c("table.rowHeight", height=heights[r], rule="exact")
            for ci, fn in enumerate(row):
                fill = fills[r][ci] if fills else None
                if fill: self.c("table.selectCell"); self.c("table.shading", color=fill.lstrip("#")); self.c("select.collapse")
                if r == 0: self.c("table.columnWidth", width=widths[ci])
                m = (margins[r][ci] if margins else None) or (0, 0, 0, 0)
                self.c("table.cellMargins", top=m[0], left=m[1], bottom=m[2], right=m[3])
                if valign and valign[r][ci]: self.c("table.cellAlign", value=valign[r][ci])
                self.fresh = True
                if fn: fn()
                self.c("caret.right")
        self.fresh = False
        # caret.right at the very last cell leaves the table: we are in the paragraph after it (end of document)

    def script(self, out):
        return {"template": "blank", "commands": self.cmds, "save": [out, out.rsplit(".", 1)[0] + ".pdf"]}


# ---------------------------------------------------------------------------------------------------- shared helpers
def avatar(path, bg="D9DEE5", fg="8895A7", size=480):
    """A neutral head-and-shoulders silhouette on a coloured disc (a stand-in for a photo; never a real face)."""
    from PIL import Image, ImageDraw
    S = size * 2
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, S - 1, S - 1), fill="#" + bg)
    layer = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.ellipse((S * 0.34, S * 0.2, S * 0.66, S * 0.56), fill="#" + fg)           # head
    ld.ellipse((S * 0.16, S * 0.6, S * 0.84, S * 1.35), fill="#" + fg)           # shoulders
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, S - 1, S - 1), fill=255)
    im.paste(layer, (0, 0), Image.composite(layer.split()[3], Image.new("L", (S, S), 0), mask))
    im.resize((size, size), Image.LANCZOS).save(path)
    return path


def bar(doc, width, pct, fill, track, thick=4):
    """A skill bar (nested 1x2 table) in the current cell; leaves the caret in the empty paragraph after it."""
    if not doc.fresh: doc.c("text.newParagraph")
    w1 = max(6.0, width * pct / 100.0); w2 = max(6.0, width - w1)      # WordCraft clamps a column to >= 6 pt
    doc.c("insert.table", rows=1, cols=2, style="Normal Table")
    doc.c("table.autofit", mode="fixed")
    if doc.padl: doc.c("table.properties", indent=doc.padl)
    doc.c("table.rowHeight", height=thick, rule="exact")
    doc.c("table.selectCell"); doc.c("table.shading", color=fill.lstrip("#")); doc.c("select.collapse")
    doc.c("table.columnWidth", width=round(w1, 1)); doc.c("table.cellMargins", top=0, left=0, bottom=0, right=0)
    doc.c("caret.right")
    doc.c("table.selectCell"); doc.c("table.shading", color=track.lstrip("#")); doc.c("select.collapse")
    doc.c("table.columnWidth", width=round(w2, 1)); doc.c("table.cellMargins", top=0, left=0, bottom=0, right=0)
    doc.c("caret.right")
    doc.fresh = True; doc.prev = None


def grid(doc, widths, rows, pre=None, style="Normal Table"):
    """A general table. widths: column widths (pt, each >= 6). rows: list of dict(h=pt|None, rule="exact"|"atLeast", m=(t,l,b,r) row-wide cell
    margins, cells=[cell, ...]) where cell = dict(span=1, fill=RRGGBB|None, v="top"|"center"|"bottom", pad=(top,left,right), fn=callable|None).
    A spanning cell takes the sum of its columns. `pad` insets one column with paragraph indents (cellMargins is ROW-wide here).
    Without merged cells the table is filled in one pass (works anywhere in the flow); with merges the caret must find the first cell
    again, which needs `pre` = the paragraphs before the table (default: counted automatically). The caret ends after the table."""
    n = len(widths)
    spans = any(c.get("span", 1) > 1 for r in rows for c in r["cells"])
    pre = doc.npara if pre is None else pre
    doc.c("insert.table", rows=len(rows), cols=n, style=style)
    doc.c("table.autofit", mode="fixed")                  # without this a narrow column is widened and squeezes its neighbours

    def home():
        doc.c("caret.docStart")
        for _ in range(pre): doc.c("caret.paraDown")

    if spans:
        for i in range(n):
            doc.c("table.columnWidth", width=widths[i])
            if i < n - 1: doc.c("caret.right")
        home()
        for r in rows:                                   # merges
            for cell in r["cells"]:
                sp = cell.get("span", 1)
                if sp > 1:
                    doc.c("table.selectCell")
                    for _ in range(sp - 1): doc.c("caret.right", extend=True)
                    doc.c("table.merge"); doc.c("select.collapse")
                doc.c("caret.right")
        home()
    for ri, r in enumerate(rows):                        # formats and content
        first_cell, col = True, 0
        for cell in r["cells"]:
            sp = cell.get("span", 1)
            if first_cell and r.get("h"):
                doc.c("table.rowHeight", height=r["h"], rule=r.get("rule", "exact"))
            if not spans and ri == 0: doc.c("table.columnWidth", width=widths[col])
            if cell.get("fill"):
                doc.c("table.selectCell"); doc.c("table.shading", color=cell["fill"].lstrip("#")); doc.c("select.collapse")
            if first_cell:
                t, l, b, rr = r.get("m", (0, 0, 0, 0))            # cellMargins is row-wide: the last call wins, so call it once per row
                doc.c("table.cellMargins", top=t, left=l, bottom=b, right=rr)
                first_cell = False
            if cell.get("v"): doc.c("table.cellAlign", value=cell["v"])
            doc.fresh = True; doc.prev = None
            pt, pl, pr = cell.get("pad", (0, 0, 0))
            doc.top, doc.padl, doc.padr = float(pt), float(pl), float(pr)
            doc.in_cell += 1
            if cell.get("fn"): cell["fn"]()
            doc.in_cell -= 1
            doc.top = doc.padl = doc.padr = 0.0
            col += sp
            doc.c("caret.right")
    doc.fresh = True        # after the table the caret sits in an empty paragraph: the next P() must reuse it, not add another


def contact_lines(d):
    return [("Phone", d["phone"]), ("Email", d["email"]), ("Location", d["location"]), ("Web", d["web"])]


def entry(doc, S, job, width, dates_right=True, blurb=True, bullet_char="•"):
    """Job entry: title + right-aligned dates, org line, optional blurb, bullets."""
    if dates_right:
        doc.P(S["job"], job["title"], ("\t", None), (job["dates"], {"font": S["datefont"], "bold": False, "size": S["datesize"], "color": S["datecolor"]}))
    else:
        doc.P(S["job"], job["title"])
    doc.P(S["org"], job["org"] + (",  " + job["place"] if job.get("place") else ""))
    if blurb and job.get("blurb"): doc.P(S["blurb"], job["blurb"])
    for b in job["bullets"]:
        doc.P(S["bul"], (bullet_char, {"color": S["bulcolor"]}), ("\t", None), b)


# ---------------------------------------------------------------------------------------------------- designs
DESIGNS = {}
PHOTO_DESIGNS = {"elegant-a", "elegant-b", "clean-b", "modern-a", "stylish-a", "stylish-b", "creative-a", "creative-b"}   # show an avatar placeholder unless --no-photo


def design(name):
    def deco(fn): DESIGNS[name] = fn; return fn
    return deco


@design("elegant-a")
def elegant_a(doc, D, out_dir):
    """Navy banner with a gold, widely tracked name; sidebar (avatar, contact, languages as gold bars) + hairline + main column."""
    NAVY, GOLD, INK, GREY, RULE = "2F3E5B", "C2A25C", "222222", "6B6B6B", "BFBFBF"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Calibri", "Corbel", "Arial")
    W, SIDE = doc.PW, 196.0; MAIN = W - SIDE
    doc.page_setup(0, 0, 0, 0)
    S = {}
    S["name"] = doc.style("EL Name", HF, 25, GOLD, spacing=4, align="center", after=3)
    S["ttl"] = doc.style("EL Title", HF, 9, "FFFFFF", spacing=3.2, align="center", caps=True)
    S["sh"] = doc.style("EL SideHead", HF, 10, INK, spacing=2.2, caps=True, before=14, after=5, bottom=(RULE, 0.5, 3))
    S["st"] = doc.style("EL SideText", BF, 8.5, INK, after=3)
    S["sl"] = doc.style("EL SideLabel", BF, 8.5, INK, after=1, before=3)
    S["h"] = doc.style("EL Head", HF, 10.5, INK, spacing=2.4, caps=True, before=14, after=6, bottom=(RULE, 0.5, 3))
    S["job"] = doc.style("EL Job", BF, 9.5, INK, bold=True, caps=True, before=7, after=0, tab=MAIN - 62)
    S["org"] = doc.style("EL Org", BF, 8.8, GREY, after=3)
    S["blurb"] = doc.style("EL Blurb", BF, 8.8, GREY, italic=True, after=2)
    S["bul"] = doc.style("EL Bullet", BF, 9, INK, after=3, left=11, first=-11, line=1.08)
    S["t"] = doc.style("EL Text", BF, 9, INK, after=4, line=1.1)
    S.update(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=INK)
    av = avatar(os.path.join(out_dir, "avatar-elegant.png"), "D9DEE5", "7A879A")

    def banner():
        doc.P(S["name"], D["name"].upper()); doc.P(S["ttl"], D["title"])

    def side():
        doc.picture(av, 112, align="center", before=18, after=6)
        doc.P(S["sh"], "Contact")
        for lab, val in contact_lines(D)[:3]: doc.P(S["st"], val)
        doc.P(S["sh"], "Links")
        for lab, val in D["links"]: doc.P(S["sl"], (lab, {"bold": True})); doc.P(S["st"], val)
        doc.P(S["sh"], "Languages")
        for lang, pct, lvl in D["languages"]:
            doc.P(S["sl"], lang); bar(doc, SIDE - 56, pct, GOLD, "D4D4D4")
        doc.P(S["sh"], "Interests"); doc.P(S["st"], ", ".join(D["interests"]))

    def main():
        doc.P(S["h"], "About me"); doc.P(S["t"], D["summary"])
        doc.P(S["h"], "Work experience")
        for j in D["jobs"]: entry(doc, S, j, MAIN, blurb=False)
        doc.P(S["h"], "Education")
        for e in D["education"]:
            doc.P(S["job"], e["degree"], ("\t", None), (e["dates"], {"bold": False, "size": 8.5, "color": GREY}))
            doc.P(S["org"], e["school"] + ",  " + e["place"])
        doc.P(S["h"], "Skills")
        for k, (name, pct) in enumerate(D["skills"][:4]):
            doc.P(S["sl"], name); bar(doc, MAIN - 80, pct, GOLD, "D4D4D4")

    grid(doc, [SIDE, MAIN], [
        {"h": 96, "cells": [{"span": 2, "fill": NAVY, "v": "center", "fn": banner}]},
        {"h": 640, "rule": "atLeast", "cells": [{"pad": (0, 28, 14), "fn": side}, {"pad": (0, 22, 30), "fn": main}]}])


# ---------------------------------------------------------------------------------------------------- shared section renderers
def tabdate(doc, S, left, date):
    doc.P(S["job"], left, ("\t", None), (date, {"font": S["datefont"], "bold": False, "size": S["datesize"], "color": S["datecolor"]}))


def r_edu(doc, S, D, dates_right=True, note=False):
    for e in D["education"]:
        if dates_right: tabdate(doc, S, e["degree"], e["dates"])
        else: doc.P(S["job"], e["degree"])
        doc.P(S["org"], e["school"] + ",  " + e["place"] + ("" if dates_right else "  |  " + e["dates"]))
        if note and e["note"]: doc.P(S["blurb"], e["note"])


def r_skillbars(doc, S, D, w, fill, track, n=6, pct=False, thick=4):
    for name, p in D["skills"][:n]:
        if pct: doc.P(S["sl"], name, ("\t", None), (str(p) + "%", {"bold": True}))
        else: doc.P(S["sl"], name)
        bar(doc, w, p, fill, track, thick)


def r_langbars(doc, S, D, w, fill, track, thick=4):
    for lang, p, lvl in D["languages"]:
        doc.P(S["sl"], lang); bar(doc, w, p, fill, track, thick)


def r_skilltext(doc, S, D, label_color=None, sep="  ·  "):
    for label, items in D["skill_groups"]:
        doc.P(S["t"], (label + ":  ", {"bold": True, **({"color": label_color} if label_color else {})}), sep.join(items))


def r_list(doc, S, items, key="st"):
    for it in items: doc.P(S[key], it)


def r_bullets(doc, S, items, color):
    for it in items: doc.P(S["bul"], ("•", {"color": color}), ("\t", None), it)


def r_refs(doc, S, D):
    for n, role, ph in D["references"]:
        doc.P(S["job"], n); doc.P(S["org"], role); doc.P(S["st"], ph)


def r_certs(doc, S, D):
    for n, org, yr in D["certs"]:
        doc.P(S["job"], n); doc.P(S["org"], org + ",  " + yr)


# ---------------------------------------------------------------------------------------------------- more designs
@design("stylish-a")
def stylish_a(doc, D, out_dir):
    """Full-height dark slate sidebar (avatar, contact, education, expertise, language) + main column with a dated timeline."""
    SLATE, INK, GREY, LINE = "2D3A55", "3C3C3C", "7A7A7A", "9AA3B5"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Calibri", "Corbel", "Arial")
    SIDE = 190.0; MAIN = doc.PW - SIDE
    doc.page_setup(0, 0, 0, 0)
    S = dict(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=SLATE)
    S["sh"] = doc.style("SA SideHead", HF, 12.5, "FFFFFF", bold=True, before=16, after=5, bottom=("FFFFFF", 0.75, 3))
    S["sl"] = doc.style("SA SideLabel", BF, 9, "FFFFFF", bold=True, before=4, after=0)
    S["st"] = doc.style("SA SideText", BF, 8.5, "E4E8F0", after=3)
    S["sb"] = doc.style("SA SideBullet", BF, 8.5, "E4E8F0", after=2, left=12, first=-12)
    S["name"] = doc.style("SA Name", HF, 26, SLATE, bold=True, spacing=2, after=2)
    S["ttl"] = doc.style("SA Title", HF, 12, GREY, spacing=3.5, after=8)
    S["t"] = doc.style("SA Text", BF, 9, GREY, after=4, line=1.12)
    S["h"] = doc.style("SA Head", HF, 14.5, SLATE, bold=True, before=14, after=8, bottom=(SLATE, 1.0, 3))
    S["dt"] = doc.style("SA Date", HF, 9, GREY, bold=True, spacing=1, before=6, after=0, left=16, leftb=(LINE, 1.25, 8))
    S["job"] = doc.style("SA Job", BF, 10, SLATE, bold=True, after=0, left=16, leftb=(LINE, 1.25, 8))
    S["org"] = doc.style("SA Org", BF, 9, GREY, after=3, left=16, leftb=(LINE, 1.25, 8))
    S["bul"] = doc.style("SA Bullet", BF, 9, "4A4A4A", after=2, left=27, first=-11, leftb=(LINE, 1.25, 8), line=1.08)
    S["ref"] = doc.style("SA Ref", HF, 11, SLATE, bold=True, after=0)
    av = avatar(os.path.join(out_dir, "avatar-stylish.png"), "E7EAF0", "8A97AE")

    def side():
        doc.picture(av, 118, align="center", before=2, after=4)
        doc.P(S["sh"], "Contact")
        for lab, val in contact_lines(D)[:3]: doc.P(S["sl"], lab); doc.P(S["st"], val)
        doc.P(S["sh"], "Education")
        for e in D["education"]:
            doc.P(S["sl"], e["dates"]); doc.P(S["st"], e["degree"]); doc.P(S["st"], e["school"])
        doc.P(S["sh"], "Expertise")
        for name, p in D["skills"][:5]: doc.P(S["sb"], ("•", None), ("\t", None), name) if False else doc.P(S["st"], "•  " + name)
        doc.P(S["sh"], "Language")
        for lang, p, lvl in D["languages"]: doc.P(S["sl"], lang)

    def main():
        doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])
        doc.P(S["t"], D["summary"])
        doc.P(S["h"], "Experience")
        for j in D["jobs"]:
            doc.P(S["dt"], ("●  ", {"color": SLATE, "size": 7}), j["dates"].upper())
            doc.P(S["job"], j["title"]); doc.P(S["org"], j["org"] + ",  " + j["place"])
            for b in j["bullets"]: doc.P(S["bul"], ("•", {"color": SLATE}), ("\t", None), b)
        doc.P(S["h"], "Reference")
        for n, role, ph in D["references"]: doc.P(S["ref"], n); doc.P(S["t"], role + "  |  " + ph)

    grid(doc, [SIDE, MAIN], [{"h": doc.PH - 14, "rule": "atLeast", "cells": [
        {"fill": SLATE, "pad": (30, 22, 18), "fn": side}, {"pad": (34, 30, 34), "fn": main}]}])


@design("modern-a")
def modern_a(doc, D, out_dir):
    """Teal banner with a tracked serif name; right-aligned left column, thin spine, contact and experience on the right."""
    TEAL, INK, GREY, LINE = "24657F", "3A3A3A", "6E6E6E", "C5D3DC"
    HF, BF, SF = doc.font("Century Gothic", "Calibri"), doc.font("Calibri", "Corbel"), doc.font("Georgia", "Cambria", "Times New Roman")
    LEFT = 224.0; RIGHT = doc.PW - LEFT
    doc.page_setup(0, 0, 0, 0)
    S = dict(datefont=BF, datesize=8.5, datecolor=TEAL, bulcolor=TEAL)
    S["name"] = doc.style("MA Name", SF, 25, "FFFFFF", spacing=5, align="center", after=3)
    S["ttl"] = doc.style("MA Title", HF, 10, "FFFFFF", spacing=2.5, caps=True, align="center")
    S["lh"] = doc.style("MA LeftHead", SF, 11, TEAL, bold=True, spacing=3, caps=True, before=16, after=5, align="right")
    S["lt"] = doc.style("MA LeftText", BF, 9, INK, after=3, align="right", line=1.12)
    S["ll"] = doc.style("MA LeftLabel", BF, 9, INK, after=1, before=3, align="right")
    S["lj"] = doc.style("MA LeftJob", BF, 9, INK, bold=True, after=0, align="right")
    S["lo"] = doc.style("MA LeftOrg", BF, 8.8, GREY, after=3, align="right")
    DIV = (LINE, 1.0, 12)
    S["h"] = doc.style("MA Head", SF, 11, TEAL, bold=True, spacing=3, caps=True, before=14, after=6, left=14, leftb=DIV)
    S["dt"] = doc.style("MA Date", BF, 9, TEAL, before=6, after=0, left=14, leftb=DIV)
    S["job"] = doc.style("MA Job", BF, 9.5, INK, bold=True, after=0, left=14, leftb=DIV)
    S["org"] = doc.style("MA Org", BF, 9, GREY, bold=True, after=3, left=14, leftb=DIV)
    S["bul"] = doc.style("MA Bullet", BF, 9, INK, after=3, left=25, first=-11, line=1.1, leftb=DIV)
    S["cl"] = doc.style("MA Contact", BF, 9, INK, after=3, left=14, leftb=DIV)
    av = avatar(os.path.join(out_dir, "avatar-modern.png"), "E4EDF2", "7A98A8")

    def banner(): doc.P(S["name"], D["name"].upper()); doc.P(S["ttl"], D["title"])

    def left():
        doc.picture(av, 96, align="right", before=4, after=2)
        doc.P(S["lh"], "Summary"); doc.P(S["lt"], D["summary"])
        doc.P(S["lh"], "Education")
        for e in D["education"]:
            doc.P(S["ll"], e["dates"]); doc.P(S["lj"], e["degree"]); doc.P(S["lo"], e["school"] + ", " + e["place"])
        doc.P(S["lh"], "Relevant skills")
        for name, p in D["skills"][:5]:
            doc.P(S["ll"], name, ("\t", None)) if False else doc.P(S["ll"], name + "   " + str(p) + "%"); bar(doc, LEFT - 48, p, TEAL, "D8E2E8", 4)

    def right():
        doc.P(S["h"], ("●  ", {"size": 6.5}), "Contact")
        for lab, val in contact_lines(D): doc.P(S["cl"], (lab.lower() + "   ", {"color": GREY}), val)
        doc.P(S["h"], ("●  ", {"size": 6.5}), "Professional experience")
        for j in D["jobs"]:
            doc.P(S["dt"], j["dates"]); doc.P(S["job"], j["title"]); doc.P(S["org"], j["org"] + ",  " + j["place"])
            for b in j["bullets"]: doc.P(S["bul"], ("•", {"color": TEAL}), ("\t", None), b)

    grid(doc, [LEFT, RIGHT], [
        {"h": 90, "cells": [{"span": 2, "fill": TEAL, "v": "center", "fn": banner}]},
        {"h": 640, "rule": "atLeast", "cells": [{"pad": (0, 34, 14), "fn": left}, {"pad": (0, 0, 34), "fn": right}]}])


@design("clean-a")
def clean_a(doc, D, out_dir):
    """Monochrome: wide-tracked name, hairline rule, two columns split by a thin vertical line."""
    INK, GREY, LINE = "1E1E1E", "6A6A6A", "B8B8B8"
    HF, BF = doc.font("Century Gothic", "Calibri"), doc.font("Calibri", "Corbel")
    SIDEW = 190.0; MAINW = doc.PW - 72 - SIDEW
    doc.page_setup(40, 0, 36, 36)
    S = dict(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=INK)
    S["name"] = doc.style("CA Name", HF, 26, INK, spacing=6, align="center", after=2, before=6)
    S["ttl"] = doc.style("CA Title", HF, 8.5, GREY, spacing=3.5, caps=True, align="center", after=14, bottom=(LINE, 0.75, 14))
    S["h"] = doc.style("CA Head", HF, 12.5, INK, before=16, after=7, spacing=0.6, caps=True)
    S["t"] = doc.style("CA Text", BF, 9, GREY, after=4, line=1.15)
    S["job"] = doc.style("CA Job", BF, 9.5, INK, bold=True, before=6, after=0, tab=MAINW - 22)
    S["org"] = doc.style("CA Org", BF, 9, INK, after=2)
    S["blurb"] = doc.style("CA Blurb", BF, 8.8, GREY, after=2, line=1.1)
    S["bul"] = doc.style("CA Bullet", BF, 9, GREY, after=3, left=11, first=-11, line=1.12)
    DIV = (LINE, 0.75, 14)
    S["st"] = doc.style("CA Side", BF, 8.8, GREY, after=3, left=16, leftb=DIV)
    S["sh"] = doc.style("CA SideHead", HF, 12.5, INK, before=16, after=7, spacing=0.6, caps=True, left=16, leftb=DIV)
    S["sj"] = doc.style("CA SideJob", BF, 9, INK, bold=True, before=4, after=0, left=16, leftb=DIV)
    S["so"] = doc.style("CA SideOrg", BF, 8.8, GREY, after=2, left=16, leftb=DIV)
    S["sb"] = doc.style("CA SideBullet", BF, 8.8, GREY, after=2, left=26, first=-10, leftb=DIV)
    S["mj"] = doc.style("CA RefName", BF, 9, INK, bold=True, before=4, after=0)
    S["mo"] = doc.style("CA RefOrg", BF, 8.8, GREY, after=2)
    doc.P(S["name"], D["name"].upper()); doc.P(S["ttl"], D["title"])

    def main():
        doc.P(S["h"], "Profile"); doc.P(S["t"], D["summary"])
        doc.P(S["h"], "Experience")
        for j in D["jobs"]:
            tabdate(doc, S, j["title"], j["dates"]); doc.P(S["org"], j["org"]); doc.P(S["blurb"], j["blurb"] or " ")
            for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
        doc.P(S["h"], "References")
        for n, role, ph in D["references"]: doc.P(S["mj"], n); doc.P(S["mo"], role + "  |  " + ph)

    def side():
        doc.P(S["sh"], "Contact")
        for lab, val in contact_lines(D): doc.P(S["st"], val)
        doc.P(S["sh"], "Education")
        for e in D["education"]: doc.P(S["sj"], e["degree"]); doc.P(S["so"], e["school"]); doc.P(S["so"], e["dates"])
        doc.P(S["sh"], "Skills")
        for name, p in D["skills"][:6]: doc.P(S["sb"], ("•", None), ("\t", None), name)
        doc.P(S["sh"], "Technical skills")
        for t in D["skill_groups"][2][1]: doc.P(S["sb"], ("•", None), ("\t", None), t)

    grid(doc, [MAINW, SIDEW], [{"h": 640, "rule": "atLeast", "cells": [
        {"pad": (0, 0, 20), "fn": main}, {"fn": side}]}], pre=2)


@design("clean-b")
def clean_b(doc, D, out_dir):
    """Light-grey header band with a round avatar and a big bold name; two grey columns split by a thin line."""
    BAND, INK, GREY, LINE = "F1F1F1", "2B2B2B", "6B6B6B", "CFCFCF"
    HF, BF = doc.font("Century Gothic", "Calibri"), doc.font("Calibri", "Corbel")
    A = 200.0; C = doc.PW - A
    doc.page_setup(0, 0, 0, 0)
    DIV = (LINE, 0.75, 16)
    S = dict(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=GREY)
    S["name"] = doc.style("CB Name", HF, 30, INK, bold=True, after=0)
    S["ttl"] = doc.style("CB Title", HF, 15, GREY, after=0)
    S["h"] = doc.style("CB Head", HF, 9.5, INK, bold=True, spacing=4.5, caps=True, before=18, after=8)
    S["mh"] = doc.style("CB MainHead", HF, 9.5, INK, bold=True, spacing=4.5, caps=True, before=18, after=8, left=18, leftb=DIV)
    S["t"] = doc.style("CB Text", BF, 9, GREY, after=4, line=1.2, left=18, leftb=DIV)
    S["st"] = doc.style("CB Side", BF, 9, GREY, after=4)
    S["job"] = doc.style("CB Job", BF, 9.5, INK, bold=True, caps=True, before=6, after=0, left=18, leftb=DIV)
    S["org"] = doc.style("CB Org", BF, 9, GREY, bold=True, after=3, left=18, leftb=DIV)
    S["bul"] = doc.style("CB Bullet", BF, 9, GREY, after=3, left=29, first=-11, line=1.15, leftb=DIV)
    S["sb"] = doc.style("CB SideBullet", BF, 9, GREY, after=3, left=10, first=-10)
    S["sj"] = doc.style("CB SideJob", BF, 9, INK, bold=True, caps=True, before=3, after=1)
    S["mjn"] = doc.style("CB RefName", BF, 9, INK, bold=True, caps=True, before=3, after=1, left=18, leftb=DIV)
    S["mst"] = doc.style("CB RefText", BF, 9, GREY, after=4, left=18, leftb=DIV)
    av = avatar(os.path.join(out_dir, "avatar-clean.png"), "CFCFCF", "7C7C7C")

    def hdr_a(): doc.picture(av, 106, align="center")

    def hdr_b(): doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])

    def side():
        doc.P(S["h"], "Contact:")
        for lab, val in contact_lines(D)[:3]: doc.P(S["st"], val)
        doc.P(S["h"], "Skills:")
        for name, p in D["skills"][:6]: doc.P(S["sb"], ("•", None), ("\t", None), name)
        doc.P(S["h"], "Education:")
        for e in D["education"]: doc.P(S["sj"], e["school"] + "  " + e["dates"]); doc.P(S["st"], e["degree"])
        doc.P(S["h"], "Language:")
        for lang, p, lvl in D["languages"]: doc.P(S["sb"], ("•", None), ("\t", None), lang)

    def main():
        doc.P(S["mh"], "Profile:"); doc.P(S["t"], D["summary"])
        doc.P(S["mh"], "Experience:")
        for j in D["jobs"]:
            doc.P(S["job"], j["title"] + "  |  " + j["dates"]); doc.P(S["org"], j["org"])
            for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
        doc.P(S["mh"], "References:")
        for n, role, ph in D["references"]: doc.P(S["mjn"], n); doc.P(S["mst"], role + "  |  " + ph)

    head = ({"h": 150, "cells": [{"fill": BAND, "v": "center", "fn": hdr_a}, {"fill": BAND, "v": "center", "pad": (0, 24, 20), "fn": hdr_b}]} if doc.photo else
            {"h": 118, "cells": [{"span": 2, "fill": BAND, "v": "center", "pad": (0, 34, 20), "fn": hdr_b}]})
    grid(doc, [A, C], [head,
        {"h": 610, "rule": "atLeast", "cells": [{"pad": (0, 34, 18), "fn": side}, {"pad": (0, 8, 34), "fn": main}]}])


def lead_bold(text, n=4):
    """Split a bullet into a bold lead-in (first n words) and the rest, as in executive résumés."""
    w = text.split(" ")
    return (" ".join(w[:n]) + " ", {"bold": True}), " ".join(w[n:])


@design("traditional-a")
def traditional_a(doc, D, out_dir):
    """Classic: centred serif name, blue title and employers, centred serif section headings over a full-width rule, right-aligned dates."""
    INK, BLUE, GREY = "151515", "2272C3", "5A5A5A"
    HF, BF = doc.font("Georgia", "Cambria", "Times New Roman"), doc.font("Calibri", "Corbel", "Arial")
    W = doc.PW - 2 * 52
    doc.page_setup(46, 36, 52, 52)
    S = dict(datefont=BF, datesize=10, datecolor=INK, bulcolor=INK)
    S["name"] = doc.style("TA Name", HF, 22, INK, bold=True, caps=True, align="center", after=1)
    S["ttl"] = doc.style("TA Title", BF, 13, BLUE, align="center", after=2)
    S["con"] = doc.style("TA Contact", BF, 9.5, INK, align="center", after=6)
    S["h"] = doc.style("TA Head", HF, 13, INK, bold=True, align="center", before=12, after=6, bottom=(INK, 1.0, 4), keep=True)
    S["t"] = doc.style("TA Text", BF, 9.5, "2B2B2B", after=4, line=1.15)
    S["org"] = doc.style("TA Org", BF, 13, BLUE, before=6, after=0)
    S["job"] = doc.style("TA Job", BF, 10.5, INK, after=1, tab=W)
    S["blurb"] = doc.style("TA Blurb", BF, 9.5, GREY, after=2, line=1.12)
    S["bul"] = doc.style("TA Bullet", BF, 9.5, "2B2B2B", after=2, left=14, first=-10, line=1.1)
    doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])
    doc.P(S["con"], D["phone"], "   •   ", D["email"], "   •   ", D["web"], "   •   ", D["location"])
    doc.P(S["h"], "Summary"); doc.P(S["t"], D["summary"])
    doc.P(S["h"], "Experience")
    for j in D["jobs"]:
        doc.P(S["org"], j["org"])
        tabdate(doc, S, j["title"], j["dates"])
        if j["blurb"]: doc.P(S["blurb"], j["blurb"])
        for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
    doc.P(S["h"], "Education")
    for e in D["education"]:
        doc.P(S["org"], e["school"]); tabdate(doc, S, e["degree"], e["dates"])
    doc.P(S["h"], "Skills")
    for label, items in D["skill_groups"]:
        doc.P(S["t"], (label + ":  ", {"color": BLUE}), "  ·  ".join(items))
    doc.P(S["h"], "Certifications")
    for n, org, yr in D["certs"]:
        doc.P(S["org"], n); tabdate(doc, S, org, yr)


@design("traditional-b")
def traditional_b(doc, D, out_dir):
    """Left-aligned bold name and tagline, three-part contact row, caps headings, and a timeline (dates left, dotted line, details right)."""
    INK, GREY, LINE, DOT = "111111", "6B6B6B", "A9A9A9", "111111"
    HF, BF = doc.font("Calibri", "Corbel", "Arial"), doc.font("Calibri", "Corbel", "Arial")
    DATEW = 110.0; MAINW = doc.PW - 2 * 52 - DATEW
    doc.page_setup(50, 36, 52, 52)
    S = dict(datefont=BF, datesize=9, datecolor=GREY, bulcolor=GREY)
    S["name"] = doc.style("TB Name", HF, 30, INK, bold=True, caps=True, after=0)
    S["ttl"] = doc.style("TB Title", HF, 14, GREY, bold=True, after=4)
    S["con"] = doc.style("TB Contact", BF, 9, INK, bold=True, after=2)
    S["h"] = doc.style("TB Head", HF, 15, INK, bold=True, caps=True, before=16, after=7, keep=True)
    S["t"] = doc.style("TB Text", BF, 9.5, GREY, after=4, line=1.15)
    S["dt"] = doc.style("TB Date", BF, 10, INK, bold=True, before=6, after=0)
    S["dp"] = doc.style("TB Place", BF, 9.5, GREY, after=0)
    TL = doc.vline_style("Timeline", LINE, 0.75)
    S["job"] = doc.style("TB Job", HF, 13, INK, before=6, after=0)
    S["org"] = doc.style("TB Org", BF, 10, GREY, bold=True, after=2)
    S["blurb"] = doc.style("TB Blurb", BF, 9, GREY, after=2, line=1.1)
    S["bul"] = doc.style("TB Bullet", BF, 9.5, GREY, after=2, left=10, first=-10, line=1.12)
    S["ach"] = doc.style("TB AchHead", HF, 11, INK, bold=True, after=2)
    doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["tagline"])
    doc.c("styles.modify", style=S["con"], para={"tabs": [{"pos": 200, "align": "left", "leader": "none"}, {"pos": 400, "align": "left", "leader": "none"}]})
    doc.P(S["con"], D["phone"], ("\t", None), D["email"], ("\t", None), D["web"])
    doc.P(S["con"], D["location"])
    doc.P(S["h"], "Key achievements")
    grid(doc, [(doc.PW - 104) / 2, (doc.PW - 104) / 2], [{"cells": [
        {"pad": (0, 0, 14), "fn": lambda: [doc.P(S["ach"], D["achievements"][0][0]), doc.P(S["t"], D["achievements"][0][1])]},
        {"pad": (0, 0, 0), "fn": lambda: [doc.P(S["ach"], D["achievements"][1][0]), doc.P(S["t"], D["achievements"][1][1])]}]}])
    doc.P(S["h"], "Experience")

    def row(date, place, title, org, blurb, bullets):
        def a():
            doc.P(S["dt"], date)
            if place: doc.P(S["dp"], place)

        def b():
            doc.P(S["job"], title); doc.P(S["org"], org)
            if blurb: doc.P(S["blurb"], blurb)
            for x in bullets: doc.P(S["bul"], ("•", None), ("\t", None), x)
        return {"cells": [{"pad": (0, 0, 12), "fn": a}, {"pad": (0, 14, 0), "fn": b}]}

    grid(doc, [DATEW, MAINW], [row(j["dates"], j["place"], j["title"], j["org"], "", j["bullets"]) for j in D["jobs"]], style=TL)
    doc.P(S["h"], "Education")
    grid(doc, [DATEW, MAINW], [row(e["dates"], e["place"], e["degree"], e["school"], "", []) for e in D["education"]], style=TL)
    doc.P(S["h"], "Skills")
    doc.P(S["t"], "   ·   ".join(n for n, p in D["skills"]))


@design("professional-a")
def professional_a(doc, D, out_dir):
    """Executive résumé: small-caps serif name between rules, centred caps headline, justified summary, expertise columns, bold lead-ins."""
    INK, GREY, LINK = "000000", "444444", "1F3FBF"
    HF = BF = doc.font("Times New Roman", "Georgia", "Cambria")
    W = doc.PW - 2 * 54
    doc.page_setup(36, 30, 54, 54)
    S = dict(datefont=BF, datesize=10.5, datecolor=INK, bulcolor=INK)
    S["name"] = doc.style("PA Name", HF, 21, INK, bold=True, smallcaps=True, align="center", spacing=1, before=2, after=1, top=(INK, 0.5, 6))
    S["con"] = doc.style("PA Contact", BF, 10, INK, align="center", after=2, bottom=(INK, 1.75, 5))
    S["ttl"] = doc.style("PA Headline", BF, 12.5, INK, bold=True, caps=True, align="center", before=8, after=4)
    S["t"] = doc.style("PA Text", BF, 10.5, INK, after=5, line=1.08, align="justify")
    S["ex"] = doc.style("PA ExpertHead", BF, 10.5, INK, bold=True, after=2)
    S["xp"] = doc.style("PA Expert", BF, 10.5, INK, after=0, left=14, first=-10)
    S["h"] = doc.style("PA Head", BF, 11.5, INK, bold=True, smallcaps=True, align="center", spacing=1, before=12, after=8, top=(INK, 0.5, 3), bottom=(INK, 1.5, 3), keep=True)
    S["job"] = doc.style("PA Job", BF, 10.5, INK, smallcaps=True, before=6, after=0, tab=W)
    S["org"] = doc.style("PA Role", BF, 10.5, INK, bold=True, after=2)
    S["blurb"] = doc.style("PA Blurb", BF, 10.5, INK, after=3, line=1.06, align="justify")
    S["bul"] = doc.style("PA Bullet", BF, 10.5, INK, after=3, left=24, first=-14, line=1.06, align="justify")
    doc.P(S["name"], D["name"]); doc.P(S["con"], D["phone"], "  |  ", (D["email"], {"color": LINK, "underline": "single"}), "  |  ", (D["location"], None))
    doc.P(S["ttl"], D["title"] + " | Nursery Operations")
    doc.P(S["t"], D["summary"] + " ", ("Areas of expertise include:", {"bold": True}))
    cols = [D["skill_groups"][0][1][:3], D["skill_groups"][0][1][3:] + D["skill_groups"][1][1][:1], D["skill_groups"][1][1][1:4]]
    grid(doc, [W / 3, W / 3, W / 3], [{"cells": [{"fn": (lambda c=c: [doc.P(S["xp"], ("•", None), ("\t", None), x) for x in c])} for c in cols]}])
    doc.P(S["h"], "Professional Experience")
    for j in D["jobs"]:
        doc.P(S["job"], (j["org"], None), ", " + j["place"], ("\t", None), j["dates"])
        doc.P(S["org"], j["title"])
        if j["blurb"]: doc.P(S["blurb"], j["blurb"])
        for b in j["bullets"]:
            lead, rest = lead_bold(b, 3); doc.P(S["bul"], ("•", None), ("\t", None), lead, rest)
    doc.P(S["h"], "Education")
    for e in D["education"]:
        doc.P(S["job"], (e["school"], None), ", " + e["place"], ("\t", None), e["dates"]); doc.P(S["org"], e["degree"])


@design("professional-b")
def professional_b(doc, D, out_dir):
    """Bold geometric sans: heavy centred name, light title, contact row between hairlines, bold caps headings with rules, 3-column skills."""
    INK, GREY, RULE = "262626", "5C5C5C", "7A7A7A"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Calibri", "Corbel", "Arial")
    W = doc.PW - 2 * 54
    doc.page_setup(42, 30, 54, 54)
    S = dict(datefont=BF, datesize=9, datecolor=GREY, bulcolor=INK)
    S["name"] = doc.style("PB Name", HF, 28, INK, bold=True, caps=True, align="center", after=0)
    S["ttl"] = doc.style("PB Title", HF, 14, INK, align="center", after=10)
    S["con"] = doc.style("PB Contact", BF, 9.5, GREY, after=4, before=0, top=(RULE, 0.75, 6), bottom=(RULE, 0.75, 6), align="center")
    S["h"] = doc.style("PB Head", HF, 12.5, INK, bold=True, spacing=1.5, caps=True, before=16, after=5, bottom=(RULE, 0.75, 5), keep=True)
    S["t"] = doc.style("PB Text", BF, 9.5, GREY, after=4, line=1.18)
    S["job"] = doc.style("PB Job", HF, 10, INK, bold=True, before=6, after=0)
    S["org"] = doc.style("PB Org", BF, 9.5, GREY, after=2)
    S["bul"] = doc.style("PB Bullet", BF, 9.5, GREY, after=2, left=14, first=-10, line=1.12)
    S["sb"] = doc.style("PB SkillBullet", BF, 9.5, GREY, after=2, left=12, first=-10)
    doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])
    doc.c("styles.modify", style=S["con"], para={"tabs": [{"pos": W, "align": "right", "leader": "none"}]})
    doc.P(S["con"], D["phone"], "     |     ", D["email"], "     |     ", D["location"])
    doc.P(S["h"], "About me"); doc.P(S["t"], D["summary"])
    doc.P(S["h"], "Work experience")
    for j in D["jobs"]:
        doc.P(S["org"], (j["org"] + "  |  " + j["dates"], None)); doc.P(S["job"], j["title"])
        for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
    doc.P(S["h"], "Education")
    for e in D["education"]:
        doc.P(S["org"], e["school"] + "  |  " + e["dates"]); doc.P(S["job"], e["degree"])
    doc.P(S["h"], "Skills")
    items = [n for n, p in D["skills"]]
    grid(doc, [W / 3, W / 3, W / 3], [{"cells": [{"fn": (lambda c=items[k::3]: [doc.P(S["sb"], ("•", None), ("\t", None), x) for x in c])} for k in range(3)]}])


@design("academic-a")
def academic_a(doc, D, out_dir):
    """Dense two-column page: heavy-ruled caps headings, skills as underlined chips, Interests and Strengths on the right."""
    INK, GREY, RULE = "1A1A1A", "5E5E5E", "1A1A1A"
    HF, BF = doc.font("Calibri", "Corbel", "Arial"), doc.font("Calibri", "Corbel", "Arial")
    LW = 340.0; RW = doc.PW - 2 * 36 - LW
    doc.page_setup(34, 24, 36, 36)
    S = dict(datefont=BF, datesize=8.2, datecolor=GREY, bulcolor=INK)
    S["name"] = doc.style("AA Name", HF, 27, INK, bold=True, caps=True, after=0)
    S["ttl"] = doc.style("AA Title", HF, 12, GREY, bold=True, after=3)
    S["con"] = doc.style("AA Contact", BF, 8.5, INK, bold=True, after=4)
    S["h"] = doc.style("AA Head", HF, 13, INK, bold=True, caps=True, before=10, after=5, bottom=(RULE, 1.75, 2), keep=True)
    S["t"] = doc.style("AA Text", BF, 8.6, "333333", after=3, line=1.1)
    S["job"] = doc.style("AA Job", HF, 11, INK, before=5, after=0)
    S["org"] = doc.style("AA Org", BF, 9, GREY, bold=True, after=0)
    S["dp"] = doc.style("AA DatePlace", BF, 8.2, GREY, after=2)
    S["bul"] = doc.style("AA Bullet", BF, 8.6, "333333", after=1.5, left=11, first=-9, line=1.08)
    S["chip"] = doc.style("AA Chip", BF, 9, INK, bold=True, before=3, after=3, bottom=("B5B5B5", 0.75, 2), right=60)
    S["ih"] = doc.style("AA InterestHead", BF, 9, INK, bold=True, before=3, after=0)
    S["it"] = doc.style("AA InterestText", BF, 8.4, GREY, after=2, bottom=("DDDDDD", 0.5, 3), line=1.08)
    S["tn"] = doc.style("AA Training", BF, 9, GREY, bold=True, before=3, after=0)
    doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"] + "  |  Nursery Operations")
    doc.c("styles.modify", style=S["con"], para={"tabs": [{"pos": 130, "align": "left", "leader": "none"}, {"pos": 330, "align": "left", "leader": "none"}, {"pos": 440, "align": "left", "leader": "none"}]})
    doc.P(S["con"], D["phone"], ("\t", None), D["email"], ("\t", None), D["web"], ("\t", None), D["location"])

    def left():
        doc.P(S["h"], "Summary"); doc.P(S["t"], D["summary"])
        doc.P(S["h"], "Experience")
        for j in D["jobs"]:
            doc.P(S["job"], j["title"]); doc.P(S["org"], j["org"]); doc.P(S["dp"], j["dates"] + "   |   " + j["place"])
            for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
        doc.P(S["h"], "Volunteering")
        for v in D["volunteer"]:
            doc.P(S["job"], v["title"]); doc.P(S["org"], v["org"]); doc.P(S["dp"], v["dates"])
            for b in v["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
        doc.P(S["h"], "Education")
        for e in D["education"]: doc.P(S["job"], e["degree"]); doc.P(S["org"], e["school"]); doc.P(S["dp"], e["dates"] + "   |   " + e["place"])

    def right():
        doc.P(S["h"], "Skills")
        for n, p in D["skills"]: doc.P(S["chip"], n)
        doc.P(S["h"], "Training / Courses")
        for n, org, yr in D["certs"]: doc.P(S["tn"], n); doc.P(S["dp"], org + ",  " + yr)
        doc.P(S["h"], "Interests")
        for i, t in zip(D["interests"], ["Native plants and pollinator gardens.", "Neighbourhood food and flower plots.", "Saving and swapping local seed.", "Garden and landscape portraits."]):
            doc.P(S["ih"], i); doc.P(S["it"], t)
        doc.P(S["h"], "Strengths")
        for a, t in D["achievements"]: doc.P(S["ih"], a); doc.P(S["it"], t)

    grid(doc, [LW, RW], [{"cells": [{"pad": (0, 0, 20), "fn": left}, {"pad": (0, 6, 0), "fn": right}]}])


@design("academic-b")
def academic_b(doc, D, out_dir):
    """US graduate style: centred bold name, spaced contact row, pale-blue shaded heading bars, institution in bold, italic role, right-aligned place and dates."""
    INK, GREY, BAND = "000000", "444444", "DCE6F2"
    HF = BF = doc.font("Arial", "Liberation Sans", "Calibri")
    W = doc.PW - 2 * 48
    doc.page_setup(40, 30, 48, 48)
    S = dict(datefont=BF, datesize=9, datecolor=INK, bulcolor=INK)
    S["name"] = doc.style("AB Name", HF, 21, INK, bold=True, align="center", after=3)
    S["con"] = doc.style("AB Contact", BF, 8.5, GREY, after=6, tab=W)
    S["h"] = doc.style("AB Head", HF, 11, INK, bold=True, caps=True, before=9, after=4, left=0, keep=True)
    S["job"] = doc.style("AB Entry", BF, 9.5, INK, before=5, after=0, tab=W)
    S["org"] = doc.style("AB Role", BF, 9.5, INK, italic=True, after=1, tab=W)
    S["bul"] = doc.style("AB Bullet", BF, 9, INK, after=1.5, left=16, first=-8, line=1.06)
    S["t"] = doc.style("AB Text", BF, 9, INK, after=2, line=1.08)
    doc.P(S["name"], D["name"].upper())
    doc.c("styles.modify", style=S["con"], para={"tabs": [{"pos": 0, "align": "left", "leader": "none"}, {"pos": 150, "align": "left", "leader": "none"}, {"pos": 330, "align": "left", "leader": "none"}, {"pos": W, "align": "right", "leader": "none"}]})
    doc.P(S["con"], D["email"], ("\t", None), D["phone"], ("\t", None), D["location"], ("\t", None), D["web"])
    doc.P(S["h"], "Education", shade=BAND)
    for e in D["education"]:
        doc.P(S["job"], (e["school"], {"bold": True}), ", " + e["degree"].split(",")[0], ("\t", None), e["place"])
        doc.P(S["org"], e["degree"], ("\t", None), e["dates"])
        if e["note"]: doc.P(S["bul"], ("•", None), ("\t", None), e["note"])
    doc.P(S["h"], "Relevant Experience", shade=BAND)
    for j in D["jobs"]:
        doc.P(S["job"], (j["org"], {"bold": True}), ("\t", None), j["place"])
        doc.P(S["org"], j["title"], ("\t", None), j["dates"])
        for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)
    doc.P(S["h"], "Additional Experience", shade=BAND)
    for v in D["volunteer"]:
        doc.P(S["job"], (v["org"], {"bold": True}), (",  " + v["title"], {"italic": True}), ("\t", None), v["dates"])
    doc.P(S["h"], "Skills", shade=BAND)
    for label, items in D["skill_groups"]:
        doc.P(S["t"], (label.upper() + ":  ", {"bold": True}), "  |  ".join(items))


@design("elegant-b")
def elegant_b(doc, D, out_dir):
    """Airy variant: no banner, a wide-tracked light-grey name, round avatar and grey tracked headings, hairline between sidebar and page."""
    INK, GREY, LIGHT, RULE = "333333", "8A8A8A", "B5B5B5", "E3E3E3"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Calibri", "Corbel", "Arial")
    SIDE = 200.0; MAIN = doc.PW - SIDE
    doc.page_setup(0, 0, 0, 0)
    DIV = (RULE, 0.75, 22)
    S = dict(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=GREY)
    S["name"] = doc.style("EB Name", HF, 30, LIGHT, spacing=9, caps=True, after=6, before=0, left=0, leftb=DIV)
    S["ttl"] = doc.style("EB Title", HF, 9.5, INK, bold=True, spacing=4, caps=True, after=10, leftb=DIV)
    S["sh"] = doc.style("EB SideHead", HF, 11, LIGHT, spacing=3.5, caps=True, before=22, after=6)
    S["st"] = doc.style("EB SideText", BF, 8.8, GREY, after=4)
    S["sj"] = doc.style("EB SideJob", BF, 8.8, INK, bold=True, caps=True, before=5, after=1)
    S["h"] = doc.style("EB Head", HF, 11, LIGHT, spacing=3.5, caps=True, before=22, after=6, left=0, leftb=DIV, bottom=(RULE, 0.75, 4))
    S["t"] = doc.style("EB Text", BF, 9, GREY, after=4, line=1.2, leftb=DIV)
    S["job"] = doc.style("EB Job", BF, 9.5, INK, bold=True, caps=True, before=8, after=0, leftb=DIV, tab=MAIN - 62)
    S["org"] = doc.style("EB Org", BF, 8.8, GREY, bold=True, after=3, leftb=DIV)
    S["bul"] = doc.style("EB Bullet", BF, 9, GREY, after=3, left=11, first=-11, line=1.15, leftb=DIV)
    av = avatar(os.path.join(out_dir, "avatar-elegant-b.png"), "E4E4E4", "9A9A9A")

    def side():
        doc.picture(av, 118, align="center", before=0, after=4)
        doc.P(S["sh"], "Contact")
        for lab, val in contact_lines(D)[:3]: doc.P(S["st"], val)
        doc.P(S["sh"], "Education")
        for e in D["education"]: doc.P(S["sj"], e["degree"]); doc.P(S["st"], e["school"] + ", " + e["dates"])
        doc.P(S["sh"], "Skills")
        for n, p in D["skills"]: doc.P(S["st"], n)

    def main():
        doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])
        doc.P(S["h"], "Profile"); doc.P(S["t"], D["summary"])
        doc.P(S["h"], "Work experience")
        for j in D["jobs"]:
            doc.P(S["job"], j["title"], ("\t", None), (j["dates"], {"bold": False, "size": 8.3, "color": GREY}))
            doc.P(S["org"], j["org"] + ",  " + j["place"])
            for b in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), b)

    grid(doc, [SIDE, MAIN], [{"h": doc.PH - 14, "rule": "atLeast", "cells": [{"pad": (40, 34, 14), "fn": side}, {"pad": (56, 0, 34), "fn": main}]}])


@design("modern-b")
def modern_b(doc, D, out_dir):
    """Bold navy name over a rule; narrow left column with ruled headings; right column with a hairline spine and round markers."""
    NAVY, INK, GREY, LINE = "1F2A44", "2B2B2B", "6A6A6A", "BCC3D0"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Calibri", "Corbel", "Arial")
    LW = 186.0; RW = doc.PW - 2 * 40 - LW
    doc.page_setup(40, 24, 40, 40)
    DIV = (LINE, 1.0, 12)
    S = dict(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=NAVY)
    S["name"] = doc.style("MB Name", HF, 31, NAVY, bold=True, caps=True, after=0)
    S["ttl"] = doc.style("MB Title", HF, 13, GREY, caps=True, spacing=1, after=10, bottom=(NAVY, 1.5, 8))
    S["lh"] = doc.style("MB LeftHead", HF, 12, NAVY, bold=True, spacing=2, caps=True, before=18, after=6, bottom=(NAVY, 0.75, 3))
    S["st"] = doc.style("MB LeftText", BF, 9, INK, after=4, line=1.12)
    S["sb"] = doc.style("MB LeftBullet", BF, 9, INK, after=3, left=11, first=-10)
    S["sj"] = doc.style("MB LeftName", BF, 9.5, INK, bold=True, before=3, after=0)
    S["h"] = doc.style("MB Head", HF, 12, NAVY, bold=True, spacing=2, caps=True, before=18, after=7, left=14, leftb=DIV, bottom=None)
    S["t"] = doc.style("MB Text", BF, 9.2, INK, after=4, line=1.18, left=14, leftb=DIV)
    S["job"] = doc.style("MB Job", BF, 9.8, INK, bold=True, before=7, after=0, left=14, leftb=DIV, tab=RW - 60)
    S["org"] = doc.style("MB Org", BF, 9.2, GREY, after=3, left=14, leftb=DIV)
    S["bul"] = doc.style("MB Bullet", BF, 9.2, INK, after=3, left=25, first=-11, line=1.14, leftb=DIV)
    doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])

    def left():
        doc.P(S["lh"], "Contact")
        for lab, val in contact_lines(D): doc.P(S["st"], val)
        doc.P(S["lh"], "Skills")
        for n, p in D["skills"]: doc.P(S["sb"], ("•", {"color": NAVY}), ("\t", None), n)
        doc.P(S["lh"], "Languages")
        for lang, p, lvl in D["languages"]: doc.P(S["sb"], ("•", {"color": NAVY}), ("\t", None), lang + " (" + lvl + ")")
        doc.P(S["lh"], "Reference")
        for n, role, ph in D["references"][:1]: doc.P(S["sj"], n); doc.P(S["st"], role); doc.P(S["st"], ph)

    def right():
        doc.P(S["h"], ("●  ", {"size": 8}), "Profile"); doc.P(S["t"], D["summary"])
        doc.P(S["h"], ("●  ", {"size": 8}), "Work experience")
        for j in D["jobs"]:
            doc.P(S["job"], j["org"], ("\t", None), (j["dates"], {"bold": False, "size": 8.5, "color": GREY}))
            doc.P(S["org"], j["title"] + ",  " + j["place"])
            for b in j["bullets"]: doc.P(S["bul"], ("•", {"color": NAVY}), ("\t", None), b)
        doc.P(S["h"], ("●  ", {"size": 8}), "Education")
        for e in D["education"]:
            doc.P(S["job"], e["degree"], ("\t", None), (e["dates"], {"bold": False, "size": 8.5, "color": GREY})); doc.P(S["org"], e["school"] + ",  " + e["place"])

    grid(doc, [LW, RW], [{"cells": [{"pad": (0, 0, 14), "fn": left}, {"pad": (0, 0, 0), "fn": right}]}])


@design("stylish-b")
def stylish_b(doc, D, out_dir):
    """Three columns: blush side panel (avatar, profile, contact) | experience under a brown name | education and skill bars."""
    BROWN, GREEN, INK, GREY, BLUSH, LINE = "8A4B1B", "2E6B57", "2E2E2E", "6B6B6B", "F9EEE9", "D9D2CD"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Calibri", "Corbel", "Arial")
    A, C = 176.0, 178.0; B = doc.PW - A - C
    doc.page_setup(0, 0, 0, 0)
    DIV = (LINE, 0.75, 14)
    S = dict(datefont=BF, datesize=8.5, datecolor=GREY, bulcolor=BROWN)
    S["ah"] = doc.style("SB SideHead", HF, 10, BROWN, bold=True, spacing=2, caps=True, before=16, after=4)
    S["at"] = doc.style("SB SideText", BF, 9, INK, after=4, line=1.15)
    S["name"] = doc.style("SB Name", HF, 27, BROWN, caps=True, after=0, line=1.0)
    S["ttl"] = doc.style("SB Title", BF, 12, INK, bold=True, after=8)
    S["h"] = doc.style("SB Head", HF, 10.5, BROWN, bold=True, spacing=2, caps=True, before=12, after=6, bottom=(LINE, 0.75, 4))
    S["job"] = doc.style("SB Job", BF, 10.5, INK, bold=True, before=8, after=0)
    S["org"] = doc.style("SB Org", BF, 9, GREY, after=0)
    S["dt"] = doc.style("SB Date", BF, 8.5, BROWN, after=3)
    S["bul"] = doc.style("SB Bullet", BF, 9, INK, after=3, left=12, first=-10, line=1.12)
    S["ch"] = doc.style("SB RightHead", HF, 10.5, BROWN, bold=True, spacing=2, caps=True, before=16, after=5, left=0, leftb=DIV)
    S["ct"] = doc.style("SB RightText", BF, 9, INK, after=3, leftb=DIV)
    S["cj"] = doc.style("SB RightJob", BF, 9.2, INK, bold=True, before=3, after=0, leftb=DIV)
    S["cl"] = doc.style("SB RightLabel", BF, 8.8, INK, before=5, after=1, leftb=DIV, tab=C - 36)
    av = avatar(os.path.join(out_dir, "avatar-stylish-b.png"), "EFE2DB", "B58E7A")

    def a():
        doc.picture(av, 128, align="center", before=0, after=0)
        doc.P(S["ah"], "Profile"); doc.P(S["at"], D["summary"])
        doc.P(S["ah"], "Phone"); doc.P(S["at"], D["phone"])
        doc.P(S["ah"], "Email"); doc.P(S["at"], D["email"])
        doc.P(S["ah"], "Address"); doc.P(S["at"], D["location"])
        doc.P(S["ah"], "Website"); doc.P(S["at"], D["web"])

    def b():
        doc.P(S["name"], D["name"].split(" ")[0]); doc.P(S["name"], D["name"].split(" ")[1]); doc.P(S["ttl"], D["title"])
        doc.P(S["h"], "Professional experience")
        for j in D["jobs"]:
            doc.P(S["job"], j["title"]); doc.P(S["org"], j["org"] + ",  " + j["place"]); doc.P(S["dt"], j["dates"])
            for x in j["bullets"]: doc.P(S["bul"], ("▪", {"color": BROWN, "size": 7}), ("\t", None), x)

    def c():
        doc.P(S["ch"], "Education")
        for e in D["education"]: doc.P(S["dt"], e["dates"]); doc.P(S["cj"], e["degree"]); doc.P(S["ct"], e["school"] + ", " + e["place"])
        doc.P(S["ch"], "Key skills")
        for name, p in D["skills"][:4]:
            doc.P(S["cl"], name, ("\t", None), (str(p) + "%", {"bold": True})); bar(doc, C - 40, p, GREEN, "E2E8E5", 4)
        doc.P(S["ch"], "Languages")
        for lang, p, lvl in D["languages"]:
            doc.P(S["cl"], lang, ("\t", None), (lvl, {"color": GREY})); bar(doc, C - 40, p, GREEN, "E2E8E5", 4)

    grid(doc, [A, B, C], [{"h": doc.PH - 14, "rule": "atLeast", "cells": [
        {"fill": BLUSH, "pad": (34, 20, 18), "fn": a}, {"pad": (40, 24, 8), "fn": b}, {"pad": (40, 14, 20), "fn": c}]}])


@design("creative-a")
def creative_a(doc, D, out_dir):
    """Pale-blue page, deep-blue block with a round avatar, huge two-tone rounded-sans name, two columns split by a hairline."""
    TEAL, DARK, TINT, GREY, LINE = "1F5FA8", "12335E", "E9F1FA", "55657A", "BFD0E4"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Century Gothic", "Corbel", "Calibri")
    A = 214.0; B = doc.PW - A
    doc.page_setup(0, 0, 0, 0)
    DIV = (LINE, 0.75, 16)
    S = dict(datefont=BF, datesize=8.3, datecolor=GREY, bulcolor=TEAL)
    S["n1"] = doc.style("CR First", HF, 34, "6FA3D8", bold=True, after=0, line=0.92)
    S["n2"] = doc.style("CR Last", HF, 34, DARK, bold=True, after=2, line=0.92, bottom=(TEAL, 1.0, 6))
    S["ttl"] = doc.style("CR Title", HF, 17, GREY, before=4, after=0)
    S["h"] = doc.style("CR Head", HF, 12, DARK, bold=True, before=16, after=5)
    S["t"] = doc.style("CR Text", BF, 8.6, DARK, after=4, line=1.25)
    S["rh"] = doc.style("CR RightHead", HF, 12, DARK, bold=True, before=16, after=5, leftb=DIV)
    S["rt"] = doc.style("CR RightText", BF, 8.6, DARK, after=3, line=1.2, leftb=DIV)
    S["rb"] = doc.style("CR RightBullet", BF, 8.6, DARK, after=2, left=10, first=-10, leftb=DIV)
    S["rj"] = doc.style("CR RightJob", BF, 8.8, "5F7FA6", bold=True, before=7, after=1, leftb=DIV)
    av = avatar(os.path.join(out_dir, "avatar-creative.png"), "F2F6FB", "7FA3D0")

    def hdr_a():
        if doc.photo: doc.picture(av, 128, align="center", before=0, after=0)
        else:
            S["mono"] = doc.style("CR Monogram", HF, 58, "FFFFFF", bold=True, align="center", spacing=3)
            doc.P(S["mono"], "".join(w[0] for w in D["name"].split(" ")))

    def hdr_b():
        doc.P(S["n1"], D["name"].split(" ")[0]); doc.P(S["n2"], D["name"].split(" ")[1]); doc.P(S["ttl"], D["title"])

    def left():
        doc.P(S["h"], "About Me"); doc.P(S["t"], D["summary"])
        doc.P(S["h"], "Contact")
        for lab, val in contact_lines(D)[:3]: doc.P(S["t"], val)
        doc.P(S["h"], "Education")
        for e in D["education"]: doc.P(S["rj"].replace("rj", "rj") if False else S["t"], (e["degree"], {"bold": True}), "  ·  ", e["dates"]); doc.P(S["t"], e["school"])

    def right():
        doc.P(S["rh"], "Tools")
        for n, p in D["skills"][:5]: doc.P(S["rb"], ("•", None), ("\t", None), n)
        doc.P(S["rh"], "Experience")
        for j in D["jobs"]:
            doc.P(S["rj"], "•  " + j["title"] + ",  " + j["dates"])
            for b in j["bullets"][:2]: doc.P(S["rt"], b)
        doc.P(S["rh"], "References")
        for n, role, ph in D["references"]: doc.P(S["rj"], "•  " + n); doc.P(S["rt"], ph)

    grid(doc, [A, B], [
        {"h": 190, "cells": [{"fill": TEAL, "v": "center", "fn": hdr_a}, {"fill": TINT, "v": "center", "pad": (0, 22, 10), "fn": hdr_b}]},
        {"h": doc.PH - 204, "rule": "atLeast", "cells": [{"fill": TINT, "pad": (6, 34, 20), "fn": left}, {"fill": TINT, "pad": (6, 10, 26), "fn": right}]}])


@design("creative-b")
def creative_b(doc, D, out_dir):
    """Colour blocks in two complementary blues: deep-blue header with a white display name, pale-blue panel for the avatar, grey-blue sidebar, medium-blue experience panel."""
    OLIVE, OLIVE2, TERRA, SAND, GREYBG, INK, WHITE = "1B4D8C", "123A6E", "2F78C4", "D6E4F4", "EAF0F7", "3F4B5E", "FFFFFF"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Century Gothic", "Corbel", "Calibri")
    A, B = 190.0, 210.0; C = doc.PW - A - B
    doc.page_setup(0, 0, 0, 0)
    S = dict(datefont=BF, datesize=9, datecolor=WHITE, bulcolor=WHITE)
    S["name"] = doc.style("CB2 Name", HF, 31, WHITE, bold=True, after=2, line=0.95)
    S["ttl"] = doc.style("CB2 Title", HF, 10, "D6E6F8", italic=True, spacing=3, caps=True, after=10)
    S["ah"] = doc.style("CB2 AboutHead", HF, 13, WHITE, bold=True, after=3)
    S["at"] = doc.style("CB2 AboutText", BF, 8.8, "EAF2FB", after=3, line=1.2)
    S["lh"] = doc.style("CB2 SideHead", HF, 12, "1B4D8C", bold=True, before=16, after=5)
    S["lt"] = doc.style("CB2 SideText", BF, 8.8, INK, after=4, line=1.15)
    S["rh"] = doc.style("CB2 RightHead", HF, 13, WHITE, bold=True, before=14, after=6)
    S["yr"] = doc.style("CB2 Year", HF, 9, WHITE, bold=True, after=0)
    S["jt"] = doc.style("CB2 JobTitle", HF, 10, WHITE, bold=True, after=0)
    S["ji"] = doc.style("CB2 JobOrg", BF, 8.8, "E3EFFC", italic=True, after=2)
    S["jb"] = doc.style("CB2 JobText", BF, 8.6, WHITE, after=3, line=1.2)
    av = avatar(os.path.join(out_dir, "avatar-creative-b.png"), "E6EEF8", "7FA3D0")

    def hdr():
        doc.P(S["name"], D["name"].split(" ")[0]); doc.P(S["name"], D["name"].split(" ")[1]); doc.P(S["ttl"], D["title"])
        doc.P(S["ah"], "About me"); doc.P(S["at"], D["summary"])

    def photo():
        if doc.photo: doc.picture(av, 138, align="center")
        else:
            S["mono"] = doc.style("CB2 Monogram", HF, 64, OLIVE2, bold=True, align="center", spacing=3)
            doc.P(S["mono"], "".join(w[0] for w in D["name"].split(" ")))

    def side():
        doc.P(S["lh"], "Contact")
        for (lab, val), col in zip(contact_lines(D)[:3], [TERRA, OLIVE, "5A6A80"]): doc.P(S["lt"], ("●  ", {"color": col}), val)
        doc.P(S["lh"], "Skills")
        for n, p in D["skills"][:4]: doc.P(S["lt"], "-  " + n)
        doc.P(S["lh"], "Language")
        for lang, p, lvl in D["languages"]: doc.P(S["lt"], "-  " + lang + " (" + lvl.lower() + ")")
        doc.P(S["lh"], "References")
        for n, role, ph in D["references"]: doc.P(S["lt"], (n, {"bold": True}), "  " + ph)

    def right():
        doc.P(S["rh"], "Education")
        for e in D["education"]: doc.P(S["yr"], e["dates"]); doc.P(S["jt"], e["degree"]); doc.P(S["ji"], e["school"])
        doc.P(S["rh"], "Experience")
        for j in D["jobs"]:
            doc.P(S["yr"], j["dates"]); doc.P(S["jt"], j["title"]); doc.P(S["ji"], j["org"] + ", " + j["place"])
            doc.P(S["jb"], j["bullets"][0])

    grid(doc, [A, B, C], [
        {"h": 214, "cells": [{"span": 2, "fill": OLIVE, "pad": (30, 30, 20), "fn": hdr}, {"fill": SAND, "v": "center", "fn": photo}]},
        {"h": doc.PH - 232, "rule": "atLeast", "cells": [{"fill": GREYBG, "pad": (4, 26, 14), "fn": side}, {"span": 2, "fill": TERRA, "pad": (4, 26, 26), "fn": right}]}])


@design("minimal-a")
def minimal_a(doc, D, out_dir):
    """Lots of white: a very tracked name over a pastel mint highlight, lowercase tagline, serif body, tracked headings, mint skill bars."""
    MINT, INK, GREY = "D3EBDD", "222222", "5A5A5A"
    HF, BF = doc.font("Century Gothic", "Corbel", "Calibri"), doc.font("Georgia", "Cambria", "Times New Roman")
    W = doc.PW - 2 * 62
    doc.page_setup(48, 30, 62, 62)
    S = dict(datefont=BF, datesize=9, datecolor=INK, bulcolor=INK)
    S["name"] = doc.style("MN Name", HF, 25, INK, spacing=9, caps=True, align="center", after=4, left=4, right=4)
    S["ttl"] = doc.style("MN Title", BF, 11, INK, spacing=1.2, align="center", after=18)
    S["h"] = doc.style("MN Head", HF, 10.5, INK, bold=True, spacing=5, caps=True, before=18, after=8, keep=True)
    S["t"] = doc.style("MN Text", BF, 9.3, INK, after=4, line=1.35)
    S["yr"] = doc.style("MN Year", BF, 9.3, INK, bold=True, before=0, after=0)
    S["job"] = doc.style("MN Job", BF, 9.3, INK, bold=True, after=0)
    S["org"] = doc.style("MN Role", BF, 9.3, INK, after=1)
    S["bul"] = doc.style("MN Bullet", BF, 9.3, INK, after=1, left=9, first=-9, line=1.3)
    S["sl"] = doc.style("MN SkillLabel", BF, 9.3, INK, after=0, before=3)
    S["foot"] = doc.style("MN Footer", BF, 9, INK, align="center", before=24, after=0, top=(MINT, 2.0, 10))
    doc.P(S["name"], D["name"], shade=MINT); doc.P(S["ttl"], "•  " + D["title"].lower() + "  •")
    grid(doc, [W * 0.512, W * 0.488], [{"cells": [
        {"pad": (0, 0, 22), "fn": lambda: [doc.P(S["h"], "About me"), doc.P(S["t"], D["summary"])]},
        {"fn": lambda: [doc.P(S["h"], "Education")] + [x for e in D["education"] for x in (doc.P(S["t"], e["dates"] + "  •  " + e["school"]), doc.P(S["t"], e["degree"]))]}]}])
    doc.P(S["h"], "Experience")

    def jobrow(j):
        def a(): doc.P(S["yr"], j["dates"].split("–")[0].strip().split(" ")[-1])

        def b():
            doc.P(S["job"], j["org"]); doc.P(S["org"], j["title"])
            for x in j["bullets"]: doc.P(S["bul"], ("•", None), ("\t", None), x)
        return {"cells": [{"fn": a}, {"fn": b}]}

    grid(doc, [58.0, W - 58.0], [jobrow(j) for j in D["jobs"]])
    doc.P(S["h"], "Skills")

    def skills(items):
        def f():
            for n, p in items:
                doc.P(S["sl"], n); bar(doc, 200, p, MINT, "F0F5F2", 6)
        return f

    grid(doc, [W * 0.512, W * 0.488], [{"cells": [{"fn": skills(D["skills"][:3])}, {"fn": skills(D["skills"][3:6])}]}])
    doc.P(S["foot"], D["phone"] + "  •  " + D["email"] + "  •  " + D["web"])


@design("minimal-b")
def minimal_b(doc, D, out_dir):
    """Quiet typographic page: serif name, hairlines, spaced small-caps headings, a date column and one muted accent."""
    INK, GREY, ACC, RULE = "1F1F1F", "6A6A6A", "9C5B43", "D8D8D8"
    HF = BF = doc.font("Georgia", "Cambria", "Times New Roman")
    SANS = doc.font("Century Gothic", "Corbel", "Calibri")
    doc.page_setup(60, 40, 72, 72)
    S = dict(datefont=BF, datesize=9, datecolor=GREY, bulcolor=ACC)
    S["name"] = doc.style("MM Name", HF, 26, INK, spacing=2, after=2)
    S["ttl"] = doc.style("MM Title", SANS, 8.5, ACC, spacing=4, caps=True, after=6)
    S["con"] = doc.style("MM Contact", BF, 9, GREY, after=14, bottom=(RULE, 0.75, 12))
    S["h"] = doc.style("MM Head", SANS, 8.5, INK, bold=True, spacing=4, caps=True, before=20, after=8, keep=True)
    S["t"] = doc.style("MM Text", BF, 9.5, INK, after=5, line=1.35)
    S["dt"] = doc.style("MM Date", SANS, 8, GREY, spacing=0.5, after=0)
    S["job"] = doc.style("MM Job", BF, 10, INK, bold=True, after=0)
    S["org"] = doc.style("MM Org", BF, 9.3, GREY, italic=True, after=2)
    S["bul"] = doc.style("MM Bullet", BF, 9.3, INK, after=2, left=10, first=-10, line=1.3)
    doc.P(S["name"], D["name"]); doc.P(S["ttl"], D["title"])
    doc.P(S["con"], D["email"] + "    " + D["phone"] + "    " + D["location"])
    doc.P(S["h"], "Profile"); doc.P(S["t"], D["summary"])
    doc.P(S["h"], "Experience")

    def row(date, title, org, bullets):
        return {"cells": [{"fn": lambda: doc.P(S["dt"], date)},
                          {"fn": lambda: [doc.P(S["job"], title), doc.P(S["org"], org)] + [doc.P(S["bul"], ("–", {"color": ACC}), ("\t", None), b) for b in bullets]}]}

    grid(doc, [104.0, doc.PW - 144 - 104.0], [row(j["dates"], j["title"], j["org"] + ", " + j["place"], j["bullets"]) for j in D["jobs"]])
    doc.P(S["h"], "Education")
    grid(doc, [104.0, doc.PW - 144 - 104.0], [row(e["dates"], e["degree"], e["school"] + ", " + e["place"], []) for e in D["education"]])
    doc.P(S["h"], "Skills"); doc.P(S["t"], "  /  ".join(n for n, p in D["skills"]))



def main(argv):
    import tempfile
    if "--list" in argv:
        print("\n".join(sorted(DESIGNS))); return
    if "--list-photo" in argv:                          # the designs that show a photo placeholder (they have a photo-free variant)
        print("\n".join(sorted(PHOTO_DESIGNS))); return
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 2: sys.exit(__doc__)
    name, out = args
    if name not in DESIGNS: sys.exit("unknown design %r; try --list" % name)
    if os.path.exists(out) and "--overwrite" not in argv: sys.exit("refusing to overwrite %s (pass --overwrite)" % out)
    data = for_design(name)
    doc = Doc(local_fonts="--local-fonts" in argv, page=A4 if "--a4" in argv else LETTER, photo="--no-photo" not in argv)
    assets = os.path.join(tempfile.gettempdir(), "resume-design-avatars"); os.makedirs(assets, exist_ok=True)   # silhouette PNGs are only needed while the job runs
    DESIGNS[name](doc, data, assets)
    if doc.fresh:                                        # the design ended with a table: its trailing empty paragraph must not inherit a heading's border
        doc.c("para.reset"); doc.c("para.style", style="Normal"); doc.c("format.resetChar")
    print(json.dumps(doc.script(out)))


if __name__ == "__main__":
    main(sys.argv)
