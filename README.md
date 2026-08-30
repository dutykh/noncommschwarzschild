# Quasinormal Modes of Noncommutative Schwarzschild Black Holes

[![Eur. Phys. J. C](https://img.shields.io/badge/Eur.%20Phys.%20J.%20C-84%20%282024%29%20622-005a9c)](https://link.springer.com/article/10.1140/epjc/s10052-024-12981-6)
[![DOI](https://img.shields.io/badge/DOI-10.1140%2Fepjc%2Fs10052--024--12981--6-1a7f37)](https://doi.org/10.1140/epjc/s10052-024-12981-6)
[![arXiv](https://img.shields.io/badge/arXiv-2406.03353-b31b1b)](https://arxiv.org/abs/2406.03353)
[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-4c1)](LICENSE)
[![Maple](https://img.shields.io/badge/Maple-2022%2B-ff6f00)](https://www.maplesoft.com/products/Maple/)
[![MATLAB](https://img.shields.io/badge/MATLAB-R2019a%2B-0076a8)](https://www.mathworks.com/products/matlab.html)
[![QNMs Hall of Fame](https://img.shields.io/badge/QNMs-Hall%20of%20Fame-8a2be2)](https://qnms.denys-dutykh.com/)
[![GitHub](https://img.shields.io/badge/GitHub-dutykh%2Fnoncommschwarzschild-181717?logo=github)](https://github.com/dutykh/noncommschwarzschild)
[![Last commit](https://img.shields.io/github/last-commit/dutykh/noncommschwarzschild)](https://github.com/dutykh/noncommschwarzschild/commits/main)

Computational supplementary material for the study of quasinormal modes (QNMs)
of noncommutative geometry inspired Schwarzschild black holes, computed with a
Chebyshev collocation (pseudospectral) method coupled to a polynomial eigenvalue
solver.

## Reference

Batic, D., Dutykh, D. *Quasinormal modes in noncommutative Schwarzschild black
holes: a spectral analysis.* **Eur. Phys. J. C 84**, 622 (2024).

* Journal (open access): https://link.springer.com/article/10.1140/epjc/s10052-024-12981-6
* DOI: https://doi.org/10.1140/epjc/s10052-024-12981-6
* Preprint: https://arxiv.org/abs/2406.03353
* Repository: https://github.com/dutykh/noncommschwarzschild

## QNMs Hall of Fame

**https://qnms.denys-dutykh.com/**

The present repository is one instalment of a longer programme. A perturbed
black hole rings, and the frequencies at which it does so are fixed by the
geometry alone: they are, in the words of the portal, the *celestial music* of
the spacetime. Computing that spectrum accurately, for geometries where no
closed form exists, is the common thread of the series.

The *Quasi-Normal Modes Hall of Fame* is the portal of the QNM Research Group at
Khalifa University of Science and Technology, led by Dr. Davide Batic and
Dr. Denys Dutykh. It gathers the whole series in one place, each manuscript
listed with its journal version, its arXiv preprint and its companion code
repository, so that any result of the group can be read and rerun from a single
page. Alongside the noncommutative Schwarzschild black hole treated here, the
catalogue covers quantum-corrected black holes (Kazakov–Solodukhin,
Bonanno–Reuter), Planck stars, Lee–Wick black holes, and Morris–Thorne,
noncommutative and phantom wormholes, together with the collaborators who
contributed to them.

Readers who arrived here for the spectral method rather than for this particular
spacetime will find the same machinery applied across all of those geometries,
and are warmly invited to browse it.

## Authors

* Dr. Davide Batic, Mathematics Department, Khalifa University of Science and
  Technology, Abu Dhabi, UAE
* Dr. Denys Dutykh, Mathematics Department, Khalifa University of Science and
  Technology, Abu Dhabi, UAE

## Method in brief

The radial perturbation equation for a spin-`s` field on a noncommutative
Schwarzschild background is mapped onto the interval `y` in `[-1, 1]` and recast
as a quadratic eigenvalue problem in the frequency `omega`,

    (M0 + i*omega*M1 + omega^2*M2) a = 0,

where `a` collects the coefficients of a truncated Chebyshev expansion of the
perturbation. Maple assembles the three matrices `M0`, `M1`, `M2` in extended
precision (`Digits := 200`) at the Chebyshev roots collocation points (extrema
points are available as a commented alternative), and Matlab solves the
resulting polynomial eigenvalue problem with `polyeig`.

Two regimes are treated separately, since the horizon structure and the
associated boundary behaviour differ:

* **non-extreme case**: the dimensionless mass `mu` is prescribed (`mu = 2.25`
  in the file as distributed) and the horizon radius `xh` is obtained by solving
  `f(xh) = 0`;
* **extreme case**: `mu` and the degenerate horizon radius `xe` are obtained
  simultaneously from `f = 0` and `df/dx = 0`.

## Repository contents

| File | Role |
| --- | --- |
| `QNMsNonExtreme.mw` | Maple worksheet assembling `M0`, `M1`, `M2` for the non-extreme black hole and exporting them in ASCII Matlab format |
| `QNMsExtreme.mw` | Same assembly for the extreme (degenerate horizon) case |
| `NONEXTREME CASE-SUPPLEMENTAL MATERIAL.mw` | Maple verification of the analytical steps of the paper in the non-extreme case: coefficient functions, boundary limits, and the reduction leading to the matrix pencil |
| `EXTREME CASE-SUPPLEMENTAL MATERIAL.mw` | Corresponding symbolic verification for the extreme case |
| `findeigs.m` | Matlab driver: reads the exported matrices, calls `polyeig`, and plots the QNM spectrum in the complex `omega` plane |
| `LICENSE` | GNU Lesser General Public License, version 2.1 |

## Software requirements

* Maple (TM), for the worksheets. Only `LinearAlgebra` is used beyond the
  standard library.
* Matlab (TM), for `findeigs.m`. `readmatrix` and `polyeig` are used, so a
  release of R2019a or later is convenient.

## How to reproduce a spectrum

1. Create a `data` subdirectory in the repository root. The Maple worksheets
   write into it and do not create it themselves:

       mkdir data

2. Open `QNMsNonExtreme.mw` (or `QNMsExtreme.mw`) in Maple. Adjust the physical
   parameters at the top if needed: the spin `s` (0, 1 or 2), the angular
   momentum `L`, and, in the non-extreme worksheet, the dimensionless mass `mu`.
   The number of Chebyshev modes is set by `n` (150 by default), which fixes the
   size of the matrices.

3. Execute the whole worksheet. The assembly loop runs at 200 significant
   digits and is the expensive part of the computation; expect it to take a
   while for `n = 150`. On completion the worksheet writes `data/M0.mat`,
   `data/M1.mat` and `data/M2.mat` as ASCII files.

4. Run `findeigs.m` in Matlab from the repository root. It solves

       polyeig(M0, 1i*M1, M2)

   and plots the computed frequencies in the complex plane. The physical QNMs
   are the converged eigenvalues; the remainder of the computed spectrum is
   discretization noise, which is identified by repeating the computation at a
   different resolution `n` and retaining only the frequencies that are stable.

## Licence

The contents of this repository are distributed under the GNU Lesser General
Public License, version 2.1. See `LICENSE` for the full text.

## Acknowledgement

Please acknowledge this work by citing the reference above if you use these
codes or derive material from them.
