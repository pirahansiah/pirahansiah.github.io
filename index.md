---
layout: default
title: Farshid Pirahansiah
permalink: /
---

<div id="site-content"></div>

<script>
fetch('/contents/site.md')
  .then(r => r.text())
  .then(text => {
    let html = '';
    text.split('\n').forEach(line => {
      const s = line.trim();
      if (!s) { html += '<br>'; return; }
      if (s.startsWith('### ')) { html += `<h3>${s.slice(4)}</h3>`; return; }
      if (s.startsWith('## '))  { html += `<h2>${s.slice(3)}</h2>`; return; }
      if (s.startsWith('# '))   { html += `<h1>${s.slice(2)}</h1>`; return; }
      const linkMatch = s.match(/^\[(.+?)\]\((.+?)\)$/);
      if (linkMatch) { html += `<p><a href="${linkMatch[2]}">${linkMatch[1]}</a></p>`; return; }
      html += `<p>${s}</p>`;
    });
    document.getElementById('site-content').innerHTML = html;
  });
</script>
<!-- SVG Filter for the Liquid Distortion -->
<svg style="display: none;">
  <defs>
    <filter id="liquid-refraction">
      <feTurbulence type="fractalNoise" baseFrequency="0.01" numOctaves="3" result="noise" />
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="5" />
    </filter>
  </defs>
</svg>

<!-- Vanilla JS for Mouse Tracking (No Packages Needed) -->
<script>
  document.addEventListener('mousemove', (e) => {
    const glassElements = document.querySelectorAll('.liquid-glass');
    glassElements.forEach(el => {
      const rect = el.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      el.style.setProperty('--mouse-x', `${x}%`);
      el.style.setProperty('--mouse-y', `${y}%`);
    });
  });
</script>
