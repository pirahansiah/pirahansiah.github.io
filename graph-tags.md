---
layout: default
title: Hashtag Graph
permalink: /graph-tags/
extra_css: graph.css
---

<div class="graph-page" data-graph="/assets/graph-hashtags.json">
  <div class="graph-header">
    <h1>Hashtag Graph</h1>
    <span class="graph-stats" id="graph-stats">Loading…</span>
    <div class="graph-controls">
      <button type="button" id="graph-reset" class="liquid-glass-item">Reset layout</button>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
      <a href="{{ '/graph/' | relative_url }}" class="liquid-glass-item">Full graph</a>
    </div>
  </div>
  <p class="graph-hint">Drag nodes · click a note to open · built from hashtags found in your contents</p>
  <div id="graph-wrap" class="liquid-glass">
    <canvas id="graph-canvas" aria-label="Interactive hashtag graph"></canvas>
  </div>
  <div class="graph-legend">
    <span class="legend-note">Note</span>
    <span class="legend-tag">Hashtag</span>
  </div>
</div>

<script src="{{ '/assets/js/graph-view.js' | relative_url }}" defer></script>
