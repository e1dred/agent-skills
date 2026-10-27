"""ATS-friendly résumé for WordCraft: prints a `wordcraft-cli run --script` job (JSON) on stdout.

    python3 -I resume_ats.py /abs/path/resume.docx /abs/path/resume.pdf > job.json
    wordcraft-cli run --script job.json

Replace the RESUME data below; the layout code does not need to change. The sample person is fictional.
Layout: Letter, 0.6" side / 0.5" top-bottom margins, Calibri 10.5, centred navy name, navy all-caps
section headings (restyled Heading 1, so ATS parsers see real headings) with a bottom rule, bold job
title with right-aligned dates on a tab stop, italic employer line, navy bullets, clickable email/profile.
"""
import json, sys

RESUME = {
    "name": "ALEX MORGAN",
    "headline": "Landscape Designer  |  Nursery Manager  |  Estimator",
    "location": "Portland, OR, USA",
    "email": "jane.doe@example.com",
    "profile": "linkedin.com/in/example",          # shown text; linked as https://www.<profile>
    "summary": (
        "Landscape designer with 9 years of experience planning residential gardens and running a retail "
        "nursery. Drafts planting plans, prices projects accurately, and schedules crews and suppliers "
        "from first sketch to final walkthrough."),
    "competencies": [
        ("Design", ["Site Planning", "Plant Selection", "Drainage Layouts", "Sketching", "Seasonal Color"]),
        ("Operations", ["Cost Estimating", "Inventory Control", "Supplier Relations", "Crew Scheduling"]),
        ("Tools", ["Vectorworks", "Spreadsheets", "Point-of-Sale Systems", "Irrigation Software"]),
    ],
    "jobs": [
        {"title": "Senior Landscape Designer", "dates": "Jan 2021 – Present",
         "org": "Sample Garden Studio  •  Portland, OR",
         "bullets": ["Designed 40 residential planting plans per year, from small courtyards to half-acre lots.",
                     "Trained 3 junior designers to draft plans, estimate costs and run client walkthroughs.",
                     "Cut estimate turnaround from five days to two with a reusable pricing sheet."]},
        {"title": "Nursery Manager", "dates": "Jun 2017 – Dec 2020",
         "org": "Demo Plant Nursery  •  Salem, OR",
         "bullets": ["Managed stock of 2,000 plant varieties and ordered from 15 growers each season.",
                     "Introduced a seasonal planting calendar that reduced unsold stock by 18%."]},
    ],
    "earlier": [  # one line each; optional note becomes a bullet
        ("Crew Lead", "Example Lawn & Garden, Eugene, OR", "2012 – 2017",
         "Led a crew of six on installation and maintenance jobs."),
    ],
    "education": [("Associate of Applied Science, Horticulture", "Example Community College, Corvallis, OR", "2011")],
    "certifications": [("Certified Landscape Professional (sample certificate)", "Example Trade Association", "2022")],
    "extra": [("Volunteer: ", "Community garden coordinator, weekend workshops for beginners")],
}

NAVY, GRAY = "1F3864", "404040"
TAB = 525  # right tab = text width at 0.6" side margins (612 - 2*43.2)
BULLET_NUM = 1  # list.define on a blank template returns num 1 (verified, WordCraft 0.10.0)

cmds = []
def c(cmd, **params):
    cmds.append({"command": cmd, "params": params} if params else cmd)

def style(name, chr=None, para=None):
    c("styles.create", name=name, basedOn="Normal")
    c("styles.modify", style=name, **({"chr": chr} if chr else {}), **({"para": para} if para else {}))

first = [True]
def para(style_name, text=None, runs=None, bullet=False):
    if not first[0]:
        c("text.newParagraph")
    first[0] = False
    c("para.style", style=style_name)
    c("para.set", props={"numbering": {"level": 0, "num": BULLET_NUM if bullet else 0}})
    for bold, t in (runs or [(False, text)]):
        if bold:
            c("format.bold", value=True)  # never set bold False: direct formatting would override the style
        c("text.insert", text=t)
        if bold:
            c("format.resetChar")

