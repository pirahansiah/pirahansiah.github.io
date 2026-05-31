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
    buildMenu(text);
    renderContent(text);
  });

function buildMenu(text) {
  const nav = document.getElementById('dynamic-nav');
  const lines = text.split('\n');
  let topLi = null;
  let subUl = null;
  let pendingH2 = null;

  function flushH2(url) {
    if (!pendingH2 || !subUl) return;
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.textContent = pendingH2;
    a.href = url || ('#' + pendingH2.toLowerCase().replace(/\s+/g,'-'));
    li.appendChild(a);
    subUl.appendChild(li);
    pendingH2 = null;
  }

  function flushTop() {
    if (!topLi) return;
    flushH2(null);
    if (subUl && subUl.children.length > 0) {
      topLi.classList.add('has-submenu');
      topLi.appendChild(subUl);
    }
    nav.insertBefore(topLi, nav.firstChild);
    topLi = null;
    subUl = null;
  }

  lines.forEach(line => {
    const s = line.trim();
    if (!s) return;

    if (s.startsWith('## ')) {
      flushH2(null);
      pendingH2 = s.slice(3).trim();
      if (!subUl) subUl = document.createElement('ul');
      subUl.className = 'submenu';

    } else if (s.startsWith('# ')) {
      flushTop();
      topLi = document.createElement('li');
      const a = document.createElement('a');
      a.textContent = s.slice(2).trim();
      a.href = '#';
      topLi.appendChild(a);
      subUl = null;
      pendingH2 = null;

    } else if (s.startsWith('[') && s.includes('](') && pendingH2) {
      const url = s.split('](')[1].replace(')', '').trim();
      flushH2(url);

    } else if (pendingH2) {
      flushH2(null);
    }
  });

  flushTop();
}

function renderContent(text) {
  // Convert markdown to HTML manually for display
  const div = document.getElementById('site-content');
  const lines = text.split('\n');
  let html = '';
  lines.forEach(line => {
    const s = line.trim();
    if (!s) { html += '<br>'; return; }
    if (s.startsWith('### ')) html += `<h3>${s.slice(4)}</h3>`;
    else if (s.startsWith('## ')) html += `<h2>${s.slice(3)}</h2>`;
    else if (s.startsWith('# ')) html += `<h1>${s.slice(2)}</h1>`;
    else if (s.startsWith('[') && s.includes('](')) {
      const label = s.split('[')[1].split(']')[0];
      const url = s.split('](')[1].replace(')', '');
      html += `<p><a href="${url}">${label}</a></p>`;
    }
    else html += `<p>${s}</p>`;
  });
  div.innerHTML = html;
}
</script>