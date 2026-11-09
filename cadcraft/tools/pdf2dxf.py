#!/usr/bin/env python3
"""Convert one vector architectural PDF page to a 1:1 real-world-inch DXF.

Usage: uv run --with pymupdf --with ezdxf python -I pdf2dxf.py IN.pdf OUT.dxf

Scale: plan is 3/32" = 1'-0", so 1 PDF point (1/72") = 128/72 inch real.
PDF y grows downward and is flipped, sheet lower-left lands on (0,0).
"""
import sys
import math
import json
from collections import Counter

import pymupdf
import ezdxf
from ezdxf.enums import TextEntityAlignment

K = 128.0 / 72.0          # real inches per PDF point
CAP = 0.716               # Arial cap height / em, used only to size wfactor
VALID_LW = [0, 5, 9, 13, 15, 18, 20, 25, 30, 35, 40, 50, 53, 60, 70, 80,
            90, 100, 106, 120, 140, 158, 200, 211]  # DXF valid values, 1/100 mm


def nearest_lw(pt_width):
    mm = (pt_width or 0.0) * 25.4 / 72.0 * 100.0  # -> 1/100 mm
    return min(VALID_LW, key=lambda v: abs(v - mm))


def rgb(c):
    if c is None:
        return None
    return tuple(max(0, min(255, int(round(v * 255)))) for v in c[:3])


def is_white(c):
    return c is not None and all(v >= 0.98 for v in c[:3])


def is_black(c):
    return c is not None and all(v <= 0.05 for v in c[:3])


def is_red(c):
    if c is None:
        return False
    r, g, b = c[:3]
    return r > 0.55 and g < 0.45 and b < 0.45


def is_gray(c):
    if c is None:
        return False
    r, g, b = c[:3]
    if max(r, g, b) - min(r, g, b) > 0.06:
        return False
    return r >= 0.55  # light gray


