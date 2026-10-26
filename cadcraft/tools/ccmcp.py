"""Talk to a RUNNING CadCraft window from the shell through its MCP bridge (stdio JSON-RPC), when the MCP tools are not loaded.

    CADCRAFT_HOST=127.0.0.1:PORT python3 -I ccmcp.py           # lists the tools
    from ccmcp import tool; tool("open", {"path": "/abs/x.dxf"}); tool("execute", {"command": "zoom", "params": {"mode": "extents"}})

Start the app with `cadcraft.appimage --control PORT`. Tools: command_line, script, execute, list_commands, inspect_drawing, query_entities, render,
find_text, new_drawing, open, save, cancel, screenshot, ui_inspect, ui_click. CADCRAFT_CLI = the cadcraft-cli binary (default ~/AppImages/cadcraft-cli).
"""
import os
import json,subprocess,sys
p=subprocess.Popen([os.environ.get('CADCRAFT_CLI', os.path.expanduser('~/AppImages/cadcraft-cli')),'mcp','--connect',os.environ.get('CADCRAFT_HOST','127.0.0.1:47827')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
n=[0]
def rpc(m,pr=None):
    n[0]+=1; msg={"jsonrpc":"2.0","id":n[0],"method":m}
    if pr is not None: msg["params"]=pr
    p.stdin.write(json.dumps(msg)+"\n"); p.stdin.flush()
    while True:
        l=p.stdout.readline()
        if not l: return {"error":"closed","stderr":p.stderr.read()[:300]}
        r=json.loads(l)
        if r.get("id")==n[0]: return r
def tool(name,args):
    r=rpc("tools/call",{"name":name,"arguments":args}); res=r.get("result",{})
    return " | ".join(x.get("text","<%s>"%x.get("type")) for x in res.get("content",[])) or json.dumps(r)[:300]
r=rpc("initialize",{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"c","version":"1"}})
p.stdin.write(json.dumps({"jsonrpc":"2.0","method":"notifications/initialized"})+"\n");p.stdin.flush()
if __name__=="__main__":
    t=rpc("tools/list")
    print([x['name'] for x in t.get('result',{}).get('tools',[])] or t)
