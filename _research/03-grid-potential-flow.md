---
title: "Potential flow on Cartesian grids"
order: 3
image: grid_potential_flow.png
alt: "Streamlines of the flow past a plate computed on a Cartesian grid, with the shed point vortices trailing downstream and rolling up"
caption: "Flow past a plate computed with the grid-based potential flow method: streamlines together with the point vortices (dots) shed from the sharp edges, which roll up downstream."
image_wide: true
link: /publication/2022-06-01-planar-potential-flow-on-cartesian-grids
link_label: "Read the paper"
---

Low-order vortex models of unsteady aerodynamics spend most of their effort on
Biot–Savart interactions between vortex elements, which scale poorly as the wake
grows. I developed a grid-based alternative in two dimensions: the circulation is
transferred onto a Cartesian grid and the streamfunction–vorticity Poisson equation
is solved there with a lattice Green's function, which satisfies unbounded boundary
conditions without a large domain. Bodies of arbitrary shape enter through the
immersed boundary projection method, whose Lagrange multiplier turns out to be the
bound vortex sheet strength, and sharp edges are handled by splitting that sheet
strength into a singular and a smooth part, so that enforcing the Kutta condition
becomes a constraint on the smooth part. Sources and sinks follow the same route
through the scalar potential, and the combined velocity field follows from a
Helmholtz decomposition.
