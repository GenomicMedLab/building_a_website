---
layout: default
title: Research Projects
permalink: /research/
---
<div class="projects-container">
  <div class="project-container">
    {% assign project = site.projects | where_exp:"project","project.name == 'Variation Representation'" | first %}
    <h2>{{ project.name }}</h2>
    {{ project.excerpt }}
    <a href="{{ project.url }}">More...</a>
  </div>
  <div class="project-container">
    {% assign project = site.projects | where_exp:"project","project.name == 'Knowledgebase Integration'" | first %}
    <h2>{{ project.name }}</h2>
    {{ project.excerpt }}
    <a href="{{ project.url }}">More...</a>
  </div>
  <div class="project-container">
    {% assign project = site.projects | where_exp:"project","project.name == 'Gene Fusion Informatics'" | first %}
    <h2>{{ project.name }}</h2>
    {{ project.excerpt }}
    <a href="{{ project.url }}">More...</a>
  </div>
</div>
