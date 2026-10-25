"""ATS-friendly résumé rebuilt LIVE in an open ONLYOFFICE document, in 4 visible stages.

    python3 -I resume_live.py OUTDIR            # writes OUTDIR/s1_styles.json ... s4_rest.json
    for s in s1_styles s2_header s3_experience s4_rest; do
        python3 -I ../tools/ooc.py "/abs/path/Open Doc.docx" OUTDIR/$s.json
    done

Stage 2 REPLACES the whole document body — only run it on a document the user asked to rebuild, and tell
them the file on disk keeps the old version until they save. Replace the RESUME data; the sample is fictional.
Layout: Letter, 0.6"/0.5" margins, Calibri 10.5, navy all-caps Heading 1 with bottom rule, bold job title with
right-tab dates, italic employer line, navy bullets, linked email/profile.
"""
import json, os, sys

RESUME = {
    "name": "ALEX MORGAN",
    "headline": "Instructional Designer  |  Corporate Trainer  |  Project Coordinator",
    "location": "Portland, OR, USA",
    "email": "alex.morgan@example.com",
    "profile": "linkedin.com/in/example",
    "summary": ("Instructional designer with 8+ years of experience creating and delivering training for adult "
                "learners in 3 industries. Builds blended courses, coaches new trainers, and coordinates "
                "cross-team projects from kickoff to launch."),
    "competencies": [
        ("Training", ["Instructional Design", "Needs Analysis", "Workshop Facilitation", "Coaching", "E-Learning"]),
        ("Management", ["Project Coordination", "Budget Tracking", "Stakeholder Communication", "Scheduling"]),
        ("Tools", ["Articulate 360", "LMS Administration", "Microsoft 365", "Canva"]),
    ],
    "jobs": [
        {"title": "Senior Instructional Designer", "dates": "Jan 2021 – Present",
         "org": "Example Learning Co.  •  Portland, OR",
         "bullets": ["Designed 12 blended onboarding courses used by 400+ new hires per year.",
                     "Coached 6 new trainers through observation, co-delivery and feedback.",
                     "Cut course update time by moving content into a shared template library."]},
        {"title": "Corporate Trainer", "dates": "Jun 2017 – Dec 2020",
         "org": "Sample Manufacturing Inc.  •  Salem, OR",
         "bullets": ["Delivered safety and systems training to 25–40 staff per month.",
                     "Wrote the site training manual and maintained training records for audits."]},
    ],
    "earlier": [("Customer Service Supervisor", "Demo Telecom, Eugene, OR", "2012 – 2017",
                 "Promoted twice in 3 years, from Representative to Supervisor.")],
    "education": [("Bachelor of Science, Education", "Example State University, Corvallis, OR", "2012")],
    "certifications": [("Certified Professional in Talent Development (CPTD)", "ATD", "2022")],
    "extra": [("Languages: ", "English (Native) • Spanish (Intermediate)")],
}

NAVY, GRAY = "#1F3864", "#404040"
TAB = 10512  # right tab at text width in twips: 12240 - 2 * 864 (0.6" side margins)

# Units: font sizes in HALF-points, spacing/indents/tabs/margins in twips (20 per pt), borders in 1/8 pt.
STAGE1 = r'''
var doc = Api.GetDocument();
doc.RemoveSelection();
var sec = doc.GetSections()[0];
sec.SetPageSize(12240, 15840);
sec.SetPageMargins(864, 720, 864, 720);
var navy = Api.Color("%(navy)s"), gray = Api.Color("%(gray)s");
var normal = doc.GetStyle("Normal");
var ntp = normal.GetTextPr(), npp = normal.GetParaPr();
ntp.SetFontFamily("Calibri"); ntp.SetFontSize(21); ntp.SetColor(Api.Color("#000000"));
npp.SetSpacingBefore(0); npp.SetSpacingAfter(0); npp.SetSpacingLine(240, "auto");
function border(pp) {
  try { pp.SetBottomBorder("single", 6, 1, navy); } catch (e) { pp.SetBottomBorder("single", 6, 1, 31, 56, 100); }
}
var h1 = doc.GetStyle("Heading 1");
var htp = h1.GetTextPr(), hpp = h1.GetParaPr();
htp.SetFontFamily("Calibri"); htp.SetFontSize(23); htp.SetBold(true); htp.SetCaps(true); htp.SetColor(navy); htp.SetSpacing(10);
hpp.SetSpacingBefore(140); hpp.SetSpacingAfter(50); hpp.SetSpacingLine(240, "auto"); hpp.SetKeepNext(true); border(hpp);
function mk(name, tp, pp) { var s = doc.CreateStyle(name, "paragraph"); s.SetBasedOn(normal); tp(s.GetTextPr()); pp(s.GetParaPr()); }
mk("Resume Name", function(t){ t.SetFontSize(44); t.SetBold(true); t.SetColor(navy); }, function(p){ p.SetJc("center"); });
mk("Resume Headline", function(t){ t.SetFontSize(23); t.SetBold(true); t.SetColor(gray); }, function(p){ p.SetJc("center"); p.SetSpacingAfter(20); });
mk("Resume Contact", function(t){ t.SetFontSize(20); }, function(p){ p.SetJc("center"); p.SetSpacingAfter(40); });
mk("Resume Body", function(t){}, function(p){ p.SetJc("both"); p.SetSpacingAfter(40); });
mk("Job Title", function(t){ t.SetFontSize(22); t.SetBold(true); }, function(p){ p.SetSpacingBefore(70); p.SetKeepNext(true); p.SetTabs([%(tab)d], ["right"]); });
mk("Job Org", function(t){ t.SetItalic(true); t.SetColor(gray); }, function(p){ p.SetSpacingAfter(30); p.SetKeepNext(true); });
mk("Resume Bullet", function(t){}, function(p){ p.SetSpacingAfter(20); p.SetIndLeft(300); p.SetIndFirstLine(-220); });
mk("Resume Line", function(t){}, function(p){ p.SetSpacingAfter(30); p.SetTabs([%(tab)d], ["right"]); });
return "styles ready";
''' % {"navy": NAVY, "gray": GRAY, "tab": TAB}

