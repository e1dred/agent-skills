"""Run ONLYOFFICE AI-tools calls against a document from the shell, when the MCP tools aren't loaded.

    python3 -I ooc.py "/abs/path/Doc.docx" calls.json      # calls.json: [["tool_name", {args}], ...]

Attaches to the document (LIVE if it is open in ONLYOFFICE Desktop), runs each call, then detaches with
close_document. Environment: OO_MCP (server command, default: onlyoffice-ai-mcp next to this file),
LIM (characters of each result to print, default 3000).
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.environ.get("OO_MCP", os.path.join(HERE, "onlyoffice-ai-mcp"))
doc, calls = sys.argv[1], json.load(open(sys.argv[2]))
lim = int(os.environ.get("LIM", "3000"))

p = subprocess.Popen([SERVER], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
n = [0]

def rpc(method, params=None):
    n[0] += 1
    msg = {"jsonrpc": "2.0", "id": n[0], "method": method}
    if params is not None:
        msg["params"] = params
    p.stdin.write(json.dumps(msg) + "\n")
    p.stdin.flush()
    while True:
        line = p.stdout.readline()
        if not line:
            sys.exit("ONLYOFFICE AI-tools server exited")
        r = json.loads(line)
        if r.get("id") == n[0]:
            return r

def tool(name, args):
    r = rpc("tools/call", {"name": name, "arguments": args})
    res = r.get("result", {})
    t = " | ".join(x.get("text", "<%s>" % x.get("type")) for x in res.get("content", []))
    return ("ERROR: " if res.get("isError") or "error" in r else "") + (t or json.dumps(r.get("error")))

rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "ooc", "version": "1"}})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
p.stdin.flush()
print("[attach]", tool("open_document", {"path": doc})[:90])
for name, args in calls:
    print(f"[{name}]", tool(name, args)[:lim])
print("[detach]", tool("close_document", {})[:60])
p.stdin.close()
