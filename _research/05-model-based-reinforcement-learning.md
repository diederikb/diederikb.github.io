---
title: "Model-based reinforcement learning for flow control"
order: 5
image: model_based_RL.png
alt: "Architecture of the physics-augmented autoencoder: a convolutional encoder and multi-layer perceptron compress flow snapshots into latent variables, a decoder reconstructs the fields, and a separate network maps the latent variables to physical variables"
caption: "The physics-augmented autoencoder: a convolutional encoder compresses CFD flow snapshots into a three-dimensional latent space, a decoder reconstructs the fields, and a separate network maps the latent variables to physical variables."
image_wide: true
link: /publication/2025-10-01-model-based-reinforcement-learning-for-control-of-strongly-disturbed-unsteady-aerodynamic-flows
link_label: "Read the paper"
---

Model-free reinforcement learning needs an enormous number of interactions with the
flow environment before it finds a workable policy, and when that environment is a
CFD simulation the training cost becomes the bottleneck. This work — led by
Zhecheng Liu at UCLA, with me as second author — replaces the full environment with
a reduced-order surrogate: a physics-augmented autoencoder compresses flow
snapshots into a three-dimensional latent space, and a latent dynamics model
predicts how trajectories in that space respond to action sequences over long
horizons. A policy trained entirely inside the surrogate transfers to the full CFD
environment, where it mitigates the lift variation of an airfoil encountering
gusts.
