"""Run a list of CadCraft commands headless in ONE `cadcraft-cli run` and get each result back as parsed JSON.

    from ccrun import run
    res = run([("circle", {"center": [0, 0], "radius": 5}), ("dimradius", {"handle": "{last}", "at": [12, 8]})],
              metric=True, save="out.dxf", export="out.pdf")
    res[0]["handle"]  # "100"

Handles are hex strings counted from 100 in creation order (dimensions, arrays, blocks, inserts each take one or more),
so read them from the results instead of guessing. "{last}" means the last handle returned (it names the SAME one if
used twice in a command). A failing command stops the run and nothing is saved: the error text is raised.
"""
import json, os, subprocess

CLI = os.environ.get("CADCRAFT_CLI", os.path.expanduser("~/AppImages/cadcraft-cli"))

def run(cmds, metric=True, save=None, export=None, file=None, cwd=None):
    args = [CLI, "run"] + ([file] if file else (["--metric"] if metric else []))
    for name, params in cmds:
        args += ["--cmd", f"{name} {json.dumps(params)}" if params is not None else name]
    if save: args += ["--save", save]
    if export: args += ["--export", export]
    p = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    out = []
    for line in p.stdout.splitlines():
        try: out.append(json.loads(line))
        except ValueError: pass          # "wrote x.dxf (n bytes)" lines
    if p.returncode: raise RuntimeError((p.stderr or p.stdout).strip()[-400:])
    return out
