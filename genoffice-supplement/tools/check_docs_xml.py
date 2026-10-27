import zipfile,re,sys
def x(case,part="word/document.xml"):
    z=zipfile.ZipFile(f"out/{case}.docx"); return z.read(part).decode() if part in z.namelist() else ""
def names(case): return zipfile.ZipFile(f"out/{case}.docx").namelist()
checks={
 "setFont":lambda:[m for m in ["<w:b/>","C00000","w:sz w:val=\"28\"","Georgia"] if m in x("setFont")],
 "setParagraphFormat":lambda:[m for m in ['w:jc w:val="both"','w:line="360"','w:firstLine="360"','w:after="240"','w:shd','w:pBdr','w:tab ','w:leader="dot"'] if m in x("setParagraphFormat")],
 "setMatchedFont":lambda:[m for m in ["w:highlight"] if m in x("setMatchedFont")],
 "setList":lambda:[m for m in ["w:numPr"] if m in x("setList")],
 "moveBlocks":lambda:re.findall(r"<w:t[^>]*>([^<]*)</w:t>",x("moveBlocks"))[:3],
 "insertToc":lambda:["TOC" in x("insertToc"), "w:fldChar" in x("insertToc") or "w:fldSimple" in x("insertToc")],
 "insertField-SEQ":lambda:re.findall(r"SEQ[^<]*",x("insertField-SEQ")),
 "insertField-DATE":lambda:re.findall(r"DATE[^<]*",x("insertField-DATE")),
 "insertField-MERGEFIELD":lambda:re.findall(r"MERGEFIELD[^<]*",x("insertField-MERGEFIELD")),
 "bookmark+REF":lambda:re.findall(r"bookmarkStart[^>]*|REF [^<]*",x("bookmark+REF")),
 "setTableCellFormat":lambda:[m for m in ["1F4E79",'w:vAlign w:val="center"',"w:tcBorders"] if m in x("setTableCellFormat")],
 "setTableStyle":lambda:re.findall(r'<w:tblStyle [^>]*>|<w:tblLook[^>]*>',x("setTableStyle")),
 "applyStyle":lambda:re.findall(r'<w:pStyle w:val="Callout"/>',x("applyStyle")),
 "insert_image":lambda:["<w:drawing" in x("insert_image"), [n for n in names("insert_image") if "media" in n]],
 "insert_picture":lambda:["wp:anchor" in x("insert_picture"),"square" in x("insert_picture"),'descr="sample"' in x("insert_picture")],
 "insert_text_box":lambda:["wps:txbx" in x("insert_text_box") or "w:txbxContent" in x("insert_text_box"),"FFF2CC" in x("insert_text_box")],
 "insert_chart":lambda:[n for n in names("insert_chart") if "chart" in n],
 "set_header_footer":lambda:[n for n in names("set_header_footer") if "header" in n or "footer" in n],
 "hf-first-even":lambda:["titlePg" in x("hf-first-even"),"evenAndOddHeaders" in x("hf-first-even","word/settings.xml")],
 "set_page_setup":lambda:re.findall(r'<w:pgSz[^>]*>|<w:cols[^>]*>|<w:pgNumType[^>]*>|<w:pgMar[^>]*>',x("set_page_setup")),
 "insert_section_break":lambda:re.findall(r'<w:sectPr.*?</w:sectPr>',x("insert_section_break"),re.S).__len__(),
 "set_watermark":lambda:["DRAFT" in "".join(x("set_watermark",p) for p in names("set_watermark") if "header" in p)],
 "add_comment":lambda:[n for n in names("add_comment") if "comment" in n],
 "footnote":lambda:[n for n in names("footnote") if "note" in n],
 "properties":lambda:[("Jane Doe" in x("properties","docProps/core.xml")),("Finance" in x("properties","docProps/custom.xml"))],
 "content_control":lambda:["w:sdt>" in x("content_control"),"sdtLocked" in x("content_control") or "w:lock" in x("content_control")],
}
for k,f in checks.items():
    try: print(k,"=>",f())
    except Exception as e: print(k,"ERR",e)
