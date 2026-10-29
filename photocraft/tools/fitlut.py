"""Fit a smooth 3D colour lookup table (.cube) that maps one image's colours onto another's, for two aligned pictures of the same scene.

    uv run --no-project --with numpy --with pillow python3 fitlut.py SOURCE.png TARGET.png out.cube [--size 17] [--sigma 0.045] [--conf 1.0]

SOURCE and TARGET must show the same framing (the target is resized to the source's size). The LUT is a kernel regression over pixel pairs
(Gaussian weights in RGB space, sigma as a fraction of the range) blended with a per-channel quantile curve where few pixels fall;
apply it with `layer.newAdjustmentLayer.colorLookup {"file":"/abs/out.cube"}`. Prints the mean absolute error of the LUT, of the
quantile curves alone and of doing nothing, so you can see whether it helped. It matches colour and tone only: it cannot add detail.
"""
import argparse, numpy as np
from PIL import Image
ap = argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('target'); ap.add_argument('out')
ap.add_argument('--size', type=int, default=17); ap.add_argument('--sigma', type=float, default=0.045); ap.add_argument('--conf', type=float, default=1.0)
a = ap.parse_args(); N = a.size
src = Image.open(a.source).convert('RGB')
S = np.asarray(src, dtype=np.float64).reshape(-1, 3) / 255
T = np.asarray(Image.open(a.target).convert('RGB').resize(src.size, Image.LANCZOS), dtype=np.float64).reshape(-1, 3) / 255
rng = np.random.default_rng(1); idx = rng.choice(len(S), min(40000, len(S)), replace=False); S2, T2 = S[idx], T[idx]
qs = np.linspace(0, 100, 101); prior = []
for c in range(3):
    xb = np.maximum.accumulate(np.percentile(S[:, c], qs) + np.arange(101) * 1e-9); prior.append((xb, np.percentile(T[:, c], qs)))
pm = lambda x: np.stack([np.interp(x[:, c], *prior[c]) for c in range(3)], 1)
g = np.linspace(0, 1, N); nodes = np.array([[r, gg, b] for b in g for gg in g for r in g])   # R varies fastest, as .cube wants
out = np.zeros_like(nodes)
for i in range(0, len(nodes), 256):
    nd = nodes[i:i + 256]; w = np.exp(-((nd[:, None, :] - S2[None, :, :]) ** 2).sum(2) / (2 * a.sigma ** 2)); ws = w.sum(1, keepdims=True)
    out[i:i + 256] = (ws / (ws + a.conf)) * (w @ T2) / np.maximum(ws, 1e-12) + (1 - ws / (ws + a.conf)) * pm(nd)
out = np.clip(out, 0, 1)
with open(a.out, 'w') as f:
    f.write('TITLE "fitted"\nLUT_3D_SIZE %d\nDOMAIN_MIN 0 0 0\nDOMAIN_MAX 1 1 1\n' % N)
    for r in out: f.write('%.6f %.6f %.6f\n' % tuple(r))
L = out.reshape(N, N, N, 3)
def apply(x):
    p = x * (N - 1); i0 = np.clip(np.floor(p).astype(int), 0, N - 2); fr = p - i0; r0, g0, b0 = i0.T; res = 0
    for dr in (0, 1):
        for dg in (0, 1):
            for db in (0, 1):
                wg = (fr[:, 0] if dr else 1 - fr[:, 0]) * (fr[:, 1] if dg else 1 - fr[:, 1]) * (fr[:, 2] if db else 1 - fr[:, 2])
                res = res + L[b0 + db, g0 + dg, r0 + dr] * wg[:, None]
    return res
print('mean abs error (0-255): LUT %.2f   quantile curves %.2f   nothing %.2f' % (np.abs(apply(S) - T).mean() * 255, np.abs(pm(S) - T).mean() * 255, np.abs(S - T).mean() * 255))
