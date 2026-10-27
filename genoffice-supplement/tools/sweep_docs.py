import json,subprocess,shutil,sys,os
W=os.path.dirname(os.path.abspath(__file__))
def g(*a):
    r=subprocess.run(["genoffice",*a,"--json"],capture_output=True,text=True,cwd=W)
    try: return json.loads(r.stdout)
    except Exception: return {"status":"nojson","raw":(r.stdout+r.stderr)[:300]}
T={"blockIndexes":[3]}
PNG=os.path.join(W,"pic.png")
cases=[
("setFont",[{"op":"setFont","target":T,"bold":True,"color":"#C00000","fontSize":14,"fontFamily":"Georgia"}],["--range","3-3","--html"]),
("setFont-link",[{"op":"setFont","target":T,"link":{"url":"https://x.org"}}],["--range","3-3","--html"]),
("setMatchedFont",[{"op":"setMatchedFont","text":"Revenue","bold":True,"highlight":"yellow"}],["--range","3-3","--html"]),
("setParagraphFormat",[{"op":"setParagraphFormat","target":T,"align":"justify","lineSpacing":1.5,"indentFirstLine":360,"spaceAfter":240,"shadingFill":"#EEEEEE","borders":"tb","tabs":[{"pos":"3in","align":"right","leader":"dot"}]}],["--range","3-3"]),
("setHeadingLevel",[{"op":"setHeadingLevel","target":{"blockIndexes":[7]},"level":3}],["--range","7-7"]),
("findReplace",[{"op":"findReplace","find":"Revenue","replace":"Sales"}],["--range","3-3"]),
("deleteBlocks",[{"op":"deleteBlocks","target":{"blockIndexes":[8]}}],[]),
("moveBlocks",[{"op":"moveBlocks","blockIndexes":[8],"afterBlockIndex":0}],["--range","0-2"]),
("setList",[{"op":"setList","target":T,"kind":"number"}],["--range","3-3"]),
("setList-default",[{"op":"setList","target":T}],["--range","3-3"]),
("clearList",[{"op":"clearList","target":{"blockIndexes":[4,5]}}],["--range","4-5"]),
("insertToc",[{"op":"insertToc","afterBlockIndex":0}],["--fields"]),
("insertField-SEQ",[{"op":"insertField","target":T,"type":"SEQ","args":"Figure \\* ARABIC"}],["--fields"]),
("insertField-DATE",[{"op":"insertField","target":T,"type":"DATE","args":"\\@ \"d MMMM yyyy\""}],["--fields"]),
("insertField-MERGEFIELD",[{"op":"insertField","target":T,"type":"MERGEFIELD","args":"Name","result":"«Name»","position":"start"}],["--fields"]),
("bookmark+REF",[{"op":"insertBookmark","target":{"blockIndexes":[2]},"name":"res"},{"op":"insertField","target":T,"type":"REF","args":"res"}],["--fields"]),
("updateFields",[{"op":"insertField","target":T,"type":"SEQ","args":"Figure"},{"op":"updateFields","scope":"all"}],["--fields"]),
("insertTableRow",[{"op":"insertTableRow","target":{"blockIndexes":[6]},"row":1,"position":"after","count":2}],["--range","6-6"]),
("deleteTableRow",[{"op":"deleteTableRow","target":{"blockIndexes":[6]},"row":2}],["--range","6-6"]),
("insertTableColumn",[{"op":"insertTableColumn","target":{"blockIndexes":[6]},"col":1}],["--range","6-6"]),
("deleteTableColumn",[{"op":"deleteTableColumn","target":{"blockIndexes":[6]},"col":2}],["--range","6-6"]),
("mergeTableCells",[{"op":"mergeTableCells","target":{"blockIndexes":[6]},"range":{"row":1,"col":0,"rowEnd":2,"colEnd":0}}],["--range","6-6"]),
("splitTableCell",[{"op":"mergeTableCells","target":{"blockIndexes":[6]},"range":{"row":1,"col":0,"rowEnd":2,"colEnd":0}},{"op":"splitTableCell","target":{"blockIndexes":[6]},"cell":{"row":1,"col":0}}],["--range","6-6"]),
("setTableCellFormat",[{"op":"setTableCellFormat","target":{"blockIndexes":[6]},"range":{"row":0,"col":0,"colEnd":2},"fill":"#1F4E79","vAlign":"center","borders":{"all":{"style":"single","width":1,"color":"#1F4E79"}}}],["--range","6-6"]),
("setTableStyle",[{"op":"define_style","styleId":"Banded","name":"Banded","type":"table"},{"op":"setTableStyle","target":{"blockIndexes":[6]},"styleId":"Banded","look":{"bandedRows":True}}],["--range","6-6"]),
("applyStyle",[{"op":"define_style","styleId":"Callout","name":"Callout","type":"paragraph","paragraph":{"spaceBefore":120},"run":{"italic":True}},{"op":"applyStyle","target":T,"styleId":"Callout"}],["--styles"]),
("insert_content",[{"op":"insert_content","html":"<h2>Added</h2><p>New <strong>text</strong>.</p><pre>code()</pre><blockquote>Quote</blockquote><p>E: <formula>E=mc^2</formula></p>","afterBlockIndex":3}],["--range","3-9"]),
("replace_blocks",[{"op":"replace_blocks","startBlockIndex":3,"endBlockIndex":3,"html":"<p>Replaced.</p>"}],["--range","3-3"]),
("insert_image",[{"op":"insert_image","url":PNG,"maxWidthPx":200,"afterBlockIndex":1}],["--range","1-3"]),
("insert_picture",[{"op":"insert_picture","url":PNG,"width":"3cm","float":{"anchor":"page","x":"10cm","y":"2cm","wrap":"square"},"altText":"sample","afterBlockIndex":1}],["--range","1-3"]),
("setImageProperties",[{"op":"insert_image","url":PNG,"afterBlockIndex":1},{"op":"setImageProperties","target":{"nodeType":"image"},"widthPx":100,"align":"center"}],["--range","1-3"]),
("insert_text_box",[{"op":"insert_text_box","afterBlockIndex":1,"text":"Boxed","width":"4cm","height":"2cm","x":"12cm","y":"3cm","fill":"#FFF2CC","borderColor":"#7F6000","bold":True}],["--range","1-3"]),
("insert_chart",[{"op":"insert_chart","kind":"bar","title":"Sales","categories":["N","S"],"series":[{"name":"Q","values":[10,15]}],"afterBlockIndex":6}],["--range","6-8"]),
("edit_chart",[{"op":"insert_chart","kind":"pie","title":"Sales","categories":["N","S"],"series":[{"values":[10,15]}],"afterBlockIndex":6},{"op":"edit_chart","blockIndex":7,"title":"Share","series":[{"index":0,"values":[40,60]}]}],["--range","6-8"]),
("set_header_footer",[{"op":"set_header_footer","kind":"header","text":"Acme Corp"},{"op":"set_header_footer","kind":"footer","text":"Page {PAGE} of {NUMPAGES}"}],["--header-footer"]),
("hf-first-even",[{"op":"set_header_footer","kind":"header","text":"First","view":"first"},{"op":"set_header_footer","kind":"footer","text":"Even","view":"even"}],["--header-footer"]),
("set_page_setup",[{"op":"set_page_setup","paper":"Letter","orientation":"landscape","margins":{"top":"1in","left":"1.25in"},"columns":{"count":2,"spacing":"0.5in"},"pageNumberStart":5}],["--sections"]),
("insert_section_break",[{"op":"insert_section_break","afterBlockIndex":5,"type":"nextPage"},{"op":"set_page_setup","section":1,"orientation":"landscape"}],["--sections"]),
("set_watermark",[{"op":"set_watermark","text":"DRAFT","color":"#C00000","opacity":0.3,"diagonal":True}],["--header-footer"]),
("define_style",[{"op":"define_style","styleId":"MyChar","name":"My Char","type":"character","run":{"bold":True,"color":"#0070C0","smallCaps":True}}],["--styles"]),
("add_comment",[{"op":"add_comment","blockIndex":3,"text":"steady","comment":"Check this","author":"Reviewer","initials":"R"}],["--comments"]),
("reply+resolve",[{"op":"add_comment","blockIndex":3,"comment":"Check"}],["--comments"]),
("footnote",[{"op":"insert_footnote","blockIndex":3,"afterText":"quarter","text":"Source: ledger."},{"op":"insert_endnote","blockIndex":1,"text":"End note."}],["--notes"]),
("properties",[{"op":"set_properties","core":{"title":"QR","creator":"Jane Doe","keywords":"a,b"},"custom":{"Dept":"Finance"}}],["--properties"]),
("content_control",[{"op":"wrap_content_control","startBlockIndex":3,"endBlockIndex":5,"tag":"sec","title":"Section","lock":"sdtLocked"}],["--range","3-5"]),
("unwrap_cc",[{"op":"wrap_content_control","startBlockIndex":3,"tag":"sec"},{"op":"unwrap_content_control","tag":"sec"}],["--range","3-5"]),
]
only=sys.argv[1:]
res=[]
for n,ops,rd in cases:
    if only and n not in only: continue
    out=os.path.join(W,"out",n+".docx"); os.makedirs(os.path.dirname(out),exist_ok=True)
    shutil.copy(os.path.join(W,"base.docx"),out)
    opsf=os.path.join(W,"out",n+".json"); json.dump(ops,open(opsf,"w"))
    r=g("docs","apply",out,"--ops",opsf)
    line={"case":n,"status":r.get("status"),"summary":str(r.get("summary") or r.get("message") or r.get("error"))[:140]}
    if r.get("status")=="ok" and rd:
        d=g("docs","read",out,*rd)
        line["read"]=json.dumps(d.get("detail"))[:420]
    res.append(line); print(json.dumps(line,ensure_ascii=False))