c("layout.margins", top=36, bottom=36, left=43.2, right=43.2)
c("styles.modify", style="Normal",
  chr={"font": "Calibri", "fontCs": "Calibri", "size": 10.5, "sizeCs": 10.5, "color": "000000"},
  para={"spaceBefore": 0, "spaceAfter": 0, "lineSpacing": {"rule": "multiple", "value": 1.0}})
c("styles.modify", style="Heading 1",
  chr={"font": "Calibri", "size": 11.5, "bold": True, "caps": True, "color": NAVY},
  para={"spaceBefore": 7, "spaceAfter": 2.5, "keepNext": True,
        "borders": {"bottom": {"style": "single", "width": 1, "color": NAVY, "space": 1}}})
style("Resume Name", chr={"size": 22, "bold": True, "color": NAVY}, para={"align": "center"})
style("Resume Headline", chr={"size": 11.5, "bold": True, "color": GRAY}, para={"align": "center", "spaceAfter": 1})
style("Resume Contact", chr={"size": 10}, para={"align": "center", "spaceAfter": 2})
style("Resume Body", para={"spaceAfter": 2, "align": "justify"})
style("Job Title", chr={"bold": True, "size": 11},
      para={"spaceBefore": 3.5, "keepNext": True, "tabs": [{"pos": TAB, "align": "right", "leader": "none"}]})
style("Job Org", chr={"italic": True, "color": GRAY}, para={"spaceAfter": 1.5, "keepNext": True})
style("Resume Bullet", para={"spaceAfter": 1})
style("Resume Line", para={"spaceAfter": 1.5, "tabs": [{"pos": TAB, "align": "right", "leader": "none"}]})
c("para.style", style="Resume Bullet")  # styles.create applied each new style to this paragraph; define the list here
c("list.define", levels=[{"format": "bullet", "text": "•", "alignedAt": 4, "indentAt": 15,
                          "follow": "tab", "tabAt": 15, "color": NAVY}], apply=True, name="Resume Bullets")
c("para.style", style="Normal")

r = RESUME
B = "  •  "
para("Resume Name", r["name"])
para("Resume Headline", r["headline"])
para("Resume Contact", B.join([r["location"], r["email"], r["profile"]]))

para("Heading 1", "Professional Summary")
para("Resume Body", r["summary"])
para("Heading 1", "Core Competencies")
for label, items in r["competencies"]:
    para("Resume Line", runs=[(True, label + ": "), (False, " • ".join(items))])

para("Heading 1", "Professional Experience")
for j in r["jobs"]:
    para("Job Title", f"{j['title']}\t{j['dates']}")
    para("Job Org", j["org"])
    for b in j["bullets"]:
        para("Resume Bullet", b, bullet=True)

if r["earlier"]:
    para("Heading 1", "Earlier Experience")
    for title, org, dates, note in r["earlier"]:
        para("Resume Line", runs=[(True, title), (False, f", {org}\t{dates}")])
        if note:
            para("Resume Bullet", note, bullet=True)

para("Heading 1", "Education")
for degree, school, year in r["education"]:
    para("Resume Line", runs=[(True, degree), (False, f" — {school}\t{year}")])
if r["certifications"]:
    para("Heading 1", "Certifications")
    for name, issuer, year in r["certifications"]:
        para("Resume Line", runs=[(True, name), (False, f" — {issuer}\t{year}")])
if r["extra"]:
    para("Heading 1", "Additional")
    for label, text in r["extra"]:
        para("Resume Line", runs=[(True, label), (False, text)])

# Links last: select.text keeps the visible text and turns it into the link (verified).
c("select.text", text=r["email"]);   c("insert.link", url="mailto:" + r["email"])
c("select.text", text=r["profile"]); c("insert.link", url="https://www." + r["profile"])
c("file.properties", title=r["name"].title() + " - Resume", author=r["name"].title(), subject=r["headline"])

json.dump({"template": "blank", "commands": cmds, "save": sys.argv[1:] or ["resume.docx"]}, sys.stdout)
