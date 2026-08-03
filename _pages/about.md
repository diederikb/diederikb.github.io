---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm a postdoctoral scholar at Caltech, specializing in multiphysics problems involving turbulent flows and the development of numerical simulation methods.

Research
======

{% assign research_examples = site.research | sort: "order" | reverse %}
{% for post in research_examples %}
  {% include research-single.html %}
{% endfor %}
