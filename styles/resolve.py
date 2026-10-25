"""Resolve a style spec from styles.json against the fonts installed on this machine.

    python3 -I resolve.py                      # list the styles and the font chosen for each role
    python3 -I resolve.py modern               # one style, as JSON, fonts resolved
    python3 -I resolve.py modern --local-fonts # allow fonts that exist only on this machine

By default only fonts that also ship with Microsoft Office are chosen (PORTABLE), so a document opens the same
on a colleague's computer. --local-fonts lets any installed font win (e.g. Montserrat), which is only safe if
the document stays on this machine or the fonts are embedded. Import `resolve(name, portable=True)` from other scripts.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PORTABLE = {"Calibri", "Cambria", "Candara", "Century Gothic", "Consolas", "Constantia", "Corbel", "Georgia",
            "Arial", "Times New Roman", "Courier New", "Trebuchet MS", "Verdana", "Tahoma", "Impact"}


def installed():
    out = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True).stdout
    names = set()
    for line in out.splitlines():
        for part in line.split(","):
            names.add(part.strip())
    return names


def load():
    return {k: v for k, v in json.load(open(os.path.join(HERE, "styles.json"))).items() if not k.startswith("_")}


def pick(stack, have, portable):
    for f in stack:
        if f in have and (not portable or f in PORTABLE):
            return f
    for f in stack:  # nothing portable installed: fall back to any installed font in the list
        if f in have:
            return f
    return stack[-1]


def resolve(name, portable=True):
    spec = load()[name]
    have = installed()
    spec = json.loads(json.dumps(spec))
    spec["name"] = name
    spec["font"] = {role: pick(stack, have, portable) for role, stack in spec["fonts"].items()}
    spec["missing_preferred"] = [stack[0] for stack in spec["fonts"].values() if stack[0] not in have]
    return spec


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    portable = "--local-fonts" not in sys.argv
    if args:
        print(json.dumps(resolve(args[0], portable), indent=1))
    else:
        for n in load():
            r = resolve(n, portable)
            print("%-13s heading=%-16s body=%-16s %s" % (n, r["font"]["heading"], r["font"]["body"],
                  ("(preferred font not installed: %s)" % ", ".join(r["missing_preferred"])) if r["missing_preferred"] else ""))
