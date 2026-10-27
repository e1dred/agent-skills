import json,subprocess,shutil,sys,os,zipfile,re
W=os.path.dirname(os.path.abspath(__file__)); os.chdir(W)
def g(*a):
    r=subprocess.run(["genoffice",*a,"--json"],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return {"status":"nojson","raw":(r.stdout+r.stderr)[:300]}
def ids(f):
    d=g("slides","read",f)["detail"]; e=d["pages"][0]["elements"]; return [x["id"] for x in e]
def apply(f,ops,tag):
    p=f"out/{tag}.json"; json.dump(ops,open(p,"w")); r=g("slides","apply",f,"--ops",p)
    d=r.get("detail") or {}
    print(f"  {tag}: {r.get('status')} | {str(r.get('summary') or r.get('message'))[:90]} | {str(d.get('failures') or '')[:160]}")
    return r
def fresh(name):
    f=f"out/{name}.pptx"; shutil.copy("base.pptx",f); return f
def run(name,stage1,stage2=None):
    f=fresh(name); T,B,E=ids(f)
    apply(f,stage1(T,B,E),name+"-1")
    if stage2:
        now=ids(f); apply(f,stage2(now,T,B,E),name+"-2")
    return f
R="slide"
M=lambda x:{"slide":0,"el":x}
cases={
"setText":lambda T,B,E:[{"op":"setText","target":M(T),"paragraphs":[{"runs":[{"text":"Hello ","bold":True},{"text":"world","italic":True,"fontSize":20,"color":"#C00000"}],"align":"center"},{"runs":[{"text":"bullet"}],"bullet":"char","level":1}]}],
"setFont":lambda T,B,E:[{"op":"setFont","target":M(B),"font":{"fontFamily":"Georgia","fontSizePt":24,"bold":True,"color":"#FFC000"}}],
"setParagraphFormat":lambda T,B,E:[{"op":"setParagraphFormat","target":M(T),"format":{"align":"right","lineSpacingPct":150,"spaceAfterPt":12}}],
"insertEquation":lambda T,B,E:[{"op":"insertEquation","target":M(T),"latex":"E=mc^2"}],
"setFill":lambda T,B,E:[{"op":"setFill","target":M(B),"fill":{"stops":[{"pos":0,"color":"#1F4E79"},{"pos":1,"color":"#9DC3E6"}],"angle":90}},{"op":"setFill","target":M(E),"fill":"none"}],
"setStroke":lambda T,B,E:[{"op":"setStroke","target":M(B),"stroke":{"color":"#FFC000","widthEmu":38100}},{"op":"setStroke","target":M(E),"stroke":None}],
"setTransform":lambda T,B,E:[{"op":"setTransform","target":M(B),"box":{"x":914400,"y":3200400,"cx":2000000,"cy":900000},"rotDeg":15}],
"flip_reorder":lambda T,B,E:[{"op":"flipElements","target":{"slide":0},"els":[B],"axis":"h"},{"op":"reorderElement","target":M(B),"dir":"front"}],
"setShapeGeometry":lambda T,B,E:[{"op":"setShapeGeometry","target":M(B),"prst":"hexagon"},{"op":"setShapeAdjust","target":M(E),"adjust":{"adj":25000}}],
"customGeometry":lambda T,B,E:[{"op":"setShapeCustomGeometry","target":M(E),"path":{"w":100,"h":100,"cmds":[{"op":"M","pts":[0,100]},{"op":"L","pts":[50,0]},{"op":"L","pts":[100,100]},{"op":"Z","pts":[]}]}}],
"textAnchor_body":lambda T,B,E:[{"op":"setTextAnchor","target":M(B),"anchor":"bottom"},{"op":"setTextBodyProps","target":M(B),"props":{"vert":"vert","autofit":"shrink","insets":{"l":182880,"t":91440}}}],
"effects":lambda T,B,E:[{"op":"setEffects","target":M(B),"effects":{"shadow":{"color":"#00000080","blurRad":76200,"dist":38100,"dirDeg":45},"glow":{"color":"#FFC000","radius":101600},"softEdge":63500}}],
"setLink":lambda T,B,E:[{"op":"setLink","target":M(B),"link":{"kind":"url","url":"https://example.com"}},{"op":"setLink","target":M(E),"link":{"kind":"slide","slideIndex":1}}],
"align_distribute":lambda T,B,E:[{"op":"alignElements","target":{"slide":0},"els":[B,E],"mode":"top"},{"op":"distributeElements","target":{"slide":0},"els":[T,B,E],"axis":"vertical"}],
"group":lambda T,B,E:[{"op":"groupElements","target":{"slide":0},"els":[B,E]}],
"deleteElement":lambda T,B,E:[{"op":"deleteElement","target":M(E)}],
"addElement_kinds":lambda T,B,E:[{"op":"addElement","target":{"slide":1},"kind":"roundRect","offset":{"x":914400,"y":914400,"cx":2000000,"cy":900000},"fill":"#00B0F0","adjustments":{"adj":30000}},{"op":"addElement","target":{"slide":1},"kind":"star5","offset":{"x":3200400,"y":914400,"cx":900000,"cy":900000},"fill":"#FFC000"},{"op":"addElement","target":{"slide":1},"kind":"lineArrow","offset":{"x":914400,"y":2400000,"cx":3000000,"cy":0},"stroke":{"color":"#000000","widthEmu":19050}}],
"addConnector":lambda T,B,E:[{"op":"addConnector","target":{"slide":0},"from":B,"to":E,"kind":"elbow","arrow":"end","line":{"color":"#C00000","widthPt":2}}],
"addTable":lambda T,B,E:[{"op":"addTable","target":{"slide":1},"rows":3,"cols":3,"offset":{"x":914400,"y":914400,"cx":7315200,"cy":1500000}}],
"addChart":lambda T,B,E:[{"op":"addChart","target":{"slide":1},"kind":"bar","categories":["Q1","Q2","Q3"],"series":[{"name":"2025","values":[4,6,8]},{"name":"2026","values":[5,7,9]}],"offset":{"x":914400,"y":914400,"cx":5000000,"cy":3000000},"title":"Sales","colorScheme":["#1F4E79","#C00000"]},{"op":"addChart","target":{"slide":1},"kind":"pie","categories":["A","B"],"series":[{"name":"S","values":[30,70]}],"offset":{"x":6200000,"y":914400,"cx":3000000,"cy":3000000}},{"op":"addChart","target":{"slide":1},"kind":"comboBarLine","categories":["Q1","Q2"],"series":[{"name":"Rev","values":[4,6]},{"name":"Margin","values":[10,12]}],"offset":{"x":914400,"y":4000000,"cx":4000000,"cy":2500000}}],
"addSmartArt":lambda T,B,E:[{"op":"addSmartArt","target":{"slide":1},"layout":"process","items":["Plan","Build","Ship"],"offset":{"x":914400,"y":914400,"cx":7315200,"cy":1800000}}],
"slides_ops":lambda T,B,E:[{"op":"duplicateSlide","target":{"slide":0}},{"op":"addSlideWithLayout","target":{"slide":0},"layout":0},{"op":"moveSlide","target":{"slide":0},"to":1}],
"background":lambda T,B,E:[{"op":"setBackground","target":{"slide":0},"kind":"solid","color":"#F2F2F2"},{"op":"setBackground","target":{"slide":1},"kind":"gradient","from":"#1F4E79","to":"#9DC3E6","angleDeg":90}],
"hidden_trans_adv":lambda T,B,E:[{"op":"setHidden","target":{"slide":1},"hidden":True},{"op":"setTransition","target":{"slide":0},"kind":"fade"},{"op":"setAdvanceTime","target":{"slide":0},"ms":5000}],
"animation":lambda T,B,E:[{"op":"addAnimation","target":M(B),"effect":"fadeIn","trigger":"onClick","duration":500},{"op":"addAnimation","target":M(E),"effect":"zoomIn","trigger":"afterPrevious","delay":200}],
"notes_comment":lambda T,B,E:[{"op":"setNotes","target":{"slide":0},"text":"Speaker notes here"},{"op":"addComment","target":{"slide":0},"text":"Check the figure","author":"Reviewer"}],
"deck_ops":lambda T,B,E:[{"op":"findReplace","find":"Quarterly","replace":"Annual"},{"op":"setSlideSize","cx":9144000,"cy":6858000},{"op":"applyHeaderFooter","settings":{"footer":"Acme","slideNum":True}},{"op":"applyTheme","name":"Custom","colors":{"accent1":"#C00000"},"majorFont":"Georgia","minorFont":"Calibri"}],
"sections":lambda T,B,E:[{"op":"setSections","sections":[{"id":"sec1","name":"Intro","slideIndices":[0]},{"id":"sec2","name":"Rest","slideIndices":[1]}]}],
}
only=sys.argv[1:]
for n,fn in cases.items():
    if only and n not in only: continue
    print(n); run(n,fn)
# staged
def st(name,s1,s2,tag=None):
    if only and name not in only: return
    print(name); run(name,s1,s2)
def tbl(name,s2):
    if only and name not in only: return
    print(name); f=fresh(name); T,B,E=ids(f)
    apply(f,[{"op":"addTable","target":{"slide":1},"rows":3,"cols":3,"offset":{"x":914400,"y":914400,"cx":7315200,"cy":1500000}}],name+"-1")
    d=g("slides","read",f)["detail"]["pages"][1]["elements"]; X=d[0]["id"]
    apply(f,s2(X),name+"-2")
    return f
P=lambda t:[{"runs":[{"text":t}]}]
tbl("table_ops",lambda X:[{"op":"setTableCell","target":{"slide":1,"el":X},"row":0,"col":0,"paragraphs":[{"runs":[{"text":"Head","bold":True}]}]},{"op":"setTableCell","target":{"slide":1,"el":X},"row":1,"col":1,"paragraphs":P("cell")},{"op":"tableStructure","target":{"slide":1,"el":X},"kind":"insert-row","index":1},{"op":"tableStructure","target":{"slide":1,"el":X},"kind":"insert-col","index":2},{"op":"tableMerge","target":{"slide":1,"el":X},"kind":"merge-right","row":2,"col":0},{"op":"setTableRowHeight","target":{"slide":1,"el":X},"row":0,"hEmu":600000},{"op":"setTableColWidth","target":{"slide":1,"el":X},"col":0,"wEmu":3000000},{"op":"setTableCellAnchor","target":{"slide":1,"el":X},"row":0,"col":0,"anchor":"middle"},{"op":"setTableStyle","target":{"slide":1,"el":X},"firstRow":True,"bandRow":True,"shadingColor":"#1F4E79","borderColor":"#FFFFFF","borderWidthPt":1}])
tbl("table_font",lambda X:[{"op":"setFont","target":{"slide":1,"el":X},"font":{"bold":True,"fontSizePt":18}}])