HELPERS = r'''
var doc = Api.GetDocument();
doc.RemoveSelection();
function isEmpty(p) { return p.GetText().replace(/[\r\n]/g, "") === ""; }  // empty paragraphs read "\r\n", not ""
function bulletLevel() {  // reuse the list from an earlier stage so all bullets share one definition
  var ps = doc.GetAllParagraphs();
  for (var i = 0; i < ps.length; i++) { var n = ps[i].GetNumbering(); if (n) return n; }
  var lvl = doc.CreateNumbering("bullet").GetLevel(0);
  lvl.SetTemplateType("bullet", "•");
  lvl.GetTextPr().SetColor(Api.Color("%(navy)s"));
  lvl.GetParaPr().SetIndLeft(300); lvl.GetParaPr().SetIndFirstLine(-220);
  lvl.SetSuff("tab");
  return lvl;
}
var LVL = null;
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
  if (style === "Resume Bullet") { if (!LVL) LVL = bulletLevel(); p.SetNumbering(LVL); }
  doc.Push(p);
}
function run(items) { for (var i = 0; i < items.length; i++) add(items[i][0], items[i][1]); }
''' % {"navy": NAVY}

def P(style, *parts):
    return [style, [{"t": x[1], "b": True} if isinstance(x, tuple) else {"t": x} for x in parts]]

r, B = RESUME, "•"
HEADER = [P("Resume Name", r["name"]), P("Resume Headline", r["headline"]),
          P("Resume Contact", f"  {B}  ".join([r["location"], r["email"], r["profile"]])),
          P("Heading 1", "Professional Summary"), P("Resume Body", r["summary"]),
          P("Heading 1", "Core Competencies")] + \
         [P("Resume Line", ("b", label + ": "), f" {B} ".join(items)) for label, items in r["competencies"]]
EXPERIENCE = [P("Heading 1", "Professional Experience")]
for j in r["jobs"]:
    EXPERIENCE += [P("Job Title", f"{j['title']}\t{j['dates']}"), P("Job Org", j["org"])] + \
                  [P("Resume Bullet", b) for b in j["bullets"]]
REST = []
if r["earlier"]:
    REST.append(P("Heading 1", "Earlier Experience"))
    for title, org, dates, note in r["earlier"]:
        REST.append(P("Resume Line", ("b", title), f", {org}\t{dates}"))
        if note:
            REST.append(P("Resume Bullet", note))
REST.append(P("Heading 1", "Education"))
REST += [P("Resume Line", ("b", d), f" — {s}\t{y}") for d, s, y in r["education"]]
if r["certifications"]:
    REST.append(P("Heading 1", "Certifications"))
    REST += [P("Resume Line", ("b", n), f" — {i}\t{y}") for n, i, y in r["certifications"]]
if r["extra"]:
    REST.append(P("Heading 1", "Additional"))
    REST += [P("Resume Line", ("b", label), text) for label, text in r["extra"]]

LINKS = r'''
var links = %s;
for (var L = 0; L < links.length; L++) { var hits = doc.Search(links[L][0], true); if (hits.length) hits[0].AddHyperlink(links[L][1], ""); }
''' % json.dumps([[r["email"], "mailto:" + r["email"]], [r["profile"], "https://www." + r["profile"]]])

def content(items, clear=False, finish=""):
    js = HELPERS + ("doc.RemoveAllElements();\n" if clear else "")
    js += "var before = doc.GetElementsCount();\nrun(" + json.dumps(items, ensure_ascii=False) + ");\n"
    if clear:  # RemoveAllElements leaves one empty paragraph at the top
        js += 'var f = doc.GetElement(0); if (f && f.GetClassType() === "paragraph" && isEmpty(f) && doc.GetElementsCount() > 1) doc.RemoveElement(0);\n'
    return js + finish + "return {added: doc.GetElementsCount() - before, total: doc.GetElementsCount()};"

out = sys.argv[1] if len(sys.argv) > 1 else "."
os.makedirs(out, exist_ok=True)
for name, code in {"s1_styles": STAGE1, "s2_header": content(HEADER, clear=True),
                   "s3_experience": content(EXPERIENCE), "s4_rest": content(REST, finish=LINKS)}.items():
    json.dump([["word_write_macro", {"code": code}]], open(os.path.join(out, name + ".json"), "w"))
print("wrote s1_styles s2_header s3_experience s4_rest to", out)
