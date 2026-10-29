# WordCraft reference: mail merge citations

Part of the wordcraft skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Mail merge (verified headless with `wordcraft-cli run --script`; letters)

> Not re-checked: `addressBlock`/`greetingLine`, `rules`, envelopes/labels, `.xlsx` recipients.

```
mailings.start {"kind":"letters"}                       # also emails|envelopes|labels|directory
mailings.recipients {"csv":"Name,Company\nAda,Acme\n…"}   # or {"path":"/abs/people.csv"} (.csv/.tsv/.xlsx/.ods…) → {"fields":[…],"records":N}
mailings.filterRecipients {"rules":[{"field":"Status","op":"equal","value":"send"}]}   # → {"of":4,"records":3}
text.insert {"text":"Dear "}, mailings.insertField {"field":"Name"}, …      # the template text, with fields
mailings.addressBlock {} / mailings.greetingLine {}     # built from STANDARD column names: First Name, Last Name,
                                                        # Address Line 1, City, State, Postal Code → "Ada Example / 1 Main St /
                                                        # Boston, MA 02101" and "Dear Ada Example,"
mailings.rules {"rule":"IF","field":"Role","value":"","then":"…","else":"…"}   # also SKIPIF|NEXTIF|NEXT|MERGEREC
mailings.checkErrors {} → {"ok":true,"records":3,"unknownFields":[]}
mailings.finish {"path":"/abs/merged.docx","from":1,"to":2}   # one page per record; from/to merges a range
```
- The filter is applied before the merge: 4 records with one `Status=skip` gave 3 letters on 3 pages.
- An empty field simply leaves a gap ("the  position"): use an `IF` rule or filter blanks out (`op:"notBlank"`).
- **`then`/`else` text in `IF` is literal**: `else:"the Role you posted"` printed the word "Role", not the field's value, so
  you cannot embed a field inside a rule's text; put the field next to the rule instead.
- `\n` inside `text.insert` is a soft line break, so each merged letter was ONE paragraph with line breaks
  (`info` said 3 paragraphs for 3 letters); use `text.newParagraph` between paragraphs if separate paragraphs matter.
- Only letters were merged; envelopes (`mailings.envelopes`) and labels (`mailings.labels {"product":"letter-3x10",
  "fromRecipients":true}`) exist but were not run. Live mode with the app open was not tried for mailings.

## Citations, bibliography, cross-references (verified headless)

> Not re-checked: the other citation styles, `references.sources`, cross-references to bookmarks, figures, tables, equations or pages.

```
references.citationStyle {"style":"APA"}     # also IEEE, MLA, Chicago, Harvard (Anglia), ISO 690, Turabian, GOST…
references.citation {"source":{"tag":"Smith2020","type":"Book","author":"Smith, John","title":"…","year":"2020",
                     "publisher":"…","city":"…"},"pages":"12"}      # inserts "(Smith, 2020, p. 12)"; later: {"tag":"Smith2020","pages":"50"}
references.bibliography {"title":"References"}   # insert after text.newParagraph; same style as the citations
```
- **`author` is ONE string, not a list or object** (a list/map is rejected with "invalid type: sequence, expected a string").
  Several authors: `"Lee, Mina; Park, Joon; Kim, Ana"` (semicolon between "Last, First" names) → APA gives
  "(Lee & Park, 2022)" / "(Lee et al., 2022)" and "Lee, M., Park, J., & Kim, A. (2022)." `"Mina Lee and Joon Park"` parsed
  wrongly ("Park, M. L. a. J."). **Unknown source keys are silently ignored**: `authors` (plural) produced "(Title, 2020)" and
  a reference with no author. Always read the bibliography output.
- Types verified: `Book`, `JournalArticle` (`journal`, `volume`, `issue`, `pages`). Same text in IEEE: "[1]", "[2]" and a numbered
  list; MLA: "(Coaching Teachers 12)". `references.sources {"add"|"remove"|"import"}` lists/manages sources (untested).
- Cross-references: `insert.crossReference {}` lists targets (`["Methods","Results"]`); `{"to":"heading","target":"Methods",
  "show":"text"}` → "Methods"; `"show":"page"` → "1" (also bookmark, figure, table, equation, `label:<Name>`).
