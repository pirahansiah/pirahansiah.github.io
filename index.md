---
layout: default
title: Farshid Pirahansiah
permalink: /
---

{% capture site_text %}{% include_relative contents/site.md %}{% endcapture %}
{% assign lines = site_text | split: "\n" %}
{% capture nav_html %}{% endcapture %}
{% capture current_h1_children %}{% endcapture %}
{% assign current_h1 = "" %}
{% assign current_h1_id = "" %}
{% assign current_h1_url = "" %}
{% assign current_h2 = "" %}
{% assign current_h2_id = "" %}
{% assign current_h2_url = "" %}

{% for line in lines %}
  {% assign stripped = line | strip %}
  {% if stripped == "" %}{% continue %}{% endif %}
  {% assign first3 = stripped | slice: 0, 3 %}
  {% assign first2 = stripped | slice: 0, 2 %}
  {% assign first10 = stripped | slice: 0, 10 %}

  {% if first2 == "# " %}
    {% if current_h2 != "" %}
      {% assign h2_href = current_h2_url %}
      {% if h2_href == "" %}
        {% assign h2_href = "#" | append: current_h2_id %}
      {% endif %}
      {% capture current_h1_children %}{{ current_h1_children }}<li class="submenu-item"><a href="{{ h2_href }}">{{ current_h2 }}</a></li>{% endcapture %}
      {% assign current_h2 = "" %}
      {% assign current_h2_id = "" %}
      {% assign current_h2_url = "" %}
    {% endif %}
    {% if current_h1 != "" %}
      {% assign h1_href = current_h1_url %}
      {% if h1_href == "" %}
        {% assign h1_href = "#" | append: current_h1_id %}
      {% endif %}
      {% if current_h1_children != "" %}
        {% capture nav_html %}{{ nav_html }}<li class="nav-item nav-dropdown"><details><summary>{{ current_h1 }}</summary><ul class="submenu">{{ current_h1_children }}</ul></details></li>{% endcapture %}
      {% else %}
        {% capture nav_html %}{{ nav_html }}<li class="nav-item"><a href="{{ h1_href }}">{{ current_h1 }}</a></li>{% endcapture %}
      {% endif %}
      {% capture current_h1_children %}{% endcapture %}
    {% endif %}
    {% assign current_h1 = stripped | slice: 2, 100 | strip %}
    {% assign current_h1_id = current_h1 | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% assign current_h1_url = "" %}
  {% elsif first3 == "## " %}
    {% if current_h2 != "" %}
      {% assign h2_href = current_h2_url %}
      {% if h2_href == "" %}
        {% assign h2_href = "#" | append: current_h2_id %}
      {% endif %}
      {% capture current_h1_children %}{{ current_h1_children }}<li class="submenu-item"><a href="{{ h2_href }}">{{ current_h2 }}</a></li>{% endcapture %}
    {% endif %}
    {% assign current_h2 = stripped | slice: 3, 100 | strip %}
    {% assign current_h2_id = current_h2 | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% assign current_h2_url = "" %}
  {% elsif first10 == "/contents/" or stripped contains "](" or stripped contains "]{" %}
    {% assign link_target = "" %}
    {% if first10 == "/contents/" %}
      {% assign link_target = stripped %}
    {% elsif stripped contains "](" %}
      {% assign link_target = stripped | split: "(" | last | split: ")" | first %}
    {% elsif stripped contains "]{" %}
      {% assign link_target = stripped | split: "]{" | last | remove: "}" %}
    {% endif %}
    {% if current_h2 != "" %}
      {% assign current_h2_url = link_target %}
    {% elsif current_h1 != "" %}
      {% assign current_h1_url = link_target %}
    {% endif %}
  {% endif %}
{% endfor %}

{% if current_h2 != "" %}
  {% assign h2_href = current_h2_url %}
  {% if h2_href == "" %}
    {% assign h2_href = "#" | append: current_h2_id %}
  {% endif %}
  {% capture current_h1_children %}{{ current_h1_children }}<li class="submenu-item"><a href="{{ h2_href }}">{{ current_h2 }}</a></li>{% endcapture %}
{% endif %}

{% if current_h1 != "" %}
  {% assign h1_href = current_h1_url %}
  {% if h1_href == "" %}
    {% assign h1_href = "#" | append: current_h1_id %}
  {% endif %}
  {% if current_h1_children != "" %}
    {% capture nav_html %}{{ nav_html }}<li class="nav-item nav-dropdown"><details><summary>{{ current_h1 }}</summary><ul class="submenu">{{ current_h1_children }}</ul></details></li>{% endcapture %}
  {% else %}
    {% capture nav_html %}{{ nav_html }}<li class="nav-item"><a href="{{ h1_href }}">{{ current_h1 }}</a></li>{% endcapture %}
  {% endif %}
{% endif %}

<nav class="navbar ios-liquid-glass">
  <div class="navbar-brand">
    <a href="{{ '/' | relative_url }}" class="navbar-title">{{ site.title }}</a>
  </div>
  <ul class="navbar-nav">
    {{ nav_html }}
    <li><a href="https://github.com/pirahansiah">github</a></li>
  </ul>
</nav>

<section class="hero">
  <p class="eyebrow">Personal Knowledge & AI</p>
  <h1>Farshid Pirahansiah</h1>
  <p class="hero-copy">A compact, mobile-first website driven directly from the PKM content repository.</p>
</section>

<div class="site-content glass-panel ios-liquid-glass">
  <pre class="site-source">{{ site_text | escape }}</pre>
</div>
