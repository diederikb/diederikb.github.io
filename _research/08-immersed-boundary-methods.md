---
title: "Accurate and well-conditioned immersed boundary methods"
order: 8
image: 2D_double_cylinder_combined.svg
alt: "Flow between two concentric interfaces, with velocity profiles and surface force distributions compared between the original IBPM, the new formulation, and the exact solution"
caption: "Flow between two concentric interfaces: the original IBPM (red) produces strongly oscillatory surface forces on $$\\Gamma_1$$, while the new formulation (blue) follows the exact solution (dashed)."
image_wide: true
link: /publication/2026-01-01-improved-accuracy-of-the-discrete-immersed-boundary-formulation
link_label: "Read the paper"
---

Immersed boundary methods let us simulate flows around complex, moving geometries
on simple Cartesian grids, but the classical continuous-forcing formulations are limited to first-order accuracy. I develop discretizations that go beyond first-order
accuracy at the interface, together with well-conditioned projection-based solvers
that keep the resulting systems cheap to solve.
