---
layout: default
title: Farshid Pirahansiah
permalink: /
---

{% capture site_text %}{% include_relative contents/site.md %}{% endcapture %}
{% assign lines = site_text | split: "\n" %}
{% capture menu_items %}{% endcapture %}
{% capture anchored_content %}{% endcapture %}
{% for line in lines %}
  {% if line contains "### " %}
    {% assign title = line | remove: "### " | strip %}
    {% assign id = title | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% capture menu_item %}<li class="nav-item sublevel-3"><a href="#{{ id }}">{{ title }}</a></li>{% endcapture %}
    {% capture menu_items %}{{ menu_items }}{{ menu_item }}{% endcapture %}
    {% capture anchored_content %}{{ anchored_content }}<a id="{{ id }}"></a>{{ line }}
{% endcapture %}
  {% elsif line contains "## " %}
    {% assign title = line | remove: "## " | strip %}
    {% assign id = title | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% capture menu_item %}<li class="nav-item sublevel-2"><a href="#{{ id }}">{{ title }}</a></li>{% endcapture %}
    {% capture menu_items %}{{ menu_items }}{{ menu_item }}{% endcapture %}
    {% capture anchored_content %}{{ anchored_content }}<a id="{{ id }}"></a>{{ line }}
{% endcapture %}
  {% elsif line contains "# " %}
    {% assign title = line | remove: "# " | strip %}
    {% assign id = title | downcase | strip | replace: " ", "-" | replace: ".", "" | replace: "/", "" | replace: ":", "" | replace: "#", "" %}
    {% capture menu_item %}<li class="nav-item sublevel-1"><a href="#{{ id }}">{{ title }}</a></li>{% endcapture %}
    {% capture menu_items %}{{ menu_items }}{{ menu_item }}{% endcapture %}
    {% capture anchored_content %}{{ anchored_content }}<a id="{{ id }}"></a>{{ line }}
{% endcapture %}
  {% else %}
    {% assign raw_line = line | append: "\n" %}
    {% capture anchored_content %}{{ anchored_content }}{{ raw_line }}{% endcapture %}
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

<div class="site-content glass-panel">
  {{ anchored_content | markdownify }}
</div>
