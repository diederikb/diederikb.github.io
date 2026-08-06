---
title: "Fluid–metamaterial interaction in wall-bounded turbulence"
order: 8
image: 3D_contours_trimmed.gif
alt: "Three-dimensional turbulent channel flow over walls deforming as streamwise traveling waves, with streamwise velocity contours on the faces of the domain"
caption: "Turbulent channel flow at $$\\mathrm{Re}_\\tau \\approx 186$$ over walls undergoing prescribed traveling-wave deformations imposed through the immersed boundary; colors show the streamwise velocity."
image_wide: true
link: /publication/2026-01-01-a-high-fidelity-simulation-framework-for-turbulent-flows-with-complex-metamaterial-structures
link_label: "Read the paper"
---

Metamaterial surfaces offer a route to passively manipulating wall-bounded
turbulence, but simulating them means resolving a turbulent flow and a complex,
moving subsurface structure at the same time. I integrated a strongly coupled
fluid–structure interaction framework, built on a continuous-forcing immersed
boundary method, into a parallel three-dimensional turbulent channel flow solver.
New discrete operators pass information between subsurface metamaterial elements
and compliant immersed boundary patches, while a hybrid uniform–stretched grid
and parallelized immersed boundary operations keep the simulations affordable.
The framework handles rigid, prescribed-moving, and compliant walls at
$$\mathrm{Re}_\tau \approx 186$$, laying the groundwork for simulations of true
fluid–metamaterial interaction.
