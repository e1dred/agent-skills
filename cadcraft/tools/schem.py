"""Small helper for drawing 2D schematics headlessly with cadcraft-cli: collect commands, then build DXF + PDF.

    from schem import Sheet
    s = Sheet()                       # metric, Arial text style, standard layers
    s.layer("WIRE", color=1, lw=0.6)  # name, AutoCAD colour index/name, lineweight in mm
    s.line((0, 0), (50, 0)); s.dot(25, 0); s.pad(50, 0); s.rect(10, 10, 40, 30); s.text(12, 12, "K1", 3)
    s.build("/abs/outdir", "name")    # -> name.dxf, name.pdf (white page, true lineweights), name.png (via ghostscript, optional)
"""
import json, os, shutil, subprocess

CLI = os.environ.get("CADCRAFT_CLI") or shutil.which("cadcraft-cli") or os.path.expanduser("~/AppImages/cadcraft-cli")


class Sheet:
    def __init__(self, font="Arial"):
        self.c = []
        self.cmd("style", name="SCH", font=font, height=0, current=True)   # the default style is a stick font
        self.cmd("linetype", load="DASHED")                                    # a layer can only use a loaded linetype

    def cmd(self, i, **p): self.c.append((i, p))

    def layer(self, name, color=7, lw=0.35, lt=None):
        p = {"name": name, "color": color, "lineweight": lw, "current": True}
        if lt: p["linetype"] = lt
        self.cmd("layer.new", **p)

    def use(self, name): self.cmd("layer.current", name=name)
    def line(self, *pts): self.cmd("line", points=[list(p) for p in pts])
    def rect(self, x0, y0, x1, y1): self.cmd("rectang", p1=[x0, y0], p2=[x1, y1])
    def circle(self, x, y, r): self.cmd("circle", center=[x, y], radius=r)
    def pad(self, x, y, r=1.2): self.circle(x, y, r)                         # terminal
    def dot(self, x, y, r=1.1): self.cmd("donut", center=[x, y], inside=0, outside=2 * r)   # junction dot
    def arc(self, x, y, r, a0, a1): self.cmd("arc", center=[x, y], radius=r, start=a0, end=a1)

    def text(self, x, y, s, h=2.6, j="L", rot=None):
        p = {"at": [x, y], "text": s, "height": h, "justify": j}
        if rot is not None: p["rotation"] = rot
        self.cmd("text", **p)

    def build(self, outdir, name, window=None, png_dpi=150):
        os.makedirs(outdir, exist_ok=True)
        base = os.path.join(outdir, name)
        if window: self.cmd("zoom", mode="window", p1=list(window[:2]), p2=list(window[2:]))
        args = [CLI, "run", "--metric"]
        for i, p in self.c: args += ["--cmd", i + " " + json.dumps(p)]
        args += ["--save", base + ".dxf", "--export", base + ".pdf"]
        r = subprocess.run(args, capture_output=True, text=True)
        bad = [l for l in (r.stdout + r.stderr).splitlines() if l and not l.startswith(('{"handle', '{"handles', 'wrote', '{"current', '{"library'))]
        if shutil.which("gs"):
            subprocess.run(["gs", "-q", "-sDEVICE=png16m", "-r%d" % png_dpi, "-o", base + ".png", base + ".pdf"], capture_output=True)
        return bad
