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
    "name": "Alex Morgan",
    "headline": "Landscape Designer  |  Nursery Manager  |  Estimator",
    "location": "Portland, OR, USA",
    "email": "alex.morgan@example.com",
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
