---
layout: default
title: Farshid Pirahansiah
permalink: /
---

{% capture site_text %}{% include_relative contents/site.md %}{% endcapture %}
{% assign lines = site_text | split: "\n" %}
{% capture menu_items %}{% endcapture %}
{% for line in lines %}
  {% if line contains "# " %}
    {% assign title = line | remove: "# " | strip %}
    {% assign id = title | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" %}
    {% capture menu_item %}<li><a href="#{{ id }}">{{ title }}</a></li>{% endcapture %}
    {% capture menu_items %}{{ menu_items }}{{ menu_item }}{% endcapture %}
  {% endif %}
{% endfor %}

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

<div class="site-content">
  {{ site_text | markdownify }}
</div>
