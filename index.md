---
layout: default
title: Farshid Pirahansiah
permalink: /
---

{% capture site_text %}{% include_relative contents/site.md %}{% endcapture %}
{% assign lines = site_text | split: "\n" %}
{% capture menu_items %}{% endcapture %}
{% capture anchored_content %}{% endcapture %}
{% assign current_title = "" %}
{% assign current_id = "" %}
{% assign current_url = "" %}
{% for line in lines %}
  {% assign stripped = line | strip %}
  {% if stripped contains "# " and stripped contains "## " == false %}
    {% if current_title != "" %}
      {% capture href %}{% if current_url != "" %}{{ current_url }}{% else %}#{{ current_id }}{% endif %}{% endcapture %}
      {% capture menu_items %}{{ menu_items }}<li class="nav-item"><a href="{{ href }}">{{ current_title }}</a></li>{% endcapture %}
    {% endif %}
    {% assign current_title = stripped | remove: "# " | strip %}
    {% assign current_id = current_title | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% assign current_url = "" %}
    {% capture anchored_content %}{{ anchored_content }}<a id="{{ current_id }}"></a>{{ line }}\n{% endcapture %}
  {% elsif stripped contains "/contents/" and current_title != "" %}
    {% assign current_url = stripped %}
    {% capture anchored_content %}{{ anchored_content }}{{ line }}\n{% endcapture %}
  {% else %}
    {% capture anchored_content %}{{ anchored_content }}{{ line }}\n{% endcapture %}
  {% endif %}
{% endfor %}
{% if current_title != "" %}
  {% capture href %}{% if current_url != "" %}{{ current_url }}{% else %}#{{ current_id }}{% endif %}{% endcapture %}
  {% capture menu_items %}{{ menu_items }}<li class="nav-item"><a href="{{ href }}">{{ current_title }}</a></li>{% endcapture %}
{% endif %}

<nav class="navbar">
  <div class="navbar-brand">
    <a href="{{ '/' | relative_url }}" class="navbar-title">{{ site.title }}</a>
  </div>
  <ul class="navbar-nav">
    {{ menu_items }}
    <li><a href="https://github.com/pirahansiah">github</a></li>
  </ul>
</nav>

<section class="hero">
  <p class="eyebrow">Personal Knowledge & AI</p>
  <h1>Farshid Pirahansiah</h1>
  <p class="hero-copy">A compact, mobile-first website driven directly from the PKM content repository.</p>
</section>

<div class="site-content glass-panel">
  {{ anchored_content | markdownify }}
</div>
