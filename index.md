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