// antoniailicb.com — comportamiento compartido

// Orden de los casos (home, índice y "next").
const PROJECTS = [
  { slug: "franca-projects", cat: "Art direction",  title: "Franca Projects",  img: "img/franca/massimo-sanvalentin-1.jpg", pos: "50% 43%" },
  { slug: "lebor-gabala",    cat: "Art direction",  title: "Lebor Gabala",     img: "img/lebor/cover-noviembre.jpg",        pos: "0% 4.5%" },
  { slug: "franciscandrea",  cat: "Brand identity", title: "francisc'andrea",  img: "img/franciscandrea/cover.jpg",          pos: "50% 40%" },
  { slug: "nebular",         cat: "Editorial",      title: "Nebular",          img: "img/nebular/nebular-composicion.jpg",             pos: "50% 50%" },
  { slug: "wild-lama",       cat: "Art direction",  title: "Wild Lama",        img: "img/wildlama/wl-25-q1-525.jpg",         pos: "50% 14.7%" },
  { slug: "sanguaza",        cat: "Editorial",      title: "Una pizca de sangre y un vaso de <i>sanguaza</i>", img: "img/sanguaza/libro-centrado.jpg", pos: "50% 45%" },
  { slug: "potra",           cat: "Web design",     title: "POTRA",            img: "img/potra/home-crop.jpg",                    pos: "50% 50%" },
];

// Ayuda de retícula: ?grid en la URL
if (new URLSearchParams(location.search).has("grid")) {
  const o = document.createElement("div");
  o.className = "grid-overlay";
  o.innerHTML = "<div></div>".repeat(12);
  document.body.appendChild(o);
}

// Menú mobile
const toggle = document.querySelector(".menu-toggle");
if (toggle) {
  toggle.addEventListener("click", () => {
    const open = document.body.classList.toggle("menu-open");
    toggle.setAttribute("aria-expanded", open);
  });
}

// --- Home: índice editorial -----------------------
const home = document.querySelector(".home-stage");
if (home) {
  const banners = home.querySelector(".banners");
  const index = document.querySelector(".index");
  PROJECTS.forEach((p, i) => {
    const img = document.createElement("img");
    img.src = p.img; img.alt = ""; img.style.objectPosition = p.pos;
    img.loading = i < 2 ? "eager" : "lazy";
    banners.appendChild(img);
    const a = document.createElement("a");
    a.href = `projects/${p.slug}.html`;
    a.innerHTML = `<span class="cat">[${p.cat}]</span><span class="ttl">${p.title}</span>`;
    a.addEventListener("mouseenter", () => { if (!mobile.matches) show(i); });
    a.addEventListener("click", e => { if (mobile.matches && current !== i) { e.preventDefault(); show(i); } });
    a.addEventListener("focus", () => { if (!mobile.matches) show(i); });
    index.appendChild(a);
  });
  const dot = document.createElement("span");
  dot.className = "dot"; index.appendChild(dot);
  const mobile = matchMedia("(max-width: 768px)");
  let current = 0;
  function placeDot() {
    const a = index.querySelectorAll("a")[current];
    const t = a.querySelector(".ttl");
    dot.style.transform = `translateY(${a.offsetTop + t.offsetHeight / 2 - 3.5}px)`;
  }
  addEventListener("resize", placeDot);
  function show(i) {
    current = (i + PROJECTS.length) % PROJECTS.length;
    banners.querySelectorAll("img").forEach((im, k) => im.classList.toggle("on", k === current));
    index.querySelectorAll("a").forEach((a, k) => a.classList.toggle("on", k === current));
    placeDot();
    const im = banners.querySelectorAll("img")[current];
    if (window.__navContrast) { im.complete ? window.__navContrast(0) : im.addEventListener("load", () => window.__navContrast(0), { once: true }); }
  }
  show(0);

  document.addEventListener("keydown", e => {
    if (e.key === "ArrowRight") show(current + 1);
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "Enter" && document.activeElement === document.body) location.href = `projects/${PROJECTS[current].slug}.html`;
  });
  // Swipe en mobile
  // Mobile: deslizar (vertical u horizontal) pasa al siguiente preview y el círculo baja con él
  let x0 = null, y0 = null;
  home.addEventListener("touchstart", e => { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  home.addEventListener("touchend", e => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
    const d = Math.abs(dy) > Math.abs(dx) ? dy : dx;
    if (Math.abs(d) > 40) show(current + (d < 0 ? 1 : -1));
    x0 = y0 = null;
  });
  let wheelLock = false;
  home.addEventListener("wheel", e => {
    if (!mobile.matches || wheelLock || Math.abs(e.deltaY) < 20) return;
    wheelLock = true; setTimeout(() => wheelLock = false, 700);
    show(current + (e.deltaY > 0 ? 1 : -1));
  }, { passive: true });
}


