"""Build a styled sample document, résumé, CV or paper in ONLYOFFICE: prints a calls.json for tools/ooc.py (headless new docx).

    python3 -I build_onlyoffice.py STYLE KIND /abs/out.docx [options] > calls.json
    python3 -I ../onlyoffice/tools/ooc.py new:docx calls.json

STYLE and KIND as in build_wordcraft.py (doc | resume | cv | paper | manuscript; the manuscript options --title --author --pen --surname --address --phone --email --wordcount --font --layout --text work here too). Options (`--name=value`): --paper=letter|a4,
--page-numbers=bottom-center|bottom-right|top-right, --header-text=…, --columns=2 (doc), --photo=/abs/pic.png (resume/cv), --figure=sample|/abs/pic.png, --merged-table, --footnotes,
--script=arabic|hebrew|japanese|chinese|korean (doc), --extras (paper),
--layout=chronological|functional|combined (resume), --format=apa|mla (paper), --local-fonts, --pdf (also save a PDF rendered by
ONLYOFFICE, for checking), --overwrite (save_document never overwrites on its own; without this flag the script refuses if out.docx exists).
Notes about ATS-safety go to stderr. Macro units: font sizes in half-points, spacing/indents in twips (20 per pt), borders in 1/8 pt.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan import make, parse_argv

style_name, kind, out, o, flags = parse_argv(sys.argv)
overwrite = "overwrite" in flags
if os.path.exists(out) and not overwrite:
    sys.exit("refusing to overwrite %s (pass --overwrite)" % out)
P = make(style_name, kind, o)
for n in P["notes"]:
    print("NOTE:", n, file=sys.stderr)

JS = r'''
var PLAN = __PLAN__;
var doc = Api.GetDocument();
doc.RemoveSelection();
function col(h) { return Api.Color("#" + h); }
function tw(pt) { return Math.round(pt * 20); }
var sec = doc.GetSections()[0];
sec.SetPageSize(tw(PLAN.page.w), tw(PLAN.page.h));
sec.SetPageMargins(tw(PLAN.page.margins[2]), tw(PLAN.page.margins[0]), tw(PLAN.page.margins[3]), tw(PLAN.page.margins[1]));
function setText(t, p) {
  if (p.font) t.SetFontFamily(p.font);
  if (p.size) t.SetFontSize(Math.round(p.size * 2));
  if (p.color) t.SetColor(col(p.color));
  if (p.bold !== undefined) t.SetBold(!!p.bold);
  if (p.italic !== undefined) t.SetItalic(!!p.italic);
  if (p.caps) t.SetCaps(true);
  if (p.spacing) t.SetSpacing(tw(p.spacing));
}
function border(pp, side, b) {
  var fn = {bottom: "SetBottomBorder", left: "SetLeftBorder"}[side];
  try { pp[fn]("single", Math.round(b[1] * 8), b[2], col(b[0])); } catch (e) {}
}
var JC = {left: "left", center: "center", right: "right", justify: "both"};
function setPara(pp, p) {
  if (p.before !== undefined) pp.SetSpacingBefore(tw(p.before));
  if (p.after !== undefined) pp.SetSpacingAfter(tw(p.after));
  if (p.line !== undefined) pp.SetSpacingLine(Math.round(240 * p.line), "auto");
  if (p.align) pp.SetJc(JC[p.align] || "left");
  if (p.indent_first !== undefined) pp.SetIndFirstLine(tw(p.indent_first));
  if (p.indent_left !== undefined) pp.SetIndLeft(tw(p.indent_left));
  if (p.keep_next) pp.SetKeepNext(true);
  if (p.border_bottom) border(pp, "bottom", p.border_bottom);
  if (p.border_left) border(pp, "left", p.border_left);
  if (p.tab_right) pp.SetTabs([tw(p.tab_right)], ["right"]);
}
var BUILTIN = {"Normal": 1, "Heading 1": 1, "Heading 2": 1, "Heading 3": 1};
var normal = doc.GetStyle("Normal");
for (var i = 0; i < PLAN.styles.length; i++) {
  var nm = PLAN.styles[i][0], p = PLAN.styles[i][1], st;
  if (BUILTIN[nm]) st = doc.GetStyle(nm);
  else { st = doc.CreateStyle(nm, "paragraph"); st.SetBasedOn(normal); }
  setText(st.GetTextPr(), p); setPara(st.GetParaPr(), p);
}
var base = PLAN.styles[0][1];
if (PLAN.header || PLAN.footer) {
  ["Header", "Footer"].forEach(function (n) {
    try { var s = doc.GetStyle(n); setText(s.GetTextPr(), {font: base.font, size: base.size, color: (PLAN.kind === "paper" || PLAN.kind === "manuscript") ? "000000" : "555555"}); } catch (e) {}
  });
}
if (PLAN.different_first) { try { sec.SetTitlePage(true); } catch (e) {} }   // page 1 (title page) gets the empty first-page header
if (PLAN.header) {
  var hp = sec.GetHeader("default", true).GetElement(0);
  hp.SetJc(JC[PLAN.header.align]);
  if (PLAN.header.text) hp.AddText(PLAN.header.text);
  if (PLAN.header.number) hp.AddPageNumber();
}
if (PLAN.footer) {
  var fp = sec.GetFooter("default", true).GetElement(0);
  fp.SetJc(JC[PLAN.footer.align]); fp.AddPageNumber();
}
doc.RemoveAllElements();
var LVL = null;
function bulletLevel() {
  var lvl = doc.CreateNumbering("bullet").GetLevel(0);
  lvl.SetTemplateType("bullet", "•");
  lvl.GetTextPr().SetColor(col(PLAN.bullet.color));
  lvl.GetParaPr().SetIndLeft(360); lvl.GetParaPr().SetIndFirstLine(-260);
  lvl.SetSuff("tab");
  return lvl;
}
var pendingBefore = 0, pendingBreak = false, lastPara = null, COLS = 0;
function addPara(style, runs, bullet, scr) {
  var p = Api.CreateParagraph();
  p.SetStyle(doc.GetStyle(style));
  if (scr) {   // no paragraph-direction call exists in this macro API: right-align RTL text, set font and proofing language on the run
    var rr = Api.CreateRun(); rr.SetFontFamily(scr.font); try { rr.SetLanguage(scr.lang); } catch (e) {}
    rr.AddText(runs[0][1]); p.AddElement(rr); if (scr.rtl) p.SetJc("right");
    doc.Push(p); lastPara = p; return;
  }
  for (var i = 0; i < runs.length; i++) {
    var seg = runs[i], r = Api.CreateRun();
    if (seg[0] === true) r.SetBold(true);
    if (seg[0] === "i") r.SetItalic(true);
    var bits = seg[1].split("\t");
    for (var k = 0; k < bits.length; k++) { if (k > 0) r.AddTabStop(); if (bits[k]) r.AddText(bits[k]); }
    p.AddElement(r);
  }
  if (bullet) { if (!LVL) LVL = bulletLevel(); p.SetNumbering(LVL); }
  if (pendingBefore) { p.SetSpacingBefore(tw(pendingBefore)); pendingBefore = 0; }
  if (pendingBreak) { p.SetPageBreakBefore(true); pendingBreak = false; }
  doc.Push(p); lastPara = p;
}
function addTable(b) {
  var rows = b.rows, nr = rows.length, nc = rows[0].length;
  var tbl = Api.CreateTable(nr, nc);  // checked: in this build the FIRST argument is the row count
  tbl.SetWidth("percent", 100);
  var merged = b.merge && b.merge.length > 0;
  if (merged) { var mc = []; for (var q = b.merge[0][1]; q <= b.merge[0][3]; q++) mc.push(tbl.GetRow(b.merge[0][0]).GetCell(q)); tbl.MergeCells(mc); }  // the row then has ONE cell
  var hdrRows = merged ? 2 : 1;
  for (var r = 0; r < nr; r++) {
    var nCells = tbl.GetRow(r).GetCellsCount();
    for (var c = 0; c < nCells && c < rows[r].length; c++) {
      var cell = tbl.GetRow(r).GetCell(c), p = cell.GetContent().GetElement(0);
      p.SetStyle(doc.GetStyle(b.style));
      var run = Api.CreateRun(); run.AddText(rows[r][c]); p.AddElement(run);
      if (r === 0) { cell.SetShd("clear", col(b.fill)); run.SetBold(true); run.SetColor(col(b.text)); if (merged) p.SetJc("center"); }
      else if (r === 1 && merged) { cell.SetShd("clear", col(b.sub_fill)); run.SetBold(true); }
    }
  }
  ["Top", "Bottom", "Left", "Right", "InsideH", "InsideV"].forEach(function (s) { tbl["SetTableBorder" + s]("single", 4, 0, col(b.border)); });
  doc.Push(tbl);
}
for (var j = 0; j < PLAN.blocks.length; j++) {
  var b = PLAN.blocks[j];
  if (b.t === "p") addPara(b.style, b.runs, b.bullet, b.script ? {font: b.font, lang: b.lang, rtl: b.rtl} : null);
  else if (b.t === "figure") addPara(b.caption_style, [[false, b.caption]], false);   // caption only; word_add_image puts the picture before it
  else if (b.t === "spacer") pendingBefore = b.pt;
  else if (b.t === "pagebreak") pendingBreak = true;
  else if (b.t === "table") addTable(b);
  else if (b.t === "columns") { doc.CreateSection(lastPara); COLS = b.n; }
}
var f0 = doc.GetElement(0);
if (f0 && f0.GetClassType() === "paragraph" && f0.GetText().replace(/[\r\n]/g, "") === "" && doc.GetElementsCount() > 1) doc.RemoveElement(0);
if (COLS) { var fin = doc.GetFinalSection(); fin.SetType("continuous"); fin.SetEqualColumns(COLS, 360); }
for (var L = 0; L < PLAN.links.length; L++) { var hits = doc.Search(PLAN.links[L][0], true); if (hits.length) hits[0].AddHyperlink(PLAN.links[L][1], ""); }
return {elements: doc.GetElementsCount()};
'''

plan_js = json.dumps(P, ensure_ascii=False)
calls = [["word_write_macro", {"code": JS.replace("__PLAN__", plan_js)}]]
# 1-based top-level element index of every paragraph/table the macro creates (the initial empty paragraph is removed)
count, images = 0, []
for b in P["blocks"]:
    if b["t"] in ("p", "table"): count += 1
    elif b["t"] == "figure":
        count += 1; images.append((count, b["path"], b["w"], b["h"], b["style"], b["alt"]))
    elif b["t"] == "photo":
        images.append((1, b["path"], b["w"], b["h"], b["style"], "Portrait photo"))
for fn in P["footnotes"]:   # this tool anchors the footnote at the END of the paragraph that contains the phrase
    calls.append(["word_comment_text", {"search": fn["anchor"], "prompt": "Add a footnote", "comment_text": fn["text"], "type": "footnote"}])
images.sort(key=lambda t: t[0])
for j, (idx, path, w, h, style, alt) in enumerate(images):      # inserting in ascending order shifts later targets by one each time
    calls.append(["word_add_image", {"src": path, "width": round(w * 0.3528), "height": round(h * 0.3528), "index": idx + j}])
if images:
    sets = ";".join('doc.GetElement(%d).SetStyle(doc.GetStyle("%s"))' % (idx + j - 1, style) for j, (idx, _, _, _, style, _) in enumerate(images))
    alts = json.dumps([a for *_, a in images])   # drawings come back in document order; the image tool sets no alt text itself
    calls.append(["word_write_macro", {"code": "var doc = Api.GetDocument(); " + sets + "; var ds = doc.GetAllDrawingObjects(), alts = " + alts + "; for (var q = 0; q < ds.length && q < alts.length; q++) ds[q].SetDescription(alts[q]); return 'images styled';"}])
calls.append(["save_document", dict({"path": out, "format": "docx"}, **({"overwrite": True} if overwrite else {}))])
if "pdf" in flags:  # also render with ONLYOFFICE itself, for checking the look
    calls.append(["save_document", dict({"path": out[:-5] + ".pdf", "format": "pdf"}, **({"overwrite": True} if overwrite else {}))])
json.dump(calls, sys.stdout)
