import os, html as H
import os
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")

def im(path):
    """Devuelve la ruta real (jpg o png) de una imagen dada sin extensión."""
    for ext in (".jpg", ".png", ".gif"):
        if os.path.exists(f"{ROOT}/img/{path}{ext}"):
            return f"img/{path}{ext}"
    raise FileNotFoundError(path)

def nav(rel="../", dark=False, current=None):
    d = " dark" if dark else ""
    a_cur = ' aria-current="page"' if current == "about" else ""
    c_cur = ' aria-current="page"' if current == "contact" else ""
    return f'''  <nav class="case-nav g{d}" aria-label="Main">
    <a class="hand portfolio" href="{rel}index.html" aria-label="Portfolio"></a>
    <a class="name" href="{rel}index.html">Antonia Ilic Bromberg</a>
    <span class="links"><a class="hand about" href="{rel}about.html" aria-label="About"{a_cur}></a><a class="hand contact" href="{rel}contact.html" aria-label="Contact"{c_cur}></a></span>
  </nav>
'''

def page(title, desc, slug, body, bg="#f6f6f6", band=None, color=None, css=""):
    root = f":root {{ --bg-case: {bg}; --band: {band or bg}; }}"
    col = f"\n    body.case {{ color: {color}; }}" if color else ""
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Antonia Ilic Bromberg</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="../css/base.css">
  <link rel="stylesheet" href="../css/case.css">
  <style>
    {root}{col}
{css}
  </style>
</head>
<body class="case" data-project="{slug}">
{nav()}
{body}
  <script src="../js/main.js"></script>
</body>
</html>
'''

def hero(img, alt, cat, name, pos="50% 50%"):
    return f'''  <header class="case-hero" style="--pos: {pos}">
    <img src="../{im(img)}" alt="{alt}">
    <div class="case-band g"><h1 class="label tag"><span class="cat">[{cat}]</span><span>{name}</span></h1></div>
  </header>
'''

def ficha(pairs):
    rows = "\n".join(f'    <div><p>{k}</p><p>{v}</p></div>' for k, v in pairs)
    return f'''  <section class="ficha g">
{rows}
  </section>
'''

def head(label, display=None, text=None, low=None, extra=""):
    parts = [f'      <h2 class="label">{label}</h2>']
    if low: parts.append(f'      <p class="label-low">{low}</p>')
    if display: parts.append(f'      <p class="display">{display}</p>')
    if text: parts.append(f'      <div class="t">{"".join(f"<p>{p}</p>" for p in text)}</div>')
    if extra: parts.append(extra)
    return '    <div class="head g">\n' + "\n".join(parts) + '\n    </div>'

def pair(a, b):
    def col(x):
        lab, paras = x
        return f'      <div class="t"><p>{lab}</p>{"".join(f"<p>{p}</p>" for p in paras)}</div>'
    return f'    <div class="pair g">\n{col(a)}\n{col(b)}\n    </div>'

def trio(cols):
    return '    <div class="trio g">\n' + "\n".join(f'      <div class="t">{c}</div>' for c in cols) + '\n    </div>'

def img(path, c, m=None, r=None, alt="", pos=None, extra_style="", cls=""):
    st = f"--c: {c};"
    if m: st += f" --m: {m};"
    if r: st += f" --r: {r};"
    if pos: st += f" object-position: {pos};"
    st += extra_style
    c_ = f' class="{cls}"' if cls else ""
    return f'      <img{c_} src="../{im(path)}" alt="{H.escape(alt)}" loading="lazy" style="{st}">'

def media(items, cls="", style=""):
    st = f' style="{style}"' if style else ""
    # Una sola imagen o video que no ocupa todo el ancho: módulo "solo", con blanco alrededor al centrarlo en pantalla
    if len(items) == 1 and "bleed" not in cls and "--c: 1 / -1" not in items[0] and "--c:1 / -1" not in items[0]:
        cls = (cls + " solo").strip()
    return f'    <div class="media g {cls}"{st}>\n' + "\n".join(items) + '\n    </div>'

def chapter(*blocks, top=False, cls="", style=""):
    t = " top" if top else ""
    st = f' style="{style}"' if style else ""
    return f'  <section class="chapter{t} {cls}"{st}>\n' + "\n".join(blocks) + '\n  </section>\n'

def credits(result_label, result, pairs, wide=False, title="Credits"):
    rows = "\n".join(f'        <dt>{k}</dt><dd>{v}</dd>' for k, v in pairs)
    w = " wide" if wide else ""
    res = ""
    if result is not None:
        lab = f"<p>{result_label}</p>" if result_label else ""
        res = f'      <div class="t" style="display:flex; flex-direction:column; gap:var(--s-text)">{lab}<p>{result}</p></div>\n'
    return f'    <div class="credits g{w}">\n{res}      <dl>\n{rows}\n      </dl>\n    </div>'

def nxt(slug, img_, cat, name, pos="50% 50%"):
    return f'''  <footer class="case-next">
    <a class="next-img" href="{slug}.html" style="--pos: {pos}"><img src="../{im(img_)}" alt="" loading="lazy"></a>
    <a class="next-title g" href="{slug}.html"><span class="label tag"><span class="cat">[{cat}]</span><span>{name} →</span></span></a>
  </footer>
'''

def _split_paras(html_):
    # Un salto doble dentro de un <p> se convierte en párrafos separados (espacio = --s-text)
    import re
    def rep(m):
        attrs, body = m.group(1), m.group(2)
        parts = [x.strip("\n") for x in re.split(r"\n\s*\n", body) if x.strip()]
        return '<div class="t">' + "".join(f"<p{attrs}>{x}</p>" for x in parts) + "</div>"
    return re.sub(r"<p([^>]*)>([^<]*\n\s*\n[^<]*)</p>", rep, html_)

def write(slug, html_):
    open(f"{ROOT}/projects/{slug}.html", "w").write(_split_paras(html_))
