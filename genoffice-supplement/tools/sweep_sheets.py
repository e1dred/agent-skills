import json,subprocess,shutil,sys,os,zipfile,re
W=os.path.dirname(os.path.abspath(__file__))
def g(*a):
    r=subprocess.run(["genoffice",*a,"--json"],capture_output=True,text=True,cwd=W)
    try: return json.loads(r.stdout)
    except Exception: return {"status":"nojson","raw":(r.stdout+r.stderr)[:300]}
S="base"
PNG=os.path.join(W,"pic.png")
C=[
("set_cell",[{"op":"set_cell","address":"G1","value":"hello"},{"op":"set_cell","address":"G2","value":42},{"op":"set_cell","address":"G3","value":True},{"op":"set_cell","address":"G4","value":"=SUM(C2:C7)"},{"op":"set_cell","address":"G5","value":"=1+1","type":"text"}],"G1:G5"),
("set_formula",[{"op":"set_formula","address":"F2","formula":"=C2*D2"},{"op":"set_formula","address":"F3","formula":"=IFERROR(VLOOKUP(\"Gadget\",B2:D7,3,FALSE),0)"},{"op":"set_formula","address":"F4","formula":"=XLOOKUP(\"Gizmo\",B2:B7,D2:D7)"},{"op":"set_formula","address":"F5","formula":"=SUMIFS(C2:C7,A2:A7,\"North\")"},{"op":"set_formula","address":"F6","formula":"=TEXTJOIN(\",\",TRUE,A2:A4)"},{"op":"set_formula","address":"F7","formula":"=FILTER(C2:C7,C2:C7>5)"}],"F1:F7"),
("set_range",[{"op":"set_range","start":"G1","values":[[1,2],[3,"=A1"],["x",None]]}],"G1:H3"),
("clear",[{"op":"clear_cell","address":"A2"},{"op":"clear_range","range":"B2:C3"}],"A1:E4"),
("fill_range",[{"op":"set_formula","address":"F2","formula":"=C2*D2"},{"op":"fill_range","source":"F2","target":"F2:F7"}],"F1:F7"),
("copy_range",[{"op":"copy_range","source":"A1:E7","target":"A10"}],"A10:E12"),
("copy_filter",[{"op":"copy_range","source":"A1:E7","target":"A10","filterColumn":"A","filterValues":["North"]}],"A10:E13"),
("move_range",[{"op":"move_range","source":"A1:B3","target":"H1"}],"A1:I4"),
("find_replace",[{"op":"find_replace","range":"A1:B7","find":"widget","replace":"Cog","matchCase":False}],"A1:B7"),
("sort_range",[{"op":"sort_range","range":"A1:E7","byColumn":"C","order":"desc","hasHeader":True}],"A1:E7"),
("convert_to_values",[{"op":"set_formula","address":"F2","formula":"=C2*D2"},{"op":"convert_to_values","range":"F2:F2"}],"F1:F3"),
("format_range",[{"op":"format_range","range":"A1:E1","format":{"bold":True,"fillColor":"#1F4E79","fontColor":"#FFFFFF","horizontalAlign":"center","fontFamily":"Calibri","fontSize":12,"borders":{"all":{"style":"thin","color":"#000000"}}}},{"op":"format_range","range":"D2:D7","format":{"numberFormat":"$#,##0.00"}},{"op":"format_range","range":"E2:E7","format":{"numberFormat":"yyyy-mm-dd"}}],"A1:E3"),
("cond_number",[{"op":"add_conditional_format","range":"C2:C7","rule":{"kind":"number","operator":"greaterThan","value":8,"format":{"fillColor":"#FFC7CE","fontColor":"#9C0006"}}}],None),
("cond_scale_bar",[{"op":"add_conditional_format","range":"C2:C7","rule":{"kind":"colorScale","minColor":"#F8696B","midColor":"#FFEB84","maxColor":"#63BE7B"}},{"op":"add_conditional_format","range":"D2:D7","rule":{"kind":"dataBar","color":"#638EC6"}},{"op":"add_conditional_format","range":"A2:A7","rule":{"kind":"text","operator":"contains","text":"North","format":{"bold":True}}},{"op":"add_conditional_format","range":"B2:B7","rule":{"kind":"duplicate","format":{"italic":True}}},{"op":"add_conditional_format","range":"C2:C7","rule":{"kind":"top10","rank":2,"format":{"bold":True}}},{"op":"add_conditional_format","range":"A2:E7","rule":{"kind":"formula","formula":"=$C2>8","format":{"fillColor":"#FFFF00"}}}],None),
("clear_cf",[{"op":"add_conditional_format","range":"C2:C7","rule":{"kind":"blank","blank":True,"format":{"bold":True}}},{"op":"clear_conditional_formats"}],None),
("validation",[{"op":"set_data_validation","range":"A2:A7","validation":{"kind":"list","values":["North","South","East"]}},{"op":"set_data_validation","range":"C2:C7","validation":{"kind":"numberBetween","min":0,"max":100}},{"op":"set_data_validation","range":"F2:F7","validation":{"kind":"checkbox"}}],None),
("validation_listref",[{"op":"set_data_validation","range":"G2:G7","validation":{"kind":"listRef","range":"A2:A7"}},{"op":"set_data_validation","range":"H2:H7","validation":{"kind":"dateBetween","start":"2026-01-01","end":"2026-12-31"}},{"op":"set_data_validation","range":"I2","validation":{"kind":"formula","formula":"=I2>0"}}],None),
("merge",[{"op":"merge_cells","range":"G1:H1"}],None),
("unmerge",[{"op":"merge_cells","range":"G1:H1"},{"op":"unmerge_cells","range":"G1:H1"}],None),
("row_col_size",[{"op":"set_row_height","row":1,"heightPoints":30},{"op":"set_col_width","column":"A","widthPx":150}],None),
("hidden",[{"op":"set_rows_hidden","row":3,"count":2,"hidden":True},{"op":"set_cols_hidden","column":"D","hidden":True}],None),
("freeze",[{"op":"set_freeze","rows":2,"columns":1}],None),
("filter",[{"op":"set_filter","range":"A1:E7"}],None),
("filter_criteria",[{"op":"clear_filter"},{"op":"set_filter","range":"A1:E7"}],None),
("page_setup",[{"op":"set_page_setup","orientation":"landscape","paperSize":9,"fitToWidth":1,"fitToHeight":0,"margins":"narrow","printGridlines":True,"printArea":"A1:E7","printTitles":"$1:$1","header":{"center":"Sales"},"footer":{"right":"&P of &N"},"rowBreaks":[4]}],None),
("protect",[{"op":"protect_sheet","protected":True,"password":"pw","allow":{"sort":True,"autoFilter":True}}],None),
("hyperlink_note",[{"op":"set_hyperlink","address":"A1","target":"https://example.com"},{"op":"set_note","address":"B1","text":"A note"}],None),
("defined_name",[{"op":"add_defined_name","name":"QtyCol","ref":"base!$C$2:$C$7"},{"op":"set_formula","address":"G1","formula":"=SUM(QtyCol)"}],"G1:G1"),
("add_table",[{"op":"add_table","range":"A1:E7","name":"Sales","style":"TableStyleMedium2","bandedRows":True}],None),
("add_pivot",[{"op":"add_sheet","name":"Piv"}],None),
("chart_column",[{"op":"add_chart","chartType":"column","dataRange":"A1:A7","title":"x"}],None),
("chart_combo",[{"op":"add_chart","chartType":"column","dataRange":"B1:D7","title":"Qty and price","anchorCell":"G2"}],None),
("chart_pie",[{"op":"add_chart","chartType":"pie","dataRange":"B1:C7","title":"Share"}],None),
("edit_chart",[{"op":"add_chart","chartType":"line","dataRange":"B1:C7","title":"T"}],None),
("image",[{"op":"add_image","path":PNG,"anchorCell":"G2"}],None),
("shape",[{"op":"add_shape","shapeType":"roundRect","anchorCell":"G2","fillColor":"#FFC000","text":"Hello"},{"op":"add_shape","shapeType":"textbox","anchorCell":"G8","text":"Box"}],None),
("sparkline",[{"op":"add_sparkline","type":"column","dataRange":"C2:D7","color":"#C00000"}],None),
("insert_rows",[{"op":"insert_rows","row":3,"count":2},{"op":"set_cell","address":"A3","value":"new"}],"A1:A8"),
("delete_rows_cols",[{"op":"delete_rows","row":2,"count":1},{"op":"insert_cols","column":"B","count":1},{"op":"delete_cols","column":"A","count":1}],"A1:E7"),
("sheets",[{"op":"add_sheet","name":"Two"},{"op":"rename_sheet","sheet":"Two","name":"Second"},{"op":"duplicate_sheet","sheet":"base","name":"Copy"},{"op":"move_sheet","sheet":"Copy","position":0},{"op":"set_sheet_hidden","sheet":"Second","hidden":True}],None),
("delete_sheet",[{"op":"add_sheet","name":"Tmp"},{"op":"delete_sheet","sheet":"Tmp"}],None),
]
only=sys.argv[1:]
for n,ops,rng in C:
    if only and n not in only: continue
    out=f"{W}/out/{n}.xlsx"; shutil.copy(f"{W}/base.xlsx",out)
    json.dump(ops,open(f"{W}/out/{n}.json","w"))
    r=g("sheet","apply",out,"--ops",f"{W}/out/{n}.json")
    d=r.get("detail") or {}
    line={"case":n,"status":r.get("status"),"summary":str(r.get("summary") or r.get("message"))[:130],"warn":str(d.get("warnings") or d.get("failures") or "")[:200]}
    if r.get("status") in("ok","partial"):
        a=["sheet","read",out]+(["--range",rng] if rng else [])
        rd=g(*a); dd=rd.get("detail",{})
        line["rows"]=json.dumps(dd.get("rows"))[:300] if rng else None
        line["formulas"]=json.dumps(dd.get("formulas"))[:200] if rng else None
        line["features"]=json.dumps(dd.get("features"))[:260]
    print(json.dumps(line,ensure_ascii=False))
