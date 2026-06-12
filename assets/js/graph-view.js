/**
 * Obsidian-style interactive knowledge graph.
 */
(function () {
  "use strict";

  var canvas = document.getElementById("graph-canvas");
  var wrap = document.getElementById("graph-wrap");
  if (!canvas || !wrap) return;

  var ctx = canvas.getContext("2d");
  var nodes = [];
  var links = [];
  var simNodes = [];
  var dragging = null;
  var hovered = null;
  var panX = 0;
  var panY = 0;
  var lastPanX = 0;
  var lastPanY = 0;
  var isPanning = false;
  var panStartX = 0;
  var panStartY = 0;
  var mouseDownX = 0;
  var mouseDownY = 0;
  var frozen = false;

  var STORAGE_KEY = "graph_positions_" + (wrap.dataset.graph || "default");

  var colors = {
    moc: "#5ac8fa",
    note: "#34c759",
    tag: "#af52de",
    link: "rgba(120, 120, 128, 0.25)",
    mocEdge: "rgba(90, 200, 250, 0.40)",
    text: "#1d1d1f",
    highlight: "#0071e3"
  };

  var isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  if (isDark) {
    colors.text = "#f5f5f7";
    colors.link = "rgba(180, 180, 190, 0.18)";
    colors.mocEdge = "rgba(90, 200, 250, 0.45)";
  }

  function resize() {
    var dpr = window.devicePixelRatio || 1;
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function loadPositions() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      return saved ? JSON.parse(saved) : {};
    } catch (e) { return {}; }
  }

  function savePositions() {
    var pos = {};
    for (var i = 0; i < simNodes.length; i++) {
      pos[simNodes[i].id] = { x: simNodes[i].x, y: simNodes[i].y };
    }
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(pos)); } catch (e) {}
  }

  function countConnections(idx) {
    var c = 0;
    for (var i = 0; i < links.length; i++) {
      if (links[i].source === idx || links[i].target === idx) c++;
    }
    return c;
  }

  function initSimulation(data) {
    nodes = data.nodes || [];
    links = data.links || [];
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;
    var saved = loadPositions();
    var idxMap = {};

    simNodes = nodes.map(function (n, i) {
      idxMap[n.id] = i;
      var sx = saved[n.id];
      if (sx && sx.x && sx.y) {
        return { id: n.id, label: n.label || n.id, url: n.url || null, raw: n.raw || null, kind: n.kind || "note", x: sx.x, y: sx.y, vx: 0, vy: 0, r: 0, connections: 0 };
      }
      var angle = (i / Math.max(nodes.length, 1)) * Math.PI * 2;
      var radius = Math.min(w, h) * 0.30;
      return { id: n.id, label: n.label || n.id, url: n.url || null, raw: n.raw || null, kind: n.kind || "note", x: w / 2 + Math.cos(angle) * radius, y: h / 2 + Math.sin(angle) * radius, vx: 0, vy: 0, r: 0, connections: 0 };
    });

    for (var i = 0; i < simNodes.length; i++) {
      simNodes[i].connections = countConnections(i);
      var n = simNodes[i];
      if (n.kind === "moc") n.r = 10 + Math.min(n.connections * 1.5, 8);
      else if (n.kind === "tag") n.r = 8 + Math.min(n.connections * 1.2, 6);
      else n.r = 5 + Math.min(n.connections * 0.8, 6);
    }

    var resolved = [];
    for (var i = 0; i < links.length; i++) {
      var s = idxMap[links[i].source];
      var t = idxMap[links[i].target];
      if (s !== undefined && t !== undefined) {
        resolved.push({ source: s, target: t, kind: links[i].kind || "link" });
      }
    }
    links = resolved;
  }

  function tick() {
    if (frozen) return;
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;
    var cx = w / 2 + panX;
    var cy = h / 2 + panY;

    for (var i = 0; i < simNodes.length; i++) {
      if (simNodes[i] === dragging) continue;
      simNodes[i].vx += (cx - simNodes[i].x) * 0.0008;
      simNodes[i].vy += (cy - simNodes[i].y) * 0.0008;
    }

    for (var i = 0; i < simNodes.length; i++) {
      for (var j = i + 1; j < simNodes.length; j++) {
        var dx = simNodes[i].x - simNodes[j].x;
        var dy = simNodes[i].y - simNodes[j].y;
        var dist = Math.sqrt(dx * dx + dy * dy) || 1;
        var force = 500 / (dist * dist);
        simNodes[i].vx += (dx / dist) * force;
        simNodes[i].vy += (dy / dist) * force;
        simNodes[j].vx -= (dx / dist) * force;
        simNodes[j].vy -= (dy / dist) * force;
      }
    }

    for (var i = 0; i < links.length; i++) {
      var a = simNodes[links[i].source];
      var b = simNodes[links[i].target];
      if (!a || !b) continue;
      var dx = b.x - a.x;
      var dy = b.y - a.y;
      var dist = Math.sqrt(dx * dx + dy * dy) || 1;
      var force = (dist - 100) * 0.025;
      a.vx += (dx / dist) * force;
      a.vy += (dy / dist) * force;
      b.vx -= (dx / dist) * force;
      b.vy -= (dy / dist) * force;
    }

    for (var i = 0; i < simNodes.length; i++) {
      if (dragging === simNodes[i]) continue;
      simNodes[i].vx *= 0.88;
      simNodes[i].vy *= 0.88;
      simNodes[i].x += simNodes[i].vx;
      simNodes[i].y += simNodes[i].vy;
    }
  }

  function draw() {
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;
    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(panX, panY);

    var connectedTo = {};
    if (hovered) {
      for (var i = 0; i < links.length; i++) {
        if (simNodes[links[i].source] === hovered) connectedTo[links[i].target] = true;
        if (simNodes[links[i].target] === hovered) connectedTo[links[i].source] = true;
      }
    }

    for (var i = 0; i < links.length; i++) {
      var a = simNodes[links[i].source];
      var b = simNodes[links[i].target];
      if (!a || !b) continue;
      var isHL = hovered && (a === hovered || b === hovered);
      var isDim = hovered && !isHL;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.strokeStyle = isHL ? colors.highlight : isDim ? "rgba(120,120,128,0.08)" : links[i].kind === "moc" ? colors.mocEdge : colors.link;
      ctx.lineWidth = isHL ? 2.5 : isDim ? 0.5 : 1;
      ctx.stroke();
    }

    for (var i = 0; i < simNodes.length; i++) {
      var n = simNodes[i];
      var isH = dragging === n || hovered === n;
      var isC = hovered && connectedTo[i];
      var isD = hovered && !isH && !isC;
      var fill = n.kind === "moc" ? colors.moc : n.kind === "tag" ? colors.tag : colors.note;
      var alpha = isD ? 0.2 : isH ? 1 : 0.82;
      var nodeR = isH ? n.r + 3 : n.r;

      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.arc(n.x, n.y, nodeR, 0, Math.PI * 2);
      ctx.fillStyle = fill;
      ctx.fill();
      ctx.strokeStyle = isH ? colors.highlight : "rgba(255,255,255,0.55)";
      ctx.lineWidth = isH ? 2.5 : 0.7;
      ctx.stroke();

      if (isH || isC || (!hovered && n.connections > 1)) {
        ctx.fillStyle = colors.text;
        ctx.font = isH ? "700 12px system-ui" : "500 10px system-ui";
        ctx.textAlign = "center";
        ctx.fillText(n.label, n.x, n.y + nodeR + 13);
      }
      ctx.globalAlpha = 1;
    }

    ctx.restore();

    if (hovered && hovered.label) {
      var sx = hovered.x + panX;
      var sy = hovered.y + panY - hovered.r - 12;
      var kind = hovered.kind === "moc" ? "Section" : hovered.kind === "tag" ? "Tag" : "Note";
      var text = kind + ": " + hovered.label;
      ctx.font = "600 11px system-ui";
      var tw = ctx.measureText(text).width;
      var pad = 7;
      var boxW = tw + pad * 2;
      var boxH = 22;
      var boxX = sx - boxW / 2;
      var boxY = sy - boxH;
      ctx.fillStyle = isDark ? "rgba(44,44,48,0.96)" : "rgba(255,255,255,0.94)";
      ctx.strokeStyle = isDark ? "rgba(255,255,255,0.10)" : "rgba(0,0,0,0.06)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.roundRect(boxX, boxY, boxW, boxH, 5);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = colors.text;
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(text, sx, boxY + boxH / 2);
      ctx.textBaseline = "alphabetic";
    }
  }

  function loop() {
    tick();
    draw();
    requestAnimationFrame(loop);
  }

  function screenPos(e) {
    var rect = canvas.getBoundingClientRect();
    return { x: e.clientX - rect.left - panX, y: e.clientY - rect.top - panY };
  }

  function hitTest(pos) {
    for (var i = simNodes.length - 1; i >= 0; i--) {
      var n = simNodes[i];
      var dx = pos.x - n.x;
      var dy = pos.y - n.y;
      if (dx * dx + dy * dy <= (n.r + 8) * (n.r + 8)) return n;
    }
    return null;
  }

  function resolveNodeUrl(n) {
    if (!n) return null;
    if (n.url) return n.url;
    if (n.raw) {
      if (/^\/contents\//i.test(n.raw)) {
        if (n.raw.endsWith("/")) return n.raw;
      }
      return n.raw;
    }
    return null;
  }

  canvas.addEventListener("mousedown", function (e) {
    mouseDownX = e.clientX;
    mouseDownY = e.clientY;
    var pos = screenPos(e);
    var hit = hitTest(pos);
    if (hit) {
      dragging = hit;
      hit.vx = hit.vy = 0;
      frozen = true;
      canvas.style.cursor = "grabbing";
    } else {
      isPanning = true;
      panStartX = e.clientX;
      panStartY = e.clientY;
      lastPanX = panX;
      lastPanY = panY;
      canvas.style.cursor = "grabbing";
    }
  });

  window.addEventListener("mousemove", function (e) {
    if (dragging) {
      dragging.x = screenPos(e).x;
      dragging.y = screenPos(e).y;
      dragging.vx = dragging.vy = 0;
      return;
    }
    if (isPanning) {
      panX = lastPanX + (e.clientX - panStartX);
      panY = lastPanY + (e.clientY - panStartY);
      return;
    }
    hovered = hitTest(screenPos(e));
    canvas.style.cursor = hovered ? "pointer" : "grab";
  });

  window.addEventListener("mouseup", function (e) {
    var movedX = Math.abs(e.clientX - mouseDownX);
    var movedY = Math.abs(e.clientY - mouseDownY);
    var didDrag = movedX > 5 || movedY > 5;

    if (dragging) {
      if (!didDrag) {
        frozen = false;
        var url = resolveNodeUrl(dragging);
        if (url) window.location.href = url;
      } else {
        savePositions();
      }
      dragging = null;
    } else if (isPanning && !didDrag) {
      var hit = hitTest(screenPos(e));
      if (hit) {
        var url = resolveNodeUrl(hit);
        if (url) window.location.href = url;
      }
    }

    isPanning = false;
    frozen = false;
    canvas.style.cursor = hovered ? "pointer" : "grab";
  });

  canvas.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) return;
    var touch = e.touches[0];
    mouseDownX = touch.clientX;
    mouseDownY = touch.clientY;
    var rect = canvas.getBoundingClientRect();
    var pos = { x: touch.clientX - rect.left - panX, y: touch.clientY - rect.top - panY };
    var hit = hitTest(pos);
    if (hit) {
      dragging = hit;
      hit.vx = hit.vy = 0;
      frozen = true;
    } else {
      isPanning = true;
      panStartX = touch.clientX;
      panStartY = touch.clientY;
      lastPanX = panX;
      lastPanY = panY;
    }
    e.preventDefault();
  }, { passive: false });

  canvas.addEventListener("touchmove", function (e) {
    if (e.touches.length !== 1) return;
    var touch = e.touches[0];
    e.preventDefault();
    var rect = canvas.getBoundingClientRect();
    if (dragging) {
      dragging.x = touch.clientX - rect.left - panX;
      dragging.y = touch.clientY - rect.top - panY;
      dragging.vx = dragging.vy = 0;
    } else if (isPanning) {
      panX = lastPanX + (touch.clientX - panStartX);
      panY = lastPanY + (touch.clientY - panStartY);
    }
  }, { passive: false });

  canvas.addEventListener("touchend", function (e) {
    var movedX = Math.abs((e.changedTouches[0] || {}).clientX - mouseDownX);
    var movedY = Math.abs((e.changedTouches[0] || {}).clientY - mouseDownY);
    var didDrag = movedX > 10 || movedY > 10;

    if (dragging) {
      if (!didDrag) {
        frozen = false;
        var url = resolveNodeUrl(dragging);
        if (url) window.location.href = url;
      } else {
        savePositions();
      }
      dragging = null;
    }
    isPanning = false;
    frozen = false;
  });

  canvas.addEventListener("wheel", function (e) {
    e.preventDefault();
  }, { passive: false });

  window.addEventListener("resize", resize);

  var resetBtn = document.getElementById("graph-reset");
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      panX = panY = 0;
      frozen = false;
      try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
      initSimulation({ nodes: nodes, links: links });
    });
  }

  var freezeBtn = document.getElementById("graph-freeze");
  if (freezeBtn) {
    freezeBtn.addEventListener("click", function () {
      frozen = !frozen;
      freezeBtn.textContent = frozen ? "Unfreeze" : "Freeze";
    });
  }

  var graphFile = wrap.dataset.graph || "/assets/graph.json";
  fetch(graphFile)
    .then(function (r) { if (!r.ok) throw new Error("no graph"); return r.json(); })
    .then(function (data) {
      resize();
      initSimulation(data);
      loop();
      var stat = document.getElementById("graph-stats");
      if (stat) {
        var tagCount = data.nodes.filter(function (n) { return n.kind === "tag"; }).length;
        var noteCount = data.nodes.filter(function (n) { return n.kind !== "tag"; }).length;
        stat.textContent = noteCount + " notes · " + tagCount + " tags · " + data.links.length + " links";
      }
    })
    .catch(function () {
      var stat = document.getElementById("graph-stats");
      if (stat) stat.textContent = "Graph data missing";
    });
})();
