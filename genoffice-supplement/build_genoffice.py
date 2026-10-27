"""Build a styled `doc` (and `report` if the plan has the same block types) with GenOffice from the app-neutral plan in ~/agent-skills/styles/plan.py.
Lives in agent-skills/genoffice-supplement; imports the app-neutral plan from ../styles/plan.py (read-only).

  PYTHONDONTWRITEBYTECODE=1 python3 build_genoffice.py STYLE KIND /abs/out.docx [--paper=a4] [--page-numbers=bottom-center] [--header-text=T] [--figure=sample] [--footnotes] [--merged-table]
"""
import json, os, subprocess, sys, html, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "styles"))
sys.dont_write_bytecode = True
import plan as planmod

def parse(argv):
    pos = [a for a in argv[1:] if not a.startswith("--")]
    o = {}
    for a in argv[1:]:
        if a.startswith("--"):
            k, _, v = a[2:].partition("=")
            o[k.replace("-", "_")] = v or True
    return pos, o

def go(*a, stdin=None):
    r = subprocess.run(["genoffice", *a, "--json"], capture_output=True, text=True)
    d = json.loads(r.stdout or "{}")
    if d.get("status") != "ok": sys.exit("genoffice %s failed: %s" % (a[:2], (r.stdout + r.stderr)[:600]))
    return d

def apply(path, ops):
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump(ops, f); f.close()
    return go("docs", "apply", path, "--ops", f.name)

_BASE_IDS = {"Normal": "Normal", "Heading 1": "Heading1", "Heading 2": "Heading2", "Doc Title": "DocTitle", "Doc Subtitle": "DocSubtitle",
             "Doc Quote": "DocQuote", "Doc Bullet": "DocBullet", "Doc Table": "DocTable", "Doc Figure": "DocFigure", "Doc Caption": "DocCaption"}

import re as _re
def sid(name):
    return _BASE_IDS.get(name) or _re.sub(r"\W", "", name)
STYLE_IDS = type("S", (), {"__getitem__": lambda self, k: sid(k), "__contains__": lambda self, k: True})()

def style_op(name, p):
    para, run = {}, {}
    if "align" in p: para["align"] = p["align"]
    if "before" in p: para["spaceBefore"] = p["before"]
    if "after" in p: para["spaceAfter"] = p["after"]
    if "line" in p: para["lineSpacing"] = p["line"]
    if "indent_left" in p: para["indentLeft"] = p["indent_left"]
    if "indent_first" in p: para["firstLineIndent"] = p["indent_first"]
    if "keep_next" in p: para["keepNext"] = bool(p["keep_next"])
    if "font" in p: run["fontFamily"] = p["font"]
    if "size" in p: run["fontSize"] = p["size"]
    if "color" in p: run["color"] = "#" + p["color"]
    for k in ("bold", "italic"):
        if k in p: run[k] = bool(p[k])
    if p.get("caps"): run["caps"] = True
    if p.get("tab_right"): para["tabs"] = [{"pos": "%dpt" % round(p["tab_right"]), "align": "right"}]
    style_id = sid(name)
    op = {"op": "define_style", "styleId": style_id, "name": name if style_id not in ("Normal", "Heading1", "Heading2") else None}
    if op["name"] is None: del op["name"]
    if style_id not in ("Normal", "Heading1", "Heading2"): op["basedOn"] = "Normal"
    if para: op["paragraph"] = para
    if run: op["run"] = run
    return op


def _border(side, spec):
    color, width, space = spec
    return '<w:%s w:val="single" w:sz="%d" w:space="%d" w:color="%s"/>' % (side, round(width * 8), round(space), color)

def post_process(out, P):
    """GenOffice's ops cannot set a coloured paragraph border, letter-spacing or a bullet colour, so patch styles.xml
    and numbering.xml of the finished .docx (a plain zip rewrite; Word and the other apps read the result normally)."""
    import zipfile, re, shutil
    styles = dict(P["styles"])
    ids = {n: sid(n) for n in styles if n != "Normal"}
    zin = zipfile.ZipFile(out); files = {n: zin.read(n) for n in zin.namelist()}; infos = {i.filename: i for i in zin.infolist()}; zin.close()
    st = files["word/styles.xml"].decode("utf-8")
    for name, style_id in ids.items():
        p = styles.get(name, {})
        m = re.search(r'<w:style [^>]*w:styleId="%s".*?</w:style>' % style_id, st, re.S)
        if not m: continue
        blk = m.group(0)
        bdr = "".join(_border(side, p["border_" + side]) for side in ("top", "left", "bottom", "right") if p.get("border_" + side))
        if bdr:
            blk = re.sub(r"(<w:pPr>.*?)(<w:(?:shd|tabs|spacing|ind|jc|outlineLvl)\b)", lambda mm: mm.group(1) + "<w:pBdr>" + bdr + "</w:pBdr>" + mm.group(2), blk, count=1, flags=re.S)
        if p.get("indent_first") == 0:   # define_style drops a zero first-line indent, so the style inherits Normal's (academic: 0.5 in); write it
            if "<w:ind " in blk:
                if "w:firstLine=" not in blk and "w:hanging=" not in blk:
                    blk = blk.replace("<w:ind ", '<w:ind w:firstLine="0" ', 1)
            else:
                blk = re.sub(r"(<w:pPr>.*?)(<w:(?:contextualSpacing|jc|outlineLvl)\b|</w:pPr>)", lambda mm: mm.group(1) + '<w:ind w:firstLine="0"/>' + mm.group(2), blk, count=1, flags=re.S)
        if p.get("spacing"):   # letter-spacing in twentieths of a point, goes before w:sz in rPr
            blk = blk.replace("<w:sz ", '<w:spacing w:val="%d"/><w:sz ' % round(p["spacing"] * 20), 1)
        st = st.replace(m.group(0), blk)
    files["word/styles.xml"] = st.encode("utf-8")
    if "word/numbering.xml" in files and P.get("bullet"):
        nx = files["word/numbering.xml"].decode("utf-8")
        nx = nx.replace('<w:rPr><w:rFonts w:ascii="Symbol"', '<w:rPr><w:color w:val="%s"/><w:rFonts w:ascii="Symbol"' % P["bullet"]["color"])
        files["word/numbering.xml"] = nx.encode("utf-8")
    tmp = out + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in files.items(): z.writestr(n, b)
    shutil.move(tmp, out)

