/**
 * Obsidian-style interactive knowledge graph (vanilla JS + canvas).
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
  var scale = 1;
  var panX = 0;
  var panY = 0;
  var animId = 0;

  var colors = {
    moc: "#5ac8fa",
    note: "#34c759",
    tag: "#af52de",
    link: "rgba(120, 120, 128, 0.30)",
    mocEdge: "rgba(90, 200, 250, 0.45)",
    text: "#1d1d1f",
    textMuted: "rgba(29, 29, 31, 0.6)",
    highlight: "#0071e3",
    tooltipBg: "rgba(255, 255, 255, 0.92)",
    tooltipBorder: "rgba(0, 0, 0, 0.08)"
  };

  var isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  if (isDark) {
    colors.text = "#f5f5f7";
    colors.textMuted = "rgba(245, 245, 247, 0.5)";
    colors.link = "rgba(180, 180, 190, 0.20)";
    colors.mocEdge = "rgba(90, 200, 250, 0.50)";
    colors.tooltipBg = "rgba(44, 44, 48, 0.94)";
    colors.tooltipBorder = "rgba(255, 255, 255, 0.12)";
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

  function indexNodes() {
    var map = {};
    for (var i = 0; i < simNodes.length; i++) {
      map[simNodes[i].id] = i;
    }
    return map;
  }

  function countConnections(nodeIdx) {
    var count = 0;
    for (var i = 0; i < links.length; i++) {
      if (links[i].source === nodeIdx || links[i].target === nodeIdx) count++;
    }
    return count;
  }

  function initSimulation(data) {
    nodes = data.nodes || [];
    links = data.links || [];
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;

    simNodes = nodes.map(function (n, i) {
      var angle = (i / Math.max(nodes.length, 1)) * Math.PI * 2;
      var r = Math.min(w, h) * 0.30;
      return {
        id: n.id,
        label: n.label || n.id,
        url: n.url || null,
        raw: n.raw || null,
        kind: n.kind || "note",
        x: w / 2 + Math.cos(angle) * r + (Math.random() - 0.5) * 60,
        y: h / 2 + Math.sin(angle) * r + (Math.random() - 0.5) * 60,
        vx: 0,
        vy: 0,
        r: 0,
        connections: 0
      };
    });

    var idx = indexNodes();
    for (var i = 0; i < simNodes.length; i++) {
      simNodes[i].connections = countConnections(i);
    }

    for (var i = 0; i < simNodes.length; i++) {
      var n = simNodes[i];
      if (n.kind === "moc") {
        n.r = 12 + Math.min(n.connections * 1.5, 8);
      } else if (n.kind === "tag") {
        n.r = 8 + Math.min(n.connections * 1.2, 6);
      } else {
        n.r = 6 + Math.min(n.connections * 0.8, 6);
      }
    }

    links = links
      .map(function (l) {
        return {
          source: idx[l.source],
          target: idx[l.target],
          kind: l.kind || "link"
        };
      })
      .filter(function (l) {
        return l.source !== undefined && l.target !== undefined;
      });
  }

  function tick() {
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;
    var cx = w / 2 + panX;
    var cy = h / 2 + panY;
    var i, j, dx, dy, dist, force;

    for (i = 0; i < simNodes.length; i++) {
      dx = cx - simNodes[i].x;
      dy = cy - simNodes[i].y;
      simNodes[i].vx += dx * 0.001;
      simNodes[i].vy += dy * 0.001;
    }

    for (i = 0; i < simNodes.length; i++) {
      for (j = i + 1; j < simNodes.length; j++) {
        dx = simNodes[i].x - simNodes[j].x;
        dy = simNodes[i].y - simNodes[j].y;
        dist = Math.sqrt(dx * dx + dy * dy) || 1;
        force = 600 / (dist * dist);
        simNodes[i].vx += (dx / dist) * force;
        simNodes[i].vy += (dy / dist) * force;
        simNodes[j].vx -= (dx / dist) * force;
        simNodes[j].vy -= (dy / dist) * force;
      }
    }

    for (i = 0; i < links.length; i++) {
      var a = simNodes[links[i].source];
      var b = simNodes[links[i].target];
      if (!a || !b) continue;
      dx = b.x - a.x;
      dy = b.y - a.y;
      dist = Math.sqrt(dx * dx + dy * dy) || 1;
      force = (dist - 100) * 0.030;
      a.vx += (dx / dist) * force;
      a.vy += (dy / dist) * force;
      b.vx -= (dx / dist) * force;
      b.vy -= (dy / dist) * force;
    }

    for (i = 0; i < simNodes.length; i++) {
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

    var i;

    var connectedTo = {};
    if (hovered) {
      for (i = 0; i < links.length; i++) {
        if (simNodes[links[i].source] === hovered) {
          connectedTo[links[i].target] = true;
        }
        if (simNodes[links[i].target] === hovered) {
          connectedTo[links[i].source] = true;
        }
      }
    }

    for (i = 0; i < links.length; i++) {
      var a = simNodes[links[i].source];
      var b = simNodes[links[i].target];
      if (!a || !b) continue;

      var isHighlighted = hovered && (a === hovered || b === hovered);
      var isDimmed = hovered && !isHighlighted;

      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.strokeStyle = isHighlighted
        ? colors.highlight
        : isDimmed
          ? "rgba(120, 120, 128, 0.10)"
          : links[i].kind === "moc"
            ? colors.mocEdge
            : colors.link;
      ctx.lineWidth = isHighlighted ? 2 : isDimmed ? 0.5 : 1;
      ctx.stroke();
    }

    for (i = 0; i < simNodes.length; i++) {
      var n = simNodes[i];
      var isHovered = dragging === n || hovered === n;
      var isConnected = hovered && connectedTo[i];
      var isDimmed = hovered && !isHovered && !isConnected;

      var fill = n.kind === "moc" ? colors.moc : n.kind === "tag" ? colors.tag : colors.note;
      var alpha = isDimmed ? 0.25 : isHovered ? 1 : 0.85;
      var nodeR = isHovered ? n.r + 3 : n.r;

      ctx.globalAlpha = alpha;

      ctx.beginPath();
      ctx.arc(n.x, n.y, nodeR, 0, Math.PI * 2);
      ctx.fillStyle = fill;
      ctx.fill();

      ctx.strokeStyle = isHovered ? colors.highlight : "rgba(255,255,255,0.60)";
      ctx.lineWidth = isHovered ? 2.5 : 0.8;
      ctx.stroke();

      if (isHovered || isConnected || (!hovered && n.connections > 2)) {
        ctx.fillStyle = colors.text;
        ctx.font = isHovered
          ? "700 12px system-ui, -apple-system, sans-serif"
          : "500 10px system-ui, -apple-system, sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(n.label, n.x, n.y + nodeR + 13);
      }

      ctx.globalAlpha = 1;
    }

    ctx.restore();

    if (hovered && hovered.label) {
      var sx = hovered.x + panX;
      var sy = hovered.y + panY - hovered.r - 10;
      var label = hovered.label;
      var kind = hovered.kind === "moc" ? "Section" : hovered.kind === "tag" ? "Tag" : "Note";
      var text = kind + ": " + label;

      ctx.font = "600 12px system-ui, -apple-system, sans-serif";
      var tw = ctx.measureText(text).width;
      var pad = 8;
      var boxW = tw + pad * 2;
      var boxH = 24;
      var boxX = sx - boxW / 2;
      var boxY = sy - boxH;

      ctx.fillStyle = colors.tooltipBg;
      ctx.strokeStyle = colors.tooltipBorder;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.roundRect(boxX, boxY, boxW, boxH, 6);
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
    animId = requestAnimationFrame(loop);
  }

  function screenPos(e) {
    var rect = canvas.getBoundingClientRect();
    return {
      x: e.clientX - rect.left - panX,
      y: e.clientY - rect.top - panY
    };
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

  canvas.addEventListener("mousedown", function (e) {
    var pos = screenPos(e);
    var hit = hitTest(pos);
    if (hit) {
      dragging = hit;
      hit.vx = hit.vy = 0;
    }
  });

  window.addEventListener("mousemove", function (e) {
    if (dragging) {
      var pos = screenPos(e);
      dragging.x = pos.x;
      dragging.y = pos.y;
      dragging.vx = dragging.vy = 0;
      return;
    }
    hovered = hitTest(screenPos(e));
    canvas.style.cursor = hovered ? "pointer" : "grab";
  });

  window.addEventListener("mouseup", function () {
    dragging = null;
  });

  canvas.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) return;
    var touch = e.touches[0];
    var rect = canvas.getBoundingClientRect();
    var pos = { x: touch.clientX - rect.left - panX, y: touch.clientY - rect.top - panY };
    var hit = hitTest(pos);
    if (hit) {
      dragging = hit;
      hit.vx = hit.vy = 0;
      e.preventDefault();
    }
  }, { passive: false });

  canvas.addEventListener("touchmove", function (e) {
    if (!dragging || e.touches.length !== 1) return;
    e.preventDefault();
    var touch = e.touches[0];
    var rect = canvas.getBoundingClientRect();
    dragging.x = touch.clientX - rect.left - panX;
    dragging.y = touch.clientY - rect.top - panY;
    dragging.vx = dragging.vy = 0;
  }, { passive: false });

  canvas.addEventListener("touchend", function () {
    if (dragging) {
      var hit = dragging;
      dragging = null;
      var url = resolveNodeUrl(hit);
      if (url) window.location.href = url;
    }
  });

  function resolveNodeUrl(n) {
    if (!n) return null;
    if (n.url) return n.url;
    if (n.raw) {
      if (/^\/contents\//i.test(n.raw)) {
        if (/\/view\/\?/.test(n.raw)) return n.raw;
        var ext = n.raw.split(".").pop().toLowerCase();
        var staticExt =
          "html htm pdf py cpp c h java js ts go rb php txt md json xml css png jpg".split(" ");
        if (n.raw.endsWith("/")) return n.raw;
        if (staticExt.indexOf(ext) !== -1 && ext !== "md") {
          return "/view/?p=" + encodeURIComponent(n.raw);
        }
      }
      return n.raw;
    }
    return null;
  }

  canvas.addEventListener("click", function (e) {
    if (dragging) return;
    var hit = hitTest(screenPos(e));
    var target = resolveNodeUrl(hit);
    if (target) {
      window.location.href = target;
    }
  });

  canvas.addEventListener(
    "wheel",
    function (e) {
      e.preventDefault();
      scale = Math.max(0.3, Math.min(3, scale - e.deltaY * 0.001));
      panX += e.deltaX * 0.5;
      panY += e.deltaY * 0.5;
    },
    { passive: false }
  );

  window.addEventListener("resize", function () {
    resize();
  });

  var resetBtn = document.getElementById("graph-reset");
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      panX = panY = 0;
      scale = 1;
      initSimulation({ nodes: nodes, links: links });
    });
  }

  var zoomInBtn = document.getElementById("graph-zoom-in");
  if (zoomInBtn) {
    zoomInBtn.addEventListener("click", function () {
      scale = Math.min(3, scale + 0.2);
    });
  }

  var zoomOutBtn = document.getElementById("graph-zoom-out");
  if (zoomOutBtn) {
    zoomOutBtn.addEventListener("click", function () {
      scale = Math.max(0.3, scale - 0.2);
    });
  }

  var graphFile = wrap.dataset.graph || "/assets/graph.json";
  fetch(graphFile)
    .then(function (r) {
      if (!r.ok) throw new Error("no graph");
      return r.json();
    })
    .then(function (data) {
      resize();
      initSimulation(data);
      loop();
      var stat = document.getElementById("graph-stats");
      if (stat) {
        var onlyTags = Array.isArray(data.nodes) && data.nodes.length > 0 && data.nodes.every(function (n) {
          return n.kind === "tag";
        });
        stat.textContent = onlyTags
          ? data.nodes.length + " tags · " + data.links.length + " co-occurrences"
          : data.nodes.length + " notes · " + data.links.length + " links";
      }
    })
    .catch(function () {
      var stat = document.getElementById("graph-stats");
      if (stat) {
        stat.textContent = "Graph data missing";
      }
    });
})();