// --- Contraste según el fondo: lee el color real bajo un punto ------------------
const px = document.createElement("canvas"); px.width = px.height = 1;
const pctx = px.getContext("2d", { willReadFrequently: true });
const lum = (r, g, b) => (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
const parseRGB = c => { const m = c.match(/[\d.]+/g); return m ? m.map(Number) : null; };
function sampleMedia(el, x, y) {
  const nw = el.naturalWidth || el.videoWidth, nh = el.naturalHeight || el.videoHeight;
  if (!nw || !nh) return null;
  const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
  let sx, sy;
  if (cs.objectFit === "cover" || cs.objectFit === "contain") {
    const k = (cs.objectFit === "cover" ? Math.max : Math.min)(r.width / nw, r.height / nh);
    const [px0, py0] = cs.objectPosition.split(" ").map(v => parseFloat(v) / 100);
    const ox = (r.width - nw * k) * (isNaN(px0) ? .5 : px0), oy = (r.height - nh * k) * (isNaN(py0) ? .5 : py0);
    sx = (x - r.left - ox) / k; sy = (y - r.top - oy) / k;
  } else { sx = (x - r.left) * nw / r.width; sy = (y - r.top) * nh / r.height; }
  if (sx < 0 || sy < 0 || sx >= nw || sy >= nh) return null;
  try { pctx.drawImage(el, sx, sy, 1, 1, 0, 0, 1, 1); const d = pctx.getImageData(0, 0, 1, 1).data; return d[3] > 20 ? lum(d[0], d[1], d[2]) : null; }
  catch (_) { return null; }
}
function brightnessAt(x, y) {
  for (const el of document.elementsFromPoint(x, y)) {
    if (el.closest(".nav-arrow, .case-nav, .banners img:not(.on)")) continue;
    if (!el.classList.contains("on") && parseFloat(getComputedStyle(el).opacity) < .05) continue;
    if (el.matches("img, video")) { const l = sampleMedia(el, x, y); if (l !== null) return l; continue; }
    const c = parseRGB(getComputedStyle(el).backgroundColor);
    if (c && (c[3] === undefined || c[3] > .5)) return lum(c[0], c[1], c[2]);
  }
  return 1;
}

// Menú sobre imágenes: cada apartado en blanco o negro según lo que tiene debajo
const navItems = [...document.querySelectorAll(".case-nav .portfolio, .case-nav .name, .case-nav .about, .case-nav .contact, .home .foot p")];
function navContrast() {
  navItems.forEach(el => {
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height || getComputedStyle(el).display === "none") return;
    let sum = 0, n = 0;
    for (let i = 0; i < 5; i++) for (let j = 0; j < 3; j++) {
      const x = r.left + r.width * (i + .5) / 5, y = r.top + r.height * (j + .5) / 3;
      if (x < 0 || y < 0 || x >= innerWidth || y >= innerHeight) continue;
      sum += brightnessAt(x, y); n++;
    }
    if (!n) return;
    const c = sum / n < .55 ? "#fff" : "#000";
    if (el.classList.contains("hand")) el.style.backgroundColor = c; else el.style.color = c;
  });
}
if (navItems.length) {
  let t = null;
  const later = (ms = 60) => { clearTimeout(t); t = setTimeout(navContrast, ms); };
  addEventListener("load", () => later(0));
  addEventListener("resize", () => later(150));
  addEventListener("scroll", () => later(120), { passive: true });
  document.querySelectorAll("img, video").forEach(m => m.addEventListener(m.tagName === "IMG" ? "load" : "loadeddata", () => later(), { once: true }));
  later(0);
  window.__navContrast = later;
}

// Carruseles en mobile: indicador de puntos tipo Instagram
document.querySelectorAll("[data-carousel]").forEach(c => {
  const n = c.children.length;
  const d = document.createElement("div");
  d.className = "dots " + (c.dataset.dotsClass || "");
  d.innerHTML = "<span></span>".repeat(n);
  c.after(d);
  const upd = () => {
    const step = c.children[0].getBoundingClientRect().width + 2;
    let i = Math.round(c.scrollLeft / step);
    if (c.scrollLeft + c.clientWidth >= c.scrollWidth - 2) i = n - 1;
    [...d.children].forEach((s, k) => s.classList.toggle("on", k === i));
  };
  c.addEventListener("scroll", upd, { passive: true });
  upd();
});

