---
layout: farshid_default
title: Knowledge Graph
permalink: /graph/
extra_css: graph.css
---

<div class="graph-page">
  <div class="graph-header">
    <h1>Knowledge Graph</h1>
    <span class="graph-stats" id="graph-stats">Loading…</span>
    <div class="graph-controls">
      <button type="button" id="graph-zoom-in" class="liquid-glass-item" title="Zoom in">+</button>
      <button type="button" id="graph-zoom-out" class="liquid-glass-item" title="Zoom out">−</button>
      <button type="button" id="graph-reset" class="liquid-glass-item">Reset</button>
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtags</a>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
    </div>
  </div>
  <p class="graph-hint">Drag nodes · click to open · scroll to zoom</p>
  <div id="graph-wrap" class="liquid-glass">
    <canvas id="graph-canvas" aria-label="Interactive knowledge graph"></canvas>
  </div>
  <div class="graph-legend">
    <span class="legend-moc">Section</span>
    <span class="legend-note">Note</span>
    <span class="legend-tag">Hashtag</span>
  </div>
</div>

<script src="{{ '/assets/js/graph-view.js' | relative_url }}" defer></script>
