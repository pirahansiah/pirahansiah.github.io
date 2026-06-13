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
    var inFrontmatter = false;

    for (var i = 0; i < lines.length; i++) {
      var line = lines[i].trim();
      if (!line) continue;

      // Skip frontmatter (between first two ---)
      if (line === "---") {
        inFrontmatter = !inFrontmatter;
        continue;
      }
      if (inFrontmatter) continue;

      // # heading = top-level menu item
      if (/^#\s+/.test(line)) {
        var topTitle = line.replace(/^#\s+/, "").replace(/[\u{1F5FA}\u{FE0F}\u{1F4CD}]/gu, "").trim();
        if (topTitle) {
          currentGroup = { title: topTitle, items: [] };
          items.push(currentGroup);
        }
        continue;
      }

      // ## heading = sub menu item (skip labels, not groups)
      if (/^##\s+/.test(line)) {
        var subTitle = line.replace(/^##\s+/, "").trim();
        if (subTitle && subTitle !== "all files" && subTitle !== "all links") {
          // If this ## has no links under it, treat as a simple link label
          // Check next non-empty line
          var nextLine = "";
          for (var j = i + 1; j < lines.length; j++) {
            var nl = lines[j].trim();
            if (nl) { nextLine = nl; break; }
          }
          if (nextLine && /^\[/.test(nextLine)) {
            // Next line is a link — this ## is a group
            currentGroup = { title: subTitle, items: [] };
            items.push(currentGroup);
          } else {
            // No link follows — add as a standalone item to current group
            if (!currentGroup) {
              currentGroup = { title: "Menu", items: [] };
              items.push(currentGroup);
            }
            currentGroup.items.push({ title: subTitle, url: "#" });
          }
        }
        continue;
      }

      // [text](url) = link item
      var linkMatch = line.match(/^\[([^\]]+)\]\(([^)]+)\)/);
      if (linkMatch) {
        var linkTitle = linkMatch[1].trim();
        var linkUrl = linkMatch[2].trim();
        if (linkUrl.endsWith(".md")) linkUrl = linkUrl.replace(/\.md$/, "");
        currentGroup.items.push({ title: linkTitle, url: linkUrl });
      }
    }

    return items;
  }

  function buildNav(items) {
    // Remove all static nav items except GitHub link
    var existing = navList.querySelectorAll("li");
    for (var i = existing.length - 1; i >= 0; i--) {
      if (!existing[i].querySelector('a[href*="github.com"]')) {
        existing[i].remove();
      }
    }

    var githubLink = navList.querySelector('a[href*="github.com"]');
    var insertBefore = githubLink ? githubLink.parentElement : null;

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
        chevron.textContent = " \u25BE";
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

      if (insertBefore) {
        navList.insertBefore(li, insertBefore);
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
