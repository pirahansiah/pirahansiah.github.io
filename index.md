---
layout: default
title: Farshid Pirahansiah
permalink: /
---

<section class="hero">
  <p class="eyebrow">Personal Knowledge & AI</p>
  <h1>Farshid Pirahansiah</h1>
  <p class="hero-copy">A compact, mobile-first website driven directly from the PKM content repository.</p>
</section>

{% capture site_content %}{% include_relative contents/site.md %}{% endcapture %}

<div class="site-content">
  {{ site_content | markdownify }}
</div>
