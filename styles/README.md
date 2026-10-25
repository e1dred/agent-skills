# Document styles

Eight ready-made looks. Each comes as a **document** (title, headings, body, bullets, quote, table), an **ATS-friendly résumé**, a
**European-style CV**, and (for the academic style) an **APA or MLA student paper**, on **US Letter or A4**. One plan feeds both
WordCraft and ONLYOFFICE, so they produce the same look. All sample text is invented.

| Style | Look | Good for |
|---|---|---|
| `traditional` | Times, black, centred headings, justified text | Formal letters, legal-style documents, conservative readers |
| `elegant` | Constantia/Georgia, burgundy, letter-spaced small headings with a hairline rule, wide margins | Invitations, personal statements, boutique-client proposals |
| `clean` | Calibri, dark grey, lots of white space, no ornament | Everyday documents, memos, handouts |
| `professional` | Calibri, navy all-caps headings with a bottom rule | Business reports, proposals, ATS résumés |
| `academic` | Times 12 pt, double-spaced, first-line indents, plain bold headings | Essays and papers (with `paper`: APA or MLA layout) |
| `modern` | Century Gothic headings in teal, Corbel body, large title | Product docs, newsletters, design-aware résumés |
| `stylish` | Georgia italic plum headings with a gold bar, Candara body | Programmes, editorial handouts, brand-conscious proposals |
| `creative` | Coral headings, teal rule, Trebuchet, big title | Portfolios, workshop handouts, creative-field résumés |

![WordCraft documents](gallery/wordcraft-doc.png)
![ONLYOFFICE résumés](gallery/onlyoffice-resume.png)
![WordCraft options: columns, APA, MLA, résumé layouts, CV with photo, header and footer](gallery/wordcraft-features.png)

More in `gallery/` (both apps; documents, résumés, A4 CVs, features).

## Use

```sh
python3 -I resolve.py                                   # which font each style gets on this machine
# WordCraft: writes the .docx
python3 -I build_wordcraft.py modern doc /abs/report.docx > job.json && wordcraft-cli run --script job.json
# ONLYOFFICE (headless): add --pdf to also save a PDF rendered by ONLYOFFICE, for checking
python3 -I build_onlyoffice.py modern doc /abs/report.docx > calls.json && python3 -I ../onlyoffice/tools/ooc.py new:docx calls.json
```

`KIND` is `doc`, `resume`, `cv` or `paper`. Options, the same in both builders (`--name=value`):

| Option | Applies to | What it does |
|---|---|---|
| `--paper=letter` / `--paper=a4` | all | Page size. Default Letter; `cv` defaults to A4. |
| `--page-numbers=bottom-center` / `bottom-right` / `top-right` | all | Page number in the footer or header. |
| `--header-text="Short title"` | all | Text in the header (with `top-right`, text then number). |
| `--columns=2` | `doc` | Body in two columns after the title (newsletter feel). |
| `--photo=/abs/pic.png` | `resume`, `cv` | Portrait above the name. |
| `--layout=chronological` / `functional` / `combined` | `resume` | Which résumé structure. |
| `--format=apa` / `--format=mla` | `paper` | Student-paper layout. |
| `--local-fonts` | all | Allow fonts installed here but not shipped with Office. |
| `--overwrite` | all | Replace an existing output file (otherwise the builder refuses). |

Cautions (for example "photo is not ATS-safe") are printed to stderr. Replace the invented text in `content.py` with real content; keep the
block types. To restyle a real document instead of the sample, copy the style-setting part of a builder onto the document's existing styles
and give paragraphs the style names (`Heading 1`, `Heading 2`, `Doc Title`, …). Always work on a copy of someone's document.

## ATS-friendly, or good for humans?

An applicant-tracking system reads the *structure* of a file, not its look. Everything a builder produces for `resume` and `cv` is a single column of
real text with real heading styles, plain bullets, text hyperlinks and dates on a tab stop, so structurally all eight styles are ATS-safe. That is
based on common ATS guidance; **it was not tested against any real ATS software**. The things that do break parsing are features, not styles:

