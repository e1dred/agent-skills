"""List the parameters of ONLYOFFICE AI-tools (MCP) tools straight from the stdio server, without the MCP tools being loaded.

    python3 -I ooschema.py docx|xlsx|pptx [tool_name ...]      # no names: every tool of that document type's group

A blank document of that type is created first (the server only advertises the tool group of the open document type), the schemas are printed as
`name  REQUIRED[...]  param=default, ...` plus the first line of the description, and the document is closed. Uses `onlyoffice-ai-mcp` next to this file
(override with OO_MCP). Handy before writing a `calls.json` for ooc.py: parameter names differ from what you would guess (e.g. `rows`/`cols`,
`new_value`, `inputY`).
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
fmt, want = sys.argv[1], set(sys.argv[2:])
p = subprocess.Popen([os.environ.get("OO_MCP", os.path.join(HERE, "onlyoffice-ai-mcp"))], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.DEVNULL, text=True)
n = [0]


def rpc(method, params=None):
    n[0] += 1
    msg = {"jsonrpc": "2.0", "id": n[0], "method": method}
    if params is not None:
        msg["params"] = params
    p.stdin.write(json.dumps(msg) + "\n"); p.stdin.flush()
    while True:
        r = json.loads(p.stdout.readline())
        if r.get("id") == n[0]:
            return r


rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "ooschema", "version": "1"}})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n"); p.stdin.flush()
rpc("tools/call", {"name": "create_document", "arguments": {"format": fmt, "discard_unsaved": True}})
prefix = {"docx": ("word_", "form_"), "xlsx": ("cell_",), "pptx": ("slide_",)}[fmt]
for t in rpc("tools/list")["result"]["tools"]:
    if (want and t["name"] in want) or (not want and t["name"].startswith(prefix)):
        sch = t["inputSchema"]
        props = ", ".join("%s=%r" % (k, v.get("default", "?")) for k, v in sch.get("properties", {}).items())
        print("%s  REQUIRED%s\n   %s\n   %s" % (t["name"], sch.get("required", []), props[:400], t["description"].strip().splitlines()[0][:160]))
rpc("tools/call", {"name": "close_document", "arguments": {}})
