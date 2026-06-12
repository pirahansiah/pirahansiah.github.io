/**
 * Farshid Liquid-Glass Cursor Logic — macOS 27 / iOS 27
 */
(function () {
  "use strict";

  const cur = document.createElement('div');
  cur.id = 'farshid-cursor';
  cur.setAttribute('aria-hidden', 'true');
  cur.innerHTML = `
    <div class="cursor-glass"></div>
    <div class="cursor-shine"></div>
    <div class="cursor-ring"></div>
    <div class="cursor-dot"></div>
  `;
  document.body.appendChild(cur);

  /* LERP: snappy 0.25 */
  const LERP = 0.25; 
  let tx = -100, ty = -100;
  let cx = -100, cy = -100;

  function lerp(a, b, t) { return a + (b - a) * t; }

  function tick() {
    cx = lerp(cx, tx, LERP);
    cy = lerp(cy, ty, LERP);
    cur.style.transform = `translate(calc(${cx}px - 50%), calc(${cy}px - 50%))`;
    requestAnimationFrame(tick);
  }

  document.addEventListener("mousemove", (e) => {
    tx = e.clientX;
    ty = e.clientY;
  }, { passive: true });

  document.addEventListener("mouseleave", () => { cur.style.opacity = "0"; });
  document.addEventListener("mouseenter", () => { cur.style.opacity = "1"; });

  document.addEventListener("mousedown", () => cur.classList.add("is-clicking"));
  document.addEventListener("mouseup", () => cur.classList.remove("is-clicking"));

  const HOVER_SEL = [
    "a", "button", "summary", "label", "[role='button']",
    ".liquid-glass-item", ".glass-pill", ".nav-brand", ".nav-list a",
    ".nav-toggle", ".nav-menu-btn", ".toolbar button", ".toolbar a"
  ].join(",");

  const TEXT_SEL = [
    "p", "li", "span", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote",
    "input[type='text']", "textarea", "[contenteditable]", "code", "pre"
  ].join(",");

  document.addEventListener("mouseover", (e) => {
    const t = e.target;
    if (!t) return;

    if (t.closest(HOVER_SEL)) {
      cur.classList.add("is-hovered");
      cur.classList.remove("is-text");
    } else if (t.closest(TEXT_SEL)) {
      cur.classList.add("is-text");
      cur.classList.remove("is-hovered");
    } else {
      cur.classList.remove("is-hovered", "is-text");
    }
  }, { passive: true });

  tick();
})();
