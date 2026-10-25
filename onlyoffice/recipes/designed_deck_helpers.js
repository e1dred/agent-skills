// Helper library for ONLYOFFICE designed decks (slide_write_macro). Verified: 16:9, Arial, light palette.
// Paste at the top of ONE macro, then compose slides with header/card/chip/arrR/takeaway/footer (see SKILL.md).
// Units: EMU for positions/sizes (12700 = 1 pt), HALF-POINTS for font sizes, TWIPS for spacing after.
var SW=12192000, SH=6858000, M=850000, CW=SW-2*M;
function C(h){return Api.Color(h);} function SF(h){return Api.CreateSolidFill(C(h));}
function NS(){return Api.CreateStroke(0, Api.CreateNoFill());} function ST(w,h){return Api.CreateStroke(w, SF(h));}
var P={bg1:"#FFFFFF",bg2:"#EEF2F7",card:"#FFFFFF",line:"#D5DDE8",text:"#1B2533",muted:"#5B6B80",accent:"#2F6FD6",accent2:"#E0703A"};
var FONT="Arial";
function shp(sl,t,x,y,w,h,f,s){var o=Api.CreateShape(t,w,h,f||Api.CreateNoFill(),s||NS());o.SetPosition(x,y);sl.AddObject(o);return o;}
function adj(o,v){try{var g=o.GetGeometry();if(g&&g.SetAdjValue)g.SetAdjValue("adj",v);}catch(e){}}
function paras(o,ps,va,pad){var p0=(pad===undefined)?0:pad;o.SetPaddings(p0,p0,p0,p0);o.SetVerticalTextAlign(va||"top");var c=o.GetContent();c.RemoveAllElements();
 for(var i=0;i<ps.length;i++){var p=(i===0)?c.GetElement(0):Api.CreateParagraph();if(i===0)p.RemoveAllElements();p.SetJc(ps[i].a||"left");
  if(ps[i].sa!==undefined&&p.SetSpacingAfter)p.SetSpacingAfter(ps[i].sa);
  for(var j=0;j<ps[i].r.length;j++){var rr=ps[i].r[j],r=Api.CreateRun();r.AddText(rr.t);r.SetFontSize(rr.s||56);r.SetFill(SF(rr.c||P.text));r.SetFontFamily(rr.f||FONT);if(rr.b)r.SetBold(true);p.AddElement(r);}
  if(i>0)c.Push(p);}return o;}
function txt(sl,x,y,w,h,ps,va){return paras(shp(sl,"rect",x,y,w,h,Api.CreateNoFill(),NS()),ps,va);}
function header(sl,kick,title){shp(sl,"rect",M,398000,430000,36000,SF(P.accent));txt(sl,M+530000,300000,CW-530000,300000,[{r:[{t:kick,s:32,c:P.accent,b:true}]}]);txt(sl,M,610000,CW,700000,[{r:[{t:title,s:88,c:P.text,b:true}]}]);}
function footer(sl,n){shp(sl,"rect",M,6350000,CW,12700,SF(P.line));txt(sl,M,6430000,5200000,300000,[{r:[{t:"Sample deck - designed route",s:28,c:P.muted}]}]);txt(sl,SW-M-800000,6430000,800000,300000,[{a:"right",r:[{t:n,s:28,c:P.accent,b:true}]}]);}
function card(sl,x,y,w,h,title,body){var o=shp(sl,"roundRect",x,y,w,h,SF(P.card),ST(12700,P.line));adj(o,8000);
 paras(o,[{sa:160,r:[{t:title,s:44,c:P.accent,b:true}]},{r:[{t:body,s:32,c:P.text}]}],"top",180000);return o;}
function chip(sl,x,y,w,h,t){var o=shp(sl,"roundRect",x,y,w,h,SF(P.card),ST(12700,P.accent));adj(o,30000);paras(o,[{a:"center",r:[{t:t,s:36,c:P.text,b:true}]}],"center",60000);return o;}
function arrR(sl,x,y){return shp(sl,"rightArrow",x,y,260000,180000,SF(P.accent2),NS());}
function takeaway(sl,y,t){shp(sl,"rect",M,y,60000,420000,SF(P.accent));txt(sl,M+200000,y+20000,CW-200000,400000,[{r:[{t:t,s:44,c:P.text,b:true}]}]);}
var pres=Api.GetPresentation(),master=pres.GetMaster(0);
var blank=master.GetLayoutByType("blank")||master.GetLayout(0);
function newSlide(){var s=Api.CreateSlide();s.ApplyLayout(blank);pres.AddSlide(s);return s;}
master.SetBackground(SF(P.bg2));
