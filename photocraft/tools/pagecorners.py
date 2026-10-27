"""Find the four corners of a bright page (paper, certificate, card) lying on a darker background, for image.perspectiveCrop.

    python3 -I pagecorners.py upright.png [THRESH=150]

Prints the corners in the order that makes the page UPRIGHT only if it already lies the right way up; otherwise reorder them (see the
photocraft skill, 'Perspective crop of a tilted page'). Output: minimal-area rotated rectangle around the bright pixels
(document px of the input image) plus its side lengths, and writes overlay.png (in the current folder) with the rectangle drawn so
you can LOOK at it. Needs only PIL.

IMPORTANT: feed it the image as PhotoCraft sees it (`photocraft-cli convert photo.jpg upright.png`), NOT the raw JPEG: phone photos
carry an EXIF orientation tag that PhotoCraft applies and PIL does not, so the corners found on the raw file are in the wrong frame.
"""
import json, math, sys
from PIL import Image, ImageDraw, ImageFilter

src = Image.open(sys.argv[1]).convert("RGB")
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 150
F = max(1, max(src.size) // 1000)
g = src.convert("L").resize((src.width // F, src.height // F))
m = g.point(lambda v: 255 if v > thr else 0).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(5))
W, H = m.size
px = m.load()
pts = [(x, y) for y in range(0, H, 2) for x in range(0, W, 2) if px[x, y]]
if not pts:
    sys.exit("no bright pixels: lower THRESH")
best = None
for a10 in range(0, 900, 5):
    a = math.radians(a10 / 10)
    c, s = math.cos(a), math.sin(a)
    us = [x * c + y * s for x, y in pts]
    vs = [-x * s + y * c for x, y in pts]
    area = (max(us) - min(us)) * (max(vs) - min(vs))
    if best is None or area < best[0]:
        best = (area, a, min(us), max(us), min(vs), max(vs))
_, a, u0, u1, v0, v1 = best
c, s = math.cos(a), math.sin(a)
back = lambda u, v: ((u * c - v * s) * F, (u * s + v * c) * F)
corners = [back(u0, v0), back(u1, v0), back(u1, v1), back(u0, v1)]
print(json.dumps([[round(x), round(y)] for x, y in corners]))
print("sides", round((u1 - u0) * F), "x", round((v1 - v0) * F), "angle", round(math.degrees(a), 1))
ov = src.copy()
d = ImageDraw.Draw(ov)
d.polygon([(x, y) for x, y in corners], outline="red", width=max(2, F))
ov.thumbnail((1000, 1000))
ov.save("overlay.png")
