// antoniailicb.com — comportamiento compartido

// Orden de los casos (home, índice y "next").
const PROJECTS = [
  { slug: "franca-projects", cat: "Art direction",  title: "Franca Projects",  img: "img/franca/massimo-sanvalentin-1.jpg", pos: "50% 43%" },
  { slug: "lebor-gabala",    cat: "Art direction",  title: "Lebor Gabala",     img: "img/lebor/cover-noviembre.jpg",        pos: "0% 4.5%" },
  { slug: "franciscandrea",  cat: "Brand identity", title: "francisc'andrea",  img: "img/franciscandrea/cover.jpg",          pos: "50% 40%" },
  { slug: "nebular",         cat: "Editorial",      title: "Nebular",          img: "img/nebular/nebular-2.jpg",             pos: "50% 50%" },
  { slug: "wild-lama",       cat: "Art direction",  title: "Wild Lama",        img: "img/wildlama/wl-25-q1-525.jpg",         pos: "50% 14.7%" },
  { slug: "sanguaza",        cat: "Editorial",      title: "Una pizca de sangre y un vaso de sanguaza", img: "img/sanguaza/libro-post-2.jpg", pos: "95% 50%" },
  { slug: "potra",           cat: "Web design",     title: "POTRA",            img: "img/potra/home.jpg",                    pos: "50% 50%" },
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
    a.addEventListener("mouseenter", () => show(i));
    a.addEventListener("focus", () => show(i));
    index.appendChild(a);
  });
  let current = 0;
  function show(i) {
    current = (i + PROJECTS.length) % PROJECTS.length;
    banners.querySelectorAll("img").forEach((im, k) => im.classList.toggle("on", k === current));
    index.querySelectorAll("a").forEach((a, k) => a.classList.toggle("on", k === current));
  }
  show(0);

  document.addEventListener("keydown", e => {
    if (e.key === "ArrowRight") show(current + 1);
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "Enter" && document.activeElement === document.body) location.href = `projects/${PROJECTS[current].slug}.html`;
  });
  // Swipe en mobile
  let x0 = null;
  home.addEventListener("touchstart", e => { x0 = e.touches[0].clientX; }, { passive: true });
  home.addEventListener("touchend", e => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(current + (dx < 0 ? 1 : -1));
    x0 = null;
  });
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
  const skip = el => el.closest("a, button, input, textarea, select, video, nav, [data-carousel], .site-nav");
  const side = e => e.clientX < innerWidth / 3 ? -1 : e.clientX > innerWidth * 2 / 3 ? 1 : 0;
  document.addEventListener("mousemove", e => {
    const s = skip(e.target) ? 0 : side(e);
    document.body.classList.toggle("go-prev", s === -1);
    document.body.classList.toggle("go-next", s === 1);
  }, { passive: true });
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
