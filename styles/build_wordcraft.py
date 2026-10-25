"""Build a styled sample document or résumé in WordCraft: prints a `wordcraft-cli run --script` job (JSON).

    python3 -I build_wordcraft.py STYLE doc|resume /abs/out.docx [--local-fonts] > job.json
    wordcraft-cli run --script job.json            # writes out.docx (and out.dotx, a template of the same style)

STYLE is a key of styles.json (traditional, elegant, clean, professional, academic, modern, stylish, creative).
`doc` is a one-to-two page report using Title, Heading 1/2, body, bullets and a quote; `resume` is the ATS-safe
single-column layout (no tables or text boxes). Replace the sample text in content.py with real content.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content
from resolve import resolve

args = [a for a in sys.argv[1:] if not a.startswith("--")]
style_name, kind, out = args[0], args[1], args[2]
S = resolve(style_name, portable="--local-fonts" not in sys.argv)
HF, BF = S["font"]["heading"], S["font"]["body"]
C, SZ, B, H, T = S["color"], S["size"], S["body"], S["heading"], S["title"]
cmds = []


def c(cmd, **params):
    cmds.append({"command": cmd, "params": params} if params else cmd)


def chr_(font, size, color, bold=False, italic=False, caps=False, spacing=0):
    d = {"font": font, "fontCs": font, "size": size, "sizeCs": size, "color": color}
    if bold: d["bold"] = True
    if italic: d["italic"] = True
    if caps: d["caps"] = True
    if spacing: d["spacing"] = spacing
    return d


def border(side, color, width, space=1):
    return {side: {"style": "single", "width": width, "color": color, "space": space}}


def new_style(name, chr=None, para=None):
    c("styles.create", name=name, basedOn="Normal")
    c("styles.modify", style=name, **({"chr": chr} if chr else {}), **({"para": para} if para else {}))


def rule(h, color):
    if h["rule"] == "bottom": return border("bottom", color, 1)
    if h["rule"] == "left": return border("left", color, 3, space=6)
    return None


first = [True]
BULLET = [None]


def para(style, text=None, runs=None, bullet=False):
    if not first[0]:
        c("text.newParagraph")
    first[0] = False
    c("para.style", style=style)
    c("para.set", props={"numbering": {"level": 0, "num": BULLET[0] if bullet else 0}})
    for bold, t in (runs or [(False, text)]):
        if bold:
            c("format.bold", value=True)
        c("text.insert", text=t)
        if bold:
            c("format.resetChar")


def define_bullets(color):
    c("list.define", levels=[{"format": "bullet", "text": "•", "alignedAt": 4, "indentAt": 18, "follow": "tab",
                              "tabAt": 18, "color": color}], apply=True, name="Style Bullets")
    c("para.style", style="Normal")
    BULLET[0] = 1  # list.define on a blank template returns num 1 (verified, WordCraft 0.10.0)


if kind == "doc":
    m = S["margins_in"]
    c("layout.margins", top=m[0] * 72, bottom=m[1] * 72, left=m[3 - 1] * 72, right=m[3] * 72)
    c("styles.modify", style="Normal", chr=chr_(BF, SZ["body"], C["text"]),
      para={"spaceBefore": 0, "spaceAfter": B["after"], "align": B["align"], "indentFirst": B["first_indent"],
            "lineSpacing": {"rule": "multiple", "value": B["line"]}})
    hp = {"spaceBefore": H["before"], "spaceAfter": H["after"], "keepNext": True, "align": H["align"], "indentFirst": 0}
    if rule(H, C["accent"]): hp["borders"] = rule(H, C["accent"])
    c("styles.modify", style="Heading 1", chr=chr_(HF, SZ["h1"], C["heading"], H["bold"], H["italic"], H["caps"], H["spacing"]),
      para=dict(hp, lineSpacing={"rule": "multiple", "value": 1.0}))
    c("styles.modify", style="Heading 2", chr=chr_(HF, SZ["h2"], C["heading"], True, H["italic"]),
      para={"spaceBefore": max(H["before"] * 0.6, 0), "spaceAfter": 3, "keepNext": True, "align": "left", "indentFirst": 0,
            "lineSpacing": {"rule": "multiple", "value": 1.0}})
    tp = {"align": T["align"], "spaceAfter": 4, "indentFirst": 0, "lineSpacing": {"rule": "multiple", "value": 1.0}}
    if T["rule"] == "bottom": tp["borders"] = border("bottom", C["accent"], 1.5, space=4)
    new_style("Doc Title", chr=chr_(HF, SZ["title"], C["heading"], T["bold"], False, T["caps"]), para=tp)
    new_style("Doc Subtitle", chr=chr_(BF, SZ["body"], C["muted"]),
              para={"align": T["align"], "spaceAfter": 14, "indentFirst": 0, "lineSpacing": {"rule": "multiple", "value": 1.0}})
    new_style("Doc Quote", chr=chr_(BF, SZ["body"], C["muted"], italic=True),
              para={"indentLeft": 24, "indentFirst": 0, "spaceBefore": 4, "spaceAfter": 10, "align": "left",
                    "borders": border("left", C["accent"], 2.5, space=8)})
    new_style("Doc Bullet", para={"indentFirst": 0, "spaceAfter": 3, "align": "left"})
    c("para.style", style="Doc Bullet")
    define_bullets(C["accent"])
    for kind_, val in content.DOC:
        if kind_ == "title": para("Doc Title", val)
        elif kind_ == "subtitle": para("Doc Subtitle", val)
        elif kind_ == "h1": para("Heading 1", val)
        elif kind_ == "h2": para("Heading 2", val)
        elif kind_ == "p": para("Normal", val)
        elif kind_ == "quote": para("Doc Quote", val)
        elif kind_ == "bullets":
            for b in val: para("Doc Bullet", b, bullet=True)
    c("file.properties", title="Style sample: " + style_name, author="Sample Author", subject=S["summary"])
else:
    R, RS = content.RESUME, S["resume"]
    m = RS["margins_in"]
    width = 612 - (m[2] + m[3]) * 72
    c("layout.margins", top=m[0] * 72, bottom=m[1] * 72, left=m[2] * 72, right=m[3] * 72)
    bs = RS["body_size"]
    c("styles.modify", style="Normal", chr=chr_(BF, bs, C["text"]),
      para={"spaceBefore": 0, "spaceAfter": 0, "align": "left", "indentFirst": 0, "lineSpacing": {"rule": "multiple", "value": 1.0}})
    hp = {"spaceBefore": 8, "spaceAfter": 3, "keepNext": True, "align": "left", "indentFirst": 0}
    if rule(H, C["accent"]): hp["borders"] = rule(H, C["accent"])
    c("styles.modify", style="Heading 1", chr=chr_(HF, min(SZ["h1"], bs + 2.5), C["heading"], H["bold"], H["italic"], H["caps"], H["spacing"]), para=hp)
    new_style("Resume Name", chr=chr_(HF, RS["name_size"], C["heading"], True), para={"align": RS["name_align"], "spaceAfter": 1, "indentFirst": 0})
    new_style("Resume Headline", chr=chr_(BF, bs + 1, C["muted"], bold=True), para={"align": RS["name_align"], "spaceAfter": 1, "indentFirst": 0})
    new_style("Resume Contact", chr=chr_(BF, bs, C["text"]), para={"align": RS["name_align"], "spaceAfter": 3, "indentFirst": 0})
    new_style("Resume Body", para={"spaceAfter": 2, "align": "left", "indentFirst": 0})
    new_style("Job Title", chr=chr_(BF, bs + 0.5, C["text"], bold=True),
              para={"spaceBefore": 4, "keepNext": True, "indentFirst": 0, "tabs": [{"pos": width, "align": "right", "leader": "none"}]})
    new_style("Job Org", chr=chr_(BF, bs, C["muted"], italic=True), para={"spaceAfter": 1.5, "keepNext": True, "indentFirst": 0})
    new_style("Resume Bullet", para={"spaceAfter": 1, "indentFirst": 0, "align": "left"})
    new_style("Resume Line", para={"spaceAfter": 1.5, "indentFirst": 0, "tabs": [{"pos": width, "align": "right", "leader": "none"}]})
    c("para.style", style="Resume Bullet")
    define_bullets(C["accent"])
    para("Resume Name", R["name"])
    para("Resume Headline", R["headline"])
    para("Resume Contact", "  •  ".join([R["location"], R["email"], R["profile"]]))
    para("Heading 1", "Professional Summary")
    para("Resume Body", R["summary"])
    para("Heading 1", "Core Competencies")
    for label, items in R["competencies"]:
        para("Resume Line", runs=[(True, label + ": "), (False, " • ".join(items))])
    para("Heading 1", "Professional Experience")
    for j in R["jobs"]:
        para("Job Title", f"{j['title']}\t{j['dates']}")
        para("Job Org", j["org"])
        for b in j["bullets"]:
            para("Resume Bullet", b, bullet=True)
    para("Heading 1", "Education")
    for d, s, y in R["education"]:
        para("Resume Line", runs=[(True, d), (False, f" — {s}\t{y}")])
    para("Heading 1", "Certifications")
    for n, i, y in R["certifications"]:
        para("Resume Line", runs=[(True, n), (False, f" — {i}\t{y}")])
    c("select.text", text=R["email"]);   c("insert.link", url="mailto:" + R["email"])
    c("select.text", text=R["profile"]); c("insert.link", url="https://www." + R["profile"])
    c("file.properties", title=R["name"] + " - Resume", author=R["name"], subject=R["headline"])

json.dump({"template": "blank", "commands": cmds, "save": [out]}, sys.stdout)
