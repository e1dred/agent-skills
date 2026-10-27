"""Invented sample content used to show a style on a real-looking page. Nothing here describes a real person or organisation."""

DOC = [
    ("title", "Community Garden Programme: Quarterly Review"),
    ("subtitle", "Prepared for the Riverside Trust board  |  October 2026"),
    ("p", "This review summarises the third quarter of the community garden programme. It covers what was planted, who took part, "
          "and what the team recommends for the winter months. Figures are from the volunteer sign-in sheets and the seed log."),
    ("h1", "Background"),
    ("p", "The programme began with four raised beds and a shared tool shed. Since then it has grown to eleven beds, a compost area and a "
          "weekly open session. Volunteers range from first-time gardeners to retired growers who now lead the Saturday workshops."),
    ("h1", "What we did"),
    ("h2", "Spring planting"),
    ("p", "Seedlings were started in March and moved outside in May. Nearly everything survived the late frost because the beds "
          "were covered on the two coldest nights."),
    ("bullets", ["Beans, courgettes and salad leaves in the main beds",
                 "A herb border along the shed wall",
                 "Sunflowers along the fence for the school visit"]),
    ("h2", "Autumn workshops"),
    ("p", "Six workshops ran between September and October. Attendance averaged fourteen people, and the seed-saving evening "
          "was fully booked a week in advance."),
    ("h1", "Findings"),
    ("p", "Interest is highest on weekends and lowest on weekday mornings. The beds nearest the gate are the best tended, "
          "while the far corner needs a clearer path and a water point."),
    ("quote", "“We came for the tomatoes and stayed for the Saturday tea.”  — volunteer feedback card"),
    ("table", [["Month", "Workshops", "Attendees", "Seeds saved"], ["September", "3", "41", "18"], ["October", "3", "44", "27"]]),
    ("h1", "Next steps"),
    ("bullets", ["Lay a gravel path to the far corner before the first frost",
                 "Install a second water butt beside the compost area",
                 "Plan the winter programme: bulbs, pruning and tool-sharpening days"]),
    ("p", "The team will report back at the January meeting with costs and a volunteer rota."),
]

RESUME = {
    "name": "Jane Doe",
    "headline": "Landscape Designer  |  Nursery Manager  |  Estimator",
    "location": "Portland, OR, USA",
    "phone": "(555) 010-0100",
    "email": "jane.doe@example.com",
    "profile": "linkedin.com/in/example",
    "summary": ("Landscape designer with 9 years of experience planning residential gardens and running a retail nursery. "
                "Drafts planting plans, prices projects accurately, and schedules crews and suppliers from first sketch to final walkthrough."),
    "competencies": [
        ("Design", ["Site Planning", "Plant Selection", "Drainage Layouts", "Sketching", "Seasonal Color"]),
        ("Operations", ["Cost Estimating", "Inventory Control", "Supplier Relations", "Crew Scheduling"]),
        ("Tools", ["Vectorworks", "Spreadsheets", "Point-of-Sale Systems", "Irrigation Software"]),
    ],
    "jobs": [
        {"title": "Senior Landscape Designer", "dates": "Jan 2021 – Present", "org": "Sample Garden Studio  •  Portland, OR",
         "bullets": ["Designed 40 residential planting plans per year, from small courtyards to half-acre lots.",
                     "Trained 3 junior designers to draft plans, estimate costs and run client walkthroughs.",
                     "Cut estimate turnaround from five days to two with a reusable pricing sheet."]},
        {"title": "Nursery Manager", "dates": "Jun 2017 – Dec 2020", "org": "Demo Plant Nursery  •  Salem, OR",
         "bullets": ["Managed stock of 2,000 plant varieties and ordered from 15 growers each season.",
                     "Introduced a seasonal planting calendar that reduced unsold stock by 18%."]},
    ],
    "education": [("Associate of Applied Science, Horticulture", "Example Community College, Corvallis, OR", "2011")],
    "certifications": [("Certified Landscape Professional (sample certificate)", "Example Trade Association", "2022")],
}

