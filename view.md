---
layout: default
title: View
permalink: /view/
extra_css: viewer.css
---

<div class="content-viewer" id="content-viewer">
  <div class="viewer-bar liquid-glass">
    <span class="viewer-title" id="viewer-title">Loading…</span>
    <div class="viewer-actions">
      <a id="viewer-open" class="liquid-glass-item" href="#" target="_blank" rel="noopener">Open file</a>
      <a id="viewer-download" class="liquid-glass-item" href="#" download>Download</a>
    </div>
  </div>
  <div class="viewer-stage liquid-glass" id="viewer-stage">
    <p class="viewer-placeholder">Select a file from the menu.</p>
  </div>
</div>

<script src="{{ '/assets/js/content-viewer.js' | relative_url }}" defer></script>
