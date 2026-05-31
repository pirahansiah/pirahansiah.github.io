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
    document.getElementById('site-content').innerHTML = '<pre>' + text + '</pre>';
    buildMenu(text);
  });

function buildMenu(text) {
  const lines = text.split('\n');
  const nav = document.getElementById('dynamic-nav');
  let currentTop = null;
  let submenu = null;

  lines.forEach(line => {
    const s = line.trim();
    if (!s) return;

    if (s.startsWith('## ')) {
      const label = s.slice(3).trim();
      if (!submenu) {
        submenu = document.createElement('ul');
        submenu.className = 'submenu';
        currentTop.appendChild(submenu);
      }
      // next line might be a link — store label, look ahead handled below
      submenu.setAttribute('data-next', label);

    } else if (s.startsWith('# ')) {
      const label = s.slice(2).trim();
      currentTop = document.createElement('li');
      currentTop.className = 'has-submenu';
      const a = document.createElement('a');
      a.href = '#';
      a.textContent = label;
      currentTop.appendChild(a);
      nav.appendChild(currentTop);
      submenu = null;

    } else if (s.startsWith('[') && submenu) {
      const url = s.split('(')[1]?.split(')')[0] || '#';
      const pendingLabel = submenu.getAttribute('data-next');
      if (pendingLabel) {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = url;
        a.textContent = pendingLabel;
        li.appendChild(a);
        submenu.appendChild(li);
        submenu.removeAttribute('data-next');
      }
    } else if (submenu && submenu.getAttribute('data-next')) {
      // ## item with no link — add as anchor
      const label = submenu.getAttribute('data-next');
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#' + label.toLowerCase().replace(/ /g,'-');
      a.textContent = label;
      li.appendChild(a);
      submenu.appendChild(li);
      submenu.removeAttribute('data-next');
    }
  });
}
</script>