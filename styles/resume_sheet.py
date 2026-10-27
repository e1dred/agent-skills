"""Make contact sheets of the résumé PNGs in a folder: sheet.png (every <style>-<a|b>.png, styles in rows) and sheet-nophoto.png
(the <style>-<a|b>-nophoto.png ones)."""
import os, sys
from PIL import Image, ImageDraw
d = sys.argv[1]
styles = ["traditional", "elegant", "clean", "professional", "academic", "modern", "stylish", "creative", "minimal"]


def sheet(suffix, out):
    cells = [(st, v) for st in styles for v in "ab" if os.path.exists(os.path.join(d, f"{st}-{v}{suffix}.png"))]
    if not cells: return
    w, h = 330, 440
    rows = (len(cells) + 1) // 2
    img = Image.new("RGB", (2 * w + 30, rows * (h + 24) + 6), "#777")
    dr = ImageDraw.Draw(img)
    for i, (st, v) in enumerate(cells):
        r, c = divmod(i, 2)
        im = Image.open(os.path.join(d, f"{st}-{v}{suffix}.png")).convert("RGB")
        im.thumbnail((w, h), Image.LANCZOS)
        img.paste(im, (10 + c * (w + 10), r * (h + 24) + 20))
        dr.text((12 + c * (w + 10), r * (h + 24) + 6), f"{st}-{v}{suffix}", fill="white")
    img.save(os.path.join(d, out)); print(out)


sheet("", "sheet.png")
sheet("-nophoto", "sheet-nophoto.png")
