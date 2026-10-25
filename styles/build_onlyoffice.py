"""Build a styled sample document or résumé in ONLYOFFICE: prints a calls.json for tools/ooc.py (headless new docx).

    python3 -I build_onlyoffice.py STYLE doc|resume|cv /abs/out.docx [--paper=a4|letter] [--local-fonts] [--pdf] > calls.json
    python3 -I ../onlyoffice/tools/ooc.py new:docx calls.json        # writes out.docx

To restyle a document that is open in the editor instead, run the same macro through `ooc.py "/abs/Open.docx"`
(live): change the last call and drop `RemoveAllElements`. STYLE is a key of styles.json. Replace the sample text in
content.py with real content. Units in the macro: font sizes in half-points, spacing/indents/margins in twips
(20 per pt), border size in 1/8 pt.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content
from resolve import resolve

args = [a for a in sys.argv[1:] if not a.startswith("--")]
style_name, kind, out = args[0], args[1], args[2]
PAPER = next((a.split("=", 1)[1].lower() for a in sys.argv if a.startswith("--paper=")), "a4" if kind == "cv" else "letter")
PW, PH = (11906, 16838) if PAPER == "a4" else (12240, 15840)   # twips
S = resolve(style_name, portable="--local-fonts" not in sys.argv)
HF, BF = S["font"]["heading"], S["font"]["body"]
C, SZ, B, H, T, RS = S["color"], S["size"], S["body"], S["heading"], S["title"], S["resume"]
tw = lambda pt: int(round(pt * 20))
hx = lambda c: "#" + c

m = RS["margins_in"] if kind in ("resume", "cv") else S["margins_in"]          # [top, bottom, left, right] inches
TOP, BOT, LEFT, RIGHT = [int(round(v * 1440)) for v in m]
WIDTH = PW - LEFT - RIGHT
BS = RS["body_size"] if kind in ("resume", "cv") else SZ["body"]

PRE = r'''
var doc = Api.GetDocument();
doc.RemoveSelection();
var sec = doc.GetSections()[0];
sec.SetPageSize(%(pw)d, %(ph)d);
sec.SetPageMargins(%(left)d, %(top)d, %(right)d, %(bot)d);
function col(h) { return Api.Color(h); }
function border(pp, side, size, space, color) {
  var fn = {bottom: "SetBottomBorder", left: "SetLeftBorder"}[side];
  try { pp[fn]("single", size, space, color); } catch (e) {}
}
function mk(name, tp, pp) { var s = doc.CreateStyle(name, "paragraph"); s.SetBasedOn(doc.GetStyle("Normal")); tp(s.GetTextPr()); pp(s.GetParaPr()); return s; }
function text(t, font, size, color, o) {
  t.SetFontFamily(font); t.SetFontSize(Math.round(size * 2)); t.SetColor(col(color));
  o = o || {};
  if (o.bold !== undefined) t.SetBold(o.bold);
  if (o.italic !== undefined) t.SetItalic(o.italic);
  if (o.caps) t.SetCaps(true);
  if (o.spacing) t.SetSpacing(o.spacing);
}
var normal = doc.GetStyle("Normal");
text(normal.GetTextPr(), "%(bf)s", %(bs)s, "%(ctext)s");
var npp = normal.GetParaPr();
npp.SetSpacingBefore(0); npp.SetSpacingAfter(%(after)d); npp.SetSpacingLine(%(line)d, "auto");
npp.SetJc("%(jc)s"); npp.SetIndFirstLine(%(first)d);
function para(pp, o) {
  pp.SetIndFirstLine(0); pp.SetSpacingLine(240, "auto");
  pp.SetSpacingBefore(o.before || 0); pp.SetSpacingAfter(o.after || 0);
  pp.SetJc(o.jc || "left"); if (o.keep) pp.SetKeepNext(true);
}
var h1 = doc.GetStyle("Heading 1");
text(h1.GetTextPr(), "%(hf)s", %(h1size)s, "%(chead)s", {bold: %(hbold)s, italic: %(hital)s, caps: %(hcaps)s, spacing: %(hspc)d});
para(h1.GetParaPr(), {before: %(hbefore)d, after: %(hafter)d, jc: "%(hjc)s", keep: true});
%(hrule)s
var h2 = doc.GetStyle("Heading 2");
text(h2.GetTextPr(), "%(hf)s", %(h2size)s, "%(chead)s", {bold: true, italic: %(hital)s});
para(h2.GetParaPr(), {before: %(h2before)d, after: 60, jc: "left", keep: true});
'''

DOC_STYLES = r'''
var tt = mk("Doc Title", function(t){ text(t, "%(hf)s", %(tsize)s, "%(chead)s", {bold: %(tbold)s, caps: %(tcaps)s}); },
  function(p){ para(p, {after: 80, jc: "%(tjc)s"}); %(trule)s });
mk("Doc Subtitle", function(t){ text(t, "%(bf)s", %(bs)s, "%(cmuted)s"); }, function(p){ para(p, {after: 280, jc: "%(tjc)s"}); });
mk("Doc Quote", function(t){ text(t, "%(bf)s", %(bs)s, "%(cmuted)s", {italic: true}); },
  function(p){ para(p, {before: 80, after: 200}); p.SetIndLeft(480); border(p, "left", 20, 6, col("%(caccent)s")); });
mk("Doc Bullet", function(t){}, function(p){ para(p, {after: 60}); p.SetIndLeft(360); p.SetIndFirstLine(-260); });
'''

RESUME_STYLES = r'''
mk("Resume Name", function(t){ text(t, "%(hf)s", %(nsize)s, "%(chead)s", {bold: true}); }, function(p){ para(p, {after: 20, jc: "%(njc)s"}); });
mk("Resume Headline", function(t){ text(t, "%(bf)s", %(bs1)s, "%(cmuted)s", {bold: true}); }, function(p){ para(p, {after: 20, jc: "%(njc)s"}); });
mk("Resume Contact", function(t){ text(t, "%(bf)s", %(bs)s, "%(ctext)s"); }, function(p){ para(p, {after: 60, jc: "%(njc)s"}); });
mk("Resume Body", function(t){}, function(p){ para(p, {after: 40}); });
mk("Job Title", function(t){ text(t, "%(bf)s", %(bs05)s, "%(ctext)s", {bold: true}); }, function(p){ para(p, {before: 80, keep: true}); p.SetTabs([%(width)d], ["right"]); });
mk("Job Org", function(t){ text(t, "%(bf)s", %(bs)s, "%(cmuted)s", {italic: true}); }, function(p){ para(p, {after: 30, keep: true}); });
mk("Resume Bullet", function(t){}, function(p){ para(p, {after: 20}); p.SetIndLeft(360); p.SetIndFirstLine(-260); });
mk("Resume Line", function(t){}, function(p){ para(p, {after: 30}); p.SetTabs([%(width)d], ["right"]); });
'''

HELPERS = r'''
function isEmpty(p) { return p.GetText().replace(/[\r\n]/g, "") === ""; }
var LVL = null;
function bulletLevel() {
  var lvl = doc.CreateNumbering("bullet").GetLevel(0);
  lvl.SetTemplateType("bullet", "•");
  lvl.GetTextPr().SetColor(col("%(caccent)s"));
  lvl.GetParaPr().SetIndLeft(360); lvl.GetParaPr().SetIndFirstLine(-260);
  lvl.SetSuff("tab");
  return lvl;
}
function add(style, parts) {
  var p = Api.CreateParagraph();
  p.SetStyle(style);
  for (var i = 0; i < parts.length; i++) {
    var seg = parts[i], r = Api.CreateRun();
    if (seg.b) r.SetBold(true);
    var bits = seg.t.split("\t");
    for (var k = 0; k < bits.length; k++) { if (k > 0) r.AddTabStop(); if (bits[k]) r.AddText(bits[k]); }
    p.AddElement(r);
  }
  if (style === "Doc Bullet" || style === "Resume Bullet") { if (!LVL) LVL = bulletLevel(); p.SetNumbering(LVL); }
  doc.Push(p);
}
function run(items) { for (var i = 0; i < items.length; i++) add(items[i][0], items[i][1]); }
doc.RemoveAllElements();
'''


def P(style, *parts):
    return [style, [{"t": x[1], "b": True} if isinstance(x, tuple) else {"t": x} for x in parts]]


items = []
if kind == "doc":
    for k, v in content.DOC:
        if k == "title": items.append(P("Doc Title", v))
        elif k == "subtitle": items.append(P("Doc Subtitle", v))
        elif k == "h1": items.append(P("Heading 1", v))
        elif k == "h2": items.append(P("Heading 2", v))
        elif k == "p": items.append(P("Normal", v))
        elif k == "quote": items.append(P("Doc Quote", v))
        elif k == "bullets": items += [P("Doc Bullet", b) for b in v]
    links = []
elif kind == "cv":
    R = content.CV
    items = [P("Resume Name", R["name"]), P("Resume Headline", R["headline"]), P("Resume Contact", R["address"]),
             P("Resume Contact", "  \u2022  ".join([R["phone"], R["email"]])),
             P("Heading 1", "Profile"), P("Resume Body", R["profile"]), P("Heading 1", "Work experience")]
    for j in R["jobs"]:
        items += [P("Job Title", f"{j['title']}\t{j['dates']}"), P("Job Org", j["org"])] + [P("Resume Bullet", b) for b in j["bullets"]]
    items.append(P("Heading 1", "Education and training"))
    for d, s, y in R["education"]:
        items += [P("Job Title", f"{d}\t{y}"), P("Job Org", s)]
    items += [P("Heading 1", "Languages"), P("Resume Line", ("b", "Mother tongue: "), R["languages"]["mother"])]
    items += [P("Resume Line", ("b", l + ": "), f"listening {a}, reading {b}, speaking {c}, writing {d} (CEFR)") for l, a, b, c, d in R["languages"]["other"]]
    items.append(P("Heading 1", "Digital skills"))
    items += [P("Resume Line", ("b", l + ": "), t) for l, t in R["digital"]]
    items.append(P("Heading 1", "Certificates"))
    items += [P("Resume Line", ("b", n), f" \u2014 {i}\t{y}") for n, i, y in R["certificates"]]
    items += [P("Heading 1", "Interests"), P("Resume Body", R["interests"])]
    links = [[R["email"], "mailto:" + R["email"]]]
else:
    R = content.RESUME
    items = [P("Resume Name", R["name"]), P("Resume Headline", R["headline"]),
             P("Resume Contact", "  •  ".join([R["location"], R["email"], R["profile"]])),
             P("Heading 1", "Professional Summary"), P("Resume Body", R["summary"]), P("Heading 1", "Core Competencies")]
    items += [P("Resume Line", ("b", l + ": "), " • ".join(i)) for l, i in R["competencies"]]
    items.append(P("Heading 1", "Professional Experience"))
    for j in R["jobs"]:
        items += [P("Job Title", f"{j['title']}\t{j['dates']}"), P("Job Org", j["org"])] + [P("Resume Bullet", b) for b in j["bullets"]]
    items.append(P("Heading 1", "Education"))
    items += [P("Resume Line", ("b", d), f" — {s}\t{y}") for d, s, y in R["education"]]
    items.append(P("Heading 1", "Certifications"))
    items += [P("Resume Line", ("b", n), f" — {i}\t{y}") for n, i, y in R["certifications"]]
    links = [[R["email"], "mailto:" + R["email"]], [R["profile"], "https://www." + R["profile"]]]


def rule_js(h, var, pfx):
    if h["rule"] == "bottom": return 'border(%s, "bottom", %d, 1, col("%s"));' % (var, 8 if pfx == "t" else 8, hx(C["accent"]))
    if h["rule"] == "left": return 'border(%s, "left", 24, 6, col("%s"));' % (var, hx(C["accent"]))
    return ""


fmt = dict(
    pw=PW, ph=PH, left=LEFT, right=RIGHT, top=TOP, bot=BOT, bf=BF, hf=HF, bs=BS, bs1=BS + 1, bs05=BS + 0.5,
    after=tw(B["after"]) if kind == "doc" else 0, line=int(round(240 * (B["line"] if kind == "doc" else 1.0))),
    jc={"justify": "both"}.get(B["align"], B["align"]) if kind == "doc" else "left", first=tw(B["first_indent"]) if kind == "doc" else 0,
    ctext=hx(C["text"]), chead=hx(C["heading"]), cmuted=hx(C["muted"]), caccent=hx(C["accent"]),
    h1size=min(SZ["h1"], BS + 2.5) if kind != "doc" else SZ["h1"], h2size=SZ["h2"],
    hbold=str(H["bold"]).lower(), hital=str(H["italic"]).lower(), hcaps=str(H["caps"]).lower(), hspc=tw(H["spacing"]),
    hbefore=tw(8 if kind != "doc" else H["before"]), hafter=tw(3 if kind != "doc" else H["after"]), hjc="left" if kind != "doc" else H["align"],
    h2before=tw(max(H["before"] * 0.6, 0)), tsize=SZ["title"], tbold=str(T["bold"]).lower(), tcaps=str(T["caps"]).lower(), tjc=T["align"],
    nsize=RS["name_size"], njc=RS["name_align"], width=WIDTH,
)
fmt["hrule"] = rule_js(H, "h1.GetParaPr()", "h")
fmt["trule"] = 'border(p, "bottom", 12, 4, col("%s"));' % hx(C["accent"]) if T["rule"] == "bottom" else ""

code = PRE % fmt + (DOC_STYLES if kind == "doc" else RESUME_STYLES) % fmt + HELPERS % fmt
code += "run(" + json.dumps(items, ensure_ascii=False) + ");\n"
code += 'var f = doc.GetElement(0); if (f && f.GetClassType() === "paragraph" && isEmpty(f) && doc.GetElementsCount() > 1) doc.RemoveElement(0);\n'
if links:
    code += "var links = %s;\nfor (var L = 0; L < links.length; L++) { var hits = doc.Search(links[L][0], true); if (hits.length) hits[0].AddHyperlink(links[L][1], \"\"); }\n" % json.dumps(links)
code += 'return {elements: doc.GetElementsCount()};'
calls = [["word_write_macro", {"code": code}], ["save_document", {"path": out, "format": "docx"}]]
if "--pdf" in sys.argv:  # also render with ONLYOFFICE itself, for checking the look
    calls.append(["save_document", {"path": out[:-5] + ".pdf", "format": "pdf"}])
json.dump(calls, sys.stdout)
