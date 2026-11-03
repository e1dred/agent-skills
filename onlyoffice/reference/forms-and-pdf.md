# ONLYOFFICE reference: forms and PDF

Part of the onlyoffice skill. The short front page is `../SKILL.md`; the sections below are unchanged from the single-file guide.

## Forms, all field types (verified headless: build, fill, save as form, reopen)

- `form_add_field` types: `text` (also `multiline:true`, `max_chars:200` → `charLimit`), `dropdown` (`items`, reported
  back as `comboBoxForm` with an extra "Choose an item" first entry), `combobox` (`items`), `checkbox`, `radio`
  (one `key` for the group, a different `choice_name` per option: add one call per option), `date` (`date_format`).
- `form_fill {"fields":[{"key","value"},…]}`: text/multiline/date as strings ("10/24/2026"), dropdown by item text,
  checkbox "yes"/"true", **radio by the choice name** on the group key (`{"key":"contact","value":"by_email"}` → `◉`).
  **A combo box refused a value that was not in its list** (`failed … "set failed"`), although the UI allows typing:
  pick a listed item.
- `save_document {"format":"form"}` → reopen with `open_document`: it comes back as an editable Word document with all
  fields and values (checked with `form_get_fields`). The `preview` shows labels and values inline without field boxes.

## PDF tools (verified headless; open a .pdf to get the `pdf_*` tools)

- `pdf_get_document_info` → page count + AcroForm field summary; `pdf_search_document {"query":"a|b","is_regex":true,
  "context_chars":20}` → matches with page, snippet, occurrence; `pdf_get_page_info {"page_number","include_forms"}`.
- Markup is a two-step pipeline: `pdf_get_text_quads {"page_number":1,"items":["requirements"]}` (items may be
  strings or `{"text"}`) → per-occurrence quads; then `pdf_markup_text {"page_number":1,"type":"highlight"|
  "strikeout"|"underline"|redact,"markup_targets":[{"text","quads":[the quad(s) of ONE occurrence],"comment"?}]}`.
  Passing only `{"text"}` fails with "empty quads". Apply `save_document` afterwards.
- **Colour trap:** `color` as a list (`[255,235,0]`, `[1,.92,0]`), `"#FFEB00"` or `"FFEB00"` all produced a solid BLACK
  box over the text in the render. Omit `color` (default yellow) or pass an object `{"r":255,"g":235,"b":0}`.
  Always render a page after marking up: the black box also looked like a redaction.
- `pdf_split {"parts":[{"pages":"1","path":ABS}],"overwrite":true}`; `pdf_merge {"sources":[{path,pages?}],
  "output_path","overwrite"}` (verified 2026-10-25: "Merged 4 page(s) from 2 file(s)").

## Fillable forms (verified headless)

- Flow: `create_document("docx")` → `form_add_field {"type":"text"|"dropdown"|"combobox"|"checkbox"…,"key","label",
  "placeholder","required","items":[…]}` per field → `save_document {"format":"form"}` (a fillable PDF that reopens
  EDITABLE as a Word document with its fields; `format:"pdf"` flattens it and says so in the reply).
- `form_get_fields` lists keys, `type` (`textForm|comboBoxForm|checkBoxForm|…`), `value`, `filled`, `required`.
  A dropdown reports as `comboBoxForm` and has an extra first list entry "Choose an item".
- **`form_fill {"fields":[{"key":"full_name","value":"Ada"},{"key":"plan","value":"Pro"},{"key":"agree","value":"true"}]}`**:
  `fields` must be a LIST of `{key,value}`; a `{key: value}` object fails with `field not found`. Checkbox values:
  "true"/"1"/"yes"/"on"/"checked"/"x". Read `form_get_fields` back (`filled:true`, checkbox `☑`).
- `word_generate_form {"description"}` is a two-call AI task that returns `{FIELD:…}` template syntax (untested).
