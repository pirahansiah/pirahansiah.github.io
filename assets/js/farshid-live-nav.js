/**
 * Live nav builder — fetches menus.md and builds nav in real-time.
 * No build step needed. Just edit menus.md and the nav updates on next page load.
 */
(function () {
  "use strict";

  var navList = document.getElementById("nav-list");
  if (!navList) return;

  var MENUS_URL = (window.location.pathname.includes("/contents/")
    ? "/contents/menus.md"
    : "/menus.md");

  function parseMenusMd(md) {
    var lines = md.split("\n");
    var items = [];
    var currentGroup = null;

    for (var i = 0; i < lines.length; i++) {
      var line = lines[i].trim();
      if (!line) continue;

      // Skip frontmatter
      if (line === "---") continue;

      // ## heading = group title
      if (/^##\s+/.test(line)) {
        var groupTitle = line.replace(/^##\s+/, "").trim();
        if (groupTitle && groupTitle !== "all files" && groupTitle !== "all links") {
          currentGroup = { title: groupTitle, items: [] };
          items.push(currentGroup);
        }
        continue;
      }

      // # heading = top-level menu item (skip "all files", "all links")
      if (/^#\s+/.test(line)) {
        var topTitle = line.replace(/^#\s+/, "").replace(/[🗺️]/g, "").trim();
        if (topTitle && topTitle !== "all files" && topTitle !== "all links") {
          currentGroup = { title: topTitle, items: [] };
          items.push(currentGroup);
        }
        continue;
      }

      // [text](url) = link item
      var linkMatch = line.match(/^\[([^\]]+)\]\(([^)]+)\)/);
      if (linkMatch && currentGroup) {
        var linkTitle = linkMatch[1].trim();
        var linkUrl = linkMatch[2].trim();
        // Convert .md links to clean URLs for GitHub Pages
        if (linkUrl.endsWith(".md")) {
          linkUrl = linkUrl.replace(/\.md$/, "");
        }
        // Make relative URLs work
        if (linkUrl.startsWith("./")) {
          linkUrl = "/contents/" + linkUrl.substring(2);
        }
        currentGroup.items.push({ title: linkTitle, url: linkUrl });
      }
    }

    return items;
  }

  function buildNav(items) {
    // Remove static nav items (keep only the GitHub link)
    var existing = navList.querySelectorAll("li");
    for (var i = existing.length - 1; i >= 0; i--) {
      if (!existing[i].querySelector('a[href*="github.com"]')) {
        existing[i].remove();
      }
    }

    // Build from parsed menus.md
    for (var g = 0; g < items.length; g++) {
      var group = items[g];
      var li = document.createElement("li");

      if (group.items.length > 0) {
        li.className = "has-children";
        var toggle = document.createElement("a");
        toggle.href = "#";
        toggle.className = "liquid-glass-item nav-link";
        toggle.setAttribute("data-nav-toggle", "");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = group.title;
        var chevron = document.createElement("span");
        chevron.className = "nav-chevron";
        chevron.setAttribute("aria-hidden", "true");
        chevron.textContent = " ▾";
        toggle.appendChild(chevron);
        li.appendChild(toggle);

        var sub = document.createElement("ul");
        sub.className = "nav-sub";
        for (var j = 0; j < group.items.length; j++) {
          var subLi = document.createElement("li");
          var subA = document.createElement("a");
          subA.href = group.items[j].url;
          subA.className = "liquid-glass-item";
          subA.textContent = group.items[j].title;
          subLi.appendChild(subA);
          sub.appendChild(subLi);
        }
        li.appendChild(sub);
      } else {
        var a = document.createElement("a");
        a.href = "#";
        a.className = "liquid-glass-item";
        a.textContent = group.title;
        li.appendChild(a);
      }

      // Insert before the GitHub link
      var githubLink = navList.querySelector('a[href*="github.com"]');
      if (githubLink) {
        navList.insertBefore(li, githubLink.parentElement);
      } else {
        navList.appendChild(li);
      }
    }
  }

  fetch(MENUS_URL + "?t=" + Date.now())
    .then(function (r) { return r.ok ? r.text() : null; })
    .then(function (md) {
      if (!md) return;
      var items = parseMenusMd(md);
      if (items.length > 0) buildNav(items);
    })
    .catch(function () {});
})();