// Landings: clic en el tercio izquierdo = proyecto anterior, tercio derecho = siguiente
const slug = document.body.dataset.project;
const idx = PROJECTS.findIndex(p => p.slug === slug);
if (idx > -1 && matchMedia("(hover: hover) and (pointer: fine)").matches) {
  const go = d => { location.href = `${PROJECTS[(idx + d + PROJECTS.length) % PROJECTS.length].slug}.html`; };
  const skip = el => el.closest("a, button, input, textarea, select, nav, [data-carousel], .site-nav");
  const side = e => e.clientX < innerWidth / 3 ? -1 : e.clientX > innerWidth * 2 / 3 ? 1 : 0;
  // Flecha propia: blanca sobre fondo oscuro, negra sobre fondo claro
  const arrow = document.createElement("div");
  arrow.className = "nav-arrow";
  arrow.innerHTML = '<svg width="14" height="20" viewBox="0 0 14 20"><path d="m4 3 7 7-7 7" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>';
  document.body.appendChild(arrow);
  let pend = null;
  document.addEventListener("mousemove", e => {
    const s = skip(e.target) ? 0 : side(e);
    document.body.classList.toggle("go-prev", s === -1);
    document.body.classList.toggle("go-next", s === 1);
    arrow.classList.toggle("on", s !== 0);
    arrow.classList.toggle("prev", s === -1);
    arrow.style.transform = `translate(${e.clientX - 7}px, ${e.clientY - 10}px)`;
    if (s && !pend) pend = requestAnimationFrame(() => {
      pend = null;
      arrow.style.color = brightnessAt(e.clientX, e.clientY) < .5 ? "#fff" : "#000";
    });
  }, { passive: true });
  document.addEventListener("mouseleave", () => arrow.classList.remove("on"));
  document.addEventListener("click", e => {
    if (skip(e.target) || getSelection().toString()) return;
    const s = side(e); if (s) go(s);
  });
  document.addEventListener("keydown", e => {
    if (e.target.closest("input, textarea")) return;
    if (e.key === "ArrowRight") go(1);
    if (e.key === "ArrowLeft") go(-1);
  });
}

// Viudas: une las dos últimas palabras de cada párrafo (respaldo para navegadores sin text-wrap: pretty)
document.querySelectorAll("p, h1, h3, li, dd, .display, .ttl").forEach(el => {
  if (el.closest(".artists, .spec .caps, .case-nav")) return;
  if (parseFloat(getComputedStyle(el).fontSize) > 40) return; // tipos grandes: solo text-wrap, para no forzar cortes de palabra
  const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
  let last = null; while (w.nextNode()) if (w.currentNode.nodeValue.trim()) last = w.currentNode;
  if (!last || el.textContent.trim().split(/\s+/).length < 4) return;
  last.nodeValue = last.nodeValue.replace(/[ \t]+(\S+\s*)$/, " $1");
});

/* Banner "siguiente": antes de cambiar de página sube el banner hasta arriba,
   donde coincide con la portada de la landing siguiente (misma imagen y recorte). */
(function () {
  const foot = document.querySelector(".case-next");
  if (!foot) return;
  const banner = foot.querySelector(".next-img");
  foot.querySelectorAll("a").forEach(a => a.addEventListener("click", e => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    e.preventDefault();
    const href = a.href;
    const top = banner.getBoundingClientRect().top + window.scrollY;
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    let gone = false;
    const go = () => { if (!gone) { gone = true; location.href = href; } };
    if (reduce) return go();
    foot.classList.add("opening"); banner.classList.add("open");
    window.scrollTo({ top, behavior: "smooth" });
    // cambia de página cuando la ventana ya creció y llegó arriba
    const full = () => banner.getBoundingClientRect().height >= Math.max(520, Math.min(innerHeight, innerWidth * 900 / 1440)) - 2;
    const tick = () => (full() && Math.abs(window.scrollY - top) < 2) ? go() : requestAnimationFrame(tick);
    requestAnimationFrame(tick);
    setTimeout(() => { window.scrollTo(0, top); go(); }, 1500);
  }));
  addEventListener("pageshow", e => { if (e.persisted) location.reload(); });
})();
