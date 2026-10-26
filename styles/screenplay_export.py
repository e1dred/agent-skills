"""Convert a plain-text script (the Fountain-like markup of this repo) to Fountain and Final Draft (.fdx) files. Standard library only.

    python3 -I screenplay_export.py --text=/abs/script.txt [--title= --author= --draft=] [--fountain=/abs/out.fountain] [--fdx=/abs/out.fdx]

It uses the same parser as the .docx builders (plan.py), so what you see in the formatted script is what is exported.
The .fountain file is plain text with the title-page keys; the .fdx is Final Draft's XML (Paragraph Types: Scene Heading, Action, Character,
Parenthetical, Dialogue, Transition, General; dual dialogue wrapped in <DualDialogue>). The .fdx was checked as well-formed XML and against
the structure Final Draft writes; it has NOT been opened in Final Draft itself. Overwrites nothing: it refuses an existing output file.
"""
import os, sys
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import make, parse_argv


def fountain(sp):
    out = []
    if sp["title"]: out.append("Title: " + sp["title"])
    if sp["credit"]: out.append("Credit: " + sp["credit"])
    if sp["author"]: out.append("Author: " + sp["author"])
    if sp["draft"]: out.append("Draft date: " + sp["draft"])
    if sp["contact"]: out.append("Contact:\n" + "\n".join("    " + l for l in sp["contact"]))
    out.append("")

    def emph(runs):
        return "".join(("**%s**" % t if f is True else "*%s*" % t if f == "i" else "_%s_" % t if f == "u" else t) for f, t in runs)

    def block(sub, dual=False):
        lines = []
        for k, v in sub:
            if k == "char": lines.append(v + (" ^" if dual else ""))
            elif k in ("paren", "more"): lines.append(v)
            else: lines.append(v)
        return "\n".join(lines)
    for k, v in sp["items"]:
        if k == "scene": out.append(v if v.split(".")[0] in ("INT", "EXT", "EST", "I/E", "INT/EXT") or v.startswith("INT./EXT") else "." + v)
        elif k == "dual": out.append(block(v[0])); out.append(block(v[1], True))
        elif k == "center": out.append(">" + v + "<")
        elif k in ("action", "trans", "act"): out.append(("> " + v) if k == "trans" and not v.endswith("TO:") else v)
        elif k in ("char", "paren", "dial", "more"):
            # re-join a dialogue block: a cue starts a block, following elements stay glued to it
            if k == "char": out.append(v)
            else: out[-1] = out[-1] + "\n" + v
    head, body = out[:out.index("")], out[out.index("") + 1:]
    return "\n".join(head) + "\n\n" + "\n\n".join(body) + "\n"


def fdx(sp):
    P = []

    def text(t, style=""):
        return '<Text%s>%s</Text>' % (' Style="%s"' % style if style else "", escape(t))

    def paragraph(kind, runs, extra=""):
        parts = "".join(text(t, {True: "Bold", "i": "Italic", "u": "Underline"}.get(f, "")) for f, t in (runs if isinstance(runs, list) else [(False, runs)]))
        return '<Paragraph Type="%s"%s>%s</Paragraph>' % (kind, extra, parts)
    TYPE = {"scene": "Scene Heading", "action": "Action", "char": "Character", "paren": "Parenthetical", "dial": "Dialogue", "trans": "Transition",
            "center": "Action", "act": "General", "more": "Parenthetical"}

    def runs_of(t):
        import re
        out = []
        for b in re.split(r"(\*\*[^*\n]+\*\*|\*[^*\n]+\*|_[^_\n]+_)", t):
            if b.startswith("**") and b.endswith("**") and len(b) > 4: out.append((True, b[2:-2]))
            elif len(b) > 2 and b[0] == b[-1] == "*": out.append(("i", b[1:-1]))
            elif len(b) > 2 and b[0] == b[-1] == "_": out.append(("u", b[1:-1]))
            elif b: out.append((False, b))
        return out
    for k, v in sp["items"]:
        if k == "dual":
            P.append("<Paragraph><DualDialogue>" + "".join(paragraph(TYPE[kk], runs_of(vv) if kk == "dial" else vv) for col in v for kk, vv in col) + "</DualDialogue></Paragraph>")
        elif k == "center": P.append(paragraph("Action", runs_of(v), ' Alignment="Center"'))
        elif k == "trans": P.append(paragraph("Transition", v))
        elif k == "act": P.append(paragraph("General", v, ' Alignment="Center"'))
        else: P.append(paragraph(TYPE[k], runs_of(v) if k in ("action", "dial") else v))
    tp = []
    for line in [sp["title"].upper(), "", sp["credit"], sp["author"], "", sp["draft"]]:
        tp.append('<Paragraph Alignment="Center"><Text>%s</Text></Paragraph>' % escape(line))
    for line in sp["contact"]:
        tp.append('<Paragraph Alignment="Left"><Text>%s</Text></Paragraph>' % escape(line))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n<FinalDraft DocumentType="Script" Template="No" Version="3">\n<Content>\n'
            + "\n".join(P) + '\n</Content>\n<TitlePage>\n<Content>\n' + "\n".join(tp) + '\n</Content>\n</TitlePage>\n</FinalDraft>\n')


if __name__ == "__main__":
    argv = [a for a in sys.argv if not a.startswith(("--fountain=", "--fdx="))]
    outs = {a.split("=", 1)[0][2:]: a.split("=", 1)[1] for a in sys.argv if a.startswith(("--fountain=", "--fdx="))}
    if not outs: sys.exit("give --fountain=/abs/out.fountain and/or --fdx=/abs/out.fdx")
    style, kind, out, o, flags = parse_argv(["x", "x", "screenplay", "/dev/null"] + argv[1:])
    sp = make("x", "screenplay", o)["sp"]
    for k, path in outs.items():
        if os.path.exists(path): sys.exit("refusing to overwrite " + path)
        with open(path, "w", encoding="utf-8") as f: f.write(fountain(sp) if k == "fountain" else fdx(sp))
        print("wrote", path)
