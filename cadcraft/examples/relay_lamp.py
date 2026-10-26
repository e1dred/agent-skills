"""Invented example: a push switch feeds a relay coil; a pilot lamp sits across the supply. python3 relay_lamp.py OUTDIR"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from schem import Sheet
s = Sheet()
for n, c, w in (("FRAME", 7, 0.35), ("POS", 1, 0.6), ("NEG", 7, 0.6), ("SYM", 5, 0.35), ("TXT", 7, 0.25)): s.layer(n, c, w)
s.use("FRAME"); s.rect(5, 5, 205, 145)
s.use("POS"); s.line((20, 100), (160, 100)); s.line((60, 100), (60, 80)); s.line((100, 100), (100, 90))
s.use("NEG"); s.line((20, 30), (160, 30)); s.line((130, 30), (130, 60)); s.line((100, 30), (100, 60)); s.line((130, 83), (130, 100))
s.use("SYM"); s.rect(50, 60, 70, 80); s.pad(60, 80); s.pad(60, 60)            # push switch box
s.line((60, 78.8), (60, 72)); s.line((60, 72), (66, 67)); s.line((60, 61.2), (60, 64))
s.rect(90, 60, 110, 90); s.line((90, 60), (110, 90)); s.circle(130, 75, 8); s.line((125, 70), (135, 80)); s.line((125, 80), (135, 70))   # relay coil, lamp
s.use("POS"); s.dot(60, 100); s.dot(100, 100)
s.use("TXT"); s.text(20, 130, "Push switch, relay coil and pilot lamp (invented example)", 5); s.text(52, 84, "S1", 3); s.text(112, 75, "K1 coil", 3); s.text(142, 75, "H1 pilot lamp", 3)
bad = s.build(sys.argv[1] if len(sys.argv) > 1 else "out", "relay_lamp", window=(0, 0, 210, 150))
print(bad or "ok")
