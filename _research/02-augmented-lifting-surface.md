---
title: "Augmented lifting line and lifting surface models"
order: 2
image: 3d_lifting_surface_t_1000.png
alt: "Vortex filaments shed from the leading and trailing edges of a finite plate in the augmented lifting surface model, seen in perspective and from downstream"
caption: "Vortex filaments shed from the edges of a finite plate in the augmented lifting surface model, shown in perspective and from downstream."
image_wide: true
link: /talk/2021-11-21-aps-74
link_label: "See the talk"
---

Two-dimensional vortex models capture unsteady aerodynamics cheaply, but a
two-dimensional model is really an infinite wing: its bound vorticity extends
forever in the span. A finite wing instead sheds its bound circulation into
streamwise filaments towards the tips. I explored a middle ground between the two,
in which two-dimensional vortex models sit at a set of spanwise stations and see a
freestream corrected for the spanwise, streamwise and outer induced velocities,
while the resulting filaments interact directly in three dimensions. Because an
unsteady lifting line cannot represent three-dimensional effects on the
leading-edge vortex, the same idea extends to a lifting surface, where the
two-dimensional models only set the strengths of the surface and wake filaments
and the system is advanced through direct filament interactions. This work is
exploratory and unpublished: it still needs vortex aggregation to keep the model
order low, a comparison of the predicted forces against truth data, and a test
inside a flow estimation framework.
