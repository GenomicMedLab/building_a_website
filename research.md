---
layout: default
title: Research
permalink: /research/
---
<h1 class="current">Research Projects</h1>

<ul>
{% for project in site.projects %}
<li><a href="{{ project.url }}">{{ project.name }}</a></li>
{% endfor %}
</ul>
