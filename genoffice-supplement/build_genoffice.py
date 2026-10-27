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

STYLE_IDS = {"Normal": "Normal", "Heading 1": "Heading1", "Heading 2": "Heading2", "Doc Title": "DocTitle", "Doc Subtitle": "DocSubtitle",
             "Doc Quote": "DocQuote", "Doc Bullet": "DocBullet", "Doc Table": "DocTable", "Doc Figure": "DocFigure", "Doc Caption": "DocCaption"}

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
    sid = STYLE_IDS[name]
    op = {"op": "define_style", "styleId": sid, "name": name if sid.startswith("Doc") else None}
    if op["name"] is None: del op["name"]
    if sid.startswith("Doc"): op["basedOn"] = "Normal"
    if para: op["paragraph"] = para
    if run: op["run"] = run
    return op

def build(style, kind, o, out):
    P = planmod.make(style, kind, o)
    assert kind in ("doc", "report"), "only doc/report block types handled"
    parts, order = [], []   # order: (style, payload) per document block, in document order
    bl = P["blocks"]; n = 0
    def runs_html(b):
        return "".join("<strong>%s</strong>" % html.escape(r[1]) if r[0] is True else "<em>%s</em>" % html.escape(r[1]) if r[0] == "i" else html.escape(r[1]) for r in b["runs"])
    while n < len(bl):
        b = bl[n]
        if b["t"] == "p" and b["bullet"]:
            items = []
            while n < len(bl) and bl[n]["t"] == "p" and bl[n]["bullet"]:
                items.append(bl[n]); n += 1
            parts.append("<ul>%s</ul>" % "".join("<li>%s</li>" % runs_html(x) for x in items))
            order += [("Doc Bullet", "li")] * len(items); continue
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
    apply(out, [style_op(nm, p) for nm, p in P["styles"] if nm in STYLE_IDS])      # styles first: later ops cannot see them in the same batch
    ops, idx, tabs, figs, cols = [], 0, [], [], None
    for st, kd in order:
        if st == "columns": cols = (idx - 1, kd); continue       # section break goes after the previous block
        if st == "table": tabs.append((idx, kd)); idx += 1; continue
        if st == "figure":
            figs.append((idx, kd))
            ops.append({"op": "applyStyle", "target": {"blockIndexes": [idx]}, "styleId": STYLE_IDS[kd["caption_style"]]}); idx += 1; continue
        ops.append({"op": "applyStyle", "target": {"blockIndexes": [idx]}, "styleId": STYLE_IDS[st]}); idx += 1
    for ti, t in tabs:
        tgt = {"blockIndexes": [ti]}; ncol = len(t["rows"][0]); merged = bool(t.get("merge"))
        ops.append({"op": "setTableCellFormat", "target": tgt, "range": {"row": 0, "col": 0, "colEnd": ncol - 1}, "fill": "#" + t["fill"], "vAlign": "center"})
        ops.append({"op": "setTableCellFormat", "target": tgt, "borders": {"all": {"style": "single", "width": 0.5, "color": "#" + t["border"]}}})
        ops.append({"op": "setFont", "target": tgt, "fontFamily": P["font"]["body"], "fontSize": 9.5})
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
    return P, order

if __name__ == "__main__":
    pos, o = parse(sys.argv)
    style, kind, out = pos
    P, order = build(style, kind, o, out)
    print("built", out, "blocks:", len(order))