CV = {
    "name": "Sam Rivera",
    "headline": "Environmental Project Coordinator",
    "address": "Example Street 12, 1000 Sampletown, Exampleland",
    "phone": "+00 000 000 000",
    "email": "sam.rivera@example.com",
    "profile": ("Project coordinator with 8 years of experience delivering river-restoration and urban-greening projects across "
                "three countries. Works comfortably between engineers, local authorities and volunteer groups, and writes the "
                "funding reports that keep projects running."),
    "jobs": [
        {"title": "Senior Project Coordinator", "dates": "03/2021 \u2013 present", "org": "Sample Rivers Foundation  \u2022  Sampletown, Exampleland",
         "bullets": ["Coordinated 12 restoration projects with a combined budget of EUR 2.4 million.",
                     "Led a team of five and managed relations with municipal partners and two national agencies.",
                     "Wrote four successful grant applications totalling EUR 850,000."]},
        {"title": "Project Officer", "dates": "09/2017 \u2013 02/2021", "org": "Demo Urban Greening Office  \u2022  Otherville, Exampleland",
         "bullets": ["Planned and monitored 30 pocket-park installations.",
                     "Introduced a shared monitoring spreadsheet used by six partner organisations."]},
    ],
    "education": [("MSc Environmental Management", "Example University of Technology, Sampletown", "2015 \u2013 2017"),
                  ("BSc Geography", "Sample State University, Otherville", "2012 \u2013 2015")],
    "languages": {"mother": "English",
                  "other": [("German", "C1", "C1", "B2", "B2"), ("French", "B1", "B1", "A2", "A2")]},
    "digital": [("Office", "word processing, spreadsheets, presentations"), ("Specialist", "QGIS, project-planning software, survey tools")],
    "certificates": [("Prince2 Foundation (sample certificate)", "Example Training Body", "2019")],
    "interests": "Trail running, community gardening, volunteering at a river clean-up group",
}

RESUME_EXTRA = {
    "skill_groups": [
        ("Planting design", ["Designed 40 residential planting plans per year, from small courtyards to half-acre lots.",
                             "Matched plant lists to soil, light and drainage, cutting replacement costs for clients."]),
        ("Estimating and project management", ["Cut estimate turnaround from five days to two with a reusable pricing sheet.",
                                               "Scheduled crews and suppliers from first sketch to final walkthrough."]),
        ("Training and customer service", ["Trained 3 junior designers to draft plans and run client walkthroughs.",
                                           "Reduced unsold nursery stock by 18% with a seasonal planting calendar."]),
    ],
    "highlights": ["40 residential planting plans per year", "Estimate turnaround cut from five days to two",
                   "Unsold nursery stock reduced by 18%"],
}

# Invented student paper. The sources are fictional; replace them with real ones.
PAPER = {
    "title": "Community Gardens and Neighbourhood Wellbeing",
    "author": "Jordan Morgan", "surname": "Morgan", "affiliation": "Example University",
    "course": "SOC 210: Urban Communities", "instructor": "Dr. Rowan Ellis", "date": "October 26, 2026",
    "body": [
        ("p", "Community gardens have become a common feature of mid-sized cities, yet their effect on the people who use them is still debated. "
              "This paper reviews two recent studies and argues that the clearest benefit is social rather than nutritional {c1}."),
        ("h1", "Background"),
        ("p", "Early work on urban gardening focused on food production and cost savings. More recent studies ask instead how shared growing spaces "
              "change the way neighbours know and trust one another {c2}."),
        ("h2", "Measuring wellbeing"),
        ("p", "Both studies rely on short surveys given at the start and end of a growing season. Respondents rate their sense of belonging, "
              "and the researchers compare gardeners with a matched group of non-gardening neighbours."),
        ("h1", "Discussion"),
        ("p", "The two studies agree on the direction of the effect and differ on its size. The larger effect appears where gardens run open weekly sessions, "
              "which suggests that the schedule matters as much as the soil {c1}."),
    ],
    "refs": [
        "Haddad, N., & Lindqvist, P. (2021). Shared plots and shared lives: Gardens in mid-sized cities. Journal of Example Studies, 12(3), 45\u201361.",
        "Okafor, T. (2022). Belonging by the bed: A seasonal survey of community gardeners. Example Press.",
    ],
    "cites": {"apa": {"c1": "(Haddad & Lindqvist, 2021)", "c2": "(Okafor, 2022)"},
              "mla": {"c1": "(Haddad and Lindqvist 52)", "c2": "(Okafor 88)"}},
    "mla_refs": [
        "Haddad, Nadia, and Per Lindqvist. \u201cShared Plots and Shared Lives: Gardens in Mid-Sized Cities.\u201d Journal of Example Studies, vol. 12, no. 3, 2021, pp. 45\u201361.",
        "Okafor, Tunde. Belonging by the Bed: A Seasonal Survey of Community Gardeners. Example Press, 2022.",
    ],
}

