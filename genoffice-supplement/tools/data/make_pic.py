"""Write pic.png (a 60x40 blue square) next to this script's working directory; the sweeps use it as a sample picture."""
import struct, zlib
w, h = 60, 40
raw = b"".join(b"\x00" + bytes([40, 100, 200]) * w for _ in range(h))
def ch(t, d):
    c = struct.pack(">I", len(d)) + t + d
    return c + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
open("pic.png", "wb").write(b"\x89PNG\r\n\x1a\n" + ch(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + ch(b"IDAT", zlib.compress(raw)) + ch(b"IEND", b""))
