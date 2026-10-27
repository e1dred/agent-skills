"""Invented sample content for the redesigned résumés (every name, employer and number is made up; the names are the usual placeholders Jane Doe, John Doe, Richard Roe and Mary Major).

Richer than content.RESUME: skills with levels (for bars and gauges), languages, achievements, certifications,
references and links, so every layout has something to show. Replace it with real content for a real résumé.
"""
DATA = {
    "name": "Jane Doe",
    "title": "Landscape Designer",
    "tagline": "Gardens that look planned and cost what the estimate said.",
    "phone": "(555) 010-0100",
    "email": "jane.doe@example.com",
    "location": "Portland, OR",
    "web": "janedoe.example.com",
    "summary": ("Landscape designer with nine years of experience planning residential gardens and running a retail nursery. "
                "Drafts planting plans, prices projects accurately, and schedules crews and suppliers from first sketch to final walkthrough."),
    "jobs": [
        {"title": "Senior Landscape Designer", "org": "Sample Garden Studio", "place": "Portland, OR", "dates": "Jan 2021 – Present",
         "blurb": "A design-build studio for residential gardens in the Pacific Northwest.",
         "bullets": ["Designed 40 residential planting plans per year, from small courtyards to half-acre lots.",
                     "Trained three junior designers to draft plans, estimate costs and run client walkthroughs.",
                     "Cut estimate turnaround from five days to two with a reusable pricing sheet."]},
        {"title": "Nursery Manager", "org": "Demo Plant Nursery", "place": "Salem, OR", "dates": "Jun 2017 – Dec 2020",
         "blurb": "A family-run retail nursery with 2,000 plant varieties.",
         "bullets": ["Managed stock of 2,000 varieties and ordered from 15 growers each season.",
                     "Introduced a seasonal planting calendar that reduced unsold stock by 18%.",
                     "Hired and scheduled a seasonal team of eight."]},
        {"title": "Garden Technician", "org": "Example Landscape Crew", "place": "Eugene, OR", "dates": "Mar 2014 – May 2017",
         "blurb": "",
         "bullets": ["Installed beds, paths and drip irrigation on 120 residential sites.",
                     "Kept a job log that became the crew's standard handover sheet."]},
    ],
    "education": [
        {"degree": "A.A.S. Horticulture", "school": "Example Community College", "place": "Corvallis, OR", "dates": "2011 – 2013", "note": "Dean's list, two terms"},
        {"degree": "Certificate, Garden Design", "school": "Sample Design Institute", "place": "Portland, OR", "dates": "2016", "note": ""},
    ],
    "skills": [("Planting design", 90), ("Cost estimating", 85), ("Site planning", 80), ("Vectorworks", 75), ("Crew scheduling", 70), ("Client presentations", 85)],
    "skill_groups": [("Design", ["Site Planning", "Plant Selection", "Drainage Layouts", "Sketching", "Seasonal Color"]),
                     ("Operations", ["Cost Estimating", "Inventory Control", "Supplier Relations", "Crew Scheduling"]),
                     ("Tools", ["Vectorworks", "Spreadsheets", "Point-of-Sale Systems", "Irrigation Software"])],
    "languages": [("English", 100, "Native"), ("Spanish", 70, "Conversational"), ("French", 40, "Basic")],
    "achievements": [("Record season", "Sold out the spring plant sale two years running."),
                     ("Faster estimates", "Estimate turnaround cut from five days to two.")],
    "certs": [("Certified Landscape Professional (sample)", "Example Trade Association", "2022"),
              ("Irrigation Auditor (sample)", "Demo Water Institute", "2019")],
    "interests": ["Trail running", "Community gardening", "Seed saving", "Photography"],
    "references": [("Richard Roe", "Director, Sample Garden Studio", "(555) 010-0111"),
                   ("Mary Major", "Owner, Demo Plant Nursery", "(555) 010-0122")],
    "links": [("Website", "janedoe.example.com"), ("LinkedIn", "linkedin.com/in/example")],
    "publications": [("Native plants for small city gardens", "Example Garden Review, May 2021")],
    "volunteer": [{"title": "Volunteer Garden Lead", "org": "Example Community Garden", "dates": "2018 – Present",
                   "bullets": ["Organised monthly work parties for 25 volunteers.", "Raised $3,200 for a rain-water tank."]}],
}


def for_design(design):
    """Jane Doe for the "a" layouts, John Doe for the "b" layouts (same content, generic names that cannot be a real person)."""
    import copy
    d = copy.deepcopy(DATA)
    if design.endswith("-b"):
        d["name"] = "John Doe"; d["email"] = "john.doe@example.com"; d["web"] = "johndoe.example.com"
        d["references"] = [("Mary Major", "Director, Sample Garden Studio", "(555) 010-0111"), ("Richard Roe", "Owner, Demo Plant Nursery", "(555) 010-0122")]
    return d
