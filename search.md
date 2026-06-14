---
layout: farshid_default
title: Search
permalink: /search/
---

<style>
  .search-box {
    max-width: 600px;
    margin: 0 auto 2rem;
  }
  .search-box input {
    width: 100%;
    padding: 14px 20px;
    font-size: 16px;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 12px;
    background: rgba(255,255,255,0.15);
    color: var(--text);
    outline: none;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
  }
  .search-box input::placeholder { color: var(--text-muted); }
  .search-box input:focus { border-color: var(--accent); }
  .search-results { max-width: 700px; margin: 0 auto; }
  .search-result {
    padding: 16px 0;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }
  .search-result a {
    color: var(--text);
    text-decoration: none;
    font-weight: 600;
    font-size: 1.05em;
  }
  .search-result a:hover { color: var(--accent); }
  .search-result p {
    color: var(--text-muted);
    font-size: 0.88em;
    margin: 4px 0 0;
    line-height: 1.5;
  }
  .search-count { color: var(--text-muted); font-size: 0.85em; margin-bottom: 1rem; text-align: center; }
</style>

<div class="search-box">
  <input type="text" id="search-input" placeholder="Search content..." autofocus>
</div>
<div class="search-count" id="search-count"></div>
<div class="search-results" id="search-results"></div>

<script>
(function() {
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  var count = document.getElementById("search-count");
  var data = [];

  fetch("/assets/search-index.json?t=" + Date.now())
    .then(function(r) { return r.json(); })
    .then(function(d) { data = d; });

  input.addEventListener("input", function() {
    var q = input.value.trim().toLowerCase();
    if (q.length < 2) { results.innerHTML = ""; count.textContent = ""; return; }

    var found = data.filter(function(item) {
      return item.title.toLowerCase().indexOf(q) !== -1 ||
             item.body.toLowerCase().indexOf(q) !== -1;
    });

    count.textContent = found.length + " result" + (found.length !== 1 ? "s" : "");
    results.innerHTML = found.map(function(item) {
      var snippet = item.body;
      var idx = snippet.toLowerCase().indexOf(q);
      if (idx !== -1) {
        var start = Math.max(0, idx - 60);
        var end = Math.min(snippet.length, idx + q.length + 60);
        snippet = (start > 0 ? "..." : "") + snippet.substring(start, end) + (end < snippet.length ? "..." : "");
        snippet = snippet.replace(new RegExp("(" + q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi"), "<strong>$1</strong>");
      }
      return '<div class="search-result"><a href="' + item.url + '">' + item.title + '</a><p>' + snippet + '</p></div>';
    }).join("");
  });
})();
</script>
