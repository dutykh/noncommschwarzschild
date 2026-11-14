#!/usr/bin/env python3
# Dr. Denys Dutykh (Mathematics Department, Khalifa University of Science and Technology, Abu Dhabi, UAE)
"""Figure of the README: horizons and potentials of the noncommutative Schwarzschild black hole.

    f(x) = 1 - erf(mu x)/x + 2 mu exp(-mu^2 x^2)/sqrt(pi)            (as in QNMsNonExtreme.mw)
    M^2 U(x) = f(x)/4 [ (1 - s^2) f'(x)/x + l(l + 1)/x^2 ],   x = r/(2M)

The extremal mass solves f = 0 and df/dx = 0 together, as QNMsExtreme.mw does. From this folder,
    python3 plot_readme_figure.py
writes ncs-horizons.png (Python 3 with NumPy, SciPy and Matplotlib). The style is the stamped copy
manuscript_style.py beside it.
"""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.optimize import brentq, fsolve
from scipy.special import erf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import manuscript_style as hs  # noqa: E402

MU = 2.25        # the mass of QNMsNonExtreme.mw as distributed


def f(x, mu):
    return 1 - erf(mu * x) / x + 2 * mu * np.exp(-(mu * x) ** 2) / np.sqrt(np.pi)


def dfdx(x, mu):
    return erf(mu * x) / x**2 - 2 * mu * np.exp(-(mu * x) ** 2) / (np.sqrt(np.pi) * x) \
        - 4 * mu**3 * x * np.exp(-(mu * x) ** 2) / np.sqrt(np.pi)


xe, mu_e = fsolve(lambda v: [f(v[0], v[1]), dfdx(v[0], v[1])], (0.79, 1.90), xtol=1e-14)
xh = brentq(lambda t: f(t, MU), 0.9, 1.1, xtol=1e-14)
print(f"extremal black hole: mu_e = {mu_e:.10f}, x_e = {xe:.10f}")
print(f"mu = {MU}: event horizon x_h = {xh:.10f}")

hs.configure(family="libertine")
plt.rcParams["savefig.dpi"] = 260
plt.rcParams["figure.facecolor"] = hs.PAPER
plt.rcParams["savefig.facecolor"] = hs.PAPER

fig, (left, right) = plt.subplots(1, 2, figsize=(hs.WIDTH, 2.75))

# (a) the function f: no horizon, a double horizon, two horizons.
x = np.linspace(1e-3, 4.0, 4000)
for k, (mu, words) in enumerate([(1.5, "no horizon"), (mu_e, "extremal"), (MU, "two horizons")]):
    style = hs.series(k)
    style["marker"] = None
    left.plot(x, f(x, mu), lw=1.1, label=rf"$\mu = {mu:.6g}$ ({words})", **style)
for xr, k in ((xe, 1), (xh, 2)):
    left.plot([xr], [0.0], linestyle="none", marker="o", markersize=4.2,
              markerfacecolor="white", markeredgecolor=hs.SERIES[k], markeredgewidth=0.9)
left.plot(x[x > 0.5], 1 - 1 / x[x > 0.5], color=hs.SLATE, lw=0.8, linestyle=(0, (5.0, 1.5, 1.5, 1.5)),
          label=r"Schwarzschild, $1 - 1/x$")
left.axhline(0.0, color=hs.SLATE, lw=0.6, linestyle=(0, (1.6, 1.6)), zorder=0)
left.set_xlim(0, 4.0)
left.set_ylim(-0.3, 1.05)
left.set_xlabel(r"$x = r/(2M)$")
left.set_ylabel(r"$f(x)$")
hs.panel(left, r"(a) the function $f$, whose zeros are the horizons")
hs.legend_outside(left, where="below", ncol=2)

# (b) the potentials of the three perturbations, l = 2, outside the event horizon at mu = 2.25.
ell = 2
x = np.linspace(xh, 8.0, 3000)
for k, s in enumerate((0, 1, 2)):
    style = hs.series(k)
    style["marker"] = None
    U = f(x, MU) / 4 * ((1 - s**2) * dfdx(x, MU) / x + ell * (ell + 1) / x**2)
    right.plot(x, U, lw=1.1, label=rf"$s = {s}$", **style)
    print(f"s = {s}: largest M^2 U = {U.max():.6f} at x = {x[U.argmax()]:.4f}")
right.set_xlim(0.9, 8.0)
right.set_ylim(0.0, 0.32)
right.set_xlabel(r"$x = r/(2M)$")
right.set_ylabel(r"$M^2\,U(x)$")
hs.panel(right, rf"(b) potentials for $\ell = {ell}$ at $\mu = {MU}$")
hs.legend_outside(right, where="below", ncol=3)

out = HERE / "ncs-horizons.png"
hs.save(fig, out)
# The background is opaque: without its alpha channel, and compressed a second time without
# loss, the file is smaller.
Image.open(out).convert("RGB").save(out, optimize=True)
print("written", out)
