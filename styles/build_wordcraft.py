"""Build a styled sample document, résumé, CV or paper in WordCraft: prints a `wordcraft-cli run --script` job (JSON).

    python3 -I build_wordcraft.py STYLE KIND /abs/out.docx [options] > job.json
    wordcraft-cli run --script job.json

STYLE: traditional elegant clean professional academic modern stylish creative   (see styles.json)
KIND:  doc | resume | cv | paper          (paper uses the academic style; add --format=apa|mla)
Options (all `--name=value`):
  --paper=letter|a4            page size (default letter; cv defaults to a4)
  --page-numbers=bottom-center|bottom-right|top-right      --header-text="Short title"
  --columns=2                  doc only: body in columns after the subtitle (newsletter feel)
  --photo=/abs/pic.png         resume/cv only (human-first, not ATS-safe)
  --layout=chronological|functional|combined              resume only
  --format=apa|mla             paper only
  --figure=sample|/abs/pic.png doc only: a captioned figure after the table (sample = styles/assets/sample-figure.png)
  --merged-table               doc only: add a merged title row to the table
  --footnotes                  doc/paper: one sample footnote
  --script=arabic|hebrew|japanese|chinese|korean   doc only: one sample sentence in that script (RTL handled)
  --extras                     paper only: abstract (APA), block quote, captioned table
  --local-fonts                allow fonts installed here but not shipped with Office
  --overwrite                  replace an existing out.docx (otherwise the script refuses)
Notes about ATS-safety and other cautions go to stderr. Replace the sample text in content.py with real content.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import make, parse_argv

style_name, kind, out, o, flags = parse_argv(sys.argv)
if os.path.exists(out) and "overwrite" not in flags:
    sys.exit("refusing to overwrite %s (pass --overwrite)" % out)
P = make(style_name, kind, o)
for n in P["notes"]:
    print("NOTE:", n, file=sys.stderr)
cmds = []


def c(cmd, **params):
    cmds.append({"command": cmd, "params": params} if params else cmd)


def rgb(h): return h.lstrip("#")


def translate(name, p):
    chr_, par = {}, {}
    if "font" in p: chr_.update(font=p["font"], fontCs=p["font"])
    if "size" in p: chr_.update(size=p["size"], sizeCs=p["size"])
    if "color" in p: chr_["color"] = rgb(p["color"])
    for k in ("bold", "italic", "caps"):
        if p.get(k): chr_[k] = True
    if p.get("spacing"): chr_["spacing"] = p["spacing"]
    if "before" in p: par["spaceBefore"] = p["before"]
    if "after" in p: par["spaceAfter"] = p["after"]
    if "align" in p: par["align"] = p["align"]
    if "indent_first" in p: par["indentFirst"] = p["indent_first"]
    if "indent_left" in p: par["indentLeft"] = p["indent_left"]
    if "line" in p: par["lineSpacing"] = {"rule": "multiple", "value": p["line"]}
    if p.get("keep_next"): par["keepNext"] = True
    if p.get("tab_right"): par["tabs"] = [{"pos": p["tab_right"], "align": "right", "leader": "none"}]
    b = {}
    if "border_bottom" in p: col, w, sp = p["border_bottom"]; b["bottom"] = {"style": "single", "width": w, "color": rgb(col), "space": sp}
    if "border_left" in p: col, w, sp = p["border_left"]; b["left"] = {"style": "single", "width": w, "color": rgb(col), "space": sp}
    if b: par["borders"] = b
    return chr_, par


pg = P["page"]
if P["paper"] == "a4": c("layout.size", name="A4")
t, b_, l, r = pg["margins"]
c("layout.margins", top=t, bottom=b_, left=l, right=r)

H, F = P["header"], P["footer"]
base_font = next((p["font"] for n, p in P["styles"] if n == "Normal"), None)
base_size = next((p["size"] for n, p in P["styles"] if n == "Normal"), 11)
if H:
    if H["number"] and not H["text"]:
        c("insert.pageNumber", position="top", align=H["align"])
    else:
        c("insert.header", text=H["text"])
        if H["number"]:
            c("caret.end"); c("insert.pageField")
        c("para.set", props={"align": H["align"]})
        c("insert.closeHeader")
if F:
    c("insert.pageNumber", position="bottom", align=F["align"])
for hf in ("Header", "Footer"):
    if (H or F) and base_font:
        c("styles.modify", style=hf, chr={"font": base_font, "fontCs": base_font, "size": base_size, "sizeCs": base_size, "color": "000000" if P["kind"] == "paper" else "555555"})

BUILTIN = {"Normal", "Heading 1", "Heading 2", "Heading 3"}
for name, p in P["styles"]:
    chr_, par = translate(name, p)
    if name not in BUILTIN:
        c("styles.create", name=name, basedOn="Normal")
    c("styles.modify", style=name, **({"chr": chr_} if chr_ else {}), **({"para": par} if par else {}))

bullet_style = next((n for n, _ in P["styles"] if n.endswith("Bullet")), None)
BULLET = [0]
if any(bk.get("bullet") for bk in P["blocks"]) and bullet_style:
    c("para.style", style=bullet_style)
    c("list.define", levels=[{"format": "bullet", "text": "•", "alignedAt": 4, "indentAt": 18, "follow": "tab", "tabAt": 18,
                              "color": rgb(P["bullet"]["color"])}], apply=True, name="Style Bullets")
    c("para.style", style="Normal")
    BULLET[0] = 1  # list.define on a blank template returns num 1 (verified, WordCraft 0.10.0)

first = [True]
pending_before = [0]
pending_break = [False]
prev_bullet = [False]
prev_script = [False]
STYLE_BEFORE = {n: p.get("before", 0) for n, p in P["styles"]}
STYLE_ALIGN = {n: p.get("align", "left") for n, p in P["styles"]}


def new_para():
    if not first[0]:
        c("text.newParagraph")
    first[0] = False


def type_runs(runs):
    for flag, text in runs:
        if flag is True: c("format.bold", value=True)       # never set bold False: direct formatting would override the style
        elif flag == "i": c("format.italic", value=True)
        c("text.insert", text=text)
        if flag: c("format.resetChar")


for blk in P["blocks"]:
    t_ = blk["t"]
    if t_ == "p":
        new_para()
        c("para.style", style=blk["style"])
        # a new paragraph inherits the previous paragraph's DIRECT properties, so set these explicitly every time
        props = {"spaceBefore": pending_before[0] or STYLE_BEFORE.get(blk["style"], 0), "pageBreakBefore": pending_break[0]}
        pending_before[0] = 0; pending_break[0] = False
        if blk["bullet"] or prev_bullet[0]:  # only touch numbering when needed: setting num 0 also drops the style's indents
            props["numbering"] = {"level": 0, "num": BULLET[0] if blk["bullet"] else 0}
        prev_bullet[0] = blk["bullet"]
        if blk.get("script"):
            # in a right-to-left paragraph "left" means the START edge, i.e. the right-hand side on the page
            props.update(bidi=bool(blk["rtl"]), align="left")
            prev_script[0] = True
        elif prev_script[0]:
            props.update(bidi=False, align=STYLE_ALIGN.get(blk["style"], "left")); prev_script[0] = False
        c("para.set", props=props)
        if blk.get("script"):
            f = blk["font"]
            c("format.set", props={"font": f, "fontCs": f, "fontEa": f})
            c("text.insert", text=blk["runs"][0][1]); c("format.resetChar")
        else:
            type_runs(blk["runs"])
    elif t_ == "spacer":
        pending_before[0] = blk["pt"]
    elif t_ == "pagebreak":
        pending_break[0] = True
    elif t_ == "columns":
        c("text.newParagraph")
        c("layout.columns", count=blk["n"], space=24, separator=True, apply="forward"); first[0] = True
    elif t_ == "photo":
        new_para()
        c("para.style", style=blk["style"])
        c("insert.picture", path=blk["path"], width=blk["w"], alt="Portrait photo")
    elif t_ == "figure":
        new_para(); c("para.style", style=blk["style"])
        c("insert.picture", path=blk["path"], width=blk["w"], alt=blk["alt"])
        c("text.newParagraph"); c("para.style", style=blk["caption_style"]); c("text.insert", text=blk["caption"])
    elif t_ == "table":
        new_para()
        rows = blk["rows"]; ncol = len(rows[0]); merged = bool(blk.get("merge"))
        c("insert.table", rows=len(rows), cols=ncol, style="Table Grid")
        for ri, row in enumerate(rows):
            for ci, cell in enumerate(row):
                c("para.style", style=blk["style"])
                if cell: c("text.insert", text=cell)
                if not (ri == len(rows) - 1 and ci == ncol - 1): c("caret.right")
        for _ in range(len(rows) - 1): c("caret.up")
        c("table.selectRow")
        if merged: c("table.merge"); c("table.selectRow")
        c("table.shading", color=rgb(blk["fill"]))
        c("format.set", props={"bold": True, "color": rgb(blk["text"])}); c("table.repeatHeader")
        if merged:
            c("para.set", props={"align": "center"})
            c("caret.down"); c("table.selectRow"); c("table.shading", color=rgb(blk["sub_fill"])); c("format.set", props={"bold": True})
        c("table.borders", color=rgb(blk["border"]), width=0.5)
        c("caret.docEnd"); first[0] = True

for text, url in P["links"]:
    c("select.text", text=text); c("insert.link", url=url)
for fn in P["footnotes"]:   # last: references.footnote leaves the caret inside the footnote; select.text finds the anchor wherever the caret is
    c("select.text", text=fn["anchor"]); c("caret.right"); c("references.footnote", text=fn["text"])
pr = P["props"]
c("file.properties", title=pr["title"], author=pr["author"], subject=pr["subject"])
json.dump({"template": "blank", "commands": cmds, "save": [out]}, sys.stdout)