# Short sample sentences used to check right-to-left and CJK rendering. Have a native reader confirm the wording before you reuse it.
SCRIPTS = {
    "arabic": ("Arabic, right to left", "\u0647\u0630\u0627 \u0646\u0635 \u062a\u062c\u0631\u064a\u0628\u064a \u0642\u0635\u064a\u0631 \u064a\u0648\u0636\u062d \u0627\u062a\u062c\u0627\u0647 \u0627\u0644\u0643\u062a\u0627\u0628\u0629 \u0645\u0646 \u0627\u0644\u064a\u0645\u064a\u0646 \u0625\u0644\u0649 \u0627\u0644\u064a\u0633\u0627\u0631.", True),
    "hebrew": ("Hebrew, right to left", "\u05d6\u05d4\u05d5 \u05d8\u05e7\u05e1\u05d8 \u05dc\u05d3\u05d5\u05d2\u05de\u05d4 \u05e7\u05e6\u05e8 \u05e9\u05de\u05e8\u05d0\u05d4 \u05db\u05ea\u05d9\u05d1\u05d4 \u05de\u05d9\u05de\u05d9\u05df \u05dc\u05e9\u05de\u05d0\u05dc.", True),
    "japanese": ("Japanese", "\u3053\u308c\u306f\u3001\u65e5\u672c\u8a9e\u306e\u6587\u7ae0\u304c\u3069\u306e\u3088\u3046\u306b\u8868\u793a\u3055\u308c\u308b\u304b\u3092\u793a\u3059\u77ed\u3044\u30b5\u30f3\u30d7\u30eb\u3067\u3059\u3002", False),
    "chinese": ("Chinese (Simplified)", "\u8fd9\u662f\u4e00\u4e2a\u7b80\u77ed\u7684\u793a\u4f8b\uff0c\u7528\u6765\u5c55\u793a\u4e2d\u6587\u6587\u672c\u7684\u663e\u793a\u6548\u679c\u3002", False),
    "korean": ("Korean", "\uc774\uac83\uc740 \ud55c\uad6d\uc5b4 \ud14d\uc2a4\ud2b8\uac00 \uc5b4\ub5bb\uac8c \ud45c\uc2dc\ub418\ub294\uc9c0 \ubcf4\uc5ec \uc8fc\ub294 \uc9e7\uc740 \uc608\ubb38\uc785\ub2c8\ub2e4.", False),
}

# Extra blocks for papers (--extras): an abstract, a block quote and a captioned table.
PAPER_EXTRAS = {
    "abstract": ("This paper compares two recent studies of community gardens and argues that their clearest benefit is social. "
                 "It summarises how each study measured belonging, notes where the findings agree, and suggests that weekly open sessions "
                 "matter more than garden size."),
    "keywords": "community gardens, belonging, urban neighbourhoods",
    "quote": ("The garden gate is rarely locked, and that, more than the vegetables, seems to be the point: anyone may walk in, "
              "pick up a trowel, and be asked what they are growing."),
    "table_caption": ("Table 1", "Survey sample by group"),
    "table_rows": [["Group", "Respondents", "Mean belonging score"], ["Gardeners", "112", "4.1"], ["Neighbours", "102", "3.4"]],
}

