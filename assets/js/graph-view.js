/**
 * Obsidian-style interactive knowledge graph (vanilla JS + canvas, no libraries).
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
    link: "rgba(120, 120, 128, 0.45)",
    mocEdge: "rgba(90, 200, 250, 0.55)",
    text: "#1d1d1f",
    highlight: "#0071e3"
  };

  if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    colors.text = "#f5f5f7";
    colors.link = "rgba(180, 180, 190, 0.35)";
    colors.mocEdge = "rgba(90, 200, 250, 0.65)";
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

  function initSimulation(data) {
    nodes = data.nodes || [];
    links = data.links || [];
    var w = wrap.clientWidth;
    var h = wrap.clientHeight;

    simNodes = nodes.map(function (n, i) {
      var angle = (i / Math.max(nodes.length, 1)) * Math.PI * 2;
      var r = Math.min(w, h) * 0.28;
      return {
        id: n.id,
        label: n.label || n.id,
        url: n.url || null,
        raw: n.raw || null,
        kind: n.kind || "note",
        x: w / 2 + Math.cos(angle) * r,
        y: h / 2 + Math.sin(angle) * r,
        vx: 0,
        vy: 0,
        r: n.kind === "moc" ? 14 : 10
      };
    });

    var idx = indexNodes();
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
    var i;
    var j;
    var dx;
    var dy;
    var dist;
    var force;

    for (i = 0; i < simNodes.length; i++) {
      dx = cx - simNodes[i].x;
      dy = cy - simNodes[i].y;
      simNodes[i].vx += dx * 0.002;
      simNodes[i].vy += dy * 0.002;
    }

    for (i = 0; i < simNodes.length; i++) {
      for (j = i + 1; j < simNodes.length; j++) {
        dx = simNodes[i].x - simNodes[j].x;
        dy = simNodes[i].y - simNodes[j].y;
        dist = Math.sqrt(dx * dx + dy * dy) || 1;
        force = 520 / (dist * dist);
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
      force = (dist - 90) * 0.035;
      a.vx += (dx / dist) * force;
      a.vy += (dy / dist) * force;
      b.vx -= (dx / dist) * force;
      b.vy -= (dy / dist) * force;
    }

    for (i = 0; i < simNodes.length; i++) {
      if (dragging === simNodes[i]) continue;
      simNodes[i].vx *= 0.86;
      simNodes[i].vy *= 0.86;
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
    for (i = 0; i < links.length; i++) {
      var a = simNodes[links[i].source];
      var b = simNodes[links[i].target];
      if (!a || !b) continue;
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.strokeStyle = links[i].kind === "moc" ? colors.mocEdge : colors.link;
      ctx.lineWidth = links[i].kind === "moc" ? 2 : 1;
      ctx.stroke();
    }

    for (i = 0; i < simNodes.length; i++) {
      var n = simNodes[i];
      var active = dragging === n || hovered === n;
      var fill = n.kind === "moc" ? colors.moc : colors.note;

      ctx.beginPath();
      ctx.arc(n.x, n.y, active ? n.r + 3 : n.r, 0, Math.PI * 2);
      ctx.fillStyle = fill;
      ctx.globalAlpha = active ? 1 : 0.88;
      ctx.fill();
      ctx.globalAlpha = 1;
      ctx.strokeStyle = active ? colors.highlight : "rgba(255,255,255,0.65)";
      ctx.lineWidth = active ? 2.5 : 1;
      ctx.stroke();

      ctx.fillStyle = colors.text;
      ctx.font = "600 11px system-ui, -apple-system, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(n.label, n.x, n.y + n.r + 14);
    }

    ctx.restore();
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
      if (dx * dx + dy * dy <= (n.r + 6) * (n.r + 6)) return n;
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
      scale = Math.max(0.5, Math.min(2, scale - e.deltaY * 0.001));
      panX += e.deltaX * 0.5;
      panY += e.deltaY * 0.5;
    },
    { passive: false }
  );

  window.addEventListener("resize", resize);

  var resetBtn = document.getElementById("graph-reset");
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      panX = panY = 0;
      scale = 1;
      initSimulation({ nodes: nodes, links: links });
    });
  }

  fetch("/assets/graph.json")
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
        stat.textContent =
          data.nodes.length + " notes · " + data.links.length + " links";
      }
    })
    .catch(function () {
      var stat = document.getElementById("graph-stats");
      if (stat) {
        stat.textContent = "Graph data missing — run ruby scripts/build-nav.rb";
      }
    });
})();
