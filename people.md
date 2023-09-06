---
layout: default
title: People
permalink: /people/
---
{% assign current_people = site.people | where:'alumnae', null %}

<h2>Faculty</h2>

{% assign faculty = current_people | where:'role', 'Principal Investigator' %}
{% for person in faculty %}
{% include people_index_item.html %}
{% endfor %}

<h2>Trainees</h2>

{% assign trainees = current_people | where_exp:'person', "person.role == 'PhD Student' or person.role == 'Postdoctoral Associate'" %}
{% for person in trainees %}
  {% include people_index_item.html %}
{% endfor %}

<h2>Staff</h2>

{% assign staff = current_people | where_exp:'person', "person.role == 'Software Developer' or person.role == 'Senior Bioinformatics Scientist'" %}
{% for person in site.people %}
  {% if person.role == "Software Developer" or person.role == "Senior Bioinformatics Scientist" %}
  {% include people_index_item.html %}
  {% endif %}
{% endfor %}

<h2>Alumni</h2>

{% assign alums = site.people | where:'alumnae', "true" %}
{% for person in alums %}
  {% include people_index_item.html %}
{% endfor %}
