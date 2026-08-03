---
title: "Cold-to-hot transformation for turbofan blades"
order: 1
image: cad_turbomachinery_project.png
alt: "Diagram of the partitioned aeroelastic loop coupling a structural solver, a CAD parameterization and a CFD solver, with blade displacement and static pressure fields"
caption: "The partitioned cold-to-hot loop: a structural analysis of the blade under centrifugal and pressure loads morphs the CAD geometry, which is remeshed for a CFD analysis, whose pressure loads are transferred back to the structure."
image_wide: true
---

A turbofan blade is manufactured in its unloaded "cold" shape, but it flies in a
"hot" shape: centrifugal and aerodynamic loads stretch it radially and untwist it
by several degrees, which is enough to shift the fan's operating point. During my
master's thesis, carried out at the von Karman Institute, I extended the existing
cold-to-hot transformation — which accounted for centrifugal loads only — into a
partitioned aeroelastic loop that also carries the aerodynamic pressure loads,
iterating between a structural analysis, a morphed CAD geometry and a CFD analysis
until the deformed blade settles. With it I quantified how untwist raises the mass
flow rate and total bypass pressure ratio while lowering the isentropic efficiency,
and ran a parametric study showing how lean, sweep, chord length and thickness each
shift the untwist.
