"""Find the four TRUE corners of a bright page (paper, certificate, card) lying on a darker background, for image.perspectiveCrop.

    python3 -I pagecorners.py upright.png [THRESH=150]

Method: threshold the bright page, take its OUTER silhouette (first/last bright pixel of every row and column, so inner dark lines
such as a printed border do not count), find a rough rectangle (minimal-area rotated box), fit a straight line along each of the four
sides from the silhouette points (least squares, outliers dropped three times) and intersect neighbouring lines. Unlike a plain
rotated box this keeps the keystone (trapezoid) distortion of a page photographed at an angle, which is what perspectiveCrop removes.
Prints the corners [c0..c3] in the order of the rough box (clockwise or not: reorder them for perspectiveCrop, see the photocraft skill),
the four side lengths, and writes overlay.png with the quad drawn: LOOK at it before using the corners. Needs only PIL.

IMPORTANT: feed it the image as PhotoCraft sees it (`photocraft-cli convert photo.jpg upright.png`), NOT the raw JPEG: phone photos
carry an EXIF orientation tag that PhotoCraft applies and PIL does not, so corners found on the raw file are in the wrong frame.
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
rect = [((u * c - v * s), (u * s + v * c)) for u, v in ((u0, v0), (u1, v0), (u1, v1), (u0, v1))]

edge = set()
for y in range(H):
    xs = [x for x in range(W) if px[x, y]]
    if xs:
        edge.update([(xs[0], y), (xs[-1], y)])
for x in range(W):
    ys = [y for y in range(H) if px[x, y]]
    if ys:
        edge.update([(x, ys[0]), (x, ys[-1])])


def fit(P):
    n = len(P)
    mx = sum(p[0] for p in P) / n
    my = sum(p[1] for p in P) / n
    sxx = sum((p[0] - mx) ** 2 for p in P)
    syy = sum((p[1] - my) ** 2 for p in P)
    sxy = sum((p[0] - mx) * (p[1] - my) for p in P)
    th = 0.5 * math.atan2(2 * sxy, sxx - syy)
    return mx, my, math.cos(th), math.sin(th)


lines = []
for i in range(4):
    p, q = rect[i], rect[(i + 1) % 4]
    L = math.dist(p, q)
    ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
    sel = [(x, y) for x, y in edge if 0.1 < ((x - p[0]) * ux + (y - p[1]) * uy) / L < 0.9 and abs(-(x - p[0]) * uy + (y - p[1]) * ux) < 30]
    ln = fit(sel)
    for _ in range(3):
        mx, my, dx, dy = ln
        sel = [t for t in sel if abs(-(t[0] - mx) * dy + (t[1] - my) * dx) < 2.5]
        ln = fit(sel)
    lines.append(ln)


def inter(l1, l2):
    x1, y1, dx1, dy1 = l1
    x2, y2, dx2, dy2 = l2
    d = dx1 * dy2 - dy1 * dx2
    t = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / d
    return x1 + t * dx1, y1 + t * dy1


cs = [(x * F, y * F) for x, y in (inter(lines[i - 1], lines[i]) for i in range(4))]
print(json.dumps([[round(x), round(y)] for x, y in cs]))
print("sides", [round(math.dist(cs[i], cs[(i + 1) % 4])) for i in range(4)])
ov = src.copy()
ImageDraw.Draw(ov).polygon(cs, outline="red", width=max(2, F))
ov.thumbnail((1000, 1000))
ov.save("overlay.png")
