"""Compare WordCraft and GenOffice builds of every style x kind: page counts and the mean absolute pixel difference of page 1..n.
Run in a work directory after build_pair.sh has produced wc-*/go-* renders (r-wc-STYLE-KIND, r-go-STYLE-KIND). Needs Pillow."""
import glob
from PIL import Image, ImageChops, ImageStat
STYLES = "traditional elegant clean professional academic modern stylish creative".split()
KINDS = ("doc", "report", "resume", "cv")
print("style         " + "   ".join(f"{k:12s}" for k in KINDS) + "   (pages WC/GO, mean page diff, 0 = identical)")
tot = []
for s in STYLES:
    row = []
    for k in KINDS:
        a = sorted(glob.glob(f"r-wc-{s}-{k}/*.png")); b = sorted(glob.glob(f"r-go-{s}-{k}/*.png"))
        d = []
        for pa, pb in zip(a, b):
            A = Image.open(pa).convert("L").resize((300, 424)); B = Image.open(pb).convert("L").resize((300, 424))
            d.append(ImageStat.Stat(ImageChops.difference(A, B)).mean[0])
        m = sum(d) / len(d) if d else -1; tot.append(m)
        row.append(f"{len(a)}/{len(b)} {m:4.1f}")
    print(f"{s:12s}  " + "   ".join(f"{x:12s}" for x in row))
print("overall mean", round(sum(tot) / len(tot), 1))
