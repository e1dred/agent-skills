# Document styles

Eight ready-made looks, each as a **document** (title, headings, body, bullets, quote) and as an **ATS-friendly résumé**
(single column, real headings, no tables or text boxes). One spec file feeds both apps, so WordCraft and ONLYOFFICE
produce the same look. All sample text is invented.

| Style | Look | Good for |
|---|---|---|
| `traditional` | Times, black, centred headings, justified text | Formal letters, legal-style documents, conservative readers |
| `elegant` | Constantia/Georgia, burgundy, letter-spaced small headings with a hairline rule, wide margins | Invitations, personal statements, boutique-client proposals |
| `clean` | Calibri, dark grey, lots of white space, no ornament | Everyday documents, memos, handouts |
| `professional` | Calibri, navy all-caps headings with a bottom rule | Business reports, proposals, ATS résumés |
| `academic` | Times 12 pt, double-spaced, first-line indents, plain bold headings | Essays and papers (check your style guide's specifics) |
| `modern` | Century Gothic headings in teal, Corbel body, large title | Product docs, newsletters, design-aware résumés |
| `stylish` | Georgia italic plum headings with a gold bar, Candara body | Programmes, editorial handouts, brand-conscious proposals |
| `creative` | Coral headings, teal rule, Trebuchet, big title | Portfolios, workshop handouts, creative-field résumés |

![WordCraft documents](gallery/wordcraft-doc.png)
![ONLYOFFICE résumés](gallery/onlyoffice-resume.png)

(More in `gallery/`: both apps, documents and résumés.)

## Use

```sh
python3 -I resolve.py                                   # which font each style gets on this machine
# WordCraft: writes out.docx
python3 -I build_wordcraft.py modern doc /abs/out.docx > job.json && wordcraft-cli run --script job.json
python3 -I build_wordcraft.py modern resume /abs/cv.docx > job.json && wordcraft-cli run --script job.json
# ONLYOFFICE (headless; add --pdf to also save a PDF rendered by ONLYOFFICE for checking)
python3 -I build_onlyoffice.py modern doc /abs/out.docx > calls.json && python3 -I ../onlyoffice/tools/ooc.py new:docx calls.json
```

Replace the invented text in `content.py` with real content (keep the block types). To restyle a real document instead of
the sample, copy the `styles.modify` / style-creation part of a builder and apply it to the existing styles, then give
paragraphs the style names (`Heading 1`, `Heading 2`, `Doc Title`, …). Always work on a copy of someone's document.

## Fonts and fallbacks

Each style lists fonts in order of preference in `styles.json`; `resolve.py` picks the first one that is **installed** here.
By default it also requires a font that ships with Microsoft Office (Calibri, Cambria, Candara, Century Gothic, Constantia, Corbel,
Georgia, Arial, Times New Roman, Trebuchet MS, Verdana…), so a file opens the same on a colleague's computer. `--local-fonts`
lets any installed font win (e.g. Montserrat or Open Sans): only use it for documents that stay on this machine or embed the
fonts. If a preferred font is missing the resolver reports it and uses the next one; the look then differs slightly.

## Résumé formats

The builders produce the **reverse-chronological** layout (summary, competencies, experience, education, certifications):
the best default for ATS software and most recruiters. Two other content structures work with every style by reordering the
same sections: **functional** (skills grouped by theme first, short job list after; use when career gaps or a change of field
would make a timeline work against you, but some recruiters distrust it) and **combined** (summary and a skills block first,
then a timeline: good for experienced people changing direction). Keep one column and real headings in all of them; use
`creative` or `stylish` for a designed copy to send to a person, and `professional`/`clean`/`traditional` for portals.

## Checked

Every style was built in both apps and rendered (WordCraft with its own renderer, ONLYOFFICE through its own PDF export).
Letter-spacing, caps, borders, tab stops, bullets and links reach the saved `.docx` (inspected in `styles.xml`).
Not covered: tables, headers/footers, page numbers, columns, A4. Page size is US Letter.
