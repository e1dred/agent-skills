"""Add (MORE) and (CONT'D) where a speech is split by a page break. Two passes with WordCraft's own layout; needs wordcraft-cli and pdftotext.

    python3 -I screenplay_paginate.py --text=/abs/script.txt --out=/abs/script.paginated.txt [--title= --author= --draft= --scene-numbers ...]

Builds the script, converts it to PDF, reads where each page ends, and when a speech continues on the next page it splits the speech there:
the first part is followed by `(MORE)` (indented like a cue) and the next page starts with `NAME (CONT'D)`. Adding those lines can move
the break again, so it repeats (up to 5 times) until no speech is split without them. The result is a text file in the same markup: build the
final .docx from it with `build_wordcraft.py x screenplay out.docx --text=script.paginated.txt`. Page breaks depend on the layout engine: another
app or a later edit can move them, so re-run this after editing; ONLYOFFICE and Word may break pages differently from WordCraft.
Environment: WORDCRAFT_CLI (default: wordcraft-cli on PATH, else ~/AppImages/wordcraft-cli).
"""
import os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from plan import make, parse_argv
from screenplay_export import fountain

CLI = os.environ.get("WORDCRAFT_CLI") or shutil.which("wordcraft-cli") or os.path.expanduser("~/AppImages/wordcraft-cli")


def page_words(text_path, o, tmp):
    """Build the script with WordCraft, return a list of per-page word lists (script pages only: the title page is dropped)."""
    import json
    o = dict(o, text=text_path)
    docx, pdf, job = (os.path.join(tmp, n) for n in ("p.docx", "p.pdf", "job.json"))
    for f in (docx, pdf):
        if os.path.exists(f): os.remove(f)
    argv = [sys.argv[0], "x", "screenplay", docx, "--overwrite"] + ["--%s=%s" % (k, v) for k, v in o.items() if isinstance(v, str)] + \
           ["--" + k.replace("_", "-") for k, v in o.items() if v is True]
    with open(job, "w") as f:
        subprocess.run([sys.executable, "-I", os.path.join(HERE, "build_wordcraft.py")] + argv[1:], stdout=f, stderr=subprocess.DEVNULL, check=True)
    subprocess.run([CLI, "run", "--script", job], capture_output=True, check=True)
    subprocess.run([CLI, "convert", docx, pdf], capture_output=True, check=True)
    n = int(re.search(r"(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.split("Pages:")[1]).group(1))
    pages = []
    for p in range(2, n + 1):                      # page 1 is the title page
        t = subprocess.run(["pdftotext", "-raw", "-f", str(p), "-l", str(p), pdf, "-"], capture_output=True, text=True).stdout.split()
        if p > 2 and t and re.fullmatch(r"\d+\.", t[0]): t = t[1:]     # the page number in the header
        pages.append(t)
    return pages


def last_line_words(pdf_path, page):
    t = subprocess.run(["pdftotext", "-layout", "-f", str(page), "-l", str(page), pdf_path, "-"], capture_output=True, text=True).stdout
    lines = [l for l in t.split("\n") if l.strip()]
    return len(lines[-1].split()) if lines else 0


def repair(items, pages):
    """Merge back any (MORE) that is not the last line of its page (the break moved after it was added). Returns (items, True) or (None, False)."""
    occ = [(pi, w.index("(MORE)") == len(w) - 1) for pi, w in enumerate(pages) if "(MORE)" in w]
    more_idx = [i for i, (k, v) in enumerate(items) if k == "more"]
    for (pi, at_end), i in zip(occ, more_idx):
        nxt = pages[pi + 1][:8] if pi + 1 < len(pages) else []
        if not at_end or "(CONT'D)" not in nxt:
            # items[i-1] = first part (dial), items[i] = (MORE), items[i+1] = cue, items[i+2] = rest
            if items[i - 1][0] == "dial" and i + 2 < len(items) and items[i + 1][0] == "char" and items[i + 2][0] == "dial":
                return items[:i - 1] + [("dial", items[i - 1][1] + " " + items[i + 2][1])] + items[i + 3:], True
    return None, False


def split_once(items, pages, pdf_path):
    for pi in range(len(pages) - 1):
        a, b = pages[pi], pages[pi + 1]
        for i, (k, v) in enumerate(items):
            if k != "dial": continue
            w = v.split()
            if len(w) < 4: continue
            for cut in range(2, len(w) - 1):          # at least two words each side
                if a[-cut:] == w[:cut] and b[:len(w) - cut] == w[cut:]:
                    cut2 = cut - last_line_words(pdf_path, pi + 2)    # (MORE) needs the last line of the page
                    if cut2 < 2 or cut2 >= len(w): cut2 = cut
                    name = next(vv for kk, vv in reversed(items[:i]) if kk == "char")
                    base = re.sub(r"\s*\(CONT'D\)", "", name)
                    return items[:i] + [("dial", " ".join(w[:cut2])), ("more", "(MORE)"), ("char", base + " (CONT'D)"), ("dial", " ".join(w[cut2:]))] + items[i + 1:]
    return None


if __name__ == "__main__":
    out = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--out=")), None)
    rest = [a for a in sys.argv[1:] if not a.startswith("--out=")]
    if not out or os.path.exists(out): sys.exit("give --out=/abs/new-file.txt (it must not exist)")
    style, kind, outp, o, flags = parse_argv(["x", "x", "screenplay", "/dev/null"] + rest)
    for f in flags: o[f.replace("-", "_")] = True
    if not o.get("text"): sys.exit("give --text=/abs/script.txt")
    sp = make("x", "screenplay", o)["sp"]
    tmp = tempfile.mkdtemp()
    cur = o["text"]
    pdf = os.path.join(tmp, "p.pdf")
    for it in range(8):
        pages = page_words(cur, {k: v for k, v in o.items() if k != "text"}, tmp)
        items, merged = repair(sp["items"], pages)
        if items is None:
            items = split_once(sp["items"], pages, pdf)
        if items is None: break
        sp["items"] = items
        cur = os.path.join(tmp, "cur.txt")
        with open(cur, "w", encoding="utf-8") as f: f.write(fountain(sp))
    with open(out, "w", encoding="utf-8") as f: f.write(fountain(sp))
    print("%d speech(es) split across a page break with (MORE)/(CONT'D); wrote %s" % (sum(1 for k, _ in sp["items"] if k == "more"), out))
