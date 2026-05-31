---
layout: default
title: Farshid Pirahansiah
permalink: /
---

<div id="site-content">Loading...</div>

<script>
fetch('/contents/site.md')
  .then(r => r.text())
  .then(text => {
    const div = document.getElementById('site-content');
    let html = '';
    text.split('\n').forEach(line => {
      const s = line.trim();
      if (!s) { html += '<br>'; return; }
      if (s.startsWith('### ')) html += `<h3>${s.slice(4)}</h3>`;
      else if (s.startsWith('## ')) html += `<h2>${s.slice(3)}</h2>`;
      else if (s.startsWith('# '))  html += `<h1>${s.slice(2)}</h1>`;
      else if (s.startsWith('[') && s.includes('](')) {
        const label = s.split('[')[1].split(']')[0];
        const url   = s.split('](')[1].replace(')', '');
        html += `<p><a href="${url}">${label}</a></p>`;
      }
      else html += `<p>${s}</p>`;
    });
    div.innerHTML = html;
  });
</script>