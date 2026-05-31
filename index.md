---
layout: default
title: Farshid Pirahansiah
permalink: /
---

{% capture site_text %}{% include_relative contents/site.md %}{% endcapture %}
{% assign lines = site_text | split: "\n" %}
{% capture nav_html %}{% endcapture %}
{% capture anchored_content %}{% endcapture %}
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

  {% assign link_target = "" %}
  {% if stripped contains "](" %}
    {% assign link_target = stripped | split: "(" | last | split: ")" | first %}
  {% elsif stripped contains "]{" %}
    {% assign link_target = stripped | split: "]{" | last | remove: "}" %}
  {% elsif stripped startswith "/contents/" %}
    {% assign link_target = stripped %}
  {% endif %}

  {% if stripped startswith "# " %}
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
        {% capture nav_html %}{{ nav_html }}<li class="nav-item has-submenu"><a href="{{ h1_href }}">{{ current_h1 }}</a><ul class="submenu">{{ current_h1_children }}</ul></li>{% endcapture %}
      {% else %}
        {% capture nav_html %}{{ nav_html }}<li class="nav-item"><a href="{{ h1_href }}">{{ current_h1 }}</a></li>{% endcapture %}
      {% endif %}
      {% capture current_h1_children %}{% endcapture %}
    {% endif %}
    {% assign current_h1 = stripped | remove_first: "# " | strip %}
    {% assign current_h1_id = current_h1 | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% assign current_h1_url = "" %}
    {% capture anchored_content %}{{ anchored_content }}<a id="{{ current_h1_id }}"></a>{{ line }}\n{% endcapture %}
  {% elsif stripped startswith "## " %}
    {% if current_h2 != "" %}
      {% assign h2_href = current_h2_url %}
      {% if h2_href == "" %}
        {% assign h2_href = "#" | append: current_h2_id %}
      {% endif %}
      {% capture current_h1_children %}{{ current_h1_children }}<li class="submenu-item"><a href="{{ h2_href }}">{{ current_h2 }}</a></li>{% endcapture %}
    {% endif %}
    {% assign current_h2 = stripped | remove_first: "## " | strip %}
    {% assign current_h2_id = current_h2 | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% assign current_h2_url = "" %}
    {% capture anchored_content %}{{ anchored_content }}<a id="{{ current_h2_id }}"></a>{{ line }}\n{% endcapture %}
  {% elsif link_target != "" %}
    {% if current_h2 != "" %}
      {% assign current_h2_url = link_target %}
    {% elsif current_h1 != "" %}
      {% assign current_h1_url = link_target %}
    {% endif %}
    {% if stripped contains "](" or stripped contains "]{" %}
      {% capture anchored_content %}{{ anchored_content }}{{ line }}\n{% endcapture %}
    {% endif %}
  {% else %}
    {% capture anchored_content %}{{ anchored_content }}{{ line }}\n{% endcapture %}
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
    {% capture nav_html %}{{ nav_html }}<li class="nav-item has-submenu"><a href="{{ h1_href }}">{{ current_h1 }}</a><ul class="submenu">{{ current_h1_children }}</ul></li>{% endcapture %}
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
  {{ anchored_content | markdownify }}
</div>
