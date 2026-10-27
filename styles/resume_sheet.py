"""Make a contact sheet (sheet.png) of every <style>-<a|b>.png in a folder, styles in rows, layouts a and b side by side."""
import os, sys
from PIL import Image, ImageDraw
d = sys.argv[1]
styles = ["traditional", "elegant", "clean", "professional", "academic", "modern", "stylish", "creative", "minimal"]
w, h = 330, 427
sheet = Image.new("RGB", (2 * w + 30, len(styles) * (h + 24) + 6), "#777")
dr = ImageDraw.Draw(sheet)
for r, st in enumerate(styles):
    for c, v in enumerate("ab"):
        p = os.path.join(d, f"{st}-{v}.png")
        if os.path.exists(p):
            im = Image.open(p).convert("RGB").resize((w, h), Image.LANCZOS)
            sheet.paste(im, (10 + c * (w + 10), r * (h + 24) + 20))
        dr.text((12 + c * (w + 10), r * (h + 24) + 6), f"{st}-{v}", fill="white")
sheet.save(os.path.join(d, "sheet.png")); print("sheet.png")
