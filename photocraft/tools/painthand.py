"""Hand-drawing helpers for a live PhotoCraft window: collect ui_pointer strokes (smooth, pressure-tapered) and tools.* brush calls, then flush() sends them through tools/pcmcp.py and takes a screenshot."""
import json,subprocess,os,math,random
PC=os.path.expanduser("~/agent-skills/photocraft/tools/pcmcp.py")
calls=[]
def cmd(i,**p): calls.append(["command_run",{"id":i,"params":p}])
def ui(**f): calls.append(["ui_set",{"fields":f}])
def color(c): cmd("tools.setColors",foreground=c)
def brush(size,preset="Soft Round",opacity=None,hard=None):
    p={"preset":preset,"size":size}
    cmd("tools.setBrush",**p)
def smooth(pts,n=6):
    # Catmull-Rom resample so the stroke is dense and smooth like a hand movement
    out=[]
    P=[pts[0]]+pts+[pts[-1]]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(n):
            t=k/n
            out.append(tuple(0.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t*t+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t**3) for j in range(2)))
    out.append(pts[-1]); return out
def hand(pts,pmax=1.0,pmin=0.25,jitter=0.35,n=6):
    S=smooth(pts,n); m=len(S); ev=[]
    for i,(x,y) in enumerate(S):
        p=pmin+(pmax-pmin)*math.sin(math.pi*i/(m-1))**0.7 if m>1 else pmax
        x+=random.uniform(-jitter,jitter); y+=random.uniform(-jitter,jitter)
        ev.append({"kind":"down" if i==0 else ("up" if i==m-1 else "move"),"x":round(x,2),"y":round(y,2),"pressure":round(p,3)})
    calls.append(["ui_pointer",{"events":ev}])
def flush(name,shot=1000,zoom=None):
    if zoom: calls.insert(0,["ui_set",{"fields":zoom}])
    calls.append(["ui_screenshot",{"max_side":shot}])
    json.dump(calls,open(name+".json","w"))
    r=subprocess.run(["python3","-I",PC,"47825",name+".json"],capture_output=True,text=True,env=dict(os.environ,LIM="160"))
    print("\n".join(l[:170] for l in r.stdout.splitlines()), r.stderr[-300:])
    calls.clear()
