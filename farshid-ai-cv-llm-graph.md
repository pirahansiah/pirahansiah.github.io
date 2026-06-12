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
      <button type="button" id="graph-reset" class="liquid-glass-item">Reset layout</button>
      <a href="{{ '/' | relative_url }}" class="liquid-glass-item">Home</a>
      <a href="{{ '/graph-tags/' | relative_url }}" class="liquid-glass-item">Hashtag graph</a>
    </div>
  </div>
  <p class="graph-hint">Drag nodes · click a note to open · built from <code>contents/farshid-ai-cv-llm-site.md</code> and wiki links in your notes</p>
  <div id="graph-wrap" class="liquid-glass">
    <canvas id="graph-canvas" aria-label="Interactive knowledge graph"></canvas>
  </div>
  <div class="graph-legend">
    <span class="legend-moc">MOC / menu section</span>
    <span class="legend-note">Markdown note</span>
    <span class="legend-tag">Hashtag</span>
  </div>
</div>

<script src="{{ '/assets/js/graph-view.js' | relative_url }}" defer></script>