| Feature | For people | For ATS |
|---|---|---|
| Single column, real headings, plain bullets (all résumé and CV styles) | good | **safe** |
| Chronological or combined layout | good | **safe** |
| Functional layout (skills first, short work history) | good if you must hide gaps; some recruiters distrust it | parses, but skills are cut off from dates and employers: use sparingly |
| `traditional`, `clean`, `professional`, `academic` | conservative, familiar | safest choice for online portals |
| `elegant`, `modern`, `stylish`, `creative` | more memorable | structure is still safe; colour and decoration are ignored, so use them for résumés a person will read |
| Photo | expected in some countries, unwanted in the US and UK | ignored at best; avoid for portals |
| Columns, tables, text boxes, graphics, icon bars (`--columns`, tables in `doc`) | fine in reports and newsletters | **not safe in résumés**: text can be read in the wrong order or dropped |
| Contact details in the header/footer | tidy | **often skipped** by parsers: keep them in the body |

So: send a `professional`/`clean`/`traditional` résumé (or any style, as long as it is the plain single-column build) through online portals, and
use a designed style, a photo or columns for a copy you hand to a person.

## Tables, headers and footers, columns

- **Tables** in `doc`: a thin grid, a filled header row in the style's colour, small body text; the header row repeats on a new page in WordCraft.
  (Per-side borders and banded rows are not supported by WordCraft's border command, so both apps use the same simple grid.)
- **Headers and footers**: `--page-numbers` and `--header-text`. `paper` builds the page-number header APA and MLA expect (MLA: surname and number).
- **Columns**: two newspaper-style columns for the body, the title spanning the page.

## Papers (APA 7 and MLA 9 layout)

`paper` uses the `academic` look: Times 12 pt, 1 in margins, double spacing, 0.5 in first-line indent, page number top right, hanging-indent
reference list. `--format=apa`: title page (bold title, author, affiliation, course, instructor, date), then the paper from page 2 with centred
bold level-1 and left bold level-2 headings, then *References*. `--format=mla`: no title page; four-line heading block at the top left, centred
title, *Works Cited* on a new page, "Surname page" header. This is a layout aid, not a style-guide checker: the sample sources are fictional and
details such as running heads for professional papers, abstracts, block quotes and table captions are not shown. Check your instructor's or
journal's current guide.

## Paper size

`--paper=letter` or `--paper=a4`. The builders set the page size, margins and the right-hand tab used for dates. A4 is narrower and taller
(595 × 842 pt) than Letter (612 × 792 pt). Checked: both sizes report the right page size in both apps.

## CV (European style)

`cv` is a single-column curriculum vitae in the order European employers expect: name, role and contact lines; *Profile*; *Work experience* (newest
first, dates as `MM/YYYY – present`); *Education and training* (degree and years, institution below); *Languages* (mother tongue, then each language
with CEFR levels A1–C2 for listening, reading, speaking and writing); *Digital skills*; *Certificates*; *Interests*. It is inspired by the Europass
structure but is **not** the official Europass template. A photo, date of birth, nationality and marital status are expected in some countries and
discouraged or unlawful to ask for in others (including the US and UK), so none are included; add them only where the local norm calls for it.
Two pages are normal for a senior CV.

## Fonts and fallbacks

Each style lists fonts in order of preference in `styles.json`; `resolve.py` picks the first one that is **installed**. By default it also requires a
font that ships with Microsoft Office (Calibri, Cambria, Candara, Century Gothic, Constantia, Corbel, Georgia, Arial, Times New Roman, Trebuchet MS,
Verdana…), so a file opens the same on a colleague's computer. `--local-fonts` lets any installed font win (e.g. Montserrat): only use it for
documents that stay on this machine or embed the fonts. If a preferred font is missing, the resolver reports it and uses the next one.

## Checked

Every style as `doc`, `resume` and `cv`, and the feature samples (columns, APA, MLA, functional, combined, photo, header and footer), were built in
both apps and rendered (WordCraft with its own renderer, ONLYOFFICE through its own PDF export). The builders check for macro errors and refuse to
overwrite an existing file unless asked.

Not covered: the official Europass template; footnotes and citations managed by the app; images other than a CV photo; right-to-left or CJK text;
tables with merged cells; real-ATS testing.
