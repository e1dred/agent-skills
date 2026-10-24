"""Call WordCraft MCP bridge tools on the live app from the shell, when the MCP tools aren't loaded.

    WORDCRAFT_PORT=7981 python3 -I wcmcp.py '[["ui_inspect",{}],["get_text",{}]]'

Environment: WORDCRAFT_PORT (default 7981), WORDCRAFT_CLI (default: wordcraft-cli on PATH),
LIM (characters of each result to print, default 4000). The app must run with `--control PORT`.
Can also be imported: `from wcmcp import tool` after setting the environment.
"""
import json, os, shutil, subprocess, sys

CLI = os.environ.get("WORDCRAFT_CLI") or shutil.which("wordcraft-cli") or os.path.expanduser("~/AppImages/wordcraft-cli")
PORT = os.environ.get("WORDCRAFT_PORT", "7981")

p = subprocess.Popen([CLI, "mcp", "--connect", f"127.0.0.1:{PORT}"],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
n = [0]

def rpc(method, params):
    n[0] += 1
    p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": n[0], "method": method, "params": params}) + "\n")
    p.stdin.flush()
    while True:
        line = p.stdout.readline()
        if not line:
            sys.exit(f"wordcraft-cli exited (is WordCraft running with --control {PORT}?)")
        m = json.loads(line)
        if m.get("id") == n[0]:
            return m

rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "wcmcp", "version": "1"}})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
p.stdin.flush()

def tool(name, args=None):
    r = rpc("tools/call", {"name": name, "arguments": args or {}})
    res = r.get("result", {})
    t = "\n".join(c.get("text", "<%s>" % c.get("type")) for c in res.get("content", []))
    if r.get("error") or res.get("isError"):
        t = "ERROR: " + (t or json.dumps(r.get("error")))
    return t

if __name__ == "__main__":
    lim = int(os.environ.get("LIM", "4000"))
    for name, args in json.loads(sys.argv[1]):
        print(f"[{name}]", tool(name, args)[:lim])
    p.stdin.close()
