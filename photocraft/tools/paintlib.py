"""Helpers for painting from code with photocraft-cli: collect commands in `cmds`, then `run(out)` executes them in ONE `photocraft-cli run`.

smooth closed/open paths (Catmull-Rom handles), fills, selection-clipped shading, tapered pressure strokes, quadratic curves.
See the "Painting a portrait from code" section of photocraft/reference/painting-a-portrait.md for the lessons.
"""
import json,math,random,subprocess,os
CLI=os.path.expanduser("~/AppImages/photocraft-cli")
cmds=[]
def C(cmd,**p): cmds.append((cmd,p))
def knots(pts,closed=True,t=0.5):
    n=len(pts); out=[]
    for i,p in enumerate(pts):
        a=pts[(i-1)%n] if (closed or i>0) else p; b=pts[(i+1)%n] if (closed or i<n-1) else p
        dx,dy=(b[0]-a[0])*t/3*1.0,(b[1]-a[1])*t/3*1.0
        out.append({"anchor":[p[0],p[1]],"in":[p[0]-dx,p[1]-dy],"out":[p[0]+dx,p[1]+dy],"smooth":True})
    return out
def newlayer(name): C("layer.new.layer",name=name)
_n=[0]
def setpath(pts,name,closed=True,t=1.0): 
    _n[0]+=1; name=f'{name}{_n[0]}'
    C("path.set",path={"subpaths":[{"closed":closed,"knots":knots(pts,closed,t)}]}); C("path.rename",to=name)
def fill(pts,color,opacity=100,name="p",blur=0,t=1.0):
    setpath(pts,name,True,t); name=f'{name}{_n[0]}'; C("path.fill",name=name,color=color,opacity=opacity)
    if blur: C("filter.blur.gaussianBlur",radius=blur)
def sel(name,feather=0): C("path.toSelection",name=f'{name}{_n[0]}',feather=feather)
def desel(): C("select.deselect")
def stroke(pts,size,color,opacity=1.0,preset="Soft Round",flow=1.0,seed=1,pressure=None):
    P=[[x,y,(pressure if pressure is not None else 1.0)] if len(p:= (x,y))==2 else [x,y] for x,y in pts] if False else None
    C("paint.stroke",points=[[x,y,pressure if pressure is not None else 1.0] for x,y in pts],size=size,color=color,opacity=opacity,preset=preset,flow=flow,seed=seed)
def tstroke(pts,size,color,opacity=1.0,preset="Soft Round",taper=True,seed=1):
    n=len(pts); pr=[0.2+0.8*math.sin(math.pi*i/(n-1)) for i in range(n)] if taper else [1]*n
    C("paint.stroke",points=[[x,y,pr[i]] for i,(x,y) in enumerate(pts)],size=size,color=color,opacity=opacity,preset=preset,seed=seed)
def curve(p0,p1,p2,n=12):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0],(1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/(n-1) for i in range(n)]]
def run(out,w=1376,h=768,bg="#16313a",save=None):
    a=[CLI,"run","--new",json.dumps({"width":w,"height":h,"background":bg})]
    for c,p in cmds: a+=["--cmd",c,"--params",json.dumps(p)]
    a+=["--out",out]
    r=subprocess.run(a,capture_output=True,text=True)
    if r.returncode: print(r.stderr[-600:]); 
    return r
