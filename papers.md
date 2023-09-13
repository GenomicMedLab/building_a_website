---
layout: default
title: Papers
permalink: /papers/
---

<h1>Papers</h1>
{% for paper in site.papers reversed %}
  {% capture year %}{{ paper.date | date: "%Y"}}{% endcapture %}
  {% capture nyear %}{{ paper.next.date | date: "%Y" }}{% endcapture %}

  {% if year != nyear %}
  {% if forloop.first %}
  <h2>{{ year }}</h2>
  <ul>
  {% else %}
  </ul>
  <h2>{{ year }}</h2>
  <ul>
  {% endif %}
  {% endif %}



  <li><div>
  <p>{% render_bold_cite %}{{ paper.authors }}{% endrender_bold_cite %}</p>
  <p><a href="{{ paper.url }}">{{ paper.title }}</a></p>
  <p>{{ paper.journal_cite }}</p>
  <p>({{ year }})</p>
  </div></li>



{% endfor %}
</ul>