# Invented manuscript (a short novel opening). Markup used by --text files too: a line "# Title" starts a chapter, a line "#" or "* * *" alone is a scene break,
# blank lines separate paragraphs, *word* is italic, a line "THE END" closes the book.
MANUSCRIPT = {
    "title": "Salt and Lantern Light",
    "author": "Rowan Tilby", "pen": "Rowan Tilby", "surname": "Tilby",
    "address": ["14 Example Row", "Harbourside, EX1 2AB, United Kingdom"],
    "phone": "(555) 010-0142", "email": "rowan.tilby@example.com",
    "text": """# Chapter One: The Last Boat

The ferry horn sounded twice, which meant the tide was turning and Ida had four minutes to decide whether she was leaving.

She stood on the quay with a suitcase that had belonged to her mother and a letter she had read so many times the folds had gone soft. Behind her, the lamp-lit windows of the village were going out one by one, as they always did at nine.

"You'll miss it," said a voice from the shadows. It was Mr. Penhallow, who mended nets and, as far as anyone knew, never slept. "The boat, I mean. Not the place. Nobody misses the place."

"I haven't decided," Ida said.

"Then the tide has decided for you." He nodded at the water, where a line of foam was already creeping back from the steps. "It does that. It's more patient than people, but it does it."

She laughed, and was surprised to hear herself.

#

By the time she climbed the lighthouse stairs the next morning, the question had changed. It was no longer *should I go?* but *what is this place hiding?*

The keeper's door stood open. Inside, a single lantern burned on the table, though the sun was already high, and beside it lay a key on a loop of blue thread.

"That wasn't there yesterday," Ida whispered.

Nobody answered. Somewhere below, the sea went on turning over its stones.

# Chapter Two: What the Tide Kept

The key fitted a door she had walked past all her life, a narrow hatch at the foot of the cliff that the village children dared one another to touch. It opened on the first try.

Beyond it, the passage smelled of rain and old rope. She counted forty steps down before the light from her lantern found the first of the shelves, and on the shelves, row after row, the lamps.

Hundreds of them. Each had a name painted on its base, and each one was lit.

Ida set her own lantern down very carefully. Then she began to read the names, and found her mother's on the ninth shelf, burning low.

THE END
""",
}

# Invented screenplay excerpt. Markup used by --text files too (a Fountain-like subset): a line starting INT. EXT. EST. INT./EXT. I/E (or a leading ".")
# is a scene heading; a line in capitals ending in "TO:" (or starting ">") is a transition; a block whose first line is a NAME IN CAPITALS followed by
# lines is a character cue with dialogue, and a line in (parentheses) inside it is a parenthetical; everything else is action. *word* is italic.
SCREENPLAY = {
    "title": "The Last Signal", "author": "Sam Whitlock",
    "contact": ["14 Example Row", "Harbourside, EX1 2AB", "(555) 010-0142", "sam.whitlock@example.com"],
    "draft": "First draft",
    "text": """FADE IN:

INT. RADIO STATION - NIGHT

A cramped room of dials and cold tea. One lamp. Rain on a tin roof. NORA VANCE (40s, sharp, tired) sits in front of a silent receiver, headphones round her neck.

The receiver crackles once. She does not move.

NORA
(without turning)
You're late.

A figure steps out of the dark: ELIAS (60s, a coat that has seen weather). He sets a battered case on the desk.

ELIAS
The road was closed. *Again.*

NORA
The road is always closed.

ELIAS
Then it is always late.

She almost smiles. The receiver crackles again, longer this time, a thread of a voice in the static.

RADIO (V.O.)
...calling any station... calling any...

Nora grabs the headphones. Elias opens the case and lifts out a small brass key.

NORA
Where did you get that?

ELIAS
(quietly)
Same place I got the news.

NORA
What news?

Elias looks at the receiver, then at her.

ELIAS
That you're not the only one still listening.

CUT TO:

EXT. CLIFF PATH - CONTINUOUS

Wind. A lantern swings from a post. Far below, a ship answers with three short blasts of its horn.

Nora comes running into frame and stops at the edge, breathless.

NORA
(into the dark)
I hear you!

The horn sounds again. Closer.

NORA
Come closer. Come *closer*.

FADE OUT.
""",
}