def build(style, kind, o, out):
    P = planmod.make(style, kind, o)
    assert kind in ("doc", "report", "resume", "cv"), "only doc/report/resume/cv block types handled"
    parts, order = [], []   # order: (style, payload) per document block, in document order
    bl = P["blocks"]; n = 0
    def esc(t):
        return "<span data-tab></span>".join(html.escape(x) for x in t.split("\t"))   # a tab in the HTML input must be this span
    def runs_html(b):
        return "".join("<strong>%s</strong>" % esc(r[1]) if r[0] is True else "<em>%s</em>" % esc(r[1]) if r[0] == "i" else esc(r[1]) for r in b["runs"])
    while n < len(bl):
        b = bl[n]
        if b["t"] == "p" and b["bullet"]:
            items = []
            while n < len(bl) and bl[n]["t"] == "p" and bl[n]["bullet"]:
                items.append(bl[n]); n += 1
            parts.append("<ul>%s</ul>" % "".join("<li>%s</li>" % runs_html(x) for x in items))
            order += [(items[0]["style"], "li")] * len(items); continue
        if b["t"] == "columns":
            order.append(("columns", b))          # marker only, no block
        elif b["t"] == "p":
            tag = {"Heading 1": "h1", "Heading 2": "h2"}.get(b["style"], "p")
            parts.append("<%s>%s</%s>" % (tag, runs_html(b), tag)); order.append((b["style"], tag))
        elif b["t"] == "table":
            rows = b["rows"]
            th = "".join("<th>%s</th>" % html.escape(c) for c in rows[0])
            tb = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % html.escape(c) for c in r) for r in rows[1:])
            parts.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, tb)); order.append(("table", b))
        elif b["t"] == "figure":
            parts.append("<p>%s</p>" % html.escape(b["caption"])); order.append(("figure", b))
        n += 1
    tmp = tempfile.mkdtemp(); h = os.path.join(tmp, "in.html"); open(h, "w").write("\n".join(parts))
    go("create", "--type", "docx", "--from", h, "--out", out, "--force")
    apply(out, [style_op(nm, p) for nm, p in P["styles"]])      # styles first: later ops cannot see them in the same batch
    ops, idx, tabs, figs, cols = [], 0, [], [], None
    for st, kd in order:
        if st == "columns": cols = (idx - 1, kd); continue       # section break goes after the previous block
        if st == "table": tabs.append((idx, kd)); idx += 1; continue
        if st == "figure":
            figs.append((idx, kd))
            ops.append({"op": "applyStyle", "target": {"blockIndexes": [idx]}, "styleId": STYLE_IDS[kd["caption_style"]]}); idx += 1; continue
        ops.append({"op": "applyStyle", "target": {"blockIndexes": [idx]}, "styleId": STYLE_IDS[st]}); idx += 1
    styles_d = dict(P["styles"])
    for ti, t in tabs:
        tgt = {"blockIndexes": [ti]}; ncol = len(t["rows"][0]); merged = bool(t.get("merge"))
        if t.get("rich"):      # report tables: per-cell styles and status fills, optional widths, header row and grid
            ops.append({"op": "setTableCellFormat", "target": tgt, "borders": ({"all": {"style": "single", "width": 0.5, "color": "#" + t["border"]}} if t["grid"] else None), "vAlign": "center"})
            base = styles_d.get(t["style"], {})
            ops.append({"op": "setFont", "target": tgt, "fontFamily": base.get("font", P["font"]["body"]), "fontSize": base.get("size", 9.5), "color": "#" + base.get("color", "000000")})
            ops.append({"op": "setParagraphFormat", "target": tgt, "spaceBefore": int(base.get("before", 2) * 20), "spaceAfter": int(base.get("after", 2) * 20), "lineSpacing": 1.0})
            if t.get("widths"):
                for ci, fr in enumerate(t["widths"]):
                    ops.append({"op": "setTableCellFormat", "target": tgt, "range": {"row": 0, "col": ci}, "width": int(fr * P["width"] * 20)})
            if t["header"]:
                ops.append({"op": "setTableCellFormat", "target": tgt, "range": {"row": 0, "col": 0, "colEnd": ncol - 1}, "fill": "#" + t["fill"]})
            for key, (fill, tcol) in t.get("fills", {}).items():
                r_, c_ = map(int, key.split(","))
                ops.append({"op": "setTableCellFormat", "target": tgt, "range": {"row": r_, "col": c_}, "fill": "#" + fill})
            for ri, row in enumerate(t["rows"]):
                for ci, cell in enumerate(row):
                    if not cell: continue
                    cs = styles_d.get(t["cell_styles"][ri][ci], {}); f = {}
                    if cs.get("font"): f["fontFamily"] = cs["font"]
                    if cs.get("size"): f["fontSize"] = cs["size"]
                    if cs.get("color"): f["color"] = "#" + cs["color"]
                    if cs.get("bold"): f["bold"] = True
                    if cs.get("italic"): f["italic"] = True
                    if t["header"] and ri == 0: f.update(bold=True, color="#" + t["text"])
                    tcol = t.get("fills", {}).get("%d,%d" % (ri, ci), (None, None))[1]
                    if tcol: f.update(bold=True, color="#" + tcol)
                    if t["cell_styles"][ri][ci] != t["style"] or "bold" in f:
                        ops.append(dict({"op": "setMatchedFont", "text": cell, "target": tgt}, **f))
            continue
        ops.append({"op": "setTableCellFormat", "target": tgt, "range": {"row": 0, "col": 0, "colEnd": ncol - 1}, "fill": "#" + t["fill"], "vAlign": "center"})
        ops.append({"op": "setTableCellFormat", "target": tgt, "borders": {"all": {"style": "single", "width": 0.5, "color": "#" + t["border"]}}})
        ops.append({"op": "setFont", "target": tgt, "fontFamily": P["font"]["body"], "fontSize": 9.5})
        ops.append({"op": "setParagraphFormat", "target": tgt, "spaceBefore": 40, "spaceAfter": 40, "lineSpacing": 1.0})   # cell paragraphs otherwise take Normal's spacing
        ops.append({"op": "setMatchedFont", "text": t["rows"][0][0], "color": "#" + t["text"], "bold": True, "target": tgt})
        if merged:
            ops.append({"op": "mergeTableCells", "target": tgt, "range": {"row": 0, "col": 0, "colEnd": ncol - 1}})
            ops.append({"op": "setTableCellFormat", "target": tgt, "range": {"row": 1, "col": 0, "colEnd": ncol - 1}, "fill": "#" + t["sub_fill"]})
            for c in t["rows"][1]:
                ops.append({"op": "setMatchedFont", "text": c, "bold": True, "color": "#" + dict(P["styles"])["Normal"]["color"], "target": tgt})
        else:
            for c in t["rows"][0][1:]:
                ops.append({"op": "setMatchedFont", "text": c, "color": "#" + t["text"], "bold": True, "target": tgt})
    m = P["page"]["margins"]
    ops.append({"op": "set_page_setup", "paper": "A4" if P["paper"] == "a4" else "Letter",
                "margins": {"top": "%.0fpt" % m[0], "bottom": "%.0fpt" % m[1], "left": "%.0fpt" % m[2], "right": "%.0fpt" % m[3]}})
    if P.get("header"): ops.append({"op": "set_header_footer", "kind": "header", "text": P["header"]["text"] + ("  {PAGE}" if P["header"]["number"] else "")})
    if P.get("footer"): ops.append({"op": "set_header_footer", "kind": "footer", "text": "{PAGE}"})
    for fn in P["footnotes"]:
        d = go("docs", "read", out, "--full")
        blk = next(i["index"] for i in d["detail"]["items"] if fn["anchor"] in i.get("text", ""))
        ops.append({"op": "insert_footnote", "blockIndex": blk, "afterText": fn["anchor"], "text": fn["text"]})
    apply(out, ops)
    # figures after everything else (each insert shifts the block indexes behind it), last one first
    for idx_, f in reversed(figs):
        apply(out, [{"op": "insert_picture", "url": f["path"], "width": "%.0fpt" % f["w"], "height": "%.0fpt" % f["h"], "altText": f["alt"], "afterBlockIndex": idx_ - 1}])
    if cols:
        aft, b = cols
        apply(out, [{"op": "insert_section_break", "afterBlockIndex": aft, "type": "continuous"}])
        apply(out, [{"op": "set_page_setup", "section": 1, "columns": {"count": b["n"], "spacing": "24pt"}}])
    post_process(out, P)
    return P, order

if __name__ == "__main__":
    pos, o = parse(sys.argv)
    style, kind, out = pos
    P, order = build(style, kind, o, out)
    print("built", out, "blocks:", len(order))
