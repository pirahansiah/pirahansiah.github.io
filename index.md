---
layout: default
title: Farshid Pirahansiah
permalink: /
---

{% capture site_content %}
{% include_relative contents/site.md %}
{% endcapture %}

{{ site_content | markdownify }}
