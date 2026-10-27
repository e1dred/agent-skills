"""Print the ops GenOffice documents, one per line as `editor op`, read from `genoffice guide docs|sheets|slides`.
Editor-only sheet ops and not-AI-callable slide ops are left out (they cannot run headless / are payload ops).
Used by ../coverage.sh and ../everyday.sh. Needs the genoffice CLI on PATH."""
import re, subprocess

def guide(*a):
    return subprocess.run(["genoffice", "guide", *a], capture_output=True, text=True).stdout

docs = guide("docs")
for n in sorted(set(re.findall(r"^  ([a-zA-Z_]+) [\{—]", docs, re.M))):
    print("docs", n)
sheets = guide("sheets").split("Editor-only")[0]
for n in sorted(set(re.findall(r"^  ([a-z_]+) [\{—]", sheets, re.M))):
    print("sheets", n)
sl = guide("slides")
vocab = re.search(r"Vocabulary:(.*)", sl, re.S).group(1)
names = set()
for line in vocab.splitlines():
    if line.startswith("- "):
        names |= set(re.findall(r"\b([a-z][A-Za-z0-9]+)\b", line.split(":", 1)[1]))
notai = set()
for g in ("element", "insert", "table", "slide", "deck", "text"):
    notai |= set(re.findall(r"### ([A-Za-z0-9]+) \(not-ai-callable\)", guide("slides", g)))
for n in sorted(names - notai):
    print("slides", n)
