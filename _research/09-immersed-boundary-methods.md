---
title: "Accurate and well-conditioned immersed boundary methods"
order: 9
image: 2D_double_cylinder_combined.svg
alt: "Flow between two concentric interfaces, with velocity profiles and surface force distributions compared between the original IBPM, the new formulation, and the exact solution"
caption: "Flow between two concentric interfaces: the original immersed boundary projection method (red) produces strongly oscillatory surface forces on $$\\Gamma_1$$, while the new formulation (blue) follows the exact solution (dashed)."
image_wide: true
link: /publication/2026-01-01-improved-accuracy-of-the-discrete-immersed-boundary-formulation
link_label: "Read the paper"
---

Immersed boundary methods let us simulate flows around complex, moving geometries on simple Cartesian grids, but classical continuous-forcing formulations are limited to first-order accuracy. I developed discretizations that achieve higher-order accuracy at the interface while improving the conditioning of the method within a projection-based framework, making the resulting systems cheaper to solve.