# Invented query letter and synopsis (companions of the manuscript sample). Replace with your own text.
QUERY = {
    "date": "October 26, 2026",
    "agent": ["Ms. Dana Example", "Example Literary Agency", "100 Sample Street", "Anytown, ST 00000"],
    "text": """Dear Ms. Example,

Ida has four minutes to decide whether to leave the island that never lets anyone leave. When a brass key appears in the lighthouse keeper's room on the morning after the last ferry, she follows it into a cave of burning lamps, each one named for a villager, and finds her mother's lamp burning low.

SALT AND LANTERN LIGHT is a 90,000-word fantasy novel for adult readers, in the vein of quiet, atmospheric island stories. It stands alone, with room for a sequel.

I have published short fiction in two small magazines and work as a ferry-timetable clerk, a job that has taught me a great deal about waiting. I would be glad to send the full manuscript or sample chapters.

Thank you for your time and consideration.""",
}

SYNOPSIS = {
    "text": """Ida Marsh is about to leave the island of Skerra for good when the tide, and a net-mender named Mr. Penhallow, persuade her to stay one more night. The next morning she finds a key on a loop of blue thread in the empty lighthouse keeper's room.

The key opens a hatch at the foot of the cliff, long a village dare. Behind it lies a passage of lit lamps, hundreds of them, each painted with a villager's name. Ida finds her mother's among them, burning low, and learns that the island keeps its people alive by tending their lamps. Whoever leaves takes a little of the island's light with them.

Ida must decide whether to leave and let her mother's lamp go out, or to take over the keeper's work that has kept the village safe for generations, and to learn what the island asks in return.""",
}

# Invented one-act play. Markup used by --text files too (see styles/README.md, "Stage play"): CHARACTERS block, SETTING:/TIME: lines, ACT ONE, SCENE 1,
# a paragraph in (parentheses) or any plain paragraph = stage direction, a NAME IN CAPITALS line followed by speech lines = a cue and its speech
# ((parenthetical) lines inside a speech are kept), BLACKOUT. / CURTAIN. / END OF PLAY close a scene or the play, *word* is italic.
STAGEPLAY = {
    "title": "Weather Station", "author": "Casey Larkin", "credit": "a play in one act", "draft": "First draft",
    "contact": ["14 Example Row", "Harbourside, EX1 2AB", "(555) 010-0142", "casey.larkin@example.com"],
    "text": """CHARACTERS
MIRA OKONKWO, 40s, the station keeper
DEV HALLORAN, 20s, her new assistant

SETTING: A weather station on a headland. One room: a desk, a barometer, a cold stove.

TIME: The present, late autumn.

ACT ONE

SCENE 1

(Evening. Rain on a tin roof. MIRA sits at the desk writing in a ledger. DEV enters, dripping, carrying a suitcase.)

MIRA
(without looking up)
You're early.

DEV
The bus was early. I only followed it.

MIRA
Nobody warned me you'd be young.

DEV
Nobody warned me you'd be *here*. The office said the station had been closed for years.

(MIRA closes the ledger and looks at him for the first time.)

MIRA
The office says a great many things. Put the case down. The floor is the only dry thing in this room, and it is not very dry.

DEV
(setting it down)
What do I do first?

MIRA
You learn to read the barometer. Then you learn to ignore it.

BLACKOUT.

SCENE 2

(Morning. The rain has stopped. DEV stands at the window with a mug. MIRA enters with a bundle of papers.)

DEV
There's a ship out there. It hasn't moved all night.

MIRA
(not looking)
It isn't a ship.

DEV
Then what is it?

MIRA
It's what the station is for.

(The lights fade slowly on the two of them, side by side at the window.)

CURTAIN.

END OF PLAY
""",
}
