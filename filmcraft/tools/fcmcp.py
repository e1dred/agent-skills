#!/usr/bin/env python3
"""Call FilmCraft MCP tools against the live app (bridge) in one session.
Usage: python3 -I fcmcp.py '[["ui_inspect",{}],["ui_screenshot",{}]]' [--port 47828] [--img-dir DIR]
Needs FILMCRAFT_CONTROL_TOKEN in the environment, or FILMCRAFT_CONTROL_TOKEN_FILE naming a file that holds it.
FCCLI: path to filmcraft-cli (default: filmcraft-cli on PATH). LIM: characters printed per result line (default 4000; 0 = all).
Images in results are written to IMG-DIR/<n>_<tool>.png and replaced by their path."""
import base64, json, os, subprocess, sys

args = sys.argv[1:]
port, img_dir = "47828", "."
if "--port" in args: i = args.index("--port"); port = args[i + 1]; del args[i:i + 2]
if "--img-dir" in args: i = args.index("--img-dir"); img_dir = args[i + 1]; del args[i:i + 2]
calls = json.loads(args[0])
env = dict(os.environ)
if not env.get("FILMCRAFT_CONTROL_TOKEN"):
    env["FILMCRAFT_CONTROL_TOKEN"] = open(os.path.expanduser(env["FILMCRAFT_CONTROL_TOKEN_FILE"])).read().strip()
p = subprocess.Popen([env.get("FCCLI", "filmcraft-cli"), "mcp", "--bridge", "127.0.0.1:" + port],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, env=env)
def send(o): p.stdin.write(json.dumps(o) + "\n"); p.stdin.flush()
def recv(want):
    while True:
        line = p.stdout.readline()
        if not line: raise SystemExit("server closed")
        m = json.loads(line)
        if m.get("id") == want: return m
send({"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "fcmcp", "version": "1"}}})
recv(0); send({"jsonrpc": "2.0", "method": "notifications/initialized"})
os.makedirs(img_dir, exist_ok=True)
for n, (tool, a) in enumerate(calls, 1):
    send({"jsonrpc": "2.0", "id": n, "method": "tools/call", "params": {"name": tool, "arguments": a}})
    m = recv(n)
    out = []
    for c in (m.get("result") or {}).get("content", []):
        if c.get("type") == "image":
            f = os.path.join(img_dir, "%d_%s.png" % (n, tool)); open(f, "wb").write(base64.b64decode(c["data"])); out.append({"image": f})
        else: out.append(c.get("text"))
    line = json.dumps({"tool": tool, "args": a, "error": m.get("error") or (m.get("result") or {}).get("isError"), "out": out})
    lim = int(os.environ.get("LIM", "4000"))
    print(line[:lim] if lim else line)
p.stdin.close(); p.wait(timeout=10)
