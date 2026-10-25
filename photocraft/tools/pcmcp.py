"""Talk to a running PhotoCraft app through its MCP bridge from the shell, when the `photocraft` MCP tools are not loaded in the session.

    python3 -I pcmcp.py PORT calls.json          # calls.json: [["tool_name", {args}], ...]

Starts `photocraft-cli mcp --bridge 127.0.0.1:PORT --control-token-file FILE`, runs each call, prints the result (first LIM characters,
default 600) and saves screenshots (tool results that contain an image) as /tmp/pcshot_<n>_<i>.png. Environment: PCCLI (path to photocraft-cli,
default ~/AppImages/photocraft-cli), PHOTOCRAFT_CONTROL_TOKEN_FILE (default ~/.config/photocraft/control.token), LIM.
The app must have been started with `--control PORT --control-token-file FILE [--automation-read-root DIR --automation-write-root DIR]`; the
CLI must be the same version as the app (0.16.0 needs the 0.16.0 CLI). With `--bridge` the CLI refuses --automation-*-root flags: set those on the app.
Example calls: [["doc_open",{"path":"~/Pictures/x.png"}],["command_batch",{"steps":[{"id":"layer.duplicate","params":{"name":"Work"}}]}],["ui_screenshot",{"max_side":700}]]
"""
import base64, json, os, subprocess, sys

port, calls = sys.argv[1], json.load(open(sys.argv[2]))
lim = int(os.environ.get("LIM", "600"))
cli = os.environ.get("PCCLI", os.path.expanduser("~/AppImages/photocraft-cli"))
tok = os.environ.get("PHOTOCRAFT_CONTROL_TOKEN_FILE", os.path.expanduser("~/.config/photocraft/control.token"))
p = subprocess.Popen([cli, "mcp", "--bridge", "127.0.0.1:" + port, "--control-token-file", tok],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
n = [0]


def rpc(method, params=None):
    n[0] += 1
    msg = {"jsonrpc": "2.0", "id": n[0], "method": method}
    if params is not None:
        msg["params"] = params
    p.stdin.write(json.dumps(msg) + "\n"); p.stdin.flush()
    while True:
        line = p.stdout.readline()
        if not line:
            sys.exit("server exited: " + p.stderr.read()[:400])
        r = json.loads(line)
        if r.get("id") == n[0]:
            return r


rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "pcmcp", "version": "1"}})
p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n"); p.stdin.flush()
for name, args in calls:
    r = rpc("tools/call", {"name": name, "arguments": args})
    res, parts = r.get("result", {}), []
    for i, x in enumerate(res.get("content", [])):
        if x.get("type") == "image":
            fn = "/tmp/pcshot_%d_%d.png" % (n[0], i)
            open(fn, "wb").write(base64.b64decode(x["data"])); parts.append("<image saved %s>" % fn)
        else:
            parts.append(x.get("text", ""))
    print("[%s]%s %s" % (name, " ERR" if res.get("isError") else "", (" | ".join(parts) or json.dumps(r.get("error")))[:lim]))