def bezier(p0, p1, p2, p3, n=8):
    out = []
    for i in range(1, n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        out.append((x, y))
    return out


def path_points(items, close):
    """Flatten a pymupdf path item list into PDF-space points (may be None)."""
    pts = []

    def add(p):
        q = (float(p[0]), float(p[1]))
        if not pts or abs(pts[-1][0] - q[0]) > 1e-9 or abs(pts[-1][1] - q[1]) > 1e-9:
            pts.append(q)

    for it in items:
        op = it[0]
        if op == "l":
            add(it[1]); add(it[2])
        elif op == "c":
            p0 = pts[-1] if pts else (it[1].x, it[1].y)
            for q in bezier((p0[0], p0[1]), (it[1].x, it[1].y),
                            (it[2].x, it[2].y), (it[3].x, it[3].y)):
                add(q)
        elif op == "re":
            r = it[1]
            add((r.x0, r.y0)); add((r.x1, r.y0)); add((r.x1, r.y1)); add((r.x0, r.y1))
            pts.append(pts[0])
        elif op == "qu":
            q = it[1]
            for p in (q.ul, q.ur, q.lr, q.ll):
                add((p.x, p.y))
            pts.append(pts[0])
        else:
            continue
    if close and pts and (abs(pts[0][0] - pts[-1][0]) > 1e-9 or
                          abs(pts[0][1] - pts[-1][1]) > 1e-9):
        pts.append(pts[0])
    return pts


def main(src, dst):
    doc = pymupdf.open(src)
    page = doc[0]
    W, H = page.rect.width, page.rect.height

    def tf(x, y):
        return (x * K, (H - y) * K)

    dxf = ezdxf.new("R2013", setup=False)
    dxf.header["$INSUNITS"] = 1
    dxf.header["$MEASUREMENT"] = 0
    dxf.header["$LUNITS"] = 4
    dxf.linetypes.add("DASHED", pattern=[0.75, 0.5, -0.25],
                      description="Dashed __ __ __")
    dxf.styles.add("ARCH", font="arial.ttf")

    layers = {
        "RED":    (1,  35),
        "GRAY":   (8,  9),
        "HEAVY":  (7,  30),
        "MEDIUM": (7,  13),
        "LIGHT":  (7,  9),
        "FILL":   (8,  0),
        "TEXT":   (3,  9),
    }
    for name, (col, lw) in layers.items():
        lay = dxf.layers.add(name)
        lay.color = col
        lay.dxf.lineweight = lw

    msp = dxf.modelspace()
    counts = Counter()
    skipped_white_fill = 0

    drawings = page.get_drawings()
    # White fills are the CAD viewport masks painted over the site plan; any
    # black/grey fill a later white one covers is invisible in the PDF, so it
    # must not become a visible hatch here either.
    white_rects = [(d.get("seqno", -1), d["rect"]) for d in drawings
                   if d.get("fill") is not None and is_white(d["fill"])]

    def covered_by_white(d):
        r = d.get("rect")
        if r is None or r.get_area() <= 0:
            return False
        c = pymupdf.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
        sq = d.get("seqno", -1)
        return any(wq > sq and wr.contains(c) for wq, wr in white_rects)

    for d in drawings:
        items = d.get("items") or []
        if not items:
            continue
        close = bool(d.get("closePath")) or d.get("type") in ("f", "fs")
        stroke = d.get("color")
        fill = d.get("fill")
        width = d.get("width") or 0.0
        dashes = d.get("dashes") or "[] 0"
        dashed = dashes.strip() not in ("[] 0", "[] 0.0", "")

        pts = path_points(items, close)
        if len(pts) < 2:
            continue
        pts = [tf(x, y) for (x, y) in pts]

        # --- stroke ---
        if stroke is not None:
            if is_red(stroke):
                layer = "RED"
            elif is_gray(stroke):
                layer = "GRAY"
            elif width >= 1.0:
                layer = "HEAVY"
            elif width >= 0.4:
                layer = "MEDIUM"
            else:
                layer = "LIGHT"
            ent = msp.add_lwpolyline(pts, close=close, dxfattribs={
                "layer": layer,
                "lineweight": nearest_lw(width),
            })
            c = rgb(stroke)
            if c is not None:
                ent.dxf.true_color = (c[0] << 16) | (c[1] << 8) | c[2]
            if dashed:
                ent.dxf.linetype = "DASHED"
            counts[layer] += 1
        elif fill is None:
            skipped_white_fill += 1

        # --- fill ---
        # The PDFs carry a couple of page-sized solid black rectangles (viewport
        # background masks, invisible in the PDF render - 5.2M and 0.44M pt2).
        # Hatching those would blacken the whole model space; drop them.
        if fill is not None and is_black(fill) and d["rect"].get_area() > 100000:
            counts["FILL_MASK_SKIPPED"] += 1
            continue
        if fill is not None and not is_white(fill) and covered_by_white(d):
            counts["FILL_HIDDEN_SKIPPED"] += 1
            continue
        if fill is not None and not is_white(fill):
            if len(pts) >= 3:
                h = msp.add_hatch(color=250, dxfattribs={"layer": "FILL"})
                h.set_solid_fill(color=250)
                c = rgb(fill)
                if c is not None:
                    h.dxf.true_color = (c[0] << 16) | (c[1] << 8) | c[2]
                h.paths.add_polyline_path(pts, is_closed=True, flags=1)
                counts["FILL"] += 1

    # --- text ---
    helv = pymupdf.Font("helv")
    ntext = 0
    tmax = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT)
    for block in tmax["blocks"]:
        for line in block.get("lines", []):
            dx, dy = line["dir"]
            rot = math.degrees(math.atan2(-dy, dx))
            rot = round(rot, 3) % 360
            if abs(rot) < 1e-3 or abs(rot - 360) < 1e-3:
                rot = 0.0
            for span in line["spans"]:
                text = span["text"]
                if not text.strip():
                    continue
                size = span["size"]
                height = size * K * 0.72
                ox, oy = span["origin"]
                x, y = tf(ox, oy)
                bb = span["bbox"]
                wfactor = 1.0
                if rot == 0.0:
                    target = (bb[2] - bb[0]) * K
                    adv = helv.text_length(text, fontsize=1.0)
                    pred = height * adv / CAP
                    if pred > 1e-6:
                        wfactor = max(0.4, min(1.5, target / pred))
                ent = msp.add_text(text, height=height, dxfattribs={
                    "layer": "TEXT",
                    "style": "ARCH",
                    "rotation": rot,
                    "width": wfactor,
                    "lineweight": nearest_lw(size * 0.10),  # ~0.1*size pt, paper mm
                })
                ent.set_placement((x, y), align=TextEntityAlignment.LEFT)
                col = span.get("color", 0)
                r = (col >> 16) & 255
                g = (col >> 8) & 255
                b = col & 255
                if (r, g, b) != (0, 0, 0):  # black stays black; layer colour is only a fallback
                    ent.dxf.true_color = (r << 16) | (g << 8) | b
                else:
                    ent.dxf.true_color = 0
                counts["TEXT"] += 1
                ntext += 1

    dxf.saveas(dst)
    info = {
        "src": src,
        "page_pt": [W, H],
        "pdf_paths": len(drawings),
        "pdf_fills": sum(1 for d in drawings if d.get("fill") is not None),
        "pdf_spans": ntext,
        "skipped_no_stroke_no_fill": skipped_white_fill,
        "layers": dict(counts),
        "entities": sum(counts.values()),
    }
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
